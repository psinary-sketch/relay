# -*- coding: utf-8 -*-
"""b710_checks.py -- THE SUITE OF b710, UNDER (R320): b709 AT ITS WEIGHT; THE NEEDLES, THE TEST AND THE LOCK GATE; THE STANDING CLAUSES BANKED;
READING 5; THE b711 REGISTRATIONS; SEVEN PARTS AS b706 SPLIT THEM.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### data/b684_rules.txt row (1) and b706's split, carried: every run in SEVEN foreground parts, each its own call in its own message --
### `--part standing-a`, `--part standing-c` (G-PRIORBANK-UNCHANGED, G-NODISCLOSURE-PUBLIC, G-WRITELIST-KINDS, the four standing figures and
### G-READ-RULE-STANDING), `--part standing-b1` (the shared additive files), `--part standing-b2a` (the act-root chain over b624-b641, its
### verdicts banked, NO ARM), `--part standing-b2b` (b642-b658, banked, NO ARM), `--part standing-b3` (the second half, b659-b710, and
### G-ACTROOT-VERIFY once over every banked verdict), `--part act` (the act's arms over this act's banks, the table regenerated in a closing run);
### each under the 590 s guard, NOT RUN beneath the 2,560 MB hold; `--combine <bank>` writes the bank. The chain halves as b693 drew them with
### b710 added to the second (the ferry's Component 5).
### ### (R264)(2), THE FREEZE: the standing arms are b709's face's (G2) arms less b709's own arms over b709's banks, carried, the twenty-four rule
### arms of tools/rule_arms.py and G-READ-RULE-STANDING among them; NO standing arm is added (N5). THE REPAIRS (R320)(3) ORDERS, each a diff in
### relay data/b710_tool_repairs.txt with its controls (data/b710_repair_controls.txt, 16 cases): G-REPORT-UNSEALED's key read case-insensitively
### (keys_ci) and G-AXIS-REGISTERED's bank read after joining wrapped lines (joined), both helpers here and the report arm reading through keys_ci;
### the lock gate's argument required; the lean-running test reading banked prints. G-RECEIPT-IN-FULL repointed to read the standing clauses by
### version ((R320)(4)). This suite carried by tools/b710_carry.py from tools/b709_checks.py (the act names substituted) and its act sections
### written by the Edit tool at the spans b709's repair diff names (data/b709_repairdiff_checks.txt): the sources over this act's banks and the
### arms over them (the weight and readings lines, the repairs, the standing clauses, reading 5, the moves record, the registrations, the fit)
### in place of b709's (the grid, the pairs, the port, the axis).
### The four standing figures read by tools/b706_standing_figures.py (unedited, over b706's roster) against b709's baselines
### (data/b709_standing_figures.json), each by b703's fig_ok. The standing runner arms (G-WORKFLOW-FILES, G-RUNNER-READ, G-RUNNER-GATE,
### G-MERGES-ON-GATE) read b709'S ONE RUN as banked -- no dispatch this act ((R320)(7)) -- port-b707 at b709's one commit (run 40123142437), its
### conclusion failure (11 of 12 modules, no grade claimed), the branch held, no main moved, no tag made, no merge.
### ### The PRERUN guard held: the per-part seconds bank is written under `if PRERUN:` alone, so no root-named bank is written by the pre-push or
### post-push run; `--guard-dry` prints, for each run mode, what the writer block would write, writing nothing.
### ### Every look-up of a landed line goes through the one conversion (imported from tools/b652_record.py through tools/b710_record.py).
### ### The harness is b568's to b709's, written by the Write tool from tools/b709_checks.py, its pure helpers imported from tools/b703_checks.py
### ### (sealed at b703 and unedited); the sources, predicates and arms over this act's banks are b710's (the act's arms over this act's banks,
### ### the b709 arms over b709's objects not carried). data/b686_rules.txt row (1): the act arm G-ENTRY-SCORES-EQUAL reads the landed entry; no
### ### scorer reads a ledger line. REQUIRED_BANKS is read against ROOT_EXCLUDE at import (b706's (j)): a required bank the route excludes refuses
### ### the suite before any part runs.
"""
import copy
import fnmatch
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
import b710_worklist as K     # noqa: E402
import b710_record as REC0    # noqa: E402  ### imported before b709's and b703's suites: b698's record tool is then rebound to b710 once
from b710_record import conv  # noqa: E402
import b709_worklist as K707  # noqa: E402
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
EF = K.EF_DIR                 # ### SIDE-explicit-formula, read unmoved this act
LV = K.LV_DIR                 # ### the kernel this act wrote: port-b707 given one commit, held; no main moved
KI = K.JOIN_DIR               # ### the join kernel, read unmoved
FACE = os.path.join(D, 'b710_registration_2026-10-24.txt')
B707_FACE = os.path.join(D, 'b709_registration_2026-10-23.txt')   # ### the previous act's face (b709's), the standing arms' source
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
# ### the sealed figures, the floors the count arms read at HEAD (standing from (R291)(3)): one prompt before the root this act (the moves table's
# ### placement, (R320)(5)(ii)), one call, its answer checked once per (R278)(4)
FLOORS = dict(prompts=1, calls=1, checks=1, defects=(('a', 'SEAT'), ('b', 'SEAT'), ('c', 'SEAT'), ('d', 'SEAT'), ('e', 'SEAT'), ('f', 'SEAT')))


def _bank_utc(text):
    """the UTC stamp a bank's head line carries, '(YYYY-MM-DDTHH:MM:SSZ)', as an epoch; None where absent."""
    m = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', NL.join((text or '').split(NL)[:2]))
    return iso_epoch(m.group(1)) if m else None


REPAIRED_TOOLS = K.REPAIRED_TOOLS
NEW_TOOLS = K.NEW_TOOLS
# ### the instruments read unedited: b703's list with b703's figures tool, b695's to b709's sealed tools, their new and repaired tools (b709's two
# ### shared tools and the roster among them, unedited this act), less this act's sealed tools
INST_BASE = tuple(C3.INST_BASE) + ('b703_standing_figures.py',)
INST = tuple(sorted((set(INST_BASE) | set(K695.SEALED) | set(K696.SEALED) | set(K697.SEALED) | set(K698.SEALED) | set(K699.SEALED) | set(K700.SEALED)
                     | set(K701.SEALED) | set(K702.SEALED) | set(K703.SEALED) | set(K704.SEALED) | set(K704.NEW_TOOLS) | set(K704.REPAIRED_TOOLS)
                     | set(K705.SEALED) | set(K705.NEW_TOOLS) | set(K705.REPAIRED_TOOLS) | set(K706.SEALED) | set(K706.REPAIRED_TOOLS)
                     | set(K707.SEALED) | set(getattr(K707, 'NEW_TOOLS', ())) | set(getattr(K707, 'REPAIRED_TOOLS', ()))
                     | set(p[6:] if p.startswith('tools/') else p for p in getattr(K707, 'REPAIRED_DATA', ())))
                    - set(K.SEALED) - set(REPAIRED_TOOLS) - set(NEW_TOOLS) - {'b710_report.py'}))


def _renamed():
    return dict((r['versioned'], r['unversioned']) for r in (jl('b706_partners.json').get('rows') or []) if r.get('versioned') and r.get('unversioned'))


# ### the corpus documents this act does not write: b703's list at the files of record after (R316)(3); no document is cut this act
CURRENTS = tuple(dict.fromkeys(_renamed().get(p, p) for p in C3.CURRENTS))
TABLE_FILES = K.TABLE_FILES
WF, PT = '.github/workflows/build-module.yml', 'print_targets.txt'
PORT_LABEL = K.PORT_LABEL     # ### b709's one run, read as banked by the standing runner arms (no dispatch this act)
CARRIED_NAMES = ('tests', 'record', 'checks', 'closing', 'reg_gate', 'regspec', 'corrigendum')
B1_ARMS = ('G-SHARED-ADDITIVE',)
B2_ARMS = ()
B3_ARMS = ('G-ACTROOT-VERIFY',)
C_ARMS = ('G-PRIORBANK-UNCHANGED', 'G-NODISCLOSURE-PUBLIC', 'G-WRITELIST-KINDS', 'G-CORRESPONDENCE-CURRENCY', 'G-README-CURRENCY', 'G-PARTNER-COPIES',
          'G-SISTER-PINS', 'G-READ-RULE-STANDING')
NEED = {'standing-a': ('live', 'rules'), 'standing-c': ('written', 'figures'), 'standing-b1': ('additive',), 'standing-b2a': ('chain_a1',),
        'standing-b2b': ('chain_a2',), 'standing-b3': ('chain_b',), 'act': ('efremote', 'lvremote')}
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
STD3 = ('Classical.choice', 'Quot.sound', 'propext')
NEXT_RULES_GLOB = 'relay/data/b710_rules.txt'
# ### (R315)(2)(b), b705's repaired predicate, carried: the root bank's items read against the root route's own item list, and the required list
# ### read against ROOT_EXCLUDE here, at import (b706's (j)); the binary banks (.gz) are not root items (data/b680_rules.txt row (1)), their hashes banks are
REQUIRED_BANKS = ('data/b710_reading5.txt', 'data/b710_r5_search.txt', 'data/b710_r5_terminals.txt', 'data/b710_r5_controls.txt', 'data/b710_r5_moves.txt',
                  'data/b710_r5_flip.txt', 'data/b710_r5_cost.txt', 'data/b710_moves_lines.json', 'data/b710_standing_control.txt', 'data/b710_standing_readers.txt',
                  'data/b710_fit.txt', 'data/b710_elab_reader_print.txt', 'data/b710_elab_reader_print_sec.txt',
                  'data/b710_registrations.txt', 'data/b710_registrations_reread.txt', 'data/b710_rules.txt', 'data/b710_tool_repairs.txt',
                  'data/b710_repair_controls.txt', 'data/b710_carry_spans.txt', 'data/b710_standing_figures.txt', 'data/b710_corrigendum.txt',
                  'data/b710_stepzero.txt', 'data/b710_report.txt', 'data/b710_citation_check.txt', 'data/b710_tests_stepzero.txt',
                  'data/b710_readfirst.txt', 'data/b710_branches.txt', 'data/b710_kernels_face.json')
STANDING_BANK = 'data/standing_clauses_v1.txt'   # ### (R320)(4): a shared bank by version, outside the act's prefix, named apart
_EXCLUDED_REQUIRED = [p for p in REQUIRED_BANKS if REC0.R.ROOT_EXCLUDE.match(os.path.basename(p))]
if _EXCLUDED_REQUIRED:
    raise SystemExit('### REQUIRED_BANKS NAMES A BANK THE ROOT ROUTE EXCLUDES (b706`s (j)): %s' % _EXCLUDED_REQUIRED)


def rec(s=''):
    L.append(s)
    print(s)


def _act_code(path):
    """the act's code in a tool: the whole file for this act's own tools; for a shared tool the ruling orders edited ((R320)(3)-(4)) the lines
    this act added to it alone (`git diff` from the act's base, its `+` lines) -- the shared tool's earlier code is its own act's, read by that
    act's arms (b378's fixture cleans its temporary directory, a line this act did not write)."""
    if os.path.basename(path) not in REPAIRED_TOOLS:
        return read(path)
    d = gs(ROOT, 'diff', PRE['relay'], '--', 'tools/' + os.path.basename(path))
    return NL.join(l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))


def is_pushed():
    return (gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b710')
            and 'data/b710_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    """tools/rule_arms.py's sources over the seat's session from (R320)'s anchor, its call trace extended by any continuation session's
    (K.SESSIONS_AFTER, none so far) through rule_arms.transcript."""
    R_ = RA.sources('b710', SESSION, K.ANCHOR, K.PARTS, lock, PRE['relay'], PRE['pp'])
    for sid, anc in K.SESSIONS_AFTER:
        R_['calls'] = list(R_.get('calls') or []) + RA.transcript('%s/%s.jsonl' % (PROJ, sid), anc)
    return R_


def conv_alone():
    P = 'p' + 'oss('
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to',
            'def ' + 'conv(']
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b710_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks):
                bad.append(f)
    return bad


def spec_planted():
    import b710_regspec as SPEC
    P = SPEC.planted()
    ctl = [ok for _w, ok in SPEC.controls()]
    return dict(read=[ok for _s, ok, _w in P], controls=ctl, shapes=[s for s, _o, _w in P])


def _deps(ax):
    return REC0._deps(ax)


def _tag_peel(repo, tag):
    return gs(repo, 'rev-parse', '--verify', '--quiet', 'refs/tags/%s^{commit}' % tag)


def wf_state():
    """b709's one run at SIDE-lv-conservation, read as banked (no dispatch this act): the workflow at port-b707's tip (b709's commit) equal to the
    workflow at b707's commit (the branch's base), written before b709; the lakefile and its Mathlib requirement; the print list ABSENT at the
    branch (the print step read as not run, no grade claimed); b709's one write on the branch the one module."""
    out = {}
    src = read_blob(LV, '%s:%s' % (K.PORT_TIP, WF)) or ''
    before = read_blob(LV, '%s:%s' % (K.PORT_BASE, WF)) or ''
    lf = read_blob(LV, '%s:lakefile.lean' % K.PORT_TIP) or read_blob(LV, '%s:lakefile.toml' % K.PORT_TIP) or ''
    req = re.search(r'(?is)require\s+(?:"?mathlib"?|\[\[require\]\]\s*name\s*=\s*"mathlib")', lf)
    pt = read_blob(LV, '%s:%s' % (K.PORT_TIP, PT)) or ''
    wrote = gs(LV, 'log', '-1', '--format=%H', K.PORT_TIP, '--', WF)
    act_writes = [x for x in gs(LV, 'diff-tree', '--no-commit-id', '--name-only', '-r', K.PORT_TIP).split(NL) if x.strip()]
    out[K.KERNEL] = dict(text=src, before=before, wrote=wrote, wrote_before_act=bool(wrote) and wrote != K.PORT_TIP,
                         lakefile=bool(lf.strip()), mathlib=bool(req), targets=[l.strip() for l in pt.split(NL) if l.strip()], print_list_absent=not pt.strip(),
                         printed=0, prints_targets=[], prints_printed=0, act_writes=act_writes, want=[K.PORT_FILE])
    return out


STANDING = sorted((set(g2_of(B707_FACE)) - set(K707.ACT_ARMS)) | set(K.STANDING_ADDED))
TESTS = ('test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py')


# ================================================================== THE CHAIN SPLIT BY ACT (b693's halves, b710 added; the first half in two quarters)
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
    return base.replace('b710_', '').replace('.txt', '')


def half_bank(i, key):
    """i is 'a1', 'a2' (the first half's quarters) or 'b' (the second half)."""
    return 'b710_chain_half_%s_%s.json' % (i, key)


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


def _primes_upto(n):
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = bytearray(len(s[i * i::i]))
    return [i for i in range(2, n + 1) if s[i]]


def prime_powers_in(lo, hi):
    """the prime powers p^k with lo < p^k <= hi, counted (the fine grid's rungs; the registration's DERIVED figures recounted here)."""
    out = 0
    for p in _primes_upto(hi):
        q = p
        while q <= hi:
            if q > lo:
                out += 1
            q *= p
    return out


def sources(need=()):
    """the sources the arms read; `need` (by part) names the heavy phases this part computes: 'live' (the three arms at HEAD), 'rules' (the
    rule arms' trace), 'written' (the written files, the public bytes, the prior banks), 'figures' (the four standing figures), 'chain_a1',
    'chain_a2' (the first half's quarters) and 'chain_b' (the second half), 'additive' (the shared files), 'efremote' (one ls-remote of
    SIDE-explicit-formula, the act part alone: main, the tags and the scratch branches' absence at the remote)."""
    import b616_record as R6
    import edit_route as ER
    import b641_record as R41
    import additive_shared as ADD
    import chain_page as CP
    REC = REC0
    face = read(FACE)
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b710_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if (f.startswith('b710_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS)
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    cit = jl('b710_citation_check.json')
    try:
        REC.R._defect_short()
        refuses = False
    except TypeError:
        refuses = True
    t0 = time.time()
    cmds = capture_now()
    ranking = (rd('b705_i6_ranking.txt') or '').split(NL)
    gz_g, gz_p = os.path.join(D, 'b710_grid.json.gz'), os.path.join(D, 'b710_pairs.json.gz')
    S = dict(
        REC=REC, ER=ER, face=face, ferry=rd('b710_ferry.txt'), scan=rd('b710_ferry_scan.txt'), stepz=rd('b710_stepzero.txt'),
        readfirst=rd('b710_readfirst.txt'), defects=rd('b710_defects.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        answers=rd('b710_author_answers.txt'), answersj=jl('b710_author_answers.json'), prerun=rd('b710_arms_prerun.txt'), rl=jl('b710_record_lines.json'),
        tests=jl('b710_tests_stepzero.json'), testst=rd('b710_tests_stepzero.txt'), withheld=jl('b710_tests_withheld.json'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b710_seal_hashes.json'), sealnow=sealed_now(), cmds=cmds, prev_cmds=prev_now(), cmdj=jl('b710_commands.json'),
        cmdt=rd('b710_commands.txt'), reads_bank=rd('b710_read_calls.txt'), reads_json=jl('b710_read_calls.json'),
        planted={t: run_test(t) for t in TESTS}, spec=spec_planted(), conv_bad=conv_alone(), suite=read(os.path.join(T, 'b710_checks.py')),
        citation=rd(K.CITATION_BANK), cit_at=iso_epoch(cit.get('at') or ''), cit_misses=cit.get('misses') or [],
        gate=rd('b710_reg_gate.txt'), rowgen=rd('b710_rowgen_stepzero.txt'),
        branchj=jl('b710_branches.json'), branchbj=jl('b710_branches_before.json'), branchest=rd('b710_branches.txt'),
        branch_lists=dict((repo, gs(repo, 'branch', '--list', *bs)) for repo, bs in K.DELETE),
        repairs=rd('b710_tool_repairs.txt'), repairsj=jl('b710_tool_repairs.json'), repair_ctl=rd('b710_repair_controls.txt'), repair_ctlj=jl('b710_repair_controls.json'),
        repairdiffs=dict((n_, rd('b710_repairdiff_%s.txt' % n_)) for n_ in CARRIED_NAMES), carry_banks=dict((n_, rd('b710_carry_%s.txt' % n_)) for n_ in CARRIED_NAMES),
        spans=rd('b710_carry_spans.txt'), rec_src=read(os.path.join(T, 'b710_record.py')),
        closing_src=read(os.path.join(T, 'b710_closing.py')),
        defshort=dict(b709=len(REC._defect_short('b709')), refuses=refuses),
        defshort_b710=REC._defect_short('b710'),
        corrj=jl('b710_corrigendum.json'), corrt=rd('b710_corrigendum.txt'), corrigenda=rd('b675_corrigenda.txt'),
        corrigenda_tri=tri(ROOT, 'data/b675_corrigenda.txt', PRE['relay']),
        guard=rd('b710_guard_dry.txt'), guardj=jl('b710_guard_dry.json'),
        rootdry=rd('b710_root_banks_dry.txt'), rootdryj=jl('b710_root_banks_dry.json'),
        figj=jl('b710_standing_figures.json'), figt=rd('b710_standing_figures.txt'),
        # ### (R320)(3): the repairs' controls, the lock gate and the test as they stand
        lockgate_src=read(os.path.join(T, 'b378_lockgate.py')), lean_test_src=read(os.path.join(T, 'test_elab_reader_b634.py')),
        elab_prints=(rd('b710_elab_reader_print.txt'), rd('b710_elab_reader_print_sec.txt')),
        # ### (R320)(4): the standing clauses by version, the control, the readers repointed
        standing_bank=read(os.path.join(ROOT, *STANDING_BANK.split('/'))), standing_ctlj=jl('b710_standing_control.json'), standing_ctl=rd('b710_standing_control.txt'),
        standing_readersj=jl('b710_standing_readers.json'), ferry709=rd('b709_ferry.txt'), ferry_scan_src=read(os.path.join(T, 'ferry_scan.py')),
        # ### (R320)(5): reading 5, its route banks, the moves record and its landing bank
        r5=rd('b710_reading5.txt'), r5banks=dict((n_, rd('b710_r5_%s.txt' % n_)) for n_ in ('search', 'terminals', 'controls', 'moves', 'flip', 'cost')),
        r5j=dict((n_, jl('b710_r5_%s.json' % n_)) for n_ in ('terminals', 'controls', 'flip', 'cost')), movesj=jl('b710_moves_lines.json'),
        # ### (R320)(6): the fit of (i)'s constants from b709's banked pairs
        fit=rd('b710_fit.txt'),
        # ### b709's one run, read as banked by the standing runner arms (no dispatch this act)
        portj=jl('b709_port.json'), portt=rd('b709_port.txt'), dispj=jl('b709_dispatches.json'), runner_rows=jl('b709_runner_rows.json'),
        dispj710=jl('b710_dispatches.json'),
        runs={PORT_LABEL: rd('b709_runner_%s_%s.txt' % (K.KERNEL, PORT_LABEL))},
        buildlogs={PORT_LABEL: rd('b709_buildlog_%s_%s.txt' % (K.KERNEL, PORT_LABEL))},
        lv_wf_tip=read_blob(LV, '%s:%s' % (K.PORT_TIP, WF)) or '', lv_wf_base=read_blob(LV, '%s:%s' % (K.PORT_BASE, WF)) or '',
        lv_tip_parent=gs(LV, 'rev-parse', '--verify', '--quiet', K.PORT_TIP + '^'),
        lv_tip_files=[x for x in gs(LV, 'diff-tree', '--no-commit-id', '--name-only', '-r', K.PORT_TIP).split(NL) if x.strip()],
        lv_tip_stat=[x for x in gs(LV, 'diff-tree', '--no-commit-id', '--numstat', '-r', K.PORT_TIP).split(NL) if x.strip()],
        lv_tip_on_main=subprocess.run(['git', '-C', LV, 'merge-base', '--is-ancestor', K.PORT_TIP, 'main']).returncode == 0,
        lv_main=gs(LV, 'rev-parse', 'main'), lv_v0100=_tag_peel(LV, 'v0.10.0'), lv_port=gs(LV, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.PORT_BRANCH),
        lv_tags=[t for t in gs(LV, 'tag', '--list').split(NL) if t.strip()], lv_remote={},
        # ### (R320)(6) and N4: the registrations (the refined law, the surgery, the coefficient observation), the rules bank, and their re-read
        regs=rd('b710_registrations.txt'), rules=rd('b710_rules.txt'), regs_reread=rd('b710_registrations_reread.txt'), regs_rereadj=jl('b710_registrations_reread.json'),
        regs_blob_reg=gs(ROOT, 'rev-parse', '--verify', '--quiet', '%s:data/b710_registrations.txt' % K.REG_COMMIT),
        regs_blob_head=gs(ROOT, 'rev-parse', '--verify', '--quiet', 'HEAD:data/b710_registrations.txt'),
        regs_blob_now=gs(ROOT, 'hash-object', '--', 'data/b710_registrations.txt'),
        regs_log=[l for l in gs(ROOT, 'log', '--format=%h', '--', 'data/b710_registrations.txt').split(NL) if l.strip()],
        ranking58=ranking[57] if len(ranking) > 57 else '', regs709=rd('b709_registrations.txt'), report709=rd('b709_report.txt'),
        computed_banks=sorted(f for f in os.listdir(D) if f.startswith('b710_') and re.search(r'nstar|pair1[15]|surgery|coeff|onset|eigen|_grid|_pairs', f)),
        report=rd('b710_report.txt'), report_tool=os.path.exists(os.path.join(T, 'b710_report.py')),
        ef_main=gs(EF, 'rev-parse', 'main'), ef_tags=dict((t, _tag_peel(EF, t)) for t in ('v0.37', 'v0.1', 'v0.2')),
        ef_log=[l for l in gs(EF, 'log', '--first-parent', '--format=%H', K.EF_V037 + '..main').split(NL) if l.strip()],
        ef_tags_all=[t for t in gs(EF, 'tag', '--list').split(NL) if t.strip()], ef_remote={},
        join_main=gs(KI, 'rev-parse', 'main') if os.path.isdir(KI) else '', join_tags=[t for t in gs(KI, 'tag', '--list').split(NL) if t.strip()] if os.path.isdir(KI) else [],
        rf_diff=rd('b710_readfirst_diff.txt'), rf_hand_now=blob(ROOT, 'HEAD:data/b710_readfirst.txt'),
        rf_hand_z=blob(ROOT, '%s:data/b710_readfirst.txt' % K.STEPZERO_BANKS) if K.STEPZERO_BANKS else None,
        asec=jl('b710_arm_seconds.json'), asect=rd('b710_arm_seconds.txt'),
        shared=dict((p, (cr0(blob(ROOT, '%s:%s' % (PRE['relay'], p))), cr0(raw(os.path.join(ROOT, *p.split('/')))), cr0(blob(ROOT, 'HEAD:' + p))))
                    for p in K.SHARED_APPENDED),
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), c2=_ct(ROOT, K.C2_RELAY), c3=_ct(ROOT, K.C3_RELAY), c3pp=_ct(PP, K.C3_PP),
               c3b=_ct(ROOT, K.C3_RELAY_B), c4=_ct(ROOT, K.C4_RELAY), stepzero=_ct(ROOT, K.STEPZERO_BANKS), reg=_ct(ROOT, K.REG_COMMIT)),
        files=dict(stepzero=files_of(ROOT, K.STEPZERO_BANKS) if K.STEPZERO_BANKS else [], c1=files_of(ROOT, K.C1_RELAY), c1pp=files_of(PP, K.C1_PP),
                   c2=files_of(ROOT, K.C2_RELAY), c3=files_of(ROOT, K.C3_RELAY), c3pp=files_of(PP, K.C3_PP), c3b=files_of(ROOT, K.C3_RELAY_B),
                   c4=files_of(ROOT, K.C4_RELAY), reg=files_of(ROOT, K.REG_COMMIT)),
        tracked=lambda p: bool(gs(ROOT, 'ls-files', '--', p).strip()),
        standing=STANDING, wf=wf_state(),
        export_present=os.path.exists(os.path.join(ROOT, *EXPORT.split('/'))), export_log=gs(ROOT, 'log', '--all', '--format=%h', '--', EXPORT),
        export_index=gs(ROOT, 'ls-files', '--', EXPORT), export_status=gs(ROOT, 'status', '--porcelain', '--', EXPORT),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b710_act_root.json'), arj0=jl('b709_act_root.json'), art=rd('b710_act_root.txt'), rootsf=rd('act_roots.txt'),
        rootbanks=jl('b710_root_banks.json'), route_list=REC.root_banks(),
        pushout=(files_of(ROOT, K.STEPZERO) if K.STEPZERO else [], bool(K.STEPZERO) and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, *f.split('/')))), cr0(blob(ROOT, 'HEAD:tools/' + f)))
              for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        pp_renames=gs(PP, 'diff', '--name-status', '-M', PRE['pp'], 'HEAD'),
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        page_changed=[x for x in (gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD', '--', K.FACES_PAGE) + NL + gs(PP, 'diff', '--name-only', '--', K.FACES_PAGE)).split(NL) if x.strip()],
        kern_face=(jl('b710_kernels_face.json').get('kernels') or {}), kerns_read=list(dict.fromkeys(REC._kerns())) + ['SIDE-faces-join'],
        tools=tools, tooltext={f: strip_prose(_act_code(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mustfail=not os.path.exists(os.path.join(D, 'b710_mustnotexist.txt')),
        fj=jl('b710_findings.json'), tj=jl('b710_trail.json'), sc=jl('b710_scores.json'), desk=rd('b710_desk_notes.txt'), tfj=jl('b710_table_final.json'),
        lsr=None,
        rlog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(ROOT, 'log', '--reverse', '--format=%h %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        plog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(PP, 'log', '--reverse', '--format=%h %ct %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()],
    )
    S['first_delete_ts'] = _first_ts(cmds, lambda c: bool(REC.delete_shape(c)[0]))
    S['first_listing_ts'] = _first_ts(cmds, lambda c: re.search(r'branch\s+--merged', c) is not None)
    S['onset_cmds'] = [r['n'] for r in cmds if r['tool'] in ('Bash', 'PowerShell') and re.search(r'python[^\n|&;]*(b70\d_onset\.py|witness_balls\.py|witness_terms\.py)', r['cmd'])]
    if 'efremote' in need:
        refs = {}
        for l in git(EF, 'ls-remote', 'origin')[1].split(NL):
            if '\t' in l:
                sha, ref = l.split('\t', 1)
                refs[ref.strip()] = sha.strip()
        S['ef_remote'] = refs
    if 'lvremote' in need:
        refs = {}
        for l in git(LV, 'ls-remote', 'origin')[1].split(NL):
            if '\t' in l:
                sha, ref = l.split('\t', 1)
                refs[ref.strip()] = sha.strip()
        S['lv_remote'] = refs
    S['root_at_commit'] = _root_named_at_commit(S['arj'])
    S['secs_ct'] = dict((p, _ct(ROOT, gs(ROOT, 'log', '-1', '--format=%H', '--', 'data/b710_arm_seconds_%s.json' % p))) for p in K.PARTS)
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
        base = jl('b709_standing_figures.json')
        S['fig'] = SF6.all_figures(baseline=((base.get('pins') or {}).get('rows') or {}), remote=KC0.remote_refs)
        S['fig_prev'] = base
        S['fig_prev_name'] = 'b709_standing_figures.json (b709`s figures; the readers over b706`s roster, data/b706_roster_read.json)'
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
            if f.startswith(('b710_', 'audit_b710_')) and os.path.isfile(os.path.join(D, f)) and not f.endswith(('.gz', '.png', '.jsonl')):
                pub.append(read(os.path.join(D, f)))
        pub += [read(f) for f in tools]
        pub += [S['lv_wf_tip'] or '', read_blob(LV, '%s:%s' % (K.PORT_TIP, K.PORT_FILE)) or '']
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


# ### the eight test files not clean at step zero: the three b706 carried and the five readers the renames of (R316)(3) broke (data/b710_defects.txt, the events)
STEPZERO_FAILING = {'test_chain_page.py': ['(1)', '(9)', '(14)'], 'test_chain_page_b629.py': ['(8)'], 'test_chain_page_b638.py': ['(4)', '(5)', '(6)', '(7)'],
                    'test_composer_b646.py': ['(10)', '(11)', '(17)', '(19)'], 'test_composer_b647.py': ['(4)', '(5)', '(7)', '(9)', '(17)', '(18)'],
                    'test_composer_b649.py': [], 'test_g_chain_page.py': ['(1)'], 'test_name_b649.py': ['(5)']}


def tests_ok(S):
    j = S['tests']
    names = sorted(S['tracked_tests'])
    nf = dict((n, x['failing']) for n, x in j.items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(j) == names and sorted(nf) == sorted(STEPZERO_FAILING) \
        and all(sorted(nf[n]) == sorted(STEPZERO_FAILING[n]) for n in nf if STEPZERO_FAILING[n]) \
        and 'b704_nodes_zeta.txt' in (j.get('test_chain_page.py') or {}).get('args', []) \
        and S['withheld'] == {} and 'test_elab_reader_b634.py' in j \
        and ('TEST FILES %d ; RUN %d ; WITHHELD 0 ; NOT CLEAN 8' % (len(names), len(names))) in unwrap(S['testst'])


UNANSWERED = "The user doesn't want to proceed with this tool use"


def answers_ok(S):
    """the answers bank at HEAD: its prompt count the bank's own (none before the root this act), each prompt with its options and result, any
    call after the lock named on the face."""
    a = S['answers']
    m = re.search(r'^### b710 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
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


def no_local_lean(S):
    return bool(S['cmds']) and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and S['REC'].local_lean(r['cmd'])]


# ================================================================== (R320) STEP ZERO: THE CITATION CHECK, THE BRANCHES, THE READ-FIRST BANK
READFIRST_NEEDLES = ('relay data/b709_closing.txt | :1 ;', 'relay data/b709_defects.txt | :1-:171 (whole)', 'relay data/b709_grid.txt | :1-:60 (the head',
                     'relay data/b709_pairs.txt | :1-:62 (whole)', 'relay data/b709_port.txt | :1-:53 (whole)', 'relay data/b709_registrations.txt | :1-:61 (whole)',
                     'relay data/b709_tool_repairs.txt | :1-:33 (whole)', 'relay data/b709_closing_push_out.txt | :1-:6 (whole)', 'relay data/b709_ferry.txt | :1-:51 (whole)',
                     'relay data/b700_reading4.txt | :1-:128 (whole)', 'relay data/b690_reading3.txt | :1-:100 (whole)', 'relay tools/b378_lockgate.py | :1-:60 ; :60-:230',
                     'relay tools/test_elab_reader_b634.py | :1-:81 (whole)', 'PLACE-papers phase1.5/method/THE_BRIGHTENING_MOVES.md | :1-:29 (whole)',
                     'PLACE-papers phase1.5/method/INSTRUMENTS.md | :1-:150', 'PLACE-papers phase1.5/method/THE_METHOD_CANON.md | :1-:120',
                     'PLACE-papers phase2/method/E_DIFFICULTY_THEOREM.md | :1-:150', 'PLACE-papers day1/Exhaustive_Enumeration.md | :1-:189 (whole)',
                     'PLACE-papers phase1.5/method/ENUMERA.md | :205-:314', 'PLACE-papers OPEN_TRAILS.md | :15450 ; :15762-:15802')
NAMED_PUSH = sorted(b for _r, bs in K.DELETE for b in bs)
SCRATCH = ()                  # ### no scratch branch this act: the one branch written is port-b707, held ((R320)(4), (7))


def readfirst_ok(S):
    z = unwrap(S['readfirst'])
    return bool(z) and all(x in z for x in READFIRST_NEEDLES) and 'ITEMS 33 ;' in z


def branches_ok(S):
    z = S['branchest']
    left = dict((r, sorted(x.strip() for x in v.split(NL) if x.strip())) for r, v in S['branch_lists'].items())
    return all(v == [] for v in left.values()) and len(left) == 2 and all(b in z for b in NAMED_PUSH) \
        and 'BRANCHES NAMED 6 ; DELETED 6 ; KEPT 0 ; EVERY TIP MERGED True ; port-b707 STANDS True' in unwrap(z)


def branches_banked_ok(S):
    rows = S['branchj'].get('rows') or []
    try:
        fates = [S['REC'].read_branch_row(r) for r in rows]
    except Exception:
        return False
    bt = iso_epoch((S['branchbj'].get('at') or '')[:19] + 'Z')
    fd = S['first_delete_ts']
    kept = S['branchj'].get('kept') or {}
    return len(rows) == 6 and all(f == 'DELETED' for _b, f in fates) and all(r['merged'] for r in rows) \
        and sorted(r['branch'] for r in rows) == NAMED_PUSH and bool(bt) and bool(fd) and bt < fd and len(S['branchbj'].get('rows') or []) == 6 \
        and bool(S['cit_at']) and S['cit_at'] < fd and kept.get('branch') == K.PORT_BRANCH and kept.get('local') == kept.get('remote') == K.PORT_TIP


def deletes_one_ok(S):
    """every branch delete of the act one branch, no glob, no variable, nothing chained after: the six of (R320)(7) alone; port-b707 deleted under
    no answer."""
    sh_ = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell')]
    shapes = [(S['REC'].delete_shape(r['cmd']), S['REC'].chained_after(r['cmd'])) for r in sh_]
    shapes = [(s, c) for s, c in shapes if s[0]]
    named = set(NAMED_PUSH) | set(SCRATCH)
    got = sorted(x for (d, _g, _v), _c in shapes for x in d)
    return bool(shapes) and all(len(d) == 1 and not gl and not vs and not c for (d, gl, vs), c in shapes) \
        and set(got) <= named and all(b in got for b in NAMED_PUSH) and all(b in got for b in SCRATCH) and K.PORT_BRANCH not in got \
        and ('BRANCH DELETES OF ONE BRANCH, NO GLOB, NO VARIABLE AND NOTHING CHAINED AFTER %d OF %d' % (len(shapes), len(shapes))) in S['cmdt']


def listings_before_ok(S):
    """N3: the listing `git branch --merged main` printed before the first delete; every branch deleted among the branches banked before any delete."""
    bb = S['branchbj'].get('rows') or []
    bj = S['branchj'].get('rows') or []
    listed = set((r.get('repo'), r.get('branch')) for r in bb)
    named = set((r.get('repo'), r.get('branch')) for r in bj)
    return bool(S['first_listing_ts']) and bool(S['first_delete_ts']) and S['first_listing_ts'] < S['first_delete_ts'] and bool(named) and named <= listed \
        and 'the listings of (R320)(8)' in S['stepz'] and 'printed before any branch or file clause was acted on' in S['stepz']


def dry_step_ok(S):
    g = S['gate']
    return '--- THE DRY-RUN STEP ((R267)(2))' in g and 'ENTRY : table cells NONE ; screens QUIET' in g and 'TRAIL : table cells NONE ; screens QUIET' in g \
        and 'THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK True' in g and 'THE TRAIL`S RESOLVED LINE EQUAL TO THE DEFECTS BANK True' in g \
        and '### ### **THE DRY-RUN STEP : CLEAN**' in g and '### ### **GATE VERDICT : CLEAR**' in g


# ### (R320)(2): the banks that carry no verdict line BY THEIR FORM -- b709's prints bank (b706's prints form, the probe step's print banked whole, the
# ### repair's ground), and this act's two hashes banks (rows of path ; sha256 ; bytes, data/b680_rules.txt row (1)) and the push tool's capture of
# ### the port branch's push, each printed by the closing's sections and each exempt by name; the string fails anywhere else in the gate's record
NO_VERDICT_EXEMPT = ('data/b709_prints_v0.17.txt', 'data/b710_elab_reader_print.txt', 'data/b710_elab_reader_print_sec.txt', 'data/b710_moves_lines.json')


def no_verdict_line_ok(g):
    """(R320)(2), the carry-time repair of G-CLOSING-DRY-STEP's needle: the closing's dry run prints '### NO VERDICT LINE' for a bank that
    carries no verdict line by its form (b709's prints bank, data/b709_prints_v0.17.txt); the arm excludes that bank's line by name and
    fails on the string anywhere else in the gate's record (a verdict-bearing bank printed without its verdict). b709's own gate record
    (data/b709_reg_gate.txt :51) passes; the NEG control -- the string on a verdict-bearing bank's line -- fails (data/b710_repair_controls.txt)."""
    rest = [l for l in g.split(NL) if not any(x in l for x in NO_VERDICT_EXEMPT)]
    return '### NO VERDICT LINE' not in NL.join(rest)


def closing_dry_ok(S):
    g = S['gate']
    return '--- THE CLOSING DRY-RUN STEP (b675 rules row 1)' in g and '### ### **THE CLOSING DRY-RUN STEP : CLEAN**' in g \
        and 'b710 closed:' in g and 'THE REPAIRS' in g and 'THE STANDING CLAUSES' in g and 'READING 5' in g and 'THE MOVES' in g and 'THE REGISTRATIONS' in g \
        and '### THE STANDING ARMS' in g and '### THE KERNELS' in g and '(g) The defects (a)' in g and no_verdict_line_ok(g)


def citation_ok(S):
    """the citation check's bank: every cite checked, OK and misses summing, its two misses entered by the fact clause ("rising with height" read
    step by step; (6)(i)'s M and A against the route's own terms); the bank written before the step-zero banks' commit and that commit before
    Component 1's."""
    c = S['citation']
    m = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', c)
    return bool(m) and int(m.group(1)) == int(m.group(2)) + int(m.group(3)) > 0 and 'A GATE STEP AT STEP ZERO' in c \
        and int(m.group(3)) == len(S['cit_misses']) == 2 and 'rising with height' in c and 'REMAINDER BOUND' in c and bool(S['cit_at']) and bool(S['t'].get('stepzero')) \
        and S['cit_at'] < S['t']['stepzero'] and bool(S['t'].get('c1')) and S['t']['stepzero'] <= S['t']['c1']


def rowgen_ok(S):
    return '### ### **CONSTELLATION EXIT 0 ; ROWGEN DIFF EXIT 0 ; TABLES 19 ; RE-POINTED 8.**' in S['rowgen']


def weight_ok(S):
    # ### this act's needles are b709's closing hashes (data/b709_closing.txt :1, 42dd8768), read on the weight line, and the readings line beside it
    return landed(S, 0, ['b709 closed: relay 8b842c9a', '42dd8768']) and landed(S, 1, ['(i) the rung hypothesis was vacuous', 'beta = 7.997097'])


# ### (R315)(2)(c), b705's repaired predicate, carried: the checks the root prompt requires are admitted after the seal, each printed with its
# ### time by the record tool's control; every other check before the lock and before the step it governs.
ROOT_PROMPT = re.compile(r'\broot\b', re.I)


def _answers_checked(S, floors, act=708, lock_key='lock_epoch'):
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


def answers_checked_ok(S):
    return _answers_checked(S, FLOORS['checks'])


def answers_before_ok(S):
    """the one mid-act answer (the moves table's placement, (R320)(5)(ii)) checked before it was acted on: its check stamp before the lock and
    before the OPEN_TRAILS record's landing (data/b710_moves_lines.json), the record in Component 3's PLACE-papers commit; every other stamp (the
    root's) after the lock; the answers bank carrying the one prompt."""
    st = re.findall(r'### \(R278\)\(4\) THE MID-ACT CHECK \((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\): the (?:navigator`s )?answer carrying \'([^\']+)\'', S['citation'])
    lk = S['lock_epoch']
    land_at = iso_epoch((S['movesj'].get('at') or '')[:19] + 'Z') if S['movesj'].get('at') else None
    before = [iso_epoch(t) for t, n in st if n.startswith('Moves table: 1')]
    rest = [iso_epoch(t) for t, n in st if not n.startswith('Moves table: 1')]
    return FLOORS['prompts'] == 1 and lk is not None and len(before) == 1 and before[0] is not None and land_at is not None and before[0] < land_at < lk \
        and all(x is not None and x >= lk for x in rest) and len(re.findall(r'^### PROMPT \d+ \(', S['answers'], re.M)) >= 1 \
        and 'OPEN_TRAILS.md' in S['files']['c3pp']


# ================================================================== (R320)(1)-(2): THE RECORD LINES, THE CORRIGENDUM, THE WRITE LIST
def scorer_banks_ok(S):
    n = ''.join(strip_prose(_fn_src(S['rec_src'], f)) for f in ('_n1', '_n2', '_n3', '_n4'))
    sc = strip_prose(_fn_src(S['rec_src'], 'scores'))
    ft = strip_prose(_fn_src(S['rec_src'], '_finding_text'))
    return bool(n) and '_commands.json' in n and '_dispatches.json' in n and '_r5_terminals' in n and '_standing_control' in n and '_registrations_reread' in n \
        and not re.search(r'\b(FIND|OT)\b|FINDINGS|OPEN_TRAILS|findings|entry_line', n) \
        and "os.path.isfile(os.path.join(D, '%s_scores.json' % ACT))" in sc and 'scores_line(S)' in ft and "jl('%s_scores.json' % ACT)" in ft


def entry_scores_ok(S):
    want = conv(S['REC'].scores_line(S['sc'])) if S['sc'] else None
    blk = _entry_block(S)
    got = [l for l in blk.split(NL) if l.startswith('**The scores.**')]
    return bool(want) and bool(S['sc']) and got == [want]


# ### the title by its objects (the ferry's Component 6), compared after case-folding the article alone (b706's repaired predicate, carried)
TITLE_NEEDLES = ('reading 5: the four principles against the corpus, ', ' of 4 with a compiled terminal and ', ' with a control object; the moves-by-locus table entered',
                 '; the standing clauses banked at v1; the refined detection law and the surgery registered for b711')


def _fold_article(t):
    """b706's fold of the article, carried, and the title's first word folded with it (this act's title opens "Reading 5:", the ferry's form
    "reading 5: ..." in lower case)."""
    t = re.sub(r'^(## )(The|A|An)( )', lambda m: m.group(1) + m.group(2).lower() + m.group(3), t)
    return re.sub(r'^(## )(Reading)( )', lambda m: m.group(1) + m.group(2).lower() + m.group(3), t)


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
    m = re.search(r'^\*\*Defects\*\* \(relay data/b710_defects\.txt\): (.*)\.$', trail_tail(S), re.M)
    return 'THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK True' in S['gate'] and bool(m) \
        and m.group(1) == conv('; '.join(S['defshort_b710']) or 'none')


RESOLVED = re.compile(r'^\*\*Resolved by the seat, for the author’s strike:\*\* .*\((\d+)\) the (\w+) navigator (?:miss|misses)'
                      r'(?: \(\([a-z]\)(?:, \([a-z]\))*\))? and the seat’s (\w+) defects? as lettered\.$', re.M)


def trail_resolved_ok(S):
    m = RESOLVED.search(trail_tail(S))
    nav, seat = _owners(S['defshort_b710'])
    return 'THE TRAIL`S RESOLVED LINE EQUAL TO THE DEFECTS BANK True' in S['gate'] and bool(m) and S['REC'].num_word(nav) == m.group(2) \
        and S['REC'].num_word(seat) == m.group(3)


def corrigendum_ok(S):
    """(R320)(3): the generated entry landed (its line in the bank, the title at that line through conv), b709's two post-seal needles (an
    unlettered event) answered, no lettered defect and no trail arm at b709; the corrigenda bank appended at row (30) and nothing before it
    changed; in Component 1's commit."""
    j = S['corrj']
    e = j.get('entry_line')
    now, pre, head = S['corrigenda_tri']
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and j.get('lettered') == [] and j.get('trail_arms') == [] \
        and j.get('events') == ['G-AXIS-REGISTERED', 'G-REPORT-UNSEALED'] and j.get('row') == 30 and '  (30) ' in S['corrigenda'] and '  (31) ' not in S['corrigenda'] \
        and pre is not None and (now or b'').startswith(pre) and (head or b'').startswith(pre) and 'FINDINGS :%d' % e in S['corrt'] \
        and 'data/b710_corrigendum.txt' in S['files']['c1']


def writelist_mirror_state_ok(S):
    """(R320)(2): the face's (W) row for the mirror builder names tools/mirror_prevbuild.json beside the zip and its stage; N5 reads it as the
    builder's own (the record tool's N5_RELAY_TOOLS)."""
    w = S['face'][S['face'].find('(W) THE WRITE LIST'):S['face'].find('(Z) THE NOTHINGS')]
    row = [l for l in w.split(NL) if 'mirror_build.ps1' in l]
    return bool(row) and 'tools/mirror_prevbuild.json' in NL.join(w.split(NL)[w.split(NL).index(row[0]):w.split(NL).index(row[0]) + 2]) \
        and 'mirror_prevbuild.json' in tuple(S['REC'].R.N5_RELAY_TOOLS)


def rules_row_ok(S):
    """data/b710_rules.txt rows (1) the standing clauses carried by version and (2) the lock gate's argument required, committed alone with the
    registrations; b709's row (1), the carry read by diff, binding this act's carry; b708's row (1), the report tool outside the sealed list until
    the root's word, the worklist's SEALED naming no report tool."""
    return '(1) THE STANDING CLAUSES CARRIED BY VERSION' in S['rules'] and '(2) THE LOCK GATE`S ARGUMENT REQUIRED'.replace('`', "'") in S['rules'] \
        and 'data/b710_rules.txt' in S['files']['reg'] and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') \
        and '(1) THE REPORT TOOL IS KEPT OUT OF THE SEALED LIST UNTIL THE ROOT' in rd('b708_rules.txt') \
        and not any('report' in t for t in K.SEALED) and 'b710_report.py' not in (S['sealj'].get('tools') or {})


def report_unsealed_ok(S):
    """the report bank written by the unsealed report tool after the root's word and before the root: its head stamp after the lock and at or
    before the root's time; the tool outside the sealed list; its lines the ferry's five (the principles' four rows, the moves table's tried and
    untried counts, the readfirst recommendation, the cost reading's top three files, the four figures beside b709's), each key read
    case-insensitively ((R320)(3), keys_ci)."""
    t = S['report']
    at = _bank_utc(t)
    root_at = S['arj'].get('at_epoch')
    return bool(t) and S['report_tool'] and 'b710_report.py' not in K.SEALED and at is not None and S['lock_epoch'] is not None and at > S['lock_epoch'] \
        and root_at is not None and at <= root_at + S['order_slack'] and keys_ci(t, ('PRINCIPLES', 'MOVES', 'READFIRST', 'COST', 'FIGURES')) \
        and len(re.findall(r'^  \(\d\) ', t, re.M)) >= 5


def keys_ci(text, keys):
    """(R320)(3), the carry-time repair of G-REPORT-UNSEALED's needle: each key read case-insensitively (b709's sealed arm wanted RATIO in capitals
    and its report printed "the twelve ratios", so the arm failed after the seal on its own needle)."""
    low = (text or '').lower()
    return all(k.lower() in low for k in keys)


def joined(text):
    """(R320)(3), the carry-time repair of G-AXIS-REGISTERED's needle: the bank read after joining its wrapped lines -- every run of white space,
    the line breaks and the continuation indents among them, read as one space (b709's registrations bank wrapped the ranking's quotation across
    its lines 12-13, so the arm's one-string needle found nothing there after the seal)."""
    return ' '.join((text or '').split())


GUARD_WRITE = "sp = os.path.join(D, 'b710_arm_seconds_%s.json' % PART)"   # ### the write's own line, stripped; matched whole, not by a needle


def guard_ok(S):
    s = S['suite'].split(NL)
    i = next((k for k, l in enumerate(s) if l.strip() == GUARD_WRITE), None)
    j = S['guardj']
    return i is not None and s[i - 1].strip() == 'if PRERUN:' and 'POST-ROOT PATH WRITES NONE' in S['guard'] \
        and (j.get('writes') or {}).get('pre-push') == [] and (j.get('writes') or {}).get('post-push') == [] \
        and (j.get('writes') or {}).get('prerun') == ['data/b710_arm_seconds_<part>.json']


def postroot_writes_none(S):
    j = S['guardj']
    w = j.get('writes') or {}
    return 'POST-ROOT PATH WRITES NONE' in S['guard'] and w.get('pre-push') == [] and w.get('post-push') == [] and bool(S['root_ct']) \
        and sorted(S['secs_ct']) == sorted(K.PARTS) and all(v is not None and v <= S['root_ct'] for v in S['secs_ct'].values())


def trail_lines_equal_defects(S):
    tail = trail_tail(S)
    dm = re.search(r'^\*\*Defects\*\* \(relay data/b710_defects\.txt\): (.*)\.$', tail, re.M)
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


# ================================================================== THE RUNNER (b709's one run: port-b707 at its tip, its failure read as banked; no dispatch this act)
IDENT_WF = ('secrets.', 'psinary', 'seale', 'york', 'hotmail', 'orcid', '0009-0008')


def wf_ok(S, rules_needle='(1) THE PROBE ROUTE\'S TARGET IS print_targets.txt WHOLE'):
    """b705's repaired reading over b709's one run (no dispatch this act, the act's own dispatch bank absent): the workflow at port-b707's tip
    b707's blob unchanged, no identifier, the hold, the lakefile and its cache step; the print list ABSENT at the branch, so the print step is read
    as not run and no grade claimed (the dispatch row saying so and `whole` False by it); b709's one write on the branch the one module."""
    if S['dispj710'].get('rows'):
        return False
    for k, v in S['wf'].items():
        t = v['text'].lower()
        if not v['text'] or v['text'] != v['before'] or not v['wrote_before_act'] or any(w in t for w in IDENT_WF):
            return False
        if 'workflow_dispatch' not in t or 'hold_mb: "2560"' not in t:
            return False
        if not v['lakefile'] or (('lake exe cache get' in t) != v['mathlib']):
            return False
        if not v['print_list_absent'] or v['targets'] or v['act_writes'] != v['want']:
            return False
    rows = S['dispj'].get('rows') or []
    return sorted(S['wf']) == [K.KERNEL] and len(rows) == 1 and rows[0].get('whole') is False and 'ABSENT' in (rows[0].get('print_list') or '') \
        and rd('b705_rules.txt').count(rules_needle) == 1


def runner_ok(S):
    """b709's one run as read by its id (banked by b709; no run this act): at the tip, its conclusion failure, the artifact's sha256 equal to the port bank's, the memory
    low above the hold, no STOP line, the gate NOT DERIVES with no grade claimed (the print step not run), build exit 1 with its 8 error lines; the
    row through the record tool's reader."""
    rows = S['runner_rows'].get('rows') or []
    if len(rows) != 1:
        return False
    try:
        S['REC'].read_runner_row(rows[0])
    except Exception:
        return False
    r = rows[0]
    return r.get('label') == PORT_LABEL and r.get('kernel') == K.KERNEL and r.get('ref') == K.PORT_TIP and r.get('run_id') == K.PORT_RUN and r.get('conclusion') == 'failure' \
        and re.match(r'^[0-9a-f]{64}$', r.get('artifact_sha256') or '') is not None and r.get('artifact_sha256') == (S['portj'].get('artifact') or {}).get('sha256') \
        and r.get('mem_low') is not None and r['mem_low'] >= K.HOLD and not r.get('stopped') and r.get('gate') == 'NOT DERIVES' and r.get('build_exit') == '1' \
        and len(r.get('errors') or []) == 8 and 'no grade claimed' in (r.get('note') or '')


def gate_ok(S):
    """the run's text bank: the artifact AGREE, the build's exit 1 with its error lines, no grade claimed."""
    t = S['runs'].get(PORT_LABEL) or ''
    return len(S['runs']) == 1 and re.search(r'^### the artifact: .* ; AGREE$', t, re.M) is not None and 'BUILD EXIT 1' in t and 'NO GRADE CLAIMED' in t.upper()


def merges_ok(S):
    """no merge this act: SIDE-explicit-formula's main at badaccc (one first-parent commit past v0.37), its tags unmoved; SIDE-lv-conservation's main
    and deposit unmoved, port-b707 at b709's one commit locally and at the remote and not on main, no tag made; the join kernel's main at its
    manifest commit, no tag."""
    er, lr = S['ef_remote'], S['lv_remote']
    return S['ef_main'] == K.EF_MAIN and len(S['ef_log']) == 1 and S['ef_tags'].get('v0.37') == K.EF_V037 \
        and not [t for t in S['ef_tags_all'] if t > 'v0.37' and t.startswith('v0.3')] \
        and (not er or (er.get('refs/heads/main') == K.EF_MAIN and er.get('refs/tags/v0.37^{}', er.get('refs/tags/v0.37')) == K.EF_V037)) \
        and S['lv_main'] == K.LV_MAIN and S['lv_v0100'] == K.LV_V0100 and S['lv_port'] == K.PORT_TIP and 'v0.10.0' in S['lv_tags'] and not S['lv_tip_on_main'] \
        and not [t for t in S['lv_tags'] if t.startswith('v0.1') and t > 'v0.13.0'] \
        and (not lr or (lr.get('refs/heads/main') == K.LV_MAIN and lr.get('refs/heads/' + K.PORT_BRANCH) == K.PORT_TIP)) \
        and S['join_main'] == K.JOIN_TIP and S['join_tags'] == []


# ================================================================== SCOPE, THE SEAL, THE ROOT, THE RECORD
def seal_hashes_ok(S):
    j = S['sealj']
    at = iso_epoch(j.get('at') or '')
    rec_ = j.get('tools') or {}
    return bool(rec_) and at is not None and S['lock_epoch'] is not None and S['lock_epoch'] <= at \
        and sorted(rec_) == sorted(K.SEALED) and all(S['sealnow'].get(t) == rec_[t] for t in K.SEALED)


POST_SEAL = ('b710 seal', 'b710 pre-root', 'b710 root', 'b710 record', 'b710 --', 'b710 closing', 'b710 entry')


def _component_commit(s):
    return s.startswith('b710') and not s.startswith(POST_SEAL)


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
    return _root_banked(S, 'b710', 87)


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b710_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    """the chain recomputed at commit in three parts: standing-b2a's and standing-b2b's banked quarters (b624-b641, b642-b658) and
    standing-b3's second half (b659-b710), every act AGREE, the boundary link equal, b680 read through its corrigendum row, b710 written LF."""
    ha = S['half_a'] or {}
    v = [tuple(x[:2]) for x in (ha.get('acts') or [])] + [tuple(x[:2]) for x in (S['ar_verify'] or [])]
    r = dict(ha.get('reads') or {}, **(S['ar_reads'] or {}))
    return ha.get('head') == gs(ROOT, 'rev-parse', 'HEAD') and [x[0] for x in v] == ['b%d' % i for i in range(624, 711)] \
        and all(x[1] == 'AGREE' for x in v) and (r.get('b710') or {}).get('crlf') == 0 and (r.get('b680') or {}).get('corrected') == 4 \
        and (ha.get('boundary') or {}).get('equal') is True and S['boundary'].get('equal') is True \
        and (ha.get('boundary') or {}).get('root') == S['boundary'].get('root')


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


def corpus_scope_ok(S):
    """N5: PLACE-papers' changed files within the two ledgers and the named document alone; no rename."""
    ch = S['pp_changed']
    ren = [l for l in S['pp_renames'].split(NL) if l[:1] in ('R', 'D')]
    return bool(ch) and set(ch) <= set(S['pp_allowed']) and 'FINDINGS.md' in ch and 'OPEN_TRAILS.md' in ch and not ren


ENTRY_NEEDLES = ('**The corrigendum**', '**The repairs**', '**The standing clauses**', '**The principles**', '**The moves table**', '**The readfirst flip**',
                 '**The cost reading**', '**The registrations**', '**The standing arms**', '**The citation check**', '**The scores.**', '**Read in mutual light**',
                 'strengthens', '**Carried to:**', '**Next.**', 'b711', 'W-ORD-MOVES-BY-LOCUS', 'standing clauses v1', 'Q0', 'DirichletC7Order.lean :212:55')


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
        and '### THE CITATION CHECK' in t and '### THE RECORD LINES' in t and '### THE DRY RUN' in t and 'THE REPAIRS' in t and 'THE STANDING CLAUSES' in t \
        and 'READING 5' in t and 'THE MOVES' in t and 'THE REGISTRATIONS' in t and 'THE STANDING ARMS' in t and '### THE KERNELS' in t \
        and '### THE MIRROR' in t and '### THE CARRY-TIME' in t


# ================================================================== THIS ACT'S ARMS OVER ITS OWN BANKS (Component 5)
NAV_LETTERS = ()              # ### every defect of this act the seat's; the ruling's two citation misses entered by the fact clause, not lettered


def defects_ok(S):
    rows = re.findall(r"^    \(([a-z])\) THE (NAVIGATOR|SEAT)'S", S['defects'], re.M)
    want = [list(x) for x in FLOORS['defects']]
    return len(rows) >= len(want) and [list(r) for r in rows[:len(want)]] == want and all(o in ('NAVIGATOR', 'SEAT') for _l, o in rows) \
        and [l for l, o in rows if o == 'NAVIGATOR'][:len(NAV_LETTERS)] == list(NAV_LETTERS)


def repairs_ok(S):
    """the repairs bank: the four repairs of (R320)(3) (the two needles, the lock gate, the test) each with its diff and its controls, and the
    carry-time rows (each carried tool's repairdiff bank present with its verdict); the controls 16 cases as wanted; both banks tracked at HEAD."""
    r = unwrap(S['repairs'])
    return all(('  (%d) ' % i) in S['repairs'] for i in (1, 2, 3, 4)) and 'tools/b378_lockgate.py main' in r and 'tools/test_elab_reader_b634.py --' in r \
        and 'keys_ci' in r and 'joined' in r and 'CONTROLS AS WANTED True' in r and 'NO SEALED TOOL OF AN EARLIER ACT EDITED' in r \
        and all(S['repairdiffs'].get(n) and 'HUNKS' in S['repairdiffs'][n] for n in CARRIED_NAMES) \
        and S['repair_ctlj'].get('as_wanted') is True and len(S['repair_ctlj'].get('cases') or []) == 16 and (S['repair_ctlj'].get('changed') == []) \
        and 'CASES 16 ; AS WANTED True' in unwrap(S['repair_ctl']) and S['tracked']('data/b710_tool_repairs.txt') and S['tracked']('data/b710_repair_controls.txt')


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
    """the four figures banked by b706's tool over b706's roster against b709's baselines, each at or below b709's; the partners rows one copy
    per table, the figure 0."""
    j, f7 = S['figj'], jl('b709_standing_figures.json')
    figs = dict((k, (j.get(k) or {}).get('figure')) for k in ('correspondence', 'readme', 'partners', 'pins'))
    prev = dict((k, (f7.get(k) or {}).get('figure')) for k in figs)
    pr = (j.get('partners') or {}).get('rows') or []
    return all(isinstance(figs[k], int) and isinstance(prev[k], int) and figs[k] <= prev[k] for k in figs) and figs['partners'] == 0 \
        and len(pr) == 20 and all((r.get('reason') or '').startswith('ONE COPY') for r in pr) and j.get('roster') == 'b706_roster_read.json' \
        and j.get('baseline') == 'b709_standing_figures.json' and 'FIGURES AT b710' in S['figt']


# ================================================================== (R320)(6) AND N4: THE REGISTRATIONS AND THE FIT
def registrations_alone_ok(S):
    """data/b710_registrations.txt (the three registrations for b711) committed alone with data/b710_rules.txt at step zero, before the step-zero
    banks' commit and Component 1's; its blob unchanged at HEAD and in the working tree; the one commit touching it; nothing computed for it."""
    return sorted(S['files']['reg']) == ['data/b710_registrations.txt', 'data/b710_rules.txt'] and bool(S['t'].get('reg')) and bool(S['t'].get('c1')) \
        and bool(S['t'].get('stepzero')) and S['t']['reg'] <= S['t']['stepzero'] <= S['t']['c1'] and bool(S['regs_blob_reg']) \
        and S['regs_blob_reg'] == S['regs_blob_head'] == S['regs_blob_now'] and len(S['regs_log']) == 1 and 'REGISTRATIONS 3' in unwrap(S['regs']) \
        and 'COMPUTED AT b711' in unwrap(S['regs']) and 'NOTHING COMPUTED AT b710' in unwrap(S['regs'])


def registrations_reread_ok(S):
    """N4: the registrations and the rules re-read after Components 1-3, each unchanged byte for byte since its commit and touched by one commit;
    nothing computed for the three rows (no such bank, no computation tool run); the re-read bank tracked."""
    j = S['regs_rereadj']
    rows = j.get('rows') or {}
    return j.get('unchanged') is True and sorted(rows) == ['data/b710_registrations.txt', 'data/b710_rules.txt'] \
        and all(v.get('unchanged') is True and v.get('commits') == [K.REG_COMMIT[:8]] for v in rows.values()) \
        and j.get('nothing_computed') is True and j.get('computed_banks') == [] and j.get('compute_runs') == [] and S['computed_banks'] == [] \
        and 'NOTHING COMPUTED FOR THE THREE ROWS True' in unwrap(S['regs_reread']) and S['tracked']('data/b710_registrations_reread.txt')


def fit_ok(S):
    """(R320)(6)(i), N4: the fitted constants and the two predictions printed in the registration equal to the fit bank's and to this suite's own
    least squares over data/b709_pairs.txt's ten computed rows (tools/b710_fit.py's reader and solver, imported); the fit bank in the step-zero
    commit, before Component 1's."""
    import b710_fit as F
    R = F.rows()
    comp = [x for x in R if x['nstar']]
    far = dict((x['idx'], x) for x in R if not x['nstar'])
    if len(comp) != 10 or sorted(far) != [11, 15]:
        return False
    import math
    xs = [math.log(x['nstar'] + 1) for x in comp]
    a2, b2 = F.lsq(xs, [x['r'] * x['nstar'] for x in comp])
    p11 = F.solve(a2, b2, far[11]['r'], 108.573953341369431556137 / far[11]['r'])
    p15 = F.solve(a2, b2, far[15]['r'], 108.573953341369431556137 / far[15]['r'])
    r = unwrap(S['regs'])
    return ('alpha = %.6f, beta = %.6f' % (a2, b2)) in r and ('F2 n* = %d' % round(p11)) in r and ('F2 n* = %d' % round(p15)) in r \
        and ('F2 alpha %.4f beta %.4f' % (a2, b2)) in unwrap(S['fit']) and 'data/b710_fit.txt' in S['files']['stepzero']


def route_terms_ok(S):
    """(R320)(6)(i): the citation check's miss entered by the fact clause in the registration -- the route's own equation by line (the remainder
    bound, the constant 1/4, the rate log(R/s)), the route's call read in tools/b675_li_bench.py as the registration quotes it."""
    r = unwrap(S['regs'])
    lb = read(os.path.join(T, 'b675_li_bench.py'))
    return 'REMAINDER BOUND C (n + 1)^2 s^n' in r and 'the constant 1/4 for every pair' in r and 'log(R/s)' in r \
        and 'onset(arb(2), R, arb(1) / 4, Cc, s)' in r and 'onset(arb(2), R, arb(1) / 4, Cc, s)' in lb


# ================================================================== (R320)(3): THE NEEDLES, THE LOCK GATE AND THE TEST
REPORT709_KEYS = ('ONSET', 'ZETA', 'RATIO', 'MODULES', 'FIGURES')
AXIS709_QUOTE = '(e) representation coordinates (the operator / Toeplitz form) -- 4'


def needles_repaired_ok(S):
    """(R320)(3): the two needles repaired -- b709's report bank failing the old key reading and passing keys_ci, b709's registrations bank failing the
    one-string quotation and passing it joined -- and the controls' eight needle cases as wanted."""
    rep, reg = S['report709'], S['regs709']
    cases = [c for c in S['repair_ctlj'].get('cases') or [] if c['case'][:3] in ('(1)', '(2)')]
    return bool(rep) and bool(reg) and not all(k in rep for k in REPORT709_KEYS) and keys_ci(rep, REPORT709_KEYS) \
        and AXIS709_QUOTE not in reg and AXIS709_QUOTE in joined(reg) and len(cases) == 8 and all(c['as_wanted'] for c in cases)


def lockgate_required_ok(S):
    """(R320)(3): the lock gate's act argument required -- the refusal before any record or write in its main, the default b378 gone -- its five
    controls as wanted (two NEG calls writing nothing, the POS call refusing at the face, relay data/ unchanged, b378's bank equal to HEAD), and
    b378's tracked bank equal to HEAD now."""
    s = S['lockgate_src']
    i, j = s.find('if not argv or not argv[0].strip():'), s.find("    act = argv[0]\n")
    cases = [c for c in S['repair_ctlj'].get('cases') or [] if c['case'].startswith('(3)')]
    return 0 < i < j and "argv[0] if argv else 'b378'" not in s and len(cases) == 5 and all(c['as_wanted'] for c in cases) \
        and gs(ROOT, 'diff', 'HEAD', '--', 'data/b378_lockgate.json') == ''


def lean_test_banked_ok(S):
    """(R320)(3), N1: the test that ran lean reads lean's banked prints -- no call of the reader's lean route in its text, the refusal in place, both
    prints banked byte for byte (their blobs those of b709's run's outputs) -- passing 7 of 7 at step zero; no command of the seat runs lean."""
    t = S['lean_test_src']
    tl = next((l for l in S['testst'].split(NL) if l.strip().startswith('test_elab_reader_b634.py')), '')
    return 'EL.call(' not in t and 'EL.call = _refuse' in t and 'b710_elab_reader_print.txt' in t and 'b710_elab_reader_print_sec.txt' in t \
        and blob_id(S['elab_prints'][0].encode('utf-8')).startswith('55277c74') and blob_id(S['elab_prints'][1].encode('utf-8')).startswith('ef99e5c3') \
        and 'exit 0' in tl and '7 of 7 cases as wanted -- PASS' in tl and no_local_lean(S)


def no_dispatch_ok(S):
    """N1's second clause, (R320)(7): no runner dispatch this act -- no dispatch bank rows, none in the command capture."""
    return not (S['dispj710'].get('rows') or []) and (S['cmdj'].get('dispatches') or []) == [] and bool(S['cmds'])


# ================================================================== (R320)(4): THE STANDING CLAUSES BY VERSION
def standing_v1_ok(S):
    """(R320)(4), N3: data/standing_clauses_v1.txt -- VERSION 1, its rows numbered and tagged, read back by its own parser; the three lines of
    (R319)'s ferry (data/b709_ferry.txt :49, :43, :45) re-assembled from it equal line for line, recomputed here; its control banked as wanted;
    the bank in Component 2's commit."""
    import collections
    import b710_standing as SC
    b = S['standing_bank']
    rows = SC.parse(b)
    ra = SC.reassemble(b)
    f = S['ferry709'].split(NL)
    kinds = collections.Counter(r[1] for r in rows)
    return bool(re.search(r'^VERSION: 1$', b, re.M)) and len(rows) == 51 and [r[0] for r in rows] == list(range(1, 52)) and dict(kinds) == {'STANDING': 42, 'ACT': 7, 'HEAD': 2} \
        and all(r[3] for r in rows) and all(ra.get(n) == f[n - 1] for n in (49, 43, 45)) and S['standing_ctlj'].get('ok') is True \
        and 'EQUAL LINE FOR LINE True' in S['standing_ctl'] and STANDING_BANK in S['files']['c2']


def standing_readers_ok(S):
    """(R320)(4), N3: the readers of the ferry's text read the bank by version -- the ferry scan's bank citation reader, the citation tool's
    standing rows, and this suite's receipt arm -- their controls banked as wanted."""
    return S['standing_readersj'].get('ok') is True and 'def bank_citation_check' in S['ferry_scan_src'] and 'STANDING CLAUSES BANK CITATION' in S['ferry_scan_src'] \
        and 'def standing_rows' in read(os.path.join(T, 'b710_citation.py')) and 'def receipt_ok' in S['suite'] and 'tools/ferry_scan.py' in S['files']['c2']


def receipt_ok(S):
    """the banked ferry received in full, its ruling's end and the ferry's tail; repointed by version ((R320)(4)): every "standing clauses v<N>" the
    ferry names outside a quotation read against data/standing_clauses_v<N>.txt, present at its VERSION line (this act's ferry names v1 inside a
    quotation alone, the form from b711), and v1's re-assembly control as wanted."""
    f = S['ferry']
    named = sorted(set(int(m.group(1)) for m in re.finditer(r'standing clauses v(\d+)', re.sub(r'“[^”]*”', '', ' '.join(f.split())), re.I)))
    have = all(re.search(r'^VERSION: %d$' % v, read(os.path.join(D, 'standing_clauses_v%d.txt' % v)) or '', re.M) for v in named)
    return 'RULING (R320) END' in f and f.rstrip().endswith(K.TAIL) and have and S['standing_ctlj'].get('ok') is True


# ================================================================== (R320)(5): READING 5
def reading5_ok(S):
    """(R320)(5): data/b710_reading5.txt in four sections with its verdict, each route bank present with its verdict line; in Component 3's commit."""
    r = S['r5']
    return all(h in r for h in ('## (i) THE FOUR PRINCIPLES', '## (ii) THE MOVES-BY-LOCUS TABLE', '## (iii) THE READFIRST FLIP', '## (iv) THE COST READING')) \
        and '### ### **READING 5:' in r and all(re.search(r'^### ### \*\*', S['r5banks'][n], re.M) for n in S['r5banks']) \
        and all(('data/b710_r5_%s.txt' % n) in S['files']['c3'] for n in S['r5banks']) and 'data/b710_reading5.txt' in S['files']['c3']


def principles_ok(S):
    """N2: each principle's row cites its papers by path and line, its terminals by kernel, tag and name with the grade read, and its control by bank
    or "NONE LOCATED" with its search printed; the counts line; the terminals bank's twenty statements read."""
    r = S['r5']
    blocks = re.split(r'^  \((S|I|D|E)\) ', r[r.find('## (i)'):r.find('## (ii)')], flags=re.M)
    rows = dict(zip(blocks[1::2], blocks[2::2]))
    ok = sorted(rows) == ['D', 'E', 'I', 'S']
    for k, b in rows.items():
        ok = ok and re.search(r'STATED: .*\.md :\d+', b) is not None and re.search(r'COMPILED: .*SIDE-[a-z-]+ v\d', b) is not None \
            and ('CONTROL: LOCATED' in b or ('CONTROL: NONE LOCATED. The search' in b and 'data/b710_r5_controls.txt' in b))
    tj = S['r5j']['terminals'].get('rows') or []
    return ok and len(tj) == 20 and all(x.get('statement') for x in tj) and 'with a compiled theorem consuming the principle' in unwrap(r) \
        and '3 of 4' in unwrap(r) and 'with a control object 1 of 4' in unwrap(r)


MOVE_ROWS = ('(1)', '(2)', '(3)', '(4)', '(5)', '(6)', '(a)', '(b)', '(c)', '(d)', '(e)', '(f)')


def moves_ok(S):
    """(R320)(5)(ii): the table's twelve rows each with its ledger lines and its reading, the counts; raised as one prompt (the answers bank) and
    entered on the author's word as W-ORD-MOVES-BY-LOCUS at OPEN_TRAILS :15804 (the landing bank's line, the head through conv), INSTRUMENTS.md
    untouched; in Component 3's PLACE-papers commit."""
    r = S['r5']
    sec = r[r.find('## (ii)'):r.find('## (iii)')]
    rows = [m.group(1) for m in re.finditer(r'^  (\([1-6a-f]\)) ', sec, re.M)]
    words = re.compile(r'\| (MOVED|NARROWED|RE-PRESENTED|REAPPEARED)')
    ls = S['movesj'].get('lines') or []
    ln = ls[0].get('line') if ls else None
    line = oline(S, ln) if ln else ''
    return tuple(rows) == MOVE_ROWS and len(words.findall(unwrap(sec))) >= 12 and 'tried at the clause 11 ; untried 1' in unwrap(sec) \
        and 'MOVED 1' in sec and 'NARROWED 4' in sec and 'RE-PRESENTED 2' in sec and 'REAPPEARED 5' in sec \
        and ln == K.ORDER_MOVES and line == conv(ls[0].get('head') or '\x00') and 'W-ORD-MOVES-BY-LOCUS' in line and 'INSTRUMENTS.md is untouched' in line \
        and 'enter in OPEN_TRAILS' in S['answers'] and 'OPEN_TRAILS.md' in S['files']['c3pp']


def flip_ok(S):
    """(R320)(5)(iii): the defects b700-b709 by class, every one classed; the closure's catch and the flip's risk counted by hand; the recommendation."""
    t = (S['r5j']['flip'].get('totals') or {})
    c = S['r5j']['flip'].get('classes') or {}
    return t.get('defects') == 101 and t.get('caught') == 0 and t.get('risked') == 0 and 'UNCLASSED' not in c and sum(c.values()) == 101 \
        and 'DO NOT FLIP' in S['r5']


def cost_ok(S):
    """(R320)(5)(iv): the read volume by file from the read banks b705-b709, the top three printed, the carried tools' share."""
    j = S['r5j']['cost']
    return j.get('calls') == 1131 and j.get('volume') == 101249 and j.get('carried_volume') == 48626 and [x[0] for x in (j.get('top') or [])[:3]] == [
        'relay/tools/b706_checks.py', 'relay/tools/b707_record.py', 'relay/tools/b706_record.py'] and '48.0%' in S['r5']


def carry_spans_ok(S):
    """b709's row (1) as the banks read it: each carried tool with its carry bank (the substitution diff and the spans b709's banks name) and a row in
    the spans bank, tracked."""
    rows = re.findall(r'^  tools/b710_(\w+)\.py \| spans (\d+) \| substitution hunks (\d+) \|', S['spans'], re.M)
    return sorted(r[0] for r in rows) == sorted(CARRIED_NAMES) and all(bool(S['carry_banks'][n]) and ('CARRIED tools/b710_%s.py' % n) in S['carry_banks'][n] for n in CARRIED_NAMES) \
        and S['tracked']('data/b710_carry_spans.txt')


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry, repointed to read the standing clauses by version ((R320)(4)): each version the ferry names read against its bank, v1`s control as wanted',
     lambda S: receipt_ok(S), lambda S: put(S, 'ferry', S['ferry'].replace(K.TAIL, ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the step-zero bank: tail, lean, lake, python and claude named, the seat`s claude alone, none of the others; no task stopped, no orphan, nothing stopped by PID',
     lambda S: procs_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('python 0', 'python 1'))),
    ('G-STEPZERO-TESTS', 'the tests bank against the test files tracked before the act, every one run (the lean-running test repaired before the run, reading banked prints, (R320)(3)), run against the list the page names, the eight not clean named (three carried, five the renames` readers)',
     lambda S: tests_ok(S), lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: S['pushout'][0] == ['data/b709_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'relay`s and PLACE-papers` branch lists by the ruling`s six names, and the branches bank with port-b707 standing',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{'D:/relay': 'push-b709'}))),
    ('G-READFIRST-CITED', 'the read-first bank: every item of the ferry`s list cited by path and line', lambda S: readfirst_ok(S),
     lambda S: put(S, 'readfirst', '')),
    ('G-ANSWERS-BANKED', 'the answers bank read at HEAD: its prompts and calls at or above the sealed floors (none before the root), each with its options and result, any call after the lock named on the face',
     lambda S: answers_ok(S), lambda S: put(S, 'answers', re.sub(r'(?m)^(### b710 -- THE AUTHOR`S ANSWERS, )(\d+)', lambda m: m.group(1) + str(int(m.group(2)) + 1),
                                                                 S['answers']))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-EXPORT-UNTRACKED', 'the navigator`s export: present, untracked, in no commit', lambda S: S['export_present'] and S['export_log'] == ''
     and S['export_index'] == '' and S['export_status'].startswith('??'), lambda S: put(S, 'export_index', EXPORT)),
    ('G-EDIT-ROUTE', 'the record tool`s one reading (tools/edit_route.py`s arms and sed in any form) over this act`s whole capture and the previous act`s after its post-push suite (b709`s own session, b701`s form), read live',
     lambda S: edit_route_ok(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -n 1p tools/b710_record.py")])),
    ('G-NO-LOCAL-LEAN', 'the act`s command capture, read live: no command of the seat runs lean or lake on this host (the repaired test runs none, (R320)(3), N1)', lambda S: no_local_lean(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd='lake env lean ChainProbe.lean')])),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s lines, found by conv: b709`s weight line and the readings line beside it', lambda S: weight_ok(S), lambda S: _rl(S, 0, 1)),
    # ### ACT ARMS (Component 5)
    ('G-DRY-STEP-CLEAN', 'the gate`s record: the dry-run step CLEAN, the trail`s Defects and Resolved lines equal to the bank, the gate CLEAR',
     lambda S: dry_step_ok(S), lambda S: put(S, 'gate', '')),
    ('G-CLOSING-DRY-STEP', 'the gate`s record: the closing tool run dry before the lock, its sections read (the repairs, the standing clauses, reading 5, the moves, the registrations, the standing arms, the kernels), its needle as b709 repaired it (the banks carrying no verdict line by their form exempt by name)',
     lambda S: closing_dry_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE CLOSING DRY-RUN STEP : CLEAN', 'THE CLOSING DRY-RUN STEP : NOT CLEAN'))),
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, the two misses entered by the fact clause ("rising with height", the route`s terms), the bank before the step-zero commit and that before Component 1`s',
     lambda S: citation_ok(S), lambda S: put(S, 'citation', '')),
    ('G-R320-ENTERED', 'the trail record`s ratification line', lambda S: '**(R320) ratified.**' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**(R320) ratified.**', '**(R320) read.**'))),
    ('G-ROWGEN-STEPZERO', 'the rowgen bank`s verdict line (the roster re-pointed, 8)', lambda S: rowgen_ok(S), lambda S: put(S, 'rowgen', '')),
    ('G-BRANCHES-BANKED', 'the branches bank through the record tool`s reader: six named, deleted, merged, banked before the first delete and after the citation check; port-b707 kept at b709`s commit locally and at the remote at step zero',
     lambda S: branches_banked_ok(S), lambda S: _mut(S, 'branchj', lambda d: d['rows'].pop())),
    ('G-DELETES-ONE-BRANCH', 'the command bank: every branch delete one branch (the six of (R320)(7) alone, port-b707 never), no glob, no variable, nothing chained after',
     lambda S: deletes_one_ok(S), lambda S: put(S, 'cmdt', '')),
    ('G-LISTINGS-BEFORE-CLAUSES', 'N3: the `--merged` listing in the capture before the first delete; every branch deleted among those banked before any delete; the step-zero bank`s listings row',
     lambda S: listings_before_ok(S), lambda S: put(S, 'first_listing_ts', 10 ** 12)),
    ('G-ANSWERS-CHECKED', 'the citation bank`s mid-act prints: the moves table`s answer checked before the lock, the root prompt`s check after it, each with its time',
     lambda S: answers_checked_ok(S), lambda S: put(S, 'citation', '')),
    ('G-ANSWERS-BEFORE-WRITES', 'the citation bank`s check stamps: the one mid-act answer checked before the OPEN_TRAILS record it governs and before the lock, every other after the lock; the answers bank carrying the prompt',
     lambda S: answers_before_ok(S), lambda S: put(S, 'answers', S['answers'] + NL + '### PROMPT 9 (planted)')),
    ('G-SCORER-READS-BANKS', 'the record tool`s scorers: banks alone, no ledger line (data/b686_rules.txt row (1))', lambda S: scorer_banks_ok(S),
     lambda S: put(S, 'rec_src', '')),
    ('G-ENTRY-SCORES-EQUAL', 'the landed entry`s scores line against the scores bank', lambda S: entry_scores_ok(S), lambda S: put(S, 'sc', {})),
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title: by its objects in the ferry`s form adjusted to what the act did (reading 5`s principles with their counts of compiled terminals and control objects, the moves table entered, the standing clauses at v1, the registrations for b711), compared after case-folding the article alone',
     lambda S: entry_title_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-CORRIGENDUM-ENTERED', 'the generated corrigendum for b709`s two post-seal needles (an unlettered event), landed; no lettered defect and no trail arm at b709; the corrigenda bank appended at row (30)',
     lambda S: corrigendum_ok(S), lambda S: put(S, 'corrj', {})),
    ('G-WRITELIST-MIRROR-STATE', '(R320)(8): the face`s (W) row for the mirror builder naming tools/mirror_prevbuild.json beside the zip and its stage; the record tool`s N5 reading it as the builder`s',
     lambda S: writelist_mirror_state_ok(S), lambda S: put(S, 'face', S['face'].replace('tools/mirror_prevbuild.json', 'tools/mirror_x.json'))),
    ('G-RULES-ROW-ENTERED', '(R320)(3)-(4): data/b710_rules.txt rows (1) the standing clauses by version and (2) the lock gate`s argument required, committed alone with the registrations; b709`s carry row and b708`s report row binding, the worklist`s SEALED naming no report tool',
     lambda S: rules_row_ok(S), lambda S: put(S, 'rules', '')),
    ('G-REPORT-UNSEALED', 'the report bank by the unsealed tool after the root`s word and before the root: its stamp after the lock and at or before the root`s, the ferry`s five lines, its keys read case-insensitively ((R320)(3)), the tool unsealed',
     lambda S: report_unsealed_ok(S), lambda S: put(S, 'report', '')),
    ('G-GUARD-HELD', 'the suite`s writer block guarded by `if PRERUN:` and its dry run banked', lambda S: guard_ok(S), lambda S: put(S, 'guard', '')),
    ('G-POSTROOT-WRITES-NONE', 'the per-part seconds banks` commit times against the root`s', lambda S: postroot_writes_none(S), lambda S: put(S, 'guard', '')),
    ('G-TRAIL-LINES-EQUAL-DEFECTS', 'the landed trail`s Defects and Resolved lines against the defects bank`s owners', lambda S: trail_lines_equal_defects(S),
     lambda S: put(S, 'defects', '')),
    ('G-TRAIL-DEFECTS-EQUAL', 'the gate`s record and the landed trail`s Defects line against the repaired reader`s rows', lambda S: trail_defects_ok(S),
     lambda S: put(S, 'gate', '')),
    ('G-TRAIL-RESOLVED-EQUAL', 'the gate`s record and the landed trail`s Resolved line against the bank`s owners', lambda S: trail_resolved_ok(S),
     lambda S: put(S, 'gate', '')),
    ('G-DEFECTS-LETTERED', 'the defects bank: the sealed floors` rows with their owners in order, every one the seat`s',
     lambda S: defects_ok(S), lambda S: put(S, 'defects', '')),
    ('G-TOOL-REPAIRS', 'the repairs bank (the four repairs of (R320)(3) with their diffs, the carried tools` repairdiff banks) and the controls (16 cases as wanted, relay data/ unchanged by the lock gate`s NEG calls)',
     lambda S: repairs_ok(S), lambda S: put(S, 'repairs', '')),
    ('G-ROOTDRY-READY', 'data/b706_rules.txt row (1): the root route run dry on the pre-root tree before the lock, READY True, printed in the face`s (0)',
     lambda S: rootdry_ok(S), lambda S: _mut(S, 'rootdryj', lambda d: d.update(ready=False))),
    ('G-FIGURES-BANKED', 'the four standing figures banked by b706`s tool over b706`s roster against b709`s baselines, each at or below b709`s, the partners figure 0 with one copy per table',
     lambda S: figures_banked_ok(S), lambda S: put(S, 'figj', {})),
    ('G-READFIRST-DIFF-BANKED', 'the closure reader`s diff banked; the readfirst bank unchanged since the step-zero commit', lambda S: readfirst_diff_ok(S),
     lambda S: put(S, 'rf_diff', '')),
    ('G-REGISTRATIONS-ALONE', '(R320)(6), N4: data/b710_registrations.txt (the refined law, the surgery, the coefficient observation) committed alone with the rules bank at step zero before the step-zero banks` and Component 1`s commits, the one commit touching it, its blob unchanged at HEAD and in the working tree',
     lambda S: registrations_alone_ok(S), lambda S: put(S, 'regs_blob_now', '0' * 40)),
    ('G-REGISTRATIONS-REREAD', 'N4: the registrations and the rules re-read after Components 1-3, unchanged since their commit, nothing computed for the three rows (no such bank, no computation tool run), banked',
     lambda S: registrations_reread_ok(S), lambda S: _mut(S, 'regs_rereadj', lambda d: d.update(unchanged=False))),
    ('G-FIT-BANKED', '(R320)(6)(i), N4: the fitted constants and the predictions for pairs 11 and 15 printed in the registration, equal to the fit bank`s and to this suite`s own least squares over b709`s ten computed pairs; the fit bank in the step-zero commit',
     lambda S: fit_ok(S), lambda S: put(S, 'regs', S['regs'].replace('F2 n* = 12294837', 'F2 n* = 12294838'))),
    ('G-ROUTE-TERMS-REGISTERED', '(R320)(6)(i): the citation check`s miss by the fact clause -- the route`s own equation in the registration by line, its call read in b675`s route as quoted',
     lambda S: route_terms_ok(S), lambda S: put(S, 'regs', S['regs'].replace('REMAINDER BOUND', 'MAIN TERM'))),
    ('G-NEEDLES-REPAIRED', '(R320)(3): the two needles repaired -- b709`s report failing the old key reading and passing keys_ci, b709`s registrations bank failing the one-string quotation and passing it joined -- the eight needle controls as wanted',
     lambda S: needles_repaired_ok(S), lambda S: put(S, 'report709', re.sub('(?i)ratio', 'quotient', S['report709']))),
    ('G-LOCKGATE-ARG-REQUIRED', '(R320)(3): the lock gate`s act argument required before any record or write, the b378 default gone, its five controls as wanted, b378`s tracked bank equal to HEAD',
     lambda S: lockgate_required_ok(S), lambda S: put(S, 'lockgate_src', S['lockgate_src'].replace('    act = argv[0]\n', "    act = argv[0] if argv else 'b378'\n"))),
    ('G-LEAN-TEST-BANKED', '(R320)(3), N1: the test that ran lean reads lean`s banked prints, no call of the reader`s lean route, the prints byte for byte, 7 of 7 at step zero, no command of the seat running lean',
     lambda S: lean_test_banked_ok(S), lambda S: put(S, 'lean_test_src', S['lean_test_src'] + NL + "EL.call('x', [], 'y')")),
    ('G-NO-DISPATCH', 'N1`s second clause, (R320)(7): no runner dispatch this act -- no dispatch bank rows, none in the command capture',
     lambda S: no_dispatch_ok(S), lambda S: put(S, 'dispj710', dict(rows=[dict(run_id=1)]))),
    ('G-STANDING-CLAUSES-V1', '(R320)(4), N3: the standing clauses bank at VERSION 1, 51 rows numbered and tagged, read back by its parser, (R319)`s three lines re-assembled from it equal line for line here, its control as wanted, in Component 2`s commit',
     lambda S: standing_v1_ok(S), lambda S: put(S, 'standing_bank', S['standing_bank'].replace('and no pipe in any command', 'and no pipe in a command', 1))),
    ('G-STANDING-READERS', '(R320)(4), N3: the readers of the ferry`s text reading the bank by version -- the ferry scan, the citation tool, this suite`s receipt arm -- their controls as wanted',
     lambda S: standing_readers_ok(S), lambda S: _mut(S, 'standing_readersj', lambda d: d.update(ok=False))),
    ('G-READING5-BANKED', '(R320)(5): the reading bank in four sections with its verdict, its six route banks each with a verdict line, in Component 3`s commit',
     lambda S: reading5_ok(S), lambda S: put(S, 'r5', S['r5'].replace('## (iii) THE READFIRST FLIP', '## (iii) THE FLIP'))),
    ('G-PRINCIPLES-ROWS', 'N2: each principle`s row with its papers by path and line, its terminals by kernel, tag and name with the grade read, its control by bank or none located with the search printed; the counts; twenty statements read',
     lambda S: principles_ok(S), lambda S: put(S, 'r5', S['r5'].replace('CONTROL: NONE LOCATED. The search', 'CONTROL: NONE LOCATED.', 1))),
    ('G-MOVES-ENTERED', '(R320)(5)(ii): the twelve rows with their readings and counts; the prompt in the answers bank; entered on the author`s word as W-ORD-MOVES-BY-LOCUS at OPEN_TRAILS :15804, INSTRUMENTS.md untouched, in Component 3`s PLACE-papers commit',
     lambda S: moves_ok(S), lambda S: _mut(S, 'movesj', lambda d: d.update(lines=[dict(d['lines'][0], line=1)]))),
    ('G-FLIP-READ', '(R320)(5)(iii): the 101 defects b700-b709 every one classed, the closure`s catch 0 and the flip`s risk 0 by hand, the recommendation',
     lambda S: flip_ok(S), lambda S: _mut(S, 'r5j', lambda d: d['flip']['totals'].update(caught=1))),
    ('G-COST-READ', '(R320)(5)(iv): the read banks b705-b709 by file -- 1131 calls, 101249 lines, 48626 on carried tools -- the top three',
     lambda S: cost_ok(S), lambda S: _mut(S, 'r5j', lambda d: d['cost'].update(calls=1))),
    ('G-CARRY-SPANS', 'b709`s row (1): each carried tool with its carry bank and its row in the spans bank, tracked',
     lambda S: carry_spans_ok(S), lambda S: put(S, 'spans', '')),
    ('G-PARTS-PRERUN', 'the pre-run bank: seven parts, each named with its arms and seconds, the longest under the 590 s guard', lambda S: parts_prerun_ok(S),
     lambda S: put(S, 'prerun', '')),
    ('G-ARM-SECONDS-BANKED', 'the per-part seconds bank gathered before the seal', lambda S: arm_seconds_ok(S), lambda S: put(S, 'asec', {})),
    ('G-SPEC-PLANTED', 'tools/b710_regspec.py`s planted rows run live through the record tool`s readers, and rows of another shape refused',
     lambda S: bool(S['spec']['read']) and all(S['spec']['read']) and all(S['spec']['controls']) and any('runner' in x for x in S['spec']['shapes']),
     lambda S: _mut(S, 'spec', lambda d: d['controls'].append(False))),
    ('G-CONVERSION-ONE', 'every b710 tool`s code: no conversion defined (conv imported from b652_record); the suite importing it',
     lambda S: S['conv_bad'] == [] and 'from b710_record import conv' in S['suite'], lambda S: put(S, 'conv_bad', ['b710_checks.py'])),
    ('G-WORKFLOW-FILES', 'b709`s one run`s workflow, read as banked (no dispatch this act): build-module.yml at port-b707`s tip b707`s blob unchanged, no author identifier, no secret, the hold, the lakefile and its cache step; the print list absent at the branch so the print step is read as not run and no grade claimed (b709`s dispatch row, `whole` False by that reading); b709`s one write on the branch the one module',
     lambda S: wf_ok(S), lambda S: _mut(S, 'wf', lambda d: d[K.KERNEL].update(text=d[K.KERNEL]['text'] + ' secrets.X'))),
    ('G-RUNNER-READ', 'b709`s one run (port-b707 at its tip) as banked, through the record tool`s reader: at the tip, its conclusion failure, the artifact`s sha256 the port bank`s, the memory low above the hold, no STOP line, the gate NOT DERIVES with no grade claimed, build exit 1 with its 8 error lines',
     lambda S: runner_ok(S), lambda S: _mut(S, 'runner_rows', lambda d: d.update(rows=[dict(r, gate='DERIVES') for r in (d.get('rows') or [])]))),
    ('G-RUNNER-GATE', 'the run`s text bank: the artifact`s digest agreeing, build exit 1, no grade claimed',
     lambda S: gate_ok(S), lambda S: put(S, 'runs', {PORT_LABEL: ''})),
    ('G-MERGES-ON-GATE', 'no merge this act: SIDE-explicit-formula`s main at badaccc with its tags unmoved; SIDE-lv-conservation`s main and deposit unmoved, port-b707 at b709`s one commit locally and at the remote and not on main, no tag; the join kernel`s main at its manifest commit, no tag',
     lambda S: merges_ok(S), lambda S: put(S, 'ef_log', S['ef_log'] + ['deadbeef'])),
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
    ('G-PP-SCOPE', 'PLACE-papers` changed files against the two ledgers alone (no document cut this act); no rename (N5)',
     lambda S: corpus_scope_ok(S), lambda S: put(S, 'pp_changed', S['pp_changed'] + ['day1/ONE_PAGE_PROOF.md'])),
    ('G-CURRENTS-UNEDITED', 'the map, the census, the monograph, the Dirichlet page, the surround, SIMPLICITY, FOUNDATIONS, INSTRUMENTS, PATHS, the substrate pages, the companions, the README, the faces page, REGISTRY and the archives, each at its file of record: working tree, before and HEAD',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'ERRATA.md': (b'x', b'y', b'y')}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read before the seal (SIDE-lv-conservation read with port-b707 at b709`s one commit and its checkout at main)',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b709`s to b695`s sealed tools and the earlier tools, the readers, the push tool, the act-root tool, the generators` tests, the corrigendum tools, edit_route.py, chain_page.py, the figures tools, b704`s read arm, e0_rule.py, the shared tools and b709`s report tool: before, working tree and HEAD',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'additive_shared.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 42dd8768 but the shared additive files (act_roots.txt and the corrigenda bank among them) and the table`s files, by blob id',
     lambda S: S['prior_bad'] == [] and S['prior_n'] > 0, lambda S: put(S, 'prior_bad', ['data/b709_stepzero.txt'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS before and now', lambda S: S['fi_pre'] is not None and (S['fi_now'] or b'').startswith(S['fi_pre']),
     lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS before and now', lambda S: S['ot_pre'] is not None and (S['ot_now'] or b'').startswith(S['ot_pre']),
     lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-NODISCLOSURE-PUBLIC', 'TECHNE-Core`s needle sets over every public byte the act writes: the ledger lines, the banks, the tools, and b709`s workflow and module at the port branch`s tip beside them',
     lambda S: bool(S['nd_pub']) and not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', {'method': 1})),
    ('G-OUTSIDE-NAMED-NOWHERE', 'the ledger lines appended', lambda S: S['outside'] == [], lambda S: put(S, 'outside', ['x'])),
    ('G-DELETE-FREE', 'the act`s tools` code, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='os' + '.remove(p)'))),
    ('G-PUBLISH-UNCALLED', 'the act`s tools` code: no publish call', lambda S: publish_uncalled(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='z_' + 'publish()'))),
    ('G-SEALED-AFTER-COMPONENTS', 'the lock time against every relay and PLACE-papers commit of the act by its subject', lambda S: sealed_after_ok(S),
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b710 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'b710_closing.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3), in seven parts summed',
     lambda S: S['lock_epoch'] is not None and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b709`s trail record on OPEN_TRAILS and its root in the chain', lambda S: K.B709_TRAIL_HEAD in S['ot']
     and S['rootsf'].count(NL + 'b709 ') == 1, lambda S: put(S, 'ot', S['ot'].replace('### b709 — lane two', '### b709 - lane two'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], grade_moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 87th chain row (the corrigendum row apart), the root bank and its items against the root route`s own item list (ROOT_EXCLUDE per data/b706_rules.txt row (1), the required list read against it at import), reading 5 and its route banks, the standing control and readers, the fit, the registrations, the repairs, the corrigendum and the report among them, no bank the route excludes',
     lambda S: root_banked_ok(S), lambda S: put(S, 'rootsf', S['rootsf'] + 'b710 x y' + NL)),
    ('G-ROOT-BANKS-COMMITTED', 'the root route`s banked reading and every named bank`s blob at the root`s recorded commit: clean and equal at HEAD, HEAD the remote main, the recorded hash carried by the recorded commit',
     lambda S: root_banks_committed_ok(S), lambda S: put(S, 'rootbanks', dict(S['rootbanks'], pushed=False))),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit in three parts by act with the suite`s own remote reads: standing-b2a`s banked b624-b641, standing-b2b`s b642-b658 and standing-b3`s b659-b710 all AGREE, the boundary link equal, b680 read through its corrigendum row (4 banks), b710 written LF',
     lambda S: verify_ok(S), lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s through conv, and its parts, the repairs, the standing clauses, the principles, the moves table, the flip, the cost and the registrations among them', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line, the head through conv', lambda S: bool(S['tj'].get('line'))
     and oline(S, S['tj']['line']) == conv(S['REC'].TRAIL_HEAD()), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b710 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b710_record.py agree', 'b710_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line: b711', lambda S: '**Next:** b711' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** b711', '**Next:** b712'))),
] + [('G-N%d-SCORED' % i, 'the scores through the record tool`s reader, and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i),
      lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written since 42dd8768 and 07978f3 against the (W) globs, the list admitting the next act`s rules file by form',
     lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b710')" in S['suite'] and "'data/b710_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b710_closing.py: the closing sentence in the rule`s words with the plain reads named; the citation check, the record lines, the dry run, the repairs, the standing clauses, reading 5, the moves, the registrations, the standing arms, the kernels, the mirror, the carry-time reading',
     lambda S: closing_sentence_ok(S), lambda S: put(S, 'closing_src', S['closing_src'].replace('no identifier of the author ' + 'in any outbound', 'x'))),
    ('G-LSREMOTE-ONE-PER-REPO', 'the part`s ls-remote calls per repository, read after every other arm of the part has run (OPEN_TRAILS :12703)',
     lambda S: lsr_ok(S), lambda S: put(S, 'lsr', {PP: 2})),
    ('G-CORRESPONDENCE-CURRENCY', 'every roster paper`s Correspondence rows by tools/b706_standing_figures.py (b703`s reading over b706`s roster at the unversioned names) against the kernel`s current tag and the statement at the cited tag: the changed-statement rows no more than b709`s figure',
     lambda S: fig_ok(S, 'correspondence'), lambda S: _raise_fig(S, 'correspondence')),
    ('G-README-CURRENCY', 'the PLACE-papers README`s currency rows against ls-remote by tools/b705_standing_figures.py through b706`s (the dated appends and the deposited versions excluded by their text): the stale lines no more than b709`s figure',
     lambda S: fig_ok(S, 'readme'), lambda S: _raise_fig(S, 'readme')),
    ('G-PARTNER-COPIES', 'the lines differing between the two copies of each roster paper`s Correspondence table by tools/b706_standing_figures.py: one copy per table from b706 on, the figure 0, no more than b709`s 0',
     lambda S: fig_ok(S, 'partners'), lambda S: _raise_fig(S, 'partners')),
    ('G-SISTER-PINS', 'each kernel`s lean-toolchain and Mathlib revision beside the federation`s by tools/b703_standing_figures.py through b706`s: no kernel the faces page names moved pin against the baseline',
     lambda S: sister_pins_ok(S), lambda S: _raise_fig(S, 'pins')),
    ('G-READ-RULE-STANDING', 'tools/b704_read_arm.py over the read bank at HEAD (the author`s word at b704`s sort; from b705 every call counts): no Read call of a file of two hundred lines or more without an offset, without a limit or with a limit above two hundred',
     lambda S: read_rule_standing_ok(S), lambda S: _read_plant(S)),
] + [(nm, 'tools/rule_arms.py (the author`s word on (R293)(6); (R301)(6) for four; G-RULE-SUITE-PARTS as repaired under (R302)(2) and (R320)(2); G-RULE-BINARY-HASHES as repaired under (R306)(2); G-RULE-RECUT-QUOTE`s sources as repaired under (R313)(2)) -- ' + reads,
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
    p = os.path.join(D, 'b710_seal_hashes.json')
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
    print('  written: b710_seal_hashes.json')
    return 0


def _base_name(pushed):
    if PRERUN:
        return 'b710_arms_prerun.txt'
    if MID and len(sys.argv) > sys.argv.index('--mid') + 1:
        return sys.argv[sys.argv.index('--mid') + 1]
    if RERUN and len(sys.argv) > sys.argv.index('--rerun-postpush') + 1:
        return sys.argv[sys.argv.index('--rerun-postpush') + 1]
    return 'b710_checks_postpush.txt' if pushed else 'b710_checks.txt'


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
    base = 'b710_arms_prerun.txt' if prerun else ('b710_checks_postpush.txt' if (rerun or pushed) else 'b710_checks.txt')
    out = [('data/' + _part_name(base, '<part>')), ('data/' + _part_name(base, '<part>').replace('b710_arms_prerun', 'b710_lsr_prerun').replace('b710_checks', 'b710_lsr').replace('.txt', '.json')),
           'data/b710_exercise_<part>.json']
    seconds = ['data/b710_arm_seconds_<part>.json'] if prerun else []
    return out, seconds


def guard_dry():
    for mode, args in (('prerun', (True, False, False, False)), ('pre-push', (False, False, False, False)), ('post-push', (False, True, False, True))):
        out, seconds = writer_plan(*args)
        print('  MODE %-9s | the part`s banks: %s | the per-part seconds bank: %s' % (mode, ', '.join(out), ', '.join(seconds) or 'NONE'))
    print('  ### POST-ROOT PATH WRITES NONE of the root-named per-part seconds banks: the pre-push and post-push modes write no data/b710_arm_seconds_<part>.json')
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
        ex.update(jl('b710_exercise_%s.json' % part).get('exercise') or {})
    if ex and base in ('b710_checks.txt', 'b710_checks_postpush.txt'):
        e = (json.dumps(dict(exercise=ex, run=n, live_failing=fails, defective=defs, neg_failures=ng), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p_ = os.path.join(D, 'b710_exercise.json')
        with open(p_ + '.tmp', 'wb') as fh:
            fh.write(e)
        os.replace(p_ + '.tmp', p_)
    print(NL.join(out[3:16]))
    print('  written: %s' % base)
    return 0 if ok else 1


# ### the carried failure declared on the face by name (section (G2)): G-READ-RULE-STANDING failing on defect (a)'s two whole reads before the
# ### ferry was banked (a memory file of 523 lines and data/b704_probe.json of 1152 lines; relay data/b710_read_calls.txt, OFFENCES 2); the
# ### combine reads it by name, and no other failure is carried.
CARRIED_FAILING = ('G-READ-RULE-STANDING',)


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
    rec('b710 -- THE SUITE. ### **%s READING.** ### PART %s ### every arm exercised on both controls.' % (
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
    rec('  ### (R264)(2) THE FREEZE: the standing arms (b709`s face less its own arms, the twenty-four rule arms and G-READ-RULE-STANDING among them; none added) %d ; '
        'carried here %d ; the act`s arms over its own banks %s ; arms beyond both %s' % (
            len(S['standing']), len(set(names) & set(S['standing'])), sorted(set(names) - set(S['standing'])),
            sorted(set(names) - set(S['standing']) - set(K.ACT_ARMS)) or 'NONE'))
    rec('  ### standing arms not carried here: %s' % (sorted(set(S['standing']) - set(names)) or 'NONE'))
    if 'figures' in NEED[PART]:
        rec('  ### THE FOUR STANDING FIGURES, each against the previous act`s (%s):' % S['fig_prev_name'])
        for k in ('correspondence', 'readme', 'partners', 'pins'):
            rec('  ###   %-15s live %s ; previous %s' % (k, (S['fig'].get(k) or {}).get('figure'), (S['fig_prev'].get(k) or {}).get('figure')))
        ok_, n_, off_, pre_, form_ = RDA.reading_text(S['reads_bank'])
        rec('  ### G-READ-RULE-STANDING`S READING (relay data/b710_read_calls.txt): %s ; rows %d ; offences %d %s ; the cap`s precursors %d' % (
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
            rec('  ### the reads at commit, b680: %s ; b710: %s' % (S['ar_reads'].get('b680'), S['ar_reads'].get('b710')))
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
    rec('  ### PLACE-papers` changed files %d against the allowed %d (the two ledgers; no document cut this act): beyond %s' % (
        len(S['pp_changed']), len(S['pp_allowed']), sorted(set(S['pp_changed']) - set(S['pp_allowed'])) or 'NONE'))
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b709`s one commit on %s, kept; b709`s port run %s, %s, %d of %d modules, read as banked) ; the join kernel main %s' % (
        S['ef_main'][:12], (S['ef_tags'].get('v0.37') or '')[:12], S['lv_main'][:12], (S['lv_v0100'] or '-')[:12], (S['lv_port'] or '-')[:12], K.PORT_BASE[:12],
        S['portj'].get('run_id') if S['portj'] else '-', (S['portj'].get('run') or {}).get('conclusion') if S['portj'] else '-', len(S['portj'].get('built') or []),
        len(S['portj'].get('modules') or []), (S['join_main'] or '-')[:12]))
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
    lp = os.path.join(D, _part_name(base, PART).replace('b710_arms_prerun', 'b710_lsr_prerun').replace('b710_checks', 'b710_lsr').replace('.txt', '.json'))
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    with open(lp + '.tmp', 'wb') as fh:
        fh.write(lb)
    os.replace(lp + '.tmp', lp)
    ex = dict(exercise=EX, run=len(arms), live_failing=fail, defective=defective, neg_failures=negfail, part=PART)
    ep = os.path.join(D, 'b710_exercise_%s.json' % PART)
    with open(ep + '.tmp', 'wb') as fh:
        fh.write((json.dumps(ex, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(ep + '.tmp', ep)
    # ### THE GUARD HELD -- the per-part seconds bank (root-named, gathered by the record tool's armsecs before the seal) is written by the pre-run
    # ### alone, as tools/b700_checks.py :1669 had it and b702 restored; the pre-push and post-push runs write no root-named bank
    if PRERUN:
        sp = os.path.join(D, 'b710_arm_seconds_%s.json' % PART)
        with open(sp + '.tmp', 'wb') as fh:
            fh.write((json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), part=PART, arms=SECS, phases=S['phase_secs'], run_secs=int(secs)),
                                 indent=1, ensure_ascii=False) + NL).encode('utf-8'))
        os.replace(sp + '.tmp', sp)
    print('  written: %s' % os.path.basename(out))
    carried_only = [f for f in fail if f not in CARRIED_FAILING] == [] and not defective and negfail == 0
    return 0 if (not fail and not defective and negfail == 0) else (4 if carried_only else 1)


if __name__ == '__main__':
    sys.exit(main())
