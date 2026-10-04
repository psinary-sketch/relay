# -*- coding: utf-8 -*-
"""b609_checks.py -- THE SUITE OF b609, UNDER (R219): THE SIEVE AT v0.4 (THREE ROWS ADDED, THE EPSTEIN ROWS READ) AND THE MONOGRAPH AT
v5.17 (THE CONVERGENCE TABLE'S CELLS, §25.8'S QUALIFIED NAME); THE SECOND READER'S SEED.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>` or `--prerun`; it writes data/b609_checks.txt before the push and
### data/b609_checks_postpush.txt after it. ### `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the
### face is sealed, no table regenerated, its counts written to data/b609_arms_prerun.txt and nothing else.
### ### The harness is b568's to b608's, carried from tools/b608_checks.py (its imports, helpers, regenerate and main); the
### sources, predicates and arms are b609's. The control arm is the frozen one of (R207)(2).
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
FACE = os.path.join(D, 'b609_registration_2026-10-03.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
SV3, SV2, SV1, SV4 = ('phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_3.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_2.md',
                      'phase2/method/THE_FINDINGS_AS_THEY_STAND.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4.md')
M16, M15, M14, M13, M17 = ('day1/A_Place_to_Stand_v5_16.md', 'day1/A_Place_to_Stand_v5_15.md', 'day1/A_Place_to_Stand_v5_14.md',
                           'day1/A_Place_to_Stand.md', 'day1/A_Place_to_Stand_v5_17.md')
CURRENTS = (SV3, SV2, SV1, M16, M15, M14, M13)
HK_LIST = 'housekeeping_terminal_table.txt'
PRE = dict(relay='af1df8d6', pp='3d2f67d', gs='3528bcf', ker='1d5d4dd')
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf69', 'SIDE-rcurve': 'd5f33b44', 'SIDE-explicit-formula': '1d5d4dd9'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b', 'product-b600': '1dd5cd7',
        'doubling-keiper-b601': '5fc0c87', 'sign-window-b602': '914c413', 'family-b603': '1d5d4dd'}
STEPZERO = '11970104'
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/eec9660e-279c-42f1-bdfb-f149381f3e02/scratchpad'


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b609')
            and 'data/b609_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    import b609_record as REC
    import b609_worklist as K
    import b604_record as R4
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b609_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b609_') and f.endswith('.py'))
    svp, mdp = os.path.join(PP, *SV4.split('/')), os.path.join(PP, *M17.split('/'))
    S = dict(
        REC=REC, K=K, R4=R4, face=face, ferry=rd('b609_ferry.txt'), scan=rd('b609_ferry_scan.txt'), cens=rd('b609_census_stepzero.txt'),
        fcens=rd('b609_faces_census_stepzero.txt'), pins0=rd('b609_pins_stepzero.txt'), procs=rd('b609_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b608_closing.txt'), reads=rd('b609_reads.txt'), branches=rd('b609_branches.txt'), answers=rd('b609_author_answers.txt'),
        prerun=rd('b609_arms_prerun.txt'), defects=rd('b609_defects.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))))
              for f in ('b608_checks.py', 'b608_record.py', 'b608_worklist.py', 'b605_record.py', 'b604_record.py', 'b602_record.py',
                        'b560_record.py', 'b566_record.py', 'test_chain_page_b596.py', 'chain_page.py', 'e0_rule.py', 'g_chain_page.py',
                        'push_gated.sh', 'banned_terms.py', 'b558_record.py', 'errata_append.py')},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        readme=(cr0(raw(os.path.join(PP, 'README.md'))), cr0(blob(PP, PRE['pp'] + ':README.md'))),
        registry=(cr0(raw(os.path.join(PP, 'REGISTRY.md'))), cr0(blob(PP, PRE['pp'] + ':REGISTRY.md'))),
        faces=(cr0(raw(os.path.join(PP, 'FACES_LEDGER.md'))), cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md'))),
        errata=(cr0(raw(os.path.join(PP, 'ERRATA.md'))), cr0(blob(PP, PRE['pp'] + ':ERRATA.md')), cr0(blob(PP, 'HEAD:ERRATA.md'))),
        spiral=(cr0(raw(os.path.join(PP, 'SPIRAL_MAP.md'))), cr0(blob(PP, PRE['pp'] + ':SPIRAL_MAP.md'))),
        currents={p: (cr0(raw(os.path.join(PP, *p.split('/')))), cr0(blob(PP, PRE['pp'] + ':' + p)), cr0(blob(PP, 'HEAD:' + p))) for p in CURRENTS},
        sv_disk=cr0(raw(svp)), sv_head=cr0(blob(PP, 'HEAD:' + SV4)), md_disk=cr0(raw(mdp)), md_head=cr0(blob(PP, 'HEAD:' + M17)),
        pages={p: (cr0(raw(os.path.join(PP, p))), cr0(blob(PP, PRE['pp'] + ':' + p)), cr0(blob(PP, 'HEAD:' + p))) for p in (PAGE, DIR_PAGE)},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        corr_pre=cr0(blob(GS, PRE['gs'] + ':CORRESPONDENCE.md')), corr_now=cr0(raw(os.path.join(GS, 'CORRESPONDENCE.md'))),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        lv_head=gs('D:/SIDE-lv-conservation', 'rev-parse', 'HEAD'), lv_dirty=gs('D:/SIDE-lv-conservation', 'status', '--porcelain', '--untracked-files=no'),
        trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain', '--untracked-files=no'),
        ktags=sorted(x for x in gs(KER, 'tag', '-l', 'v0.*').split(NL) if x.strip()),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b608*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b609_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b609_mustnotexist.txt')), table_changed=None,
        fj=jl('b609_findings.json'), tj=jl('b609_trail.json'), sc=jl('b609_scores.json'), desk=rd('b609_desk_notes.txt'),
        rl=jl('b609_record_lines.json'), RJ=jl('b609_rows.json'), rtxt=rd('b609_rows_v04.txt'), RS=jl('b609_residue.json'),
        seed=rd('b609_residue_seed.txt'), hk=rd(HK_LIST), hk_path=os.path.join(D, HK_LIST),
        ES=jl('b609_sieve_edition.json'), HS=jl('b609_h28_sieve.json'), sbank=rd('b609_edition_FINDINGS_STAND.txt'), srepin=rd('b609_repin_sieve.txt'),
        sscan=rd('b609_sieve_termscan.txt'),
        EM=jl('b609_mono_edition.json'), HM=jl('b609_h28_mono.json'), mbank=rd('b609_edition_PLACE.txt'), mrepin=rd('b609_repin_mono.txt'),
        mscan=rd('b609_mono_termscan.txt'),
        PZ=jl('b609_page_zeta.json'), PX=jl('b609_page_chi.json'), arms_c2=rd('b609_page_arms_c2.txt'),
    )
    S['sv'] = lines_of(S['sv_disk']) if S['sv_disk'] else []
    S['md'] = lines_of(S['md_disk']) if S['md_disk'] else []
    S['s3'] = lines_of(S['currents'][SV3][1])
    S['m16'] = lines_of(S['currents'][M16][1])
    S['sscan_now'] = _scan(svp) if S['sv_disk'] else ''
    S['mscan_now'] = _scan(mdp) if S['md_disk'] else ''
    S['written'] = written_files(lock_epoch or 0)
    S['globs'] = wl_globs(face)
    S['instr_now'] = K.resolve_instruments()
    S['pieces_now'] = {p: [l for l in (blob(PP, 'HEAD:' + p) or b'').decode('utf-8', 'replace').split(NL) if re.search(REC.PIECES_RE, l)] for p in (PAGE, DIR_PAGE)}
    S['residue_now'] = K.residue_hits(S['m16'], K.M_CORR - 1) if S['m16'] else []
    S['classify17'] = REC._classify17(S['md'], S['EM'])[0] if S['md'] and S['EM'] else []
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
    S['hk_tracked'] = gs(ROOT, 'ls-files', 'data/' + HK_LIST)
    S['hk_mtime'] = os.path.getmtime(S['hk_path']) if os.path.exists(S['hk_path']) else None
    S.update(extra_sources(S))
    return S


def extra_sources(S):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    X = {}
    X['gcp_zeta'] = GCP.arm(os.path.join(D, 'b602_nodes_zeta.txt'), os.path.join(SP, '_b609_gcp'), os.path.join(D, 'b602_probe_out.txt'))
    X['gcp_chi'] = GCP.arm(os.path.join(D, 'b603_nodes_chi.txt'), os.path.join(SP, '_b609_gcp'), os.path.join(D, 'b603_chi_probe_out.txt'))
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
    return ls[i] if len(ls) == 4 else {}


def weight_ok(S):
    x = _rl(S, 0)
    a = fline(S, x.get('line'))
    return bool(x) and x.get('file') == 'FINDINGS.md' and a.startswith(x['head']) and '(:7158)' in a and 'b608 AT ITS WEIGHT, CP-8 CLOSED' in a \
        and 're-pin 919 of 919' in a and '108 corrected and 46 carried' in a and '15 corrected and 3 carried' in a and 'CP-8 CLOSED.' in a \
        and '80 of 80' in a and x['line'] > 7158


def items_ok(S):
    x = _rl(S, 1)
    a = fline(S, x.get('line'))
    return bool(x) and x.get('file') == 'FINDINGS.md' and a.startswith(x['head']) and 'THE SEAT’S ITEMS, RULED' in a \
        and 'Reading R-8 stands' in a and HK_LIST in a and 'Chapter 25, Conservation of Spectra Chapter 13' in a \
        and 'b609_residue_seed.txt' in a and x['line'] > _rl(S, 0).get('line', 10 ** 9)


def batch_ok(S):
    x, R = _rl(S, 2), S['RS']
    a = oline(S, x.get('line'))
    return bool(x) and bool(R) and x.get('file') == 'OPEN_TRAILS.md' and a.startswith(x['head']) and '(:12212)' in a \
        and 'THE BATCH NAMED AND THE SEED BANKED' in a and all(y in a for y in ('v5.14 (b606', 'v5.15 (b607', 'v5.16 (b608', 'v0.2 (b604', 'v0.3 (b605')) \
        and ('-- %d candidates' % R['n16']) in a and ('%d marked kin, %d proof labels' % (R['kin'], R['label'])) in a and x['line'] > 12522


def phase_ok(S):
    x = _rl(S, 3)
    a = oline(S, x.get('line'))
    return bool(x) and x.get('file') == 'OPEN_TRAILS.md' and a.startswith(x['head']) and '(:4049)' in a and 'A PHASE-STATE READING, PRICED' in a \
        and 'Price: one act, reads and one census bank, one edition of the chosen document. Not started.' in a \
        and x['line'] > _rl(S, 2).get('line', 10 ** 9)


def seed_ok(S):
    K, R = S['K'], S['RS']
    hits = S['residue_now']
    marks = [K.MARKS16.get((n, w)) for _m, n, w in hits]
    kin = sum(1 for m in marks if m and m[0] == K.KIN)
    return bool(R) and len(hits) == R.get('n16') and None not in marks and kin == R.get('kin') \
        and ('### ### **THE SEED: v5.16`s body %d candidates -- KIN %d ;' % (len(hits), kin)) in S['seed'] and 'unmarked 0.**' in S['seed']


def hk_ok(S):
    return S['hk'].startswith('b609 -- THE HOUSEKEEPING LIST OF THE TERMINAL TABLE') and 'H-TT-1 (2026-10-03, b609' in S['hk'] \
        and '`_root_.structural_exhaustiveness_proved`' in S['hk'] and S['hk_mtime'] is not None and S['lock_epoch'] is not None \
        and S['hk_mtime'] > S['lock_epoch']


def rows_bank_ok(S):
    RJ, ES = S['RJ'], S['ES']
    return bool(RJ) and bool(ES) and RJ.get('at', 'z') < ES.get('at', '') and S['rtxt'].startswith('b609 -- COMPONENT 2') \
        and all(h in S['rtxt'] for h in ('### PART A', '### PART B', '### PART C')) and all(x['ok'] for x in RJ.get('instruments') or [{}]) \
        and len(RJ.get('instruments') or []) == _n_sources(S)


def instr_now_ok(S):
    return len(S['instr_now']) == _n_sources(S) == 23 and all(x['ok'] for x in S['instr_now'])


def _n_sources(S):
    return sum(len(v) for v in S['K'].INSTRUMENTS.values()) + len(S['K'].FD_READ['lines'])


def _hs(S, hkey, skey, src, bank, want):
    return S[src].get(hkey) == want and (S['sc'].get(skey) or [''])[0] == want and ('(%s)' % skey.upper()) in S['desk'] \
        and ('### ### **%s %s' % (hkey, want)) in S[bank]


def unedited_all(S):
    return all(bool(b) and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == 7


def sieve_carries(S):
    REC, ES, sv = S['REC'], S['ES'], S['sv']
    if not sv or not ES:
        return False
    ok, bad = REC.sieve_carried(ES, sv, S['s3'])
    return not bad and ok == sum(1 for l in S['s3'] if l.strip()) and hashlib.sha256(S['sv_disk']).hexdigest() == ES.get('sha256')


def sieve_version(S):
    sv, s3 = S['sv'], S['s3']
    return bool(sv) and sv[:2] == s3[:2] and sv[2] == S['K'].VERSION4 and sv[3] == '' and sv[4] == s3[2] and s3[2].startswith('*v0.3, 2026-10-03')


def sieve_rows(S):
    K, sv, P = S['K'], S['sv'], (S['ES'].get('pos') or {}).get('rows') or {}
    if not sv or not P:
        return False
    return all(sv[P[r['id']] - 1] == K.row_line(r) for r in K.NEW_ROWS) and sv[P['RH-58'] - 2].startswith('| RH-57 | ') \
        and [P['RH-58'], P['RH-59'], P['RH-60']] == [P['RH-57'] + 1, P['RH-57'] + 2, P['RH-57'] + 3] and sv[P['RH-60']] == ''


def sieve_counts(S):
    sv, R4 = S['sv'], S['R4']
    if not sv or R4.BM_TAG not in sv:
        return False
    body = sv[:sv.index(R4.BM_TAG)]
    rows = [l for l in body if re.match(r'^\| (RH|FD|MT|CT|MC)-\d\d \| ', l)]
    v = [l.strip('|').split(' | ')[4].strip() for l in rows]
    cnt = {k: v.count(k) for k in ('FACE', 'BRIGHT', 'DARK', 'NOT A ROUTE')}
    rh = [x for l, x in zip(rows, v) if l.startswith('| RH-')]
    rc = {k: rh.count(k) for k in ('FACE', 'BRIGHT', 'DARK', 'NOT A ROUTE')}
    head = '%d rows -- %d BRIGHT, %d DARK, %d NOT A ROUTE, and %d FACE rows' % (len(rows), cnt['BRIGHT'], cnt['DARK'], cnt['NOT A ROUTE'], cnt['FACE'])
    clus = '— %d rows: %d FACE, %d BRIGHT, %d DARK, %d NOT A ROUTE' % (len(rh), rc['FACE'], rc['BRIGHT'], rc['DARK'], rc['NOT A ROUTE'])
    return len(rows) == 87 and any(head in l for l in body) and any(l.startswith('## Simplicity / RH cascade ' + clus) for l in body) \
        and any('5 of them carry the table’s %d rows' % len(rows) in l for l in body)


def sieve_bm_ok(S):
    REC, sv = S['REC'], S['sv']
    if not sv or REC.BM_TAG4 not in sv or REC.B605_TAG not in sv:
        return False
    bm = sv[sv.index(REC.BM_TAG4):]
    heads = ['### The readings', '### Removals', '### The three rows added', '### The mechanism enumeration’s verdict', '### FD-01 and FD-02, read once',
             '### Rewrites', '### Insertions ordered by the ruling', '### Re-pins of v0.3’s back matter', '### Placement', '### Correspondence', '### Version history']
    pos = [next((i for i, l in enumerate(bm) if l.startswith(h)), -1) for h in heads]
    blanks = [l for l in bm if l.startswith('| ') and not l.startswith('|:--') and l.rstrip().endswith('|  |')]
    return all(p >= 0 for p in pos) and pos == sorted(pos) and not blanks and sv.index(REC.BM_TAG4) > sv.index(REC.B605_TAG)


def sieve_bank_ok(S):
    b, ES = S['sbank'], S['ES']
    return b.startswith('### OFFSET FROM v0.3 (R190)(3):') and b.count('### OFFSET FROM') == 1 and ('sha256 %s' % ES.get('sha256', '#')) in b \
        and '### THE THREE ROWS, PRINTED, EACH WITH ONE VERDICT (H43a):' in b and '### THE MECHANISM ROW`S VERDICT AND THE LINES THAT DECIDE IT' in b \
        and ('the BACK MATTER %d' % ES.get('n_backmatter', -1)) in b and '### ### **THE SIEVE LANDS: NO SENTENCE HELD.**' in b


def _repin_ok(t, floor):
    m = re.search(r'RE-PIN : (\d+) of (\d+) citations hold', t)
    return bool(m) and m.group(1) == m.group(2) and int(m.group(2)) > floor


def h28b_sieve(S):
    ES, sv, R4 = S['ES'], S['sv'], S['R4']
    if not sv or not ES:
        return False
    b4, _x = R4._body_and_bm(sv)
    b3, _y = R4._body_and_bm(S['s3'])
    nb, nc = R4._count([l for _i, l in b4]), R4._count([l for _i, l in b3])
    allowed = ES['ruled_insertions'] + ES['version_lines'] + sum(abs(x['d']) for x in ES['rewrite_deltas'])
    return nb == ES.get('n_body') and nc == ES.get('n_v3_body') and ES['removals'] == 0 and ES['version_lines'] == 1 and ES['ruled_insertions'] == 3 \
        and _hs(S, 'H28b', 'H28b-SIEVE', 'HS', 'sbank', 'HOLDS' if abs(nb - nc) <= allowed else 'REFUTED')


def h28c_sieve(S):
    sv, R4 = S['sv'], S['R4']
    if not sv:
        return False
    body, _bm = R4._body_and_bm(sv)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN\s*$', S['sscan_now'], re.M) is not None
    beyond = [i for i, l in body if R4.CEILING.search(l)]
    return _hs(S, 'H28c', 'H28c-SIEVE', 'HS', 'sbank', 'HOLDS' if clean and not beyond else 'REFUTED') and S['sscan_now'].strip() == S['sscan'].strip()


def h43a_ok(S):
    sv, P = S['sv'], (S['ES'].get('pos') or {}).get('rows') or {}
    if not sv or not P:
        return False
    good = 0
    for r in S['K'].NEW_ROWS:
        c = [x.strip() for x in sv[P[r['id']] - 1].strip('|').split(' | ')]
        src = [x for x in S['instr_now'] if x['row'] == r['id']]
        good += c[4] in ('FACE', 'BRIGHT', 'DARK', 'NOT A ROUTE') and bool(src) and all(x['ok'] for x in src) and ((c[4] == 'NOT A ROUTE') == (c[5] == '—'))
    return _hs(S, 'H43a', 'H43a', 'HS', 'sbank', 'HOLDS' if good == 3 else 'REFUTED')


def h43b_ok(S):
    sv, ES, K = S['sv'], S['ES'], S['K']
    if not sv or not ES:
        return False
    row = sv[ES['pos']['rows']['RH-60'] - 1]
    bm = NL.join(sv[ES['bm4'] - 1:])
    ok = ('| DARK | %s |' % K.T2) in row and all(('- %s: ' % S['R4']._cell(S['REC']._poss(a_))) in bm for a_, _b in K.MECH['deciding']) \
        and 'Schema/Detector.lean :99 (the χ page node 29, its line :33)' in bm and not any(S['pieces_now'].values())
    return _hs(S, 'H43b', 'H43b', 'HS', 'sbank', 'HOLDS' if ok else 'REFUTED')


def _alone(S, path, prefix):
    c = [h for h, f in S['pp_files'].items() if path in f]
    return len(c) == 1 and S['pp_files'][c[0]] == [path] and dict(S['pp_log'])[c[0]].startswith(prefix)


def mono_carries(S):
    REC, EM, md = S['REC'], S['EM'], S['md']
    if not md or not EM:
        return False
    ok, bad = REC.mono_carried(EM, md, S['m16'])
    return not bad and ok == sum(1 for l in S['m16'] if l.strip()) and hashlib.sha256(S['md_disk']).hexdigest() == EM.get('sha256')


def mono_version(S):
    md, m = S['md'], S['m16']
    return bool(md) and md[18] == S['REC'].VERSION17 and md[19] == m[18] and m[18].startswith('**v5.16, 2026-10-03**') and md[:18] == m[:18] \
        and md[20] == m[19]


def mono_cells(S):
    md, m, K = S['md'], S['m16'], S['K']
    if not md:
        return False
    w = lambda n: n + 1 if n >= 19 else n
    changed = [n for n in range(1, K.M_CORR) if md[w(n) - 1] != m[n - 1]]
    cells = S['REC']._cells(S['ES'].get('pos') or {'rows': {}})
    return changed == sorted(c[1] for c in K.CELLS) and all(md[w(c['line']) - 1] == m[c['line'] - 1].replace(c['old'], c['new']) for c in cells)


def mono_bm_ok(S):
    REC, md = S['REC'], S['md']
    tags = [REC.B606_TAG, '<!-- b607 (R217) THE v5.15 EDITION`S BACK MATTER, 2026-10-03 -->', REC.B608_TAG, REC.BM_TAG17]
    if not md or any(t not in md for t in tags):
        return False
    bm = md[md.index(REC.BM_TAG17):]
    heads = ['### The act’s readings', '### The five cells', '### Collisions resolved', '### Removals', '### Fact corrections', '### Stem corrections',
             '### Placement', '### Correspondence', '### Version history']
    pos = [next((i for i, l in enumerate(bm) if l.startswith(h)), -1) for h in heads]
    blanks = [l for l in bm if l.startswith('| ') and not l.startswith('|:--') and l.rstrip().endswith('|  |')]
    return all(p >= 0 for p in pos) and pos == sorted(pos) and not blanks and [md.index(t) for t in tags] == sorted(md.index(t) for t in tags) \
        and any(l.startswith('- :') and ', carried-by-history — the era annotation of 2026-08-14 (v5.16 :' in l for l in bm)


def mono_bank_ok(S):
    b, EM = S['mbank'], S['EM']
    return b.startswith('### OFFSET FROM v5.16 (R190)(3):') and b.count('### OFFSET FROM') == 1 and ('sha256 %s' % EM.get('sha256', '#')) in b \
        and '### THE FIVE CELLS, OLD AND NEW:' in b and ('the BACK MATTER %d' % EM.get('n_backmatter', -1)) in b \
        and '### ### **THE EDITION LANDS: NO SENTENCE HELD.**' in b and '### H43c`s body count, by its letter:' in b


def h28a_mono(S):
    EM, md = S['EM'], S['md']
    if not md or not EM:
        return False
    bm = NL.join(md[EM['bm'] - 1:])
    ok = all(('was: “%s”' % c['old']) in bm and ('now: “%s”' % c['new']) in bm and c['cites'] for c in EM['changes'])
    return len(EM['changes']) == 5 and _hs(S, 'H28a', 'H28a-MONO', 'HM', 'mbank', 'HOLDS' if ok else 'REFUTED')


def h28b_mono(S):
    EM, md, REC = S['EM'], S['md'], S['REC']
    if not md or not EM:
        return False
    ci, cm = REC._corr_idx(md), REC._corr_idx(S['m16'])
    nb, nc = REC._count(md[:ci]), REC._count(S['m16'][:cm])
    allowed = EM['credit'] + EM['removals'] + EM['history_lines'] + EM['version_lines'] + sum(abs(x['d']) for x in EM['seg_d'])
    return nb == EM.get('n_body') and nc == EM.get('n_cur_body') and EM.get('version_lines') == 1 \
        and _hs(S, 'H28b', 'H28b-MONO', 'HM', 'mbank', 'HOLDS' if abs(nb - nc) <= allowed else 'REFUTED')


def h28c_mono(S):
    if not S['md']:
        return False
    clean = re.search(r'^\s*VERDICT\s*: CLEAN\s*$', S['mscan_now'], re.M) is not None
    unexc = [h for h in S['classify17'] if h['kind'] == 'UNEXCEPTED']
    return _hs(S, 'H28c', 'H28c-MONO', 'HM', 'mbank', 'HOLDS' if clean and not unexc else 'REFUTED') and S['mscan_now'].strip() == S['mscan'].strip() \
        and S['HM'].get('unexcepted') == len(unexc)


def h43c_ok(S):
    if not S['md'] or not S['EM']:
        return False
    REC = S['REC']
    nb, nc = REC._count(S['md'][:REC._corr_idx(S['md'])]), REC._count(S['m16'][:REC._corr_idx(S['m16'])])
    want = 'HOLDS' if mono_cells(S) and nb == nc else 'REFUTED'
    return _hs(S, 'H43c', 'H43c', 'HM', 'mbank', want)


def h43d_ok(S):
    want = 'HOLDS' if all(S['HS'].get(k) == 'HOLDS' for k in ('H28a', 'H28b', 'H28c')) and all(S['HM'].get(k) == 'HOLDS' for k in ('H28a', 'H28b', 'H28c')) else 'REFUTED'
    return _hs(S, 'H43d', 'H43d', 'HM', 'mbank', want)


def pages_banked(S):
    out = []
    for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])):
        a, b, c = S['pages'][p]
        if z.get('changed') is True:
            pl = c.decode('utf-8').split('## Placement')[-1]
            out.append(z.get('rc') == 0 and bool(a) and a == c and a != b and hashlib.sha256(c).hexdigest() == z.get('sha256')
                       and ('`%s`' % SV4) in pl and ('`%s`' % M17) in pl)
        else:
            out.append(z.get('rc') == 0 and z.get('changed') is False and a == b == c)
    return all(out) and (S['PZ'].get('changed') or S['PX'].get('changed'))


def pages_alone(S):
    out = []
    for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])):
        if z.get('changed') is True:
            out.append(_alone(S, p, 'b609 (R219)(3): ' + p))
        else:
            out.append(z.get('changed') is False and not [h for h, f in S['pp_files'].items() if p in f])
    order = [h for h, _s in S['pp_log']]
    eds = [h for h, f in S['pp_files'].items() if SV4 in f or M17 in f]
    pc = [h for h, f in S['pp_files'].items() if PAGE in f or DIR_PAGE in f]
    return all(out) and len(eds) == 2 and all(order.index(h) > max(order.index(e) for e in eds) for h in pc)


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 30]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') and fline(S, e).startswith('## The sieve at v0.4 with the computational range') \
        and all(x in tail for x in ('**The sieve at v0.4**', '**The monograph at v5.17**', '**The scores.**', '**The pages.**',
                                    '**The second reader’s seed.**', '**Read in mutual light**', 'strengthens', '**Next.**', SV4, M17))


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


def g2_names(face):
    try:
        g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def _mut(S, k, i, x):
    ls = list(S[k])
    if 0 < i <= len(ls):
        ls[i - 1] = ls[i - 1] + x
    return put(S, k, ls)


def _sc(S, k):
    return put(S, 'sc', dict(S['sc'], **{k: ['x', '']}))


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R219) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b608`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b608' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b609 -- x'])),
    ('G-R219-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R219) END' in S['ferry'] and S['ot'].count('**(R219) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R219) ratified', '(R219) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in (
        SV3 + ' @ 3d2f67db', 'OPEN_TRAILS.md @ 3d2f67db', M16 + ' @ 3d2f67db', 'Schema/Detector.lean @ c404e727', 'Schema/Epstein.lean @ c404e727',
        'Schema/PlateauRamp.lean @ 914c4137', 'Bridge/TheBridgeComplete.lean @ 0e5233f0', 'Kernel/Integration.lean @ 0e5233f0',
        'Bridge/ConservationBridge.lean @ 0e5233f0', 'data/terminal_table.json @ 11970104', 'SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md @ 3d2f67db',
        'INSTRUMENTS.md @ 847e4333', 'INVARIANCE_BARRIERS_v1_4.md @ 1d0109f3', 'data/b608_edition_PLACE.txt @ 11970104',
        'data/b608_closing_push_out.txt @ 11970104', 'FINDINGS.md @ 3d2f67db', ':11864 ', ':12212 ', ':12228 ', ':12496 ', ':12518 ',
        ':12520 ', ':12522 ', ':1500 ', ':1674 ', ':240 ', ':343 ', ':4049 ')) and 'NO SUCH LINE' not in S['reads'],
     lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ANSWERS-BANKED', 'the act`s answers bank: no prompt put, said so', lambda S: S['answers'].startswith('### b609 -- THE AUTHOR`S ANSWERS, 0 prompt(s)')
     and '### NONE: no prompt was put to the author in this act' in S['answers'] and S['answers'].count('### PROMPT ') == 0,
     lambda S: put(S, 'answers', S['answers'].replace('### b609 -- THE AUTHOR', '### b6O9 -- THE AUTHOR', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay 11970104`s files', lambda S: S['pushout'][0] == ['data/b608_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/b608_closing_push_out.txt', 'x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b608') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b608'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'family-b603': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80 and every PLACE-papers read at ba5f0ea, run afresh through the test`s control()',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(S['ctl'][0], ok=False)] + S['ctl'][1:])),
    ('G-INSTRUMENTS-UNEDITED', 'b608`s sealed suite, record tool and work-list tool, b605`s record tool, the shared record tools and appender, the control`s test file, the generator, its arm, the E0 rule, the push gate, the scanner, the sentence counter and the ERRATA id appender against af1df8d6',
     lambda S: all(bool(a) and a == b for a, b in S['inst'].values()) and len(S['inst']) == 16,
     lambda S: put(S, 'inst', dict(S['inst'], **{'b558_record.py': (S['inst']['b558_record.py'][0], (S['inst']['b558_record.py'][1] or b'') + b'x')}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b608`s weight, CP-8 closed, its figures from its banks', lambda S: weight_ok(S),
     lambda S: put(S, 'find', S['find'].replace('re-pin 919 of 919', 're-pin 919'))),
    ('G-ITEMS-LINE', 'FINDINGS at the banked line: the seat`s items ruled', lambda S: items_ok(S),
     lambda S: put(S, 'find', S['find'].replace('Reading R-8 stands', 'Reading R-8'))),
    ('G-BATCH-LINE', 'OPEN_TRAILS at the banked line: the second reader`s batch named, the seed`s counts as banked', lambda S: batch_ok(S),
     lambda S: put(S, 'RS', dict(S['RS'], n16=-1))),
    ('G-PHASE-LINE', 'OPEN_TRAILS at the banked line: the phase-state reading priced, not started', lambda S: phase_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('one edition of the chosen document. Not started.', 'one edition.'))),
    ('G-SEED-BANKED', 'v5.16`s body re-read now by the four matchers against the seed: every candidate marked, the counts as banked', lambda S: seed_ok(S),
     lambda S: put(S, 'residue_now', S['residue_now'] + [('M1', 1, 'establish')])),
    ('G-HOUSEKEEPING-LIST', 'the terminal table`s housekeeping list: opened after the lock, its entry H-TT-1', lambda S: hk_ok(S),
     lambda S: put(S, 'hk_mtime', 1)),
    ('G-ROWS-BANKED', 'the rows bank and its json: banked before the sieve`s edition, its three parts, every source resolving', lambda S: rows_bank_ok(S),
     lambda S: put(S, 'RJ', dict(S['RJ'], at='9999'))),
    ('G-INSTRUMENTS-RESOLVE-NOW', 'every row`s and the FD reading`s sources re-resolved now by git at their pins', lambda S: instr_now_ok(S),
     lambda S: put(S, 'instr_now', [dict(S['instr_now'][0], ok=False)] + S['instr_now'][1:])),
    ('G-PAGES-NO-PIECE', 'both pages at PLACE-papers HEAD searched for the four compiled pieces: none', lambda S: not any(S['pieces_now'].values())
     and set(S['pieces_now']) == {PAGE, DIR_PAGE}, lambda S: put(S, 'pieces_now', dict(S['pieces_now'], **{PAGE: ['none_produce']}))),
    ('G-CURRENT-UNEDITED', 'v0.3, v0.2, the unnumbered sieve, v5.16, v5.15, v5.14 and v5.13 on disk and at HEAD against 3d2f67d', lambda S: unedited_all(S),
     lambda S: put(S, 'currents', dict(S['currents'], **{M16: (S['currents'][M16][0] + b'x', S['currents'][M16][1], S['currents'][M16][2])}))),
    ('G-SIEVE-CARRIES', 'v0.4 at its banked sha: every non-blank v0.3 line carried verbatim, rewritten with its fragments recorded, or re-pinned', lambda S: sieve_carries(S),
     lambda S: _mut(S, 'sv', (S['ES'].get('where') or {}).get('46', 0) if S['ES'] else 0, ' x')),
    ('G-SIEVE-VERSION-LINE', 'v0.4`s version line on :3 above v0.3`s, the head above it unchanged', lambda S: sieve_version(S),
     lambda S: put(S, 'sv', [l.replace('*v0.4, 2026-10-03 --', '*v0.4 --') for l in S['sv']])),
    ('G-SIEVE-ROWS', 'the three rows on their banked lines after RH-57', lambda S: sieve_rows(S),
     lambda S: put(S, 'sv', [l.replace('| RH-59 | ', '| RH-61 | ') for l in S['sv']])),
    ('G-SIEVE-HEAD-COUNTS', 'the body`s rows and verdicts counted afresh against the head`s and the cluster`s re-stated counts', lambda S: sieve_counts(S),
     lambda S: put(S, 'sv', [l.replace('87 rows -- 2 BRIGHT', '86 rows -- 2 BRIGHT') for l in S['sv']])),
    ('G-SIEVE-BACKMATTER', 'v0.4`s back matter after v0.3`s: its sections in order, no blank Status cell', lambda S: sieve_bm_ok(S),
     lambda S: put(S, 'sv', [l.replace('### FD-01 and FD-02, read once', '### FD-01 and FD-02') for l in S['sv']])),
    ('G-SIEVE-BANK', 'the sieve`s diff bank: its offset head once, the final sha, the three rows, the deciding lines, the counts, the landing line', lambda S: sieve_bank_ok(S),
     lambda S: put(S, 'sbank', S['sbank'].replace('THE SIEVE LANDS', 'THE SIEVE'))),
    ('G-SIEVE-REPIN', 'the sieve`s re-pin bank against the final file', lambda S: _repin_ok(S['srepin'], 250) and S['ES'].get('sha256', '#') in S['sbank'],
     lambda S: put(S, 'srepin', S['srepin'].replace('RE-PIN : ', 'RE-PIN : 1'))),
    ('G-H28A-SIEVE-SCORED', 'H28a for v0.4 in its bank, the scores and the desk', lambda S: _hs(S, 'H28a', 'H28a-SIEVE', 'HS', 'sbank', S['HS'].get('H28a'))
     and S['HS'].get('H28a') == ('HOLDS' if all(x['recorded'] for x in S['HS'].get('h28a_rows') or [{}]) and instr_now_ok(S) else 'REFUTED'),
     lambda S: _sc(S, 'H28a-SIEVE')),
    ('G-H28B-SIEVE-SCORED', 'the bodies of v0.3 and v0.4 counted afresh, the bound recomputed', lambda S: h28b_sieve(S),
     lambda S: put(S, 'ES', dict(S['ES'], n_body=-1))),
    ('G-H28C-SIEVE-SCORED', 'the scanner run afresh on v0.4 and its body read for the ceiling', lambda S: h28c_sieve(S),
     lambda S: put(S, 'sscan_now', S['sscan_now'].replace('VERDICT          : CLEAN', 'VERDICT          : NOT CLEAN'))),
    ('G-H43A-SCORED', 'the three rows re-read on v0.4: one verdict each, their sources resolving now', lambda S: h43a_ok(S),
     lambda S: _sc(S, 'H43a')),
    ('G-H43B-SCORED', 'the mechanism row`s verdict and its deciding lines on v0.4, the pages searched now', lambda S: h43b_ok(S),
     lambda S: _sc(S, 'H43b')),
    ('G-SIEVE-COMMITTED-ALONE', 'PLACE-papers` log since 3d2f67d: v0.4 in one commit of its own, on disk as committed', lambda S: _alone(S, SV4, 'b609 (R219)(3)(a): ' + SV4)
     and bool(S['sv_head']) and S['sv_head'] == S['sv_disk'], lambda S: put(S, 'pp_files', {h: (f + ['FINDINGS.md'] if SV4 in f else f) for h, f in S['pp_files'].items()})),
    ('G-MONO-CARRIES', 'v5.17 at its banked sha: every non-blank v5.16 line carried verbatim, rewritten with both wordings recorded, or re-pinned', lambda S: mono_carries(S),
     lambda S: _mut(S, 'md', 1675, ' x')),
    ('G-MONO-VERSION-LINE', 'v5.17`s version line on :19 above v5.16`s, the head above it unchanged', lambda S: mono_version(S),
     lambda S: put(S, 'md', [l.replace('**v5.17, 2026-10-03**', '**v5.17**') for l in S['md']])),
    ('G-MONO-CELLS', 'the body of v5.17 against v5.16: the five cells changed and no other line', lambda S: mono_cells(S),
     lambda S: _mut(S, 'md', 1497, ' x')),
    ('G-MONO-BACKMATTER', 'v5.17`s back matter after v5.16`s, v5.15`s and v5.14`s: its sections in order, the era row re-listed, no blank Status cell', lambda S: mono_bm_ok(S),
     lambda S: put(S, 'md', [l.replace('### The five cells', '### Cells') for l in S['md']])),
    ('G-MONO-BANK', 'the monograph`s diff bank: its offset head once, the final sha, the five cells, the counts, H43c`s letter, the landing line', lambda S: mono_bank_ok(S),
     lambda S: put(S, 'mbank', S['mbank'].replace('THE EDITION LANDS', 'THE EDITION'))),
    ('G-MONO-REPIN', 'the monograph`s re-pin bank against the final file', lambda S: _repin_ok(S['mrepin'], 400) and S['EM'].get('sha256', '#') in S['mbank'],
     lambda S: put(S, 'mrepin', S['mrepin'].replace('RE-PIN : ', 'RE-PIN : 1'))),
    ('G-H28A-MONO-SCORED', 'every cell`s both wordings in v5.17`s back matter and its citation, the scores, the desk', lambda S: h28a_mono(S),
     lambda S: _sc(S, 'H28a-MONO')),
    ('G-H28B-MONO-SCORED', 'the bodies of v5.16 and v5.17 counted afresh, the bound recomputed', lambda S: h28b_mono(S),
     lambda S: put(S, 'EM', dict(S['EM'], n_body=-1))),
    ('G-H28C-MONO-SCORED', 'the scanner run afresh on v5.17 and its body`s ceiling hits classified afresh', lambda S: h28c_mono(S),
     lambda S: put(S, 'classify17', S['classify17'] + [dict(line=1, src=1, hit='proof', kind='UNEXCEPTED')])),
    ('G-H43C-SCORED', 'the five cells and the bodies counted afresh: H43c by its letter', lambda S: h43c_ok(S), lambda S: _sc(S, 'H43c')),
    ('G-H43D-SCORED', 'H28a-H28c of both editions in their banks: H43d', lambda S: h43d_ok(S), lambda S: _sc(S, 'H43d')),
    ('G-MONO-COMMITTED-ALONE', 'PLACE-papers` log since 3d2f67d: v5.17 in one commit of its own, on disk as committed', lambda S: _alone(S, M17, 'b609 (R219)(3)(b): ' + M17)
     and bool(S['md_head']) and S['md_head'] == S['md_disk'], lambda S: put(S, 'pp_files', {h: (f + ['FINDINGS.md'] if M17 in f else f) for h, f in S['pp_files'].items()})),
    ('G-PAGES-BANKED', 'both pages at HEAD and their banks: each changed page re-emitted from its probe with both editions in its Placement', lambda S: pages_banked(S),
     lambda S: put(S, 'PZ', dict(S['PZ'], sha256='0'))),
    ('G-PAGES-COMMITTED-ALONE', 'PLACE-papers` log since 3d2f67d: each changed page in one commit of its own, after both editions`', lambda S: pages_alone(S),
     lambda S: put(S, 'pp_files', {h: (f + ['FINDINGS.md'] if (PAGE in f or DIR_PAGE in f) else f) for h, f in S['pp_files'].items()})),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b602`s list and v0.20 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b603`s list and v0.21 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank after the page commits: both page arms and the frozen control', lambda S: 'PAGE ARMS PASSING : 2 of 2' in S['arms_c2']
     and ('%s PASSING : 2 of 2' % CONTROL_ARM) in S['arms_c2'], lambda S: put(S, 'arms_c2', S['arms_c2'].replace('PASSING : 2 of 2', 'PASSING : 1 of 2'))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD,
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and 'R-1 to R-5' in trail(S) and 'CL1-CL2' in trail(S) and 'For the author:' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('Resolved by the seat, for the author’s strike', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b610, the phase-state reading' in trail(S) and 'W-ORD-QUANTIFIER-COLUMN' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b610, the phase-state reading', 'x'))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, lv`s HEAD and status, the explicit-formula checkout on main and clean with no new tag, the trial branch',
     lambda S: all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['kcur'] == 'main' and S['kdirty'] == ''
     and 'v0.21' in S['ktags'] and 'v0.22' not in S['ktags'] and S['trial'] == 'f22ff35' and S['lv_head'].startswith('2f71068a')
     and S['lv_dirty'] == '', lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-kernel': '0'}))),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('36352a0', '36352a0', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b609_record.py'): S['tooltext'].get(os.path.join(T, 'b609_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                              if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces'][1] and S['faces'][0] == S['faces'][1],
     lambda S: put(S, 'faces', (S['faces'][0] + b'x', S['faces'][1]))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-REGISTRY-UNTOUCHED', 'REGISTRY.md and SPIRAL_MAP.md against their pre-act blobs', lambda S: S['registry'][1] and S['registry'][0] == S['registry'][1]
     and S['spiral'][1] and S['spiral'][0] == S['spiral'][1], lambda S: put(S, 'spiral', (S['spiral'][0] + b'x', S['spiral'][1]))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md on disk and at HEAD against 3d2f67d', lambda S: bool(S['errata'][1]) and S['errata'][0] == S['errata'][1] == S['errata'][2],
     lambda S: put(S, 'errata', (S['errata'][0] + b'x', S['errata'][1], S['errata'][2]))),
    ('G-KEYSTONES-SCOPE', 'PLACE-papers` phase, day1 and outputs paths, tracked and untracked: the two edition files alone', lambda S: S['keystone_changes'] == sorted([SV4, M17]),
     lambda S: put(S, 'keystone_changes', sorted([SV4, M17, M16]))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at af1df8d6, by blob id', lambda S: S['prior_bad'] == []
     and S['prior_n'] > 6000, lambda S: put(S, 'prior_bad', ['data/b608_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == sorted(
        ['FINDINGS.md', 'OPEN_TRAILS.md', SV4, M17] + [p for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])) if z.get('changed')]),
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
                                                                          and "startswith('b609')" in S['suite'] and "data/b609_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b609')", ''))),
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
    rec('b609 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('PRE-SEAL (R202)(3)' if PRERUN else 'POST-PUSH' if pushed else 'PRE-PUSH'))
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
        out = os.path.join(D, 'b609_arms_prerun.txt')
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b609_checks_postpush.txt' if pushed else 'b609_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    if not (RERUN or PRERUN):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b609_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
