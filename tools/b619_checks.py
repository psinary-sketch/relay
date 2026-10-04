# -*- coding: utf-8 -*-
"""b619_checks.py -- THE SUITE OF b619, UNDER (R229): THE_KEYSTONE_CENSUS AT v0.4 -- THE SIX SYNTHESES NAMED IN THEIR ROWS WITH TIERS,
THE EDITION, KERNEL-TAG AND SIEVE COLUMNS REFRESHED; THE N5 SCORER'S STANDING REPAIR.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`, `--mid <name>` or `--prerun`; it writes data/b619_checks.txt before the push and
### data/b619_checks_postpush.txt after it; `--mid <name>` (the whole suite re-run after Component 4, as (R229) orders) writes
### data/<name> and regenerates nothing. `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the face is sealed,
### no table regenerated, its counts written to data/b619_arms_prerun.txt. ### Every remote is read once per run (OPEN_TRAILS :12703,
### b616_claims.remote_refs) -- the kernels' tags among them -- each run's ls-remote calls banked per repository beside its output
### (data/b619_lsr*.json); G-LSREMOTE-ONE-PER-REPO runs last.
### ### The harness is b568's to b618's, carried from tools/b618_checks.py (its imports, helpers, regenerate and main); the sources,
### predicates and arms are b619's. The control arm is the frozen one of (R207)(2). Every positive control mutates a line whose text occurs
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
FACE = os.path.join(D, 'b619_registration_2026-10-04.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
CEN3, CEN4 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_3.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md'
PRE = dict(relay='fda4e81b', pp='9dbac4b', gs='3528bcf', ker='1d5d4dd')
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-explicit-formula': '1d5d4dd9', 'SIDE-global-section': '3528bcfc',
             'SIDE-spinor': '520abe7a'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b', 'product-b600': '1dd5cd7',
        'doubling-keiper-b601': '5fc0c87', 'sign-window-b602': '914c413', 'family-b603': '1d5d4dd'}
STEPZERO = 'db0aaa5b'
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/a7f90da7-bccd-48d0-914d-84e76892ff54/scratchpad'
SCORER_EDIT = 'b619 (R229)(2): the N5 scorer'
SCORER_SEALED = 'b619 (R229)(2): the record tool as sealed'


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b619')
            and 'data/b619_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    p = os.path.join(SP, '_b619_suite_scan_%s.md' % name)
    open(p + '.tmp', 'wb').write(text.encode('utf-8'))
    os.replace(p + '.tmp', p)
    return subprocess.run([sys.executable, os.path.join(T, 'banned_terms.py'), '--new', p], capture_output=True, text=True,
                          encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8')).stdout


def remotes_now(kernels):
    """### each kernel's tags read now, ONE `git ls-remote origin` per repository (b616_claims.remote_refs), in b610's shape"""
    C = KC0  # noqa: F841
    import b619_census as K
    out = {}
    for k in kernels:
        path = 'D:/' + k
        refs = KC0.remote_refs(path)
        tags = {}
        for r, h in refs.items():
            if r.startswith('refs/tags/'):
                nm = r[len('refs/tags/'):]
                if nm.endswith('^{}'):
                    tags.setdefault(nm[:-3], {})['peeled'] = h
                else:
                    tags.setdefault(nm, {})['obj'] = h
        rt = dict(repo=k, ok=bool(refs), err='' if refs else 'no read', tags={a: b.get('peeled', b.get('obj')) for a, b in tags.items()})
        ct = K.C.current_tag(rt) if rt['ok'] else None
        rt['current'] = ct
        rt['remote_peel'] = rt['tags'].get(ct) if ct else None
        rt['local_peel'] = K.C.local_peel(k, ct) if ct else None
        rt['local_only'] = [list(x) for x in K.C.local_only_tags(k, rt)]
        out[k] = rt
    return out


def sources():
    import b619_record as REC
    import b619_census as K
    import b616_record as R6
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b619_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b619_') and f.endswith('.py'))
    S = dict(
        REC=REC, K=K, face=face, ferry=rd('b619_ferry.txt'), scan=rd('b619_ferry_scan.txt'), cens=rd('b619_census_stepzero.txt'),
        fcens=rd('b619_faces_census_stepzero.txt'), pins0=rd('b619_pins_stepzero.txt'), procs=rd('b619_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b618_closing.txt'), reads=rd('b619_reads.txt'), branches=rd('b619_branches.txt'), answers=rd('b619_author_answers.txt'),
        prerun=rd('b619_arms_prerun.txt'), defects=rd('b619_defects.txt'),
        mapping=rd('b619_census.txt'), CJ=jl('b619_census.json'), EJ=jl('b619_edition.json'), H28=jl('b619_h28.json'), H53=jl('b619_h53.json'),
        edbank=rd('b619_edition_CENSUS.txt'), repin=rd('b619_repin.txt'), T5=jl('b619_test_n5.json'), t5txt=rd('b619_test_n5.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))))
              for f in ('b618_checks.py', 'b618_record.py', 'b610_census.py', 'b610_record.py', 'b616_record.py', 'b616_claims.py', 'b604_record.py',
                        'b602_record.py', 'b560_record.py', 'b566_record.py', 'test_chain_page_b596.py', 'chain_page.py', 'e0_rule.py', 'g_chain_page.py',
                        'push_gated.sh', 'banned_terms.py', 'b558_record.py', 'terminal_table.py', 'errata_append.py')},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        readme=(cr0(raw(os.path.join(PP, 'README.md'))), cr0(blob(PP, PRE['pp'] + ':README.md'))),
        errata=(cr0(raw(os.path.join(PP, 'ERRATA.md'))), cr0(blob(PP, PRE['pp'] + ':ERRATA.md'))),
        ed_disk=cr0(raw(os.path.join(PP, *CEN4.split('/')))), ed_head=cr0(blob(PP, 'HEAD:' + CEN4)),
        v3=cr0(blob(PP, PRE['pp'] + ':' + CEN3)),
        currents={p: (cr0(raw(os.path.join(PP, *p.split('/')))), cr0(blob(PP, PRE['pp'] + ':' + p)), cr0(blob(PP, 'HEAD:' + p))) for p in REC.CURRENTS},
        pages={p: (cr0(raw(os.path.join(PP, p))), cr0(blob(PP, PRE['pp'] + ':' + p)), cr0(blob(PP, 'HEAD:' + p))) for p in (PAGE, DIR_PAGE)},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        corr_pre=cr0(blob(GS, PRE['gs'] + ':CORRESPONDENCE.md')), corr_now=cr0(raw(os.path.join(GS, 'CORRESPONDENCE.md'))),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        kern_face=(jl('b619_kernels_face.json').get('kernels') or {}),
        lv_head=gs('D:/SIDE-lv-conservation', 'rev-parse', 'HEAD'), lv_dirty=gs('D:/SIDE-lv-conservation', 'status', '--porcelain', '--untracked-files=no'),
        trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain', '--untracked-files=no'),
        ktags=sorted(x for x in gs(KER, 'tag', '-l', 'v0.*').split(NL) if x.strip()),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b618*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b619_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b619_mustnotexist.txt')), table_changed=None,
        fj=jl('b619_findings.json'), tj=jl('b619_trail.json'), sc=jl('b619_scores.json'), desk=rd('b619_desk_notes.txt'),
        rl=jl('b619_record_lines.json'), PZ=jl('b619_page_zeta.json'), PX=jl('b619_page_chi.json'), arms_c2=rd('b619_page_arms_c2.txt'),
        lsr=None,
        rec_head=cr0(blob(ROOT, 'HEAD:tools/b619_record.py')),
        rlog=[l.split(' ', 1) for l in gs(ROOT, 'log', '--format=%h %s', PRE['relay'] + '..HEAD', '--', 'tools/b619_record.py').split(NL) if l.strip()],
    )
    S['kern_now'] = {k: list(v) for k, v in REC.kern_state(list(S['kern_face'])).items()} if S['kern_face'] else {}
    S['written'] = written_files(lock_epoch or 0)
    S['globs'] = wl_globs(face)
    S['nd_sets'] = R6.nd_sets()
    pub = []
    for nm, pre, now in (('FINDINGS', S['fi_pre'], S['fi_now']), ('OPEN_TRAILS', S['ot_pre'], S['ot_now'])):
        pub.append((now or b'')[len(pre or b''):].decode('utf-8', 'replace') if now and pre and now.startswith(pre) else '')
    pub.append((S['ed_disk'] or b'').decode('utf-8', 'replace'))
    for f in sorted(os.listdir(D)):
        if f.startswith(('b619_', 'audit_b619_')):
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
    # ### the census rendered now: REGISTRY and the documents at the pins, the kernels' tags read now, once per repository
    B = K.build(read_remotes=False)
    kern = sorted(set(x for row in B['J'] for x in row['kernel_src']))
    S['remotes'] = remotes_now(kern)
    for row in B['J']:
        row['kernels'] = K.ker_cell(row['kernel_src'], S['remotes'])
        row['table_line'] = K.table_line(row)
    S['J_now'] = B['J']
    S['facts'] = K.syn_facts()
    S['ed_text'] = (S['ed_disk'] or b'').decode('utf-8', 'replace')
    S['ed_scan'] = _scan_bytes(S['ed_text'], 'edition') if S['ed_text'] else ''
    S.update(extra_sources(S))
    return S


def extra_sources(S):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    X = {}
    X['gcp_zeta'] = GCP.arm(os.path.join(D, 'b602_nodes_zeta.txt'), os.path.join(SP, '_b619_gcp'), os.path.join(D, 'b602_probe_out.txt'))
    X['gcp_chi'] = GCP.arm(os.path.join(D, 'b603_nodes_chi.txt'), os.path.join(SP, '_b619_gcp'), os.path.join(D, 'b603_chi_probe_out.txt'))
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


def weight_ok(S):
    x = (S['rl'].get('lines') or [{}])[0]
    a = fline(S, x.get('line'))
    return bool(x) and x.get('file') == 'FINDINGS.md' and a.startswith(x['head']) and '(:7386)' in a and 'b618 AT ITS WEIGHT' in a \
        and 'The suite 77 of 78 before the push and 77 of 78 after it' in a and 'INSTRUMENTS’ ids I-16 to I-39' in a \
        and 'fold into the table at next hand edit' in a and 'OPEN_TRAILS :12280 as b596’s answer' in a and ':12797 the proper repair' in a \
        and x['line'] > 7386


def standing_ok(S):
    x = (S['rl'].get('lines') or [{}, {}])[1:2]
    x = x[0] if x else {}
    a = oline(S, x.get('line'))
    return bool(x) and x.get('file') == 'OPEN_TRAILS.md' and a.startswith(S['REC'].N5_HEAD) and '(:12356)' in a \
        and 'takes the trail record’s expected line on OPEN_TRAILS as a parameter' in a and 'expects the same verdict' in a and x['line'] > 12797


def mapping_ok(S):
    t, J = S['mapping'], S['CJ']
    ch = J.get('changes') or []
    return t.startswith('b619 -- COMPONENT 2: THE MAPPING') and '### PART B --' in t and '### PART C --' in t and bool(ch) \
        and all(('      %-9s v0.4: %s' % ('', c['new'])) in t for c in ch) and ('### ### **CELLS CHANGED : %d, in ' % len(ch)) in t \
        and all(('### ### **%s HOLDS**' % k) in t for k in ('H53a', 'H53b', 'H53c'))


def mapping_first(S):
    a, b = iso_epoch(S['CJ'].get('at', '')), iso_epoch(S['EJ'].get('at', ''))
    ts = [int(gs(PP, 'log', '-1', '--format=%ct', h)) for h, f in S['pp_files'].items() if CEN4 in f]
    return a is not None and b is not None and a < b and bool(ts) and a < min(ts)


def edition_written(S):
    d, h = S['ed_disk'], S['ed_head']
    return bool(d) and d == h and hashlib.sha256(d).hexdigest() == S['EJ'].get('sha256') and S['EJ'].get('dry') is False


def edition_alone(S):
    c = [x for x, f in S['pp_files'].items() if CEN4 in f]
    return len(c) == 1 and S['pp_files'][c[0]] == [CEN4] and dict(S['pp_log'])[c[0]].startswith(S['REC'].EDITION_PREFIX)


def carries(S):
    REC = S['REC']
    cur = lines_of(S['v3'])
    ed = (S['ed_text'] or '').split(NL)
    E = S['EJ']
    if not E or not cur or not ed:
        return False
    import b619_record as R
    ok, bad = R._carried(cur, ed, E)
    return bad == [] and ok == sum(1 for l in cur if l.strip()) and REC is R


def cells_now(S):
    rows = S['REC']._v4_rows(S['ed_text'])
    return len(rows) == 23 and all(rows.get(r['n'], {}).get('n') == r['n'] and ('| %s | ' % r['n']) + ' | '.join(rows[r['n']][c] for c in (
        'label', 'documents', 'keystones', 'editions', 'sieve', 'kernels', 'deposit')) + ' |' == r['table_line'] for r in S['J_now'])


def section2_ok(S):
    t = S['ed_text']
    return S['REC']._v4_section2(t) == ['R22'] and S['REC'].ANNEX4 in t and S['REC'].NK_LINE4 in t \
        and '1 of the census’s 23 rows holds documents and no keystone' in t


def h53_now(S):
    return S['REC'].h53_readback(S['ed_text'], S['remotes'], S['facts'])


def syn_ok(S):
    R = h53_now(S)
    return R['H53a'] == 'HOLDS' and S['H53'].get('H53a') == 'HOLDS'


def tags_ok(S):
    R = h53_now(S)
    return R['H53c'] == 'HOLDS' and S['H53'].get('H53c') == 'HOLDS' and len(R['unpushed']) <= 9 and all(k in S['K'].TAG_REMOTES for k in R['unpushed'])


def repin_ok(S):
    pos = S['EJ'].get('pos') or {}
    ed = (S['ed_text'] or '').split(NL)
    good = all(0 < v <= len(ed) and ed[v - 1].strip() for v in pos.values()) and all(ed[pos[r] - 1].startswith('| %s | ' % r) for r in pos if re.fullmatch(r'R\d\d', r))
    return good and bool(pos) and re.search(r'RE-PIN : (\d+) of \1 citations hold', S['repin']) is not None and '{E:' not in S['ed_text']


def ed_scan_ok(S):
    return re.search(r'^\s*VERDICT\s*: CLEAN\s*$', S['ed_scan'], re.M) is not None and re.search(r'live uses\s*: 0\b', S['ed_scan']) is not None


def h28_ok(S):
    H = S['H28']
    return (H.get('H28a'), H.get('H28b'), H.get('H28c')) == ('HOLDS',) * 3 and H.get('carried_bad') == [] and '### ### **THE CENSUS LANDS: NO SENTENCE HELD.**' in S['edbank'] \
        and '(H53D)' in S['desk']


def _h(S, k, want):
    return (S['sc'].get(k) or [''])[0] == want and ('(%s)' % k.upper()) in S['desk'] and ('### **%s.**' % want) in S['desk']


def h53x_ok(S, k):
    R = h53_now(S)
    want = {'H53a': R['H53a'], 'H53b': R['H53b'], 'H53c': R['H53c'],
            'H53d': 'HOLDS' if (S['H28'].get('H28a'), S['H28'].get('H28b'), S['H28'].get('H28c')) == ('HOLDS',) * 3 else 'REFUTED'}[k]
    return _h(S, k, want)


def scorer_repaired(S):
    sealed = [h for h, s in S['rlog'] if s.startswith(SCORER_SEALED)]
    edit = [h for h, s in S['rlog'] if s.startswith(SCORER_EDIT)]
    m = re.search(r'b619_record\.py sha256 ([0-9a-f]{64})', S['face'])
    if len(sealed) != 1 or len(edit) != 1 or not m:
        return False
    sb = cr0(blob(ROOT, '%s:tools/b619_record.py' % sealed[0]))
    order = [h for h, _s in S['rlog']][::-1]
    return hashlib.sha256(sb).hexdigest() == m.group(1) and files_of(ROOT, sealed[0]) == ['tools/b619_record.py'] \
        and set(files_of(ROOT, edit[0])) <= {'tools/b619_record.py', 'tools/b619_test_n5.py', 'data/b619_test_n5.txt', 'data/b619_test_n5.json'} \
        and order.index(sealed[0]) < order.index(edit[0]) and b'def n5(trail_line' in (S['rec_head'] or b'')


def n5_test_ok(S):
    T5 = S['T5']
    runs = T5.get('runs') or []
    st = [r.get('stage') for r in runs]
    return T5.get('same') is True and all(x in st for x in ('c4-before', 'c4-after', 'c6-before', 'c6-after')) \
        and len(set(r.get('verdict') for r in runs if r.get('form') == 'repaired')) == 1 and '### ### **THE N5 TEST : THE SAME VERDICT' in S['t5txt']


def unedited_all(S):
    return all(bool(b) and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(S['REC'].CURRENTS)


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
            out.append(len(c) == 1 and S['pp_files'][c[0]] == [p] and dict(S['pp_log'])[c[0]].startswith('b619 (R229): ' + p))
        else:
            out.append(z.get('changed') is False and not [h for h, f in S['pp_files'].items() if p in f])
    return all(out) and bool(S['PZ']) and bool(S['PX'])


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 20]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') and fline(S, e).startswith('## THE_KEYSTONE_CENSUS at v0.4: the six syntheses in their rows with tiers') \
        and all(x in tail for x in ('**The edition**', '**The record lines.**', '**The scores.**', '**Read in mutual light**', 'strengthens', '**Next.**',
                                    'the ANNEX alone', 'b620'))


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
        and S['lv_dirty'] == '' and len(S['kern_face']) >= 30 and S['kern_face'] == S['kern_now']


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


def _mut_ed(S, old, new):
    return put(S, 'ed_text', (S['ed_text'] or '').replace(old, new, 1))


READ_NEEDLES = ('THE_KEYSTONE_CENSUS_v0_3.md @ 9dbac4bd (314 lines cited', 'THE_FOUR_PRESENTATIONS_OF_THE_MECHANISM_EXCLUSION.md @ 9dbac4bd',
                'THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md @ 9dbac4bd', 'THE_SILENCE_PRINCIPLE_AND_INTERFACE_DARKNESS.md @ 9dbac4bd',
                'THE_CONSTANTS_v0_2.md @ 9dbac4bd', 'ELLIPTIC_CURVES.md @ 9dbac4bd', 'THE_LOCAL_COSMIC_INTERFACE_AND_THE_DARK_SECTOR.md @ 9dbac4bd',
                'THE_FINDINGS_AS_THEY_STAND_v0_5.md @ 9dbac4bd', 'REGISTRY.md @ a939198e', 'data/b610_census.txt @ fda4e81b',
                'data/b617_currency.txt @ fda4e81b', 'tools/b618_record.py @ fda4e81b', 'OPEN_TRAILS.md @ 9dbac4bd', 'FINDINGS.md @ 9dbac4bd',
                'data/b618_closing_push_out.txt @ db0aaa5b', ':11864 ', ':12228 ', ':12356 ', ':12595 ', ':12597 ', ':12777 ', ':12797 ', ':1276 ')

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R229) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b618`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b618' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b619 -- x'])),
    ('G-R229-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R229) END' in S['ferry'] and S['ot'].count('**(R229) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R229) ratified', '(R229) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in READ_NEEDLES) and 'NO SUCH LINE' not in S['reads'],
     lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ANSWERS-BANKED', 'the act`s answers bank: no prompt put, said in its own line',
     lambda S: S['answers'].startswith('### b619 -- THE AUTHOR`S ANSWERS BEFORE THE SEAL, 0 prompt(s)') and S['answers'].count('### PROMPT ') == 0
     and '### NONE: no prompt was put to the author in this act' in S['answers'],
     lambda S: put(S, 'answers', S['answers'].replace('0 prompt(s)', '1 prompt(s)', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay db0aaa5b`s files', lambda S: S['pushout'][0] == ['data/b618_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/b618_closing_push_out.txt', 'x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b618') == 4, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b618'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'family-b603': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80 and every PLACE-papers read at ba5f0ea, run afresh through the test`s control()',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(S['ctl'][0], ok=False)] + S['ctl'][1:])),
    ('G-INSTRUMENTS-UNEDITED', 'b618`s suite and record tool, b610`s census module and record tool, b616`s record tool and claims module, the shared record tools, the control`s test file, the generator, its arm, the E0 rule, the push gate, the scanner, the sentence counter, the table generator and the errata appender against fda4e81b',
     lambda S: all(bool(a) and a == b for a, b in S['inst'].values()) and len(S['inst']) == 19,
     lambda S: put(S, 'inst', dict(S['inst'], **{'b610_census.py': (S['inst']['b610_census.py'][0], (S['inst']['b610_census.py'][1] or b'') + b'x')}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b618`s weight, the three acceptances, the refuted prediction`s repair', lambda S: weight_ok(S),
     lambda S: put(S, 'find', S['find'].replace(':12797 the proper repair', 'x'))),
    ('G-N5-STANDING-LINE', 'OPEN_TRAILS at the banked line: the N5 scorer`s standing line beneath :12356', lambda S: standing_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('takes the trail record’s expected line on OPEN_TRAILS as a parameter', 'x'))),
    ('G-MAPPING-BANKED', 'the mapping bank and its json: every changed cell old and new with its source, H53a-H53c on the bank', lambda S: mapping_ok(S),
     lambda S: put(S, 'CJ', dict(S['CJ'], changes=(S['CJ'].get('changes') or []) + [dict(new='x-not-in-the-bank')]))),
    ('G-MAPPING-BEFORE-EDITION', 'the mapping`s stamp against the edition`s write stamp and its commit time', lambda S: mapping_first(S),
     lambda S: put(S, 'CJ', dict(S['CJ'], at='2099-01-01T00:00:00Z'))),
    ('G-EDITION-WRITTEN', 'v0.4 on disk and at HEAD against the banked sha', lambda S: edition_written(S),
     lambda S: put(S, 'ed_disk', (S['ed_disk'] or b'') + b'x')),
    ('G-EDITION-ALONE', 'PLACE-papers` log since 9dbac4b: the edition in one commit of its own', lambda S: edition_alone(S),
     lambda S: put(S, 'pp_files', {h: (f + ['FINDINGS.md'] if CEN4 in f else f) for h, f in S['pp_files'].items()})),
    ('G-EDITION-CARRIES', 'every non-blank v0.3 line at its mapped line in v0.4: verbatim, its recorded rewrite, or recorded as removed', lambda S: carries(S),
     lambda S: _mut_ed(S, '- **The title layer.**', '- **The title  layer.**')),
    ('G-CELLS-NOW', 'every §1 row of v0.4 against the row rendered now from REGISTRY and the documents at 9dbac4b and the kernels` tags read now',
     lambda S: cells_now(S), lambda S: _mut_ed(S, 'SIDE-yang-mills-formation v0.1.1 = 73e9e2c', 'SIDE-yang-mills-formation v0.1.1 = 73e9e2d')),
    ('G-SECTION2-ANNEX', 'v0.4`s §2: the ANNEX alone with its reason, the line on the six, the count', lambda S: section2_ok(S),
     lambda S: _mut_ed(S, '## §2 — THE CLUSTERS WITH DOCUMENTS AND NO KEYSTONE *(under §0)*', '## §2 — THE CLUSTERS WITH DOCUMENTS AND NO KEYSTONE *(under §0)*\n\n- **R99 x** x')),
    ('G-SYNTHESES-READBACK', 'H53a recomputed now: each synthesis cell against the document`s own head and class line', lambda S: syn_ok(S),
     lambda S: _mut_ed(S, 'p2-d10 (`phase2/physics-speculative/THE_LOCAL_COSMIC_INTERFACE_AND_THE_DARK_SECTOR.md` v0.1)',
                       'p2-d10 (`phase2/physics-speculative/THE_LOCAL_COSMIC_INTERFACE_AND_THE_DARK_SECTOR.md` v0.2)')),
    ('G-TAGS-READBACK', 'H53c recomputed now: every kernel entry against its remote read now, the unpushed tags by name', lambda S: tags_ok(S),
     lambda S: _mut_ed(S, 'SIDE-orchestrator v0.1.0 = 5d0a341 (unpushed by name: v0.1 = f0fcc40)', 'SIDE-orchestrator v0.1.0 = 5d0a341')),
    ('G-REPIN-HOLDS', 'the re-pin bank and every cited line of v0.4 against the final file', lambda S: repin_ok(S),
     lambda S: put(S, 'EJ', dict(S['EJ'], pos=dict(S['EJ'].get('pos') or {}, R01=1)))),
    ('G-EDITION-SCAN', 'the scanner run afresh on v0.4', lambda S: ed_scan_ok(S), lambda S: put(S, 'ed_scan', S['ed_scan'].replace('CLEAN', 'DIRTY'))),
    ('G-H28-SCORED', 'H28a-H28c in the diff bank and its json, no sentence held, the desk', lambda S: h28_ok(S),
     lambda S: put(S, 'H28', dict(S['H28'], H28b='REFUTED'))),
    ('G-H53A-SCORED', 'H53a recomputed now, against the scores and the desk', lambda S: h53x_ok(S, 'H53a'), lambda S: _sc(S, 'H53a')),
    ('G-H53B-SCORED', 'H53b recomputed now, against the scores and the desk', lambda S: h53x_ok(S, 'H53b'), lambda S: _sc(S, 'H53b')),
    ('G-H53C-SCORED', 'H53c recomputed now, against the scores and the desk', lambda S: h53x_ok(S, 'H53c'), lambda S: _sc(S, 'H53c')),
    ('G-H53D-SCORED', 'H53d from the diff bank`s json, against the scores and the desk', lambda S: h53x_ok(S, 'H53d'), lambda S: _sc(S, 'H53d')),
    ('G-SCORER-REPAIRED', 'relay`s log of the record tool: the tool as sealed (its sha256 on the face), then the N5 edit, each committed alone; the parameter at HEAD',
     lambda S: scorer_repaired(S), lambda S: put(S, 'rec_head', (S['rec_head'] or b'').replace(b'def n5(trail_line', b'def n5(x'))),
    ('G-N5-TEST-SAME', 'the N5 test`s bank: the repaired scorer`s verdict the same before and after the trail write, at Component 4 and at Component 6',
     lambda S: n5_test_ok(S), lambda S: put(S, 'T5', dict(S['T5'], same=False))),
    ('G-CURRENT-UNEDITED', 'README, ERRATA, SPIRAL_MAP and v0.7, REGISTRY, the census`s current version and v0.3, the sieve v0.5, the spine, the monograph v5.17 and the six syntheses, on disk and at HEAD against 9dbac4b',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{CEN3: (S['currents'][CEN3][0] + b'x', S['currents'][CEN3][1], S['currents'][CEN3][2])}))),
    ('G-NODISCLOSURE-PUBLIC', 'the no-disclosure arm on every public byte this act writes: the appended ledger bytes, the edition, its relay banks and tools',
     lambda S: bool(S['nd_pub']) and not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', dict(S['nd_pub'], method=1))),
    ('G-PAGES-BANKED', 'both pages at HEAD and their banks: a changed page re-emitted and committed, an unchanged one unwritten', lambda S: pages_banked(S),
     lambda S: put(S, 'PZ', dict(S['PZ'], sha256='0'))),
    ('G-PAGES-COMMITTED-ALONE', 'PLACE-papers` log since 9dbac4b: a changed page in one commit of its own, an unchanged one in none', lambda S: pages_alone(S),
     lambda S: put(S, 'pp_files', dict(S['pp_files'], deadbee=[PAGE]))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b602`s list and v0.20 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b603`s list and v0.21 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank after the pages: both page arms and the frozen control', lambda S: 'PAGE ARMS PASSING : 2 of 2' in S['arms_c2']
     and ('%s PASSING : 2 of 2' % CONTROL_ARM) in S['arms_c2'], lambda S: put(S, 'arms_c2', S['arms_c2'].replace('PASSING : 2 of 2', 'PASSING : 1 of 2'))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD, lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record: the strike items, b620 priced', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and 'b620 priced' in trail(S), lambda S: put(S, 'ot', S['ot'].replace('b620 priced', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b620, W-ORD-SECOND-READER’s batch; the author rules on the closing' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b620, W-ORD-SECOND-READER’s batch; the author rules on the closing', 'x'))),
    ('G-KERNELS-UNTOUCHED', 'every kernel this act reads: its main, tags and branches against the face, lv`s HEAD and status, the explicit-formula checkout on main and clean with no new tag, the trial branch',
     lambda S: kernels_untouched(S), lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-spinor': '0'}))),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('36352a0', '36352a0', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b619_record.py'): S['tooltext'].get(os.path.join(T, 'b619_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                              if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md against its pre-act blob', lambda S: S['errata'][1] and S['errata'][0] == S['errata'][1],
     lambda S: put(S, 'errata', (S['errata'][0] + b'x', S['errata'][1]))),
    ('G-KEYSTONES-SCOPE', 'PLACE-papers` phase, day1, outputs and heritage paths, tracked and untracked: the edition alone',
     lambda S: S['keystone_changes'] == [CEN4], lambda S: put(S, 'keystone_changes', sorted(S['keystone_changes'] + ['phase1.5/method/ENUMERA_v1_6.md']))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at fda4e81b, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 6000,
     lambda S: put(S, 'prior_bad', ['data/b618_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == sorted(
        [CEN4, 'FINDINGS.md', 'OPEN_TRAILS.md'] + [p for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])) if z.get('changed')]),
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + ['README.md']))),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-GS-UNTOUCHED', 'SIDE-global-section`s diff against 3528bcf and its HEAD', lambda S: S['gs_diff'] == [] and S['gs_head'].startswith(PRE['gs'])
     and S['corr_now'] == S['corr_pre'], lambda S: put(S, 'gs_diff', ['CORRESPONDENCE.md'])),
    ('G-TABLE-UNMOVED', 'the regenerated table`s diff: no row added or gone and no grade cell moved, as the face declares', lambda S: S['table_changed'] is not None
     and S['table_changed'] == [], lambda S: put(S, 'table_changed', [['SIDE-explicit-formula', 'x']])),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', ''))
     for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3', 'S4', 'S5', 'S6')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every file written, against the (W) globs', lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/unlisted.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                          and "startswith('b619')" in S['suite'] and "data/b619_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b619')", ''))),
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
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b619 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
        'PRE-SEAL (R202)(3)' if PRERUN else 'MID-ACT, AFTER COMPONENT 4' if MID else 'POST-PUSH' if pushed else 'PRE-PUSH'))
    if PRERUN or MID:
        rec('### run at (UTC) : %s   ### %s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                                              'the standing line of (R202)(3): every arm run at HEAD before the face is sealed, its count printed.'
                                              if PRERUN else '(R229) Component 4: the suite re-run whole and counted after the scorer`s repair; no table regenerated.'))
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
        out = os.path.join(D, 'b619_arms_prerun.txt')
    elif MID:
        out = os.path.join(D, sys.argv[sys.argv.index('--mid') + 1])
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b619_checks_postpush.txt' if pushed else 'b619_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b619_arms_prerun.txt', 'b619_lsr_prerun.json').replace('b619_checks', 'b619_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b619_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
