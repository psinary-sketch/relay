# -*- coding: utf-8 -*-
"""b689_checks.py -- THE SUITE OF b689, UNDER (R299): b688 AT ITS WEIGHT; DEFECT (f) REPAIRED BY CORRIGENDUM; THE HEAD-LINE ARM REPAIRED; THE
STRIP-FREE LI CONVERSE PLANNED FROM ITS BANKS, RAISED, AND BUILT ON A BRANCH (SIDE-explicit-formula v0.34).

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### data/b684_rules.txt row (1) and data/b685_rules.txt row (1), standing: every run in FOUR foreground parts, each its own call in its own
### message -- `--part standing-a`, `--part standing-c` (G-PRIORBANK-UNCHANGED, G-NODISCLOSURE-PUBLIC, G-WRITELIST-KINDS), `--part standing-b`
### (the act-root chain and the shared additive files) and `--part act` (the act's arms over this act's banks, the table regenerated in a
### closing run) -- each under the 590 s guard the seat runs it in, and NOT RUN beneath the 2,560 MB hold; `--combine <bank>` writes the bank.
### ### (R264)(2), THE FREEZE: the standing arms are b688's face's (G2) arms less b688's own arms over b688's banks, carried -- the twenty rule
### arms of tools/rule_arms.py among them, G-RULE-HEAD-LINE-QUOTED in the author's form ((R299)(2)); NO STANDING ARM ADDED ((R299)'s N5). The
### act's own arms read this act's banks alone (ACT_ARMS). The standing runner arms read this act's run and merge, SIDE-explicit-formula's
### (tools/b689_worklist.py MERGES).
### ### The carry-time repairs (relay data/b689_tool_repairs.txt): rule_arms.py sealed with the act and out of INST; the faces page back in
### CURRENTS; the branches arm on the local lists of four repositories; the step-zero tests' set with the re-run against the page's list;
### the previous act's window in its own session (the record tool).
### ### Every look-up of a landed line goes through the one conversion (imported from tools/b652_record.py through tools/b689_record.py).
### ### The harness is b568's to b688's, written by the Write tool from tools/b688_checks.py; the sources, predicates and arms over this act's
### ### banks are b689's. data/b686_rules.txt row (1): the act arm G-ENTRY-SCORES-EQUAL reads the landed entry; no scorer reads a ledger line.
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
import b689_worklist as K     # noqa: E402
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
from b689_record import conv  # noqa: E402

NL = chr(10)
PP = K.PP
FACE = os.path.join(D, 'b689_registration_2026-10-19.txt')
B688_FACE = os.path.join(D, 'b688_registration_2026-10-19.txt')
B688_ACT_ARMS = K688.ACT_ARMS
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
FLOORS = dict(prompts=2, calls=2, checks=2, defects=(('a', 'SEAT'), ('b', 'SEAT'), ('c', 'NAVIGATOR')))
REPAIRED_TOOLS = K.REPAIRED_TOOLS                      # ### (R299)(2): tools/rule_arms.py, sealed with the act
INST = tuple(t for t in K688.SEALED) + tuple(t for t in K687.SEALED) + ('b687_readings.py',) + tuple(t for t in K686.SEALED) + \
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
        'test_act_root_commit_b644.py', 'test_act_root_order_b641.py', 'act_root.py', 'rule_arms.py',
        'b670_record.py', 'b672_record.py', 'rowgen/rowgen.py', 'rowgen/diff_rowpin.py', 'rowgen/namemap.json')
INST = tuple(sorted(set(INST) - set(K.SEALED) - set(REPAIRED_TOOLS)))
# ### b689's repair (relay data/b689_tool_repairs.txt REPAIR 4): THE_CLAUSE_AND_ITS_COMPILED_FACES.md back in CURRENTS -- (R299)(5) leaves the
# ### page untouched; G-PP-SCOPE allows FINDINGS and OPEN_TRAILS alone.
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md',
            'phase2/method/THE_KEYSTONE_CENSUS_v0_8.md', 'day1/A_Place_to_Stand_v5_18.md',
            'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md', 'day1/ONE_PAGE_PROOF.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md',
            'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', 'README.md', 'REGISTRY.md',
            'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md', 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md',
            'THE_CLAUSE_AND_ITS_COMPILED_FACES.md')
TABLE_FILES = K.TABLE_FILES
WF, PT = '.github/workflows/build-module.yml', 'print_targets.txt'
MERGES = K.MERGES
KERN = 'D:/SIDE-explicit-formula'
B_ARMS = ('G-ACTROOT-VERIFY', 'G-SHARED-ADDITIVE')        # ### standing-b's arms: the act-root chain and the shared additive files
C_ARMS = ('G-PRIORBANK-UNCHANGED', 'G-NODISCLOSURE-PUBLIC', 'G-WRITELIST-KINDS')   # ### standing-c's arms: the written files
NEED = {'standing-a': ('live', 'rules'), 'standing-c': ('written',), 'standing-b': ('chain', 'additive'), 'act': ()}
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
FACES_PAGE = K.FACES_PAGE
STD3 = ('Classical.choice', 'Quot.sound', 'propext')
W = 'SIDEExplicitFormula.Schema.Wide.'


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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b689')
            and 'data/b689_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    import b689_record as REC
    return REC.capture()


def prev_now():
    import b689_record as REC
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
        if (f.startswith('b689_') and f.endswith('.py')) or f in REPAIRED_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks):
                bad.append(f)
    return bad


def spec_planted():
    import b689_regspec as SPEC
    P = SPEC.planted()
    ctl = [ok for _w, ok in SPEC.controls()]
    return dict(read=[ok for _s, ok, _w in P], controls=ctl, shapes=[s for s, _o, _w in P])


def _deps(ax):
    import b689_record as REC
    return REC._deps(ax)


def _prints_count(k):
    return len(_deps(rd(K.RUNNER_BANK)))


def wf_state():
    """b688's reading, carried: every kernel the act merged, its workflow at main against the workflow at its own first commit, its dependency
    form read from its tree (a lakefile requiring Mathlib, or no lakefile), its print list against the act's print bank for it, and the files
    the act wrote on main since the main before the act."""
    out = {}
    for k, _pre, _tip, _merge, _tag, before, files in MERGES:
        td = 'D:/' + k
        t = read_blob(td, 'main:' + WF)
        first = (gs(td, 'log', '--diff-filter=A', '--format=%h', '--', WF).split() or [''])[-1]
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


STANDING = sorted(set(g2_of(B688_FACE)) - set(B688_ACT_ARMS))
TESTS = ('test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py', 'test_correspondence_gen.py')


def _ct(repo, rev):
    t = gs(repo, 'log', '-1', '--format=%ct', rev)
    return int(t) if t.isdigit() else None


def _tag_ct(repo, tag):
    t = gs(repo, 'for-each-ref', '--format=%(taggerdate:unix)', 'refs/tags/' + tag)
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


def _arm_reading():
    """(R299)(2): the arm G-RULE-HEAD-LINE-QUOTED read through tools/rule_arms.py's own reading against b688's ferry bank and this act's, and
    its planted case over each: [(act, ok, planted fires)]."""
    import b689_record as REC
    out = []
    for act in ('b688', 'b689'):
        R = REC._arm_inputs(act)
        ok = RA.reading('G-RULE-HEAD-LINE-QUOTED', R)[0]
        pok = RA.reading('G-RULE-HEAD-LINE-QUOTED', dict(R, prev_head=R['prev_head'] + ' planted'))[0]
        out.append((act, bool(ok), not pok))
    return out


def sources(need=()):
    """the sources the arms read; `need` (by part, data/b684_rules.txt row (1)) names the heavy phases this part computes: 'live' (the three
    arms at HEAD), 'rules' (the rule arms' trace), 'written' (the written files, the public bytes, the prior banks), 'chain' (the act-root
    chain), 'additive' (the shared files)."""
    import b689_record as REC
    import b616_record as R6
    import edit_route as ER
    import b641_record as R41
    import additive_shared as ADD
    face = read(FACE)
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b689_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if (f.startswith('b689_') and f.endswith('.py')) or f in REPAIRED_TOOLS)
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    cit = jl('b689_citation_check.json')
    t0 = time.time()
    S = dict(
        REC=REC, ER=ER, face=face, ferry=rd('b689_ferry.txt'), scan=rd('b689_ferry_scan.txt'), stepz=rd('b689_stepzero.txt'),
        readfirst=rd('b689_readfirst.txt'), defects=rd('b689_defects.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        answers=rd('b689_author_answers.txt'), answersj=jl('b689_author_answers.json'), prerun=rd('b689_arms_prerun.txt'), rl=jl('b689_record_lines.json'),
        tests=jl('b689_tests_stepzero.json'), testst=rd('b689_tests_stepzero.txt'), tests2=jl('b689_tests_b688list.json'), withheld=jl('b689_tests_withheld.json'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b689_seal_hashes.json'), sealnow=sealed_now(), cmds=capture_now(), prev_cmds=prev_now(), cmdj=jl('b689_commands.json'),
        cmdt=rd('b689_commands.txt'),
        planted={t: run_test(t) for t in TESTS}, spec=spec_planted(), conv_bad=conv_alone(), suite=read(os.path.join(T, 'b689_checks.py')),
        citation=rd(K.CITATION_BANK), cit_at=iso_epoch(cit.get('at') or ''), cit_misses=cit.get('misses') or [],
        gate=rd('b689_reg_gate.txt'), rowgen=rd('b689_rowgen_stepzero.txt'),
        branchj=jl('b689_branches.json'), branchest=rd('b689_branches.txt'),
        branch_lists=dict((repo, gs(repo, 'branch', '--list', *bs)) for repo, bs in K.DELETE),
        repairs=rd('b689_tool_repairs.txt'), rec_src=read(os.path.join(T, 'b689_record.py')),
        corr=rd('b689_corrigendum.txt'), corrl=jl('b689_corrigendum_landing.json'), armread=_arm_reading(),
        ra_src=read(os.path.join(T, 'rule_arms.py')),
        plan=rd('b689_plan.txt'), s11=REC._section11_state(), sfw=REC._strip_free_write_ts(),
        landing=rd('b689_landing.txt'), grade=rd('b689_grade.txt'), gradestate=REC._grade_state(), axioms=dict(_deps(rd(K.RUNNER_BANK))),
        main_src=read_blob(KERN, 'main:' + REC.MAIN_FILE), obstruction=os.path.exists(os.path.join(D, 'b689_obstruction.txt')),
        constants=rd('b689_constants.txt'), q0=rd('b689_q0_reread.txt'), faces_rows=rd('b689_faces_rows.txt'),
        nodes=rd(os.path.basename(K.NODES)),
        shared=dict((p, (cr0(blob(ROOT, '%s:%s' % (PRE['relay'], p))), cr0(raw(os.path.join(ROOT, *p.split('/')))), cr0(blob(ROOT, 'HEAD:' + p))))
                    for p in K.SHARED_APPENDED),
        t=dict(arm=_ct(ROOT, K.ARM_COMMIT), s11=_ct(ROOT, K.SECTION11_COMMIT), plan=_ct(ROOT, K.PLAN_COMMIT), grade=_ct(ROOT, K.GRADE_COMMIT),
               branch=_ct(KERN, K.BRANCH_FIRST), merge=_ct(KERN, K.MERGE_COMMIT), c1=_ct(PP, K.C1_PP)),
        standing=STANDING, wf=wf_state(), runner=jl('b689_runner_rows.json'),
        rbanks=dict(('%s_%s' % (r.get('kernel'), r.get('label')), rd('b689_runner_%s_%s.txt' % (r.get('kernel'), r.get('label'))))
                    for r in jl('b689_runner_rows.json').get('rows') or []),
        merges=merges_state(),
        export_present=os.path.exists(os.path.join(ROOT, *EXPORT.split('/'))), export_log=gs(ROOT, 'log', '--all', '--format=%h', '--', EXPORT),
        export_index=gs(ROOT, 'ls-files', '--', EXPORT), export_status=gs(ROOT, 'status', '--porcelain', '--', EXPORT),
        closing_src=read(os.path.join(T, 'b689_closing.py')),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b689_act_root.json'), arj0=jl('b688_act_root.json'), art=rd('b689_act_root.txt'), rootsf=rd('act_roots.txt'),
        rootbanks=jl('b689_root_banks.json'),
        pushout=(files_of(ROOT, K.STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, *f.split('/')))), cr0(blob(ROOT, 'HEAD:tools/' + f)))
              for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b689_kernels_face.json').get('kernels') or {}), kerns_read=list(dict.fromkeys(REC._kerns())),
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mustfail=not os.path.exists(os.path.join(D, 'b689_mustnotexist.txt')),
        fj=jl('b689_findings.json'), tj=jl('b689_trail.json'), sc=jl('b689_scores.json'), desk=rd('b689_desk_notes.txt'), tfj=jl('b689_table_final.json'),
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
    S['ra'] = RA.sources('b689', SESSION, K.ANCHOR, K.PARTS, S['lock_epoch'], PRE['relay'], PRE['pp']) if 'rules' in need else {}
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
            if f.startswith(('b689_', 'audit_b689_')) and os.path.isfile(os.path.join(D, f)) and not f.endswith(('.gz', '.png', '.jsonl')):
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


# ### b689's repair (REPAIR 3): the step-zero bank's failing set as run against b680's list as carried, and the re-run against the page's list
STEPZERO_FAILING = {'test_chain_page.py': ['(1)', '(9)', '(14)'], 'test_chain_page_b638.py': ['(4)', '(5)', '(6)', '(7)']}
RERUN_FAILING = {'test_chain_page.py': ['(9)']}


def tests_ok(S):
    j = S['tests']
    names = sorted(S['tracked_tests'])
    nf = dict((n, x['failing']) for n, x in j.items() if x['rc'] != 0 or x['failing'])
    nf2 = dict((n, x['failing']) for n, x in (S['tests2'] or {}).items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(j) == sorted(set(names) - {'test_elab_reader_b634.py'}) and nf == STEPZERO_FAILING \
        and nf2 == RERUN_FAILING and 'b688_nodes_zeta.txt' in ((S['tests2'] or {}).get('test_chain_page.py') or {}).get('args', []) \
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
    m = re.search(r'^### b689 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
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
    """b687's reading, carried (b689's window): the record tool's one reading over this act's whole capture and the previous act's after its
    post-push suite in its own session -- tools/edit_route.py's arms and sed in any form (data/b685_rules.txt row (2))."""
    return bool(S['cmds']) and bool(S['prev_cmds']) and S['REC'].edit_route_offences(S['cmds'] + S['prev_cmds']) == []


def no_local_lean(S):
    import b689_record as REC
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


# ================================================================== (R299) STEP ZERO: THE CITATION CHECK, THE BRANCHES
READFIRST_NEEDLES = ('relay data/b688_closing.txt :1', 'relay data/b688_defects.txt :5-:40', 'relay data/b688_citation_check.txt :96',
                     'FINDINGS.md :9314', 'OPEN_TRAILS.md :14946', 'relay tools/b678_corrigendum.py :82-:93', 'relay tools/rule_arms.py :387-:391',
                     'relay data/b679_strip_plan.txt :224-:239', 'relay data/b676_strip_uses.txt :9-:30', 'Converse.lean :191-:192',
                     'relay data/b679_runner_run39064453563.txt', 'relay data/b679_q0_membership.txt :16-:65', 'relay data/b687_p3_status.txt :8',
                     'relay data/b688_closing_push_out.txt')
NAMED_LOCAL = sorted(b for _r, bs in K.DELETE for b in bs)
NAMED_ALL = sorted(NAMED_LOCAL + [b for _r, b in K.DELETE_REMOTE])


def readfirst_ok(S):
    z = unwrap(S['readfirst'])
    return bool(z) and all(x in z for x in READFIRST_NEEDLES)


def branches_ok(S):
    """b689's repair (REPAIR 2): the four repositories' LOCAL branch lists by the ruling's names -- the recut branches stand at their remotes,
    the ruling naming no remote branch -- and the branches bank."""
    z = S['branchest']
    left = dict((r, sorted(x.strip() for x in v.split(NL) if x.strip())) for r, v in S['branch_lists'].items())
    return all(v == [] for v in left.values()) and len(left) == 4 and all(b in z for b in NAMED_LOCAL) \
        and 'BRANCHES 10 (LOCAL 10, REMOTE 0) ; MERGED 10 ; TO BE DELETED 10 ; UNNAMED OF b688 0' in z


def branches_banked_ok(S):
    import b689_record as REC
    rows = S['branchj'].get('rows') or []
    try:
        fates = [REC.read_branch_row(r) for r in rows]
    except Exception:
        return False
    return len(rows) == 10 and all(f == 'DELETED' for _b, f in fates) and all(r['merged'] for r in rows) \
        and sum(1 for r in rows if r['where'] == 'remote') == 0


def deletes_one_ok(S):
    import b689_record as REC
    shapes = [REC.delete_shape(r['cmd']) for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell')]
    shapes = [s for s in shapes if s[0]]
    return bool(shapes) and all(len(d) == 1 and not gl for d, gl in shapes) and sorted(x for d, _g in shapes for x in d) == NAMED_ALL \
        and 'BRANCH DELETES OF ONE BRANCH AND NO GLOB 10 OF 10' in S['cmdt']


def dry_step_ok(S):
    g = S['gate']
    return '--- THE DRY-RUN STEP ((R267)(2))' in g and 'ENTRY : table cells NONE ; screens QUIET' in g and 'TRAIL : table cells NONE ; screens QUIET' in g \
        and '### ### **THE DRY-RUN STEP : CLEAN**' in g and '### ### **GATE VERDICT : CLEAR**' in g


def closing_dry_ok(S):
    g = S['gate']
    return '--- THE CLOSING DRY-RUN STEP (b675 rules row 1)' in g and '### ### **THE CLOSING DRY-RUN STEP : CLEAN**' in g \
        and 'b689 closed:' in g and 'the misses as the bank lists them' in g and '(annotated, peeled) ; main' in g \
        and '### THE ROUTE' in g and '### THE FACES LINE' in g and '### THE KERNELS' in g and '### NO VERDICT LINE' not in g


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
    return landed(S, 0, ['b688 AT ITS WEIGHT', 'ITS DEFECT (f) REPAIRED BY A GENERATED CORRIGENDUM ENTRY', '007d4ead'])


ANSWER_GOVERNS = (('no space retained', 'arm'), ('the lexicon a check on that reading', 'branch'))


def answers_checked_ok(S):
    """the citation bank's mid-act prints read at HEAD, at or above the sealed floor, each before the write its answer governs: the arm's
    answer before the arm's commit, the plan's answer before the kernel branch's commit."""
    c = S['citation']
    stamps = re.findall(r'### \(R278\)\(4\) THE MID-ACT CHECK \((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\): the answer carrying \'([^\']+)\'', c)
    acts = dict((n, iso_epoch(t)) for t, n in stamps)
    return len(stamps) >= FLOORS['checks'] and all(acts.get(n) and S['t'].get(w) and acts[n] < S['t'][w] for n, w in ANSWER_GOVERNS)


# ================================================================== (R299)(1)-(5): THE SCORER, THE CORRIGENDUM, THE ARM, THE PLAN, THE BUILD
def _fn_src(src, name):
    if ('\ndef %s(' % name) not in src:
        return ''
    i = src.index('\ndef %s(' % name) + 1
    m = re.search(r'\n(?=\S)', src[i + 1:])
    return src[i:i + 1 + m.start() + 1] if m else src[i:]


def scorer_banks_ok(S):
    """data/b686_rules.txt row (1), standing: the N3 scorer's code reads the grade bank and the run's axioms bank and no ledger and no
    findings bank; the scores route writes its bank once; the entry's composer takes its scores line from the scores bank."""
    n3 = strip_prose(_fn_src(S['rec_src'], '_n3')) + strip_prose(_fn_src(S['rec_src'], '_grade_state'))
    sc = strip_prose(_fn_src(S['rec_src'], 'scores'))
    ft = strip_prose(_fn_src(S['rec_src'], '_finding_text'))
    return bool(n3) and 'b689_grade.txt' in n3 and 'RUNNER_BANK' in n3 \
        and not re.search(r'\b(FIND|OT)\b|FINDINGS|OPEN_TRAILS|findings|entry_line', n3) \
        and "os.path.isfile(os.path.join(D, 'b689_scores.json'))" in sc and 'scores_line(S)' in ft and "jl('b689_scores.json')" in ft


def _entry_block(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    if not e:
        return ''
    end = next((i for i in range(e, len(ls)) if ls[i].startswith('## ')), len(ls))
    return NL.join(ls[e - 1:end])


def entry_scores_ok(S):
    """data/b686_rules.txt row (1): the landed entry's scores line equals the line composed from the scores bank."""
    import b689_record as REC
    want = conv(REC.scores_line(S['sc'])) if S['sc'] else None
    blk = _entry_block(S)
    got = [l for l in blk.split(NL) if l.startswith('**The scores.**')]
    return bool(want) and bool(S['sc']) and got == [want]


def entry_title_ok(S):
    """the ferry's Component 6: the landed entry's title in the ferry's form, its parts read from the banks by the record tool, equal to the
    worklist's title."""
    e = S['fj'].get('entry_line')
    return bool(e) and S['REC']._title() == K.TITLE and fline(S, e) == conv(K.TITLE)


def corrigendum_ok(S):
    """(R299)(2): the corrigendum's landing at FINDINGS by its bank, found by conv; its bank counting three rows by line against the entry's
    two and the trail's three; the corrigenda bank's row (3) appended."""
    ln = ((S['corrl'].get('lines') or [{}])[0]).get('line')
    head = ((S['corrl'].get('lines') or [{}])[0]).get('head') or '\x00'
    pre, now, hd = S['shared'].get('data/b675_corrigenda.txt') or (None, None, None)
    return ln == K.CORRIGENDUM_LINE and fline(S, ln) == conv(head) and 'Corrigendum to b688' in head \
        and 'THE SENTENCE AT FINDINGS :9320 ; AS WRITTEN TWO ; THE BANK THREE (ROWS :96, :107, :116) ; THE TRAIL THREE ; THE ENTRY AT FINDINGS :%d' % K.CORRIGENDUM_LINE in S['corr'] \
        and '(3) PLACE-papers FINDINGS.md :9320' in appended(pre, now)


def arm_repaired_ok(S):
    """(R299)(2) and the author's word: the arm in tools/rule_arms.py in the author's form, read at HEAD against b688's ferry bank and this act's
    -- both OK, the planted case firing on both -- and the repairs bank carrying the counts under all three forms."""
    a = dict((x[0], x[1:]) for x in S['armread'])
    return a.get('b688') == (True, True) and a.get('b689') == (True, True) \
        and "ok = bool(h) and bool(m) and ''.join(h.split()) in ''.join(m.group(1).split())" in S['ra_src'] \
        and "THE COUNTS: b688 before 0 of 1, under the ruled form 0 of 1, under the author's form 1 of 1" in S['repairs']


def plan_s11_ok(S):
    s = S['s11']
    return s.get('equal') is True and s.get('alone') is True and s.get('before') is True


USE_ROW = re.compile(r'^    :(\d+) +(Li\w+\.lean :\d+) +(DISCHARGED|RE-PROVED|OBSTRUCTED)\s', re.M)


def uses_ok(S):
    """the plan bank's == 2: the 22 strip uses of data/b676_strip_uses.txt :9-:30, each once with its class, through the record tool's reader;
    the counts printed beneath them."""
    import b689_record as REC
    rows = [dict(row=int(n), at=at, cls=c, why='the plan row') for n, at, c in USE_ROW.findall(S['plan'])]
    try:
        cls = [REC.read_use_row(r) for r in rows]
    except Exception:
        return False
    import collections
    cnt = collections.Counter(c for _r, c in cls)
    return sorted(r for r, _c in cls) == list(range(9, 31)) and cnt == {'DISCHARGED': 13, 'RE-PROVED': 9} \
        and 'THE COUNT: 22 of 22 classified ; DISCHARGED 13' in S['plan'] and 'OBSTRUCTED 0' in S['plan']


def prompt_before_lean_ok(S):
    """N2's second clause: the plan prompt put and answered after section 11's commit and before the first Lean file of the form existed --
    the Write tool's call on StripFree.lean, the first kernel commit touching it."""
    calls = S['answersj'].get('calls') or []
    if len(calls) < 2:
        return False
    ask, ans = iso_epoch((calls[1].get('ts') or '')[:19] + 'Z'), iso_epoch((calls[1].get('result_ts') or '')[:19] + 'Z')
    w, c = S['sfw']
    return bool(ask and ans and w and c and S['t']['s11']) and S['t']['s11'] < ask < ans < w and ans < c and S['t']['plan'] < ask


def landing_ok(S):
    ax = S['axioms']
    return 'LANDED 11 OF 11 DERIVES AT THE STANDARD THREE' in S['landing'] and len(K.NEW_NAMES) == 11 \
        and all(W + n in ax and set(ax[W + n]) <= set(STD3) and ax[W + n] for n in K.NEW_NAMES)


def grade_banked_ok(S):
    g = S['gradestate']
    return g.get('verbatim') is True and g.get('graded') is True and g.get('before') is True and bool(S['t']['grade'] and S['t']['merge']) \
        and S['t']['grade'] < S['t']['merge']


CONTROL_NAMES = ('c2_ne_zero', 'c2_w_eq_one', 'c2_liCoeff_one_neg', 'c3_real_segment', 'c2b_not_ne_zero', 'c2b_lesson', 'c2_not_excl',
                 'c2b_nonneg_offline')


def controls_ok(S):
    ax = S['axioms']
    return all(W + n in ax and ax[W + n] and set(ax[W + n]) <= set(STD3) for n in CONTROL_NAMES) \
        and 'C2b UNDER THE STRIP-FREE FORM' in S['landing'] and 'C3, THE REAL SEGMENT' in S['landing']


def no_sorry_branch_ok(S):
    code = NL.join(l.split('--', 1)[0] for l in re.sub(r'/-[\s\S]*?-/', '', S['main_src']).split(NL))
    return bool(S['main_src']) and not re.search(r'\bsorry\b', code) and not any('sorryAx' in d for d in S['axioms'].values()) \
        and not S['obstruction'] and bool(S['axioms'])


def constants_ok(S):
    c = S['constants']
    return 'ROWS 8 ; EQUAL OR OVERLAPPING 8' in c and 'n*` 63676 (v0.33 63676)' in c and 'THE CONSTANTS UNCHANGED BY ROW' in c \
        and 'a point with w = 1 ABSENT (certified)' in c


def q0_ok(S):
    q = unwrap(S['q0'])
    return 'ROWS READ 10' in q and 'UNDER THE STRIP-FREE FORM HOLDING 5' in q and 'strip-free: HOLDS, ON LESS' in q \
        and 'strip-free: NOT IN THE SET' in q and 'strip-free: NOT REQUIRED' in q


def faces_held_ok(S):
    rows = [l for l in S['faces_rows'].split(NL) if l.startswith('# backmatter:')]
    nodes = S['nodes'].split(NL)
    return len(rows) == 2 and len(nodes) >= K.NODES_ROW and rows[0] == nodes[K.NODES_ROW - 1] and 'v0.34' in rows[1] \
        and 'li_nonneg_cfg_imp_online_ne_zero' in rows[1] and FACES_PAGE not in S['pp_changed']


def shared_rows_ok(S):
    return len(S['shared']) == 1 and all(pre is not None and now is not None and head is not None and now.startswith(pre) and head == now
                                         and 'b689' in appended(pre, now) for pre, now, head in S['shared'].values())


def repairs_ok(S):
    return '### ### **REPAIRS 5 ; THE SEALED COPIES AGREE ; TOOLS CARRIED 8 OF 8 ; THE STANDING INSTRUMENTS UNEDITED True ; THE REPAIRED SHARED TOOL 1' in S['repairs'] \
        and 'REPAIRS 3 ; TO A SHARED TOOL 1' in S['repairs']


def parts_ok(S):
    return all(re.search(r'PART %s : ARMS \d+ ; \d+ s' % p, S['prerun']) for p in K.PARTS)


def defects_ok(S):
    """the defects bank's letters read at HEAD, the sealed letters its prefix, every owner the seat or the navigator."""
    letters = re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", S['defects'], re.M)
    fl = list(FLOORS['defects'])
    return letters[:len(fl)] == fl and [x for x, _o in letters] == list('abcdefghijklmnopqrstuvwxyz'[:len(letters)]) \
        and all(o in ('SEAT', 'NAVIGATOR') for _x, o in letters)


# ================================================================== THE RUNNER (the standing arms, this act's run and merge)
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
    import b689_record as REC
    rows = S['runner'].get('rows') or []
    tips = dict((k, gs('D:/' + k, 'rev-parse', tip)) for k, _p, tip, *_r in MERGES)
    try:
        for r in rows:
            REC.read_runner_row(r)
    except Exception:
        return False
    return len(rows) == 1 and all(r['ref'] == tips.get(r['kernel']) for r in rows) \
        and all(r['conclusion'] == 'success' and r['artifact_sha256'] and r['mem_low'] is not None and r['mem_low'] >= K.HOLD and not r['stopped']
                for r in rows)


def gate_ok(S):
    bs = S['rbanks']
    return len(bs) == 1 and all('GATE DERIVES' in t and 'BUILD EXIT 0 ; ERROR LINES 0' in t and 'SORRYAX 0' in t
                                and re.search(r'^### the artifact: .* ; AGREE$', t, re.M) for t in bs.values())


def merges_ok(S):
    for k, m in S['merges'].items():
        pre, tip, merge, tag = m['want']
        if m['main'] != merge or m['parents'] != [pre, tip] or m['tree_main'] != m['tree_built'] or m['tags'].get(tag) != merge:
            return False
    return len(S['merges']) == 1


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


POST_SEAL = ('b689 seal', 'b689 pre-root', 'b689 root', 'b689 record', 'b689 --', 'b689 closing', 'b689 entry')


def _component_commit(s):
    return s.startswith('b689') and not s.startswith(POST_SEAL)


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
    return bool(j) and len(rows) == 66 and rows[65][:3] == ['b689', j.get('root'), j0.get('root')] \
        and AR.root_of(items, j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) \
        and not [it for it in items if 'b628_intake_crank' in it or 'b647_navigator_memory' in it or 'b690_' in it or 'mirror' in it
                 or it.split()[0].endswith(('.gz', '.png', '.jsonl'))] \
        and any(it.startswith('data/b689_plan.txt ') for it in items) and any(it.startswith('data/b689_grade.txt ') for it in items) \
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
    return at is not None and 'data/b689_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    v = S['ar_verify'] or []
    r = S['ar_reads'].get('b689') or {}
    return [x[0] for x in v] == ['b%d' % i for i in range(624, 690)] and all(x[1] == 'AGREE' for x in v) and r.get('crlf') == 0 \
        and (S['ar_reads'].get('b680') or {}).get('corrected') == 4


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**The citation check**', '**The corrigendum**', '**The arm**', '**The plan**', '**The build**', '**The grade**',
                 '**The controls**', '**The constants**', '**Q0**', '**The scores.**', '**Read in mutual light**', 'strengthens', '**Carried to:**',
                 '**Next.**', 'b690')


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
    import b689_record as REC
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
    """b689's repair: PLACE-papers' changed files against the two ledgers alone, the faces page untouched under (R299)(5)."""
    return S['pp_changed'] == S['pp_allowed']


def closing_sentence_ok(S):
    t = S['closing_src']
    return ('no identifier of the author ' + 'in any outbound') in t and ('plain requests to ' + 'github.com') in t \
        and '### THE CITATION CHECK' in t and '### THE RECORD LINES' in t and '### THE DRY RUN' in t and '### THE ROUTE' in t \
        and '### THE FACES LINE' in t and '### THE KERNELS' in t and '### THE MIRROR' in t and '### THE CARRY-TIME' in t


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
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R299) END' in S['ferry'] and S['ferry'].rstrip().endswith(K.TAIL),
     lambda S: put(S, 'ferry', S['ferry'].replace(K.TAIL, ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the step-zero bank: tail, lean, lake, python and claude named, the seat`s claude alone, none of the others; no task stopped, no orphan, nothing stopped by PID',
     lambda S: procs_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('python 0', 'python 1'))),
    ('G-STEPZERO-TESTS', 'the runner bank against the test files tracked before the act, test_elab_reader_b634.py withheld (no lean on this host), and the re-run against the page`s list',
     lambda S: tests_ok(S), lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: 'data/b688_closing_push_out.txt' in S['pushout'][0] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'the four repositories` local branch lists by the ruling`s names and the branches bank (the ruling`s list alone, every branch local)',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{'D:/relay': 'push-b688'}))),
    ('G-READFIRST-CITED', 'the read-first bank: every item of the ferry`s list cited by path and line', lambda S: readfirst_ok(S),
     lambda S: put(S, 'readfirst', '')),
    ('G-ANSWERS-BANKED', 'the answers bank read at HEAD: its prompts and calls at or above the sealed floors, each with its options and result, any call after the lock named on the face',
     lambda S: answers_ok(S), lambda S: put(S, 'answers', S['answers'].replace('### PROMPT 1 (', '### PROMPTED ('))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-EXPORT-UNTRACKED', 'the navigator`s export: present, untracked, in no commit', lambda S: S['export_present'] and S['export_log'] == ''
     and S['export_index'] == '' and S['export_status'].startswith('??'), lambda S: put(S, 'export_index', EXPORT)),
    ('G-EDIT-ROUTE', 'the record tool`s one reading (tools/edit_route.py`s arms and sed in any form) over this act`s whole capture and the previous act`s after its post-push suite in its own session, read live',
     lambda S: edit_route_ok(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -n 1p tools/b689_record.py")])),
    ('G-NO-LOCAL-LEAN', 'the act`s command capture, read live: no command runs lean or lake on this host (N1)', lambda S: no_local_lean(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd='LEAN_PATH=build lean Core/X.lean -o build/X.olean')])),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line, found by conv', lambda S: weight_ok(S), lambda S: _rl(S, 0, 1)),
    ('G-DRY-STEP-CLEAN', 'the gate`s record: the dry-run step run, the entry and the trail record quiet under their screens, CLEAN printed, the gate CLEAR',
     lambda S: dry_step_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE DRY-RUN STEP : CLEAN', 'THE DRY-RUN STEP : NOT CLEAN'))),
    ('G-CLOSING-DRY-STEP', 'the gate`s record: the closing run dry before the lock, its head line, citation line, route, faces and kernels lines and tag rows printed (b675 rules row 1)',
     lambda S: closing_dry_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE CLOSING DRY-RUN STEP : CLEAN', 'THE CLOSING DRY-RUN STEP : NOT CLEAN'))),
    ('G-CITATION-CHECKED', 'the citation check`s bank (the gate step at step zero): no miss of the ruling or the ferry; every commit miss of a mid-act check tested directly and noted',
     lambda S: citation_ok(S), lambda S: put(S, 'citation', S['citation'].replace('CITES CHECKED 78 ; OK 78 ; MISSES 0', 'CITES CHECKED 78 ; OK 77 ; MISSES 1'))),
    ('G-R299-ENTERED', 'the ferry and the trail', lambda S: 'RULING (R299) END' in S['ferry'] and S['ot'].count('**(R299) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R299) ratified', '**(R2990) ratified'))),
    ('G-ROWGEN-STEPZERO', 'the rowgen bank: constellation and the build-free diff over the 19 roster tables, both exit 0 (b670 rules row 3)',
     lambda S: rowgen_ok(S), lambda S: put(S, 'rowgen', S['rowgen'].replace('ROWGEN DIFF EXIT 0', 'ROWGEN DIFF EXIT 1'))),
    ('G-BRANCHES-BANKED', 'the branches bank: ten rows through the record tool`s reader, all local, each merged and deleted',
     lambda S: branches_banked_ok(S), lambda S: _mut(S, 'branchj', lambda d: d['rows'][0].update(fate='GONE'))),
    ('G-DELETES-ONE-BRANCH', 'the command capture by the record tool`s reader and the command bank: each branch delete naming one branch, no glob in any half, the ruling`s list exactly',
     lambda S: deletes_one_ok(S), lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="git branch -d push-b688 push-b688-root")])),
    ('G-ANSWERS-CHECKED', 'the citation bank`s mid-act prints read at HEAD, each before the write its answer governs: the arm`s commit, the kernel branch`s commit',
     lambda S: answers_checked_ok(S), lambda S: put(S, 't', dict(S['t'], arm=1))),
    ('G-SCORER-READS-BANKS', 'tools/b689_record.py`s code, prose stripped: the N3 scorer reading the grade bank and the run`s axioms bank and no ledger, the scores bank written once, the entry`s scores line from it',
     lambda S: scorer_banks_ok(S), lambda S: put(S, 'rec_src', S['rec_src'].replace("def _n3():", "def _n3():\n    _x = rd(FIND)"))),
    ('G-ENTRY-SCORES-EQUAL', 'FINDINGS at the findings bank`s line and the scores bank: the entry`s scores line equal to the line composed from the bank',
     lambda S: entry_scores_ok(S), lambda S: _mut(S, 'sc', lambda d: d.update(N1=['REFUTED', 'planted']))),
    ('G-ENTRY-TITLE-FORM', 'FINDINGS at the findings bank`s line, the record tool`s title from the grade, merge, corrigendum and repairs banks, and the worklist`s: the ferry`s form',
     lambda S: entry_title_ok(S), lambda S: put(S, 'find', S['find'].replace(conv(K.TITLE), conv(K.TITLE).replace('v0.34;', 'branch held at the obstruction;')))),
    ('G-CORRIGENDUM-ENTRY', 'the corrigendum`s landing bank and FINDINGS at its line by conv; its bank`s three rows against the entry`s two and the trail`s three; the corrigenda bank`s row (3)',
     lambda S: corrigendum_ok(S), lambda S: put(S, 'corr', S['corr'].replace('THE BANK THREE', 'THE BANK TWO'))),
    ('G-HEADLINE-ARM-REPAIRED', 'tools/rule_arms.py`s reading at HEAD over b688`s ferry bank and this act`s, its planted case, its source line and the repairs bank`s counts ((R299)(2), the author`s form)',
     lambda S: arm_repaired_ok(S), lambda S: put(S, 'armread', [('b688', False, True), ('b689', True, True)])),
    ('G-PLAN-SECTION11-FIRST', 'the plan bank against data/b679_strip_plan.txt :224-:239, the plan bank at its first commit (section 11 alone), the plan rows` commit after it (N2)',
     lambda S: plan_s11_ok(S), lambda S: _mut(S, 's11', lambda d: d.update(alone=False))),
    ('G-USES-CLASSIFIED', 'the plan bank`s == 2 through the record tool`s reader: the 22 uses :9-:30 each once with its class, DISCHARGED 13, RE-PROVED 9, OBSTRUCTED 0',
     lambda S: uses_ok(S), lambda S: put(S, 'plan', S['plan'].replace('    :29 LiConverseCfg.lean :231 RE-PROVED', '    :29 LiConverseCfg.lean :231 OBSTRUCTED'))),
    ('G-PROMPT-BEFORE-LEAN', 'the answers bank`s second call against section 11`s and the plan rows` commits, the Write tool`s call on StripFree.lean and the first kernel commit touching it (N2)',
     lambda S: prompt_before_lean_ok(S), lambda S: put(S, 'sfw', (1, 1))),
    ('G-LANDING-BANKED', 'the landing bank and the run`s axioms bank: eleven new names, each printed at the standard three',
     lambda S: landing_ok(S), lambda S: _mut(S, 'axioms', lambda d: d.update({W + 'powerSum_re_ge_split': ['sorryAx']}))),
    ('G-GRADE-BANKED', 'the grade bank against the branch`s statement lines, its grade and check, the salt-check, its commit before the merge`s (N3)',
     lambda S: grade_banked_ok(S), lambda S: put(S, 't', dict(S['t'], grade=10 ** 11))),
    ('G-CONTROLS-PRINTED', 'the run`s axioms bank: C2, C3 and C2b under the strip-free form and v0.33`s two controls, each printed at the standard three; the landing bank`s readings (N3)',
     lambda S: controls_ok(S), lambda S: _mut(S, 'axioms', lambda d: d.pop(W + 'c2b_lesson', None))),
    ('G-NO-SORRY-BRANCH', 'SIDE-explicit-formula main`s StripFree.lean, its code: no sorry; the run`s print: no sorryAx; no obstruction bank (N4)',
     lambda S: no_sorry_branch_ok(S), lambda S: put(S, 'main_src', S['main_src'] + NL + '  sorry')),
    ('G-CONSTANTS-BY-ROW', 'the constants bank: eight rows under the strip-free form equal to v0.33`s, n*` 63676, no w = 1 point at Q0',
     lambda S: constants_ok(S), lambda S: put(S, 'constants', S['constants'].replace('ROWS 8 ; EQUAL OR OVERLAPPING 8', 'ROWS 8 ; EQUAL OR OVERLAPPING 7'))),
    ('G-Q0-REREAD', 'the Q0 re-read bank: ten rows, each status under both forms, ρ ≠ 0 holding on less',
     lambda S: q0_ok(S), lambda S: put(S, 'q0', S['q0'].replace('HOLDS, ON LESS', 'ASSUMED'))),
    ('G-FACES-ROWS-HELD', 'the faces rows bank, b688`s node list :167 and PLACE-papers` changed files: the current row verbatim, the successor drafted, the page untouched',
     lambda S: faces_held_ok(S), lambda S: put(S, 'pp_changed', S['pp_changed'] + [FACES_PAGE])),
    ('G-SHARED-ROWS-APPENDED', 'the corrigenda bank: before, working tree and HEAD, a prefix extension carrying b689`s row',
     lambda S: shared_rows_ok(S), lambda S: _mut(S, 'shared', lambda d: d.update({'data/b675_corrigenda.txt': (b'a', b'b', b'b')}))),
    ('G-TOOL-REPAIRS', 'the repairs bank`s two verdicts: three repairs, the shared one in the author`s form; the carry-time reading, five repairs, the sealed copies agreeing, eight tools carried, the standing instruments unedited',
     lambda S: repairs_ok(S), lambda S: put(S, 'repairs', S['repairs'].replace('REPAIRS 5 ;', 'REPAIRS 0 ;'))),
    ('G-PARTS-PRERUN', 'data/b684_rules.txt row (1) and the pre-run bank`s four parts with their seconds',
     lambda S: parts_ok(S), lambda S: put(S, 'prerun', S['prerun'].replace('PART standing-c', 'PART standing-x'))),
    ('G-DEFECTS-LETTERED', 'the defects bank read at HEAD: the sealed letters its prefix, consecutive letters, owners the seat or the navigator',
     lambda S: defects_ok(S), lambda S: put(S, 'defects', S['defects'].replace("(a) THE SEAT'S", "(a) THE AUTHOR'S"))),
    ('G-SPEC-PLANTED', 'tools/b689_regspec.py`s planted rows run live through the record tool`s readers, and rows of another shape refused',
     lambda S: bool(S['spec']['read']) and all(S['spec']['read']) and all(S['spec']['controls']) and any('branch' in x for x in S['spec']['shapes']),
     lambda S: _mut(S, 'spec', lambda d: d['controls'].append(False))),
    ('G-CONVERSION-ONE', 'every b689 tool`s code and the repaired shared tool`s: no conversion defined (conv imported from b652_record); the suite importing it',
     lambda S: S['conv_bad'] == [] and 'from b689_record import conv' in S['suite'], lambda S: put(S, 'conv_bad', ['b689_checks.py'])),
    ('G-WORKFLOW-FILES', 'every kernel the act merged, its main: the workflow unchanged since its own commit, no author identifier, no secret, the hold, the build path its dependency form takes, the print step over its list, the files the act wrote',
     lambda S: wf_ok(S), lambda S: _mut(S, 'wf', lambda d: _first_wf(d).update(text=_first_wf(d)['text'] + ' secrets.X'))),
    ('G-RUNNER-READ', 'this act`s run`s row (one) through the record tool`s reader: the built tip, success, the artifact`s sha256, the memory low above the hold',
     lambda S: runner_ok(S), lambda S: _mut(S, 'runner', lambda d: [r.update(mem_low=2000) for r in d['rows']])),
    ('G-RUNNER-GATE', 'this act`s run`s gate reading: build exit 0, no error line, no sorryAx, the artifact`s digest agreeing',
     lambda S: gate_ok(S), lambda S: put(S, 'rbanks', dict(S['rbanks'], **{'x_after': 'GATE NOT DERIVES'}))),
    ('G-MERGES-ON-GATE', 'SIDE-explicit-formula`s main: the merge commit of the built tip on its main, the merged tree the built tree, v0.34 peeled to it',
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
    ('G-PP-SCOPE', 'PLACE-papers` changed files against FINDINGS and OPEN_TRAILS (declared; the faces page untouched)',
     lambda S: corpus_scope(S), lambda S: put(S, 'pp_changed', S['pp_changed'] + ['day1/ONE_PAGE_PROOF.md'])),
    ('G-CURRENTS-UNEDITED', 'the map, the census, the monograph, the Dirichlet page, the surround, SIMPLICITY, README, REGISTRY, FOUNDATIONS and its one-copy partner, the faces page: working tree, before and HEAD',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'ERRATA.md': (b'x', b'y', b'y')}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read before the seal',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b688`s and the earlier tools, b687`s readings, b685`s derivation, the generator and its test, the maps and evaluation routes, the corrigendum tool, act_root.py, rowgen`s, edit_route.py, chain_page.py, e0_rule.py, the mirror`s, the instruments and the shared tools (rule_arms.py, repaired, sealed with the act): before, working tree and HEAD',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'additive_shared.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 007d4ead but the shared additive files (act_roots.txt and the corrigenda bank among them), by blob id',
     lambda S: S['prior_bad'] == [] and S['prior_n'] > 0, lambda S: put(S, 'prior_bad', ['data/b688_stepzero.txt'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS before and now', lambda S: S['fi_pre'] is not None and (S['fi_now'] or b'').startswith(S['fi_pre']),
     lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS before and now', lambda S: S['ot_pre'] is not None and (S['ot_now'] or b'').startswith(S['ot_pre']),
     lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-NODISCLOSURE-PUBLIC', 'TECHNE-Core`s needle sets over every public byte the act writes: the ledger lines, the banks and the tools',
     lambda S: bool(S['nd_pub']) and not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', {'method': 1})),
    ('G-OUTSIDE-NAMED-NOWHERE', 'the ledger lines appended', lambda S: S['outside'] == [], lambda S: put(S, 'outside', ['x'])),
    ('G-DELETE-FREE', 'the act`s tools` code and the repaired shared tool`s, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='os' + '.remove(p)'))),
    ('G-PUBLISH-UNCALLED', 'the act`s tools` code: no publish call', lambda S: publish_uncalled(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='z_' + 'publish()'))),
    ('G-SEALED-AFTER-COMPONENTS', 'the lock time against every relay and PLACE-papers commit of the act by its subject', lambda S: sealed_after_ok(S),
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b689 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now, the repaired shared tool among them', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'b689_record.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3), in four parts summed',
     lambda S: S['lock_epoch'] is not None and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b688`s trail record on OPEN_TRAILS and its root in the chain', lambda S: '### b688 — lane two, act one hundred and fifteen, the re-cut act' in S['ot']
     and S['rootsf'].count(NL + 'b688 ') == 1, lambda S: put(S, 'ot', S['ot'].replace('### b688 — lane two', '### b688 - lane two'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], grade_moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 66th chain row (the corrigendum row apart), the root bank and its items, the plan and grade banks and the shared file among them, no binary, mirror or untracked bank',
     lambda S: root_banked_ok(S), lambda S: put(S, 'rootsf', S['rootsf'] + 'b690 x y' + NL)),
    ('G-ROOT-BANKS-COMMITTED', 'the root route`s banked reading and every named bank`s blob at the root`s recorded commit: clean and equal at HEAD, HEAD the remote main, the recorded hash carried by the recorded commit',
     lambda S: root_banks_committed_ok(S), lambda S: put(S, 'rootbanks', dict(S['rootbanks'], pushed=False))),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit with the suite`s own remote reads: b624 to b689 AGREE, b680 read through its corrigendum row (4 banks), b689 written LF',
     lambda S: verify_ok(S), lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s through conv, and its parts', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line, the head through conv', lambda S: bool(S['tj'].get('line'))
     and oline(S, S['tj']['line']) == conv(S['REC'].TRAIL_HEAD()), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b689 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b689_record.py agree', 'b689_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line: b690', lambda S: '**Next:** b690' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** b690', '**Next:** b691'))),
] + [('G-N%d-SCORED' % i, 'the scores through the record tool`s reader, and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i),
      lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written since 007d4ead and c3af808 against the (W) globs',
     lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b689')" in S['suite'] and "'data/b689_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b689_closing.py: the closing sentence in the rule`s words with the plain reads named; the citation check, the record lines, the dry run, the route, the faces line, the kernels, the mirror, the carry-time reading',
     lambda S: closing_sentence_ok(S), lambda S: put(S, 'closing_src', S['closing_src'].replace('no identifier of the author ' + 'in any outbound', 'x'))),
    ('G-LSREMOTE-ONE-PER-REPO', 'the part`s ls-remote calls per repository, read after every other arm of the part has run (OPEN_TRAILS :12703)',
     lambda S: lsr_ok(S), lambda S: put(S, 'lsr', {PP: 2})),
] + [(nm, 'tools/rule_arms.py (the author`s word on (R293)(6)) -- ' + reads, (lambda p: lambda S: p(S['ra']))(pred),
      (lambda pl: lambda S: put(S, 'ra', pl(S['ra'])))(plant)) for nm, reads, pred, plant in RA.ARMS]


def _part_of(name):
    if name in K.ACT_ARMS:
        return 'act'
    if name in B_ARMS:
        return 'standing-b'
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
    p = os.path.join(D, 'b689_seal_hashes.json')
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
    print('  written: b689_seal_hashes.json')
    return 0


def _base_name(pushed):
    if PRERUN:
        return 'b689_arms_prerun.txt'
    if MID and len(sys.argv) > sys.argv.index('--mid') + 1:
        return sys.argv[sys.argv.index('--mid') + 1]
    if RERUN and len(sys.argv) > sys.argv.index('--rerun-postpush') + 1:
        return sys.argv[sys.argv.index('--rerun-postpush') + 1]
    return 'b689_checks_postpush.txt' if pushed else 'b689_checks.txt'


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
    out = ['=' * 104, heads[0].replace('PART standing-a', 'FOUR PARTS SUMMED (data/b684_rules.txt row (1))'), '=' * 104] + [
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
        ex.update(jl('b689_exercise_%s.json' % part).get('exercise') or {})
    if ex and base in ('b689_checks.txt', 'b689_checks_postpush.txt'):
        e = (json.dumps(dict(exercise=ex, run=n, live_failing=fails, defective=defs, neg_failures=ng), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p_ = os.path.join(D, 'b689_exercise.json')
        open(p_ + '.tmp', 'wb').write(e)
        os.replace(p_ + '.tmp', p_)
    print(NL.join(out[3:12]))
    print('  written: %s' % base)
    return 0 if ok else 1


def main():
    if SEAL:
        return seal()
    if COMBINE:
        return combine()
    if PART not in K.PARTS:
        print('### data/b684_rules.txt row (1): every run in four foreground parts -- give `--part %s`' % ' | '.join(K.PARTS))
        return 2
    fm = free_mb()
    if fm < K.HOLD:
        print('%s  ### THE HOST`S FREE MEMORY %d MB, BENEATH THE HOLD %d MB: PART %s NOT RUN ((R294)(2))' % (
            time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), fm, K.HOLD, PART))
        return 3
    t_start = time.time()
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b689 -- THE SUITE. ### **%s READING.** ### PART %s (data/b684_rules.txt row (1)) ### every arm exercised on both controls.' % (
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
    rec('  ### (R264)(2) THE FREEZE: the standing arms (b688`s face less its own arms, the twenty rule arms among them) %d ; carried here %d ; added %s ; '
        'the act`s arms over its own banks %s ; arms beyond both %s' % (len(S['standing']), len(set(names) & set(S['standing'])), list(K.STANDING_ADDED) or 'NONE',
                                                                     sorted(set(names) - set(S['standing'])),
                                                                     sorted(set(names) - set(S['standing']) - set(K.ACT_ARMS)) or 'NONE'))
    rec('  ### standing arms not carried here: %s' % (sorted(set(S['standing']) - set(names)) or 'NONE'))
    if 'rules' in NEED[PART]:
        rec('  ### THE TWENTY RULE ARMS, EACH WITH ITS COUNT (tools/rule_arms.py; rows read, rows failing, the reading):')
        for nm in RA.NAMES:
            ok_, n_, b_, note = RA.reading(nm, S['ra'])
            rec('  ###   %-28s %-4s read %d ; failing %d ; %s' % (nm, 'PASS' if ok_ else 'FAIL', n_, b_, note[:260]))
    if 'chain' in NEED[PART]:
        av = S['ar_verify']
        rec('  ### THE ACT-ROOT CHAIN, recomputed: %s' % ('; '.join('%s %s%s' % (a, v, (' (' + '; '.join(w) + ')') if w else '') for a, v, w in av) or 'no act rooted'))
        rec('  ### the reads at commit, b680: %s ; b689: %s' % (S['ar_reads'].get('b680'), S['ar_reads'].get('b689')))
    sj = S['sealj'].get('tools') or {}
    rec('  ### THE SEALED TOOLS, recorded at the seal %s : %s' % (S['sealj'].get('at', '### NOT RECORDED'), '; '.join(
        '%s %s' % (t, ('agree' if sj.get(t) == S['sealnow'].get(t) else 'DIFFER') if t in sj else 'not recorded') for t in K.SEALED)))
    off = S['REC'].edit_route_offences(S['cmds'] + S['prev_cmds'])
    rec('  ### G-EDIT-ROUTE read %d captured commands of this act and %d of the previous act after its post-push suite (its own session); offences %d: %s' % (
        len(S['cmds']), len(S['prev_cmds']), len(off), ['#%s %s' % (r['n'], [k for k, _ in o]) for r, o in off] or 'none'))
    mc = re.search(r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', S['citation'])
    rec('  ### THE CITATION CHECK: %s ; THE ARM AT HEAD: %s ; SECTION 11: %s ; THE GRADE: %s' % (
        mc.group(0) if mc else '### NOT READ', S['armread'], dict((k, v) for k, v in S['s11'].items() if k in ('equal', 'alone', 'before')),
        dict((k, v) for k, v in S['gradestate'].items() if k != 'lines')))
    rec('  ### PLACE-papers` changed files %d against the allowed %d (the two ledgers): beyond %s' % (
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
    rec('  %-46s %-5s %-5s %-5s %s' % ('arm', 'LIVE', 'NEG', 'POS', 'verdict'))
    rec('  ' + '-' * 98)
    fail, defective, negfail, EX = [], [], 0, {}
    for name, reads, pred, pos in arms:
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
    rec('  ### the run took %.0f s' % secs)
    rec('  ### PART %s : ARMS %d ; LIVE PASSING %d ; LIVE FAILING %d %s ; NEGATIVE-CONTROL FAILURES %d ; POSITIVE-CONTROL PASSES %d %s ; '
        'DECLARED EQ RUN %s ; %d s' % (PART, len(arms), len(arms) - len(fail), len(fail), json.dumps(fail) if fail else 'NONE', negfail, len(defective),
                                       json.dumps(defective) if defective else 'NONE', S['declared_eq_run'], int(secs)))
    rec('=' * 104)
    base = _base_name(pushed)
    out = _write(_part_name(base, PART), L)
    lp = os.path.join(D, _part_name(base, PART).replace('b689_arms_prerun', 'b689_lsr_prerun').replace('b689_checks', 'b689_lsr').replace('.txt', '.json'))
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(arms), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b689_exercise_%s.json' % PART)
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if (not fail and not defective and negfail == 0 and S['declared_eq_run']) else 1


if __name__ == '__main__':
    sys.exit(main())
