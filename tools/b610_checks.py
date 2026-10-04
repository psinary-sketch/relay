# -*- coding: utf-8 -*-
"""b610_checks.py -- THE SUITE OF b610, UNDER (R220): THE PHASE-STATE READING -- THE_KEYSTONE_CENSUS AT v0.3 ONE ROW PER PHASE AND
CLUSTER, THE KEYSTONE TEST RULED TO THE TAXONOMY, SPIRAL_MAP AT v0.7 POINTING TO THE ROWS; THE SECOND READER'S ADDENDUM.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>` or `--prerun`; it writes data/b610_checks.txt before the push and
### data/b610_checks_postpush.txt after it. ### `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the
### face is sealed, no table regenerated, its counts written to data/b610_arms_prerun.txt and nothing else.
### ### The harness is b568's to b609's, carried from tools/b609_checks.py (its imports, helpers, regenerate and main); the
### sources, predicates and arms are b610's. The control arm is the frozen one of (R207)(2).
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
FACE = os.path.join(D, 'b610_registration_2026-10-03.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
CEN, CEN3 = 'phase2/method/THE_KEYSTONE_CENSUS.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_3.md'
SPI, SPI7 = 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md'
CURRENTS = (CEN, SPI, 'phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md', 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_4.md',
            'day1/A_Place_to_Stand_v5_17.md')
PRE = dict(relay='d121b88f', pp='7055f04', gs='3528bcf', ker='1d5d4dd')
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf69', 'SIDE-rcurve': 'd5f33b44', 'SIDE-explicit-formula': '1d5d4dd9'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b', 'product-b600': '1dd5cd7',
        'doubling-keiper-b601': '5fc0c87', 'sign-window-b602': '914c413', 'family-b603': '1d5d4dd'}
STEPZERO = '05ee3f9c'
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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b610')
            and 'data/b610_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
            ch |= set(untracked(PP, 'phase1.5', 'phase2', 'day1', SPI7))
        res += ['%s/%s' % (name, x) for x in ch]
    return sorted(res)


def lines_of(b):
    l = cr0(b).decode('utf-8', 'replace').split(NL)
    return l[:-1] if l and l[-1] == '' else l


def _scan(path):
    return subprocess.run([sys.executable, os.path.join(T, 'banned_terms.py'), '--new', path], capture_output=True, text=True,
                          encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8')).stdout


def sources():
    import b610_record as REC
    import b610_census as C
    import b604_record as R4
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b610_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b610_') and f.endswith('.py'))
    cp, sp = os.path.join(PP, *CEN3.split('/')), os.path.join(PP, SPI7)
    S = dict(
        REC=REC, C=C, R4=R4, face=face, ferry=rd('b610_ferry.txt'), scan=rd('b610_ferry_scan.txt'), cens=rd('b610_census_stepzero.txt'),
        fcens=rd('b610_faces_census_stepzero.txt'), pins0=rd('b610_pins_stepzero.txt'), procs=rd('b610_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b609_closing.txt'), reads=rd('b610_reads.txt'), branches=rd('b610_branches.txt'), answers=rd('b610_author_answers.txt'),
        prerun=rd('b610_arms_prerun.txt'), defects=rd('b610_defects.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))))
              for f in ('b609_checks.py', 'b609_record.py', 'b609_worklist.py', 'b604_record.py', 'b602_record.py', 'b560_record.py',
                        'b566_record.py', 'test_chain_page_b596.py', 'chain_page.py', 'e0_rule.py', 'g_chain_page.py', 'push_gated.sh',
                        'banned_terms.py', 'b558_record.py', 'errata_append.py', 'terminal_table.py')},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        readme=(cr0(raw(os.path.join(PP, 'README.md'))), cr0(blob(PP, PRE['pp'] + ':README.md'))),
        registry=(cr0(raw(os.path.join(PP, 'REGISTRY.md'))), cr0(blob(PP, PRE['pp'] + ':REGISTRY.md'))),
        faces=(cr0(raw(os.path.join(PP, 'FACES_LEDGER.md'))), cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md'))),
        errata=(cr0(raw(os.path.join(PP, 'ERRATA.md'))), cr0(blob(PP, PRE['pp'] + ':ERRATA.md')), cr0(blob(PP, 'HEAD:ERRATA.md'))),
        currents={p: (cr0(raw(os.path.join(PP, *p.split('/')))), cr0(blob(PP, PRE['pp'] + ':' + p)), cr0(blob(PP, 'HEAD:' + p))) for p in CURRENTS},
        cd_disk=cr0(raw(cp)), cd_head=cr0(blob(PP, 'HEAD:' + CEN3)), sd_disk=cr0(raw(sp)), sd_head=cr0(blob(PP, 'HEAD:' + SPI7)),
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
        push_lists={r: gs(r, 'branch', '--list', 'push-b609*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b610_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b610_mustnotexist.txt')), table_changed=None,
        fj=jl('b610_findings.json'), tj=jl('b610_trail.json'), sc=jl('b610_scores.json'), desk=rd('b610_desk_notes.txt'),
        rl=jl('b610_record_lines.json'), AJ=jl('b610_residue_addendum.json'), atxt=rd('b610_residue_addendum.txt'),
        CJ=jl('b610_census.json'), ctxt=rd('b610_census.txt'),
        EC=jl('b610_census_edition.json'), HC=jl('b610_h28_census.json'), cbank=rd('b610_edition_CENSUS.txt'), crepin=rd('b610_repin_census.txt'),
        cscan=rd('b610_census_termscan.txt'),
        ES=jl('b610_spiral_edition.json'), HS=jl('b610_h28_spiral.json'), sbank=rd('b610_edition_SPIRAL.txt'), srepin=rd('b610_repin_spiral.txt'),
        sscan=rd('b610_spiral_termscan.txt'),
        PZ=jl('b610_page_zeta.json'), PX=jl('b610_page_chi.json'), arms_c2=rd('b610_page_arms_c2.txt'),
    )
    S['cd'] = lines_of(S['cd_disk']) if S['cd_disk'] else []
    S['sd'] = lines_of(S['sd_disk']) if S['sd_disk'] else []
    S['ccur'] = lines_of(S['currents'][CEN][1])
    S['scur'] = lines_of(S['currents'][SPI][1])
    S['cscan_now'] = _scan(cp) if S['cd_disk'] else ''
    S['sscan_now'] = _scan(sp) if S['sd_disk'] else ''
    S['written'] = written_files(lock_epoch or 0)
    S['globs'] = wl_globs(face)
    B = C.build()
    S['B'] = B
    S['placed_now'] = [(r['line'], r['census']) for r in B['rows']]
    S['kl_now'] = C.keystone_less(B)
    S['add_now'] = [(p, n, ms) for p, n, ms, _l in REC.add_hits(B)]
    S['tags_now'] = {k: C.local_peel(k, v['current']) for k, v in (S['CJ'].get('remotes') or {}).items() if v.get('current')}
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
    ch |= set(untracked(PP, 'phase1.5', 'phase2', 'day1', 'outputs', SPI7))
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
    X['gcp_zeta'] = GCP.arm(os.path.join(D, 'b602_nodes_zeta.txt'), os.path.join(SP, '_b610_gcp'), os.path.join(D, 'b602_probe_out.txt'))
    X['gcp_chi'] = GCP.arm(os.path.join(D, 'b603_nodes_chi.txt'), os.path.join(SP, '_b610_gcp'), os.path.join(D, 'b603_chi_probe_out.txt'))
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
    return bool(x) and x.get('file') == 'FINDINGS.md' and a.startswith(x['head']) and '(:7186)' in a and 'THE NAVIGATOR’S BRIGHT REFUTED' in a \
        and 're-pin 326 of 326' in a and 're-pin 496 of 496' in a and 'TheBridgeComplete.lean :157-:159' in a and '90 of 90' in a and x['line'] > 7186


def enum_ok(S):
    x, A = _rl(S, 1), S['AJ']
    a = fline(S, x.get('line'))
    return bool(x) and bool(A) and x.get('file') == 'FINDINGS.md' and a.startswith(x['head']) and 'THE ENUMERATION’S COMPILED FORM' in a \
        and 'b610_residue_addendum.txt' in a and ('-- %d lines of' % A['n']) in a and ('%d marked kin' % A['kin']) in a \
        and x['line'] > _rl(S, 0).get('line', 10 ** 9)


def test_ok(S):
    x = _rl(S, 2)
    a = oline(S, x.get('line'))
    return bool(x) and x.get('file') == 'OPEN_TRAILS.md' and a.startswith(x['head']) and '(:4049)' in a and '(:12544)' in a \
        and 'THE KEYSTONE TEST, RULED' in a and 'retires to the taxonomy' in a and 'closes under this clause' in a and x['line'] > 12550


def seq_ok(S):
    x = _rl(S, 3)
    a = oline(S, x.get('line'))
    return bool(x) and x.get('file') == 'OPEN_TRAILS.md' and a.startswith(x['head']) and 'THE SYNTHESIS SEQUENCE, ENTERED WITH ITS FORM' in a \
        and 'the first is b611' in a and 'Each act prices the next.' in a and x['line'] > _rl(S, 2).get('line', 10 ** 9)


def add_ok(S):
    REC, A = S['REC'], S['AJ']
    now = S['add_now']
    marks = [REC.ADD_MARKS.get((p, n)) for p, n, _m in now]
    kin = sum(1 for m in marks if m and m[0] == REC.KIN)
    return bool(A) and len(now) == A.get('n') and None not in marks and kin == A.get('kin') and len(REC.ADD_MARKS) == len(now) \
        and ('### ### **THE ADDENDUM: %d lines read -- KIN %d ;' % (len(now), kin)) in S['atxt'] and 'unmarked 0.**' in S['atxt'] \
        and 'that bank is a prior bank and is not edited' in S['atxt']


def census_banked(S):
    CJ, EC, t = S['CJ'], S['EC'], S['ctxt']
    return bool(CJ) and bool(EC) and CJ.get('at', 'z') < EC.get('at', '') and t.startswith('b610 -- COMPONENT 2') \
        and all(('### PART %s' % p) in t for p in 'ABCDEF') and all(('### ### **H44%s ' % h) in t for h in 'abc') and len(CJ.get('rows') or []) == 23


def placed_now(S):
    bank = [(r['line'], r['census']) for r in S['CJ'].get('registry_rows') or []]
    return bool(bank) and bank == S['placed_now'] and None not in [k for _l, k in S['placed_now']]


def kl_now(S):
    return S['kl_now'] == (S['CJ'].get('h44') or {}).get('kl') and 5 <= len(S['kl_now']) <= 8


def tags_now(S):
    R = S['CJ'].get('remotes') or {}
    tagged = {k: v for k, v in R.items() if v.get('current')}
    return bool(tagged) and all(S['tags_now'].get(k) == v['remote_peel'] for k, v in tagged.items()) and len(S['tags_now']) == len(tagged)


def unedited_all(S):
    return all(bool(b) and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


def _hs(S, hkey, skey, src, bank, want):
    return S[src].get(hkey) == want and (S['sc'].get(skey) or [''])[0] == want and ('(%s)' % skey.upper()) in S['desk'] \
        and ('### ### **%s %s' % (hkey, want)) in S[bank]


def census_carries(S):
    cd, EC = S['cd'], S['EC']
    if not cd or not EC:
        return False
    nset = set(cd)
    miss = [i for i, l in enumerate(S['ccur'], 1) if l.strip() and l not in nset]
    return not miss and hashlib.sha256(S['cd_disk']).hexdigest() == EC.get('sha256')


def census_version(S):
    cd, c = S['cd'], S['ccur']
    return bool(cd) and cd[:9] == c[:9] and cd[9] == S['REC'].VERSION3 and cd[10] == '' and cd[11] == c[9] and c[9].startswith('**Method register · v0.1')


def census_test(S):
    cd = S['cd']
    if not cd:
        return False
    i = next((n for n, l in enumerate(cd) if l.startswith('## §0 — THE KEYSTONE TEST, RULED')), -1)
    j = next((n for n, l in enumerate(cd) if l.startswith('## §0 — THE CATEGORY, DEFINED BEFORE COUNTING')), -1)
    block = S['ccur'][11:21]
    return 0 <= i < j and cd[j:j + 10] == block and cd[j + 11] == S['REC'].HIST3 and 'Tier KC' in cd[i + 2] and '(R19)' in cd[i + 2]


def census_rows(S):
    cd, EC, CJ = S['cd'], S['EC'], S['CJ']
    if not cd or not EC or not CJ:
        return False
    ok = 0
    for row in CJ['rows']:
        p = EC['pos'].get(row['n'])
        l = cd[p - 1] if p else ''
        ok += l.startswith('| %s | ' % row['n']) and all(('(:%d)' % x['line']) in l for x in row['rows'])
    body = cd[:EC['bm'] - 1]
    return ok == len(CJ['rows']) == 23 and sum(1 for l in body if re.match(r'^\| R\d\d \| ', l)) == 23


def census_nokey(S):
    cd, CJ = S['cd'], S['CJ']
    if not cd or not CJ:
        return False
    i = next((n for n, l in enumerate(cd) if l.startswith('## §2 — THE CLUSTERS WITH DOCUMENTS AND NO KEYSTONE')), -1)
    j = next((n for n, l in enumerate(cd) if l.startswith('## §3 — ')), -1)
    got = [re.match(r'^- \*\*(R\d\d) ', l).group(1) for l in cd[i:j] if re.match(r'^- \*\*R\d\d ', l)] if 0 <= i < j else []
    want = [r['n'] for r in CJ['rows'] if not r['has_keystone']]
    return bool(want) and got == want


def census_bm(S):
    cd, EC, REC = S['cd'], S['EC'], S['REC']
    if not cd or REC.BM_TAG3 not in cd:
        return False
    bm = cd[cd.index(REC.BM_TAG3):]
    heads = ['### The readings', '### Removals', '### History lines', '### The census at v0.1 and v0.2, moved whole', '### Placement',
             '### Correspondence', '### Version history']
    pos = [next((i for i, l in enumerate(bm) if l.startswith(h)), -1) for h in heads]
    blanks = [l for l in bm if l.startswith('| ') and not l.startswith('|:--') and l.rstrip().endswith('|  |')]
    mi = pos[3] + 2
    moved = S['ccur'][21:]
    return all(p >= 0 for p in pos) and pos == sorted(pos) and not blanks and bm[mi:mi + len(moved)] == moved and cd.index(REC.BM_TAG3) + 1 == EC['bm']


def cbank_ok(S):
    b, EC = S['cbank'], S['EC']
    return b.startswith('### OFFSET FROM THE CURRENT VERSION (R190)(3):') and b.count('### OFFSET FROM') == 1 and ('sha256 %s' % EC.get('sha256', '#')) in b \
        and '### THE ROWS, EACH WITH ITS LINE IN v0.3 AND ITS REGISTRY LINES:' in b and ('the BACK MATTER %d' % EC.get('n_backmatter', -1)) in b \
        and '### ### **THE CENSUS LANDS: NO SENTENCE HELD.**' in b


def _repin_ok(t, floor):
    m = re.search(r'RE-PIN : (\d+) of (\d+) citations hold', t)
    return bool(m) and m.group(1) == m.group(2) and int(m.group(2)) > floor and 'unresolved tokens in the back matter: none' in t


def _body_count(S, lines, bm):
    return S['REC']._count(lines[:bm - 1])


def h28b_census(S):
    EC, cd = S['EC'], S['cd']
    if not cd or not EC:
        return False
    nb, nc = _body_count(S, cd, EC['bm']), S['REC']._count(S['ccur'])
    allowed = EC['removals'] + EC['ruled'] + EC['history_lines'] + EC['version_lines']
    strict = nb == nc - EC['removals'] + EC['ruled'] + EC['history_lines'] + EC['version_lines']
    return nb == EC.get('n_body') and nc == EC.get('n_cur_body') and strict and _hs(S, 'H28b', 'H28b-CENSUS', 'HC', 'cbank', 'HOLDS' if abs(nb - nc) <= allowed else 'REFUTED')


def h28c_census(S):
    cd, EC = S['cd'], S['EC']
    if not cd:
        return False
    clean = re.search(r'^\s*VERDICT\s*: CLEAN\s*$', S['cscan_now'], re.M) is not None
    beyond = [i for i, l in enumerate(cd[:EC['bm'] - 1]) if S['R4'].CEILING.search(l)]
    return _hs(S, 'H28c', 'H28c-CENSUS', 'HC', 'cbank', 'HOLDS' if clean and not beyond else 'REFUTED') and S['cscan_now'].strip() == S['cscan'].strip()


def _alone(S, path, prefix):
    c = [h for h, f in S['pp_files'].items() if path in f]
    return len(c) == 1 and S['pp_files'][c[0]] == [path] and dict(S['pp_log'])[c[0]].startswith(prefix)


def spiral_carries(S):
    sd, ES = S['sd'], S['ES']
    if not sd or not ES:
        return False
    fix = dict((f['line'], f) for f in ES['fixes'])
    nset = set(sd)
    miss = [i for i, l in enumerate(S['scur'], 1) if l.strip() and l not in nset and not (i in fix and l.replace(fix[i]['old'], fix[i]['new']) in nset)]
    return not miss and hashlib.sha256(S['sd_disk']).hexdigest() == ES.get('sha256')


def spiral_version(S):
    sd, s = S['sd'], S['scur']
    return bool(sd) and sd[:17] == s[:17] and sd[17] == S['REC'].VERSION7 and sd[18] == '' and sd[19] == s[17] and s[17].startswith('**v0.6 — July 2026**')


def spiral_pointers(S):
    sd, ES, CJ = S['sd'], S['ES'], S['CJ']
    if not sd or not ES or not CJ:
        return False
    want = S['REC']._pointer_lines(CJ['rows'])
    got = [sd[ES['pos']['p%d' % k] - 1] for k in range(len(S['C'].SPIRAL_CLUSTERS))]
    return got == want and len(got) == 8 and all(re.search(r'rows R\d\d \(', l) for l in got) \
        and sd[ES['pos']['pt0'] - 1].startswith('**THE CENSUS ROWS — 2026-10-03 (b610)') and sd[ES['pos']['pt0'] - 2] == ''


def spiral_fixes(S):
    sd, ES = S['sd'], S['ES']
    if not sd or not ES:
        return False
    return len(ES['fixes']) == 4 and all(sd[f['at'] - 1] == S['scur'][f['line'] - 1].replace(f['old'], f['new']) and f['old'] not in sd[f['at'] - 1]
                                         for f in ES['fixes'])


def spiral_bm(S):
    sd, ES, REC = S['sd'], S['ES'], S['REC']
    if not sd or REC.BM_TAG7 not in sd:
        return False
    bm = sd[sd.index(REC.BM_TAG7):]
    heads = ['### The readings', '### Insertions ordered by the ruling', '### Stem corrections', '### Ceiling corrections',
             '### The ceiling pattern’s other hits', '### Placement', '### Correspondence', '### Version history']
    pos = [next((i for i, l in enumerate(bm) if l.startswith(h)), -1) for h in heads]
    blanks = [l for l in bm if l.startswith('| ') and not l.startswith('|:--') and l.rstrip().endswith('|  |')]
    stem = [l for l in bm if '(banned stem; correction record)' in l]
    return all(p >= 0 for p in pos) and pos == sorted(pos) and not blanks and len(stem) == 1 and sd.index(REC.BM_TAG7) + 1 == ES['bm']


def sbank_ok(S):
    b, ES = S['sbank'], S['ES']
    return b.startswith('### OFFSET FROM v0.6 (R190)(3):') and b.count('### OFFSET FROM') == 1 and ('sha256 %s' % ES.get('sha256', '#')) in b \
        and '### THE CORRECTIONS, BOTH WORDINGS:' in b and ('the BACK MATTER %d' % ES.get('n_backmatter', -1)) in b \
        and '### ### **THE MAP LANDS: NO SENTENCE HELD.**' in b


def h28b_spiral(S):
    ES, sd = S['ES'], S['sd']
    if not sd or not ES:
        return False
    nb, nc = _body_count(S, sd, ES['bm']), S['REC']._count(S['scur'])
    allowed = ES['ruled'] + ES['version_lines'] + sum(abs(x['d']) for x in ES['seg_d'])
    return nb == ES.get('n_body') and nc == ES.get('n_cur_body') and _hs(S, 'H28b', 'H28b-SPIRAL', 'HS', 'sbank', 'HOLDS' if abs(nb - nc) <= allowed else 'REFUTED')


def h28c_spiral(S):
    sd, ES = S['sd'], S['ES']
    if not sd or not ES:
        return False
    clean = re.search(r'^\s*VERDICT\s*: CLEAN\s*$', S['sscan_now'], re.M) is not None
    carried = set(ES['where'][str(n)] for n in S['REC'].SP_CARRY)
    beyond = [i + 1 for i, l in enumerate(sd[:ES['bm'] - 1]) if S['R4'].CEILING.search(l) and (i + 1) not in carried]
    return _hs(S, 'H28c', 'H28c-SPIRAL', 'HS', 'sbank', 'HOLDS' if clean and not beyond else 'REFUTED') and S['sscan_now'].strip() == S['sscan'].strip()


def h44_ok(S, k):
    H = S['CJ'].get('h44') or {}
    if k == 'H44a':
        want = 'HOLDS' if placed_now(S) and H.get('unplaced') == 0 and H.get('sums') == H.get('n_rows') == len(S['placed_now']) else 'REFUTED'
    elif k == 'H44b':
        want = 'HOLDS' if 5 <= len(S['kl_now']) <= 8 and kl_now(S) else 'REFUTED'
    elif k == 'H44c':
        want = 'HOLDS' if tags_now(S) and not H.get('unread') else 'REFUTED'
    else:
        want = 'HOLDS' if all(S['HC'].get(x) == 'HOLDS' for x in ('H28a', 'H28b', 'H28c')) and all(S['HS'].get(x) == 'HOLDS' for x in ('H28a', 'H28b', 'H28c')) else 'REFUTED'
    return H.get(k, want) == want and (S['sc'].get(k) or [''])[0] == want and ('(%s)' % k.upper()) in S['desk']


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
            out.append(_alone(S, p, 'b610 (R220)(4): ' + p))
        else:
            out.append(z.get('changed') is False and not [h for h, f in S['pp_files'].items() if p in f])
    return all(out)


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 32]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') and fline(S, e).startswith('## The phase-state reading: THE_KEYSTONE_CENSUS at v0.3') \
        and all(x in tail for x in ('**The census at v0.3**', '**The clusters with documents and no keystone**', '**The keystone test, ruled**',
                                    '**SPIRAL_MAP at v0.7**', '**The kernels.**', '**The scores.**', '**Read in mutual light**', 'strengthens', '**Next.**',
                                    CEN3, SPI7))


def seq_named(S):
    t, CJ = trail(S), S['CJ']
    kl = [r for r in CJ.get('rows') or [] if not r['has_keystone']]
    return bool(kl) and all(('- **b%d** -- %s %s: one new document in the cluster’s folder' % (611 + i, r['n'], r['label'])) in t for i, r in enumerate(kl))


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


READ_NEEDLES = ('REGISTRY.md @ 7055f04f', 'phase2/method/THE_KEYSTONE_CENSUS.md @ 7055f04f', 'THE_DOCUMENT_CLASS_TAXONOMY.md @ 7055f04f',
                'SPIRAL_MAP.md @ 7055f04f', 'OPEN_TRAILS.md @ 7055f04f', 'FINDINGS.md @ 7055f04f', 'THE_FINDINGS_AS_THEY_STAND_v0_4.md @ 7055f04f',
                'README.md @ 7055f04f', 'tools/mirror_roster.json @ 05ee3f9c', 'data/b609_closing_push_out.txt @ 05ee3f9c',
                'data/b577_edition_order.txt @ 05ee3f9c', ':4049 ', ':4397 ', ':11864 ', ':12228 ', ':12456 ', ':12542 ', ':12544 ', ':7186 ',
                ':780 ', ':956 ', ':960 ', ':102 ', ':669 ', ':57 ')

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R220) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b609`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b609' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b610 -- x'])),
    ('G-R220-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R220) END' in S['ferry'] and S['ot'].count('**(R220) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R220) ratified', '(R220) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in READ_NEEDLES) and 'NO SUCH LINE' not in S['reads'],
     lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ANSWERS-BANKED', 'the act`s answers bank: no prompt put, said so', lambda S: S['answers'].startswith('### b610 -- THE AUTHOR`S ANSWERS, 0 prompt(s)')
     and '### NONE: no prompt was put to the author in this act' in S['answers'] and S['answers'].count('### PROMPT ') == 0,
     lambda S: put(S, 'answers', S['answers'].replace('### b610 -- THE AUTHOR', '### b61O -- THE AUTHOR', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay 05ee3f9c`s files', lambda S: S['pushout'][0] == ['data/b609_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/b609_closing_push_out.txt', 'x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b609') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b609'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'family-b603': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80 and every PLACE-papers read at ba5f0ea, run afresh through the test`s control()',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(S['ctl'][0], ok=False)] + S['ctl'][1:])),
    ('G-INSTRUMENTS-UNEDITED', 'b609`s sealed suite, record tool and work-list tool, the shared record tools and appender, the control`s test file, the generator, its arm, the E0 rule, the push gate, the scanner, the sentence counter, the ERRATA id appender and the table generator against d121b88f',
     lambda S: all(bool(a) and a == b for a, b in S['inst'].values()) and len(S['inst']) == 16,
     lambda S: put(S, 'inst', dict(S['inst'], **{'b558_record.py': (S['inst']['b558_record.py'][0], (S['inst']['b558_record.py'][1] or b'') + b'x')}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b609`s weight, the navigator`s BRIGHT refuted', lambda S: weight_ok(S),
     lambda S: put(S, 'find', S['find'].replace('re-pin 326 of 326', 're-pin 326'))),
    ('G-ENUMERATION-LINE', 'FINDINGS at the banked line: the enumeration`s compiled form, the addendum`s counts as banked', lambda S: enum_ok(S),
     lambda S: put(S, 'AJ', dict(S['AJ'], n=-1))),
    ('G-TEST-LINE', 'OPEN_TRAILS at the banked line: the keystone test ruled, b375`s item closed', lambda S: test_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('closes under this clause', 'closes'))),
    ('G-SEQUENCE-LINE', 'OPEN_TRAILS at the banked line: the synthesis sequence`s form', lambda S: seq_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('the first is b611', 'the first is b612'))),
    ('G-ADDENDUM-BANKED', 'the keystones re-read now by the four matchers against the addendum: every line marked, the counts as banked', lambda S: add_ok(S),
     lambda S: put(S, 'add_now', S['add_now'] + [('x.md', 1, ['A1'])])),
    ('G-CENSUS-BANKED', 'the census bank and its json: banked before the census edition, its six parts and three scores', lambda S: census_banked(S),
     lambda S: put(S, 'CJ', dict(S['CJ'], at='9999'))),
    ('G-CENSUS-PLACED-NOW', 'REGISTRY re-read now at 7055f04: every row placed as banked, none unplaced', lambda S: placed_now(S),
     lambda S: put(S, 'placed_now', S['placed_now'][:-1] + [(S['placed_now'][-1][0], None)])),
    ('G-KEYSTONELESS-NOW', 'the tiers re-read now: the clusters with documents and no keystone as banked', lambda S: kl_now(S),
     lambda S: put(S, 'kl_now', S['kl_now'] + ['2A'])),
    ('G-TAGS-READ-BACK', 'every banked current tag`s remote peel against the clone`s peel now', lambda S: tags_now(S),
     lambda S: put(S, 'tags_now', dict(S['tags_now'], **{'SIDE-kernel': '0' * 40}))),
    ('G-CURRENT-UNEDITED', 'the census`s current version, SPIRAL_MAP, the taxonomy, the sieve v0.4 and the monograph v5.17 on disk and at HEAD against 7055f04',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{CEN: (S['currents'][CEN][0] + b'x', S['currents'][CEN][1], S['currents'][CEN][2])}))),
    ('G-CENSUS-CARRIES', 'v0.3 at its banked sha: every non-blank current line carried verbatim', lambda S: census_carries(S),
     lambda S: _mut(S, 'cd', S['EC'].get('bm', 0) + 40 if S['EC'] else 0, ' x')),
    ('G-CENSUS-VERSION-LINE', 'v0.3`s version line on :10 above v0.1`s register line, the head above it unchanged', lambda S: census_version(S),
     lambda S: put(S, 'cd', [l.replace('*v0.3, 2026-10-03 --', '*v0.3 --') for l in S['cd']])),
    ('G-CENSUS-TEST-RULED', 'v0.3`s §0 ruled above the current §0, carried whole, its history line directly beneath', lambda S: census_test(S),
     lambda S: put(S, 'cd', [l.replace('*History line, v0.3, 2026-10-03', '*History line, v0.3') for l in S['cd']])),
    ('G-CENSUS-ROWS', 'v0.3`s body: the 23 rows on their banked lines, each citing every REGISTRY line of its rows', lambda S: census_rows(S),
     lambda S: put(S, 'cd', [l.replace('(:83)', '(:84)', 1) for l in S['cd']])),
    ('G-CENSUS-NOKEY', 'v0.3`s §2 against the bank: the clusters with documents and no keystone, in order', lambda S: census_nokey(S),
     lambda S: put(S, 'cd', [l.replace('- **R07 ', '- **R7 ') for l in S['cd']])),
    ('G-CENSUS-BACKMATTER', 'v0.3`s back matter: its sections in order, no blank Status cell, the moved body verbatim', lambda S: census_bm(S),
     lambda S: put(S, 'cd', [l.replace('### History lines', '### History') for l in S['cd']])),
    ('G-CENSUS-BANK', 'the census`s diff bank: its offset head once, the final sha, the rows, the counts, the landing line', lambda S: cbank_ok(S),
     lambda S: put(S, 'cbank', S['cbank'].replace('THE CENSUS LANDS', 'THE CENSUS'))),
    ('G-CENSUS-REPIN', 'the census`s re-pin bank against the final file', lambda S: _repin_ok(S['crepin'], 20) and S['EC'].get('sha256', '#')[:16] in S['crepin'],
     lambda S: put(S, 'crepin', S['crepin'].replace('RE-PIN : ', 'RE-PIN : 1'))),
    ('G-H28A-CENSUS-SCORED', 'H28a for v0.3 in its bank, the scores and the desk', lambda S: _hs(S, 'H28a', 'H28a-CENSUS', 'HC', 'cbank', 'HOLDS')
     and S['HC'].get('vacuous_a') is True and 'VACUOUS on its letter' in S['cbank'], lambda S: _sc(S, 'H28a-CENSUS')),
    ('G-H28B-CENSUS-SCORED', 'the bodies of the current version and v0.3 counted afresh, the bound and the strict figure recomputed', lambda S: h28b_census(S),
     lambda S: put(S, 'EC', dict(S['EC'], n_body=-1))),
    ('G-H28C-CENSUS-SCORED', 'the scanner run afresh on v0.3 and its body read for the ceiling', lambda S: h28c_census(S),
     lambda S: put(S, 'cscan_now', S['cscan_now'].replace('VERDICT          : CLEAN', 'VERDICT          : NOT CLEAN'))),
    ('G-CENSUS-COMMITTED-ALONE', 'PLACE-papers` log since 7055f04: v0.3 in one commit of its own, on disk as committed', lambda S: _alone(S, CEN3, 'b610 (R220)(4): ' + CEN3)
     and bool(S['cd_head']) and S['cd_head'] == S['cd_disk'], lambda S: put(S, 'pp_files', {h: (f + ['FINDINGS.md'] if CEN3 in f else f) for h, f in S['pp_files'].items()})),
    ('G-SPIRAL-CARRIES', 'v0.7 at its banked sha: every non-blank v0.6 line carried verbatim or as its recorded correction', lambda S: spiral_carries(S),
     lambda S: _mut(S, 'sd', 20, ' x')),
    ('G-SPIRAL-VERSION-LINE', 'v0.7`s version line on :18 above v0.6`s, the head above it unchanged', lambda S: spiral_version(S),
     lambda S: put(S, 'sd', [l.replace('**v0.7 — 2026-10-03**', '**v0.7**') for l in S['sd']])),
    ('G-SPIRAL-POINTERS', 'v0.7`s census rows: one line per cluster on its banked line, as recomputed from the census bank', lambda S: spiral_pointers(S),
     lambda S: put(S, 'sd', [l.replace('rows R01 (', 'rows R02 (') for l in S['sd']])),
    ('G-SPIRAL-CORRECTIONS', 'v0.7`s four corrected lines: each v0.6 line with its old wording replaced, nothing else', lambda S: spiral_fixes(S),
     lambda S: _mut(S, 'sd', (S['ES'].get('fixes') or [{}])[0].get('at', 0), ' x')),
    ('G-SPIRAL-BACKMATTER', 'v0.7`s back matter: its sections in order, the stem record marked, no blank Status cell', lambda S: spiral_bm(S),
     lambda S: put(S, 'sd', [l.replace('### Stem corrections', '### Stems') for l in S['sd']])),
    ('G-SPIRAL-BANK', 'SPIRAL_MAP`s diff bank: its offset head once, the final sha, the corrections, the counts, the landing line', lambda S: sbank_ok(S),
     lambda S: put(S, 'sbank', S['sbank'].replace('THE MAP LANDS', 'THE MAP'))),
    ('G-SPIRAL-REPIN', 'SPIRAL_MAP`s re-pin bank against the final file', lambda S: _repin_ok(S['srepin'], 15) and S['ES'].get('sha256', '#')[:16] in S['srepin'],
     lambda S: put(S, 'srepin', S['srepin'].replace('RE-PIN : ', 'RE-PIN : 1'))),
    ('G-H28A-SPIRAL-SCORED', 'H28a for v0.7 in its bank, the scores and the desk', lambda S: _hs(S, 'H28a', 'H28a-SPIRAL', 'HS', 'sbank', 'HOLDS')
     and S['HS'].get('vacuous_a') is True and 'VACUOUS on its letter' in S['sbank'], lambda S: _sc(S, 'H28a-SPIRAL')),
    ('G-H28B-SPIRAL-SCORED', 'the bodies of v0.6 and v0.7 counted afresh, the bound recomputed', lambda S: h28b_spiral(S),
     lambda S: put(S, 'ES', dict(S['ES'], n_body=-1))),
    ('G-H28C-SPIRAL-SCORED', 'the scanner run afresh on v0.7 and its body read for the ceiling, the carried hits apart', lambda S: h28c_spiral(S),
     lambda S: put(S, 'sscan_now', S['sscan_now'].replace('VERDICT          : CLEAN', 'VERDICT          : NOT CLEAN'))),
    ('G-SPIRAL-COMMITTED-ALONE', 'PLACE-papers` log since 7055f04: v0.7 in one commit of its own, on disk as committed', lambda S: _alone(S, SPI7, 'b610 (R220)(4): ' + SPI7)
     and bool(S['sd_head']) and S['sd_head'] == S['sd_disk'], lambda S: put(S, 'pp_files', {h: (f + ['FINDINGS.md'] if SPI7 in f else f) for h, f in S['pp_files'].items()})),
    ('G-H44A-SCORED', 'H44a recomputed from REGISTRY now, against the bank, the scores and the desk', lambda S: h44_ok(S, 'H44a'), lambda S: _sc(S, 'H44a')),
    ('G-H44B-SCORED', 'H44b recomputed from the tiers now, against the bank, the scores and the desk', lambda S: h44_ok(S, 'H44b'), lambda S: _sc(S, 'H44b')),
    ('G-H44C-SCORED', 'H44c recomputed from the clones` peels now, against the bank, the scores and the desk', lambda S: h44_ok(S, 'H44c'), lambda S: _sc(S, 'H44c')),
    ('G-H44D-SCORED', 'H44d from both editions` H28 banks, the scores and the desk', lambda S: h44_ok(S, 'H44d'), lambda S: _sc(S, 'H44d')),
    ('G-PAGES-BANKED', 'both pages at HEAD and their banks: each re-emitted from its probe, unchanged pages unwritten', lambda S: pages_banked(S),
     lambda S: put(S, 'PZ', dict(S['PZ'], sha256='0'))),
    ('G-PAGES-COMMITTED-ALONE', 'PLACE-papers` log since 7055f04: a changed page in one commit of its own, an unchanged page in none', lambda S: pages_alone(S),
     lambda S: put(S, 'pp_files', dict(S['pp_files'], deadbee=[PAGE]))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b602`s list and v0.20 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b603`s list and v0.21 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank after the editions: both page arms and the frozen control', lambda S: 'PAGE ARMS PASSING : 2 of 2' in S['arms_c2']
     and ('%s PASSING : 2 of 2' % CONTROL_ARM) in S['arms_c2'], lambda S: put(S, 'arms_c2', S['arms_c2'].replace('PASSING : 2 of 2', 'PASSING : 1 of 2'))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD,
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and 'R-1 to R-8' in trail(S) and 'R-1 to R-3' in trail(S) and 'For the author:' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('Resolved by the seat, for the author’s strike', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b611, the synthesis act for the census’s opening-listed cluster' in trail(S)
     and 'W-ORD-QUANTIFIER-COLUMN' in trail(S), lambda S: put(S, 'ot', S['ot'].replace('b611, the synthesis act', 'x'))),
    ('G-SEQUENCE-NAMED', 'this act`s trail record: one act per cluster with no keystone, numbered from b611 in the census`s order', lambda S: seq_named(S),
     lambda S: put(S, 'ot', S['ot'].replace('- **b611** --', '- **b612** --'))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, lv`s HEAD and status, the explicit-formula checkout on main and clean with no new tag, the trial branch',
     lambda S: all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['kcur'] == 'main' and S['kdirty'] == ''
     and 'v0.21' in S['ktags'] and 'v0.22' not in S['ktags'] and S['trial'] == 'f22ff35' and S['lv_head'].startswith('2f71068a')
     and S['lv_dirty'] == '', lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-kernel': '0'}))),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('36352a0', '36352a0', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b610_record.py'): S['tooltext'].get(os.path.join(T, 'b610_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                              if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces'][1] and S['faces'][0] == S['faces'][1],
     lambda S: put(S, 'faces', (S['faces'][0] + b'x', S['faces'][1]))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-REGISTRY-UNTOUCHED', 'REGISTRY.md against its pre-act blob', lambda S: S['registry'][1] and S['registry'][0] == S['registry'][1],
     lambda S: put(S, 'registry', (S['registry'][0] + b'x', S['registry'][1]))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md on disk and at HEAD against 7055f04', lambda S: bool(S['errata'][1]) and S['errata'][0] == S['errata'][1] == S['errata'][2],
     lambda S: put(S, 'errata', (S['errata'][0] + b'x', S['errata'][1], S['errata'][2]))),
    ('G-KEYSTONES-SCOPE', 'PLACE-papers` phase, day1 and outputs paths, tracked and untracked: the census edition alone', lambda S: S['keystone_changes'] == [CEN3],
     lambda S: put(S, 'keystone_changes', sorted([CEN3, CEN]))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at d121b88f, by blob id', lambda S: S['prior_bad'] == []
     and S['prior_n'] > 6000, lambda S: put(S, 'prior_bad', ['data/b609_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == sorted(
        ['FINDINGS.md', 'OPEN_TRAILS.md', CEN3, SPI7] + [p for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])) if z.get('changed')]),
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
                                                                          and "startswith('b610')" in S['suite'] and "data/b610_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b610')", ''))),
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
    rec('b610 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('PRE-SEAL (R202)(3)' if PRERUN else 'POST-PUSH' if pushed else 'PRE-PUSH'))
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
        out = os.path.join(D, 'b610_arms_prerun.txt')
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b610_checks_postpush.txt' if pushed else 'b610_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    if not (RERUN or PRERUN):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b610_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
