# -*- coding: utf-8 -*-
"""b599_checks.py -- THE SUITE OF b599, UNDER (R209): CP-7 ACTS EIGHTEEN AND NINETEEN, THE EDITIONS OF SILENCE_STAGES_DEALIGNMENT
AND REPARAMETERIZATION_BARRIERS FROM THEIR b598 BANKS; THE SILENCE PRINCIPLE ALIAS; b394's ERRATUM.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>` or `--prerun`; it writes data/b599_checks.txt before the push and
### data/b599_checks_postpush.txt after it. ### `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the
### face is sealed, no table regenerated, its counts written to data/b599_arms_prerun.txt and nothing else.
### ### The harness is b568's to b598's, carried; the arms are b599's. The control arm is the frozen one of (R207)(2).
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
FACE = os.path.join(D, 'b599_registration_2026-10-02.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
ORDER = ('SILENCE', 'REPARAM')
PRE = dict(relay='32fdac16', pp='fcb498e', gs='3528bcf')
PRE_HEADS = {'SIDE-explicit-formula': '5a1630b8', 'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b'}
STEPZERO = '9da1209d'
ALIAS_C = 'd3f32506'
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/11d35e08-0b91-42db-86b9-9969753496cd/scratchpad'


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b599')
            and 'data/b599_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    import b599_record as REC
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b599_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b599_') and f.endswith('.py'))
    S = dict(
        REC=REC, face=face, ferry=rd('b599_ferry.txt'), scan=rd('b599_ferry_scan.txt'), cens=rd('b599_census_stepzero.txt'),
        fcens=rd('b599_faces_census_stepzero.txt'), pins0=rd('b599_pins_stepzero.txt'), procs=rd('b599_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b598_closing.txt'), reads=rd('b599_reads.txt'), branches=rd('b599_branches.txt'), answers=rd('b599_author_answers.txt'),
        prerun=rd('b599_arms_prerun.txt'), alias=rd('b599_alias_rerun.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        alias_c=(files_of(ROOT, ALIAS_C), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', ALIAS_C, 'HEAD']).returncode == 0,
                 gs(ROOT, 'log', '-1', '--pretty=%s', ALIAS_C), cr0(blob(ROOT, PRE['relay'] + ':tools/b558_record.py')),
                 cr0(blob(ROOT, ALIAS_C + ':tools/b558_record.py')), cr0(raw(os.path.join(T, 'b558_record.py')))),
        suite598=(cr0(blob(ROOT, PRE['relay'] + ':tools/b598_checks.py')), cr0(raw(os.path.join(T, 'b598_checks.py')))),
        testsrc=(cr0(blob(ROOT, PRE['relay'] + ':tools/test_chain_page_b596.py')), cr0(raw(os.path.join(T, 'test_chain_page_b596.py')))),
        gen_same=(cr0(blob(ROOT, PRE['relay'] + ':tools/chain_page.py')), cr0(raw(os.path.join(T, 'chain_page.py')))),
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')), errata=read(os.path.join(PP, 'ERRATA.md')),
        readme=(cr0(raw(os.path.join(PP, 'README.md'))), cr0(blob(PP, PRE['pp'] + ':README.md'))),
        registry=(cr0(raw(os.path.join(PP, 'REGISTRY.md'))), cr0(blob(PP, PRE['pp'] + ':REGISTRY.md'))),
        faces=(cr0(raw(os.path.join(PP, 'FACES_LEDGER.md'))), cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md'))),
        cur={k: (cr0(raw(os.path.join(PP, REC.DOC[k]['cur']))), cr0(blob(PP, PRE['pp'] + ':' + REC.DOC[k]['cur'])), cr0(blob(PP, 'HEAD:' + REC.DOC[k]['cur'])))
             for k in ORDER},
        pages={p: (cr0(raw(os.path.join(PP, p))), cr0(blob(PP, PRE['pp'] + ':' + p)), cr0(blob(PP, 'HEAD:' + p))) for p in (PAGE, DIR_PAGE)},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        er_pre=cr0(blob(PP, PRE['pp'] + ':ERRATA.md')), er_now=cr0(raw(os.path.join(PP, 'ERRATA.md'))),
        corr_pre=cr0(blob(GS, PRE['gs'] + ':CORRESPONDENCE.md')), corr_now=cr0(raw(os.path.join(GS, 'CORRESPONDENCE.md'))),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain', '--untracked-files=no'),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b598*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b599_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b599_mustnotexist.txt')), table_changed=None,
        fj=jl('b599_findings.json'), tj=jl('b599_trail.json'), sc=jl('b599_scores.json'), desk=rd('b599_desk_notes.txt'),
        wl1=jl('b599_weight_line.json'), er=jl('b599_erratum.json'), wo=jl('b599_work_order.json'),
        PZ=jl('b599_page_zeta.json'), PX=jl('b599_page_chi.json'), arms_c4=rd('b599_page_arms_c4.txt'),
        E={k: jl('b599_edition_%s.json' % k) for k in ORDER}, H={k: jl('b599_h28_%s.json' % k) for k in ORDER},
        bank={k: rd(REC.DOC[k]['diffbank']) for k in ORDER}, termscan={k: rd(REC.DOC[k]['termscan']) for k in ORDER},
        repin={k: rd(REC.DOC[k]['repin']) for k in ORDER},
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
    S.update(extra_sources(S))
    return S


def extra_sources(S):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import b598_record as R8
    REC = S['REC']
    X = {}
    X['gcp_zeta'] = GCP.arm(os.path.join(D, 'b596_nodes_faces.txt'), os.path.join(SP, '_b599_gcp'), os.path.join(D, 'b596_probe_out.txt'))
    X['gcp_chi'] = GCP.arm(os.path.join(D, 'b596_nodes_chi.txt'), os.path.join(SP, '_b599_gcp'), os.path.join(D, 'b596_chi_probe_out.txt'))
    X['ctl'] = TC.control()
    X['ctl_arm'] = TC.ARM
    rows, _second, _txt = R8.rows_of('SILENCE')
    X['alias_live'] = sorted((r['line'], r['sentence']) for r in rows if 'Silence Principle' in r['by'])
    X['second598'] = sorted((x['line'], x['sentence']) for x in jl('b598_bank_SILENCE.json').get('second', []))
    X['ed'], X['ed_head'], X['scan_now'] = {}, {}, {}
    for k in ORDER:
        p = REC.DOC[k]['ed']
        X['ed_head'][k] = cr0(blob(PP, 'HEAD:' + p))
        X['ed'][k] = lines_of(X['ed_head'][k]) if X['ed_head'][k] else []
        r = subprocess.run([sys.executable, os.path.join(T, 'banned_terms.py'), '--new', os.path.join(PP, *p.split('/'))], capture_output=True, text=True,
                           encoding='utf-8', errors='replace') if os.path.exists(os.path.join(PP, *p.split('/'))) else None
        X['scan_now'][k] = r.stdout if r else ''
    return X


# ### the act's own predicates
def E_(S, k, n):
    return S['REC']._edl(k, n)


def eline(S, k, n):
    ed = S['ed'][k]
    i = E_(S, k, n)
    return ed[i - 1] if ed and 0 < i <= len(ed) else ''


def cur_unedited(S):
    return all(bool(b) and a == b == c for a, b, c in S['cur'].values())


def ed_carries(S, k):
    REC = S['REC']
    ed, cur = S['ed'][k], lines_of(S['cur'][k][1])
    changed = set(x[0] for x in REC._all_changes(k))
    if not ed or REC._bm_tag(k) not in ed:
        return False
    return all(ed[E_(S, k, n) - 1] == cur[n - 1] for n in range(1, len(cur) + 1) if n not in changed) \
        and all(ed[E_(S, k, n) - 1] != cur[n - 1] for n in changed) and S['E'][k].get('sha256') == hashlib.sha256(S['ed_head'][k]).hexdigest()


def moved_row(S):
    l = eline(S, 'SILENCE', 209)
    rows = [r for r in jl('b598_bank_SILENCE.json').get('rows', []) if r['verdict'] == 'MOVED-IN-MEANING']
    return len(rows) == 1 and rows[0]['line'] == 209 and l.startswith('| The single-error syndrome condition') \
        and '`Function.Injective H ∧ ∀ i : Fin 7, H i ≠ 0`' in l and 'Knill–Laflamme error-correction conditions' in l and 'not compiled' in l \
        and '| `knill_laflamme_t1` |' in l and '`SteaneExemplar.knill_laflamme_t1`' not in l and '`SIDECosmo/SteaneExemplar.lean` :72-:75' in l and '(`c5cba30`)' in l


def names_ok(S):
    REC, k = S['REC'], 'SILENCE'
    cur = lines_of(S['cur'][k][1])
    if not S['ed'][k]:
        return False
    named = [(n, s) for n in sorted(REC.DOC[k]['NAMES']) for s in REC._segs(cur[n - 1]) if 'Silence Principle' in s]
    carried = all(s in REC._segs(eline(S, k, n)) for n, s in named)
    h = S['E'][k].get('hist_at', {}).get('21')
    hl = S['ed'][k][h - 1] if h else ''
    return len(named) == 5 and carried and h == E_(S, k, 21) + 2 and '`phase1.5/structural/SILENCE_FORMAL.md` :43' in hl \
        and all((':%d' % E_(S, k, n)) in hl for n in (121, 144, 162)) and '`silence_universal`' in hl and '`667c254`' in hl


def defs_ok(S):
    a, b = eline(S, 'SILENCE', 210), eline(S, 'SILENCE', 211)
    return '`SIDEStructuralErrorCorrection.d_eff_formula`' in a and '(`6a4f482`)' in a and 'T2, definitional' in a and 'no printed profile' in a \
        and '`SIDEStructuralErrorCorrection.silence_yields_protection`' in b and '(`6a4f482`)' in b and 'T2, definitional' in b \
        and '— no terminal |' not in a + b and 'none (manuscript)' not in a + b


def facts_ok(S):
    REC = S['REC']
    for k in ORDER:
        for ln, old, rep, _w in REC.DOC[k]['FACTS']:
            l = eline(S, k, ln)
            if rep not in l or l.count(old) > rep.count(old):
                return False
    r219 = eline(S, 'REPARAM', 219)
    return 'CURRENT kernel pin' not in r219 and '`0256e9e`' in r219 and '`e4e8d23b`' in r219 and '`steane_parameters`' in eline(S, 'SILENCE', 208) \
        and 'SteaneExemplar.' not in eline(S, 'SILENCE', 208) and len(REC.DOC['SILENCE']['FACTS']) == S['H']['SILENCE'].get('n_facts') \
        and len(REC.DOC['REPARAM']['FACTS']) == S['H']['REPARAM'].get('n_facts')


def ceilings_ok(S):
    REC = S['REC']
    for k in ORDER:
        for ln, old, rep, _w in REC.DOC[k]['CEILS']:
            l = eline(S, k, ln)
            if rep not in l or l.count(old) > rep.count(old):
                return False
        if len(REC.DOC[k]['CEILS']) != S['H'][k].get('n_ceils') or len([x for x in S['E'][k].get('diff', []) if x['kind'] == 'ceiling']) != len(REC.DOC[k]['CEILS']):
            return False
    return 'We prove' not in eline(S, 'SILENCE', 21) and 'proved' not in eline(S, 'REPARAM', 41) and 'proved' not in eline(S, 'REPARAM', 180)


def no_profile_line(S):
    ed = S['ed']['SILENCE']
    tag = S['REC']._bm_tag('SILENCE')
    if not ed or tag not in ed:
        return False
    bm = NL.join(ed[ed.index(tag):])
    w = S['wo'].get('line')
    return bool(w) and ('`W-ORD-SEC-AXIOM-ARTEFACT` (OPEN_TRAILS :%d)' % w) in bm and 'no printed profile of the kernel’s own' in bm \
        and oline(S, w) == S['wo'].get('head') and S['E']['SILENCE'].get('word_line') == w


def collisions(S):
    REC = S['REC']
    for k in ORDER:
        ed = S['ed'][k]
        tag = REC._bm_tag(k)
        if not ed or tag not in ed:
            return False
        bm = NL.join(ed[ed.index(tag):])
        try:
            sec = bm[bm.index('### Collisions resolved by the precedence order'):bm.index('### History lines')]
        except ValueError:
            return False
        rows = [l for l in sec.split(NL) if re.match(r'^\| :\d+ \| ', l)]
        if not (len(rows) == len(REC.DOC[k]['COLLISIONS']) == len(S['E'][k].get('collisions', [])) and all(('| :%d |' % E_(S, k, c[0])) in sec for c in REC.DOC[k]['COLLISIONS'])):
            return False
    return True


def history_lines(S):
    REC, k = S['REC'], 'SILENCE'
    ed, at = S['ed'][k], S['E'][k].get('hist_at', {})
    if not ed or sorted(at) != ['21', '282']:
        return False
    return all(ed[at[a] - 1] == REC._hist_text(k, int(a)) and ed[at[a] - 2] == '' for a in at) and at['21'] == E_(S, k, 21) + 2 \
        and at['282'] == E_(S, k, 282) + 2 and S['E']['REPARAM'].get('hist_at') == {}


def version_lines(S):
    REC = S['REC']
    s, r = S['ed']['SILENCE'], S['ed']['REPARAM']
    return bool(s) and bool(r) and s[14] == REC.DOC['SILENCE']['VERSION'] and s[15] == '' and s[16] == '**v1.2, 2026-07-29** (retitle per the title law; was v1.1)' \
        and r[5] == REC.DOC['REPARAM']['VERSION'] and r[6] == '**v0.1 — 2026-08-04 — DRAFT**'


def backmatter(S):
    REC = S['REC']
    heads = ['### Removals', '### Rewrites -- the work-list', '### Ceiling corrections', '### Fact corrections', '### Restatement rewrites',
             '### Collisions resolved by the precedence order', '### History lines', '### Names excepted', '### Stem corrections',
             '### Ceiling-shaped sentences read and carried', '### Sentences read and left, for the author’s strike', '### The axiom profiles',
             '### The ruling’s readings of `(R209)`', '### Placement', '### Correspondence']
    for k in ORDER:
        ed = S['ed'][k]
        if not ed or REC._bm_tag(k) not in ed:
            return False
        bm = NL.join(ed[ed.index(REC._bm_tag(k)):])
        pos = [bm.find(h) for h in heads]
        if not (all(p >= 0 for p in pos) and pos == sorted(pos) and S['E'][k].get('status_blanks') == [] and '{E:' not in bm):
            return False
    return True


def ed_banks(S):
    REC = S['REC']
    for k in ORDER:
        b = S['bank'][k]
        if not (b.startswith('### OFFSET FROM THE CURRENT VERSION (R190)(3): ' + REC._offset(k)) and '### ### **THE EDITION LANDS: NO SENTENCE HELD.**' in b
                and ('sha256 %s' % S['E'][k].get('sha256', '#')) in b and 'BACK MATTER %d, printed separately' % S['E'][k].get('n_backmatter', -1) in b):
            return False
    return True


def repin_ok(S):
    for k, floor in (('SILENCE', 40), ('REPARAM', 10)):
        m = re.search(r'RE-PIN : (\d+) of (\d+) citations hold', S['repin'][k])
        if not (m and m.group(1) == m.group(2) and int(m.group(2)) > floor and S['E'][k].get('sha256', '#') in S['bank'][k]):
            return False
    return True


def h28a_ok(S):
    for k in ORDER:
        wl = [x for x in S['E'][k].get('diff', []) if x['kind'] == 'work-list']
        want = 'HELD' if all(x['changed'] and x['cites'] for x in wl) else 'REFUTED'
        n = {'SILENCE': 1, 'REPARAM': 0}[k]
        if not (len(wl) == n and S['H'][k].get('H28a') == want and S['sc'].get('H28a_' + k, [''])[0] == want and S['H'][k].get('h28a_vacuous') == (n == 0)):
            return False
    return '(H28A_SILENCE)' in S['desk'] and '(H28A_REPARAM)' in S['desk']


def h28b_ok(S):
    import b558_record as CP
    for k in ORDER:
        ed = S['ed'][k]
        if not ed:
            return False
        body = ed[:ed.index(S['REC']._bm_tag(k))]
        while body and body[-1] == '':
            body = body[:-1]
        cur = lines_of(S['cur'][k][1])
        nb = sum(len([s for s in CP.segments(l) if s]) for l in body)
        nc = sum(len([s for s in CP.segments(l) if s]) for l in cur)
        E = S['E'][k]
        allowed = E.get('credit', 0) + E.get('removals', 0) + E.get('ruled_citations', 0) + E.get('version_lines', 0)
        want = 'HELD' if abs(nb - nc) <= allowed else 'REFUTED'
        if not (nb == E.get('n_body') and nc == E.get('n_cur') and S['H'][k].get('H28b') == want and S['sc'].get('H28b_' + k, [''])[0] == want):
            return False
    return True


def h28c_ok(S):
    REC = S['REC']
    for k in ORDER:
        ed = S['ed'][k]
        if not ed:
            return False
        cut = ed.index(REC._bm_tag(k))
        ok_lines = set(E_(S, k, n) for n in REC.DOC[k]['CARRIED']) | set(E_(S, k, x[0]) for x in REC._all_changes(k)) | set(S['E'][k].get('hist_at', {}).values())
        beyond = [i for i, l in enumerate(ed[:cut], 1) for m in REC.CEILING.finditer(l) if i not in ok_lines]
        sn = S['scan_now'][k]
        clean = re.search(r'^\s*VERDICT\s*: CLEAN\s*$', sn, re.M) is not None and re.search(r'live uses\s*:\s*0\b', sn) is not None
        want = 'HELD' if clean and not beyond else 'REFUTED'
        if not (S['H'][k].get('H28c') == want and S['sc'].get('H28c_' + k, [''])[0] == want and sn.strip() == S['termscan'][k].strip()):
            return False
    return True


def editions_alone(S):
    REC = S['REC']
    log = S['pp_log']
    for k in ORDER:
        c = [h for h, s_ in log if S['pp_files'][h] == [REC.DOC[k]['ed']]]
        if len(c) != 1 or not dict(log)[c[0]].startswith('b599 (R209)(4)'):
            return False
        if any(REC.DOC[k]['ed'] in f for h, f in S['pp_files'].items() if h != c[0]):
            return False
    return True


def erratum_ok(S):
    er, REC = S['er'], S['REC']
    t = S['errata']
    head_ok = t.count(REC.ERR_ID) >= 1 and len(re.findall(r'^## ' + re.escape(REC.ERR_ID) + r' ', t, re.M)) == 1
    el = er.get('errata_line')
    ls = t.split(NL)
    at = ls[el - 1] if el and 0 < el <= len(ls) else ''
    ol = oline(S, er.get('ot_line'))
    return head_ok and at == REC.ERR_HEAD and 'OPEN_TRAILS :4540' in t and '`4cd1cd2`' in t and ':202-:211' in t and ol.startswith(er.get('ot_head', '#')) \
        and 'addressed to :4540' in ol and REC.ERR_ID in ol and ('ERRATA :%s' % el) in ol and er.get('addressed') == 4540 and er.get('ot_line', 0) > 12326


def erratum_alone(S):
    c = [h for h, s_ in S['pp_log'] if 'ERRATA.md' in S['pp_files'][h]]
    return len(c) == 1 and S['pp_files'][c[0]] == ['ERRATA.md', 'OPEN_TRAILS.md'] and dict(S['pp_log'])[c[0]].startswith('b599 (R209)(2)(ii)')


def weight_ok(S):
    ls = S['wl1'].get('lines', [])
    if len(ls) != 2:
        return False
    a, b = fline(S, ls[0]['line']), fline(S, ls[1]['line'])
    return a.startswith(ls[0]['head']) and '(:6902)' in a and 'b598 AT ITS WEIGHT' in a and '16919d87' in a and '697eb1ed' in a \
        and b.startswith(ls[1]['head']) and 'THE ITEMS, AS RULED' in b and 'd3f32506' in b and ls[0]['line'] < ls[1]['line']


def work_order_ok(S):
    w = S['wo']
    t = S['ot']
    i = t.find(w.get('head', '#'))
    seg = t[i:i + 1400] if i >= 0 else ''
    return oline(S, w.get('line')) == w.get('head') and 'W-ORD-SEC-AXIOM-ARTEFACT' in w.get('head', '') and '**Items.**' in seg \
        and '**Price:** one kernel housekeeping commit at the memory hold, one table regeneration' in seg and '**Trigger:** the author’s word' in seg \
        and 'a T2 grade with no printed profile is a grade from recall' in seg


def alias_ok(S):
    files, anc, subj, pre, at, now = S['alias_c']
    if not (files == ['tools/b558_record.py'] and anc and subj.startswith('b599 step zero (R209)(2)(i)') and bool(pre) and at == now):
        return False
    a, b = pre.decode('utf-8').split(NL), at.decode('utf-8').split(NL)
    import difflib
    d = [x for x in difflib.unified_diff(a, b, lineterm='', n=0) if x.startswith(('+', '-')) and not x.startswith(('+++', '---'))]
    minus = [x for x in d if x.startswith('-')]
    plus = [x for x in d if x.startswith('+')]
    return minus == ["-         'conservation_of_spectra': [('Conservation of Spectra', r'Conservation of Spectra')]}"] and len(plus) == 6 \
        and any("'silence_principle': [('Silence Principle', r'Silence Principle')]}" in x for x in plus) \
        and any('SILENCE_HOME' in x and 'SILENCE_FORMAL.md' in x for x in plus)


def alias_hits(S):
    return len(S['alias_live']) == 5 and S['alias_live'] == S['second598'] and 'ALIAS HITS ON SILENCE_STAGES_DEALIGNMENT : 5.' in S['alias'] \
        and 'the same lines: True' in S['alias'] and 'phase1.5/structural/SILENCE_FORMAL.md :43' in S['alias']


def pages_unchanged(S):
    return all(bool(b) and a == b == c for a, b, c in S['pages'].values()) and S['PZ'].get('changed') is False and S['PX'].get('changed') is False \
        and S['PZ'].get('rc') == 0 and S['PX'].get('rc') == 0 and not [h for h, f in S['pp_files'].items() if PAGE in f or DIR_PAGE in f]


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


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    tail = NL.join(ls[e - 1:e + 18]) if e else ''
    return bool(e) and fline(S, e) == S['REC'].TITLE and '**The editions**' in tail and '**Read in mutual light**' in tail \
        and all(S['REC'].DOC[k]['ed'] in tail and ('sha256 `%s`' % S['E'][k].get('sha256', '#')) in tail for k in ORDER) \
        and 'FINDINGS :6902' in tail and 'strengthen' in tail and S['REC'].ERR_ID in tail


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


def _ed_mut(S, k, a, b):
    return put(S, 'ed', dict(S['ed'], **{k: [x.replace(a, b) for x in S['ed'][k]]}))


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R209) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-REG-LOCKED-FIRST', 'the lock time against the step-zero and alias commits and every later commit', lambda S: S['lock_epoch'] is not None
     and all(any(l.startswith(c) and int(l.split()[1]) < S['lock_epoch'] for l in S['before_lock']) for c in (STEPZERO, ALIAS_C))
     and all(int(l.split()[1]) > S['lock_epoch'] for l in S['before_lock'] if not l.startswith((STEPZERO, ALIAS_C))), lambda S: put(S, 'lock_epoch', 1)),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8', 'PASSING : 7'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b598`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b598' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [ALIAS_C, STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b599 -- x'])),
    ('G-R209-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R209) END' in S['ferry'] and S['ot'].count('**(R209) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R209) ratified', '(R209) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in (
        'data/b558_editions/SILENCE_STAGES_DEALIGNMENT.txt @ 16919d87', 'data/b558_editions/REPARAMETERIZATION_BARRIERS_v0_1.txt @ 697eb1ed',
        'phase2/quantum/SILENCE_STAGES_DEALIGNMENT.md @ fcb498e', 'phase2/method/REPARAMETERIZATION_BARRIERS_v0_1.md @ fcb498e',
        'phase1.5/structural/SILENCE_FORMAL.md @ fcb498e', 'OPEN_TRAILS.md @ fcb498e', 'ERRATA.md @ fcb498e', 'phase2/quantum/SILENCE_STAGES_DEALIGNMENT.md @ 4cd1cd2',
        'tools/b558_record.py @ d3f32506', 'SIDEStructuralErrorCorrection/DeAlignment.lean @', 'SIDECosmo/SteaneExemplar.lean @',
        'data/b598_closing_push_out.txt @', '"Silence Principle" by name across PLACE-papers', 'opens a namespace at c5cba30: False',
        'rows :202-:211 10'))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ANSWERS-BANKED', 'the act`s answers bank: one prompt, question, options and recommended mark verbatim, the result',
     lambda S: S['answers'].count('### PROMPT ') == 1 and S['answers'].count('\n  OPTION ') == 3 and S['answers'].count('[RECOMMENDED]') == 1
     and S['answers'].count('\nRESULT ') == 1 and '="option 1. Append at the end' in S['answers'],
     lambda S: put(S, 'answers', S['answers'].replace('[RECOMMENDED]', '', 1))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay 9da1209d`s files', lambda S: S['pushout'][0] == ['data/b598_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/b598_closing_push_out.txt', 'x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b598') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b598'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'simplicity-b596': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80 and every PLACE-papers read at ba5f0ea, run afresh through the test`s control()',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(S['ctl'][0], ok=False)] + S['ctl'][1:])),
    ('G-ALIAS-ALONE', 'relay d3f32506`s files and subject, and b558_record.py against 32fdac16: the alias and its home, nothing else',
     lambda S: alias_ok(S), lambda S: put(S, 'alias_c', (S['alias_c'][0] + ['tools/x.py'],) + S['alias_c'][1:])),
    ('G-ALIAS-HITS', 'b558`s matcher re-run afresh on SILENCE_STAGES at fcb498e against b598`s second shape and the step-zero bank',
     lambda S: alias_hits(S), lambda S: put(S, 'alias_live', S['alias_live'][:4])),
    ('G-INSTRUMENTS-UNEDITED', 'b598`s sealed suite, the control`s test file and the generator on disk against 32fdac16',
     lambda S: bool(S['suite598'][0]) and S['suite598'][0] == S['suite598'][1] and bool(S['testsrc'][0]) and S['testsrc'][0] == S['testsrc'][1]
     and bool(S['gen_same'][0]) and S['gen_same'][0] == S['gen_same'][1], lambda S: put(S, 'suite598', (S['suite598'][0], S['suite598'][1] + b'x'))),
    ('G-WEIGHT-LINES', 'FINDINGS at the two banked lines: b598`s weight and the items as ruled', lambda S: weight_ok(S),
     lambda S: put(S, 'wl1', dict(S['wl1'], lines=S['wl1'].get('lines', [])[:1]))),
    ('G-ERRATUM', 'ERRATA at the banked entry and OPEN_TRAILS at the history line addressed to :4540', lambda S: erratum_ok(S),
     lambda S: put(S, 'er', dict(S['er'], addressed=4541))),
    ('G-ERRATUM-COMMITTED-ALONE', 'PLACE-papers` log since fcb498e: ERRATA and its history line in one commit, alone', lambda S: erratum_alone(S),
     lambda S: put(S, 'pp_files', {h: (f + ['FINDINGS.md'] if 'ERRATA.md' in f else f) for h, f in S['pp_files'].items()})),
    ('G-WORK-ORDER', 'OPEN_TRAILS at W-ORD-SEC-AXIOM-ARTEFACT: items, price, trigger, reason', lambda S: work_order_ok(S),
     lambda S: put(S, 'wo', dict(S['wo'], line=1))),
    ('G-CURRENT-UNEDITED', 'both current versions on disk and at HEAD against fcb498e', lambda S: cur_unedited(S),
     lambda S: put(S, 'cur', dict(S['cur'], REPARAM=(S['cur']['REPARAM'][0] + b'x', S['cur']['REPARAM'][1], S['cur']['REPARAM'][2])))),
    ('G-EDITION-CARRIES-SILENCE', 'the v1.3 edition at HEAD: every v1.2 line at its offset, unchanged unless changed by the form', lambda S: ed_carries(S, 'SILENCE'),
     lambda S: _ed_mut(S, 'SILENCE', 'Four systems. Same architecture.', 'Four systems, one architecture.')),
    ('G-EDITION-CARRIES-REPARAM', 'the v0.2 edition at HEAD: every v0.1 line at its offset, unchanged unless changed by the form', lambda S: ed_carries(S, 'REPARAM'),
     lambda S: _ed_mut(S, 'REPARAM', 'The payoff is targeting.', 'The payoff is aim.')),
    ('G-MOVED-ROW', 'the one MOVED row, §9 :209, against the b598 bank: the syndrome condition, the field`s name kept, the docstring not compiled',
     lambda S: moved_row(S), lambda S: _ed_mut(S, 'SILENCE', ', not compiled | SIDE-cosmo', ' | SIDE-cosmo')),
    ('G-SILENCE-NAMES', 'the five Silence Principle sentences carried, the history line citing the home by path and line', lambda S: names_ok(S),
     lambda S: _ed_mut(S, 'SILENCE', '`phase1.5/structural/SILENCE_FORMAL.md` :43', '`phase1.5/structural/SILENCE_FORMAL.md`')),
    ('G-DEFINITIONAL-ROWS', '§9`s two rows citing d_eff_formula and silence_yields_protection at 6a4f482, T2 as definitional', lambda S: defs_ok(S),
     lambda S: _ed_mut(S, 'SILENCE', 'T2, definitional; the survey', 'T4; the survey')),
    ('G-FACT-CORRECTIONS', 'every fact correction in place in both editions, the old wording gone', lambda S: facts_ok(S),
     lambda S: _ed_mut(S, 'REPARAM', 'at the kernel pin `5e668b4`, current on that date', 'at the CURRENT kernel pin `5e668b4`')),
    ('G-CEILING-CORRECTIONS', 'every ceiling correction in place in both editions, the old wording gone', lambda S: ceilings_ok(S),
     lambda S: _ed_mut(S, 'REPARAM', 'shown by explicit construction', 'proved')),
    ('G-NO-PRINTED-PROFILE', 'SILENCE`s back matter: no printed profile stated, W-ORD-SEC-AXIOM-ARTEFACT named at its OPEN_TRAILS line', lambda S: no_profile_line(S),
     lambda S: put(S, 'wo', dict(S['wo'], line=(S['wo'].get('line') or 0) + 1))),
    ('G-COLLISIONS', 'each back matter`s collision rows against the tool`s lists and the edition jsons', lambda S: collisions(S),
     lambda S: put(S, 'ed', dict(S['ed'], REPARAM=[x for x in S['ed']['REPARAM'] if 'the dated re-verification note of 2026-08-06' not in x]))),
    ('G-HISTORY-LINES', 'the two SILENCE history lines beneath :21 and b557`s table; none in REPARAM', lambda S: history_lines(S),
     lambda S: _ed_mut(S, 'SILENCE', 'staying manuscript-resident.*', 'staying manuscript-resident.')),
    ('G-VERSION-LINES', 'the v1.3 and v0.2 lines above the v1.2 and v0.1 lines', lambda S: version_lines(S),
     lambda S: _ed_mut(S, 'REPARAM', '**v0.2 — 2026-10-02', '**v0.2')),
    ('G-BACKMATTER', 'both back matters` sections in order, no blank Status cell, no unresolved line token', lambda S: backmatter(S),
     lambda S: _ed_mut(S, 'SILENCE', '### The axiom profiles', '### Profiles')),
    ('G-EDITION-BANKS', 'the two diff banks` offset heads, counts and landing lines', lambda S: ed_banks(S),
     lambda S: put(S, 'bank', dict(S['bank'], REPARAM=S['bank']['REPARAM'][5:]))),
    ('G-REPIN', 'the two re-pin banks against the final files', lambda S: repin_ok(S),
     lambda S: put(S, 'repin', dict(S['repin'], SILENCE=S['repin']['SILENCE'].replace('RE-PIN : ', 'RE-PIN : 9', 1)))),
    ('G-H28A-SCORED', 'each edition`s MOVED rows` citations, the scores, the desk', lambda S: h28a_ok(S),
     lambda S: put(S, 'H', dict(S['H'], SILENCE=dict(S['H']['SILENCE'], H28a='REFUTED')))),
    ('G-H28B-SCORED', 'each body and current version counted afresh', lambda S: h28b_ok(S),
     lambda S: put(S, 'E', dict(S['E'], REPARAM=dict(S['E']['REPARAM'], n_body=1)))),
    ('G-H28C-SCORED', 'the scanner run afresh on each edition and the ceiling read afresh', lambda S: h28c_ok(S),
     lambda S: put(S, 'scan_now', dict(S['scan_now'], SILENCE=S['scan_now']['SILENCE'].replace('VERDICT          : CLEAN', 'VERDICT          : NOT CLEAN')))),
    ('G-EDITIONS-COMMITTED-ALONE', 'PLACE-papers` log since fcb498e: each edition file in one commit of its own', lambda S: editions_alone(S),
     lambda S: put(S, 'pp_files', {h: (f + ['FINDINGS.md'] if f == [S['REC'].DOC['REPARAM']['ed']] else f) for h, f in S['pp_files'].items()})),
    ('G-PAGES-UNCHANGED', 'both pages on disk and at HEAD against fcb498e, the re-emits unchanged, no page commit', lambda S: pages_unchanged(S),
     lambda S: put(S, 'PZ', dict(S['PZ'], changed=True))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b596`s faces list and v0.17 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b596`s χ list and v0.17 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-PAGE-ARMS-COUNTED', 'the page-arm bank after the two edition commits: both page arms and the frozen control', lambda S: 'PAGE ARMS PASSING : 2 of 2' in S['arms_c4']
     and ('%s PASSING : 2 of 2' % CONTROL_ARM) in S['arms_c4'], lambda S: put(S, 'arms_c4', S['arms_c4'].replace('PASSING : 2 of 2', 'PASSING : 1 of 2'))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD,
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record', lambda S: 'Resolved by the seat under the precedence order, for the author’s strike' in trail(S)
     and 'Recorded as the navigator’s' in trail(S) and 'beneath :4540' in trail(S), lambda S: put(S, 'ot', S['ot'].replace('Recorded as the navigator’s', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b600, REMAINDER 5 -- the product lemma' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b600, REMAINDER 5 -- the product lemma', 'x'))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, the explicit-formula checkout, the trial branch',
     lambda S: all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['kcur'] == 'main' and S['kdirty'] == ''
     and S['trial'] == 'f22ff35', lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-structural-error-correction': '0'}))),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('36352a0', '36352a0', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b599_record.py'): S['tooltext'].get(os.path.join(T, 'b599_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                              if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces'][1] and S['faces'][0] == S['faces'][1],
     lambda S: put(S, 'faces', (S['faces'][0] + b'x', S['faces'][1]))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-REGISTRY-UNTOUCHED', 'REGISTRY.md against its pre-act blob', lambda S: S['registry'][1] and S['registry'][0] == S['registry'][1],
     lambda S: put(S, 'registry', (S['registry'][0] + b'x', S['registry'][1]))),
    ('G-KEYSTONES-SCOPE', 'PLACE-papers` phase, day1 and outputs paths, tracked and untracked', lambda S: S['keystone_changes'] == sorted(S['REC'].DOC[k]['ed'] for k in ORDER),
     lambda S: put(S, 'keystone_changes', S['keystone_changes'] + [S['REC'].DOC['SILENCE']['cur']])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 32fdac16, by blob id', lambda S: S['prior_bad'] == []
     and S['prior_n'] > 6000, lambda S: put(S, 'prior_bad', ['data/b598_closing.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == sorted(
        ['ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md'] + [S['REC'].DOC[k]['ed'] for k in ORDER]),
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + [PAGE]))),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-ERRATA-APPEND-ONLY', 'ERRATA -- its pre-act blob a true prefix', lambda S: S['er_pre'] and S['er_now'] is not None
     and S['er_now'].startswith(S['er_pre']) and len(S['er_now']) > len(S['er_pre']), lambda S: put(S, 'er_now', b'x' + (S['er_now'] or b''))),
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
                                                                          and "startswith('b599')" in S['suite'] and "data/b599_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b599')", ''))),
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
    rec('b599 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('PRE-SEAL (R202)(3)' if PRERUN else 'POST-PUSH' if pushed else 'PRE-PUSH'))
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
        out = os.path.join(D, 'b599_arms_prerun.txt')
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b599_checks_postpush.txt' if pushed else 'b599_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    if not (RERUN or PRERUN):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b599_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
