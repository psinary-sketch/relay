# -*- coding: utf-8 -*-
"""b693_checks.py -- THE SUITE OF b693, UNDER (R303): b692 AT ITS WEIGHT; ITS POST-SEAL FIGURES BY CORRIGENDUM; THE CLOSING TOOL'S DEFECTS
RANGE AND THE PUSH TOOL'S BRANCH MODE REPAIRED AT CARRY TIME; SIDE-archimedean CUT UNDER THE QUOTATION RULE; SIX PARTS, THE CHAIN SPLIT BY ACT.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### (R303)(4) and data/b684_rules.txt row (1): every run in SIX foreground parts, each its own call in its own message -- `--part
### standing-a`, `--part standing-c` (G-PRIORBANK-UNCHANGED, G-NODISCLOSURE-PUBLIC, G-WRITELIST-KINDS), `--part standing-b1` (the shared
### additive files), `--part standing-b2` (the act-root chain's first half, b624-b658, its verdicts banked, NO ARM), `--part standing-b3` (the
### second half, b659-b693, and G-ACTROOT-VERIFY once over both halves' verdicts), `--part act` (the act's arms over this act's banks, the
### table regenerated in a closing run); each under the 590 s guard the seat runs it in, and NOT RUN beneath the 2,560 MB hold; `--combine
### <bank>` writes the bank. On the author's word at (R303)(4)'s prompt the chain is split by act, the boundary link b658 -> b659 read from
### data/act_roots.txt and printed by both halves; `--chain-control`, this act alone, runs the whole chain once in the old form after the
### pre-push halves and banks the three verdicts beside each other (data/b693_chain_control.txt).
### ### (R264)(2), THE FREEZE: the standing arms are b692's face's (G2) arms less b692's own arms over b692's banks, carried, the twenty-four
### rule arms of tools/rule_arms.py among them; no standing arm added (N5). The act's own arms read this act's banks alone (ACT_ARMS). The
### standing runner arms read this act's two runs at SIDE-archimedean -- before at the print list's commit, after at the cut's tip -- and its
### one merge.
### ### THE ACT'S TRANSCRIPT IS TWO SESSIONS (the host rebooted after Component 3): the command capture and the rule arms' call trace read
### the first session from (R303)'s line and the resume session from the resume order's line (tools/b693_worklist.py SESSIONS_AFTER).
### ### Every look-up of a landed line goes through the one conversion (imported from tools/b652_record.py through tools/b693_record.py).
### ### The harness is b568's to b692's, written by the Write tool from tools/b692_checks.py; the sources, predicates and arms over this act's
### ### banks are b693's. data/b686_rules.txt row (1): the act arm G-ENTRY-SCORES-EQUAL reads the landed entry; no scorer reads a ledger line.
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
import b693_worklist as K     # noqa: E402
import b692_worklist as K692  # noqa: E402
import b691_worklist as K691  # noqa: E402
import rule_arms as RA        # noqa: E402
from b693_record import conv  # noqa: E402

NL = chr(10)
PP = K.PP
ARCH = 'D:/' + K.ARCH
FACE = os.path.join(D, 'b693_registration_2026-10-19.txt')
B692_FACE = os.path.join(D, 'b692_registration_2026-10-19.txt')
B692_ACT_ARMS = K692.ACT_ARMS
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP)
EXPORT = K.EXPORT
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
SEAL = '--seal' in sys.argv
COMBINE = '--combine' in sys.argv
CONTROL = '--chain-control' in sys.argv
PART = sys.argv[sys.argv.index('--part') + 1] if '--part' in sys.argv and len(sys.argv) > sys.argv.index('--part') + 1 else None
L = []
# ### the sealed figures, the floors the count arms read at HEAD (standing from (R291)(3))
FLOORS = dict(prompts=4, calls=1, checks=4, defects=(('a', 'SEAT'), ('b', 'NAVIGATOR'), ('c', 'SEAT'), ('d', 'SEAT'), ('e', 'SEAT'), ('f', 'SEAT'), ('g', 'SEAT')))
REPAIRED_TOOLS = K.REPAIRED_TOOLS                      # ### the reader, the push tool and its test, the act-root verify and its test
NEW_TOOLS = K.NEW_TOOLS
# ### the instruments read unedited: b692's list, b691's and b692's sealed tools back among them, less this act's sealed and repaired tools
INST_BASE = ('b690_corrigendum.py', 'b690_readings.py', 'b689_corrigendum.py', 'b689_constants.py', 'b687_readings.py',
             'b685_count.py', 'b683_epstein_map_angle.py', 'correspondence_gen.py', 'test_correspondence_gen.py', 'b681_narrow.py',
             'b680_readings.py', 'b680_rules_index.py', 'b680_fig_tie.py', 'b680_fig_q0.py', 'b680_fig_li.py', 'b679_q0_membership.py',
             'b679_onset.py', 'b678_corrigendum.py', 'b677_epstein_map_angle.py', 'b675_li_bench.py',
             'b670_record.py', 'b669_record.py', 'b667_epstein_certify.py', 'b667_epstein_map_balls.py', 'b667_tail_recheck.py',
             'b663_epstein_map.py', 'b655_record.py', 'edit_route.py', 'test_edit_route_b646.py', 'b652_record.py', 'b651_record.py',
             'b649_record.py', 'b648_record.py', 'b646_record.py', 'b645_record.py', 'b644_record.py', 'b643_record.py', 'b641_record.py',
             'b633_record.py', 'b616_record.py', 'additive_shared.py', 'premise_status.py', 'terminal_table.py',
             'banned_terms.py', 'reg_seal.py', 'b378_lockgate.py', 'push_gated.sh', 'table_gate.py', 'mirror_build.ps1', 'mirror_verify.py',
             'b616_claims.py', 'ferry_scan.py', 'e0_rule.py', 'test_e0_rule.py', 'build_watch.py', 'chain_page.py', 'ledger_split.py',
             'axiom_claim.py', 'licensed_table.py', 'registration_gate.py', 'b300_regspec.py', 'no_sorry_main.py', 'module_header.py',
             'test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py', 'test_act_root.py',
             'test_act_root_commit_b644.py', 'test_act_root_order_b641.py', 'act_root.py', 'repair_snapshot.py', 'b672_record.py',
             'rowgen/rowgen.py', 'rowgen/diff_rowpin.py', 'rowgen/namemap.json')
INST = tuple(sorted((set(INST_BASE) | set(K691.SEALED) | set(K692.SEALED)) - set(K.SEALED) - set(REPAIRED_TOOLS) - set(NEW_TOOLS)))
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md',
            'phase2/method/THE_KEYSTONE_CENSUS_v0_8.md', 'day1/A_Place_to_Stand_v5_18.md', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md',
            'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md', 'day1/ONE_PAGE_PROOF.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md',
            'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', 'README.md', 'REGISTRY.md',
            'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md', 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md',
            'phase1.5/method/INSTRUMENTS.md', 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md', 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md')
TABLE_FILES = K.TABLE_FILES
WF, PT = '.github/workflows/build-module.yml', 'print_targets.txt'
CUT_FILE = 'SIDEArchimedean/Reflection.lean'
B1_ARMS = ('G-SHARED-ADDITIVE',)        # ### standing-b1: the shared additive files
B2_ARMS = ()                            # ### standing-b2: the chain's first half, its verdicts banked, no arm (the author's word)
B3_ARMS = ('G-ACTROOT-VERIFY',)         # ### standing-b3: the chain's second half and the arm over both halves
C_ARMS = ('G-PRIORBANK-UNCHANGED', 'G-NODISCLOSURE-PUBLIC', 'G-WRITELIST-KINDS')   # ### standing-c's arms: the written files
NEED = {'standing-a': ('live', 'rules'), 'standing-c': ('written',), 'standing-b1': ('additive',), 'standing-b2': ('chain_a',),
        'standing-b3': ('chain_b',), 'act': ()}
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
SESSIONS_AFTER = tuple(('%s/%s.jsonl' % (PROJ, s), a) for s, a in K.SESSIONS_AFTER)
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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b693')
            and 'data/b693_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    import b693_record as REC
    return REC.capture()


def prev_now():
    import b693_record as REC
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
        if (f.startswith('b693_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks):
                bad.append(f)
    return bad


def spec_planted():
    import b693_regspec as SPEC
    P = SPEC.planted()
    ctl = [ok for _w, ok in SPEC.controls()]
    return dict(read=[ok for _s, ok, _w in P], controls=ctl, shapes=[s for s, _o, _w in P])


def _deps(ax):
    import b693_record as REC
    return REC._deps(ax)


def wf_state():
    """this act's kernel workflow: SIDE-archimedean's workflow at main against the workflow the act wrote at 79a8527, its dependency form read
    from its tree, its print list against the after run's print bank, and the files the act wrote on its main since the main before it."""
    t = read_blob(ARCH, 'main:' + WF)
    lf = read_blob(ARCH, 'main:lakefile.toml') + read_blob(ARCH, 'main:lakefile.lean')
    req = re.search(r'(?im)^\s*require\b[^\n]*mathlib', lf) or re.search(r'(?is)\[\[require\]\][^\[]*name\s*=\s*"mathlib"', lf)
    pt = read_blob(ARCH, 'main:' + PT)
    return {K.ARCH: dict(text=t, before=read_blob(ARCH, '%s:%s' % (K.ARCH_WF, WF)), lakefile=bool(lf.strip()), mathlib=bool(req),
                         targets=[l.strip() for l in pt.split(NL) if l.strip()], printed=len(_deps(rd('b693_axioms_SIDE-archimedean_after.txt'))),
                         act_writes=sorted(set(x for x in gs(ARCH, 'diff', '--name-only', K.ARCH_BEFORE, 'main').split(NL) if x.strip())),
                         want=sorted([WF, PT, CUT_FILE]))}


def main_state():
    """SIDE-archimedean's main after the re-cut: its tip, its first-parent line back to the main before the act, the merge's parents, the files
    each commit wrote, the tags peeled, the merge's tree against the gated tip's, the tag's message."""
    line = gs(ARCH, 'rev-list', '--first-parent', '--abbrev-commit', '--abbrev=7', '%s..main' % K.ARCH_BEFORE).split()
    return dict(main=gs(ARCH, 'rev-parse', '--short=7', 'main'), line=list(reversed(line)),
                parents=gs(ARCH, 'log', '-1', '--format=%p', '--abbrev=7', K.ARCH_MERGE).split(),
                files=dict((c, files_of(ARCH, c)) for c in (K.ARCH_WF, K.ARCH_PT, K.ARCH_CUT)),
                tags=sorted(set(sum((gs(ARCH, 'tag', '--points-at', c).split() for c in (K.ARCH_WF, K.ARCH_PT, K.ARCH_CUT, K.ARCH_MERGE)), []))),
                tag=gs(ARCH, 'rev-parse', '--short=7', K.ARCH_TAG + '^{commit}'), prior=gs(ARCH, 'rev-parse', '--short=7', K.ARCH_PRIOR_TAG + '^{commit}'),
                trees=(gs(ARCH, 'rev-parse', K.ARCH_MERGE + '^{tree}'), gs(ARCH, 'rev-parse', K.ARCH_CUT + '^{tree}')),
                tagmsg=gs(ARCH, 'tag', '-l', '-n9', K.ARCH_TAG))


def g2_of(path):
    t = read(path)
    try:
        g2 = t[t.index('### (G2) THE GATE ARMS.'):t.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


STANDING = sorted((set(g2_of(B692_FACE)) - set(B692_ACT_ARMS)) | set(K.STANDING_ADDED))
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


# ================================================================== THE CHAIN SPLIT BY ACT ((R303)(4), the author's word at its prompt)
def chain_names():
    return [l.split()[0] for l in rd('act_roots.txt').split(NL) if l.strip() and not l.startswith('corrigendum ')]


def half_acts(i):
    lo, hi = (int(x[1:]) for x in K.CHAIN_HALVES[i])
    return [a for a in chain_names() if lo <= int(a[1:]) <= hi]


def boundary():
    """the link at the split read from data/act_roots.txt: the first half's last root against the second half's first previous."""
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
    return base.replace('b693_', '').replace('.txt', '')


def half_bank(i, key):
    return 'b693_chain_half_%s_%s.json' % ('ab'[i], key)


def write_half(i, key, verdicts, reads):
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), head=gs(ROOT, 'rev-parse', 'HEAD'), half='%s-%s' % K.CHAIN_HALVES[i],
             acts=verdicts, reads=reads, boundary=boundary())
    p = os.path.join(D, half_bank(i, key))
    open(p + '.tmp', 'wb').write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)


def sources(need=()):
    """the sources the arms read; `need` (by part) names the heavy phases this part computes: 'live' (the three arms at HEAD), 'rules' (the
    rule arms' trace), 'written' (the written files, the public bytes, the prior banks), 'chain_a' and 'chain_b' (the act-root chain's two
    halves), 'additive' (the shared files)."""
    import b693_record as REC
    import b616_record as R6
    import edit_route as ER
    import b641_record as R41
    import additive_shared as ADD
    face = read(FACE)
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b693_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if (f.startswith('b693_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS)
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    cit = jl('b693_citation_check.json')
    t0 = time.time()
    S = dict(
        REC=REC, ER=ER, face=face, ferry=rd('b693_ferry.txt'), scan=rd('b693_ferry_scan.txt'), stepz=rd('b693_stepzero.txt'),
        readfirst=rd('b693_readfirst.txt'), defects=rd('b693_defects.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        answers=rd('b693_author_answers.txt'), answersj=jl('b693_author_answers.json'), prerun=rd('b693_arms_prerun.txt'), rl=jl('b693_record_lines.json'),
        tests=jl('b693_tests_stepzero.json'), testst=rd('b693_tests_stepzero.txt'), withheld=jl('b693_tests_withheld.json'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b693_seal_hashes.json'), sealnow=sealed_now(), cmds=capture_now(), prev_cmds=prev_now(), cmdj=jl('b693_commands.json'),
        cmdt=rd('b693_commands.txt'),
        planted={t: run_test(t) for t in TESTS}, spec=spec_planted(), conv_bad=conv_alone(), suite=read(os.path.join(T, 'b693_checks.py')),
        citation=rd(K.CITATION_BANK), cit_at=iso_epoch(cit.get('at') or ''), cit_misses=cit.get('misses') or [],
        gate=rd('b693_reg_gate.txt'), rowgen=rd('b693_rowgen_stepzero.txt'),
        branchj=jl('b693_branches.json'), branchest=rd('b693_branches.txt'),
        branch_lists=dict((repo, gs(repo, 'branch', '--list', *bs)) for repo, bs in K.DELETE),
        repairs=rd('b693_tool_repairs.txt'), rec_src=read(os.path.join(T, 'b693_record.py')), closing_src=read(os.path.join(T, 'b693_closing.py')),
        corr=rd('b693_corrigendum.txt'), corrland=jl('b693_corrigendum_landing.json'), corrigenda=rd('b675_corrigenda.txt'),
        d692=rd('b692_defects.txt'), range_ex=rd('b693_range_exercise.txt'), branch_mode=rd('b693_branch_mode.txt'),
        push_blob=gs(ROOT, 'hash-object', os.path.join(T, 'push_gated.sh')), push_src=read(os.path.join(T, 'push_gated.sh')),
        ar_blob=gs(ROOT, 'hash-object', os.path.join(T, 'act_root.py')), rule_blob=gs(ROOT, 'hash-object', os.path.join(T, 'rule_arms.py')),
        root_push=rd('b693_root_push_out.txt'), root_branch_push=rd('b693_root_branch_push_out.txt'),
        tie=rd('b693_tie.txt'), cut=rd('b693_cut.txt'), cutj=jl('b693_cut.json'), quote=rd('b693_quote_archimedean.txt'),
        prints_arch=rd('b693_prints_SIDE-archimedean.txt'), cells=rd('b693_correspondence_dry.txt'),
        rf_diff=rd('b693_readfirst_diff.txt'), rf_hand_now=blob(ROOT, 'HEAD:data/b693_readfirst.txt'), rf_hand_z=blob(ROOT, '1d1a9fc3:data/b693_readfirst.txt'),
        parts_probe=rd('b693_parts_probe.txt'), chain_control=rd('b693_chain_control.txt'), resume=rd('b693_resume.txt'),
        asec=jl('b693_arm_seconds.json'), asect=rd('b693_arm_seconds.txt'),
        shared=dict((p, (cr0(blob(ROOT, '%s:%s' % (PRE['relay'], p))), cr0(raw(os.path.join(ROOT, *p.split('/')))), cr0(blob(ROOT, 'HEAD:' + p))))
                    for p in K.SHARED_APPENDED),
        t=dict(c1=_ct(PP, K.C1_PP), answers=_ct(ROOT, K.ANSWERS_RELAY), repairs=_ct(ROOT, K.REPAIRS_RELAY), tie=_ct(ROOT, K.TIE_RELAY),
               named=_ct(ARCH, K.ARCH_WF), quote=_ct(ROOT, K.CUTRUN_RELAY), merge=_ct(ARCH, K.ARCH_MERGE), parts=_ct(ROOT, K.PARTS_RELAY),
               resume=_ct(ROOT, K.RESUME_RELAY)),
        files=dict(tie=files_of(ROOT, K.TIE_RELAY), quote=files_of(ROOT, K.CUTRUN_RELAY), cut=files_of(ROOT, K.CUT_RELAY), parts=files_of(ROOT, K.PARTS_RELAY),
                   resume=files_of(ROOT, K.RESUME_RELAY), stepzero=files_of(ROOT, '1d1a9fc3')),
        resume_parent=gs(ROOT, 'log', '-1', '--format=%p', '--abbrev=8', K.RESUME_RELAY),
        standing=STANDING, wf=wf_state(), runner=jl(K.RUNNER_ROWS),
        rbanks=dict(('%s_%s' % (r.get('kernel'), r.get('label')), rd('b693_runner_%s_%s.txt' % (r.get('kernel'), r.get('label'))))
                    for r in jl(K.RUNNER_ROWS).get('rows') or []),
        mainst=main_state(),
        export_present=os.path.exists(os.path.join(ROOT, *EXPORT.split('/'))), export_log=gs(ROOT, 'log', '--all', '--format=%h', '--', EXPORT),
        export_index=gs(ROOT, 'ls-files', '--', EXPORT), export_status=gs(ROOT, 'status', '--porcelain', '--', EXPORT),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b693_act_root.json'), arj0=jl('b692_act_root.json'), art=rd('b693_act_root.txt'), rootsf=rd('act_roots.txt'),
        rootbanks=jl('b693_root_banks.json'),
        pushout=(files_of(ROOT, K.STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, *f.split('/')))), cr0(blob(ROOT, 'HEAD:tools/' + f)))
              for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b693_kernels_face.json').get('kernels') or {}), kerns_read=list(dict.fromkeys(REC._kerns())),
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mustfail=not os.path.exists(os.path.join(D, 'b693_mustnotexist.txt')),
        fj=jl('b693_findings.json'), tj=jl('b693_trail.json'), sc=jl('b693_scores.json'), desk=rd('b693_desk_notes.txt'), tfj=jl('b693_table_final.json'),
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
    if 'rules' in need:
        S['ra'] = RA.sources('b693', SESSION, K.ANCHOR, K.PARTS, S['lock_epoch'], PRE['relay'], PRE['pp'])
        # ### the resume session's calls beside the first session's (the reboot): the shared reader called once more, unedited
        for path, anc in SESSIONS_AFTER:
            S['ra']['calls'] = sorted(S['ra']['calls'] + (RA.transcript(path, anc) if os.path.exists(path) else []), key=lambda c: c['ts'])
    else:
        S['ra'] = {}
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
            if f.startswith(('b693_', 'audit_b693_')) and os.path.isfile(os.path.join(D, f)) and not f.endswith(('.gz', '.png', '.jsonl')):
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


STEPZERO_FAILING = {'test_chain_page.py': ['(1)', '(9)', '(14)'], 'test_chain_page_b638.py': ['(4)', '(5)', '(6)', '(7)'],
                    'test_g_chain_page.py': ['(1)']}


def tests_ok(S):
    j = S['tests']
    names = sorted(S['tracked_tests'])
    nf = dict((n, x['failing']) for n, x in j.items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(j) == sorted(set(names) - {'test_elab_reader_b634.py'}) and nf == STEPZERO_FAILING \
        and 'b690_nodes_zeta.txt' in (j.get('test_chain_page.py') or {}).get('args', []) \
        and 'test_elab_reader_b634.py' in S['withheld'] \
        and ('TEST FILES %d ; RUN %d ; WITHHELD 1 ; NOT CLEAN 3' % (len(names), len(names) - 1)) in unwrap(S['testst'])


UNANSWERED = "The user doesn't want to proceed with this tool use"


def _post_seal_named(face):
    m = re.search(r'### POST-SEAL PROMPTS NAMED: (NONE|\d+)', face)
    return 0 if not m or m.group(1) == 'NONE' else int(m.group(1))


def answers_ok(S):
    a = S['answers']
    m = re.search(r'^### b693 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
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
    import b693_record as REC
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


# ================================================================== (R303) STEP ZERO: THE CITATION CHECK, THE BRANCHES
READFIRST_NEEDLES = ('relay data/b692_closing.txt :1', 'relay data/b692_defects.txt :5-:60', 'relay data/b692_circuit_dominance.txt :21',
                     'relay data/b692_circuit_spec.txt :7-:46', 'relay data/b692_parts_probe.txt :16, :21', 'relay data/b692_tool_repairs.txt :5-:13',
                     'relay tools/b692_closing.py :115', 'relay tools/push_gated.sh :4', 'relay tools/rule_arms.py :480-:486',
                     'relay data/b670_licensed_table.txt :89-:123', 'relay data/b674_rules.txt :8-:11', 'relay data/b690_rules.txt :9',
                     'relay data/b684_rules.txt :5-:12', 'relay data/b691_cut.txt :22-:27', 'relay tools/correspondence_gen.py :241-:247',
                     'relay data/b692_closing_push_out.txt')
NAMED_LOCAL = sorted(b for _r, bs in K.DELETE for b in bs)
NAMED_ALL = NAMED_LOCAL


def readfirst_ok(S):
    z = unwrap(S['readfirst'])
    return bool(z) and all(x in z for x in READFIRST_NEEDLES) and 'ITEMS 17 ; READ AT HEAD 17' in z


def branches_ok(S):
    """the eight names gone from relay, PLACE-papers and SIDE-explicit-formula, and the branches bank's verdict."""
    z = S['branchest']
    left = dict((r, sorted(x.strip() for x in v.split(NL) if x.strip())) for r, v in S['branch_lists'].items())
    return all(v == [] for v in left.values()) and len(left) == 3 and all(b in z for b in NAMED_LOCAL) \
        and 'NAMED 8 (MERGED 8) ; UNNAMED OF b692 0' in unwrap(z)


def branches_banked_ok(S):
    import b693_record as REC
    rows = S['branchj'].get('rows') or []
    try:
        fates = [REC.read_branch_row(r) for r in rows]
    except Exception:
        return False
    return len(rows) == 8 and all(f == 'DELETED' for _b, f in fates) and all(r['merged'] for r in rows) and all(r['where'] == 'local' for r in rows)


def deletes_one_ok(S):
    import b693_record as REC
    shapes = [REC.delete_shape(r['cmd']) for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell')]
    shapes = [s for s in shapes if s[0]]
    return bool(shapes) and all(len(d) == 1 and not gl and not vs for d, gl, vs in shapes) and sorted(x for d, _g, _v in shapes for x in d) == NAMED_ALL \
        and 'BRANCH DELETES OF ONE BRANCH, NO GLOB AND NO VARIABLE 8 OF 8' in S['cmdt']


def dry_step_ok(S):
    g = S['gate']
    return '--- THE DRY-RUN STEP ((R267)(2))' in g and 'ENTRY : table cells NONE ; screens QUIET' in g and 'TRAIL : table cells NONE ; screens QUIET' in g \
        and '### ### **THE DRY-RUN STEP : CLEAN**' in g and '### ### **GATE VERDICT : CLEAR**' in g


def closing_dry_ok(S):
    g = S['gate']
    return '--- THE CLOSING DRY-RUN STEP (b675 rules row 1)' in g and '### ### **THE CLOSING DRY-RUN STEP : CLEAN**' in g \
        and 'b693 closed:' in g and 'the misses as the bank lists them' in g and '### THE RE-CUT' in g and '### THE PARTS' in g \
        and '### THE KERNELS' in g and 'relay push-b693-root' in g and '(g) The defects (a)' in g and '### NO VERDICT LINE' not in g


def citation_ok(S):
    """the citation check's bank (the gate step at step zero): every cite checked, OK and misses summing; each miss raised to the author before
    the component that cites it -- the answers banked (relay 602b88c3) before Component 1's first commit -- and none repaired silently."""
    c = S['citation']
    m = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', c)
    raised = 'THE MISSES, EACH RAISED TO THE AUTHOR BEFORE THE COMPONENT THAT CITES IT RUNS (none repaired silently):' in c
    return bool(m) and int(m.group(1)) == int(m.group(2)) + int(m.group(3)) > 0 and 'A GATE STEP AT STEP ZERO' in c \
        and int(m.group(3)) == len(S['cit_misses']) == 2 and raised and bool(S['t'].get('answers')) and bool(S['t'].get('c1')) \
        and S['t']['answers'] <= S['t']['c1']


def rowgen_ok(S):
    return '### ### **CONSTELLATION EXIT 0 ; ROWGEN DIFF EXIT 0 ; TABLES 19.**' in S['rowgen']


def weight_ok(S):
    return landed(S, 0, ['b692 AT ITS WEIGHT', 'cb41d267'])


def _first_ts(S, needle):
    ts = [iso_epoch((r.get('ts') or '')[:19] + 'Z') for r in S['cmds'] if needle in r['cmd']]
    ts = [t for t in ts if t]
    return min(ts) if ts else None


def answers_checked_ok(S):
    """the citation bank's mid-act prints read at HEAD, at or above the sealed floor, each before the write its answer governs: the weight
    line's landing, the closing tool's repair, the act-root verify's range, the branch mode's push of push-b693-root."""
    c = S['citation']
    stamps = re.findall(r'### \(R278\)\(4\) THE MID-ACT CHECK \((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\): the answer carrying \'([^\']+)\'', c)
    acts = dict((n, iso_epoch(t)) for t, n in stamps)
    gov = (('both from the banks', S['t'].get('c1')), ('the closing tool', S['t'].get('repairs')), ('the chain split by act', S['t'].get('parts')),
           ('push-b693-root pushed alone', _first_ts(S, '--branch ' + K.BRANCH_MODE_BRANCH)))
    return len(stamps) >= FLOORS['checks'] and all(any(k in n for n in acts) and w and max(v for n, v in acts.items() if k in n) < w for k, w in gov)


# ================================================================== (R303)(1)-(4): THE CORRIGENDUM, THE REPAIRS, THE RE-CUT, THE PARTS
def _fn_src(src, name):
    if ('\ndef %s(' % name) not in src:
        return ''
    i = src.index('\ndef %s(' % name) + 1
    m = re.search(r'\n(?=\S)', src[i + 1:])
    return src[i:i + 1 + m.start() + 1] if m else src[i:]


def scorer_banks_ok(S):
    """data/b686_rules.txt row (1), standing: the N1-N5 scorers' code reads banks and commits and no ledger and no findings bank; the scores
    route writes its bank once; the entry's composer takes its scores line from the scores bank."""
    n = ''.join(strip_prose(_fn_src(S['rec_src'], f)) for f in ('_n1', '_first_prerun_epoch', '_n2', '_n3', '_n4', '_vl'))
    sc = strip_prose(_fn_src(S['rec_src'], 'scores'))
    ft = strip_prose(_fn_src(S['rec_src'], '_finding_text'))
    return bool(n) and 'b693_tie.txt' in n and 'b693_cut.txt' in n and 'b693_corrigendum.txt' in n and 'b693_range_exercise.txt' in n \
        and not re.search(r'\b(FIND|OT)\b|FINDINGS|OPEN_TRAILS|findings|entry_line', n) \
        and "os.path.isfile(os.path.join(D, 'b693_scores.json'))" in sc and 'scores_line(S)' in ft and "jl('b693_scores.json')" in ft


def _entry_block(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    if not e:
        return ''
    end = next((i for i in range(e, len(ls)) if ls[i].startswith('## ')), len(ls))
    return NL.join(ls[e - 1:end])


def entry_scores_ok(S):
    import b693_record as REC
    want = conv(REC.scores_line(S['sc'])) if S['sc'] else None
    blk = _entry_block(S)
    got = [l for l in blk.split(NL) if l.startswith('**The scores.**')]
    return bool(want) and bool(S['sc']) and got == [want]


def entry_title_ok(S):
    e = S['fj'].get('entry_line')
    return bool(e) and S['REC']._title() == K.TITLE and fline(S, e) == conv(K.TITLE)


LOAD = 'Zeta23.reflect (825), Zeta23.ZeroConfig.mk (716), Zeta23.ZeroConfig (716)'


def corrigendum_ok(S):
    ls = S['corrland'].get('lines') or []
    x = ls[0] if ls else {}
    return len(ls) == 1 and x.get('line') == K.CORRIGENDUM_LINE and fline(S, K.CORRIGENDUM_LINE) == conv(x.get('head') or '\x00') \
        and ('LOAD is led by ' + LOAD) in fline(S, K.CORRIGENDUM_LINE + 2) and 'the factor is 1.53' in fline(S, K.CORRIGENDUM_LINE + 2) \
        and LOAD in ' '.join(S['d692'].split()) and 'THE ENTRY AT FINDINGS :%d' % K.CORRIGENDUM_LINE in S['corr'] \
        and '  (7) ' in S['corrigenda']


def range_ok(S):
    """(R303)(2) on the author's word: the closing tool's carried-forward row computed by defects_row through the record tool's DEFECT_ROW, no
    fixed range left; its exercise bank reading b692's thirteen as (a)-(m) and the control b691's as (a)-(k)."""
    src = strip_prose(S['closing_src'])
    fn = _fn_src(src, 'defects_row')
    return 'REC.DEFECT_ROW' in fn and "defects_row('b693', 'g')" in src and '(a)-(k)' not in src \
        and "b692's BANK READ AS (a)–(m), THE RULED EXCEPTION (i), THE NAVIGATOR'S (j)–(k) ; THE CONTROL b691 READ AS (a)–(k)" in S['range_ex']


def branch_mode_tested_ok(S):
    s = S['push_src']
    return S['push_blob'].startswith('e7410053') and '--branch' in s and '--scratch' in s and 'exit 11' in s and 'exit 12' in s \
        and 'THE TEST 52 OF 52' in S['branch_mode'] and '  (3) tools/push_gated.sh, d7c39c5b -> e7410053' in S['repairs']


def branch_mode_exercised_ok(S):
    """the one exercise on the author's word: push-b693-root pushed alone by the branch mode, its capture banked with the read-back, before
    main is pushed from it by the main mode."""
    b, m = S['root_branch_push'], S['root_push']
    br = re.search(r'push_gated: branch %s read back at the remote: ([0-9a-f]{40})' % re.escape(K.BRANCH_MODE_BRANCH), b)
    mr = re.search(r'push_gated: main read back at the remote: ([0-9a-f]{40})', m)
    return ('; branch mode ; branch %s ;' % K.BRANCH_MODE_BRANCH) in b and ('DONE -- branch %s pushed alone and read back' % K.BRANCH_MODE_BRANCH) in b \
        and bool(br) and bool(mr) and br.group(1) == mr.group(1)


def tie_ok(S):
    t = S['tie']
    return '### b674`S TIE-BREAK RULE, VERBATIM FROM relay data/b674_rules.txt :8-:11:' in t and '### THE KERNEL ROWS, VERBATIM' in t \
        and "THE NEXT DOCUMENT BY b652`S ORDER: SIDE-archimedean AT 2, ALONE AT THE TOP COUNT ; b674`S TIE-BREAK NOT REACHED." in t \
        and [f for f in S['files']['tie'] if f.startswith('data/')] == ['data/b693_tie.json', 'data/b693_tie.txt'] and bool(S['t'].get('tie')) and bool(S['t'].get('named')) \
        and S['t']['tie'] <= S['t']['named']


def cut_merged_ok(S):
    m = S['mainst']
    return m['main'] == K.ARCH_MERGE and m['line'] == [K.ARCH_WF, K.ARCH_PT, K.ARCH_MERGE] and m['parents'] == [K.ARCH_PT, K.ARCH_CUT] \
        and m['files'] == {K.ARCH_WF: [WF], K.ARCH_PT: [PT], K.ARCH_CUT: [CUT_FILE]} and m['tag'] == K.ARCH_MERGE and m['prior'] == K.ARCH_BEFORE \
        and m['tags'] == [K.ARCH_TAG] and m['trees'][0] == m['trees'][1] and bool(m['trees'][0]) and 'v0.1.0' in m['tagmsg']


def quote_ok(S):
    q = S['quote']
    return 'REMOVED OR CHANGED LINES 11 ; NEEDLES SEARCHED 11 IN TWO SHAPES ; QUOTING LINES 3 -- EACH ENTERED AS A RESIDUE.' in q \
        and '### the control FIRES FOR EVERY NEEDLE IN BOTH SHAPES' in q and 'data/b693_quote_archimedean.txt' in S['files']['quote'] \
        and bool(S['t'].get('quote')) and bool(S['t'].get('merge')) and S['t']['quote'] <= S['t']['merge'] \
        and len(re.findall(r'^  R-\d  ', S['cut'], re.M)) == 3


def distance_ok(S):
    j = S['cutj']
    rows = j.get('rows') or []
    return 'THE DISTANCE BEFORE 2, AFTER 0' in S['cut'] and j.get('before') == 2 and j.get('after') == 0 and len(rows) == 2 \
        and all(r.get('applied') for r in rows) and 'EQUAL LINE FOR LINE True' in S['prints_arch'] and 'data/b693_cut.txt' in S['files']['cut']


def cells_ok(S):
    return 'HELD, NONE WRITTEN' in S['cells'] and 'THE :301 CLAUSE CARRIED' in S['cells'] and not [x for x in S['pp_changed'] if 'PATHS_TO_THE_CRITICAL_LINE' in x]


def readfirst_diff_ok(S):
    return 'THE HAND LIST 26 PATHS ; THE TEXT CITES 21 ; BOTH 15 ; LINES DIFFERING 17' in S['rf_diff'] and 'No bank is rewritten by this reading.' in S['rf_diff'] \
        and 'data/b693_readfirst_diff.txt' in S['files']['stepzero'] and S['rf_hand_now'] is not None and S['rf_hand_now'] == S['rf_hand_z']


def parts_probe_ok(S):
    pr = utc_epoch(S['prerun'], 'run at (UTC)') or utc_epoch(rd('b693_arms_prerun_standing-a.txt'), 'run at (UTC)')
    return S['rule_blob'] == '3f183f15d44c16fb0d4961f6ea57765c92f35481' and 'THE SIX-PART RUN PASS' in S['parts_probe'] \
        and 'THE PLANTED CONTROL FAIL' in S['parts_probe'] and 'data/b693_parts_probe.txt' in S['files']['parts'] \
        and bool(S['t'].get('parts')) and bool(pr) and S['t']['parts'] <= pr


def chain_range_ok(S):
    r = S['repairs']
    return S['ar_blob'].startswith('d10756fc') and '  (6) tools/act_root.py, 5b8b3d74 -> d10756fc' in r and '"10 of 10"' in r \
        and '  (7) tools/test_act_root.py, cab4c911 -> 7a9a4c55' in r and 'tools/act_root.py' in S['files']['parts']


def chain_control_ok(S):
    c = S['chain_control']
    return 'THE THREE EQUAL True' in c and 'THE BOUNDARY b658 -> b659 EQUAL True' in c and re.search(r'THE WHOLE CHAIN b624-b693 IN THE OLD FORM: 70 ACTS, AGREE 70', c) is not None


def resume_ok(S):
    r = S['resume']
    return S['files']['resume'] == ['data/b693_resume.txt'] and S['resume_parent'] == K.PARTS_RELAY \
        and 'THE ACT CONTINUES FROM C4' in r and 'CHECKS 4 OF 4 OK' in r \
        and re.search(r'THE HOST REBOOT\s+between relay 0574078e \(b693 C3, the last commit before it[^)]*\) and relay 91c2df0c', S['defects']) is not None


def repairs_ok(S):
    return ('### ### **REPAIRS 10 ; THE SEALED COPIES AGREE ; TOOLS CARRIED 10 OF 10 ; THE STANDING INSTRUMENTS UNEDITED True ; THE REPAIRED SHARED '
            'TOOLS` ROWS ABOVE 7') in S['repairs']


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


# ================================================================== THE RUNNER (the standing arms, this act's two runs, its one merge)
IDENT_WF = ('secrets.', 'psinary', 'seale', 'york', 'hotmail', 'orcid', '0009-0008')


def wf_ok(S):
    """the one kernel workflow the act wrote: at main equal to the act's own write, no author identifier, no secret, the hold, the lake path
    and the cache step its lakefile's Mathlib requires, the print step over its list, the files the act wrote on main."""
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
    return sorted(S['wf']) == [K.ARCH]


def runner_ok(S):
    """this act's two runs through its record tool's reader: each at its own ref, success, the artifact's sha256, the memory low above the
    hold."""
    import b693_record as REC
    rows = S['runner'].get('rows') or []
    want = dict((lab, gs(ARCH, 'rev-parse', ref)) for lab, ref in K.RUNNER_LABELS)
    try:
        for r in rows:
            REC.read_runner_row(r)
    except Exception:
        return False
    return len(rows) == 2 and sorted(r['label'] for r in rows) == sorted(want) and all(r['kernel'] == K.ARCH and r['ref'] == want[r['label']] for r in rows) \
        and all(r['conclusion'] == 'success' and r['artifact_sha256'] and r['mem_low'] is not None and r['mem_low'] >= K.HOLD and not r['stopped']
                for r in rows)


def gate_ok(S):
    bs = S['rbanks']
    return len(bs) == 2 and all('GATE DERIVES' in t and 'BUILD EXIT 0 ; ERROR LINES 0' in t and 'SORRYAX 0' in t
                                and re.search(r'^### the artifact: .* ; AGREE$', t, re.M) for t in bs.values())


def merges_ok(S):
    """this act's one merge: SIDE-archimedean's main at the merge, its first parent the print list's commit and its second the gated tip (the
    after run's ref), the merged tree the built tree, the tag v0.1.1 peeled to the merge and v0.1.0 unmoved, no other tag."""
    m = S['mainst']
    after = [r for r in (S['runner'].get('rows') or []) if r.get('label') == 'after']
    return m['main'] == K.ARCH_MERGE and m['parents'] == [K.ARCH_PT, K.ARCH_CUT] and bool(after) and after[0]['ref'].startswith(K.ARCH_CUT) \
        and m['trees'][0] == m['trees'][1] and m['tag'] == K.ARCH_MERGE and m['prior'] == K.ARCH_BEFORE and m['tags'] == [K.ARCH_TAG]


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


POST_SEAL = ('b693 seal', 'b693 pre-root', 'b693 root', 'b693 record', 'b693 --', 'b693 closing', 'b693 entry')


def _component_commit(s):
    return s.startswith('b693') and not s.startswith(POST_SEAL)


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
    return bool(j) and len(rows) == 70 and rows[69][:3] == ['b693', j.get('root'), j0.get('root')] \
        and AR.root_of(items, j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) \
        and not [it for it in items if 'b628_intake_crank' in it or 'b647_navigator_memory' in it or 'b694_' in it or 'mirror' in it
                 or 'chain_' in it or it.split()[0].endswith(('.gz', '.png', '.jsonl'))] \
        and any(it.startswith('data/b693_cut.txt ') for it in items) and any(it.startswith('data/b693_resume.txt ') for it in items) \
        and all(any(it.startswith(p + ' ') for it in items) for p in K.SHARED_APPENDED) and (j.get('commit') or {}).get('relay')


def root_banks_committed_ok(S):
    rb, rows = S['rootbanks'], S['root_at_commit']
    commit = (S['arj'].get('commit') or {}).get('relay') or ''
    return bool(rb) and rb.get('clean') is True and rb.get('pushed') is True and rb.get('head') == commit and bool(rows) \
        and all(c and e for _b, c, e in rows) and sorted(b for b, _c, _e in rows) == sorted(r['bank'] for r in rb.get('rows') or [])


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b693_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    """G-ACTROOT-VERIFY, counted once in standing-b3 (the author's word): the first half's verdicts banked by standing-b2 at this same HEAD, the
    second half's computed here, together b624 to b693 AGREE; the boundary link equal in both halves' reading; b680 read through its
    corrigendum row (4 banks); b693 written LF."""
    ha = S['half_a'] or {}
    v = [tuple(x[:2]) for x in (ha.get('acts') or [])] + [tuple(x[:2]) for x in (S['ar_verify'] or [])]
    r = dict(ha.get('reads') or {}, **(S['ar_reads'] or {}))
    return ha.get('head') == gs(ROOT, 'rev-parse', 'HEAD') and [x[0] for x in v] == ['b%d' % i for i in range(624, 694)] \
        and all(x[1] == 'AGREE' for x in v) and (r.get('b693') or {}).get('crlf') == 0 and (r.get('b680') or {}).get('corrected') == 4 \
        and (ha.get('boundary') or {}).get('equal') is True and S['boundary'].get('equal') is True \
        and (ha.get('boundary') or {}).get('root') == S['boundary'].get('root')


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**The citation check**', '**The corrigendum**', '**The repairs**', '**The naming**', '**The cut**', '**The quotation search**',
                 '**The Correspondence cells**', '**The parts**', '**The reboot**', '**The scores.**', '**Read in mutual light**', 'strengthens',
                 '**Carried to:**', '**Next.**', 'b694')


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
    import b693_record as REC
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
    return S['pp_changed'] == S['pp_allowed']


def closing_sentence_ok(S):
    t = S['closing_src']
    return ('no identifier of the author ' + 'in any outbound') in t and ('plain requests to ' + 'github.com') in t \
        and '### THE CITATION CHECK' in t and '### THE RECORD LINES' in t and '### THE DRY RUN' in t and '### THE CORRIGENDUM AND THE REPAIRS' in t \
        and '### THE RE-CUT' in t and '### THE PARTS' in t and '### THE KERNELS' in t and '### THE MIRROR' in t and '### THE CARRY-TIME' in t


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
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R303) END' in S['ferry'] and S['ferry'].rstrip().endswith(K.TAIL),
     lambda S: put(S, 'ferry', S['ferry'].replace(K.TAIL, ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the step-zero bank: tail, lean, lake, python and claude named, the seat`s claude alone, none of the others; no task stopped, no orphan, nothing stopped by PID',
     lambda S: procs_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('python 0', 'python 1'))),
    ('G-STEPZERO-TESTS', 'the tests bank against the test files tracked before the act, test_elab_reader_b634.py withheld (no lean on this host), run against the list the page names',
     lambda S: tests_ok(S), lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: S['pushout'][0] == ['data/b692_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'relay`s, PLACE-papers` and SIDE-explicit-formula`s branch lists by the ruling`s eight names, and the branches bank',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{'D:/relay': 'push-b692'}))),
    ('G-READFIRST-CITED', 'the read-first bank: every item of the ferry`s list cited by path and line', lambda S: readfirst_ok(S),
     lambda S: put(S, 'readfirst', '')),
    ('G-ANSWERS-BANKED', 'the answers bank read at HEAD: its prompts and calls at or above the sealed floors, each with its options and result, any call after the lock named on the face',
     lambda S: answers_ok(S), lambda S: put(S, 'answers', S['answers'].replace('### PROMPT 1 (', '### PROMPTED ('))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-EXPORT-UNTRACKED', 'the navigator`s export: present, untracked, in no commit', lambda S: S['export_present'] and S['export_log'] == ''
     and S['export_index'] == '' and S['export_status'].startswith('??'), lambda S: put(S, 'export_index', EXPORT)),
    ('G-EDIT-ROUTE', 'the record tool`s one reading (tools/edit_route.py`s arms and sed in any form) over this act`s whole capture -- both sessions -- and the previous act`s after its post-push suite, read live',
     lambda S: edit_route_ok(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -n 1p tools/b693_record.py")])),
    ('G-NO-LOCAL-LEAN', 'the act`s command capture over both sessions, read live: no command runs lean or lake on this host (N1)', lambda S: no_local_lean(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd='lake env lean SIDEArchimedean/Reflection.lean')])),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line, found by conv', lambda S: weight_ok(S), lambda S: _rl(S, 0, 1)),
    ('G-DRY-STEP-CLEAN', 'the gate`s record: the dry-run step run, the entry and the trail record quiet under their screens, CLEAN printed, the gate CLEAR',
     lambda S: dry_step_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE DRY-RUN STEP : CLEAN', 'THE DRY-RUN STEP : NOT CLEAN'))),
    ('G-CLOSING-DRY-STEP', 'the gate`s record: the closing run dry before the lock, its head line, citation line, re-cut, parts and kernels lines, the branch mode`s row and the defects row printed (b675 rules row 1)',
     lambda S: closing_dry_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE CLOSING DRY-RUN STEP : CLEAN', 'THE CLOSING DRY-RUN STEP : NOT CLEAN'))),
    ('G-CITATION-CHECKED', 'the citation check`s bank (the gate step at step zero): every cite checked, its two misses raised to the author by the answers banked before Component 1, none repaired silently',
     lambda S: citation_ok(S), lambda S: put(S, 'citation', S['citation'].replace('CITES CHECKED 89 ; OK 87 ; MISSES 2', 'CITES CHECKED 89 ; OK 86 ; MISSES 3'))),
    ('G-R303-ENTERED', 'the ferry and the trail', lambda S: 'RULING (R303) END' in S['ferry'] and S['ot'].count('**(R303) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R303) ratified', '**(R3030) ratified'))),
    ('G-ROWGEN-STEPZERO', 'the rowgen bank: constellation and the build-free diff over the 19 roster tables, both exit 0 (b670 rules row 3)',
     lambda S: rowgen_ok(S), lambda S: put(S, 'rowgen', S['rowgen'].replace('ROWGEN DIFF EXIT 0', 'ROWGEN DIFF EXIT 1'))),
    ('G-BRANCHES-BANKED', 'the branches bank: the eight named rows deleted through the record tool`s reader, each merged, each local',
     lambda S: branches_banked_ok(S), lambda S: _mut(S, 'branchj', lambda d: d['rows'][0].update(fate='GONE'))),
    ('G-DELETES-ONE-BRANCH', 'the command capture by the record tool`s reader and the command bank: each branch delete naming one branch, no glob in any half, the ruling`s eight exactly',
     lambda S: deletes_one_ok(S), lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="git branch -d push-b692 push-b692-root")])),
    ('G-ANSWERS-CHECKED', 'the citation bank`s mid-act prints read at HEAD, each before the write its answer governs: the weight line, the closing tool`s repair, the chain split, the branch mode`s exercise',
     lambda S: answers_checked_ok(S), lambda S: put(S, 't', dict(S['t'], repairs=1))),
    ('G-SCORER-READS-BANKS', 'tools/b693_record.py`s code, prose stripped: the N1-N5 scorers reading banks and commits and no ledger, the scores bank written once, the entry`s scores line from it',
     lambda S: scorer_banks_ok(S), lambda S: put(S, 'rec_src', S['rec_src'].replace("def _n2():", "def _n2():\n    _x = rd(FIND)"))),
    ('G-ENTRY-SCORES-EQUAL', 'FINDINGS at the findings bank`s line and the scores bank: the entry`s scores line equal to the line composed from the bank',
     lambda S: entry_scores_ok(S), lambda S: _mut(S, 'sc', lambda d: d.update(N1=['REFUTED', 'planted']))),
    ('G-ENTRY-TITLE-FORM', 'FINDINGS at the findings bank`s line, the record tool`s title from the tie, cut and corrigendum banks, and the worklist`s: the ferry`s form adjusted',
     lambda S: entry_title_ok(S), lambda S: put(S, 'find', S['find'].replace(conv(K.TITLE), conv(K.TITLE).replace('to 0,', 'to 1,')))),
    ('G-CORRIGENDUM-ENTERED', 'FINDINGS at the corrigendum`s landed line by conv, its LOAD names and figures and the factor beneath, b692`s defects bank (m) and the corrigenda bank`s row (7) (N4)',
     lambda S: corrigendum_ok(S), lambda S: put(S, 'd692', ' '.join(S['d692'].split()).replace('Zeta23.ZeroConfig.mk (716)', 'Zeta23.ZeroConfig.mk (717)'))),
    ('G-RANGE-FROM-BANK', 'tools/b693_closing.py, prose stripped: the carried-forward row from defects_row through the record tool`s DEFECT_ROW, no fixed range; the exercise bank b692 (a)-(m), b691 (a)-(k) (N4)',
     lambda S: range_ok(S), lambda S: put(S, 'closing_src', S['closing_src'] + NL + "X = '(a)-(k)'")),
    ('G-BRANCH-MODE-TESTED', 'tools/push_gated.sh`s blob and source (the branch mode, --scratch, exits 11 and 12), the branch-mode bank`s test 52 of 52 and the repairs bank`s row (3)',
     lambda S: branch_mode_tested_ok(S), lambda S: put(S, 'branch_mode', S['branch_mode'].replace('THE TEST 52 OF 52', 'THE TEST 51 OF 52'))),
    ('G-BRANCH-MODE-EXERCISED', 'the pre-root captures: push-b693-root pushed alone by the branch mode with its read-back, then main by the main mode (the author`s word, prompt 4)',
     lambda S: branch_mode_exercised_ok(S), lambda S: put(S, 'root_branch_push', '')),
    ('G-TIE-PRINTED', 'the naming bank: b674`s rule and the kernel rows verbatim, the verdict, its commit alone and before the document`s first write (N2)',
     lambda S: tie_ok(S), lambda S: put(S, 't', dict(S['t'], tie=(S['t'].get('named') or 0) + 1))),
    ('G-CUT-MERGED', 'SIDE-archimedean`s main: the workflow and the print list each alone, the cut alone on its branch, the merge`s parents, the merged tree the built tree, v0.1.1 at the merge naming v0.1.0',
     lambda S: cut_merged_ok(S), lambda S: _mut(S, 'mainst', lambda d: d.update(trees=('a', 'b')))),
    ('G-QUOTE-BEFORE-MERGE', 'the quotation bank: eleven needles in two shapes, the control firing, three quoting lines entered as residues in the cut bank, its commit before the merge (N3)',
     lambda S: quote_ok(S), lambda S: put(S, 't', dict(S['t'], quote=(S['t'].get('merge') or 0) + 1))),
    ('G-DISTANCE-READ', 'the cut bank and its rows: the distance by the b670 method 2 before, 0 after, both ACTIONs applied; the prints equal line for line (N3)',
     lambda S: distance_ok(S), lambda S: _mut(S, 'cutj', lambda d: d.update(after=1))),
    ('G-CELLS-HELD', 'the generator`s dry bank and PLACE-papers` changed files: the three cells held, none written, the :301 clause carried (N3)',
     lambda S: cells_ok(S), lambda S: put(S, 'pp_changed', S['pp_changed'] + ['phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md'])),
    ('G-READFIRST-DIFF-BANKED', 'the readfirst diff bank and the step-zero commit, and the hand list`s blob at HEAD against step zero`s: the diff banked, no bank rewritten',
     lambda S: readfirst_diff_ok(S), lambda S: put(S, 'rf_hand_now', b'x')),
    ('G-PARTS-PROBE-READ', 'the parts probe bank and tools/rule_arms.py`s blob: the six-part run read PASS in memory, the planted control FAIL, committed before the suite`s first part (N2)',
     lambda S: parts_probe_ok(S), lambda S: put(S, 'rule_blob', 'x')),
    ('G-CHAIN-RANGE-REPAIRED', 'tools/act_root.py`s blob and the repairs bank`s rows (6)-(7): verify given an act range, its test 10 of 10, committed at Component 3',
     lambda S: chain_range_ok(S), lambda S: put(S, 'ar_blob', 'x')),
    ('G-CHAIN-CONTROL', 'the whole-chain control bank, this act alone: the chain in the old form beside the two halves` banked verdicts, the boundary equal, the three equal',
     lambda S: chain_control_ok(S), lambda S: put(S, 'chain_control', S['chain_control'].replace('THE THREE EQUAL True', 'THE THREE EQUAL False'))),
    ('G-RESUME-BANKED', 'the resume bank committed alone as the first commit after the reboot, its state rows, the four checks, and the reboot entered as an event in the defects bank',
     lambda S: resume_ok(S), lambda S: put(S, 'resume_parent', 'deadbeef')),
    ('G-TOOL-REPAIRS', 'the repairs bank`s verdict: ten carry-time repairs, the sealed copies agreeing, ten tools carried, the standing instruments unedited, the seven repaired shared tools` rows above',
     lambda S: repairs_ok(S), lambda S: put(S, 'repairs', S['repairs'].replace('REPAIRS 10 ;', 'REPAIRS 0 ;'))),
    ('G-PARTS-PRERUN', 'the pre-run bank`s six parts with their seconds, named in the form the parts arm reads',
     lambda S: parts_ok(S), lambda S: put(S, 'prerun', S['prerun'].replace('PART standing-b3', 'PART standing-x'))),
    ('G-ARM-SECONDS-BANKED', 'the per-arm seconds bank: every standing arm clocked at the pre-run, the three slowest named, each part`s seconds',
     lambda S: arm_seconds_ok(S), lambda S: _mut(S, 'asec', lambda d: d.update(clocked=0))),
    ('G-DEFECTS-LETTERED', 'the defects bank read at HEAD: the sealed letters its prefix, consecutive letters, owners the seat or the navigator',
     lambda S: defects_ok(S), lambda S: put(S, 'defects', S['defects'].replace("(a) THE SEAT'S", "(a) THE AUTHOR'S"))),
    ('G-SPEC-PLANTED', 'tools/b693_regspec.py`s planted rows run live through the record tool`s readers, and rows of another shape refused',
     lambda S: bool(S['spec']['read']) and all(S['spec']['read']) and all(S['spec']['controls']) and any('branch' in x for x in S['spec']['shapes']),
     lambda S: _mut(S, 'spec', lambda d: d['controls'].append(False))),
    ('G-CONVERSION-ONE', 'every b693 tool`s code and the repaired shared tools`: no conversion defined (conv imported from b652_record); the suite importing it',
     lambda S: S['conv_bad'] == [] and 'from b693_record import conv' in S['suite'], lambda S: put(S, 'conv_bad', ['b693_checks.py'])),
    ('G-WORKFLOW-FILES', 'SIDE-archimedean`s workflow at main: equal to the act`s own write at 79a8527, no author identifier, no secret, the hold, the lake path and the cache, the print step over its list, the files the act wrote',
     lambda S: wf_ok(S), lambda S: _mut(S, 'wf', lambda d: d[K.ARCH].update(text=d[K.ARCH]['text'] + ' secrets.X'))),
    ('G-RUNNER-READ', 'this act`s two runs through its record tool`s reader: each at its own ref, success, the artifact`s sha256, the memory low above the hold',
     lambda S: runner_ok(S), lambda S: _mut(S, 'runner', lambda d: [r.update(mem_low=2000) for r in d['rows']])),
    ('G-RUNNER-GATE', 'this act`s two runs` gate readings: build exit 0, no error line, no sorryAx in the print step, the artifact`s digest agreeing',
     lambda S: gate_ok(S), lambda S: put(S, 'rbanks', dict(S['rbanks'], **{'x_after': 'GATE NOT DERIVES'}))),
    ('G-MERGES-ON-GATE', 'SIDE-archimedean`s main: the merge`s second parent the gated tip, the merged tree the built tree, v0.1.1 at the merge, v0.1.0 unmoved, no other tag',
     lambda S: merges_ok(S), lambda S: _mut(S, 'mainst', lambda d: d['tags'].append('v0.2'))),
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
    ('G-PP-SCOPE', 'PLACE-papers` changed files against FINDINGS and OPEN_TRAILS',
     lambda S: corpus_scope(S), lambda S: put(S, 'pp_changed', S['pp_changed'] + ['day1/ONE_PAGE_PROOF.md'])),
    ('G-CURRENTS-UNEDITED', 'the map, the census, the monograph, the faces page, the Dirichlet page, the surround, SIMPLICITY, README, REGISTRY, FOUNDATIONS and its one-copy partner, INSTRUMENTS and the paths pages: working tree, before and HEAD',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'ERRATA.md': (b'x', b'y', b'y')}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read before the seal',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b692`s and the earlier tools, the generator and its test, the rule arms, b672`s record tool, rowgen`s, edit_route.py, chain_page.py, e0_rule.py, the mirror`s, repair_snapshot.py and the shared tools -- the repaired tools apart: before, working tree and HEAD',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'additive_shared.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 1749abbb but the shared additive files (act_roots.txt and the corrigenda bank among them), by blob id',
     lambda S: S['prior_bad'] == [] and S['prior_n'] > 0, lambda S: put(S, 'prior_bad', ['data/b692_stepzero.txt'])),
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
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b693 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now, the repaired shared tools among them', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'push_gated.sh': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3), in six parts summed',
     lambda S: S['lock_epoch'] is not None and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b692`s trail record on OPEN_TRAILS and its root in the chain', lambda S: '### b692 — lane two, act one hundred and nineteen, the research act' in S['ot']
     and S['rootsf'].count(NL + 'b692 ') == 1, lambda S: put(S, 'ot', S['ot'].replace('### b692 — lane two', '### b692 - lane two'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], grade_moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 70th chain row (the corrigendum row apart), the root bank and its items, the cut and resume banks among them, no binary, mirror, chain-half or untracked bank',
     lambda S: root_banked_ok(S), lambda S: put(S, 'rootsf', S['rootsf'] + 'b694 x y' + NL)),
    ('G-ROOT-BANKS-COMMITTED', 'the root route`s banked reading and every named bank`s blob at the root`s recorded commit: clean and equal at HEAD, HEAD the remote main, the recorded hash carried by the recorded commit',
     lambda S: root_banks_committed_ok(S), lambda S: put(S, 'rootbanks', dict(S['rootbanks'], pushed=False))),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit in two halves by act with the suite`s own remote reads: standing-b2`s banked b624-b658 and standing-b3`s b659-b693 all AGREE, the boundary link equal, b680 read through its corrigendum row (4 banks), b693 written LF',
     lambda S: verify_ok(S), lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s through conv, and its parts', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line, the head through conv', lambda S: bool(S['tj'].get('line'))
     and oline(S, S['tj']['line']) == conv(S['REC'].TRAIL_HEAD()), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b693 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b693_record.py agree', 'b693_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line: b694', lambda S: '**Next:** b694' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** b694', '**Next:** b695'))),
] + [('G-N%d-SCORED' % i, 'the scores through the record tool`s reader, and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i),
      lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written since 1749abbb and 62b632f against the (W) globs',
     lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b693')" in S['suite'] and "'data/b693_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b693_closing.py: the closing sentence in the rule`s words with the plain reads named; the citation check, the record lines, the dry run, the corrigendum and repairs, the re-cut, the parts, the kernels, the mirror, the carry-time reading',
     lambda S: closing_sentence_ok(S), lambda S: put(S, 'closing_src', S['closing_src'].replace('no identifier of the author ' + 'in any outbound', 'x'))),
    ('G-LSREMOTE-ONE-PER-REPO', 'the part`s ls-remote calls per repository, read after every other arm of the part has run (OPEN_TRAILS :12703)',
     lambda S: lsr_ok(S), lambda S: put(S, 'lsr', {PP: 2})),
] + [(nm, 'tools/rule_arms.py (the author`s word on (R293)(6); (R301)(6) for four; G-RULE-SUITE-PARTS as repaired under (R302)(2)), the trace over both sessions -- ' + reads,
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
    p = os.path.join(D, 'b693_seal_hashes.json')
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
    print('  written: b693_seal_hashes.json')
    return 0


def chain_control():
    """(R303)(4) on the author's word, this act alone: the whole chain verified once in the old form (act_root.verify with no range) after the
    pre-push halves, its verdicts printed beside the two halves' banked verdicts and the boundary link; the three equal or not. Writes
    data/b693_chain_control.txt (.json)."""
    import act_root as AR
    fm = free_mb()
    if fm < K.HOLD:
        print('### THE HOST`S FREE MEMORY %d MB, BENEATH THE HOLD %d MB: THE CONTROL NOT RUN' % (fm, K.HOLD))
        return 3
    key = sys.argv[sys.argv.index('--chain-control') + 1] if len(sys.argv) > sys.argv.index('--chain-control') + 1 else 'checks'
    ha, hb = jl(half_bank(0, key)), jl(half_bank(1, key))
    head = gs(ROOT, 'rev-parse', 'HEAD')
    t0 = time.time()
    try:
        whole = [list(x) for x in AR.verify(remote=KC0.remote_refs)]
    except Exception as e:
        whole = [['raised', type(e).__name__, []]]
    secs = time.time() - t0
    wv = [tuple(x[:2]) for x in whole if not str(x[0]).startswith('corrigendum')]
    av, bv = [tuple(x[:2]) for x in ha.get('acts') or []], [tuple(x[:2]) for x in hb.get('acts') or []]
    bd = boundary()
    lo, hi = K.CHAIN_HALVES[0][0], K.CHAIN_HALVES[1][1]
    want = ['b%d' % i for i in range(int(lo[1:]), int(hi[1:]) + 1)]
    same_head = ha.get('head') == hb.get('head') == head
    equal = same_head and wv == av + bv and [x[0] for x in wv] == want and all(v == 'AGREE' for _a, v in wv)
    Lc = ['b693 -- THE WHOLE-CHAIN CONTROL, (R303)(4) ON THE AUTHOR`S WORD, THIS ACT ALONE (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
          '### the whole chain verified once in the old form (tools/act_root.py verify, no act range, the suite`s own remote reads) at relay HEAD %s,' % head[:12],
          '### %.0f s; beside it the two halves` verdicts as standing-b2 and standing-b3 banked them in the run `%s` (relay data/%s, data/%s), each' % (
              secs, key, half_bank(0, key), half_bank(1, key)),
          '### read at HEAD %s and %s. Rows are acts: the whole chain`s verdict | the half`s verdict.' % ((ha.get('head') or '-')[:12], (hb.get('head') or '-')[:12]), '']
    hv = dict(av + bv)
    Lc += ['  %-6s %-9s | %s' % (a, v, hv.get(a, '### NOT IN A HALF')) for a, v in wv]
    Lc += ['', '### THE BOUNDARY (relay data/act_roots.txt): %s root %s ; %s previous %s ; equal %s ; as the first half read it %s ; as the second %s' % (
        bd['first'], bd['root'][:16], bd['second'], bd['previous'][:16], bd['equal'], (ha.get('boundary') or {}).get('equal'), (hb.get('boundary') or {}).get('equal')),
           '', '### ### **THE WHOLE CHAIN %s-%s IN THE OLD FORM: %d ACTS, AGREE %d ; THE HALVES: %s-%s %d AGREE %d, %s-%s %d AGREE %d ; THE BOUNDARY %s -> %s '
           'EQUAL %s ; THE THREE EQUAL %s.**' % (
               lo, hi, len(wv), sum(1 for _a, v in wv if v == 'AGREE'), K.CHAIN_HALVES[0][0], K.CHAIN_HALVES[0][1], len(av), sum(1 for _a, v in av if v == 'AGREE'),
               K.CHAIN_HALVES[1][0], K.CHAIN_HALVES[1][1], len(bv), sum(1 for _a, v in bv if v == 'AGREE'), bd['first'], bd['second'],
               bd['equal'] and (ha.get('boundary') or {}).get('equal') is True and (hb.get('boundary') or {}).get('equal') is True, equal)]
    p = os.path.join(D, 'b693_chain_control.txt')
    open(p + '.tmp', 'wb').write((NL.join(Lc) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)
    pj = os.path.join(D, 'b693_chain_control.json')
    open(pj + '.tmp', 'wb').write((json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), head=head, key=key, whole=whole, secs=round(secs, 1),
                                                   halves=[ha.get('acts'), hb.get('acts')], boundary=bd, equal=equal, lsr=dict(KC0.LSR)),
                                              indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(pj + '.tmp', pj)
    print(NL.join(Lc[-1:]))
    print('  written: b693_chain_control.txt, b693_chain_control.json')
    return 0 if equal else 1


def _base_name(pushed):
    if PRERUN:
        return 'b693_arms_prerun.txt'
    if MID and len(sys.argv) > sys.argv.index('--mid') + 1:
        return sys.argv[sys.argv.index('--mid') + 1]
    if RERUN and len(sys.argv) > sys.argv.index('--rerun-postpush') + 1:
        return sys.argv[sys.argv.index('--rerun-postpush') + 1]
    return 'b693_checks_postpush.txt' if pushed else 'b693_checks.txt'


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
        ex.update(jl('b693_exercise_%s.json' % part).get('exercise') or {})
    if ex and base in ('b693_checks.txt', 'b693_checks_postpush.txt'):
        e = (json.dumps(dict(exercise=ex, run=n, live_failing=fails, defective=defs, neg_failures=ng), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p_ = os.path.join(D, 'b693_exercise.json')
        open(p_ + '.tmp', 'wb').write(e)
        os.replace(p_ + '.tmp', p_)
    print(NL.join(out[3:14]))
    print('  written: %s' % base)
    return 0 if ok else 1


def main():
    if SEAL:
        return seal()
    if COMBINE:
        return combine()
    if CONTROL:
        return chain_control()
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
    rec('b693 -- THE SUITE. ### **%s READING.** ### PART %s ### every arm exercised on both controls.' % (
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
    rec('  ### (R264)(2) THE FREEZE: the standing arms (b692`s face less its own arms, the twenty-four rule arms among them; none added) %d ; '
        'carried here %d ; the act`s arms over its own banks %s ; arms beyond both %s' % (
            len(S['standing']), len(set(names) & set(S['standing'])), sorted(set(names) - set(S['standing'])),
            sorted(set(names) - set(S['standing']) - set(K.ACT_ARMS)) or 'NONE'))
    rec('  ### standing arms not carried here: %s' % (sorted(set(S['standing']) - set(names)) or 'NONE'))
    if 'rules' in NEED[PART]:
        rec('  ### THE RULE ARMS, EACH WITH ITS COUNT (tools/rule_arms.py; rows read, rows failing, the reading); the call trace %d calls over both sessions:' % len(
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
            rec('  ### standing-b2 CARRIES NO ARM (the author`s word at (R303)(4)`s prompt): its verdicts banked for standing-b3 in relay data/%s' % half_bank(0, _run_key(base)))
        else:
            ha = S['half_a'] or {}
            rec('  ### the reads at commit, b680: %s ; b693: %s' % (S['ar_reads'].get('b680'), S['ar_reads'].get('b693')))
            rec('  ### THE FIRST HALF AS standing-b2 BANKED IT (relay data/%s): %d acts, AGREE %d, at HEAD %s (now %s), its boundary equal %s' % (
                half_bank(0, _run_key(base)), len(ha.get('acts') or []), sum(1 for x in ha.get('acts') or [] if x[1] == 'AGREE'), (ha.get('head') or '-')[:12],
                gs(ROOT, 'rev-parse', 'HEAD')[:12], (ha.get('boundary') or {}).get('equal')))
        write_half(i, _run_key(base), av, S['ar_reads'])
    sj = S['sealj'].get('tools') or {}
    rec('  ### THE SEALED TOOLS, recorded at the seal %s : %s' % (S['sealj'].get('at', '### NOT RECORDED'), '; '.join(
        '%s %s' % (t, ('agree' if sj.get(t) == S['sealnow'].get(t) else 'DIFFER') if t in sj else 'not recorded') for t in K.SEALED)))
    off = S['REC'].edit_route_offences(S['cmds'] + S['prev_cmds'])
    rec('  ### G-EDIT-ROUTE read %d captured commands of this act (both sessions) and %d of the previous act after its post-push suite; offences %d: %s' % (
        len(S['cmds']), len(S['prev_cmds']), len(off), ['#%s %s' % (r['n'], [k for k, _ in o]) for r, o in off] or 'none'))
    mc = re.search(r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', S['citation'])
    rec('  ### THE CITATION CHECK: %s' % (mc.group(0) if mc else '### NOT READ'))
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
    lp = os.path.join(D, _part_name(base, PART).replace('b693_arms_prerun', 'b693_lsr_prerun').replace('b693_checks', 'b693_lsr').replace('.txt', '.json'))
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if PRERUN:
        sb = (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), part=PART, arms=SECS,
                              phases=dict((k, round(v, 1)) for k, v in S['phase_secs'].items()), run_secs=round(secs, 1)),
                         indent=1, ensure_ascii=False) + NL).encode('utf-8')
        sp = os.path.join(D, 'b693_arm_seconds_%s.json' % PART)
        open(sp + '.tmp', 'wb').write(sb)
        os.replace(sp + '.tmp', sp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(arms), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b693_exercise_%s.json' % PART)
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if (not fail and not defective and negfail == 0 and S['declared_eq_run']) else 1


if __name__ == '__main__':
    sys.exit(main())
