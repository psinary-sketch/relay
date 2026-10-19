# -*- coding: utf-8 -*-
"""b691_checks.py -- THE SUITE OF b691, UNDER (R301): b690 AT ITS WEIGHT; SIDE-rcurve RE-CUT UNDER THE QUOTATION RULE; THE CORRESPONDENCE
GENERATOR'S CARRIED-AT REPAIR, ITS DRY, ITS RUN ON THE AUTHOR'S WORD AND THE BEHIND COUNT BY ROW; THE EPSTEINQ0 DOCSTRINGS RE-CUT; THE STALE
ORDERS TRIAGED; FOUR RULE ARMS ADDED.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### (R301)(8) and data/b685_rules.txt row (1): every run in FIVE foreground parts, each its own call in its own message -- `--part
### standing-a`, `--part standing-c` (G-PRIORBANK-UNCHANGED, G-NODISCLOSURE-PUBLIC, G-WRITELIST-KINDS), `--part standing-b1` (the shared
### additive files), `--part standing-b2` (the act-root chain) -- b690's standing-b split at its midpoint, the two arms falling either side
### of it (relay data/b691_readfirst.txt, the seconds bank row) -- and `--part act` (the act's arms over this act's banks, the table
### regenerated in a closing run); each under the 590 s guard the seat runs it in, and NOT RUN beneath the 2,560 MB hold; `--combine <bank>`
### writes the bank.
### ### (R264)(2), THE FREEZE, AND (R301)(6): the standing arms are b690's face's (G2) arms less b690's own arms over b690's banks, carried,
### the twenty rule arms of tools/rule_arms.py among them, and the four rule arms (R301)(6) adds through tools/rule_arms.py, each counted at
### HEAD before this face named it (relay data/b691_arms_added.txt). The act's own arms read this act's banks alone (ACT_ARMS). The standing
### runner arms read this act's two runs and merges -- SIDE-rcurve's and SIDE-explicit-formula's (tools/b691_worklist.py MERGES).
### ### Every look-up of a landed line goes through the one conversion (imported from tools/b652_record.py through tools/b691_record.py).
### ### The harness is b568's to b690's, written by the Write tool from tools/b690_checks.py; the sources, predicates and arms over this act's
### ### banks are b691's. data/b686_rules.txt row (1): the act arm G-ENTRY-SCORES-EQUAL reads the landed entry; no scorer reads a ledger line.
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
import b691_worklist as K     # noqa: E402
import b690_worklist as K690  # noqa: E402
import b689_worklist as K689  # noqa: E402
import b688_worklist as K688  # noqa: E402
import b687_worklist as K687  # noqa: E402
import b686_worklist as K686  # noqa: E402
import b685_worklist as K685  # noqa: E402
import b684_worklist as K684  # noqa: E402
import b683_worklist as K683  # noqa: E402
import b682_worklist as K682  # noqa: E402
import b681_worklist as K681  # noqa: E402
import b680_worklist as K680  # noqa: E402
import b679_worklist as K679  # noqa: E402
import b678_worklist as K678  # noqa: E402
import b677_worklist as K677  # noqa: E402
import b676_worklist as K676  # noqa: E402
import b675_worklist as K675  # noqa: E402
import b674_worklist as K674  # noqa: E402
import rule_arms as RA        # noqa: E402
from b691_record import conv  # noqa: E402

NL = chr(10)
PP = K.PP
FACE = os.path.join(D, 'b691_registration_2026-10-19.txt')
B690_FACE = os.path.join(D, 'b690_registration_2026-10-19.txt')
B690_ACT_ARMS = K690.ACT_ARMS
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
FLOORS = dict(prompts=4, calls=4, checks=4, defects=tuple((x, 'SEAT') for x in 'abcdefghijk'))
REPAIRED_TOOLS = K.REPAIRED_TOOLS                      # ### the generator, its test and the rule arms: their diffs in data/b691_tool_repairs.txt
INST = tuple(t for t in K690.SEALED) + ('b690_corrigendum.py', 'b690_readings.py') + tuple(t for t in K689.SEALED) + \
    ('b689_corrigendum.py', 'b689_constants.py') + tuple(t for t in K688.SEALED) + \
    tuple(t for t in K687.SEALED) + ('b687_readings.py',) + tuple(t for t in K686.SEALED) + \
    tuple(t for t in K685.SEALED) + ('b685_count.py',) + tuple(t for t in K684.SEALED) + \
    tuple(t for t in K683.SEALED) + ('b683_epstein_map_angle.py',) + \
    tuple(t for t in K682.SEALED) + ('correspondence_gen.py', 'test_correspondence_gen.py') + tuple(t for t in K681.SEALED) + \
    ('b681_narrow.py',) + tuple(t for t in K680.SEALED) + (
    'b680_readings.py', 'b680_rules_index.py', 'b680_fig_tie.py', 'b680_fig_q0.py', 'b680_fig_li.py') + \
    K679.SEALED + ('b679_q0_membership.py', 'b679_onset.py') + K678.SEALED + ('b678_corrigendum.py',) + K677.SEALED + \
    ('b677_epstein_map_angle.py',) + K676.SEALED + K675.SEALED + ('b675_li_bench.py',) + K674.SEALED + (
        'b673_checks.py', 'b673_closing.py', 'b673_tests.py', 'b673_worklist.py', 'b673_reg_gate.py', 'b673_regspec.py', 'b673_record.py',
        'b673_citation.py', 'b673_v4_control.py',
        'b672_checks.py', 'b672_closing.py', 'b672_tests.py', 'b672_worklist.py', 'b672_reg_gate.py', 'b672_regspec.py', 'b672_record.py',
        'b672_citation.py',
        'b671_checks.py', 'b671_closing.py', 'b671_tests.py', 'b671_worklist.py', 'b671_reg_gate.py', 'b671_regspec.py', 'b671_record.py',
        'b671_citation.py', 'b671_narrow.py', 'b671_epstein_map_narrowed.py', 'b671_tie_diagnostic.py',
        'b670_record.py', 'b669_record.py', 'b667_epstein_certify.py', 'b667_epstein_map_balls.py', 'b667_tail_recheck.py',
        'b663_epstein_map.py', 'b655_record.py', 'edit_route.py', 'test_edit_route_b646.py', 'b652_record.py', 'b651_record.py',
        'b649_record.py', 'b648_record.py', 'b646_record.py', 'b645_record.py', 'b644_record.py', 'b643_record.py', 'b641_record.py',
        'b633_record.py', 'b616_record.py', 'additive_shared.py', 'premise_status.py', 'terminal_table.py',
        'banned_terms.py', 'reg_seal.py', 'b378_lockgate.py', 'push_gated.sh', 'table_gate.py', 'mirror_build.ps1', 'mirror_verify.py',
        'b616_claims.py', 'ferry_scan.py', 'e0_rule.py', 'test_e0_rule.py', 'build_watch.py', 'chain_page.py', 'ledger_split.py',
        'axiom_claim.py', 'licensed_table.py', 'registration_gate.py', 'b300_regspec.py', 'no_sorry_main.py', 'module_header.py',
        'test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py', 'test_act_root.py',
        'test_act_root_commit_b644.py', 'test_act_root_order_b641.py', 'act_root.py', 'rule_arms.py', 'repair_snapshot.py',
        'b670_record.py', 'b672_record.py', 'rowgen/rowgen.py', 'rowgen/diff_rowpin.py', 'rowgen/namemap.json')
INST = tuple(sorted(set(INST) - set(K.SEALED) - set(REPAIRED_TOOLS)))
# ### b691's repair (relay data/b691_tool_repairs.txt REPAIR 4): the faces page back among the files read unedited -- no faces write this act;
# ### the two pages the generator wrote on the author's word are not CURRENTS, G-PP-SCOPE allows them
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md',
            'phase2/method/THE_KEYSTONE_CENSUS_v0_8.md', 'day1/A_Place_to_Stand_v5_18.md', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md',
            'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md', 'day1/ONE_PAGE_PROOF.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md',
            'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', 'README.md', 'REGISTRY.md',
            'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md', 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md')
TABLE_FILES = K.TABLE_FILES
WF, PT = '.github/workflows/build-module.yml', 'print_targets.txt'
MERGES = K.MERGES
B1_ARMS = ('G-SHARED-ADDITIVE',)        # ### standing-b1: the shared additive files
B2_ARMS = ('G-ACTROOT-VERIFY',)         # ### standing-b2: the act-root chain
C_ARMS = ('G-PRIORBANK-UNCHANGED', 'G-NODISCLOSURE-PUBLIC', 'G-WRITELIST-KINDS')   # ### standing-c's arms: the written files
NEED = {'standing-a': ('live', 'rules'), 'standing-c': ('written',), 'standing-b1': ('additive',), 'standing-b2': ('chain',), 'act': ()}
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b691')
            and 'data/b691_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    import b691_record as REC
    return REC.capture()


def prev_now():
    import b691_record as REC
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
        if (f.startswith('b691_') and f.endswith('.py')) or f in REPAIRED_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks):
                bad.append(f)
    return bad


def spec_planted():
    import b691_regspec as SPEC
    P = SPEC.planted()
    ctl = [ok for _w, ok in SPEC.controls()]
    return dict(read=[ok for _s, ok, _w in P], controls=ctl, shapes=[s for s, _o, _w in P])


def _deps(ax):
    import b691_record as REC           # ### this act's runner reader
    return REC._deps(ax)


def _prints_count(k):
    return len(_deps(rd('b691_axioms_%s_after.txt' % k)))


def wf_state():
    """b689's reading, carried over this act's two merged runs: every kernel this act merged, its workflow at main against the workflow at its
    own first commit (where the act wrote it) or at the main before the act (where it did not), its dependency form read from its tree, its
    print list against this act's after-print bank for it, and the files the act wrote on its main since the main before it."""
    out = {}
    for k, _pre, _tip, _merge, _tag, before, files in MERGES:
        td = 'D:/' + k
        t = read_blob(td, 'main:' + WF)
        first = (gs(td, 'log', '--diff-filter=A', '--format=%h', '--', WF).split() or [''])[-1] if WF in files else before
        lf = read_blob(td, 'main:lakefile.toml') + read_blob(td, 'main:lakefile.lean')
        req = re.search(r'(?im)^\s*require\b[^\n]*mathlib', lf) or re.search(r'(?is)\[\[require\]\][^\[]*name\s*=\s*"mathlib"', lf)
        pt = read_blob(td, 'main:' + PT)
        out[k] = dict(text=t, before=read_blob(td, '%s:%s' % (first, WF)) if first else '', lakefile=bool(lf.strip()), mathlib=bool(req),
                      targets=[l.strip() for l in pt.split(NL) if l.strip()], printed=_prints_count(k),
                      act_writes=sorted(set(x for x in gs(td, 'diff', '--name-only', before, 'main').split(NL) if x.strip())), want=sorted(files))
    return out


def merges_state():
    out = {}
    for k, pre, tip, merge, tag, _before, _files in MERGES:
        p = 'D:/' + k
        out[k] = dict(main=gs(p, 'rev-parse', '--short=7', 'main'), parents=gs(p, 'log', '-1', '--format=%p', '--abbrev=7', 'main').split(),
                      want=(pre, tip, merge, tag), tree_main=gs(p, 'rev-parse', 'main^{tree}'), tree_built=gs(p, 'rev-parse', tip + '^{tree}'),
                      tags=dict((t, gs(p, 'rev-parse', '--short=7', t + '^{commit}')) for t in gs(p, 'tag', '--points-at', 'main').split()))
    return out


def g2_of(path):
    t = read(path)
    try:
        g2 = t[t.index('### (G2) THE GATE ARMS.'):t.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


STANDING = sorted((set(g2_of(B690_FACE)) - set(B690_ACT_ARMS)) | set(K.STANDING_ADDED))
TESTS = ('test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py', 'test_correspondence_gen.py')


def _ct(repo, rev):
    t = gs(repo, 'log', '-1', '--format=%ct', rev)
    return int(t) if t.isdigit() else None


def _root_named_at_commit(arj):
    """G-ROOT-BANKS-COMMITTED: every data/ bank the root names, its blob at the root's recorded relay commit hashed against the hash the root
    recorded: [(bank, carried at the commit, equal)]."""
    commit = (arj.get('commit') or {}).get('relay') or ''
    out = []
    for it in arj.get('items') or []:
        p = it.split()
        if p[0].startswith('data/') and len(p) == 2:
            b = blob(ROOT, '%s:%s' % (commit, p[0])) if commit else None
            out.append((p[0], b is not None, b is not None and hashlib.sha256(b).hexdigest() == p[1]))
    return out


def sources(need=()):
    """the sources the arms read; `need` (by part, (R301)(8)) names the heavy phases this part computes: 'live' (the three arms at HEAD),
    'rules' (the rule arms' trace), 'written' (the written files, the public bytes, the prior banks), 'chain' (the act-root chain), 'additive'
    (the shared files)."""
    import b691_record as REC
    import b616_record as R6
    import edit_route as ER
    import b641_record as R41
    import additive_shared as ADD
    face = read(FACE)
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b691_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if (f.startswith('b691_') and f.endswith('.py')) or f in REPAIRED_TOOLS)
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    cit = jl('b691_citation_check.json')
    t0 = time.time()
    S = dict(
        REC=REC, ER=ER, face=face, ferry=rd('b691_ferry.txt'), scan=rd('b691_ferry_scan.txt'), stepz=rd('b691_stepzero.txt'),
        readfirst=rd('b691_readfirst.txt'), defects=rd('b691_defects.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        answers=rd('b691_author_answers.txt'), answersj=jl('b691_author_answers.json'), prerun=rd('b691_arms_prerun.txt'), rl=jl('b691_record_lines.json'),
        tests=jl('b691_tests_stepzero.json'), testst=rd('b691_tests_stepzero.txt'), withheld=jl('b691_tests_withheld.json'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b691_seal_hashes.json'), sealnow=sealed_now(), cmds=capture_now(), prev_cmds=prev_now(), cmdj=jl('b691_commands.json'),
        cmdt=rd('b691_commands.txt'),
        planted={t: run_test(t) for t in TESTS}, spec=spec_planted(), conv_bad=conv_alone(), suite=read(os.path.join(T, 'b691_checks.py')),
        citation=rd(K.CITATION_BANK), cit_at=iso_epoch(cit.get('at') or ''), cit_misses=cit.get('misses') or [],
        gate=rd('b691_reg_gate.txt'), rowgen=rd('b691_rowgen_stepzero.txt'),
        branchj=jl('b691_branches.json'), branchest=rd('b691_branches.txt'),
        branch_lists=dict((repo, gs(repo, 'branch', '--list', *bs)) for repo, bs in K.DELETE),
        remote_lists=dict((repo + ' ' + b, gs(repo, 'branch', '-r', '--list', 'origin/' + b)) for repo, b in K.DELETE_REMOTE),
        repairs=rd('b691_tool_repairs.txt'), rec_src=read(os.path.join(T, 'b691_record.py')),
        tie=rd('b691_tie.txt'), cutj=jl('b691_cut.json'), cut_txt=rd('b691_cut.txt'), quote_ep=rd('b691_quote_epstein.txt'),
        quote_rc=rd('b691_quote_rcurve.txt'), prints_rc=rd('b691_prints_SIDE-rcurve.txt'), prints_ef=rd('b691_prints_SIDE-explicit-formula.txt'),
        gen_dry=rd('b691_correspondence_dry.txt'), gen_run=rd('b691_correspondence_run.txt'), gen_test=rd('b691_gen_test.txt'),
        gen_snap=rd('b691_gen_snapshot.txt'), gen_live=rd('b691_gen_live.txt'), run_paths=rd('b691_correspondence_run_PATHS.txt'),
        run_rcurve=rd('b691_correspondence_run_RCURVE.txt'), behind=rd('b691_behind.txt'), behindj=jl('b691_behind.json'),
        ep_lines=rd('b691_epstein_lines.txt'), ep_cut=rd('b691_epstein_cut.txt'), triagej=jl('b691_orders_triage.json'),
        triage_t=rd('b691_orders_triage.txt'), sort_t=rd('b691_arms_sort.txt'), added_t=rd('b691_arms_added.txt'),
        order_head=REC.OH, ostate=REC._order_state(), cutstate=REC._cut_state(), bstate=REC._behind_state(),
        asec=jl('b691_arm_seconds.json'), asect=rd('b691_arm_seconds.txt'),
        shared=dict((p, (cr0(blob(ROOT, '%s:%s' % (PRE['relay'], p))), cr0(raw(os.path.join(ROOT, *p.split('/')))), cr0(blob(ROOT, 'HEAD:' + p))))
                    for p in K.SHARED_APPENDED),
        t=dict(gen_run=_ct(PP, K.GEN_RUN_PP), epstein_lines=_ct(ROOT, K.EPSTEIN_LINES_COMMIT), epstein_cut=_ct('D:/SIDE-explicit-formula', 'c5aa058'),
               arms=_ct(ROOT, K.ARMS_COMMIT), c1=_ct(PP, K.C1_PP), order=_ct(PP, K.ORDER_PP)),
        files=dict(order=files_of(PP, K.ORDER_PP), triage=files_of(ROOT, K.TRIAGE_COMMIT), gen_run=files_of(PP, K.GEN_RUN_PP),
                   arms=files_of(ROOT, K.ARMS_COMMIT)),
        standing=STANDING, wf=wf_state(), runner=jl(K.RUNNER_ROWS),
        rbanks=dict(('%s_%s' % (r.get('kernel'), r.get('label')), rd('b691_runner_%s_%s.txt' % (r.get('kernel'), r.get('label'))))
                    for r in jl(K.RUNNER_ROWS).get('rows') or []),
        merges=merges_state(),
        export_present=os.path.exists(os.path.join(ROOT, *EXPORT.split('/'))), export_log=gs(ROOT, 'log', '--all', '--format=%h', '--', EXPORT),
        export_index=gs(ROOT, 'ls-files', '--', EXPORT), export_status=gs(ROOT, 'status', '--porcelain', '--', EXPORT),
        closing_src=read(os.path.join(T, 'b691_closing.py')),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b691_act_root.json'), arj0=jl('b690_act_root.json'), art=rd('b691_act_root.txt'), rootsf=rd('act_roots.txt'),
        rootbanks=jl('b691_root_banks.json'),
        pushout=(files_of(ROOT, K.STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, *f.split('/')))), cr0(blob(ROOT, 'HEAD:tools/' + f)))
              for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b691_kernels_face.json').get('kernels') or {}), kerns_read=list(dict.fromkeys(REC._kerns())),
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mustfail=not os.path.exists(os.path.join(D, 'b691_mustnotexist.txt')),
        fj=jl('b691_findings.json'), tj=jl('b691_trail.json'), sc=jl('b691_scores.json'), desk=rd('b691_desk_notes.txt'), tfj=jl('b691_table_final.json'),
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
    S['ra'] = RA.sources('b691', SESSION, K.ANCHOR, K.PARTS, S['lock_epoch'], PRE['relay'], PRE['pp']) if 'rules' in need else {}
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
            if f.startswith(('b691_', 'audit_b691_')) and os.path.isfile(os.path.join(D, f)) and not f.endswith(('.gz', '.png', '.jsonl')):
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
    if 'chain' in need:
        try:
            S['ar_verify'] = AR.verify(remote=KC0.remote_refs)
            S['ar_reads'] = dict(AR.READS_AT)
        except Exception as e:
            S['ar_verify'], S['ar_reads'] = [('raised', type(e).__name__, [])], {}
    else:
        S['ar_verify'], S['ar_reads'] = [], {}
    S['phase_secs']['the act-root chain' + ('' if 'chain' in need else ' (not in this part)')] = time.time() - t1
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


# ### b691's reading (REPAIR 5): the step-zero bank's failing set, run against the list the page named at step zero (b690's)
STEPZERO_FAILING = {'test_chain_page.py': ['(9)'], 'test_chain_page_b638.py': ['(4)', '(5)', '(6)', '(7)']}


def tests_ok(S):
    j = S['tests']
    names = sorted(S['tracked_tests'])
    nf = dict((n, x['failing']) for n, x in j.items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(j) == sorted(set(names) - {'test_elab_reader_b634.py'}) and nf == STEPZERO_FAILING \
        and 'b690_nodes_zeta.txt' in (j.get('test_chain_page.py') or {}).get('args', []) \
        and 'test_elab_reader_b634.py' in S['withheld'] \
        and ('TEST FILES %d ; RUN %d ; WITHHELD 1 ; NOT CLEAN 2' % (len(names), len(names) - 1)) in unwrap(S['testst'])


UNANSWERED = "The user doesn't want to proceed with this tool use"


def _post_seal_named(face):
    m = re.search(r'### POST-SEAL PROMPTS NAMED: (NONE|\d+)', face)
    return 0 if not m or m.group(1) == 'NONE' else int(m.group(1))


def answers_ok(S):
    """the answers bank read at HEAD (standing from (R291)(3)): its prompt and call counts at or above the sealed floors, every prompt with
    its options and every call with its result; any call put after the lock named on the face."""
    a = S['answers']
    m = re.search(r'^### b691 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
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
    """b687's reading, carried (b691's window): the record tool's one reading over this act's whole capture and the previous act's after its
    post-push suite in this same session -- tools/edit_route.py's arms and sed in any form (data/b685_rules.txt row (2))."""
    return bool(S['cmds']) and bool(S['prev_cmds']) and S['REC'].edit_route_offences(S['cmds'] + S['prev_cmds']) == []


def no_local_lean(S):
    import b691_record as REC
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


# ================================================================== (R301) STEP ZERO: THE CITATION CHECK, THE BRANCHES
READFIRST_NEEDLES = ('relay data/b690_closing.txt :1', 'relay data/b690_defects.txt :5-:45', 'relay data/b690_reading3.txt',
                     'relay data/b690_rules.txt :6, :9, :13', 'relay data/b690_circuit_spec.txt', 'relay data/b690_arm_seconds.txt :93-:94',
                     'relay data/b670_licensed_table.txt :100', 'data/b647_table_SIDE-rcurve.txt :30', 'relay data/b674_rules.txt :8-:11',
                     'relay data/b683_arms_sort.txt :3-:8', 'relay tools/rule_arms.py', 'relay tools/correspondence_gen.py',
                     'relay data/b688_correspondence_dry.txt :12', 'PLACE-papers OPEN_TRAILS.md :14922', 'relay data/b690_r3_orders.json',
                     'relay data/b690_closing_push_out.txt')
NAMED_LOCAL = sorted(b for _r, bs in K.DELETE for b in bs)
NAMED_ALL = sorted(NAMED_LOCAL + [b for _r, b in K.DELETE_REMOTE])


def readfirst_ok(S):
    z = unwrap(S['readfirst'])
    return bool(z) and all(x in z for x in READFIRST_NEEDLES)


def branches_ok(S):
    """the two repositories' local branch lists by the ruling's names (no remote branch named), and the branches bank."""
    z = S['branchest']
    left = dict((r, sorted(x.strip() for x in v.split(NL) if x.strip())) for r, v in S['branch_lists'].items())
    rem = dict((r, sorted(x.strip() for x in v.split(NL) if x.strip())) for r, v in S['remote_lists'].items())
    return all(v == [] for v in left.values()) and len(left) == 2 and all(v == [] for v in rem.values()) and len(rem) == 0 \
        and all(b in z for b in NAMED_LOCAL) and 'BRANCHES 5 (LOCAL 5, REMOTE 0) ; MERGED 5 ; TO BE DELETED 5 ; UNNAMED OF b690 0' in unwrap(z)


def branches_banked_ok(S):
    import b691_record as REC
    rows = S['branchj'].get('rows') or []
    try:
        fates = [REC.read_branch_row(r) for r in rows]
    except Exception:
        return False
    return len(rows) == 5 and all(f == 'DELETED' for _b, f in fates) and all(r['merged'] for r in rows) \
        and sum(1 for r in rows if r['where'] == 'remote') == 0


def deletes_one_ok(S):
    import b691_record as REC
    shapes = [REC.delete_shape(r['cmd']) for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell')]
    shapes = [s for s in shapes if s[0]]
    return bool(shapes) and all(len(d) == 1 and not gl for d, gl in shapes) and sorted(x for d, _g in shapes for x in d) == NAMED_ALL \
        and 'BRANCH DELETES OF ONE BRANCH AND NO GLOB 5 OF 5' in S['cmdt']


def dry_step_ok(S):
    g = S['gate']
    return '--- THE DRY-RUN STEP ((R267)(2))' in g and 'ENTRY : table cells NONE ; screens QUIET' in g and 'TRAIL : table cells NONE ; screens QUIET' in g \
        and '### ### **THE DRY-RUN STEP : CLEAN**' in g and '### ### **GATE VERDICT : CLEAR**' in g


def closing_dry_ok(S):
    g = S['gate']
    return '--- THE CLOSING DRY-RUN STEP (b675 rules row 1)' in g and '### ### **THE CLOSING DRY-RUN STEP : CLEAN**' in g \
        and 'b691 closed:' in g and 'the misses as the bank lists them' in g and '(annotated, peeled) ; main' in g \
        and '### THE RE-CUT' in g and '### THE GENERATOR' in g and '### THE KERNELS' in g and '### NO VERDICT LINE' not in g


def citation_ok(S):
    """the citation bank: run at step zero, no miss of the ruling or the ferry; every mid-act check printed in it, each commit miss of a kernel
    outside the route's repositories tested directly and noted beneath its check."""
    c = S['citation']
    m = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', c)
    raised = re.findall(r'RAISED: ([0-9a-f]{7})\.\*\*', c)
    tested = re.findall(r'### the miss tested directly by the seat \([^)]*\): ([0-9a-f]{7}) is a commit of SIDE-', c)
    return bool(m) and int(m.group(1)) == int(m.group(2)) + int(m.group(3)) > 0 and 'A GATE STEP AT STEP ZERO' in c \
        and int(m.group(3)) == 0 == len(S['cit_misses']) and sorted(raised) == sorted(tested)


def rowgen_ok(S):
    return '### ### **CONSTELLATION EXIT 0 ; ROWGEN DIFF EXIT 0 ; TABLES 19.**' in S['rowgen']


def weight_ok(S):
    return landed(S, 0, ['b690 AT ITS WEIGHT', 'READING 3 ON THE RECORD', '55e34098'])


# ### each mid-act answer's check before the write its answer governs: the generator's run (the pages' commit), the Epstein lines bank, the cut
ANSWER_GOVERNS = (('W-ORD-CORRESPONDENCE-BEHIND-SCOPE', 'gen_run'), ('recut-epstein-b691', 'epstein_lines'),
                  ('its count T3 read off the bench', 'epstein_cut'), ('P4 by its own docstring', 'epstein_cut'))


def answers_checked_ok(S):
    """the citation bank's mid-act prints read at HEAD, at or above the sealed floor, each before the write its answer governs."""
    c = S['citation']
    stamps = re.findall(r'### \(R278\)\(4\) THE MID-ACT CHECK \((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\): the answer carrying \'([^\']+)\'', c)
    acts = dict((n, iso_epoch(t)) for t, n in stamps)
    return len(stamps) >= FLOORS['checks'] and all(any(k in n for n in acts) and S['t'].get(w) and max(v for n, v in acts.items() if k in n) < S['t'][w]
                                                   for k, w in ANSWER_GOVERNS)


# ================================================================== (R301)(2)-(6): THE RE-CUT, THE GENERATOR, EPSTEINQ0, THE ORDERS, THE ARMS
def _fn_src(src, name):
    if ('\ndef %s(' % name) not in src:
        return ''
    i = src.index('\ndef %s(' % name) + 1
    m = re.search(r'\n(?=\S)', src[i + 1:])
    return src[i:i + 1 + m.start() + 1] if m else src[i:]


def scorer_banks_ok(S):
    """data/b686_rules.txt row (1), standing: the N2-N4 scorers' code reads banks and commits and no ledger and no findings bank; the scores
    route writes its bank once; the entry's composer takes its scores line from the scores bank."""
    n = ''.join(strip_prose(_fn_src(S['rec_src'], f)) for f in ('_n2', '_order_state', '_n3', '_cut_state', '_n4', '_behind_state'))
    sc = strip_prose(_fn_src(S['rec_src'], 'scores'))
    ft = strip_prose(_fn_src(S['rec_src'], '_finding_text'))
    return bool(n) and 'b691_tie.txt' in n and 'b691_cut.json' in n and 'b691_behind.txt' in n \
        and not re.search(r'\b(FIND|OT)\b|FINDINGS|OPEN_TRAILS|findings|entry_line', n) \
        and "os.path.isfile(os.path.join(D, 'b691_scores.json'))" in sc and 'scores_line(S)' in ft and "jl('b691_scores.json')" in ft


def _entry_block(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    if not e:
        return ''
    end = next((i for i in range(e, len(ls)) if ls[i].startswith('## ')), len(ls))
    return NL.join(ls[e - 1:end])


def entry_scores_ok(S):
    """data/b686_rules.txt row (1): the landed entry's scores line equals the line composed from the scores bank."""
    import b691_record as REC
    want = conv(REC.scores_line(S['sc'])) if S['sc'] else None
    blk = _entry_block(S)
    got = [l for l in blk.split(NL) if l.startswith('**The scores.**')]
    return bool(want) and bool(S['sc']) and got == [want]


def entry_title_ok(S):
    """the ferry's Component 6: the landed entry's title in the ferry's form adjusted to what the act read, its parts read from the banks by the
    record tool, equal to the worklist's title."""
    e = S['fj'].get('entry_line')
    return bool(e) and S['REC']._title() == K.TITLE and fline(S, e) == conv(K.TITLE)


def tie_ok(S):
    """N2: the tie's rule and rows banked before SIDE-rcurve's first write of the act, the bank's verdict naming the document by b674's row (2)."""
    return S['ostate'].get('tie') is True and 'THE TIE BROKEN BY b674`S ROW (2): SIDE-rcurve IS CUT' in S['tie']


def cut_ok(S):
    c = S['cutj']
    return c.get('before') == 2 and c.get('after') == 0 and c.get('tag') == 'v0.1.1' and S['cutstate'].get('distance') is True \
        and 'SIDE-rcurve RE-CUT: THE DISTANCE BEFORE 2, AFTER 0 ; TAG v0.1.1 ; PRINTS EQUAL' in S['cut_txt'] and 'R-K1' in S['cut_txt'] \
        and len(c.get('residues') or []) == 4


def prints_equal_ok(S):
    return S['cutstate'].get('prints') is True and 'BEFORE 8 TERMINALS' in S['prints_rc'] and 'BEFORE 72 TERMINALS' in S['prints_ef'] \
        and all('DIFFERING 0 ; NEW 0 ; EQUAL LINE FOR LINE True' in p for p in (S['prints_rc'], S['prints_ef']))


def quote_ok(S):
    q = S['cutstate'].get('quotes') or []
    return len(q) == 2 and all(x['before'] and x['printed'] for x in q) and 'the control FIRES FOR EVERY NEEDLE IN BOTH SHAPES' in S['quote_ep'] \
        and 'QUOTING LINES 4' in S['quote_rc'] and 'QUOTING LINES 0' in S['quote_ep']


def gen_carried_ok(S):
    """(R301)(3): the generator's carried-at repair -- its planted cases six of six, its diff banked as row 1 of the repairs bank with its test
    as row 2, the dry beside b688's two with the :302 cell read at its carry and out of the diff."""
    return planted_ok(S, 'test_correspondence_gen.py', 6, form='PLANTED CASES 6 ; AS WANTED 6 ; PASS') \
        and '### ROW 1 -- tools/correspondence_gen.py' in S['repairs'] and '### ROW 2 -- tools/test_correspondence_gen.py' in S['repairs'] \
        and 'PLANTED CASES 6 ; AS WANTED 6 ; PASS' in S['gen_test'] and S['cutstate'].get('carry') is True \
        and "b688`s FIVE: FOUR IN THE DIFF AS AT b688`s SECOND" in S['gen_dry']


def behind_ok(S):
    j = S['behindj']
    return S['bstate'].get('rows') is True and S['bstate'].get('cause') is True and len(j.get('rows') or []) == 57 and j.get('claim') == 1 \
        and 'THE GENERATOR`S CLAIM AFTER THE WRITE 0 of 1' in S['behind'] and 'TECHNE_TOOLKIT :511; TECHNE_TOOLKIT :513' in S['behind']


def gen_run_ok(S):
    """N4's second clause and the author's word: the pages written by the generator alone after the answer, its snapshot and live banks clean,
    the two page diffs banked."""
    return S['bstate'].get('after_word') is True and S['cutstate'].get('by_generator') is True and S['files']['gen_run'] == sorted(K.GEN_PAGES) \
        and 'SNAPSHOT: EXIT 0 ; ESCAPED 0 ; STILL DIFFERING 0' in S['gen_snap'] and 'STILL DIFFERING 0' in S['gen_live'] \
        and 'LINES CHANGED 3' in S['run_paths'] and 'LINES CHANGED 1' in S['run_rcurve'] and ':301 HELD, VERSION DIFFERS' in S['run_paths']


def order_ok(S):
    o = oline(S, K.ORDER_LINE)
    return o.startswith(conv(S['order_head'])) and 'Trigger: the next re-cut act after b691. Status OPEN.' in o and S['files']['order'] == ['OPEN_TRAILS.md']


def epstein_lines_ok(S):
    e = S['ep_lines']
    return S['ostate'].get('epstein') is True and ':106 BEFORE' in e and ':106 AFTER' in e and ':111 AFTER' in e \
        and 'P4 READS "CITED, NOT COMPILED" (Epstein.lean :40) -- RAISED ; NO BRANCH' in e and 'SUCCESSOR LINES 3 ; DOCSTRINGS ALONE' in e


def epstein_recut_ok(S):
    m = S['merges'].get('SIDE-explicit-formula') or {}
    return 'EpsteinQ0 DOCSTRINGS RE-CUT, v0.34.1 = e5fcda7 ; LINES 3 ; PRINTS EQUAL (72) ; QUOTING LINES 0 (CONTROL FIRES)' in S['ep_cut'] \
        and (m.get('tags') or {}).get('v0.34.1') == 'e5fcda7' and gs('D:/SIDE-explicit-formula', 'rev-parse', '--short=7', 'v0.34^{commit}') == '8fbc27b'


def triage_ok(S):
    import b691_record as REC
    rows = S['triagej'].get('rows') or []
    try:
        ds = [REC.read_triage_row(r) for r in rows]
    except Exception:
        return False
    return len(rows) == 35 and len(set(n for n, _d in ds)) == 35 and 'EVERY TRIGGER AND GROUND STANDING AT ITS LINE ; NO LEDGER WRITTEN' in S['triage_t'] \
        and S['files']['triage'] and not [f for f in S['files']['triage'] if not f.startswith(('data/b691_orders_triage', 'tools/b691_record.py'))]


def arms_added_ok(S):
    a = S['added_t']
    return all(re.search(r'^  %s\s+\| LIVE PASS .*\| NEG PASS \| POS FIRES$' % re.escape(n), a, re.M) for n in K.STANDING_ADDED) \
        and 'THE CONTROL FIRES' in a and 'ARMS ADDED 4 ; EACH LIVE, NEG AND POS AS WANTED True' in a and set(K.STANDING_ADDED) <= set(RA.NAMES) \
        and S['lock_epoch'] is not None and bool(S['t'].get('arms')) and S['t']['arms'] < S['lock_epoch'] and 'tools/rule_arms.py' in S['files']['arms']


def sort_first_ok(S):
    return S['ostate'].get('sort') is True and 'RULES 4 ; TRACEABLE 4 (LIVE 4) ; PROSE 0 ; ARMS ADMITTED 4' in S['sort_t']


def repairs_ok(S):
    return ('### ### **REPAIRS 8 ; THE SEALED COPIES AGREE ; TOOLS CARRIED 8 OF 8 ; THE STANDING INSTRUMENTS UNEDITED True ; THE REPAIRED SHARED '
            'TOOLS 3, EACH ITS DIFF BANKED') in S['repairs'] and '### ROW 3 -- tools/rule_arms.py' in S['repairs']


def parts_ok(S):
    return all(re.search(r'PART %s : ARMS \d+ ; \d+ s' % p, S['prerun']) for p in K.PARTS)


def arm_seconds_ok(S):
    j = S['asec']
    return bool(j) and j.get('clocked') == j.get('standing') == len(STANDING) and not j.get('missing') and len(j.get('slowest') or []) == 3 \
        and 'THE THREE SLOWEST' in S['asect'] and all((j.get('run_secs') or {}).get(p) for p in K.PARTS)


def defects_ok(S):
    """the defects bank's letters read at HEAD, the sealed letters its prefix, every owner the seat or the navigator."""
    letters = re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", S['defects'], re.M)
    fl = list(FLOORS['defects'])
    return letters[:len(fl)] == fl and [x for x, _o in letters] == list('abcdefghijklmnopqrstuvwxyz'[:len(letters)]) \
        and all(o in ('SEAT', 'NAVIGATOR') for _x, o in letters)


# ================================================================== THE RUNNER (the standing arms, this act's two runs and merges)
IDENT_WF = ('secrets.', 'psinary', 'seale', 'york', 'hotmail', 'orcid', '0009-0008')


def wf_ok(S):
    """b688's reading, carried: each merged kernel read in its own dependency form -- the lake path and the cache step where a lakefile
    requires Mathlib, the plain-lean path where there is no lakefile."""
    for k, v in S['wf'].items():
        t = v['text'].lower()
        if not v['text'] or v['text'] != v['before']:
            return False
        if any(w in t for w in IDENT_WF):
            return False
        if 'workflow_dispatch' not in t or 'hold_mb: "2560"' not in t or 'print_targets.txt' not in t:
            return False
        if v['lakefile']:
            if 'lake env lean out/axioms.lean' not in t or (('lake exe cache get' in t) != v['mathlib']):
                return False
        elif 'lean_path=build lean out/axioms.lean' not in t or 'lake build' in t or 'lake env' in t:
            return False
        if len(v['targets']) != v['printed'] or v['act_writes'] != v['want']:
            return False
    return sorted(S['wf']) == sorted(k for k, *_r in MERGES)


def runner_ok(S):
    """this act's four runs through its record tool's reader: each before run at the main the merge sits on, each after run at the built tip,
    success, the artifact's sha256, the memory low above the hold."""
    import b691_record as REC
    rows = S['runner'].get('rows') or []
    want = {}
    for k, pre, tip, *_r in MERGES:
        want[(k, 'before')] = gs('D:/' + k, 'rev-parse', pre)
        want[(k, 'after')] = gs('D:/' + k, 'rev-parse', tip)
    try:
        for r in rows:
            REC.read_runner_row(r)
    except Exception:
        return False
    return len(rows) == 4 and sorted((r['kernel'], r['label']) for r in rows) == sorted(want) \
        and all(r['ref'] == want.get((r['kernel'], r['label'])) for r in rows) \
        and all(r['conclusion'] == 'success' and r['artifact_sha256'] and r['mem_low'] is not None and r['mem_low'] >= K.HOLD and not r['stopped']
                for r in rows)


def gate_ok(S):
    bs = S['rbanks']
    return len(bs) == 4 and all('GATE DERIVES' in t and 'BUILD EXIT 0 ; ERROR LINES 0' in t and 'SORRYAX 0' in t
                                and re.search(r'^### the artifact: .* ; AGREE$', t, re.M) for t in bs.values())


def merges_ok(S):
    for k, m in S['merges'].items():
        pre, tip, merge, tag = m['want']
        if m['main'] != merge or m['parents'] != [pre, tip] or m['tree_main'] != m['tree_built'] or m['tags'].get(tag) != merge:
            return False
    return len(S['merges']) == 2


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


POST_SEAL = ('b691 seal', 'b691 pre-root', 'b691 root', 'b691 record', 'b691 --', 'b691 closing', 'b691 entry')


def _component_commit(s):
    return s.startswith('b691') and not s.startswith(POST_SEAL)


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
    return bool(j) and len(rows) == 68 and rows[67][:3] == ['b691', j.get('root'), j0.get('root')] \
        and AR.root_of(items, j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) \
        and not [it for it in items if 'b628_intake_crank' in it or 'b647_navigator_memory' in it or 'b692_' in it or 'mirror' in it
                 or it.split()[0].endswith(('.gz', '.png', '.jsonl'))] \
        and any(it.startswith('data/b691_behind.txt ') for it in items) and any(it.startswith('data/b691_orders_triage.txt ') for it in items) \
        and all(any(it.startswith(p + ' ') for it in items) for p in K.SHARED_APPENDED) and (j.get('commit') or {}).get('relay')


def root_banks_committed_ok(S):
    """G-ROOT-BANKS-COMMITTED (standing from (R291)(4)): the root route's reading before the root -- every named bank clean and equal at HEAD,
    HEAD the remote main -- and every data/ bank the root names carried by the commit the root records, its blob there hashing to the hash
    the root recorded."""
    rb, rows = S['rootbanks'], S['root_at_commit']
    commit = (S['arj'].get('commit') or {}).get('relay') or ''
    return bool(rb) and rb.get('clean') is True and rb.get('pushed') is True and rb.get('head') == commit and bool(rows) \
        and all(c and e for _b, c, e in rows) and sorted(b for b, _c, _e in rows) == sorted(r['bank'] for r in rb.get('rows') or [])


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b691_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    v = S['ar_verify'] or []
    r = S['ar_reads'].get('b691') or {}
    return [x[0] for x in v] == ['b%d' % i for i in range(624, 692)] and all(x[1] == 'AGREE' for x in v) and r.get('crlf') == 0 \
        and (S['ar_reads'].get('b680') or {}).get('corrected') == 4


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**The citation check**', '**The re-cut**', '**The generator**', '**The behind count**', '**EpsteinQ0**', '**The orders**',
                 '**The arms**', '**The scores.**', '**Read in mutual light**', 'strengthens', '**Carried to:**', '**Next.**', 'b692')


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
    import b691_record as REC
    v = S['sc'].get(k)
    try:
        _k, w, _t = REC.read_score_row(k, v)
    except Exception:
        return False
    return w.split(' ')[0].split(',')[0] in ('HELD', 'REFUTED', 'NOT', 'HOLDS', 'PENDING') and ('(%s)' % k) in S['desk']


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
    """b691's reading: PLACE-papers' changed files against the two ledgers and the two pages the generator wrote on the author's word."""
    return S['pp_changed'] == S['pp_allowed']


def closing_sentence_ok(S):
    t = S['closing_src']
    return ('no identifier of the author ' + 'in any outbound') in t and ('plain requests to ' + 'github.com') in t \
        and '### THE CITATION CHECK' in t and '### THE RECORD LINES' in t and '### THE DRY RUN' in t and '### THE RE-CUT' in t \
        and '### THE GENERATOR' in t and '### THE KERNELS' in t and '### THE MIRROR' in t and '### THE CARRY-TIME' in t


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


def _first_wf(d):
    return d[sorted(d)[0]]


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R301) END' in S['ferry'] and S['ferry'].rstrip().endswith(K.TAIL),
     lambda S: put(S, 'ferry', S['ferry'].replace(K.TAIL, ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the step-zero bank: tail, lean, lake, python and claude named, the seat`s claude alone, none of the others; no task stopped, no orphan, nothing stopped by PID',
     lambda S: procs_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('python 0', 'python 1'))),
    ('G-STEPZERO-TESTS', 'the runner bank against the test files tracked before the act, test_elab_reader_b634.py withheld (no lean on this host), run against the list the page named',
     lambda S: tests_ok(S), lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: 'data/b690_closing_push_out.txt' in S['pushout'][0] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'the two repositories` local branch lists by the ruling`s names and the branches bank (the ruling`s list alone)',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{'D:/relay': 'push-b690'}))),
    ('G-READFIRST-CITED', 'the read-first bank: every item of the ferry`s list cited by path and line', lambda S: readfirst_ok(S),
     lambda S: put(S, 'readfirst', '')),
    ('G-ANSWERS-BANKED', 'the answers bank read at HEAD: its prompts and calls at or above the sealed floors, each with its options and result, any call after the lock named on the face',
     lambda S: answers_ok(S), lambda S: put(S, 'answers', S['answers'].replace('### PROMPT 1 (', '### PROMPTED ('))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-EXPORT-UNTRACKED', 'the navigator`s export: present, untracked, in no commit', lambda S: S['export_present'] and S['export_log'] == ''
     and S['export_index'] == '' and S['export_status'].startswith('??'), lambda S: put(S, 'export_index', EXPORT)),
    ('G-EDIT-ROUTE', 'the record tool`s one reading (tools/edit_route.py`s arms and sed in any form) over this act`s whole capture and the previous act`s after its post-push suite in this same session, read live',
     lambda S: edit_route_ok(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -n 1p tools/b691_record.py")])),
    ('G-NO-LOCAL-LEAN', 'the act`s command capture, read live: no command runs lean or lake on this host (N1)', lambda S: no_local_lean(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd='LEAN_PATH=build lean Core/X.lean -o build/X.olean')])),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line, found by conv', lambda S: weight_ok(S), lambda S: _rl(S, 0, 1)),
    ('G-DRY-STEP-CLEAN', 'the gate`s record: the dry-run step run, the entry and the trail record quiet under their screens, CLEAN printed, the gate CLEAR',
     lambda S: dry_step_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE DRY-RUN STEP : CLEAN', 'THE DRY-RUN STEP : NOT CLEAN'))),
    ('G-CLOSING-DRY-STEP', 'the gate`s record: the closing run dry before the lock, its head line, citation line, re-cut, generator and kernels lines and tag rows printed (b675 rules row 1)',
     lambda S: closing_dry_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE CLOSING DRY-RUN STEP : CLEAN', 'THE CLOSING DRY-RUN STEP : NOT CLEAN'))),
    ('G-CITATION-CHECKED', 'the citation check`s bank (the gate step at step zero): no miss of the ruling or the ferry; every commit miss of a mid-act check tested directly and noted',
     lambda S: citation_ok(S), lambda S: put(S, 'citation', S['citation'].replace('CITES CHECKED 85 ; OK 85 ; MISSES 0', 'CITES CHECKED 85 ; OK 84 ; MISSES 1'))),
    ('G-R301-ENTERED', 'the ferry and the trail', lambda S: 'RULING (R301) END' in S['ferry'] and S['ot'].count('**(R301) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R301) ratified', '**(R3010) ratified'))),
    ('G-ROWGEN-STEPZERO', 'the rowgen bank: constellation and the build-free diff over the 19 roster tables, both exit 0 (b670 rules row 3)',
     lambda S: rowgen_ok(S), lambda S: put(S, 'rowgen', S['rowgen'].replace('ROWGEN DIFF EXIT 0', 'ROWGEN DIFF EXIT 1'))),
    ('G-BRANCHES-BANKED', 'the branches bank: five rows through the record tool`s reader, all local, each merged and deleted',
     lambda S: branches_banked_ok(S), lambda S: _mut(S, 'branchj', lambda d: d['rows'][0].update(fate='GONE'))),
    ('G-DELETES-ONE-BRANCH', 'the command capture by the record tool`s reader and the command bank: each branch delete naming one branch, no glob in any half, the ruling`s list exactly',
     lambda S: deletes_one_ok(S), lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="git branch -d push-b690 push-b690-root")])),
    ('G-ANSWERS-CHECKED', 'the citation bank`s mid-act prints read at HEAD, each before the write its answer governs: the generator`s run, the Epstein lines bank, the Epstein cut',
     lambda S: answers_checked_ok(S), lambda S: put(S, 't', dict(S['t'], gen_run=1))),
    ('G-SCORER-READS-BANKS', 'tools/b691_record.py`s code, prose stripped: the N2-N4 scorers reading banks and commits and no ledger, the scores bank written once, the entry`s scores line from it',
     lambda S: scorer_banks_ok(S), lambda S: put(S, 'rec_src', S['rec_src'].replace("def _n2():", "def _n2():\n    _x = rd(FIND)"))),
    ('G-ENTRY-SCORES-EQUAL', 'FINDINGS at the findings bank`s line and the scores bank: the entry`s scores line equal to the line composed from the bank',
     lambda S: entry_scores_ok(S), lambda S: _mut(S, 'sc', lambda d: d.update(N1=['REFUTED', 'planted']))),
    ('G-ENTRY-TITLE-FORM', 'FINDINGS at the findings bank`s line, the record tool`s title from the cut, generator, behind, Epstein, triage and arms banks, and the worklist`s: the ferry`s form adjusted',
     lambda S: entry_title_ok(S), lambda S: put(S, 'find', S['find'].replace(conv(K.TITLE), conv(K.TITLE).replace('2 pages regenerated', '2 pages held')))),
    ('G-TIE-BEFORE-NAMING', 'the tie bank and the commit times: b674`s rule and both tables` rows banked before SIDE-rcurve`s first write of the act, the bank naming the document by row (2) (N2)',
     lambda S: tie_ok(S), lambda S: _mut(S, 'ostate', lambda d: d.update(tie=False))),
    ('G-CUT-DISTANCE', 'the cut bank: SIDE-rcurve`s distance 2 to 0 by b670`s method, v0.1.1, the prints equal, the four README residues and the SIDE-kernel row`s residue entered (N3)',
     lambda S: cut_ok(S), lambda S: _mut(S, 'cutj', lambda d: d.update(after=1))),
    ('G-PRINTS-EQUAL', 'the two prints banks: SIDE-rcurve 8 and SIDE-explicit-formula 72 terminals, each equal line for line before and after (N3)',
     lambda S: prints_equal_ok(S), lambda S: put(S, 'prints_ef', S['prints_ef'].replace('DIFFERING 0', 'DIFFERING 1'))),
    ('G-QUOTE-HITS-PRINTED', 'the two quotation-search banks and the merges` times: each search before its merge with its hit count printed, the Epstein control firing (N3, data/b690_rules.txt row (2))',
     lambda S: quote_ok(S), lambda S: put(S, 'quote_ep', S['quote_ep'].replace('the control FIRES', 'the control DOES NOT FIRE'))),
    ('G-GEN-CARRIED-AT', 'the generator`s planted cases run live, the repairs bank`s rows 1-2, the test bank and the dry beside b688`s: the :302 cell at its carry 73cee42, out of the diff (N3)',
     lambda S: gen_carried_ok(S), lambda S: _planted(S, 'test_correspondence_gen.py')),
    ('G-BEHIND-BANKED', 'the behind bank: 57 rows read with the generator`s reading beside, the cause by line of each tool, the claim 1 before the write and 0 after, the withheld rows by line (N4)',
     lambda S: behind_ok(S), lambda S: _mut(S, 'behindj', lambda d: d.update(claim=0))),
    ('G-GEN-RUN-AFTER-WORD', 'the pages` commit against the answer`s time, its files, the snapshot and live banks and the two page diffs: the generator`s write alone, after the word (N4)',
     lambda S: gen_run_ok(S), lambda S: _mut(S, 'bstate', lambda d: d.update(after_word=False))),
    ('G-ORDER-ENTERED', 'OPEN_TRAILS at the order`s line by conv, its trigger and status, its commit the ledger alone',
     lambda S: order_ok(S), lambda S: put(S, 'ot', S['ot'].replace('Trigger: the next re-cut act after b691. Status OPEN.', 'Trigger: later.'))),
    ('G-EPSTEIN-LINES-BEFORE-BRANCH', 'the Epstein lines bank and the commit times: the three lines, the premises` status, the raise and the successor lines banked before the print-list commit and the cut (N2)',
     lambda S: epstein_lines_ok(S), lambda S: _mut(S, 'ostate', lambda d: d.update(epstein=False))),
    ('G-EPSTEIN-RECUT', 'the Epstein cut bank and SIDE-explicit-formula`s tags: the docstrings re-cut, v0.34.1 peeled to the merge, v0.34 unmoved, the prints equal, no quoting line',
     lambda S: epstein_recut_ok(S), lambda S: put(S, 'ep_cut', S['ep_cut'].replace('LINES 3 ;', 'LINES 4 ;'))),
    ('G-TRIAGE-BANKED', 'the triage bank through the record tool`s reader: thirty-five rows, each trigger and ground standing at its line, its commit writing no ledger',
     lambda S: triage_ok(S), lambda S: _mut(S, 'triagej', lambda d: d['rows'][0].update(disposition='KEEP'))),
    ('G-ARMS-ADDED-COUNTED', 'the arms-added bank and the commit times: the four arms LIVE, NEG and POS at HEAD, the defect control firing, committed before the lock (N5)',
     lambda S: arms_added_ok(S), lambda S: put(S, 'added_t', S['added_t'].replace('POS FIRES', 'POS PASSES'))),
    ('G-SORT-WORDS-FIRST', 'the sort bank: b683`s words printed before any rule is sorted, the four rules TRACEABLE (N2)',
     lambda S: sort_first_ok(S), lambda S: _mut(S, 'ostate', lambda d: d.update(sort=False))),
    ('G-TOOL-REPAIRS', 'the repairs bank`s verdict: eight carry-time repairs, the sealed copies agreeing, eight tools carried, the standing instruments unedited, the three repaired shared tools each with its diff banked',
     lambda S: repairs_ok(S), lambda S: put(S, 'repairs', S['repairs'].replace('REPAIRS 8 ;', 'REPAIRS 0 ;'))),
    ('G-PARTS-PRERUN', '(R301)(8) and the pre-run bank`s five parts with their seconds',
     lambda S: parts_ok(S), lambda S: put(S, 'prerun', S['prerun'].replace('PART standing-b2', 'PART standing-x'))),
    ('G-ARM-SECONDS-BANKED', 'the per-arm seconds bank: every standing arm clocked at the pre-run, the three slowest named, each part`s seconds',
     lambda S: arm_seconds_ok(S), lambda S: _mut(S, 'asec', lambda d: d.update(clocked=0))),
    ('G-DEFECTS-LETTERED', 'the defects bank read at HEAD: the sealed letters its prefix, consecutive letters, owners the seat or the navigator',
     lambda S: defects_ok(S), lambda S: put(S, 'defects', S['defects'].replace("(a) THE SEAT'S", "(a) THE AUTHOR'S"))),
    ('G-SPEC-PLANTED', 'tools/b691_regspec.py`s planted rows run live through the record tool`s readers, and rows of another shape refused',
     lambda S: bool(S['spec']['read']) and all(S['spec']['read']) and all(S['spec']['controls']) and any('branch' in x for x in S['spec']['shapes']),
     lambda S: _mut(S, 'spec', lambda d: d['controls'].append(False))),
    ('G-CONVERSION-ONE', 'every b691 tool`s code and the repaired shared tools`: no conversion defined (conv imported from b652_record); the suite importing it',
     lambda S: S['conv_bad'] == [] and 'from b691_record import conv' in S['suite'], lambda S: put(S, 'conv_bad', ['b691_checks.py'])),
    ('G-WORKFLOW-FILES', 'every kernel this act merged, its main: the workflow unchanged since its own commit, no author identifier, no secret, the hold, the build path its dependency form takes, the print step over its list, the files the act wrote',
     lambda S: wf_ok(S), lambda S: _mut(S, 'wf', lambda d: _first_wf(d).update(text=_first_wf(d)['text'] + ' secrets.X'))),
    ('G-RUNNER-READ', 'this act`s four runs through its record tool`s reader: each before run at the main its merge sits on, each after run at the built tip, success, the artifact`s sha256, the memory low above the hold',
     lambda S: runner_ok(S), lambda S: _mut(S, 'runner', lambda d: [r.update(mem_low=2000) for r in d['rows']])),
    ('G-RUNNER-GATE', 'this act`s four runs` gate readings: build exit 0, no error line, no sorryAx, the artifact`s digest agreeing',
     lambda S: gate_ok(S), lambda S: put(S, 'rbanks', dict(S['rbanks'], **{'x_after': 'GATE NOT DERIVES'}))),
    ('G-MERGES-ON-GATE', 'SIDE-rcurve`s and SIDE-explicit-formula`s mains: each merge commit of the built tip, the merged tree the built tree, v0.1.1 and v0.34.1 peeled to them',
     lambda S: merges_ok(S), lambda S: _mut(S, 'merges', lambda d: d['SIDE-explicit-formula']['tags'].clear())),
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
    ('G-PP-SCOPE', 'PLACE-papers` changed files against FINDINGS, OPEN_TRAILS and the two pages the generator wrote on the author`s word',
     lambda S: corpus_scope(S), lambda S: put(S, 'pp_changed', S['pp_changed'] + ['day1/ONE_PAGE_PROOF.md'])),
    ('G-CURRENTS-UNEDITED', 'the map, the census, the monograph, the faces page, the Dirichlet page, the surround, SIMPLICITY, README, REGISTRY, FOUNDATIONS and its one-copy partner: working tree, before and HEAD',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'ERRATA.md': (b'x', b'y', b'y')}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read before the seal',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b690`s and the earlier tools, b672`s record tool, act_root.py, rowgen`s, edit_route.py, chain_page.py, e0_rule.py, the mirror`s, repair_snapshot.py, the instruments and the shared tools -- the three repaired shared tools apart: before, working tree and HEAD',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'additive_shared.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 9fc2c81b but the shared additive files (act_roots.txt among them), by blob id',
     lambda S: S['prior_bad'] == [] and S['prior_n'] > 0, lambda S: put(S, 'prior_bad', ['data/b690_stepzero.txt'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS before and now', lambda S: S['fi_pre'] is not None and (S['fi_now'] or b'').startswith(S['fi_pre']),
     lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS before and now', lambda S: S['ot_pre'] is not None and (S['ot_now'] or b'').startswith(S['ot_pre']),
     lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-NODISCLOSURE-PUBLIC', 'TECHNE-Core`s needle sets over every public byte the act writes: the ledger lines, the banks and the tools',
     lambda S: bool(S['nd_pub']) and not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', {'method': 1})),
    ('G-OUTSIDE-NAMED-NOWHERE', 'the ledger lines appended', lambda S: S['outside'] == [], lambda S: put(S, 'outside', ['x'])),
    ('G-DELETE-FREE', 'the act`s tools` code and the repaired shared tools`, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='os' + '.remove(p)'))),
    ('G-PUBLISH-UNCALLED', 'the act`s tools` code: no publish call', lambda S: publish_uncalled(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='z_' + 'publish()'))),
    ('G-SEALED-AFTER-COMPONENTS', 'the lock time against every relay and PLACE-papers commit of the act by its subject', lambda S: sealed_after_ok(S),
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b691 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'b691_record.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3), in five parts summed',
     lambda S: S['lock_epoch'] is not None and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b690`s trail record on OPEN_TRAILS and its root in the chain', lambda S: '### b690 — lane two, act one hundred and seventeen, the reading act' in S['ot']
     and S['rootsf'].count(NL + 'b690 ') == 1, lambda S: put(S, 'ot', S['ot'].replace('### b690 — lane two', '### b690 - lane two'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], grade_moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 68th chain row (the corrigendum row apart), the root bank and its items, the behind and triage banks among them, no binary, mirror or untracked bank',
     lambda S: root_banked_ok(S), lambda S: put(S, 'rootsf', S['rootsf'] + 'b692 x y' + NL)),
    ('G-ROOT-BANKS-COMMITTED', 'the root route`s banked reading and every named bank`s blob at the root`s recorded commit: clean and equal at HEAD, HEAD the remote main, the recorded hash carried by the recorded commit',
     lambda S: root_banks_committed_ok(S), lambda S: put(S, 'rootbanks', dict(S['rootbanks'], pushed=False))),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit with the suite`s own remote reads: b624 to b691 AGREE, b680 read through its corrigendum row (4 banks), b691 written LF',
     lambda S: verify_ok(S), lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s through conv, and its parts', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line, the head through conv', lambda S: bool(S['tj'].get('line'))
     and oline(S, S['tj']['line']) == conv(S['REC'].TRAIL_HEAD()), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b691 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b691_record.py agree', 'b691_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line: b692', lambda S: '**Next:** b692' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** b692', '**Next:** b693'))),
] + [('G-N%d-SCORED' % i, 'the scores through the record tool`s reader, and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i),
      lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written since 9fc2c81b and 64936ae against the (W) globs',
     lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b691')" in S['suite'] and "'data/b691_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b691_closing.py: the closing sentence in the rule`s words with the plain reads named; the citation check, the record lines, the dry run, the re-cut, the generator, the kernels, the mirror, the carry-time reading',
     lambda S: closing_sentence_ok(S), lambda S: put(S, 'closing_src', S['closing_src'].replace('no identifier of the author ' + 'in any outbound', 'x'))),
    ('G-LSREMOTE-ONE-PER-REPO', 'the part`s ls-remote calls per repository, read after every other arm of the part has run (OPEN_TRAILS :12703)',
     lambda S: lsr_ok(S), lambda S: put(S, 'lsr', {PP: 2})),
] + [(nm, 'tools/rule_arms.py (the author`s word on (R293)(6); (R301)(6) for the four added) -- ' + reads, (lambda p: lambda S: p(S['ra']))(pred),
      (lambda pl: lambda S: put(S, 'ra', pl(S['ra'])))(plant)) for nm, reads, pred, plant in RA.ARMS]


def _part_of(name):
    if name in K.ACT_ARMS:
        return 'act'
    if name in B1_ARMS:
        return 'standing-b1'
    if name in B2_ARMS:
        return 'standing-b2'
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
    p = os.path.join(D, 'b691_seal_hashes.json')
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
        print('  %-38s %s' % (t, now[t]))
    print('  written: b691_seal_hashes.json')
    return 0


def _base_name(pushed):
    if PRERUN:
        return 'b691_arms_prerun.txt'
    if MID and len(sys.argv) > sys.argv.index('--mid') + 1:
        return sys.argv[sys.argv.index('--mid') + 1]
    if RERUN and len(sys.argv) > sys.argv.index('--rerun-postpush') + 1:
        return sys.argv[sys.argv.index('--rerun-postpush') + 1]
    return 'b691_checks_postpush.txt' if pushed else 'b691_checks.txt'


def _part_name(base, part):
    return base.replace('.txt', '_%s.txt' % part)


def _write(name, lines):
    out = os.path.join(D, name)
    b = (NL.join(lines) + NL).encode('utf-8')
    open(out + '.tmp', 'wb').write(b)
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
    out = ['=' * 104, heads[0].replace('PART standing-a', 'FIVE PARTS SUMMED ((R301)(8))'), '=' * 104] + [
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
        ex.update(jl('b691_exercise_%s.json' % part).get('exercise') or {})
    if ex and base in ('b691_checks.txt', 'b691_checks_postpush.txt'):
        e = (json.dumps(dict(exercise=ex, run=n, live_failing=fails, defective=defs, neg_failures=ng), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p_ = os.path.join(D, 'b691_exercise.json')
        open(p_ + '.tmp', 'wb').write(e)
        os.replace(p_ + '.tmp', p_)
    print(NL.join(out[3:13]))
    print('  written: %s' % base)
    return 0 if ok else 1


def main():
    if SEAL:
        return seal()
    if COMBINE:
        return combine()
    if PART not in K.PARTS:
        print('### (R301)(8): every run in five foreground parts -- give `--part %s`' % ' | '.join(K.PARTS))
        return 2
    fm = free_mb()
    if fm < K.HOLD:
        print('%s  ### THE HOST`S FREE MEMORY %d MB, BENEATH THE HOLD %d MB: PART %s NOT RUN ((R294)(2))' % (
            time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), fm, K.HOLD, PART))
        return 3
    t_start = time.time()
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b691 -- THE SUITE. ### **%s READING.** ### PART %s ((R301)(8)) ### every arm exercised on both controls.' % (
        'PRE-SEAL (R202)(3)' if PRERUN else 'MID-ACT' if MID else 'POST-PUSH' if pushed else 'PRE-PUSH', PART))
    rec('### the host`s free memory at the part`s start %d MB (the hold %d MB)' % (fm, K.HOLD))
    if PRERUN or MID:
        rec('### run at (UTC) : %s   ### %s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                                              'the standing line of (R202)(3): every arm run at HEAD before the face is sealed, its count printed.'
                                              if PRERUN else 'a mid-act re-run; no table regenerated.'))
    rec('=' * 104)
    S = sources(NEED[PART])
    S['pushed'] = pushed
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
    rec('  ### (R264)(2) THE FREEZE AND (R301)(6): the standing arms (b690`s face less its own arms, the twenty rule arms among them, and the four '
        'added) %d ; carried here %d ; added %s ; the act`s arms over its own banks %s ; arms beyond both %s' % (
            len(S['standing']), len(set(names) & set(S['standing'])), list(K.STANDING_ADDED) or 'NONE', sorted(set(names) - set(S['standing'])),
            sorted(set(names) - set(S['standing']) - set(K.ACT_ARMS)) or 'NONE'))
    rec('  ### standing arms not carried here: %s' % (sorted(set(S['standing']) - set(names)) or 'NONE'))
    if 'rules' in NEED[PART]:
        rec('  ### THE RULE ARMS, EACH WITH ITS COUNT (tools/rule_arms.py; rows read, rows failing, the reading):')
        for nm in RA.NAMES:
            ok_, n_, b_, note = RA.reading(nm, S['ra'])
            rec('  ###   %-28s %-4s read %d ; failing %d ; %s' % (nm, 'PASS' if ok_ else 'FAIL', n_, b_, note[:260]))
    if 'chain' in NEED[PART]:
        av = S['ar_verify']
        rec('  ### THE ACT-ROOT CHAIN, recomputed: %s' % ('; '.join('%s %s%s' % (a, v, (' (' + '; '.join(w) + ')') if w else '') for a, v, w in av) or 'no act rooted'))
        rec('  ### the reads at commit, b680: %s ; b691: %s' % (S['ar_reads'].get('b680'), S['ar_reads'].get('b691')))
    sj = S['sealj'].get('tools') or {}
    rec('  ### THE SEALED TOOLS, recorded at the seal %s : %s' % (S['sealj'].get('at', '### NOT RECORDED'), '; '.join(
        '%s %s' % (t, ('agree' if sj.get(t) == S['sealnow'].get(t) else 'DIFFER') if t in sj else 'not recorded') for t in K.SEALED)))
    off = S['REC'].edit_route_offences(S['cmds'] + S['prev_cmds'])
    rec('  ### G-EDIT-ROUTE read %d captured commands of this act and %d of the previous act after its post-push suite (this same session); offences %d: %s' % (
        len(S['cmds']), len(S['prev_cmds']), len(off), ['#%s %s' % (r['n'], [k for k, _ in o]) for r, o in off] or 'none'))
    mc = re.search(r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', S['citation'])
    rec('  ### THE CITATION CHECK: %s ; THE ORDER OF THE READS: %s ; THE CUT: %s ; THE BEHIND COUNT: %s' % (
        mc.group(0) if mc else '### NOT READ', S['ostate'], dict((k, v) for k, v in S['cutstate'].items() if k != 'quotes'), S['bstate']))
    rec('  ### PLACE-papers` changed files %d against the allowed %d (the two ledgers and the two generator pages): beyond %s' % (
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
        ta = time.time()      # ### (R300)(3), carried: the arm's three readings clocked
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
    rec('  ### the arms` own seconds summed %.1f, the slowest %s' % (sum(SECS.values()), ', '.join('%s %.2f' % kv for kv in sorted(SECS.items(), key=lambda x: -x[1])[:3])))
    rec('  ### the run took %.0f s' % secs)
    rec('  ### PART %s : ARMS %d ; LIVE PASSING %d ; LIVE FAILING %d %s ; NEGATIVE-CONTROL FAILURES %d ; POSITIVE-CONTROL PASSES %d %s ; '
        'DECLARED EQ RUN %s ; %d s' % (PART, len(arms), len(arms) - len(fail), len(fail), json.dumps(fail) if fail else 'NONE', negfail, len(defective),
                                       json.dumps(defective) if defective else 'NONE', S['declared_eq_run'], int(secs)))
    rec('=' * 104)
    base = _base_name(pushed)
    out = _write(_part_name(base, PART), L)
    lp = os.path.join(D, _part_name(base, PART).replace('b691_arms_prerun', 'b691_lsr_prerun').replace('b691_checks', 'b691_lsr').replace('.txt', '.json'))
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if PRERUN:
        sb = (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), part=PART, arms=SECS,
                              phases=dict((k, round(v, 1)) for k, v in S['phase_secs'].items()), run_secs=round(secs, 1)),
                         indent=1, ensure_ascii=False) + NL).encode('utf-8')
        sp = os.path.join(D, 'b691_arm_seconds_%s.json' % PART)
        open(sp + '.tmp', 'wb').write(sb)
        os.replace(sp + '.tmp', sp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(arms), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b691_exercise_%s.json' % PART)
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if (not fail and not defective and negfail == 0 and S['declared_eq_run']) else 1


if __name__ == '__main__':
    sys.exit(main())
