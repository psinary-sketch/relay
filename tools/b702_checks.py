# -*- coding: utf-8 -*-
"""b702_checks.py -- THE SUITE OF b702, UNDER (R312): b701 AT ITS WEIGHT; THE UNDECLARED FAILURES AND THE UNLETTERED ITEMS BY CORRIGENDUM; THE
GUARD RESTORED; THE NEXT DOCUMENT CUT; THE FACES ROW, THE README AND THE PARTNER-COPIES RESOLUTIONS RAISED; TWO ORDERS AND A SPEC ROW ENTERED;
SIX PARTS, THE CHAIN SPLIT BY ACT.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### data/b684_rules.txt row (1) and b693's split: every run in SIX foreground parts, each its own call in its own message -- `--part
### standing-a`, `--part standing-c` (G-PRIORBANK-UNCHANGED, G-NODISCLOSURE-PUBLIC, G-WRITELIST-KINDS), `--part standing-b1` (the shared
### additive files), `--part standing-b2` (the act-root chain's first half, b624-b658, its verdicts banked, NO ARM), `--part standing-b3` (the
### second half, b659-b702, and G-ACTROOT-VERIFY once over both halves' verdicts), `--part act` (the act's arms over this act's banks, the
### table regenerated in a closing run); each under the 590 s guard the seat runs it in, and NOT RUN beneath the 2,560 MB hold; `--combine
### <bank>` writes the bank. The chain halves as b693 drew them with b702 added to the second (the ferry's Component 5).
### ### (R264)(2), THE FREEZE: the standing arms are b701's face's (G2) arms less b701's own arms over b701's banks, carried, the twenty-four
### rule arms of tools/rule_arms.py among them, unedited; no standing arm added (N5). The act's own arms read this act's banks alone (ACT_ARMS).
### The standing runner arms (G-WORKFLOW-FILES, G-RUNNER-READ, G-RUNNER-GATE, G-MERGES-ON-GATE) read the LAST MERGED RUN -- b701's at
### SIDE-explicit-formula (v0.35 = d4e046a, run 39635057369), no runner being dispatched this act (a paper is the table's next document) --
### through b701's banks and the record tool's reader (b700's form).
### ### (R312)(2): THE PRERUN GUARD RESTORED -- the per-part seconds bank is written under `if PRERUN:` alone, as b700 had it (tools/b700_checks.py
### :1669), so no root-named bank is written by the pre-push or post-push run; `--guard-dry` prints, for each run mode, what the writer block
### would write, writing nothing (the dry run of (R312)(2), banked by the record tool as data/b702_guard_dry.txt).
### ### Every look-up of a landed line goes through the one conversion (imported from tools/b652_record.py through tools/b702_record.py).
### ### The harness is b568's to b701's, written by the Write tool from tools/b701_checks.py; the sources, predicates and arms over this act's
### ### banks are b702's. data/b686_rules.txt row (1): the act arm G-ENTRY-SCORES-EQUAL reads the landed entry; no scorer reads a ledger line.
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
import b702_worklist as K     # noqa: E402
import b701_worklist as K701  # noqa: E402
import b700_worklist as K700  # noqa: E402
import b699_worklist as K699  # noqa: E402
import b698_worklist as K698  # noqa: E402
import b697_worklist as K697  # noqa: E402
import b696_worklist as K696  # noqa: E402
import b695_worklist as K695  # noqa: E402
import rule_arms as RA        # noqa: E402
from b702_record import conv  # noqa: E402

NL = chr(10)
PP = K.PP
KI = K.KERNEL_DIR             # ### the kernel b701 wrote, read only this act: SIDE-explicit-formula
FACE = os.path.join(D, 'b702_registration_2026-10-21.txt')
B701_FACE = os.path.join(D, 'b701_registration_2026-10-21.txt')
B701_ACT_ARMS = K701.ACT_ARMS
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP)
EXPORT = K.EXPORT
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
SEAL = '--seal' in sys.argv
COMBINE = '--combine' in sys.argv
GUARD_DRY = '--guard-dry' in sys.argv
PART = sys.argv[sys.argv.index('--part') + 1] if '--part' in sys.argv and len(sys.argv) > sys.argv.index('--part') + 1 else None
L = []
# ### the sealed figures, the floors the count arms read at HEAD (standing from (R291)(3)): filled at the seal (stage two, by the Edit tool)
FLOORS = dict(prompts=1, calls=1, checks=1, defects=(('a', 'SEAT'),))
REPAIRED_TOOLS = K.REPAIRED_TOOLS
NEW_TOOLS = K.NEW_TOOLS
# ### the instruments read unedited: b701's list, b695's to b701's sealed tools and the earlier readers among them, less this act's sealed tools
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
             'circuit_correspondence.py', 'b700_corrigendum.py', 'b699_corrigendum.py')
INST = tuple(sorted((set(INST_BASE) | set(K695.SEALED) | set(K696.SEALED) | set(K697.SEALED) | set(K698.SEALED) | set(K699.SEALED) | set(K700.SEALED)
                     | set(K701.SEALED)) - set(K.SEALED) - set(REPAIRED_TOOLS) - set(NEW_TOOLS)))
# ### the corpus documents this act does not write: every page but the faces page (regenerated on the word), the monograph, the Dirichlet
# ### page, the surround, both SIMPLICITY copies, REGISTRY (its README row raised: no row exists), FOUNDATIONS and its partner, INSTRUMENTS, both
# ### PATHS copies, the substrate pages, the six other companions; the three the word may change -- README.md, THE_CLAUSE_AND_ITS_COMPILED_FACES.md
# ### and the cut document -- are read by their own arms
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md',
            'phase2/method/THE_KEYSTONE_CENSUS_v0_8.md', 'day1/A_Place_to_Stand_v5_18.md',
            'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md', 'day1/ONE_PAGE_PROOF.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md',
            'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md', 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', 'REGISTRY.md',
            'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md', 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md',
            'phase1.5/method/INSTRUMENTS.md', 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md', 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md',
            'phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md', 'phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM_v0_2.md',
            'day1/Exhaustive_Enumeration.md', 'day1/Which_Structure_Confines.md', 'day1/Spectral_Inertness.md', 'day1/Third_Identity_Element.md',
            'day1/Silence_of_Foundations.md')
TABLE_FILES = K.TABLE_FILES
WF, PT = '.github/workflows/build-module.yml', 'print_targets.txt'
B1_ARMS = ('G-SHARED-ADDITIVE',)        # ### standing-b1: the shared additive files
B2_ARMS = ()                            # ### standing-b2: the chain's first half, its verdicts banked, no arm
B3_ARMS = ('G-ACTROOT-VERIFY',)         # ### standing-b3: the chain's second half and the arm over both halves
C_ARMS = ('G-PRIORBANK-UNCHANGED', 'G-NODISCLOSURE-PUBLIC', 'G-WRITELIST-KINDS')   # ### standing-c's arms: the written files
NEED = {'standing-a': ('live', 'rules'), 'standing-c': ('written',), 'standing-b1': ('additive',), 'standing-b2': ('chain_a',),
        'standing-b3': ('chain_b',), 'act': ('efremote',)}
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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b702')
            and 'data/b702_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    import b702_record as REC
    return REC.capture()


def prev_now():
    import b702_record as REC
    return REC.prev_capture()


def ra_sources(lock):
    """tools/rule_arms.py's sources over the seat's session from (R312)'s anchor, its call trace extended by any continuation session's
    (K.SESSIONS_AFTER, none so far) through rule_arms.transcript; tools/rule_arms.py unedited."""
    R_ = RA.sources('b702', SESSION, K.ANCHOR, K.PARTS, lock, PRE['relay'], PRE['pp'])
    for sid, anc in K.SESSIONS_AFTER:
        R_['calls'] = list(R_.get('calls') or []) + RA.transcript('%s/%s.jsonl' % (PROJ, sid), anc)
    return R_


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
        if (f.startswith('b702_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks):
                bad.append(f)
    return bad


def spec_planted():
    import b702_regspec as SPEC
    P = SPEC.planted()
    ctl = [ok for _w, ok in SPEC.controls()]
    return dict(read=[ok for _s, ok, _w in P], controls=ctl, shapes=[s for s, _o, _w in P])


def _deps(ax):
    import b702_record as REC
    return REC._deps(ax)


def _tag_peel(tag):
    return gs(KI, 'rev-parse', '--verify', '--quiet', 'refs/tags/%s^{commit}' % tag)


def last_merges():
    """the last merged run's merge at SIDE-explicit-formula -- b701's v0.35 (b700's form: the previous act's merge, read through its banks),
    no runner being dispatched this act: the merge commit the tag peels to, its parents, the merged tree against the branch tip's as b701
    banked it (the branch deleted at this act's step zero on the word), the tag's message, the files against the main before b701."""
    m = _tag_peel(K701.BRIDGE_TAG)
    if not m:
        return []
    return [dict(tag=K701.BRIDGE_TAG, branch=K701.BRIDGE_BRANCH, merge=m, parents=gs(KI, 'log', '-1', '--format=%P', m).split(), tip=K701.BRIDGE_TIP,
                 prev_main=K701.EF_MAIN_BEFORE, trees=(gs(KI, 'rev-parse', m + '^{tree}'), gs(KI, 'rev-parse', K701.BRIDGE_TIP + '^{tree}')),
                 tagmsg=gs(KI, 'tag', '-l', '-n9', K701.BRIDGE_TAG),
                 files=sorted(x for x in gs(KI, 'diff', '--name-only', K701.EF_MAIN_BEFORE, m).split(NL) if x.strip()),
                 ct=int(gs(KI, 'log', '-1', '--format=%ct', m) or 0))]


def wf_state():
    """the kernel b701 wrote, read this act: its workflow at main against the commit that last wrote it (before b701), its lakefile's Mathlib
    requirement, its print list against b701's merged run's print bank, the files b701 wrote on its main; this act writes none."""
    t = read_blob(KI, 'main:' + WF)
    wrote = gs(KI, 'log', '-1', '--format=%H', 'main', '--', WF)
    lf = read_blob(KI, 'main:lakefile.toml') + read_blob(KI, 'main:lakefile.lean')
    req = re.search(r'(?im)^\s*require\b[^\n]*mathlib', lf) or re.search(r'(?is)\[\[require\]\][^\[]*name\s*=\s*"mathlib"', lf)
    pt = read_blob(KI, 'main:' + PT)
    merged = [r for r in (jl('b701_runner_rows.json').get('rows') or []) if r.get('ref') and git(KI, 'merge-base', '--is-ancestor', r['ref'], 'main')[0] == 0]
    last = merged[-1] if merged else None
    want = sorted(set([PT] + [f for f in (K701.BRIDGE_FILE,) if any(f in m['files'] for m in last_merges())]))
    return {K.KERNEL: dict(text=t, before=read_blob(KI, '%s:%s' % (wrote, WF)) if wrote else '', wrote=wrote,
                           wrote_before_act=bool(wrote) and git(KI, 'merge-base', '--is-ancestor', wrote, K701.EF_MAIN_BEFORE)[0] == 0,
                           lakefile=bool(lf.strip()), mathlib=bool(req), targets=[l.strip() for l in pt.split(NL) if l.strip()],
                           printed=len(_deps(rd('b701_axioms_%s_%s.txt' % (last['kernel'], last['label'])))) if last else 0,
                           act_writes=sorted(set(x for x in gs(KI, 'diff', '--name-only', K701.EF_MAIN_BEFORE, 'main').split(NL) if x.strip())),
                           this_act_writes=sorted(set(x for x in gs(KI, 'diff', '--name-only', K.EF_MAIN_BEFORE, 'main').split(NL) if x.strip())),
                           want=want)}


def _ef_sorry_code():
    """`sorry` tokens OUTSIDE comments and strings in every module under SIDEExplicitFormula/ at main, through tools/no_sorry_main.py's lean_code
    (b701's repair (6) carried): main's docstrings say "0 sorry" and a raw grep would refuse a clean main."""
    import no_sorry_main as NSM
    out = []
    for f in gs(KI, 'ls-tree', '-r', '--name-only', 'main', '--', 'SIDEExplicitFormula').split(NL):
        if f.strip().endswith('.lean'):
            out += ['%s:%d: %s' % (f.strip(), ln, t.strip()) for ln, t in NSM.sorry_hits(read_blob(KI, 'main:' + f.strip()))]
    return NL.join(out)


def g2_of(path):
    t = read(path)
    try:
        g2 = t[t.index('### (G2) THE GATE ARMS.'):t.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


STANDING = sorted((set(g2_of(B701_FACE)) - set(B701_ACT_ARMS)) | set(K.STANDING_ADDED))
TESTS = ('test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py')


def _ct(repo, rev):
    t = gs(repo, 'log', '-1', '--format=%ct', rev) if rev else ''
    return int(t) if t.isdigit() else None


def _added_ct(path):
    t = gs(ROOT, 'log', '--diff-filter=A', '--format=%ct', '--', path).split()
    return int(t[-1]) if t and t[-1].isdigit() else None


def _root_named_at_commit(arj):
    commit = (arj.get('commit') or {}).get('relay') or ''
    out = []
    for it in arj.get('items') or []:
        p = it.split()
        if p[0].startswith('data/') and len(p) == 2:
            b = blob(ROOT, '%s:%s' % (commit, p[0])) if commit else None
            out.append((p[0], b is not None, b is not None and hashlib.sha256(b).hexdigest() == p[1]))
    return out


# ================================================================== THE CHAIN SPLIT BY ACT (b693's, the halves as b693 drew them, b702 added)
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
    return base.replace('b702_', '').replace('.txt', '')


def half_bank(i, key):
    return 'b702_chain_half_%s_%s.json' % ('ab'[i], key)


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
    halves), 'additive' (the shared files), 'efremote' (one ls-remote of the kernel b701 wrote, the act part alone: widening-b701 stands)."""
    import b702_record as REC
    import b616_record as R6
    import edit_route as ER
    import b641_record as R41
    import additive_shared as ADD
    face = read(FACE)
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b702_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if (f.startswith('b702_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS)
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    cit = jl('b702_citation_check.json')
    try:
        REC.R._defect_short()
        refuses = False
    except TypeError:
        refuses = True
    t0 = time.time()
    merges = last_merges()
    runner = jl('b701_runner_rows.json')
    S = dict(
        REC=REC, ER=ER, face=face, ferry=rd('b702_ferry.txt'), scan=rd('b702_ferry_scan.txt'), stepz=rd('b702_stepzero.txt'),
        readfirst=rd('b702_readfirst.txt'), defects=rd('b702_defects.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        answers=rd('b702_author_answers.txt'), answersj=jl('b702_author_answers.json'), prerun=rd('b702_arms_prerun.txt'), rl=jl('b702_record_lines.json'),
        tests=jl('b702_tests_stepzero.json'), testst=rd('b702_tests_stepzero.txt'), withheld=jl('b702_tests_withheld.json'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b702_seal_hashes.json'), sealnow=sealed_now(), cmds=capture_now(), prev_cmds=prev_now(), cmdj=jl('b702_commands.json'),
        cmdt=rd('b702_commands.txt'), reads_bank=rd('b702_read_calls.txt'),
        planted={t: run_test(t) for t in TESTS}, spec=spec_planted(), conv_bad=conv_alone(), suite=read(os.path.join(T, 'b702_checks.py')),
        citation=rd(K.CITATION_BANK), cit_at=iso_epoch(cit.get('at') or ''), cit_misses=cit.get('misses') or [],
        gate=rd('b702_reg_gate.txt'), rowgen=rd('b702_rowgen_stepzero.txt'),
        branchj=jl('b702_branches.json'), branchbj=jl('b702_branches_before.json'), branchest=rd('b702_branches.txt'),
        branch_lists=dict((repo, gs(repo, 'branch', '--list', *bs)) for repo, bs in K.DELETE),
        kernel_branch_lists=gs(KI, 'branch', '--list', *[b for _r, b, _w in K.KERNEL_BRANCHES_RAISED]),
        widen_tip=gs(KI, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.WIDEN_BRANCH),
        repairs=rd('b702_tool_repairs.txt'), rec_src=read(os.path.join(T, 'b702_record.py')),
        closing_src=read(os.path.join(T, 'b702_closing.py')),
        defshort=dict(b701=len(REC._defect_short('b701')), closing=len(REC.closing_defects('b701')), refuses=refuses),
        defshort_b702=REC._defect_short('b702'),
        corrj=jl('b702_corrigendum.json'), corrt=rd('b702_corrigendum.txt'), corrigenda=rd('b675_corrigenda.txt'),
        corrigenda_tri=tri(ROOT, 'data/b675_corrigenda.txt', PRE['relay']),
        guard=rd('b702_guard_dry.txt'), guardj=jl('b702_guard_dry.json'),
        tiej=jl('b702_tie.json'), tiet=rd('b702_tie.txt'), cutj=jl('b702_cut.json'), cutt=rd('b702_cut.txt'), quotej=jl('b702_quote.json'), quotet=rd('b702_quote.txt'),
        facesj=jl('b702_faces.json'), facest=rd('b702_faces.txt'), faces_diff=rd('b702_faces_diff.txt'), nodes=rd('b702_nodes_zeta.txt'),
        readmej=jl('b702_readme.json'), readmet=rd('b702_readme.txt'), readme_cur=rd('b702_readme_currency.txt'), readme_diff=rd('b702_readme_diff.txt'),
        partnersj=jl('b702_partners.json'), partnerst=rd('b702_partners.txt'), partners_line=jl('b702_partners_line.json'),
        orders_line=jl('b702_orders_line.json'), faces_order=jl('b702_faces_order_line.json'), spec_txt=rd('b702_circuit_spec.txt'),
        runner=runner, rbanks=dict(('%s_%s' % (r.get('kernel'), r.get('label')), rd('b701_runner_%s_%s.txt' % (r.get('kernel'), r.get('label'))))
                                   for r in runner.get('rows') or []),
        merges=merges, ef_main=gs(KI, 'rev-parse', 'main'),
        ef_log=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
                gs(KI, 'log', '--reverse', '--first-parent', '--format=%H %ct %s', K701.EF_MAIN_BEFORE + '..main').split(NL) if l.strip()],
        ef_sorry=_ef_sorry_code(), ef_remote={},
        rf_diff=rd('b702_readfirst_diff.txt'), rf_hand_now=blob(ROOT, 'HEAD:data/b702_readfirst.txt'),
        rf_hand_z=blob(ROOT, '%s:data/b702_readfirst.txt' % K.STEPZERO_BANKS) if K.STEPZERO_BANKS else None,
        asec=jl('b702_arm_seconds.json'), asect=rd('b702_arm_seconds.txt'),
        shared=dict((p, (cr0(blob(ROOT, '%s:%s' % (PRE['relay'], p))), cr0(raw(os.path.join(ROOT, *p.split('/')))), cr0(blob(ROOT, 'HEAD:' + p))))
                    for p in K.SHARED_APPENDED),
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), c2=_ct(ROOT, K.C2_RELAY), c2pp=_ct(PP, K.C2_PP), c3=_ct(ROOT, K.C3_RELAY), c3pp=_ct(PP, K.C3_PP),
               c4=_ct(ROOT, K.C4_RELAY), stepzero=_ct(ROOT, K.STEPZERO_BANKS), readme_cur=_ct(ROOT, K.README_BANK), spec=_ct(ROOT, K.SPEC_BANK),
               tie=_added_ct('data/b702_tie.txt'), cut=_added_ct('data/b702_cut.txt'), quote=_added_ct('data/b702_quote.txt'), cutpp=_ct(PP, K.CUT_COMMIT)),
        files=dict(stepzero=files_of(ROOT, K.STEPZERO_BANKS) if K.STEPZERO_BANKS else [], c1=files_of(ROOT, K.C1_RELAY) if K.C1_RELAY else [],
                   readme_cur=files_of(ROOT, K.README_BANK) if K.README_BANK else [], spec=files_of(ROOT, K.SPEC_BANK) if K.SPEC_BANK else [],
                   cutpp=files_of(PP, K.CUT_COMMIT) if K.CUT_COMMIT else []),
        standing=STANDING, wf=wf_state(),
        export_present=os.path.exists(os.path.join(ROOT, *EXPORT.split('/'))), export_log=gs(ROOT, 'log', '--all', '--format=%h', '--', EXPORT),
        export_index=gs(ROOT, 'ls-files', '--', EXPORT), export_status=gs(ROOT, 'status', '--porcelain', '--', EXPORT),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b702_act_root.json'), arj0=jl('b701_act_root.json'), art=rd('b702_act_root.txt'), rootsf=rd('act_roots.txt'),
        rootbanks=jl('b702_root_banks.json'),
        pushout=(files_of(ROOT, K.STEPZERO) if K.STEPZERO else [], bool(K.STEPZERO) and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, *f.split('/')))), cr0(blob(ROOT, 'HEAD:tools/' + f)))
              for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        readme_tri=tri(PP, 'README.md', PRE['pp']), faces_tri=tri(PP, K.FACES_PAGE, PRE['pp']), cut_tri=tri(PP, K.CUT_DOC, PRE['pp']) if K.CUT_DOC else (None, None, None),
        pp_renames=gs(PP, 'diff', '--name-status', '-M', PRE['pp'], 'HEAD'),
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b702_kernels_face.json').get('kernels') or {}), kerns_read=list(dict.fromkeys(REC._kerns())),
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mustfail=not os.path.exists(os.path.join(D, 'b702_mustnotexist.txt')),
        fj=jl('b702_findings.json'), tj=jl('b702_trail.json'), sc=jl('b702_scores.json'), desk=rd('b702_desk_notes.txt'), tfj=jl('b702_table_final.json'),
        lsr=None,
        rlog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(ROOT, 'log', '--reverse', '--format=%h %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        plog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(PP, 'log', '--reverse', '--format=%h %ct %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()],
    )
    if 'efremote' in need:
        refs = {}
        for l in git(KI, 'ls-remote', 'origin')[1].split(NL):
            if '\t' in l:
                sha, ref = l.split('\t', 1)
                refs[ref.strip()] = sha.strip()
        S['ef_remote'] = refs
    S['root_at_commit'] = _root_named_at_commit(S['arj'])
    # ### the author's (C), G-POSTROOT-WRITES-NONE: each per-part seconds bank's last commit time, and the root's recorded commit's time
    S['secs_ct'] = dict((p, _ct(ROOT, gs(ROOT, 'log', '-1', '--format=%H', '--', 'data/b702_arm_seconds_%s.json' % p))) for p in K.PARTS)
    S['root_ct'] = _ct(ROOT, (S['arj'].get('commit') or {}).get('relay') or '')
    S['phase_secs'] = {'the banks and the state': time.time() - t0}
    S['pp_allowed'] = sorted(K.PP_WRITTEN)
    t1 = time.time()
    S['live'] = live_arms() if 'live' in need else dict(names=[], nsm=[], ac=[], ac_counts={}, mh=[], mh_per={}, secs=(0, 0, 0))
    S['phase_secs']['the three arms at HEAD' + ('' if 'live' in need else ' (not in this part)')] = time.time() - t1
    t1 = time.time()
    S['ra'] = ra_sources(S['lock_epoch']) if 'rules' in need else {}
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
            if f.startswith(('b702_', 'audit_b702_')) and os.path.isfile(os.path.join(D, f)) and not f.endswith(('.gz', '.png', '.jsonl')):
                pub.append(read(os.path.join(D, f)))
        pub += [read(f) for f in tools]
        for p in (K.CUT_DOC, 'README.md', K.FACES_PAGE):
            if p:
                pub.append(appended(cr0(blob(PP, PRE['pp'] + ':' + p)) or b'', cr0(raw(os.path.join(PP, *p.split('/')))) or b''))
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
    m = re.search(r'^### b702 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
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
    import b702_record as REC
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


# ================================================================== (R312) STEP ZERO: THE CITATION CHECK, THE BRANCHES, THE TWO BANKS
READFIRST_NEEDLES = ('relay data/b701_closing.txt | :1 ; :244-:261', 'relay data/b701_defects.txt | :6-:50', 'relay data/b701_tool_repairs.txt | :6',
                     'relay data/b701_obstruction.txt | :11-:18', 'relay data/b701_faces_rows.txt | :10 ; :14', 'relay data/b701_grade.txt | :41',
                     'relay data/b701_correspondence_restatement.txt | :57', 'relay data/b701_clause_dominance.txt | :58',
                     'PLACE-papers OPEN_TRAILS.md | :15406 ; :15408 ; :15410', 'PLACE-papers OPEN_TRAILS.md | :14386 ; :14450 ; :15296 ; :15332',
                     'relay data/b700_reading4.txt | :66-:76 ; :90-:100', 'relay data/b695_circuit_spec.txt | :7-:64', 'PLACE-papers README.md | :15-:18',
                     'PLACE-papers REGISTRY.md | :83 ; :87', 'relay data/b690_nodes_zeta.txt | :126', 'relay tools/b700_checks.py | :1669-:1676',
                     'relay tools/b701_checks.py | :1782-:1786', 'relay data/b670_licensed_table.txt | :4-:58', 'relay data/b700_r4_licensed.txt | :7-:11 ; :52-:84',
                     'relay data/b648_recut_order.txt | :4-:36', 'relay data/b652_ferry.txt | :19', 'relay data/b674_rules.txt | :8-:11',
                     'relay data/b690_rules.txt | :9', 'relay data/b698_rules.txt | :6', 'relay data/b646_table_Seven_Mechanism_Classes.txt | :3 ; :9-:329 ; :331',
                     'relay data/b672_one_copy.txt | :3', 'relay data/b675_corrigenda.txt | :113', 'relay data/b701_closing_push_out.txt')
NAMED_LOCAL = sorted(b for _r, bs in K.DELETE for b in bs)
NAMED_ALL = sorted(NAMED_LOCAL + [b for _r, b in K.DELETE_REMOTE])
NAMED_KERNEL = sorted(b for _r, b, _w in K.KERNEL_BRANCHES_RAISED)
MISSES_RAISED = ('the (R245)(5)(ii) sentence at :188 and the (R284)(3) sentence at :184', 'REGISTRY`s README row')
MISS_HEADERS = ('README lines', 'README row')     # ### filled at the seal with the prompt's header words (stage two)


def readfirst_ok(S):
    z = unwrap(S['readfirst'])
    return bool(z) and all(x in z for x in READFIRST_NEEDLES)


def branches_ok(S):
    z = S['branchest']
    left = dict((r, sorted(x.strip() for x in v.split(NL) if x.strip())) for r, v in S['branch_lists'].items())
    return all(v == [] for v in left.values()) and len(left) == 2 and all(b in z for b in NAMED_LOCAL) and S['kernel_branch_lists'].strip() == '' \
        and all(b in z for b in NAMED_KERNEL) and 'BRANCHES NAMED 8 ; DELETED 8 ; KEPT 0 ; EVERY TIP MERGED True ; widening-b701 STANDS' in unwrap(z)


def _first_delete_ts(S):
    import b702_record as REC
    ts = [r['ts'] for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and REC.delete_shape(r['cmd'])[0]]
    return iso_epoch(min(ts)[:19] + 'Z') if ts else None


def _kernel_prompt_ts(S):
    """the kernel-branches prompt's call time (data/b702_author_answers.json, the call whose question names bridge-b701)."""
    for c in S['answersj'].get('calls') or []:
        if 'bridge-b701' in (c.get('question') or '') or 'Kernel branches' in (c.get('header') or '') or 'bridge-b701' in json.dumps(c):
            return iso_epoch((c.get('ts') or '')[:19] + 'Z')
    return None


def branches_banked_ok(S):
    import b702_record as REC
    rows = S['branchj'].get('rows') or []
    try:
        fates = [REC.read_branch_row(r) for r in rows]
    except Exception:
        return False
    bt = iso_epoch((S['branchbj'].get('at') or '')[:19] + 'Z')
    fd = _first_delete_ts(S)
    pt = _kernel_prompt_ts(S)
    return len(rows) == 8 and all(f == 'DELETED' for _b, f in fates) and all(r['merged'] for r in rows) \
        and sorted(r['branch'] for r in rows if r['repo'] != KI) == NAMED_ALL and sorted(set(r['branch'] for r in rows if r['repo'] == KI)) == NAMED_KERNEL \
        and bool(bt) and bool(fd) and bt < fd and bool(pt) and pt < fd and len(S['branchbj'].get('rows') or []) == 5 \
        and S['widen_tip'] == K.WIDEN_TIP and S['branchj'].get('widening') == K.WIDEN_TIP


def deletes_one_ok(S):
    import b702_record as REC
    sh_ = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell')]
    shapes = [(REC.delete_shape(r['cmd']), REC.chained_after(r['cmd'])) for r in sh_]
    shapes = [(s, c) for s, c in shapes if s[0]]
    return bool(shapes) and all(len(d) == 1 and not gl and not vs and not c for (d, gl, vs), c in shapes) \
        and sorted(x for (d, _g, _v), _c in shapes for x in d) == sorted(NAMED_ALL + NAMED_KERNEL + ['bridge-b701']) \
        and 'BRANCH DELETES OF ONE BRANCH, NO GLOB, NO VARIABLE AND NOTHING CHAINED AFTER 8 OF 8' in S['cmdt']


def dry_step_ok(S):
    g = S['gate']
    return '--- THE DRY-RUN STEP ((R267)(2))' in g and 'ENTRY : table cells NONE ; screens QUIET' in g and 'TRAIL : table cells NONE ; screens QUIET' in g \
        and 'THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK True' in g and 'THE TRAIL`S RESOLVED LINE EQUAL TO THE DEFECTS BANK True' in g \
        and '### ### **THE DRY-RUN STEP : CLEAN**' in g and '### ### **GATE VERDICT : CLEAR**' in g


def closing_dry_ok(S):
    g = S['gate']
    return '--- THE CLOSING DRY-RUN STEP (b675 rules row 1)' in g and '### ### **THE CLOSING DRY-RUN STEP : CLEAN**' in g \
        and 'b702 closed:' in g and 'the misses as the bank lists them' in g and '### THE CORRIGENDUM' in g and '### THE GUARD' in g \
        and '### THE RE-CUT' in g and '### THE FACES ROW' in g and '### THE README' in g and '### THE PARTNER COPIES' in g and '### THE ORDERS' in g \
        and '### THE KERNELS' in g and '(g) The defects (a)' in g and '### NO VERDICT LINE' not in g


def citation_ok(S):
    """the citation check's bank: every cite checked, OK and misses summing; the two misses the ruling's (5), each raised as a prompt before
    Component 3 (the answers bank's headers); the bank written before the step-zero banks' commit and that commit before Component 1's."""
    c = S['citation']
    m = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', c)
    raised = all(('(%s)' % h) in S['answers'] for h in MISS_HEADERS)
    return bool(m) and int(m.group(1)) == int(m.group(2)) + int(m.group(3)) > 0 and 'A GATE STEP AT STEP ZERO' in c \
        and int(m.group(3)) == len(S['cit_misses']) == 2 and all(any(w in x for x in S['cit_misses']) for w in MISSES_RAISED) and raised \
        and bool(S['cit_at']) and bool(S['t'].get('stepzero')) and S['cit_at'] < S['t']['stepzero'] \
        and bool(S['t'].get('c1')) and S['t']['stepzero'] <= S['t']['c1']


def rowgen_ok(S):
    return '### ### **CONSTELLATION EXIT 0 ; ROWGEN DIFF EXIT 0 ; TABLES 19.**' in S['rowgen']


def weight_ok(S):
    return landed(S, 0, ['b701 AT ITS WEIGHT', '613847d6'])


def answers_checked_ok(S):
    """the citation bank's mid-act prints read at HEAD, at or above the sealed floor, each before the step its answer governs: the kernel
    branches answer before the first delete; the faces, README and partner-copies answers before their writes (the banks' times)."""
    c = S['citation']
    stamps = re.findall(r'### \(R278\)\(4\) THE MID-ACT CHECK \((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\): the answer carrying \'([^\']+)\'', c)
    acts = dict()
    for t_, n in stamps:
        acts.setdefault(n, []).append(iso_epoch(t_))
    gov = [('Kernel branches', _first_delete_ts(S))]
    for needle, bank in (('Faces', 'facesj'), ('README', 'readmej'), ('Partner', 'partnersj')):
        at = iso_epoch((S[bank].get('at') or ''))
        if at:
            gov.append((needle, at))
    return len(stamps) >= FLOORS['checks'] and all(any(k in n for n in acts) and w and max(v for n, vs in acts.items() if k in n for v in vs) < w
                                                   for k, w in gov)


# ================================================================== (R312)(1)-(7): THE CORRIGENDUM, THE GUARD, THE RE-CUT, THE FACES, THE README, THE PARTNERS, THE ORDERS
def _fn_src(src, name):
    if ('\ndef %s(' % name) not in src:
        return ''
    i = src.index('\ndef %s(' % name) + 1
    m = re.search(r'\n(?=\S)', src[i + 1:])
    return src[i:i + 1 + m.start() + 1] if m else src[i:]


def scorer_banks_ok(S):
    n = ''.join(strip_prose(_fn_src(S['rec_src'], f)) for f in ('_n1', '_n2', '_n3', '_n4'))
    sc = strip_prose(_fn_src(S['rec_src'], 'scores'))
    ft = strip_prose(_fn_src(S['rec_src'], '_finding_text'))
    return bool(n) and '_commands.json' in n and '_tie.json' in n and '_cut.json' in n and '_guard_dry.json' in n \
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
    import b702_record as REC
    want = conv(REC.scores_line(S['sc'])) if S['sc'] else None
    blk = _entry_block(S)
    got = [l for l in blk.split(NL) if l.startswith('**The scores.**')]
    return bool(want) and bool(S['sc']) and got == [want]


def entry_title_ok(S):
    e = S['fj'].get('entry_line')
    t = S['REC']._title()
    return bool(e) and fline(S, e) == conv(t) and t.startswith('## ') and ' re-cut: ' in t and 'rows outside LICENSED/CITED to' in t \
        and 'the faces page’s lv-conservation row' in t and 'the README’s currency lines and ceiling append' in t \
        and 'W-ORD-PAPER-PARTNER-COPIES in place of ONE-COPY, resolution' in t and 'b701’s undeclared failures by corrigendum' in t


def trail_tail(S):
    t = S['ot']
    i = t.find(conv(S['REC'].TRAIL_HEAD()))
    return t[i:] if i >= 0 else ''


def trail_defects_ok(S):
    m = re.search(r'^\*\*Defects\*\* \(relay data/b702_defects\.txt\): (.*)\.$', trail_tail(S), re.M)
    return 'THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK True' in S['gate'] and bool(m) \
        and m.group(1) == conv('; '.join(S['defshort_b702']) or 'none')


def _owners(rows):
    nav = sum(1 for r in rows if "THE NAVIGATOR'S" in r)
    return nav, len(rows) - nav


def trail_resolved_ok(S):
    """the trail's Resolved line's defect counts (its last item) equal to the bank's owners (b701's defect (k), answered here)."""
    m = re.search(r'^\*\*Resolved by the seat, for the author’s strike:\*\* .*\((\d+)\) the (\w+) navigator (?:miss|misses)(?: \(\([a-z]\)(?:, \([a-z]\))*\))? and the seat’s (\w+) defects? as lettered\.$',
                  trail_tail(S), re.M)
    nav, seat = _owners(S['defshort_b702'])
    return 'THE TRAIL`S RESOLVED LINE EQUAL TO THE DEFECTS BANK True' in S['gate'] and bool(m) and S['REC'].num_word(nav) == m.group(2) and S['REC'].num_word(seat) == m.group(3)


def corrigendum_ok(S):
    """(R312)(2): the generated entry landed (its line in the bank, the title at that line through conv), lettering (h)-(k), the two failures
    named, the counts 2 and 5; the corrigenda bank appended at rows (17)-(21) and nothing before them changed; the sealed face, trail and
    root-named banks unedited (G-INSTRUMENTS-UNEDITED and G-PRIORBANK-UNCHANGED read those)."""
    j = S['corrj']
    e = j.get('entry_line')
    pre, now, head = S['corrigenda_tri']
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and j.get('lettered') == ['h', 'i', 'j', 'k'] \
        and j.get('failures') == ['G-READ-RULE', 'G-ACTROOT-LAST'] and (j.get('owners') or {}) == dict(navigator=2, seat=5) \
        and all(('  (%d) ' % i) in S['corrigenda'] for i in range(17, 22)) and '  (22) ' not in S['corrigenda'] \
        and pre is not None and (now or b'').startswith(pre) and (head or b'').startswith(pre) and 'FINDINGS.md :%d' % e in S['corrt']


GUARD_WRITE = "sp = os.path.join(D, 'b702_arm_seconds_%s.json' % PART)"   # ### the write's own line, stripped; matched whole, not by a needle


def guard_ok(S):
    """(R312)(2), N4: the suite's writer block guarded (`if PRERUN:` the line above the per-part seconds write, read from this tool's own
    text), the guard's dry run printing no write on the pre-push and post-push paths and the write on the pre-run path, banked."""
    s = S['suite'].split(NL)
    i = next((k for k, l in enumerate(s) if l.strip() == GUARD_WRITE), None)
    j = S['guardj']
    return i is not None and s[i - 1].strip() == 'if PRERUN:' and 'POST-ROOT PATH WRITES NONE' in S['guard'] \
        and (j.get('writes') or {}).get('pre-push') == [] and (j.get('writes') or {}).get('post-push') == [] \
        and (j.get('writes') or {}).get('prerun') == ['data/b702_arm_seconds_<part>.json'] and 'data/b702_tool_repairs.txt' in S['guard']


def postroot_writes_none(S):
    """the author's (C), G-POSTROOT-WRITES-NONE: the guard's dry run prints no write on the post-root path (the pre-push and post-push modes),
    and no per-part seconds bank's commit time follows the root's recorded commit's time -- every part's bank committed, each at or before it."""
    j = S['guardj']
    w = j.get('writes') or {}
    return 'POST-ROOT PATH WRITES NONE' in S['guard'] and w.get('pre-push') == [] and w.get('post-push') == [] and bool(S['root_ct']) \
        and sorted(S['secs_ct']) == sorted(K.PARTS) and all(v is not None and v <= S['root_ct'] for v in S['secs_ct'].values())


KIND = re.compile(r"\(([a-z])\) THE (NAVIGATOR|SEAT)[’']S")


def trail_lines_equal_defects(S):
    """the author's (C), G-TRAIL-LINES-EQUAL-DEFECTS: the trail's Defects line and its Resolved line, each counted by kind (the navigator's,
    the seat's), equal data/b702_defects.txt counted by kind -- the bank read at HEAD by its own lettered rows, not through the trail."""
    tail = trail_tail(S)
    dm = re.search(r'^\*\*Defects\*\* \(relay data/b702_defects\.txt\): (.*)\.$', tail, re.M)
    rm = re.search(r'^\*\*Resolved by the seat, for the author’s strike:\*\* .*\(\d+\) the (\w+) navigator (?:miss|misses)(?: \(\([a-z]\)(?:, \([a-z]\))*\))? '
                   r'and the seat’s (\w+) defects? as lettered\.$', tail, re.M)
    bank = re.findall(r"^    \(([a-z])\) THE (NAVIGATOR|SEAT)'S", S['defects'], re.M)
    want = (sum(1 for _x, o in bank if o == 'NAVIGATOR'), sum(1 for _x, o in bank if o == 'SEAT'))
    if not dm or not rm or not bank:
        return False
    got_d = KIND.findall(dm.group(1))
    have_d = (sum(1 for _x, o in got_d if o == 'NAVIGATOR'), sum(1 for _x, o in got_d if o == 'SEAT'))
    have_r = (rm.group(1), rm.group(2))
    return have_d == want and have_r == (S['REC'].num_word(want[0]), S['REC'].num_word(want[1]))


def tie_ok(S):
    """(R312)(3), N2: the tie bank prints b674's rule and b652's order verbatim and every row before the document is named; the kernels all at
    0 so the companions are read; one document at the top count or b674's rule applied step by step; the bank before the cut bank."""
    j, t = S['tiej'], S['tiet']
    return bool(j) and j.get('named') == K.CUT_NAME and '(2) THE TIE-BREAK BEYOND THE COUNT' in t and 'the next kernel by descending count under the same rules, then the companions' in t \
        and t.index('THE TIE-BREAK BEYOND THE COUNT') < t.index('THE NEXT DOCUMENT BY b652`S ORDER') and (j.get('kernels_top') or 0) == 0 \
        and all(r.get('now') == 0 for r in (j.get('rows') or []) if r.get('kind') == 'kernel') \
        and bool(S['t'].get('tie')) and bool(S['t'].get('cut')) and S['t']['tie'] <= S['t']['cut'] and iso_epoch(j.get('at') or '') < iso_epoch(S['cutj'].get('at') or '')


def cut_ok(S):
    """(R312)(3), N3: the distance after the cut at or below the distance before by the b670 method; every applied row's ACTION met in the
    document at HEAD and not at the base; the cut one commit on PLACE-papers main carrying the document alone; the paper not moved or renamed."""
    j = S['cutj']
    pre, now, head = S['cut_tri']
    return bool(j) and j.get('document') == K.CUT_DOC and isinstance(j.get('before'), int) and isinstance(j.get('after'), int) and j['after'] <= j['before'] \
        and j.get('applied') == j['before'] - j['after'] and all(r.get('met_at_head') and not r.get('met_at_base') for r in (j.get('rows') or []) if r.get('applied')) \
        and S['files']['cutpp'] == [K.CUT_DOC] and pre is not None and now == head and now != pre \
        and ('%s RE-CUT: THE DISTANCE BEFORE %d, AFTER %d' % (K.CUT_NAME, j['before'], j['after'])) in S['cutt']


def quote_ok(S):
    """data/b690_rules.txt row (2): every line the cut removes or changes searched by a distinctive substring with git grep across the
    papers' tracked tree before the cut's commit, in two shapes, its hit count printed, every quoting line entered as a residue in the cut bank."""
    j = S['quotej']
    q = S['quotet']
    m = re.search(r'REMOVED OR CHANGED LINES (\d+) ; NEEDLES SEARCHED (\d+) IN TWO SHAPES ; QUOTING LINES (\d+)', q)
    return bool(j) and bool(m) and m.group(1) == m.group(2) and int(m.group(1)) > 0 and len(j.get('rows') or []) == int(m.group(1)) \
        and bool(S['t'].get('quote')) and bool(S['t'].get('cutpp')) and iso_epoch(j.get('at') or '') < S['t']['cutpp'] \
        and all(('%s :%d' % tuple(x)) in S['cutt'] for x in (S['cutj'].get('residues') or [])) and len(S['cutj'].get('residues') or []) == int(m.group(3))


def faces_ok(S):
    """(R312)(4): the successor printed verbatim beside the page's line before the prompt; on 'regenerate' the control re-emitting the
    current page byte for byte, the page regenerated by tools/chain_page.py from data/b702_nodes_zeta.txt, the diff two lines (the list's
    name, the row), the header tag unchanged; on 'hold' the page unedited."""
    j = S['facesj']
    pre, now, head = S['faces_tri']
    if not j or j.get('outcome') not in ('regenerated', 'held'):
        return False
    if j['outcome'] == 'held':
        return pre is not None and pre == now == head and 'HELD' in S['facest']
    # ### the author's word on the raise (2026-10-21T21:12Z): three lines -- :3 replaced, :191 inserted (the cut a1d5d59's Placement row), the
    # ### row replaced: five diff lines, two removed and three added
    d = [l for l in S['faces_diff'].split(NL) if l.startswith(('-', '+')) and not l.startswith(('---', '+++'))]
    return j.get('control') is True and pre is not None and now == head and now != pre and len(d) == 5 \
        and sum(1 for l in d if l.startswith('+')) == 3 and K.FACES_HEADER_TAG in (now or b'').decode('utf-8', 'replace') \
        and j.get('changed') == [3, K.FACES_ROW_LINE] and '| keystone naming a node | `day1/Seven_Mechanism_Classes.md` |' in (now or b'').decode('utf-8', 'replace')


def faces_order_ok(S):
    j = S['faces_order']
    ln = (j.get('lines') or [{}])[0].get('line')
    return bool(ln) and 'W-ORD-FACES-PROBE-CURRENT' in oline(S, ln) and 'the re-cut act b704' in oline(S, ln) and 'one dispatch' in oline(S, ln)


def readme_ok(S):
    """(R312)(5): the currency rows banked and committed alone before the prompt, the append drafted in the README's own form; on 'apply' the
    edits at the named lines by the Edit tool and the append beneath :131, the diff banked; on 'hold' the README unedited; REGISTRY carrying no
    README row, raised, nothing written to it."""
    j = S['readmej']
    pre, now, head = S['readme_tri']
    if not j or j.get('outcome') not in ('applied', 'currency rows alone', 'held'):
        return False
    cur_ok = S['files']['readme_cur'] == ['data/b702_readme_currency.txt'] and 'THE CEILING APPEND, DRAFTED' in S['readme_cur'] and 'THE ABOUT FIELD' in S['readme_cur'] \
        and bool(S['t'].get('readme_cur')) and iso_epoch(j.get('prompt_at') or '') and S['t']['readme_cur'] < iso_epoch(j.get('prompt_at'))
    if j['outcome'] == 'held':
        return cur_ok and pre is not None and pre == now == head
    rg = S['currents'].get('REGISTRY.md')
    return cur_ok and pre is not None and now == head and now != pre and bool(S['readme_diff']) and rg[0] is not None and rg[0] == rg[1] == rg[2] \
        and ((j['outcome'] == 'applied') == ('(R312)(5)' in (now or b'').decode('utf-8', 'replace')))


def partners_ok(S):
    """(R312)(6): W-ORD-PAPER-PARTNER-COPIES landed with the object, the condition and the unit of its figures and reading 4's counts by cause;
    the old ONE-COPY line annotated 'superseded'; the three resolutions raised before the landing; the disposition entered with a trigger;
    no paper moved or renamed (N5)."""
    j, lines = S['partnersj'], S['partners_line']
    ls = lines.get('lines') or []
    if not j or len(ls) != 2:
        return False
    new, old = oline(S, ls[0].get('line')), oline(S, ls[1].get('line'))
    return 'W-ORD-PAPER-PARTNER-COPIES' in new and 'superseded by W-ORD-PAPER-PARTNER-COPIES' in old and 'a regenerated cell 123, a hand edit 8' in new \
        and j.get('resolution') in ('(i)', '(ii)', '(iii)', 'held') and ('Trigger:' in new) and 'lines differing between the two copies of one paper' in new \
        and not [l for l in S['pp_renames'].split(NL) if l.startswith(('R', 'D'))] and iso_epoch(j.get('prompt_at') or '') < iso_epoch(lines.get('at') or '')


def spec_row_ok(S):
    t = S['spec_txt']
    return S['files']['spec'] == ['data/b702_circuit_spec.txt'] and 'BINDER-PROVENANCE' in t and 'ROWS 12 ; THE ELEVEN OF b695 UNCHANGED' in unwrap(t) \
        and rd('b695_circuit_spec.txt').split(NL)[6:64] == t.split(NL)[6:64]


def orders_ok(S):
    j = S['orders_line']
    ln = (j.get('lines') or [{}])[0].get('line')
    return bool(ln) and 'W-ORD-STANDING-CLAUSES-BANK' in oline(S, ln) and 'the reading act b710' in oline(S, ln) and 'priced' in oline(S, ln).lower()


def widening_stands(S):
    r = S['ef_remote']
    return S['widen_tip'] == K.WIDEN_TIP and r.get('refs/heads/' + K.WIDEN_BRANCH) == K.WIDEN_TIP and r.get('refs/tags/v0.35^{}') == K.EF_V035 \
        and r.get('refs/heads/main') == S['ef_main'] == K.EF_V035 and 'refs/heads/bridge-b701' not in r


def kernel_writes_ok(S):
    """N5: no kernel written by this act -- SIDE-explicit-formula's main at v0.35 as b701 left it, nothing of this act on it."""
    w = S['wf'][K.KERNEL]
    return S['ef_main'] == K.EF_V035 and w['this_act_writes'] == [] and bool(S['merges'])


def readfirst_diff_ok(S):
    return 'THE HAND LIST 43 PATHS ; THE TEXT CITES 29 ; BOTH 22 ; LINES DIFFERING 28' in S['rf_diff'] and 'No bank is rewritten by this reading.' in S['rf_diff'] \
        and 'data/b702_readfirst_diff.txt' in S['files']['stepzero'] and S['rf_hand_now'] is not None and S['rf_hand_now'] == S['rf_hand_z']


REPAIRS_WANT = 2


def repairs_ok(S):
    return ('REPAIRS %d ;' % REPAIRS_WANT) in S['repairs'] and 'NO FROZEN BANK EDITED' in S['repairs'] and '  (1) tools/b702_checks.py' in S['repairs']


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
    b = S['reads_bank']
    off = re.findall(r'^  ([\w:]+) \| \S+ \| \d+ \| ### AN OFFENCE \|', b, re.M)
    m = re.search(r'WHOLE OF A FILE OF 200 LINES OR MORE (\d+)', b)
    return bool(m) and int(m.group(1)) == len(off) and all(('transcript line %s' % n) in S['defects'] for n in off)


# ================================================================== THE RUNNER (the last merged run, b701's at SIDE-explicit-formula)
IDENT_WF = ('secrets.', 'psinary', 'seale', 'york', 'hotmail', 'orcid', '0009-0008')


def wf_ok(S):
    for k, v in S['wf'].items():
        t = v['text'].lower()
        if not v['text'] or v['text'] != v['before'] or not v['wrote_before_act'] or any(w in t for w in IDENT_WF):
            return False
        if 'workflow_dispatch' not in t or 'hold_mb: "2560"' not in t or 'print_targets.txt' not in t:
            return False
        if not v['lakefile'] or 'lake env lean out/axioms.lean' not in t or (('lake exe cache get' in t) != v['mathlib']):
            return False
        if len(v['targets']) != v['printed'] or v['act_writes'] != v['want']:
            return False
    return sorted(S['wf']) == [K.KERNEL]


def runner_ok(S):
    import b702_record as REC
    rows = [r for r in (S['runner'].get('rows') or []) if r.get('ref') in set(m['tip'] for m in S['merges'])]
    try:
        for r in rows:
            REC.read_runner_row(r)
    except Exception:
        return False
    return len(rows) == len(S['merges']) > 0 and all(r['kernel'] == K.KERNEL and r['conclusion'] == 'success' and r['artifact_sha256'] and r['mem_low'] is not None
                                                     and r['mem_low'] >= K.HOLD and not r['stopped'] and r['gate'] == 'DERIVES' for r in rows)


def gate_ok(S):
    merged_labels = [r.get('label') for r in (S['runner'].get('rows') or []) if r.get('ref') in set(m['tip'] for m in S['merges'])]
    bs = dict((k, v) for k, v in S['rbanks'].items() if k.split('_')[-1] in merged_labels)
    return len(bs) == len(S['merges']) > 0 and all('GATE DERIVES' in t and 'BUILD EXIT 0 ; ERROR LINES 0' in t and 'SORRYAX 0' in t
                                                   and re.search(r'^### the artifact: .* ; AGREE$', t, re.M) for t in bs.values())


def merges_ok(S):
    if not S['merges']:
        return False
    prior = 'v0.34.1'
    for m in S['merges']:
        if not (len(m['parents']) == 2 and m['parents'][0] == m['prev_main'] and m['parents'][1] == m['tip'] and m['trees'][0] == m['trees'][1]
                and prior in m['tagmsg'] and m['merge'] in [h for h, _s, _t in S['ef_log']]):
            return False
        prior = m['tag']
    return sorted(h for h, _s, _t in S['ef_log']) == sorted(m['merge'] for m in S['merges']) and S['ef_main'] == S['merges'][-1]['merge'] \
        and not S['ef_sorry'].strip()


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


POST_SEAL = ('b702 seal', 'b702 pre-root', 'b702 root', 'b702 record', 'b702 --', 'b702 closing', 'b702 entry')


def _component_commit(s):
    return s.startswith('b702') and not s.startswith(POST_SEAL)


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
    return bool(j) and len(rows) == 79 and rows[78][:3] == ['b702', j.get('root'), j0.get('root')] \
        and AR.root_of(items, j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) \
        and not [it for it in items if 'b628_intake_crank' in it or 'b647_navigator_memory' in it or 'b703_' in it or 'mirror' in it
                 or 'chain_' in it or 'units' in it or it.split()[0].endswith(('.gz', '.png', '.jsonl'))] \
        and any(it.startswith('data/b702_tie.txt ') for it in items) and any(it.startswith('data/b702_cut.txt ') for it in items) \
        and any(it.startswith('data/b702_corrigendum.txt ') for it in items) and any(it.startswith('data/b702_guard_dry.txt ') for it in items) \
        and (j.get('commit') or {}).get('relay')


def root_banks_committed_ok(S):
    rb, rows = S['rootbanks'], S['root_at_commit']
    commit = (S['arj'].get('commit') or {}).get('relay') or ''
    return bool(rb) and rb.get('clean') is True and rb.get('pushed') is True and rb.get('head') == commit and bool(rows) \
        and all(c and e for _b, c, e in rows) and sorted(b for b, _c, _e in rows) == sorted(r['bank'] for r in rb.get('rows') or [])


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b702_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    ha = S['half_a'] or {}
    v = [tuple(x[:2]) for x in (ha.get('acts') or [])] + [tuple(x[:2]) for x in (S['ar_verify'] or [])]
    r = dict(ha.get('reads') or {}, **(S['ar_reads'] or {}))
    return ha.get('head') == gs(ROOT, 'rev-parse', 'HEAD') and [x[0] for x in v] == ['b%d' % i for i in range(624, 703)] \
        and all(x[1] == 'AGREE' for x in v) and (r.get('b702') or {}).get('crlf') == 0 and (r.get('b680') or {}).get('corrected') == 4 \
        and (ha.get('boundary') or {}).get('equal') is True and S['boundary'].get('equal') is True \
        and (ha.get('boundary') or {}).get('root') == S['boundary'].get('root')


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**The corrigendum**', '**The guard**', '**The re-cut**', '**The faces row**', '**The README**', '**The partner copies**',
                 '**The orders**', '**The citation check**', '**The scores.**', '**Read in mutual light**', 'strengthens', '**Carried to:**', '**Next.**', 'b703')


def finding_ok(S):
    e = S['fj'].get('entry_line')
    tail = _entry_block(S)
    return bool(e) and fline(S, e) == conv(S['fj'].get('title') or '\x00') and all(conv(x) in tail for x in ENTRY_NEEDLES)


def wl_ok(S):
    return bool(S['globs']) and bool(S['written']) and all(any(fnmatch.fnmatch(f, p) for p in S['globs']) for f in S['written'])


def scored(S, k):
    import b702_record as REC
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
        and '### THE CITATION CHECK' in t and '### THE RECORD LINES' in t and '### THE DRY RUN' in t and 'THE CORRIGENDUM' in t and 'THE GUARD' in t \
        and 'THE RE-CUT' in t and 'THE FACES ROW' in t and 'THE README' in t and 'THE PARTNER COPIES' in t and 'THE ORDERS' in t and '### THE KERNELS' in t \
        and '### THE MIRROR' in t and '### THE CARRY-TIME' in t


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
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R312) END' in S['ferry'] and S['ferry'].rstrip().endswith(K.TAIL),
     lambda S: put(S, 'ferry', S['ferry'].replace(K.TAIL, ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the step-zero bank: tail, lean, lake, python and claude named, the seat`s claude alone, none of the others; no task stopped, no orphan, nothing stopped by PID',
     lambda S: procs_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('python 0', 'python 1'))),
    ('G-STEPZERO-TESTS', 'the tests bank against the test files tracked before the act, test_elab_reader_b634.py withheld (no lean on this host), run against the list the page names',
     lambda S: tests_ok(S), lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: S['pushout'][0] == ['data/b701_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'relay`s, PLACE-papers` and the kernel`s branch lists by the ruling`s names and the author`s word, and the branches bank; widening-b701 standing',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{'D:/relay': 'push-b701'}))),
    ('G-READFIRST-CITED', 'the read-first bank: every item of the ferry`s list cited by path and line', lambda S: readfirst_ok(S),
     lambda S: put(S, 'readfirst', '')),
    ('G-ANSWERS-BANKED', 'the answers bank read at HEAD: its prompts and calls at or above the sealed floors, each with its options and result, any call after the lock named on the face',
     lambda S: answers_ok(S), lambda S: put(S, 'answers', re.sub(r'(?m)^(### b702 -- THE AUTHOR`S ANSWERS, )(\d+)', lambda m: m.group(1) + str(int(m.group(2)) + 1),
                                                                 S['answers']))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-EXPORT-UNTRACKED', 'the navigator`s export: present, untracked, in no commit', lambda S: S['export_present'] and S['export_log'] == ''
     and S['export_index'] == '' and S['export_status'].startswith('??'), lambda S: put(S, 'export_index', EXPORT)),
    ('G-EDIT-ROUTE', 'the record tool`s one reading (tools/edit_route.py`s arms and sed in any form) over this act`s whole capture and the previous act`s after its post-push suite, read live',
     lambda S: edit_route_ok(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -n 1p tools/b702_record.py")])),
    ('G-NO-LOCAL-LEAN', 'the act`s command capture, read live: no command runs lean or lake on this host (N1)', lambda S: no_local_lean(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd='lake env lean SIDEExplicitFormula/RegisterBridge.lean')])),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line, found by conv', lambda S: weight_ok(S), lambda S: _rl(S, 0, 1)),
    ('G-DRY-STEP-CLEAN', 'the gate`s record: the dry-run step run, the entry and the trail record quiet under their screens, the trail`s Defects and Resolved lines equal to the defects bank, CLEAN printed, the gate CLEAR',
     lambda S: dry_step_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE DRY-RUN STEP : CLEAN', 'THE DRY-RUN STEP : NOT CLEAN'))),
    ('G-CLOSING-DRY-STEP', 'the gate`s record: the closing run dry before the lock, its head line, citation line, the corrigendum, the guard, the re-cut, the faces row, the README, the partner copies, the orders and kernels sections and the defects row printed (b675 rules row 1)',
     lambda S: closing_dry_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE CLOSING DRY-RUN STEP : CLEAN', 'THE CLOSING DRY-RUN STEP : NOT CLEAN'))),
    ('G-CITATION-CHECKED', 'the citation check`s bank (the gate step at step zero): every cite checked, the two misses the ruling`s (5) and each raised as a prompt before Component 3, its bank written before the step-zero banks` commit and that commit before Component 1',
     lambda S: citation_ok(S), lambda S: put(S, 'cit_misses', S['cit_misses'] + ['planted'])),
    ('G-R312-ENTERED', 'the ferry and the trail', lambda S: 'RULING (R312) END' in S['ferry'] and S['ot'].count('**(R312) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R312) ratified', '**(R3120) ratified'))),
    ('G-ROWGEN-STEPZERO', 'the rowgen bank: constellation and the build-free diff over the 19 roster tables, both exit 0 (b670 rules row 3)',
     lambda S: rowgen_ok(S), lambda S: put(S, 'rowgen', S['rowgen'].replace('ROWGEN DIFF EXIT 0', 'ROWGEN DIFF EXIT 1'))),
    ('G-BRANCHES-BANKED', 'the branches banks: every tip banked before the first delete (b695 (a)), the kernel branches` prompt before it, then the eight rows through the record tool`s reader, each merged and deleted, widening-b701 at its tip',
     lambda S: branches_banked_ok(S), lambda S: _mut(S, 'branchbj', lambda d: d.update(at='2099-01-01T00:00:00Z'))),
    ('G-DELETES-ONE-BRANCH', 'the command capture by the record tool`s reader and the command bank: each branch delete naming one branch, no glob and no variable in any half, nothing chained after (data/b694_rules.txt row (1)), the ruling`s five and the word`s three exactly',
     lambda S: deletes_one_ok(S), lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="git branch -d push-b701; echo EXIT $?")])),
    ('G-ANSWERS-CHECKED', 'the citation bank`s mid-act prints read at HEAD, each before the step its answer governs (the first delete; the faces, README and partner-copies banks` times)',
     lambda S: answers_checked_ok(S), lambda S: put(S, 'cmds', [dict(r, ts='2026-10-21T00:00:00.000Z') if r['tool'] == 'Bash' and 'branch -d' in r['cmd'] else r for r in S['cmds']])),
    ('G-SCORER-READS-BANKS', 'tools/b702_record.py`s code, prose stripped: the N1-N4 scorers reading banks and commits and no ledger, the scores bank written once, the entry`s scores line from it',
     lambda S: scorer_banks_ok(S), lambda S: put(S, 'rec_src', S['rec_src'].replace("def _n2():", "def _n2():\n    _x = rd(FIND)"))),
    ('G-ENTRY-SCORES-EQUAL', 'FINDINGS at the findings bank`s line and the scores bank: the entry`s scores line equal to the line composed from the bank',
     lambda S: entry_scores_ok(S), lambda S: _mut(S, 'sc', lambda d: d.update(N1=['REFUTED', 'planted']))),
    ('G-ENTRY-TITLE-FORM', 'FINDINGS at the findings bank`s line and the record tool`s title from the banks: the ferry`s form, titled by its objects, adjusted to what the act did',
     lambda S: entry_title_ok(S), lambda S: put(S, 'find', S['find'].replace('rows outside LICENSED/CITED to', 'rows outside LICENSED/CITED at'))),
    ('G-CORRIGENDUM-ENTERED', 'the generated corrigendum entry at FINDINGS (its bank`s line, the title through conv), (h)-(k) lettered, the two failures named, the counts 2 and 5; the corrigenda bank appended at rows (17)-(21) and nothing before them changed ((R312)(2))',
     lambda S: corrigendum_ok(S), lambda S: _mut(S, 'corrj', lambda d: d.update(lettered=['h', 'i', 'j']))),
    ('G-GUARD-RESTORED', 'this suite`s own text at the per-part seconds write (the line above it `if PRERUN:`) and the guard`s dry-run bank: no write on the pre-push and post-push paths, the write on the pre-run path alone ((R312)(2), N4)',
     lambda S: guard_ok(S), lambda S: put(S, 'suite', S['suite'].replace("if PRERUN:\n        sp = os.path.join(D, 'b702_arm_seconds_%s.json' % PART)", "sp = os.path.join(D, 'b702_arm_seconds_%s.json' % PART)"))),
    ('G-POSTROOT-WRITES-NONE', 'the guard`s dry-run bank and the log: no write on the post-root path, and every per-part seconds bank`s last commit at or before the root`s recorded commit (the author`s (C))',
     lambda S: postroot_writes_none(S), lambda S: put(S, 'secs_ct', dict(S['secs_ct'], **{K.PARTS[0]: (S['root_ct'] or 0) + 1}))),
    ('G-TRAIL-LINES-EQUAL-DEFECTS', 'OPEN_TRAILS from the trail`s head and data/b702_defects.txt at HEAD: the Defects line and the Resolved line, each counted by kind, equal the bank counted by kind (the author`s (C))',
     lambda S: trail_lines_equal_defects(S), lambda S: put(S, 'defects', S['defects'] + NL + "    (z) THE NAVIGATOR'S: A PLANTED ROW.")),
    ('G-TIE-PRINTED','the tie bank and its json: b674`s rule and b652`s order verbatim before the document is named, every kernel at 0, the companions read, the named document the cut`s, the bank before the cut bank (N2)',
     lambda S: tie_ok(S), lambda S: _mut(S, 'tiej', lambda d: d.update(named='SIDE-x'))),
    ('G-CUT-DISTANCE', 'the cut bank and its json against the document at the base, at HEAD and in the working tree: the distance after at or below the distance before by the b670 method, each applied row met at HEAD and not at the base, the cut one commit carrying the document alone (N3)',
     lambda S: cut_ok(S), lambda S: _mut(S, 'cutj', lambda d: d.update(after=d.get('before', 0) + 1))),
    ('G-QUOTE-BEFORE-MERGE', 'the quotation search`s bank (data/b690_rules.txt row (2)): every removed or changed line searched by git grep across the papers` tree in two shapes before the cut`s commit, its hit count printed, every quoting line entered as a residue in the cut bank (N3)',
     lambda S: quote_ok(S), lambda S: _mut(S, 'quotej', lambda d: d.update(at='2099-01-01T00:00:00Z'))),
    ('G-FACES-ROW', 'the faces bank, the page before, now and at HEAD, the control and the diff: regenerated by the generator from data/b702_nodes_zeta.txt with the control byte for byte and two lines changed, the header tag unchanged -- or held with the page unedited ((R312)(4))',
     lambda S: faces_ok(S), lambda S: _mut(S, 'facesj', lambda d: d.update(outcome='x'))),
    ('G-FACES-PROBE-ORDER', 'OPEN_TRAILS at the faces order`s landing line: W-ORD-FACES-PROBE-CURRENT with its price and trigger ((R312)(4))',
     lambda S: faces_order_ok(S), lambda S: _mut(S, 'faces_order', lambda d: d.update(lines=[dict(line=1)]))),
    ('G-README-ROWS', 'the README currency bank committed alone before its prompt, the README before, now and at HEAD against the author`s word (applied, the rows alone, or held), REGISTRY unedited ((R312)(5))',
     lambda S: readme_ok(S), lambda S: _mut(S, 'readmej', lambda d: d.update(outcome='x'))),
    ('G-PARTNER-COPIES-ORDER', 'OPEN_TRAILS at the two landing lines: W-ORD-PAPER-PARTNER-COPIES with the object, the condition, the unit and reading 4`s counts by cause, the old line annotated superseded; the resolution the author`s word with a trigger; no paper moved or renamed ((R312)(6), N5)',
     lambda S: partners_ok(S), lambda S: put(S, 'pp_renames', 'R100\tx.md\ty.md')),
    ('G-SPEC-ROW-TWELFTH', 'the spec bank committed alone: b695`s eleven rows byte for byte and BINDER-PROVENANCE the twelfth ((R312)(7))',
     lambda S: spec_row_ok(S), lambda S: put(S, 'spec_txt', S['spec_txt'].replace('BINDER-PROVENANCE', 'BINDER-X'))),
    ('G-STANDING-CLAUSES-ORDER', 'OPEN_TRAILS at the orders` landing line: W-ORD-STANDING-CLAUSES-BANK with its price and trigger ((R312)(7))',
     lambda S: orders_ok(S), lambda S: _mut(S, 'orders_line', lambda d: d.update(lines=[dict(line=1)]))),
    ('G-WIDENING-STANDS', 'one ls-remote of SIDE-explicit-formula in this part: widening-b701 at 8a4ab68 local and remote, v0.35 peeled at d4e046a, main at v0.35, bridge-b701 absent (N4)',
     lambda S: widening_stands(S), lambda S: put(S, 'ef_remote', dict(S['ef_remote'], **{'refs/heads/' + K.WIDEN_BRANCH: '0' * 40}))),
    ('G-KERNEL-WRITES-NAMED', 'SIDE-explicit-formula`s main against v0.35: nothing of this act on it (N5)',
     lambda S: kernel_writes_ok(S), lambda S: _mut(S, 'wf', lambda d: d[K.KERNEL].update(this_act_writes=['Zeta23/x.lean']))),
    ('G-READFIRST-DIFF-BANKED', 'the readfirst diff bank and the step-zero commit, and the hand list`s blob at HEAD against step zero`s: the diff banked, no bank rewritten',
     lambda S: readfirst_diff_ok(S), lambda S: put(S, 'rf_hand_now', b'x')),
    ('G-TOOL-REPAIRS', 'the repairs bank`s verdict: the carry-time repairs, each by the defect or order it answers, the guard first, no frozen bank edited',
     lambda S: repairs_ok(S), lambda S: put(S, 'repairs', S['repairs'].replace('REPAIRS %d ;' % REPAIRS_WANT, 'REPAIRS 0 ;'))),
    ('G-PARTS-PRERUN', 'the pre-run bank`s six parts with their seconds, named in the form the parts arm reads',
     lambda S: parts_ok(S), lambda S: put(S, 'prerun', S['prerun'].replace('PART standing-b3', 'PART standing-x'))),
    ('G-ARM-SECONDS-BANKED', 'the per-arm seconds bank: every standing arm clocked at the pre-run, the three slowest named, each part`s seconds',
     lambda S: arm_seconds_ok(S), lambda S: _mut(S, 'asec', lambda d: d.update(clocked=0))),
    ('G-DEFECTS-LETTERED', 'the defects bank read at HEAD: the sealed letters its prefix, consecutive letters, owners the seat or the navigator',
     lambda S: defects_ok(S), lambda S: put(S, 'defects', S['defects'].replace("(a) THE SEAT'S", "(a) THE AUTHOR'S"))),
    ('G-READ-RULE', 'the read-call bank (data/b698_rules.txt row (2)) and the defects bank: every whole read of a file of two hundred lines or more entered by its transcript line',
     lambda S: read_rule_ok(S), lambda S: put(S, 'reads_bank', re.sub(r'WHOLE OF A FILE OF 200 LINES OR MORE (\d+)',
                                                                      lambda m: 'WHOLE OF A FILE OF 200 LINES OR MORE %d' % (int(m.group(1)) + 1), S['reads_bank']))),
    ('G-TRAIL-DEFECTS-EQUAL', 'the gate`s record and OPEN_TRAILS from the trail`s head: the trail`s Defects line equal to the defects bank in the dry run and as landed',
     lambda S: trail_defects_ok(S), lambda S: put(S, 'defshort_b702', list(S['defshort_b702']) + ['(z) THE SEAT`S: A PLANTED ROW'])),
    ('G-TRAIL-RESOLVED-EQUAL', 'the gate`s record and OPEN_TRAILS from the trail`s head: the trail`s Resolved line`s last item counting the navigator`s and the seat`s defects as the bank letters them, in the dry run and as landed (b701`s (k))',
     lambda S: trail_resolved_ok(S), lambda S: put(S, 'defshort_b702', list(S['defshort_b702']) + ["(z) THE NAVIGATOR'S: A PLANTED ROW"])),
    ('G-SPEC-PLANTED', 'tools/b702_regspec.py`s planted rows run live through the record tool`s readers, and rows of another shape refused',
     lambda S: bool(S['spec']['read']) and all(S['spec']['read']) and all(S['spec']['controls']) and any('runner' in x for x in S['spec']['shapes']),
     lambda S: _mut(S, 'spec', lambda d: d['controls'].append(False))),
    ('G-CONVERSION-ONE', 'every b702 tool`s code: no conversion defined (conv imported from b652_record); the suite importing it',
     lambda S: S['conv_bad'] == [] and 'from b702_record import conv' in S['suite'], lambda S: put(S, 'conv_bad', ['b702_checks.py'])),
    ('G-WORKFLOW-FILES', 'SIDE-explicit-formula`s workflow at main: equal to its last write and that write before b701, no author identifier, no secret, the hold, the cache step for its Mathlib lakefile, the print step over its list, every listed name printed by the last merged run, the files b701 wrote',
     lambda S: wf_ok(S), lambda S: _mut(S, 'wf', lambda d: d[K.KERNEL].update(text=d[K.KERNEL]['text'] + ' secrets.X'))),
    ('G-RUNNER-READ', 'the last merged run (b701`s at SIDE-explicit-formula) through the record tool`s reader: at its branch tip, success, the artifact`s sha256, the memory low above the hold, the gate DERIVES',
     lambda S: runner_ok(S), lambda S: _mut(S, 'runner', lambda d: [r.update(mem_low=2000) for r in d['rows']])),
    ('G-RUNNER-GATE', 'the last merged run`s gate reading: build exit 0, no error line, no sorryAx in the print step, the artifact`s digest agreeing',
     lambda S: gate_ok(S), lambda S: put(S, 'rbanks', dict((k, v.replace('GATE DERIVES', 'GATE NOT DERIVES')) for k, v in S['rbanks'].items()))),
    ('G-MERGES-ON-GATE', 'SIDE-explicit-formula`s main: the last merge --no-ff with the main before b701 and the branch tip as parents, the merged tree the built tree, the tag at the merge naming the prior tag, main`s first-parent line the merge alone, no sorry in code on main',
     lambda S: merges_ok(S), lambda S: put(S, 'merges', [dict(m, trees=(m['trees'][0], 'x')) for m in S['merges']])),
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
    ('G-PP-SCOPE', 'PLACE-papers` changed files against FINDINGS, OPEN_TRAILS and the files the word allowed (the cut document, the faces page, the README) (N5)',
     lambda S: corpus_scope(S), lambda S: put(S, 'pp_changed', S['pp_changed'] + ['day1/ONE_PAGE_PROOF.md'])),
    ('G-CURRENTS-UNEDITED', 'the map, the census, the monograph, the Dirichlet page, the surround, both SIMPLICITY copies, REGISTRY, FOUNDATIONS and its one-copy partner, INSTRUMENTS, both PATHS copies, the substrate pages and the six other companions: working tree, before and HEAD',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'ERRATA.md': (b'x', b'y', b'y')}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read before the seal (read after step zero`s deletes)',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b701`s to b695`s sealed tools and the earlier tools, the readers, the push tool, the act-root tool, the generators and their tests, the corrigendum tools, edit_route.py, chain_page.py, e0_rule.py, the witness`s window, the mirror`s and the shared tools, rule_arms.py and circuit_correspondence.py among them: before, working tree and HEAD',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'additive_shared.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 613847d6 but the shared additive files (act_roots.txt and the corrigenda bank among them), by blob id',
     lambda S: S['prior_bad'] == [] and S['prior_n'] > 0, lambda S: put(S, 'prior_bad', ['data/b701_stepzero.txt'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS before and now', lambda S: S['fi_pre'] is not None and (S['fi_now'] or b'').startswith(S['fi_pre']),
     lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS before and now', lambda S: S['ot_pre'] is not None and (S['ot_now'] or b'').startswith(S['ot_pre']),
     lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-NODISCLOSURE-PUBLIC', 'TECHNE-Core`s needle sets over every public byte the act writes: the ledger lines, the banks, the tools and the bytes appended to the cut document, the README and the faces page',
     lambda S: bool(S['nd_pub']) and not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', {'method': 1})),
    ('G-OUTSIDE-NAMED-NOWHERE', 'the ledger lines appended', lambda S: S['outside'] == [], lambda S: put(S, 'outside', ['x'])),
    ('G-DELETE-FREE', 'the act`s tools` code, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='os' + '.remove(p)'))),
    ('G-PUBLISH-UNCALLED', 'the act`s tools` code: no publish call', lambda S: publish_uncalled(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='z_' + 'publish()'))),
    ('G-SEALED-AFTER-COMPONENTS', 'the lock time against every relay and PLACE-papers commit of the act by its subject', lambda S: sealed_after_ok(S),
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b702 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'b702_closing.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3), in six parts summed',
     lambda S: S['lock_epoch'] is not None and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b701`s trail record on OPEN_TRAILS and its root in the chain', lambda S: K.B701_TRAIL_HEAD in S['ot']
     and S['rootsf'].count(NL + 'b701 ') == 1, lambda S: put(S, 'ot', S['ot'].replace('### b701 — lane two', '### b701 - lane two'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], grade_moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 79th chain row (the corrigendum row apart), the root bank and its items, the tie, the cut, the corrigendum and the guard among them, no binary, mirror, chain-half or untracked bank',
     lambda S: root_banked_ok(S), lambda S: put(S, 'rootsf', S['rootsf'] + 'b703 x y' + NL)),
    ('G-ROOT-BANKS-COMMITTED', 'the root route`s banked reading and every named bank`s blob at the root`s recorded commit: clean and equal at HEAD, HEAD the remote main, the recorded hash carried by the recorded commit',
     lambda S: root_banks_committed_ok(S), lambda S: put(S, 'rootbanks', dict(S['rootbanks'], pushed=False))),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit in two halves by act with the suite`s own remote reads: standing-b2`s banked b624-b658 and standing-b3`s b659-b702 all AGREE, the boundary link equal, b680 read through its corrigendum row (4 banks), b702 written LF',
     lambda S: verify_ok(S), lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s through conv, and its parts', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line, the head through conv', lambda S: bool(S['tj'].get('line'))
     and oline(S, S['tj']['line']) == conv(S['REC'].TRAIL_HEAD()), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b702 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b702_record.py agree', 'b702_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line: b703', lambda S: '**Next:** b703' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** b703', '**Next:** b704'))),
] + [('G-N%d-SCORED' % i, 'the scores through the record tool`s reader, and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i),
      lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written since 613847d6 and 1e3fda0 against the (W) globs',
     lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b702')" in S['suite'] and "'data/b702_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b702_closing.py: the closing sentence in the rule`s words with the plain reads named; the citation check, the record lines, the dry run, the corrigendum, the guard, the re-cut, the faces row, the README, the partner copies, the orders, the kernels, the mirror, the carry-time reading',
     lambda S: closing_sentence_ok(S), lambda S: put(S, 'closing_src', S['closing_src'].replace('no identifier of the author ' + 'in any outbound', 'x'))),
    ('G-LSREMOTE-ONE-PER-REPO', 'the part`s ls-remote calls per repository, read after every other arm of the part has run (OPEN_TRAILS :12703)',
     lambda S: lsr_ok(S), lambda S: put(S, 'lsr', {PP: 2})),
] + [(nm, 'tools/rule_arms.py (the author`s word on (R293)(6); (R301)(6) for four; G-RULE-SUITE-PARTS as repaired under (R302)(2); G-RULE-BINARY-HASHES as repaired under (R306)(2)) -- ' + reads,
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
    p = os.path.join(D, 'b702_seal_hashes.json')
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
    print('  written: b702_seal_hashes.json')
    return 0


def _base_name(pushed):
    if PRERUN:
        return 'b702_arms_prerun.txt'
    if MID and len(sys.argv) > sys.argv.index('--mid') + 1:
        return sys.argv[sys.argv.index('--mid') + 1]
    if RERUN and len(sys.argv) > sys.argv.index('--rerun-postpush') + 1:
        return sys.argv[sys.argv.index('--rerun-postpush') + 1]
    return 'b702_checks_postpush.txt' if pushed else 'b702_checks.txt'


def _part_name(base, part):
    return base.replace('.txt', '_%s.txt' % part)


def _write(name, lines):
    out = os.path.join(D, name)
    b = (NL.join(lines) + NL).encode('utf-8')
    with open(out + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(out + '.tmp', out)
    return out


def writer_plan(prerun, rerun, mid, pushed):
    """(R312)(2): the banks the writer block at the end of a part would write, by mode -- the part bank and the ls-remote bank in every mode,
    the exercise bank in every mode, the per-part seconds bank under `if PRERUN:` alone. Read by `--guard-dry`; the writer block beneath follows
    this plan exactly (the arm G-GUARD-RESTORED reads the block's own text)."""
    base = 'b702_arms_prerun.txt' if prerun else ('b702_checks_postpush.txt' if (rerun or pushed) else 'b702_checks.txt')
    out = [('data/' + _part_name(base, '<part>')), ('data/' + _part_name(base, '<part>').replace('b702_arms_prerun', 'b702_lsr_prerun').replace('b702_checks', 'b702_lsr').replace('.txt', '.json')),
           'data/b702_exercise_<part>.json']
    seconds = ['data/b702_arm_seconds_<part>.json'] if prerun else []
    return out, seconds


def guard_dry():
    """the dry run of (R312)(2): for each run mode, what the writer block would write; nothing written by this route, the record tool banks it."""
    for mode, args in (('prerun', (True, False, False, False)), ('pre-push', (False, False, False, False)), ('post-push', (False, True, False, True))):
        out, seconds = writer_plan(*args)
        print('  MODE %-9s | the part`s banks: %s | the per-part seconds bank: %s' % (mode, ', '.join(out), ', '.join(seconds) or 'NONE'))
    print('  ### POST-ROOT PATH WRITES NONE of the root-named per-part seconds banks: the pre-push and post-push modes write no data/b702_arm_seconds_<part>.json')
    return 0


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
        ex.update(jl('b702_exercise_%s.json' % part).get('exercise') or {})
    if ex and base in ('b702_checks.txt', 'b702_checks_postpush.txt'):
        e = (json.dumps(dict(exercise=ex, run=n, live_failing=fails, defective=defs, neg_failures=ng), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p_ = os.path.join(D, 'b702_exercise.json')
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
    if GUARD_DRY:
        return guard_dry()
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
    rec('b702 -- THE SUITE. ### **%s READING.** ### PART %s ### every arm exercised on both controls.' % (
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
    rec('  ### (R264)(2) THE FREEZE: the standing arms (b701`s face less its own arms, the twenty-four rule arms among them; none added) %d ; '
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
            rec('  ### the reads at commit, b680: %s ; b702: %s' % (S['ar_reads'].get('b680'), S['ar_reads'].get('b702')))
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
    rec('  ### PLACE-papers` changed files %d against the allowed %d (the two ledgers and the files the word allowed): beyond %s' % (
        len(S['pp_changed']), len(S['pp_allowed']), sorted(set(S['pp_changed']) - set(S['pp_allowed'])) or 'NONE'))
    rec('  ### SIDE-explicit-formula: main %s (v0.35 %s) ; the last merge %s ; widening-b701 %s' % (
        S['ef_main'][:12], K.EF_V035[:12], '; '.join('%s %s' % (m['tag'], m['merge'][:12]) for m in S['merges']) or 'NONE', (S['widen_tip'] or 'absent')[:12]))
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
    lp = os.path.join(D, _part_name(base, PART).replace('b702_arms_prerun', 'b702_lsr_prerun').replace('b702_checks', 'b702_lsr').replace('.txt', '.json'))
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    with open(lp + '.tmp', 'wb') as fh:
        fh.write(lb)
    os.replace(lp + '.tmp', lp)
    ex = dict(exercise=EX, run=len(arms), live_failing=fail, defective=defective, neg_failures=negfail, part=PART)
    ep = os.path.join(D, 'b702_exercise_%s.json' % PART)
    with open(ep + '.tmp', 'wb') as fh:
        fh.write((json.dumps(ex, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(ep + '.tmp', ep)
    # ### (R312)(2): THE GUARD RESTORED -- the per-part seconds bank (root-named, gathered by the record tool's armsecs before the seal) is
    # ### written by the pre-run alone, as tools/b700_checks.py :1669 had it; the pre-push and post-push runs write no root-named bank (N4)
    if PRERUN:
        sp = os.path.join(D, 'b702_arm_seconds_%s.json' % PART)
        with open(sp + '.tmp', 'wb') as fh:
            fh.write((json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), part=PART, arms=SECS, phases=S['phase_secs'], run_secs=int(secs)),
                                 indent=1, ensure_ascii=False) + NL).encode('utf-8'))
        os.replace(sp + '.tmp', sp)
    print('  written: %s' % os.path.basename(out))
    return 0 if (not fail and not defective and negfail == 0) else 1


if __name__ == '__main__':
    sys.exit(main())
