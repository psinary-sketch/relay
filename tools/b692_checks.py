# -*- coding: utf-8 -*-
"""b692_checks.py -- THE SUITE OF b692, UNDER (R302): b691 AT ITS WEIGHT; ITS TWO POST-ROOT ITEMS BY CORRIGENDUM; THE SUITE-PARTS ARM
REPAIRED; THE DEPENDENCY-CIRCUIT READING BUILT AND RUN AT SIDE-explicit-formula; CLAUSE-DOMINANCE READ; THE TRIAGE RAISED BY CLASS.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### data/b685_rules.txt row (1) and the ferry's Component 5: every run in FIVE foreground parts, each its own call in its own message --
### `--part standing-a`, `--part standing-c` (G-PRIORBANK-UNCHANGED, G-NODISCLOSURE-PUBLIC, G-WRITELIST-KINDS), `--part standing-b1` (the
### shared additive files), `--part standing-b2` (the act-root chain), `--part act` (the act's arms over this act's banks, the table
### regenerated in a closing run) -- the part names of the form the repaired G-RULE-SUITE-PARTS reads ((R302)(2)); each under the 590 s
### guard the seat runs it in, and NOT RUN beneath the 2,560 MB hold; `--combine <bank>` writes the bank.
### ### (R264)(2), THE FREEZE: the standing arms are b691's face's (G2) arms less b691's own arms over b691's banks, carried, the twenty-four
### rule arms of tools/rule_arms.py among them; no standing arm added (N5). The act's own arms read this act's banks alone (ACT_ARMS). The
### standing runner arms read this act's four runs -- the closure step's three at SIDE-explicit-formula's main and the shorts control at the
### scratch branch's tip -- and no merge.
### ### Every look-up of a landed line goes through the one conversion (imported from tools/b652_record.py through tools/b692_record.py).
### ### The harness is b568's to b691's, written by the Write tool from tools/b691_checks.py; the sources, predicates and arms over this act's
### ### banks are b692's. data/b686_rules.txt row (1): the act arm G-ENTRY-SCORES-EQUAL reads the landed entry; no scorer reads a ledger line.
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
import b692_worklist as K     # noqa: E402
import b691_worklist as K691  # noqa: E402
import rule_arms as RA        # noqa: E402
from b692_record import conv  # noqa: E402

NL = chr(10)
PP = K.PP
EF = 'D:/' + K.EF
FACE = os.path.join(D, 'b692_registration_2026-10-19.txt')
B691_FACE = os.path.join(D, 'b691_registration_2026-10-19.txt')
B691_ACT_ARMS = K691.ACT_ARMS
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
FLOORS = dict(prompts=4, calls=4, checks=4, defects=tuple((x, 'SEAT') for x in 'abcdefghi') + (('j', 'NAVIGATOR'), ('k', 'NAVIGATOR')))
REPAIRED_TOOLS = K.REPAIRED_TOOLS                      # ### the rule arms: its diff in data/b692_tool_repairs.txt row 1
NEW_TOOLS = K.NEW_TOOLS                                # ### the reader
# ### the instruments read unedited: b691's list, b691's sealed tools and b691's repaired generator and its test back among them, less this
# ### act's sealed and repaired tools
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
INST = tuple(sorted((set(INST_BASE) | set(K691.SEALED)) - set(K.SEALED) - set(REPAIRED_TOOLS) - set(NEW_TOOLS)))
CURRENTS = ('ERRATA.md', 'SPIRAL_MAP.md', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md',
            'phase2/method/THE_KEYSTONE_CENSUS_v0_8.md', 'day1/A_Place_to_Stand_v5_18.md', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md',
            'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md', 'day1/ONE_PAGE_PROOF.md', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md',
            'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', 'README.md', 'REGISTRY.md',
            'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md', 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md')
TABLE_FILES = K.TABLE_FILES
WF, PT = '.github/workflows/build-module.yml', 'print_targets.txt'
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
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b692')
            and 'data/b692_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    import b692_record as REC
    return REC.capture()


def prev_now():
    import b692_record as REC
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
        if (f.startswith('b692_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks):
                bad.append(f)
    return bad


def spec_planted():
    import b692_regspec as SPEC
    P = SPEC.planted()
    ctl = [ok for _w, ok in SPEC.controls()]
    return dict(read=[ok for _s, ok, _w in P], controls=ctl, shapes=[s for s, _o, _w in P])


def _deps(ax):
    import b692_record as REC
    return REC._deps(ax)


def wf_state():
    """this act's one kernel write: SIDE-explicit-formula's workflow at main against the workflow the act wrote at the closure step's first
    commit, its dependency form read from its tree, its print list against the third run's print bank, and the files the act wrote on its main
    since the main before it."""
    t = read_blob(EF, 'main:' + WF)
    lf = read_blob(EF, 'main:lakefile.toml') + read_blob(EF, 'main:lakefile.lean')
    req = re.search(r'(?im)^\s*require\b[^\n]*mathlib', lf) or re.search(r'(?is)\[\[require\]\][^\[]*name\s*=\s*"mathlib"', lf)
    pt = read_blob(EF, 'main:' + PT)
    return {K.EF: dict(text=t, before=read_blob(EF, '%s:%s' % (K.CLOSURE_COMMITS[0], WF)), lakefile=bool(lf.strip()), mathlib=bool(req),
                       targets=[l.strip() for l in pt.split(NL) if l.strip()], printed=len(_deps(rd('b692_axioms_SIDE-explicit-formula_after3.txt'))),
                       act_writes=sorted(set(x for x in gs(EF, 'diff', '--name-only', K.EF_BEFORE, 'main').split(NL) if x.strip())),
                       want=sorted([WF, 'CircuitClosure.lean']))}


def main_state():
    """SIDE-explicit-formula's main after the closure step: its tip, its first-parent line back to the main before the act, the tags at each
    closure commit, v0.34 and v0.34.1 peeled."""
    line = gs(EF, 'rev-list', '--first-parent', '--abbrev-commit', '--abbrev=7', '%s..main' % K.EF_BEFORE).split()
    return dict(main=gs(EF, 'rev-parse', '--short=7', 'main'), line=list(reversed(line)),
                files=dict((c, files_of(EF, c)) for c in K.CLOSURE_COMMITS),
                tags=sum((gs(EF, 'tag', '--points-at', c).split() for c in K.CLOSURE_COMMITS), []),
                v034=gs(EF, 'rev-parse', '--short=7', 'v0.34^{commit}'), v0341=gs(EF, 'rev-parse', '--short=7', 'v0.34.1^{commit}'))


def g2_of(path):
    t = read(path)
    try:
        g2 = t[t.index('### (G2) THE GATE ARMS.'):t.index('### (W) THE WRITE LIST.')]
    except ValueError:
        return []
    return sorted(set(x.rstrip('-') for x in re.findall(r'\b[GF]-[A-Z0-9][A-Za-z0-9-]*', g2)) - {'G-NO'})


STANDING = sorted((set(g2_of(B691_FACE)) - set(B691_ACT_ARMS)) | set(K.STANDING_ADDED))
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


def _gz_state():
    """the closure banks against the runner rows and their text hashes banks: (bank, its sha256 equal to the row's, carried by the hashes bank,
    its record lines, the header's count, the programme modules)."""
    import gzip
    out = []
    for r in jl(K.RUNNER_ROWS).get('rows') or []:
        c = r.get('closure') or {}
        if not c.get('bank'):
            continue
        b = raw(os.path.join(D, c['bank']))
        sha = hashlib.sha256(b).hexdigest() if b else None
        lines, head = 0, {}
        if b:
            for l in gzip.decompress(b).decode('utf-8').split(NL):
                if l.strip():
                    j = json.loads(l)
                    if j.get('header'):
                        head = j
                    else:
                        lines += 1
        out.append(dict(bank=c['bank'], label=r.get('label'), equal=bool(sha) and sha == c.get('sha256'),
                        carried=bool(sha) and sha in rd(c['bank'].replace('.jsonl.gz', '_hashes.txt')), lines=lines, count=head.get('records'),
                        modules=len(head.get('modules') or [])))
    return out


def sources(need=()):
    """the sources the arms read; `need` (by part) names the heavy phases this part computes: 'live' (the three arms at HEAD), 'rules' (the
    rule arms' trace), 'written' (the written files, the public bytes, the prior banks), 'chain' (the act-root chain), 'additive' (the shared
    files)."""
    import b692_record as REC
    import b616_record as R6
    import edit_route as ER
    import b641_record as R41
    import additive_shared as ADD
    face = read(FACE)
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b692_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if (f.startswith('b692_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS)
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    cit = jl('b692_citation_check.json')
    t0 = time.time()
    S = dict(
        REC=REC, ER=ER, face=face, ferry=rd('b692_ferry.txt'), scan=rd('b692_ferry_scan.txt'), stepz=rd('b692_stepzero.txt'),
        readfirst=rd('b692_readfirst.txt'), defects=rd('b692_defects.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        answers=rd('b692_author_answers.txt'), answersj=jl('b692_author_answers.json'), prerun=rd('b692_arms_prerun.txt'), rl=jl('b692_record_lines.json'),
        tests=jl('b692_tests_stepzero.json'), testst=rd('b692_tests_stepzero.txt'), withheld=jl('b692_tests_withheld.json'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b692_seal_hashes.json'), sealnow=sealed_now(), cmds=capture_now(), prev_cmds=prev_now(), cmdj=jl('b692_commands.json'),
        cmdt=rd('b692_commands.txt'),
        planted={t: run_test(t) for t in TESTS}, spec=spec_planted(), conv_bad=conv_alone(), suite=read(os.path.join(T, 'b692_checks.py')),
        citation=rd(K.CITATION_BANK), cit_at=iso_epoch(cit.get('at') or ''), cit_misses=cit.get('misses') or [],
        gate=rd('b692_reg_gate.txt'), rowgen=rd('b692_rowgen_stepzero.txt'),
        branchj=jl('b692_branches.json'), branchest=rd('b692_branches.txt'),
        branch_lists=dict((repo, gs(repo, 'branch', '--list', *bs)) for repo, bs in K.DELETE),
        kbranch_lists=dict(('%s %s %s' % (r_, b_, w_), gs(r_, 'branch', '--list', b_) if w_ == 'local' else gs(r_, 'branch', '-r', '--list', 'origin/' + b_))
                           for r_, b_, w_ in REC.KERNEL_BRANCHES),
        repairs=rd('b692_tool_repairs.txt'), rec_src=read(os.path.join(T, 'b692_record.py')),
        corr=rd('b692_corrigendum.txt'), corrj=jl('b692_corrigendum.json'), corrigenda=rd('b675_corrigenda.txt'),
        parts_probe=rd('b692_parts_probe.txt'), parts_after=rd('b692_parts_after.txt'),
        rule_blob=gs(ROOT, 'hash-object', os.path.join(T, 'rule_arms.py')), rules=rd('b692_rules.txt'),
        closure_step=rd('b692_closure_step.txt'), prints_ef=rd('b692_prints_SIDE-explicit-formula.txt'), gz=_gz_state(),
        reading=rd(K.READING_BANK), bars=rd('b692_circuit_bars.txt'), reader_src=read(os.path.join(T, 'circuit_read.py')),
        dominance=rd('b692_circuit_dominance.txt'), controls=rd('b692_circuit_controls.txt'), shorts_branch=rd('b692_circuit_shorts_branch.txt'),
        rf_diff=rd('b692_readfirst_diff.txt'), rf_closure=rd('b692_readfirst_closure.txt'),
        rf_hand_now=blob(ROOT, 'HEAD:data/b692_readfirst.txt'), rf_hand_z=blob(ROOT, '0215ccf9:data/b692_readfirst.txt'),
        spec_now=rd('b692_circuit_spec.txt'), spec_old=rd('b690_circuit_spec.txt'), suite_load=rd('b692_suite_load.txt'),
        inst_diff=rd('b692_instruments_diff.txt'),
        inst_pp=gs(PP, 'diff', '--unified=0', PRE['pp'], 'HEAD', '--', 'phase1.5/method/INSTRUMENTS.md'),
        triage_counts=rd('b692_triage_counts.txt'), olines=jl('b692_orders_lines.json'), shorts_push=rd('b692_shorts_push_out.txt'),
        price_z=rd('b692_stepzero.txt'), candidates=rd('b692_candidates_priced.txt'),
        asec=jl('b692_arm_seconds.json'), asect=rd('b692_arm_seconds.txt'),
        shared=dict((p, (cr0(blob(ROOT, '%s:%s' % (PRE['relay'], p))), cr0(raw(os.path.join(ROOT, *p.split('/')))), cr0(blob(ROOT, 'HEAD:' + p))))
                    for p in K.SHARED_APPENDED),
        t=dict(c1=_ct(PP, K.C1_PP), arm=_ct(ROOT, K.C1_RELAY), orders=_ct(PP, K.ORDERS_PP), shorts=_ct(EF, K.SHORTS_TIP),
               read=_ct(ROOT, K.READ_RELAY)),
        files=dict(rules=files_of(ROOT, K.RULES_COMMIT), spec=files_of(ROOT, K.SPEC_COMMIT), inst=files_of(PP, K.INSTRUMENTS_PP),
                   orders=files_of(PP, K.ORDERS_PP), read=files_of(ROOT, K.READ_RELAY)),
        standing=STANDING, wf=wf_state(), runner=jl(K.RUNNER_ROWS),
        rbanks=dict(('%s_%s' % (r.get('kernel'), r.get('label')), rd('b692_runner_%s_%s.txt' % (r.get('kernel'), r.get('label'))))
                    for r in jl(K.RUNNER_ROWS).get('rows') or []),
        mainst=main_state(),
        export_present=os.path.exists(os.path.join(ROOT, *EXPORT.split('/'))), export_log=gs(ROOT, 'log', '--all', '--format=%h', '--', EXPORT),
        export_index=gs(ROOT, 'ls-files', '--', EXPORT), export_status=gs(ROOT, 'status', '--porcelain', '--', EXPORT),
        closing_src=read(os.path.join(T, 'b692_closing.py')),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b692_act_root.json'), arj0=jl('b691_act_root.json'), art=rd('b692_act_root.txt'), rootsf=rd('act_roots.txt'),
        rootbanks=jl('b692_root_banks.json'),
        pushout=(files_of(ROOT, K.STEPZERO), subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, *f.split('/')))), cr0(blob(ROOT, 'HEAD:tools/' + f)))
              for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b692_kernels_face.json').get('kernels') or {}), kerns_read=list(dict.fromkeys(REC._kerns())),
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mustfail=not os.path.exists(os.path.join(D, 'b692_mustnotexist.txt')),
        fj=jl('b692_findings.json'), tj=jl('b692_trail.json'), sc=jl('b692_scores.json'), desk=rd('b692_desk_notes.txt'), tfj=jl('b692_table_final.json'),
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
    S['ra'] = RA.sources('b692', SESSION, K.ANCHOR, K.PARTS, S['lock_epoch'], PRE['relay'], PRE['pp']) if 'rules' in need else {}
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
            if f.startswith(('b692_', 'audit_b692_')) and os.path.isfile(os.path.join(D, f)) and not f.endswith(('.gz', '.png', '.jsonl')):
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
    a = S['answers']
    m = re.search(r'^### b692 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
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
    import b692_record as REC
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


# ================================================================== (R302) STEP ZERO: THE CITATION CHECK, THE BRANCHES
READFIRST_NEEDLES = ('relay data/b691_closing.txt :1', 'relay data/b691_defects.txt :5-:48', 'relay data/b691_cut.txt',
                     'relay data/b691_orders_triage.txt :151', 'relay tools/rule_arms.py :268', 'relay data/b690_circuit_spec.txt :10-:48',
                     'relay data/b691_axioms_SIDE-explicit-formula_after.txt', 'relay data/b690_nodes_zeta.txt :94-:164',
                     'relay data/b689_runner_SIDE-explicit-formula_run1.txt :4', 'relay data/b518_report.txt :2, :127, :260',
                     'PLACE-papers phase1.5/method/INSTRUMENTS.md :472-:474', 'relay data/b691_closing_push_out.txt')
NAMED_LOCAL = sorted(b for _r, bs in K.DELETE for b in bs)


def _kernel_names():
    import b692_record as REC
    return sorted(b for _r, b, _w in REC.KERNEL_BRANCHES)


NAMED_ALL = sorted(NAMED_LOCAL + _kernel_names())


def readfirst_ok(S):
    z = unwrap(S['readfirst'])
    return bool(z) and all(x in z for x in READFIRST_NEEDLES)


def branches_ok(S):
    """the five names gone from relay and PLACE-papers, the eight kernel branches gone from SIDE-rcurve and SIDE-explicit-formula (local and
    the remote-tracking refs), and the branches bank's verdict."""
    z = S['branchest']
    left = dict((r, sorted(x.strip() for x in v.split(NL) if x.strip())) for r, v in S['branch_lists'].items())
    kleft = dict((r, v.strip()) for r, v in S['kbranch_lists'].items())
    return all(v == [] for v in left.values()) and len(left) == 2 and all(v == '' for v in kleft.values()) and len(kleft) == 8 \
        and all(b in z for b in NAMED_LOCAL) and 'NAMED 5 (MERGED 5) ; KERNEL BRANCHES 8 (MERGED 8), RAISED ; UNNAMED OF b691 0' in unwrap(z)


def branches_banked_ok(S):
    import b692_record as REC
    rows, krows = S['branchj'].get('rows') or [], S['branchj'].get('kernel_rows') or []
    try:
        fates = [REC.read_branch_row(r) for r in rows]
        kf = [REC.read_branch_row(r) for r in krows]
    except Exception:
        return False
    return len(rows) == 5 and all(f == 'DELETED' for _b, f in fates) and all(r['merged'] for r in rows) and len(krows) == 8 \
        and all(f == 'RAISED' for _b, f in kf) and all(r['merged'] for r in krows) and sum(1 for r in krows if r['where'] == 'remote') == 2


def deletes_one_ok(S):
    import b692_record as REC
    shapes = [REC.delete_shape(r['cmd']) for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell')]
    shapes = [s for s in shapes if s[0]]
    return bool(shapes) and all(len(d) == 1 and not gl for d, gl in shapes) and sorted(x for d, _g in shapes for x in d) == NAMED_ALL \
        and 'BRANCH DELETES OF ONE BRANCH AND NO GLOB 13 OF 13' in S['cmdt']


def dry_step_ok(S):
    g = S['gate']
    return '--- THE DRY-RUN STEP ((R267)(2))' in g and 'ENTRY : table cells NONE ; screens QUIET' in g and 'TRAIL : table cells NONE ; screens QUIET' in g \
        and '### ### **THE DRY-RUN STEP : CLEAN**' in g and '### ### **GATE VERDICT : CLEAR**' in g


def closing_dry_ok(S):
    g = S['gate']
    return '--- THE CLOSING DRY-RUN STEP (b675 rules row 1)' in g and '### ### **THE CLOSING DRY-RUN STEP : CLEAN**' in g \
        and 'b692 closed:' in g and 'the misses as the bank lists them' in g and '(annotated, peeled) ; main' in g \
        and '### THE CLOSURE STEP' in g and '### THE READINGS' in g and '### THE KERNELS' in g and '### NO VERDICT LINE' not in g


def citation_ok(S):
    c = S['citation']
    m = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', c)
    raised = re.findall(r'RAISED: ([0-9a-f]{7})\.\*\*', c)
    tested = re.findall(r'### the miss tested directly by the seat \([^)]*\): ([0-9a-f]{7}) is a commit of SIDE-', c)
    return bool(m) and int(m.group(1)) == int(m.group(2)) + int(m.group(3)) > 0 and 'A GATE STEP AT STEP ZERO' in c \
        and int(m.group(3)) == 0 == len(S['cit_misses']) and sorted(raised) == sorted(tested)


def rowgen_ok(S):
    return '### ### **CONSTELLATION EXIT 0 ; ROWGEN DIFF EXIT 0 ; TABLES 19.**' in S['rowgen']


def weight_ok(S):
    return landed(S, 0, ['b691 AT ITS WEIGHT', 'f5318624'])


def _first_ts(S, needle):
    ts = [iso_epoch((r.get('ts') or '')[:19] + 'Z') for r in S['cmds'] if needle in r['cmd']]
    ts = [t for t in ts if t]
    return min(ts) if ts else None


def answers_checked_ok(S):
    """the citation bank's mid-act prints read at HEAD, at or above the sealed floor, each before the write its answer governs: the first kernel
    branch delete, the shared tool's repair commit, the scratch branch's commit, the orders' landing commit."""
    c = S['citation']
    stamps = re.findall(r'### \(R278\)\(4\) THE MID-ACT CHECK \((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\): the answer carrying \'([^\']+)\'', c)
    acts = dict((n, iso_epoch(t)) for t, n in stamps)
    gov = (('delete all eight', _first_ts(S, 'branch -d push-b691-main')), ('the pattern widened at :268', S['t'].get('arm')),
           ('the plain branch push', S['t'].get('shorts')), ('each of the 24 DISCHARGED-BY-READING', S['t'].get('orders')))
    return len(stamps) >= FLOORS['checks'] and all(any(k in n for n in acts) and w and max(v for n, v in acts.items() if k in n) < w for k, w in gov)


# ================================================================== (R302)(1)-(4): THE CORRIGENDUM, THE ARM, THE CIRCUIT, THE ORDERS
def _fn_src(src, name):
    if ('\ndef %s(' % name) not in src:
        return ''
    i = src.index('\ndef %s(' % name) + 1
    m = re.search(r'\n(?=\S)', src[i + 1:])
    return src[i:i + 1 + m.start() + 1] if m else src[i:]


def scorer_banks_ok(S):
    """data/b686_rules.txt row (1), standing: the N1-N5 scorers' code reads banks and commits and no ledger and no findings bank; the scores
    route writes its bank once; the entry's composer takes its scores line from the scores bank."""
    n = ''.join(strip_prose(_fn_src(S['rec_src'], f)) for f in ('_n1', '_runner_state', '_n2', '_modules_state', '_n3', '_controls_state', '_n4',
                                                                '_dominance_state'))
    sc = strip_prose(_fn_src(S['rec_src'], 'scores'))
    ft = strip_prose(_fn_src(S['rec_src'], '_finding_text'))
    return bool(n) and 'b692_circuit_controls.txt' in n and 'b692_circuit_dominance.txt' in n and 'b692_prints_SIDE-explicit-formula.txt' in n \
        and not re.search(r'\b(FIND|OT)\b|FINDINGS|OPEN_TRAILS|findings|entry_line', n) \
        and "os.path.isfile(os.path.join(D, 'b692_scores.json'))" in sc and 'scores_line(S)' in ft and "jl('b692_scores.json')" in ft


def _entry_block(S):
    e = S['fj'].get('entry_line')
    ls = S['find'].split(NL)
    if not e:
        return ''
    end = next((i for i in range(e, len(ls)) if ls[i].startswith('## ')), len(ls))
    return NL.join(ls[e - 1:end])


def entry_scores_ok(S):
    import b692_record as REC
    want = conv(REC.scores_line(S['sc'])) if S['sc'] else None
    blk = _entry_block(S)
    got = [l for l in blk.split(NL) if l.startswith('**The scores.**')]
    return bool(want) and bool(S['sc']) and got == [want]


def entry_title_ok(S):
    e = S['fj'].get('entry_line')
    return bool(e) and S['REC']._title() == K.TITLE and fline(S, e) == conv(K.TITLE)


def corrigendum_ok(S):
    j = S['corrj']
    return j.get('entry_line') == K.CORRIGENDUM_LINE and fline(S, K.CORRIGENDUM_LINE) == conv(j.get('title') or '\x00') \
        and "(l) G-RULE-SUITE-PARTS FAILS pre-push and post-push" in fline(S, K.CORRIGENDUM_LINE + 2) and '(m) The PLACE-papers trail commit' in fline(S, K.CORRIGENDUM_LINE + 2) \
        and 'THE ENTRY AT FINDINGS :%d' % K.CORRIGENDUM_LINE in S['corr'] and '  (5) relay data/b691_registration_2026-10-19.txt :63' in S['corrigenda'] \
        and '  (6) PLACE-papers 9a0dc76' in S['corrigenda']


def parts_repaired_ok(S):
    return S['rule_blob'] == '3f183f15d44c16fb0d4961f6ea57765c92f35481' and '  ROW 1  tools/rule_arms.py' in S['repairs'] \
        and 'AFTER 3f183f15d44c16fb0d4961f6ea57765c92f35481' in S['repairs'] \
        and "b691`S BANKS PASS ; THE FIVE-PART b692 RUN PASS ; THE PLANTED CONTROL FAIL" in S['parts_after'] \
        and re.search(r'V1 the pattern widened alone\s+governing: [^\n]*\n\s+over b691`s banks: FAIL', S['parts_probe']) is not None \
        and re.search(r'V2 the pattern widened, the parts read by family\s+governing: [^\n]*\n\s+over b691`s banks: PASS', S['parts_probe']) is not None


def rules_banked_ok(S):
    return S['files']['rules'] == ['data/b692_rules.txt'] and '  (1) A COMMIT MADE AFTER THE SEAL THAT FAILS AN ARM IS LEFT AS IT STANDS.' in S['rules'] \
        and 'Binds from b692.' in S['rules']


def closure_step_ok(S):
    m = S['mainst']
    return m['line'] == list(K.CLOSURE_COMMITS) and m['main'] == K.EF_TIP and not m['tags'] and m['v034'] == '8fbc27b' and m['v0341'] == K.EF_BEFORE \
        and all(set(f) <= {WF, 'CircuitClosure.lean'} for f in m['files'].values()) \
        and 'EACH PRINTED AFTER True ; DIFFERING 0 ; NEW 0 ; EQUAL LINE FOR LINE True' in S['prints_ef'] \
        and 'PRINTS EQUAL LINE FOR LINE' in S['closure_step'] and 'THE MODULES UNTOUCHED, NO TAG' in S['closure_step']


def closure_banked_ok(S):
    gz = dict((x['label'], x) for x in S['gz'])
    a3, sh = gz.get('after3') or {}, gz.get('shorts') or {}
    return bool(a3) and a3['equal'] and a3['carried'] and a3['lines'] == a3['count'] == 3365 and a3['modules'] == 179 \
        and bool(sh) and sh['equal'] and sh['carried'] and sh['lines'] == sh['count'] == 3366


def price_ok(S):
    z = unwrap(S['price_z'])
    return 'THE PRICE 4 DISPATCHES x 414 s = 1656 s OF RUNNER TIME' in z and 'THE PRICE 1656 s PASSED AT 1780 s ; SIDE-lv-conservation CARRIED TO b694' \
        in unwrap(S['closure_step']) and 'NEITHER TAKEN ; W-ORD-EPSTEIN-COUNT-LEAN CARRIED TO b694' in unwrap(S['candidates'])


def reader_controls_ok(S):
    return 'THE CONTROLS AS WANTED True' in S['controls'] and 'THE PLANTED DECLARATION SIDEExplicitFormula.B321.circuit_shorts_control_b692 THE ONE FIRST' \
        in S['shorts_branch'] and 'SHORTS 1 (RECORDS CARRYING sorryAx)' in S['shorts_branch']


def width_bar_ok(S):
    return 'FEW = 5 ; NO CLOSURE BANK READ BEFORE THIS BANK' in S['bars'] \
        and '(FEW = 5 ; the main theorem SIDEExplicitFormula.B321.h2_sign_iff_rh)' in S['reading'] and '\nFEW = 5 ' in S['reader_src'] \
        and 'AT OR UNDER FEW = 5: 25' in S['reading']


def dominance_ok(S):
    d = S['dominance']
    return 'CLAUSE-DOMINANCE 1 OF 1 FACES KERNELS REACHED (SIDE-explicit-formula IN) ; 1 NOT REACHED (SIDE-lv-conservation)' in d \
        and re.search(r'^  SIDE-explicit-formula\s+SIDEExplicitFormula\.B321\.h2_sign_iff_rh\s+IN ; the path: ', d, re.M) is not None \
        and re.search(r'^  SIDE-lv-conservation\s+-\s+NOT REACHED', d, re.M) is not None and 'THE CLAUSE`S FACE IN 2 OF 9 FACES' in d


def readfirst_diff_ok(S):
    return 'THE HAND LIST 27 PATHS ; THE TEXT CITES 24 ; BOTH 14 ; LINES DIFFERING 23' in S['rf_diff'] and 'No bank is rewritten by this reading.' in S['rf_diff'] \
        and 'data/b692_readfirst_diff.txt' in S['files']['read'] and S['rf_hand_now'] is not None and S['rf_hand_now'] == S['rf_hand_z']


def spec_tenth_ok(S):
    old = S['spec_old'].split(NL)[9:48]
    new = S['spec_now'].split(NL)
    try:
        i = new.index(old[0])
    except ValueError:
        return False
    return new[i:i + 39] == old and new[i + 39].startswith('  SUITE-LOAD        reads:') and S['files']['spec'] == ['data/b692_circuit_spec.txt']


def suite_load_ok(S):
    return re.search(r'RULE ARMS 24 ; WITH A SOURCE READ 11 ; ANSWERING A DEFECT ALONE 11 ; DEFECTS PER ACT [\d.]+ -> [\d.]+ AS ARMS [\d.]+ -> [\d.]+ ; '
                     r'THE FACTOR [\d.]+', S['suite_load']) is not None and 'a ratio of two means over a short series, not a fit' in S['suite_load']


def instruments_entry_ok(S):
    adds = [l for l in S['inst_pp'].split(NL) if l.startswith('+') and not l.startswith('+++')]
    dels = [l for l in S['inst_pp'].split(NL) if l.startswith('-') and not l.startswith('---')]
    return S['files']['inst'] == ['phase1.5/method/INSTRUMENTS.md'] and len(adds) == 4 and not dels \
        and adds[1].startswith('+## I-40 — THE DEPENDENCY-CIRCUIT READING') and 'THE ENTRY I-40 ; LINES ADDED 4 ; REMOVED 0' in S['inst_diff']


def triage_entered_ok(S):
    ls = S['olines'].get('lines') or []
    heads = [x.get('head') or '' for x in ls]
    return len(ls) == 35 and [x.get('line') for x in ls] == list(range(K.ORDERS_LINES[0], K.ORDERS_LINES[1] + 1, 2)) \
        and all(oline(S, x['line']).startswith(conv(x['head'])) for x in ls) and S['files']['orders'] == ['OPEN_TRAILS.md'] \
        and sum(1 for h in heads if '` CARRIED (' in h) == 12 and sum(1 for h in heads if '` DISCHARGED BY READING (' in h) == 23 \
        and 'ORDERS 35 ; CARRY 11 ; DISCHARGED-BY-READING 24 ; RETIRE 0 ; THE BANK`S VERDICT EQUAL True' in S['triage_counts']


def shorts_exception_ok(S):
    a = S['answers']
    p3 = re.search(r'### PROMPT 1 \(Shorts ctrl\)[\s\S]*?RESULT \(transcript line \d+, (\S+)\): ([^\n]*)', a)
    at = iso_epoch((p3.group(1) if p3 else '')[:19] + 'Z')
    return bool(p3) and 'the plain branch push' in p3.group(2) and bool(at) and bool(S['t'].get('shorts')) and at < S['t']['shorts'] \
        and 'git -C /d/SIDE-explicit-formula push origin circuit-shorts-control-b692' in S['shorts_push'] \
        and '5866ff203a08925689bc35964b9c1d71f0742a57\trefs/heads/circuit-shorts-control-b692' in S['shorts_push'] \
        and "(i) THE SEAT'S, A RULED EXCEPTION AND NOT A SLIP" in S['defects']


def repairs_ok(S):
    return ('### ### **REPAIRS 8 ; THE SEALED COPIES AGREE ; TOOLS CARRIED 8 OF 8 ; THE STANDING INSTRUMENTS UNEDITED True ; THE REPAIRED SHARED '
            'TOOL 1, ITS DIFF BANKED True') in S['repairs']


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


# ================================================================== THE RUNNER (the standing arms, this act's four runs, no merge)
IDENT_WF = ('secrets.', 'psinary', 'seale', 'york', 'hotmail', 'orcid', '0009-0008')


def wf_ok(S):
    """the one kernel workflow the act wrote: at main equal to the act's own write, no author identifier, no secret, the hold, the lake path
    and the cache step its lakefile's Mathlib requires, the print step over its list, the closure step, the files the act wrote on main."""
    for k, v in S['wf'].items():
        t = v['text'].lower()
        if not v['text'] or v['text'] != v['before'] or any(w in t for w in IDENT_WF):
            return False
        if 'workflow_dispatch' not in t or 'hold_mb: "2560"' not in t or 'print_targets.txt' not in t or 'circuitclosure.lean' not in t \
                or 'out/closure.jsonl' not in t:
            return False
        if not v['lakefile'] or 'lake env lean out/axioms.lean' not in t or (('lake exe cache get' in t) != v['mathlib']):
            return False
        if len(v['targets']) != v['printed'] or v['act_writes'] != v['want']:
            return False
    return sorted(S['wf']) == [K.EF]


def runner_ok(S):
    """this act's four runs through its record tool's reader: each at its own ref, success, the artifact's sha256, the memory low above the
    hold."""
    import b692_record as REC
    rows = S['runner'].get('rows') or []
    want = dict((lab, gs(EF, 'rev-parse', ref)) for lab, ref in K.RUNNER_LABELS)
    try:
        for r in rows:
            REC.read_runner_row(r)
    except Exception:
        return False
    return len(rows) == 4 and sorted(r['label'] for r in rows) == sorted(want) and all(r['kernel'] == K.EF and r['ref'] == want[r['label']] for r in rows) \
        and all(r['conclusion'] == 'success' and r['artifact_sha256'] and r['mem_low'] is not None and r['mem_low'] >= K.HOLD and not r['stopped']
                for r in rows)


def gate_ok(S):
    bs = S['rbanks']
    return len(bs) == 4 and all('GATE DERIVES' in t and 'BUILD EXIT 0 ; ERROR LINES 0' in t and 'SORRYAX 0' in t
                                and re.search(r'^### the artifact: .* ; AGREE$', t, re.M) for t in bs.values())


def merges_ok(S):
    """this act made no merge and no tag: SIDE-explicit-formula's main at the third closure commit, its first-parent line the three closure
    commits from the main before the act, no tag at any of them, v0.34 and v0.34.1 unmoved."""
    m = S['mainst']
    return m['main'] == K.EF_TIP and m['line'] == list(K.CLOSURE_COMMITS) and not m['tags'] and m['v034'] == '8fbc27b' and m['v0341'] == K.EF_BEFORE


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


POST_SEAL = ('b692 seal', 'b692 pre-root', 'b692 root', 'b692 record', 'b692 --', 'b692 closing', 'b692 entry')


def _component_commit(s):
    return s.startswith('b692') and not s.startswith(POST_SEAL)


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
    return bool(j) and len(rows) == 69 and rows[68][:3] == ['b692', j.get('root'), j0.get('root')] \
        and AR.root_of(items, j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) \
        and not [it for it in items if 'b628_intake_crank' in it or 'b647_navigator_memory' in it or 'b693_' in it or 'mirror' in it
                 or it.split()[0].endswith(('.gz', '.png', '.jsonl'))] \
        and any(it.startswith('data/b692_circuit_dominance.txt ') for it in items) and any(it.startswith('data/b692_readfirst_diff.txt ') for it in items) \
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
    return at is not None and 'data/b692_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    v = S['ar_verify'] or []
    r = S['ar_reads'].get('b692') or {}
    return [x[0] for x in v] == ['b%d' % i for i in range(624, 693)] and all(x[1] == 'AGREE' for x in v) and r.get('crlf') == 0 \
        and (S['ar_reads'].get('b680') or {}).get('corrected') == 4


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**The citation check**', '**The corrigendum**', '**The parts arm**', '**The closure step**', '**The readings**',
                 '**CLAUSE-DOMINANCE**', '**READFIRST-CLOSURE**', '**SUITE-LOAD**', '**INSTRUMENTS**', '**The orders**', '**The scores.**',
                 '**Read in mutual light**', 'strengthens', '**Carried to:**', '**Next.**', 'b693')


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
    import b692_record as REC
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
        and '### THE CITATION CHECK' in t and '### THE RECORD LINES' in t and '### THE DRY RUN' in t and '### THE CLOSURE STEP' in t \
        and '### THE READINGS' in t and '### THE KERNELS' in t and '### THE MIRROR' in t and '### THE CARRY-TIME' in t


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
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R302) END' in S['ferry'] and S['ferry'].rstrip().endswith(K.TAIL),
     lambda S: put(S, 'ferry', S['ferry'].replace(K.TAIL, ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the step-zero bank: tail, lean, lake, python and claude named, the seat`s claude alone, none of the others; no task stopped, no orphan, nothing stopped by PID',
     lambda S: procs_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('python 0', 'python 1'))),
    ('G-STEPZERO-TESTS', 'the tests bank against the test files tracked before the act, test_elab_reader_b634.py withheld (no lean on this host), run against the list the page names',
     lambda S: tests_ok(S), lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: S['pushout'][0] == ['data/b691_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'relay`s and PLACE-papers` branch lists by the ruling`s five names, SIDE-rcurve`s and SIDE-explicit-formula`s by the eight kernel names (local and remote-tracking), and the branches bank',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{'D:/relay': 'push-b691'}))),
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
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -n 1p tools/b692_record.py")])),
    ('G-NO-LOCAL-LEAN', 'the act`s command capture, read live: no command runs lean or lake on this host (N1)', lambda S: no_local_lean(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd='lake env lean CircuitClosure.lean')])),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line, found by conv', lambda S: weight_ok(S), lambda S: _rl(S, 0, 1)),
    ('G-DRY-STEP-CLEAN', 'the gate`s record: the dry-run step run, the entry and the trail record quiet under their screens, CLEAN printed, the gate CLEAR',
     lambda S: dry_step_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE DRY-RUN STEP : CLEAN', 'THE DRY-RUN STEP : NOT CLEAN'))),
    ('G-CLOSING-DRY-STEP', 'the gate`s record: the closing run dry before the lock, its head line, citation line, closure step, readings and kernels lines and tag rows printed (b675 rules row 1)',
     lambda S: closing_dry_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE CLOSING DRY-RUN STEP : CLEAN', 'THE CLOSING DRY-RUN STEP : NOT CLEAN'))),
    ('G-CITATION-CHECKED', 'the citation check`s bank (the gate step at step zero): no miss of the ruling or the ferry; every commit miss of a mid-act check tested directly and noted',
     lambda S: citation_ok(S), lambda S: put(S, 'citation', S['citation'].replace('CITES CHECKED 93 ; OK 93 ; MISSES 0', 'CITES CHECKED 93 ; OK 92 ; MISSES 1'))),
    ('G-R302-ENTERED', 'the ferry and the trail', lambda S: 'RULING (R302) END' in S['ferry'] and S['ot'].count('**(R302) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R302) ratified', '**(R3020) ratified'))),
    ('G-ROWGEN-STEPZERO', 'the rowgen bank: constellation and the build-free diff over the 19 roster tables, both exit 0 (b670 rules row 3)',
     lambda S: rowgen_ok(S), lambda S: put(S, 'rowgen', S['rowgen'].replace('ROWGEN DIFF EXIT 0', 'ROWGEN DIFF EXIT 1'))),
    ('G-BRANCHES-BANKED', 'the branches bank: five named rows deleted and eight kernel rows raised through the record tool`s reader, each merged, two of them remote',
     lambda S: branches_banked_ok(S), lambda S: _mut(S, 'branchj', lambda d: d['rows'][0].update(fate='GONE'))),
    ('G-DELETES-ONE-BRANCH', 'the command capture by the record tool`s reader and the command bank: each branch delete naming one branch, no glob in any half, the ruling`s five and the author`s eight exactly',
     lambda S: deletes_one_ok(S), lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="git branch -d push-b691 push-b691-root")])),
    ('G-ANSWERS-CHECKED', 'the citation bank`s mid-act prints read at HEAD, each before the write its answer governs: the kernel deletes, the arm`s repair, the scratch branch, the orders',
     lambda S: answers_checked_ok(S), lambda S: put(S, 't', dict(S['t'], arm=1))),
    ('G-SCORER-READS-BANKS', 'tools/b692_record.py`s code, prose stripped: the N1-N5 scorers reading banks and commits and no ledger, the scores bank written once, the entry`s scores line from it',
     lambda S: scorer_banks_ok(S), lambda S: put(S, 'rec_src', S['rec_src'].replace("def _n2():", "def _n2():\n    _x = rd(FIND)"))),
    ('G-ENTRY-SCORES-EQUAL', 'FINDINGS at the findings bank`s line and the scores bank: the entry`s scores line equal to the line composed from the bank',
     lambda S: entry_scores_ok(S), lambda S: _mut(S, 'sc', lambda d: d.update(N1=['REFUTED', 'planted']))),
    ('G-ENTRY-TITLE-FORM', 'FINDINGS at the findings bank`s line, the record tool`s title from the dominance, reading, readfirst and orders banks, and the worklist`s: the ferry`s form adjusted',
     lambda S: entry_title_ok(S), lambda S: put(S, 'find', S['find'].replace(conv(K.TITLE), conv(K.TITLE).replace('SHORTS 0', 'SHORTS 1')))),
    ('G-CORRIGENDUM-ENTERED', 'FINDINGS at the corrigendum`s line by conv, its (l) and (m), its bank`s verdict and the corrigenda bank`s rows (5) and (6)',
     lambda S: corrigendum_ok(S), lambda S: put(S, 'corrigenda', S['corrigenda'].replace('  (6) PLACE-papers 9a0dc76', '  (6) x'))),
    ('G-PARTS-ARM-REPAIRED', 'tools/rule_arms.py`s blob, the repairs bank`s row 1, the probe (V1 failing, V2 passing) and the after bank: b691`s banks passing at HEAD, the planted control firing',
     lambda S: parts_repaired_ok(S), lambda S: put(S, 'parts_after', S['parts_after'].replace('THE PLANTED CONTROL FAIL', 'THE PLANTED CONTROL PASS'))),
    ('G-RULES-BANKED', 'the rules commit`s files and the rules bank: row (1) alone in its commit, binding from b692',
     lambda S: rules_banked_ok(S), lambda S: put(S, 'files', dict(S['files'], rules=['data/b692_rules.txt', 'x']))),
    ('G-CLOSURE-STEP', 'SIDE-explicit-formula`s main: the three closure commits on its first-parent line, each the script or the step alone, no tag, v0.34 and v0.34.1 unmoved; the prints equal (N2)',
     lambda S: closure_step_ok(S), lambda S: _mut(S, 'mainst', lambda d: d['files'].update({'ccec1ba': ['SIDEExplicitFormula/Seam.lean']}))),
    ('G-CLOSURE-BANKED', 'the closure banks against the runner rows and their text hashes banks: sha256 equal and carried, records equal to the header`s count, 179 modules (N1)',
     lambda S: closure_banked_ok(S), lambda S: put(S, 'gz', [dict(x, carried=False) for x in S['gz']])),
    ('G-PRICE-KEPT', 'the step-zero price, the closure-step bank`s ledger of runner seconds and the candidates bank: 1656 s priced, passed at 1780 s, SIDE-lv-conservation carried, neither candidate taken',
     lambda S: price_ok(S), lambda S: put(S, 'closure_step', S['closure_step'].replace('PASSED AT 1780 s', 'PASSED AT 1000 s'))),
    ('G-READER-CONTROLS', 'the controls bank and the shorts-branch bank: SHORTS 0 on main with the planted copy one short, HCount a terminal, no premise at the main, SHORTS 1 at the planted declaration (N3)',
     lambda S: reader_controls_ok(S), lambda S: put(S, 'shorts_branch', S['shorts_branch'].replace('THE ONE FIRST', 'NOT THE ONE FIRST'))),
    ('G-WIDTH-BAR-NAMED', 'the bars bank, the reading bank and the reader`s code: FEW = 5 named before the run and read by the reading',
     lambda S: width_bar_ok(S), lambda S: put(S, 'reader_src', S['reader_src'].replace('\nFEW = 5 ', '\nFEW = 9 '))),
    ('G-DOMINANCE-PRINTED', 'the dominance bank: the fraction over the faces kernels, each kernel named with its reading, the faces within the kernel (N4)',
     lambda S: dominance_ok(S), lambda S: put(S, 'dominance', S['dominance'].replace('NOT REACHED --', 'IN --'))),
    ('G-READFIRST-DIFF-BANKED', 'the readfirst diff bank and its commit, and the hand list`s blob at HEAD against step zero`s: the diff banked, no bank rewritten (N4)',
     lambda S: readfirst_diff_ok(S), lambda S: put(S, 'rf_hand_now', b'x')),
    ('G-SPEC-TENTH-ROW', 'the successor spec against b690`s: the nine rows byte for byte, SUITE-LOAD beneath, committed alone',
     lambda S: spec_tenth_ok(S), lambda S: put(S, 'spec_now', S['spec_now'].replace('  SERIES            reads:', '  SERIES            read:'))),
    ('G-SUITE-LOAD-BANKED', 'the suite-load bank`s verdict: the rule arms` sources read, the defects-per-act factor printed as a ratio and not a fit',
     lambda S: suite_load_ok(S), lambda S: put(S, 'suite_load', S['suite_load'].replace('not a fit', 'a fit'))),
    ('G-INSTRUMENTS-ENTRY', 'PLACE-papers` INSTRUMENTS.md: its commit alone, its diff four lines added and none removed, I-40 the entry; the diff bank',
     lambda S: instruments_entry_ok(S), lambda S: put(S, 'inst_pp', S['inst_pp'] + NL + '-a line removed')),
    ('G-TRIAGE-ENTERED', 'OPEN_TRAILS at the orders` landing lines by conv: thirty-five entries, 12 carried and 23 discharged, their commit the ledger alone, the counts bank equal to the triage verdict',
     lambda S: triage_entered_ok(S), lambda S: _mut(S, 'olines', lambda d: d['lines'][0].update(line=1))),
    ('G-SHORTS-PUSH-EXCEPTION', 'the answers bank`s prompt and result before the scratch branch`s commit, the push bank`s command and read-back, the defect lettered as a ruled exception',
     lambda S: shorts_exception_ok(S), lambda S: put(S, 'shorts_push', S['shorts_push'].replace('5866ff203a08925689bc35964b9c1d71f0742a57\trefs', 'x\trefs'))),
    ('G-TOOL-REPAIRS', 'the repairs bank`s verdict: eight carry-time repairs, the sealed copies agreeing, eight tools carried, the standing instruments unedited, the repaired shared tool with its diff banked',
     lambda S: repairs_ok(S), lambda S: put(S, 'repairs', S['repairs'].replace('REPAIRS 8 ;', 'REPAIRS 0 ;'))),
    ('G-PARTS-PRERUN', 'the pre-run bank`s five parts with their seconds, named in the form the repaired arm reads',
     lambda S: parts_ok(S), lambda S: put(S, 'prerun', S['prerun'].replace('PART standing-b2', 'PART standing-x'))),
    ('G-ARM-SECONDS-BANKED', 'the per-arm seconds bank: every standing arm clocked at the pre-run, the three slowest named, each part`s seconds',
     lambda S: arm_seconds_ok(S), lambda S: _mut(S, 'asec', lambda d: d.update(clocked=0))),
    ('G-DEFECTS-LETTERED', 'the defects bank read at HEAD: the sealed letters its prefix, consecutive letters, owners the seat or the navigator',
     lambda S: defects_ok(S), lambda S: put(S, 'defects', S['defects'].replace("(a) THE SEAT'S", "(a) THE AUTHOR'S"))),
    ('G-SPEC-PLANTED', 'tools/b692_regspec.py`s planted rows run live through the record tool`s readers, and rows of another shape refused',
     lambda S: bool(S['spec']['read']) and all(S['spec']['read']) and all(S['spec']['controls']) and any('branch' in x for x in S['spec']['shapes']),
     lambda S: _mut(S, 'spec', lambda d: d['controls'].append(False))),
    ('G-CONVERSION-ONE', 'every b692 tool`s code, the reader`s and the repaired shared tool`s: no conversion defined (conv imported from b652_record); the suite importing it',
     lambda S: S['conv_bad'] == [] and 'from b692_record import conv' in S['suite'], lambda S: put(S, 'conv_bad', ['b692_checks.py'])),
    ('G-WORKFLOW-FILES', 'SIDE-explicit-formula`s workflow at main: equal to the act`s own write at the closure step`s first commit, no author identifier, no secret, the hold, the lake path and the cache, the print step over its list, the closure step, the files the act wrote',
     lambda S: wf_ok(S), lambda S: _mut(S, 'wf', lambda d: d[K.EF].update(text=d[K.EF]['text'] + ' secrets.X'))),
    ('G-RUNNER-READ', 'this act`s four runs through its record tool`s reader: each at its own ref, success, the artifact`s sha256, the memory low above the hold',
     lambda S: runner_ok(S), lambda S: _mut(S, 'runner', lambda d: [r.update(mem_low=2000) for r in d['rows']])),
    ('G-RUNNER-GATE', 'this act`s four runs` gate readings: build exit 0, no error line, no sorryAx in the print step, the artifact`s digest agreeing',
     lambda S: gate_ok(S), lambda S: put(S, 'rbanks', dict(S['rbanks'], **{'x_after': 'GATE NOT DERIVES'}))),
    ('G-MERGES-ON-GATE', 'SIDE-explicit-formula`s main: no merge and no tag this act, its first-parent line the closure step`s three commits, v0.34 and v0.34.1 unmoved',
     lambda S: merges_ok(S), lambda S: _mut(S, 'mainst', lambda d: d['tags'].append('v0.35'))),
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
    ('G-PP-SCOPE', 'PLACE-papers` changed files against FINDINGS, OPEN_TRAILS and INSTRUMENTS.md',
     lambda S: corpus_scope(S), lambda S: put(S, 'pp_changed', S['pp_changed'] + ['day1/ONE_PAGE_PROOF.md'])),
    ('G-CURRENTS-UNEDITED', 'the map, the census, the monograph, the faces page, the Dirichlet page, the surround, SIMPLICITY, README, REGISTRY, FOUNDATIONS and its one-copy partner: working tree, before and HEAD',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'ERRATA.md': (b'x', b'y', b'y')}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read before the seal',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b691`s and the earlier tools, the generator and its test, b672`s record tool, act_root.py, rowgen`s, edit_route.py, chain_page.py, e0_rule.py, the mirror`s, repair_snapshot.py and the shared tools -- the repaired rule arms apart: before, working tree and HEAD',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'additive_shared.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at f5318624 but the shared additive files (act_roots.txt and the corrigenda bank among them), by blob id',
     lambda S: S['prior_bad'] == [] and S['prior_n'] > 0, lambda S: put(S, 'prior_bad', ['data/b691_stepzero.txt'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS before and now', lambda S: S['fi_pre'] is not None and (S['fi_now'] or b'').startswith(S['fi_pre']),
     lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS before and now', lambda S: S['ot_pre'] is not None and (S['ot_now'] or b'').startswith(S['ot_pre']),
     lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-NODISCLOSURE-PUBLIC', 'TECHNE-Core`s needle sets over every public byte the act writes: the ledger lines, the banks and the tools',
     lambda S: bool(S['nd_pub']) and not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', {'method': 1})),
    ('G-OUTSIDE-NAMED-NOWHERE', 'the ledger lines appended', lambda S: S['outside'] == [], lambda S: put(S, 'outside', ['x'])),
    ('G-DELETE-FREE', 'the act`s tools` code, the reader`s and the repaired shared tool`s, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='os' + '.remove(p)'))),
    ('G-PUBLISH-UNCALLED', 'the act`s tools` code: no publish call', lambda S: publish_uncalled(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='z_' + 'publish()'))),
    ('G-SEALED-AFTER-COMPONENTS', 'the lock time against every relay and PLACE-papers commit of the act by its subject', lambda S: sealed_after_ok(S),
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b692 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now, the repaired rule arms and the reader among them', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'rule_arms.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3), in five parts summed',
     lambda S: S['lock_epoch'] is not None and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b691`s trail record on OPEN_TRAILS and its root in the chain', lambda S: '### b691 — lane two, act one hundred and eighteen, the re-cut act' in S['ot']
     and S['rootsf'].count(NL + 'b691 ') == 1, lambda S: put(S, 'ot', S['ot'].replace('### b691 — lane two', '### b691 - lane two'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], grade_moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 69th chain row (the corrigendum row apart), the root bank and its items, the dominance and readfirst-diff banks among them, no binary, mirror or untracked bank',
     lambda S: root_banked_ok(S), lambda S: put(S, 'rootsf', S['rootsf'] + 'b693 x y' + NL)),
    ('G-ROOT-BANKS-COMMITTED', 'the root route`s banked reading and every named bank`s blob at the root`s recorded commit: clean and equal at HEAD, HEAD the remote main, the recorded hash carried by the recorded commit',
     lambda S: root_banks_committed_ok(S), lambda S: put(S, 'rootbanks', dict(S['rootbanks'], pushed=False))),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit with the suite`s own remote reads: b624 to b692 AGREE, b680 read through its corrigendum row (4 banks), b692 written LF',
     lambda S: verify_ok(S), lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s through conv, and its parts', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line, the head through conv', lambda S: bool(S['tj'].get('line'))
     and oline(S, S['tj']['line']) == conv(S['REC'].TRAIL_HEAD()), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b692 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b692_record.py agree', 'b692_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line: b693', lambda S: '**Next:** b693' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** b693', '**Next:** b694'))),
] + [('G-N%d-SCORED' % i, 'the scores through the record tool`s reader, and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i),
      lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written since f5318624 and 9a0dc76 against the (W) globs',
     lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b692')" in S['suite'] and "'data/b692_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b692_closing.py: the closing sentence in the rule`s words with the plain reads named; the citation check, the record lines, the dry run, the closure step, the readings, the kernels, the mirror, the carry-time reading',
     lambda S: closing_sentence_ok(S), lambda S: put(S, 'closing_src', S['closing_src'].replace('no identifier of the author ' + 'in any outbound', 'x'))),
    ('G-LSREMOTE-ONE-PER-REPO', 'the part`s ls-remote calls per repository, read after every other arm of the part has run (OPEN_TRAILS :12703)',
     lambda S: lsr_ok(S), lambda S: put(S, 'lsr', {PP: 2})),
] + [(nm, 'tools/rule_arms.py (the author`s word on (R293)(6); (R301)(6) for four; G-RULE-SUITE-PARTS repaired under (R302)(2)) -- ' + reads,
      (lambda p: lambda S: p(S['ra']))(pred), (lambda pl: lambda S: put(S, 'ra', pl(S['ra'])))(plant)) for nm, reads, pred, plant in RA.ARMS]


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
    p = os.path.join(D, 'b692_seal_hashes.json')
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
    print('  written: b692_seal_hashes.json')
    return 0


def _base_name(pushed):
    if PRERUN:
        return 'b692_arms_prerun.txt'
    if MID and len(sys.argv) > sys.argv.index('--mid') + 1:
        return sys.argv[sys.argv.index('--mid') + 1]
    if RERUN and len(sys.argv) > sys.argv.index('--rerun-postpush') + 1:
        return sys.argv[sys.argv.index('--rerun-postpush') + 1]
    return 'b692_checks_postpush.txt' if pushed else 'b692_checks.txt'


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
    out = ['=' * 104, heads[0].replace('PART standing-a', 'FIVE PARTS SUMMED'), '=' * 104] + [
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
        ex.update(jl('b692_exercise_%s.json' % part).get('exercise') or {})
    if ex and base in ('b692_checks.txt', 'b692_checks_postpush.txt'):
        e = (json.dumps(dict(exercise=ex, run=n, live_failing=fails, defective=defs, neg_failures=ng), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p_ = os.path.join(D, 'b692_exercise.json')
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
        print('### every run in five foreground parts -- give `--part %s`' % ' | '.join(K.PARTS))
        return 2
    fm = free_mb()
    if fm < K.HOLD:
        print('%s  ### THE HOST`S FREE MEMORY %d MB, BENEATH THE HOLD %d MB: PART %s NOT RUN ((R294)(2))' % (
            time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), fm, K.HOLD, PART))
        return 3
    t_start = time.time()
    pushed = RERUN or (not PRERUN and not MID and is_pushed())
    rec('=' * 104)
    rec('b692 -- THE SUITE. ### **%s READING.** ### PART %s ### every arm exercised on both controls.' % (
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
    rec('  ### (R264)(2) THE FREEZE: the standing arms (b691`s face less its own arms, the twenty-four rule arms among them; none added) %d ; '
        'carried here %d ; the act`s arms over its own banks %s ; arms beyond both %s' % (
            len(S['standing']), len(set(names) & set(S['standing'])), sorted(set(names) - set(S['standing'])),
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
        rec('  ### the reads at commit, b680: %s ; b692: %s' % (S['ar_reads'].get('b680'), S['ar_reads'].get('b692')))
    sj = S['sealj'].get('tools') or {}
    rec('  ### THE SEALED TOOLS, recorded at the seal %s : %s' % (S['sealj'].get('at', '### NOT RECORDED'), '; '.join(
        '%s %s' % (t, ('agree' if sj.get(t) == S['sealnow'].get(t) else 'DIFFER') if t in sj else 'not recorded') for t in K.SEALED)))
    off = S['REC'].edit_route_offences(S['cmds'] + S['prev_cmds'])
    rec('  ### G-EDIT-ROUTE read %d captured commands of this act and %d of the previous act after its post-push suite (this same session); offences %d: %s' % (
        len(S['cmds']), len(S['prev_cmds']), len(off), ['#%s %s' % (r['n'], [k for k, _ in o]) for r, o in off] or 'none'))
    mc = re.search(r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', S['citation'])
    rec('  ### THE CITATION CHECK: %s ; THE CLOSURE BANKS: %s' % (mc.group(0) if mc else '### NOT READ',
                                                                 '; '.join('%s equal %s carried %s records %s/%s' % (x['label'], x['equal'], x['carried'], x['lines'], x['count'])
                                                                           for x in S['gz'])))
    rec('  ### PLACE-papers` changed files %d against the allowed %d (the two ledgers and INSTRUMENTS.md): beyond %s' % (
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
    lp = os.path.join(D, _part_name(base, PART).replace('b692_arms_prerun', 'b692_lsr_prerun').replace('b692_checks', 'b692_lsr').replace('.txt', '.json'))
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    open(lp + '.tmp', 'wb').write(lb)
    os.replace(lp + '.tmp', lp)
    if PRERUN:
        sb = (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), part=PART, arms=SECS,
                              phases=dict((k, round(v, 1)) for k, v in S['phase_secs'].items()), run_secs=round(secs, 1)),
                         indent=1, ensure_ascii=False) + NL).encode('utf-8')
        sp = os.path.join(D, 'b692_arm_seconds_%s.json' % PART)
        open(sp + '.tmp', 'wb').write(sb)
        os.replace(sp + '.tmp', sp)
    if not (RERUN or PRERUN or MID):
        ej = (json.dumps(dict(exercise=EX, run=len(arms), live_failing=fail, defective=defective, neg_failures=negfail), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p = os.path.join(D, 'b692_exercise_%s.json' % PART)
        open(p + '.tmp', 'wb').write(ej)
        os.replace(p + '.tmp', p)
    print('  written: %s, %s' % (os.path.basename(out), os.path.basename(lp)))
    return 0 if (not fail and not defective and negfail == 0 and S['declared_eq_run']) else 1


if __name__ == '__main__':
    sys.exit(main())
