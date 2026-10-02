# -*- coding: utf-8 -*-
"""b600_checks.py -- THE SUITE OF b600, UNDER (R210): REMAINDER 5, THE PRODUCT LEMMA STATED AS A SALT-CHECKED PROP AND PROVED OR
CARRIED TO ITS NAMED OBLIGATIONS; THE GENERATOR-RUN LINE AMENDED; THE AUTHORITY ORDER ENTERED.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>` or `--prerun`; it writes data/b600_checks.txt before the push and
### data/b600_checks_postpush.txt after it. ### `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the
### face is sealed, no table regenerated, its counts written to data/b600_arms_prerun.txt and nothing else.
### ### The harness is b568's to b599's, carried; the arms are b600's. The control arm is the frozen one of (R207)(2).
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
FACE = os.path.join(D, 'b600_registration_2026-10-02.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PRE = dict(relay='2b9f75cd', pp='bc1337a', gs='3528bcf', ker='5a1630b8')
TAG = 'v0.18'
BRANCH = 'product-b600'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b'}
OWN = ['AxiomCheckProduct.lean', 'SIDEExplicitFormula/Product.lean', 'SIDEExplicitFormula/SaltCheckProduct.lean']
NS = 'SIDEExplicitFormula.Product.'
THE_NODE = NS + 'productLemma_holds'
NEW_NODES = [NS + 'sum', NS + 'sum_ef', NS + 'ProductLemma', NS + 'h2_sign_cfg_sum_iff_targets', NS + 'productLemma_holds']
SALT = [NS + 'SaltCheck.' + n for n in ('product_satisfiable', 'product_part_load_bearing', 'product_sum_not_forced')]
STD3 = {'propext', 'Classical.choice', 'Quot.sound'}
GRH = 'phase1.5/spectral/GRH_CASCADE_v0_3_6.md'
SIMP = 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md'
STEPZERO = '92b1c086'
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/35432614-be58-48b9-8b45-54387165dcef/scratchpad'


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b600')
            and 'data/b600_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    import b600_record as REC
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b600_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b600_') and f.endswith('.py'))
    tagc = gs(KER, 'rev-parse', '--verify', '-q', TAG + '^{commit}')
    S = dict(
        REC=REC, face=face, ferry=rd('b600_ferry.txt'), scan=rd('b600_ferry_scan.txt'), cens=rd('b600_census_stepzero.txt'),
        fcens=rd('b600_faces_census_stepzero.txt'), pins0=rd('b600_pins_stepzero.txt'), procs=rd('b600_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b599_closing.txt'), reads=rd('b600_reads.txt'), branches=rd('b600_branches.txt'), answers=rd('b600_author_answers.txt'),
        prerun=rd('b600_arms_prerun.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))))
              for f in ('b599_checks.py', 'test_chain_page_b596.py', 'chain_page.py', 'e0_rule.py', 'g_chain_page.py', 'push_gated.sh')},
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
        kmain=gs(KER, 'rev-parse', 'main'), ktag=tagc, kbranch=gs(KER, 'rev-parse', '--verify', '-q', BRANCH),
        kfiles=sorted(x for x in gs(KER, 'diff', '--name-only', PRE['ker'], TAG).split(NL) if x.strip()) if tagc else [],
        kmerges=[x for x in gs(KER, 'rev-list', '--merges', '%s..%s' % (PRE['ker'], TAG)).split(NL) if x.strip()] if tagc else ['none'],
        kanc=subprocess.run(['git', '-C', KER, 'merge-base', '--is-ancestor', PRE['ker'], TAG]).returncode == 0 if tagc else False,
        ksrc={f: (blob(KER, '%s:%s' % (TAG, f)) or b'').decode('utf-8', 'replace') for f in OWN} if tagc else {},
        kpush=rd('b600_kernel_push_out.txt'), bpush=rd('b600_branch_push_out.txt'),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b599*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b600_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b600_mustnotexist.txt')), table_changed=None,
        fj=jl('b600_findings.json'), tj=jl('b600_trail.json'), sc=jl('b600_scores.json'), desk=rd('b600_desk_notes.txt'),
        wl1=jl('b600_weight_line.json'), rl=jl('b600_rule_lines.json'),
        st=jl('b600_statements_prod.json'), stxt=rd('b600_statements_prod.txt'), pr=jl('b600_prints.json'),
        ep=jl('b600_e0_prod.json'), es=jl('b600_e0_salt.json'), gp=jl('b600_grep.json'), br=jl('b600_bearing.json'),
        builds={k: rd('b600_build_%s.txt' % k) for k in ('prod', 'salt', 'axiom')},
        PZ=jl('b600_page_zeta.json'), PX=jl('b600_page_chi.json'), arms_c2=rd('b600_page_arms_c2.txt'),
        nodes=rd('b600_nodes_zeta.txt'), nodes596=rd('b596_nodes_faces.txt'),
    )
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
    X['gcp_zeta'] = GCP.arm(os.path.join(D, 'b600_nodes_zeta.txt'), os.path.join(SP, '_b600_gcp'), os.path.join(D, 'b600_probe_out.txt')) \
        if os.path.exists(os.path.join(D, 'b600_probe_out.txt')) else dict(ok=False)
    X['gcp_chi'] = GCP.arm(os.path.join(D, 'b596_nodes_chi.txt'), os.path.join(SP, '_b600_gcp'), os.path.join(D, 'b596_chi_probe_out.txt'))
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


def weight_ok(S):
    ls = S['wl1'].get('lines', [])
    if len(ls) != 1:
        return False
    a = fline(S, ls[0]['line'])
    return a.startswith(ls[0]['head']) and '(:6928)' in a and 'b599 AT ITS WEIGHT' in a and 'ad82d5e' in a and '31d4fa4' in a \
        and 'E-2026-10-02-1' in a and '79 of 79' in a and ls[0]['line'] > 6944


def amend_ok(S):
    ls = S['rl'].get('lines', [])
    if len(ls) != 2 or S['rl'].get('addressed') != 12288:
        return False
    a = oline(S, ls[0]['line'])
    return a.startswith(ls[0]['head']) and '(:12288)' in a and 'the browser clause is struck' in a and 'HOLD_MB' in a \
        and 'one page per call in the foreground' in a and 'recorded as a stop, not an OOM' in a and 'No line is added for the network' in a \
        and oline(S, 12288).startswith(S['REC'].GEN_LINE) and ls[0]['line'] > 12348


def authority_ok(S):
    ls = S['rl'].get('lines', [])
    if len(ls) != 2:
        return False
    a = oline(S, ls[1]['line'])
    return a.startswith(S['REC'].AUTH_HEAD) and 'A PLACE TO STAND research programme' in a and 'the ledgers on D: are newer than any mirror' in a \
        and 'not from the mirror where a newer edition exists' in a and ls[1]['line'] > ls[0]['line']


def work_order_printed(S):
    wo = oline(S, 12136)
    return bool(wo) and wo.startswith('*Appended 2026-10-01 by b589 to W-ORD-GRH-WEIL (:11373)') and ('    :12136  ' + wo) in S['reads'] \
        and 'Trigger: the author' in wo


def statement_ok(S):
    it = S['st'].get('items') or []
    return len(it) == len(S['REC'].ITEMS) and all(i['in_work_order'] and i['declared'] for i in it) \
        and 'EVERY ITEM OF THE STATEMENT CARRIED BY A DECLARATION' in S['stxt'] and S['st'].get('file') == 'SIDEExplicitFormula/Product.lean'


def house_form(S):
    src = S['ksrc']
    if sorted(src) != OWN or not all(src.values()):
        return False
    for f in ('SIDEExplicitFormula/Product.lean', 'SIDEExplicitFormula/SaltCheckProduct.lean'):
        t = src[f]
        if not (t.startswith('/-\nSIDE-explicit-formula -- %s\n' % f) and "THIS PROGRAMME'S WORK (act b600" in t and '`theorem`, never `lemma`' in t
                and 'NOT VENDORED' in t):
            return False
        if re.search(r'^\s*lemma\s', t, re.M) or re.search(r'\bsorry\b', strip_lean(t)) or 'native_decide' in strip_lean(t):
            return False
    a = src['AxiomCheckProduct.lean']
    return a.startswith('import SIDEExplicitFormula.Product\nimport SIDEExplicitFormula.SaltCheckProduct\n') and '#print axioms ' + THE_NODE in a


def strip_lean(t):
    t = re.sub(r'/-[\s\S]*?-/', '', t)
    return NL.join(l.split('--', 1)[0] for l in t.split(NL))


def prints_ok(S):
    ax = S['pr'].get('axioms') or {}
    decl = list((S['ep'].get('rows') or {}).keys()) + list((S['es'].get('rows') or {}).keys())
    return bool(ax) and bool(decl) and all(n in ax for n in decl) and all(set(v) <= STD3 for v in ax.values()) and not S['pr'].get('sorry') \
        and S['pr'].get('errors') == 0 and S['pr'].get('std3') is True and 'rc=0' in (S['pr'].get('exit') or '')


def e0_ok(S):
    r = S['ep'].get('rows') or {}
    return S['ep'].get('gate') is True and S['es'].get('gate') is True and r.get(THE_NODE, {}).get('grade') == 'DERIVES' \
        and r.get(NS + 'sum_ef', {}).get('grade') == 'DERIVES' and S['ep'].get('same_file') is True and S['es'].get('same_file') is True \
        and S['ep'].get('tip', '').startswith(S['ktag'][:7] or '#')


def salt_ok(S):
    r = S['es'].get('rows') or {}
    txt = S['pr'].get('text') or ''
    return all(r.get(n, {}).get('std3') and r.get(n, {}).get('grade') == 'DERIVES' for n in SALT) and all((n + ' :') in txt for n in SALT)


def grep_ok(S):
    gp = S['gp']
    rows = gp.get('rows') or []
    return gp.get('bad') == [] and bool(rows) and all((gp.get('controls') or {}).values()) and len(gp.get('controls') or {}) == 4 \
        and any(r['cls'] == 'OWN' and r['name'] == 'productLemma_holds' for r in rows) and len(gp.get('kernels') or []) > 40


def tagged_ok(S):
    t = S['ktag']
    return bool(t) and S['kmain'] == t and S['kanc'] and ('push_gated: main read back at the remote: %s' % t) in S['kpush'] \
        and ('push_gated: tag %s peeled local %s remote %s' % (TAG, t, t)) in S['kpush'] and 'push_gated: DONE -- main and 1 tag(s) pushed and read back' in S['kpush']


def kfiles_ok(S):
    return S['kfiles'] == OWN and S['kmerges'] == []


def branch_ok(S):
    t = S['ktag']
    return bool(t) and S['kbranch'] == t and ('%s local %s remote %s' % (BRANCH, t, t)) in S['bpush']


def hold_ok(S):
    for k in ('prod', 'salt', 'axiom'):
        m = re.search(r'free MB before: (\d+)', S['builds'][k])
        if not (m and int(m.group(1)) >= 2560 and re.search(r'^### EXIT rc=0 ', S['builds'][k], re.M)):
            return False
    return (S['PZ'].get('free_mb_before') or 0) >= 2560


def page_zeta_ok(S):
    z = S['PZ']
    new = {x['name']: x for x in z.get('new') or []}
    a, b, c = S['pages'][PAGE]
    return z.get('rc') == 0 and z.get('changed') is True and sorted(new) == sorted(NEW_NODES) and new[THE_NODE].get('grade') == 'DERIVES' \
        and bool(z.get('rows', {}).get(THE_NODE)) and bool(a) and a == c and a != b and hashlib.sha256(c).hexdigest() == z.get('sha256') \
        and all(('`%s`' % n) in c.decode('utf-8') or n in c.decode('utf-8') for n in NEW_NODES)


def page_chi_ok(S):
    a, b, c = S['pages'][DIR_PAGE]
    return S['PX'].get('rc') == 0 and S['PX'].get('changed') is False and bool(b) and a == b == c


def pages_alone(S):
    c = [h for h, f in S['pp_files'].items() if PAGE in f]
    return len(c) == 1 and S['pp_files'][c[0]] == [PAGE] and dict(S['pp_log'])[c[0]].startswith('b600 (R210)(4): ' + PAGE) \
        and not [h for h, f in S['pp_files'].items() if DIR_PAGE in f]


def node_list_ok(S):
    n, o = S['nodes'].rstrip(NL).split(NL), S['nodes596'].split(NL)
    body = [l for l in o if l.strip()]
    return bool(body) and '# pin: v0.18' in n and '# pin: v0.17' not in n and all(x in n for x in S['REC'].NODE_ADD) \
        and n[-2] == S['REC'].NODE_ADD[-1] and n[-1] == body[-1] and all((('# pin: v0.18' if l == '# pin: v0.17' else l) in n) for l in body)


def bearing_ok(S):
    rows = S['br'].get('rows') or []
    return [(r['path'], r['line']) for r in rows] == [(GRH, 45), (SIMP, 290)] and all(r['found'] for r in rows) \
        and all(S['bear_now'].get((r['path'], r['line'])) == r['sentence'] for r in rows) and all(len(r['reading']) > 200 for r in rows) \
        and all('productLemma_holds' in r['reading'] or 'product_part_load_bearing' in r['reading'] for r in rows)


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 18]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') and fline(S, e).startswith('## REMAINDER 5: the product lemma as a salt-checked Prop at SIDE-explicit-formula v0.18') \
        and '**The lemma**' in tail and '**Its bearing**' in tail and '**Read in mutual light**' in tail and 'strengthens' in tail \
        and (S['ktag'][:7] or '#') in tail and 'GRH_CASCADE v0.3.6 :45' in tail and 'SIMPLICITY_OF_RIEMANN_ZEROS v1.1.3 :290' in tail


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


def _h34(S, k):
    v = S['sc'].get(k)
    return bool(v) and v[0] in ('HOLDS', 'REFUTED') and ('(%s)' % k.upper()) in S['desk']


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R210) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-STEPZERO-CENSUS', 'the two censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'cens', S['cens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 1'))),
    ('G-STEPZERO-PINS', 'the pins', lambda S: '### REPOS HARD-FAILING : 0' in S['pins0'],
     lambda S: put(S, 'pins0', S['pins0'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-PROCS', 'the process listing', lambda S: 'powershell.exe' in S['procs'] and '### ORPHANS:' in S['procs'] and '\\v1.0\\' in S['procs']
     and not re.search(r'^\s*\d+\s+\d+\s+(lean|lake|grep|du|find|rg|head|cut|python)\.exe', S['procs'], re.M),
     lambda S: put(S, 'procs', S['procs'] + '\n  1234   5678 grep.exe  grep x\n')),
    ('G-REG-LOCKED-FIRST', 'the lock time against the step-zero commit and every later commit', lambda S: S['lock_epoch'] is not None
     and any(l.startswith(STEPZERO) and int(l.split()[1]) < S['lock_epoch'] for l in S['before_lock'])
     and all(int(l.split()[1]) > S['lock_epoch'] for l in S['before_lock'] if not l.startswith(STEPZERO)), lambda S: put(S, 'lock_epoch', 1)),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 7'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b599`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b599' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b600 -- x'])),
    ('G-R210-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R210) END' in S['ferry'] and S['ot'].count('**(R210) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R210) ratified', '(R210) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in (
        'OPEN_TRAILS.md @ bc1337a', 'FINDINGS.md @ bc1337a', 'data/b589_product_price.txt @', 'SIDEExplicitFormula/Schema/Config.lean @ 5a1630b8',
        'SIDEExplicitFormula/Schema/Converse.lean @ 5a1630b8', 'Zeta23/WeilEF/ZeroSummability.lean @ 5a1630b8', 'SIDEExplicitFormula/Simplicity.lean @',
        'SIDEExplicitFormula/SaltCheckSimplicity.lean @', 'AxiomCheckSimplicity.lean @', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md @ bc1337a',
        'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md @ bc1337a', GRH + ' @ bc1337a', SIMP + ' @ bc1337a', 'data/b599_closing_push_out.txt @',
        "chain_page.py`s hold: ['HOLD_MB = 2560']"))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-WORK-ORDER-PRINTED', 'OPEN_TRAILS :12136 against the reads bank: the work-order printed whole', lambda S: work_order_printed(S),
     lambda S: put(S, 'reads', S['reads'].replace('    :12136  ' + oline(S, 12136), '    :12136  ' + oline(S, 12136)[:400]))),
    ('G-ANSWERS-BANKED', 'the act`s answers bank: every prompt with its options and recommended mark verbatim, or none',
     lambda S: S['answers'].startswith('### b600 -- THE AUTHOR`S ANSWERS') and S['answers'].count('### PROMPT ') == S['answers'].count('\nRESULT ')
     and (S['answers'].count('### PROMPT ') > 0 or '### NONE: no prompt was put' in S['answers']),
     lambda S: put(S, 'answers', S['answers'].replace('### b600 -- THE AUTHOR', '### b6OO -- THE AUTHOR', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay 92b1c086`s files', lambda S: S['pushout'][0] == ['data/b599_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/b599_closing_push_out.txt', 'x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b599') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b599'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'simplicity-b596': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80 and every PLACE-papers read at ba5f0ea, run afresh through the test`s control()',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(S['ctl'][0], ok=False)] + S['ctl'][1:])),
    ('G-INSTRUMENTS-UNEDITED', 'b599`s sealed suite, the control`s test file, the generator, its arm, the E0 rule and the push gate against 2b9f75cd',
     lambda S: all(bool(a) and a == b for a, b in S['inst'].values()) and len(S['inst']) == 6,
     lambda S: put(S, 'inst', dict(S['inst'], **{'e0_rule.py': (S['inst']['e0_rule.py'][0], (S['inst']['e0_rule.py'][1] or b'') + b'x')}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b599`s weight, addressed to its entry', lambda S: weight_ok(S),
     lambda S: put(S, 'wl1', dict(S['wl1'], lines=[]))),
    ('G-AMENDMENT', 'OPEN_TRAILS at the banked line: the generator-run line amended, addressed to :12288, appended past the pre-act end',
     lambda S: amend_ok(S), lambda S: put(S, 'rl', dict(S['rl'], addressed=12289))),
    ('G-AUTHORITY-LINE', 'OPEN_TRAILS at the banked line: the authority order, standing', lambda S: authority_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('the ledgers on D: are newer than any mirror', 'the ledgers are newer'))),
    ('G-STATEMENT-AGAINST-WORK-ORDER', 'the statements bank: every item of the work-order`s statement carried by a declaration of Product.lean',
     lambda S: statement_ok(S), lambda S: put(S, 'st', dict(S['st'], items=(S['st'].get('items') or [])[:-1]))),
    ('G-HOUSE-FORM', 'the three kernel files at the tag: the head, the rule line, no lemma, no sorry, no native_decide, the audit`s imports',
     lambda S: house_form(S), lambda S: put(S, 'ksrc', dict(S['ksrc'], **{OWN[1]: S['ksrc'].get(OWN[1], '') + '\nlemma x : True := trivial\n'}))),
    ('G-HOLD-READ', 'the three build logs and the ζ page run: free memory read above the hold before each Lean call, each exit 0',
     lambda S: hold_ok(S), lambda S: put(S, 'PZ', dict(S['PZ'], free_mb_before=2000))),
    ('G-PRINTS-STD3', 'the axiom audit`s prints: every declaration of both files printed, each at the standard three or less, no sorryAx, no error',
     lambda S: prints_ok(S), lambda S: put(S, 'pr', dict(S['pr'], axioms=dict(S['pr'].get('axioms') or {}, **{THE_NODE: ['sorryAx']})))),
    ('G-E0-GATES', 'the E0 reads at the tip: both gates, productLemma_holds and sum_ef DERIVES, the files the printed ones', lambda S: e0_ok(S),
     lambda S: put(S, 'ep', dict(S['ep'], gate=False))),
    ('G-SALT-CHECK', 'the salt-check`s three theorems: DERIVES at the standard three, each #check printed', lambda S: salt_ok(S),
     lambda S: put(S, 'es', dict(S['es'], rows={k: v for k, v in (S['es'].get('rows') or {}).items() if k != SALT[1]}))),
    ('G-FED-GREP', 'the federation walk: no declaration outside the act`s files concluding the Prop or its negation; the strict shapes exercised',
     lambda S: grep_ok(S), lambda S: put(S, 'gp', dict(S['gp'], bad=[{'cls': 'CONCLUDES'}]))),
    ('G-KERNEL-TAGGED', 'SIDE-explicit-formula: main and the peeled tag, the push capture`s read-back', lambda S: tagged_ok(S),
     lambda S: put(S, 'kpush', S['kpush'].replace('read back at the remote', 'read'))),
    ('G-KERNEL-FILES-ONLY', 'SIDE-explicit-formula 5a1630b..v0.18: the three files, no merge commit', lambda S: kfiles_ok(S),
     lambda S: put(S, 'kfiles', S['kfiles'] + ['README.md'])),
    ('G-BRANCH-KEPT-PUSHED', 'the working branch at the tag, pushed by name and read back', lambda S: branch_ok(S),
     lambda S: put(S, 'kbranch', '0' * 40)),
    ('G-NODE-LIST', 'the ζ node list against b596`s: every line carried, the pin moved, the five nodes before the backmatter record', lambda S: node_list_ok(S),
     lambda S: put(S, 'nodes', S['nodes'].replace('# pin: v0.18', '# pin: v0.17'))),
    ('G-PAGE-ZETA-NODES', 'the ζ page at HEAD and its bank: re-emitted at v0.18, the five nodes on it, productLemma_holds DERIVES', lambda S: page_zeta_ok(S),
     lambda S: put(S, 'PZ', dict(S['PZ'], new=[x for x in S['PZ'].get('new') or [] if x.get('name') != THE_NODE]))),
    ('G-PAGE-CHI-UNCHANGED', 'the χ page on disk and at HEAD against bc1337a, its re-emission unchanged', lambda S: page_chi_ok(S),
     lambda S: put(S, 'PX', dict(S['PX'], changed=True))),
    ('G-PAGES-COMMITTED-ALONE', 'PLACE-papers` log since bc1337a: the ζ page in one commit of its own, no χ page commit', lambda S: pages_alone(S),
     lambda S: put(S, 'pp_files', {h: (f + ['FINDINGS.md'] if PAGE in f else f) for h, f in S['pp_files'].items()})),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from this act`s list and v0.18 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b596`s χ list and v0.17 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank after the page commit: both page arms and the frozen control', lambda S: 'PAGE ARMS PASSING : 2 of 2' in S['arms_c2']
     and ('%s PASSING : 2 of 2' % CONTROL_ARM) in S['arms_c2'], lambda S: put(S, 'arms_c2', S['arms_c2'].replace('PASSING : 2 of 2', 'PASSING : 1 of 2'))),
    ('G-BEARING', 'the bearing bank against each keystone at PLACE-papers HEAD: the two sentences on their cited lines, the reading beside each',
     lambda S: bearing_ok(S), lambda S: put(S, 'bear_now', {k: v + 'x' for k, v in S['bear_now'].items()})),
    ('G-H34A-SCORED', 'the scores and the desk', lambda S: _h34(S, 'H34a'), lambda S: put(S, 'desk', '')),
    ('G-H34B-SCORED', 'the scores and the desk', lambda S: _h34(S, 'H34b'), lambda S: put(S, 'sc', dict(S['sc'], H34b=['x', '']))),
    ('G-H34C-SCORED', 'the scores and the desk', lambda S: _h34(S, 'H34c'), lambda S: put(S, 'sc', dict(S['sc'], H34c=['x', '']))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD,
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and 'beneath :12288' in trail(S) and 'ζ page' in trail(S), lambda S: put(S, 'ot', S['ot'].replace('Resolved by the seat, for the author’s strike', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b601, W-ORD-KEIPER-FACE (two lemmas)' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b601, W-ORD-KEIPER-FACE (two lemmas)', 'x'))),
    ('G-KERNELS-UNTOUCHED', 'every other kernel`s main, the explicit-formula checkout on main at the tag and clean, the trial branch',
     lambda S: all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['kcur'] == 'main' and S['kdirty'] == ''
     and bool(S['ktag']) and S['kmain'] == S['ktag'] and S['trial'] == 'f22ff35', lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-kernel': '0'}))),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('36352a0', '36352a0', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b600_record.py'): S['tooltext'].get(os.path.join(T, 'b600_record.py'), '') + NL + 'os' + '.remove(p)'}))),
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
     lambda S: put(S, 'keystone_changes', [GRH])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 2b9f75cd, by blob id', lambda S: S['prior_bad'] == []
     and S['prior_n'] > 6000, lambda S: put(S, 'prior_bad', ['data/b599_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', PAGE]),
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + [DIR_PAGE]))),
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
                                                                          and "startswith('b600')" in S['suite'] and "data/b600_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b600')", ''))),
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
    rec('b600 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('PRE-SEAL (R202)(3)' if PRERUN else 'POST-PUSH' if pushed else 'PRE-PUSH'))
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
        out = os.path.join(D, 'b600_arms_prerun.txt')
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b600_checks_postpush.txt' if pushed else 'b600_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    if not (RERUN or PRERUN):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b600_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
