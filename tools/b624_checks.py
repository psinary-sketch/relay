# -*- coding: utf-8 -*-
"""b624_checks.py -- THE SUITE OF b624, UNDER (R234): THE E0 GATE'S READING OF INDUCTION STEPS, WITH ITS TEST AND THE χ PAGE
RE-EMITTED; THE ACT ROOT CHAINED FROM THIS ACT AND VERIFIED BY A SUITE ARM.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>`, `--mid <name>` or `--prerun`; it writes data/b624_checks.txt before the push and
### data/b624_checks_postpush.txt after it; `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the face is
### sealed, no table regenerated, its counts written to data/b624_arms_prerun.txt.
### ### Every remote is read once per run (OPEN_TRAILS :12703, b616_claims.remote_refs); G-LSREMOTE-ONE-PER-REPO runs last.
### ### THE ACT-ROOT ARM ((R234)(3)): a SOURCE of this suite and not counted on the face, by the ferry's Component 0 -- tools/act_root.py
### does not exist at the seal, so the arm cannot be run at HEAD before it; every run recomputes the chain (act_root.verify, its
### remote reads the suite's own, one per repository) and prints AGREE or DISAGREE per act; the record tool banks it as the arm's
### count (data/b624_root_arm.txt) and H58d is scored on it.
### ### b623'S DEFECTS' SOURCES, REPAIRED ((R234)'s Component 0): (d) a housekeeping commit holds the table files that moved -- no
### predicate asks for all five; (e) every positive control mutates the text its predicate reads -- the count arms count the bank's
### text inside the predicate; (b), (f) the record tool reads its banks from relay and finds a commit by its subject.
### ### The harness is b568's to b623's, carried from tools/b623_checks.py; the sources, predicates and arms are b624's.
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
import b624_worklist as K     # noqa: E402

NL = chr(10)
PP, GS, KER = 'D:/MY-DOwnloads/PLACE-papers', 'D:/SIDE-global-section', 'D:/SIDE-explicit-formula'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
FACE = os.path.join(D, 'b624_registration_2026-10-05.txt')
PAGE, DIR_PAGE = K.PAGE, K.DIR_PAGE
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP, gs='3528bcf')
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b', 'product-b600': '1dd5cd7',
        'doubling-keiper-b601': '5fc0c87', 'sign-window-b602': '914c413', 'family-b603': '1d5d4dd'}
STEPZERO = K.STEPZERO
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
ABSENT = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_9.md'
OLD_PINS = ('02fba720', 'f695c98')
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/db8d87ba-3c6c-4b82-8201-6f0312a45734/scratchpad'
INST = ('b623_checks.py', 'b623_record.py', 'b604_record.py', 'b602_record.py', 'b566_record.py', 'b565_record.py', 'b616_record.py',
        'b616_claims.py', 'b611_claims.py', 'b558_record.py', 'chain_page.py', 'test_chain_page_b596.py', 'g_chain_page.py', 'banned_terms.py',
        'terminal_table.py', 'table_gate.py', 'reg_seal.py', 'b378_lockgate.py', 'push_gated.sh', 'test_push_gated.sh')
E0_SUBJECT = 'b624 (R234)(2)'
ROOT_SUBJECT = 'b624 (R234)(3)'
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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b624')
            and 'data/b624_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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


def sources():
    import b624_record as REC
    import b616_record as R6
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b624_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b624_') and f.endswith('.py'))
    S = dict(
        REC=REC, face=face, ferry=rd('b624_ferry.txt'), scan=rd('b624_ferry_scan.txt'), cens=rd('b624_census_stepzero.txt'),
        fcens=rd('b624_faces_census_stepzero.txt'), pins0=rd('b624_pins_stepzero.txt'), procs=rd('b624_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b623_closing.txt'), reads=rd('b624_reads.txt'), branches=rd('b624_branches.txt'), answers=rd('b624_author_answers.txt'),
        prerun=rd('b624_arms_prerun.txt'), rl=jl('b624_record_lines.json'),
        e0b=rd('b624_e0_before.txt'), e0d=rd('b624_e0_diff.txt'), e0t=rd('b624_e0_test.txt'), e0j=jl('b624_e0_test.json'),
        nodesj=jl('b624_e0_nodes.json'), nodest=rd('b624_e0_nodes.txt'), tblj=jl('b624_table.json'),
        pj={k: jl('b624_page_%s.json' % k) for k in ('zeta', 'chi')}, arms=rd('b624_page_arms.txt'),
        rtt=rd('b624_root_test.txt'), rtj=jl('b624_root_test.json'), arj=jl('b624_act_root.json'), art=rd('b624_act_root.txt'),
        rootsf=rd('act_roots.txt'), armj=jl('b624_root_arm.json'),
        rpush=rd('b624_root_push_out.txt'), ppush=rd('b624_pp_root_push_out.txt'),
        absent=tri(PP, ABSENT, PRE['pp']),
        e0files={p: tri(ROOT, p, PRE['relay']) for p in K.E0_FILES},
        rootfiles={p: tri(ROOT, p, PRE['relay']) for p in K.ROOT_FILES},
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
        kern_face=(jl('b624_kernels_face.json').get('kernels') or {}),
        lv_head=gs('D:/SIDE-lv-conservation', 'rev-parse', 'HEAD'), trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        kcur=gs(KER, 'branch', '--show-current'),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b623*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b624_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b624_mustnotexist.txt')), table_changed=None,
        fj=jl('b624_findings.json'), tj=jl('b624_trail.json'), sc=jl('b624_scores.json'), desk=rd('b624_desk_notes.txt'),
        lsr=None,
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
    S['pp_remote'] = KC0.remote_refs(PP).get('refs/heads/main', '')
    pub = []
    for nm, pre, now in (('FINDINGS', S['fi_pre'], S['fi_now']), ('OPEN_TRAILS', S['ot_pre'], S['ot_now'])):
        pub.append(now[len(pre):].decode('utf-8', 'replace') if now and pre and now.startswith(pre) else '')
    for f in sorted(os.listdir(D)):
        if f.startswith(('b624_', 'audit_b624_')) and os.path.isfile(os.path.join(D, f)):
            pub.append(read(os.path.join(D, f)))
    pub += [read(f) for f in tools] + [rd('act_roots.txt')]
    for p, (now, _b, _h) in list(S['e0files'].items()) + list(S['rootfiles'].items()):
        pub.append((now or b'').decode('utf-8', 'replace'))
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
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    X = {}
    for k in ('zeta', 'chi'):
        X['gcp_' + k] = GCP.arm(os.path.join(D, K.NODES[k]), os.path.join(SP, '_b624_gcp'), os.path.join(D, K.PROBE[k]))
    X['ctl'] = TC.control()
    X['ctl_arm'] = TC.ARM
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
    # ### every page node graded now by the rule before (its blob at PRE_RELAY) and after (the working file)
    try:
        oldr, newr = S['REC'].e0_module(PRE['relay']), S['REC'].e0_module(None)
        seen, _p = S['REC']._headers(newr)
        heads = {}
        for (k, n), (h, kind) in seen.items():
            heads.setdefault(n, (h, kind))
        X['moved_now'] = sorted(n for n, (h, kind) in heads.items()
                                if oldr.grade(h, 'theorem' if kind == 'theorem' else 'def')[0] != newr.grade(h, 'theorem' if kind == 'theorem' else 'def')[0])
        X['nodes_now'] = len(heads)
    except Exception as e:
        X['moved_now'], X['nodes_now'] = None, 'raised %s' % type(e).__name__
    # ### THE ACT-ROOT ARM, a source not counted on the face (the ferry's Component 0): the chain recomputed, one read per repository
    try:
        import act_root as AR
        X['ar_verify'] = AR.verify(remote=KC0.remote_refs)
    except ImportError:
        X['ar_verify'] = None
    X['e0_stat'] = gs(ROOT, 'diff', '--stat', PRE['relay'], '--', *K.E0_FILES).split(NL)[-1].strip()
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


def weight_ok(S):
    x = rline(S, 0)
    a = fline(S, x.get('line'))
    return bool(x) and a.startswith(x.get('head', '\x00')) and '(:7492)' in a and '**N5, ruled, `(R234)`(1):**' in a and 'relay 40f13d5f' in a \
        and 'defects (a)-(f) the seat’s' in a and ('OPEN_TRAILS :%d-:%d' % (rline(S, 1).get('line', 0), rline(S, 5).get('line', 0))) in a


def readings_ok(S):
    rd_ = K.b623_readings()
    out = []
    for i in range(5):
        x = rline(S, 1 + i)
        o = oline(S, x.get('line'))
        line, _what, key = K.READINGS[i]
        out.append(bool(x) and bool(rd_.get(key)) and o.startswith(x.get('head', '\x00')) and ('(:%d)' % line) in o and rd_[key] in o
                   and ('READING %s,' % key) in o)
    return len(out) == 5 and all(out)


def manifest_ok(S):
    x = rline(S, 6)
    o = oline(S, x.get('line'))
    return bool(x) and o.startswith(x.get('head', '\x00')) and '(:12210)' in o and '“Act root: <act> <root>”' in o and 'No MANIFEST is written by b624' in o


def alone(S, files, prefix):
    c = [h for h, f in S['rfiles'].items() if f == sorted(files)]
    msg = {h: s for h, s in S['rlog']}
    return len(c) == 1 and msg[c[0]].split(' ', 1)[1].startswith(prefix) and S['lock_epoch'] is not None \
        and int(msg[c[0]].split(' ', 1)[0]) > S['lock_epoch'] and not [h for h, f in S['rfiles'].items() if set(f) & set(files) and h != c[0]]


def count(text):
    """### b623's defect (e), repaired: the count is made here, from the text the positive control mutates."""
    cases = [l for l in (text or '').split(NL) if re.match(COUNT_CASE, l)]
    return len(cases), sum(1 for c in cases if c.rstrip().endswith('PASS'))


def e0_before_ok(S):
    b = S['e0b']
    old = (blob(ROOT, '%s:tools/e0_rule.py' % PRE['relay']) or b'').decode('utf-8')
    gi = [l for l in b.split(NL) if l.startswith('    :160  def grade(')]
    return bool(gi) and all(re.sub(r'^\s*:\d+\s{1,4}', '', l) in old for l in b.split(NL)[2:] if l.startswith('    :')) \
        and "DOMAIN = r'(?:≠|<|≤|=|∈|\\.Even\\b|IsPrimitive)'" in b


def e0_diff_ok(S):
    files = S['e0files']
    banked = [l[4:].strip() for l in S['e0d'].split(NL) if l.startswith('### ') and 'changed' in l]
    return all(a is not None and a == c and a != b for a, b, c in files.values()) and bool(S['e0_stat']) and banked == [S['e0_stat'].strip()] \
        and '+def statement_only(head):' in S['e0d'] and '+DOMAIN = r\'(?:≠|<|≤|=|∈|∉|\\.Even\\b|IsPrimitive)\'' in S['e0d']


def e0_test_ok(S):
    n, p = count(S['e0t'])
    return n == 13 and p == 13 and S['e0j'].get('cases') == n and S['e0j'].get('passing') == p and S['e0j'].get('rc') == 0 \
        and '### ### **13 of 13 cases as wanted -- PASS**' in S['e0t']


def e0_control_ok(S):
    c = S['e0j'].get('control') or {}
    m = re.search(r'the rule as it stood at relay \w+ \(exit (\d+)\): cases (\d+), passing (\d+), failing (.*)$', S['e0t'], re.M)
    return bool(m) and m.group(2) == '13' and m.group(3) == '10' and c.get('failing') == ['(8) ', '(9) ', '(11)'] and m.group(1) == '1'


def nodes_ok(S):
    j = S['nodesj']
    return S['moved_now'] is not None and S['moved_now'] == j.get('moved') == [K.CLAUSE_NODES[1][0]] and len(j.get('rows') or []) == S['nodes_now'] \
        and bool(j.get('disagreements'))


def planted_ok(S):
    ps = S['e0j'].get('planted') or []
    out = []
    for p in ps:
        m = re.match(r'planted: (.+\.lean) \((\d+) bytes\)$', p)
        out.append(bool(m) and os.path.isabs(m.group(1)) and os.path.exists(m.group(1)) and os.path.getsize(m.group(1)) == int(m.group(2))
                   and m.group(1).replace('\\', '/').startswith(SP.replace('\\', '/')))
    return len(out) == 2 and all(out)


def _h(S, k, want):
    return (S['sc'].get(k) or [''])[0] == want and ('(%s)' % k.upper()) in S['desk'] and ('### **%s.**' % want) in S['desk']


def h58_ok(S, k):
    rows = {r['name']: r for r in S['nodesj'].get('rows') or []}
    if k == 'H58a':
        pl, ins = rows.get(K.CLAUSE_NODES[0][0], {}), rows.get(K.CLAUSE_NODES[1][0], {})
        want = 'HOLDS' if pl.get('after') == ins.get('after') == 'DERIVES' and pl.get('before') == 'DERIVES' and ins.get('before') == 'DERIVES' else 'REFUTED'
    elif k == 'H58b':
        ok = all(re.search(r'^  \(%d\) .* PASS$' % n, S['e0t'], re.M) for n in (10, 11, 12))
        want = 'HOLDS' if ok else 'REFUTED'
    elif k == 'H58c':
        t = S['tblj']
        want = 'HOLDS' if t and not (t.get('changed') or t.get('added') or t.get('gone')) else 'REFUTED'
    else:
        a = S['armj']
        want = 'HOLDS' if a and a.get('root_recomputed') == a.get('root') and a.get('root_copy') != a.get('root') and S['ar_verify'] \
            and all(v == 'AGREE' for _x, v, _w in S['ar_verify']) else 'REFUTED'
    return _h(S, k, want)


def table_after_ok(S):
    t = S['tblj']
    return bool(t) and t.get('rc') == 0 and not (t.get('changed') or t.get('added') or t.get('gone')) and t.get('files_moved') is not None


def page_chi_ok(S):
    j = S['pj']['chi']
    a, b, c = S['pages'][DIR_PAGE]
    ga, gc = S['REC']._grade_cells((b or b'').decode('utf-8')), S['REC']._grade_cells((c or b'').decode('utf-8'))
    moved = sorted(n for n in set(ga) | set(gc) if ga.get(n) != gc.get(n) and not n.startswith('tier:'))
    commits = [h for h, f in S['pp_files'].items() if DIR_PAGE in f]
    alone_ = (len(commits) == 1 and S['pp_files'][commits[0]] == [DIR_PAGE] and dict(S['pp_log'])[commits[0]].startswith('b624 (R234)')) if j.get('changed') else not commits
    return j.get('rc') == 0 and j.get('dry') is False and a is not None and a == c and hashlib.sha256(c).hexdigest() == j.get('sha256') and alone_ \
        and moved == [] and j.get('grade_cells_moved') == [] and len(ga) > 30


def disagree_ok(S):
    d = S['nodesj'].get('disagreements') or []
    return bool(d) and all(('  %s' % x['name']) in S['nodest'] for x in d) and any(x['name'] == K.CLAUSE_NODES[1][0] and x['table'] == 'INTERFACES'
                                                                              and x['rule'] == 'DERIVES' for x in d)


def arms_ok(t):
    return 'PAGE ARMS PASSING : 2 of 2' in t and ('%s PASSING : 2 of 2' % CONTROL_ARM) in t


def root_test_ok(S):
    n, p = count(S['rtt'])
    return n >= 4 and n == p and S['rtj'].get('cases') == n and S['rtj'].get('rc') == 0


def root_banked_ok(S):
    import act_root as AR
    j = S['arj']
    rows = [l.split() for l in S['rootsf'].split(NL) if l.strip()]
    return bool(j) and len(rows) >= 1 and rows[0] == ['b624', j.get('root'), AR.EMPTY] and j.get('previous') == AR.EMPTY \
        and AR.root_of(j.get('items') or [], j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and len(j['reads']['heads']) == 34 and len(j['reads']['banks']) > 20


def midpush_ok(S):
    j = S['arj']
    heads = (j.get('reads') or {}).get('heads') or {}
    m1 = re.search(r'push_gated: main read back at the remote: (\w+)', S['rpush'])
    m2 = re.search(r'push_gated: main read back at the remote: (\w+)', S['ppush'])
    return bool(m1 and m2) and heads.get('relay') == m1.group(1) and heads.get('PLACE-papers') == m2.group(1)


def hold_ok(S):
    a = S['answers']
    return re.search(r'### b624 -- THE AUTHOR`S ANSWERS, 3 prompt\(s\)', a) is not None and a.count('RESULT (transcript line') == 2 \
        and '∉' in a and 'ENCODES-CONCLUSION' in a and 'MANIFEST' in a and 'option 1' in a


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(S['REC'].CURRENTS)


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 20]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') and fline(S, e).startswith('## The E0 gate at induction steps: ') \
        and all(x in tail for x in ('**The clause**', '**The table and the page.**', '**The act root**', '**The record lines**', '**The scores.**',
                                    '**Read in mutual light**', 'strengthens', '**Next.**', 'b625'))


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
    return bool(f) and len(f) == 8 and all(k in n and n[k] == f[k] for k in f) and all(n[k][0].startswith(v) for k, v in S['REC'].KERN_PIN.items()) \
        and S['kcur'] == 'main' and S['trial'] == 'f22ff35' and S['lv_head'].startswith('2f71068a')


def corpus_scope(S):
    pages = [K.PNAME[k] for k in ('zeta', 'chi') if S['pj'][k].get('changed')]
    return S['pp_changed'] == sorted(['FINDINGS.md', 'OPEN_TRAILS.md'] + pages)


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


READ_NEEDLES = ('OPEN_TRAILS.md @ 271de076', 'tools/e0_rule.py @ 884d0848', 'tools/test_e0_rule.py @ 884d0848', 'tools/chain_page.py @ 884d0848',
                'Family.lean @ 1d5d4dd9', 'PowerWindow.lean @ 1d5d4dd9', 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md @ 271de076',
                'THE_KEYSTONE_CENSUS_v0_4.md @ 271de076', 'data/b623_tags.txt @ 884d0848', 'data/b622_unclassified.txt @ 884d0848',
                'tools/mirror_build.ps1 @ 884d0848', 'data/b623_closing_push_out.txt @ 313b8e48',
                ':12210 ', ':12436 ', ':12438 ', ':11864 ', ':12228 ', ':12266 ', ':12354 ', ':12356 ', ':12799 ', ':12887 ', ':12917 ')

ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R234) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b623`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b623' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b624 -- x'])),
    ('G-R234-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R234) END' in S['ferry'] and S['ot'].count('**(R234) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R234) ratified', '(R234) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in READ_NEEDLES) and 'NO SUCH LINE' not in S['reads'],
     lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ANSWERS-BANKED', 'the act`s answers bank: the three prompts before the seal in two calls, verbatim, their options and answers', lambda S: hold_ok(S),
     lambda S: put(S, 'answers', S['answers'].replace('3 prompt(s)', '4 prompt(s)', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay 313b8e48`s files', lambda S: S['pushout'][0] == ['data/b623_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/b623_closing_push_out.txt', 'x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b623') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b623'}))),
    ('G-KEPT-BRANCHES', 'the explicit-formula kernel`s kept branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'family-b603': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80 and every PLACE-papers read at ba5f0ea, run afresh through the test`s control()',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(S['ctl'][0], ok=False)] + S['ctl'][1:])),
    ('G-INSTRUMENTS-UNEDITED', 'b623`s suite and record tool, the shared record tools, the claims modules, the generator and its test, the page arm, the scanner, the table generator and its gate, the seal, the lock gate and the push gate against 884d0848',
     lambda S: all(a is not None and a == b for a, b in S['inst'].values()) and len(S['inst']) == len(INST),
     lambda S: put(S, 'inst', dict(S['inst'], **{'b623_record.py': (S['inst']['b623_record.py'][0], (S['inst']['b623_record.py'][1] or b'') + b'x')}))),
    ('G-ABSENT-IS-NONE', 'the source builder on a file no act wrote and on empty bytes', lambda S: absent_ok(S), lambda S: put(S, 'absent', (b'', b'', b''))),
    ('G-GEN-OLD-LISTS-FROZEN', 'b602`s and b603`s lists re-emitted now with every relay read at 02fba720 and every PLACE-papers read at f695c98, against the pages at f695c98',
     lambda S: len(S['old_frozen']) == 2 and all(x['rc'] == 0 and x['equal'] for x in S['old_frozen']),
     lambda S: put(S, 'old_frozen', [S['old_frozen'][0], dict(S['old_frozen'][1], equal=False)] if len(S['old_frozen']) == 2 else [])),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b623`s weight, N5`s ruling, the defects cited, the readings` lines', lambda S: weight_ok(S),
     lambda S: put(S, 'find', S['find'].replace('**N5, ruled, `(R234)`(1):**', '**N5:**'))),
    ('G-READINGS-BESIDE-CLAUSES', 'OPEN_TRAILS at the banked lines: each of b623`s five readings as printed, addressed to the clause it resolves', lambda S: readings_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('READING (3), CONFIRMED AS PRINTED', 'READING (3), CONFIRMED'))),
    ('G-MANIFEST-STANDING', 'OPEN_TRAILS at the banked line: the act root in MANIFEST, standing, addressed to :12210', lambda S: manifest_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('No MANIFEST is written by b624', 'MANIFEST is written by b624'))),
    ('G-E0-BEFORE-BANKED', 'the grade function bank against the rule`s blob at 884d0848', lambda S: e0_before_ok(S),
     lambda S: put(S, 'e0b', S['e0b'].replace('def grade(', 'def graded('))),
    ('G-E0-COMMITTED-ALONE', 'relay`s log: the rule and its test in one commit of their own, after the lock', lambda S: alone(S, list(K.E0_FILES), E0_SUBJECT),
     lambda S: put(S, 'rfiles', dict(S['rfiles'], deadbee=sorted(K.E0_FILES)))),
    ('G-E0-DIFF-BANKED', 'the rule and its test on disk and at HEAD against 884d0848; the diff bank`s stat line, both sides stripped; the clause in it', lambda S: e0_diff_ok(S),
     lambda S: put(S, 'e0d', S['e0d'].replace('+def statement_only(head):', '+def statement(head):'))),
    ('G-E0-TEST-COUNTED', 'the test bank`s text counted here by its case pattern: thirteen of thirteen', lambda S: e0_test_ok(S),
     lambda S: put(S, 'e0t', S['e0t'] + '\n  (14) planted : PASS')),
    ('G-E0-CONTROL-REFUTED', 'the test with the rule as it stood: exactly the clause`s cases (8), (9) and (11) fail', lambda S: e0_control_ok(S),
     lambda S: put(S, 'e0t', S['e0t'].replace('cases 13, passing 10', 'cases 13, passing 13'))),
    ('G-E0-NODES-NOW', 'every page node graded now by the rule before and after: exactly the step lemma moves, against the bank', lambda S: nodes_ok(S),
     lambda S: put(S, 'moved_now', (S['moved_now'] or []) + ['x'])),
    ('G-PLANTED-AT-PATHS', 'the two planted modules at the absolute paths the test printed, under the scratchpad, their sizes as printed', lambda S: planted_ok(S),
     lambda S: put(S, 'e0j', dict(S['e0j'], planted=(S['e0j'].get('planted') or [])[:1]))),
    ('G-H58A-SCORED', 'H58a recomputed from the nodes bank, against the scores and the desk', lambda S: h58_ok(S, 'H58a'), lambda S: _sc(S, 'H58a')),
    ('G-H58B-SCORED', 'H58b recomputed from the test bank, against the scores and the desk', lambda S: h58_ok(S, 'H58b'), lambda S: _sc(S, 'H58b')),
    ('G-TABLE-AFTER-CLAUSE', 'the table bank after the clause: no row added, gone or changed', lambda S: table_after_ok(S),
     lambda S: put(S, 'tblj', dict(S['tblj'], changed=[['SIDE-explicit-formula', 'x']]))),
    ('G-PAGE-CHI-NOW', 'the χ page on disk and at HEAD against its bank; its grade cells against c9e9a9c`s successor 271de07, unmoved; committed alone where changed', lambda S: page_chi_ok(S),
     lambda S: put(S, 'pages', dict(S['pages'], **{DIR_PAGE: (S['pages'][DIR_PAGE][0], S['pages'][DIR_PAGE][1], (S['pages'][DIR_PAGE][2] or b'').replace(
         b'| SIDE-explicit-formula | DERIVES |', b'| SIDE-explicit-formula | SHELL |', 1))}))),
    ('G-DISAGREEMENTS-PRINTED', 'the nodes bank: every page node whose table grade differs from the rule`s read printed, the step lemma among them', lambda S: disagree_ok(S),
     lambda S: put(S, 'nodest', S['nodest'].replace('finsetSum_insert', 'finsetSum_x'))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b622`s list and b602`s v0.20 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b622`s list and b603`s v0.21 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank after the clause: both page arms and the frozen control', lambda S: arms_ok(S['arms']),
     lambda S: put(S, 'arms', S['arms'].replace('PAGE ARMS PASSING : 2 of 2', 'PAGE ARMS PASSING : 1 of 2'))),
    ('G-H58C-SCORED', 'H58c recomputed from the table bank, against the scores and the desk', lambda S: h58_ok(S, 'H58c'), lambda S: _sc(S, 'H58c')),
    ('G-ACTROOT-COMMITTED-ALONE', 'relay`s log: act_root.py and its test in one commit of their own, after the lock', lambda S: alone(S, list(K.ROOT_FILES), ROOT_SUBJECT),
     lambda S: put(S, 'rfiles', dict(S['rfiles'], deadbee=sorted(K.ROOT_FILES)))),
    ('G-ACTROOT-TEST-COUNTED', 'the act-root test bank`s text counted here by its case pattern, every case passing', lambda S: root_test_ok(S),
     lambda S: put(S, 'rtt', S['rtt'] + '\n  (99) planted : FAIL')),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s first line, the root bank and its items: b624 from the empty string`s sha256, the root recomputing', lambda S: root_banked_ok(S),
     lambda S: put(S, 'rootsf', S['rootsf'].replace('b624 ', 'b62x ', 1))),
    ('G-ACTROOT-MIDPUSH', 'the root`s relay and PLACE-papers heads against the read-backs of the pushes made before it', lambda S: midpush_ok(S),
     lambda S: put(S, 'rpush', S['rpush'].replace('main read back at the remote: ', 'main read back at the remote: 0', 1))),
    ('G-H58D-SCORED', 'H58d recomputed from the arm`s run in this suite and the one-byte control`s bank, against the scores and the desk', lambda S: h58_ok(S, 'H58d'),
     lambda S: _sc(S, 'H58d')),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD, lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'this act`s trail record: the root and its previous, as data/act_roots.txt holds them', lambda S: bool(S['arj'])
     and ('**Act root:** b624 `%s` (previous `%s`' % (S['arj'].get('root'), S['arj'].get('previous'))) in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Act root:** b624', '**Act root:** b62x'))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record: the strike items, the answers and the disagreements', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and '**The author’s three answers before the seal**' in trail(S) and '**For the author’s ruling:**' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**For the author’s ruling:**', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b625, W-ORD-VENDOR-FINALMULT' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b625, W-ORD-VENDOR-FINALMULT', 'x'))),
    ('G-CURRENTS-UNEDITED', 'the current versions, the census, REGISTRY, ERRATA, README, SPIRAL_MAP and the ζ page on disk and at HEAD against 271de07',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'REGISTRY.md': ((S['currents']['REGISTRY.md'][0] or b'') + b'x',
                                                                                                    S['currents']['REGISTRY.md'][1], S['currents']['REGISTRY.md'][2])}))),
    ('G-NODISCLOSURE-PUBLIC', 'the no-disclosure arm on every public byte this act writes: the ledger appends, its banks and tools, the rule, act_root.py and the roots file',
     lambda S: bool(S['nd_pub']) and not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', dict(S['nd_pub'], method=1))),
    ('G-KERNELS-UNTOUCHED', 'every kernel this act reads: main, tags by peel, branches and status against the face; the explicit-formula checkout on main; lv and its trial branch',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', dict(S['kern_now'], **{'SIDE-cosmo': ['0', {}, [], '']}))),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('36352a0', '36352a0', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b624_record.py'): S['tooltext'].get(os.path.join(T, 'b624_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                              if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md against its pre-act blob', lambda S: S['errata'][1] is not None and S['errata'][0] == S['errata'][1],
     lambda S: put(S, 'errata', ((S['errata'][0] or b'') + b'x', S['errata'][1]))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 884d0848, by blob id', lambda S: S['prior_bad'] == [] and S['prior_n'] > 6000,
     lambda S: put(S, 'prior_bad', ['data/b623_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files: the ledgers and a page only where its re-emission changed', lambda S: corpus_scope(S),
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + ['README.md']))),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] is not None and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] is not None and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-GS-UNTOUCHED', 'SIDE-global-section`s diff against 3528bcf and its HEAD', lambda S: S['gs_diff'] == [] and S['gs_head'].startswith(PRE['gs'])
     and S['corr_now'] == S['corr_pre'], lambda S: put(S, 'gs_diff', ['CORRESPONDENCE.md'])),
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
                                                                          and "startswith('b624')" in S['suite'] and "data/b624_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b624')", ''))),
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
    rec('b624 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
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
    rec('  ### THE ACT-ROOT ARM ((R234)(3)), a source of this suite, not counted on the face: %s' % (
        'tools/act_root.py absent at this run' if av is None else '; '.join('%s %s%s' % (a, v, (' (' + '; '.join(w) + ')') if w else '') for a, v, w in av) or 'no act rooted'))
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
        out = os.path.join(D, 'b624_arms_prerun.txt')
    elif MID:
        out = os.path.join(D, sys.argv[sys.argv.index('--mid') + 1])
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b624_checks_postpush.txt' if pushed else 'b624_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b624_arms_prerun.txt', 'b624_lsr_prerun.json').replace('b624_checks', 'b624_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b624_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
