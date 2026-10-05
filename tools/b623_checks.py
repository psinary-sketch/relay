# -*- coding: utf-8 -*-
"""b623_checks.py -- THE SUITE OF b623, UNDER (R233): THE UNPUSHED TAGS SETTLED BY CITATION; THE DE-ALIGNMENT KERNEL'S AXIOM ARTEFACT
PRINTED AND ITS ROWS ENTERED; FOUR RESEARCH WORK-ORDERS AND ONE ARM ENTERED.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`, `--mid <name>` or `--prerun`; it writes data/b623_checks.txt before the push and
### data/b623_checks_postpush.txt after it; `--mid <name>` writes data/<name> and regenerates nothing. `--prerun` (the standing line of
### (R202)(3)): every arm run at HEAD BEFORE the face is sealed, no table regenerated, its counts written to data/b623_arms_prerun.txt.
### ### Every remote is read once per run (OPEN_TRAILS :12703, b616_claims.remote_refs), each run's ls-remote calls banked per repository
### beside its output (data/b623_lsr*.json); G-LSREMOTE-ONE-PER-REPO runs last.
### ### THE b622 DEFECTS' SOURCES, REPAIRED ((R233)'s Component 0): (a) a test's cases are counted by its case pattern, never by a line that
### merely ends in PASS (G-COUNT-TEST-COUNTED, G-PUSHGATED-TEST-COUNTED recount the banks); (c) a diff bank's stat line is compared with
### both sides stripped (G-PUSHGATED-DIFF-BANKED); (d) a re-emission compared against pages at a pin reads every repository at that same
### pin (G-GEN-OLD-LISTS-FROZEN: b602's and b603's lists with every relay read at 02fba720 and every PLACE-papers read at f695c98, through
### the frozen control's own swap). The source builder keeps an absent file as None (b621's repair, G-ABSENT-IS-NONE).
### ### The harness is b568's to b622's, carried from tools/b622_checks.py (its imports, helpers, regenerate and main); the sources,
### predicates and arms are b623's. Every positive control mutates a value its predicate reads and sets no value equal to this act's own.
### The no-disclosure needles are built at run time from TECHNE-Core's module documents and never printed.
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
import b623_worklist as K     # noqa: E402

NL = chr(10)
PP, GS, KER = 'D:/MY-DOwnloads/PLACE-papers', 'D:/SIDE-global-section', 'D:/SIDE-explicit-formula'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
FACE = os.path.join(D, 'b623_registration_2026-10-04.txt')
PAGE, DIR_PAGE = K.PAGE, K.DIR_PAGE
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP, gs='3528bcf', ker='1d5d4dd')
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b', 'product-b600': '1dd5cd7',
        'doubling-keiper-b601': '5fc0c87', 'sign-window-b602': '914c413', 'family-b603': '1d5d4dd'}
STEPZERO = K.STEPZERO
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
PUSH_FILES = ('tools/push_gated.sh', 'tools/test_push_gated.sh')
COUNT_FILES = ('tools/b623_record.py', 'tools/b623_test_count.py')
ABSENT = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_9.md'    # ### a file no act has written: G-ABSENT-IS-NONE's subject
OLD_PINS = ('02fba720', 'f695c98')                            # ### b622's S2 limb: relay and PLACE-papers before b622
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/db8d87ba-3c6c-4b82-8201-6f0312a45734/scratchpad'
INST = ('b622_checks.py', 'b622_record.py', 'b604_record.py', 'b602_record.py', 'b566_record.py', 'b565_record.py', 'b616_record.py',
        'b616_claims.py', 'b611_claims.py', 'b558_record.py', 'chain_page.py', 'test_chain_page_b596.py', 'g_chain_page.py', 'e0_rule.py',
        'banned_terms.py', 'terminal_table.py', 'table_gate.py', 'reg_seal.py', 'b378_lockgate.py')
SEALED_SUBJECT = 'b623 (R233)(3): the record tool as sealed'
COUNT_SUBJECT = 'b623 (R233)(3): the test count'
PUSH_SUBJECT = 'b623 (R233)(5)(a): push_gated.sh'
TABLE_SUBJECT = 'b623 housekeeping'
PROFILE_SUBJECT = 'b623 (R233)(5)(b): the prints'


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
    """### b621's repair, carried: an absent file stays None; only bytes are normalised."""
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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b623')
            and 'data/b623_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def strip_prose(t):
    t = re.sub(r'"""[\s\S]*?"""', '', t)
    t = re.sub(r"'''[\s\S]*?'''", '', t)
    return NL.join(l.split('#', 1)[0] for l in t.split(NL))


def wl_globs(face):
    try:
        w = face[face.index('### (W) THE WRITE LIST.'):face.index('### (Z) THE NOTHINGS.')]
    except ValueError:
        return []
    return sorted(set(re.findall(r'`((?:relay|PLACE-papers|SIDE-global-section|SIDE-structural-error-correction)/[^`\s]+)`', w)))


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
    for repo, name, pre in ((PP, 'PLACE-papers', PRE['pp']), (GS, 'SIDE-global-section', PRE['gs']), (K.SEC, 'SIDE-structural-error-correction', K.SEC_PIN[1])):
        ch = set(x for x in gs(repo, 'diff', '--name-only', pre).split(NL) if x.strip())
        ch |= set(x for x in gs(repo, 'diff', '--name-only', pre, 'HEAD').split(NL) if x.strip())
        if repo == PP:
            ch |= set(untracked(PP, 'phase1.5', 'phase2', 'day1'))
        if repo == K.SEC:
            ch |= set(untracked(K.SEC, '.'))
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


def kern_now(face):
    out = {}
    for k in face:
        p = 'D:/' + k
        tags = {}
        for l in gs(p, 'for-each-ref', '--format=%(refname:short) %(objectname) %(*objectname)', 'refs/tags').split(NL):
            if l.strip():
                x = l.split()
                tags[x[0]] = (x[2] if len(x) > 2 else x[1])[:7]
        out[k] = [gs(p, 'rev-parse', '--short=7', 'main'), tags, sorted(x for x in gs(p, 'branch', '--format=%(refname:short)').split(NL) if x.strip())]
    return out


def sources():
    import b623_record as REC
    import b616_record as R6
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b623_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b623_') and f.endswith('.py'))
    S = dict(
        REC=REC, face=face, ferry=rd('b623_ferry.txt'), scan=rd('b623_ferry_scan.txt'), cens=rd('b623_census_stepzero.txt'),
        fcens=rd('b623_faces_census_stepzero.txt'), pins0=rd('b623_pins_stepzero.txt'), procs=rd('b623_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b622_closing.txt'), reads=rd('b623_reads.txt'), branches=rd('b623_branches.txt'), answers=rd('b623_author_answers.txt'),
        prerun=rd('b623_arms_prerun.txt'), defects=rd('b623_defects.txt'),
        rl=jl('b623_record_lines.json'), offj=jl('b623_offering.json'), offt=rd('b623_offering.txt'),
        ctj=jl('b623_count_test.json'), ctt=rd('b623_count_test.txt'), ptj=jl('b623_push_test.json'), ptt=rd('b623_push_test.txt'),
        pdiff=rd('b623_push_diff.txt'), tagj=jl('b623_tags.json'), tagt=rd('b623_tags.txt'), rbj=jl('b623_tags_readback.json'),
        hkj=jl('b623_housekeeping.json'), regj=jl('b623_registry.json'), sexj=jl('b623_sec_exports.json'), sart=jl('b623_sec_artefact.json'),
        prof=jl('b623_profile.json'), sprt=rd('b623_sec_prints.txt'), stag=jl('b623_sec_tag.json'), tblj=jl('b623_table.json'),
        tierj=jl('b623_tiers_reread.json'), buildj=jl('b623_sec_build.json'),
        pj={k: jl('b623_page_%s.json' % k) for k in ('zeta', 'chi')}, arms=rd('b623_page_arms.txt'),
        absent=tri(PP, ABSENT, PRE['pp']),
        pushfiles={p: tri(ROOT, p, PRE['relay']) for p in PUSH_FILES},
        countfiles={p: tri(ROOT, p, PRE['relay']) for p in COUNT_FILES},
        registry=tri(PP, 'REGISTRY.md', PRE['pp']),
        hkfiles={x['file']: tri(ROOT, x['file'], PRE['relay']) for x in (jl('b623_housekeeping.json').get('files') or [])},
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
        kern_face=(jl('b623_kernels_face.json').get('kernels') or {}),
        lv_head=gs('D:/SIDE-lv-conservation', 'rev-parse', 'HEAD'), lv_dirty=gs('D:/SIDE-lv-conservation', 'status', '--porcelain', '--untracked-files=no'),
        trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain', '--untracked-files=no'),
        sec=dict(cur=gs(K.SEC, 'branch', '--show-current'), dirty=gs(K.SEC, 'status', '--porcelain', '--untracked-files=no'),
                 main=gs(K.SEC, 'rev-parse', 'main'), branch=gs(K.SEC, 'rev-parse', '-q', '--verify', 'refs/heads/' + K.SEC_BRANCH),
                 tag_peel=gs(K.SEC, 'rev-parse', '-q', '--verify', K.SEC_TAG + '^{commit}'),
                 tag_type=gs(K.SEC, 'cat-file', '-t', 'refs/tags/' + K.SEC_TAG),
                 pushb=gs(K.SEC, 'branch', '--list', 'push-*'), artefact=cr0(blob(K.SEC, '%s:%s' % (K.SEC_TAG, K.SEC_ARTEFACT))),
                 mods_pin={m: blob(K.SEC, '%s:%s' % (K.SEC_PIN[1], m)) for m in K.SEC_MODULES},
                 mods_tag={m: blob(K.SEC, '%s:%s' % (K.SEC_TAG, m)) for m in K.SEC_MODULES}),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b622*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b623_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b623_mustnotexist.txt')), table_changed=None,
        fj=jl('b623_findings.json'), tj=jl('b623_trail.json'), sc=jl('b623_scores.json'), desk=rd('b623_desk_notes.txt'),
        tbl_now=jl('terminal_table.json'), lsr=None,
        rlog=[(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in gs(ROOT, 'log', '--reverse', '--format=%h %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
    )
    S['kern_now'] = kern_now(S['kern_face']) if S['kern_face'] else {}
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
    # ### every tag kernel's and SEC's remote, read once (OPEN_TRAILS :12703)
    S['remotes'] = {k: KC0.remote_refs('D:/' + k) for k in K.TAG_KERNELS + [K.SEC_NAME]}
    S['peels'] = {(k, t): gs('D:/' + k, 'rev-parse', '-q', '--verify', t + '^{commit}') for k, t, _s in K.TAGS}
    # ### the act's new public text: the ledger appends, its relay banks and tools, the housekeeping lists, REGISTRY's appended note, the
    # ### artefact module
    pub = []
    for nm, pre, now in (('FINDINGS', S['fi_pre'], S['fi_now']), ('OPEN_TRAILS', S['ot_pre'], S['ot_now'])):
        pub.append(now[len(pre):].decode('utf-8', 'replace') if now and pre and now.startswith(pre) else '')
    for f in sorted(os.listdir(D)):
        if f.startswith(('b623_', 'audit_b623_')) and os.path.isfile(os.path.join(D, f)):
            pub.append(read(os.path.join(D, f)))
    pub += [read(f) for f in tools]
    for p, (now, _pre, _h) in S['hkfiles'].items():
        pub.append((now or b'').decode('utf-8', 'replace'))
    a, pre_r, _h = S['registry']
    pub.append((a or b'')[len(pre_r or b''):].decode('utf-8', 'replace'))
    pub.append((S['sec']['artefact'] or b'').decode('utf-8', 'replace'))
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
    S.update(extra_sources(S))
    return S


def extra_sources(S):
    import chain_page as CP
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    X = {}
    for k in ('zeta', 'chi'):
        X['gcp_' + k] = GCP.arm(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b623_gcp'), os.path.join(D, K.PROBE[k]))
    X['ctl'] = TC.control()
    X['ctl_arm'] = TC.ARM
    # ### b622's defect (d), repaired: b602's and b603's lists, without the column, re-emitted with EVERY relay read at 02fba720 and EVERY
    # ### PLACE-papers read at f695c98 -- the frozen control's own swap, its pins set for the call and restored -- against the pages at f695c98
    old = []
    pins = (TC.RELAY_PIN, TC.PRE_PP)
    TC.RELAY_PIN, TC.PRE_PP = OLD_PINS
    try:
        for k in ('zeta', 'chi'):
            rc, got = TC.regen(os.path.join(D, K.OLD_NODES[k]), os.path.join(D, K.PROBE[k]))
            old.append(dict(list=K.OLD_NODES[k], rc=rc, equal=got is not None and got == cr0(blob(PP, '%s:%s' % (OLD_PINS[1], K.PNAME[k])))))
    finally:
        TC.RELAY_PIN, TC.PRE_PP = pins
    X['old_frozen'] = old
    X['cites_now'] = {}
    ruled = {f: K.show(f, PRE['pp']) for f in K.RULED_LEDGERS}
    for k, t, _s in K.TAGS:
        X['cites_now'][(k, t)] = sorted((f, n, s) for f, v in K.citations(k, t, ruled).items() for n, s, _l in v)
    X['exports_now'] = K.sec_exports()
    X['sec_text_now'] = S['REC'].sec_text()[0] if X['exports_now'] else None
    X['offer_now'] = S['REC'].offering_rows(read(os.path.join(PP, 'FINDINGS.md')))
    X['push_stat'] = gs(ROOT, 'diff', '--stat', PRE['relay'], '--', *PUSH_FILES).split(NL)[-1].strip()
    import b623_record as REC
    X['count_bank_now'] = REC.count_cases(S['ctt'], REC.COUNT_CASE) if S['ctt'] else None
    X['push_bank_now'] = REC.count_cases(S['ptt'], REC.PUSH_CASE) if S['ptt'] else None
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


def rline(S, i):
    x = (S['rl'].get('lines') or [])
    return x[i] if len(x) > i else {}


def weight_ok(S):
    x = rline(S, 0)
    a = fline(S, x.get('line'))
    ot = [rline(S, i).get('line') for i in range(1, 7)]
    return bool(x) and x.get('file') == 'FINDINGS.md' and a.startswith(x['head']) and '(:7466)' in a and 'b622 AT ITS WEIGHT' in a \
        and 'the ζ page at 52 nodes' in a and 'the χ page at 36' in a and '27 rows at the generator’s mark, 25 agreeing' in a \
        and 're-pin 503 of 503' in a and 'The suite 78 of 81 before the push' in a and '**Ruled, `(R233)`(1):**' in a \
        and all(o for o in ot) and ('OPEN_TRAILS :%d (the three nodes' % ot[0]) in a and (':%d-:%d (the four work-orders)' % (ot[2], ot[5])) in a


def unc_ok(S):
    x = rline(S, 1)
    o = oline(S, x.get('line'))
    return bool(x) and o.startswith(x.get('head', '\x00')) and '(:12266)' in o and 'EF_lit_zetaZeroConfig, KeiperObligations, WindowObligations take UNIVERSAL' in o \
        and '**The bundle clause:**' in o and 'RH-03' in o and x['line'] > 12885


def tc_ok(S):
    x = rline(S, 2)
    o = oline(S, x.get('line'))
    return bool(x) and o.startswith(x.get('head', '\x00')) and '(:12799)' in o and 'never by its summary lines' in o and 'plants a summary line' in o \
        and 'b597 and b622' in o


def wo_ok(S):
    out = []
    for i, (wid, roman, items, price) in enumerate(K.WORK_ORDERS):
        x = rline(S, 3 + i)
        o = oline(S, x.get('line'))
        out.append(bool(x) and o.startswith(x.get('head', '\x00')) and wid in o and ('Items: %s.' % items) in o and ('Price: %s.' % price) in o
                   and 'Trigger: the author’s word.' in o and 'Not started.' in o)
    return len(out) == 4 and all(out) and [rline(S, 3 + i).get('line') for i in range(4)] == sorted(rline(S, 3 + i).get('line') or 0 for i in range(4))


def offer_ok(S):
    r = S['offer_now']
    keyf = lambda x: (x['line'], x['act'], x['carries'])   # noqa: E731
    return bool(r) and [keyf(x) for x in r] == [keyf(x) for x in S['offj'].get('rows') or []] and S['offj'].get('entries') == len(r) \
        and S['offj'].get('carrying') == sum(x['carries'] for x in r) and S['offj'].get('without') == sum(not x['carries'] for x in r) \
        and ('CARRYING THE OFFERING LINE : %d ; WITHOUT : %d.**' % (S['offj'].get('carrying'), S['offj'].get('without'))) in S['offt']


def alone(S, files, prefix):
    c = [h for h, f in S['rfiles'].items() if f == sorted(files)]
    msg = {h: s for h, s in S['rlog']}
    return len(c) == 1 and msg[c[0]].split(' ', 1)[1].startswith(prefix) and S['lock_epoch'] is not None \
        and int(msg[c[0]].split(' ', 1)[0]) > S['lock_epoch']


def count_alone(S):
    """### the record tool as sealed in one commit of its own, then the repair and its test in one commit of their own, after the lock;
    ### the repair's diff against the sealed form touches count_cases alone."""
    msg = {h: s for h, s in S['rlog']}
    sealed = [h for h, f in S['rfiles'].items() if f == ['tools/b623_record.py'] and msg[h].split(' ', 1)[1].startswith(SEALED_SUBJECT)]
    rep = [h for h, f in S['rfiles'].items() if f == sorted(COUNT_FILES) and msg[h].split(' ', 1)[1].startswith(COUNT_SUBJECT)]
    if len(sealed) != 1 or len(rep) != 1 or S['lock_epoch'] is None:
        return False
    d = gs(ROOT, 'diff', '-U0', sealed[0], rep[0], '--', 'tools/b623_record.py')
    ch = [l for l in d.split(NL) if l[:1] in '+-' and not l.startswith(('+++', '---'))]
    order = [h for h, _s in S['rlog']]
    return all(int(msg[h].split(' ', 1)[0]) > S['lock_epoch'] for h in sealed + rep) and order.index(sealed[0]) < order.index(rep[0]) \
        and bool(ch) and all(('cases' in l or 'rx' in l or 'case_re' in l or '"""' in l or '###' in l) for l in ch)


def count_test_ok(S):
    n = S['count_bank_now']
    return bool(n) and n[0] == S['ctj'].get('cases') == 6 and n[1] == S['ctj'].get('passing') == 6 and S['ctj'].get('sealed_refuted') is True \
        and S['ctj'].get('repaired_all_pass') is True and '### ALL PASS' in S['ctt'] and S['ctj'].get('rc') == 0


def push_diff_ok(S):
    files = S['pushfiles']
    stat = S['push_stat']
    banked = [l[4:].strip() for l in S['pdiff'].split(NL) if l.startswith('### ') and 'changed' in l]
    return all(a is not None and a == c and a != b for a, b, c in files.values()) and bool(stat) and banked == [stat.strip()] \
        and '+if [ "$branch" = "--existing-tag" ]; then' in S['pdiff'] and '+echo "### CASE J -- the existing-tag mode, a lightweight tag"' in S['pdiff']


def push_test_ok(S):
    n = S['push_bank_now']
    m = re.search(r'\*\*(\d+) of (\d+) checks as wanted -- PASS\*\*', S['ptt'])
    return bool(n) and bool(m) and n[0] == int(m.group(2)) == S['ptj'].get('cases') and n[1] == int(m.group(1)) == S['ptj'].get('passing') == n[0] \
        and S['ptj'].get('rc') == 0 and all(('  %s exit : wanted' % c) in S['ptt'] for c in 'JKLM')


def tags_banked(S):
    rows = S['tagj'].get('rows') or []
    return len(rows) == 12 and [(r['kernel'], r['tag']) for r in rows] == [(k, t) for k, t, _s in K.TAGS] \
        and all(r['local_peel'].startswith(s) for r, (_k, _t, s) in zip(rows, K.TAGS)) and all(r['url'].startswith('https://github.com/') for r in rows) \
        and 'CITED : 9 ; CITED BY NO LEDGER : 3' in S['tagt'] and S['tagj'].get('pre_pp') == PRE['pp']


def cites_now(S):
    rows = S['tagj'].get('rows') or []
    if len(rows) != 12:
        return False
    for r in rows:
        got = sorted((f, n, s) for f, v in r['cited'].items() for n, s in v)
        if got != S['cites_now'][(r['kernel'], r['tag'])]:
            return False
    return True


def at_remote(S):
    """### each tag read now at its remote (read once this run): a cited tag present with the local peel, an uncited one absent."""
    rows = S['tagj'].get('rows') or []
    out = []
    for r in rows:
        refs = S['remotes'].get(r['kernel']) or {}
        rp = refs.get('refs/tags/%s^{}' % r['tag']) or refs.get('refs/tags/%s' % r['tag'])
        loc = S['peels'].get((r['kernel'], r['tag']))
        out.append((rp == loc and bool(loc)) if r['cited'] else rp is None)
    return len(out) == 12 and all(out) and bool(S['remotes'])


def tags_unmoved(S):
    f, n = S['kern_face'], S['kern_now']
    return bool(f) and all(k in f and k in n and n[k][0] == f[k][0] and n[k][1] == f[k][1] and n[k][2] == f[k][2] for k in K.TAG_KERNELS)


def tagpush_logs(S):
    rows = S['tagj'].get('rows') or []
    out = []
    for r in rows:
        p = 'b623_tagpush_%s_%s.txt' % (r['kernel'][5:], r['tag'])
        t = rd(p)
        if r['cited']:
            m = re.search(r'push_gated: tag %s peeled local (\w+) remote (\w+)' % re.escape(r['tag']), t)
            out.append(bool(m) and m.group(1) == m.group(2) and m.group(1).startswith(r['local_peel'][:7]) and t.count('push_gated: DONE -- existing tag %s' % r['tag']) == 1
                       and ('existing tag %s (' % r['tag']) in t and 'no main push' in t and 'main read back at the remote' not in t)
        else:
            out.append(not os.path.exists(os.path.join(D, p)))
    return len(out) == 12 and all(out)


def hk_ok(S):
    files = S['hkj'].get('files') or []
    want = {'data/SIDE-bijection_housekeeping.txt', 'data/SIDE-class-coupling_housekeeping.txt', 'data/SIDE-meta_housekeeping.txt',
            'data/SIDE-omega-b_housekeeping.txt', 'data/SIDE-substrate-cluster_housekeeping.txt'}
    if set(x['file'] for x in files) != want or S['hkj'].get('dry') is not False:
        return False
    for x in files:
        now, pre, head = S['hkfiles'][x['file']]
        if now is None or pre is not None or now != head or hashlib.sha256(now).hexdigest() != x['sha256']:
            return False
    t = {x['file']: (S['hkfiles'][x['file']][0] or b'').decode('utf-8') for x in files}
    return 'SIDE-meta v0.1 = e262713 -- LOCAL, NOT PUSHED' in t['data/SIDE-meta_housekeeping.txt'] \
        and 'SIDE-meta v0.3 = 6bb7b23 -- PUSHED, ONE COMMIT WITH v0.1.0' in t['data/SIDE-meta_housekeeping.txt'] \
        and 'SIDE-substrate-cluster v0.1 = 5b102b4 -- LOCAL, NOT PUSHED' in t['data/SIDE-substrate-cluster_housekeeping.txt'] \
        and 'SIDE-substrate-cluster v0.2 = 9068d3c -- LOCAL, NOT PUSHED' in t['data/SIDE-substrate-cluster_housekeeping.txt'] \
        and 'SIDE-bijection v0.1 = dd487e6 -- PUSHED, ONE COMMIT WITH v0.1.0' in t['data/SIDE-bijection_housekeeping.txt']


def registry_ok(S):
    a, pre, head = S['registry']
    if a is None or pre is None or a != head or not a.startswith(pre) or len(a) <= len(pre):
        return False
    add = a[len(pre):].decode('utf-8')
    return add.count(S['REC'].REG_HEAD) == 1 and add.rstrip(NL).endswith(S['REC'].REG_TAIL) and S['regj'].get('para', '\x00') in add \
        and hashlib.sha256(a).hexdigest() == S['regj'].get('sha256') and 'the peeled commit read back equal at each remote' in add \
        and 'NOT READ' not in add


def pp_alone(S, path, prefix, n=1):
    c = [h for h, f in S['pp_files'].items() if path in f]
    return len(c) == n and all(S['pp_files'][h] == [path] and dict(S['pp_log'])[h].startswith(prefix) for h in c)


def _h(S, k, want):
    return (S['sc'].get(k) or [''])[0] == want and ('(%s)' % k.upper()) in S['desk'] and ('### **%s.**' % want) in S['desk']


def h57_ok(S, k):
    if k == 'H57a':
        want = 'HOLDS' if at_remote(S) and tagpush_logs(S) else 'REFUTED'
    elif k == 'H57b':
        want = 'HOLDS' if at_remote(S) and sum(1 for r in S['tagj'].get('rows') or [] if r['cited']) == 9 else 'REFUTED'
    elif k == 'H57c':
        want = 'HOLDS' if prints_ok(S) else 'REFUTED'
    else:
        want = 'HOLDS' if table_rows_ok(S) else 'REFUTED'
    return _h(S, k, want)


def exports_ok(S):
    ex = S['exports_now'] or []
    return len(ex) == 62 and [list(x) for x in ex] == S['sexj'].get('exports') and sum(1 for x in ex if x[2] == 'theorem') == 34 \
        and all(n in [x[3] for x in ex] for n in K.SEC_SIX + K.SEC_NAMED)


def artefact_ok(S):
    a = S['sec']['artefact']
    ex = S['exports_now'] or []
    return a is not None and S['sec_text_now'] is not None and a == S['sec_text_now'].encode('utf-8') \
        and a.decode('utf-8').count('#print axioms ') == len(ex) == 62 and hashlib.sha256(a).hexdigest() == S['sart'].get('sha256')


def sec_tag_ok(S):
    st, sec = S['stag'], S['sec']
    rp = (S['remotes'].get(K.SEC_NAME) or {}).get('refs/tags/%s^{}' % K.SEC_TAG)
    return bool(sec['tag_peel']) and rp == sec['tag_peel'] and sec['tag_type'] == 'tag' and st.get('equal') is True and st.get('files') == [K.SEC_ARTEFACT] \
        and st.get('parent') == K.SEC_PIN[1] and st.get('local_peel') == sec['tag_peel'] \
        and (S['remotes'].get(K.SEC_NAME) or {}).get('refs/heads/main') == sec['tag_peel']


def prints_ok(S):
    P = S['prof']
    ex = S['exports_now'] or []
    th = [n for _m, _l, k, n in ex if k == 'theorem']
    got = {}
    for l in P.get('lines') or []:
        m = S['REC'].PRINT_LINE.match(l)
        if m:
            got[m.group(1)] = [x.strip() for x in (m.group(3) or '').split(',') if x.strip()]
    return len(ex) == 62 and set(got) == set(n for _m, _l, _k, n in ex) and P.get('exit') == 0 and P.get('sorry') is False \
        and all(all(x in K.STD3 for x in got[n]) for n in th) and all(P['std3'].get(n) == all(x in K.STD3 for x in got[n]) for n in got) \
        and 'PRINTED : 62 of 62' in S['sprt']


def build_ok(S):
    B = S['buildj']
    calls = B.get('calls') or []
    return len(calls) == 4 and all(c.get('start_free') is not None and c['start_free'] >= 2560 and c.get('rc') == 0 and c.get('detached') is True for c in calls) \
        and [c.get('target') for c in calls] == ['+SIDEStructuralErrorCorrection.Basic', '+SIDEStructuralErrorCorrection.DeAlignment',
                                                 '+SIDEStructuralErrorCorrection', 'AxiomCheck.lean']


def sec_branch_ok(S):
    sec = S['sec']
    return bool(sec['tag_peel']) and sec['branch'] == sec['tag_peel'] == sec['main'] and sec['cur'] == 'main' and sec['dirty'] == '' and sec['pushb'] == '' \
        and all(sec['mods_pin'][m] is not None and sec['mods_pin'][m] == sec['mods_tag'][m] for m in K.SEC_MODULES)


def profile_committed(S):
    msg = {h: s for h, s in S['rlog']}
    c = [h for h, f in S['rfiles'].items() if 'data/b623_profile.json' in f]
    t = [h for h, f in S['rfiles'].items() if f == sorted('data/' + x for x in TABLE_FILES)]
    order = [h for h, _s in S['rlog']]
    return len(c) == 1 and msg[c[0]].split(' ', 1)[1].startswith(PROFILE_SUBJECT) and len(t) == 1 and order.index(c[0]) < order.index(t[0]) \
        and cr0(blob(ROOT, '%s:data/b623_profile.json' % c[0])) == cr0(raw(os.path.join(D, 'b623_profile.json')))


def table_rows_ok(S):
    B = S['tblj']
    rows = [x for x in (S['tbl_now'].get('rows') or []) if x['repo'] == K.SEC_NAME]
    added = B.get('added') or []
    return len(rows) == 62 and all(x['profile_state'] == 'PROFILED' for x in rows) and len(added) == 62 and all(x and x[0] == K.SEC_NAME for x in added) \
        and not B.get('gone') and not B.get('changed') and B.get('sec_rows') == 62 and B.get('sec_profiled') == 62


def table_alone(S):
    msg = {h: s for h, s in S['rlog']}
    t = [h for h, f in S['rfiles'].items() if f == sorted('data/' + x for x in TABLE_FILES)]
    return len(t) == 1 and msg[t[0]].split(' ', 1)[1].startswith(TABLE_SUBJECT) and S['lock_epoch'] is not None \
        and int(msg[t[0]].split(' ', 1)[0]) > S['lock_epoch']


def tiers_ok(S):
    rows = S['tierj'].get('rows') or []
    return len(rows) >= 6 and all(x['same'] and x['modules_same_at_tag'] for x in rows) and set(x['name'] for x in rows) >= set(K.SEC_SIX)


def pages_now(S):
    out = []
    for k, p in (('zeta', PAGE), ('chi', DIR_PAGE)):
        a, _b, c = S['pages'][p]
        j = S['pj'][k]
        out.append(j.get('rc') == 0 and j.get('dry') is False and a is not None and a == c and hashlib.sha256(c).hexdigest() == j.get('sha256')
                   and (pp_alone(S, p, 'b623 (R233)', 1) if j.get('changed') else not [h for h, f in S['pp_files'].items() if p in f]))
    return all(out)


def arms_ok(t):
    return 'PAGE ARMS PASSING : 2 of 2' in t and ('%s PASSING : 2 of 2' % CONTROL_ARM) in t


def hold_ok(S):
    a = S['answers']
    return re.search(r'### b623 -- THE AUTHOR`S ANSWERS, 2 prompt\(s\)', a) is not None and a.count('RESULT (transcript line') == 1 \
        and 'existing-tag mode' in a and 'option 1' in a and 'version cell' in a


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(S['REC'].CURRENTS)


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 20]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') and fline(S, e).startswith('## The unpushed tags: ') \
        and all(x in tail for x in ('**The tags**', '**The artefact**', '**The record lines**', '**The scores.**', '**Read in mutual light**',
                                    'strengthens', '**Next.**', 'b624'))


def wl_ok(S):
    return bool(S['globs']) and all(any(fnmatch.fnmatch(f, p) for p in S['globs']) for f in S['written'])


def scored(S, k):
    v = S['sc'].get(k)
    return bool(v) and v[0] in ('HELD', 'REFUTED', 'NOT SCORABLE', 'HOLDS') and ('(%s)' % k.upper() in S['desk'] or '(%s)' % k in S['desk'])


def no_delete(S):
    words = ['os' + r'\.' + 'remove', 'os' + r'\.' + 'unlink', 'shutil' + r'\.' + 'rmtree', 'os' + r'\.' + 'rmdir',
             'rm' + ' -' + 'rf', 'Remove' + '-' + 'Item', r'\.' + 'unlink' + r'\(', 'git' + ' branch -' + 'D', 'worktree' + ' remove' + r'\b',
             'tag' + ' -' + 'd' + r'\b']
    pat = re.compile(r'(' + '|'.join(words) + r')')
    return bool(S['tooltext']) and not [f for f, t in S['tooltext'].items() if pat.search(t)]


def kernels_untouched(S):
    f, n = S['kern_face'], S['kern_now']
    seven = [k for k in S['REC'].KERNS]
    return bool(f) and all(k in f and n[k] == f[k] for k in seven) and all(n[k][0].startswith(v) for k, v in S['REC'].KERN_PIN.items()) \
        and S['kcur'] == 'main' and S['kdirty'] == '' and S['trial'] == 'f22ff35' and S['lv_head'].startswith('2f71068a') and S['lv_dirty'] == '' \
        and all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items())


def corpus_scope(S):
    pages = [K.PNAME[k] for k in ('zeta', 'chi') if S['pj'][k].get('changed')]
    return S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', 'REGISTRY.md'] + pages)


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


def _mut_rl(S, i, key, val):
    x = copy.deepcopy(S['rl'])
    if len(x.get('lines') or []) > i:
        x['lines'][i][key] = val
    return put(S, 'rl', x)


READ_NEEDLES = ('THE_KEYSTONE_CENSUS_v0_4.md @ c9e9a9c7', 'OPEN_TRAILS.md @ c9e9a9c7', 'REGISTRY.md @ c9e9a9c7', 'SPIRAL_MAP.md @ c9e9a9c7',
                'SPIRAL_MAP_v0_7.md @ c9e9a9c7', 'FINDINGS.md @ c9e9a9c7', 'lakefile.toml @ 6a4f4829', 'AxiomCheckFamily.lean @ ',
                'tools/terminal_table.py @ 5d0816dd', 'tools/push_gated.sh @ 5d0816dd', 'data/b557_tiers.txt @ 5d0816dd',
                'data/b622_unclassified.txt @ 5d0816dd', 'data/b622_closing_push_out.txt @ 6cbe1a2a',
                ':12597 ', ':12330 ', ':11864 ', ':12228 ', ':12266 ', ':12799 ', ':12863 ', ':12885 ', ':628 ', ':7304 ')

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R233) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b622`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b622' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b623 -- x'])),
    ('G-R233-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R233) END' in S['ferry'] and S['ot'].count('**(R233) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R233) ratified', '(R233) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in READ_NEEDLES) and 'NO SUCH LINE' not in S['reads'],
     lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ANSWERS-BANKED', 'the act`s answers bank: the two prompts before the seal, verbatim, their options and their answers', lambda S: hold_ok(S),
     lambda S: put(S, 'answers', S['answers'].replace('2 prompt(s)', '3 prompt(s)', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay 6cbe1a2a`s files', lambda S: S['pushout'][0] == ['data/b622_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/b622_closing_push_out.txt', 'x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b622') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b622'}))),
    ('G-KEPT-BRANCHES', 'the explicit-formula kernel`s kept branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'family-b603': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80 and every PLACE-papers read at ba5f0ea, run afresh through the test`s control()',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(S['ctl'][0], ok=False)] + S['ctl'][1:])),
    ('G-INSTRUMENTS-UNEDITED', 'b622`s suite and record tool, the shared record tools, b616`s and b611`s claims modules, the generator and its test, the page arm, the E0 rule, the scanner, the table generator and its gate, the seal and the lock gate against 5d0816dd',
     lambda S: all(a is not None and a == b for a, b in S['inst'].values()) and len(S['inst']) == len(INST),
     lambda S: put(S, 'inst', dict(S['inst'], **{'b622_record.py': (S['inst']['b622_record.py'][0], (S['inst']['b622_record.py'][1] or b'') + b'x')}))),
    ('G-ABSENT-IS-NONE', 'the source builder on a file no act wrote (disk, c9e9a9c, HEAD) and on empty bytes', lambda S: absent_ok(S),
     lambda S: put(S, 'absent', (b'', b'', b''))),
    ('G-GEN-OLD-LISTS-FROZEN', 'b602`s and b603`s lists re-emitted now with every relay read at 02fba720 and every PLACE-papers read at f695c98, against the pages at f695c98',
     lambda S: len(S['old_frozen']) == 2 and all(x['rc'] == 0 and x['equal'] for x in S['old_frozen']),
     lambda S: put(S, 'old_frozen', [S['old_frozen'][0], dict(S['old_frozen'][1], equal=False)] if len(S['old_frozen']) == 2 else [])),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b622`s weight with the ruling and the OPEN_TRAILS lines it cites', lambda S: weight_ok(S),
     lambda S: put(S, 'find', S['find'].replace('re-pin 503 of 503', 're-pin 502 of 503'))),
    ('G-UNCLASSIFIED-RULED', 'OPEN_TRAILS at the banked line: the three nodes ruled UNIVERSAL and the bundle clause, addressed to :12266', lambda S: unc_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('**The bundle clause:**', '**A clause:**'))),
    ('G-TESTCOUNT-STANDING', 'OPEN_TRAILS at the banked line: the test count, standing, addressed to :12799', lambda S: tc_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('plants a summary line', 'plants a line'))),
    ('G-WORKORDERS-ENTERED', 'OPEN_TRAILS at the banked lines: the four work-orders with their items, prices and triggers', lambda S: wo_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('Price: one act, one module, no new analysis.', 'Price: two acts.'))),
    ('G-OFFERING-LINE-COUNT', 'FINDINGS read now: the entries b594-b622 carrying the offering line and those without, against the bank and its printed count',
     lambda S: offer_ok(S), lambda S: put(S, 'offer_now', [dict(x, carries=False) if i == 0 else x for i, x in enumerate(S['offer_now'])])),
    ('G-COUNT-REPAIR-ALONE', 'relay`s log: the record tool as sealed, then its count repair and the test in one commit of their own, after the lock, the diff touching the counter alone',
     lambda S: count_alone(S), lambda S: put(S, 'rfiles', dict(S['rfiles'], deadbee=sorted(COUNT_FILES)))),
    ('G-COUNT-TEST-COUNTED', 'the count test`s bank, recounted now by its case pattern: six of six, the sealed form refuted', lambda S: count_test_ok(S),
     lambda S: put(S, 'ctt', S['ctt'] + '\n  (7) planted : PASS')),
    ('G-PUSHGATED-COMMITTED-ALONE', 'relay`s log: push_gated.sh and its test in one commit of their own, after the lock', lambda S: alone(S, list(PUSH_FILES), PUSH_SUBJECT),
     lambda S: put(S, 'rfiles', dict(S['rfiles'], deadbee=sorted(PUSH_FILES)))),
    ('G-PUSHGATED-DIFF-BANKED', 'push_gated.sh and its test on disk and at HEAD against 5d0816dd, the diff bank`s stat line with both sides stripped, the mode and the cases in it',
     lambda S: push_diff_ok(S), lambda S: put(S, 'pdiff', S['pdiff'].replace('+if [ "$branch" = "--existing-tag" ]; then', '+if true; then'))),
    ('G-PUSHGATED-TEST-COUNTED', 'the push_gated test`s bank, recounted now by its case pattern against its own summary line, the four new cases present',
     lambda S: push_test_ok(S), lambda S: put(S, 'ptt', S['ptt'] + '\n  Z extra : wanted 1 ; got 1 ; PASS')),
    ('G-TAGS-BANKED', 'the tags bank: the twelve tags in the census`s order, each peel, remote and the count line', lambda S: tags_banked(S),
     lambda S: put(S, 'tagt', S['tagt'].replace('CITED : 9 ; CITED BY NO LEDGER : 3', 'CITED : 8 ; CITED BY NO LEDGER : 4'))),
    ('G-TAGS-CITED-NOW', 'every tag`s citations recomputed now over the ruled ledgers at c9e9a9c, against the bank', lambda S: cites_now(S),
     lambda S: put(S, 'cites_now', dict(S['cites_now'], **{('SIDE-meta', 'v0.1'): [('SPIRAL_MAP.md', 1, 'cell')]}))),
    ('G-TAGS-AT-REMOTE', 'each tag read now at its remote: every cited one at the local peel, every uncited one absent', lambda S: at_remote(S),
     lambda S: put(S, 'remotes', dict(S['remotes'], **{'SIDE-coupling': {}}))),
    ('G-TAGS-UNMOVED', 'the nine kernels` mains, local tags by name and peel, and branches against the face', lambda S: tags_unmoved(S),
     lambda S: put(S, 'kern_now', dict(S['kern_now'], **{'SIDE-omega-b': [S['kern_now'].get('SIDE-omega-b', ['', {}, []])[0], {'v0.1': '0000000'}, []]}))),
    ('G-TAGPUSH-LOGS', 'each cited tag`s push_gated capture: the existing-tag mode, no main push, the peels equal, done; no capture for an uncited tag', lambda S: tagpush_logs(S),
     lambda S: put(S, 'tagj', dict(S['tagj'], rows=[dict(r, cited={}) if r['tag'] == 'v0.4' else r for r in S['tagj'].get('rows') or []]))),
    ('G-HOUSEKEEPING-LISTS', 'the five housekeeping lists on disk and at HEAD, created, against their bank, the local and one-commit rows in them', lambda S: hk_ok(S),
     lambda S: put(S, 'hkj', dict(S['hkj'], files=(S['hkj'].get('files') or [])[1:]))),
    ('G-REGISTRY-ROW-UPDATE', 'REGISTRY on disk and at HEAD: its blob at c9e9a9c with the one dated row update appended, the read-backs equal in it', lambda S: registry_ok(S),
     lambda S: put(S, 'registry', ((S['registry'][0] or b'') + b'x', S['registry'][1], S['registry'][2]))),
    ('G-REGISTRY-COMMITTED-ALONE', 'PLACE-papers` log since c9e9a9c: REGISTRY in one commit of its own', lambda S: pp_alone(S, 'REGISTRY.md', 'b623 (R233)(5)(a)'),
     lambda S: put(S, 'pp_files', dict(S['pp_files'], deadbee=['REGISTRY.md']))),
    ('G-H57A-SCORED', 'H57a recomputed now, against the scores and the desk', lambda S: h57_ok(S, 'H57a'), lambda S: _sc(S, 'H57a')),
    ('G-H57B-SCORED', 'H57b recomputed now, against the scores and the desk', lambda S: h57_ok(S, 'H57b'), lambda S: _sc(S, 'H57b')),
    ('G-SEC-EXPORTS-NOW', 'SIDE-structural-error-correction`s declarations read now from the blobs at 6a4f482, against the bank', lambda S: exports_ok(S),
     lambda S: put(S, 'exports_now', (S['exports_now'] or [])[1:])),
    ('G-SEC-ARTEFACT-AT-TAG', 'AxiomCheck.lean at v0.2.2 against the house form built now from the exports, one print per declaration', lambda S: artefact_ok(S),
     lambda S: put(S, 'sec', dict(S['sec'], artefact=(S['sec']['artefact'] or b'').replace(b'#print axioms DeAlignment.fano_two_design', b'')))),
    ('G-SEC-TAG-READBACK', 'v0.2.2 at the remote (read once) against the local peel: annotated, on 6a4f482, adding AxiomCheck.lean alone, the remote main at it',
     lambda S: sec_tag_ok(S), lambda S: put(S, 'stag', dict(S['stag'], files=[K.SEC_ARTEFACT, 'README.md']))),
    ('G-SEC-PRINTS', 'the prints bank and the profile json: every declaration printed, exit 0, no sorryAx, every theorem within the standard three', lambda S: prints_ok(S),
     lambda S: put(S, 'prof', dict(S['prof'], sorry=True))),
    ('G-SEC-BUILD-DETACHED', 'the build bank: four detached calls, one module each in import order, each started above the hold, each exit 0', lambda S: build_ok(S),
     lambda S: put(S, 'buildj', dict(S['buildj'], calls=[dict(c, start_free=1000) if i == 0 else c for i, c in enumerate(S['buildj'].get('calls') or [])]))),
    ('G-SEC-BRANCH-KEPT', 'SIDE-structural-error-correction: the branch, main and the tag on one commit, main checked out clean, no push branch left, the modules unchanged at the tag',
     lambda S: sec_branch_ok(S), lambda S: put(S, 'sec', dict(S['sec'], pushb='push-b623-sec'))),
    ('G-PROFILE-COMMITTED', 'relay`s log: the profile json committed before the table`s housekeeping commit, its blob equal to the bank', lambda S: profile_committed(S),
     lambda S: put(S, 'rfiles', {h: (f if 'data/b623_profile.json' not in f else []) for h, f in S['rfiles'].items()})),
    ('G-TABLE-SEC-ROWS', 'the table at relay and its bank: the 62 SEC rows, all profiled, added and nothing gone or changed', lambda S: table_rows_ok(S),
     lambda S: put(S, 'tblj', dict(S['tblj'], changed=[['SIDE-explicit-formula', 'x']]))),
    ('G-TABLE-COMMITTED-ALONE', 'relay`s log: the five table files in one housekeeping commit of their own, after the lock', lambda S: table_alone(S),
     lambda S: put(S, 'rfiles', dict(S['rfiles'], deadbee=sorted('data/' + x for x in TABLE_FILES)))),
    ('G-TIERS-REREAD', 'the tier bank re-read: b557`s readings of the SEC terminals, each profile the same and the modules unchanged at the tag', lambda S: tiers_ok(S),
     lambda S: put(S, 'tierj', dict(S['tierj'], rows=[dict(x, same=False) if i == 0 else x for i, x in enumerate(S['tierj'].get('rows') or [])]))),
    ('G-H57C-SCORED', 'H57c recomputed now, against the scores and the desk', lambda S: h57_ok(S, 'H57c'), lambda S: _sc(S, 'H57c')),
    ('G-H57D-SCORED', 'H57d recomputed now, against the scores and the desk', lambda S: h57_ok(S, 'H57d'), lambda S: _sc(S, 'H57d')),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b622`s list and b602`s v0.20 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b622`s list and b603`s v0.21 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGES-NOW', 'both pages on disk and at HEAD against their re-emission banks, a changed page in one commit of its own and an unchanged one in none', lambda S: pages_now(S),
     lambda S: put(S, 'pj', dict(S['pj'], zeta=dict(S['pj']['zeta'], sha256='0')))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank after the kernel tag: both page arms and the frozen control', lambda S: arms_ok(S['arms']),
     lambda S: put(S, 'arms', S['arms'].replace('PAGE ARMS PASSING : 2 of 2', 'PAGE ARMS PASSING : 1 of 2'))),
    ('G-CURRENTS-UNEDITED', 'the current versions, the census, ERRATA, README and SPIRAL_MAP on disk and at HEAD against c9e9a9c',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{K.CENSUS: ((S['currents'][K.CENSUS][0] or b'') + b'x', S['currents'][K.CENSUS][1],
                                                                                              S['currents'][K.CENSUS][2])}))),
    ('G-NODISCLOSURE-PUBLIC', 'the no-disclosure arm on every public byte this act writes: the appended ledger bytes, its relay banks and tools, the housekeeping lists, REGISTRY`s note, the artefact',
     lambda S: bool(S['nd_pub']) and not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', dict(S['nd_pub'], method=1))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD, lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record: the strike items and the two answers', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and '**The author’s two answers before the seal**' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**The author’s two answers before the seal**', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b624, W-ORD-E0-INDUCTION and W-ORD-ACT-ROOT in one act' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b624, W-ORD-E0-INDUCTION and W-ORD-ACT-ROOT in one act', 'x'))),
    ('G-KERNELS-UNTOUCHED', 'the seven kernels this act reads beside the nine: main, tags and branches against the face, lv`s HEAD and status, the explicit-formula checkout on main and clean, its kept branches, the trial branch',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', dict(S['kern_now'], **{'SIDE-cosmo': ['0', {}, []]}))),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('36352a0', '36352a0', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b623_record.py'): S['tooltext'].get(os.path.join(T, 'b623_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                              if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md against its pre-act blob', lambda S: S['errata'][1] is not None and S['errata'][0] == S['errata'][1],
     lambda S: put(S, 'errata', ((S['errata'][0] or b'') + b'x', S['errata'][1]))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 5d0816dd, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 6000,
     lambda S: put(S, 'prior_bad', ['data/b622_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked: the ledgers, REGISTRY and a page only where its re-emission changed', lambda S: corpus_scope(S),
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + ['README.md']))),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] is not None and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] is not None and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-GS-UNTOUCHED', 'SIDE-global-section`s diff against 3528bcf and its HEAD', lambda S: S['gs_diff'] == [] and S['gs_head'].startswith(PRE['gs'])
     and S['corr_now'] == S['corr_pre'], lambda S: put(S, 'gs_diff', ['CORRESPONDENCE.md'])),
    ('G-TABLE-UNMOVED', 'the suite`s own regeneration against the committed housekeeping table: no row added or gone and no grade cell moved', lambda S: S['table_changed'] is not None
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
                                                                          and "startswith('b623')" in S['suite'] and "data/b623_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b623')", ''))),
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
    rec('b623 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
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
    rec('  ### (R233)(4)`s arm, printed: FINDINGS entries b594-b622 %d ; carrying the offering line %d ; without %d' % (
        len(S['offer_now']), sum(x['carries'] for x in S['offer_now']), sum(not x['carries'] for x in S['offer_now'])))
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
        out = os.path.join(D, 'b623_arms_prerun.txt')
    elif MID:
        out = os.path.join(D, sys.argv[sys.argv.index('--mid') + 1])
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b623_checks_postpush.txt' if pushed else 'b623_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b623_arms_prerun.txt', 'b623_lsr_prerun.json').replace('b623_checks', 'b623_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b623_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
