# -*- coding: utf-8 -*-
"""b621_checks.py -- THE SUITE OF b621, UNDER (R231): THE SECOND READER'S DISAGREEMENTS RULED BY CLASS AND APPLIED -- THE MONOGRAPH AT
v5.18, THE SYNTHESES RE-GRADED WHERE THE READER WAS RIGHT, THE FORM AMENDED TO SHOW THE READER WHAT THE SEAT GRADED.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`, `--mid <name>` or `--prerun`; it writes data/b621_checks.txt before the push and
### data/b621_checks_postpush.txt after it; `--mid <name>` writes data/<name> and regenerates nothing. `--prerun` (the standing line of
### (R202)(3)): every arm run at HEAD BEFORE the face is sealed, no table regenerated, its counts written to data/b621_arms_prerun.txt.
### ### Every remote is read once per run (OPEN_TRAILS :12703, b616_claims.remote_refs), each run's ls-remote calls banked per repository
### beside its output (data/b621_lsr*.json); G-LSREMOTE-ONE-PER-REPO runs last.
### ### The harness is b568's to b620's, carried from tools/b620_checks.py (its imports, helpers, regenerate and main); the sources,
### predicates and arms are b621's. The control arm is the frozen one of (R207)(2). Every positive control mutates a line whose text occurs
### once in its source and that its predicate reads. The edition arms rebuild the monograph's body and the syntheses' rows afresh from the
### current versions' blobs and the work-list, apart from the record tool's edition code; the kernel-statement arm re-reads every terminal
### at its pin. The no-disclosure needles are built at run time from TECHNE-Core's module documents and never printed.
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
import b621_worklist as K     # noqa: E402

NL = chr(10)
PP, GS, KER = 'D:/MY-DOwnloads/PLACE-papers', 'D:/SIDE-global-section', 'D:/SIDE-explicit-formula'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
FACE = os.path.join(D, 'b621_registration_2026-10-04.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PRE = dict(relay='7838dd02', pp='e6a3fbf', gs='3528bcf', ker='1d5d4dd')
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-explicit-formula': '1d5d4dd9', 'SIDE-global-section': '3528bcfc',
             'SIDE-spinor': '520abe7a', 'SIDE-effects': 'ef4cff77', 'SIDE-cosmo': 'c5cba30c'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b', 'product-b600': '1dd5cd7',
        'doubling-keiper-b601': '5fc0c87', 'sign-window-b602': '914c413', 'family-b603': '1d5d4dd'}
STEPZERO = 'dd5a86c8'
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/5e646bda-5dd5-4aca-9274-32c06d1d3da9/scratchpad'
PROMPT_HEAD = '(R231)(3)(iv) and (5) on the residue at v5.18: the 56 residue disagreements split 55 seat-BEYOND/reader-AT and ONE'
EDITED = ('15E', '2D', '2G', 'P12')
INST = ('b620_checks.py', 'b620_record.py', 'b609_record.py', 'b609_worklist.py', 'b608_record.py', 'b615_record.py', 'b558_record.py',
        'b604_record.py', 'b602_record.py', 'b560_record.py', 'b566_record.py', 'b616_record.py', 'b616_claims.py', 'test_chain_page_b596.py',
        'chain_page.py', 'g_chain_page.py', 'push_gated.sh', 'banned_terms.py', 'terminal_table.py')


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b621')
            and 'data/b621_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    l = cr0(b if isinstance(b, bytes) else (b or '').encode('utf-8')).decode('utf-8', 'replace').split(NL)
    return l[:-1] if l and l[-1] == '' else l


def sources():
    import b621_record as REC
    import b616_record as R6
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b621_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b621_') and f.endswith('.py'))
    nexts = {k: K.NEXT[k][0] for k in K.SYN}
    S = dict(
        REC=REC, face=face, ferry=rd('b621_ferry.txt'), scan=rd('b621_ferry_scan.txt'), cens=rd('b621_census_stepzero.txt'),
        fcens=rd('b621_faces_census_stepzero.txt'), pins0=rd('b621_pins_stepzero.txt'), procs=rd('b621_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b620_closing.txt'), reads=rd('b621_reads.txt'), branches=rd('b621_branches.txt'), answers=rd('b621_author_answers.txt'),
        prerun=rd('b621_arms_prerun.txt'), defects=rd('b621_defects.txt'),
        sieve=rd('b621_sieve_rate.txt'), sj=jl('b621_sieve_rate.json'), ag=json.loads(cr0(blob(ROOT, PRE['relay'] + ':data/b620_agreement.json')) or b'{}'),
        rowstxt=raw(os.path.join(D, 'b621_rows.txt')), rj=jl('b621_rows.json'), rs=jl('b621_residue.json'),
        me=jl('b621_mono_edition.json'), h28m=jl('b621_h28_mono.json'), edtxt=rd('b621_edition_PLACE.txt'), repin=rd('b621_repin_mono.txt'),
        mscan=rd('b621_mono_termscan.txt'),
        sjs={k: jl('b621_syn_%s.json' % k) for k in EDITED}, h28s={k: jl('b621_h28_%s.json' % k) for k in EDITED},
        sbanks={k: rd('b621_edition_%s.txt' % k) for k in EDITED},
        m17=cr0(blob(PP, PRE['pp'] + ':' + K.M17)), m18=(cr0(raw(os.path.join(PP, *K.M18.split('/')))), cr0(blob(PP, 'HEAD:' + K.M18))),
        syncur={k: cr0(blob(PP, PRE['pp'] + ':' + p)) for k, p in K.SYN.items()},
        synnext={k: (cr0(raw(os.path.join(PP, *nexts[k].split('/')))), cr0(blob(PP, 'HEAD:' + nexts[k]))) for k in K.SYN},
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f)))) for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        readme=(cr0(raw(os.path.join(PP, 'README.md'))), cr0(blob(PP, PRE['pp'] + ':README.md'))),
        errata=(cr0(raw(os.path.join(PP, 'ERRATA.md'))), cr0(blob(PP, PRE['pp'] + ':ERRATA.md'))),
        currents={p: (cr0(raw(os.path.join(PP, *p.split('/')))), cr0(blob(PP, PRE['pp'] + ':' + p)), cr0(blob(PP, 'HEAD:' + p))) for p in REC.CURRENTS},
        pages={p: (cr0(raw(os.path.join(PP, p))), cr0(blob(PP, PRE['pp'] + ':' + p)), cr0(blob(PP, 'HEAD:' + p))) for p in (PAGE, DIR_PAGE)},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        corr_pre=cr0(blob(GS, PRE['gs'] + ':CORRESPONDENCE.md')), corr_now=cr0(raw(os.path.join(GS, 'CORRESPONDENCE.md'))),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        kern_face=(jl('b621_kernels_face.json').get('kernels') or {}),
        lv_head=gs('D:/SIDE-lv-conservation', 'rev-parse', 'HEAD'), lv_dirty=gs('D:/SIDE-lv-conservation', 'status', '--porcelain', '--untracked-files=no'),
        trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain', '--untracked-files=no'),
        ktags=sorted(x for x in gs(KER, 'tag', '-l', 'v0.*').split(NL) if x.strip()),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b620*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b621_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b621_mustnotexist.txt')), table_changed=None,
        fj=jl('b621_findings.json'), tj=jl('b621_trail.json'), sc=jl('b621_scores.json'), desk=rd('b621_desk_notes.txt'),
        rl=jl('b621_record_lines.json'), PZ=jl('b621_page_zeta.json'), PX=jl('b621_page_chi.json'), arms_c2=rd('b621_page_arms_c2.txt'),
        lsr=None,
        rlog=[l.split(' ', 1) for l in gs(ROOT, 'log', '--format=%h %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
    )
    S['kern_now'] = {k: list(v) for k, v in REC.kern_state(list(S['kern_face'])).items()} if S['kern_face'] else {}
    S['written'] = written_files(lock_epoch or 0)
    S['globs'] = wl_globs(face)
    S['nd_sets'] = R6.nd_sets()
    S['rowstext'] = cr0(S['rowstxt']).decode('utf-8', 'replace') if S['rowstxt'] else ''
    S['mtimes'] = {p: (os.path.getmtime(os.path.join(PP, *p.split('/'))) if os.path.exists(os.path.join(PP, *p.split('/'))) else None)
                   for p in [K.M18] + [K.NEXT[k][0] for k in EDITED]}
    S['rows_mtime'] = os.path.getmtime(os.path.join(D, 'b621_rows.json')) if os.path.exists(os.path.join(D, 'b621_rows.json')) else None
    # ### the act's new public text: the ledger appends, its relay banks and tools, the editions' new wordings and back matter
    pub = []
    for nm, pre, now in (('FINDINGS', S['fi_pre'], S['fi_now']), ('OPEN_TRAILS', S['ot_pre'], S['ot_now'])):
        pub.append((now or b'')[len(pre or b''):].decode('utf-8', 'replace') if now and pre and now.startswith(pre) else '')
    for f in sorted(os.listdir(D)):
        if f.startswith(('b621_', 'audit_b621_')) and os.path.isfile(os.path.join(D, f)):
            pub.append(read(os.path.join(D, f)))
    pub += [read(f) for f in tools]
    m18 = lines_of(S['m18'][0]) if S['m18'][0] else []
    if REC.BM_TAG18 in m18:
        pub.append(NL.join(m18[m18.index(REC.BM_TAG18):]))
    pub += [c[3] for c in K.CHANGES] + [K.HISTORY]
    for k in EDITED:
        nx = lines_of(S['synnext'][k][0]) if S['synnext'][k][0] else []
        bi = [i for i, l in enumerate(nx) if l.startswith('## Back matter of %s' % K.NEXT[k][1])]
        if bi:
            pub.append(NL.join(nx[bi[0]:]))
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
    S['pp_log'] = [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in gs(PP, 'log', '--reverse', '--format=%h %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()]
    S['pp_files'] = {h: files_of(PP, h) for h, _s in S['pp_log']}
    S['pp_head'], S['pp_remote'] = gs(PP, 'rev-parse', 'HEAD'), KC0.remote_refs(PP).get('refs/heads/main', '')   # ### read once (OPEN_TRAILS :12703)
    # ### the terminals the six kernel-verified rows name, re-read now at their pins
    S['kv_now'] = {rid: [(os.path.basename(repo), rev, path, a, lines_of(blob(repo, '%s:%s' % (rev, path)) or b'')[a - 1:b])
                         for repo, rev, path, a, b in k['terms']] for rid, k in K.KV.items()}
    S.update(extra_sources(S))
    return S


def extra_sources(S):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    X = {}
    X['gcp_zeta'] = GCP.arm(os.path.join(D, 'b602_nodes_zeta.txt'), os.path.join(SP, '_b621_gcp'), os.path.join(D, 'b602_probe_out.txt'))
    X['gcp_chi'] = GCP.arm(os.path.join(D, 'b603_nodes_chi.txt'), os.path.join(SP, '_b621_gcp'), os.path.join(D, 'b603_chi_probe_out.txt'))
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
    return bool(x) and x.get('file') == 'FINDINGS.md' and a.startswith(x['head']) and '(:7422)' in a and 'b620 AT ITS WEIGHT' in a \
        and 'beside the original 114 of 119 (0.958)' in a and '**The reading, `(R231)`(2):**' in a and 'The suite 70 of 70 before the push' in a \
        and x['line'] > 7438


def clause_ok(S):
    y = (S['rl'].get('lines') or [{}, {}])[1:2] or [{}]
    y = y[0]
    o = oline(S, y.get('line'))
    return bool(y) and y.get('file') == 'OPEN_TRAILS.md' and o.startswith(y['head']) and '(:12212)' in o and '`(R231)`(4)' in o \
        and 'printed from the kernel at the pin without its grade' in o and 'stands at 0.75 for the next batch' in o and y['line'] > 12837


def sieve_ok(S):
    ed = S['ag'].get('editions') or {}
    sv = [k for k in ed if k.startswith('the sieve')]
    a0, n0 = sum(ed[k][0] for k in sv), sum(ed[k][1] for k in sv)
    a1, n1 = sum(ed[k][0] for k in sv if k != 'the sieve v0.2'), sum(ed[k][1] for k in sv if k != 'the sieve v0.2')
    struck = sorted(d['id'] for d in S['ag'].get('dis_s') or [] if d['doc'] == 'the sieve')
    return bool(sv) and ('%d of %d = %.3f' % (a0, n0, a0 / n0)) in S['sieve'] and ('WITHOUT THE FIVE STRUCK PAIRS: %d of %d = %.3f' % (a1, n1, a1 / n1)) in S['sieve'] \
        and struck == sorted(S['REC'].STRUCK) and all(('  %s -- ' % i) in S['sieve'] for i in struck) and n0 - n1 == 5


def rows_banked(S):
    RJ, RS = S['rj'], S['rs']
    b = cr0(S['rowstxt'])
    return bool(b) and bool(RJ) and bool(RS) and hashlib.sha256(b).hexdigest() == RS.get('sha256') and RJ.get('sha256') == RS.get('rows_sha') \
        and hashlib.sha256(b[:len(b) - len(b.split(b'\n### PART C')[-1]) - len(b'\n### PART C')]).hexdigest() == RJ.get('sha256') \
        and '### PART A' in S['rowstext'] and '### PART B' in S['rowstext'] and '### PART C' in S['rowstext']


def rows_before(S):
    t = iso_epoch(S['rj'].get('at', ''))
    ats = [S['me'].get('at')] + [S['sjs'][k].get('at') for k in EDITED]
    return bool(t) and all(iso_epoch(x or '') and iso_epoch(x) >= t for x in ats) and S['rows_mtime'] is not None \
        and all(m is not None and S['rows_mtime'] <= m for m in S['mtimes'].values()) and S['me'].get('dry') is False \
        and all(S['sjs'][k].get('dry') is False for k in EDITED)


def kv_now(S):
    txt = S['rowstext']
    out = []
    for rid, terms in S['kv_now'].items():
        for repo, rev, path, a, ls in terms:
            out.append(bool(ls) and ('      %s @ %s (' % (repo, rev)) in txt and all(('        :%-4d %s' % (a + j, l)) in txt for j, l in enumerate(ls)))
        out.append(('### VERDICT: %s at kernel-verified' % K.KV[rid]['verdict'].upper()) in txt.split('  %s  ' % rid, 1)[-1][:12000])
    return bool(out) and all(out) and len(S['kv_now']) == 6


def rows_cover(S):
    RJ, AG = S['rj'], S['ag']
    kv = {x['id']: x['verdict'] for x in RJ.get('kv') or []}
    ot = {x['id']: x['verdict'] for x in RJ.get('others') or []}
    ids = set(d['id'] for d in AG.get('dis_r') or [])
    return bool(ids) and len(ids) == 52 and set(kv) == set(K.KV) and set(ot) == set(K.OTHERS) and set(kv) | set(ot) == ids \
        and all(kv[i] == K.KV[i]['verdict'] for i in kv) and all(ot[i] == K.OTHERS[i][0] for i in ot) and RJ.get('regraded') == len(K.REGRADES) \
        and sum(1 for v in ot.values() if v == 'moves') == len(K.REGRADES)


def residue_ok(S):
    RS, AG = S['rs'], S['ag']
    ids = [d['id'] for d in AG.get('dis_x') or []]
    m = sorted(set(K.ITEMS_BOTH + K.ITEMS_READER + K.ITEMS_SEAT))
    return len(ids) == 56 and all(('  %s  ' % i) in S['rowstext'] for i in ids) and RS.get('m_items') == m and RS.get('m_missing') == [] \
        and all(RS['item_changes'].get(i) for i in m) and RS.get('n_other') == 39 and len(RS.get('dis') or []) == 56


def survey_now(S):
    """### the needle survey recomputed now over v5.17's body: every hit line answered by a change, the history line or a kept reason"""
    import b604_record as R4
    M = lines_of(S['m17'])
    changed = set(c[1] for c in K.CHANGES)
    hit = set()
    for _n, pat in K.SURVEY_NEEDLES:
        for i, l in enumerate(M[:K.M_CORR - 1], 1):
            if any(re.search(pat, s, re.I) for s in R4._segs(l)):
                hit.add(i)
    fate = all(i in changed or 2231 <= i <= 2239 or i in K.SURVEY_KEPT for i in hit)
    return bool(hit) and fate and sorted(int(k) for k in (S['rs'].get('survey') or {})) == sorted(hit) and (S['rs'].get('fates') or {}).get('none') == 0


def mono_banked(S):
    a, b = S['m18']
    return bool(a) and a == b and hashlib.sha256(a).hexdigest() == S['me'].get('sha256') and S['me'].get('dry') is False


def committed_alone(S, path):
    c = [h for h, f in S['pp_files'].items() if path in f]
    return len(c) == 1 and S['pp_files'][c[0]] == [path] and dict(S['pp_log'])[c[0]].startswith('b621 (R231)')


def mono_now(S):
    """### v5.18's body rebuilt now from v5.17's blob and the work-list, apart from the record tool's edition code"""
    M, ed = lines_of(S['m17']), lines_of(S['m18'][0])
    by = {}
    for c in K.CHANGES:
        by.setdefault(c[1], []).append(c)
    exp = []
    for i, l in enumerate(M[:K.HISTORY_AFTER], 1):
        if i == 19:
            exp.append(S['REC'].VERSION18)
        s = l
        for c in by.get(i, []):
            if s.count(c[2]) != 1:
                return False
            s = s.replace(c[2], c[3])
        exp.append(s)
    exp += [K.HISTORY, '']
    return bool(M) and len(ed) > len(exp) and ed[:len(exp)] == exp and ed[len(exp)] == M[K.HISTORY_AFTER] and M[K.HISTORY_AFTER].startswith('## Correspondence')


def repin_ok(S):
    m = re.search(r'RE-PIN : (\d+) of (\d+) citations hold', S['repin'])
    return bool(m) and m.group(1) == m.group(2) and int(m.group(2)) > 600


def h28_mono_ok(S):
    H = S['h28m']
    return bool(H) and all(H.get(k) == 'HOLDS' for k in ('H28a', 'H28b', 'H28c')) and all(
        ('### ### **%s HOLDS' % k) in S['edtxt'] for k in ('H28a', 'H28b', 'H28c')) and 'THE EDITION LANDS: NO SENTENCE HELD' in S['edtxt'] \
        and H.get('carried_bad') == [] and H.get('history_in_place') is True


def syn_banked(S):
    return all(bool(S['synnext'][k][0]) and S['synnext'][k][0] == S['synnext'][k][1] and hashlib.sha256(S['synnext'][k][0]).hexdigest() == S['sjs'][k].get('sha256')
               and S['sjs'][k].get('dry') is False for k in EDITED)


def syn_rows_now(S):
    """### every next version's Correspondence rows rebuilt now from the current version's blob and the work-list"""
    for k in EDITED:
        cur, nx = lines_of(S['syncur'][k]), lines_of(S['synnext'][k][0])
        if not cur or not nx:
            return False
        rows_c = {l.split(' | ')[0]: l for l in cur if re.match(r'^\| [A-Z]{2}-\d\d \|', l)}
        rows_n = {l.split(' | ')[0]: l for l in nx if re.match(r'^\| [A-Z]{2}-\d\d \|', l)}
        if set(rows_c) != set(rows_n):
            return False
        want = dict(rows_c)
        for rid, key, cid, og, ng, ob, nb in K.REGRADES:
            if key == k:
                c = K.row_cells(rows_c['| ' + cid])
                c[3], c[4] = ng, nb
                want['| ' + cid] = '| ' + ' | '.join(c) + ' |'
        for fid, key, cid, old, new, why in K.FACTS:
            if key == k:
                want['| ' + cid] = want['| ' + cid].replace(old, new)
        if want != rows_n or cur[2] != nx[2]:
            return False
    return True


def syn_tiers(S):
    untouched = [k for k in K.SYN if k not in EDITED]
    return all(S['h28s'][k].get('tier_same') is True for k in EDITED) and all(S['synnext'][k][0] is None and S['synnext'][k][1] is None for k in untouched) \
        and all(lines_of(S['syncur'][k])[2] == lines_of(S['synnext'][k][0])[2] for k in EDITED if S['synnext'][k][0])


def h28_syn_ok(S):
    return all(all(S['h28s'][k].get(x) == 'HOLDS' for x in ('H28a', 'H28b', 'H28c')) and S['h28s'][k].get('carried_bad') == []
               and ('THE EDITION LANDS: NO SENTENCE HELD' in S['sbanks'][k]) and (S['h28s'][k].get('repin') or [0, 1])[0] == (S['h28s'][k].get('repin') or [0, 1])[1]
               for k in EDITED)


def _h(S, k, want):
    return (S['sc'].get(k) or [''])[0] == want and ('(%s)' % k.upper()) in S['desk'] and ('### **%s.**' % want) in S['desk']


def h55_ok(S, k):
    RJ, H = S['rj'], S['h28m']
    if k == 'H55a':
        want = 'HOLDS' if sum(1 for x in RJ.get('kv') or [] if x['verdict'] == 'stands') >= 4 else 'REFUTED'
    elif k == 'H55b':
        want = 'HOLDS' if syn_tiers(S) else 'REFUTED'
    elif k == 'H55c':
        clean = re.search(r'^\s*VERDICT\s*: CLEAN', S['mscan'], re.M) is not None and re.search(r'live uses\s*:\s*0\b', S['mscan']) is not None
        want = 'HOLDS' if len(S['rs'].get('m_items') or []) >= 10 and clean and H.get('unexcepted') == 0 else 'REFUTED'
    else:
        want = 'HOLDS' if h28_mono_ok(S) and h28_syn_ok(S) else 'REFUTED'
    return bool(RJ) and _h(S, k, want)


def hold_ok(S):
    a = S['answers']
    return PROMPT_HEAD in a and 'RESULT (transcript line' in a and 'option 3' in a and re.search(r'### b621 -- THE AUTHOR`S ANSWERS, 1 prompt\(s\)', a) is not None


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
            out.append(len(c) == 1 and S['pp_files'][c[0]] == [p] and dict(S['pp_log'])[c[0]].startswith('b621 (R231): ' + p))
        else:
            out.append(z.get('changed') is False and not [h for h, f in S['pp_files'].items() if p in f])
    return all(out) and bool(S['PZ']) and bool(S['PX'])


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 24]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') and fline(S, e).startswith('## The second reader’s disagreements applied: the monograph at v5.18') \
        and all(x in tail for x in ('**The rows**', '**The residue**', '**The editions.**', '**The record lines.**', '**The scores.**',
                                    '**Read in mutual light**', 'strengthens', '**Next.**', 'b622'))


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
    want = sorted(['FINDINGS.md', 'OPEN_TRAILS.md', K.M18] + [K.NEXT[k][0] for k in EDITED]
                  + [p for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])) if z.get('changed')])
    return S['pp_changed'] == want


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


def _mut_bytes(S, key, old, new):
    a, b = S[key]
    return put(S, key, (a.replace(old.encode('utf-8'), new.encode('utf-8'), 1), b))


def _mut_next(S, k, old, new):
    a, b = S['synnext'][k]
    return put(S, 'synnext', dict(S['synnext'], **{k: (a.replace(old.encode('utf-8'), new.encode('utf-8'), 1), b)}))


READ_NEEDLES = ('data/b620_agreement.txt @ 7838dd02', 'OPEN_TRAILS.md @ e6a3fbf1', 'day1/A_Place_to_Stand_v5_17.md @ e6a3fbf1',
                'Kernel/SpectralCannonFull.lean @ b1407b22', 'Kernel/Voice1.lean @ b1407b22', 'Kernel/Integration.lean @ b1407b22',
                'SIDEEffects/Structural.lean @ c66f3c59', 'SIDEEffects/Structural.lean @ a27415d1', 'SIDECosmo/FormationPhaseSpace.lean @ c5cba30c',
                'THE_FINDINGS_AS_THEY_STAND_v0_5.md @ e6a3fbf1', 'FINDINGS.md @ e6a3fbf1', 'README.md @ e6a3fbf1', 'data/b620_closing_push_out.txt @ dd5a86c8',
                ':12212 ', ':12819 ', ':11864 ', ':12228 ', ':12601 ', ':12799 ', ':7210 ', ':124 ', ':1218 ')
C01_NEW = "while the step from the classes to ξ's zeros is the located clause, open (RH-60, the sieve v0.5 :124, and FINDINGS :7210)"

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R231) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b620`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b620' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b621 -- x'])),
    ('G-R231-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R231) END' in S['ferry'] and S['ot'].count('**(R231) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R231) ratified', '(R231) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in READ_NEEDLES) and 'NO SUCH LINE' not in S['reads'],
     lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ANSWERS-BANKED', 'the act`s answers bank: the one prompt before the seal, verbatim, its options and its answer', lambda S: hold_ok(S),
     lambda S: put(S, 'answers', S['answers'].replace('1 prompt(s)', '2 prompt(s)', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay dd5a86c8`s files', lambda S: S['pushout'][0] == ['data/b620_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/b620_closing_push_out.txt', 'x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b620') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b620'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'family-b603': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80 and every PLACE-papers read at ba5f0ea, run afresh through the test`s control()',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(S['ctl'][0], ok=False)] + S['ctl'][1:])),
    ('G-INSTRUMENTS-UNEDITED', 'b620`s suite and record tool, b609`s record tool and work-list, b608`s, b615`s and b558`s record tools, the shared record tools, b616`s, the control`s test file, the generator, its arm, the push gate, the scanner and the table generator against 7838dd02',
     lambda S: all(bool(a) and a == b for a, b in S['inst'].values()) and len(S['inst']) == len(INST),
     lambda S: put(S, 'inst', dict(S['inst'], **{'b609_record.py': (S['inst']['b609_record.py'][0], (S['inst']['b609_record.py'][1] or b'') + b'x')}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b620`s weight, the struck pairs` rate and the reading of (R231)(2)', lambda S: weight_ok(S),
     lambda S: put(S, 'find', S['find'].replace('beside the original 114 of 119 (0.958)', 'x'))),
    ('G-FORM-CLAUSE', 'OPEN_TRAILS at the banked line: the form`s clause addressed to :12212', lambda S: clause_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('stands at 0.75 for the next batch', 'x'))),
    ('G-SIEVE-RATE', 'the sieve`s rate bank against the rate recomputed now from b620`s agreement bank at 7838dd02, the five pairs struck', lambda S: sieve_ok(S),
     lambda S: put(S, 'sieve', S['sieve'].replace('WITHOUT THE FIVE STRUCK PAIRS: 114 of 114', 'WITHOUT THE FIVE STRUCK PAIRS: 113 of 114'))),
    ('G-ROWS-BANKED', 'the rows bank on disk: Parts A and B by the rows json`s sha256, the whole by the residue json`s', lambda S: rows_banked(S),
     lambda S: put(S, 'rowstxt', (S['rowstxt'] or b'') + b'x')),
    ('G-ROWS-BEFORE-EDITIONS', 'the rows json`s stamp and file time against every edition`s bank and file', lambda S: rows_before(S),
     lambda S: put(S, 'rj', dict(S['rj'], at='2099-01-01T00:00:00Z'))),
    ('G-KV-STATEMENTS-NOW', 'every terminal the six kernel-verified rows name, re-read now at its pin, against the rows bank`s printed statement', lambda S: kv_now(S),
     lambda S: put(S, 'rowstext', S['rowstext'].replace('theorem spectral_cannon (t', 'theorem spectral_canon (t', 1))),
    ('G-ROWS-COVER', 'the rows json against b620`s 52 disagreement rows and the work-list`s verdicts', lambda S: rows_cover(S),
     lambda S: put(S, 'rj', dict(S['rj'], others=(S['rj'].get('others') or [])[1:]))),
    ('G-RESIDUE-COVERS', 'the residue part and json: the 56 disagreements listed, the 33 monograph items answered, 39 sentences listed', lambda S: residue_ok(S),
     lambda S: put(S, 'rs', dict(S['rs'], n_other=38))),
    ('G-SURVEY-NOW', 'the restatement survey recomputed now over v5.17`s body: every hit line answered', lambda S: survey_now(S),
     lambda S: put(S, 'rs', dict(S['rs'], survey={k: v for k, v in list((S['rs'].get('survey') or {}).items())[1:]}))),
    ('G-MONO-BANKED', 'v5.18 on disk and at HEAD against the edition bank`s sha256', lambda S: mono_banked(S),
     lambda S: put(S, 'me', dict(S['me'], sha256='0'))),
    ('G-MONO-COMMITTED-ALONE', 'PLACE-papers` log since e6a3fbf: v5.18 in one commit of its own', lambda S: committed_alone(S, K.M18),
     lambda S: put(S, 'pp_files', dict(S['pp_files'], deadbee=[K.M18]))),
    ('G-MONO-NOW', 'v5.18`s body rebuilt now from v5.17`s blob and the work-list', lambda S: mono_now(S),
     lambda S: _mut_bytes(S, 'm18', C01_NEW, C01_NEW.replace('open (RH-60', 'open, (RH-60'))),
    ('G-MONO-REPIN', 'the monograph`s re-pin bank', lambda S: repin_ok(S), lambda S: put(S, 'repin', S['repin'].replace('citations hold', 'citations held'))),
    ('G-MONO-H28', 'the monograph`s H28 bank and its diff bank`s verdict lines', lambda S: h28_mono_ok(S),
     lambda S: put(S, 'edtxt', S['edtxt'].replace('### ### **H28c HOLDS', '### ### **H28c REFUTED'))),
    ('G-SYN-BANKED', 'each edited synthesis`s next version on disk and at HEAD against its bank`s sha256', lambda S: syn_banked(S),
     lambda S: put(S, 'sjs', dict(S['sjs'], **{'2G': dict(S['sjs']['2G'], sha256='0')}))),
    ('G-SYN-COMMITTED-ALONE', 'PLACE-papers` log since e6a3fbf: each next version in one commit of its own', lambda S: all(committed_alone(S, K.NEXT[k][0]) for k in EDITED),
     lambda S: put(S, 'pp_files', dict(S['pp_files'], deadbee=[K.NEXT['P12'][0]]))),
    ('G-SYN-ROWS-NOW', 'every next version`s Correspondence rows rebuilt now from the current version`s blob and the work-list', lambda S: syn_rows_now(S),
     lambda S: _mut_next(S, '15E', 'no pattern read across results', 'a pattern read across results')),
    ('G-SYN-TIERS', 'the tier lines of the next versions against the current ones; 2B and 2F with no next version', lambda S: syn_tiers(S),
     lambda S: put(S, 'synnext', dict(S['synnext'], **{'2B': (b'x', b'x')}))),
    ('G-SYN-H28', 'each synthesis`s H28 bank and its diff bank`s verdict lines', lambda S: h28_syn_ok(S),
     lambda S: put(S, 'sbanks', dict(S['sbanks'], **{'2D': S['sbanks']['2D'].replace('THE EDITION LANDS: NO SENTENCE HELD', 'x')}))),
    ('G-H55A-SCORED', 'H55a recomputed from the rows bank, against the scores and the desk', lambda S: h55_ok(S, 'H55a'), lambda S: _sc(S, 'H55a')),
    ('G-H55B-SCORED', 'H55b recomputed from the tier lines, against the scores and the desk', lambda S: h55_ok(S, 'H55b'), lambda S: _sc(S, 'H55b')),
    ('G-H55C-SCORED', 'H55c recomputed from the residue json, the scanner and the H28 bank, against the scores and the desk', lambda S: h55_ok(S, 'H55c'), lambda S: _sc(S, 'H55c')),
    ('G-H55D-SCORED', 'H55d recomputed from every edition`s H28 bank, against the scores and the desk', lambda S: h55_ok(S, 'H55d'), lambda S: _sc(S, 'H55d')),
    ('G-CURRENTS-UNEDITED', 'the current versions, the documents read, README, ERRATA, REGISTRY and SPIRAL_MAP on disk and at HEAD against e6a3fbf',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{K.M17: (
         S['currents'][K.M17][0] + b'x', S['currents'][K.M17][1], S['currents'][K.M17][2])}))),
    ('G-NODISCLOSURE-PUBLIC', 'the no-disclosure arm on every public byte this act writes: the appended ledger bytes, its relay banks and tools, the editions` new wordings and back matter',
     lambda S: bool(S['nd_pub']) and not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', dict(S['nd_pub'], method=1))),
    ('G-PAGES-BANKED', 'both pages at HEAD and their banks: a changed page re-emitted and committed, an unchanged one unwritten', lambda S: pages_banked(S),
     lambda S: put(S, 'PZ', dict(S['PZ'], sha256='0'))),
    ('G-PAGES-COMMITTED-ALONE', 'PLACE-papers` log since e6a3fbf: a changed page in one commit of its own, an unchanged one in none', lambda S: pages_alone(S),
     lambda S: put(S, 'pp_files', dict(S['pp_files'], deadbee=[PAGE]))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b602`s list and v0.20 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b603`s list and v0.21 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank after the pages: both page arms and the frozen control', lambda S: 'PAGE ARMS PASSING : 2 of 2' in S['arms_c2']
     and ('%s PASSING : 2 of 2' % CONTROL_ARM) in S['arms_c2'], lambda S: put(S, 'arms_c2', S['arms_c2'].replace('PASSING : 2 of 2', 'PASSING : 1 of 2'))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD, lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record: the strike items and the residue sentences listed for their next editions', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and '**The residue sentences listed for their documents’ next editions**' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**The residue sentences listed for their documents’ next editions**', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b622, W-ORD-QUANTIFIER-COLUMN’s generator with DENSITY' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b622, W-ORD-QUANTIFIER-COLUMN’s generator with DENSITY', 'x'))),
    ('G-KERNELS-UNTOUCHED', 'every kernel this act reads: its main, tags and branches against the face, lv`s HEAD and status, the explicit-formula checkout on main and clean with no new tag, the trial branch',
     lambda S: kernels_untouched(S), lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-cosmo': '0'}))),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('36352a0', '36352a0', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b621_record.py'): S['tooltext'].get(os.path.join(T, 'b621_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                              if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md against its pre-act blob', lambda S: S['errata'][1] and S['errata'][0] == S['errata'][1],
     lambda S: put(S, 'errata', (S['errata'][0] + b'x', S['errata'][1]))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 7838dd02, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 6000,
     lambda S: put(S, 'prior_bad', ['data/b620_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked: the ledgers, the editions and a changed page', lambda S: corpus_scope(S),
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
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every file written, against the (W) globs', lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/unlisted.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                          and "startswith('b621')" in S['suite'] and "data/b621_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b621')", ''))),
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
    rec('b621 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
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
        out = os.path.join(D, 'b621_arms_prerun.txt')
    elif MID:
        out = os.path.join(D, sys.argv[sys.argv.index('--mid') + 1])
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b621_checks_postpush.txt' if pushed else 'b621_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b621_arms_prerun.txt', 'b621_lsr_prerun.json').replace('b621_checks', 'b621_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b621_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
