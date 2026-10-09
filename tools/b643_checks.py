# -*- coding: utf-8 -*-
"""b643_checks.py -- THE SUITE OF b643, UNDER (R253): THE TWO READERS REPAIRED (DATA BINDERS, PRIMED NAMES) AND RERUN; THE PAGES RE-EMITTED
AT v0.26; THE KEYSTONE CENSUS AT v0.7 WITH SIX STATUSES, A NON-VACUITY COLUMN, A CONSUMERS COLUMN AND HINGES MARKED, EVERY CELL FROM BANKS; THE
PI-0-1 FORM READ AT SOURCE; THE SECOND READER.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### (R253)(8): the face is sealed AFTER Components 2-6, so the components' relay and PLACE-papers commits precede the lock and are declared
### in section (0); the record, the root and every commit after them follow it.
### ### G-ACTROOT-VERIFY reads the chain: b624 to b639 and b641 to b643 AGREE, b640 DISAGREE on its two re-banked files alone (its defect (h)).
### ### The harness is b568's to b642's (helpers, runner, seal), carried from tools/b642_checks.py; the sources, predicates and arms are b643's.
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
import b643_worklist as K     # noqa: E402
import b641_worklist as K41   # noqa: E402

NL = chr(10)
PP, EF = K.PP, K.EF
GS = 'D:/SIDE-global-section'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
FACE = os.path.join(D, 'b643_registration_2026-10-08.txt')
PAGE, DIR_PAGE = K.PAGE, K.DIR_PAGE
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP, gs='17ce9ff')
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52', 'epstein-b590': 'c404e72', 'simplicity-b596': '5a1630b', 'product-b600': '1dd5cd7',
        'doubling-keiper-b601': '5fc0c87', 'sign-window-b602': '914c413', 'family-b603': '1d5d4dd', 'platt-b626': 'e939c92',
        'cite-b628': '98b7668', 'nb-b629': 'aa17442', 'dedekind-b631': '8c51431', 'v0.26-work': '82550e4'}
STEPZERO = K.STEPZERO
CONTROL_ARM = 'G-B592-LISTS-CONTROL-AT-12C15C80-BA5F0EA-E0-12C15C80'
FROZEN_ARM = 'G-GEN-OLD-LISTS-FROZEN-AT-84BAE29A-52822A5-GEN-84BAE29A'
FROZEN_PINS = ('84bae29a', '52822a5')
FROZEN_NODES = {'zeta': 'b622_nodes_zeta.txt', 'chi': 'b622_nodes_chi.txt'}
FROZEN_PROBE = {'zeta': 'b602_probe_out.txt', 'chi': 'b603_chi_probe_out.txt'}
TABLE_FILES = K.TABLE_FILES
ABSENT = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_9.md'
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
SEAL = '--seal' in sys.argv
L = []
SP = K.SP
# ### the instruments b643 does not edit, against relay 13b1c48b: b642's tools, the readers and their tools, the generators and their tests, the
# ### shared tools; tools/e0_rule.py and tools/b378_terminals.py are the two repairs and are read by their own arms (G-REPAIR-*).
INST = ('b642_checks.py', 'b642_closing.py', 'b642_tests.py', 'b642_worklist.py', 'b642_reg_gate.py', 'b642_regspec.py', 'b642_record.py',
        'b641_record.py', 'b640_record.py', 'b639_record.py', 'b638_record.py', 'b637_record.py', 'b635_record.py', 'b634_record.py', 'b634_elab.py',
        'b634_worklist.py', 'b633_record.py', 'b632_record.py', 'b626_record.py', 'b627_record.py', 'b616_record.py', 'b616_claims.py',
        'b602_record.py', 'b566_record.py', 'premise_status.py', 'test_premise_status.py', 'test_e0_rule.py', 'test_e0_existential.py',
        'chain_page.py', 'g_chain_page.py', 'test_chain_page.py', 'test_g_chain_page.py', 'test_chain_page_b596.py', 'test_chain_page_b638.py',
        'banned_terms.py', 'terminal_table.py', 'table_gate.py', 'reg_seal.py', 'b378_lockgate.py', 'push_gated.sh', 'test_push_gated.sh',
        'act_root.py', 'test_act_root.py', 'corr_row.py', 'mirror_build.ps1', 'mirror_verify.py', 'mirror_roster.json', 'test_elab_reader_b634.py')
COUNT_CASE = r'^  \(\d+\) '
REPAIRED = ('tools/e0_rule.py', 'tools/b378_terminals.py')
PRIOR_EDITED = ('data/glossary.txt',)      # ### (R253)(5)(a): the glossary extended through the Edit tool, read by G-GLOSSARY-SIX
SIX = ('OPEN', 'CITED', 'DISCHARGED', 'WITNESSED', 'DOMAIN', 'REFUTED-BY-COMPUTATION')
NEW_TERMS = ('REFUTED-BY-COMPUTATION', 'WITNESS', 'DEGENERATE', 'CONSUMER', 'CHAIN', 'HINGE')
CHAIN_DEF = ("a weakly connected component of a kernel's use-graph restricted to the declarations consuming the premise directly or transitively, "
             "the premise and its projections removed, named by its terminal declaration")
PRIMED = ("SIDEExplicitFormula.Schema.Dedekind.dedekind_rhs'", "SIDEExplicitFormula.Schema.Dedekind.TrivialSummandPremise'",
          "SIDEExplicitFormula.SaltCheckNonvacuity.trivialSummandPremise'_witness'")
CORR = {'zeta': (443, 497), 'chi': (351, 391)}


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b643')
            and 'data/b643_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def strip_prose(t):
    t = re.sub(r'"""[\s\S]*?"""', '', t)
    t = re.sub(r"'''[\s\S]*?'''", '', t)
    return NL.join(l.split('#', 1)[0] for l in t.split(NL))


def wl_globs(face):
    try:
        w = face[face.index('### (W) THE WRITE LIST.'):face.index('### (Z) THE NOTHINGS.')]
    except ValueError:
        return []
    return sorted(set(re.findall(r'`((?:relay|PLACE-papers|SIDE-global-section|SIDE-explicit-formula|SIDE-structural-error-correction)/[^`\s]+)`', w)))


def untracked(repo, *paths):
    return [l[3:].strip() for l in git(repo, 'status', '--porcelain', '--untracked-files=all', '--', *paths)[1].split(NL) if l.startswith('?? ')]


def written_files():
    res = []
    for repo, name, pre in ((ROOT, 'relay', PRE['relay']), (PP, 'PLACE-papers', PRE['pp']), (GS, 'SIDE-global-section', PRE['gs']),
                            (EF, 'SIDE-explicit-formula', K.EF_PIN)):
        ch = set(x for x in gs(repo, 'diff', '--name-only', pre).split(NL) if x.strip())
        ch |= set(x for x in gs(repo, 'diff', '--name-only', pre, 'HEAD').split(NL) if x.strip())
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


def sealed_now():
    out = {}
    for t in K.SEALED:
        b = raw(os.path.join(T, t))
        out[t] = hashlib.sha256(b).hexdigest() if b is not None else None
    return out


def appended(pre, now):
    return now[len(pre):].decode('utf-8', 'replace') if now and pre and now.startswith(pre) else ''




def rows_of_table():
    try:
        return json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))['rows']
    except Exception:
        return []


def sources():
    import b643_record as REC
    import b616_record as R6
    face = read(FACE)
    lockn = sorted(glob.glob(os.path.join(D, 'b643_lockgate_notes*.txt')))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if f.startswith('b643_') and f.endswith('.py'))
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    cen7 = cr0(raw(os.path.join(PP, *K.CEN7.split('/'))))
    S = dict(
        REC=REC, face=face, ferry=rd('b643_ferry.txt'), scan=rd('b643_ferry_scan.txt'), cens=rd('b643_census_stepzero.txt'),
        fcens=rd('b643_faces_census_stepzero.txt'), pins0=rd('b643_pins_stepzero.txt'), procs=rd('b643_procs_stepzero.txt'),
        lock=read(lockn[-1]) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        prior=rd('b642_closing.txt'), reads=rd('b643_reads.txt'), branches=rd('b643_branches.txt'), answers=rd('b643_author_answers.txt'),
        prerun=rd('b643_arms_prerun.txt'), rl=jl('b643_record_lines.json'),
        tests=jl('b643_tests_stepzero.json'), testst=rd('b643_tests_stepzero.txt'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', 'HEAD', 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b643_seal_hashes.json'), sealnow=sealed_now(),
        repairs=rd('b643_repairs.txt'), rerun=jl('b643_rerun.json'), reruntxt=rd('b643_rerun.txt'),
        trows=dict((r['name'], r) for r in rows_of_table() if r['repo'] == 'SIDE-explicit-formula'),
        pagej={k: jl('b643_page_%s.json' % k) for k in ('zeta', 'chi')}, pga=rd('b643_page_arms.txt'),
        nodes={k: (cr0(raw(os.path.join(D, K.NODES_PREV[k]))), cr0(raw(os.path.join(D, K.NODES[k])))) for k in ('zeta', 'chi')},
        probes={k: raw(os.path.join(D, K.PROBE[k])) for k in ('zeta', 'chi')},
        pages_head={k: cr0(blob(PP, 'HEAD:' + K.PNAME[k])) for k in ('zeta', 'chi')},
        glossary=read(os.path.join(D, 'glossary.txt')), glossary_pre=(cr0(blob(ROOT, '%s:data/glossary.txt' % PRE['relay'])) or b'').decode('utf-8'),
        cen7=cen7, cen7_head=cr0(blob(PP, 'HEAD:' + K.CEN7)), cen6=(cr0(raw(os.path.join(PP, *K.CEN6.split('/')))), cr0(blob(PP, PRE['pp'] + ':' + K.CEN6))),
        edj=jl('b643_edition.json'), ediff=rd('b643_edition_diff.txt'), cj=jl('b643_consumers.json'), ct=rd('b643_consumers.txt'),
        deps=jl('b643_deps_runs.json'), ptj=jl('b643_premise_table.json'), ptt=rd('b643_premise_table.txt'), pi=rd('b643_pi01_attempts.txt'),
        rdj=jl('b643_reader_compare.json'), rdt=rd('b643_reader_compare.txt'), rpk=rd('b643_reader_packet.txt'), tfj=jl('b643_table_final.json'),
        closing_src=read(os.path.join(T, 'b643_closing.py')),
        local_present=os.path.exists(local),
        local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK),
        local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b643_act_root.json'), arj0=jl('b642_act_root.json'), art=rd('b643_act_root.txt'), rootsf=rd('act_roots.txt'),
        rpush=rd('b643_root_push_out.txt'), ppush=rd('b643_pp_root_push_out.txt'),
        absent=tri(PP, ABSENT, PRE['pp']),
        pushout=(files_of(ROOT, STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, f))), cr0(blob(ROOT, 'HEAD:tools/' + f))) for f in INST},
        rfiles_e0=files_of(ROOT, K.E0_COMMIT), rfiles_b378=files_of(ROOT, K.B378_COMMIT),
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        errata=(cr0(raw(os.path.join(PP, 'ERRATA.md'))), cr0(blob(PP, PRE['pp'] + ':ERRATA.md'))),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b643_kernels_face.json').get('kernels') or {}),
        lv_head=gs('D:/SIDE-lv-conservation', 'rev-parse', 'HEAD'), trial=gs('D:/SIDE-lv-conservation', 'rev-parse', '--short=7', 'toolchain-trial-b551'),
        te=(gs(TE, 'rev-parse', '--short=7', 'HEAD'), gs(TE, 'rev-parse', '--short=7', 'origin/main'), gs(TE, 'status', '--porcelain', '--untracked-files=no')),
        kbranches={l.split()[0]: l.split()[1] for l in gs(EF, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()},
        push_lists={r: gs(r, 'branch', '--list', 'push-b642*') for r in ('D:/relay', PP, EF)},
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'), suite=read(os.path.join(T, 'b643_checks.py')),
        mustfail=not os.path.exists(os.path.join(D, 'b643_mustnotexist.txt')), table_changed=None,
        fj=jl('b643_findings.json'), tj=jl('b643_trail.json'), sc=jl('b643_scores.json'), desk=rd('b643_desk_notes.txt'),
        lsr=None,
        rlog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(ROOT, 'log', '--reverse', '--format=%h %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        plog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(PP, 'log', '--reverse', '--format=%h %ct %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()],
    )
    S['kern_now'] = kern_now(S['kern_face']) if S['kern_face'] else {}
    S['written'] = written_files()
    S['globs'] = wl_globs(face)
    S['nd_sets'] = R6.nd_sets()
    ch = set(x for x in gs(PP, 'diff', '--name-only', PRE['pp']).split(NL) if x.strip())
    ch |= set(x for x in gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD').split(NL) if x.strip())
    ch |= set(untracked(PP, 'phase1.5', 'phase2', 'day1', 'outputs', 'heritage'))
    S['pp_changed'] = sorted(ch)
    S['gs_diff'] = sorted(set(x for x in (gs(GS, 'diff', '--name-only', PRE['gs']) + NL + gs(GS, 'diff', '--name-only', PRE['gs'], 'HEAD')).split(NL) if x.strip()))
    S['ledger_adds'] = appended(S['fi_pre'], S['fi_now']) + NL + appended(S['ot_pre'], S['ot_now'])
    pub = [S['ledger_adds'], (S['cen7'] or b'').decode('utf-8', 'replace')] + [(S['pages_head'][k] or b'').decode('utf-8', 'replace') for k in ('zeta', 'chi')]
    for f in sorted(os.listdir(D)):
        if f.startswith(('b643_', 'audit_b643_')) and os.path.isfile(os.path.join(D, f)):
            pub.append(read(os.path.join(D, f)))
    pub += [read(f) for f in tools] + [rd('act_roots.txt'), S['glossary']]
    S['nd_pub'] = R6.nd_hits(NL.join(pub), S['nd_sets'])[0]
    S['outside'] = [n for n in S['REC'].OUTSIDE_NEEDLES if n in S['ledger_adds'] or n in (S['cen7'] or b'').decode('utf-8', 'replace')]
    pre_ids = {}
    for l in git(ROOT, 'ls-tree', '-r', PRE['relay'], '--', 'data/')[1].split(NL):
        if '\t' in l:
            meta, p = l.split('\t', 1)
            pre_ids[p] = meta.split()[2]
    bad = []
    for p, i in pre_ids.items():
        if os.path.basename(p) in TABLE_FILES or p == 'data/act_roots.txt' or p in PRIOR_EDITED:
            continue
        fp = os.path.join(ROOT, p)
        rb = open(fp, 'rb').read() if os.path.exists(fp) else None
        if rb is None or i not in (blob_id(rb), blob_id(cr0(rb))):
            bad.append(p)
    S['prior_bad'], S['prior_n'] = bad, len(pre_ids)
    S['roots_pre'] = cr0(blob(ROOT, PRE['relay'] + ':data/act_roots.txt'))
    S['roots_now'] = cr0(raw(os.path.join(D, 'act_roots.txt')))
    S['bank_mtimes'] = {}
    for it in (S['arj'].get('items') or []):
        p = it.split()[0]
        if p.startswith('data/') and os.path.exists(os.path.join(ROOT, *p.split('/'))):
            S['bank_mtimes'][p] = os.path.getmtime(os.path.join(ROOT, *p.split('/')))
    S.update(extra_sources(S))
    return S


CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'SPIRAL_MAP_v0_7.md', 'README.md', 'REGISTRY.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md', K41.CEN5, K41.CEN6,
            K41.MONO, K41.SIEVE6) + tuple('day1/' + c for c in K41.COMPANIONS)


def extra_sources(S):
    import chain_page as CP
    import g_chain_page as GCP
    import test_chain_page_b596 as TC
    import b626_record as R26
    import b627_record as R27
    import act_root as AR
    import b638_record as R8
    import e0_rule as E
    X = {}
    for k in ('zeta', 'chi'):
        lp = os.path.join(D, K.NODES[k])
        try:
            X['gcp_' + k] = GCP.arm(lp, os.path.join(SP, '_b643_gcp'), os.path.join(D, K.PROBE[k]))
        except Exception as e:
            X['gcp_' + k] = dict(ok=False, why='raised %s' % type(e).__name__)
    rule = CP.E0
    CP.E0 = R26.e0_module(TC.RELAY_PIN)
    try:
        X['ctl'] = TC.control()
    finally:
        CP.E0 = rule
    X['ctl_arm'] = TC.ARM
    old = []
    pins, tc_c, tc_git = (TC.RELAY_PIN, TC.PRE_PP), TC.C, TC._GIT
    try:
        gen = R27.cp_module(FROZEN_PINS[0])
        gen.E0 = R26.e0_module(FROZEN_PINS[0])
        TC.RELAY_PIN, TC.PRE_PP = FROZEN_PINS
        TC.C, TC._GIT = gen, gen.git
        for k in ('zeta', 'chi'):
            lb, pb = blob(ROOT, '%s:data/%s' % (FROZEN_PINS[0], FROZEN_NODES[k])), blob(ROOT, '%s:data/%s' % (FROZEN_PINS[0], FROZEN_PROBE[k]))
            d = os.path.join(SP, '_b643_frozen')
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
        X['ar_verify'] = AR.verify(remote=KC0.remote_refs)
    except Exception as e:
        X['ar_verify'] = [('raised', type(e).__name__, [])]
    X['order_slack'] = AR.ORDER_SLACK
    X['sorry_tokens'] = S['REC'].sorry_tokens('main')
    try:
        X['gloss_block'] = CP.glossary_block()
    except Exception as e:
        X['gloss_block'] = ['raised %s' % type(e).__name__]
    X['gl_pages'] = {k: R8.glossary_lines((S['pages_head'][k] or b'').decode('utf-8', 'replace')) for k in ('zeta', 'chi')}
    X['gl_census'] = R8.glossary_lines((S['cen7'] or b'').decode('utf-8', 'replace'))
    X['contdiff'] = (E.typing('WithTop ℕ∞')[0], E.grade('{n : WithTop ℕ∞} : ContDiff ℂ n riemannZeta₀', 'theorem')[0])
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
    i = t.find(S['REC'].TRAIL_HEAD())
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


def rline(S, i, key='rl'):
    x = (S[key].get('lines') or [])
    return x[i] if len(x) > i else {}


def landed(S, i, need, key='rl'):
    x = rline(S, i, key)
    o = (fline if x.get('file') == 'FINDINGS.md' else oline)(S, x.get('line'))
    return bool(x) and o.startswith(poss(x.get('head', '\x00'))) and all(n in o for n in need)


UNANSWERED = "The user doesn't want to proceed with this tool use"


def answers_ok(S):
    """### the answers bank as it prints: its count line against its prompt headers, each prompt's options, each call's result, every answer read
    ### back by the record tool."""
    a = S['answers']
    m = re.search(r'^### b643 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
    blocks = re.split(r'^### CALL ', a, flags=re.M)[1:]
    heads = re.findall(r'^### PROMPT \d+ \(', a, re.M)
    per = [len(re.findall(r'^  OPTION \d+', p, re.M)) for p in re.split(r'^### PROMPT \d+ \(', a, flags=re.M)[1:]]
    if not m:
        return False
    unanswered = []
    i = 0
    for b in blocks:
        n = len(re.findall(r'^### PROMPT \d+ \(', b, re.M))
        if UNANSWERED in b:
            unanswered += list(range(i, i + n))
        i += n
    return int(m.group(1)) == len(heads) and len(heads) >= 2 and all(x >= 2 for x in per) and len(per) == len(heads) \
        and len(blocks) == a.count('RESULT (transcript line') and '### NO RESULT' not in a \
        and all((S['REC'].answer_of(k) != 'no answer banked') == (k not in unanswered) for k in range(len(heads)))


def tests_ok(S):
    """### every test file tracked at HEAD in the runner bank; every one clean but test_chain_page_b638.py, whose cases (4)-(7) fail on the
    ### v0.25 lists it carries against the v0.26 table (defect, recorded); the page tests run again on the v0.26 lists after Component 3."""
    j = S['tests']
    names = S['tracked_tests']
    nf = sorted(n for n, x in j.items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(j) == names and nf == ['test_chain_page_b638.py'] \
        and j['test_chain_page_b638.py']['failing'] == ['(4)', '(5)', '(6)', '(7)'] \
        and ('TEST FILES %d ; RUN %d ; NOT CLEAN 1' % (len(names), len(names))) in S['testst'] \
        and j['test_chain_page.py']['args'][:2] == ['b643_nodes_zeta.txt', 'b643_probe_out_zeta.txt'] \
        and j['test_g_chain_page.py']['args'][:2] == ['b643_nodes_zeta.txt', 'b643_probe_out_zeta.txt']


def instruments_ok(S):
    for f, (pre, now, head) in S['inst'].items():
        if pre is None or pre != now:
            return False
    return True


def local_ok(S):
    return S['local_present'] and S['local_log'] == '' and S['local_index'] == '' and S['local_status'].startswith('??')


def seal_hashes_ok(S):
    j = S['sealj']
    at = iso_epoch(j.get('at') or '')
    rec_ = j.get('tools') or {}
    return bool(rec_) and at is not None and S['lock_epoch'] is not None and S['lock_epoch'] <= at \
        and sorted(rec_) == sorted(K.SEALED) and all(S['sealnow'].get(t) == rec_[t] for t in K.SEALED)


def _component_commit(s):
    return s.startswith('b643 step zero') or s.startswith('b643 Component')


def sealed_after_ok(S):
    """### (R253)(8): the face locked after every relay and PLACE-papers commit of the components (subjects `b643 step zero` and `b643
    ### Component`), before every other commit of the act."""
    lk = S['lock_epoch']
    if lk is None:
        return False
    return all((t < lk) == _component_commit(s) for h, s, t in S['rlog']) and all((t < lk) == _component_commit(s) for h, s, t in S['plog']) \
        and any(_component_commit(s) for h, s, t in S['plog'])


def repair_ok(S, files, tool, test, before, after):
    j = (S['tests'].get(os.path.basename(test)) or {})
    return sorted(files) == sorted([tool, test]) and j.get('rc') == 0 and j.get('cases') == after and j.get('passing') == after \
        and ('before the edit : ### ### **%d of %d cases as wanted -- FAIL**' % (before, after)) in S['repairs']


def primed_ok(S):
    return all(n in S['trows'] and S['trows'][n]['grade'] not in ('—', 'UNGRADED') and S['trows'][n].get('statement_state') == 'RESOLVED'
               for n in PRIMED)


def rerun_ok(S):
    j = S['rerun']
    t = j.get('table') or {}
    mv = [m for m in j.get('moves') or [] if m[1] == 'SIDEExplicitFormula.Keiper.contDiff_riemannZeta₀']
    return len(j.get('moves') or []) == 1 and len(mv) == 1 and mv[0][2:4] == ['INTERFACES', 'DERIVES'] and len(t.get('moved') or []) == 12 \
        and len(t.get('grade_moved') or []) == 5 and not t.get('added') and not t.get('gone') \
        and '**ELABORATED GRADE MOVES 1 ; TABLE ROWS MOVED 12 (GRADE MOVED 5) ; ADDED 0 ; GONE 0.**' in S['reruntxt']


def pins_ok(S):
    for k in ('zeta', 'chi'):
        a, b = S['nodes'][k]
        if a is None or b is None:
            return False
        la, lb = a.decode('utf-8').split(NL), b.decode('utf-8').split(NL)
        d = [(x, y) for x, y in zip(la, lb) if x != y]
        if len(la) != len(lb) or d != [('# pin: v0.25', '# pin: v0.26')]:
            return False
    return True


def pages_ok(S):
    for k in ('zeta', 'chi'):
        j = S['pagej'][k]
        pb = S['probes'][k]
        ph = S['pages_head'][k]
        # ### the bank`s sha256 against HEAD proves the page landed; `written` is False on a re-emission that found HEAD already equal, so the
        # ### counts are checked as taken before the act (corr_at) instead.
        if not (j and pb and ph and j.get('same_as_run') and j.get('corr_at') == K.PRE_PP and j.get('probe_sha256') == hashlib.sha256(pb).hexdigest()
                and j.get('sha256') == hashlib.sha256(ph).hexdigest() and (j.get('corr_before'), j.get('corr_after')) == CORR[k]
                and not j.get('corr_removed')):
            return False
    return True


def glossary_six_ok(S):
    pre = [l.split('\t')[0] for l in S['glossary_pre'].split(NL) if l.strip() and not l.startswith('#')]
    now = [l.split('\t') for l in S['glossary'].split(NL) if l.strip() and not l.startswith('#')]
    return [x[0] for x in now] == pre + list(NEW_TERMS) and dict((x[0], x[1]) for x in now if len(x) > 1).get('CHAIN') == CHAIN_DEF


def glossary_everywhere_ok(S):
    b = S['gloss_block']
    return isinstance(b, list) and len(b) > 4 and all(S['gl_pages'][k] == b for k in ('zeta', 'chi')) and S['gl_census'] == b \
        and all(('- **%s** —' % t) in NL.join(b) for t in NEW_TERMS)


def consumers_ok(S):
    j = S['cj']
    rows = j.get('rows') or []
    calls = S['deps'].get('calls') or []
    failed = [c for c in calls if c.get('rc') != 0]
    return len(rows) == 50 and all('consumers' in r for r in rows) and failed and all(c.get('note') for c in failed) \
        and all(any(c2.get('rc') == 0 and c2['kernel'] == c['kernel'] and c2['top'] == c['top'] for c2 in calls) for c in failed) \
        and all(p.get('read') or p.get('why') for r in rows for p in r['per']) and '### ### **HEADS 50 ;' in S['ct'] \
        and all((r['consumers'] is None) == (not any(p.get('read') for p in r['per'])) for r in rows)


def hinges_ok(S):
    rows = S['cj'].get('rows') or []
    for r in rows:
        if r['hinge']:
            if not (r['hinge_kernels'] or r['hinge_chains']):
                return False
            for p in r['per']:
                if p['kernel'] in r['hinge_chains'] and (p['n_chains'] < 2 or not all(p['chains'])):
                    return False
    return any(r['hinge'] for r in rows)


def premise_table_ok(S):
    rows = S['ptj'].get('rows') or []
    deg = set(l.split()[0] for l in rd('b642_nonvacuity.txt').split(NL) if re.match(r'^\S+  \[DEGENERATE;', l))
    return len(rows) == 50 and len(set(r['head'] for r in rows)) == 50 and all(r['status'] in SIX for r in rows) \
        and all(r['nonvacuity'] in ('WITNESSED', 'DEGENERATE') or r['nonvacuity'].startswith('UNWITNESSED (') for r in rows) \
        and all(r['nonvacuity'] == 'DEGENERATE' for r in rows if r['head'] in deg) and len(deg) == 3 \
        and 'DEGENERATE counted as WITNESSED: 0' in S['ptt'] and 'every head one status and one non-vacuity value: True' in S['ptt'] \
        and all(r.get('cons_cell') for r in rows)


def edition_ok(S):
    j = S['edj']
    c7 = S['cen7']
    a6, b6 = S['cen6']
    return bool(j and c7) and S['cen7_head'] == c7 and j.get('sha256') == hashlib.sha256(c7).hexdigest() and a6 is not None and a6 == b6 \
        and 'v0.6 LINES REMOVED OUTSIDE THE GLOSSARY BLOCK : 0.' in S['ediff'] and not j.get('dry')


def pi01_ok(S):
    t = (S['cen7'] or b'').decode('utf-8', 'replace')
    return '**SOURCES NAMED 2 ; REACHED AND READ 0.**' in S['pi'] and 'neither was reached' in t and 'Π⁰₁' not in t.split('## Glossary')[0]


def reader_ok(S):
    j = S['rdj']
    a = j.get('answers') or {}
    return len(a) == 3 and all((a.get(str(q)) or a.get(q) or {}).get('answer') for q in (1, 2, 3)) and isinstance(j.get('needles'), int) \
        and isinstance(j.get('hand'), int) and 'BY THE NEEDLES' in S['rdt'] and 'reader_b643' in S['rpk'] \
        and 'memory named in the run log: False' in S['rdt']


def table_final_ok(S):
    t = S['tfj']
    return bool(t) and t.get('rc') == 0 and not t.get('gone') and not t.get('added') and not t.get('grade_moved') and not t.get('moved')


def root_banked_ok(S):
    import act_root as AR
    j, j0 = S['arj'], S['arj0']
    rows = [l.split(None, 3) for l in S['rootsf'].split(NL) if l.strip()]
    return bool(j) and len(rows) == 20 and rows[19][:3] == ['b643', j.get('root'), j0.get('root')] \
        and AR.root_of(j.get('items') or [], j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) and not [it for it in j.get('items') or [] if 'b628_intake_crank' in it] \
        and any(it.startswith('data/b643_premise_table.txt ') for it in j.get('items') or [])


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b643_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def midpush_ok(S):
    heads = (S['arj'].get('reads') or {}).get('heads') or {}
    m1 = re.search(r'push_gated: main read back at the remote: (\w+)', S['rpush'])
    m2 = re.search(r'push_gated: main read back at the remote: (\w+)', S['ppush'])
    return bool(m1 and m2) and heads.get('relay') == m1.group(1) and heads.get('PLACE-papers') == m2.group(1)


B640_DEFECT_H = ['bank data/b640_author_answers.txt changed', 'bank data/b640_seal_hashes.json changed']


def verify_ok(S):
    v = S['ar_verify'] or []
    return [x[0] for x in v] == ['b%d' % i for i in range(624, 644)] and all(x[1] == 'AGREE' for x in v if x[0] != 'b640') \
        and [(x[1], sorted(x[2])) for x in v if x[0] == 'b640'] == [('DISAGREE', B640_DEFECT_H)]


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**The repairs**', '**The rerun**', '**The pages**', '**The census at v0.7**', '**The Π⁰₁ form**', '**The second reader**',
                 '**The record lines**', '**The root.**', '**The scores.**', '**Read in mutual light**', 'strengthens', '**Next.**', 'b644')


def finding_ok(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    end = next((i for i in range(e, len(ls)) if ls[i].startswith('## ')), len(ls)) if e else 0
    tail = NL.join(ls[e - 1:end]) if e else ''
    return bool(e) and fline(S, e) == S['fj'].get('title') == S['REC'].TITLE and all(x in tail for x in ENTRY_NEEDLES)


def wl_ok(S):
    return bool(S['globs']) and all(any(fnmatch.fnmatch(f, p) for p in S['globs']) for f in S['written'])


def scored(S, k):
    v = S['sc'].get(k)
    return bool(v) and v[0].split(',')[0].split(' ')[0] in ('HELD', 'REFUTED', 'NOT', 'HOLDS', 'PENDING') and ('(%s)' % k) in S['desk']


def no_delete(S):
    words = ['os' + r'\.' + 'remove', 'os' + r'\.' + 'unlink', 'shutil' + r'\.' + 'rmtree', 'os' + r'\.' + 'rmdir',
             'rm' + ' -' + 'rf', 'Remove' + '-' + 'Item', r'\.' + 'unlink' + r'\(', 'git' + ' branch -' + 'D', 'worktree' + ' remove' + r'\b',
             'tag' + ' -' + 'd' + r'\b']
    pat = re.compile(r'(' + '|'.join(words) + r')')
    return bool(S['tooltext']) and not [f for f, t in S['tooltext'].items() if pat.search(t)]


def platform_free(S):
    lib = 'urllib' + '.request'
    return bool(S['tooltext']) and not [f for f, t in S['tooltext'].items() if lib in t or ('ZENODO' + '_TOKEN') in t or ('R9' + '.http') in t]


def kernels_untouched(S):
    f, n = S['kern_face'], S['kern_now']
    return bool(f) and len(f) == len(S['REC'].KERNS_READ) and all(k in n and n[k] == f[k] for k in f) \
        and S['trial'] == 'f22ff35' and S['lv_head'].startswith('2f71068a') and S['gs_diff'] == []


CORPUS = sorted(['FINDINGS.md', 'OPEN_TRAILS.md', PAGE, DIR_PAGE, K.CEN7])


def corpus_scope(S):
    return S['pp_changed'] == CORPUS


def closing_sentence_ok(S):
    t = S['closing_src']
    return ('no identifier of the author in any ' + 'outbound request') in t and ('plain requests to ' + 'github.com') in t \
        and (', no ' + 'outbound request,') not in t


def lsr_ok(S):
    lsr = S['lsr'] if S['lsr'] is not None else dict(KC0.LSR)
    return bool(lsr) and all(v <= 1 for v in lsr.values())


def g2_names(face):
    try:
        g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


READ_NEEDLES = ('data/b642_grades.txt @ 13b1c48b', 'data/b642_table.txt @ 13b1c48b', 'data/b642_nonvacuity.txt @ 13b1c48b',
                'data/b641_premise_status.txt @ 13b1c48b', 'data/b642_defects.txt @ 13b1c48b', 'tools/e0_rule.py @ 13b1c48b',
                'tools/terminal_table.py @ 13b1c48b', 'tools/b378_terminals.py @ 13b1c48b', 'tools/chain_page.py @ 13b1c48b',
                'data/b638_nodes_zeta.txt @ 13b1c48b', 'data/b638_nodes_chi.txt @ 13b1c48b', 'tools/act_root.py @ 13b1c48b',
                'tools/b634_elab.py @ 13b1c48b', 'THE_KEYSTONE_CENSUS_v0_6.md @ 69b74d08', 'data/glossary.txt @ 13b1c48b', ':13561 ', ':13535 ',
                'data/b642_closing_push_out.txt @ 3f9a7920', '### the local intake bank`s state: ?? data/b628_intake_crank_v0_5.txt')


def prompts_banked(S):
    return len(re.findall(r'^### PROMPT ', S['answers'], re.M))


def _rl(S, i, line, key='rl'):
    ls = list(S[key].get('lines') or [])
    ls[i:i + 1] = [dict(rline(S, i, key), line=line)]
    return put(S, key, dict(S[key], lines=ls))


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R253) END' in S['ferry'] and 'FERRY END (part 1 of 1)' in S['ferry'],
     lambda S: put(S, 'ferry', S['ferry'].replace('FERRY END (part 1 of 1)', ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-STEPZERO-CENSUS', 'the two censuses', lambda S: 'TOTAL MISSING : 0' in S['cens'] and 'TOTAL MISSING : 0' in S['fcens'],
     lambda S: put(S, 'cens', S['cens'].replace('TOTAL MISSING : 0', 'TOTAL MISSING : 1'))),
    ('G-STEPZERO-PINS', 'the pins', lambda S: '### REPOS HARD-FAILING : 0' in S['pins0'],
     lambda S: put(S, 'pins0', S['pins0'].replace('HARD-FAILING : 0', 'HARD-FAILING : 1'))),
    ('G-STEPZERO-PROCS', 'the process listing: tail named, every matched row stopped by PID', lambda S: procs_ok(S),
     lambda S: put(S, 'procs', S['procs'] + NL + ' 11 22 lean.exe  lean x')),
    ('G-STEPZERO-TESTS', 'the runner bank against the test files tracked at HEAD: every one clean but test_chain_page_b638.py (4)-(7), the page tests on the v0.26 lists',
     lambda S: tests_ok(S), lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-SEALED-AFTER-COMPONENTS', '(R253)(8): the lock time against every relay and PLACE-papers commit of the act by its subject',
     lambda S: sealed_after_ok(S), lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b643 record', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b642`s closing', lambda S: 'THE COMMITS, THE CENSUSES' in S['prior'] and 'b642' in S['prior'], lambda S: put(S, 'prior', '')),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: the component commits alone, each declared',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-R253-ENTERED', 'the ferry AND the trail', lambda S: 'RULING (R253) END' in S['ferry'] and S['ot'].count('**(R253) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R253) ratified', '**(R2530) ratified'))),
    ('G-READS-CITED', 'the reads bank', lambda S: all(x in S['reads'] for x in READ_NEEDLES) and 'NO SUCH LINE' not in S['reads'] and 'NO SUCH BLOB' not in S['reads'],
     lambda S: put(S, 'reads', S['reads'].replace(':13561 ', ':13560 '))),
    ('G-ANSWERS-BANKED', 'the answers bank as it prints: its count line against its prompts, every call`s result', lambda S: answers_ok(S),
     lambda S: put(S, 'answers', S['answers'].replace('prompt(s)', 'prompts'))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3)', lambda S: S['lock_epoch'] is not None
     and 'PRE-SEAL (R202)(3) READING' in S['prerun'] and ('ARMS RUN : %d.' % len(ARMS)) in S['prerun']
     and (utc_epoch(S['prerun'], 'run at (UTC)') or 10 ** 12) < S['lock_epoch'],
     lambda S: put(S, 'prerun', S['prerun'].replace('PRE-SEAL', 'POST-SEAL'))),
    ('G-PUSHOUT-COMMITTED', 'relay 3f9a7920`s files', lambda S: S['pushout'][0] == ['data/b642_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', ([], True))),
    ('G-BRANCHES-DELETED', 'the branch lists and the bank', lambda S: all(v == '' for v in S['push_lists'].values())
     and S['branches'].count('Deleted branch push-b642') == 6, lambda S: put(S, 'push_lists', {'x': 'push-b642'})),
    ('G-KEPT-BRANCHES', 'the explicit-formula kernel`s kept branch heads, v0.26-work among them', lambda S: all(S['kbranches'].get(b, '').startswith(v) for b, v in KEPT.items()),
     lambda S: put(S, 'kbranches', dict(S['kbranches'], **{'dedekind-b631': '0000000'}))),
    (CONTROL_ARM, 'b592`s lists, probes and table at relay 12c15c80, every PLACE-papers read at ba5f0ea and the E0 rule`s blob at 12c15c80',
     lambda S: len(S['ctl']) == 2 and all(x.get('ok') is True for x in S['ctl']) and S['ctl_arm'] + '-E0-12C15C80' == CONTROL_ARM,
     lambda S: put(S, 'ctl', [dict(x, ok=False) for x in S['ctl']])),
    (FROZEN_ARM, 'b622`s lists with every relay read at 84bae29a, the E0 rule`s and the generator`s blobs at 84bae29a, against the pages at 52822a5',
     lambda S: len(S['old_frozen']) == 2 and all(x.get('rc') == 0 and x.get('equal') is True for x in S['old_frozen']),
     lambda S: put(S, 'old_frozen', [dict(x, equal=False) for x in S['old_frozen']])),
    ('G-INSTRUMENTS-UNEDITED', 'b642`s tools, the readers, the reader`s tools, the shared tools, the rule`s tests, the generators and their tests, the roster, the builder and verifier, the row writer, the root tool against 13b1c48b',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'terminal_table.py': (b'a', b'b', b'b')}))),
    ('G-ABSENT-IS-NONE', 'the source builder on a file no act wrote and on empty bytes', lambda S: absent_ok(S), lambda S: put(S, 'absent', (b'', None, None))),
    ('G-SEAL-HASHES', 'the sealed tools` sha256 recorded at the seal against the tools on disk', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{K.SEALED[0]: '0' * 64}))),
    ('G-REPAIR-E0', 'relay 07c43e89 alone with tools/e0_rule.py and its planted test; the test 10 of 10 after the edit, 6 of 10 before',
     lambda S: repair_ok(S, S['rfiles_e0'], K.E0_TOOL, K.E0_TEST, 6, 10), lambda S: put(S, 'rfiles_e0', S['rfiles_e0'] + ['tools/x.py'])),
    ('G-REPAIR-PRIMED', 'relay 213902e2 alone with tools/b378_terminals.py and its planted test; the test 8 of 8 after the edit, 3 of 8 before',
     lambda S: repair_ok(S, S['rfiles_b378'], K.B378_TOOL, K.B378_TEST, 3, 8), lambda S: put(S, 'repairs', S['repairs'].replace('3 of 8', '9 of 8'))),
    ('G-CONTDIFF-DATA', 'the live rule: n : WithTop ℕ∞ types data and contDiff_riemannZeta₀`s header grades DERIVES', lambda S: S['contdiff'] == ('data', 'DERIVES'),
     lambda S: put(S, 'contdiff', ('prop', 'INTERFACES'))),
    ('G-PRIMED-GRADED', 'the regenerated table: the three primed rows resolved and graded', lambda S: primed_ok(S),
     lambda S: put(S, 'trows', dict(S['trows'], **{PRIMED[0]: dict(S['trows'].get(PRIMED[0]) or {}, grade='—')}))),
    ('G-RERUN-BANKED', 'the rerun bank: one elaborated move (contDiff_riemannZeta₀ INTERFACES to DERIVES); the table 12 rows moved, 5 in grade, none added or gone',
     lambda S: rerun_ok(S), lambda S: put(S, 'rerun', dict(S['rerun'], moves=[]))),
    ('G-WEIGHT-LINE', 'FINDINGS at the banked line: b642`s weight, its figures from its banks',
     lambda S: landed(S, 0, ('(:7965)', '82550e4', 'REFUTED IN ONE CLAUSE', '83 of 85', 'defect (k)', 'DEGENERATE')), lambda S: _rl(S, 0, 1)),
    ('G-WATCHDOG-LINE', 'OPEN_TRAILS at the banked line: W-ORD-WATCHDOG-STOP with its price and trigger',
     lambda S: landed(S, 1, ('W-ORD-WATCHDOG-STOP', 'one act', 'Trigger: a second act with lows beneath the hold')), lambda S: _rl(S, 1, 1)),
    ('G-DEFECT-J-LINE', 'OPEN_TRAILS at the banked line: the navigator`s defect (j) beneath the squeeze`s correction',
     lambda S: landed(S, 2, ('(:13527)', ':2485', ':2457', 'navigator')), lambda S: _rl(S, 2, 1)),
    ('G-PIN-LINES', 'the lists in force against b638`s: the pin line alone moved, v0.25 to v0.26', lambda S: pins_ok(S),
     lambda S: put(S, 'nodes', dict(S['nodes'], chi=(S['nodes']['chi'][0], (S['nodes']['chi'][1] or b'') + b'x')))),
    ('G-PAGES-AT-V026', 'both page banks against the probes and PLACE-papers HEAD: re-emitted from the banked probe equal to the run, written, the Correspondence 443 to 497 and 351 to 391, no row removed',
     lambda S: pages_ok(S), lambda S: put(S, 'pagej', dict(S['pagej'], chi=dict(S['pagej']['chi'], corr_after=390)))),
    ('G-PAGE-ARMS-BANKED', 'the page arms bank: 2 of 2, the frozen control 2 of 2', lambda S: '**PAGE ARMS PASSING : 2 of 2.**' in S['pga'] and S['pga'].count('PASSING : 2 of 2.') == 2,
     lambda S: put(S, 'pga', S['pga'].replace('2 of 2', '1 of 2', 1))),
    ('G-CHAIN-PAGE', 'the ζ page re-emitted from this act`s list and probe against PLACE-papers HEAD', lambda S: S['gcp_zeta'].get('ok') is True,
     lambda S: put(S, 'gcp_zeta', dict(S['gcp_zeta'], ok=False))),
    ('G-CHAIN-PAGE-CHI', 'the χ page re-emitted from this act`s list and probe against PLACE-papers HEAD', lambda S: S['gcp_chi'].get('ok') is True,
     lambda S: put(S, 'gcp_chi', dict(S['gcp_chi'], ok=False))),
    ('G-GLOSSARY-SIX', 'data/glossary.txt against 13b1c48b: the six entries appended in order, CHAIN in the author`s words', lambda S: glossary_six_ok(S),
     lambda S: put(S, 'glossary', S['glossary'].replace('named by its terminal declaration', 'named by its head'))),
    ('G-GLOSSARY-EVERYWHERE', '(N4): the glossary block on both pages at PLACE-papers HEAD and in the census at v0.7, byte for byte the live builder`s, the six entries in it',
     lambda S: glossary_everywhere_ok(S), lambda S: put(S, 'gl_census', (S['gl_census'] or [''])[:-1])),
    ('G-CONSUMERS', 'the consumers bank and the dependency print: 50 heads each with a count, every kernel read, every failed call noted and run again clean',
     lambda S: consumers_ok(S), lambda S: put(S, 'cj', dict(S['cj'], rows=(S['cj'].get('rows') or [])[:49]))),
    ('G-HINGES-NAMED', 'the consumers bank: every hinge with its kernels or its chains, each chain named by its terminal declarations', lambda S: hinges_ok(S),
     lambda S: put(S, 'cj', dict(S['cj'], rows=[dict(r, hinge_kernels=[], hinge_chains=[]) for r in S['cj'].get('rows') or []]))),
    ('G-PREMISE-TABLE', 'the premise table: 50 heads, one status of six, one non-vacuity value, the three DEGENERATE never WITNESSED', lambda S: premise_table_ok(S),
     lambda S: put(S, 'ptj', dict(S['ptj'], rows=[dict(r, nonvacuity='WITNESSED') if r['nonvacuity'] == 'DEGENERATE' else r for r in S['ptj'].get('rows') or []]))),
    ('G-EDITION', 'the census at v0.7 at PLACE-papers HEAD against its bank; v0.6 unedited; no v0.6 line removed outside the glossary block', lambda S: edition_ok(S),
     lambda S: put(S, 'ediff', S['ediff'].replace('GLOSSARY BLOCK : 0.', 'GLOSSARY BLOCK : 1.'))),
    ('G-OUTSIDE-NAMED-NOWHERE', 'the census at v0.7 and every byte the act appends to the ledgers: no outside collection named', lambda S: S['outside'] == [],
     lambda S: put(S, 'outside', ['x'])),
    ('G-PI01-ATTEMPTED', 'the attempt bank (two sources, none reached) and the census: the paragraph not written, its absence said in back matter', lambda S: pi01_ok(S),
     lambda S: put(S, 'pi', S['pi'].replace('REACHED AND READ 0', 'REACHED AND READ 1'))),
    ('G-READER-SCORED', 'the reader`s bank: three answers from off D:\\, the needles and the hand figure both printed, no project memory in the run', lambda S: reader_ok(S),
     lambda S: put(S, 'rdj', dict(S['rdj'], hand=None))),
    ('G-TABLE-FINAL', 'the final table bank against the table committed at Component 2: no row moved, added or gone', lambda S: table_final_ok(S),
     lambda S: put(S, 'tfj', dict(S['tfj'], gone=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s b643 line, the root bank and its items: previous b642`s root, the premise table among the banks',
     lambda S: root_banked_ok(S), lambda S: put(S, 'rootsf', S['rootsf'] + 'b643 x y' + NL)),
    ('G-ACTROOT-LAST', 'the root bank`s time against every bank it names, the seal bank among them (W-ORD-ROOT-ORDER)', lambda S: root_last_ok(S),
     lambda S: put(S, 'arj', dict(S['arj'], at_epoch=0.0))),
    ('G-ACTROOT-MIDPUSH', 'the root`s relay and PLACE-papers heads against the read-backs of the pushes before it', lambda S: midpush_ok(S),
     lambda S: put(S, 'rpush', S['rpush'].replace('main read back at the remote: ', 'main read back at the remote: 0', 1))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed by this suite, one remote read per repository: b624 to b639 and b641 to b643 AGREE, b640 DISAGREE on its two re-banked files alone',
     lambda S: verify_ok(S), lambda S: put(S, 'ar_verify', [(a, 'DISAGREE' if a == 'b643' else v, w) for a, v, w in S['ar_verify']])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the banked line, the entry read to the next heading', lambda S: finding_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS at the banked line', lambda S: oline(S, S['tj'].get('line')) == S['REC'].TRAIL_HEAD(), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'this act`s trail record: the root and its previous', lambda S: bool(S['arj'])
     and ('**Act root:** b643 `%s` (previous `%s`' % (S['arj'].get('root'), S['arj'].get('previous'))) in trail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-TERMINALS', 'this act`s trail record: the next act named without a kernel terminal', lambda S: 'b644 names no kernel terminal' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b644 names no kernel terminal', 'x'))),
    ('G-TRAIL-CARRIES-SEAL', 'this act`s trail record: every sealed tool agreeing at the record', lambda S: all(
        ('%s agree' % t_) in trail(S) for t_ in K.SEALED), lambda S: put(S, 'ot', S['ot'].replace('%s agree' % K.SEALED[0], '%s differ' % K.SEALED[0]))),
    ('G-RESOLVED-RECORDED', 'this act`s trail record: the strike items and the prompts, counted from the answers bank', lambda S: 'Resolved by the seat, for the author’s strike' in trail(S)
     and ('**Prompts to the author:** %d ' % prompts_banked(S)) in trail(S), lambda S: put(S, 'answers', S['answers'] + NL + '### PROMPT 9 (x): y')),
    ('G-NEXT-ACT-NAMED', 'this act`s trail record', lambda S: 'b644, the author’s word pending' in trail(S),
     lambda S: put(S, 'ot', S['ot'].replace('b644, the author’s word pending', 'b645'))),
    ('G-CURRENTS-UNEDITED', 'the current versions -- ERRATA, SPIRAL_MAP, README, REGISTRY, the census at v0.4, v0.5 and v0.6, v5.18, the sieve and the seven companions -- against 69b74d0',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'ERRATA.md': (b'a', b'b', b'a')}))),
    ('G-NODISCLOSURE-PUBLIC', 'the no-disclosure arm on every public byte this act writes: the ledger appends, the census, both pages, its banks, its tools, the roots file, the glossary',
     lambda S: not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', dict(S['nd_pub'], method=1))),
    ('G-KERNELS-UNTOUCHED', 'every kernel this act reads, none written: main, tags by peel, branches and status against the face; SIDE-global-section unchanged',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', dict(S['kern_now'], **{'SIDE-kernel': ['0000000', {}, [], '']}))),
    ('G-SORRY-TOKENS', 'the explicit-formula kernel`s main, comments stripped: no sorry token', lambda S: S['sorry_tokens'] == 0,
     lambda S: put(S, 'sorry_tokens', 1)),
    ('G-TECHNE-UNPUSHED', 'TECHNE-Core`s HEAD, its remote-tracking main and its status', lambda S: S['te'] == ('36352a0', '29208f6', ''),
     lambda S: put(S, 'te', ('x', 'y', ''))),
    ('G-DELETE-FREE', 'this act`s tools, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], **{os.path.join(T, 'b643_record.py'): S['tooltext'].get(os.path.join(T, 'b643_record.py'), '') + NL + 'os' + '.remove(p)'}))),
    ('G-PLATFORM-FREE', 'this act`s tools: no request library, no platform token, no route call', lambda S: platform_free(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='import urllib' + '.request'))),
    ('G-ERRATA-UNTOUCHED', 'ERRATA.md against its pre-act blob', lambda S: S['errata'][1] is not None and S['errata'][0] == S['errata'][1],
     lambda S: put(S, 'errata', (b'x', S['errata'][1]))),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 13b1c48b, by blob id, the roots file and the glossary read by their own arms', lambda S: S['prior_n'] > 0 and S['prior_bad'] == [],
     lambda S: put(S, 'prior_bad', ['data/x'])),
    ('G-CORPUS-SCOPE', 'PLACE-papers` changed files: the ledgers, the two pages and the census at v0.7', lambda S: corpus_scope(S),
     lambda S: put(S, 'pp_changed', S['pp_changed'] + ['SPIRAL_MAP.md'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS -- its pre-act blob a true prefix', lambda S: S['fi_pre'] is not None and S['fi_now'] is not None
     and S['fi_now'].startswith(S['fi_pre']) and len(S['fi_now']) > len(S['fi_pre']), lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS -- its pre-act blob a true prefix', lambda S: S['ot_pre'] is not None and S['ot_now'] is not None
     and S['ot_now'].startswith(S['ot_pre']) and len(S['ot_now']) > len(S['ot_pre']), lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-TABLE-UNMOVED', 'the suite`s own regeneration against the table before it: no row added or gone and no grade cell moved', lambda S: S['table_changed'] == [],
     lambda S: put(S, 'table_changed', [['x']])),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present on disk, in no relay commit of any branch, not in the index, untracked', lambda S: local_ok(S),
     lambda S: put(S, 'local_log', 'abc1234')),
] + [('G-N%d-SCORED' % i, 'the scores and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i), lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3', 'S4', 'S5')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written, against the (W) globs', lambda S: wl_ok(S),
     lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b643')" in S['suite'] and "'data/b643_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b643_closing.py: the closing sentence in the rule`s words with the plain reads named', lambda S: closing_sentence_ok(S),
     lambda S: put(S, 'closing_src', S['closing_src'].replace('no identifier of the author in any ' + 'outbound request', 'x'))),
    ('G-LSREMOTE-ONE-PER-REPO', 'the whole run`s ls-remote calls per repository, read after every other arm has run (OPEN_TRAILS :12703)',
     lambda S: lsr_ok(S), lambda S: put(S, 'lsr', {PP: 2})),
]


def regenerate():
    r = subprocess.run([sys.executable, os.path.join(T, 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8', errors='replace')
    try:
        diff = json.loads(rd('terminal_table_diff.json') or '{}')
    except Exception:
        diff = {}
    return r.returncode, diff


def seal():
    """### (R246)(3): the sha256 of every sealed tool, recorded at the seal; refuses before the face is locked or once recorded."""
    import time
    face = read(FACE)
    lock = utc_epoch(face, 'locked at (UTC)')
    p = os.path.join(D, 'b643_seal_hashes.json')
    if lock is None:
        print('### THE FACE IS NOT LOCKED -- NOTHING RECORDED')
        return 3
    if os.path.exists(p):
        print('### THE HASHES ARE RECORDED ALREADY -- NOTHING RECORDED TWICE')
        return 3
    now = sealed_now()
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), lock=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(lock)), tools=now,
             relay_head=gs(ROOT, 'rev-parse', 'HEAD'))
    b = (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    for t in K.SEALED:
        print('  %-22s %s' % (t, now[t]))
    print('  written: b643_seal_hashes.json')
    return 0


def main():
    import time
    if SEAL:
        return seal()
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b643 -- THE SUITE. ### **%s READING.** ### every arm exercised on both controls.' % (
        'PRE-SEAL (R202)(3)' if PRERUN else 'MID-ACT' if MID else 'POST-PUSH' if pushed else 'PRE-PUSH'))
    if PRERUN or MID:
        rec('### run at (UTC) : %s   ### %s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                                              'the standing line of (R202)(3): every arm run at HEAD before the face is sealed, its count printed.'
                                              if PRERUN else 'a mid-act re-run; no table regenerated.'))
    rec('=' * 104)
    S = sources()
    S['pushed'] = pushed
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
    sj = S['sealj'].get('tools') or {}
    rec('  ### THE SEALED TOOLS, recorded at the seal %s : %s' % (S['sealj'].get('at', '### NOT RECORDED'), '; '.join(
        '%s %s' % (t, ('agree' if sj.get(t) == S['sealnow'].get(t) else 'DIFFER') if t in sj else 'not recorded') for t in K.SEALED)))
    rec('  ### the live rule on contDiff_riemannZeta₀`s binder and header: %s ; the hinges the consumers bank marks: %d' % (
        S['contdiff'], sum(1 for r in S['cj'].get('rows') or [] if r.get('hinge'))))
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
    rec('  ### tracked files written (%d), each against the (W) globs: uncovered %s' % (len(S['written']), [f for f in S['written']
                                                                                          if not any(fnmatch.fnmatch(f, p) for p in S['globs'])] or 'NONE'))
    rec('  ### G-PRIORBANK-UNCHANGED checked %d relay data banks tracked at %s by blob id; changed %s' % (S['prior_n'], PRE['relay'], S['prior_bad'] or 'NONE'))
    lsr = dict(KC0.LSR)
    rec('  ### OPEN_TRAILS :12703: ls-remote calls this run, per repository: %d repositories, at most %d each' % (len(lsr), max(lsr.values()) if lsr else 0))
    if not (RERUN or PRERUN or MID):
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d %s' % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
                                                                                 len(gen_diff.get('changed') or []), (gen_diff.get('changed') or '')[:20]))
    rec('  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (len(ARMS), len(ARMS) - len(fail), len(fail), fail or ''))
    rec('  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (negfail, len(defective), defective or ''))
    ok = not fail and not defective and negfail == 0 and S['declared_eq_run']
    rec('  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'))
    rec('=' * 104)
    if PRERUN:
        out = os.path.join(D, 'b643_arms_prerun.txt')
    elif MID:
        out = os.path.join(D, sys.argv[sys.argv.index('--mid') + 1])
    else:
        out = os.path.join(D, sys.argv[sys.argv.index('--rerun-postpush') + 1] if RERUN else ('b643_checks_postpush.txt' if pushed else 'b643_checks.txt'))
    b = (NL.join(L) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
    os.replace(out + '.tmp', out)
    lp = out.replace('b643_arms_prerun.txt', 'b643_lsr_prerun.json').replace('b643_checks', 'b643_lsr').replace('.txt', '.json')
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(ARMS), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b643_exercise.json')
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
