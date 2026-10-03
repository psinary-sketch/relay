# -*- coding: utf-8 -*-
"""b603_checks.py -- THE SUITE OF b603, UNDER (R213): THE FAMILY FORM OVER χ MOD q -- THE FINITE SUM OF CONFIGURATIONS AND THE
FAMILY THEOREM FROM THE PRODUCT LEMMA; THE DEDEKIND READING'S TWO OBSTRUCTIONS NAMED.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>` or `--prerun`; it writes data/b603_checks.txt before the push and
### data/b603_checks_postpush.txt after it. ### `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the
### face is sealed, no table regenerated, its counts written to data/b603_arms_prerun.txt and nothing else.
### ### The harness is b568's to b602's, carried by slicing tools/b602_checks.py (its imports, helpers, regenerate and main); the
### sources, predicates and arms are b603's. The control arm is the frozen one of (R207)(2).
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
FACE = os.path.join(D, 'b603_registration_2026-10-03.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PRE = dict(relay='3d88436a', pp='a09c470', gs='3528bcf', ker='914c413')
TAG = 'v0.21'
BRANCH = 'family-b603'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b', 'product-b600': '1dd5cd7',
        'doubling-keiper-b601': '5fc0c87', 'sign-window-b602': '914c413'}
OWN = ['AxiomCheckFamily.lean', 'SIDEExplicitFormula/Schema/Family.lean', 'SIDEExplicitFormula/Schema/SaltCheckFamily.lean']
MODS = OWN[1:]
KEYS = ('fam', 'sfam')
FN = 'SIDEExplicitFormula.Schema.Family.'
STD3 = {'propext', 'Classical.choice', 'Quot.sound'}
GRHC = 'phase1.5/spectral/GRH_CASCADE_v0_3_6.md'
SIMP = 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md'
PRE_ADDENDUM = 'b558_editions/BALANCE_AND_POSITIVITY_addendum.txt'
PRE_LVLIST = 'SIDE-lv-conservation_housekeeping.txt'
STEPZERO = 'f0860e0b'
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/66b08248-485c-49c9-9f98-79f2f4e189ca/scratchpad'


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b603')
            and 'data/b603_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    import b603_record as REC
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b603_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b603_') and f.endswith('.py'))
    tagc = gs(KER, 'rev-parse', '--verify', '-q', TAG + '^{commit}')
    S = dict(
        REC=REC, face=face, ferry=rd('b603_ferry.txt'), scan=rd('b603_ferry_scan.txt'), cens=rd('b603_census_stepzero.txt'),
        fcens=rd('b603_faces_census_stepzero.txt'), pins0=rd('b603_pins_stepzero.txt'), procs=rd('b603_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b602_closing.txt'), reads=rd('b603_reads.txt'), branches=rd('b603_branches.txt'), answers=rd('b603_author_answers.txt'),
        prerun=rd('b603_arms_prerun.txt'), arith=rd('b603_arith.txt'), dtxt=rd('b603_dedekind.txt'), dd=jl('b603_dedekind.json'),
        dline=jl('b603_dedekind_line.json'),
        addendum=rd(PRE_ADDENDUM), lvlist=rd(PRE_LVLIST),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))))
              for f in ('b602_checks.py', 'test_chain_page_b596.py', 'chain_page.py', 'e0_rule.py', 'g_chain_page.py', 'push_gated.sh')},
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
        lv_head=gs('D:/SIDE-lv-conservation', 'rev-parse', 'HEAD'), lv_dirty=gs('D:/SIDE-lv-conservation', 'status', '--porcelain', '--untracked-files=no'),
        trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain', '--untracked-files=no'),
        kmain=gs(KER, 'rev-parse', 'main'), ktag=tagc, kbranch=gs(KER, 'rev-parse', '--verify', '-q', BRANCH),
        kanc=(subprocess.run(['git', '-C', KER, 'merge-base', '--is-ancestor', PRE['ker'], TAG]).returncode == 0) if tagc else False,
        kfiles=sorted(x for x in gs(KER, 'diff', '--name-only', PRE['ker'], TAG).split(NL) if x.strip()) if tagc else [],
        kmerges=[x for x in gs(KER, 'rev-list', '--merges', '%s..%s' % (PRE['ker'], TAG)).split(NL) if x.strip()] if tagc else ['none'],
        ksrc={f: (blob(KER, '%s:%s' % (TAG, f)) or b'').decode('utf-8', 'replace') for f in OWN} if tagc else {},
        kpush=rd('b603_kernel_push_out.txt'), bpush=rd('b603_branch_push_out.txt'),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b602*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b603_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b603_mustnotexist.txt')), table_changed=None,
        fj=jl('b603_findings.json'), tj=jl('b603_trail.json'), sc=jl('b603_scores.json'), desk=rd('b603_desk_notes.txt'),
        rl=jl('b603_record_lines.json'),
        st=jl('b603_statements_fam.json'), stxt=rd('b603_statements_fam.txt'),
        pr=jl('b603_prints_fam.json'),
        e0={k: jl('b603_e0_%s.json' % k) for k in KEYS}, gp=jl('b603_grep.json'), br=jl('b603_bearing.json'),
        builds={k: rd('b603_build_%s.txt' % k) for k in KEYS + ('axfam',)},
        PZ=jl('b603_page_zeta.json'), PX=jl('b603_page_chi.json'), arms_c2=rd('b603_page_arms_c2.txt'),
        nodes_x=rd('b603_nodes_chi.txt'), nodes602x=rd('b602_nodes_chi.txt'),
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
    X['gcp_zeta'] = GCP.arm(os.path.join(D, 'b602_nodes_zeta.txt'), os.path.join(SP, '_b603_gcp'), os.path.join(D, 'b602_probe_out.txt'))
    X['gcp_chi'] = GCP.arm(os.path.join(D, 'b603_nodes_chi.txt'), os.path.join(SP, '_b603_gcp'), os.path.join(D, 'b603_chi_probe_out.txt')) \
        if os.path.exists(os.path.join(D, 'b603_chi_probe_out.txt')) else \
        GCP.arm(os.path.join(D, 'b602_nodes_chi.txt'), os.path.join(SP, '_b603_gcp'), os.path.join(D, 'b602_chi_probe_out.txt'))
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
    return a.startswith(ls[0]['head']) and '(:6998)' in a and 'b602 AT ITS WEIGHT' in a and '35488da' in a and '914c413' in a \
        and '86 of 86' in a and ls[0]['line'] > 6998


def credit_ok(S):
    ls = S['rl'].get('lines', [])
    if len(ls) != 2:
        return False
    a = fline(S, ls[1]['line'])
    return a.startswith(ls[1]['head']) and 'n_one_binding_instance' in a and 'ef62027' in a and 'non-strict' in a \
        and 'MOVED-IN-MEANING' in a and ':400' in a and PRE_ADDENDUM in a and PRE_LVLIST in a and ls[1]['line'] > ls[0]['line']


def addendum_ok(S):
    a = S['addendum']
    return a.startswith('b603 -- THE BALANCE_AND_POSITIVITY WORK-LIST ADDENDUM, FOR v0.9.6') \
        and ':400 -- `n_one_binding_instance` -- MOVED-IN-MEANING' in a and 'liCoeff_one_pos' in a and 'v0.20 = 914c413' in a \
        and '**OPEN**' in a and '### 1 sentence-row (1 distinct line).' in a


def lvlist_ok(S):
    a = S['lvlist']
    return a.startswith('b603 -- THE HOUSEKEEPING LIST OF SIDE-lv-conservation') \
        and ':304 @ ef62027 = :356 @ 2f71068' in a and 'MOVED-IN-MEANING' in a and 'WHY IT IS NOT PROVED HERE' in a \
        and 'liCoeff_one_pos' in a and 'v0.20 = 914c413' in a


def statements_ok(S):
    it = S['st'].get('items') or []
    return len(it) == len(S['REC'].ITEMS['fam']) and all(i['in_statement'] and i['declared'] for i in it) \
        and 'EVERY ITEM OF THE STATEMENT CARRIED BY A DECLARATION' in S['stxt']


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
        if not (t.startswith('/-\nSIDE-explicit-formula -- %s\n' % f) and "THIS PROGRAMME'S WORK (act b603" in head
                and '`theorem`, never `lemma`' in head and 'NOT VENDORED' in head):
            return False
        if re.search(r'^\s*lemma\s', t, re.M) or re.search(r'\bsorry\b', strip_lean(t)) or 'native_decide' in strip_lean(t) \
                or re.search(r'^\s*axiom\s', strip_lean(t), re.M):
            return False
    return src['AxiomCheckFamily.lean'].startswith('import SIDEExplicitFormula.Schema.Family\nimport SIDEExplicitFormula.Schema.SaltCheckFamily\n')


def rows_all(S):
    return {n: r for e in S['e0'].values() for n, r in (e.get('rows') or {}).items()}


def prints_ok(S):
    p = S['pr']
    ax = p.get('axioms') or {}
    decl = [n for kk in KEYS for n in (S['e0'][kk].get('rows') or {})]
    return bool(ax and decl) and all(n in ax for n in decl) and all(set(v) <= STD3 for v in ax.values()) and not p.get('sorry') \
        and p.get('errors') == 0 and p.get('std3') is True and 'rc=0' in (p.get('exit') or '')


def e0_ok(S):
    r = rows_all(S)
    want = {FN + 'finsetSum_productLemma': 'DERIVES', FN + 'family_theorem': 'DERIVES', FN + 'family_three': 'DERIVES',
            FN + 'family_three_statement': 'DERIVES', FN + 'familyConfig_arith': 'DERIVES', FN + 'zeta_rhs_pole': 'DERIVES'}
    return all(S['e0'][k].get('gate') is True and S['e0'][k].get('same_file') is True
               and re.fullmatch(r'[0-9a-f]{40}', S['e0_blob'].get(k, ('', '#'))[0]) is not None
               and S['e0_blob'].get(k, ('', '#'))[0] == S['e0_blob'].get(k, ('', '#'))[1] for k in KEYS) \
        and all(r.get(n, {}).get('grade') == g_ for n, g_ in want.items())


SALT = [FN + 'SaltCheck.' + n for n in ('finsetSum_satisfiable', 'finsetSum_summand_load_bearing', 'family_one_empty', 'family_one_h2')]


def salt_ok(S):
    r = rows_all(S)
    txt = S['pr'].get('text') or ''
    return all(r.get(n, {}).get('std3') and r.get(n, {}).get('grade') == 'DERIVES' for n in SALT) and all((n + ' :') in txt for n in SALT)


def check_of(S, n):
    # ### the #check's statement: from its name to the next unindented line (Lean wraps a statement on indented lines and
    # ### prints every name qualified, so a cut at the next qualified name would stop inside the statement -- b603 (d))
    txt = S['pr'].get('text') or ''
    if (FN + n + ' : ') not in txt:
        return ''
    ls = txt.split(FN + n + ' : ', 1)[1].split(NL)
    out = [ls[0]]
    for l in ls[1:]:
        if not l.startswith(' '):
            break
        out.append(l)
    return flat(NL.join(out))


def finset_ok(S):
    r = rows_all(S).get(FN + 'finsetSum_productLemma', {})
    t = S['ksrc'].get(MODS[0], '')
    body = t.split('theorem finsetSum_productLemma')[-1].split('\ntheorem ')[0]
    return r.get('grade') == 'DERIVES' and r.get('std3') is True and 'induction s using Finset.induction_on with' in body \
        and 'Product.productLemma_holds' in body \
        and ('h2_sign_cfg (' + FN + 'finsetSum s f) ↔ ∀ i ∈ s, SIDEExplicitFormula.Schema.h2_sign_cfg (f i)') in check_of(S, 'finsetSum_productLemma')


def family_ok(S):
    r = rows_all(S).get(FN + 'family_theorem', {})
    c = check_of(S, 'family_theorem')
    return r.get('grade') == 'DERIVES' and r.get('std3') is True and 'h2_sign_cfg (SIDEExplicitFormula.Schema.Family.familyConfig q) ↔' in c \
        and 'GRH_chi' in c and 'primitiveCharacter' in c


def modulus_ok(S):
    t = S['ksrc'].get(MODS[0], '')
    r = rows_all(S)
    return re.search(r'theorem family_three_statement :[\s\S]*?:=\s*rfl\b', t) is not None \
        and r.get(FN + 'family_three_statement', {}).get('std3') is True and r.get(FN + 'family_three', {}).get('std3') is True \
        and 'THE MODULUS CHOSEN: q = 3' in S['arith'] and 'not two' in S['arith']


def arith_ok(S):
    a = S['arith']
    return 'familyConfig_arith' in a and 'Real.log (χ.conductor / Real.pi)' in a and 'Real.log (N / Real.pi)' in a \
        and 'one log (N_χ/π) per character of the family' in a and '### MISSING' not in a


def dedekind_ok(S):
    d = S['dd']
    t = S['ksrc'].get(MODS[0], '')
    return d.get('concluding') == [] and sorted(d.get('named') or []) == sorted(S['REC'].PREMISES) \
        and 'NOTHING OF EITHER OBSTRUCTION IS DISCHARGED: TRUE' in S['dtxt'] and 'poleTerm' in S['dtxt'] \
        and 'def TrivialSummandPremise : Prop :=' in t and 'def EulerFactorPremise (q : ℕ) [NeZero q] : Prop :=' in t \
        and 'structure DedekindPremises (q : ℕ) [NeZero q] : Prop where' in t


def dline_ok(S):
    n = S['dline'].get('line')
    a = fline(S, n)
    return bool(n) and a.startswith(S['REC'].DED_HEAD) and 'TrivialSummandPremise' in a and 'EulerFactorPremise' in a \
        and 'not a theorem' in a and 'Struck or kept on the author’s word' in a and n > 6998


def grep_ok(S):
    gp = S['gp']
    rows = gp.get('rows') or []
    return gp.get('bad') == [] and bool(rows) and all((gp.get('controls') or {}).values()) and len(gp.get('controls') or {}) == 4 \
        and any(r['cls'] == 'OWN' and r['name'] == 'finsetSum_productLemma' for r in rows) \
        and any(r['cls'] == 'OWN' and r['name'] == 'family_theorem' for r in rows) and len(gp.get('kernels') or []) > 40


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
    for k in KEYS + ('axfam',):
        m = re.search(r'free MB before: (\d+)', S['builds'][k])
        if not (m and int(m.group(1)) >= 2560 and re.search(r'^### EXIT rc=0 ', S['builds'][k], re.M)):
            return False
    return (S['PZ'].get('free_mb_before') or 0) >= 2560 and (S['PX'].get('free_mb_before') or 0) >= 2560


def page_zeta_ok(S):
    z = S['PZ']
    a, b, c = S['pages'][PAGE]
    return z.get('rc') == 0 and z.get('changed') is False and z.get('diff') == [] and bool(a) and a == b == c \
        and hashlib.sha256(c).hexdigest() == z.get('sha256')


def page_chi_ok(S):
    z = S['PX']
    new = {x['name']: x for x in z.get('new') or []}
    a, b, c = S['pages'][DIR_PAGE]
    return z.get('rc') == 0 and z.get('changed') is True and sorted(new) == sorted(S['REC'].FAM_NODES) \
        and new.get(FN + 'family_theorem', {}).get('grade') == 'DERIVES' and bool(a) and a == c and a != b \
        and hashlib.sha256(c).hexdigest() == z.get('sha256') and all(('`%s`' % n) in c.decode('utf-8') for n in S['REC'].FAM_NODES)


def pages_alone(S):
    out = []
    for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])):
        c = [h for h, f in S['pp_files'].items() if p in f]
        if z.get('changed') is True:
            out.append(len(c) == 1 and S['pp_files'][c[0]] == [p] and dict(S['pp_log'])[c[0]].startswith('b603 (R213)(4): ' + p))
        else:
            out.append(z.get('changed') is False and c == [])
    return all(out) and S['PX'].get('changed') is True


def node_lists_ok(S):
    R = S['REC']
    x, ox = S['nodes_x'].rstrip(NL).split(NL), S['nodes602x'].rstrip(NL).split(NL)
    if '# pin: v0.21' not in x or '# pin: v0.20' in x:
        return False
    i = x.index(R.CHI_ANCHOR) if R.CHI_ANCHOR in x else -1
    return i > 0 and x[i + 1:i + 1 + len(R.FAM_ADD)] == R.FAM_ADD \
        and all((('# pin: v0.21' if l == '# pin: v0.20' else l) in x) for l in ox if l.strip())


def bearing_ok(S):
    rows = S['br'].get('rows') or []
    return [(r['path'], r['line']) for r in rows] == S['REC'].BEAR_WANT and all(r['found'] for r in rows) \
        and all(S['bear_now'].get((r['path'], r['line'])) == r['sentence'] for r in rows) and all(len(r['reading']) > 200 for r in rows)


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 30]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') and fline(S, e).startswith('## The family form over χ mod q') \
        and '**The finite sum**' in tail and '**The family**' in tail and '**The modulus**' in tail and '**The Dedekind reading**' in tail \
        and '**The ceiling.**' in tail and '**Read in mutual light**' in tail and 'strengthens' in tail and (S['ktag'][:7] or '#') in tail \
        and 'not a reduction of GRH' in tail


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


def _h37(S, k):
    v = S['sc'].get(k)
    return bool(v) and v[0] in ('HOLDS', 'REFUTED') and ('(%s)' % k.upper()) in S['desk']


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R213) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b602`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b602' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b603 -- x'])),
    ('G-R213-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R213) END' in S['ferry'] and S['ot'].count('**(R213) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R213) ratified', '(R213) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in (
        'SIDEExplicitFormula/Product.lean @ 914c4137', 'SIDEExplicitFormula/Schema/Config.lean @ 21c8c522',
        'SIDEExplicitFormula/Schema/Converse.lean @ 21c8c522', 'SIDEExplicitFormula/Schema/Instances.lean @ 21c8c522',
        'SIDEExplicitFormula/Chi/Main.lean @ ac157c1d', 'Mathlib/NumberTheory/DirichletCharacter/Basic.lean @ de5ce8a9',
        'Mathlib/NumberTheory/MulChar/Duality.lean @ de5ce8a9', GRHC + ' @ a09c4700', SIMP + ' @ a09c4700',
        'data/b558_editions/BALANCE_AND_POSITIVITY.txt @', 'SIDELvConservation/CouplingsAtPhi.lean @ ef620273', DIR_PAGE + ' @ a09c4700',
        'OPEN_TRAILS.md @ a09c4700', 'data/b602_closing_push_out.txt @', "chain_page.py`s hold: ['HOLD_MB = 2560']"))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ANSWERS-BANKED', 'the act`s answers bank: every prompt with its options and recommended mark verbatim, or none',
     lambda S: S['answers'].startswith('### b603 -- THE AUTHOR`S ANSWERS') and S['answers'].count('### PROMPT ') == S['answers'].count('\nRESULT ')
     and (S['answers'].count('### PROMPT ') > 0 or '### NONE: no prompt was put' in S['answers']),
     lambda S: put(S, 'answers', S['answers'].replace('### b603 -- THE AUTHOR', '### b6O3 -- THE AUTHOR', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay f0860e0b`s files', lambda S: S['pushout'][0] == ['data/b602_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/b602_closing_push_out.txt', 'x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b602') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b602'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'sign-window-b602': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80 and every PLACE-papers read at ba5f0ea, run afresh through the test`s control()',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(S['ctl'][0], ok=False)] + S['ctl'][1:])),
    ('G-INSTRUMENTS-UNEDITED', 'b602`s sealed suite, the control`s test file, the generator, its arm, the E0 rule and the push gate against 3d88436a',
     lambda S: all(bool(a) and a == b for a, b in S['inst'].values()) and len(S['inst']) == 6,
     lambda S: put(S, 'inst', dict(S['inst'], **{'e0_rule.py': (S['inst']['e0_rule.py'][0], (S['inst']['e0_rule.py'][1] or b'') + b'x')}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b602`s weight, addressed to its entry', lambda S: weight_ok(S),
     lambda S: put(S, 'rl', dict(S['rl'], lines=(S['rl'].get('lines') or [])[1:]))),
    ('G-PRIOR-ART-CREDITED', 'FINDINGS at the banked line: the prior art credited and the two stale lines routed', lambda S: credit_ok(S),
     lambda S: put(S, 'find', S['find'].replace('non-strict constants form, credited', 'constants form, credited'))),
    ('G-ADDENDUM-ROW', 'the BALANCE_AND_POSITIVITY work-list addendum: the :400 row, MOVED-IN-MEANING, citing liCoeff_one_pos at v0.20',
     lambda S: addendum_ok(S), lambda S: put(S, 'addendum', S['addendum'].replace('MOVED-IN-MEANING', 'STANDS'))),
    ('G-LV-LIST-ROW', 'the lv kernel`s housekeeping list: the docstring row, MOVED-IN-MEANING, citing liCoeff_one_pos at v0.20',
     lambda S: lvlist_ok(S), lambda S: put(S, 'lvlist', S['lvlist'].replace(':304 @ ef62027', ':300 @ ef62027'))),
    ('G-STATEMENT-AGAINST-RULING', 'the statements bank of Schema/Family.lean: every item of (R213)(3) carried by a declaration',
     lambda S: statements_ok(S), lambda S: put(S, 'st', dict(S['st'], items=(S['st'].get('items') or [])[:-1]))),
    ('G-HOUSE-FORM', 'the three kernel files at the tag: the head (read whitespace-joined), the rule line, no lemma, no sorry, no axiom, the audit`s imports',
     lambda S: house_form(S), lambda S: put(S, 'ksrc', dict(S['ksrc'], **{MODS[0]: S['ksrc'].get(MODS[0], '') + '\naxiom x : True\n'}))),
    ('G-HOLD-READ', 'the three build logs and both page runs: free memory read above the hold before each Lean call, each exit 0',
     lambda S: hold_ok(S), lambda S: put(S, 'PX', dict(S['PX'], free_mb_before=2000))),
    ('G-PRINTS-STD3', 'the axiom audit`s prints: every declaration of the two files printed, each at the standard three or less, no sorryAx, no error',
     lambda S: prints_ok(S), lambda S: put(S, 'pr', dict(S['pr'], axioms=dict(S['pr'].get('axioms') or {}, **{FN + 'family_theorem': ['sorryAx']})))),
    ('G-E0-GATES', 'the E0 reads: two gates, each read file`s blob at its tip equal to its blob at the tag, the grades named', lambda S: e0_ok(S),
     lambda S: put(S, 'e0', dict(S['e0'], fam=dict(S['e0']['fam'], gate=False)))),
    ('G-SALT-CHECK', 'the salt-check`s four theorems: DERIVES at the standard three, each #check printed', lambda S: salt_ok(S),
     lambda S: put(S, 'pr', dict(S['pr'], text=(S['pr'].get('text') or '').replace(SALT[1] + ' :', 'x')))),
    ('G-FINSET-NO-PREMISE', 'the E0 read, the source and the #check of finsetSum_productLemma: DERIVES at the standard three, by Finset induction',
     lambda S: finset_ok(S), lambda S: put(S, 'ksrc', dict(S['ksrc'], **{MODS[0]: S['ksrc'].get(MODS[0], '').replace('induction s using Finset.induction_on with', 'induction s with')}))),
    ('G-FAMILY-THEOREM', 'the E0 read and the #check of family_theorem: DERIVES at the standard three, the summed configuration against GRH_chi',
     lambda S: family_ok(S), lambda S: put(S, 'e0', dict(S['e0'], fam=dict(S['e0']['fam'], rows={k: (dict(v, grade='INTERFACES') if k.endswith('.family_theorem') else v)
                                                                                             for k, v in (S['e0']['fam'].get('rows') or {}).items()})))),
    ('G-MODULUS-RFL', 'the source at the tag, the E0 read and the arithmetic bank: q = 3 by rfl, the choice and its reason printed', lambda S: modulus_ok(S),
     lambda S: put(S, 'arith', S['arith'].replace('THE MODULUS CHOSEN: q = 3', 'THE MODULUS CHOSEN'))),
    ('G-ARITH-PRINTED', 'the arithmetic bank: the summed side and the conductor`s log (N/π) per summand, printed from the kernel', lambda S: arith_ok(S),
     lambda S: put(S, 'arith', S['arith'] + '### MISSING')),
    ('G-DEDEKIND-NAMED', 'the Dedekind bank and the source at the tag: both obstructions named Props, nothing concluding either', lambda S: dedekind_ok(S),
     lambda S: put(S, 'dd', dict(S['dd'], concluding=['x']))),
    ('G-DEDEKIND-LINE', 'FINDINGS at the banked line: the reading carried beside the entry, the author`s strike item', lambda S: dline_ok(S),
     lambda S: put(S, 'dline', dict(S['dline'], line=1))),
    ('G-FED-GREP', 'the federation walk: no unread declaration outside the act`s files concluding the family theorem, the finite lemma, a premise or a negation',
     lambda S: grep_ok(S), lambda S: put(S, 'gp', dict(S['gp'], bad=[{'cls': 'CONCLUDES'}]))),
    ('G-KERNEL-TAGGED', 'SIDE-explicit-formula: main and the peeled tag v0.21, the push capture`s read-back, v0.20 its ancestor', lambda S: tagged_ok(S),
     lambda S: put(S, 'kpush', S['kpush'].replace('read back at the remote', 'read'))),
    ('G-KERNEL-FILES-ONLY', 'SIDE-explicit-formula v0.20..v0.21: the three files, no merge commit', lambda S: kfiles_ok(S),
     lambda S: put(S, 'kfiles', S['kfiles'] + ['README.md'])),
    ('G-BRANCH-KEPT-PUSHED', 'the working branch at the tag, pushed by name and read back', lambda S: branch_ok(S),
     lambda S: put(S, 'kbranch', '0' * 40)),
    ('G-NODE-LISTS', 'the χ node list against b602`s: every line carried, the pin moved, the family nodes after the χ instance`s check',
     lambda S: node_lists_ok(S), lambda S: put(S, 'nodes_x', S['nodes_x'].replace('# pin: v0.21', '# pin: v0.20'))),
    ('G-PAGE-ZETA-UNCHANGED', 'the ζ page at HEAD and its bank: re-emitted from b602`s list, byte for byte, nothing written', lambda S: page_zeta_ok(S),
     lambda S: put(S, 'PZ', dict(S['PZ'], changed=True))),
    ('G-PAGE-CHI-NODES', 'the χ page at HEAD and its bank: re-emitted at v0.21, the ten family nodes on it, family_theorem DERIVES',
     lambda S: page_chi_ok(S), lambda S: put(S, 'PX', dict(S['PX'], changed=False))),
    ('G-PAGES-COMMITTED-ALONE', 'PLACE-papers` log since a09c470: each changed page in one commit of its own, an unchanged page in none', lambda S: pages_alone(S),
     lambda S: put(S, 'pp_files', {h: (f + ['FINDINGS.md'] if DIR_PAGE in f else f) for h, f in S['pp_files'].items()})),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b602`s list and v0.20 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from this act`s χ list and v0.21 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank after the page commits: both page arms and the frozen control', lambda S: 'PAGE ARMS PASSING : 2 of 2' in S['arms_c2']
     and ('%s PASSING : 2 of 2' % CONTROL_ARM) in S['arms_c2'], lambda S: put(S, 'arms_c2', S['arms_c2'].replace('PASSING : 2 of 2', 'PASSING : 1 of 2'))),
    ('G-BEARING', 'the bearing bank against each keystone at PLACE-papers HEAD: the four sentences on their cited lines, the reading beside each',
     lambda S: bearing_ok(S), lambda S: put(S, 'bear_now', {k: v + 'x' for k, v in S['bear_now'].items()})),
    ('G-H37A-SCORED', 'the scores and the desk', lambda S: _h37(S, 'H37a'), lambda S: put(S, 'desk', '')),
    ('G-H37B-SCORED', 'the scores and the desk', lambda S: _h37(S, 'H37b'), lambda S: put(S, 'sc', dict(S['sc'], H37b=['x', '']))),
    ('G-H37C-SCORED', 'the scores and the desk', lambda S: _h37(S, 'H37c'), lambda S: put(S, 'sc', dict(S['sc'], H37c=['x', '']))),
    ('G-H37D-SCORED', 'the scores and the desk', lambda S: _h37(S, 'H37d'), lambda S: put(S, 'sc', dict(S['sc'], H37d=['x', '']))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD,
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and 'primitive inducer' in trail(S) and 'distributively' in trail(S), lambda S: put(S, 'ot', S['ot'].replace('Resolved by the seat, for the author’s strike', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b604, the edition of THE_FINDINGS_AS_THEY_STAND' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b604, the edition of THE_FINDINGS_AS_THEY_STAND', 'x'))),
    ('G-KERNELS-UNTOUCHED', 'every other kernel`s main, lv`s HEAD and status, the explicit-formula checkout on main at the tag and clean, the trial branch',
     lambda S: all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['kcur'] == 'main' and S['kdirty'] == ''
     and bool(S['ktag']) and S['kmain'] == S['ktag'] and S['trial'] == 'f22ff35' and S['lv_head'].startswith('2f71068a') and S['lv_dirty'] == '',
     lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-kernel': '0'}))),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('36352a0', '36352a0', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b603_record.py'): S['tooltext'].get(os.path.join(T, 'b603_record.py'), '') + NL + 'os' + '.remove(p)'}))),
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
     lambda S: put(S, 'keystone_changes', [GRHC])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 3d88436a, by blob id', lambda S: S['prior_bad'] == []
     and S['prior_n'] > 6000, lambda S: put(S, 'prior_bad', ['data/b602_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', DIR_PAGE]),
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
                                                                          and "startswith('b603')" in S['suite'] and "data/b603_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b603')", ''))),
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
    rec('b603 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('PRE-SEAL (R202)(3)' if PRERUN else 'POST-PUSH' if pushed else 'PRE-PUSH'))
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
        out = os.path.join(D, 'b603_arms_prerun.txt')
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b603_checks_postpush.txt' if pushed else 'b603_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    if not (RERUN or PRERUN):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b603_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
