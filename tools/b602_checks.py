# -*- coding: utf-8 -*-
"""b602_checks.py -- THE SUITE OF b602, UNDER (R212): THE AUDIT FILE REPAIRED AT v0.19.1; THE SIGN OF λ_1 AT T0; (E3)'S COMPILED
WINDOW AT DETECTION-REGION.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>` or `--prerun`; it writes data/b602_checks.txt before the push and
### data/b602_checks_postpush.txt after it. ### `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the
### face is sealed, no table regenerated, its counts written to data/b602_arms_prerun.txt and nothing else.
### ### The harness is b568's to b601's, carried; the arms are b602's. The control arm is the frozen one of (R207)(2). Every
### predicate reading Lean output or a hard-wrapped head reads it whitespace-joined (b601 (a), (d)); every E0 read is held to the
### tag by blob (b601 (c)).
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
FACE = os.path.join(D, 'b602_registration_2026-10-02.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PRE = dict(relay='97485547', pp='ca841ca', gs='3528bcf', ker='5fc0c87')
TAG, POINT = 'v0.20', 'v0.19.1'
BRANCH = 'sign-window-b602'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b', 'product-b600': '1dd5cd7',
        'doubling-keiper-b601': '5fc0c87'}
OWN = ['AxiomCheckKeiperSign.lean', 'AxiomCheckPlateauRamp.lean', 'SIDEExplicitFormula/KeiperSign.lean',
       'SIDEExplicitFormula/SaltCheckKeiperSign.lean', 'SIDEExplicitFormula/Schema/PlateauRamp.lean',
       'SIDEExplicitFormula/Schema/SaltCheckPlateauRamp.lean']
MODS = OWN[2:]
KEYS = ('sign', 'ssign', 'win', 'swin')
SN, WN = 'SIDEExplicitFormula.KeiperSign.', 'SIDEExplicitFormula.Schema.PlateauRamp.'
STD3 = {'propext', 'Classical.choice', 'Quot.sound'}
BALPOS = 'phase1.5/spectral/BALANCE_AND_POSITIVITY_v0_9_5.md'
TFAS = 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md'
STEPZERO = '7a60bad2'
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/5dce8424-ec16-4701-8f42-69078426fd40/scratchpad'


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b602')
            and 'data/b602_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
            ch |= set(untracked(PP, 'phase1.5', 'phase2'))
        res += ['%s/%s' % (name, x) for x in ch]
    return sorted(res)


def lines_of(b):
    l = cr0(b).decode('utf-8', 'replace').split(NL)
    return l[:-1] if l and l[-1] == '' else l


def sources():
    import b602_record as REC
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b602_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b602_') and f.endswith('.py'))
    tagc = gs(KER, 'rev-parse', '--verify', '-q', TAG + '^{commit}')
    pointc = gs(KER, 'rev-parse', '--verify', '-q', POINT + '^{commit}')
    S = dict(
        REC=REC, face=face, ferry=rd('b602_ferry.txt'), scan=rd('b602_ferry_scan.txt'), cens=rd('b602_census_stepzero.txt'),
        fcens=rd('b602_faces_census_stepzero.txt'), pins0=rd('b602_pins_stepzero.txt'), procs=rd('b602_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b601_closing.txt'), reads=rd('b602_reads.txt'), branches=rd('b602_branches.txt'), answers=rd('b602_author_answers.txt'),
        prerun=rd('b602_arms_prerun.txt'), bounds=rd('b602_bounds.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))))
              for f in ('b601_checks.py', 'test_chain_page_b596.py', 'chain_page.py', 'e0_rule.py', 'g_chain_page.py', 'push_gated.sh')},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        readme=(cr0(raw(os.path.join(PP, 'README.md'))), cr0(blob(PP, PRE['pp'] + ':README.md'))),
        registry=(cr0(raw(os.path.join(PP, 'REGISTRY.md'))), cr0(blob(PP, PRE['pp'] + ':REGISTRY.md'))),
        faces=(cr0(raw(os.path.join(PP, 'FACES_LEDGER.md'))), cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md'))),
        errata=(cr0(raw(os.path.join(PP, 'ERRATA.md'))), cr0(blob(PP, PRE['pp'] + ':ERRATA.md'))),
        pages={p: (cr0(raw(os.path.join(PP, p))), cr0(blob(PP, PRE['pp'] + ':' + p)), cr0(blob(PP, 'HEAD:' + p))) for p in (PAGE, DIR_PAGE)},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        corr_pre=cr0(blob(GS, PRE['gs'] + ':CORRESPONDENCE.md')), corr_now=cr0(raw(os.path.join(GS, 'CORRESPONDENCE.md'))),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain', '--untracked-files=no'),
        kmain=gs(KER, 'rev-parse', 'main'), ktag=tagc, kpoint=pointc, kbranch=gs(KER, 'rev-parse', '--verify', '-q', BRANCH),
        kanc=(subprocess.run(['git', '-C', KER, 'merge-base', '--is-ancestor', POINT, TAG]).returncode == 0
              and subprocess.run(['git', '-C', KER, 'merge-base', '--is-ancestor', PRE['ker'], POINT]).returncode == 0) if tagc and pointc else False,
        kfiles=sorted(x for x in gs(KER, 'diff', '--name-only', POINT, TAG).split(NL) if x.strip()) if tagc and pointc else [],
        kmerges=[x for x in gs(KER, 'rev-list', '--merges', '%s..%s' % (PRE['ker'], TAG)).split(NL) if x.strip()] if tagc else ['none'],
        ksrc={f: (blob(KER, '%s:%s' % (TAG, f)) or b'').decode('utf-8', 'replace') for f in OWN} if tagc else {},
        kpush=rd('b602_kernel_push_out.txt'), ppush=rd('b602_point_push_out.txt'), bpush=rd('b602_branch_push_out.txt'),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b601*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b602_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b602_mustnotexist.txt')), table_changed=None,
        fj=jl('b602_findings.json'), tj=jl('b602_trail.json'), sc=jl('b602_scores.json'), desk=rd('b602_desk_notes.txt'),
        rl=jl('b602_record_lines.json'), pdiff=jl('b602_point_diff.json'), srr=rd('b602_salt_rerun.txt'), etags=jl('b602_entry_tags.json'),
        st={k: jl('b602_statements_%s.json' % k) for k in ('sign', 'win')}, stxt={k: rd('b602_statements_%s.txt' % k) for k in ('sign', 'win')},
        pr={k: jl('b602_prints_%s.json' % k) for k in ('sign', 'win')},
        e0={k: jl('b602_e0_%s.json' % k) for k in KEYS}, gp=jl('b602_grep.json'), br=jl('b602_bearing.json'), rel=jl('b602_relation.json'),
        builds={k: rd('b602_build_%s.txt' % k) for k in KEYS + ('axsign', 'axwin', 'axpoint')},
        PZ=jl('b602_page_zeta.json'), PX=jl('b602_page_chi.json'), arms_c2=rd('b602_page_arms_c2.txt'),
        nodes_z=rd('b602_nodes_zeta.txt'), nodes_x=rd('b602_nodes_chi.txt'), nodes601=rd('b601_nodes_zeta.txt'), nodes596x=rd('b596_nodes_chi.txt'),
    )
    S['e0_blob'] = {k: (gs(KER, 'rev-parse', '%s:%s' % (S['e0'][k].get('tip', '#'), S['e0'][k].get('file', '#'))),
                        gs(KER, 'rev-parse', '%s:%s' % (TAG, S['e0'][k].get('file', '#')))) for k in KEYS} if tagc else {}
    S['written'] = written_files(lock_epoch or 0)
    S['globs'] = wl_globs(face)
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
    S['bear_now'] = {(r.get('path'), r.get('line')): (lines_of(blob(PP, 'HEAD:' + r.get('path', 'x')) or b'') or [''] * 9999)[r.get('line', 1) - 1]
                     for r in S['br'].get('rows', [])} if S['br'] else {}
    S.update(extra_sources(S))
    return S


def extra_sources(S):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    X = {}
    X['gcp_zeta'] = GCP.arm(os.path.join(D, 'b602_nodes_zeta.txt'), os.path.join(SP, '_b602_gcp'), os.path.join(D, 'b602_probe_out.txt')) \
        if os.path.exists(os.path.join(D, 'b602_probe_out.txt')) else \
        GCP.arm(os.path.join(D, 'b601_nodes_zeta.txt'), os.path.join(SP, '_b602_gcp'), os.path.join(D, 'b601_probe_out.txt'))
    X['gcp_chi'] = GCP.arm(os.path.join(D, 'b602_nodes_chi.txt'), os.path.join(SP, '_b602_gcp'), os.path.join(D, 'b602_chi_probe_out.txt')) \
        if os.path.exists(os.path.join(D, 'b602_chi_probe_out.txt')) else \
        GCP.arm(os.path.join(D, 'b596_nodes_chi.txt'), os.path.join(SP, '_b602_gcp'), os.path.join(D, 'b596_chi_probe_out.txt'))
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


def flat(t):
    return ' '.join((t or '').split())


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
    ls = S['rl'].get('lines', [])
    if len(ls) != 2:
        return False
    a = fline(S, ls[0]['line'])
    return a.startswith(ls[0]['head']) and '(:6972)' in a and 'b601 AT ITS WEIGHT' in a and '5fc0c87' in a and '80 of 81' in a \
        and 'v0.19.1' in a and ls[0]['line'] > 6990


def reading_ok(S):
    ls = S['rl'].get('lines', [])
    if len(ls) != 2:
        return False
    a = fline(S, ls[1]['line'])
    return a.startswith(ls[1]['head']) and 'THE READING STANDS' in a and 'is not struck' in a and '(:6970)' in a.replace('at :6970', '(:6970)') \
        and fline(S, 6970).startswith('*Appended 2026-10-02 by b601 beside b600’s entry (:6950)') and ls[1]['line'] > ls[0]['line']


def sieve_ok(S):
    sv = S['rl'].get('sieve') or {}
    a = oline(S, sv.get('line'))
    return a.startswith(S['REC'].SIEVE_HEAD) and 'THE_FINDINGS_AS_THEY_STAND' in a and 'sieve table by cluster' in a \
        and 'after b603' in a and 'not started' in a and (sv.get('line') or 0) > 12392


def work_order_printed(S):
    wo = oline(S, 12170)
    return wo.startswith('*Appended 2026-10-02 by b591 to the DETECTION-REGION re-scope') and ('    :12170  ' + wo) in S['reads'] \
        and ('    ' + wo) in S['stxt']['win'] and 'no new price is named' in wo


def statements_ok(S, keys):
    for k in keys:
        it = S['st'][k].get('items') or []
        if not (len(it) == len(S['REC'].ITEMS[k]) and all(i['in_statement'] and i['declared'] for i in it)
                and 'EVERY ITEM OF THE STATEMENT CARRIED BY A DECLARATION' in S['stxt'][k]):
            return False
    return True


def strip_lean(t):
    t = re.sub(r'/-[\s\S]*?-/', '', t)
    return NL.join(l.split('--', 1)[0] for l in t.split(NL))


def house_form(S):
    src = S['ksrc']
    if sorted(src) != sorted(OWN) or not all(src.values()):
        return False
    for f in MODS:
        t = src[f]
        head = flat(t.split('-/')[0])
        if not (t.startswith('/-\nSIDE-explicit-formula -- %s\n' % f) and "THIS PROGRAMME'S WORK (act b602" in head
                and '`theorem`, never `lemma`' in head and 'NOT VENDORED' in head):
            return False
        if re.search(r'^\s*lemma\s', t, re.M) or re.search(r'\bsorry\b', strip_lean(t)) or 'native_decide' in strip_lean(t) \
                or re.search(r'^\s*axiom\s', strip_lean(t), re.M):
            return False
    return src['AxiomCheckKeiperSign.lean'].startswith('import SIDEExplicitFormula.KeiperSign\nimport SIDEExplicitFormula.SaltCheckKeiperSign\n') \
        and src['AxiomCheckPlateauRamp.lean'].startswith('import SIDEExplicitFormula.Schema.PlateauRamp\nimport SIDEExplicitFormula.Schema.SaltCheckPlateauRamp\n')


def rows_all(S):
    return {n: r for e in S['e0'].values() for n, r in (e.get('rows') or {}).items()}


def prints_ok(S):
    for k, keys in (('sign', ('sign', 'ssign')), ('win', ('win', 'swin'))):
        p = S['pr'][k]
        ax = p.get('axioms') or {}
        decl = [n for kk in keys for n in (S['e0'][kk].get('rows') or {})]
        if not (ax and decl and all(n in ax for n in decl) and all(set(v) <= STD3 for v in ax.values()) and not p.get('sorry')
                and p.get('errors') == 0 and p.get('std3') is True and 'rc=0' in (p.get('exit') or '')):
            return False
    return True


def e0_ok(S):
    r = rows_all(S)
    want = {SN + 'liCoeff_one_pos': 'DERIVES', SN + 'threshold_lt_gamma': 'DERIVES', SN + 'liCoeff_one_pos_iff': 'DERIVES',
            WN + 'plateauRampWindow_of': 'INTERFACES', WN + 'box_paperFT': 'DERIVES', WN + 'window_even': 'DERIVES',
            WN + 'window_hasCompactSupport': 'DERIVES'}
    return all(S['e0'][k].get('gate') is True and S['e0'][k].get('same_file') is True
               and re.fullmatch(r'[0-9a-f]{40}', S['e0_blob'].get(k, ('', '#'))[0]) is not None
               and S['e0_blob'].get(k, ('', '#'))[0] == S['e0_blob'].get(k, ('', '#'))[1] for k in KEYS) \
        and all(r.get(n, {}).get('grade') == g_ for n, g_ in want.items())


SALT = [SN + 'SaltCheck.' + n for n in ('coarse_lower_insufficient', 'liCoeff_one_lt_tenth', 'liCoeff_one_pos_holds')] + \
       [WN + 'SaltCheck.' + n for n in ('box_transform_zero_at_pi', 'box_transform_ne_zero_at_half_pi', 'window_even_compact_at_seven')]


def salt_ok(S):
    r = rows_all(S)
    txt = (S['pr']['sign'].get('text') or '') + NL + (S['pr']['win'].get('text') or '')
    return all(r.get(n, {}).get('std3') and r.get(n, {}).get('grade') == 'DERIVES' for n in SALT) and all((n + ' :') in txt for n in SALT)


def sign_ok(S):
    r = rows_all(S).get(SN + 'liCoeff_one_pos', {})
    txt = S['pr']['sign'].get('text') or ''
    chk = flat(txt.split(SN + 'liCoeff_one_pos : ')[-1].split(SN)[0]) if (SN + 'liCoeff_one_pos : ') in txt else ''
    return r.get('grade') == 'DERIVES' and r.get('std3') is True and 'no hypothesis binder' in (r.get('why') or '') \
        and chk.startswith('0 < SIDEExplicitFormula.LiWeil.LiCoeff 1')


def window_carried_ok(S):
    r = rows_all(S).get(WN + 'plateauRampWindow_of', {})
    t = S['ksrc'].get('SIDEExplicitFormula/Schema/PlateauRamp.lean', '')
    return r.get('grade') == 'INTERFACES' and 'hP : WindowObligations' in flat(r.get('head') or '') \
        and 'structure WindowObligations (W h : ℝ) : Prop where' in t and 'conv_step : ConvStep W h' in t and 'smooth : Smooth4 W h' in t \
        and 'def ConvStep (W h : ℝ) : Prop :=' in t and 'def Smooth4 (W h : ℝ) : Prop :=' in t


def relation_ok(S):
    rel = S['rel']
    r = rows_all(S).get(WN + 'epstein_ef_at_window', {})
    return rel.get('word') in ('DISCHARGES-PART', 'INDEPENDENT', 'NEEDS-IT') and rel.get('concl_ep') == [] \
        and rel.get('with_ep') == ['epstein_ef_at_window'] and r.get('std3') is True and len(rel.get('reason') or '') > 200


def point_ok(S):
    p = S['pdiff']
    return p.get('exact') is True and p.get('files') == ['AxiomCheckKeiper.lean'] and len(p.get('added') or []) == 2 \
        and p.get('removed') == [] and p.get('rev') == POINT


def point_pushed_ok(S):
    c = S['kpoint']
    return bool(c) and ('push_gated: tag %s peeled local %s remote %s' % (POINT, c, c)) in S['ppush'] \
        and 'push_gated: DONE -- main and 1 tag(s) pushed and read back' in S['ppush'] and S['kanc']


def bounds_ok(S):
    b = S['bounds']
    return 'THE INDEX CHOSEN: 15' in b and 'H_15 = 1195757/360360' in b and 'Real.eulerMascheroniSeq_lt_eulerMascheroniConstant' in b \
        and 'Real.log_two_lt_d9' in b and 'Real.pi_lt_d4' in b and 'Real.exp_one_gt_d9' in b and b.count('    n = ') == 25


def grep_ok(S):
    gp = S['gp']
    rows = gp.get('rows') or []
    return gp.get('bad') == [] and bool(rows) and all((gp.get('controls') or {}).values()) and len(gp.get('controls') or {}) == 4 \
        and any(r['cls'] == 'OWN' and r['name'] == 'liCoeff_one_pos' for r in rows) \
        and any(r['cls'] == 'OWN' and r['name'] == 'plateauRampWindow_of' for r in rows) \
        and any(r['name'] == 'n_one_binding_instance' and r['cls'] == 'READ' and r['reading'] for r in rows) and len(gp.get('kernels') or []) > 40


def tagged_ok(S):
    t = S['ktag']
    return bool(t) and S['kmain'] == t and S['kanc'] and ('push_gated: main read back at the remote: %s' % t) in S['kpush'] \
        and ('push_gated: tag %s peeled local %s remote %s' % (TAG, t, t)) in S['kpush'] and 'push_gated: DONE -- main and 1 tag(s) pushed and read back' in S['kpush']


def kfiles_ok(S):
    return S['kfiles'] == sorted(OWN) and S['kmerges'] == []


def branch_ok(S):
    t = S['ktag']
    return bool(t) and S['kbranch'] == t and ('%s local %s remote %s' % (BRANCH, t, t)) in S['bpush']


def hold_ok(S):
    for k in KEYS + ('axsign', 'axwin', 'axpoint'):
        m = re.search(r'free MB before: (\d+)', S['builds'][k])
        if not (m and int(m.group(1)) >= 2560 and re.search(r'^### EXIT rc=0 ', S['builds'][k], re.M)):
            return False
    return (S['PZ'].get('free_mb_before') or 0) >= 2560 and (S['PX'].get('free_mb_before') or 0) >= 2560


def page_ok(S, k):
    z = S['PZ'] if k == 'zeta' else S['PX']
    nodes = S['REC'].SIGN_NODES if k == 'zeta' else S['REC'].WIN_NODES
    new = {x['name']: x for x in z.get('new') or []}
    a, b, c = S['pages'][PAGE if k == 'zeta' else DIR_PAGE]
    key = SN + 'liCoeff_one_pos' if k == 'zeta' else WN + 'plateauRampWindow_of'
    want = 'DERIVES' if k == 'zeta' else 'INTERFACES'
    return z.get('rc') == 0 and z.get('changed') is True and sorted(new) == sorted(nodes) and new.get(key, {}).get('grade') == want \
        and bool(a) and a == c and a != b and hashlib.sha256(c).hexdigest() == z.get('sha256') \
        and all(('`%s`' % n) in c.decode('utf-8') for n in nodes)


def pages_alone(S):
    out = []
    for p in (PAGE, DIR_PAGE):
        c = [h for h, f in S['pp_files'].items() if p in f]
        out.append(len(c) == 1 and S['pp_files'][c[0]] == [p] and dict(S['pp_log'])[c[0]].startswith('b602 (R212)(5): ' + p))
    return all(out)


def node_lists_ok(S):
    R = S['REC']
    z, oz = S['nodes_z'].rstrip(NL).split(NL), S['nodes601'].rstrip(NL).split(NL)
    x, ox = S['nodes_x'].rstrip(NL).split(NL), S['nodes596x'].rstrip(NL).split(NL)
    if '# pin: v0.20' not in z or '# pin: v0.19' in z or z[-1] != oz[-1] or '# pin: v0.20' not in x or '# pin: v0.17' in x:
        return False
    i = z.index(R.SIGN_ANCHOR) if R.SIGN_ANCHOR in z else -1
    dets = [j for j, l in enumerate(x) if l.startswith(R.DET_ANCHOR_PREFIX)]
    return i > 0 and z[i + 1:i + 1 + len(R.SIGN_ADD)] == R.SIGN_ADD and len(dets) == 1 and x[dets[0] + 1:dets[0] + 1 + len(R.WIN_ADD)] == R.WIN_ADD \
        and all((('# pin: v0.20' if l == '# pin: v0.19' else l) in z) for l in oz if l.strip()) \
        and all((('# pin: v0.20' if l == '# pin: v0.17' else l) in x) for l in ox if l.strip())


def bearing_ok(S):
    rows = S['br'].get('rows') or []
    return [(r['path'], r['line']) for r in rows] == [(BALPOS, 398), (TFAS, 497)] and all(r['found'] for r in rows) \
        and all(S['bear_now'].get((r['path'], r['line'])) == r['sentence'] for r in rows) and all(len(r['reading']) > 200 for r in rows) \
        and [r['component'] for r in rows] == ['sign', 'window']


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 26]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') and fline(S, e).startswith('## The sign of λ₁ at T0 from Mathlib’s γ and π bounds') \
        and '**The point tag**' in tail and '**The sign of λ₁**' in tail and '**(E3)’s window**' in tail and '**Its bearing**' in tail \
        and '**Read in mutual light**' in tail and 'strengthens' in tail and (S['ktag'][:7] or '#') in tail and 'n_one_binding_instance' in tail


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


def _h36(S, k):
    v = S['sc'].get(k)
    return bool(v) and v[0] in ('HOLDS', 'REFUTED') and ('(%s)' % k.upper()) in S['desk']


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R212) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b601`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b601' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b602 -- x'])),
    ('G-R212-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R212) END' in S['ferry'] and S['ot'].count('**(R212) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R212) ratified', '(R212) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in (
        'AxiomCheckKeiper.lean @ 5fc0c878', 'tools/b601_checks.py @', 'SIDEExplicitFormula/Keiper.lean @ 5fc0c878',
        'Mathlib/NumberTheory/Harmonic/EulerMascheroni.lean @ de5ce8a9', 'Mathlib/Analysis/Real/Pi/Bounds.lean @ de5ce8a9',
        'Mathlib/Analysis/Complex/ExponentialBounds.lean @ de5ce8a9', 'OPEN_TRAILS.md @ ca841ca', 'FINDINGS.md @ ca841ca',
        'SIDEExplicitFormula/Schema/Detector.lean @ c404e727', 'SIDEExplicitFormula/Schema/Epstein.lean @ c404e727',
        'SIDELvConservation/CouplingsAtPhi.lean @ 2f71068a', THE_PAGE_AT, 'data/b601_closing_push_out.txt @',
        "chain_page.py`s hold: ['HOLD_MB = 2560']"))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-WORK-ORDER-PRINTED', 'OPEN_TRAILS :12170 against the reads and statements banks: the work-order printed whole', lambda S: work_order_printed(S),
     lambda S: put(S, 'reads', S['reads'].replace('    :12170  ' + oline(S, 12170), '    :12170  ' + oline(S, 12170)[:400]))),
    ('G-ANSWERS-BANKED', 'the act`s answers bank: every prompt with its options and recommended mark verbatim, or none',
     lambda S: S['answers'].startswith('### b602 -- THE AUTHOR`S ANSWERS') and S['answers'].count('### PROMPT ') == S['answers'].count('\nRESULT ')
     and (S['answers'].count('### PROMPT ') > 0 or '### NONE: no prompt was put' in S['answers']),
     lambda S: put(S, 'answers', S['answers'].replace('### b602 -- THE AUTHOR', '### b6O2 -- THE AUTHOR', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay 7a60bad2`s files', lambda S: S['pushout'][0] == ['data/b601_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/b601_closing_push_out.txt', 'x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b601') == 4, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b601'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'doubling-keiper-b601': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80 and every PLACE-papers read at ba5f0ea, run afresh through the test`s control()',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(S['ctl'][0], ok=False)] + S['ctl'][1:])),
    ('G-INSTRUMENTS-UNEDITED', 'b601`s sealed suite, the control`s test file, the generator, its arm, the E0 rule and the push gate against 97485547',
     lambda S: all(bool(a) and a == b for a, b in S['inst'].values()) and len(S['inst']) == 6,
     lambda S: put(S, 'inst', dict(S['inst'], **{'e0_rule.py': (S['inst']['e0_rule.py'][0], (S['inst']['e0_rule.py'][1] or b'') + b'x')}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b601`s weight, addressed to its entry', lambda S: weight_ok(S),
     lambda S: put(S, 'rl', dict(S['rl'], lines=(S['rl'].get('lines') or [])[1:]))),
    ('G-READING-STANDS', 'FINDINGS at the banked line: the (R211)(2) reading recorded as standing, addressed to :6970', lambda S: reading_ok(S),
     lambda S: put(S, 'find', S['find'].replace('is not struck', 'is struck'))),
    ('G-SIEVE-ENTERED', 'OPEN_TRAILS at the banked line: the sieve-table edition entered after b603 as the author`s word', lambda S: sieve_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('sieve table by cluster', 'table'))),
    ('G-POINT-TAG-TWO-LINES', 'the point tag`s diff bank: v0.19..v0.19.1, one file, the ruled two #check lines, nothing removed', lambda S: point_ok(S),
     lambda S: put(S, 'pdiff', dict(S['pdiff'], removed=['x']))),
    ('G-POINT-TAG-PUSHED', 'the point tag`s push capture: v0.19.1 peeled at the remote, v0.19 its ancestor', lambda S: point_pushed_ok(S),
     lambda S: put(S, 'ppush', S['ppush'].replace('peeled local', 'local'))),
    ('G-SALT-CHECK-AT-POINT', 'the re-run bank: b601`s G-SALT-CHECK at v0.19.1, counted', lambda S: 'G-SALT-CHECK AT v0.19.1 : PASSES ; COUNTED 1 OF 1' in S['srr']
     and 'theorems whose #check is not printed: NONE' in S['srr'], lambda S: put(S, 'srr', S['srr'].replace('PASSES', 'FAILS'))),
    ('G-ENTRY-TAGS-READ', 'the entry-tag bank: the pages` node files against v0.19..v0.19.1, the decision and its reason', lambda S: S['etags'].get('reemit') is False
     and S['etags'].get('changed') == ['AxiomCheckKeiper.lean'] and len(S['etags'].get('rows') or []) == 2
     and all(r['changed_files_on_page'] == [] and len(r['node_files']) > 5 for r in S['etags'].get('rows') or []),
     lambda S: put(S, 'etags', dict(S['etags'], reemit=True))),
    ('G-BOUNDS-PRINTED', 'the bounds bank: Mathlib`s bounds by name and file, every index to 25, the index chosen', lambda S: bounds_ok(S),
     lambda S: put(S, 'bounds', S['bounds'].replace('THE INDEX CHOSEN: 15', 'THE INDEX CHOSEN'))),
    ('G-STATEMENT-AGAINST-RULING', 'the statements bank of KeiperSign.lean: every item of (R212)(3) carried by a declaration',
     lambda S: statements_ok(S, ('sign',)), lambda S: put(S, 'st', dict(S['st'], sign=dict(S['st']['sign'], items=(S['st']['sign'].get('items') or [])[:-1])))),
    ('G-STATEMENT-AGAINST-WORK-ORDER', 'the statements bank of Schema/PlateauRamp.lean: every item of :12170 and b554`s C1-C2 carried',
     lambda S: statements_ok(S, ('win',)), lambda S: put(S, 'stxt', dict(S['stxt'], win=S['stxt']['win'].replace('EVERY ITEM OF THE STATEMENT', 'SOME ITEMS')))),
    ('G-HOUSE-FORM', 'the six kernel files at the tag: the head (read whitespace-joined), the rule line, no lemma, no sorry, no axiom, the audits` imports',
     lambda S: house_form(S), lambda S: put(S, 'ksrc', dict(S['ksrc'], **{MODS[0]: S['ksrc'].get(MODS[0], '') + '\naxiom x : True\n'}))),
    ('G-HOLD-READ', 'the seven build logs and both page runs: free memory read above the hold before each Lean call, each exit 0',
     lambda S: hold_ok(S), lambda S: put(S, 'PX', dict(S['PX'], free_mb_before=2000))),
    ('G-PRINTS-STD3', 'the two axiom audits` prints: every declaration of the four files printed, each at the standard three or less, no sorryAx, no error',
     lambda S: prints_ok(S), lambda S: put(S, 'pr', dict(S['pr'], sign=dict(S['pr']['sign'], axioms=dict(S['pr']['sign'].get('axioms') or {}, **{SN + 'liCoeff_one_pos': ['sorryAx']}))))),
    ('G-E0-GATES', 'the E0 reads: four gates, each read file`s blob at its tip equal to its blob at the tag, the grades named', lambda S: e0_ok(S),
     lambda S: put(S, 'e0', dict(S['e0'], win=dict(S['e0']['win'], gate=False)))),
    ('G-SALT-CHECK', 'the salt-checks` six theorems: DERIVES at the standard three, each #check printed', lambda S: salt_ok(S),
     lambda S: put(S, 'pr', dict(S['pr'], win=dict(S['pr']['win'], text=(S['pr']['win'].get('text') or '').replace(SALT[4] + ' :', 'x'))))),
    ('G-SIGN-NO-PREMISE', 'the E0 read and the #check of liCoeff_one_pos: 0 < LiCoeff 1, DERIVES at the standard three, no hypothesis', lambda S: sign_ok(S),
     lambda S: put(S, 'e0', dict(S['e0'], sign=dict(S['e0']['sign'], rows={k: (dict(v, why='hP : x') if k.endswith('liCoeff_one_pos') else v)
                                                                            for k, v in (S['e0']['sign'].get('rows') or {}).items()})))),
    ('G-WINDOW-CARRIED-NAMED', 'Schema/PlateauRamp.lean at the tag and its E0 read: the window at INTERFACES on WindowObligations, both obligations named Props',
     lambda S: window_carried_ok(S), lambda S: put(S, 'ksrc', dict(S['ksrc'], **{MODS[2]: S['ksrc'].get(MODS[2], '').replace('smooth : Smooth4 W h', 'smooth : True')}))),
    ('G-RELATION-WORD', 'the relation bank: one of the three words, no declaration concluding EpsteinPremises, the compiled witness at the standard three',
     lambda S: relation_ok(S), lambda S: put(S, 'rel', dict(S['rel'], word='UNRELATED'))),
    ('G-FED-GREP', 'the federation walk: no unread declaration outside the act`s files concluding the sign or the window or a negation; lv`s read',
     lambda S: grep_ok(S), lambda S: put(S, 'gp', dict(S['gp'], bad=[{'cls': 'CONCLUDES'}]))),
    ('G-KERNEL-TAGGED', 'SIDE-explicit-formula: main and the peeled tag v0.20, the push capture`s read-back, v0.19.1 its ancestor', lambda S: tagged_ok(S),
     lambda S: put(S, 'kpush', S['kpush'].replace('read back at the remote', 'read'))),
    ('G-KERNEL-FILES-ONLY', 'SIDE-explicit-formula v0.19.1..v0.20: the six files, no merge commit', lambda S: kfiles_ok(S),
     lambda S: put(S, 'kfiles', S['kfiles'] + ['README.md'])),
    ('G-BRANCH-KEPT-PUSHED', 'the working branch at the tag, pushed by name and read back', lambda S: branch_ok(S),
     lambda S: put(S, 'kbranch', '0' * 40)),
    ('G-NODE-LISTS', 'both node lists against their sources: every line carried, the pins moved, the nodes placed after their anchors',
     lambda S: node_lists_ok(S), lambda S: put(S, 'nodes_x', S['nodes_x'].replace('# pin: v0.20', '# pin: v0.17'))),
    ('G-PAGE-ZETA-NODES', 'the ζ page at HEAD and its bank: re-emitted at v0.20, the three sign nodes on it, liCoeff_one_pos DERIVES', lambda S: page_ok(S, 'zeta'),
     lambda S: put(S, 'PZ', dict(S['PZ'], new=[x for x in S['PZ'].get('new') or [] if not x.get('name', '').endswith('liCoeff_one_pos')]))),
    ('G-PAGE-CHI-NODES', 'the χ page at HEAD and its bank: re-emitted at v0.20, the seven window nodes on it, plateauRampWindow_of INTERFACES',
     lambda S: page_ok(S, 'chi'), lambda S: put(S, 'PX', dict(S['PX'], changed=False))),
    ('G-PAGES-COMMITTED-ALONE', 'PLACE-papers` log since ca841ca: each page in one commit of its own', lambda S: pages_alone(S),
     lambda S: put(S, 'pp_files', {h: (f + ['FINDINGS.md'] if PAGE in f else f) for h, f in S['pp_files'].items()})),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from this act`s list and v0.20 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from this act`s χ list and v0.20 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank after the page commits: both page arms and the frozen control', lambda S: 'PAGE ARMS PASSING : 2 of 2' in S['arms_c2']
     and ('%s PASSING : 2 of 2' % CONTROL_ARM) in S['arms_c2'], lambda S: put(S, 'arms_c2', S['arms_c2'].replace('PASSING : 2 of 2', 'PASSING : 1 of 2'))),
    ('G-BEARING', 'the bearing bank against each keystone at PLACE-papers HEAD: the two sentences on their cited lines, the reading beside each',
     lambda S: bearing_ok(S), lambda S: put(S, 'bear_now', {k: v + 'x' for k, v in S['bear_now'].items()})),
    ('G-H36A-SCORED', 'the scores and the desk', lambda S: _h36(S, 'H36a'), lambda S: put(S, 'desk', '')),
    ('G-H36B-SCORED', 'the scores and the desk', lambda S: _h36(S, 'H36b'), lambda S: put(S, 'sc', dict(S['sc'], H36b=['x', '']))),
    ('G-H36C-SCORED', 'the scores and the desk', lambda S: _h36(S, 'H36c'), lambda S: put(S, 'sc', dict(S['sc'], H36c=['x', '']))),
    ('G-H36D-SCORED', 'the scores and the desk', lambda S: _h36(S, 'H36d'), lambda S: put(S, 'sc', dict(S['sc'], H36d=['x', '']))),
    ('G-H36E-SCORED', 'the scores and the desk', lambda S: _h36(S, 'H36e'), lambda S: put(S, 'sc', dict(S['sc'], H36e=['x', '']))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD,
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and 'n_one_binding_instance' in trail(S) and 'χ page' in trail(S), lambda S: put(S, 'ot', S['ot'].replace('Resolved by the seat, for the author’s strike', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b603, the family form over χ mod q' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b603, the family form over χ mod q', 'x'))),
    ('G-KERNELS-UNTOUCHED', 'every other kernel`s main, the explicit-formula checkout on main at the tag and clean, the trial branch',
     lambda S: all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['kcur'] == 'main' and S['kdirty'] == ''
     and bool(S['ktag']) and S['kmain'] == S['ktag'] and S['trial'] == 'f22ff35', lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-kernel': '0'}))),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('36352a0', '36352a0', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b602_record.py'): S['tooltext'].get(os.path.join(T, 'b602_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                              if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces'][1] and S['faces'][0] == S['faces'][1],
     lambda S: put(S, 'faces', (S['faces'][0] + b'x', S['faces'][1]))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-REGISTRY-UNTOUCHED', 'REGISTRY.md against its pre-act blob', lambda S: S['registry'][1] and S['registry'][0] == S['registry'][1],
     lambda S: put(S, 'registry', (S['registry'][0] + b'x', S['registry'][1]))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md against its pre-act blob', lambda S: S['errata'][1] and S['errata'][0] == S['errata'][1],
     lambda S: put(S, 'errata', (S['errata'][0] + b'x', S['errata'][1]))),
    ('G-KEYSTONES-SCOPE', 'PLACE-papers` phase, day1 and outputs paths, tracked and untracked: none written', lambda S: S['keystone_changes'] == [],
     lambda S: put(S, 'keystone_changes', [BALPOS])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 97485547, by blob id', lambda S: S['prior_bad'] == []
     and S['prior_n'] > 6000, lambda S: put(S, 'prior_bad', ['data/b601_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', PAGE, DIR_PAGE]),
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
                                                                          and "startswith('b602')" in S['suite'] and "data/b602_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b602')", ''))),
]
THE_PAGE_AT = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md @ ca841ca0'


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
    rec('b602 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('PRE-SEAL (R202)(3)' if PRERUN else 'POST-PUSH' if pushed else 'PRE-PUSH'))
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
        out = os.path.join(D, 'b602_arms_prerun.txt')
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b602_checks_postpush.txt' if pushed else 'b602_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    if not (RERUN or PRERUN):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b602_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
