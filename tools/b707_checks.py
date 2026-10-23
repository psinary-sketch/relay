# -*- coding: utf-8 -*-
"""b707_checks.py -- THE SUITE OF b707, UNDER (R317): b706 AT ITS WEIGHT; THE RENAMES' READERS AND THE SPLIT ARM REPAIRED; THE SIGN-ONSET
RADIUS AT Q0; THE HIGHER PAIRS' ROUTE REGISTERED; lv-CONSERVATION'S FORWARD-PORT OPENED; SEVEN PARTS AS b706 SPLIT THEM.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### data/b684_rules.txt row (1) and b706's split, carried: every run in SEVEN foreground parts, each its own call in its own message --
### `--part standing-a`, `--part standing-c` (G-PRIORBANK-UNCHANGED, G-NODISCLOSURE-PUBLIC, G-WRITELIST-KINDS, the four standing figures and
### G-READ-RULE-STANDING), `--part standing-b1` (the shared additive files), `--part standing-b2a` (the act-root chain over b624-b641, its
### verdicts banked, NO ARM), `--part standing-b2b` (b642-b658, banked, NO ARM), `--part standing-b3` (the second half, b659-b707, and
### G-ACTROOT-VERIFY once over every banked verdict), `--part act` (the act's arms over this act's banks, the table regenerated in a closing run);
### each under the 590 s guard, NOT RUN beneath the 2,560 MB hold; `--combine <bank>` writes the bank. The chain halves as b693 drew them with
### b707 added to the second (the ferry's Component 5); the family reading of the split parts repaired at tools/rule_arms.py under (R317)(2).
### ### (R264)(2), THE FREEZE: the standing arms are b706's face's (G2) arms less b706's own arms over b706's banks, carried, the twenty-four rule
### arms of tools/rule_arms.py and G-READ-RULE-STANDING among them; NO standing arm is added (N5). THE REPAIRS AT THE CARRY, (R317)(2) and the
### carry's own, each a diff in relay data/b707_tool_repairs.txt with its control (data/b707_repair_controls.txt): the three readers --
### tools/mirror_roster.json re-pointed to 70 entries, tools/terminal_table.py's ledger walk bounded by path (the retired copies' directory out),
### tools/rule_arms.py's G-RULE-SUITE-PARTS reading a lettered half as a half of the numbered half it splits -- and the record tool's rowgen
### roster, prev_capture (b701's form for another session) and ROOT_EXCLUDE (data/b706_rules.txt row (1)).
### The four standing figures read by tools/b706_standing_figures.py (unedited: correspondence() and partners() over b706's roster at the
### unversioned names, readme() b705's and pins() b703's through it) against b706's baselines (data/b706_standing_figures.json), each by b703's
### fig_ok (the partners baseline 0 from b706 on, so a raised copy fails). G-READ-RULE-STANDING reads every call from the anchor on. The standing
### runner arms (G-WORKFLOW-FILES, G-RUNNER-READ, G-RUNNER-GATE, G-MERGES-ON-GATE) read THIS ACT'S ONE RUN -- the port branch of
### SIDE-lv-conservation, dispatched once at its tip with the workflow carried onto the branch, held at C7OrderBounds.lean :277 with the print
### step not run and no grade claimed -- so the first three fail on it by (R317)(5)'s own clause and the author's word, declared on the face;
### no kernel main moves this act and no merge is made.
### ### The PRERUN guard held: the per-part seconds bank is written under `if PRERUN:` alone, so no root-named bank is written by the pre-push or
### post-push run; `--guard-dry` prints, for each run mode, what the writer block would write, writing nothing.
### ### Every look-up of a landed line goes through the one conversion (imported from tools/b652_record.py through tools/b707_record.py).
### ### The harness is b568's to b706's, written by the Write tool from tools/b706_checks.py, its pure helpers imported from tools/b703_checks.py
### ### (sealed at b703 and unedited); the sources, predicates and arms over this act's banks are b707's (the act's arms over this act's banks,
### ### the b706 arms over b706's objects not carried). data/b686_rules.txt row (1): the act arm G-ENTRY-SCORES-EQUAL reads the landed entry; no
### ### scorer reads a ledger line. REQUIRED_BANKS is read against ROOT_EXCLUDE at import (b706's (j)): a required bank the route excludes refuses
### ### the suite before any part runs.
"""
import copy
import fnmatch
import gzip
import hashlib
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
import b707_worklist as K     # noqa: E402
import b707_record as REC0    # noqa: E402  ### imported before b706's and b703's suites: b698's record tool is then rebound to b707 once
from b707_record import conv  # noqa: E402
import b706_worklist as K706  # noqa: E402
import b705_worklist as K705  # noqa: E402
import b704_worklist as K704  # noqa: E402
import b703_worklist as K703  # noqa: E402
import b702_worklist as K702  # noqa: E402
import b701_worklist as K701  # noqa: E402
import b700_worklist as K700  # noqa: E402
import b699_worklist as K699  # noqa: E402
import b698_worklist as K698  # noqa: E402
import b697_worklist as K697  # noqa: E402
import b696_worklist as K696  # noqa: E402
import b695_worklist as K695  # noqa: E402
import rule_arms as RA        # noqa: E402
import b704_read_arm as RDA   # noqa: E402
import b703_checks as C3      # noqa: E402  ### the pure helpers alone (no source, no predicate over an act's banks)

git, gs, blob, read, rd, jl, cr0, raw, blob_id = C3.git, C3.gs, C3.blob, C3.read, C3.rd, C3.jl, C3.cr0, C3.raw, C3.blob_id
files_of, read_blob, iso_epoch, utc_epoch, free_mb, strip_prose, wl_globs, tri = (C3.files_of, C3.read_blob, C3.iso_epoch, C3.utc_epoch,
                                                                                   C3.free_mb, C3.strip_prose, C3.wl_globs, C3.tri)
kern_now, appended, run_test, live_arms, g2_of, _ct, _root_named_at_commit = C3.kern_now, C3.appended, C3.run_test, C3.live_arms, C3.g2_of, C3._ct, C3._root_named_at_commit
put, oline, fline, rline, landed, unwrap, procs_ok, planted_ok = C3.put, C3.oline, C3.fline, C3.rline, C3.landed, C3.unwrap, C3.procs_ok, C3.planted_ok
nsm_hits, no_sorry_main, ac_count, axiom_claim, module_header = C3.nsm_hits, C3.no_sorry_main, C3.ac_count, C3.axiom_claim, C3.module_header
_fn_src, _entry_block, _owners, instruments_ok, table_final_ok, _chain_rows = C3._fn_src, C3._entry_block, C3._owners, C3.instruments_ok, C3.table_final_ok, C3._chain_rows
root_banks_committed_ok, kernels_untouched, lsr_ok, g2_names, no_delete, publish_uncalled = (
    C3.root_banks_committed_ok, C3.kernels_untouched, C3.lsr_ok, C3.g2_names, C3.no_delete, C3.publish_uncalled)
_rl, _mut, _live, _planted, _raise_fig, fig_ok, sister_pins_ok = C3._rl, C3._mut, C3._live, C3._planted, C3._raise_fig, C3.fig_ok, C3.sister_pins_ok
_post_seal_named, edit_route_ok, PART_FOOT, KIND = C3._post_seal_named, C3.edit_route_ok, C3.PART_FOOT, C3.KIND

NL = chr(10)
PP = K.PP
LV = K.LV_DIR                 # ### the kernel this act writes: its port branch alone, no main moved
EF = K.EF_DIR
KI = K.JOIN_DIR               # ### the join kernel, read unmoved
FACE = os.path.join(D, 'b707_registration_2026-10-22.txt')
B706_FACE = os.path.join(D, 'b706_registration_2026-10-22.txt')
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
FLOORS = dict(prompts=2, calls=1, checks=2, defects=(('a', 'SEAT'), ('b', 'SEAT'), ('c', 'NAVIGATOR'), ('d', 'NAVIGATOR'), ('e', 'NAVIGATOR'),
                                                     ('f', 'NAVIGATOR'), ('g', 'NAVIGATOR'), ('h', 'SEAT')))


def _jgz(name):
    """a binary bank's json read from its gz (data/b680_rules.txt row (1): the gz beside its hashes bank); {} where absent."""
    p = os.path.join(D, name)
    try:
        return json.loads(gzip.decompress(open(p, 'rb').read()).decode('utf-8'))
    except Exception:
        return {}


def _bank_utc(text):
    """the UTC stamp a bank's head line carries, '(YYYY-MM-DDTHH:MM:SSZ)', as an epoch; None where absent."""
    m = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', (text or '').split(NL)[0] + NL + ((text or '').split(NL)[1] if text and NL in text else ''))
    return iso_epoch(m.group(1)) if m else None


REPAIRED_TOOLS = K.REPAIRED_TOOLS
NEW_TOOLS = K.NEW_TOOLS
# ### the instruments read unedited: b703's list with b703's figures tool, b695's to b706's sealed tools, their new and repaired tools, less this
# ### act's sealed tools and the two shared tools the ruling names (tools/terminal_table.py and tools/rule_arms.py, edited by the Edit tool under
# ### (R317)(2)); tools/mirror_roster.json is data, read by the mirror arms
INST_BASE = tuple(C3.INST_BASE) + ('b703_standing_figures.py',)
INST = tuple(sorted((set(INST_BASE) | set(K695.SEALED) | set(K696.SEALED) | set(K697.SEALED) | set(K698.SEALED) | set(K699.SEALED) | set(K700.SEALED)
                     | set(K701.SEALED) | set(K702.SEALED) | set(K703.SEALED) | set(K704.SEALED) | set(K704.NEW_TOOLS) | set(K704.REPAIRED_TOOLS)
                     | set(K705.SEALED) | set(K705.NEW_TOOLS) | set(K705.REPAIRED_TOOLS) | set(K706.SEALED) | set(K706.REPAIRED_TOOLS))
                    - set(K.SEALED) - set(REPAIRED_TOOLS) - set(NEW_TOOLS)))


def _renamed():
    return dict((r['versioned'], r['unversioned']) for r in (jl('b706_partners.json').get('rows') or []) if r.get('versioned') and r.get('unversioned'))


# ### the corpus documents this act does not write: b703's list with every retired versioned path read at its file of record after (R316)(3)
CURRENTS = tuple(dict.fromkeys(_renamed().get(p, p) for p in C3.CURRENTS))
TABLE_FILES = K.TABLE_FILES
WF, PT = '.github/workflows/build-module.yml', 'print_targets.txt'
PORT_LABEL = 'port'
B1_ARMS = ('G-SHARED-ADDITIVE',)        # ### standing-b1: the shared additive files
B2_ARMS = ()                            # ### standing-b2a, standing-b2b: the chain's first half in two quarters, their verdicts banked, no arm
B3_ARMS = ('G-ACTROOT-VERIFY',)         # ### standing-b3: the chain's second half and the arm over every banked verdict
C_ARMS = ('G-PRIORBANK-UNCHANGED', 'G-NODISCLOSURE-PUBLIC', 'G-WRITELIST-KINDS', 'G-CORRESPONDENCE-CURRENCY', 'G-README-CURRENCY', 'G-PARTNER-COPIES',
          'G-SISTER-PINS', 'G-READ-RULE-STANDING')   # ### standing-c: the written files, the four figures and the read arm
NEED = {'standing-a': ('live', 'rules'), 'standing-c': ('written', 'figures'), 'standing-b1': ('additive',), 'standing-b2a': ('chain_a1',),
        'standing-b2b': ('chain_a2',), 'standing-b3': ('chain_b',), 'act': ('lvremote',)}
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
STD3 = ('Classical.choice', 'Quot.sound', 'propext')
LV_MODULES = tuple(REC0.LV_MODULES)
NEXT_RULES_GLOB = 'relay/data/b708_rules.txt'
# ### (R315)(2)(b), b705's repaired predicate, carried: the root bank's items read against the root route's own item list (tools/b698_record.py
# ### root_banks, rebound at tools/b707_record.py with ROOT_EXCLUDE extended per data/b706_rules.txt row (1)), no bank the route excludes
# ### required or admitted -- and (b706's (j)) the required list read against ROOT_EXCLUDE here, at import
REQUIRED_BANKS = ('data/b707_onset.txt', 'data/b707_onset_controls.txt', 'data/b707_onset_hashes.txt', 'data/b707_port.txt', 'data/b707_port_files.txt',
                  'data/b707_tool_repairs.txt', 'data/b707_repair_controls.txt', 'data/b707_roster_control.txt', 'data/b707_table_scope.txt',
                  'data/b707_corrigendum.txt', 'data/b707_registrations.txt', 'data/b707_registrations_reread.txt', 'data/b707_standing_figures.txt',
                  'data/b707_stepzero.txt', 'data/b707_report.txt', 'data/b707_citation_check.txt', 'data/b707_tests_stepzero.txt')
_EXCLUDED_REQUIRED = [p for p in REQUIRED_BANKS if REC0.R.ROOT_EXCLUDE.match(os.path.basename(p))]
if _EXCLUDED_REQUIRED:
    raise SystemExit('### REQUIRED_BANKS NAMES A BANK THE ROOT ROUTE EXCLUDES (b706`s (j)): %s' % _EXCLUDED_REQUIRED)


def rec(s=''):
    L.append(s)
    print(s)


def is_pushed():
    return (gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b707')
            and 'data/b707_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


def sealed_now():
    out = {}
    for t in K.SEALED:
        b = raw(os.path.join(T, t))
        out[t] = hashlib.sha256(b).hexdigest() if b is not None else None
    return out


def written_files():
    res = []
    for repo, name, pre in ((ROOT, 'relay', PRE['relay']), (PP, 'PLACE-papers', PRE['pp'])):
        ch = set(x for x in gs(repo, 'diff', '--name-only', pre).split(NL) if x.strip())
        ch |= set(x for x in gs(repo, 'diff', '--name-only', pre, 'HEAD').split(NL) if x.strip())
        res += ['%s/%s' % (name, x) for x in ch]
    return sorted(res)


def capture_now():
    return REC0.capture()


def prev_now():
    return REC0.prev_capture()


def ra_sources(lock):
    """tools/rule_arms.py's sources over the seat's session from (R317)'s anchor, its call trace extended by any continuation session's
    (K.SESSIONS_AFTER, none so far) through rule_arms.transcript."""
    R_ = RA.sources('b707', SESSION, K.ANCHOR, K.PARTS, lock, PRE['relay'], PRE['pp'])
    for sid, anc in K.SESSIONS_AFTER:
        R_['calls'] = list(R_.get('calls') or []) + RA.transcript('%s/%s.jsonl' % (PROJ, sid), anc)
    return R_


def conv_alone():
    P = 'p' + 'oss('
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to',
            'def ' + 'conv(']
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b707_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks):
                bad.append(f)
    return bad


def spec_planted():
    import b707_regspec as SPEC
    P = SPEC.planted()
    ctl = [ok for _w, ok in SPEC.controls()]
    return dict(read=[ok for _s, ok, _w in P], controls=ctl, shapes=[s for s, _o, _w in P])


def _deps(ax):
    return REC0._deps(ax)


def _tag_peel(repo, tag):
    return gs(repo, 'rev-parse', '--verify', '--quiet', 'refs/tags/%s^{commit}' % tag)


def wf_state():
    """this act's one run: the port branch's workflow at its commit against SIDE-explicit-formula's build-module.yml at main (badaccc, carried
    verbatim onto the branch under the author's word), the branch's lakefile's Mathlib requirement, its print list (absent at 93c27ec: the print
    step read as not run) against the run's print bank (none)."""
    out = {}
    t = read_blob(LV, '%s:%s' % (K.PORT_COMMIT, WF))
    src = read_blob(EF, '%s:%s' % (K.EF_MAIN, WF))
    lf = read_blob(LV, '%s:lakefile.lean' % K.PORT_COMMIT)
    req = re.search(r'(?im)^\s*require\b[^\n]*mathlib', lf)
    pt = read_blob(LV, '%s:%s' % (K.PORT_COMMIT, PT))
    out[K.KERNEL] = dict(text=t, before=src, wrote=gs(LV, 'log', '-1', '--format=%H', K.PORT_COMMIT, '--', WF), wrote_before_act=False,
                         lakefile=bool(lf.strip()), mathlib=bool(req), targets=[l.strip() for l in pt.split(NL) if l.strip()],
                         printed=len(_deps(rd('b707_axioms_%s_%s.txt' % (K.KERNEL, PORT_LABEL)))), act_writes=[WF], want=[])
    return out


def _kernel_sorry_code(repo, ref, subdir):
    """`sorry` tokens OUTSIDE comments and strings in every module under the kernel's lib at `ref`, through tools/no_sorry_main.py's lean_code."""
    import no_sorry_main as NSM
    out = []
    if not os.path.isdir(repo):
        return ''
    for f in gs(repo, 'ls-tree', '-r', '--name-only', ref, '--', subdir).split(NL):
        if f.strip().endswith('.lean'):
            out += ['%s:%d: %s' % (f.strip(), ln, t.strip()) for ln, t in NSM.sorry_hits(read_blob(repo, '%s:%s' % (ref, f.strip())))]
    return NL.join(out)


STANDING = sorted((set(g2_of(B706_FACE)) - set(K706.ACT_ARMS)) | set(K.STANDING_ADDED))
TESTS = ('test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py')


# ================================================================== THE CHAIN SPLIT BY ACT (b693's halves, b707 added; the first half in two quarters)
def chain_names():
    return [l.split()[0] for l in rd('act_roots.txt').split(NL) if l.strip() and not l.startswith('corrigendum ')]


def _acts_between(lo_hi):
    lo, hi = (int(x[1:]) for x in lo_hi)
    return [a for a in chain_names() if lo <= int(a[1:]) <= hi]


def half_acts(i):
    return _acts_between(K.CHAIN_HALVES[i])


def quarter_acts(q):
    return _acts_between(K.CHAIN_QUARTERS[q])


def boundary():
    a, b = K.CHAIN_HALVES[0][1], K.CHAIN_HALVES[1][0]
    rows = dict((l.split()[0], l.split()) for l in rd('act_roots.txt').split(NL) if l.strip() and not l.startswith('corrigendum '))
    ra, rb = rows.get(a) or [], rows.get(b) or []
    root_a, prev_b = (ra[1] if len(ra) > 1 else ''), (rb[2] if len(rb) > 2 else '')
    return dict(first=a, second=b, root=root_a, previous=prev_b, equal=bool(root_a) and root_a == prev_b)


def _verify(acts):
    import act_root as AR
    acts = set(acts)
    try:
        v = AR.verify(remote=KC0.remote_refs, acts=acts)
        reads = dict((k, v_) for k, v_ in dict(AR.READS_AT).items() if k in acts)
    except Exception as e:
        v, reads = [('raised', type(e).__name__, [])], {}
    return [list(x) for x in v], reads


def half_verify(i):
    return _verify(half_acts(i))


def quarter_verify(q):
    return _verify(quarter_acts(q))


def _run_key(base):
    return base.replace('b707_', '').replace('.txt', '')


def half_bank(i, key):
    """i is 'a1', 'a2' (the first half's quarters) or 'b' (the second half)."""
    return 'b707_chain_half_%s_%s.json' % (i, key)


def write_half(i, key, verdicts, reads, span):
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), head=gs(ROOT, 'rev-parse', 'HEAD'), half='%s-%s' % span,
             acts=verdicts, reads=reads, boundary=boundary())
    p = os.path.join(D, half_bank(i, key))
    with open(p + '.tmp', 'wb') as fh:
        fh.write((json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(p + '.tmp', p)


def _first_ts(cmds, pred):
    ts = [r['ts'] for r in cmds if r['tool'] in ('Bash', 'PowerShell') and pred(r['cmd'])]
    return iso_epoch(min(ts)[:19] + 'Z') if ts else None


def sources(need=()):
    """the sources the arms read; `need` (by part) names the heavy phases this part computes: 'live' (the three arms at HEAD), 'rules' (the
    rule arms' trace), 'written' (the written files, the public bytes, the prior banks), 'figures' (the four standing figures), 'chain_a1',
    'chain_a2' (the first half's quarters) and 'chain_b' (the second half), 'additive' (the shared files), 'lvremote' (one ls-remote of
    SIDE-lv-conservation, the act part alone: main, the deposit tag and the port branch at the remote)."""
    import b616_record as R6
    import edit_route as ER
    import b641_record as R41
    import additive_shared as ADD
    REC = REC0
    face = read(FACE)
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b707_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if (f.startswith('b707_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS)
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    cit = jl('b707_citation_check.json')
    try:
        REC.R._defect_short()
        refuses = False
    except TypeError:
        refuses = True
    t0 = time.time()
    cmds = capture_now()
    onset = _jgz('b707_onset.json.gz')
    S = dict(
        REC=REC, ER=ER, face=face, ferry=rd('b707_ferry.txt'), scan=rd('b707_ferry_scan.txt'), stepz=rd('b707_stepzero.txt'),
        readfirst=rd('b707_readfirst.txt'), defects=rd('b707_defects.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        answers=rd('b707_author_answers.txt'), answersj=jl('b707_author_answers.json'), prerun=rd('b707_arms_prerun.txt'), rl=jl('b707_record_lines.json'),
        tests=jl('b707_tests_stepzero.json'), testst=rd('b707_tests_stepzero.txt'), withheld=jl('b707_tests_withheld.json'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b707_seal_hashes.json'), sealnow=sealed_now(), cmds=cmds, prev_cmds=prev_now(), cmdj=jl('b707_commands.json'),
        cmdt=rd('b707_commands.txt'), reads_bank=rd('b707_read_calls.txt'), reads_json=jl('b707_read_calls.json'),
        planted={t: run_test(t) for t in TESTS}, spec=spec_planted(), conv_bad=conv_alone(), suite=read(os.path.join(T, 'b707_checks.py')),
        citation=rd(K.CITATION_BANK), cit_at=iso_epoch(cit.get('at') or ''), cit_misses=cit.get('misses') or [],
        gate=rd('b707_reg_gate.txt'), rowgen=rd('b707_rowgen_stepzero.txt'),
        branchj=jl('b707_branches.json'), branchbj=jl('b707_branches_before.json'), branchest=rd('b707_branches.txt'),
        branch_lists=dict((repo, gs(repo, 'branch', '--list', *bs)) for repo, bs in K.DELETE),
        repairs=rd('b707_tool_repairs.txt'), repair_ctl=rd('b707_repair_controls.txt'), rec_src=read(os.path.join(T, 'b707_record.py')),
        closing_src=read(os.path.join(T, 'b707_closing.py')),
        defshort=dict(b706=len(REC._defect_short('b706')), refuses=refuses),
        defshort_b707=REC._defect_short('b707'),
        corrj=jl('b707_corrigendum.json'), corrt=rd('b707_corrigendum.txt'), corrigenda=rd('b675_corrigenda.txt'),
        corrigenda_tri=tri(ROOT, 'data/b675_corrigenda.txt', PRE['relay']),
        guard=rd('b707_guard_dry.txt'), guardj=jl('b707_guard_dry.json'),
        rootdry=rd('b707_root_banks_dry.txt'), rootdryj=jl('b707_root_banks_dry.json'),
        figj=jl('b707_standing_figures.json'), figt=rd('b707_standing_figures.txt'),
        # ### (R317)(2): the three readers` repairs and their controls
        roster=jl('mirror_roster.json') if os.path.isfile(os.path.join(D, 'mirror_roster.json')) else json.loads(read(os.path.join(T, 'mirror_roster.json')) or '{}'),
        roster_ctl=rd('b707_roster_control.txt'), roster_pre=json.loads(blob(ROOT, PRE['relay'] + ':tools/mirror_roster.json') or b'{}'),
        tscope=rd('b707_table_scope.txt'), tscopej=jl('b707_table_scope.json'), tt_src=read(os.path.join(T, 'terminal_table.py')),
        ra_src=read(os.path.join(T, 'rule_arms.py')), b706_tfj=jl('b706_table_final.json'),
        # ### (R317)(3): the onset
        onset=rd('b707_onset.txt'), onset_ctl=rd('b707_onset_controls.txt'), onset_hashes=rd('b707_onset_hashes.txt'), onsetj=onset,
        onset_gz=raw(os.path.join(D, 'b707_onset.json.gz')),
        # ### (R317)(4): the registrations
        regs=rd('b707_registrations.txt'), regs_reread=rd('b707_registrations_reread.txt'), regs_rereadj=jl('b707_registrations_reread.json'),
        regs_blob_reg=gs(ROOT, 'rev-parse', '--verify', '--quiet', '%s:data/b707_registrations.txt' % K.REG_COMMIT),
        regs_blob_head=gs(ROOT, 'rev-parse', '--verify', '--quiet', 'HEAD:data/b707_registrations.txt'),
        regs_blob_now=gs(ROOT, 'hash-object', '--', 'data/b707_registrations.txt'),
        regs_log=[l for l in gs(ROOT, 'log', '--format=%h', '--', 'data/b707_registrations.txt').split(NL) if l.strip()],
        # ### (R317)(5): the port
        port=rd('b707_port.txt'), portj=jl('b707_port.json'), port_files=rd('b707_port_files.txt'), port_filesj=jl('b707_port_files.json'),
        port_push=rd('b707_port_push_out.txt'), dispj=jl('b707_dispatches.json'), runner_rows=jl('b707_runner_rows.json'),
        buildlog=rd('b707_buildlog_%s_%s.txt' % (K.KERNEL, PORT_LABEL)), portrun=rd('b707_runner_%s_%s.txt' % (K.KERNEL, PORT_LABEL)),
        lv_main=gs(LV, 'rev-parse', 'main'), lv_v0100=_tag_peel(LV, 'v0.10.0'), lv_port=gs(LV, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.PORT_BRANCH),
        lv_port_parent=gs(LV, 'rev-parse', '--verify', '--quiet', K.PORT_COMMIT + '^'), lv_port_files=files_of(LV, K.PORT_COMMIT),
        lv_tags=[t for t in gs(LV, 'tag', '--list').split(NL) if t.strip()], lv_remote={},
        lv_sorry=_kernel_sorry_code(LV, K.PORT_COMMIT, 'SIDELvConservation'),
        ef_main=gs(EF, 'rev-parse', 'main'), ef_tags=dict((t, _tag_peel(EF, t)) for t in ('v0.37', 'v0.1', 'v0.2')),
        ef_log=[l for l in gs(EF, 'log', '--first-parent', '--format=%H', K.EF_V037 + '..main').split(NL) if l.strip()],
        join_main=gs(KI, 'rev-parse', 'main') if os.path.isdir(KI) else '', join_tags=[t for t in gs(KI, 'tag', '--list').split(NL) if t.strip()] if os.path.isdir(KI) else [],
        orders_line=jl('b707_orders.json'), orders_line1=jl('b707_orders_1.json'),
        prompt1=rd('b707_prompt1_print.txt'),
        rf_diff=rd('b707_readfirst_diff.txt'), rf_hand_now=blob(ROOT, 'HEAD:data/b707_readfirst.txt'),
        rf_hand_z=blob(ROOT, '%s:data/b707_readfirst.txt' % K.STEPZERO_BANKS) if K.STEPZERO_BANKS else None,
        asec=jl('b707_arm_seconds.json'), asect=rd('b707_arm_seconds.txt'),
        shared=dict((p, (cr0(blob(ROOT, '%s:%s' % (PRE['relay'], p))), cr0(raw(os.path.join(ROOT, *p.split('/')))), cr0(blob(ROOT, 'HEAD:' + p))))
                    for p in K.SHARED_APPENDED),
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), c2=_ct(ROOT, K.C2_RELAY), c2pp=(_ct(PP, K.C2_PP) if K.C2_PP else None),
               c3=_ct(ROOT, K.C3_RELAY), c3pp=(_ct(PP, K.C3_PP) if K.C3_PP else None), c4=_ct(ROOT, K.C4_RELAY), stepzero=_ct(ROOT, K.STEPZERO_BANKS),
               reg=_ct(ROOT, K.REG_COMMIT), port=_ct(LV, K.PORT_COMMIT)),
        files=dict(stepzero=files_of(ROOT, K.STEPZERO_BANKS) if K.STEPZERO_BANKS else [], c1=files_of(ROOT, K.C1_RELAY), c1pp=files_of(PP, K.C1_PP),
                   c2=files_of(ROOT, K.C2_RELAY), c2pp=(files_of(PP, K.C2_PP) if K.C2_PP else []), c3=files_of(ROOT, K.C3_RELAY), c3pp=(files_of(PP, K.C3_PP) if K.C3_PP else []),
                   c4=files_of(ROOT, K.C4_RELAY), reg=files_of(ROOT, K.REG_COMMIT), port=files_of(LV, K.PORT_COMMIT)),
        standing=STANDING, wf=wf_state(),
        export_present=os.path.exists(os.path.join(ROOT, *EXPORT.split('/'))), export_log=gs(ROOT, 'log', '--all', '--format=%h', '--', EXPORT),
        export_index=gs(ROOT, 'ls-files', '--', EXPORT), export_status=gs(ROOT, 'status', '--porcelain', '--', EXPORT),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b707_act_root.json'), arj0=jl('b706_act_root.json'), art=rd('b707_act_root.txt'), rootsf=rd('act_roots.txt'),
        rootbanks=jl('b707_root_banks.json'), route_list=REC.root_banks(),
        pushout=(files_of(ROOT, K.STEPZERO) if K.STEPZERO else [], bool(K.STEPZERO) and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, *f.split('/')))), cr0(blob(ROOT, 'HEAD:tools/' + f)))
              for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        pp_renames=gs(PP, 'diff', '--name-status', '-M', PRE['pp'], 'HEAD'),
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b707_kernels_face.json').get('kernels') or {}), kerns_read=list(dict.fromkeys(REC._kerns())) + ['SIDE-faces-join'],
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mustfail=not os.path.exists(os.path.join(D, 'b707_mustnotexist.txt')),
        fj=jl('b707_findings.json'), tj=jl('b707_trail.json'), sc=jl('b707_scores.json'), desk=rd('b707_desk_notes.txt'), tfj=jl('b707_table_final.json'),
        lsr=None,
        rlog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(ROOT, 'log', '--reverse', '--format=%h %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        plog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(PP, 'log', '--reverse', '--format=%h %ct %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()],
    )
    S['first_delete_ts'] = _first_ts(cmds, lambda c: bool(REC.delete_shape(c)[0]))
    if 'lvremote' in need:
        refs = {}
        for l in git(LV, 'ls-remote', 'origin')[1].split(NL):
            if '\t' in l:
                sha, ref = l.split('\t', 1)
                refs[ref.strip()] = sha.strip()
        S['lv_remote'] = refs
    S['root_at_commit'] = _root_named_at_commit(S['arj'])
    S['secs_ct'] = dict((p, _ct(ROOT, gs(ROOT, 'log', '-1', '--format=%H', '--', 'data/b707_arm_seconds_%s.json' % p))) for p in K.PARTS)
    S['root_ct'] = _ct(ROOT, (S['arj'].get('commit') or {}).get('relay') or '')
    S['phase_secs'] = {'the banks and the state': time.time() - t0}
    S['pp_allowed'] = sorted(set(K.PP_WRITTEN))
    t1 = time.time()
    S['live'] = live_arms() if 'live' in need else dict(names=[], nsm=[], ac=[], ac_counts={}, mh=[], mh_per={}, secs=(0, 0, 0))
    S['phase_secs']['the three arms at HEAD' + ('' if 'live' in need else ' (not in this part)')] = time.time() - t1
    t1 = time.time()
    S['ra'] = ra_sources(S['lock_epoch']) if 'rules' in need else {}
    S['phase_secs']['the rule arms` trace' + ('' if 'rules' in need else ' (not in this part)')] = time.time() - t1
    t1 = time.time()
    if 'figures' in need:
        import b706_standing_figures as SF6   # ### b706's tool, unedited: the readers over b706's roster at the unversioned names
        base = jl('b706_standing_figures.json')
        S['fig'] = SF6.all_figures(baseline=((base.get('pins') or {}).get('rows') or {}), remote=KC0.remote_refs)
        S['fig_prev'] = base
        S['fig_prev_name'] = 'b706_standing_figures.json (b706`s figures; the readers over b706`s roster, data/b706_roster_read.json)'
    else:
        S['fig'], S['fig_prev'], S['fig_prev_name'] = {}, {}, ''
    S['phase_secs']['the four standing figures' + ('' if 'figures' in need else ' (not in this part)')] = time.time() - t1
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
            if f.startswith(('b707_', 'audit_b707_')) and os.path.isfile(os.path.join(D, f)) and not f.endswith(('.gz', '.png', '.jsonl')):
                pub.append(read(os.path.join(D, f)))
        pub += [read(f) for f in tools]
        pub += [read_blob(LV, '%s:%s' % (K.PORT_COMMIT, WF)), read(os.path.join(T, 'mirror_roster.json'))]
        S['nd_pub'] = R6.nd_hits(NL.join(pub), S['nd_sets'])[0]
        shared = set(ADD.shared_files()) | set(K.SHARED_APPENDED)
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
    if 'chain_a1' in need:
        S['ar_verify'], S['ar_reads'] = quarter_verify(0)
    if 'chain_a2' in need:
        S['ar_verify'], S['ar_reads'] = quarter_verify(1)
    if 'chain_b' in need:
        S['ar_verify'], S['ar_reads'] = half_verify(1)
    S['phase_secs']['the act-root chain`s part' + ('' if any(x in need for x in ('chain_a1', 'chain_a2', 'chain_b')) else ' (not in this part)')] = time.time() - t1
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


# ### the eight test files not clean at step zero: the three b706 carried and the five readers the renames of (R316)(3) broke (data/b707_defects.txt, the events)
STEPZERO_FAILING = {'test_chain_page.py': ['(1)', '(9)', '(14)'], 'test_chain_page_b629.py': ['(8)'], 'test_chain_page_b638.py': ['(4)', '(5)', '(6)', '(7)'],
                    'test_composer_b646.py': ['(10)', '(11)', '(17)', '(19)'], 'test_composer_b647.py': ['(4)', '(5)', '(7)', '(9)', '(17)', '(18)'],
                    'test_composer_b649.py': [], 'test_g_chain_page.py': ['(1)'], 'test_name_b649.py': ['(5)']}


def tests_ok(S):
    j = S['tests']
    names = sorted(S['tracked_tests'])
    nf = dict((n, x['failing']) for n, x in j.items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(j) == sorted(set(names) - {'test_elab_reader_b634.py'}) and sorted(nf) == sorted(STEPZERO_FAILING) \
        and all(sorted(nf[n]) == sorted(STEPZERO_FAILING[n]) for n in nf if STEPZERO_FAILING[n]) \
        and 'b704_nodes_zeta.txt' in (j.get('test_chain_page.py') or {}).get('args', []) \
        and 'test_elab_reader_b634.py' in S['withheld'] \
        and ('TEST FILES %d ; RUN %d ; WITHHELD 1 ; NOT CLEAN 8' % (len(names), len(names) - 1)) in unwrap(S['testst'])


UNANSWERED = "The user doesn't want to proceed with this tool use"


def answers_ok(S):
    a = S['answers']
    m = re.search(r'^### b707 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
    heads = re.findall(r'^### PROMPT \d+ \(', a, re.M)
    calls = re.findall(r'^### CALL tool-use id ', a, re.M)
    res = re.findall(r'^RESULT \(transcript line [^)]*\): (.*)$', a, re.M)
    if not m or int(m.group(1)) != len(heads) or len(heads) < FLOORS['prompts'] or len(calls) < FLOORS['calls'] or not heads:
        return False
    per = [len(re.findall(r'^  OPTION \d+', p, re.M)) for p in re.split(r'^### PROMPT \d+ \(', a, flags=re.M)[1:]]
    lk = S['lock_epoch']
    after = [c for c in S['answersj'].get('calls') or [] if lk and iso_epoch((c.get('ts') or '')[:19] + 'Z') and iso_epoch((c.get('ts') or '')[:19] + 'Z') > lk]
    return all(x >= 2 for x in per) and len(res) == len(calls) and not any(UNANSWERED in r or '### NO RESULT' in r for r in res) \
        and len(after) <= _post_seal_named(S['face'])


def no_local_lean(S):
    return bool(S['cmds']) and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and S['REC'].local_lean(r['cmd'])]


# ================================================================== (R317) STEP ZERO: THE CITATION CHECK, THE BRANCHES, THE READ-FIRST BANK
READFIRST_NEEDLES = ('relay data/b706_closing.txt | :1-:200 ; :201-:400 ; :401-:420', 'relay data/b706_defects.txt | :1-:152', 'relay data/b706_report.txt | :1-:12',
                     'relay data/b706_buildlog_SIDE-faces-join_join.txt | :1-:25 ; :150-:169', 'relay tools/mirror_roster.json | :1-:91',
                     'relay tools/terminal_table.py | :470-:514', 'relay tools/rule_arms.py | :285-:314 ; :530-:574', 'relay data/b705_registrations.txt | :1-:57',
                     'relay data/b705_i6_ranking.txt | :1-:72', 'relay tools/b696_witness_balls.py | :1-:200 ; :201-:400', 'relay tools/b705_window.py | :1-:200 ; :201-:285',
                     'relay tools/b694_witness_terms.py | :1-:200 ; :201-:400', 'relay data/b705_detection.txt ; data/b705_detection_controls.txt',
                     'SIDE-lv-conservation lean-toolchain ; lake-manifest.json ; lakefile.lean', 'SIDE-lv-conservation SIDELvConservation/GammaBounds.lean | :140-:209',
                     'SIDE-explicit-formula lean-toolchain ; lake-manifest.json ; .github/workflows/build-module.yml', 'relay data/b705_source_cc_2006_13771.txt | :1-:30 ; :88-:137',
                     'PLACE-papers OPEN_TRAILS.md | :15450-:15455 ; :15588-:15593 ; :15628-:15657', 'relay data/b706_table_final.txt | :1-:34')
NAMED_PUSH = sorted(b for _r, bs in K.DELETE for b in bs)


def readfirst_ok(S):
    z = unwrap(S['readfirst'])
    return bool(z) and all(x in z for x in READFIRST_NEEDLES) and 'ITEMS 44 ;' in z


def branches_ok(S):
    z = S['branchest']
    left = dict((r, sorted(x.strip() for x in v.split(NL) if x.strip())) for r, v in S['branch_lists'].items())
    return all(v == [] for v in left.values()) and len(left) == 4 and all(b in z for b in NAMED_PUSH) \
        and 'BRANCHES NAMED 8 ; DELETED 8 ; KEPT 0 ; EVERY TIP MERGED True' in unwrap(z)


def branches_banked_ok(S):
    rows = S['branchj'].get('rows') or []
    try:
        fates = [S['REC'].read_branch_row(r) for r in rows]
    except Exception:
        return False
    bt = iso_epoch((S['branchbj'].get('at') or '')[:19] + 'Z')
    fd = S['first_delete_ts']
    return len(rows) == 8 and all(f == 'DELETED' for _b, f in fates) and all(r['merged'] for r in rows) \
        and sorted(r['branch'] for r in rows) == NAMED_PUSH and bool(bt) and bool(fd) and bt < fd and len(S['branchbj'].get('rows') or []) == 8 \
        and bool(S['cit_at']) and S['cit_at'] < fd


def deletes_one_ok(S):
    """every branch delete of the act one branch, no glob, no variable, nothing chained after: the eight of (R317)(7) alone; port-b707 deleted
    under no answer."""
    sh_ = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell')]
    shapes = [(S['REC'].delete_shape(r['cmd']), S['REC'].chained_after(r['cmd'])) for r in sh_]
    shapes = [(s, c) for s, c in shapes if s[0]]
    named = set(NAMED_PUSH)
    got = sorted(x for (d, _g, _v), _c in shapes for x in d)
    return bool(shapes) and all(len(d) == 1 and not gl and not vs and not c for (d, gl, vs), c in shapes) \
        and set(got) <= named and all(b in got for b in NAMED_PUSH) and K.PORT_BRANCH not in got \
        and ('BRANCH DELETES OF ONE BRANCH, NO GLOB, NO VARIABLE AND NOTHING CHAINED AFTER %d OF %d' % (len(shapes), len(shapes))) in S['cmdt']


def dry_step_ok(S):
    g = S['gate']
    return '--- THE DRY-RUN STEP ((R267)(2))' in g and 'ENTRY : table cells NONE ; screens QUIET' in g and 'TRAIL : table cells NONE ; screens QUIET' in g \
        and 'THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK True' in g and 'THE TRAIL`S RESOLVED LINE EQUAL TO THE DEFECTS BANK True' in g \
        and '### ### **THE DRY-RUN STEP : CLEAN**' in g and '### ### **GATE VERDICT : CLEAR**' in g


def closing_dry_ok(S):
    g = S['gate']
    return '--- THE CLOSING DRY-RUN STEP (b675 rules row 1)' in g and '### ### **THE CLOSING DRY-RUN STEP : CLEAN**' in g \
        and 'b707 closed:' in g and 'THE REPAIRS' in g and 'THE ONSET' in g and 'THE PORT' in g and 'THE REGISTRATIONS' in g \
        and '### THE STANDING ARMS' in g and '### THE ORDERS' in g and '### THE KERNELS' in g and '(g) The defects (a)' in g and '### NO VERDICT LINE' not in g


def citation_ok(S):
    """the citation check's bank: every cite checked, OK and misses summing, its five misses the navigator's ((c), (d), (e) by the fact clause,
    (f) and (g) raised and answered); the bank written before the step-zero banks' commit and that commit before Component 1's."""
    c = S['citation']
    m = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', c)
    return bool(m) and int(m.group(1)) == int(m.group(2)) + int(m.group(3)) > 0 and 'A GATE STEP AT STEP ZERO' in c \
        and int(m.group(3)) == len(S['cit_misses']) == 5 and bool(S['cit_at']) and bool(S['t'].get('stepzero')) \
        and S['cit_at'] < S['t']['stepzero'] and bool(S['t'].get('c1')) and S['t']['stepzero'] <= S['t']['c1']


def rowgen_ok(S):
    return '### ### **CONSTELLATION EXIT 0 ; ROWGEN DIFF EXIT 0 ; TABLES 19 ; RE-POINTED 8.**' in S['rowgen']


def weight_ok(S):
    return landed(S, 0, ['b706 AT ITS WEIGHT', '37e4a12f'])


# ### (R315)(2)(c), b705's repaired predicate, carried: the checks the root prompt requires are admitted after the seal, each printed with its
# ### time by the record tool's control; every other check before the lock and before the step it governs.
ROOT_PROMPT = re.compile(r'\broot\b', re.I)


def _answers_checked(S, floors, act=707, lock_key='lock_epoch'):
    c = S['citation']
    stamps = re.findall(r'### \(R278\)\(4\) THE MID-ACT CHECK \((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\): the (?:navigator`s )?answer carrying \'([^\']+)\'', c)
    figs = re.findall(r'ANSWER CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)(?: -- RAISED: ([^*]*?))?\.\*\*', c)
    last = {}
    for (t_, n_), f_ in zip(stamps, figs):
        last[n_] = f_
    later = all(m_ == '0' or (bool(r_) and all(re.match(r'^data/b(\d{3})_\S+$', x.strip()) and int(re.match(r'^data/b(\d{3})_', x.strip()).group(1)) > act
                                               for x in (r_ or '').split(';') if x.strip())) for _c, _o, m_, r_ in last.values())
    lk = S[lock_key] or 10 ** 12
    times = [iso_epoch(t_) for t_, _n in stamps]
    rootc = [(x, t_, n) for x, (t_, n) in zip(times, stamps) if x and x >= lk]
    return len(stamps) >= max(floors, 1) and len(figs) >= len(stamps) and later and all(times) and bool(rootc) == (S.get(lock_key) is not None and bool(S.get('root_prompted', rootc)))


def root_checks(S, lock_key='lock_epoch'):
    c = S['citation']
    stamps = re.findall(r'### \(R278\)\(4\) THE MID-ACT CHECK \((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\): the (?:navigator`s )?answer carrying \'([^\']+)\'', c)
    lk = S[lock_key] or 10 ** 12
    return [(t_, n) for t_, n in stamps if iso_epoch(t_) and iso_epoch(t_) >= lk]


def answers_checked_ok(S):
    return _answers_checked(S, FLOORS['checks'])


# ================================================================== (R317)(1)-(2): THE RECORD LINES, THE REPAIRS, THE CORRIGENDUM
def scorer_banks_ok(S):
    n = ''.join(strip_prose(_fn_src(S['rec_src'], f)) for f in ('_n1', '_n2', '_n3', '_n4'))
    sc = strip_prose(_fn_src(S['rec_src'], 'scores'))
    ft = strip_prose(_fn_src(S['rec_src'], '_finding_text'))
    return bool(n) and '_commands.json' in n and '_dispatches.json' in n and '_onset' in n and '_port' in n \
        and not re.search(r'\b(FIND|OT)\b|FINDINGS|OPEN_TRAILS|findings|entry_line', n) \
        and "os.path.isfile(os.path.join(D, '%s_scores.json' % ACT))" in sc and 'scores_line(S)' in ft and "jl('%s_scores.json' % ACT)" in ft


def entry_scores_ok(S):
    want = conv(S['REC'].scores_line(S['sc'])) if S['sc'] else None
    blk = _entry_block(S)
    got = [l for l in blk.split(NL) if l.startswith('**The scores.**')]
    return bool(want) and bool(S['sc']) and got == [want]


# ### the title by its objects ((R317)(6)), compared after case-folding the article alone (b706's repaired predicate, carried)
TITLE_NEEDLES = ('the sign-onset radius at the Epstein zeta of x² + xy + 6y²', 'the ζ form positive at every radius', 'SIDE-lv-conservation’s forward-port at the shared pin',
                 'of 15 modules building', 'the twelve higher pairs’ route registered')


def _fold_article(t):
    return re.sub(r'^(## )(The|A|An)( )', lambda m: m.group(1) + m.group(2).lower() + m.group(3), t)


def entry_title_ok(S):
    e = S['fj'].get('entry_line')
    t = S['REC']._title()
    f = _fold_article(t)
    return bool(e) and fline(S, e) == conv(t) and t.startswith('## ') and all(n in f for n in TITLE_NEEDLES)


def trail_tail(S):
    t = S['ot']
    i = t.find(conv(S['REC'].TRAIL_HEAD()))
    return t[i:] if i >= 0 else ''


def trail_defects_ok(S):
    m = re.search(r'^\*\*Defects\*\* \(relay data/b707_defects\.txt\): (.*)\.$', trail_tail(S), re.M)
    return 'THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK True' in S['gate'] and bool(m) \
        and m.group(1) == conv('; '.join(S['defshort_b707']) or 'none')


RESOLVED = re.compile(r'^\*\*Resolved by the seat, for the author’s strike:\*\* .*\((\d+)\) the (\w+) navigator (?:miss|misses)'
                      r'(?: \(\([a-z]\)(?:, \([a-z]\))*\))? and the seat’s (\w+) defects? as lettered\.$', re.M)


def trail_resolved_ok(S):
    m = RESOLVED.search(trail_tail(S))
    nav, seat = _owners(S['defshort_b707'])
    return 'THE TRAIL`S RESOLVED LINE EQUAL TO THE DEFECTS BANK True' in S['gate'] and bool(m) and S['REC'].num_word(nav) == m.group(2) \
        and S['REC'].num_word(seat) == m.group(3)


def corrigendum_ok(S):
    """(R317)(2): the generated entry landed (its line in the bank, the title at that line through conv), (i)-(m) and the three trail arms
    answered; the corrigenda bank appended at row (27) and nothing before it changed; in Component 1's commit."""
    j = S['corrj']
    e = j.get('entry_line')
    now, pre, head = S['corrigenda_tri']
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and j.get('lettered') == ['i', 'j', 'k', 'l', 'm'] and len(j.get('trail_arms') or []) == 3 \
        and j.get('row') == 27 and '  (27) ' in S['corrigenda'] and '  (28) ' not in S['corrigenda'] \
        and pre is not None and (now or b'').startswith(pre) and (head or b'').startswith(pre) and 'FINDINGS :%d' % e in S['corrt'] \
        and 'data/b707_corrigendum.txt' in S['files']['c1']


GUARD_WRITE = "sp = os.path.join(D, 'b707_arm_seconds_%s.json' % PART)"   # ### the write's own line, stripped; matched whole, not by a needle


def guard_ok(S):
    s = S['suite'].split(NL)
    i = next((k for k, l in enumerate(s) if l.strip() == GUARD_WRITE), None)
    j = S['guardj']
    return i is not None and s[i - 1].strip() == 'if PRERUN:' and 'POST-ROOT PATH WRITES NONE' in S['guard'] \
        and (j.get('writes') or {}).get('pre-push') == [] and (j.get('writes') or {}).get('post-push') == [] \
        and (j.get('writes') or {}).get('prerun') == ['data/b707_arm_seconds_<part>.json']


def postroot_writes_none(S):
    j = S['guardj']
    w = j.get('writes') or {}
    return 'POST-ROOT PATH WRITES NONE' in S['guard'] and w.get('pre-push') == [] and w.get('post-push') == [] and bool(S['root_ct']) \
        and sorted(S['secs_ct']) == sorted(K.PARTS) and all(v is not None and v <= S['root_ct'] for v in S['secs_ct'].values())


def trail_lines_equal_defects(S):
    tail = trail_tail(S)
    dm = re.search(r'^\*\*Defects\*\* \(relay data/b707_defects\.txt\): (.*)\.$', tail, re.M)
    rm = RESOLVED.search(tail)
    bank = re.findall(r"^    \(([a-z])\) THE (NAVIGATOR|SEAT)'S", S['defects'], re.M)
    want = (sum(1 for _x, o in bank if o == 'NAVIGATOR'), sum(1 for _x, o in bank if o == 'SEAT'))
    if not dm or not rm or not bank:
        return False
    got_d = KIND.findall(dm.group(1))
    have_d = (sum(1 for _x, o in got_d if o == 'NAVIGATOR'), sum(1 for _x, o in got_d if o == 'SEAT'))
    have_r = (rm.group(2), rm.group(3))
    return have_d == want and have_r == (S['REC'].num_word(want[0]), S['REC'].num_word(want[1]))


def read_rule_standing_ok(S):
    return RDA.reading_text(S['reads_bank'])[0]


def _read_plant(S):
    return put(S, 'reads_bank', S['reads_bank'] + NL + '  99999 | 2099-01-01T00:00:00Z | 500 | offset None | limit None | WHOLE | planted.py')


def wl_ok(S):
    return C3.wl_ok(S) and S.get('next_rules', NEXT_RULES_GLOB) in S['globs']


# ================================================================== THE RUNNER (this act's one run: the port branch, held; the print step not run)
IDENT_WF = ('secrets.', 'psinary', 'seale', 'york', 'hotmail', 'orcid', '0009-0008')


def _wf_ok(S, kernel, rules_needle='(1) THE PROBE ROUTE\'S TARGET IS print_targets.txt WHOLE'):
    """b705's repaired reading over every run of the act: the workflow as carried, no identifier, the hold, the cache step, the print step over
    its list, every listed name printed by the run, AND each dispatch's target the whole target the rule names (data/b705_rules.txt row (1))."""
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
    rows = S['dispj'].get('rows') or []
    return sorted(S['wf']) == [kernel] and len(rows) == 1 and all(r.get('whole') is True for r in rows) \
        and rd('b705_rules.txt').count(rules_needle) == 1


def wf_ok(S):
    return _wf_ok(S, K.KERNEL)


def runner_ok(S):
    """this act's one run as read by its id: at its ref, success, the artifact's sha256, the memory low above the hold, no STOP line, the gate
    DERIVES; the row through the record tool's reader. The port run holds (6 of 12, the print step not run), so the arm fails, declared."""
    rows = S['runner_rows'].get('rows') or []
    if len(rows) != 1:
        return False
    try:
        for r in rows:
            S['REC'].read_runner_row(r)
    except Exception:
        return False
    r = rows[0]
    return r.get('kernel') == K.KERNEL and r.get('ref') == K.PORT_COMMIT and r.get('run_id') == K.PORT_RUN \
        and r.get('conclusion') == 'success' and bool(r.get('artifact_sha256')) and r.get('mem_low') is not None and r['mem_low'] >= K.HOLD \
        and not r.get('stopped') and r['gate'] == 'DERIVES'


def gate_ok(S):
    t = S['portrun']
    return 'GATE DERIVES' in t and 'BUILD EXIT 0 ; ERROR LINES 0' in t and re.search(r'^### the artifact: .* ; AGREE$', t, re.M) is not None


def merges_ok(S):
    """no merge this act: SIDE-lv-conservation's main and its deposit v0.10.0 unmoved, its port branch at the one commit on 93c27ec locally and
    at the remote, no tag made; SIDE-explicit-formula's main at badaccc (one first-parent commit past v0.37), its tags unmoved; the join
    kernel's main at its manifest commit, no tag; no sorry in code on the port branch beyond v0.10.0's own pinned one (T3_StepNineBridge :92)."""
    sorry_lines = [l for l in S['lv_sorry'].split(NL) if l.strip()]
    return S['lv_main'] == K.LV_MAIN and S['lv_v0100'] == K.LV_V0100 and S['lv_port'] == K.PORT_COMMIT and S['lv_port_parent'] == K.LV_V0100 \
        and sorted(S['lv_port_files']) == sorted(K.PORT_FILES) and 'v0.10.0' in S['lv_tags'] and not [t for t in S['lv_tags'] if t.startswith('v0.1') and t > 'v0.13.0'] \
        and (not S['lv_remote'] or (S['lv_remote'].get('refs/heads/' + K.PORT_BRANCH) == K.PORT_COMMIT and S['lv_remote'].get('refs/heads/main') == K.LV_MAIN)) \
        and S['ef_main'] == K.EF_MAIN and len(S['ef_log']) == 1 and S['ef_tags'].get('v0.37') == K.EF_V037 \
        and S['join_main'] == K.JOIN_TIP and S['join_tags'] == [] and all('T3_StepNineBridge.lean' in l for l in sorry_lines)


# ================================================================== SCOPE, THE SEAL, THE ROOT, THE RECORD
def seal_hashes_ok(S):
    j = S['sealj']
    at = iso_epoch(j.get('at') or '')
    rec_ = j.get('tools') or {}
    return bool(rec_) and at is not None and S['lock_epoch'] is not None and S['lock_epoch'] <= at \
        and sorted(rec_) == sorted(K.SEALED) and all(S['sealnow'].get(t) == rec_[t] for t in K.SEALED)


POST_SEAL = ('b707 seal', 'b707 pre-root', 'b707 root', 'b707 record', 'b707 --', 'b707 closing', 'b707 entry')


def _component_commit(s):
    return s.startswith('b707') and not s.startswith(POST_SEAL)


def sealed_after_ok(S):
    lk = S['lock_epoch']
    if lk is None:
        return False
    return all((t < lk) == _component_commit(s) for h, s, t in S['rlog']) and all((t < lk) == _component_commit(s) for h, s, t in S['plog']) \
        and any(_component_commit(s) for h, s, t in S['plog'])


def _root_banked(S, act, nrows, prev_key='arj0', route_key='route_list', required=REQUIRED_BANKS, exclude=None):
    import act_root as AR
    j, j0 = S['arj'], S[prev_key]
    rows = _chain_rows(S)
    items = j.get('items') or []
    paths = sorted(it.split()[0] for it in items if it.startswith('data/'))
    ex = exclude or S['REC'].R.ROOT_EXCLUDE
    return bool(j) and len(rows) == nrows and rows[nrows - 1][:3] == [act, j.get('root'), j0.get('root')] \
        and AR.root_of(items, j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) \
        and paths == sorted(S[route_key]) \
        and not [p for p in paths if ex.match(os.path.basename(p)) or p.endswith(('.gz', '.png', '.jsonl'))
                 or 'b628_intake_crank' in p or 'b647_navigator_memory' in p] \
        and all(p in paths for p in required) and (j.get('commit') or {}).get('relay')


def root_banked_ok(S):
    return _root_banked(S, 'b707', 84)


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b707_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    """the chain recomputed at commit in three parts: standing-b2a's and standing-b2b's banked quarters (b624-b641, b642-b658) and
    standing-b3's second half (b659-b707), every act AGREE, the boundary link equal, b680 read through its corrigendum row, b707 written LF."""
    ha = S['half_a'] or {}
    v = [tuple(x[:2]) for x in (ha.get('acts') or [])] + [tuple(x[:2]) for x in (S['ar_verify'] or [])]
    r = dict(ha.get('reads') or {}, **(S['ar_reads'] or {}))
    return ha.get('head') == gs(ROOT, 'rev-parse', 'HEAD') and [x[0] for x in v] == ['b%d' % i for i in range(624, 708)] \
        and all(x[1] == 'AGREE' for x in v) and (r.get('b707') or {}).get('crlf') == 0 and (r.get('b680') or {}).get('corrected') == 4 \
        and (ha.get('boundary') or {}).get('equal') is True and S['boundary'].get('equal') is True \
        and (ha.get('boundary') or {}).get('root') == S['boundary'].get('root')


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


def corpus_scope_ok(S):
    """N5: PLACE-papers' changed files within the two ledgers alone; no rename."""
    ch = S['pp_changed']
    ren = [l for l in S['pp_renames'].split(NL) if l[:1] in ('R', 'D')]
    return bool(ch) and set(ch) <= set(S['pp_allowed']) and 'FINDINGS.md' in ch and 'OPEN_TRAILS.md' in ch and not ren


ENTRY_NEEDLES = ('**The corrigendum**', '**The repairs**', '**The onset**', '**The registrations**', '**The port**', '**The standing arms**',
                 '**The orders**', '**The citation check**', '**The scores.**', '**Read in mutual light**', 'strengthens', '**Carried to:**',
                 '**Next.**', 'b708', 'SIDE-lv-conservation', 'C7OrderBounds.lean :277')


def finding_ok(S):
    e = S['fj'].get('entry_line')
    tail = _entry_block(S)
    return bool(e) and fline(S, e) == conv(S['fj'].get('title') or '\x00') and all(conv(x) in tail for x in ENTRY_NEEDLES)


def scored(S, k):
    v = S['sc'].get(k)
    try:
        _k, w, _t = S['REC'].read_score_row(k, v)
    except Exception:
        return False
    return w.split(' ')[0].split(',')[0].rstrip(';') in ('HELD', 'REFUTED', 'NOT', 'HOLDS', 'PENDING') and ('(%s)' % k) in S['desk']


def closing_sentence_ok(S):
    t = S['closing_src']
    return ('no identifier of the author ' + 'in any outbound') in t and ('plain requests to ' + 'github.com') in t \
        and '### THE CITATION CHECK' in t and '### THE RECORD LINES' in t and '### THE DRY RUN' in t and 'THE REPAIRS' in t and 'THE ONSET' in t \
        and 'THE PORT' in t and 'THE REGISTRATIONS' in t and 'THE STANDING ARMS' in t and 'THE ORDERS' in t and '### THE KERNELS' in t \
        and '### THE MIRROR' in t and '### THE CARRY-TIME' in t


# ================================================================== THIS ACT'S ARMS OVER ITS OWN BANKS (Component 5)
NAV_LETTERS = ('c', 'd', 'e', 'f', 'g')
# ### each mid-act answer's needle and the component commit that acted on it: the roster answer at Component 1's relay commit, the port answer at
# ### the port branch's commit (Component 3)
ANSWER_NEEDLES = (('Roster: 1, re-point four', 'c1'), ('Port: 1, two more files', 'port'))


def defects_ok(S):
    rows = re.findall(r"^    \(([a-z])\) THE (NAVIGATOR|SEAT)'S", S['defects'], re.M)
    want = [list(x) for x in FLOORS['defects']]
    return len(rows) >= len(want) and [list(r) for r in rows[:len(want)]] == want and all(o in ('NAVIGATOR', 'SEAT') for _l, o in rows) \
        and [l for l, o in rows if o == 'NAVIGATOR'][:len(NAV_LETTERS)] == list(NAV_LETTERS)


def answers_before_ok(S):
    stamps = dict((n, iso_epoch(t)) for t, n in re.findall(
        r'### \(R278\)\(4\) THE MID-ACT CHECK \((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\): the (?:navigator`s )?answer carrying \'([^\']+)\'', S['citation']))
    return bool(ANSWER_NEEDLES) and all(any(k.startswith(n) for k in stamps) for n, _c in ANSWER_NEEDLES) and all(
        bool(S['t'].get(c)) and all(v is not None and v < S['t'][c] for k, v in stamps.items() if k.startswith(n)) for n, c in ANSWER_NEEDLES)


def repairs_ok(S):
    """the six repairs banked with their diffs (the three readers of (R317)(2) as shared-file diffs, the carry's three as function diffs), every
    control case as wanted and each repaired reading distinguished from the old on a row; in Component 1's commit."""
    z = unwrap(S['repair_ctl'])
    m = re.search(r'EACH REPAIRED READING DISTINGUISHED FROM THE OLD ON A ROW: \[([^\]]*)\]', z)
    dist = set(re.findall(r"'([^']+)'", m.group(1))) if m else set()
    return 'REPAIRS 6 ; SHARED FILES EDITED 3 UNDER (R317)(2)' in unwrap(S['repairs']) and 'AS WANTED True' in z \
        and dist >= {'G-RULE-SUITE-PARTS', 'ROOT_EXCLUDE', 'mirror_roster', 'prev_capture', 'rowgen roster', 'terminal_table'} \
        and all(('(%d) tools/' % i) in S['repairs'] for i in range(1, 7)) and 'data/b707_tool_repairs.txt' in S['files']['c1'] \
        and 'data/b707_repair_controls.txt' in S['files']['c1']


def rootdry_ok(S):
    j = S['rootdryj']
    at = iso_epoch(j.get('at') or '')
    return bool(j) and j.get('ready') is True and at is not None and S['lock_epoch'] is not None and at <= S['lock_epoch'] \
        and 'READY True' in unwrap(S['rootdry']) and ('the root route`s dry run READY %s' % j.get('ready')) in unwrap(S['face'])


def readfirst_diff_ok(S):
    return 'THE HAND LIST' in unwrap(S['rf_diff']) and S['rf_hand_now'] is not None and S['rf_hand_z'] is not None and S['rf_hand_now'] == S['rf_hand_z']


def parts_prerun_ok(S):
    t = S['prerun']
    return all(('### PART %s : ARMS' % p) in t for p in K.PARTS) and 'under the 590 s guard True' in t and 'PRE-SEAL (R202)(3)' in t


def arm_seconds_ok(S):
    j = S['asec']
    return sorted(j.get('parts') or []) == sorted(K.PARTS) if isinstance(j.get('parts'), (list, dict)) else (
        sorted(j) >= [] and all(p in json.dumps(j) for p in K.PARTS) and 'THE PER-PART SECONDS' in S['asect'].upper())


def figures_banked_ok(S):
    """the four figures banked by b706's tool over b706's roster, each at or below b706's; the partners rows one copy per table, the figure 0."""
    j, f6 = S['figj'], jl('b706_standing_figures.json')
    figs = dict((k, (j.get(k) or {}).get('figure')) for k in ('correspondence', 'readme', 'partners', 'pins'))
    prev = dict((k, (f6.get(k) or {}).get('figure')) for k in figs)
    pr = (j.get('partners') or {}).get('rows') or []
    return all(isinstance(figs[k], int) and isinstance(prev[k], int) and figs[k] <= prev[k] for k in figs) and figs['partners'] == 0 \
        and len(pr) == 20 and all((r.get('reason') or '').startswith('ONE COPY') for r in pr) and j.get('roster') == 'b706_roster_read.json' \
        and 'FIGURES AT b707' in S['figt']


def orders_ok(S):
    ls = (S['orders_line'].get('lines') or []) + (S['orders_line1'].get('lines') or [])
    heads = [h for _ln, _nm, h, _b in S['REC'].ORDERS]
    return len(ls) == len(heads) == 2 and all(x.get('file') == 'OPEN_TRAILS.md' and bool(x.get('line')) for x in ls) \
        and all(oline(S, x['line']).startswith(conv(h)) for x, h in zip(ls, heads)) and any('W-ORD-LV-FORWARD-PORT' in oline(S, x['line']) for x in ls)


# ================================================================== (R317)(2): THE THREE READERS` REPAIRS, READ AT HEAD
RETIRED_FOUR = ('EXHAUSTIVENESS_LICENSE.md', 'TECHNE_TOOLKIT.md', 'R_CURVE_CRITERION.md', 'E_DIFFICULTY_THEOREM.md')


def roster_ok(S):
    """tools/mirror_roster.json at HEAD: 70 entries, none listed twice, no retired versioned path, the four re-pointed names present; b706's
    roster (at the act's base) 83 with the 17 retired paths; the control bank: b706's export verified clauses 1 and 2 CLEAN and clause 3 NOT
    CLEAN by exactly the four names MISSING, none EXTRA."""
    files = S['roster'].get('files') or []
    pre = S['roster_pre'].get('files') or []
    ren = _renamed()
    z = S['roster_ctl']
    miss = re.findall(r'MISSING : (\S+)', z)
    m3 = re.search(r'in roster, MISSING from archive : (\d+)', z)
    x3 = re.search(r'in archive, NOT in roster\s+: (\d+)', z)
    return len(files) == 70 and len(set(files)) == 70 and not [p for p in files if p.replace('\\', '/') in ren] \
        and all(any(p.replace('\\', '/').endswith('/' + n) for p in files) for n in RETIRED_FOUR) \
        and len(pre) == 83 and sum(1 for p in pre if p.replace('\\', '/') in ren) == 17 \
        and 'CLAUSE 1 : CLEAN' in z and 'CLAUSE 2 : CLEAN' in z and bool(m3) and m3.group(1) == '4' and bool(x3) and x3.group(1) == '0' \
        and sorted(miss) == sorted(RETIRED_FOUR) and 'tools/mirror_roster.json' in S['files']['c1']


def table_scope_ok(S):
    """tools/terminal_table.py's ledger walk bounded by path (RETIRED_DIRS naming the retired copies' directory); the regeneration against b706's
    final table: the 12 added rows gone, the 18 moved restored (15 grades), nothing added, no other row changed; the walk dropping 17 files, every
    one a retired copy; in Component 1's commit."""
    j, b6 = S['tscopej'], S['b706_tfj']
    src = S['tt_src']
    return j.get('ok') is True and j.get('rc') == 0 and len(j.get('dropped') or []) == 17 and all(d.startswith('PLACE-papers/' + K.ARCHIVE_DIR + '/') for d in j.get('dropped') or []) \
        and sorted(tuple(x) for x in j.get('gone') or []) == sorted(tuple(x) for x in b6.get('added') or []) and len(j.get('gone') or []) == 12 \
        and not j.get('added') and len(j.get('moved') or []) == 18 and len(j.get('restored') or []) == 18 and len(j.get('grade_moved') or []) == 15 and not j.get('other') \
        and "RETIRED_DIRS = ('%s',)" % K.ARCHIVE_DIR in src and 'for d in RETIRED_DIRS' in _fn_src(src, 'ledger_files') \
        and 'AS WANTED True' in unwrap(S['tscope']) and 'data/b707_table_scope.txt' in S['files']['c1'] and 'tools/terminal_table.py' in S['files']['c1']


def split_arm_ok(S):
    """tools/rule_arms.py's G-RULE-SUITE-PARTS at HEAD: the family regex strips a digit and a letter, the `whole` clause present; the repair's
    controls: b706's run banks pass, b705's pass, every mutated copy fails, the lettered half alone fails; the live arm (standing-a's reading)
    over every run bank; in Component 1's commit."""
    src = S['ra_src']
    z = S['repair_ctl']
    rows = [l for l in z.split(NL) if l.startswith('  G-RULE-SUITE-PARTS ')]
    want = ['old False | repaired True', 'old True  | repaired True', 'old False | repaired True', 'old False | repaired False', 'old False | repaired False',
            'old False | repaired False', 'old False | repaired False', 'old True  | repaired False']
    return "re.sub(r'(?<=^standing-[a-z])[0-9][a-z]?$', '', p)" in src and 'def whole(k, v):' in src and len(rows) == 8 \
        and all(w in r and 'AS WANTED' in r for r, w in zip(rows, want)) and 'tools/rule_arms.py' in S['files']['c1']


# ================================================================== (R317)(3): THE ONSET
def _onset_units(S):
    return S['onsetj'].get('units') or []


def onset_controls_first_ok(S):
    """the controls before the figures: every zeta unit and the C2 units stamped before the first Q0 unit of the ladder; C1 read POSITIVE
    DEFINITE at every rung of both frequencies; C2 as wanted (5 cases); the rung structure printed (Lambda_Q(2) = Lambda_Q(3) = 0 as computed)."""
    U = _onset_units(S)
    z = [iso_epoch(u.get('at') or '') for u in U if u.get('route') == 'terms' and u.get('obj') == 'zeta']
    q = [iso_epoch(u.get('at') or '') for u in U if u.get('route') == 'terms' and u.get('obj') == 'q0']
    c2 = [iso_epoch(u.get('at') or '') for u in U if u.get('route') == 'c2']
    j = S['onsetj']
    rg = j.get('rung_structure') or {}
    small = rg.get('small') or []
    return bool(z) and bool(q) and bool(c2) and all(z) and all(q) and all(c2) and max(z) < min(q) and max(c2) < min(q) \
        and len(z) == 42 and len(q) == 42 and j.get('c1_zeta_ok') is True and (j.get('c2') or {}).get('ok') is True and len((j.get('c2') or {}).get('rows') or []) == 5 \
        and len(small) >= 2 and small[0].get('n') == 2 and small[1].get('n') == 3 and small[0].get('lambda_q', '').startswith('0 ') and small[1].get('lambda_q', '').startswith('0 ') \
        and 'C1 ZETA POSITIVE DEFINITE AT EVERY RUNG OF BOTH FREQUENCIES True ; C2 AS WANTED True (5 cases)' in unwrap(S['onset_ctl'])


def onset_banked_ok(S):
    """the onset bank: seven rungs from log 2, two frequencies, every Q0 rung read in balls; a* = 192 at the band zero's family and 32 at rho_0's,
    the falsifier not fired, the hypothesis HELD; the entry's figures those of the bank; in Component 2's commit."""
    j = S['onsetj']
    on = j.get('onset') or {}
    rungs = [r.get('rung') for r in j.get('rungs') or []]
    rows = [r for r in j.get('rows') or [] if r.get('obj') == 'q0']
    return rungs == ['log2', '32', '48', '64', '96', '128', '192'] and len(rows) == 14 \
        and all(r.get('reading') in ('NEGATIVE DIRECTION BEYOND ITS BOUND', 'POSITIVE DEFINITE BEYOND ITS BOUND') for r in rows) \
        and (on.get('band') or {}).get('a_star') == '192' and (on.get('rho0') or {}).get('a_star') == '32' and j.get('falsifier_fired') is False \
        and j.get('hypothesis') == 'HELD' and j.get('prec') == 128 \
        and 'THE ONSET AT THE BAND ZERO`S FAMILY: a* = 192 ; AT rho_0`S FAMILY: a* = 32 ; THE FALSIFIER NOT FIRED ; THE HYPOTHESIS HELD' in unwrap(S['onset']) \
        and 'data/b707_onset.txt' in S['files']['c2'] and 'data/b707_onset.json.gz' in S['files']['c2']


def onset_hashes_ok(S):
    """data/b680_rules.txt row (1): the gz's sha256 and its JSON's equal the hashes bank's rows; the root names the text bank, not the gz."""
    h = S['onset_hashes']
    gzb = S['onset_gz']
    if not gzb or not h:
        return False
    m_gz = re.search(r'^data/b707_onset\.json\.gz ; ([0-9a-f]{64}) ; (\d+)$', h, re.M)
    m_js = re.search(r'^data/b707_onset\.json \(inside the gz\) ; ([0-9a-f]{64}) ; (\d+)$', h, re.M)
    raw_ = gzip.decompress(gzb)
    return bool(m_gz) and bool(m_js) and hashlib.sha256(gzb).hexdigest() == m_gz.group(1) and int(m_gz.group(2)) == len(gzb) \
        and hashlib.sha256(raw_).hexdigest() == m_js.group(1) and int(m_js.group(2)) == len(raw_) and 'data/b707_onset_hashes.txt' in S['files']['c2']


# ================================================================== (R317)(4): THE REGISTRATIONS
def registrations_alone_ok(S):
    """data/b707_registrations.txt committed alone at step zero (one file in its commit), before the onset's first unit and before Component 2's
    commit; its blob unchanged at HEAD and in the working tree; the one commit touching it."""
    U = _onset_units(S)
    first_unit = min([iso_epoch(u.get('at') or '') or 10 ** 12 for u in U] or [10 ** 12])
    return S['files']['reg'] == ['data/b707_registrations.txt'] and bool(S['t'].get('reg')) and S['t']['reg'] < first_unit and S['t']['reg'] < S['t']['c2'] \
        and S['regs_blob_reg'] and S['regs_blob_reg'] == S['regs_blob_head'] == S['regs_blob_now'] and len(S['regs_log']) == 1 \
        and 'REGISTRATIONS 1' in unwrap(S['regs']) and 'COMPUTED AT b709' in unwrap(S['regs'])


def registrations_reread_ok(S):
    j = S['regs_rereadj']
    return j.get('unchanged') is True and j.get('commit') == K.REG_COMMIT and j.get('work_blob') == S['regs_blob_now'] and j.get('then_blob') == S['regs_blob_reg'] \
        and 'UNCHANGED SINCE %s True' % K.REG_COMMIT in unwrap(S['regs_reread']) and 'data/b707_registrations_reread.txt' in S['files']['c4']


def next_axis_ok(S):
    j = S['regs_rereadj']
    return j.get('axis_ok') is True and j.get('next_axis') == '(e) representation coordinates' and j.get('ranking_line') == 58 \
        and (j.get('ranking_text') or '').startswith('2. (e) representation coordinates') \
        and '(e) representation coordinates' in rd('b705_i6_ranking.txt').split(NL)[57]


# ================================================================== (R317)(5): THE PORT
def port_files_ok(S):
    """the five files printed before the one commit: the toolchain, lakefile :12 and the manifest at the shared pin with lv's own name kept, the
    one line repaired, the workflow carried verbatim (its blob SIDE-explicit-formula's at main, no identifier); the commit's files those five
    on 93c27ec; the bank before the commit; the push in branch mode read back at the tip."""
    j = S['port_filesj']
    at = iso_epoch(j.get('at') or '')
    wf_blob = gs(LV, 'rev-parse', '%s:%s' % (K.PORT_COMMIT, WF))
    ef_blob = gs(EF, 'rev-parse', '%s:%s' % (K.EF_MAIN, WF))
    return j.get('ok') is True and j.get('workflow_equal') is True and j.get('ident') == [] and j.get('base') == K.LV_V0100 and j.get('branch') == K.PORT_BRANCH \
        and sorted(j.get('files') or []) == sorted(K.PORT_FILES) and sorted(S['lv_port_files']) == sorted(K.PORT_FILES) and wf_blob == ef_blob \
        and at is not None and bool(S['t'].get('port')) and at < S['t']['port'] \
        and ('branch %s read back at the remote: %s' % (K.PORT_BRANCH, K.PORT_COMMIT)) in S['port_push'] and 'branch mode' in S['port_push'] \
        and 'AS THE WORD ORDERS True' in unwrap(S['port_files']) and 'data/b707_port_files.txt' in S['files']['c3']


def port_dispatch_ok(S):
    rows = S['dispj'].get('rows') or []
    by_n = dict((str(r.get('n')), r.get('cmd') or '') for r in S['cmds'])
    disp = [str(n) for n in (S['cmdj'].get('dispatches') or [])]
    cap = [n for n in disp if K.KERNEL in by_n.get(n, '') or 'portdispatch' in by_n.get(n, '')]
    pt = iso_epoch((rows[0].get('dispatched') or '')[:19] + 'Z') if rows else None
    pushed_at = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', S['port_push'])
    return len(rows) == 1 and rows[0].get('kernel') == K.KERNEL and rows[0].get('ref') == K.PORT_COMMIT and rows[0].get('run_id') == K.PORT_RUN \
        and rows[0].get('branch') == K.PORT_BRANCH and rows[0].get('whole') is False and rows[0].get('target') == 'SIDELvConservation' \
        and len(disp) == 1 and len(cap) == 1 and pt is not None and bool(pushed_at) and iso_epoch(pushed_at.group(1)) < pt


def port_run_ok(S):
    """the run read by its id, its artifact chosen by name with the sha256 agreeing; the cache served; 6 of 12 modules built, GammaBounds among
    them; held at C7OrderBounds.lean :277:55 with the first error line banked; 6 remaining; the print step NOT RUN; no grade claimed (the gate
    NOT DERIVES, the row's note); the build log banked whole; in Component 3's commit."""
    j, r = S['portj'], ([x for x in (S['runner_rows'].get('rows') or []) if x.get('label') == PORT_LABEL] or [{}])[0]
    art = j.get('artifact') or {}
    return j.get('run_id') == K.PORT_RUN and (j.get('run') or {}).get('headSha') == K.PORT_COMMIT and art.get('agree') is True \
        and re.match(r'^[0-9a-f]{64}$', art.get('sha256') or '') is not None and (art.get('name') or '') == 'build-module-%d' % K.PORT_RUN \
        and j.get('build_exit') == '1' and len(j.get('built') or []) == 6 and 'GammaBounds' in (j.get('built') or []) and j.get('held') == ['C7OrderBounds'] \
        and (j.get('first_error') or '').startswith('error: SIDELvConservation/C7OrderBounds.lean:277:55:') and len(j.get('remaining') or []) == 6 \
        and j.get('print_step') == 'NOT RUN' and j.get('grade_claimed') is False and r.get('gate') == 'NOT DERIVES' and r.get('run_id') == K.PORT_RUN \
        and 'no grade claimed' in (r.get('note') or '') and j.get('stopped') is False and isinstance(j.get('mem_low'), int) and j['mem_low'] >= K.HOLD \
        and 'Decompressed 8691 file(s)' in S['port'] and any('C7OrderBounds.lean:277:55' in l for l in S['buildlog'].split(NL)) \
        and 'MODULES BUILT 6 OF 12 (FILES 6 OF 15)' in unwrap(S['port']) and 'THE PRINT STEP NOT RUN ; NO GRADE CLAIMED' in unwrap(S['port']) \
        and 'data/b707_port.txt' in S['files']['c3'] and 'data/b707_buildlog_%s_%s.txt' % (K.KERNEL, PORT_LABEL) in S['files']['c3']


def port_branch_kept_ok(S):
    """port-b707 at the one commit on 93c27ec, locally and at the remote; no merge, no tag; main and the deposit unmoved; the forward-port order
    entered at OPEN_TRAILS beneath the join's hold."""
    ls = S['orders_line1'].get('lines') or []
    return S['lv_port'] == K.PORT_COMMIT and S['lv_port_parent'] == K.LV_V0100 and S['lv_main'] == K.LV_MAIN and S['lv_v0100'] == K.LV_V0100 \
        and (not S['lv_remote'] or S['lv_remote'].get('refs/heads/' + K.PORT_BRANCH) == K.PORT_COMMIT) \
        and 'v0.10.0' in S['lv_tags'] and not any(t.startswith('v0.10.') and t != 'v0.10.0' for t in S['lv_tags']) \
        and len(ls) == 1 and 'W-ORD-LV-FORWARD-PORT' in oline(S, ls[0]['line']) and 'C7OrderBounds.lean :277' in oline(S, ls[0]['line'])


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R317) END' in S['ferry'] and S['ferry'].rstrip().endswith(K.TAIL),
     lambda S: put(S, 'ferry', S['ferry'].replace(K.TAIL, ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the step-zero bank: tail, lean, lake, python and claude named, the seat`s claude alone, none of the others; no task stopped, no orphan, nothing stopped by PID',
     lambda S: procs_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('python 0', 'python 1'))),
    ('G-STEPZERO-TESTS', 'the tests bank against the test files tracked before the act, test_elab_reader_b634.py withheld (no lean on this host), run against the list the page names, the eight not clean named (three carried, five the renames` readers)',
     lambda S: tests_ok(S), lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: S['pushout'][0] == ['data/b706_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'relay`s, PLACE-papers`, SIDE-faces-join`s and SIDE-explicit-formula`s branch lists by the ruling`s eight names, and the branches bank',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{'D:/relay': 'push-b706'}))),
    ('G-READFIRST-CITED', 'the read-first bank: every item of the ferry`s list cited by path and line', lambda S: readfirst_ok(S),
     lambda S: put(S, 'readfirst', '')),
    ('G-ANSWERS-BANKED', 'the answers bank read at HEAD: its prompts and calls at or above the sealed floors, each with its options and result, any call after the lock named on the face',
     lambda S: answers_ok(S), lambda S: put(S, 'answers', re.sub(r'(?m)^(### b707 -- THE AUTHOR`S ANSWERS, )(\d+)', lambda m: m.group(1) + str(int(m.group(2)) + 1),
                                                                 S['answers']))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-EXPORT-UNTRACKED', 'the navigator`s export: present, untracked, in no commit', lambda S: S['export_present'] and S['export_log'] == ''
     and S['export_index'] == '' and S['export_status'].startswith('??'), lambda S: put(S, 'export_index', EXPORT)),
    ('G-EDIT-ROUTE', 'the record tool`s one reading (tools/edit_route.py`s arms and sed in any form) over this act`s whole capture and the previous act`s after its post-push suite (b706`s own session, b701`s form), read live',
     lambda S: edit_route_ok(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -n 1p tools/b707_record.py")])),
    ('G-NO-LOCAL-LEAN', 'the act`s command capture, read live: no command runs lean or lake on this host (N1)', lambda S: no_local_lean(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd='lake env lean GammaBounds.lean')])),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line, found by conv', lambda S: weight_ok(S), lambda S: _rl(S, 0, 1)),
    # ### ACT ARMS (Component 5)
    ('G-DRY-STEP-CLEAN', 'the gate`s record: the dry-run step CLEAN, the trail`s Defects and Resolved lines equal to the bank, the gate CLEAR',
     lambda S: dry_step_ok(S), lambda S: put(S, 'gate', '')),
    ('G-CLOSING-DRY-STEP', 'the gate`s record: the closing tool run dry before the lock, its sections read (the repairs, the onset, the port, the registrations, the standing arms, the orders, the kernels)',
     lambda S: closing_dry_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE CLOSING DRY-RUN STEP : CLEAN', 'THE CLOSING DRY-RUN STEP : NOT CLEAN'))),
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, the five misses the navigator`s (three by the fact clause, two raised and answered), the bank before the step-zero commit and that before Component 1`s',
     lambda S: citation_ok(S), lambda S: put(S, 'citation', '')),
    ('G-R317-ENTERED', 'the trail record`s ratification line', lambda S: '**(R317) ratified.**' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**(R317) ratified.**', '**(R317) read.**'))),
    ('G-ROWGEN-STEPZERO', 'the rowgen bank`s verdict line (the roster re-pointed, 8)', lambda S: rowgen_ok(S), lambda S: put(S, 'rowgen', '')),
    ('G-BRANCHES-BANKED', 'the branches bank through the record tool`s reader: eight named, deleted, merged, banked before the first delete and after the citation check',
     lambda S: branches_banked_ok(S), lambda S: _mut(S, 'branchj', lambda d: d['rows'].pop())),
    ('G-DELETES-ONE-BRANCH', 'the command bank: every branch delete one branch (the eight of (R317)(7) alone, port-b707 never), no glob, no variable, nothing chained after',
     lambda S: deletes_one_ok(S), lambda S: put(S, 'cmdt', '')),
    ('G-ANSWERS-CHECKED', 'the citation bank`s mid-act prints: every answer checked before it was acted on (the roster and the port in one call), the root prompt`s checks after the lock each with its time',
     lambda S: answers_checked_ok(S), lambda S: put(S, 'citation', '')),
    ('G-ANSWERS-BEFORE-WRITES', 'the citation bank`s check stamps against the commits that acted on each answer: the roster answer`s before Component 1`s, the port answer`s before the port branch`s commit',
     lambda S: answers_before_ok(S), lambda S: put(S, 'citation', '')),
    ('G-SCORER-READS-BANKS', 'the record tool`s scorers: banks alone, no ledger line (data/b686_rules.txt row (1))', lambda S: scorer_banks_ok(S),
     lambda S: put(S, 'rec_src', '')),
    ('G-ENTRY-SCORES-EQUAL', 'the landed entry`s scores line against the scores bank', lambda S: entry_scores_ok(S), lambda S: put(S, 'sc', {})),
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title: by its objects (the sign-onset radius at the Epstein zeta, the ζ form, the forward-port with its modules of 15, the higher pairs` route), compared after case-folding the article alone',
     lambda S: entry_title_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-CORRIGENDUM-ENTERED', 'the generated corrigendum for b706`s seven post-seal items ((i)-(m) and the three trail arms), landed; the corrigenda bank appended at row (27)',
     lambda S: corrigendum_ok(S), lambda S: put(S, 'corrj', {})),
    ('G-GUARD-HELD', 'the suite`s writer block guarded by `if PRERUN:` and its dry run banked', lambda S: guard_ok(S), lambda S: put(S, 'guard', '')),
    ('G-POSTROOT-WRITES-NONE', 'the per-part seconds banks` commit times against the root`s', lambda S: postroot_writes_none(S), lambda S: put(S, 'guard', '')),
    ('G-TRAIL-LINES-EQUAL-DEFECTS', 'the landed trail`s Defects and Resolved lines against the defects bank`s owners', lambda S: trail_lines_equal_defects(S),
     lambda S: put(S, 'defects', '')),
    ('G-TRAIL-DEFECTS-EQUAL', 'the gate`s record and the landed trail`s Defects line against the repaired reader`s rows', lambda S: trail_defects_ok(S),
     lambda S: put(S, 'gate', '')),
    ('G-TRAIL-RESOLVED-EQUAL', 'the gate`s record and the landed trail`s Resolved line against the bank`s owners', lambda S: trail_resolved_ok(S),
     lambda S: put(S, 'gate', '')),
    ('G-DEFECTS-LETTERED', 'the defects bank: the sealed floors` rows (a)-(h) with their owners in order, (c) to (g) the navigator`s',
     lambda S: defects_ok(S), lambda S: put(S, 'defects', '')),
    ('G-TOOL-REPAIRS', 'the repairs bank (6: the three readers of (R317)(2) as shared-file diffs, the carry`s three) and their controls (22 cases as wanted, each repaired reading distinguished)',
     lambda S: repairs_ok(S), lambda S: put(S, 'repairs', '')),
    ('G-ROOTDRY-READY', 'data/b706_rules.txt row (1): the root route run dry on the pre-root tree before the lock, READY True, printed in the face`s (0)',
     lambda S: rootdry_ok(S), lambda S: _mut(S, 'rootdryj', lambda d: d.update(ready=False))),
    ('G-FIGURES-BANKED', 'the four standing figures banked by b706`s tool over b706`s roster, each at or below b706`s, the partners figure 0 with one copy per table', lambda S: figures_banked_ok(S),
     lambda S: put(S, 'figj', {})),
    ('G-READFIRST-DIFF-BANKED', 'the closure reader`s diff banked; the readfirst bank unchanged since the step-zero commit', lambda S: readfirst_diff_ok(S),
     lambda S: put(S, 'rf_diff', '')),
    ('G-ORDERS-ENTERED', 'the two order lines at OPEN_TRAILS at the landing banks` lines, each found by conv (the tag-prints remainder, W-ORD-LV-FORWARD-PORT entered)',
     lambda S: orders_ok(S), lambda S: put(S, 'orders_line', {})),
    ('G-REGISTRATIONS-ALONE', '(R317)(4), N2: data/b707_registrations.txt committed alone before any computation (before the onset`s first unit and Component 2`s commit), the one commit touching it, its blob unchanged at HEAD and in the working tree',
     lambda S: registrations_alone_ok(S), lambda S: put(S, 'regs_blob_now', '0' * 40)),
    ('G-ROSTER-REPAIRED', '(R317)(2), b706`s (m): tools/mirror_roster.json at HEAD 70 entries, none twice, no retired path, the four re-pointed; the control the dry run of b706`s export: clauses 1 and 2 CLEAN, clause 3 NOT CLEAN by exactly the four names',
     lambda S: roster_ok(S), lambda S: _mut(S, 'roster', lambda d: d['files'].append('FINDINGS.md'))),
    ('G-TABLE-SCOPE-RESTORED', '(R317)(2), b706`s (i): the ledger walk bounded by path, the regeneration against b706`s final table -- 12 added rows gone, 18 restored (15 grades), no other row changed, 17 retired copies dropped',
     lambda S: table_scope_ok(S), lambda S: _mut(S, 'tscopej', lambda d: d.update(other=[['x', 'y']]))),
    ('G-SPLIT-ARM-REPAIRED', '(R317)(2), b706`s (l): tools/rule_arms.py`s family reading at HEAD (`[0-9][a-z]?$`, `whole`) and its eight control rows as wanted',
     lambda S: split_arm_ok(S), lambda S: put(S, 'ra_src', S['ra_src'].replace('def whole(k, v):', 'def whole_(k, v):'))),
    ('G-ONSET-CONTROLS-FIRST', '(R317)(3): the ζ form and C2 banked before any Q0 unit of the ladder (the units` stamps), C1 positive definite at every rung of both frequencies, C2 as wanted, the rung structure with Λ_Q(2) = Λ_Q(3) = 0 computed',
     lambda S: onset_controls_first_ok(S), lambda S: _mut(S, 'onsetj', lambda d: d.update(c1_zeta_ok=False))),
    ('G-ONSET-BANKED', '(R317)(3): the ladder of seven rungs from log 2, two frequencies, every Q0 rung read in balls; a* = 192 at the band zero`s family and 32 at rho_0`s, the falsifier not fired, the hypothesis HELD; in Component 2`s commit',
     lambda S: onset_banked_ok(S), lambda S: _mut(S, 'onsetj', lambda d: d.update(hypothesis='REFUTED'))),
    ('G-ONSET-HASHES', 'data/b680_rules.txt row (1): the onset`s gz and its JSON against the hashes bank`s sha256 and byte counts', lambda S: onset_hashes_ok(S),
     lambda S: put(S, 'onset_hashes', '')),
    ('G-REGISTRATIONS-REREAD', '(R317)(4): the registrations re-read after the computations, unchanged since their commit, banked; in Components 3-4`s commit',
     lambda S: registrations_reread_ok(S), lambda S: _mut(S, 'regs_rereadj', lambda d: d.update(unchanged=False))),
    ('G-PORT-FILES', '(R317)(5) and the author`s word: the five files of port-b707 printed before the one commit, the workflow`s blob SIDE-explicit-formula`s at main, no identifier, the commit those five on 93c27ec, pushed in branch mode and read back',
     lambda S: port_files_ok(S), lambda S: _mut(S, 'port_filesj', lambda d: d.update(workflow_equal=False))),
    ('G-PORT-ONE-DISPATCH', 'N1: one dispatch at the branch with its tip as the ref, after the push, whole False by the print list`s absence, one in the capture',
     lambda S: port_dispatch_ok(S), lambda S: _mut(S, 'dispj', lambda d: d['rows'].append(dict(d['rows'][0])))),
    ('G-PORT-RUN-READ', 'N1, (R317)(5): the run read by its id with the artifact`s sha256 verified, the cache served, 6 of 12 modules built (GammaBounds among them), held at C7OrderBounds.lean :277:55 with the first error banked, the print step not run, no grade claimed',
     lambda S: port_run_ok(S), lambda S: _mut(S, 'portj', lambda d: d.update(grade_claimed=True))),
    ('G-PORT-BRANCH-KEPT', '(R317)(5): port-b707 at its one commit on 93c27ec locally and at the remote, no merge, no tag, main and the deposit unmoved; W-ORD-LV-FORWARD-PORT entered beneath the join`s hold',
     lambda S: port_branch_kept_ok(S), lambda S: put(S, 'lv_port', '0' * 40)),
    ('G-NEXT-AXIS-NAMED', '(R317)(6): the next axis named from data/b705_i6_ranking.txt :58, (e) representation coordinates, in the re-read bank',
     lambda S: next_axis_ok(S), lambda S: _mut(S, 'regs_rereadj', lambda d: d.update(axis_ok=False))),
    ('G-PARTS-PRERUN', 'the pre-run bank: seven parts, each named with its arms and seconds, the longest under the 590 s guard', lambda S: parts_prerun_ok(S),
     lambda S: put(S, 'prerun', '')),
    ('G-ARM-SECONDS-BANKED', 'the per-part seconds bank gathered before the seal', lambda S: arm_seconds_ok(S), lambda S: put(S, 'asec', {})),
    ('G-SPEC-PLANTED', 'tools/b707_regspec.py`s planted rows run live through the record tool`s readers, and rows of another shape refused',
     lambda S: bool(S['spec']['read']) and all(S['spec']['read']) and all(S['spec']['controls']) and any('runner' in x for x in S['spec']['shapes']),
     lambda S: _mut(S, 'spec', lambda d: d['controls'].append(False))),
    ('G-CONVERSION-ONE', 'every b707 tool`s code: no conversion defined (conv imported from b652_record); the suite importing it',
     lambda S: S['conv_bad'] == [] and 'from b707_record import conv' in S['suite'], lambda S: put(S, 'conv_bad', ['b707_checks.py'])),
    ('G-WORKFLOW-FILES', 'this act`s one run`s workflow: the port branch`s carried verbatim from SIDE-explicit-formula`s build-module.yml at main (written onto the branch this act), no author identifier, no secret, the hold, the cache step, the print step over its list (absent at 93c27ec), each dispatch`s target whole by data/b705_rules.txt row (1)',
     lambda S: wf_ok(S), lambda S: _mut(S, 'wf', lambda d: d[K.KERNEL].update(text=d[K.KERNEL]['text'] + ' secrets.X'))),
    ('G-RUNNER-READ', 'this act`s one run (the port branch at its tip) read by its id through the record tool`s reader: at its ref, success, the artifact`s sha256, the memory low above the hold, no STOP line, the gate DERIVES',
     lambda S: runner_ok(S), lambda S: _mut(S, 'runner_rows', lambda d: d.update(rows=[dict(r, gate='NOT DERIVES') for r in (d.get('rows') or [])]))),
    ('G-RUNNER-GATE', 'the run`s reading: GATE DERIVES, build exit 0, no error line, the artifact`s digest agreeing',
     lambda S: gate_ok(S), lambda S: put(S, 'portrun', '')),
    ('G-MERGES-ON-GATE', 'no merge this act: SIDE-lv-conservation`s main and deposit unmoved, port-b707 at its one commit locally and at the remote, no tag made; SIDE-explicit-formula`s main at badaccc with its tags unmoved; the join kernel`s main at its manifest commit, no tag; no sorry in code on the port branch beyond v0.10.0`s pinned one',
     lambda S: merges_ok(S), lambda S: put(S, 'ef_log', S['ef_log'] + [('deadbeef', 'x', 1)])),
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
    ('G-PP-SCOPE', 'PLACE-papers` changed files against the two ledgers alone; no rename (N5)',
     lambda S: corpus_scope_ok(S), lambda S: put(S, 'pp_changed', S['pp_changed'] + ['day1/Spectral_Inertness.md'])),
    ('G-CURRENTS-UNEDITED', 'the map, the census, the monograph, the Dirichlet page, the surround, SIMPLICITY, FOUNDATIONS, INSTRUMENTS, PATHS, the substrate pages, the companions, the README, the faces page, REGISTRY and the archives, each at its file of record after (R316)(3): working tree, before and HEAD',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'ERRATA.md': (b'x', b'y', b'y')}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read before the seal (SIDE-lv-conservation read after its port branch was pushed)',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b706`s to b695`s sealed tools and the earlier tools, the readers, the push tool, the act-root tool, the generators` tests, the corrigendum tools, edit_route.py, chain_page.py, b703`s, b705`s and b706`s figures tools, b704`s read arm, e0_rule.py and the shared tools -- less the two the ruling names (terminal_table.py, rule_arms.py): before, working tree and HEAD',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'additive_shared.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 37e4a12f but the shared additive files (act_roots.txt and the corrigenda bank among them) and the table`s files, by blob id',
     lambda S: S['prior_bad'] == [] and S['prior_n'] > 0, lambda S: put(S, 'prior_bad', ['data/b706_stepzero.txt'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS before and now', lambda S: S['fi_pre'] is not None and (S['fi_now'] or b'').startswith(S['fi_pre']),
     lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS before and now', lambda S: S['ot_pre'] is not None and (S['ot_now'] or b'').startswith(S['ot_pre']),
     lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-NODISCLOSURE-PUBLIC', 'TECHNE-Core`s needle sets over every public byte the act writes: the ledger lines, the banks, the tools, the roster and the workflow on the port branch',
     lambda S: bool(S['nd_pub']) and not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', {'method': 1})),
    ('G-OUTSIDE-NAMED-NOWHERE', 'the ledger lines appended', lambda S: S['outside'] == [], lambda S: put(S, 'outside', ['x'])),
    ('G-DELETE-FREE', 'the act`s tools` code, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='os' + '.remove(p)'))),
    ('G-PUBLISH-UNCALLED', 'the act`s tools` code: no publish call', lambda S: publish_uncalled(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='z_' + 'publish()'))),
    ('G-SEALED-AFTER-COMPONENTS', 'the lock time against every relay and PLACE-papers commit of the act by its subject', lambda S: sealed_after_ok(S),
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b707 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'b707_closing.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3), in seven parts summed',
     lambda S: S['lock_epoch'] is not None and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b706`s trail record on OPEN_TRAILS and its root in the chain', lambda S: K.B706_TRAIL_HEAD in S['ot']
     and S['rootsf'].count(NL + 'b706 ') == 1, lambda S: put(S, 'ot', S['ot'].replace('### b706 — lane two', '### b706 - lane two'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], grade_moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 84th chain row (the corrigendum row apart), the root bank and its items against the root route`s own item list (ROOT_EXCLUDE extended per data/b706_rules.txt row (1), the required list read against it at import), the onset, the port, the repairs, the registrations, the corrigendum and the report among them, no bank the route excludes',
     lambda S: root_banked_ok(S), lambda S: put(S, 'rootsf', S['rootsf'] + 'b708 x y' + NL)),
    ('G-ROOT-BANKS-COMMITTED', 'the root route`s banked reading and every named bank`s blob at the root`s recorded commit: clean and equal at HEAD, HEAD the remote main, the recorded hash carried by the recorded commit',
     lambda S: root_banks_committed_ok(S), lambda S: put(S, 'rootbanks', dict(S['rootbanks'], pushed=False))),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit in three parts by act with the suite`s own remote reads: standing-b2a`s banked b624-b641, standing-b2b`s b642-b658 and standing-b3`s b659-b707 all AGREE, the boundary link equal, b680 read through its corrigendum row (4 banks), b707 written LF',
     lambda S: verify_ok(S), lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s through conv, and its parts, the onset and the port among them', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line, the head through conv', lambda S: bool(S['tj'].get('line'))
     and oline(S, S['tj']['line']) == conv(S['REC'].TRAIL_HEAD()), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b707 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b707_record.py agree', 'b707_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line: b708', lambda S: '**Next:** b708' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** b708', '**Next:** b709'))),
] + [('G-N%d-SCORED' % i, 'the scores through the record tool`s reader, and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i),
      lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written since 37e4a12f and c9e0086 against the (W) globs, the list admitting the next act`s rules file by form',
     lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b707')" in S['suite'] and "'data/b707_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b707_closing.py: the closing sentence in the rule`s words with the plain reads named; the citation check, the record lines, the dry run, the repairs, the onset, the port, the registrations, the standing arms, the orders, the kernels, the mirror, the carry-time reading',
     lambda S: closing_sentence_ok(S), lambda S: put(S, 'closing_src', S['closing_src'].replace('no identifier of the author ' + 'in any outbound', 'x'))),
    ('G-LSREMOTE-ONE-PER-REPO', 'the part`s ls-remote calls per repository, read after every other arm of the part has run (OPEN_TRAILS :12703)',
     lambda S: lsr_ok(S), lambda S: put(S, 'lsr', {PP: 2})),
    ('G-CORRESPONDENCE-CURRENCY', 'every roster paper`s Correspondence rows by tools/b706_standing_figures.py (b703`s reading over b706`s roster at the unversioned names) against the kernel`s current tag and the statement at the cited tag: the changed-statement rows no more than b706`s figure',
     lambda S: fig_ok(S, 'correspondence'), lambda S: _raise_fig(S, 'correspondence')),
    ('G-README-CURRENCY', 'the PLACE-papers README`s currency rows against ls-remote by tools/b705_standing_figures.py through b706`s (the dated appends and the deposited versions excluded by their text): the stale lines no more than b706`s figure',
     lambda S: fig_ok(S, 'readme'), lambda S: _raise_fig(S, 'readme')),
    ('G-PARTNER-COPIES', 'the lines differing between the two copies of each roster paper`s Correspondence table by tools/b706_standing_figures.py: one copy per table from b706 on, the figure 0, no more than b706`s 0',
     lambda S: fig_ok(S, 'partners'), lambda S: _raise_fig(S, 'partners')),
    ('G-SISTER-PINS', 'each kernel`s lean-toolchain and Mathlib revision beside the federation`s by tools/b703_standing_figures.py through b706`s: no kernel the faces page names moved pin against the baseline (the port branch is no main)',
     lambda S: sister_pins_ok(S), lambda S: _raise_fig(S, 'pins')),
    ('G-READ-RULE-STANDING', 'tools/b704_read_arm.py over the read bank at HEAD (the author`s word at b704`s sort; from b705 every call counts): no Read call of a file of two hundred lines or more without an offset, without a limit or with a limit above two hundred',
     lambda S: read_rule_standing_ok(S), lambda S: _read_plant(S)),
] + [(nm, 'tools/rule_arms.py (the author`s word on (R293)(6); (R301)(6) for four; G-RULE-SUITE-PARTS as repaired under (R302)(2) and (R317)(2); G-RULE-BINARY-HASHES as repaired under (R306)(2); G-RULE-RECUT-QUOTE`s sources as repaired under (R313)(2)) -- ' + reads,
      (lambda p: lambda S: p(S['ra']))(pred), (lambda pl: lambda S: put(S, 'ra', pl(S['ra'])))(plant)) for nm, reads, pred, plant in RA.ARMS]


def _part_of(name):
    if name in K.ACT_ARMS:
        return 'act'
    if name in B1_ARMS:
        return 'standing-b1'
    if name in B2_ARMS:
        return 'standing-b2a'
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
    p = os.path.join(D, 'b707_seal_hashes.json')
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
    print('  written: b707_seal_hashes.json')
    return 0


def _base_name(pushed):
    if PRERUN:
        return 'b707_arms_prerun.txt'
    if MID and len(sys.argv) > sys.argv.index('--mid') + 1:
        return sys.argv[sys.argv.index('--mid') + 1]
    if RERUN and len(sys.argv) > sys.argv.index('--rerun-postpush') + 1:
        return sys.argv[sys.argv.index('--rerun-postpush') + 1]
    return 'b707_checks_postpush.txt' if pushed else 'b707_checks.txt'


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
    """the banks the writer block at the end of a part would write, by mode -- the part bank and the ls-remote bank in every mode, the exercise
    bank in every mode, the per-part seconds bank under `if PRERUN:` alone. Read by `--guard-dry`; the writer block beneath follows this plan
    exactly (the arm G-GUARD-HELD reads the block's own text)."""
    base = 'b707_arms_prerun.txt' if prerun else ('b707_checks_postpush.txt' if (rerun or pushed) else 'b707_checks.txt')
    out = [('data/' + _part_name(base, '<part>')), ('data/' + _part_name(base, '<part>').replace('b707_arms_prerun', 'b707_lsr_prerun').replace('b707_checks', 'b707_lsr').replace('.txt', '.json')),
           'data/b707_exercise_<part>.json']
    seconds = ['data/b707_arm_seconds_<part>.json'] if prerun else []
    return out, seconds


def guard_dry():
    for mode, args in (('prerun', (True, False, False, False)), ('pre-push', (False, False, False, False)), ('post-push', (False, True, False, True))):
        out, seconds = writer_plan(*args)
        print('  MODE %-9s | the part`s banks: %s | the per-part seconds bank: %s' % (mode, ', '.join(out), ', '.join(seconds) or 'NONE'))
    print('  ### POST-ROOT PATH WRITES NONE of the root-named per-part seconds banks: the pre-push and post-push modes write no data/b707_arm_seconds_<part>.json')
    return 0


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
    carried = [f for f in fails if f in CARRIED_FAILING]
    ok = lf == len(carried) and pc == 0 and ng == 0 and deq
    out = ['=' * 104, heads[0].replace('PART standing-a', 'SEVEN PARTS SUMMED'), '=' * 104] + [
        '  ### PART %s : ARMS %s ; %s s' % (p, m.group(2), m.group(10)) for p, m, _t in parts] + [
        '  ### the parts` seconds summed %d ; the longest part %s s, under the 590 s guard %s' % (
            sum(int(m.group(10)) for _p, m, _t in parts), max(int(m.group(10)) for _p, m, _t in parts),
            max(int(m.group(10)) for _p, m, _t in parts) < 590),
        '  ### the failures declared on the face as carried (section (G2)): %s ; failing among them %s ; failing beyond them %s' % (
            list(CARRIED_FAILING) or 'NONE', carried or 'NONE', [f for f in fails if f not in CARRIED_FAILING] or 'NONE'),
        '  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s.**' % (n, lp, lf, fails or ''),
        '  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (ng, pc, defs or ''),
        '  ### ### **VERDICT : %s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if (ok and not fails) else
                                       'EVERY ARM PASSES BUT THE CARRIED FAILURE DECLARED ON THE FACE, AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN'),
        '=' * 104, '']
    for p, _m, t in parts:
        out += ['### THE PART BANK %s, WHOLE:' % _part_name(base, p)] + t.rstrip(NL).split(NL) + ['']
    _write(base, out)
    ex = {}
    for part in K.PARTS:
        ex.update(jl('b707_exercise_%s.json' % part).get('exercise') or {})
    if ex and base in ('b707_checks.txt', 'b707_checks_postpush.txt'):
        e = (json.dumps(dict(exercise=ex, run=n, live_failing=fails, defective=defs, neg_failures=ng), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p_ = os.path.join(D, 'b707_exercise.json')
        with open(p_ + '.tmp', 'wb') as fh:
            fh.write(e)
        os.replace(p_ + '.tmp', p_)
    print(NL.join(out[3:16]))
    print('  written: %s' % base)
    return 0 if ok else 1


# ### the carried failures declared on the face by name (section (G2)): the three standing runner arms failing on the held port run by (R317)(5)'s
# ### own clause and the author's word (the print step not run, no grade claimed), and G-READ-RULE-STANDING failing on defect (a)'s one whole read
# ### of a memory file before the ferry was banked (relay data/b707_read_calls.txt, OFFENCES 1); the combine reads them by name, and no other
# ### failure is carried.
CARRIED_FAILING = ('G-WORKFLOW-FILES', 'G-RUNNER-READ', 'G-RUNNER-GATE', 'G-READ-RULE-STANDING')


def main():
    if SEAL:
        return seal()
    if COMBINE:
        return combine()
    if GUARD_DRY:
        return guard_dry()
    if PART not in K.PARTS:
        print('### every run in seven foreground parts -- give `--part %s`' % ' | '.join(K.PARTS))
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
    rec('b707 -- THE SUITE. ### **%s READING.** ### PART %s ### every arm exercised on both controls.' % (
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
        a1, a2 = jl(half_bank('a1', _run_key(base))), jl(half_bank('a2', _run_key(base)))
        S['half_a'] = dict(head=a1.get('head') if a1.get('head') == a2.get('head') else None, acts=(a1.get('acts') or []) + (a2.get('acts') or []),
                           reads=dict(a1.get('reads') or {}, **(a2.get('reads') or {})), boundary=a2.get('boundary') or a1.get('boundary') or {})
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
    rec('  ### (R264)(2) THE FREEZE: the standing arms (b706`s face less its own arms, the twenty-four rule arms and G-READ-RULE-STANDING among them; none added) %d ; '
        'carried here %d ; the act`s arms over its own banks %s ; arms beyond both %s' % (
            len(S['standing']), len(set(names) & set(S['standing'])), sorted(set(names) - set(S['standing'])),
            sorted(set(names) - set(S['standing']) - set(K.ACT_ARMS)) or 'NONE'))
    rec('  ### standing arms not carried here: %s' % (sorted(set(S['standing']) - set(names)) or 'NONE'))
    if 'figures' in NEED[PART]:
        rec('  ### THE FOUR STANDING FIGURES, each against the previous act`s (%s):' % S['fig_prev_name'])
        for k in ('correspondence', 'readme', 'partners', 'pins'):
            rec('  ###   %-15s live %s ; previous %s' % (k, (S['fig'].get(k) or {}).get('figure'), (S['fig_prev'].get(k) or {}).get('figure')))
        ok_, n_, off_, pre_, form_ = RDA.reading_text(S['reads_bank'])
        rec('  ### G-READ-RULE-STANDING`S READING (relay data/b707_read_calls.txt): %s ; rows %d ; offences %d %s ; the cap`s precursors %d' % (
            'PASS' if ok_ else 'FAIL', n_, len(off_), [RDA._show(r) for r in off_], len(pre_)))
    if 'rules' in NEED[PART]:
        rec('  ### THE RULE ARMS, EACH WITH ITS COUNT (tools/rule_arms.py; rows read, rows failing, the reading); the call trace %d calls:' % len(
            S['ra'].get('calls') or []))
        for nm in RA.NAMES:
            ok_, n_, b_, note = RA.reading(nm, S['ra'])
            rec('  ###   %-28s %-4s read %d ; failing %d ; %s' % (nm, 'PASS' if ok_ else 'FAIL', n_, b_, note[:260]))
    chain_part = next((x for x in ('chain_a1', 'chain_a2', 'chain_b') if x in NEED[PART]), None)
    if chain_part:
        key, span = {'chain_a1': ('a1', K.CHAIN_QUARTERS[0]), 'chain_a2': ('a2', K.CHAIN_QUARTERS[1]), 'chain_b': ('b', K.CHAIN_HALVES[1])}[chain_part]
        av = S['ar_verify']
        bd = S['boundary']
        rec('  ### THE ACT-ROOT CHAIN`S PART %s, %s-%s, recomputed at commit: %s' % (key.upper(), span[0], span[1],
                                                                                 '; '.join('%s %s%s' % (a, v, (' (' + '; '.join(w) + ')') if w else '') for a, v, w in av) or 'no act rooted'))
        rec('  ### THE BOUNDARY (relay data/act_roots.txt): %s root %s ; %s previous %s ; equal %s' % (bd['first'], bd['root'], bd['second'], bd['previous'], bd['equal']))
        if key != 'b':
            rec('  ### the reads at commit, %s: %s' % (span[1], S['ar_reads'].get(span[1])))
            rec('  ### PART %s CARRIES NO ARM: its verdicts banked for standing-b3 in relay data/%s' % (PART, half_bank(key, _run_key(base))))
        else:
            ha = S['half_a'] or {}
            rec('  ### the reads at commit, b680: %s ; b707: %s' % (S['ar_reads'].get('b680'), S['ar_reads'].get('b707')))
            rec('  ### THE FIRST HALF AS standing-b2a AND standing-b2b BANKED IT (relay data/%s, data/%s): %d acts, AGREE %d, at HEAD %s (now %s), its boundary equal %s' % (
                half_bank('a1', _run_key(base)), half_bank('a2', _run_key(base)), len(ha.get('acts') or []), sum(1 for x in ha.get('acts') or [] if x[1] == 'AGREE'),
                (ha.get('head') or '-')[:12], gs(ROOT, 'rev-parse', 'HEAD')[:12], (ha.get('boundary') or {}).get('equal')))
        write_half(key, _run_key(base), av, S['ar_reads'], span)
    sj = S['sealj'].get('tools') or {}
    rec('  ### THE SEALED TOOLS, recorded at the seal %s : %s' % (S['sealj'].get('at', '### NOT RECORDED'), '; '.join(
        '%s %s' % (t, ('agree' if sj.get(t) == S['sealnow'].get(t) else 'DIFFER') if t in sj else 'not recorded') for t in K.SEALED)))
    off = S['REC'].edit_route_offences(S['cmds'] + S['prev_cmds'])
    rec('  ### G-EDIT-ROUTE read %d captured commands of this act and %d of the previous act after its post-push suite; offences %d: %s' % (
        len(S['cmds']), len(S['prev_cmds']), len(off), ['#%s %s' % (r['n'], [k for k, _ in o]) for r, o in off] or 'none'))
    mc = re.search(r'(?<!ANSWER )CITES CHECKED \d+ ; OK \d+ ; MISSES \d+', S['citation'])
    rec('  ### THE CITATION CHECK: %s' % (mc.group(0) if mc else '### NOT READ'))
    rec('  ### PLACE-papers` changed files %d against the allowed %d (the two ledgers): beyond %s' % (
        len(S['pp_changed']), len(S['pp_allowed']), sorted(set(S['pp_changed']) - set(S['pp_allowed'])) or 'NONE'))
    rec('  ### SIDE-lv-conservation: main %s ; v0.10.0 %s ; port-b707 %s (its parent %s) ; tags %d ; the port run %s ; SIDE-explicit-formula main %s ; the join kernel main %s' % (
        S['lv_main'][:12], (S['lv_v0100'] or '')[:12], (S['lv_port'] or '-')[:12], (S['lv_port_parent'] or '-')[:12], len(S['lv_tags']), S['portj'].get('run_id') if S['portj'] else '-',
        S['ef_main'][:12], (S['join_main'] or '-')[:12]))
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
                                                 'OK' if (live and neg and not posv) else ('### POS PASSES -- DEFECTIVE' if posv else
                                                                                           '### FAILS -- THE CARRIED FAILURE DECLARED ON THE FACE' if name in CARRIED_FAILING else '### FAILS')))
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
    lp = os.path.join(D, _part_name(base, PART).replace('b707_arms_prerun', 'b707_lsr_prerun').replace('b707_checks', 'b707_lsr').replace('.txt', '.json'))
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    with open(lp + '.tmp', 'wb') as fh:
        fh.write(lb)
    os.replace(lp + '.tmp', lp)
    ex = dict(exercise=EX, run=len(arms), live_failing=fail, defective=defective, neg_failures=negfail, part=PART)
    ep = os.path.join(D, 'b707_exercise_%s.json' % PART)
    with open(ep + '.tmp', 'wb') as fh:
        fh.write((json.dumps(ex, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(ep + '.tmp', ep)
    # ### THE GUARD HELD -- the per-part seconds bank (root-named, gathered by the record tool's armsecs before the seal) is written by the pre-run
    # ### alone, as tools/b700_checks.py :1669 had it and b702 restored; the pre-push and post-push runs write no root-named bank
    if PRERUN:
        sp = os.path.join(D, 'b707_arm_seconds_%s.json' % PART)
        with open(sp + '.tmp', 'wb') as fh:
            fh.write((json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), part=PART, arms=SECS, phases=S['phase_secs'], run_secs=int(secs)),
                                 indent=1, ensure_ascii=False) + NL).encode('utf-8'))
        os.replace(sp + '.tmp', sp)
    print('  written: %s' % os.path.basename(out))
    carried_only = [f for f in fail if f not in CARRIED_FAILING] == [] and not defective and negfail == 0
    return 0 if (not fail and not defective and negfail == 0) else (4 if carried_only else 1)


if __name__ == '__main__':
    sys.exit(main())
