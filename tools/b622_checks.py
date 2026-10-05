# -*- coding: utf-8 -*-
"""b622_checks.py -- THE SUITE OF b622, UNDER (R232): THE QUANTIFIER COLUMN -- THE GENERATOR READING EACH NODE'S SHAPE FROM ITS LEAN
STATEMENT, BOTH PAGES RE-EMITTED, THE SIEVE'S HAND MARKS REPLACED; README'S SUPPORTABLE SENTENCE FOR v0.17-v0.21; THE 39 OWED SENTENCES
ENTERED AS WORK-LIST ITEMS.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`, `--mid <name>` or `--prerun`; it writes data/b622_checks.txt before the push and
### data/b622_checks_postpush.txt after it; `--mid <name>` writes data/<name> and regenerates nothing. `--prerun` (the standing line of
### (R202)(3)): every arm run at HEAD BEFORE the face is sealed, no table regenerated, its counts written to data/b622_arms_prerun.txt.
### ### Every remote is read once per run (OPEN_TRAILS :12703, b616_claims.remote_refs), each run's ls-remote calls banked per repository
### beside its output (data/b622_lsr*.json); G-LSREMOTE-ONE-PER-REPO runs last.
### ### THE SOURCES' REPAIR, (R232)'s Component 0 (b621's defect (a)): the source builder holds an ABSENT file as None, never as empty
### bytes -- `cr0` passes None through, and every reader of a source takes None for absent -- and G-ABSENT-IS-NONE tests it on a file that
### does not exist and on empty bytes.
### ### The harness is b568's to b621's, carried from tools/b621_checks.py (its imports, helpers, regenerate and main); the sources,
### predicates and arms are b622's. The control arm is the frozen one of (R207)(2). Every positive control mutates a line whose text occurs
### once in its source and that its predicate reads. The shape arms recompute every node's shape now through the generator's own reader;
### the sieve arm rebuilds v0.6's body afresh from v0.5's blob and those shapes, apart from the record tool's edition code. The
### no-disclosure needles are built at run time from TECHNE-Core's module documents and never printed.
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
import b622_worklist as K     # noqa: E402

NL = chr(10)
PP, GS, KER = 'D:/MY-DOwnloads/PLACE-papers', 'D:/SIDE-global-section', 'D:/SIDE-explicit-formula'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
FACE = os.path.join(D, 'b622_registration_2026-10-04.txt')
PAGE, DIR_PAGE = K.PAGE, K.DIR_PAGE
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP, gs='3528bcf', ker='1d5d4dd')
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-explicit-formula': '1d5d4dd9', 'SIDE-global-section': '3528bcfc',
             'SIDE-spinor': '520abe7a', 'SIDE-effects': 'ef4cff77', 'SIDE-cosmo': 'c5cba30c'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b', 'product-b600': '1dd5cd7',
        'doubling-keiper-b601': '5fc0c87', 'sign-window-b602': '914c413', 'family-b603': '1d5d4dd'}
STEPZERO = K.STEPZERO
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
GEN_FILES = ('tools/chain_page.py', 'tools/test_chain_page_b596.py')
WL = sorted('data/%s/%s' % (K.WL_DIR, fn) for fn, _k in K.WL_FILES.values())
WL_LISTS = sorted('data/%s/%s' % (K.WL_DIR, fn) for fn, k in K.WL_FILES.values() if k == 'list')
ABSENT = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_9.md'    # ### a file no act has written: G-ABSENT-IS-NONE's subject
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/37c7fa81-fdbc-49b5-acbe-57f6d60b97ad/scratchpad'
PROMPT_HEAD = '(R232)(4) on the quantifier column: the generator prints one of FINITE, UNIVERSAL, LIMIT, DENSITY, FAMILY or UNCLASSIFIED.'
INST = ('b621_checks.py', 'b621_record.py', 'b617_record.py', 'b604_record.py', 'b602_record.py', 'b566_record.py', 'b565_record.py',
        'b616_record.py', 'b616_claims.py', 'b558_record.py', 'g_chain_page.py', 'e0_rule.py', 'push_gated.sh', 'banned_terms.py',
        'terminal_table.py', 'reg_seal.py', 'b378_lockgate.py')


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
    """### THE REPAIR (b621's defect (a)): an absent file stays None; only bytes are normalised."""
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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b622')
            and 'data/b622_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def strip_prose(t):
    t = re.sub(r'"""[\s\S]*?"""', '', t)
    t = re.sub(r"'''[\s\S]*?'''", '', t)
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
    """### None (an absent file) reads as no lines."""
    if b is None:
        return []
    l = cr0(b if isinstance(b, bytes) else b.encode('utf-8')).decode('utf-8', 'replace').split(NL)
    return l[:-1] if l and l[-1] == '' else l


def tri(repo, path, pre):
    """### (disk, the pre-act blob, HEAD's blob), each None where the file is absent."""
    return (cr0(raw(os.path.join(repo, *path.split('/')))), cr0(blob(repo, '%s:%s' % (pre, path))), cr0(blob(repo, 'HEAD:' + path)))


def sources():
    import b622_record as REC
    import b616_record as R6
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b622_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b622_') and f.endswith('.py'))
    S = dict(
        REC=REC, face=face, ferry=rd('b622_ferry.txt'), scan=rd('b622_ferry_scan.txt'), cens=rd('b622_census_stepzero.txt'),
        fcens=rd('b622_faces_census_stepzero.txt'), pins0=rd('b622_pins_stepzero.txt'), procs=rd('b622_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b621_closing.txt'), reads=rd('b622_reads.txt'), branches=rd('b622_branches.txt'), answers=rd('b622_author_answers.txt'),
        prerun=rd('b622_arms_prerun.txt'), defects=rd('b622_defects.txt'),
        rl=jl('b622_record_lines.json'), wj=jl('b622_worklists.json'), wtxt=rd('b622_worklists.txt'), rmj=jl('b622_readme.json'),
        rscan=rd('b622_readme_termscan.txt'), gdiff=rd('b622_gen_diff.txt'), gtest=rd('b622_gen_test.txt'), h56a=jl('b622_h56a.json'),
        gcj=jl('b622_gen_commit.json'), old=jl('b622_old_lists.json'),
        pj={(k, t): jl('b622_page_%s_%s.json' % (k, t)) for k in ('zeta', 'chi') for t in ('c3', 'c4')},
        arms3=rd('b622_page_arms_c3.txt'), arms4=rd('b622_page_arms_c4.txt'), uj=jl('b622_unclassified.json'), utxt=rd('b622_unclassified.txt'),
        sj=jl('b622_sieve_shapes.json'), se=jl('b622_sieve_edition.json'), h28=jl('b622_h28.json'), edtxt=rd('b622_edition_FINDINGS_STAND.txt'),
        repin=rd('b622_repin_sieve.txt'), sscan=rd('b622_sieve_termscan.txt'),
        sv5=cr0(blob(PP, PRE['pp'] + ':' + K.SV5)), sv6=(cr0(raw(os.path.join(PP, *K.SV6.split('/')))), cr0(blob(PP, 'HEAD:' + K.SV6))),
        readme=tri(PP, 'README.md', PRE['pp']), absent=tri(PP, ABSENT, PRE['pp']),
        wlfiles={p: tri(ROOT, p, PRE['relay']) for p in WL},
        nodelists={k: (cr0(raw(os.path.join(D, K.NODES[k]))), cr0(blob(ROOT, PRE['relay'] + ':data/' + K.OLD_NODES[k]))) for k in ('zeta', 'chi')},
        genfiles={p: tri(ROOT, p, PRE['relay']) for p in GEN_FILES},
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f)))) for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        errata=(cr0(raw(os.path.join(PP, 'ERRATA.md'))), cr0(blob(PP, PRE['pp'] + ':ERRATA.md'))),
        currents={p: tri(PP, p, PRE['pp']) for p in REC.CURRENTS},
        pages={p: tri(PP, p, PRE['pp']) for p in (PAGE, DIR_PAGE)},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        corr_pre=cr0(blob(GS, PRE['gs'] + ':CORRESPONDENCE.md')), corr_now=cr0(raw(os.path.join(GS, 'CORRESPONDENCE.md'))),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        kern_face=(jl('b622_kernels_face.json').get('kernels') or {}),
        lv_head=gs('D:/SIDE-lv-conservation', 'rev-parse', 'HEAD'), lv_dirty=gs('D:/SIDE-lv-conservation', 'status', '--porcelain', '--untracked-files=no'),
        trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain', '--untracked-files=no'),
        ktags=sorted(x for x in gs(KER, 'tag', '-l', 'v0.*').split(NL) if x.strip()),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b621*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b622_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b622_mustnotexist.txt')), table_changed=None,
        fj=jl('b622_findings.json'), tj=jl('b622_trail.json'), sc=jl('b622_scores.json'), desk=rd('b622_desk_notes.txt'),
        lsr=None,
        rlog=[(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in gs(ROOT, 'log', '--reverse', '--format=%h %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
    )
    S['kern_now'] = {k: list(v) for k, v in REC.kern_state(list(S['kern_face'])).items()} if S['kern_face'] else {}
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
    S['pp_head'], S['pp_remote'] = gs(PP, 'rev-parse', 'HEAD'), KC0.remote_refs(PP).get('refs/heads/main', '')   # ### read once (OPEN_TRAILS :12703)
    # ### the act's new public text: the ledger appends, its relay banks and tools, the work-list entries, README's new lines, the pages'
    # ### head line and the edition's new wordings and back matter
    pub = []
    for nm, pre, now in (('FINDINGS', S['fi_pre'], S['fi_now']), ('OPEN_TRAILS', S['ot_pre'], S['ot_now'])):
        pub.append(now[len(pre):].decode('utf-8', 'replace') if now and pre and now.startswith(pre) else '')
    for f in sorted(os.listdir(D)):
        if f.startswith(('b622_', 'audit_b622_')) and os.path.isfile(os.path.join(D, f)):
            pub.append(read(os.path.join(D, f)))
    pub += [read(f) for f in tools]
    for p, (now, pre, _h) in S['wlfiles'].items():
        pub.append((now or b'')[len(pre or b''):].decode('utf-8', 'replace'))
    pub += [K.README_PARA, K.DEPOSIT_NEW, K.SHAPE_NEW]
    s6 = lines_of(S['sv6'][0])
    if K.BM_TAG6 in s6:
        pub.append(NL.join(s6[s6.index(K.BM_TAG6):]))
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
        if p in WL_LISTS:   # ### a work-list this act enters: its pre-act bytes a true prefix of its bytes now
            pb = cr0(blob(ROOT, '%s:%s' % (PRE['relay'], p)))
            if rb is None or not cr0(rb).startswith(pb or b'\x00') or len(cr0(rb)) <= len(pb or b''):
                bad.append(p)
            continue
        if rb is None or i not in (blob_id(rb), blob_id(cr0(rb))):
            bad.append(p)
    S['prior_bad'], S['prior_n'] = bad, len(pre_ids)
    S.update(extra_sources(S))
    return S


def _cells(k):
    import chain_page as CP
    return CP.parse(io.open(os.path.join(D, K.PROBE[k]), encoding='utf-8').read().replace(chr(13), ''))[0]


def extra_sources(S):
    import chain_page as CP
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    X = {}
    for k in ('zeta', 'chi'):   # ### a list not yet written reads as a failing arm, never as a crash of the run
        X['gcp_' + k] = (GCP.arm(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b622_gcp'), os.path.join(D, K.PROBE[k]))
                         if os.path.exists(os.path.join(D, K.NODES[k])) else dict(ok=False, rc=-1))
    X['ctl'] = TC.control()
    X['ctl_arm'] = TC.ARM
    # ### every node's shape recomputed now through the generator's own reader, from the banked probes
    X['shapes_now'] = {}
    X['reader'] = hasattr(CP, 'shape_of') and hasattr(CP, 'node_column') and hasattr(CP, 'SHAPE_KEY')
    for k in ('zeta', 'chi'):
        if not X['reader'] or not os.path.exists(os.path.join(D, K.NODES[k])):
            X['shapes_now'][k] = {}
            continue
        cells = _cells(k)
        nodes = CP.read_nodes(os.path.join(D, K.NODES[k]))[0]
        X['shapes_now'][k] = {x['name']: CP.shape_of(x['name'], cells) for x in nodes}
    X['five_now'] = [(n, w, CP.shape_of(n, _cells(k)) if X['reader'] else None) for n, k, w, _y in K.TEST_NODES]
    # ### the lists without the column re-emitted now against their pages before the act
    X['old_now'] = []
    for k in ('zeta', 'chi'):
        rc, pg, _m, _l = CP.build(os.path.join(D, K.OLD_NODES[k]), os.path.join(SP, '_b622_oldnow'), os.path.join(D, K.PROBE[k]))
        X['old_now'].append(rc == 0 and pg is not None and pg.encode('utf-8') == cr0(blob(PP, '%s:%s' % (PRE['pp'], K.PNAME[k]))))
    X['gen_stat'] = gs(ROOT, 'diff', '--stat', PRE['relay'], '--', *GEN_FILES).split(NL)[-1].strip()
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


def absent_ok(S):
    a, b, c = S['absent']
    return a is None and b is None and c is None and cr0(None) is None and cr0(b'') == b'' and cr0(b'x\r\n') == b'x\n' and lines_of(None) == []


def weight_ok(S):
    x = (S['rl'].get('lines') or [{}])[0]
    y = ((S['rl'].get('lines') or [{}, {}])[1:2] or [{}])[0]
    a = fline(S, x.get('line'))
    return bool(x) and bool(y) and x.get('file') == 'FINDINGS.md' and a.startswith(x['head']) and '(:7442)' in a and 'b621 AT ITS WEIGHT' in a \
        and 'beside 114 of 119 as keyed' in a and '**Confirmed, `(R232)`(1):**' in a and 'The suite 76 of 78 before the push' in a \
        and ('(OPEN_TRAILS :%d, appended to the :12839 clause)' % y.get('line', 0)) in a and x['line'] > 7460


def offer_ok(S):
    y = ((S['rl'].get('lines') or [{}, {}])[1:2] or [{}])[0]
    o = oline(S, y.get('line'))
    return bool(y) and y.get('file') == 'OPEN_TRAILS.md' and o.startswith(y['head']) and '(:12839)' in o \
        and 'the lines the row’s backing cell cites' in o and '`(R232)`(1)' in o and y['line'] > 12861


def wl_entered(S):
    items = S['REC'].K.residue_items()
    by = {}
    for x in items:
        by.setdefault('data/%s/%s' % (K.WL_DIR, K.WL_FILES[x['doc']][0]), []).append(x)
    if len(items) != 39 or sorted(by) != WL:
        return False
    for p, xs in by.items():
        now, pre, head = S['wlfiles'][p]
        if now is None or now != head:
            return False
        kind = [k for fn, k in K.WL_FILES.values() if p.endswith('/' + fn)][0]
        if kind == 'list' and (pre is None or not now.startswith(pre) or len(now) <= len(pre)):
            return False
        if kind == 'addendum' and pre is not None:
            return False
        t = now[len(pre or b''):].decode('utf-8')
        for x in xs:
            if t.count(':%d -- CEILING ITEM (%s)' % (x['line'], x['id'])) != 1 or t.count('    the sentence: "%s"' % x['sentence']) != 1:
                return False
    return True


def wl_now(S):
    """### the items recomputed now from b620's key and b621's residue bank, each sentence on its line at PLACE-papers f695c98, against the
    ### work-list bank's json"""
    items = S['REC'].K.residue_items()
    want = {}
    for x in items:
        want.setdefault(x['doc'], []).append(dict(id=x['id'], line=x['line']))
        src = lines_of(blob(PP, '%s:%s' % (PRE['pp'], x['doc'])))
        if not src or x['sentence'] not in src[x['line'] - 1]:
            return False
    got = {f['doc']: f['items'] for f in S['wj'].get('files') or []}
    return bool(got) and got == {d: sorted(v, key=lambda y: y['line']) for d, v in want.items()} and S['wj'].get('n_items') == 39 and S['wj'].get('dry') is False


def alone(S, files, prefix):
    c = [h for h, f in S['rfiles'].items() if f == sorted(files)]
    msg = {h: s for h, s in S['rlog']}
    return len(c) == 1 and msg[c[0]].split(' ', 1)[1].startswith(prefix) and not [h for h, f in S['rfiles'].items() if set(f) & set(files) and h != c[0]]


def pp_alone(S, path, prefix, n=1):
    c = [h for h, f in S['pp_files'].items() if path in f]
    return len(c) == n and all(S['pp_files'][h] == [path] and dict(S['pp_log'])[h].startswith(prefix) for h in c)


def readme_ok(S):
    a, pre, head = S['readme']
    want, _at = S['REC'].readme_text((pre or b'').decode('utf-8'))
    return bool(want) and a is not None and a == head == want.encode('utf-8') and a != pre


def readme_scanned(S):
    return re.search(r'^\s*VERDICT\s*: CLEAN', S['rscan'], re.M) is not None and re.search(r'live uses\s*:\s*0\b', S['rscan']) is not None \
        and S['rmj'].get('clean') is True and S['rmj'].get('dry') is False and S['rmj'].get('sha256') == hashlib.sha256(S['readme'][0] or b'').hexdigest()


def gen_alone(S):
    c = [l for l in S['rlog'] if S['rfiles'].get(l[0]) == sorted(GEN_FILES)]
    return alone(S, list(GEN_FILES), 'b622') and len(c) == 1 and S['lock_epoch'] is not None and int(c[0][1].split(' ', 1)[0]) > S['lock_epoch'] \
        and S['gcj'].get('commit') == c[0][0]


def gen_diff_ok(S):
    return all(a is not None and a == c and a != b for a, b, c in S['genfiles'].values()) and bool(S['gen_stat']) \
        and ('### ' + S['gen_stat']) in S['gdiff'] and '+def shape_of(n, cells):' in S['gdiff'] and '+def node_column(path):' in S['gdiff']


def gen_test_ok(S):
    m = re.search(r'### CASES : (\d+) ; PASSING : (\d+) ; FAILING : (\d+)', S['gtest'])
    return bool(m) and int(m.group(1)) == 9 and m.group(1) == m.group(2) and m.group(3) == '0' and '### ALL PASS' in S['gtest'] \
        and S['h56a'].get('cases') == 9 and S['h56a'].get('passing') == 9 and S['h56a'].get('rc') == 0


def five_now(S):
    return bool(S['five_now']) and all(g_ == w for _n, w, g_ in S['five_now']) and \
        [x.get('got') for x in S['h56a'].get('reads') or []] == [g_ for _n, _w, g_ in S['five_now']]


def old_ok(S):
    return S['old'].get('ok') is True and len(S['old_now']) == 2 and all(S['old_now'])


def nodes_ok(S):
    out = []
    for k in ('zeta', 'chi'):
        a, b = S['nodelists'][k]
        want = (NL.join(K.LIST_HEAD[k]) + NL + (b or b'').decode('utf-8').rstrip(NL) + NL + K.COLUMN_MARK + NL).encode('utf-8')
        out.append(a is not None and b is not None and a == want)
    return all(out)


def page_shapes(text):
    out = {}
    for l in (text or b'').decode('utf-8').split(NL):
        m = re.match(r'^\d+\. `([^`]+)` — .*? — shape: (\S+) — premises: ', l)
        if m:
            out[m.group(1)] = m.group(2)
    return out


def column_now(S):
    import chain_page as CP
    out = []
    for k, p in (('zeta', PAGE), ('chi', DIR_PAGE)):
        a, _b, c = S['pages'][p]
        sh = page_shapes(c)
        out.append(bool(S['shapes_now'][k]) and a == c and sh == S['shapes_now'][k] and (c or b'').decode('utf-8').count(CP.SHAPE_KEY) == 1)
    return all(out)


def unc_now(S):
    return [n for k in ('zeta', 'chi') for n, s in S['shapes_now'][k].items() if s == 'UNCLASSIFIED']


def unc_ok(S):
    u = unc_now(S)
    return bool(S['shapes_now']['zeta']) and bool(S['shapes_now']['chi']) and bool(S['uj']) and S['uj'].get('nodes') == u and S['utxt'].count('### THE SEAT`S PROPOSAL: ') == len(u) \
        and sorted(S['uj'].get('proposals') or {}) == sorted(u)


def pages_banked(S):
    out = []
    for k, p in (('zeta', PAGE), ('chi', DIR_PAGE)):
        a, b, c = S['pages'][p]
        z3, z4 = S['pj'][(k, 'c3')], S['pj'][(k, 'c4')]
        out.append(z3.get('rc') == 0 and z4.get('rc') == 0 and z3.get('changed') is True and a is not None and a == c and a != b
                   and hashlib.sha256(c).hexdigest() == z4.get('sha256') and z3.get('dry') is False and z4.get('dry') is False)
    return all(out)


def pages_alone(S):
    out = []
    for k, p in (('zeta', PAGE), ('chi', DIR_PAGE)):
        n = sum(1 for t in ('c3', 'c4') if S['pj'][(k, t)].get('changed'))
        out.append(n >= 1 and pp_alone(S, p, 'b622 (R232): ' + p, n))
    return all(out)


def arms_ok(t):
    return 'PAGE ARMS PASSING : 2 of 2' in t and ('%s PASSING : 2 of 2' % CONTROL_ARM) in t


def rows_now(S):
    """### the sieve's rows naming a page node, recomputed now from v0.5's blob and the shapes read now"""
    pn = {}
    for k in ('zeta', 'chi'):
        for n, s in S['shapes_now'][k].items():
            pn.setdefault(n.split('.')[-1], (k, n, s))
    return S['REC']._shape_rows(lines_of(S['sv5']), pn) if pn else []


def shapes_banked(S):
    r = rows_now(S)
    key = lambda x: (x['id'], x['line'], x['decl'], x['node'], x['hand'], x['gen'])   # noqa: E731
    t0, t1 = iso_epoch(S['sj'].get('at', '')), iso_epoch(S['se'].get('at', ''))
    return bool(r) and [key(x) for x in r] == [key(x) for x in S['sj'].get('rows') or []] and bool(t0) and bool(t1) and t0 <= t1 \
        and S['se'].get('dry') is False


def sieve_banked(S):
    a, b = S['sv6']
    return a is not None and a == b and hashlib.sha256(a).hexdigest() == S['se'].get('sha256') and S['se'].get('dry') is False


def sieve_now(S):
    """### v0.6's body rebuilt now from v0.5's blob and the shapes read now, apart from the record tool's edition code"""
    S5, S6 = lines_of(S['sv5']), lines_of(S['sv6'][0])
    rows = {x['line']: x for x in rows_now(S)}
    if not S5 or not S6 or not rows:
        return False
    diff = [x for x in rows.values() if not x['same']]
    ver = K.VERSION6 % (len(rows), len(rows) - len(diff), len(diff), ', '.join('%s %s' % (x['id'], x['gen']) for x in sorted(diff, key=lambda y: y['line'])) or 'none')
    cut = S5.index('<!-- b604 (R214) THE v0.2 EDITION`S BACK MATTER, 2026-10-03 -->')
    exp = []
    for n, l in enumerate(S5[:cut], 1):
        if n == 3:
            exp += [ver, '']
        if l == K.SHAPE_OLD:
            exp.append(K.SHAPE_NEW)
        elif n in rows:
            exp.append(l.replace('| %s |' % rows[n]['hand'], '| %s |' % rows[n]['new_cell'], 1))
        else:
            exp.append(l)
    return S6[:len(exp)] == exp and S6[len(exp)] == S5[cut]


def repin_ok(S):
    m = re.search(r'RE-PIN : (\d+) of (\d+) citations hold', S['repin'])
    return bool(m) and m.group(1) == m.group(2) and int(m.group(2)) > 400


def h28_ok(S):
    H = S['h28']
    return bool(H) and all(H.get(k) == 'HOLDS' for k in ('H28a', 'H28b', 'H28c')) and all(
        ('### ### **%s HOLDS' % k) in S['edtxt'] for k in ('H28a', 'H28b', 'H28c')) and 'THE SIEVE LANDS: NO SENTENCE HELD' in S['edtxt'] \
        and H.get('carried_bad') == [] and re.search(r'^\s*VERDICT\s*: CLEAN', S['sscan'], re.M) is not None


def _h(S, k, want):
    return (S['sc'].get(k) or [''])[0] == want and ('(%s)' % k.upper()) in S['desk'] and ('### **%s.**' % want) in S['desk']


def h56_ok(S, k):
    if k == 'H56a':
        want = 'HOLDS' if five_now(S) else 'REFUTED'
    elif k == 'H56b':
        want = 'HOLDS' if S['shapes_now']['zeta'] and S['shapes_now']['chi'] and len(unc_now(S)) <= 3 else 'REFUTED'
    elif k == 'H56c':
        r = rows_now(S)
        S6 = lines_of(S['sv6'][0])
        took = bool(r) and all(len(S6) > x['line'] + 1 and S6[x['line'] + 1].count('| %s |' % x['new_cell']) == 1 for x in r)
        want = 'HOLDS' if took and sum(1 for x in r if not x['same']) <= 2 else 'REFUTED'
    else:
        want = 'HOLDS' if h28_ok(S) and arms_ok(S['arms3']) and arms_ok(S['arms4']) else 'REFUTED'
    return _h(S, k, want)


def hold_ok(S):
    a = S['answers']
    return PROMPT_HEAD in a and 'RESULT (transcript line' in a and 'option 1' in a and re.search(r'### b622 -- THE AUTHOR`S ANSWERS, 1 prompt\(s\)', a) is not None


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(S['REC'].CURRENTS)


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 24]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') and fline(S, e).startswith('## The quantifier column: five shapes read from the Lean statements') \
        and all(x in tail for x in ('**The generator**', '**The pages**', '**The sieve at v0.6**', '**README**', '**The 39 owed sentences**',
                                    '**The record lines.**', '**The scores.**', '**Read in mutual light**', 'strengthens', '**Next.**', 'b623'))


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
        and S['lv_dirty'] == '' and len(S['kern_face']) == 7 and S['kern_face'] == S['kern_now']


def corpus_scope(S):
    return S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', 'README.md', K.SV6, PAGE, DIR_PAGE])


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


def _mut3(S, key, sub, old, new):
    d = dict(S[key])
    a, b, c = d[sub]
    d[sub] = ((a or b'').replace(old.encode('utf-8'), new.encode('utf-8'), 1), b, c)
    return put(S, key, d)


def _mut_page(S, p):
    a, b, c = S['pages'][p]
    t = (c or b'').decode('utf-8')
    i = t.find(' — shape: ')
    return put(S, 'pages', dict(S['pages'], **{p: (a, b, (t[:i] + ' — shape: LIMIT' + t[i + len(' — shape: ') + len(t[i + len(' — shape: '):].split(' ', 1)[0]):]).encode('utf-8'))}))


READ_NEEDLES = ('OPEN_TRAILS.md @ f695c98f', 'tools/chain_page.py @ 02fba720', 'tools/test_chain_page_b596.py @ 02fba720',
                'THE_FINDINGS_AS_THEY_STAND_v0_5.md @ f695c98f', 'README.md @ f695c98f', 'data/b558_editions/GRH_CASCADE.txt @ 02fba720',
                'data/b558_editions/BALANCE_AND_POSITIVITY_addendum.txt @ 02fba720', 'data/b621_closing_push_out.txt @ 92d1b584',
                'KeiperSign.lean @ v0.20 = 914c413 :82', 'Family.lean @ v0.21 = 1d5d4dd :213', 'Simplicity.lean @ v0.20 = 914c413 :45',
                ':12266 ', ':12296 ', ':11864 ', ':12228 ', ':12839 ', ':12851 ', ':12861 ', ':125 ', ':154 ', ':21 ', ':321 ', ':333 ')

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R232) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b621`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b621' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b622 -- x'])),
    ('G-R232-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R232) END' in S['ferry'] and S['ot'].count('**(R232) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R232) ratified', '(R232) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in READ_NEEDLES) and 'NO SUCH LINE' not in S['reads'],
     lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ANSWERS-BANKED', 'the act`s answers bank: the one prompt before the seal, verbatim, its options and its answer', lambda S: hold_ok(S),
     lambda S: put(S, 'answers', S['answers'].replace('1 prompt(s)', '2 prompt(s)', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay 92d1b584`s files', lambda S: S['pushout'][0] == ['data/b621_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/b621_closing_push_out.txt', 'x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b621') == 4, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b621'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'family-b603': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80 and every PLACE-papers read at ba5f0ea, run afresh through the test`s control()',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(S['ctl'][0], ok=False)] + S['ctl'][1:])),
    ('G-INSTRUMENTS-UNEDITED', 'b621`s suite and record tool, b617`s record tool, the shared record tools, b616`s, the page arm, the E0 rule, the push gate, the scanner, the table generator, the seal and the lock gate against 02fba720',
     lambda S: all(a is not None and a == b for a, b in S['inst'].values()) and len(S['inst']) == len(INST),
     lambda S: put(S, 'inst', dict(S['inst'], **{'b617_record.py': (S['inst']['b617_record.py'][0], (S['inst']['b617_record.py'][1] or b'') + b'x')}))),
    ('G-ABSENT-IS-NONE', 'the repaired source builder on a file no act wrote (disk, f695c98, HEAD) and on empty bytes', lambda S: absent_ok(S),
     lambda S: put(S, 'absent', (b'', b'', b''))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b621`s weight with the confirmations, citing the offer`s line', lambda S: weight_ok(S),
     lambda S: put(S, 'find', S['find'].replace('beside 114 of 119 as keyed', 'x'))),
    ('G-OFFER-CLAUSE', 'OPEN_TRAILS at the banked line: the offer taken, addressed to :12839', lambda S: offer_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('the lines the row’s backing cell cites', 'x'))),
    ('G-WORKLISTS-ENTERED', 'the fourteen work-list and addendum files on disk and at HEAD: each of the 39 items once, by line, its sentence verbatim; each list`s pre-act bytes a true prefix, each addendum absent before',
     lambda S: wl_entered(S), lambda S: _mut3(S, 'wlfiles', 'data/b558_editions/CATALOGOS_addendum.txt', ':759 -- CEILING ITEM (X002)', ':758 -- CEILING ITEM (X002)')),
    ('G-WORKLISTS-NOW', 'the items recomputed now from b620`s key and b621`s residue bank, each sentence on its line at f695c98, against the bank`s json',
     lambda S: wl_now(S), lambda S: put(S, 'wj', dict(S['wj'], n_items=38))),
    ('G-WORKLISTS-COMMITTED-ALONE', 'relay`s log since 02fba720: the fourteen files in one commit of their own', lambda S: alone(S, WL, 'b622'),
     lambda S: put(S, 'rfiles', dict(S['rfiles'], deadbee=[WL[0]]))),
    ('G-README-APPEND', 'README on disk and at HEAD against its blob at f695c98 with the paragraph and the refresh, and nothing else', lambda S: readme_ok(S),
     lambda S: put(S, 'readme', ((S['readme'][0] or b'') + b'x', S['readme'][1], S['readme'][2]))),
    ('G-README-SCANNED', 'the scanner`s bank on README and its json`s digest against README on disk', lambda S: readme_scanned(S),
     lambda S: put(S, 'rscan', S['rscan'].replace('VERDICT          : CLEAN', 'VERDICT          : NOT CLEAN'))),
    ('G-README-COMMITTED-ALONE', 'PLACE-papers` log since f695c98: README in one commit of its own', lambda S: pp_alone(S, 'README.md', 'b622 (R232)(3)'),
     lambda S: put(S, 'pp_files', dict(S['pp_files'], deadbee=['README.md']))),
    ('G-GEN-COMMITTED-ALONE', 'relay`s log: the generator and its test in one commit of their own, after the lock', lambda S: gen_alone(S),
     lambda S: put(S, 'lock_epoch', 4102444800)),
    ('G-GEN-DIFF-BANKED', 'the generator and its test on disk and at HEAD against 02fba720, and the diff bank`s stat line and its new functions', lambda S: gen_diff_ok(S),
     lambda S: put(S, 'gdiff', S['gdiff'].replace('+def shape_of(n, cells):', '+def shape(n, cells):'))),
    ('G-GEN-TEST-COUNTED', 'the test bank and H56a`s json: nine cases, all passing', lambda S: gen_test_ok(S),
     lambda S: put(S, 'gtest', S['gtest'].replace('### ALL PASS', '### NOT ALL PASS'))),
    ('G-GEN-FIVE-NOW', 'the five test nodes read now through the generator from their banked probes, against the expectations and the bank', lambda S: five_now(S),
     lambda S: put(S, 'five_now', S['five_now'][:4] + [(S['five_now'][4][0], S['five_now'][4][1], 'UNIVERSAL')])),
    ('G-GEN-OLD-LISTS', 'b602`s and b603`s lists, without the column, re-emitted now and at the bank against their pages at f695c98', lambda S: old_ok(S),
     lambda S: put(S, 'old_now', [S['old_now'][0], False])),
    ('G-H56A-SCORED', 'H56a recomputed now, against the scores and the desk', lambda S: h56_ok(S, 'H56a'), lambda S: _sc(S, 'H56a')),
    ('G-NODES-LISTS', 'this act`s two node lists against b602`s and b603`s at 02fba720, the head and the column`s line added', lambda S: nodes_ok(S),
     lambda S: put(S, 'nodelists', dict(S['nodelists'], zeta=((S['nodelists']['zeta'][0] or b'').replace(b'# column: quantifier', b'# column: none'),
                                                               S['nodelists']['zeta'][1])))),
    ('G-PAGES-BANKED', 'both pages on disk and at HEAD against their last pass`s bank, each changed at the column`s pass', lambda S: pages_banked(S),
     lambda S: put(S, 'pj', dict(S['pj'], **{('zeta', 'c4'): dict(S['pj'][('zeta', 'c4')], sha256='0')}))),
    ('G-PAGES-COMMITTED-ALONE', 'PLACE-papers` log since f695c98: each changed pass of each page in one commit of its own', lambda S: pages_alone(S),
     lambda S: put(S, 'pp_files', dict(S['pp_files'], deadbee=[PAGE]))),
    ('G-PAGE-COLUMN-NOW', 'every node line of both pages at HEAD: its shape cell against the shape read now, the key`s line once', lambda S: column_now(S),
     lambda S: _mut_page(S, DIR_PAGE)),
    ('G-UNCLASSIFIED-BANKED', 'the UNCLASSIFIED bank against the nodes read UNCLASSIFIED now, a proposal for each', lambda S: unc_ok(S),
     lambda S: put(S, 'uj', dict(S['uj'], nodes=(S['uj'].get('nodes') or [])[1:]))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from this act`s list and b602`s v0.20 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from this act`s list and b603`s v0.21 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm banks after each pass: both page arms and the frozen control', lambda S: arms_ok(S['arms3']) and arms_ok(S['arms4']),
     lambda S: put(S, 'arms4', S['arms4'].replace('PAGE ARMS PASSING : 2 of 2', 'PAGE ARMS PASSING : 1 of 2'))),
    ('G-H56B-SCORED', 'H56b recomputed now, against the scores and the desk', lambda S: h56_ok(S, 'H56b'), lambda S: _sc(S, 'H56b')),
    ('G-SIEVE-SHAPES-BANKED', 'the shapes bank against the rows recomputed now from v0.5`s blob, banked before the edition', lambda S: shapes_banked(S),
     lambda S: put(S, 'sj', dict(S['sj'], rows=(S['sj'].get('rows') or [])[1:]))),
    ('G-SIEVE-BANKED', 'v0.6 on disk and at HEAD against the edition bank`s sha256', lambda S: sieve_banked(S),
     lambda S: put(S, 'se', dict(S['se'], sha256='0'))),
    ('G-SIEVE-COMMITTED-ALONE', 'PLACE-papers` log since f695c98: v0.6 in one commit of its own', lambda S: pp_alone(S, K.SV6, 'b622 (R232)(4)'),
     lambda S: put(S, 'pp_files', dict(S['pp_files'], deadbee=[K.SV6]))),
    ('G-SIEVE-NOW', 'v0.6`s body rebuilt now from v0.5`s blob and the shapes read now', lambda S: sieve_now(S),
     lambda S: put(S, 'sv6', ((S['sv6'][0] or b'').replace('UNCLASSIFIED (G)'.encode('utf-8'), 'UNIVERSAL (G)'.encode('utf-8'), 1), S['sv6'][1]))),
    ('G-SIEVE-REPIN', 'the sieve`s re-pin bank', lambda S: repin_ok(S), lambda S: put(S, 'repin', S['repin'].replace('citations hold', 'citations held'))),
    ('G-SIEVE-H28', 'the sieve`s H28 bank, its diff bank`s verdict lines and its scanner bank', lambda S: h28_ok(S),
     lambda S: put(S, 'edtxt', S['edtxt'].replace('### ### **H28c HOLDS', '### ### **H28c REFUTED'))),
    ('G-H56C-SCORED', 'H56c recomputed now from v0.6 and the rows, against the scores and the desk', lambda S: h56_ok(S, 'H56c'), lambda S: _sc(S, 'H56c')),
    ('G-H56D-SCORED', 'H56d recomputed from the H28 bank and both page-arm banks, against the scores and the desk', lambda S: h56_ok(S, 'H56d'), lambda S: _sc(S, 'H56d')),
    ('G-CURRENTS-UNEDITED', 'the current versions, the documents of the 39 sentences, ERRATA, REGISTRY and SPIRAL_MAP on disk and at HEAD against f695c98',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{K.SV5: ((S['currents'][K.SV5][0] or b'') + b'x', S['currents'][K.SV5][1],
                                                                                            S['currents'][K.SV5][2])}))),
    ('G-NODISCLOSURE-PUBLIC', 'the no-disclosure arm on every public byte this act writes: the appended ledger bytes, its relay banks and tools, the work-list entries, README`s new lines, the edition`s back matter',
     lambda S: bool(S['nd_pub']) and not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', dict(S['nd_pub'], method=1))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD, lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record: the strike items and the UNCLASSIFIED nodes with their proposals', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and '**For the author’s ruling, the UNCLASSIFIED nodes with the seat’s proposals**' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**For the author’s ruling, the UNCLASSIFIED nodes with the seat’s proposals**', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b623, W-ORD-TAG-REMOTES and W-ORD-SEC-AXIOM-ARTEFACT in one act' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b623, W-ORD-TAG-REMOTES and W-ORD-SEC-AXIOM-ARTEFACT in one act', 'x'))),
    ('G-KERNELS-UNTOUCHED', 'every kernel this act reads: its main, tags and branches against the face, lv`s HEAD and status, the explicit-formula checkout on main and clean with no new tag, the trial branch',
     lambda S: kernels_untouched(S), lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-cosmo': '0'}))),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('36352a0', '36352a0', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b622_record.py'): S['tooltext'].get(os.path.join(T, 'b622_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                              if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md against its pre-act blob', lambda S: S['errata'][1] is not None and S['errata'][0] == S['errata'][1],
     lambda S: put(S, 'errata', ((S['errata'][0] or b'') + b'x', S['errata'][1]))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 02fba720, by blob id; the seven work-lists entered, append-only', lambda S: S['prior_bad'] == [] and S['prior_n'] > 6000,
     lambda S: put(S, 'prior_bad', ['data/b621_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked: the ledgers, README, the sieve`s v0.6 and both pages', lambda S: corpus_scope(S),
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + ['REGISTRY.md']))),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] is not None and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] is not None and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-GS-UNTOUCHED', 'SIDE-global-section`s diff against 3528bcf and its HEAD', lambda S: S['gs_diff'] == [] and S['gs_head'].startswith(PRE['gs'])
     and S['corr_now'] == S['corr_pre'], lambda S: put(S, 'gs_diff', ['CORRESPONDENCE.md'])),
    ('G-TABLE-UNMOVED', 'the regenerated table`s diff: no row added or gone and no grade cell moved, as the face declares', lambda S: S['table_changed'] is not None
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
                                                                          and "startswith('b622')" in S['suite'] and "data/b622_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b622')", ''))),
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
    rec('b622 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
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
    rec('  ### G-PRIORBANK-UNCHANGED checked %d relay data banks tracked at %s by blob id, the work-lists by prefix; changed %s' % (
        S['prior_n'], PRE['relay'], S['prior_bad'] or 'NONE'))
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
        out = os.path.join(D, 'b622_arms_prerun.txt')
    elif MID:
        out = os.path.join(D, sys.argv[sys.argv.index('--mid') + 1])
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b622_checks_postpush.txt' if pushed else 'b622_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b622_arms_prerun.txt', 'b622_lsr_prerun.json').replace('b622_checks', 'b622_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b622_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
