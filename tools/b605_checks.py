# -*- coding: utf-8 -*-
"""b605_checks.py -- THE SUITE OF b605, UNDER (R215): THE SIEVE TABLE AT v0.3 -- THE VERDICT COLUMN RE-READ WITH NOT A ROUTE AS A
THIRD VERDICT AND THE FACES OF ONE CLAUSE UNDER ONE VERDICT.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>` or `--prerun`; it writes data/b605_checks.txt before the push and
### data/b605_checks_postpush.txt after it. ### `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the
### face is sealed, no table regenerated, its counts written to data/b605_arms_prerun.txt and nothing else.
### ### The harness is b568's to b604's, carried from tools/b604_checks.py (its imports, helpers, regenerate and main); the
### sources, predicates and arms are b605's. The control arm is the frozen one of (R207)(2).
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
FACE = os.path.join(D, 'b605_registration_2026-10-03.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
CUR = 'phase2/method/THE_FINDINGS_AS_THEY_STAND.md'
ED2 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_2.md'
ED = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_3.md'
PRE = dict(relay='3651a663', pp='c7d3d48', gs='3528bcf', ker='1d5d4dd')
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf69', 'SIDE-rcurve': 'd5f33b44', 'SIDE-explicit-formula': '1d5d4dd9'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b', 'product-b600': '1dd5cd7',
        'doubling-keiper-b601': '5fc0c87', 'sign-window-b602': '914c413', 'family-b603': '1d5d4dd'}
STEPZERO = '61594b11'
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/c780ded1-4e24-4686-94a2-dbeb16d65f7a/scratchpad'


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b605')
            and 'data/b605_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    import b605_record as REC
    import b604_record as R4
    import b604_rows as W
    import b605_verdicts as V
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b605_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b605_') and f.endswith('.py'))
    edp = os.path.join(PP, *ED.split('/'))
    S = dict(
        REC=REC, R4=R4, W=W, V=V, face=face, ferry=rd('b605_ferry.txt'), scan=rd('b605_ferry_scan.txt'), cens=rd('b605_census_stepzero.txt'),
        fcens=rd('b605_faces_census_stepzero.txt'), pins0=rd('b605_pins_stepzero.txt'), procs=rd('b605_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b604_closing.txt'), reads=rd('b605_reads.txt'), branches=rd('b605_branches.txt'), answers=rd('b605_author_answers.txt'),
        prerun=rd('b605_arms_prerun.txt'), defects=rd('b605_defects.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))))
              for f in ('b604_checks.py', 'b604_record.py', 'b604_rows.py', 'test_chain_page_b596.py', 'chain_page.py', 'e0_rule.py',
                        'g_chain_page.py', 'push_gated.sh', 'banned_terms.py', 'b558_record.py')},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        readme=(cr0(raw(os.path.join(PP, 'README.md'))), cr0(blob(PP, PRE['pp'] + ':README.md'))),
        registry=(cr0(raw(os.path.join(PP, 'REGISTRY.md'))), cr0(blob(PP, PRE['pp'] + ':REGISTRY.md'))),
        faces=(cr0(raw(os.path.join(PP, 'FACES_LEDGER.md'))), cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md'))),
        errata=(cr0(raw(os.path.join(PP, 'ERRATA.md'))), cr0(blob(PP, PRE['pp'] + ':ERRATA.md'))),
        spiral=(cr0(raw(os.path.join(PP, 'SPIRAL_MAP.md'))), cr0(blob(PP, PRE['pp'] + ':SPIRAL_MAP.md'))),
        cur=(cr0(raw(os.path.join(PP, *CUR.split('/')))), cr0(blob(PP, PRE['pp'] + ':' + CUR)), cr0(blob(PP, 'HEAD:' + CUR))),
        v2=(cr0(raw(os.path.join(PP, *ED2.split('/')))), cr0(blob(PP, PRE['pp'] + ':' + ED2)), cr0(blob(PP, 'HEAD:' + ED2))),
        ed_disk=cr0(raw(edp)), ed_head=cr0(blob(PP, 'HEAD:' + ED)),
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
        push_lists={r: gs(r, 'branch', '--list', 'push-b604*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b605_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b605_mustnotexist.txt')), table_changed=None,
        fj=jl('b605_findings.json'), tj=jl('b605_trail.json'), sc=jl('b605_scores.json'), desk=rd('b605_desk_notes.txt'),
        rl=jl('b605_record_lines.json'), VB=jl('b605_verdicts.json'), vtxt=rd('b605_verdicts.txt'),
        E=jl('b605_edition.json'), H=jl('b605_h28.json'), bank=rd('b605_edition_FINDINGS_STAND.txt'), repin=rd('b605_repin.txt'),
        termscan=rd('b605_edition_termscan.txt'),
        PZ=jl('b605_page_zeta.json'), PX=jl('b605_page_chi.json'), arms_c2=rd('b605_page_arms_c2.txt'),
    )
    S['ed'] = lines_of(S['ed_disk']) if S['ed_disk'] else []
    S['v2l'] = lines_of(S['v2'][1])
    S['scan_now'] = subprocess.run([sys.executable, os.path.join(T, 'banned_terms.py'), '--new', edp], capture_output=True, text=True,
                                   encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8')).stdout if S['ed_disk'] else ''
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
    S.update(extra_sources(S))
    return S


def extra_sources(S):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    X = {}
    X['gcp_zeta'] = GCP.arm(os.path.join(D, 'b602_nodes_zeta.txt'), os.path.join(SP, '_b605_gcp'), os.path.join(D, 'b602_probe_out.txt'))
    X['gcp_chi'] = GCP.arm(os.path.join(D, 'b603_nodes_chi.txt'), os.path.join(SP, '_b605_gcp'), os.path.join(D, 'b603_chi_probe_out.txt'))
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
    return ls[i] if len(ls) == 3 else {}


def weight_ok(S):
    x = _rl(S, 0)
    a = fline(S, x.get('line'))
    return bool(x) and x.get('file') == 'FINDINGS.md' and a.startswith(x['head']) and '(:7060)' in a and 'b604 AT ITS WEIGHT' in a \
        and 'aca6804' in a and '216 of 216' in a and '78 of 78' in a and 'accepted at `(R215)`(3)' in a and x['line'] > 7060


def correction_ok(S):
    x = _rl(S, 1)
    a = fline(S, x.get('line'))
    return bool(x) and x.get('file') == 'FINDINGS.md' and a.startswith(x['head']) and 'THE VERDICT COLUMN, READ' in a \
        and 'navigator’s mis-specification' in a and 'recorded as correct' in a and 'NOT A ROUTE' in a and x['line'] > _rl(S, 0).get('line', 10 ** 9)


def h28b_clause_ok(S):
    x = _rl(S, 2)
    n = x.get('line')
    a = oline(S, n)
    return bool(x) and x.get('file') == 'OPEN_TRAILS.md' and a.startswith(S['REC'].H_HEAD) and '(:11864)' in a \
        and 'every sentence moved whole to back matter counts as a recorded removal in H28b’s bound' in a \
        and 'the diff bank lists each with its destination' in a and n > 12440


def verdicts_banked(S):
    VB, E, REC, W, V = S['VB'], S['E'], S['REC'], S['W'], S['V']
    vt = S['vtxt'].split(NL)
    if not VB or not E or VB.get('at', 'z') >= E.get('at', ''):
        return False
    rows = VB.get('rows') or []
    ok = [r['id'] for r in rows] == [r['id'] for r in W.ROWS] and all(
        r['new'] == REC._new(r['id']) and r['why'] == V.NEW[r['id']]['why'] and r['old'] == REC._old(REC.R4._row(r['id'])) for r in rows)
    lines = VB.get('lines') or {}
    ok = ok and all(0 < lines.get(r['id'], 0) <= len(vt) and vt[lines[r['id']] - 1].startswith('  %s | ' % r['id'])
                    and (' -> %s | ' % r['new']) in vt[lines[r['id']] - 1] for r in rows)
    c = VB.get('counts') or {}
    return ok and sum(c.values()) == len(W.ROWS) and '### THE FACE GROUPS' in S['vtxt'] and '### THE COUNTS' in S['vtxt'] \
        and S['vtxt'].count('### ### **H39') == 4


def face_group_ok(S):
    REC, V, E, ed = S['REC'], S['V'], S['E'], S['ed']
    if not ed or not E:
        return False
    P = E['pos']
    fh, cl, rh = P['face_head'], P['clause_line'], P['rest_head']
    rows = [P['rows'].get(k, 0) for k in V.FACE_GROUP]
    return ed[fh - 1] == REC.FACE_HEAD % len(V.FACE_GROUP) and ed[cl - 1].startswith('**The clause’s verdict, stated once: BRIGHT, by test 2 (')\
        and all(fh < x < rh for x in rows) and rows == sorted(rows) and all(' | FACE | — | ' in ed[x - 1] for x in rows) \
        and len(V.FACE_GROUP) >= 7 and sum(1 for l in ed[:ed.index(S['R4'].BM_TAG)] if ' | FACE | — | ' in l) == len(V.FACE_GROUP) \
        and ('%s (%d rows): %s' % (V.CLAUSE['name'], len(V.FACE_GROUP), ', '.join(V.FACE_GROUP))) in S['vtxt']


def h39_ok(S, k):
    S9, _X = S['REC'].h39()
    v = (S['VB'].get('scores') or {}).get(k) or ['', '']
    return v[0] == S9[k][0] and (S['sc'].get(k) or [''])[0] == S9[k][0] and ('(%s)' % k.upper()) in S['desk'] \
        and ('### ### **%s %s' % (k, S9[k][0])) in S['vtxt']


def unedited3(t):
    a, b, c = t
    return bool(b) and a == b == c


def ed_carries(S):
    REC, E, ed = S['REC'], S['E'], S['ed']
    if not ed or not E:
        return False
    ok, bad = REC.carried(E, ed, S['v2l'])
    return not bad and ok == sum(1 for l in S['v2l'] if l.strip()) and hashlib.sha256(S['ed_disk']).hexdigest() == E.get('sha256')


def rows_ok(S):
    REC, R4, W, E, ed = S['REC'], S['R4'], S['W'], S['E'], S['ed']
    if not ed or not E:
        return False
    P = E['pos']['rows']
    body = ed[:ed.index(R4.BM_TAG)] if R4.BM_TAG in ed else ed
    return all(0 < P.get(r['id'], 0) <= len(ed) and ed[P[r['id']] - 1] == REC._line3(r) for r in W.ROWS) \
        and sum(1 for l in body if re.match(r'^\| [A-Z]{2}-\d\d \| ', l)) == len(W.ROWS)


def head_ok(S):
    REC, R4, V, E, ed = S['REC'], S['R4'], S['V'], S['E'], S['ed']
    if not ed or not E:
        return False
    P = E['pos']
    c = (S['VB'].get('counts') or {})
    want = '**The verdicts at this edition:** %d rows -- %d BRIGHT, %d DARK, %d NOT A ROUTE, and %d FACE rows' % (
        len(S['W'].ROWS), c.get(V.BRIGHT, -1), c.get(V.DARK, -1), c.get(V.NAR, -1), c.get(V.FACE, -1))
    return ed[P['version'] - 1] == REC.VERSION3 and ed[P['version'] + 1] == R4.VERSION and P['version'] < ed.index(R4.VERSION) + 1 \
        and ed[P['bullet'] - 1] == REC.BULLET3 and ed[P['routes'] - 1] == REC.ROUTES and REC.TEST1_SCOPE in ed[P['test1'] - 1] \
        and ed[P['test1'] - 1].startswith('1. **Placement register**') and ed[P['verdicts'] - 1].startswith(want) \
        and not any(l.startswith('- **Bright or dark**') for l in ed[:ed.index(R4.BM_TAG)])


def _block(ls, start, stop):
    try:
        a = ls.index(start)
    except ValueError:
        return None
    try:
        b = ls.index(stop, a)
    except ValueError:
        return None
    return ls[a:b]


def bench_ok(S):
    ed, v2 = S['ed'], S['v2l']
    h = '## The bench — the dark registers as falsifiers'
    a, b = _block(ed, h, '---'), _block(v2, h, '---')
    return bool(a) and a == b and len(a) >= 5


def dated_ok(S):
    R4, ed, v2 = S['R4'], S['ed'], S['v2l']

    def blocks(ls):
        out, cur = [], None
        for l in ls:
            if l.startswith('<!-- HISTORY CARRIED BENEATH THIS TABLE'):
                cur = [l]
                continue
            if cur is not None:
                cur.append(l)
                if l == R4.HIST_CLOSE:
                    out.append(cur)
                    cur = None
        return out
    a, b = blocks(ed), blocks(v2)
    return len(a) == 5 and a == b


def mutual_ok(S):
    REC, E, ed, v2 = S['REC'], S['E'], S['ed'], S['v2l']
    if not ed or not E:
        return False
    m = E['pos']['mutual']
    with_rows = [c for c, _n in S['W'].CLUSTERS if any(r['cluster'] == c for r in S['W'].ROWS)]
    v2m = [l for l in v2 if l.startswith('Read in mutual light')]
    return sorted(m) == sorted(with_rows) and all(ed[m[c] - 1] == REC.MUTUAL3[c] for c in REC.MUTUAL3) \
        and all(ed[m[c] - 1] in v2m for c in with_rows if c not in REC.MUTUAL3)


def backmatter_ok(S):
    REC, R4, ed = S['REC'], S['R4'], S['ed']
    if not ed or REC.BM_TAG3 not in ed or R4.BM_TAG not in ed or ed.index(R4.BM_TAG) > ed.index(REC.BM_TAG3):
        return False
    bm = ed[ed.index(REC.BM_TAG3):]
    heads = ['### The re-read and its readings', '### Removals', '### Verdict changes -- every row re-read', '### Rewrites -- the head',
             '### Insertions ordered by the ruling', '### Fact corrections', '### Re-pins of v0.2', '### Placement', '### Correspondence',
             '### Version history']
    pos = [next((i for i, l in enumerate(bm) if l.startswith(h)), -1) for h in heads]
    blanks = [l for l in bm if l.startswith('| ') and not l.startswith('|:--') and l.rstrip().endswith('|  |')]
    return all(p >= 0 for p in pos) and pos == sorted(pos) and not blanks and not any('{ROW3:' in l or '{POS:' in l for l in ed)


def ed_bank_ok(S):
    b, E = S['bank'], S['E']
    return b.startswith('### OFFSET FROM v0.2 (R190)(3):') and ('sha256 %s' % E.get('sha256', '#')) in b \
        and ('the BACK MATTER %d' % E.get('n_backmatter', -1)) in b and '### ### **THE EDITION LANDS: NO SENTENCE HELD.**' in b \
        and b.count('### OFFSET FROM') == 1 and '### THE HEAD`S RESTATEMENT, PRINTED:' in b and '### EVERY CHANGED ROW, PRINTED' in b


def repin_ok(S):
    m = re.search(r'RE-PIN : (\d+) of (\d+) citations hold', S['repin'])
    return bool(m) and m.group(1) == m.group(2) and int(m.group(2)) > 300 and S['E'].get('sha256', '#') in S['bank']


def _hs(S, k, want):
    return S['H'].get(k) == want and (S['sc'].get(k) or [''])[0] == want and ('(%s)' % k.upper()) in S['desk']


def h28a_ok(S):
    E, ed, VB = S['E'], S['ed'], S['VB']
    if not ed or not E or not VB:
        return False
    vt = S['vtxt'].split(NL)
    bmt = NL.join(ed[E['pos']['bm3'] - 1:])
    ok = True
    for rid in VB.get('changed') or []:
        bl = VB['lines'][rid]
        ok = ok and 0 < bl <= len(vt) and vt[bl - 1].startswith('  %s | ' % rid) and ('| %s | :%d | ' % (rid, E['pos']['rows'][rid])) in bmt \
            and ('`data/b605_verdicts.txt` :%d |' % bl) in bmt
    return len(VB.get('changed') or []) > 50 and _hs(S, 'H28a', 'HOLDS' if ok else 'REFUTED')


def h28b_ok(S):
    R4, E, ed = S['R4'], S['E'], S['ed']
    if not ed or not E:
        return False
    body, _bm = R4._body_and_bm(ed)
    b2, _bm2 = R4._body_and_bm(S['v2l'])
    nb, nc = R4._count([l for _i, l in body]), R4._count([l for _i, l in b2])
    allowed = E.get('credit', 0) + E.get('removals', 0) + E.get('ruled_insertions', 0) + sum(abs(x['d']) for x in E.get('rewrite_deltas') or []) \
        + E.get('version_lines', 0)
    want = 'HOLDS' if abs(nb - nc) <= allowed else 'REFUTED'
    return nb == E.get('n_body') and nc == E.get('n_v2_body') and E.get('removals') == 0 and E.get('version_lines') == 1 and _hs(S, 'H28b', want)


def h28c_ok(S):
    R4, ed = S['R4'], S['ed']
    if not ed:
        return False
    body, _bm = R4._body_and_bm(ed)
    beyond = [i for i, l in body for m in R4.CEILING.finditer(l)]
    sn = S['scan_now']
    clean = re.search(r'^\s*VERDICT\s*: CLEAN\s*$', sn, re.M) is not None and re.search(r'live uses\s*:\s*0\b', sn) is not None
    return _hs(S, 'H28c', 'HOLDS' if clean and not beyond else 'REFUTED') and sn.strip() == S['termscan'].strip()


def edition_alone(S):
    c = [h for h, f in S['pp_files'].items() if ED in f]
    return len(c) == 1 and S['pp_files'][c[0]] == [ED] and dict(S['pp_log'])[c[0]].startswith('b605 (R215)(4): ' + ED) \
        and bool(S['ed_head']) and S['ed_head'] == S['ed_disk']


def pages_changed(S):
    out = []
    for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])):
        a, b, c = S['pages'][p]
        out.append(z.get('rc') == 0 and z.get('changed') is True and bool(a) and a == c and a != b
                   and hashlib.sha256(c).hexdigest() == z.get('sha256') and ('`%s`' % ED) in c.decode('utf-8').split('## Placement')[-1])
    return all(out)


def pages_alone(S):
    out = []
    for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])):
        c = [h for h, f in S['pp_files'].items() if p in f]
        if z.get('changed') is True:
            out.append(len(c) == 1 and S['pp_files'][c[0]] == [p] and dict(S['pp_log'])[c[0]].startswith('b605 (R215)(4): ' + p))
        else:
            out.append(z.get('changed') is False and c == [])
    ec = [h for h, f in S['pp_files'].items() if ED in f]
    pc = [h for h, f in S['pp_files'].items() if PAGE in f or DIR_PAGE in f]
    order = [h for h, _s in S['pp_log']]
    return all(out) and bool(ec) and all(order.index(h) > order.index(ec[0]) for h in pc)


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 30]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') and fline(S, e).startswith('## The sieve table at v0.3: NOT A ROUTE as the third verdict') \
        and '**The edition**' in tail and '**The verdicts.**' in tail and '**The scores.**' in tail and '**The pages.**' in tail \
        and '**Read in mutual light**' in tail and 'strengthens' in tail and '**Next.**' in tail and ED in tail


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


def _mut_ed(S, i, x):
    ed = list(S['ed'])
    if 0 < i <= len(ed):
        ed[i - 1] = ed[i - 1] + x
    return put(S, 'ed', ed)


def _pos(S, k):
    return (S['E'].get('pos') or {}).get(k, 0) if S['E'] else 0


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R215) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b604`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b604' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b605 -- x'])),
    ('G-R215-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R215) END' in S['ferry'] and S['ot'].count('**(R215) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R215) ratified', '(R215) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in (
        ED2 + ' @ c7d3d48f', 'data/b604_sieve_mapping.txt @ 61594b11', 'data/b604_author_answers.txt @ 61594b11', PAGE + ' @ c7d3d48f',
        DIR_PAGE + ' @ c7d3d48f', 'SIDEExplicitFormula/Keiper.lean @ 914c4137', 'SIDEExplicitFormula/KeiperSign.lean @ 914c4137',
        'SIDEExplicitFormula/DetectionRegion.lean @ 1d5d4dd9', 'OPEN_TRAILS.md @ c7d3d48f', 'FINDINGS.md @ c7d3d48f',
        'data/b604_closing_push_out.txt @ 61594b11', ':11864 ', ':12440 ', ':7060 ', 'theorem liCoeff_one_pos', 'theorem liCoeff_one_keiper'))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ANSWERS-BANKED', 'the act`s answers bank: no prompt put, said so', lambda S: S['answers'].startswith('### b605 -- THE AUTHOR`S ANSWERS, 0 prompt(s)')
     and '### NONE: no prompt was put to the author in this act' in S['answers'] and S['answers'].count('### PROMPT ') == 0,
     lambda S: put(S, 'answers', S['answers'].replace('### b605 -- THE AUTHOR', '### b6O5 -- THE AUTHOR', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay 61594b11`s files', lambda S: S['pushout'][0] == ['data/b604_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/b604_closing_push_out.txt', 'x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b604') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b604'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'family-b603': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80 and every PLACE-papers read at ba5f0ea, run afresh through the test`s control()',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(S['ctl'][0], ok=False)] + S['ctl'][1:])),
    ('G-INSTRUMENTS-UNEDITED', 'b604`s sealed suite, record tool and rows, the control`s test file, the generator, its arm, the E0 rule, the push gate, the scanner and the sentence counter against 3651a663',
     lambda S: all(bool(a) and a == b for a, b in S['inst'].values()) and len(S['inst']) == 10,
     lambda S: put(S, 'inst', dict(S['inst'], **{'b604_rows.py': (S['inst']['b604_rows.py'][0], (S['inst']['b604_rows.py'][1] or b'') + b'x')}))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b604`s weight addressed to its entry, H28b`s reading accepted at (R215)(3)', lambda S: weight_ok(S),
     lambda S: put(S, 'find', S['find'].replace('accepted at `(R215)`(3)', 'accepted'))),
    ('G-CORRECTION-LINE', 'FINDINGS at the banked line: the navigator`s mis-specification, the seat`s application recorded as correct', lambda S: correction_ok(S),
     lambda S: put(S, 'find', S['find'].replace('recorded as correct', 'recorded'))),
    ('G-H28B-CLAUSE', 'OPEN_TRAILS at the banked line: the H28b clause for a reorganising edition, addressed to :11864', lambda S: h28b_clause_ok(S),
     lambda S: put(S, 'ot', S['ot'].replace('the diff bank lists each with its destination', 'the diff bank lists each'))),
    ('G-VERDICTS-BANKED', 'the verdict bank and its json against the edition`s: banked first, every row old -> new with its reason on its line', lambda S: verdicts_banked(S),
     lambda S: put(S, 'VB', dict(S['VB'], at='9999'))),
    ('G-FACE-GROUP', 'the FACE group under its heading, the clause`s verdict stated once, every FACE row inside it', lambda S: face_group_ok(S),
     lambda S: put(S, 'ed', [l.replace('stated once: BRIGHT, by test 2', 'stated: BRIGHT') for l in S['ed']])),
    ('G-H39A-SCORED', 'H39a recomputed from the verdicts data, the bank, the scores, the desk', lambda S: h39_ok(S, 'H39a'),
     lambda S: put(S, 'sc', dict(S['sc'], H39a=['x', '']))),
    ('G-H39B-SCORED', 'H39b recomputed from the verdicts data, the bank, the scores, the desk', lambda S: h39_ok(S, 'H39b'),
     lambda S: put(S, 'sc', dict(S['sc'], H39b=['x', '']))),
    ('G-H39C-SCORED', 'H39c recomputed from the verdicts data, the bank, the scores, the desk', lambda S: h39_ok(S, 'H39c'),
     lambda S: put(S, 'vtxt', S['vtxt'].replace('### ### **H39c', '### ### **H39x'))),
    ('G-H39D-SCORED', 'H39d recomputed from the verdicts data, the bank, the scores, the desk', lambda S: h39_ok(S, 'H39d'),
     lambda S: put(S, 'VB', dict(S['VB'], scores=dict(S['VB'].get('scores') or {}, H39d=['x', ''])))),
    ('G-V02-UNEDITED', 'v0.2 on disk and at HEAD against c7d3d48', lambda S: unedited3(S['v2']),
     lambda S: put(S, 'v2', (S['v2'][0] + b'x', S['v2'][1], S['v2'][2]))),
    ('G-CURRENT-UNEDITED', 'the current version on disk and at HEAD against c7d3d48', lambda S: unedited3(S['cur']),
     lambda S: put(S, 'cur', (S['cur'][0] + b'x', S['cur'][1], S['cur'][2]))),
    ('G-EDITION-CARRIES', 'the edition at its banked sha: every non-blank v0.2 line carried, re-pinned or rewritten with its old wording recorded', lambda S: ed_carries(S),
     lambda S: _mut_ed(S, (S['E'].get('where') or {}).get('13', 0) if S['E'] else 0, ' x')),
    ('G-ROWS', 'the edition`s rows against the rows and verdicts data: every row on its banked line, written from the data, 84 in the body', lambda S: rows_ok(S),
     lambda S: _mut_ed(S, ((S['E'].get('pos') or {}).get('rows') or {}).get('RH-13', 0), 'x')),
    ('G-HEAD-RESTATED', 'the head: the version line above the previous, the verdict bullet, the routes sentence, test 1`s scope, the counts', lambda S: head_ok(S),
     lambda S: put(S, 'ed', [l.replace('The five tests are tests of routes', 'The five tests') for l in S['ed']])),
    ('G-BENCH-UNCHANGED', 'the bench section against v0.2`s, byte for byte', lambda S: bench_ok(S),
     lambda S: put(S, 'ed', [l.replace('What it would refute', 'What it would show') for l in S['ed']])),
    ('G-DATED-UNCHANGED', 'every history block beneath a table against v0.2`s, byte for byte', lambda S: dated_ok(S),
     lambda S: put(S, 'ed', [l for l in S['ed'] if l != S['R4'].HIST_CLOSE])),
    ('G-MUTUAL-LIGHT', 'one mutual-light line per cluster carrying rows: three restated, two carried', lambda S: mutual_ok(S),
     lambda S: _mut_ed(S, ((S['E'].get('pos') or {}).get('mutual') or {}).get('FD', 0), 'x')),
    ('G-BACKMATTER', 'v0.3`s back matter after v0.2`s: its sections in order, no blank Status cell, no unresolved token', lambda S: backmatter_ok(S),
     lambda S: put(S, 'ed', [l.replace('### Re-pins of v0.2', '### Repins') for l in S['ed']])),
    ('G-EDITION-BANK', 'the diff bank: its offset head once, the final sha, the restatement, every changed row, the counts, the landing line', lambda S: ed_bank_ok(S),
     lambda S: put(S, 'bank', S['bank'].replace('THE EDITION LANDS', 'THE EDITION'))),
    ('G-REPIN', 'the re-pin bank against the final file', lambda S: repin_ok(S), lambda S: put(S, 'repin', S['repin'].replace('RE-PIN : ', 'RE-PIN : 1'))),
    ('G-H28A-SCORED', 'every changed row`s verdict-change line and bank line re-read, the scores, the desk', lambda S: h28a_ok(S),
     lambda S: put(S, 'sc', dict(S['sc'], H28a=['x', '']))),
    ('G-H28B-SCORED', 'the bodies of v0.2 and v0.3 counted afresh, the bound recomputed', lambda S: h28b_ok(S),
     lambda S: put(S, 'E', dict(S['E'], n_body=-1))),
    ('G-H28C-SCORED', 'the scanner run afresh on the edition and the ceiling read afresh on its body', lambda S: h28c_ok(S),
     lambda S: put(S, 'scan_now', S['scan_now'].replace('CLEAN', 'NOT CLEAN'))),
    ('G-EDITION-COMMITTED-ALONE', 'PLACE-papers` log since c7d3d48: the edition in one commit of its own, on disk as committed', lambda S: edition_alone(S),
     lambda S: put(S, 'pp_files', {h: (f + ['FINDINGS.md'] if ED in f else f) for h, f in S['pp_files'].items()})),
    ('G-PAGES-CHANGED', 'both pages at HEAD and their banks: re-emitted from their probes, changed, the edition in their Placement', lambda S: pages_changed(S),
     lambda S: put(S, 'PX', dict(S['PX'], changed=False))),
    ('G-PAGES-COMMITTED-ALONE', 'PLACE-papers` log since c7d3d48: each changed page in one commit of its own, after the edition`s', lambda S: pages_alone(S),
     lambda S: put(S, 'pp_files', {h: (f + ['FINDINGS.md'] if DIR_PAGE in f else f) for h, f in S['pp_files'].items()})),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b602`s list and v0.20 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b603`s list and v0.21 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank after the page commits: both page arms and the frozen control', lambda S: 'PAGE ARMS PASSING : 2 of 2' in S['arms_c2']
     and ('%s PASSING : 2 of 2' % CONTROL_ARM) in S['arms_c2'], lambda S: put(S, 'arms_c2', S['arms_c2'].replace('PASSING : 2 of 2', 'PASSING : 1 of 2'))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD,
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and 'FACE group' in trail(S) and 'decided by test 2' in trail(S) and 'KeiperSign.lean' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('Resolved by the seat, for the author’s strike', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b606, CP-8' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b606, CP-8', 'x'))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, lv`s HEAD and status, the explicit-formula checkout on main and clean with no new tag, the trial branch',
     lambda S: all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['kcur'] == 'main' and S['kdirty'] == ''
     and 'v0.21' in S['ktags'] and 'v0.22' not in S['ktags'] and S['trial'] == 'f22ff35' and S['lv_head'].startswith('2f71068a')
     and S['lv_dirty'] == '', lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-kernel': '0'}))),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('36352a0', '36352a0', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b605_record.py'): S['tooltext'].get(os.path.join(T, 'b605_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                              if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces'][1] and S['faces'][0] == S['faces'][1],
     lambda S: put(S, 'faces', (S['faces'][0] + b'x', S['faces'][1]))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-REGISTRY-UNTOUCHED', 'REGISTRY.md and SPIRAL_MAP.md against their pre-act blobs', lambda S: S['registry'][1] and S['registry'][0] == S['registry'][1]
     and S['spiral'][1] and S['spiral'][0] == S['spiral'][1], lambda S: put(S, 'spiral', (S['spiral'][0] + b'x', S['spiral'][1]))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md against its pre-act blob', lambda S: S['errata'][1] and S['errata'][0] == S['errata'][1],
     lambda S: put(S, 'errata', (S['errata'][0] + b'x', S['errata'][1]))),
    ('G-KEYSTONES-SCOPE', 'PLACE-papers` phase, day1 and outputs paths, tracked and untracked: the edition file alone', lambda S: S['keystone_changes'] == [ED],
     lambda S: put(S, 'keystone_changes', [ED, ED2])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 3651a663, by blob id', lambda S: S['prior_bad'] == []
     and S['prior_n'] > 6000, lambda S: put(S, 'prior_bad', ['data/b604_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == sorted(
        ['FINDINGS.md', 'OPEN_TRAILS.md', ED] + [p for p, z in ((PAGE, S['PZ']), (DIR_PAGE, S['PX'])) if z.get('changed')]),
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
                                                                          and "startswith('b605')" in S['suite'] and "data/b605_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b605')", ''))),
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
    rec('b605 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('PRE-SEAL (R202)(3)' if PRERUN else 'POST-PUSH' if pushed else 'PRE-PUSH'))
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
        out = os.path.join(D, 'b605_arms_prerun.txt')
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b605_checks_postpush.txt' if pushed else 'b605_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    if not (RERUN or PRERUN):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b605_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
