# -*- coding: utf-8 -*-
"""b627_checks.py -- THE SUITE OF b627, UNDER (R237): THE POSITIVITY MARGIN AT HEIGHT FROM THE PRIME SIDE; THE SEAM EQUIVALENCE RULED;
THE BOUNDED SHAPE ENTERED; THE CLOSING FORM AMENDED.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`, `--mid <name>` or `--prerun`; it writes data/b627_checks.txt before the push and
### data/b627_checks_postpush.txt after it; `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the face is
### sealed, no table regenerated, its counts written to data/b627_arms_prerun.txt.
### ### Every remote is read once per run (OPEN_TRAILS :12703, b616_claims.remote_refs); G-LSREMOTE-ONE-PER-REPO runs last.
### ### b626'S DEFECT (a), ITS SOURCE REPAIRED ((R237)'s Component 0): the answers arm counts the prompts FROM THE BANK -- its count
### line against the prompt headers it carries, every prompt with its options, every call with its result -- and fixes no figure.
### ### The generator is frozen with the E0 rule in the old-lists control: (R237)(3) edits tools/chain_page.py after the seal, so the
### control re-emits b622's lists with the generator's own blob at its pin as well (b597's principle, the control frozen at what it controls).
### ### The harness is b568's to b626's, carried from tools/b626_checks.py; the sources, predicates and arms are b627's.
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
import b627_worklist as K     # noqa: E402

NL = chr(10)
PP, GS, KER = K.PP, K.GS, K.KER
TE = 'D:/MY-DOwnloads/TECHNE-Core'
FACE = os.path.join(D, 'b627_registration_2026-10-05.txt')
PAGE, DIR_PAGE = K.PAGE, K.DIR_PAGE
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP, gs=K.PRE_GS)
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b', 'product-b600': '1dd5cd7',
        'doubling-keiper-b601': '5fc0c87', 'sign-window-b602': '914c413', 'family-b603': '1d5d4dd', 'platt-b626': 'e939c92'}
STEPZERO = K.STEPZERO
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA-E0-12C15C80'
FROZEN_ARM = 'G-GEN-OLD-LISTS-FROZEN-AT-84BAE29A-52822A5-GEN-84BAE29A'
FROZEN_PINS = ('84bae29a', '52822a5')
FROZEN_NODES = {'zeta': 'b622_nodes_zeta.txt', 'chi': 'b622_nodes_chi.txt'}
FROZEN_PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
ABSENT = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_9.md'
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/f5c41941-fa74-40e9-b806-a98e7280e315/scratchpad'
INST = ('b626_checks.py', 'b626_record.py', 'b626_closing.py', 'b604_record.py', 'b602_record.py', 'b566_record.py', 'b565_record.py',
        'b616_record.py', 'b616_claims.py', 'b611_claims.py', 'b558_record.py', 'e0_rule.py', 'test_e0_rule.py', 'g_chain_page.py',
        'banned_terms.py', 'terminal_table.py', 'table_gate.py', 'reg_seal.py', 'b378_lockgate.py', 'push_gated.sh', 'test_push_gated.sh',
        'act_root.py', 'test_act_root.py', 'corr_row.py')
GEN_SUBJECT = 'b627 (R237)(3)'
CLOSING_SUBJECT = 'b627 (R237)(4)'
CHIFF_SUBJECT = 'b627 (R237)(2)'
COUNT_CASE = r'^  \(\d+\) '


def rec(s=''):
    L.append(s)
    print(s)


def git(repo, *a):
    if 'ls-remote' in a:
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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b627')
            and 'data/b627_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def strip_prose(t):
    t = re.sub(r'"""[\s\S]*?"""', '', t)
    t = re.sub(r"'''[\s\S]*?'''", '', t)
    return NL.join(l.split('#', 1)[0] for l in t.split(NL))


def wl_globs(face):
    try:
        w = face[face.index('### (W) THE WRITE LIST.'):face.index('### (Z) THE NOTHINGS.')]
    except ValueError:
        return []
    return sorted(set(re.findall(r'`((?:relay|PLACE-papers|SIDE-global-section|SIDE-explicit-formula)/[^`\s]+)`', w)))


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
    for repo, name, pre in ((PP, 'PLACE-papers', PRE['pp']), (GS, 'SIDE-global-section', PRE['gs']), (KER, 'SIDE-explicit-formula', K.PRE_KER)):
        ch = set(x for x in gs(repo, 'diff', '--name-only', pre).split(NL) if x.strip())
        ch |= set(x for x in gs(repo, 'diff', '--name-only', pre, 'HEAD').split(NL) if x.strip())
        if repo == PP:
            ch |= set(untracked(PP, 'phase1.5', 'phase2', 'day1'))
        res += ['%s/%s' % (name, x) for x in ch]
    return sorted(res)


def lines_of(b):
    if b is None:
        return []
    l = cr0(b if isinstance(b, bytes) else b.encode('utf-8')).decode('utf-8', 'replace').split(NL)
    return l[:-1] if l and l[-1] == '' else l


def tri(repo, path, pre):
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
        out[k] = [gs(p, 'rev-parse', '--short=7', 'main'), tags, sorted(x for x in gs(p, 'branch', '--format=%(refname:short)').split(NL) if x.strip()),
                  gs(p, 'status', '--porcelain', '--untracked-files=no')]
    return out


def term_stmt(repo, pin, path, line):
    """### the statement a next-act terminal carries at its pin: its declaration line and the next, whitespace-joined."""
    t = lines_of(blob(repo, '%s:%s' % (pin, path)))
    return ' '.join(' '.join(t[line - 1:line + 1]).split()) if len(t) >= line else None


def sources():
    import b627_record as REC
    import b616_record as R6
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b627_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b627_') and f.endswith('.py'))
    S = dict(
        REC=REC, face=face, ferry=rd('b627_ferry.txt'), scan=rd('b627_ferry_scan.txt'), cens=rd('b627_census_stepzero.txt'),
        fcens=rd('b627_faces_census_stepzero.txt'), pins0=rd('b627_pins_stepzero.txt'), procs=rd('b627_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b626_closing.txt'), reads=rd('b627_reads.txt'), branches=rd('b627_branches.txt'), answers=rd('b627_author_answers.txt'),
        prerun=rd('b627_arms_prerun.txt'), rl=jl('b627_record_lines.json'), ctj=jl('b627_chiff_trail.json'), crj=jl('b627_chiff_row.json'),
        cej=jl('b627_closing_edit.json'), gd=rd('b627_gen_diff.txt'), gt=rd('b627_gen_test.txt'), gtj=jl('b627_gen_test.json'),
        shj=jl('b627_shapes.json'), tblj=jl('b627_table_final.json'),
        pj={k: jl('b627_page_%s.json' % k) for k in ('zeta', 'chi')}, arms=rd('b627_page_arms.txt'),
        inputs=rd('b627_margin_inputs.txt'), margin=rd('b627_margin.txt'), rerun=jl('b627_margin_rerun.json'),
        margin_raw=raw(os.path.join(D, 'b627_margin.txt')), script=read(os.path.join(ROOT, K.BENCH_SCRIPT)),
        arj=jl('b627_act_root.json'), arj0=jl('b626_act_root.json'), art=rd('b627_act_root.txt'), rootsf=rd('act_roots.txt'),
        rpush=rd('b627_root_push_out.txt'), ppush=rd('b627_pp_root_push_out.txt'), gpush=rd('b627_gs_push_out.txt'),
        absent=tri(PP, ABSENT, PRE['pp']),
        genfiles={p: tri(ROOT, p, PRE['relay']) for p in K.GEN_FILES},
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f)))) for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')), corr=read(os.path.join(GS, 'CORRESPONDENCE.md')),
        errata=(cr0(raw(os.path.join(PP, 'ERRATA.md'))), cr0(blob(PP, PRE['pp'] + ':ERRATA.md'))),
        currents={p: tri(PP, p, PRE['pp']) for p in REC.CURRENTS},
        pages={p: tri(PP, p, PRE['pp']) for p in (PAGE, DIR_PAGE)},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        corr_pre=cr0(blob(GS, PRE['gs'] + ':CORRESPONDENCE.md')), corr_now=cr0(raw(os.path.join(GS, 'CORRESPONDENCE.md'))),
        kern_face=(jl('b627_kernels_face.json').get('kernels') or {}),
        lv_head=gs('D:/SIDE-lv-conservation', 'rev-parse', 'HEAD'), trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        kcur=gs(KER, 'branch', '--show-current'), ker_main=gs(KER, 'rev-parse', '--short=7', 'main'),
        ker_diff=sorted(set(x for x in (gs(KER, 'diff', '--name-only', K.PRE_KER, 'main') + NL + gs(KER, 'diff', '--name-only')).split(NL) if x.strip())),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_log=[(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in gs(GS, 'log', '--reverse', '--format=%h %s', PRE['gs'] + '..HEAD').split(NL) if l.strip()],
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b626*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools + [os.path.join(ROOT, K.BENCH_SCRIPT)] if os.path.exists(f)},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b627_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b627_mustnotexist.txt')), table_changed=None,
        fj=jl('b627_findings.json'), tj=jl('b627_trail.json'), sc=jl('b627_scores.json'), desk=rd('b627_desk_notes.txt'),
        lsr=None,
        rlog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(ROOT, 'log', '--reverse', '--format=%h %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
    )
    S['next_stmts'] = [(n, term_stmt(repo, pin, path, line)) for _r, ts in K.NEXT_ROUTES for n, repo, pin, path, line in ts]
    S['gs_files'] = {h: files_of(GS, h) for h, _s in S['gs_log']}
    S['kern_now'] = kern_now(S['kern_face']) if S['kern_face'] else {}
    S['written'] = written_files(lock_epoch or 0)
    S['globs'] = wl_globs(face)
    S['nd_sets'] = R6.nd_sets()
    S['rfiles'] = {h: files_of(ROOT, h) for h, _s, _t in S['rlog']}
    ch = set(x for x in gs(PP, 'diff', '--name-only', PRE['pp']).split(NL) if x.strip())
    ch |= set(x for x in gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD').split(NL) if x.strip())
    ch |= set(untracked(PP, 'phase1.5', 'phase2', 'day1', 'outputs', 'heritage'))
    S['pp_changed'] = sorted(ch)
    S['pp_log'] = [(l.split(' ', 1)[0], l.split(' ', 1)[1] if ' ' in l else '') for l in gs(PP, 'log', '--reverse', '--format=%h %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()]
    S['pp_files'] = {h: files_of(PP, h) for h, _s in S['pp_log']}
    pub = []
    for nm, pre, now in (('FINDINGS', S['fi_pre'], S['fi_now']), ('OPEN_TRAILS', S['ot_pre'], S['ot_now']), ('CORR', S['corr_pre'], S['corr_now'])):
        pub.append(now[len(pre):].decode('utf-8', 'replace') if now and pre and now.startswith(pre) else '')
    for f in sorted(os.listdir(D)):
        if f.startswith(('b627_', 'audit_b627_')) and os.path.isfile(os.path.join(D, f)):
            pub.append(read(os.path.join(D, f)))
    pub += [read(f) for f in tools] + [rd('act_roots.txt'), S['script']]
    for p, (now, _b, _h) in S['genfiles'].items():
        pub.append((now or b'').decode('utf-8', 'replace'))
    S['nd_pub'] = R6.nd_hits(NL.join(pub), S['nd_sets'])[0]
    pre_ids = {}
    for l in git(ROOT, 'ls-tree', '-r', PRE['relay'], '--', 'data/')[1].split(NL):
        if '\t' in l:
            meta, p = l.split('\t', 1)
            pre_ids[p] = meta.split()[2]
    bad = []
    for p, i in pre_ids.items():
        if os.path.basename(p) in TABLE_FILES or p == 'data/act_roots.txt':
            continue
        fp = os.path.join(ROOT, p)
        rb = open(fp, 'rb').read() if os.path.exists(fp) else None
        if rb is None or i not in (blob_id(rb), blob_id(cr0(rb))):
            bad.append(p)
    S['prior_bad'], S['prior_n'] = bad, len(pre_ids)
    S['roots_pre'] = cr0(blob(ROOT, PRE['relay'] + ':data/act_roots.txt'))
    S['roots_now'] = cr0(raw(os.path.join(D, 'act_roots.txt')))
    S['table_grades'] = REC._table_grades()
    S.update(extra_sources(S))
    return S


def extra_sources(S):
    import chain_page as CP
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import b626_record as R26
    X = {}
    X['gcp_zeta'] = GCP.arm(os.path.join(D, K.NODES['zeta']), os.path.join(SP, '_b627_gcp'), os.path.join(D, K.PROBE['zeta']))
    X['gcp_chi'] = GCP.arm(os.path.join(D, K.NODES['chi']), os.path.join(SP, '_b627_gcp'), os.path.join(D, K.PROBE['chi']))
    rule = CP.E0
    CP.E0 = R26.e0_module(TC.RELAY_PIN)     # ### the carried control's E0 rule at its own pin
    try:
        X['ctl'] = TC.control()
    finally:
        CP.E0 = rule
    X['ctl_arm'] = TC.ARM
    old = []
    pins, tc_c, tc_git = (TC.RELAY_PIN, TC.PRE_PP), TC.C, TC._GIT
    try:
        gen = S['REC'].cp_module(FROZEN_PINS[0])          # ### the generator's own blob at its pin, beside the E0 rule's
        gen.E0 = R26.e0_module(FROZEN_PINS[0])
        TC.RELAY_PIN, TC.PRE_PP = FROZEN_PINS
        TC.C, TC._GIT = gen, gen.git
        for k in ('zeta', 'chi'):
            lb, pb = blob(ROOT, '%s:data/%s' % (FROZEN_PINS[0], FROZEN_NODES[k])), blob(ROOT, '%s:data/%s' % (FROZEN_PINS[0], FROZEN_PROBE[k]))
            d = os.path.join(SP, '_b627_frozen')
            os.makedirs(d, exist_ok=True)
            lp, pp = os.path.join(d, FROZEN_NODES[k]), os.path.join(d, FROZEN_PROBE[k])
            open(lp, 'wb').write(lb or b'')
            open(pp, 'wb').write(pb or b'')
            rc, got = TC.regen(lp, pp)
            old.append(dict(list=FROZEN_NODES[k], rc=rc, equal=got is not None and got == cr0(blob(PP, '%s:%s' % (FROZEN_PINS[1], K.PNAME[k])))))
    except Exception as e:
        old.append(dict(list='raised %s' % type(e).__name__, rc=-1, equal=False))
    finally:
        TC.RELAY_PIN, TC.PRE_PP = pins
        TC.C, TC._GIT = tc_c, tc_git
    X['old_frozen'] = old
    try:
        o, n = S['REC']._node_shapes(S['REC'].cp_module(PRE['relay'])), S['REC']._node_shapes(S['REC'].cp_module(None))
        X['moved_now'] = sorted(nm for (k, nm) in o if o[(k, nm)] != n.get((k, nm)))
    except Exception as e:
        X['moved_now'] = ['raised %s' % type(e).__name__]
    try:
        import act_root as AR
        X['ar_verify'] = AR.verify(remote=KC0.remote_refs)
    except Exception as e:
        X['ar_verify'] = [('raised', type(e).__name__, [])]
    X['gen_stat'] = gs(ROOT, 'diff', '--stat', PRE['relay'], '--', *K.GEN_FILES).split(NL)[-1].strip()
    X['sorry_tokens'] = S['REC'].sorry_tokens('main')
    X['page_bad'] = S['REC']._page_lines_ok('zeta') + S['REC']._page_lines_ok('chi') if S['pj']['zeta'] else ['no page bank']
    return X


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


def poss(t):
    import b566_record as R6
    return R6.Q.poss(t)


def procs_ok(S):
    p = S['procs']
    rows = [l for l in p.split(NL) if re.match(r'^\s*\d+\s+\d+\s+(lean|lake|grep|du|find|rg|head|cut|python|tail)\.exe', l)]
    return 'powershell.exe' in p and '### ORPHANS:' in p and '\\v1.0\\' in p and all('### STOPPED BY PID' in l for l in rows) \
        and 'tail' in p.split('### names matched:')[1].split(NL)[0]


def absent_ok(S):
    a, b, c = S['absent']
    return a is None and b is None and c is None and cr0(None) is None and cr0(b'') == b'' and lines_of(None) == []


def rline(S, i):
    x = (S['rl'].get('lines') or [])
    return x[i] if len(x) > i else {}


def landed(S, i, need):
    x = rline(S, i)
    o = (fline if x.get('file') == 'FINDINGS.md' else oline)(S, x.get('line'))
    return bool(x) and o.startswith(poss(x.get('head', '\x00'))) and all(n in o for n in need)


def alone(S, files, prefix):
    c = [h for h, f in S['rfiles'].items() if f == sorted(files)]
    msg = {h: (s, t) for h, s, t in S['rlog']}
    return len(c) == 1 and msg[c[0]][0].startswith(prefix) and S['lock_epoch'] is not None and msg[c[0]][1] > S['lock_epoch'] \
        and not [h for h, f in S['rfiles'].items() if set(f) & set(files) and h != c[0]]


def count(text):
    cases = [l for l in (text or '').split(NL) if re.match(COUNT_CASE, l)]
    return len(cases), sum(1 for c in cases if c.rstrip().endswith('PASS'))


def answers_ok(S):
    """### b626's defect (a), repaired: the prompts counted from the bank -- the count line against the prompt headers it carries, each
    ### prompt with at least two options, each call with a result -- no figure fixed in this source."""
    a = S['answers']
    m = re.search(r'^### b627 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
    blocks = [b for b in re.split(r'^### CALL ', a, flags=re.M)[1:]]
    heads = re.findall(r'^### PROMPT \d+ \(', a, re.M)
    per = [len(re.findall(r'^  OPTION \d+', p, re.M)) for p in re.split(r'^### PROMPT \d+ \(', a, flags=re.M)[1:]]
    return bool(m) and int(m.group(1)) == len(heads) > 0 and all(x >= 2 for x in per) and len(per) == len(heads) \
        and len(blocks) == a.count('RESULT (transcript line') and '### NO RESULT' not in a and blocks


def corr_rows_ok(S, j, pairs):
    rows = j.get('rows') or []
    lines = S['corr'].split(NL)
    out = []
    for x, (sup, name) in zip(rows, pairs):
        ln = [l for l in lines if re.match(r'^\|\s*%d\s*\|' % x['row'], l)]
        out.append(len(ln) == 1 and ('SUPERSEDES row %d: INTERFACES -- `%s`' % (sup, name)) in ln[0] and x['supersedes'] == sup and x['name'] == name)
    return len(rows) == len(pairs) and all(out)


def gs_alone(S, prefix):
    c = [h for h, s in S['gs_log'] if s.startswith(prefix)]
    return len(c) == 1 and S['gs_files'][c[0]] == ['CORRESPONDENCE.md']


def pp_alone(S, prefix, files):
    c = [h for h, s in S['pp_log'] if s.startswith(prefix)]
    return len(c) == 1 and S['pp_files'][c[0]] == sorted(files)


def chiff_trail_ok(S):
    j = S['ctj']
    n = j.get('line')
    return bool(n) and oline(S, n) == S['REC'].CT_HEAD % K.CHIFF_TRAIL and oline(S, n + 1).startswith(
        'SUPERSEDES OPEN_TRAILS :%d for `ch_iff_h2_sign_of_seam`: INTERFACES -- ' % K.CHIFF_TRAIL) and pp_alone(S, CHIFF_SUBJECT, ['OPEN_TRAILS.md'])


def closing_alone(S):
    c = [h for h, f in S['rfiles'].items() if 'tools/b627_closing.py' in f]
    msg = {h: (s, t) for h, s, t in S['rlog']}
    edit = [h for h in c if S['rfiles'][h] == ['tools/b627_closing.py']]
    return len(c) == 2 and len(edit) == 1 and msg[edit[0]][0].startswith(CLOSING_SUBJECT) and S['lock_epoch'] is not None \
        and all(msg[h][1] > S['lock_epoch'] for h in c) and S['cej'].get('sealed') in c and S['cej'].get('sealed') != edit[0]


def closing_terms_ok(S):
    t = ' '.join(S['cej'].get('terminals') or [])
    return bool(S['next_stmts']) and all(st and n in t and st in t for n, st in S['next_stmts']) and 'W-ORD-NYMAN-BEURLING-FACE' in t \
        and 'no kernel terminal' in t


def gen_diff_ok(S):
    files = S['genfiles']
    banked = [l[4:].strip() for l in S['gd'].split(NL) if l.startswith('### ') and 'changed' in l]
    return all(a is not None and a == c and a != b for a, b, c in files.values()) and bool(S['gen_stat']) and banked == [S['gen_stat'].strip()] \
        and '+def _measure_bounded(nm, ty, body):' in S['gd'] and "+SHAPES = ('FINITE', 'BOUNDED', 'UNIVERSAL'" in S['gd']


def gen_test_ok(S):
    n, p = count(S['gt'])
    return n == p and n >= 11 and S['gtj'].get('cases') == n and S['gtj'].get('passing') == p and S['gtj'].get('rc') == 0


def gen_control_ok(S):
    c = S['gtj'].get('control') or {}
    m = re.search(S['REC'].CONTROL_RE, S['gt'], re.M)
    return bool(m) and m.group(1) == PRE['relay'] and m.group(2) == '1' and c.get('failing') == K.GEN_CONTROL_FAILING \
        and m.group(5) == str(K.GEN_CONTROL_FAILING) and int(m.group(3)) == S['gtj'].get('cases')


def shapes_ok(S):
    j = S['shj']
    return S['moved_now'] == sorted(K.BOUNDED_WANT) and sorted(x[1] for x in j.get('moved') or []) == sorted(K.BOUNDED_WANT)


def page_ok(S, k, need_rung):
    j = S['pj'][k]
    a, b, c = S['pages'][K.PNAME[k]]
    commits = [h for h, f in S['pp_files'].items() if K.PNAME[k] in f]
    ok = j.get('rc') == 0 and a is not None and a == c and hashlib.sha256(c).hexdigest() == j.get('sha256') \
        and all(S['pp_files'][h] == [K.PNAME[k]] for h in commits) and (len(commits) >= 1) == bool(j.get('changed'))
    if need_rung:
        ok = ok and all((j.get('rung') or {}).get(n) == 'BOUNDED' for n in K.BOUNDED_WANT) and ' — shape: BOUNDED — ' in (c or b'').decode('utf-8')
    return ok


def table_final_ok(S):
    t, tg = S['tblj'], S['table_grades']
    return bool(t) and t.get('rc') == 0 and tg.get(K.CHIFF) == 'INTERFACES' and not t.get('gone')


def margin_rows(S):
    return [l for l in S['margin'].split(NL) if l.startswith('ROW ')]


def inputs_ok(S):
    t = S['inputs']
    m = re.search(r'ordinates in the read (\d+) ; taken (\d+)', t)
    ords = re.findall(r'^ORD (\d+) (\S+)$', t, re.M)
    return ('### THE ZERO TABLE, READ ONCE: %s' % K.ZERO_URL) in t and bool(m) and int(m.group(2)) == K.N_ORD == len(ords) \
        and int(m.group(1)) >= K.N_ORD and [int(i) for i, _x in ords] == list(range(1, K.N_ORD + 1)) and re.search(r'sha256 [0-9a-f]{64}', t)


def inputs_first(S):
    c_in = [h for h, f in S['rfiles'].items() if f == ['data/b627_margin_inputs.txt']]
    c_out = [h for h, f in S['rfiles'].items() if 'data/b627_margin.txt' in f]
    order = [h for h, _s, _t in S['rlog']]
    return len(c_in) == 1 and len(c_out) >= 1 and order.index(c_in[0]) < min(order.index(h) for h in c_out) \
        and not [h for h, f in S['rfiles'].items() if 'data/b627_margin_inputs.txt' in f and h != c_in[0]]


def kernel_cited_ok(S):
    t = S['inputs']
    cited = re.findall(r'; in the script (True|False)$', t, re.M)
    want = sum(len(ns) for _f, ns in K.KERNEL_LINES)
    return len(cited) == want and all(x == 'True' for x in cited) and t.count('equals the blob at v0.22') == len(K.KERNEL_LINES) \
        and all(('# %s %s :%d:' % (K.KPIN, f, n)) in S['script'] for f, ns in K.KERNEL_LINES for n in ns)


def rows_ok(S):
    rows = margin_rows(S)
    ords = dict(re.findall(r'^ORD (\d+) (\S+)$', S['inputs'], re.M))
    js = [int(l.split()[1]) for l in rows]
    pos = sum(' positive=YES' in l for l in rows)
    m = re.search(r'VALUES (\d+) ; POSITIVE \(THE WHOLE BALL ABOVE ZERO\) (\d+) ; STRADDLING (\d+) ; NEGATIVE (\d+)', S['margin'])
    vals = {int(l.split()[1]): float(re.search(r' Q=(\S+)', l).group(1)) for l in rows}
    mm = re.search(r'THE MINIMUM OVER N : (\S+) AT ORDINATE (\d+)', S['margin'])
    jm = min(vals, key=vals.get) if vals else None
    return js == list(range(1, K.N_ORD + 1)) and all(re.search(r' t=(\S+) ', l).group(1) == ords[l.split()[1]][:32] for l in rows) \
        and bool(m) and [int(m.group(i)) for i in (1, 2)] == [len(rows), pos] and bool(mm) and int(mm.group(2)) == jm


def reproduces_ok(S):
    r = S['rerun']
    return r.get('equal') is True and S['margin_raw'] is not None and (r.get('sha256') or [''])[0] == hashlib.sha256(S['margin_raw']).hexdigest() \
        and len(set(r.get('sha256') or [])) == 1


def _h(S, k, want):
    return (S['sc'].get(k) or [''])[0] == want and ('(%s)' % k.upper()) in S['desk'] and ('### **%s.**' % want) in S['desk']


def h61_ok(S, k):
    rows = margin_rows(S)
    if k == 'H61a':
        want = 'HOLDS' if len(rows) == K.N_ORD and all(' positive=YES' in l for l in rows) else 'REFUTED'
    elif k == 'H61b':
        want = 'NOT SCORABLE'
    elif k == 'H61c':
        want = 'HOLDS' if kernels_untouched(S) and S['ker_diff'] == [] and S['page_bad'] == [] else 'REFUTED'
    else:
        want = 'HOLDS' if reproduces_ok(S) else 'REFUTED'
    return _h(S, k, want)


def arms_ok(t):
    return 'PAGE ARMS PASSING : 2 of 2' in t and ('PASSING : 2 of 2.**') in t.split('PAGE ARMS PASSING : 2 of 2.**')[-1]


def root_banked_ok(S):
    import act_root as AR
    j, j0 = S['arj'], S['arj0']
    rows = [l.split(None, 3) for l in S['rootsf'].split(NL) if l.strip()]
    return bool(j) and len(rows) == 4 and rows[3][:3] == ['b627', j.get('root'), j0.get('root')] and len(rows[3]) == 3 \
        and AR.root_of(j.get('items') or [], j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and len(j['reads']['heads']) == 38 and S['roots_pre'] is not None and (S['roots_now'] or b'').startswith(S['roots_pre'])


def midpush_ok(S):
    heads = (S['arj'].get('reads') or {}).get('heads') or {}
    ms = [re.search(r'push_gated: main read back at the remote: (\w+)', S[k]) for k in ('rpush', 'ppush', 'gpush')]
    return all(ms) and heads.get('relay') == ms[0].group(1) and heads.get('PLACE-papers') == ms[1].group(1) \
        and heads.get('SIDE-global-section') == ms[2].group(1)


def verify_ok(S):
    v = S['ar_verify'] or []
    return [x[0] for x in v] == ['b624', 'b625', 'b626', 'b627'] and all(x[1] == 'AGREE' for x in v)


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(S['REC'].CURRENTS)


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 24]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') and fline(S, e).startswith(
        '## The positivity margin at height: the v0.20 window from the prime side at the lowest ') \
        and all(x in tail for x in ('**The bench**', '**What the bench is.**', 'not a test of positivity beyond the table', '**The seam equivalence**',
                                    '**The BOUNDED shape**', '**The closing form**', '**The record lines and the root.**', '**The scores.**',
                                    '**Read in mutual light**', 'strengthens', 'W-BENCH-1', '**Next.**', 'b628'))


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
    rest = [k for k in f if k not in S['REC'].WRITTEN_KERNS]
    return bool(f) and len(f) == 11 and all(k in n and n[k] == f[k] for k in rest) and all(n[k][0].startswith(v) for k, v in S['REC'].KERN_PIN.items()) \
        and S['trial'] == 'f22ff35' and S['lv_head'].startswith('2f71068a')


def corpus_scope(S):
    pages = [K.PNAME[k] for k in ('zeta', 'chi') if S['pj'][k].get('changed') or any(K.PNAME[k] in f for f in S['pp_files'].values())]
    return S['pp_changed'] == sorted(set(['FINDINGS.md', 'OPEN_TRAILS.md'] + pages))


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


READ_NEEDLES = ('OPEN_TRAILS.md @ a43e1ba', 'FINDINGS.md @ a43e1ba', 'PlateauRamp.lean @ ', 'B321Identity.lean @ ', 'ExplicitFormula.lean @ ',
                'PowerLimit.lean @ e939c92', 'PlattRung.lean @ e939c92', 'Simplicity.lean @ e939c92', 'FinalMult.lean @ 3635e748',
                'CORRESPONDENCE.md @ dbacb9f', 'tools/chain_page.py @ 746ab804', 'tools/test_chain_page_b596.py @ 746ab804',
                'tools/b626_closing.py @ 746ab804', 'VERIFICATION_LOOM-archive-1', 'data/b626_closing_push_out.txt @ 152039e5',
                ':10884 ', ':11864 ', ':12228 ', ':12354 ', ':12356 ', ':12799 ', ':12891 ', ':12893 ', ':12897 ', ':12970 ', ':13026 ',
                'names none')

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R237) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b626`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b626' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b627 -- x'])),
    ('G-R237-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R237) END' in S['ferry'] and S['ot'].count('**(R237) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R237) ratified', '(R237) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in READ_NEEDLES) and 'NO SUCH LINE' not in S['reads'],
     lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ANSWERS-BANKED', 'the answers bank as it prints: its count line against its prompt headers, each prompt`s options, each call`s result',
     lambda S: answers_ok(S), lambda S: put(S, 'answers', S['answers'].replace('RESULT (transcript line', 'RESULT (line', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay 152039e5`s files', lambda S: S['pushout'][0] == ['data/b626_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/b626_closing_push_out.txt', 'x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b626') == 7, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b626'}))),
    ('G-KEPT-BRANCHES', 'the explicit-formula kernel`s kept branch heads, platt-b626 among them', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'platt-b626': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80, every PLACE-papers read at ba5f0ea and the E0 rule`s blob at 12c15c80',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] + '-E0-12C15C80' == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(S['ctl'][0], ok=False)] + S['ctl'][1:])),
    (FROZEN_ARM, 'b622`s lists with every relay read at 84bae29a, the E0 rule`s and the generator`s blobs at 84bae29a, against the pages at 52822a5',
     lambda S: len(S['old_frozen']) == 2 and all(x['rc'] == 0 and x['equal'] for x in S['old_frozen']),
     lambda S: put(S, 'old_frozen', [S['old_frozen'][0], dict(S['old_frozen'][1], equal=False)] if len(S['old_frozen']) == 2 else [])),
    ('G-INSTRUMENTS-UNEDITED', 'b626`s suite, record tool and closing, the shared record tools, the claims modules, the E0 rule and its test, the page arm, the scanner, the table generator and its gate, the seal, the lock gate, the push gate, act_root.py and the row writer against 746ab804',
     lambda S: all(a is not None and a == b for a, b in S['inst'].values()) and len(S['inst']) == len(INST),
     lambda S: put(S, 'inst', dict(S['inst'], **{'b626_record.py': (S['inst']['b626_record.py'][0], (S['inst']['b626_record.py'][1] or b'') + b'x')}))),
    ('G-ABSENT-IS-NONE', 'the source builder on a file no act wrote and on empty bytes', lambda S: absent_ok(S), lambda S: put(S, 'absent', (b'', b'', b''))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b626`s weight', lambda S: landed(S, 0, ('(:7563)', 'Relay 746ab804', 'b624-b626 verifying', 'defects (a)-(c) the seat’s')),
     lambda S: put(S, 'find', S['find'].replace('Relay 746ab804', 'Relay x'))),
    ('G-CLOSING-FORM-LINE', 'OPEN_TRAILS at the banked line: the closing form', lambda S: landed(S, 1, ('prints, beneath each name', 'statement read at its pin', 'tools/b627_closing.py')),
     lambda S: put(S, 'ot', S['ot'].replace('prints, beneath each name', 'prints each name'))),
    ('G-SIEVE-ITEM-LINE', 'OPEN_TRAILS at the banked line: the sieve`s item, to :12865', lambda S: landed(S, 2, ('(:12865)', 'BOUNDED', 'Finset and finite-range forms', 'Not started')),
     lambda S: put(S, 'rl', dict(S['rl'], lines=(S['rl'].get('lines') or [])[:2]))),
    ('G-CHIFF-TRAIL-LANDED', 'OPEN_TRAILS at the banked line: the directive superseding :10884 for the seam equivalence, committed alone in PLACE-papers',
     lambda S: chiff_trail_ok(S), lambda S: put(S, 'ot', S['ot'].replace('for `ch_iff_h2_sign_of_seam`: INTERFACES', 'for `ch_iff_h2_sign_of_seam`: DERIVES'))),
    ('G-CHIFF-ROW-LANDED', 'CORRESPONDENCE: the seam equivalence`s row superseding row 383, committed alone in SIDE-global-section',
     lambda S: corr_rows_ok(S, S['crj'], K.CHIFF_CORR) and gs_alone(S, CHIFF_SUBJECT),
     lambda S: put(S, 'corr', S['corr'].replace('SUPERSEDES row 383: INTERFACES -- `%s`' % K.CHIFF, 'SUPERSEDES row 383: DERIVES -- `%s`' % K.CHIFF))),
    ('G-GS-APPEND-ONLY', 'SIDE-global-section: CORRESPONDENCE alone changed, its pre-act blob a true prefix', lambda S: S['gs_diff'] == ['CORRESPONDENCE.md']
     and S['corr_pre'] is not None and S['corr_now'] is not None and S['corr_now'].startswith(S['corr_pre'].rstrip(b'\n')), lambda S: put(S, 'corr_now', b'x' + (S['corr_now'] or b''))),
    ('G-CLOSING-EDIT-ALONE', 'relay`s log: the closing tool in the sealed tools` commit and its edit in one commit of its own, both after the lock',
     lambda S: closing_alone(S), lambda S: put(S, 'rfiles', dict(S['rfiles'], deadbee=['tools/b627_closing.py']))),
    ('G-CLOSING-TERMINALS', 'the closing edit`s bank: each next-act terminal`s statement as git reads it at its pin, the work-order with none named',
     lambda S: closing_terms_ok(S), lambda S: put(S, 'cej', dict(S['cej'], terminals=(S['cej'].get('terminals') or [])[:1]))),
    ('G-GEN-COMMITTED-ALONE', 'relay`s log: the generator and its test in one commit of their own, after the lock', lambda S: alone(S, list(K.GEN_FILES), GEN_SUBJECT),
     lambda S: put(S, 'rfiles', dict(S['rfiles'], deadbee=sorted(K.GEN_FILES)))),
    ('G-GEN-DIFF-BANKED', 'the generator and its test on disk and at HEAD against 746ab804; the diff bank`s stat line; the clause in it', lambda S: gen_diff_ok(S),
     lambda S: put(S, 'gd', S['gd'].replace('+def _measure_bounded(nm, ty, body):', '+def _measured(nm, ty, body):'))),
    ('G-GEN-TEST-COUNTED', 'the test bank`s text counted here by its case pattern, every case passing', lambda S: gen_test_ok(S),
     lambda S: put(S, 'gt', S['gt'] + '\n  (99) planted : FAIL')),
    ('G-GEN-CONTROL-REFUTED', 'the test with the reader as it stood, read by the record tool`s own pattern: exactly (10) and (11) fail', lambda S: gen_control_ok(S),
     lambda S: put(S, 'gtj', dict(S['gtj'], control=dict(S['gtj'].get('control') or {}, failing=['(10)'])))),
    ('G-SHAPES-NOW', 'every page node`s shape read now by the reader`s blob at 746ab804 and as edited: the three the clause names, against the bank', lambda S: shapes_ok(S),
     lambda S: put(S, 'moved_now', (S['moved_now'] or []) + ['x'])),
    ('G-PAGE-ZETA-BOUNDED', 'the ζ page on disk and at HEAD against its bank, committed alone, the rung`s three read BOUNDED', lambda S: page_ok(S, 'zeta', True),
     lambda S: put(S, 'pj', dict(S['pj'], zeta=dict(S['pj']['zeta'], rung={})))),
    ('G-PAGE-CHI-EMITTED', 'the χ page on disk and at HEAD against its bank, committed alone where it changed', lambda S: page_ok(S, 'chi', False),
     lambda S: put(S, 'pj', dict(S['pj'], chi=dict(S['pj']['chi'], sha256='0')))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from its list and probe against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b622`s list and b603`s v0.21 probe against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank: both page arms and the frozen control', lambda S: arms_ok(S['arms']),
     lambda S: put(S, 'arms', S['arms'].replace('PAGE ARMS PASSING : 2 of 2', 'PAGE ARMS PASSING : 1 of 2'))),
    ('G-TABLE-FINAL', 'the table itself: the seam equivalence INTERFACES, no row gone', lambda S: table_final_ok(S),
     lambda S: put(S, 'table_grades', dict(S['table_grades'], **{K.CHIFF: 'DERIVES'}))),
    ('G-ZERO-TABLE-READ', 'the inputs bank: the table`s URL, the read`s digest, the count taken and every ordinate', lambda S: bool(inputs_ok(S)),
     lambda S: put(S, 'inputs', S['inputs'].replace('ORD 100 ', 'ORD 101 '))),
    ('G-INPUTS-BEFORE-BENCH', 'relay`s log: the inputs bank in one commit of its own before any commit carrying the margin bank', lambda S: inputs_first(S),
     lambda S: put(S, 'rfiles', dict(S['rfiles'], deadbee=['data/b627_margin_inputs.txt']))),
    ('G-BENCH-KERNEL-CITED', 'the inputs bank`s kernel lines against the script`s text, each file`s blob at v0.20 equal to v0.22', lambda S: kernel_cited_ok(S),
     lambda S: put(S, 'script', S['script'].replace('# v0.20 Zeta23/Defs.lean :60:', '# v0.20 Zeta23/Defs.lean :61:'))),
    ('G-BENCH-ROWS-RECOUNTED', 'the margin bank`s rows recounted here: every ordinate once at its table value, the totals and the minimum`s ordinate', lambda S: rows_ok(S),
     lambda S: put(S, 'margin', S['margin'].replace('ROW 7 ', 'ROW 8 ', 1))),
    ('G-BENCH-REPRODUCES', 'the second run`s comparison against the margin bank as it stands, by sha256', lambda S: reproduces_ok(S),
     lambda S: put(S, 'rerun', dict(S['rerun'], equal=False))),
    ('G-H61A-SCORED', 'H61a recomputed from the margin bank`s rows, against the scores and the desk', lambda S: h61_ok(S, 'H61a'), lambda S: _sc(S, 'H61a')),
    ('G-H61B-SCORED', 'H61b, NOT SCORABLE by the author`s answer, against the scores and the desk', lambda S: h61_ok(S, 'H61b'), lambda S: _sc(S, 'H61b')),
    ('G-H61C-SCORED', 'H61c recomputed from the kernels and the page banks` changed lines, against the scores and the desk', lambda S: h61_ok(S, 'H61c'), lambda S: _sc(S, 'H61c')),
    ('G-H61D-SCORED', 'H61d recomputed from the second run`s comparison, against the scores and the desk', lambda S: h61_ok(S, 'H61d'), lambda S: _sc(S, 'H61d')),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s b627 line, the root bank and its items: previous b626`s root, 38 repositories, the file a true prefix', lambda S: root_banked_ok(S),
     lambda S: put(S, 'rootsf', S['rootsf'].replace('b627 ', 'b62x ', 1))),
    ('G-ACTROOT-MIDPUSH', 'the root`s relay, PLACE-papers and SIDE-global-section heads against the read-backs of the pushes before it', lambda S: midpush_ok(S),
     lambda S: put(S, 'rpush', S['rpush'].replace('main read back at the remote: ', 'main read back at the remote: 0', 1))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed by this suite, one remote read per repository: b624 to b627 AGREE', lambda S: verify_ok(S),
     lambda S: put(S, 'ar_verify', [('b624', 'AGREE', []), ('b625', 'AGREE', []), ('b626', 'AGREE', []), ('b627', 'DISAGREE', ['x'])])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD, lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'this act`s trail record: the root and its previous', lambda S: bool(S['arj'])
     and ('**Act root:** b627 `%s` (previous `%s`' % (S['arj'].get('root'), S['arj'].get('previous'))) in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Act root:** b627', '**Act root:** b62x'))),
    ('G-TRAIL-CARRIES-TERMINALS', 'this act`s trail record: each next-act terminal`s statement as git reads it at its pin', lambda S: bool(S['next_stmts'])
     and '**The next act’s terminals, each statement at its pin**' in trail(S) and all(st and st in trail(S) for _n, st in S['next_stmts']),
     lambda S: put(S, 'ot', S['ot'].replace('**The next act’s terminals, each statement at its pin**', 'x'))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record: the strike items and the answers', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and '**The author’s three answers before the seal**' in trail(S), lambda S: put(S, 'ot', S['ot'].replace('**The author’s three answers before the seal**', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b628 -- the cross-kernel discharge route (b) of W-ORD-VENDOR-FINALMULT' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b628 -- the cross-kernel discharge route (b)', 'x'))),
    ('G-CURRENTS-UNEDITED', 'the current versions, the census, REGISTRY, ERRATA, README, SPIRAL_MAP and the sieve on disk and at HEAD against a43e1ba',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'REGISTRY.md': ((S['currents']['REGISTRY.md'][0] or b'') + b'x',
                                                                                                    S['currents']['REGISTRY.md'][1], S['currents']['REGISTRY.md'][2])}))),
    ('G-NODISCLOSURE-PUBLIC', 'the no-disclosure arm on every public byte this act writes: the ledger and CORRESPONDENCE appends, its banks and tools, the bench script, the generator and its test, the roots file',
     lambda S: bool(S['nd_pub']) and not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', dict(S['nd_pub'], method=1))),
    ('G-KERNELS-UNTOUCHED', 'every kernel this act does not write: main, tags by peel, branches and status against the face; lv and its trial branch',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', dict(S['kern_now'], **{'SIDE-cosmo': ['0', {}, [], '']}))),
    ('G-EXPLICIT-FORMULA-UNMOVED', 'the explicit-formula kernel: main at e939c92, no file changed against v0.22 in the tree or the index, the checkout on main',
     lambda S: S['ker_main'] == K.PRE_KER and S['ker_diff'] == [] and S['kcur'] == 'main', lambda S: put(S, 'ker_diff', ['x.lean'])),
    ('G-SORRY-TOKENS', 'the explicit-formula kernel`s main, comments stripped: no sorry token', lambda S: S['sorry_tokens'] == 0,
     lambda S: put(S, 'sorry_tokens', 1)),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('36352a0', '36352a0', ''))),
    ('G-DELETE-FREE', 'this act`s tools and the bench script, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b627_record.py'): S['tooltext'].get(os.path.join(T, 'b627_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools and the bench script: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                                                    if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md against its pre-act blob', lambda S: S['errata'][1] is not None and S['errata'][0] == S['errata'][1],
     lambda S: put(S, 'errata', ((S['errata'][0] or b'') + b'x', S['errata'][1]))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 746ab804, by blob id, the roots file read by G-ACTROOT-BANKED', lambda S: S['prior_bad'] == [] and S['prior_n'] > 6000,
     lambda S: put(S, 'prior_bad', ['data/b626_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files: the ledgers and the pages', lambda S: corpus_scope(S),
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + ['README.md']))),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] is not None and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] is not None and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-TABLE-UNMOVED', 'the suite`s own regeneration against the committed table: no row added or gone and no grade cell moved', lambda S: S['table_changed'] is not None
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
                                                                          and "startswith('b627')" in S['suite'] and "data/b627_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b627')", ''))),
    ('G-LSREMOTE-ONE-PER-REPO', 'the whole run`s ls-remote calls per repository, the act-root arm`s included, read after every other arm has run (OPEN_TRAILS :12703)',
     lambda S: lsr_ok(S), lambda S: put(S, 'lsr', {PP: 2})),
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
    rec('b627 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
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
    av = S['ar_verify']
    rec('  ### THE ACT-ROOT CHAIN, recomputed: %s' % ('; '.join('%s %s%s' % (a, v, (' (' + '; '.join(w) + ')') if w else '') for a, v, w in av) or 'no act rooted'))
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
        out = os.path.join(D, 'b627_arms_prerun.txt')
    elif MID:
        out = os.path.join(D, sys.argv[sys.argv.index('--mid') + 1])
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b627_checks_postpush.txt' if pushed else 'b627_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b627_arms_prerun.txt', 'b627_lsr_prerun.json').replace('b627_checks', 'b627_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b627_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
