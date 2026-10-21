# -*- coding: utf-8 -*-
"""b699_checks.py -- THE SUITE OF b699, UNDER (R309): b698 AT ITS WEIGHT; THE UNDECLARED FAILURE AND THE POST-ROOT REWRITE BY CORRIGENDUM;
SIDE-substrate-cluster CUT UNDER THE QUOTATION RULE; THE ARCHIMEDEAN CELLS REGENERATED; THE BRIDGE PRICED; SIX PARTS, THE CHAIN SPLIT BY ACT.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### data/b684_rules.txt row (1) and b693's split: every run in SIX foreground parts, each its own call in its own message -- `--part
### standing-a`, `--part standing-c` (G-PRIORBANK-UNCHANGED, G-NODISCLOSURE-PUBLIC, G-WRITELIST-KINDS), `--part standing-b1` (the shared
### additive files), `--part standing-b2` (the act-root chain's first half, b624-b658, its verdicts banked, NO ARM), `--part standing-b3` (the
### second half, b659-b699, and G-ACTROOT-VERIFY once over both halves' verdicts), `--part act` (the act's arms over this act's banks, the
### table regenerated in a closing run); each under the 590 s guard the seat runs it in, and NOT RUN beneath the 2,560 MB hold; `--combine
### <bank>` writes the bank. The chain halves as b693 drew them with b699 added to the second (the ferry's Component 4).
### ### (R264)(2), THE FREEZE: the standing arms are b698's face's (G2) arms less b698's own arms over b698's banks, carried, the twenty-four
### rule arms of tools/rule_arms.py among them, unedited; no standing arm added (N5). The act's own arms read this act's banks alone (ACT_ARMS).
### This act dispatches the runner twice, once per tree state, for the re-cut of SIDE-substrate-cluster: the standing runner arms read this
### act's two runs at SIDE-substrate-cluster, its one merge and its one tag (b695's form for an act with a runner).
### ### Every look-up of a landed line goes through the one conversion (imported from tools/b652_record.py through tools/b699_record.py).
### ### The harness is b568's to b698's, written by the Write tool from tools/b698_checks.py; the sources, predicates and arms over this act's
### ### banks are b699's. data/b686_rules.txt row (1): the act arm G-ENTRY-SCORES-EQUAL reads the landed entry; no scorer reads a ledger line.
"""
import copy
import ctypes
import fnmatch
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b616_claims as KC0     # noqa: E402
import b699_worklist as K     # noqa: E402
import b698_worklist as K698  # noqa: E402
import b697_worklist as K697  # noqa: E402
import b696_worklist as K696  # noqa: E402
import b695_worklist as K695  # noqa: E402
import b694_worklist as K694  # noqa: E402
import b693_worklist as K693  # noqa: E402
import rule_arms as RA        # noqa: E402
from b699_record import conv  # noqa: E402

NL = chr(10)
PP = K.PP
KI = K.KERNEL_DIR
FACE = os.path.join(D, 'b699_registration_2026-10-21.txt')
B698_FACE = os.path.join(D, 'b698_registration_2026-10-21.txt')
B698_ACT_ARMS = K698.ACT_ARMS
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP)
EXPORT = K.EXPORT
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
SEAL = '--seal' in sys.argv
COMBINE = '--combine' in sys.argv
PART = sys.argv[sys.argv.index('--part') + 1] if '--part' in sys.argv and len(sys.argv) > sys.argv.index('--part') + 1 else None
L = []
# ### the sealed figures, the floors the count arms read at HEAD (standing from (R291)(3))
FLOORS = dict(prompts=4, calls=3, checks=4, defects=(('a', 'SEAT'), ('b', 'SEAT')))
REPAIRED_TOOLS = K.REPAIRED_TOOLS
NEW_TOOLS = K.NEW_TOOLS
# ### the instruments read unedited: b698's list, b693's to b698's sealed tools and b698's reader among them, less this act's sealed tools
INST_BASE = ('b690_corrigendum.py', 'b690_readings.py', 'b690_record.py', 'b689_corrigendum.py', 'b689_constants.py', 'b687_readings.py',
             'b685_count.py', 'b683_epstein_map_angle.py', 'correspondence_gen.py', 'test_correspondence_gen.py', 'b681_narrow.py',
             'b680_readings.py', 'b680_rules_index.py', 'b680_fig_tie.py', 'b680_fig_q0.py', 'b680_fig_li.py', 'b679_q0_membership.py',
             'b679_onset.py', 'b678_corrigendum.py', 'b677_epstein_map_angle.py', 'b675_li_bench.py', 'b695_corrigendum.py',
             'b670_record.py', 'b669_record.py', 'b667_epstein_certify.py', 'b667_epstein_map_balls.py', 'b667_tail_recheck.py',
             'b663_epstein_map.py', 'b655_record.py', 'edit_route.py', 'test_edit_route_b646.py', 'b652_record.py', 'b651_record.py',
             'b649_record.py', 'b648_record.py', 'b646_record.py', 'b645_record.py', 'b644_record.py', 'b643_record.py', 'b641_record.py',
             'b633_record.py', 'b616_record.py', 'additive_shared.py', 'premise_status.py', 'terminal_table.py',
             'banned_terms.py', 'reg_seal.py', 'b378_lockgate.py', 'push_gated.sh', 'table_gate.py', 'mirror_build.ps1', 'mirror_verify.py',
             'b616_claims.py', 'ferry_scan.py', 'e0_rule.py', 'test_e0_rule.py', 'build_watch.py', 'chain_page.py', 'ledger_split.py',
             'axiom_claim.py', 'licensed_table.py', 'registration_gate.py', 'b300_regspec.py', 'no_sorry_main.py', 'module_header.py',
             'test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py', 'test_act_root.py',
             'test_act_root_commit_b644.py', 'test_act_root_order_b641.py', 'act_root.py', 'repair_snapshot.py', 'b672_record.py',
             'rowgen/rowgen.py', 'rowgen/diff_rowpin.py', 'rowgen/namemap.json', 'circuit_read.py', 'test_push_gated.sh', 'rule_arms.py',
             'b511_families.py', 'b514_window.py', 'b518_window.py', 'b325_epstein.py', 'b326_windows.py', 'b677_citation.py', 'b682_citation.py',
             'circuit_correspondence.py')
INST = tuple(sorted((set(INST_BASE) | set(K693.SEALED) | set(K694.SEALED) | set(K695.SEALED) | set(K696.SEALED) | set(K697.SEALED) | set(K698.SEALED))
                    - set(K.SEALED) - set(REPAIRED_TOOLS) - set(NEW_TOOLS)))
# ### the corpus documents this act does not write: the faces page, both SIMPLICITY copies, the PATHS partner copy and the substrate pages
# ### among them; PATHS_TO_THE_CRITICAL_LINE_v0_7.md is written this act through the generator on the author's word ((R309)(4)) and so not here
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md',
            'phase2/method/THE_KEYSTONE_CENSUS_v0_8.md', 'day1/A_Place_to_Stand_v5_18.md',
            'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md', 'day1/ONE_PAGE_PROOF.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md',
            'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md', 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', 'README.md',
            'REGISTRY.md', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md',
            'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md', 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md',
            'phase1.5/method/INSTRUMENTS.md', 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md',
            'phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md', 'phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM_v0_2.md')
TABLE_FILES = K.TABLE_FILES
WF, PT, CUT_FILE = '.github/workflows/build-module.yml', 'print_targets.txt', 'SIDESubstrateCluster/T7Labeling.lean'
B1_ARMS = ('G-SHARED-ADDITIVE',)        # ### standing-b1: the shared additive files
B2_ARMS = ()                            # ### standing-b2: the chain's first half, its verdicts banked, no arm
B3_ARMS = ('G-ACTROOT-VERIFY',)         # ### standing-b3: the chain's second half and the arm over both halves
C_ARMS = ('G-PRIORBANK-UNCHANGED', 'G-NODISCLOSURE-PUBLIC', 'G-WRITELIST-KINDS')   # ### standing-c's arms: the written files
NEED = {'standing-a': ('live', 'rules'), 'standing-c': ('written',), 'standing-b1': ('additive',), 'standing-b2': ('chain_a',),
        'standing-b3': ('chain_b',), 'act': ()}
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
STD3 = ('Classical.choice', 'Quot.sound', 'propext')


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


def read_blob(repo, spec):
    b = blob(repo, spec)
    return b.decode('utf-8', 'replace').replace(chr(13), '') if b is not None else ''


def iso_epoch(s):
    import calendar
    try:
        return calendar.timegm(time.strptime(s, '%Y-%m-%dT%H:%M:%SZ'))
    except Exception:
        return None


def utc_epoch(text, label):
    m = re.search(re.escape(label) + r'[^0-9]*(\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)', text)
    return iso_epoch(m.group(1)) if m else None


def head_epoch(text):
    m = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', (text or '').split(NL)[0])
    return iso_epoch(m.group(1)) if m else None


def free_mb():
    class MS(ctypes.Structure):
        _fields_ = [('dwLength', ctypes.c_ulong), ('dwMemoryLoad', ctypes.c_ulong), ('ullTotalPhys', ctypes.c_ulonglong),
                    ('ullAvailPhys', ctypes.c_ulonglong), ('ullTotalPageFile', ctypes.c_ulonglong), ('ullAvailPageFile', ctypes.c_ulonglong),
                    ('ullTotalVirtual', ctypes.c_ulonglong), ('ullAvailVirtual', ctypes.c_ulonglong), ('ullAvailExtendedVirtual', ctypes.c_ulonglong)]
    m = MS()
    m.dwLength = ctypes.sizeof(MS)
    ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(m))
    return int(m.ullAvailPhys // (1024 * 1024))


def is_pushed():
    return (gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b699')
            and 'data/b699_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def strip_prose(t):
    t = re.sub(r'"""[\s\S]*?"""', '', t)
    t = re.sub(r"'''[\s\S]*?'''", '', t)
    return NL.join(l.split('#', 1)[0] for l in t.split(NL))


def wl_globs(face):
    try:
        w = face[face.index('### (W) THE WRITE LIST.'):face.index('### (Z) THE NOTHINGS.')]
    except ValueError:
        return []
    return sorted(set(re.findall(r'`((?:relay|PLACE-papers)/[^`\s]+)`', w)))


def written_files():
    res = []
    for repo, name, pre in ((ROOT, 'relay', PRE['relay']), (PP, 'PLACE-papers', PRE['pp'])):
        ch = set(x for x in gs(repo, 'diff', '--name-only', pre).split(NL) if x.strip())
        ch |= set(x for x in gs(repo, 'diff', '--name-only', pre, 'HEAD').split(NL) if x.strip())
        res += ['%s/%s' % (name, x) for x in ch]
    return sorted(res)


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


def capture_now():
    import b699_record as REC
    return REC.capture()


def prev_now():
    import b699_record as REC
    return REC.prev_capture()


def run_test(name):
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, name)], capture_output=True, text=True, encoding='utf-8', errors='replace')
    return dict(rc=r.returncode, out=r.stdout or '')


def live_arms():
    import no_sorry_main as NSM
    import axiom_claim as AC
    import module_header as MH
    names = NSM.kernels()
    t0 = time.time()
    nsm = NSM.run(names, KC0.remote_refs)
    t1 = time.time()
    idx, counts = AC.index()
    ac_rows, ac_per = AC.run(names, idx)
    t2 = time.time()
    mh_per, mh_rows = MH.run(names)
    t3 = time.time()
    return dict(names=names, nsm=nsm, ac=ac_rows, ac_counts=counts, mh=mh_rows, mh_per=mh_per, secs=(t1 - t0, t2 - t1, t3 - t2))


def conv_alone():
    P = 'p' + 'oss('
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to',
            'def ' + 'conv(']
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b699_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks):
                bad.append(f)
    return bad


def spec_planted():
    import b699_regspec as SPEC
    P = SPEC.planted()
    ctl = [ok for _w, ok in SPEC.controls()]
    return dict(read=[ok for _s, ok, _w in P], controls=ctl, shapes=[s for s, _o, _w in P])


def _deps(ax):
    import b699_record as REC
    return REC._deps(ax)


def wf_state():
    """this act's kernel workflow (SIDE-substrate-cluster's, written this act at cebec19 and unedited after): its workflow at main against that
    write, its dependency form read from its tree, its print list against the after-run's print bank, and the files b699 wrote on its main."""
    t = read_blob(KI, 'main:' + WF)
    lf = read_blob(KI, 'main:lakefile.toml') + read_blob(KI, 'main:lakefile.lean')
    req = re.search(r'(?im)^\s*require\b[^\n]*mathlib', lf) or re.search(r'(?is)\[\[require\]\][^\[]*name\s*=\s*"mathlib"', lf)
    pt = read_blob(KI, 'main:' + PT)
    return {K.KERNEL: dict(text=t, before=read_blob(KI, '%s:%s' % (K.KI_WF, WF)), lakefile=bool(lf.strip()), mathlib=bool(req),
                           targets=[l.strip() for l in pt.split(NL) if l.strip()],
                           printed=len(_deps(rd('b699_axioms_SIDE-substrate-cluster_after.txt'))),
                           act_writes=sorted(set(x for x in gs(KI, 'diff', '--name-only', K.KI_BEFORE, 'main').split(NL) if x.strip())),
                           want=sorted([WF, PT, CUT_FILE]))}


def main_state():
    """SIDE-substrate-cluster's main after b699's re-cut: its tip, its first-parent line back to the main before b699, the merge's parents, the
    files the cut wrote, the tags peeled, the merge's tree against the gated tip's, the tag's message."""
    line = gs(KI, 'rev-list', '--first-parent', '--abbrev-commit', '--abbrev=7', '%s..main' % K.KI_BEFORE).split()
    return dict(main=gs(KI, 'rev-parse', '--short=7', 'main'), line=list(reversed(line)),
                parents=gs(KI, 'log', '-1', '--format=%p', '--abbrev=7', K.KI_MERGE).split(),
                files=dict((c, files_of(KI, c)) for c in (K.KI_CUT, K.KI_WF, K.KI_PT)),
                tags=sorted(set(sum((gs(KI, 'tag', '--points-at', c).split() for c in (K.KI_WF, K.KI_PT, K.KI_CUT, K.KI_MERGE)), []))),
                tag=gs(KI, 'rev-parse', '--short=7', K.NEXT_TAG + '^{commit}'), prior=gs(KI, 'rev-parse', '--short=7', K.PRIOR_TAG + '^{commit}'),
                trees=(gs(KI, 'rev-parse', K.KI_MERGE + '^{tree}'), gs(KI, 'rev-parse', K.KI_CUT + '^{tree}')),
                tagmsg=gs(KI, 'tag', '-l', '-n9', K.NEXT_TAG))


def g2_of(path):
    t = read(path)
    try:
        g2 = t[t.index('### (G2) THE GATE ARMS.'):t.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


STANDING = sorted((set(g2_of(B698_FACE)) - set(B698_ACT_ARMS)) | set(K.STANDING_ADDED))
TESTS = ('test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py')


def _ct(repo, rev):
    t = gs(repo, 'log', '-1', '--format=%ct', rev)
    return int(t) if t.isdigit() else None


def _root_named_at_commit(arj):
    commit = (arj.get('commit') or {}).get('relay') or ''
    out = []
    for it in arj.get('items') or []:
        p = it.split()
        if p[0].startswith('data/') and len(p) == 2:
            b = blob(ROOT, '%s:%s' % (commit, p[0])) if commit else None
            out.append((p[0], b is not None, b is not None and hashlib.sha256(b).hexdigest() == p[1]))
    return out


# ================================================================== THE CHAIN SPLIT BY ACT (b693's, the halves as b693 drew them, b699 added)
def chain_names():
    return [l.split()[0] for l in rd('act_roots.txt').split(NL) if l.strip() and not l.startswith('corrigendum ')]


def half_acts(i):
    lo, hi = (int(x[1:]) for x in K.CHAIN_HALVES[i])
    return [a for a in chain_names() if lo <= int(a[1:]) <= hi]


def boundary():
    a, b = K.CHAIN_HALVES[0][1], K.CHAIN_HALVES[1][0]
    rows = dict((l.split()[0], l.split()) for l in rd('act_roots.txt').split(NL) if l.strip() and not l.startswith('corrigendum '))
    ra, rb = rows.get(a) or [], rows.get(b) or []
    root_a, prev_b = (ra[1] if len(ra) > 1 else ''), (rb[2] if len(rb) > 2 else '')
    return dict(first=a, second=b, root=root_a, previous=prev_b, equal=bool(root_a) and root_a == prev_b)


def half_verify(i):
    import act_root as AR
    acts = set(half_acts(i))
    try:
        v = AR.verify(remote=KC0.remote_refs, acts=acts)
        reads = dict((k, v_) for k, v_ in dict(AR.READS_AT).items() if k in acts)
    except Exception as e:
        v, reads = [('raised', type(e).__name__, [])], {}
    return [list(x) for x in v], reads


def _run_key(base):
    return base.replace('b699_', '').replace('.txt', '')


def half_bank(i, key):
    return 'b699_chain_half_%s_%s.json' % ('ab'[i], key)


def write_half(i, key, verdicts, reads):
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), head=gs(ROOT, 'rev-parse', 'HEAD'), half='%s-%s' % K.CHAIN_HALVES[i],
             acts=verdicts, reads=reads, boundary=boundary())
    p = os.path.join(D, half_bank(i, key))
    with open(p + '.tmp', 'wb') as fh:
        fh.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)


def sources(need=()):
    """the sources the arms read; `need` (by part) names the heavy phases this part computes: 'live' (the three arms at HEAD), 'rules' (the
    rule arms' trace), 'written' (the written files, the public bytes, the prior banks), 'chain_a' and 'chain_b' (the act-root chain's two
    halves), 'additive' (the shared files)."""
    import b699_record as REC
    import b616_record as R6
    import edit_route as ER
    import b641_record as R41
    import additive_shared as ADD
    face = read(FACE)
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b699_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if (f.startswith('b699_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS)
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    cit = jl('b699_citation_check.json')
    t0 = time.time()
    S = dict(
        REC=REC, ER=ER, face=face, ferry=rd('b699_ferry.txt'), scan=rd('b699_ferry_scan.txt'), stepz=rd('b699_stepzero.txt'),
        readfirst=rd('b699_readfirst.txt'), defects=rd('b699_defects.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        answers=rd('b699_author_answers.txt'), answersj=jl('b699_author_answers.json'), prerun=rd('b699_arms_prerun.txt'), rl=jl('b699_record_lines.json'),
        tests=jl('b699_tests_stepzero.json'), testst=rd('b699_tests_stepzero.txt'), withheld=jl('b699_tests_withheld.json'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b699_seal_hashes.json'), sealnow=sealed_now(), cmds=capture_now(), prev_cmds=prev_now(), cmdj=jl('b699_commands.json'),
        cmdt=rd('b699_commands.txt'), reads_bank=rd('b699_read_calls.txt'),
        planted={t: run_test(t) for t in TESTS}, spec=spec_planted(), conv_bad=conv_alone(), suite=read(os.path.join(T, 'b699_checks.py')),
        citation=rd(K.CITATION_BANK), cit_at=iso_epoch(cit.get('at') or ''), cit_misses=cit.get('misses') or [],
        gate=rd('b699_reg_gate.txt'), rowgen=rd('b699_rowgen_stepzero.txt'),
        branchj=jl('b699_branches.json'), branchbj=jl('b699_branches_before.json'), branchest=rd('b699_branches.txt'),
        branch_lists=dict((repo, gs(repo, 'branch', '--list', *bs)) for repo, bs in K.DELETE),
        repairs=rd('b699_tool_repairs.txt'), rec_src=read(os.path.join(T, 'b699_record.py')),
        closing_src=read(os.path.join(T, 'b699_closing.py')), corrigenda=rd('b675_corrigenda.txt'),
        corr=rd('b699_corrigendum.txt'), corrj=jl('b699_corrigendum.json'), corrland=jl('b699_corrigendum_landing.json'),
        tie=rd('b699_tie.txt'), tiej=jl('b699_tie.json'), cut=rd('b699_cut.txt'), cutj=jl('b699_cut.json'),
        quote=rd('b699_quote_substrate.txt'), quotej=jl('b699_quote_substrate.json'), prints_ki=rd('b699_prints_SIDE-substrate-cluster.txt'),
        dry_sub=rd('b699_correspondence_dry_substrate.txt'), dry_arch=rd('b699_correspondence_dry_archimedean.txt'),
        page_diff=rd('b699_correspondence_page_diff_archimedean.txt'), onecopy=rd('b699_onecopy.txt'),
        bridgej=jl('b699_bridge_line.json'), onecopyj=jl('b699_onecopy_line.json'), plan=rd('b699_bridge_plan.txt'),
        page_paths=read_blob(PP, 'HEAD:' + K.PATHS_PAGE), b674=rd('b674_rules.txt'),
        rf_diff=rd('b699_readfirst_diff.txt'), rf_hand_now=blob(ROOT, 'HEAD:data/b699_readfirst.txt'),
        rf_hand_z=blob(ROOT, '%s:data/b699_readfirst.txt' % K.STEPZERO_BANKS),
        asec=jl('b699_arm_seconds.json'), asect=rd('b699_arm_seconds.txt'),
        shared=dict((p, (cr0(blob(ROOT, '%s:%s' % (PRE['relay'], p))), cr0(raw(os.path.join(ROOT, *p.split('/')))), cr0(blob(ROOT, 'HEAD:' + p))))
                    for p in K.SHARED_APPENDED),
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), c2=_ct(ROOT, K.C2_RELAY), c3=_ct(ROOT, K.C3_RELAY), page=_ct(PP, K.C3_PAGE_PP),
               onecopy_pp=_ct(PP, K.C3_ONECOPY_PP), plan=_ct(ROOT, K.C3_PLAN), bridge=_ct(ROOT, K.C3_BRIDGE), bridge_pp=_ct(PP, K.C3_BRIDGE_PP),
               cut=_ct(KI, K.KI_CUT), merge=_ct(KI, K.KI_MERGE), stepzero=_ct(ROOT, K.STEPZERO_BANKS)),
        files=dict(stepzero=files_of(ROOT, K.STEPZERO_BANKS), c1=files_of(ROOT, K.C1_RELAY), c2=files_of(ROOT, K.C2_RELAY),
                   plan=files_of(ROOT, K.C3_PLAN), page=files_of(PP, K.C3_PAGE_PP), c3=files_of(ROOT, K.C3_RELAY)),
        standing=STANDING, wf=wf_state(), runner=jl('b699_runner_rows.json'),
        rbanks=dict(('%s_%s' % (r.get('kernel'), r.get('label')), rd('b699_runner_%s_%s.txt' % (r.get('kernel'), r.get('label'))))
                    for r in jl('b699_runner_rows.json').get('rows') or []),
        mainst=main_state(),
        export_present=os.path.exists(os.path.join(ROOT, *EXPORT.split('/'))), export_log=gs(ROOT, 'log', '--all', '--format=%h', '--', EXPORT),
        export_index=gs(ROOT, 'ls-files', '--', EXPORT), export_status=gs(ROOT, 'status', '--porcelain', '--', EXPORT),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b699_act_root.json'), arj0=jl('b698_act_root.json'), art=rd('b699_act_root.txt'), rootsf=rd('act_roots.txt'),
        rootbanks=jl('b699_root_banks.json'),
        pushout=(files_of(ROOT, K.STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, *f.split('/')))), cr0(blob(ROOT, 'HEAD:tools/' + f)))
              for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b699_kernels_face.json').get('kernels') or {}), kerns_read=list(dict.fromkeys(REC._kerns())),
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mustfail=not os.path.exists(os.path.join(D, 'b699_mustnotexist.txt')),
        fj=jl('b699_findings.json'), tj=jl('b699_trail.json'), sc=jl('b699_scores.json'), desk=rd('b699_desk_notes.txt'), tfj=jl('b699_table_final.json'),
        lsr=None,
        rlog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(ROOT, 'log', '--reverse', '--format=%h %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        plog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(PP, 'log', '--reverse', '--format=%h %ct %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()],
    )
    S['root_at_commit'] = _root_named_at_commit(S['arj'])
    S['phase_secs'] = {'the banks and the state': time.time() - t0}
    S['pp_allowed'] = sorted(K.PP_WRITTEN)
    t1 = time.time()
    S['live'] = live_arms() if 'live' in need else dict(names=[], nsm=[], ac=[], ac_counts={}, mh=[], mh_per={}, secs=(0, 0, 0))
    S['phase_secs']['the three arms at HEAD' + ('' if 'live' in need else ' (not in this part)')] = time.time() - t1
    t1 = time.time()
    S['ra'] = RA.sources('b699', SESSION, K.ANCHOR, K.PARTS, S['lock_epoch'], PRE['relay'], PRE['pp']) if 'rules' in need else {}
    S['phase_secs']['the rule arms` trace' + ('' if 'rules' in need else ' (not in this part)')] = time.time() - t1
    t1 = time.time()
    S['kern_now'] = kern_now(S['kern_face']) if S['kern_face'] else {}
    ch = set(x for x in gs(PP, 'diff', '--name-only', PRE['pp']).split(NL) if x.strip())
    ch |= set(x for x in gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD').split(NL) if x.strip())
    S['pp_changed'] = sorted(ch)
    S['ledger_adds'] = appended(S['fi_pre'], S['fi_now']) + NL + appended(S['ot_pre'], S['ot_now'])
    S['globs'] = wl_globs(face)
    S['outside'] = [n for n in R41.OAI_NEEDLES if n in S['ledger_adds']]
    if 'written' in need:
        S['written'] = written_files()
        S['nd_sets'] = R6.nd_sets()
        pub = [S['ledger_adds']]
        for f in sorted(os.listdir(D)):
            if f.startswith(('b699_', 'audit_b699_')) and os.path.isfile(os.path.join(D, f)) and not f.endswith(('.gz', '.png', '.jsonl')):
                pub.append(read(os.path.join(D, f)))
        pub += [read(f) for f in tools]
        S['nd_pub'] = R6.nd_hits(NL.join(pub), S['nd_sets'])[0]
        import additive_shared as ADD2
        shared = set(ADD2.shared_files()) | set(K.SHARED_APPENDED)
        pre_ids = {}
        for l in git(ROOT, 'ls-tree', '-r', PRE['relay'], '--', 'data/')[1].split(NL):
            if '\t' in l:
                meta, p = l.split('\t', 1)
                pre_ids[p] = meta.split()[2]
        bad = []
        for p, i in pre_ids.items():
            if os.path.basename(p) in TABLE_FILES or p in shared:
                continue
            fp = os.path.join(ROOT, p)
            rb = open(fp, 'rb').read() if os.path.exists(fp) else None
            if rb is None or i not in (blob_id(rb), blob_id(cr0(rb))):
                bad.append(p)
        S['prior_bad'], S['prior_n'] = bad, len(pre_ids)
    else:
        S['written'], S['nd_pub'], S['prior_bad'], S['prior_n'] = [], {}, [], 0
    S['phase_secs']['the written files, the public bytes and the prior banks' + ('' if 'written' in need else ' (not in this part)')] = time.time() - t1
    t1 = time.time()
    S['roots_pre'] = cr0(blob(ROOT, PRE['relay'] + ':data/act_roots.txt'))
    S['roots_now'] = cr0(raw(os.path.join(D, 'act_roots.txt')))
    S['bank_mtimes'] = {}
    for it in (S['arj'].get('items') or []):
        p = it.split()[0]
        if p.startswith('data/') and os.path.exists(os.path.join(ROOT, *p.split('/'))):
            S['bank_mtimes'][p] = os.path.getmtime(os.path.join(ROOT, *p.split('/')))
    import act_root as AR
    S['order_slack'] = AR.ORDER_SLACK
    S['boundary'] = boundary()
    S['ar_verify'], S['ar_reads'], S['half_a'] = [], {}, {}
    if 'chain_a' in need:
        S['ar_verify'], S['ar_reads'] = half_verify(0)
    if 'chain_b' in need:
        S['ar_verify'], S['ar_reads'] = half_verify(1)
    S['phase_secs']['the act-root chain`s half' + ('' if ('chain_a' in need or 'chain_b' in need) else ' (not in this part)')] = time.time() - t1
    t1 = time.time()
    if 'additive' in need:
        try:
            S['additive'] = ADD.check(worktree=True)
        except Exception as e:
            S['additive'] = [('raised', type(e).__name__, [('x', [])])]
    else:
        S['additive'] = []
    S['phase_secs']['the shared additive files' + ('' if 'additive' in need else ' (not in this part)')] = time.time() - t1
    return S


def put(S, k, v):
    S[k] = v
    return S


def oline(S, n):
    ls = S['ot'].split(NL)
    return ls[n - 1] if n and 0 < n <= len(ls) else ''


def fline(S, n):
    ls = S['find'].split(NL)
    return ls[n - 1] if n and 0 < n <= len(ls) else ''


def rline(S, i, key='rl'):
    x = (S[key].get('lines') or [])
    return x[i] if len(x) > i else {}


def landed(S, i, need, key='rl'):
    x = rline(S, i, key)
    o = (fline if x.get('file') == 'FINDINGS.md' else oline)(S, x.get('line'))
    return bool(x) and o.startswith(conv(x.get('head', '\x00'))) and all(n in o for n in need)


def unwrap(t):
    return ' '.join(' '.join(re.sub(r'^\s*(?:###\s*)+', '', l) for l in t.split(NL)).split())


def procs_ok(S):
    p = unwrap(S['stepz'])
    return 'tail, lean, lake, python and claude named' in p and 'claude 1 (pid' in p and 'tail 0, lean 0, lake 0, python 0' in p \
        and 'No task of this session stopped; no orphan, nothing stopped by PID' in p


STEPZERO_FAILING = {'test_chain_page.py': ['(9)'], 'test_chain_page_b638.py': ['(4)', '(5)', '(6)', '(7)']}


def tests_ok(S):
    j = S['tests']
    names = sorted(S['tracked_tests'])
    nf = dict((n, x['failing']) for n, x in j.items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(j) == sorted(set(names) - {'test_elab_reader_b634.py'}) and nf == STEPZERO_FAILING \
        and 'b697_nodes_zeta.txt' in (j.get('test_chain_page.py') or {}).get('args', []) \
        and 'test_elab_reader_b634.py' in S['withheld'] \
        and ('TEST FILES %d ; RUN %d ; WITHHELD 1 ; NOT CLEAN 2' % (len(names), len(names) - 1)) in unwrap(S['testst'])


UNANSWERED = "The user doesn't want to proceed with this tool use"


def _post_seal_named(face):
    m = re.search(r'### POST-SEAL PROMPTS NAMED: (NONE|\d+)', face)
    return 0 if not m or m.group(1) == 'NONE' else int(m.group(1))


def answers_ok(S):
    a = S['answers']
    m = re.search(r'^### b699 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
    heads = re.findall(r'^### PROMPT \d+ \(', a, re.M)
    calls = re.findall(r'^### CALL tool-use id ', a, re.M)
    res = re.findall(r'^RESULT \(transcript line [^)]*\): (.*)$', a, re.M)
    if not m or int(m.group(1)) != len(heads) or len(heads) < FLOORS['prompts'] or len(calls) < FLOORS['calls']:
        return False
    per = [len(re.findall(r'^  OPTION \d+', p, re.M)) for p in re.split(r'^### PROMPT \d+ \(', a, flags=re.M)[1:]]
    lk = S['lock_epoch']
    after = [c for c in S['answersj'].get('calls') or [] if lk and iso_epoch((c.get('ts') or '')[:19] + 'Z') and iso_epoch((c.get('ts') or '')[:19] + 'Z') > lk]
    return all(x >= 2 for x in per) and len(res) == len(calls) and not any(UNANSWERED in r or '### NO RESULT' in r for r in res) \
        and len(after) <= _post_seal_named(S['face'])


def edit_route_ok(S):
    return bool(S['cmds']) and bool(S['prev_cmds']) and S['REC'].edit_route_offences(S['cmds'] + S['prev_cmds']) == []


def no_local_lean(S):
    import b699_record as REC
    return bool(S['cmds']) and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and REC.local_lean(r['cmd'])]


def planted_ok(S, t, n, form='%d of %d cases as wanted -- PASS'):
    p = S['planted'][t]
    return p['rc'] == 0 and (form % (n, n) if '%d' in form else form) in p['out']


def nsm_hits(S):
    return [(r['kernel'], f, ln) for r in S['live']['nsm'] for f, ln, _t in r['hits']]


def no_sorry_main(S):
    rows = S['live']['nsm']
    return len(rows) == len(S['live']['names']) > 0 and all(r['equal'] for r in rows) and not nsm_hits(S)


def ac_count(rows, v):
    return sum(1 for r in rows if r['verdict'] == v)


def axiom_claim(S):
    rows = S['live']['ac']
    return bool(rows) and ac_count(rows, 'CONTRADICTED') == 0


def module_header(S):
    per = S['live']['mh_per']
    return len(per) == len(S['live']['names']) > 0 and sum(v['headers'] for v in per.values()) > 0 and S['live']['mh'] == []


# ================================================================== (R309) STEP ZERO: THE CITATION CHECK, THE BRANCHES
READFIRST_NEEDLES = ('relay data/b698_closing.txt :1', 'relay data/b698_closing.txt :92-:93', 'relay data/b698_defects.txt :6-:32',
                     'relay data/b698_correspondence_dominance.txt :33', 'relay data/b698_regularity_uses.txt :24', 'relay data/b698_rules.txt :6-:9',
                     'PLACE-papers OPEN_TRAILS.md :10257', 'PLACE-papers OPEN_TRAILS.md :14386', 'relay data/b697_cut.txt :19',
                     'data/b698_readme_cut.txt :21-:23', 'relay data/b670_licensed_table.txt :54', 'relay data/b674_rules.txt :8-:11',
                     'relay data/b690_rules.txt :9-:12', 'relay tools/correspondence_gen.py :247', 'relay tools/b695_corrigendum.py :73',
                     'relay data/b698_closing_push_out.txt :5')
NAMED_LOCAL = sorted(b for _r, bs in K.DELETE for b in bs)
NAMED_ALL = sorted(NAMED_LOCAL + [b for _r, b in K.DELETE_REMOTE])


def readfirst_ok(S):
    z = unwrap(S['readfirst'])
    return bool(z) and all(x in z for x in READFIRST_NEEDLES)


def branches_ok(S):
    """the seven local names gone from relay`s, PLACE-papers` and SIDE-simplicity`s branch lists; the branches bank`s verdict."""
    z = S['branchest']
    left = dict((r, sorted(x.strip() for x in v.split(NL) if x.strip())) for r, v in S['branch_lists'].items())
    return all(v == [] for v in left.values()) and len(left) == 3 and all(b in z for b in NAMED_LOCAL) \
        and 'BRANCHES NAMED 8 ; DELETED 8 ; KEPT 0 ; EVERY TIP MERGED True' in unwrap(z)


def _first_delete_ts(S):
    import b699_record as REC
    ts = [r['ts'] for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and REC.delete_shape(r['cmd'])[0]]
    return iso_epoch(min(ts)[:19] + 'Z') if ts else None


def branches_banked_ok(S):
    """b695 (a)'s lesson: every named branch's tip banked before the first delete; then eight rows through the record tool's reader, each
    merged, seven local and one remote, every one DELETED."""
    import b699_record as REC
    rows = S['branchj'].get('rows') or []
    try:
        fates = [REC.read_branch_row(r) for r in rows]
    except Exception:
        return False
    bt = iso_epoch((S['branchbj'].get('at') or '')[:19] + 'Z')
    fd = _first_delete_ts(S)
    return len(rows) == 8 and all(f == 'DELETED' for _b, f in fates) and all(r['merged'] for r in rows) \
        and sorted(r['where'] for r in rows) == ['local'] * 7 + ['remote'] and sorted(r['branch'] for r in rows) == NAMED_ALL \
        and bool(bt) and bool(fd) and bt < fd and len(S['branchbj'].get('rows') or []) == 8


def deletes_one_ok(S):
    import b699_record as REC
    sh_ = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell')]
    shapes = [(REC.delete_shape(r['cmd']), REC.chained_after(r['cmd'])) for r in sh_]
    shapes = [(s, c) for s, c in shapes if s[0]]
    return bool(shapes) and all(len(d) == 1 and not gl and not vs and not c for (d, gl, vs), c in shapes) \
        and sorted(x for (d, _g, _v), _c in shapes for x in d) == NAMED_ALL \
        and 'BRANCH DELETES OF ONE BRANCH, NO GLOB, NO VARIABLE AND NOTHING CHAINED AFTER 8 OF 8' in S['cmdt']


def dry_step_ok(S):
    g = S['gate']
    return '--- THE DRY-RUN STEP ((R267)(2))' in g and 'ENTRY : table cells NONE ; screens QUIET' in g and 'TRAIL : table cells NONE ; screens QUIET' in g \
        and '### ### **THE DRY-RUN STEP : CLEAN**' in g and '### ### **GATE VERDICT : CLEAR**' in g


def closing_dry_ok(S):
    g = S['gate']
    return '--- THE CLOSING DRY-RUN STEP (b675 rules row 1)' in g and '### ### **THE CLOSING DRY-RUN STEP : CLEAN**' in g \
        and 'b699 closed:' in g and 'the misses as the bank lists them' in g and '### THE CORRIGENDUM' in g and '### THE RE-CUT' in g \
        and '### THE CELLS' in g and '### THE BRIDGE' in g and '### THE KERNELS' in g and '(g) The defects (a)' in g and '### NO VERDICT LINE' not in g


def citation_ok(S):
    """the citation check's bank: every cite checked, OK and misses summing; its two misses, raised to the author at step zero in one call
    before the readfirst bank's commit; the check at step zero, before Component 1's first commit."""
    c = S['citation']
    m = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', c)
    calls = S['answersj'].get('calls') or []
    p0 = iso_epoch((calls[0].get('ts') or '')[:19] + 'Z') if calls else None
    return bool(m) and int(m.group(1)) == int(m.group(2)) + int(m.group(3)) > 0 and 'A GATE STEP AT STEP ZERO' in c \
        and int(m.group(3)) == len(S['cit_misses']) == 2 and bool(p0) and bool(S['t'].get('stepzero')) and p0 < S['t']['stepzero'] \
        and bool(S['t'].get('c1')) and S['t']['stepzero'] <= S['t']['c1']


def rowgen_ok(S):
    return '### ### **CONSTELLATION EXIT 0 ; ROWGEN DIFF EXIT 0 ; TABLES 19.**' in S['rowgen']


def weight_ok(S):
    return landed(S, 0, ['b698 AT ITS WEIGHT', 'f19eccc4'])


def answers_checked_ok(S):
    """the citation bank's mid-act prints read at HEAD, at or above the sealed floor, each before the step its answer governs: the two answers
    on the misses before the step-zero banks' and Component 1's commits, the tag-cell answer before Component 2's, the archimedean answer before
    the page's commit."""
    c = S['citation']
    stamps = re.findall(r'### \(R278\)\(4\) THE MID-ACT CHECK \((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\): the answer carrying \'([^\']+)\'', c)
    acts = dict()
    for t_, n in stamps:
        acts.setdefault(n, []).append(iso_epoch(t_))
    gov = (('Option 1, cite both', S['t'].get('stepzero')), ('Option 1: tools/b695_corrigendum.py', S['t'].get('c1')),
           ('Option 1, nothing to write', S['t'].get('c2')), ('Option 1, run: the generator alone writes PATHS', S['t'].get('page')))
    return len(stamps) >= FLOORS['checks'] and all(any(k in n for n in acts) and w and max(v for n, vs in acts.items() if k in n for v in vs) < w
                                                   for k, w in gov)


# ================================================================== (R309)(1)-(5): THE RECORD, THE CORRIGENDUM, THE RE-CUT, THE CELLS, THE BRIDGE
def _fn_src(src, name):
    if ('\ndef %s(' % name) not in src:
        return ''
    i = src.index('\ndef %s(' % name) + 1
    m = re.search(r'\n(?=\S)', src[i + 1:])
    return src[i:i + 1 + m.start() + 1] if m else src[i:]


def scorer_banks_ok(S):
    """data/b686_rules.txt row (1), standing: the N1-N4 scorers' code reads banks and commits and no ledger and no findings bank; the scores
    route writes its bank once; the entry's composer takes its scores line from the scores bank."""
    n = ''.join(strip_prose(_fn_src(S['rec_src'], f)) for f in ('_n1', '_n2', '_n3', '_n4'))
    sc = strip_prose(_fn_src(S['rec_src'], 'scores'))
    ft = strip_prose(_fn_src(S['rec_src'], '_finding_text'))
    return bool(n) and '_commands.json' in n and '_dispatches.json' in n and '_tie.txt' in n and '_cut.json' in n and '_bridge_plan.txt' in n \
        and not re.search(r'\b(FIND|OT)\b|FINDINGS|OPEN_TRAILS|findings|entry_line', n) \
        and "os.path.isfile(os.path.join(D, '%s_scores.json' % ACT))" in sc and 'scores_line(S)' in ft and "jl('%s_scores.json' % ACT)" in ft


def _entry_block(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    if not e:
        return ''
    end = next((i for i in range(e, len(ls)) if ls[i].startswith('## ')), len(ls))
    return NL.join(ls[e - 1:end])


def entry_scores_ok(S):
    import b699_record as REC
    want = conv(REC.scores_line(S['sc'])) if S['sc'] else None
    blk = _entry_block(S)
    got = [l for l in blk.split(NL) if l.startswith('**The scores.**')]
    return bool(want) and bool(S['sc']) and got == [want]


def entry_title_ok(S):
    e = S['fj'].get('entry_line')
    t = S['REC']._title()
    return bool(e) and fline(S, e) == conv(t) \
        and t.startswith('## SIDE-substrate-cluster re-cut: 1 row outside LICENSED/CITED to 0, v0.4.1;') \
        and 'the SIDE-archimedean cells at PATHS :285 regenerated; the bridge at binder 1 priced;' in t \
        and t.endswith('b698’s undeclared failure by corrigendum')


def corrigendum_ok(S):
    """(R309)(2): the generated entry at FINDINGS at the landing bank's line, found by conv, its head the tool's title; the bank's verdict;
    the two commits named by hash as the arm reads them."""
    x = (S['corrland'].get('lines') or [{}])[0]
    o = fline(S, x.get('line'))
    blk = NL.join(S['find'].split(NL)[(x.get('line') or 1) - 1:(x.get('line') or 1) + 12])
    return x.get('line') == K.CORR_LINE and o.startswith(conv(x.get('head') or '\x00')) and 'G-NOTHING-RAN-AHEAD' in o \
        and '`2d19edd3`' in blk and '`069778f6`' in blk and 'THE ENTRY AT FINDINGS :%d' % K.CORR_LINE in S['corr'] \
        and [m.get('hash', '')[:7] for m in S['corrj'].get('missing') or []] == ['2d19edd', '069778f']


def corrigenda_rows_ok(S):
    """(R309)(2): rows (11)-(13) appended beneath data/b675_corrigenda.txt, every line above unchanged (the blob before the act a prefix of the
    file now and at HEAD), Component 1's commit carrying it."""
    pre, now, head = S['shared'].get('data/b675_corrigenda.txt', (None, None, None))
    add = appended(pre, now)
    return pre is not None and now == head and add != '' and '### appended by b699, 2026-10-21, under (R309)(2)' in add \
        and all(('  (%d) ' % n) in add for n in (11, 12, 13)) and 'data/b675_corrigenda.txt' in S['files']['c1']


def tie_first_ok(S):
    """N2: b674's rule verbatim and every kernel row printed before the document is named; the named document SIDE-substrate-cluster."""
    t = S['tie'].split(NL)
    ir = next((i for i, l in enumerate(t) if l.startswith('### b674`S TIE-BREAK RULE, VERBATIM')), None)
    it = next((i for i, l in enumerate(t) if l.startswith('### THE KERNEL ROWS, VERBATIM')), None)
    iname = next((i for i, l in enumerate(t) if l.startswith('### ### **THE NEXT DOCUMENT')), None)
    verb = S['b674'].split(NL)[7:11]
    return ir is not None and it is not None and iname is not None and ir < it < iname and all(('  ' + v) in t for v in verb) \
        and S['tiej'].get('named') == K.KERNEL and 'SIDE-substrate-cluster (THE TOP COUNT 1, 1 DOCUMENT AT IT ; NO TIE)' in t[iname]


def recut_ok(S):
    j = S['cutj']
    return j.get('before') == 1 and j.get('after') == 0 and j.get('tag') == K.NEXT_TAG and (j.get('tag_peel') or '').startswith(K.KI_MERGE) \
        and j.get('merged_tree') == j.get('built_tree') and 'THE DISTANCE BEFORE 1, AFTER 0 ; TAG v0.4.1 ; PRINTS EQUAL ; QUOTING LINES 0' in S['cut']


def prints_equal_ok(S):
    return 'BEFORE 11 TERMINALS ; EACH PRINTED AFTER True ; DIFFERING 0 ; NEW 0 ; EQUAL LINE FOR LINE True' in S['prints_ki']


def quote_first_ok(S):
    j = S['quotej']
    at = iso_epoch((j.get('at') or '')[:19] + 'Z')
    return bool(at) and bool(S['t'].get('merge')) and at < S['t']['merge'] and j.get('base') == K.KI_PT and j.get('tip') == K.KI_CUT \
        and 'FIRES FOR EVERY NEEDLE IN BOTH SHAPES' in S['quote'] and 'QUOTING LINES 0 -- EACH ENTERED AS A RESIDUE' in S['quote']


def tag_cells_ok(S):
    """(R309)(3): the generator's dry run over the cells naming the kernel printed after the tag, the prompt put after it and before Component
    2's commit, the dry bank carried by that commit, nothing written."""
    calls = S['answersj'].get('calls') or []
    p = iso_epoch((calls[1].get('ts') or '')[:19] + 'Z') if len(calls) > 1 else None
    d_at = head_epoch(S['dry_sub'])
    tag_ct = _ct(KI, K.NEXT_TAG)
    return bool(p) and bool(d_at) and bool(S['t'].get('c2')) and d_at < p < S['t']['c2'] \
        and 'data/b699_correspondence_dry_substrate.txt' in S['files']['c2'] \
        and 'CELLS NAMING IT THE GENERATOR WOULD CHANGE 0' in S['dry_sub'] and 'NOTHING WRITTEN' in S['dry_sub'] and bool(tag_ct)


def arch_cells_ok(S):
    """(R309)(4), on the word "run": the dry run printed before the prompt, the prompt before the page's commit, the page alone written by the
    generator, its :285 carrying v0.1.1."""
    calls = S['answersj'].get('calls') or []
    p = iso_epoch((calls[2].get('ts') or '')[:19] + 'Z') if len(calls) > 2 else None
    d_at = head_epoch(S['dry_arch'])
    pl = S['page_paths'].split(NL)
    return bool(p) and bool(d_at) and bool(S['t'].get('page')) and d_at < p < S['t']['page'] and S['files']['page'] == [K.PATHS_PAGE] \
        and 'THE ROSTER`S PAGES ALONE True' in S['page_diff'] and len(pl) > 284 and '| SIDE-archimedean v0.1.1 |' in pl[284] \
        and 'CELLS NAMING IT THE GENERATOR WOULD CHANGE 3' in S['dry_arch']


def onecopy_ok(S):
    x = (S['onecopyj'].get('lines') or [{}])[0]
    o = oline(S, x.get('line'))
    return x.get('line') == K.ONECOPY_LINE and o.startswith(conv(x.get('head') or '\x00')) and 'differ in 24 lines' in o \
        and 'THE TWO TABLES DIFFER IN 24 LINES AT HEAD' in S['onecopy'] and 'partner_lines_differing reads 4' in o


def bridge_plan_ok(S):
    """N4: the plan's binders' section before its statements', 14 rows each with its translation, nothing compiled; the plan committed alone."""
    p = S['plan']
    i1, i2 = p.find('== 1. THE BINDERS'), p.find('== 2. THE EXPECTED STATEMENTS')
    blk = p[i1:i2] if 0 <= i1 < i2 else ''
    rows = re.findall(r'^  (binder \d+|conclusion) +\|', blk, re.M)
    return 0 <= i1 < i2 and len(rows) == 14 and blk.count('| THE TRANSLATION:') == 14 and 'NOTHING COMPILED' in p \
        and S['files']['plan'] == ['data/b699_bridge_plan.txt']


def bridge_order_ok(S):
    x = (S['bridgej'].get('lines') or [{}])[0]
    o = oline(S, x.get('line'))
    return x.get('line') == K.BRIDGE_LINE and o.startswith(conv(x.get('head') or '\x00')) and '**`W-ORD-H2-BRIDGE-THEOREM`**' in o \
        and 'beneath `W-ORD-H2-BRIDGE` (:10257' in o and 'Status OPEN.' in o


def readfirst_diff_ok(S):
    return 'THE HAND LIST 19 PATHS ; THE TEXT CITES 21 ; BOTH 13 ; LINES DIFFERING 14' in S['rf_diff'] and 'No bank is rewritten by this reading.' in S['rf_diff'] \
        and 'data/b699_readfirst_diff.txt' in S['files']['stepzero'] and S['rf_hand_now'] is not None and S['rf_hand_now'] == S['rf_hand_z']


REPAIRS_WANT = 5


def repairs_ok(S):
    return ('REPAIRS %d ; NO SHARED TOOL EDITED' % REPAIRS_WANT) in S['repairs'] and 'NO FROZEN BANK EDITED' in S['repairs'] \
        and '  (1) tools/b699_record.py prev_capture' in S['repairs']


def parts_ok(S):
    return all(re.search(r'PART %s : ARMS \d+ ; \d+ s' % p, S['prerun']) for p in K.PARTS)


def arm_seconds_ok(S):
    j = S['asec']
    return bool(j) and j.get('clocked') == j.get('standing') == len(STANDING) and not j.get('missing') and len(j.get('slowest') or []) == 3 \
        and 'THE THREE SLOWEST' in S['asect'] and all((j.get('run_secs') or {}).get(p) for p in K.PARTS)


def defects_ok(S):
    letters = re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", S['defects'], re.M)
    fl = list(FLOORS['defects'])
    return letters[:len(fl)] == fl and [x for x, _o in letters] == list('abcdefghijklmnopqrstuvwxyz'[:len(letters)]) \
        and all(o in ('SEAT', 'NAVIGATOR') for _x, o in letters)


def read_rule_ok(S):
    """data/b698_rules.txt row (2), binding: the read-call bank written by the record tool, every whole read of a file of two hundred lines or
    more entered in the defects bank by its transcript line."""
    b = S['reads_bank']
    off = re.findall(r'^  (\d+) \| \S+ \| \d+ \| ### AN OFFENCE \|', b, re.M)
    m = re.search(r'WHOLE OF A FILE OF 200 LINES OR MORE (\d+)', b)
    return bool(m) and int(m.group(1)) == len(off) and all(('transcript line %s' % n) in S['defects'] for n in off)


# ================================================================== THE RUNNER (the standing arms, this act's two runs: b699's)
IDENT_WF = ('secrets.', 'psinary', 'seale', 'york', 'hotmail', 'orcid', '0009-0008')


def wf_ok(S):
    """this act's kernel workflow: at main equal to its write at cebec19 (unedited after), no author identifier, no secret, the hold, the lake
    path and no cache step for its Mathlib-free lakefile, the print step over its list, the files b699 wrote."""
    for k, v in S['wf'].items():
        t = v['text'].lower()
        if not v['text'] or v['text'] != v['before'] or any(w in t for w in IDENT_WF):
            return False
        if 'workflow_dispatch' not in t or 'hold_mb: "2560"' not in t or 'print_targets.txt' not in t:
            return False
        if not v['lakefile'] or 'lake env lean out/axioms.lean' not in t or (('lake exe cache get' in t) != v['mathlib']):
            return False
        if len(v['targets']) != v['printed'] or v['act_writes'] != v['want']:
            return False
    return sorted(S['wf']) == [K.KERNEL]


def runner_ok(S):
    """this act's two runs through b699's record tool's reader: before at main (the print list's commit), after at the cut's tip, each success,
    the artifact's sha256, the memory low above the hold."""
    import b699_record as REC
    rows = S['runner'].get('rows') or []
    want = dict(before=gs(KI, 'rev-parse', K.KI_PT), after=gs(KI, 'rev-parse', K.KI_CUT))
    try:
        for r in rows:
            REC.read_runner_row(r)
    except Exception:
        return False
    return len(rows) == 2 and sorted(r['label'] for r in rows) == ['after', 'before'] and all(r['kernel'] == K.KERNEL and r['ref'] == want[r['label']]
                                                                                             for r in rows) \
        and all(r['conclusion'] == 'success' and r['artifact_sha256'] and r['mem_low'] is not None and r['mem_low'] >= K.HOLD and not r['stopped']
                for r in rows)


def gate_ok(S):
    bs = S['rbanks']
    return len(bs) == 2 and all('GATE DERIVES' in t and 'BUILD EXIT 0 ; ERROR LINES 0' in t and 'SORRYAX 0' in t
                                and re.search(r'^### the artifact: .* ; AGREE$', t, re.M) for t in bs.values())


def merges_ok(S):
    """this act's one merge: SIDE-substrate-cluster's main at the merge, its parents the print list's commit and the gated tip, the merged tree
    the built tree, v0.4.1 at the merge naming v0.4, no other tag on the act's commits."""
    m = S['mainst']
    after = [r for r in (S['runner'].get('rows') or []) if r.get('label') == 'after']
    return m['main'] == K.KI_MERGE and m['parents'] == [K.KI_PT, K.KI_CUT] and bool(after) and after[0]['ref'].startswith(K.KI_CUT) \
        and m['trees'][0] == m['trees'][1] and m['tag'] == K.KI_MERGE and m['prior'] == K.KI_PRIOR_PEEL and m['tags'] == [K.NEXT_TAG] \
        and 'v0.4' in m['tagmsg'] and m['files'][K.KI_CUT] == [CUT_FILE] and m['files'][K.KI_WF] == [WF] and m['files'][K.KI_PT] == [PT]


# ================================================================== SCOPE, THE SEAL, THE ROOT, THE RECORD
def instruments_ok(S):
    for f, (pre, now, head) in S['inst'].items():
        if pre is None or pre != now or pre != head:
            return False
    return True


def seal_hashes_ok(S):
    j = S['sealj']
    at = iso_epoch(j.get('at') or '')
    rec_ = j.get('tools') or {}
    return bool(rec_) and at is not None and S['lock_epoch'] is not None and S['lock_epoch'] <= at \
        and sorted(rec_) == sorted(K.SEALED) and all(S['sealnow'].get(t) == rec_[t] for t in K.SEALED)


POST_SEAL = ('b699 seal', 'b699 pre-root', 'b699 root', 'b699 record', 'b699 --', 'b699 closing', 'b699 entry')


def _component_commit(s):
    return s.startswith('b699') and not s.startswith(POST_SEAL)


def sealed_after_ok(S):
    lk = S['lock_epoch']
    if lk is None:
        return False
    return all((t < lk) == _component_commit(s) for h, s, t in S['rlog']) and all((t < lk) == _component_commit(s) for h, s, t in S['plog']) \
        and any(_component_commit(s) for h, s, t in S['plog'])


def table_final_ok(S):
    t = S['tfj']
    return bool(t) and t.get('rc') == 0 and not t.get('gone') and not t.get('grade_moved')


def _chain_rows(S):
    return [l.split(None, 3) for l in S['rootsf'].split(NL) if l.strip() and not l.startswith('corrigendum ')]


def root_banked_ok(S):
    import act_root as AR
    j, j0 = S['arj'], S['arj0']
    rows = _chain_rows(S)
    items = j.get('items') or []
    return bool(j) and len(rows) == 76 and rows[75][:3] == ['b699', j.get('root'), j0.get('root')] \
        and AR.root_of(items, j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) \
        and not [it for it in items if 'b628_intake_crank' in it or 'b647_navigator_memory' in it or 'b700_' in it or 'mirror' in it
                 or 'chain_' in it or 'units' in it or it.split()[0].endswith(('.gz', '.png', '.jsonl'))] \
        and any(it.startswith('data/b699_cut.txt ') for it in items) and any(it.startswith('data/b699_bridge_plan.txt ') for it in items) \
        and any(it.startswith('data/b699_corrigendum.txt ') for it in items) and (j.get('commit') or {}).get('relay')


def root_banks_committed_ok(S):
    rb, rows = S['rootbanks'], S['root_at_commit']
    commit = (S['arj'].get('commit') or {}).get('relay') or ''
    return bool(rb) and rb.get('clean') is True and rb.get('pushed') is True and rb.get('head') == commit and bool(rows) \
        and all(c and e for _b, c, e in rows) and sorted(b for b, _c, _e in rows) == sorted(r['bank'] for r in rb.get('rows') or [])


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b699_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    """G-ACTROOT-VERIFY, counted once in standing-b3: the first half's verdicts banked by standing-b2 at this same HEAD, the second half's computed
    here, together b624 to b699 AGREE; the boundary link equal in both halves' reading; b680 read through its corrigendum row (4 banks); b699
    written LF."""
    ha = S['half_a'] or {}
    v = [tuple(x[:2]) for x in (ha.get('acts') or [])] + [tuple(x[:2]) for x in (S['ar_verify'] or [])]
    r = dict(ha.get('reads') or {}, **(S['ar_reads'] or {}))
    return ha.get('head') == gs(ROOT, 'rev-parse', 'HEAD') and [x[0] for x in v] == ['b%d' % i for i in range(624, 700)] \
        and all(x[1] == 'AGREE' for x in v) and (r.get('b699') or {}).get('crlf') == 0 and (r.get('b680') or {}).get('corrected') == 4 \
        and (ha.get('boundary') or {}).get('equal') is True and S['boundary'].get('equal') is True \
        and (ha.get('boundary') or {}).get('root') == S['boundary'].get('root')


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**The re-cut**', '**The archimedean cells**', '**The bridge**', '**The corrigendum**', '**The citation check**',
                 '**The scores.**', '**Read in mutual light**', 'strengthens', '**Carried to:**', '**Next.**', 'b700')


def finding_ok(S):
    e = S['fj'].get('entry_line')
    tail = _entry_block(S)
    return bool(e) and fline(S, e) == conv(S['fj'].get('title') or '\x00') and all(conv(x) in tail for x in ENTRY_NEEDLES)


def trail_tail(S):
    t = S['ot']
    i = t.find(conv(S['REC'].TRAIL_HEAD()))
    return t[i:] if i >= 0 else ''


def wl_ok(S):
    return bool(S['globs']) and bool(S['written']) and all(any(fnmatch.fnmatch(f, p) for p in S['globs']) for f in S['written'])


def scored(S, k):
    import b699_record as REC
    v = S['sc'].get(k)
    try:
        _k, w, _t = REC.read_score_row(k, v)
    except Exception:
        return False
    return w.split(' ')[0].split(',')[0].rstrip(';') in ('HELD', 'REFUTED', 'NOT', 'HOLDS', 'PENDING') and ('(%s)' % k) in S['desk']


def no_delete(S):
    words = ['os' + r'\.' + 'remove', 'os' + r'\.' + 'unlink', 'shutil' + r'\.' + 'rmtree', 'os' + r'\.' + 'rmdir',
             'rm' + ' -' + 'rf', 'Remove' + '-' + 'Item', r'\.' + 'unlink' + r'\(', 'git' + ' branch -' + 'D', 'worktree' + ' remove' + r'\b',
             'tag' + ' -' + 'd' + r'\b']
    pat = re.compile(r'(' + '|'.join(words) + r')')
    return bool(S['tooltext']) and not [f for f, t in S['tooltext'].items() if pat.search(t)]


def publish_uncalled(S):
    pub = ['actions' + '/pub' + 'lish', 'z_' + 'publish']
    return bool(S['tooltext']) and not [f for f, t in S['tooltext'].items() if any(p in t for p in pub)]


def kernels_untouched(S):
    f, n = S['kern_face'], S['kern_now']
    return bool(f) and sorted(f) == sorted(S['kerns_read']) and all(k in n and n[k] == f[k] for k in f)


def corpus_scope(S):
    return S['pp_changed'] == S['pp_allowed']


def closing_sentence_ok(S):
    t = S['closing_src']
    return ('no identifier of the author ' + 'in any outbound') in t and ('plain requests to ' + 'github.com') in t \
        and '### THE CITATION CHECK' in t and '### THE RECORD LINES' in t and '### THE DRY RUN' in t and 'THE CORRIGENDUM' in t \
        and 'THE RE-CUT' in t and 'THE CELLS' in t and 'THE BRIDGE' in t and '### THE KERNELS' in t and '### THE MIRROR' in t \
        and '### THE CARRY-TIME' in t


def lsr_ok(S):
    lsr = S['lsr'] if S['lsr'] is not None else dict(KC0.LSR)
    return bool(lsr) and all(v <= 1 for v in lsr.values())


def g2_names(face):
    try:
        g2 = face[face.index('### (G2) THE GATE ARMS.'):face.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


def _rl(S, i, line, key='rl'):
    ls = list(S[key].get('lines') or [])
    ls[i:i + 1] = [dict(rline(S, i, key), line=line)]
    return put(S, key, dict(S[key], lines=ls))


def _mut(S, key, f):
    d = copy.deepcopy(S[key])
    f(d)
    return put(S, key, d)


def _live(S, f):
    d = copy.deepcopy(S['live'])
    f(d)
    return put(S, 'live', d)


def _planted(S, t):
    return put(S, 'planted', dict(S['planted'], **{t: dict(rc=1, out='')}))


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R309) END' in S['ferry'] and S['ferry'].rstrip().endswith(K.TAIL),
     lambda S: put(S, 'ferry', S['ferry'].replace(K.TAIL, ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the step-zero bank: tail, lean, lake, python and claude named, the seat`s claude alone, none of the others; no task stopped, no orphan, nothing stopped by PID',
     lambda S: procs_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('python 0', 'python 1'))),
    ('G-STEPZERO-TESTS', 'the tests bank against the test files tracked before the act, test_elab_reader_b634.py withheld (no lean on this host), run against the list the page names',
     lambda S: tests_ok(S), lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: S['pushout'][0] == ['data/b698_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'relay`s, PLACE-papers` and SIDE-simplicity`s branch lists by the ruling`s names, and the branches bank',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{'D:/relay': 'push-b698'}))),
    ('G-READFIRST-CITED', 'the read-first bank: every item of the ferry`s list cited by path and line', lambda S: readfirst_ok(S),
     lambda S: put(S, 'readfirst', '')),
    ('G-ANSWERS-BANKED', 'the answers bank read at HEAD: its prompts and calls at or above the sealed floors, each with its options and result, any call after the lock named on the face',
     lambda S: answers_ok(S), lambda S: put(S, 'answers', S['answers'].replace('### PROMPT 1 (', '### PROMPTED ('))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-EXPORT-UNTRACKED', 'the navigator`s export: present, untracked, in no commit', lambda S: S['export_present'] and S['export_log'] == ''
     and S['export_index'] == '' and S['export_status'].startswith('??'), lambda S: put(S, 'export_index', EXPORT)),
    ('G-EDIT-ROUTE', 'the record tool`s one reading (tools/edit_route.py`s arms and sed in any form) over this act`s whole capture and the previous act`s after its post-push suite, read live',
     lambda S: edit_route_ok(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -n 1p tools/b699_record.py")])),
    ('G-NO-LOCAL-LEAN', 'the act`s command capture, read live: no command runs lean or lake on this host (N1)', lambda S: no_local_lean(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd='lake env lean SIDESubstrateCluster/T7Labeling.lean')])),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line, found by conv', lambda S: weight_ok(S), lambda S: _rl(S, 0, 1)),
    ('G-DRY-STEP-CLEAN', 'the gate`s record: the dry-run step run, the entry and the trail record quiet under their screens, CLEAN printed, the gate CLEAR',
     lambda S: dry_step_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE DRY-RUN STEP : CLEAN', 'THE DRY-RUN STEP : NOT CLEAN'))),
    ('G-CLOSING-DRY-STEP', 'the gate`s record: the closing run dry before the lock, its head line, citation line, corrigendum, re-cut, cells, bridge and kernels sections and the defects row printed (b675 rules row 1)',
     lambda S: closing_dry_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE CLOSING DRY-RUN STEP : CLEAN', 'THE CLOSING DRY-RUN STEP : NOT CLEAN'))),
    ('G-CITATION-CHECKED', 'the citation check`s bank (the gate step at step zero): every cite checked, its two misses raised at step zero before the readfirst bank`s commit, none repaired silently, before Component 1',
     lambda S: citation_ok(S), lambda S: put(S, 'cit_misses', S['cit_misses'][:-1])),
    ('G-R309-ENTERED', 'the ferry and the trail', lambda S: 'RULING (R309) END' in S['ferry'] and S['ot'].count('**(R309) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R309) ratified', '**(R3090) ratified'))),
    ('G-ROWGEN-STEPZERO', 'the rowgen bank: constellation and the build-free diff over the 19 roster tables, both exit 0 (b670 rules row 3)',
     lambda S: rowgen_ok(S), lambda S: put(S, 'rowgen', S['rowgen'].replace('ROWGEN DIFF EXIT 0', 'ROWGEN DIFF EXIT 1'))),
    ('G-BRANCHES-BANKED', 'the branches banks: every tip banked before the first delete (b695 (a)), then the eight rows through the record tool`s reader, each merged, seven local and one remote, all deleted',
     lambda S: branches_banked_ok(S), lambda S: _mut(S, 'branchbj', lambda d: d.update(at='2099-01-01T00:00:00Z'))),
    ('G-DELETES-ONE-BRANCH', 'the command capture by the record tool`s reader and the command bank: each branch delete naming one branch, no glob and no variable in any half, nothing chained after (data/b694_rules.txt row (1)), the ruling`s eight exactly',
     lambda S: deletes_one_ok(S), lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="git branch -d push-b698; echo EXIT $?")])),
    ('G-ANSWERS-CHECKED', 'the citation bank`s mid-act prints read at HEAD, each before the step its answer governs',
     lambda S: answers_checked_ok(S), lambda S: put(S, 't', dict(S['t'], c2=1))),
    ('G-SCORER-READS-BANKS', 'tools/b699_record.py`s code, prose stripped: the N1-N4 scorers reading banks and commits and no ledger, the scores bank written once, the entry`s scores line from it',
     lambda S: scorer_banks_ok(S), lambda S: put(S, 'rec_src', S['rec_src'].replace("def _n2():", "def _n2():\n    _x = rd(FIND)"))),
    ('G-ENTRY-SCORES-EQUAL', 'FINDINGS at the findings bank`s line and the scores bank: the entry`s scores line equal to the line composed from the bank',
     lambda S: entry_scores_ok(S), lambda S: _mut(S, 'sc', lambda d: d.update(N1=['REFUTED', 'planted']))),
    ('G-ENTRY-TITLE-FORM', 'FINDINGS at the findings bank`s line and the record tool`s title from the banks: the ferry`s form adjusted to what the act did',
     lambda S: entry_title_ok(S), lambda S: put(S, 'find', S['find'].replace('cells at PATHS :285 regenerated', 'cells at PATHS :285 held'))),
    ('G-CORRIGENDUM-ENTERED', 'FINDINGS at the corrigendum`s landing line, found by conv, the corrigendum bank and its json: G-NOTHING-RAN-AHEAD by its two commits as the arm reads them ((R309)(2))',
     lambda S: corrigendum_ok(S), lambda S: _mut(S, 'corrland', lambda d: d['lines'][0].update(line=1))),
    ('G-CORRIGENDA-ROWS', 'data/b675_corrigenda.txt before the act, now and at HEAD, and Component 1`s commit: rows (11)-(13) appended beneath it, every line above unchanged ((R309)(2))',
     lambda S: corrigenda_rows_ok(S), lambda S: put(S, 'shared', dict(S['shared'], **{'data/b675_corrigenda.txt': (b'x', b'y', b'y')}))),
    ('G-TIE-PRINTED-FIRST', 'the tie bank and its json: b674`s rule verbatim and every kernel row printed before the document is named, SIDE-substrate-cluster named (N2)',
     lambda S: tie_first_ok(S), lambda S: _mut(S, 'tiej', lambda d: d.update(named='SIDE-x'))),
    ('G-RECUT-CUT', 'the cut bank and its json: the distance 1 to 0, the merged tree the built tree, v0.4.1 peeled to the merge ((R309)(3), N3)',
     lambda S: recut_ok(S), lambda S: _mut(S, 'cutj', lambda d: d.update(after=1))),
    ('G-PRINTS-EQUAL', 'the prints bank: the 11 terminals of the before-run and the after-run equal line for line (N3)',
     lambda S: prints_equal_ok(S), lambda S: put(S, 'prints_ki', S['prints_ki'].replace('DIFFERING 0', 'DIFFERING 1'))),
    ('G-QUOTE-BEFORE-MERGE', 'the quotation bank and its json against the merge`s commit time: the search at the cut`s base and tip before the merge, the control firing, no quoting line left (data/b690_rules.txt row (2), N3)',
     lambda S: quote_first_ok(S), lambda S: put(S, 't', dict(S['t'], merge=1))),
    ('G-TAG-CELLS-RAISED', 'the dry bank over the cells naming SIDE-substrate-cluster, the tag-cell prompt`s time and Component 2`s commit: the dry run printed, the prompt put, nothing written ((R309)(3))',
     lambda S: tag_cells_ok(S), lambda S: put(S, 'dry_sub', S['dry_sub'].replace('WOULD CHANGE 0', 'WOULD CHANGE 1'))),
    ('G-ARCH-CELLS-REGENERATED', 'the archimedean dry bank, the cell prompt`s time, the page`s commit and the page at HEAD: the dry run before the prompt, the generator alone writing :285, v0.1.1 ((R309)(4), N2)',
     lambda S: arch_cells_ok(S), lambda S: put(S, 'page_paths', S['page_paths'].replace('| SIDE-archimedean v0.1.1 |', '| SIDE-archimedean v0.1.0 |'))),
    ('G-ONECOPY-ENTERED', 'OPEN_TRAILS at the one-copy bank`s line and the one-copy bank: the PATHS partner copy`s 24 differing lines entered beneath W-ORD-ONE-COPY, the stored 4 named (the author`s word on "run")',
     lambda S: onecopy_ok(S), lambda S: put(S, 'onecopy', S['onecopy'].replace('DIFFER IN 24 LINES', 'DIFFER IN 4 LINES'))),
    ('G-BRIDGE-PLAN-BINDERS', 'the bridge plan and its commit: the 14 binders each with its translation before any statement, nothing compiled, the plan committed alone ((R309)(5), N4)',
     lambda S: bridge_plan_ok(S), lambda S: put(S, 'plan', S['plan'].replace('| THE TRANSLATION:', '| A TRANSLATION:', 1))),
    ('G-BRIDGE-ORDER-ENTERED', 'OPEN_TRAILS at the bridge bank`s line, found by conv: W-ORD-H2-BRIDGE-THEOREM entered beneath W-ORD-H2-BRIDGE ((R309)(5))',
     lambda S: bridge_order_ok(S), lambda S: _mut(S, 'bridgej', lambda d: d['lines'][0].update(line=1))),
    ('G-READFIRST-DIFF-BANKED', 'the readfirst diff bank and the step-zero commit, and the hand list`s blob at HEAD against step zero`s: the diff banked, no bank rewritten',
     lambda S: readfirst_diff_ok(S), lambda S: put(S, 'rf_hand_now', b'x')),
    ('G-TOOL-REPAIRS', 'the repairs bank`s verdict: the carry-time repairs, each by the defect or order it answers, no shared tool edited, no frozen bank edited',
     lambda S: repairs_ok(S), lambda S: put(S, 'repairs', S['repairs'].replace('REPAIRS %d ;' % REPAIRS_WANT, 'REPAIRS 0 ;'))),
    ('G-PARTS-PRERUN', 'the pre-run bank`s six parts with their seconds, named in the form the parts arm reads',
     lambda S: parts_ok(S), lambda S: put(S, 'prerun', S['prerun'].replace('PART standing-b3', 'PART standing-x'))),
    ('G-ARM-SECONDS-BANKED', 'the per-arm seconds bank: every standing arm clocked at the pre-run, the three slowest named, each part`s seconds',
     lambda S: arm_seconds_ok(S), lambda S: _mut(S, 'asec', lambda d: d.update(clocked=0))),
    ('G-DEFECTS-LETTERED', 'the defects bank read at HEAD: the sealed letters its prefix, consecutive letters, owners the seat or the navigator',
     lambda S: defects_ok(S), lambda S: put(S, 'defects', S['defects'].replace("(a) THE SEAT'S", "(a) THE AUTHOR'S"))),
    ('G-READ-RULE', 'the read-call bank (data/b698_rules.txt row (2)) and the defects bank: every whole read of a file of two hundred lines or more entered by its transcript line',
     lambda S: read_rule_ok(S), lambda S: put(S, 'defects', S['defects'].replace('transcript line', 'line'))),
    ('G-SPEC-PLANTED', 'tools/b699_regspec.py`s planted rows run live through the record tool`s readers, and rows of another shape refused',
     lambda S: bool(S['spec']['read']) and all(S['spec']['read']) and all(S['spec']['controls']) and any('branch' in x for x in S['spec']['shapes']),
     lambda S: _mut(S, 'spec', lambda d: d['controls'].append(False))),
    ('G-CONVERSION-ONE', 'every b699 tool`s code: no conversion defined (conv imported from b652_record); the suite importing it',
     lambda S: S['conv_bad'] == [] and 'from b699_record import conv' in S['suite'], lambda S: put(S, 'conv_bad', ['b699_checks.py'])),
    ('G-WORKFLOW-FILES', 'this act`s kernel workflow at SIDE-substrate-cluster: equal to its write at cebec19, no author identifier, no secret, the hold, the lake path and no cache step for its Mathlib-free lakefile, the print step over its list, the files b699 wrote',
     lambda S: wf_ok(S), lambda S: _mut(S, 'wf', lambda d: d[K.KERNEL].update(text=d[K.KERNEL]['text'] + ' secrets.X'))),
    ('G-RUNNER-READ', 'this act`s two runs through b699`s record tool`s reader: before at main, after at the cut`s tip, success, the artifact`s sha256, the memory low above the hold',
     lambda S: runner_ok(S), lambda S: _mut(S, 'runner', lambda d: [r.update(mem_low=2000) for r in d['rows']])),
    ('G-RUNNER-GATE', 'this act`s gate readings: build exit 0, no error line, no sorryAx in the print step, the artifact`s digest agreeing, both runs',
     lambda S: gate_ok(S), lambda S: put(S, 'rbanks', dict(S['rbanks'], **{'x_after': 'GATE NOT DERIVES'}))),
    ('G-MERGES-ON-GATE', 'SIDE-substrate-cluster`s main (b699`s merge): the merge at main, its parents the print list`s commit and the gated tip, the merged tree the built tree, v0.4.1 at the merge naming v0.4, no other tag',
     lambda S: merges_ok(S), lambda S: _mut(S, 'mainst', lambda d: d['tags'].append('v0.5'))),
    ('G-NO-SORRY-MAIN', 'tools/no_sorry_main.py run at HEAD over every kernel, its remote read once by this run: no `sorry` in code, every pair equal',
     lambda S: no_sorry_main(S), lambda S: _live(S, lambda d: d['nsm'][0]['hits'].append(('x.lean', 1, 'sorry')))),
    ('G-NO-SORRY-MAIN-PLANTED', 'tools/test_no_sorry_main.py run: 5 of 5', lambda S: planted_ok(S, 'test_no_sorry_main.py', 5),
     lambda S: _planted(S, 'test_no_sorry_main.py')),
    ('G-AXIOM-CLAIM', 'tools/axiom_claim.py run at HEAD over every kernel against the banked prints: no claim CONTRADICTED', lambda S: axiom_claim(S),
     lambda S: _live(S, lambda d: d['ac'].append(dict(d['ac'][0], verdict='CONTRADICTED')))),
    ('G-AXIOM-CLAIM-PLANTED', 'tools/test_axiom_claim.py run: 12 of 12', lambda S: planted_ok(S, 'test_axiom_claim.py', 12),
     lambda S: _planted(S, 'test_axiom_claim.py')),
    ('G-MODULE-HEADER', 'tools/module_header.py run at HEAD over every kernel: no header OVERREACHES', lambda S: module_header(S),
     lambda S: _live(S, lambda d: d['mh'].append(dict(kernel='x', file='x.lean', line=1, name='x', why='planted')))),
    ('G-MODULE-HEADER-PLANTED', 'tools/test_module_header.py run: 12 of 12', lambda S: planted_ok(S, 'test_module_header.py', 12),
     lambda S: _planted(S, 'test_module_header.py')),
    ('G-CONVERSION-TEST', 'tools/test_conversion_b652.py run: 7 of 7', lambda S: planted_ok(S, 'test_conversion_b652.py', 7),
     lambda S: _planted(S, 'test_conversion_b652.py')),
    ('G-PP-SCOPE', 'PLACE-papers` changed files against FINDINGS, OPEN_TRAILS and the PATHS page (the page through the generator on the author`s word; N5)',
     lambda S: corpus_scope(S), lambda S: put(S, 'pp_changed', S['pp_changed'] + ['day1/ONE_PAGE_PROOF.md'])),
    ('G-CURRENTS-UNEDITED', 'the map, the census, the monograph, the Dirichlet page, the surround, both SIMPLICITY copies, README, REGISTRY, the faces page, FOUNDATIONS and its one-copy partner, INSTRUMENTS, the PATHS partner copy and the substrate pages: working tree, before and HEAD',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'ERRATA.md': (b'x', b'y', b'y')}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read before the seal',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b698`s to b693`s sealed tools and the earlier tools, the readers, the push tool, the act-root tool, the generators and their tests, the corrigendum tools, edit_route.py, chain_page.py, e0_rule.py, the witness`s window, the mirror`s and the shared tools, rule_arms.py among them: before, working tree and HEAD',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'additive_shared.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 14a0cb57 but the shared additive files (act_roots.txt among them) and the corrigenda bank`s appended rows, by blob id',
     lambda S: S['prior_bad'] == [] and S['prior_n'] > 0, lambda S: put(S, 'prior_bad', ['data/b698_stepzero.txt'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS before and now', lambda S: S['fi_pre'] is not None and (S['fi_now'] or b'').startswith(S['fi_pre']),
     lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS before and now', lambda S: S['ot_pre'] is not None and (S['ot_now'] or b'').startswith(S['ot_pre']),
     lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-NODISCLOSURE-PUBLIC', 'TECHNE-Core`s needle sets over every public byte the act writes: the ledger lines, the banks and the tools',
     lambda S: bool(S['nd_pub']) and not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', {'method': 1})),
    ('G-OUTSIDE-NAMED-NOWHERE', 'the ledger lines appended', lambda S: S['outside'] == [], lambda S: put(S, 'outside', ['x'])),
    ('G-DELETE-FREE', 'the act`s tools` code, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='os' + '.remove(p)'))),
    ('G-PUBLISH-UNCALLED', 'the act`s tools` code: no publish call', lambda S: publish_uncalled(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='z_' + 'publish()'))),
    ('G-SEALED-AFTER-COMPONENTS', 'the lock time against every relay and PLACE-papers commit of the act by its subject', lambda S: sealed_after_ok(S),
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b699 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'b699_closing.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3), in six parts summed',
     lambda S: S['lock_epoch'] is not None and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b698`s trail record on OPEN_TRAILS and its root in the chain', lambda S: '### b698 — lane two, act one hundred and twenty-five, the research act' in S['ot']
     and S['rootsf'].count(NL + 'b698 ') == 1, lambda S: put(S, 'ot', S['ot'].replace('### b698 — lane two', '### b698 - lane two'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], grade_moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 76th chain row (the corrigendum row apart), the root bank and its items, the cut, the bridge plan and the corrigendum among them, no binary, mirror, chain-half or untracked bank',
     lambda S: root_banked_ok(S), lambda S: put(S, 'rootsf', S['rootsf'] + 'b700 x y' + NL)),
    ('G-ROOT-BANKS-COMMITTED', 'the root route`s banked reading and every named bank`s blob at the root`s recorded commit: clean and equal at HEAD, HEAD the remote main, the recorded hash carried by the recorded commit',
     lambda S: root_banks_committed_ok(S), lambda S: put(S, 'rootbanks', dict(S['rootbanks'], pushed=False))),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit in two halves by act with the suite`s own remote reads: standing-b2`s banked b624-b658 and standing-b3`s b659-b699 all AGREE, the boundary link equal, b680 read through its corrigendum row (4 banks), b699 written LF',
     lambda S: verify_ok(S), lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s through conv, and its parts', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line, the head through conv', lambda S: bool(S['tj'].get('line'))
     and oline(S, S['tj']['line']) == conv(S['REC'].TRAIL_HEAD()), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b699 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b699_record.py agree', 'b699_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line: b700', lambda S: '**Next:** b700' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** b700', '**Next:** b701'))),
] + [('G-N%d-SCORED' % i, 'the scores through the record tool`s reader, and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i),
      lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written since 14a0cb57 and 1a8d8d1 against the (W) globs',
     lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b699')" in S['suite'] and "'data/b699_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b699_closing.py: the closing sentence in the rule`s words with the plain reads named; the citation check, the record lines, the dry run, the corrigendum, the re-cut, the cells, the bridge, the kernels, the mirror, the carry-time reading',
     lambda S: closing_sentence_ok(S), lambda S: put(S, 'closing_src', S['closing_src'].replace('no identifier of the author ' + 'in any outbound', 'x'))),
    ('G-LSREMOTE-ONE-PER-REPO', 'the part`s ls-remote calls per repository, read after every other arm of the part has run (OPEN_TRAILS :12703)',
     lambda S: lsr_ok(S), lambda S: put(S, 'lsr', {PP: 2})),
] + [(nm, 'tools/rule_arms.py (the author`s word on (R293)(6); (R301)(6) for four; G-RULE-SUITE-PARTS as repaired under (R302)(2); G-RULE-BINARY-HASHES as repaired under (R306)(2)), the trace -- ' + reads,
      (lambda p: lambda S: p(S['ra']))(pred), (lambda pl: lambda S: put(S, 'ra', pl(S['ra'])))(plant)) for nm, reads, pred, plant in RA.ARMS]


def _part_of(name):
    if name in K.ACT_ARMS:
        return 'act'
    if name in B1_ARMS:
        return 'standing-b1'
    if name in B2_ARMS:
        return 'standing-b2'
    if name in B3_ARMS:
        return 'standing-b3'
    if name in C_ARMS:
        return 'standing-c'
    return 'standing-a'


def regenerate():
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'terminal_table.py')], capture_output=True, text=True, encoding='utf-8', errors='replace')
    try:
        diff = json.loads(rd('terminal_table_diff.json') or '{}')
    except Exception:
        diff = {}
    return r.returncode, diff


def seal():
    face = read(FACE)
    lock = utc_epoch(face, 'locked at (UTC)')
    p = os.path.join(D, 'b699_seal_hashes.json')
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
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)
    for t in K.SEALED:
        print('  %-38s %s' % (t, now[t]))
    print('  written: b699_seal_hashes.json')
    return 0


def _base_name(pushed):
    if PRERUN:
        return 'b699_arms_prerun.txt'
    if MID and len(sys.argv) > sys.argv.index('--mid') + 1:
        return sys.argv[sys.argv.index('--mid') + 1]
    if RERUN and len(sys.argv) > sys.argv.index('--rerun-postpush') + 1:
        return sys.argv[sys.argv.index('--rerun-postpush') + 1]
    return 'b699_checks_postpush.txt' if pushed else 'b699_checks.txt'


def _part_name(base, part):
    return base.replace('.txt', '_%s.txt' % part)


def _write(name, lines):
    out = os.path.join(D, name)
    b = (NL.join(lines) + NL).encode('utf-8')
    with open(out + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(out + '.tmp', out)
    return out


PART_FOOT = re.compile(r'### PART ([\w-]+) : ARMS (\d+) ; LIVE PASSING (\d+) ; LIVE FAILING (\d+) (\[[^\]]*\]|NONE) ; NEGATIVE-CONTROL FAILURES (\d+) ; '
                       r'POSITIVE-CONTROL PASSES (\d+) (\[[^\]]*\]|NONE) ; DECLARED EQ RUN (\w+) ; (\d+) s')


def combine():
    base = sys.argv[sys.argv.index('--combine') + 1]
    parts, heads = [], []
    for part in K.PARTS:
        t = rd(_part_name(base, part))
        m = PART_FOOT.search(t)
        if not m or m.group(1) != part:
            print('### THE PART BANK %s HAS NO FOOTER -- NOTHING WRITTEN' % _part_name(base, part))
            return 2
        parts.append((part, m, t))
        heads.append(t.split(NL)[1] if len(t.split(NL)) > 1 else '')
    n = sum(int(m.group(2)) for _p, m, _t in parts)
    lp = sum(int(m.group(3)) for _p, m, _t in parts)
    lf = sum(int(m.group(4)) for _p, m, _t in parts)
    ng = sum(int(m.group(6)) for _p, m, _t in parts)
    pc = sum(int(m.group(7)) for _p, m, _t in parts)
    fails = sum((json.loads(m.group(5)) if m.group(5) != 'NONE' else [] for _p, m, _t in parts), [])
    defs = sum((json.loads(m.group(8)) if m.group(8) != 'NONE' else [] for _p, m, _t in parts), [])
    deq = all(m.group(9) == 'True' for _p, m, _t in parts)
    ok = lf == 0 and pc == 0 and ng == 0 and deq
    out = ['=' * 104, heads[0].replace('PART standing-a', 'SIX PARTS SUMMED'), '=' * 104] + [
        '  ### PART %s : ARMS %s ; %s s' % (p, m.group(2), m.group(10)) for p, m, _t in parts] + [
        '  ### the parts` seconds summed %d ; the longest part %s s, under the 590 s guard %s' % (
            sum(int(m.group(10)) for _p, m, _t in parts), max(int(m.group(10)) for _p, m, _t in parts),
            max(int(m.group(10)) for _p, m, _t in parts) < 590),
        '  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (n, lp, lf, fails or ''),
        '  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (ng, pc, defs or ''),
        '  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'), '=' * 104, '']
    for p, _m, t in parts:
        out += ['### THE PART BANK %s, WHOLE:' % _part_name(base, p)] + t.rstrip(NL).split(NL) + ['']
    _write(base, out)
    ex = {}
    for part in K.PARTS:
        ex.update(jl('b699_exercise_%s.json' % part).get('exercise') or {})
    if ex and base in ('b699_checks.txt', 'b699_checks_postpush.txt'):
        e = (json.dumps(dict(exercise=ex, run=n, live_failing=fails, defective=defs, neg_failures=ng), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p_ = os.path.join(D, 'b699_exercise.json')
        with open(p_ + '.tmp', 'wb') as fh:
            fh.write(e)
        os.replace(p_ + '.tmp', p_)
    print(NL.join(out[3:14]))
    print('  written: %s' % base)
    return 0 if ok else 1


def main():
    if SEAL:
        return seal()
    if COMBINE:
        return combine()
    if PART not in K.PARTS:
        print('### every run in six foreground parts -- give `--part %s`' % ' | '.join(K.PARTS))
        return 2
    fm = free_mb()
    if fm < K.HOLD:
        print('%s  ### THE HOST`S FREE MEMORY %d MB, BENEATH THE HOLD %d MB: PART %s NOT RUN ((R294)(2))' % (
            time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), fm, K.HOLD, PART))
        return 3
    t_start = time.time()
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    base = _base_name(pushed)
    rec('=' * 104)
    rec('b699 -- THE SUITE. ### **%s READING.** ### PART %s ### every arm exercised on both controls.' % (
        'PRE-SEAL (R202)(3)' if PRERUN else 'MID-ACT' if MID else 'POST-PUSH' if pushed else 'PRE-PUSH', PART))
    rec('### the host`s free memory at the part`s start %d MB (the hold %d MB)' % (fm, K.HOLD))
    if PRERUN or MID:
        rec('### run at (UTC) : %s   ### %s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                                              'the standing line of (R202)(3): every arm run at HEAD before the face is sealed, its count printed.'
                                              if PRERUN else 'a mid-act re-run; no table regenerated.'))
    rec('=' * 104)
    S = sources(NEED[PART])
    S['pushed'] = pushed
    if PART == 'standing-b3':
        S['half_a'] = jl(half_bank(0, _run_key(base)))
    t1 = time.time()
    regen = PART == 'act' and not (RERUN or PRERUN or MID)
    rc_gen, gen_diff = regenerate() if regen else (0, dict(rerun=True))
    S['phase_secs']['the table regenerated' + ('' if regen else ' (not in this part or run)')] = time.time() - t1
    rec('  ### THE PHASES, IN SECONDS: %s' % '; '.join('%s %.0f' % kv for kv in S['phase_secs'].items()))
    rec('  ### THE LONGEST PHASE %.0f s ; above 450 s: %s (b675 rules row 2)' % (max(S['phase_secs'].values()), max(S['phase_secs'].values()) > 450))
    declared = g2_names(S['face'])
    names = [a[0] for a in ARMS]
    S['declared_eq_run'] = sorted(names) == declared and len(names) == len(set(names))
    arms = [a for a in ARMS if _part_of(a[0]) == PART]
    rec('  arms in the (G2) block : %d ; in the suite : %d ; run in this part : %d' % (len(declared), len(names), len(arms)))
    if set(names) != set(declared):
        rec('  ### declared not run : %s' % sorted(set(declared) - set(names)))
        rec('  ### run not declared : %s' % sorted(set(names) - set(declared)))
    rec('  ### (R264)(2) THE FREEZE: the standing arms (b698`s face less its own arms, the twenty-four rule arms among them; none added) %d ; '
        'carried here %d ; the act`s arms over its own banks %s ; arms beyond both %s' % (
            len(S['standing']), len(set(names) & set(S['standing'])), sorted(set(names) - set(S['standing'])),
            sorted(set(names) - set(S['standing']) - set(K.ACT_ARMS)) or 'NONE'))
    rec('  ### standing arms not carried here: %s' % (sorted(set(S['standing']) - set(names)) or 'NONE'))
    if 'rules' in NEED[PART]:
        rec('  ### THE RULE ARMS, EACH WITH ITS COUNT (tools/rule_arms.py; rows read, rows failing, the reading); the call trace %d calls:' % len(
            S['ra'].get('calls') or []))
        for nm in RA.NAMES:
            ok_, n_, b_, note = RA.reading(nm, S['ra'])
            rec('  ###   %-28s %-4s read %d ; failing %d ; %s' % (nm, 'PASS' if ok_ else 'FAIL', n_, b_, note[:260]))
    if 'chain_a' in NEED[PART] or 'chain_b' in NEED[PART]:
        i = 0 if 'chain_a' in NEED[PART] else 1
        av = S['ar_verify']
        bd = S['boundary']
        rec('  ### THE ACT-ROOT CHAIN`S %s HALF, %s-%s, recomputed at commit: %s' % ('FIRST' if i == 0 else 'SECOND', K.CHAIN_HALVES[i][0], K.CHAIN_HALVES[i][1],
                                                                                  '; '.join('%s %s%s' % (a, v, (' (' + '; '.join(w) + ')') if w else '') for a, v, w in av) or 'no act rooted'))
        rec('  ### THE BOUNDARY (relay data/act_roots.txt): %s root %s ; %s previous %s ; equal %s' % (bd['first'], bd['root'], bd['second'], bd['previous'], bd['equal']))
        if i == 0:
            rec('  ### the reads at commit, b658: %s' % S['ar_reads'].get('b658'))
            rec('  ### standing-b2 CARRIES NO ARM: its verdicts banked for standing-b3 in relay data/%s' % half_bank(0, _run_key(base)))
        else:
            ha = S['half_a'] or {}
            rec('  ### the reads at commit, b680: %s ; b699: %s' % (S['ar_reads'].get('b680'), S['ar_reads'].get('b699')))
            rec('  ### THE FIRST HALF AS standing-b2 BANKED IT (relay data/%s): %d acts, AGREE %d, at HEAD %s (now %s), its boundary equal %s' % (
                half_bank(0, _run_key(base)), len(ha.get('acts') or []), sum(1 for x in ha.get('acts') or [] if x[1] == 'AGREE'), (ha.get('head') or '-')[:12],
                gs(ROOT, 'rev-parse', 'HEAD')[:12], (ha.get('boundary') or {}).get('equal')))
        write_half(i, _run_key(base), av, S['ar_reads'])
    sj = S['sealj'].get('tools') or {}
    rec('  ### THE SEALED TOOLS, recorded at the seal %s : %s' % (S['sealj'].get('at', '### NOT RECORDED'), '; '.join(
        '%s %s' % (t, ('agree' if sj.get(t) == S['sealnow'].get(t) else 'DIFFER') if t in sj else 'not recorded') for t in K.SEALED)))
    off = S['REC'].edit_route_offences(S['cmds'] + S['prev_cmds'])
    rec('  ### G-EDIT-ROUTE read %d captured commands of this act and %d of the previous act after its post-push suite; offences %d: %s' % (
        len(S['cmds']), len(S['prev_cmds']), len(off), ['#%s %s' % (r['n'], [k for k, _ in o]) for r, o in off] or 'none'))
    mc = re.search(r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', S['citation'])
    rec('  ### THE CITATION CHECK: %s' % (mc.group(0) if mc else '### NOT READ'))
    rec('  ### PLACE-papers` changed files %d against the allowed %d (the two ledgers and the PATHS page): beyond %s' % (
        len(S['pp_changed']), len(S['pp_allowed']), sorted(set(S['pp_changed']) - set(S['pp_allowed'])) or 'NONE'))
    if 'live' in NEED[PART]:
        lv = S['live']
        rec('  ### THE THREE ARMS AT HEAD (seconds %s):' % ', '.join('%.0f' % x for x in lv['secs']))
        rec('  ###   G-NO-SORRY-MAIN read %d kernels` mains, pairs unequal %d; sorry in code %d: %s' % (
            len(lv['nsm']), sum(1 for r in lv['nsm'] if not r['equal']), len(nsm_hits(S)), '; '.join('%s %s:%d' % h for h in nsm_hits(S)) or 'none'))
        rec('  ###   G-AXIOM-CLAIM read %d claims: CONTRADICTED %d, UNVERIFIABLE %d, VERIFIED %d, UNBOUND %d, MENTION %d' % (
            sum(1 for r in lv['ac'] if r['verdict'] != 'OUT OF SCOPE'), ac_count(lv['ac'], 'CONTRADICTED'), ac_count(lv['ac'], 'UNVERIFIABLE'),
            ac_count(lv['ac'], 'VERIFIED'), ac_count(lv['ac'], 'UNBOUND'), ac_count(lv['ac'], 'MENTION')))
        rec('  ###   G-MODULE-HEADER read %d headers: OVERREACHES %d rows %s' % (sum(v['headers'] for v in lv['mh_per'].values()), len(lv['mh']),
                                                                             ['%s %s:%s' % (x.get('kernel'), x.get('file'), x.get('line')) for x in lv['mh']][:6] or ''))
    rec('  %-46s %-5s %-5s %-5s %-8s %s' % ('arm', 'LIVE', 'NEG', 'POS', 'secs', 'verdict'))
    rec('  ' + '-' * 106)
    fail, defective, negfail, EX, SECS = [], [], 0, {}, {}
    for name, reads, pred, pos in arms:
        if name == 'G-ARMS-NO-LIVE-LIMB':
            S['no_live_limb'] = not defective
        ta = time.time()
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
        SECS[name] = round(time.time() - ta, 4)
        if not live:
            fail.append(name)
        if neg != live:
            negfail += 1
        if posv:
            defective.append(name)
        EX[name] = dict(live=live, neg=neg, pos=posv, reads=reads, secs=SECS[name])
        rec('  %-46s %-5s %-5s %-5s %-8.3f %s' % (name, 'PASS' if live else 'FAIL', 'PASS' if neg else 'FAIL', 'PASS' if posv else 'FAIL', SECS[name],
                                                 'OK' if (live and neg and not posv) else ('### POS PASSES -- DEFECTIVE' if posv else '### FAILS')))
    if not arms:
        rec('  (no arm in this part)')
    rec('')
    if 'written' in NEED[PART]:
        rec('  ### tracked files written (%d), each against the (W) globs: uncovered %s' % (len(S['written']), [f for f in S['written']
                                                                                              if not any(fnmatch.fnmatch(f, p) for p in S['globs'])] or 'NONE'))
        rec('  ### G-PRIORBANK-UNCHANGED checked %d relay data banks tracked at %s by blob id; changed %s' % (S['prior_n'], PRE['relay'], S['prior_bad'] or 'NONE'))
    lsr = dict(KC0.LSR)
    rec('  ### OPEN_TRAILS :12703: ls-remote calls this part, per repository: %d repositories, at most %d each' % (len(lsr), max(lsr.values()) if lsr else 0))
    if regen:
        rec('  ### ### **(R107): THE GENERATOR WAS RE-RUN BY THIS SUITE.** ### exit %d.' % rc_gen)
        rec('  ###   rows added %d ; rows gone %d ; grade-or-profile changed %d %s' % (len(gen_diff.get('added') or []), len(gen_diff.get('gone') or []),
                                                                                 len(gen_diff.get('changed') or []), (gen_diff.get('changed') or '')[:20]))
    secs = time.time() - t_start
    rec('  ### the arms` own seconds summed %.1f, the slowest %s' % (sum(SECS.values()), ', '.join('%s %.2f' % kv for kv in sorted(SECS.items(), key=lambda x: -x[1])[:3]) or 'NONE'))
    rec('  ### the run took %.0f s' % secs)
    rec('  ### PART %s : ARMS %d ; LIVE PASSING %d ; LIVE FAILING %d %s ; NEGATIVE-CONTROL FAILURES %d ; POSITIVE-CONTROL PASSES %d %s ; '
        'DECLARED EQ RUN %s ; %d s' % (PART, len(arms), len(arms) - len(fail), len(fail), json.dumps(fail) if fail else 'NONE', negfail, len(defective),
                                       json.dumps(defective) if defective else 'NONE', S['declared_eq_run'], int(secs)))
    rec('=' * 104)
    out = _write(_part_name(base, PART), L)
    lp = os.path.join(D, _part_name(base, PART).replace('b699_arms_prerun', 'b699_lsr_prerun').replace('b699_checks', 'b699_lsr').replace('.txt', '.json'))
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    with open(lp + '.tmp', 'wb') as fh:
        fh.write(lb)
    os.replace(lp + '.tmp', lp)
    if PRERUN:
        sb = (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), part=PART, arms=SECS,
                              phases=dict((k, round(v, 1)) for k, v in S['phase_secs'].items()), run_secs=round(secs, 1)),
                         indent=1, ensure_ascii=False) + NL).encode('utf-8')
        sp = os.path.join(D, 'b699_arm_seconds_%s.json' % PART)
        with open(sp + '.tmp', 'wb') as fh:
            fh.write(sb)
        os.replace(sp + '.tmp', sp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(arms), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b699_exercise_%s.json' % PART)
        with open(p + '.tmp', 'wb') as fh:
            fh.write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if (not fail and not defective and negfail == 0 and S['declared_eq_run']) else 1


if __name__ == '__main__':
    sys.exit(main())
