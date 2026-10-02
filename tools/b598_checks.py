# -*- coding: utf-8 -*-
"""b598_checks.py -- THE SUITE OF b598, UNDER (R208): CP-1b, THE TIER BLOCKS AND WORK-LISTS OF SILENCE_STAGES_DEALIGNMENT AND
REPARAMETERIZATION BY THE b558 FORM.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). The suite regenerates the terminal table (R107)
### unless `--rerun-postpush <name>` or `--prerun`; it writes data/b598_checks.txt before the push and
### data/b598_checks_postpush.txt after it. ### `--prerun` (the standing line of (R202)(3)): every arm run at HEAD BEFORE the
### face is sealed, no table regenerated, its counts written to data/b598_arms_prerun.txt and nothing else.
### ### The harness is b568's to b597's, carried; the arms are b598's. The frozen control is b597's, read through the test file's
### control() (relay tools/test_chain_page_b596.py, as repaired at 276a7698), unedited.
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
FACE = os.path.join(D, 'b598_registration_2026-10-02.txt')
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
DOCP = {'SILENCE': 'phase2/quantum/SILENCE_STAGES_DEALIGNMENT.md', 'REPARAM': 'phase2/method/REPARAMETERIZATION_BARRIERS_v0_1.md'}
BANKF = {'SILENCE': 'data/b558_editions/SILENCE_STAGES_DEALIGNMENT.txt', 'REPARAM': 'data/b558_editions/REPARAMETERIZATION_BARRIERS_v0_1.txt'}
NTERMS = {'SILENCE': 9, 'REPARAM': 2}
PRE = dict(relay='022d2bf0', pp='eb9b057', gs='3528bcf')
PRE_HEADS = {'SIDE-explicit-formula': '5a1630b8', 'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b'}
STEPZERO = 'cab56f31'
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']
RERUN = '--rerun-postpush' in sys.argv
PRERUN = '--prerun' in sys.argv
L = []
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/c36c4b1c-6feb-4e3e-9e2c-aeb65eff6769/scratchpad'


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b598')
            and 'data/b598_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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


def sources():
    import b598_record as REC
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b598_lockgate_notes*.txt')))
    lock_epoch = utc_epoch(face, 'locked at (UTC)')
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b598_') and f.endswith('.py'))
    S = dict(
        REC=REC, face=face, ferry=rd('b598_ferry.txt'), scan=rd('b598_ferry_scan.txt'), cens=rd('b598_census_stepzero.txt'),
        fcens=rd('b598_faces_census_stepzero.txt'), pins0=rd('b598_pins_stepzero.txt'), procs=rd('b598_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=lock_epoch,
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b597_closing.txt'), reads=rd('b598_reads.txt'), branches=rd('b598_branches.txt'), answers=rd('b598_author_answers.txt'),
        prerun=rd('b598_arms_prerun.txt'),
        before_lock=[l for l in gs(ROOT, 'log', '--pretty=%H %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        suite597=(cr0(blob(ROOT, PRE['relay'] + ':tools/b597_checks.py')), cr0(raw(os.path.join(T, 'b597_checks.py')))),
        testsrc=(cr0(blob(ROOT, PRE['relay'] + ':tools/test_chain_page_b596.py')), cr0(raw(os.path.join(T, 'test_chain_page_b596.py')))),
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        readme=(cr0(raw(os.path.join(PP, 'README.md'))), cr0(blob(PP, PRE['pp'] + ':README.md'))),
        registry=(cr0(raw(os.path.join(PP, 'REGISTRY.md'))), cr0(blob(PP, PRE['pp'] + ':REGISTRY.md'))),
        faces=(cr0(raw(os.path.join(PP, 'FACES_LEDGER.md'))), cr0(blob(PP, PRE['pp'] + ':FACES_LEDGER.md'))),
        docs={k: (cr0(raw(os.path.join(PP, p))), cr0(blob(PP, PRE['pp'] + ':' + p)), cr0(blob(PP, 'HEAD:' + p))) for k, p in DOCP.items()},
        pages={p: (cr0(raw(os.path.join(PP, p))), cr0(blob(PP, PRE['pp'] + ':' + p)), cr0(blob(PP, 'HEAD:' + p))) for p in (PAGE, DIR_PAGE)},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        corr_pre=cr0(blob(GS, PRE['gs'] + ':CORRESPONDENCE.md')), corr_now=cr0(raw(os.path.join(GS, 'CORRESPONDENCE.md'))),
        heads={r: gs('D:/' + r, 'rev-parse', 'main') for r in PRE_HEADS},
        trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        kcur=gs(KER, 'branch', '--show-current'), kdirty=gs(KER, 'status', '--porcelain', '--untracked-files=no'),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        gs_diff=sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip())),
        gs_head=gs(GS, 'rev-parse', 'HEAD'),
        kbranches={l.split()[0]: l.split()[1] for l in gs(KER, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b597*') for r in ('D:/relay', PP, GS, KER)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b598_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b598_mustnotexist.txt')), table_changed=None,
        fj=jl('b598_findings.json'), tj=jl('b598_trail.json'), sc=jl('b598_scores.json'), desk=rd('b598_desk_notes.txt'),
        wl=jl('b598_weight_line.json'), comps=rd('b598_components.txt'),
        J={k: jl('b598_bank_%s.json' % k) for k in DOCP},
        bank={k: read(os.path.join(ROOT, f)) for k, f in BANKF.items()},
        bank_raw={k: (cr0(raw(os.path.join(ROOT, f))), cr0(blob(ROOT, 'HEAD:' + f))) for k, f in BANKF.items()},
        bank_commits={k: [l for l in gs(ROOT, 'log', '--format=%h', PRE['relay'] + '..HEAD', '--', f).split(NL) if l.strip()] for k, f in BANKF.items()},
        eds=(sorted(x for x in gs(ROOT, 'diff', '--name-only', PRE['relay'], 'HEAD', '--', 'data/b558_editions').split(NL) if x.strip()),
             sorted(x for x in gs(ROOT, 'diff', '--name-only', '--', 'data/b558_editions').split(NL) if x.strip()),
             untracked(ROOT, 'data/b558_editions')),
        doc_s_old=cr0(blob(PP, '4cd1cd2:' + DOCP['SILENCE'])).decode('utf-8', 'replace').split(NL),
    )
    S['bank_files'] = {k: files_of(ROOT, c[0]) if c else [] for k, c in S['bank_commits'].items()}
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
    S.update(extra_sources(S))
    return S


def extra_sources(S):
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    REC = S['REC']
    X = {}
    X['gcp_zeta'] = GCP.arm(os.path.join(D, 'b596_nodes_faces.txt'), os.path.join(SP, '_b598_gcp'), os.path.join(D, 'b596_probe_out.txt'))
    X['gcp_chi'] = GCP.arm(os.path.join(D, 'b596_nodes_chi.txt'), os.path.join(SP, '_b598_gcp'), os.path.join(D, 'b596_chi_probe_out.txt'))
    X['ctl'] = TC.control()
    X['ctl_arm'] = TC.ARM
    X['tb_live'] = {k: REC.tier_block(k) for k in DOCP}
    X['rows_live'] = {}
    X['second_live'] = {}
    for k in DOCP:
        rows, second, _t = REC.rows_of(k)
        X['rows_live'][k] = rows
        X['second_live'][k] = second
    return X


# ### the act's own predicates
def _key(rs):
    return [(r['line'], r['terminal'], r['verdict'], r['reading'], r['own']) for r in rs]


def weight_ok(S):
    ls = S['wl'].get('lines', [])
    if len(ls) != 2:
        return False
    a, b = fline(S, ls[0]['line']), fline(S, ls[1]['line'])
    return a.startswith(ls[0]['head']) and '(:6880)' in ls[0]['head'] and 'b597 AT ITS WEIGHT' in a and 'fe1c68be' in a and '68c8dfa' in a \
        and 'body 551 against 545' in a and b.startswith(ls[1]['head']) and 'THE STRIKE ITEMS, AS RULED' in b and '(:6880)' in ls[1]['head'] \
        and 'the navigator’s' in b and ls[0]['line'] < ls[1]['line']


def docs_unedited(S):
    return all(bool(b) and a == b == c for a, b, c in S['docs'].values())


def pages_unchanged(S):
    return all(bool(b) and a == b == c for a, b, c in S['pages'].values())


def tier_ok(S):
    for k in DOCP:
        J, tb, bank = S['J'].get(k) or {}, S['tb_live'][k], S['bank'][k]
        if not J or json.dumps(J.get('tier_block'), sort_keys=True, ensure_ascii=False) != json.dumps(tb, sort_keys=True, ensure_ascii=False):
            return False
        if len(tb) != NTERMS[k] or not all(e['line'] and re.match(r'^T\d', e['tier']) and e['tier_source'].startswith('data/') for e in tb):
            return False
        if not all(('`%s` -- ' % e['written']) in bank for e in tb) or ('TIER BLOCK : %d terminals cited' % NTERMS[k]) not in bank:
            return False
    return True


def rows_ok(S):
    for k in DOCP:
        J, rows, bank = S['J'].get(k) or {}, S['rows_live'][k], S['bank'][k]
        if not J or _key(J.get('rows', [])) != _key(rows) or not rows:
            return False
        if not all(r['verdict'] in ('STANDS', 'MOVED-IN-MEANING', 'CREDIT') and r['reading'] for r in rows):
            return False
        if not all((':%d -- `%s` -- %s (' % (r['line'], r['terminal'], r['verdict'])) in bank for r in rows):
            return False
    return True


def moved_cite(S):
    pins = ('c5cba30', '6a4f482', '5e668b4', '5a1630b', '0e5233f')
    moved = [r for k in DOCP for r in (S['J'].get(k) or {}).get('rows', []) if r['verdict'] == 'MOVED-IN-MEANING']
    return bool(moved) and all(any(p in r['reading'] for p in pins) and re.search(r'\.lean` :\d+', r['reading']) is not None
                               and r['reading'].count('`') >= 6 for r in moved)


def b450_ok(S):
    REC = S['REC']
    for k in DOCP:
        bank = S['bank'][k]
        if '## b450`S ITEMS, LOCATED BY NAME AND PLACED' not in bank or not all(w in bank for w, _q, _p in REC.B450[k]):
            return False
    s_pre = cr0(S['docs']['SILENCE'][1]).decode('utf-8', 'replace').split(NL)
    r_pre = cr0(S['docs']['REPARAM'][1]).decode('utf-8', 'replace').split(NL)
    return s_pre[195].startswith('## 9. Correspondence') and S['doc_s_old'][195].startswith('## 9. Correspondence') \
        and 'VERDICT: `DISTINCT`' in r_pre[259]


def second_ok(S):
    s, r = S['second_live']['SILENCE'], S['second_live']['REPARAM']
    rowlines = set(x['line'] for x in S['rows_live']['SILENCE'])
    return len(s) == 5 and len(r) == 0 and 'SECOND SHAPE : 5 segment(s)' in S['bank']['SILENCE'] and 'SECOND SHAPE : 0 segment(s)' in S['bank']['REPARAM'] \
        and not (set(x['line'] for x in s) & rowlines) and all((':%d -- "%s"' % (x['line'], x['sentence'])) in S['bank']['SILENCE'] for x in s)


def banks_alone(S):
    for k, f in BANKF.items():
        c, files = S['bank_commits'][k], S['bank_files'][k]
        a, b = S['bank_raw'][k]
        if len(c) != 1 or files != [f] or not b or a != b or (S['J'].get(k) or {}).get('sha256') != hashlib.sha256(b).hexdigest():
            return False
    return True


SECTIONS = ['## THE TIER BLOCK', '## THE WORK-LIST', '## b450`S ITEMS, LOCATED BY NAME AND PLACED', '## OBJECTS FOR THE EDITION`S OTHER CLAUSES',
            '## THE SECOND SHAPE, PRINTED AND NOT APPLIED']


def bank_form(S):
    for k in DOCP:
        t = S['bank'][k]
        if not t.startswith('b598 -- THE TIER BLOCK AND EDITION WORK-LIST OF ') or 'AN INPUT TO CP-7`S EDITION, NOT AN EDITION' not in t.split(NL)[0]:
            return False
        idx = [t.find(x) for x in SECTIONS]
        if min(idx) < 0 or idx != sorted(idx):
            return False
    return True


def moved_printed(S):
    tot = 0
    for k in DOCP:
        m = re.search(r'MOVED-IN-MEANING ROWS FOR THE b599 DECISION : (\d+)\.', S['bank'][k])
        n = sum(1 for r in (S['J'].get(k) or {}).get('rows', []) if r['verdict'] == 'MOVED-IN-MEANING')
        if not m or int(m.group(1)) != n or (S['J'].get(k) or {}).get('moved') != n:
            return False
        tot += n
    return ('MOVED-IN-MEANING ROWS FOR THE b599 DECISION : %d' % tot) in S['comps']


def eds_scope(S):
    a, b, c = S['eds']
    return a == sorted(BANKF.values()) and b == [] and c == []


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
    tail = NL.join(ls[e - 1:e + 20]) if e else ''
    return bool(e) and fline(S, e) == S['REC'].TITLE and '**The tier blocks**' in tail and '**The work-lists.**' in tail \
        and '**Read in mutual light**' in tail and 'strengthens' in tail and all(f in tail for f in BANKF.values()) \
        and 'knill_laflamme_t1' in tail and ':5870' in tail and ':5990' in tail and 'OPEN_TRAILS :4540' in tail


def answers_banked(S):
    a = S['answers']
    return a.count('### PROMPT ') == 0 and 'NO PROMPT WAS PUT' in a and a.startswith('### b598 -- THE AUTHOR`S ANSWERS, 0 prompt(s)')


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


def _bad_rows(S, k):
    J = dict(S['J'].get(k) or {})
    rs = [dict(r) for r in J.get('rows', [])]
    if rs:
        rs[0]['verdict'] = 'CREDIT' if rs[0]['verdict'] != 'CREDIT' else 'STANDS'
    J['rows'] = rs
    return dict(S['J'], **{k: J})


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R208) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
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
    ('G-PRIOR-CLOSED-PUSHED', 'b597`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b597' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and relay`s log before the lock', lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face']
     and S['lock_epoch'] is not None and [l.split()[0][:8] for l in S['before_lock'] if int(l.split()[1]) <= S['lock_epoch']] == [STEPZERO],
     lambda S: put(S, 'before_lock', S['before_lock'] + ['deadbeef 1 b598 -- x'])),
    ('G-R208-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R208) END' in S['ferry'] and S['ot'].count('**(R208) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R208) ratified', '(R208) noted'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in (
        'data/b558_editions/SIMPLICITY_OF_RIEMANN_ZEROS.txt @', DOCP['SILENCE'] + ' @ eb9b057', DOCP['REPARAM'] + ' @ eb9b057', PAGE + ' @ eb9b057',
        DIR_PAGE + ' @ eb9b057', 'OPEN_TRAILS.md @ eb9b057', 'data/b450_components.txt @', 'data/b394_components.txt @', 'data/b557_tiers.txt @',
        'data/b597_closing_push_out.txt @', '### the terminal table at relay HEAD', 'Kernel/Cascade/InvarianceBarrier.lean @',
        'SIDECosmo/SteaneExemplar.lean @', 'SIDEStructuralErrorCorrection/DeAlignment.lean @', '`## 9. Correspondence` at :196'))
     and 'NO SUCH LINE' not in S['reads'], lambda S: put(S, 'reads', S['reads'] + '### NO SUCH LINE')),
    ('G-ANSWERS-BANKED', 'the act`s answers bank: no prompt put, said so', lambda S: answers_banked(S),
     lambda S: put(S, 'answers', S['answers'] + '\n### PROMPT 1 (x): y\n')),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 1e12) < S['lock_epoch'] and all(('  %s ' % a[0]) in S['prerun'] for a in ARMS)
     and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None, lambda S: put(S, 'prerun', '')),
    ('G-PUSHOUT-COMMITTED', 'relay cab56f31`s files', lambda S: S['pushout'][0] == ['data/b597_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/b597_closing_push_out.txt', 'x'], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b597') == 3, lambda S: put(S, 'push_lists', dict(S['push_lists'], **{'D:/relay': 'push-b597'}))),
    ('G-KEPT-BRANCHES', 'the kernel`s branch heads', lambda S: all(S['kbranches'].get(b, '').startswith(h) for b, h in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'simplicity-b596': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80 and every PLACE-papers read at ba5f0ea, run afresh through the test`s control()',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(S['ctl'][0], ok=False)] + S['ctl'][1:])),
    ('G-INSTRUMENTS-UNEDITED', 'b597`s sealed suite and the control`s test file on disk against 022d2bf0',
     lambda S: bool(S['suite597'][0]) and S['suite597'][0] == S['suite597'][1] and bool(S['testsrc'][0]) and S['testsrc'][0] == S['testsrc'][1],
     lambda S: put(S, 'suite597', (S['suite597'][0], S['suite597'][1] + b'x'))),
    ('G-WEIGHT-LINES', 'FINDINGS at the two banked lines: b597`s weight and the strike items', lambda S: weight_ok(S),
     lambda S: put(S, 'wl', dict(S['wl'], lines=S['wl'].get('lines', [])[:1]))),
    ('G-DOCUMENTS-UNEDITED', 'both documents on disk and at HEAD against eb9b057', lambda S: docs_unedited(S),
     lambda S: put(S, 'docs', dict(S['docs'], SILENCE=(S['docs']['SILENCE'][0] + b'x', S['docs']['SILENCE'][1], S['docs']['SILENCE'][2])))),
    ('G-TIER-BLOCKS', 'each bank`s tier block against the tier block re-derived afresh from b557`s tiers, the table and the kernels',
     lambda S: tier_ok(S), lambda S: put(S, 'tb_live', dict(S['tb_live'], REPARAM=S['tb_live']['REPARAM'][:1]))),
    ('G-WORKLIST-ROWS', 'each bank`s rows against the b558 matcher re-run afresh over the document at eb9b057, one verdict each',
     lambda S: rows_ok(S), lambda S: put(S, 'J', _bad_rows(S, 'SILENCE'))),
    ('G-MOVED-CITES-DECLARATION', 'every MOVED-IN-MEANING row: the statement, its file line and its pin', lambda S: moved_cite(S),
     lambda S: put(S, 'J', dict(S['J'], SILENCE=dict(S['J'].get('SILENCE') or {}, rows=[dict(r, reading='x') if r['verdict'] == 'MOVED-IN-MEANING' else r
                                                                                       for r in (S['J'].get('SILENCE') or {}).get('rows', [])])))),
    ('G-B450-PLACED', 'each bank`s b450 section against the tool`s items, the §9 heading at eb9b057 and at 4cd1cd2, b454`s verdict line',
     lambda S: b450_ok(S), lambda S: put(S, 'doc_s_old', [''] * 300)),
    ('G-SECOND-SHAPE-PRINTED', 'the second shape re-run afresh against the bank: five segments printed, none a row', lambda S: second_ok(S),
     lambda S: put(S, 'second_live', dict(S['second_live'], SILENCE=S['second_live']['SILENCE'][:4]))),
    ('G-BANKS-COMMITTED-ALONE', 'relay`s log since 022d2bf0 for each bank: one commit, that file alone, the banked sha256', lambda S: banks_alone(S),
     lambda S: put(S, 'bank_files', dict(S['bank_files'], SILENCE=[BANKF['SILENCE'], BANKF['REPARAM']]))),
    ('G-BANK-FORM', 'each bank`s head line and its sections in order', lambda S: bank_form(S),
     lambda S: put(S, 'bank', dict(S['bank'], REPARAM=S['bank']['REPARAM'].replace('## THE TIER BLOCK', '## TIER')))),
    ('G-MOVED-COUNT-PRINTED', 'each bank`s MOVED line against its rows, and the components bank`s sum for the b599 decision', lambda S: moved_printed(S),
     lambda S: put(S, 'comps', S['comps'].replace('FOR THE b599 DECISION : ', 'FOR THE b599 DECISION : 7'))),
    ('G-EDITIONS-DIR-SCOPE', 'relay data/b558_editions: the two new files and nothing else', lambda S: eds_scope(S),
     lambda S: put(S, 'eds', (S['eds'][0], ['data/b558_editions/SIMPLICITY_OF_RIEMANN_ZEROS.txt'], S['eds'][2]))),
    ('G-PAGES-UNCHANGED', 'both pages on disk and at HEAD against eb9b057', lambda S: pages_unchanged(S),
     lambda S: put(S, 'pages', dict(S['pages'], **{PAGE: (S['pages'][PAGE][0] + b'x', S['pages'][PAGE][1], S['pages'][PAGE][2])}))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from b596`s faces list and v0.17 probe bank against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from b596`s χ list and v0.17 probe bank against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD,
     lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-PRINTED-RECORDED', 'this act`s trail record: what was printed for the author`s ruling', lambda S: 'Printed for the author’s ruling, not graded' in trail(S)
     and 'Silence Principle' in trail(S) and '§9' in trail(S), lambda S: put(S, 'ot', S['ot'].replace('Printed for the author’s ruling, not graded', 'x'))),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b599, the editions of SILENCE_STAGES_DEALIGNMENT and REPARAMETERIZATION_BARRIERS in one act' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b599, the editions of SILENCE_STAGES_DEALIGNMENT and REPARAMETERIZATION_BARRIERS in one act', 'x'))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, the explicit-formula checkout, the trial branch',
     lambda S: all(S['heads'][r].startswith(h) for r, h in PRE_HEADS.items()) and S['kcur'] == 'main' and S['kdirty'] == ''
     and S['trial'] == 'f22ff35', lambda S: put(S, 'heads', dict(S['heads'], **{'SIDE-cosmo': '0'}))),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('36352a0', '36352a0', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b598_record.py'): S['tooltext'].get(os.path.join(T, 'b598_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-NODEPOSIT', 'this act`s tools: no platform call', lambda S: bool(S['tooltext']) and not [f for f, t in S['tooltext'].items()
                                                                                              if ('zenodo' + '.org') in t or ('urllib' + '.request') in t],
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-NOH2-MOVED', 'FACES_LEDGER.md against its pre-act blob', lambda S: S['faces'][1] and S['faces'][0] == S['faces'][1],
     lambda S: put(S, 'faces', (S['faces'][0] + b'x', S['faces'][1]))),
    ('G-README-UNTOUCHED', 'README.md against its pre-act blob', lambda S: S['readme'][1] and S['readme'][0] == S['readme'][1],
     lambda S: put(S, 'readme', (S['readme'][0] + b'x', S['readme'][1]))),
    ('G-REGISTRY-UNTOUCHED', 'REGISTRY.md against its pre-act blob', lambda S: S['registry'][1] and S['registry'][0] == S['registry'][1],
     lambda S: put(S, 'registry', (S['registry'][0] + b'x', S['registry'][1]))),
    ('G-KEYSTONES-SCOPE', 'PLACE-papers` phase, day1 and outputs paths, tracked and untracked', lambda S: S['keystone_changes'] == [],
     lambda S: put(S, 'keystone_changes', [DOCP['SILENCE']])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 022d2bf0, by blob id', lambda S: S['prior_bad'] == []
     and S['prior_n'] > 6000, lambda S: put(S, 'prior_bad', ['data/b558_editions/SIMPLICITY_OF_RIEMANN_ZEROS.txt'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files, tracked and untracked', lambda S: S['pp_changed'] == ['FINDINGS.md', 'OPEN_TRAILS.md'],
     lambda S: put(S, 'pp_changed', sorted(S['pp_changed'] + [PAGE]))),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-GS-UNTOUCHED', 'SIDE-global-section`s diff against 3528bcf and its HEAD', lambda S: S['gs_diff'] == [] and S['gs_head'].startswith(PRE['gs'])
     and S['corr_now'] == S['corr_pre'], lambda S: put(S, 'gs_diff', ['CORRESPONDENCE.md'])),
    ('G-TABLE-GRADES-UNMOVED', 'the regenerated table`s diff', lambda S: S['table_changed'] is not None and all(('TABLE CELL: %s / %s' % tuple(k)) in S['face']
                                                                                                             for k in S['table_changed']),
     lambda S: put(S, 'table_changed', [['SIDE-cosmo', 'x']])),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', ''))
     for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every file written, against the (W) globs', lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/unlisted.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                          and "startswith('b598')" in S['suite'] and "data/b598_components.txt' in gs(ROOT, 'show'" in S['suite']),
     lambda S: put(S, 'suite', S['suite'].replace("startswith('b598')", ''))),
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
    rec('b598 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % ('PRE-SEAL (R202)(3)' if PRERUN else 'POST-PUSH' if pushed else 'PRE-PUSH'))
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
        out = os.path.join(D, 'b598_arms_prerun.txt')
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b598_checks_postpush.txt' if pushed else 'b598_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    if not (RERUN or PRERUN):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b598_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s' % os.path.basename(out))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
