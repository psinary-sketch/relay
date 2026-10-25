# -*- coding: utf-8 -*-
"""b712_checks.py -- THE SUITE OF b712, UNDER (R322): b711 AT ITS WEIGHT; THE STANDING CLAUSES AT v2; THE INDEPENDENCE SUPPLEMENT; THE PORT AND
THE JOIN; THE SURGERY, THE COEFFICIENTS, THE AXIS; THE LIST TOWARD 443 AND PAIRS 11 AND 15; SEVEN PARTS AS b706 SPLIT THEM.

### ### Component 5 (the Edit tool): the act's sources, predicates and arms over this act's banks replace b711's (reading 5, the moves, the fit,
### the registrations committed, the needles, the lock gate, the lean test, v1) -- see the act section beneath "(R322)(2)-(7) AND N1-N3"; the
### standing runner arms read this act's one run (port-b707 at be3052ac, run 40154341879, 11 of 12, held at DirichletC7Order :501:31).

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### data/b684_rules.txt row (1) and b706's split, carried: every run in SEVEN foreground parts, each its own call in its own message --
### `--part standing-a`, `--part standing-c` (G-PRIORBANK-UNCHANGED, G-NODISCLOSURE-PUBLIC, G-WRITELIST-KINDS, the four standing figures and
### G-READ-RULE-STANDING), `--part standing-b1` (the shared additive files), `--part standing-b2a` (the act-root chain over b624-b641, its
### verdicts banked, NO ARM), `--part standing-b2b` (b642-b658, banked, NO ARM), `--part standing-b3` (the second half, b659-b712, and
### G-ACTROOT-VERIFY once over every banked verdict), `--part act` (the act's arms over this act's banks, the table regenerated in a closing run);
### each under the 590 s guard, NOT RUN beneath the 2,560 MB hold; `--combine <bank>` writes the bank. The chain halves as b693 drew them with
### b712 added to the second (the ferry's Component 5).
### ### (R264)(2), THE FREEZE: the standing arms are b711's face's (G2) arms less b711's own arms over b711's banks, carried, the twenty-four rule
### arms of tools/rule_arms.py and G-READ-RULE-STANDING among them; NO standing arm is added (N5). THE REPAIRS (R322)(3) ORDERS, each a diff in
### relay data/b712_tool_repairs.txt with its controls (data/b712_repair_controls.txt, 16 cases): G-REPORT-UNSEALED's key read case-insensitively
### (keys_ci) and G-AXIS-REGISTERED's bank read after joining wrapped lines (joined), both helpers here and the report arm reading through keys_ci;
### the lock gate's argument required; the lean-running test reading banked prints. G-RECEIPT-IN-FULL repointed to read the standing clauses by
### version ((R322)(4)). This suite carried by tools/b712_carry.py from tools/b711_checks.py (the act names substituted) and its act sections
### written by the Edit tool at the spans b711's repair diff names (data/b711_repairdiff_checks.txt): the sources over this act's banks and the
### arms over them (the weight and readings lines, the repairs, the standing clauses, reading 5, the moves record, the registrations, the fit)
### in place of b711's (the grid, the pairs, the port, the axis).
### The four standing figures read by tools/b706_standing_figures.py (unedited, over b706's roster) against b711's baselines
### (data/b711_standing_figures.json), each by b703's fig_ok. The standing runner arms (G-WORKFLOW-FILES, G-RUNNER-READ, G-RUNNER-GATE,
### G-MERGES-ON-GATE) read b711'S ONE RUN as banked -- no dispatch this act ((R322)(7)) -- port-b707 at b711's one commit (run 40123142437), its
### conclusion failure (11 of 12 modules, no grade claimed), the branch held, no main moved, no tag made, no merge.
### ### The PRERUN guard held: the per-part seconds bank is written under `if PRERUN:` alone, so no root-named bank is written by the pre-push or
### post-push run; `--guard-dry` prints, for each run mode, what the writer block would write, writing nothing.
### ### Every look-up of a landed line goes through the one conversion (imported from tools/b652_record.py through tools/b712_record.py).
### ### The harness is b568's to b711's, written by the Write tool from tools/b711_checks.py, its pure helpers imported from tools/b703_checks.py
### ### (sealed at b703 and unedited); the sources, predicates and arms over this act's banks are b712's (the act's arms over this act's banks,
### ### the b711 arms over b711's objects not carried). data/b686_rules.txt row (1): the act arm G-ENTRY-SCORES-EQUAL reads the landed entry; no
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
import b712_worklist as K     # noqa: E402
import b712_record as REC0    # noqa: E402  ### imported before b711's and b703's suites: b698's record tool is then rebound to b712 once
from b712_record import conv  # noqa: E402
import b711_worklist as K707  # noqa: E402
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
FACE = os.path.join(D, 'b712_registration_%s.txt' % K.DATE)
B707_FACE = os.path.join(ROOT, *K.B711_FACE.split('/'))   # ### the previous act's face (b711's, data/b711_registration_2026-10-25.txt), the standing arms' source
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP)
EXPORT = K.EXPORT
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
SEAL = '--seal' in sys.argv
COMBINE = '--combine' in sys.argv
GUARD_DRY = '--guard-dry' in sys.argv
# ### (R322)(2)(iii), standing clauses v2 row (54): `--prev --part <p>` runs every arm of the part on the PREVIOUS ACT'S banks before the seal --
# ### the banks' act prefix, the face, the worklist and the pre-act heads read as b711's (_prev_rebind, at the foot) -- and banks each arm's
# ### verdict beside b711's own (data/b711_exercise.json): an arm passes there unless b711 failed it. ACTN is the act whose banks the run reads.
PREV = '--prev' in sys.argv
ACTN = 'b711' if PREV else 'b712'
PART =sys.argv[sys.argv.index('--part') + 1] if '--part' in sys.argv and len(sys.argv) > sys.argv.index('--part') + 1 else None
L = []
# ### the sealed figures, the floors the count arms read at HEAD (standing from (R291)(3)): no mid-act prompt this act; one prompt before the root
# ### (the root's own, (R322)(9): "the root's prompt put once"), one call, its answer checked once per (R278)(4) after the lock; the ten letters
# ### at the seal, (d) the navigator's (the ruling's control of (2)(i), for the author's strike)
FLOORS = dict(prompts=1, calls=1, checks=1, defects=(('a', 'SEAT'), ('b', 'SEAT'), ('c', 'SEAT'), ('d', 'NAVIGATOR'), ('e', 'SEAT'), ('f', 'SEAT'),
                                                     ('g', 'SEAT'), ('h', 'SEAT'), ('i', 'SEAT'), ('j', 'SEAT')))


def _bank_utc(text):
    """the UTC stamp a bank's head line carries, '(YYYY-MM-DDTHH:MM:SSZ)', as an epoch; None where absent."""
    m = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', NL.join((text or '').split(NL)[:2]))
    return iso_epoch(m.group(1)) if m else None


REPAIRED_TOOLS = K.REPAIRED_TOOLS
NEW_TOOLS = K.NEW_TOOLS
# ### the instruments read unedited: b703's list with b703's figures tool, b695's to b711's sealed tools, their new and repaired tools (b711's two
# ### shared tools and the roster among them, unedited this act), less this act's sealed tools
INST_BASE = tuple(C3.INST_BASE) + ('b703_standing_figures.py',)
INST = tuple(sorted((set(INST_BASE) | set(K695.SEALED) | set(K696.SEALED) | set(K697.SEALED) | set(K698.SEALED) | set(K699.SEALED) | set(K700.SEALED)
                     | set(K701.SEALED) | set(K702.SEALED) | set(K703.SEALED) | set(K704.SEALED) | set(K704.NEW_TOOLS) | set(K704.REPAIRED_TOOLS)
                     | set(K705.SEALED) | set(K705.NEW_TOOLS) | set(K705.REPAIRED_TOOLS) | set(K706.SEALED) | set(K706.REPAIRED_TOOLS)
                     | set(K707.SEALED) | set(getattr(K707, 'NEW_TOOLS', ())) | set(getattr(K707, 'REPAIRED_TOOLS', ()))
                     | set(p[6:] if p.startswith('tools/') else p for p in getattr(K707, 'REPAIRED_DATA', ())))
                    - set(K.SEALED) - set(REPAIRED_TOOLS) - set(NEW_TOOLS) - {'b712_report.py'}))


def _renamed():
    return dict((r['versioned'], r['unversioned']) for r in (jl('b706_partners.json').get('rows') or []) if r.get('versioned') and r.get('unversioned'))


# ### the corpus documents this act does not write: b703's list at the files of record after (R316)(3); no document is cut this act
CURRENTS = tuple(dict.fromkeys(_renamed().get(p, p) for p in C3.CURRENTS))
TABLE_FILES = K.TABLE_FILES
WF, PT = '.github/workflows/build-module.yml', 'print_targets.txt'
PORT_LABEL = K.PORT_LABEL     # ### b711's one run, read as banked by the standing runner arms (no dispatch this act)
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
NEXT_RULES_GLOB = 'relay/data/b712_rules.txt'   # ### (R322)(9): data/b712_rules.txt and data/b712_rules.txt named by form; this act writes no rules bank
# ### (R315)(2)(b), b705's repaired predicate, carried: the root bank's items read against the root route's own item list, and the required list
# ### read against ROOT_EXCLUDE here, at import (b706's (j)); the binary banks (.gz) are not root items (data/b680_rules.txt row (1)), their hashes banks are
REQUIRED_BANKS = ('data/b712_independence.txt', 'data/b712_standing_control.txt', 'data/b712_tool_repairs.txt', 'data/b712_repair_controls.txt',
                  'data/b712_corrigendum.txt', 'data/b712_port.txt', 'data/b712_port_edit.txt', 'data/b712_dispatches.json', 'data/b712_order_lines.json',
                  'data/b712_surgery.txt', 'data/b712_coeffs.txt', 'data/b712_axis.txt', 'data/b712_list.txt', 'data/b712_pairs.txt',
                  'data/b712_surgery_hashes.txt', 'data/b712_coeffs_hashes.txt', 'data/b712_axis_hashes.txt', 'data/b712_list_hashes.txt', 'data/b712_pairs_hashes.txt',
                  'data/b712_registrations_reread.txt', 'data/b712_standing_figures.txt', 'data/b712_stepzero.txt', 'data/b712_report.txt',
                  'data/b712_citation_check.txt', 'data/b712_tests_stepzero.txt', 'data/b712_readfirst.txt', 'data/b712_branches.txt', 'data/b712_kernels_face.json')
STANDING_BANK = 'data/standing_clauses_v2.txt'   # ### (R322)(2): a shared bank by version, outside the act's prefix, named apart
_EXCLUDED_REQUIRED = [p for p in REQUIRED_BANKS if REC0.R.ROOT_EXCLUDE.match(os.path.basename(p))]
if _EXCLUDED_REQUIRED:
    raise SystemExit('### REQUIRED_BANKS NAMES A BANK THE ROOT ROUTE EXCLUDES (b706`s (j)): %s' % _EXCLUDED_REQUIRED)


def rec(s=''):
    L.append(s)
    print(s)


def _act_code(path):
    """the act's code in a tool: the whole file for this act's own tools; for a shared tool the ruling orders edited ((R322)(3)-(4)) the lines
    this act added to it alone (`git diff` from the act's base, its `+` lines) -- the shared tool's earlier code is its own act's, read by that
    act's arms (b378's fixture cleans its temporary directory, a line this act did not write)."""
    if os.path.basename(path) not in REPAIRED_TOOLS:
        return read(path)
    d = gs(ROOT, 'diff', PRE['relay'], '--', 'tools/' + os.path.basename(path))
    return NL.join(l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))


def is_pushed():
    return (gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b712')
            and 'data/b712_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    """tools/rule_arms.py's sources over the seat's session from (R322)'s anchor, its call trace extended by any continuation session's
    (K.SESSIONS_AFTER, none so far) through rule_arms.transcript."""
    R_ = RA.sources('b712', SESSION, K.ANCHOR, K.PARTS, lock, PRE['relay'], PRE['pp'])
    for sid, anc in K.SESSIONS_AFTER:
        R_['calls'] = list(R_.get('calls') or []) + RA.transcript('%s/%s.jsonl' % (PROJ, sid), anc)
    return R_


def conv_alone():
    P = 'p' + 'oss('
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to',
            'def ' + 'conv(']
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b712_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks):
                bad.append(f)
    return bad


def spec_planted():
    import b712_regspec as SPEC
    P = SPEC.planted()
    ctl = [ok for _w, ok in SPEC.controls()]
    return dict(read=[ok for _s, ok, _w in P], controls=ctl, shapes=[s for s, _o, _w in P])


def _deps(ax):
    return REC0._deps(ax)


def _tag_peel(repo, tag):
    return gs(repo, 'rev-parse', '--verify', '--quiet', 'refs/tags/%s^{commit}' % tag)


def wf_state():
    """this act's one run at SIDE-lv-conservation ((R322)(4)): the workflow at port-b707's new tip (this act's one commit) equal to the workflow at
    b707's commit (the branch's base), written before b712; the lakefile and its Mathlib requirement; the print list ABSENT at the branch (the
    print step read as not run, no grade claimed); this act's one write on the branch the one module."""
    out = {}
    tip = K.PORT_NEW_TIP
    src = read_blob(LV, '%s:%s' % (tip, WF)) or ''
    before = read_blob(LV, '%s:%s' % (K.PORT_BASE, WF)) or ''
    lf = read_blob(LV, '%s:lakefile.lean' % tip) or read_blob(LV, '%s:lakefile.toml' % tip) or ''
    req = re.search(r'(?is)require\s+(?:"?mathlib"?|\[\[require\]\]\s*name\s*=\s*"mathlib")', lf)
    pt = read_blob(LV, '%s:%s' % (tip, PT)) or ''
    wrote = gs(LV, 'log', '-1', '--format=%H', tip, '--', WF)
    act_writes = [x for x in gs(LV, 'diff-tree', '--no-commit-id', '--name-only', '-r', tip).split(NL) if x.strip()]
    out[K.KERNEL] = dict(text=src, before=before, wrote=wrote, wrote_before_act=bool(wrote) and wrote != tip,
                         lakefile=bool(lf.strip()), mathlib=bool(req), targets=[l.strip() for l in pt.split(NL) if l.strip()], print_list_absent=not pt.strip(),
                         printed=0, prints_targets=[], prints_printed=0, act_writes=act_writes, want=[K.PORT_FILE])
    return out


STANDING = sorted((set(g2_of(B707_FACE)) - set(K707.ACT_ARMS)) | set(K.STANDING_ADDED))
TESTS = ('test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py')


# ================================================================== THE CHAIN SPLIT BY ACT (b693's halves, b712 added; the first half in two quarters)
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
    return base.replace('b712_', '').replace('.txt', '')


def half_bank(i, key):
    """i is 'a1', 'a2' (the first half's quarters) or 'b' (the second half)."""
    return 'b712_chain_half_%s_%s.json' % (i, key)


def write_half(i, key, verdicts, reads, span):
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), head=gs(ROOT, 'rev-parse', 'HEAD'), half='%s-%s' % span,
             acts=verdicts, reads=reads, boundary=boundary())
    p = os.path.join(D, half_bank(i, key))
    _membrane(p)
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
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b712_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if (f.startswith('b712_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS)
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    cit = jl('b712_citation_check.json')
    try:
        REC.R._defect_short()
        refuses = False
    except TypeError:
        refuses = True
    t0 = time.time()
    cmds = capture_now()
    ranking = (rd('b705_i6_ranking.txt') or '').split(NL)
    gz_g, gz_p = os.path.join(D, 'b712_grid.json.gz'), os.path.join(D, 'b712_pairs.json.gz')
    S = dict(
        REC=REC, ER=ER, face=face, ferry=rd('b712_ferry.txt'), scan=rd('b712_ferry_scan.txt'), stepz=rd('b712_stepzero.txt'),
        readfirst=rd('b712_readfirst.txt'), defects=rd('b712_defects.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        answers=rd('b712_author_answers.txt'), answersj=jl('b712_author_answers.json'), prerun=rd('b712_arms_prerun.txt'), rl=jl('b712_record_lines.json'),
        tests=jl('b712_tests_stepzero.json'), testst=rd('b712_tests_stepzero.txt'), withheld=jl('b712_tests_withheld.json'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b712_seal_hashes.json'), sealnow=sealed_now(), cmds=cmds, prev_cmds=prev_now(), cmdj=jl('b712_commands.json'),
        cmdt=rd('b712_commands.txt'), reads_bank=rd('b712_read_calls.txt'), reads_json=jl('b712_read_calls.json'),
        planted={t: run_test(t) for t in TESTS}, spec=spec_planted(), conv_bad=conv_alone(), suite=read(os.path.join(T, 'b712_checks.py')),
        citation=rd(K.CITATION_BANK), cit_at=iso_epoch(cit.get('at') or ''), cit_misses=cit.get('misses') or [],
        gate=rd('b712_reg_gate.txt'), rowgen=rd('b712_rowgen_stepzero.txt'),
        branchj=jl('b712_branches.json'), branchbj=jl('b712_branches_before.json'), branchest=rd('b712_branches.txt'),
        branch_lists=dict((repo, gs(repo, 'branch', '--list', *bs)) for repo, bs in K.DELETE),
        repairs=rd('b712_tool_repairs.txt'), repairsj=jl('b712_tool_repairs.json'), repair_ctl=rd('b712_repair_controls.txt'), repair_ctlj=jl('b712_repair_controls.json'),
        repairdiffs=dict((n_, rd('b712_repairdiff_%s.txt' % n_)) for n_ in CARRIED_NAMES), carry_banks=dict((n_, rd('b712_carry_%s.txt' % n_)) for n_ in CARRIED_NAMES),
        spans=rd('b712_carry_spans.txt'), rec_src=read(os.path.join(T, 'b712_record.py')),
        closing_src=read(os.path.join(T, 'b712_closing.py')),
        defshort=dict(b711=len(REC._defect_short('b711')), refuses=refuses),
        defshort_b712=REC._defect_short(ACTN), letters_seal=REC.letters_at_seal(ACTN),
        corrj=jl('b712_corrigendum.json'), corrt=rd('b712_corrigendum.txt'), corrigenda=rd('b675_corrigenda.txt'),
        corrigenda_tri=tri(ROOT, 'data/b675_corrigenda.txt', PRE['relay']),
        guard=rd('b712_guard_dry.txt'), guardj=jl('b712_guard_dry.json'),
        rootdry=rd('b712_root_banks_dry.txt'), rootdryj=jl('b712_root_banks_dry.json'),
        figj=jl('b712_standing_figures.json'), figt=rd('b712_standing_figures.txt'),
        # ### (R322)(2): the standing clauses by version (v2 written at step zero, v1 unchanged) and the control
        standing_bank=read(os.path.join(ROOT, *STANDING_BANK.split('/'))), standing_v1=read(os.path.join(ROOT, *K.DATA_STANDING_V1.split('/'))),
        standing_ctlj=jl('b712_standing_control.json'), standing_ctl=rd('b712_standing_control.txt'),
        membrane_src=read(os.path.join(T, 'act_membrane.py')),
        # ### (R322)(3): the Independence supplement
        indep=rd('b712_independence.txt'), indepj=jl('b712_independence.json'),
        # ### (R322)(4): the port's edit, its one run, the dispatch bank, the runner row, the order; the join kernel read beside
        portj=jl('b712_port.json'), portt=rd('b712_port.txt'), portej=jl('b712_port_edit.json'), dispj=jl('b712_dispatches.json'),
        runner_rows=jl('b712_runner_rows.json'), orderj=jl('b712_order_lines.json'),
        runs={PORT_LABEL: rd('b712_port.txt')},
        buildlogs={PORT_LABEL: rd('b712_buildlog_%s_%s.txt' % (K.KERNEL, PORT_LABEL))},
        lv_wf_tip=read_blob(LV, '%s:%s' % (K.PORT_NEW_TIP, WF)) or '', lv_wf_base=read_blob(LV, '%s:%s' % (K.PORT_BASE, WF)) or '',
        lv_tip_parent=gs(LV, 'rev-parse', '--verify', '--quiet', K.PORT_NEW_TIP + '^'),
        lv_tip_files=[x for x in gs(LV, 'diff-tree', '--no-commit-id', '--name-only', '-r', K.PORT_NEW_TIP).split(NL) if x.strip()],
        lv_tip_stat=[x for x in gs(LV, 'diff-tree', '--no-commit-id', '--numstat', '-r', K.PORT_NEW_TIP).split(NL) if x.strip()],
        lv_tip_on_main=subprocess.run(['git', '-C', LV, 'merge-base', '--is-ancestor', K.PORT_NEW_TIP, 'main']).returncode == 0,
        lv_main=gs(LV, 'rev-parse', 'main'), lv_v0100=_tag_peel(LV, 'v0.10.0'), lv_port=gs(LV, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.PORT_BRANCH),
        lv_tags=[t for t in gs(LV, 'tag', '--list').split(NL) if t.strip()], lv_tip_tags=[t for t in gs(LV, 'tag', '--points-at', K.PORT_NEW_TIP).split(NL) if t.strip()],
        lv_remote={},
        join_lake=dict((n_, (cr0(blob(KI, '%s:%s' % (K.JOIN_TIP, n_))), cr0(raw(os.path.join(KI, n_))))) for n_ in ('lakefile.lean', 'lakefile.toml', 'lake-manifest.json'))
        if os.path.isdir(KI) else {},
        join_status=gs(KI, 'status', '--porcelain') if os.path.isdir(KI) else '### NO KERNEL', join_grade=os.path.exists(os.path.join(D, 'b712_join_grade.txt')),
        # ### (R322)(5)-(7): the five computations' banks, text and JSON, and their hashes banks
        comp=dict((n_, (rd('b712_%s.txt' % n_), jl('b712_%s.json' % n_), rd('b712_%s_hashes.txt' % n_))) for n_ in ('surgery', 'coeffs', 'axis', 'list', 'pairs')),
        # ### N3: the registrations computed, read at their commits and now
        regs_b711=(blob(ROOT, '%s:data/b711_registrations.txt' % K.REG_B710), blob(ROOT, 'HEAD:data/b711_registrations.txt'), raw(os.path.join(D, 'b711_registrations.txt')),
                   [l for l in gs(ROOT, 'log', '--format=%h', '--', 'data/b711_registrations.txt').split(NL) if l.strip()]),
        regs_b709=(blob(ROOT, '%s:%s' % (PRE['relay'], K.REG_B709)), blob(ROOT, 'HEAD:' + K.REG_B709), raw(os.path.join(ROOT, *K.REG_B709.split('/'))),
                   [l for l in gs(ROOT, 'log', '--format=%h', '--', K.REG_B709).split(NL) if l.strip()]),
        fit710=rd('b711_fit.txt'),
        regs_rereadj=jl('b712_registrations_reread.json'), regs_reread=rd('b712_registrations_reread.txt'), rules=rd('b712_rules.txt'),
        report=rd('b712_report.txt'), reportj=jl('b712_report.json'), report_tool=os.path.exists(os.path.join(T, 'b712_report.py')),
        ef_main=gs(EF, 'rev-parse', 'main'), ef_tags=dict((t, _tag_peel(EF, t)) for t in ('v0.37', 'v0.1', 'v0.2')),
        ef_log=[l for l in gs(EF, 'log', '--first-parent', '--format=%H', K.EF_V037 + '..main').split(NL) if l.strip()],
        ef_tags_all=[t for t in gs(EF, 'tag', '--list').split(NL) if t.strip()], ef_remote={},
        join_main=gs(KI, 'rev-parse', 'main') if os.path.isdir(KI) else '', join_tags=[t for t in gs(KI, 'tag', '--list').split(NL) if t.strip()] if os.path.isdir(KI) else [],
        rf_diff=rd('b712_readfirst_diff.txt'), rf_hand_now=blob(ROOT, 'HEAD:data/b712_readfirst.txt'),
        rf_hand_z=blob(ROOT, '%s:data/b712_readfirst.txt' % K.STEPZERO_BANKS) if K.STEPZERO_BANKS else None,
        asec=jl('b712_arm_seconds.json'), asect=rd('b712_arm_seconds.txt'),
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
        arj=jl('b712_act_root.json'), arj0=jl('b711_act_root.json'), art=rd('b712_act_root.txt'), rootsf=rd('act_roots.txt'),
        rootbanks=jl('b712_root_banks.json'), route_list=REC.root_banks(),
        pushout=(files_of(ROOT, K.STEPZERO) if K.STEPZERO else [], bool(K.STEPZERO) and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, *f.split('/')))), cr0(blob(ROOT, 'HEAD:tools/' + f)))
              for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        pp_renames=gs(PP, 'diff', '--name-status', '-M', PRE['pp'], 'HEAD'),
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        page_changed=[x for x in (gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD', '--', K.FACES_PAGE) + NL + gs(PP, 'diff', '--name-only', '--', K.FACES_PAGE)).split(NL) if x.strip()],
        kern_face=(jl('b712_kernels_face.json').get('kernels') or {}), kerns_read=list(dict.fromkeys(REC._kerns())) + ['SIDE-faces-join'],
        tools=tools, tooltext={f: strip_prose(_act_code(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mustfail=not os.path.exists(os.path.join(D, 'b712_mustnotexist.txt')),
        steps=jl('b712_steps.json').get('rows') or [],
        fj=jl('b712_findings.json'), tj=jl('b712_trail.json'), sc=jl('b712_scores.json'), desk=rd('b712_desk_notes.txt'), tfj=jl('b712_table_final.json'),
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
    S['secs_ct'] = dict((p, _ct(ROOT, gs(ROOT, 'log', '-1', '--format=%H', '--', 'data/b712_arm_seconds_%s.json' % p))) for p in K.PARTS)
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
        base = jl('b711_standing_figures.json')
        S['fig'] = SF6.all_figures(baseline=((base.get('pins') or {}).get('rows') or {}), remote=KC0.remote_refs)
        S['fig_prev'] = base
        S['fig_prev_name'] = 'b711_standing_figures.json (b711`s figures; the readers over b706`s roster, data/b706_roster_read.json)'
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
            if f.startswith(('b712_', 'audit_b712_')) and os.path.isfile(os.path.join(D, f)) and not f.endswith(('.gz', '.png', '.jsonl')):
                pub.append(read(os.path.join(D, f)))
        pub += [read(f) for f in tools]
        pub += [S['lv_wf_tip'] or '', read_blob(LV, '%s:%s' % (K.PORT_NEW_TIP, K.PORT_FILE)) or '']
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


# ### the eight test files not clean at step zero: the three b706 carried and the five readers the renames of (R316)(3) broke (data/b712_defects.txt, the events)
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


def post_seal_named(face):
    """(R322)(3)(i): the face's row `### POST-SEAL PROMPTS NAMED: <n>[ (the root`s prompt)]` read as n; NONE or no row reads 0."""
    m = re.search(r'### POST-SEAL PROMPTS NAMED: (NONE|\d+)', face or '')
    return 0 if not m or m.group(1) == 'NONE' else int(m.group(1))


def answers_bank_ok(a, answersj, lock_epoch, face, act, floors):
    """the answers bank's form for <act>, pure in its arguments: its prompt count the bank's own, each prompt with two options or more and its
    result, the calls at or above the floors, and every call after the lock named on the face's post-seal row ((R322)(3)(i))."""
    m = re.search(r'^### %s -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)' % act, a, re.M)
    heads = re.findall(r'^### PROMPT \d+ \(', a, re.M)
    calls = re.findall(r'^### CALL tool-use id ', a, re.M)
    res = re.findall(r'^RESULT \(transcript line [^)]*\): (.*)$', a, re.M)
    if not m or int(m.group(1)) != len(heads) or len(heads) < floors['prompts'] or len(calls) < floors['calls']:
        return False
    per = [len(re.findall(r'^  OPTION \d+', p, re.M)) for p in re.split(r'^### PROMPT \d+ \(', a, flags=re.M)[1:]]
    lk = lock_epoch
    after = [c for c in (answersj or {}).get('calls') or [] if lk and iso_epoch((c.get('ts') or '')[:19] + 'Z') and iso_epoch((c.get('ts') or '')[:19] + 'Z') > lk]
    return all(x >= 2 for x in per) and len(res) == len(calls) and not any(UNANSWERED in r or '### NO RESULT' in r for r in res) \
        and len(after) <= post_seal_named(face)


def answers_ok(S):
    """the answers bank at HEAD under answers_bank_ok, this act's floors."""
    return answers_bank_ok(S['answers'], S['answersj'], S['lock_epoch'], S['face'], 'b712', FLOORS)


def no_local_lean(S):
    return bool(S['cmds']) and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and S['REC'].local_lean(r['cmd'])]


# ================================================================== (R322) STEP ZERO: THE CITATION CHECK, THE BRANCHES, THE READ-FIRST BANK
# ### the ferry's read-first list (data/b712_ferry.txt :37) by its banked rows (data/b712_readfirst.txt :11-:33)
READFIRST_NEEDLES = ('relay data/b711_closing.txt | :1 ;', 'relay data/b711_defects.txt | :1-:133 (whole', 'relay data/standing_clauses_v1.txt | :1-:119 (whole)',
                     'relay data/b711_reading5.txt | :1-:194 (whole)', 'relay data/b711_registrations.txt | :1-:84 (whole)', 'relay data/b709_registrations.txt | :1-:61 (whole)',
                     'relay data/b709_port.txt | :1-:53 (whole)', 'relay data/b709_pairs.txt | :1-:62 (whole)', 'relay data/b711_tool_repairs.txt | :1-:175 (whole)',
                     'relay data/b711_closing_push_out.txt | :1-:6 (whole)', 'PLACE-papers OPEN_TRAILS.md | :15802-:15809',
                     'PLACE-papers phase1.5/method/EXCLUSION_ENGINE.md | :1-:200 ; :200-:237')
NAMED_PUSH = sorted(b for _r, bs in K.DELETE for b in bs)
SCRATCH = ()                  # ### no scratch branch this act: the one branch written is port-b707, held ((R322)(4), (7))


def readfirst_ok(S):
    z = unwrap(S['readfirst'])
    return bool(z) and all(x in z for x in READFIRST_NEEDLES) and 'ITEMS 23 ;' in z


def branches_ok(S):
    z = S['branchest']
    left = dict((r, sorted(x.strip() for x in v.split(NL) if x.strip())) for r, v in S['branch_lists'].items())
    return all(v == [] for v in left.values()) and len(left) == 2 and all(b in z for b in NAMED_PUSH) \
        and 'BRANCHES NAMED 8 ; DELETED 8 ; KEPT 0 ; EVERY TIP MERGED True ; port-b707 STANDS True' in unwrap(z)


def branches_banked_ok(S):
    rows = S['branchj'].get('rows') or []
    try:
        fates = [S['REC'].read_branch_row(r) for r in rows]
    except Exception:
        return False
    bt = iso_epoch((S['branchbj'].get('at') or '')[:19] + 'Z')
    fd = S['first_delete_ts']
    kept = S['branchj'].get('kept') or {}
    return len(rows) == 8 and all(f == 'DELETED' for _b, f in fates) and all(r['merged'] for r in rows) \
        and sorted(r['branch'] for r in rows) == NAMED_PUSH and bool(bt) and bool(fd) and bt < fd and len(S['branchbj'].get('rows') or []) == 8 \
        and bool(S['cit_at']) and S['cit_at'] < fd and kept.get('branch') == K.PORT_BRANCH and kept.get('local') == kept.get('remote') == K.PORT_TIP


def deletes_one_ok(S):
    """every branch delete of the act one branch, no glob, no variable, nothing chained after: the eight of (R322)(8) alone; port-b707 never."""
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
        and 'data/b712_branches_before.json (before any delete)' in S['stepz'] and '`git branch --merged main`' in S['stepz']


def dry_step_ok(S):
    g = S['gate']
    return '--- THE DRY-RUN STEP ((R267)(2))' in g and 'ENTRY : table cells NONE ; screens QUIET' in g and 'TRAIL : table cells NONE ; screens QUIET' in g \
        and 'THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK True' in g and 'THE TRAIL`S RESOLVED LINE EQUAL TO THE DEFECTS BANK True' in g \
        and '### ### **THE DRY-RUN STEP : CLEAN**' in g and '### ### **GATE VERDICT : CLEAR**' in g


# ### (R322)(2)(iii), standing clauses v2 row (54), ARMS READ STRUCTURE: the gate's '### NO VERDICT LINE' rows read by the bank each row names and
# ### not by a list of names -- b709's and b711's lists named their own acts' banks, and the carry's substitution turned b711's entry into a bank
# ### that does not exist (data/b711_prints_v0.17.txt for b708's data/b708_prints_v0.17.txt). A row passes where its bank exists, is not empty and
# ### carries no verdict line by the closing tool's own reader (tools/b712_closing.py VLINE); a row naming no bank, an absent or empty bank, or a
# ### verdict-bearing bank printed without its verdict fails. The gate writes no JSON bank, so its text is read (data/b712_repair_controls.txt (iii)).
NO_VERDICT_ROW = re.compile(r'\(relay (data/[^\s)]+)\): ### NO VERDICT LINE')
VLINE_FORM = re.compile(r'^\s*### ### \*\*(.*?)\*\*\s*$', re.M)


def no_verdict_line_ok(g, root=ROOT):
    for l in (g or '').split(NL):
        if '### NO VERDICT LINE' not in l:
            continue
        m = NO_VERDICT_ROW.search(l)
        if not m:
            return False
        p = os.path.join(root, *m.group(1).split('/'))
        t = open(p, encoding='utf-8', errors='replace').read() if os.path.isfile(p) else ''
        if not t.strip() or VLINE_FORM.search(t):
            return False
    return True


def closing_dry_ok(S):
    g = S['gate']
    return '--- THE CLOSING DRY-RUN STEP (b675 rules row 1)' in g and '### ### **THE CLOSING DRY-RUN STEP : CLEAN**' in g \
        and 'b712 closed:' in g and 'THE REPAIRS' in g and 'THE STANDING CLAUSES AND THE SUPPLEMENT' in g and 'THE PORT AND THE JOIN' in g \
        and 'THE SURGERY, THE COEFFICIENTS AND THE AXIS' in g and 'THE LIST AND THE PAIRS' in g and 'THE REGISTRATIONS' in g \
        and '### THE STANDING ARMS' in g and '### THE KERNELS' in g and '(g) The defects (a)' in g and no_verdict_line_ok(g)


def citation_ok(S):
    """the citation check's bank: every cite checked, OK and misses summing, its two misses entered by the fact clause (the head line's quotation
    of data/b711_closing.txt :1 against the file's backticks; "its Independence lemma", no kernel declaration of the name); the bank written before
    the step-zero banks' commit and that commit before Component 1's."""
    c = S['citation']
    m = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', c)
    return bool(m) and int(m.group(1)) == int(m.group(2)) + int(m.group(3)) > 0 and 'A GATE STEP AT STEP ZERO' in c \
        and int(m.group(3)) == len(S['cit_misses']) == 2 and 'RECORDS, and the PLACE-papers subject' in c and 'NO DECLARATION NAMED FOR INDEPENDENCE' in c \
        and bool(S['cit_at']) and bool(S['t'].get('stepzero')) \
        and S['cit_at'] < S['t']['stepzero'] and bool(S['t'].get('c1')) and S['t']['stepzero'] <= S['t']['c1']


def rowgen_ok(S):
    return '### ### **CONSTELLATION EXIT 0 ; ROWGEN DIFF EXIT 0 ; TABLES 19 ; RE-POINTED 8.**' in S['rowgen']


def weight_ok(S):
    # ### this act's needles: b711's head line as its closing prints it (data/b711_closing.txt :1) and the record's commits the repaired builder read
    return landed(S, 0, ['b711 AT ITS WEIGHT', 'suite 137 of 143; root 11fe3e21e2fc796a', 'relay 2c200e8d and PLACE-papers df2dd7c'])


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
    """no mid-act answer this act: the one prompt is the root's ((R322)(9)), so every check stamp in the citation bank lies after the lock and at
    or before the root (data/b712_act_root.json, within the chain's order slack) -- the write it governs; the answers bank carrying the one prompt,
    written once before the root."""
    st = re.findall(r'### \(R278\)\(4\) THE MID-ACT CHECK \((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\): the (?:navigator`s )?answer carrying \'([^\']+)\'', S['citation'])
    lk = S['lock_epoch']
    root_at = S['arj'].get('at_epoch')
    xs = [iso_epoch(t) for t, _n in st]
    return FLOORS['prompts'] == 1 and lk is not None and root_at is not None and bool(xs) \
        and all(x is not None and lk <= x <= root_at + S['order_slack'] for x in xs) \
        and len(re.findall(r'^### PROMPT \d+ \(', S['answers'], re.M)) == FLOORS['prompts']


CHECK_STAMP = re.compile(r'(### \(R278\)\(4\) THE MID-ACT CHECK \()\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ(\))')


def answers_plant(S):
    """(R322)(2)(iv), standing clauses v2 row (55): G-ANSWERS-BEFORE-WRITES given a control that fails -- every check stamp in the citation bank
    moved after the write it governs, the landing and the lock and the root among them (to 2099-01-01T00:00:00Z), so the mutated copy carries
    an answer checked after it was acted on. b711's plant appended a prompt to the answers bank where the predicate reads one prompt or more,
    so the mutated copy passed and the control could not fire (b711's events; data/b712_repair_controls.txt (iv))."""
    return put(S, 'citation', CHECK_STAMP.sub(r'\g<1>2099-01-01T00:00:00Z\2', S['citation']))


# ================================================================== (R322)(1)-(2): THE RECORD LINES, THE CORRIGENDUM, THE WRITE LIST
def scorer_banks_ok(S):
    n = ''.join(strip_prose(_fn_src(S['rec_src'], f)) for f in ('_n1', '_n2', '_n3', '_n4'))
    sc = strip_prose(_fn_src(S['rec_src'], 'scores'))
    ft = strip_prose(_fn_src(S['rec_src'], '_finding_text'))
    return bool(n) and '_commands.json' in n and '_dispatches.json' in n and '_port.json' in n and '_registrations_reread' in n and '_steps.json' in n \
        and not re.search(r'\b(FIND|OT)\b|FINDINGS|OPEN_TRAILS|findings|entry_line', n) \
        and "os.path.isfile(os.path.join(D, '%s_scores.json' % ACT))" in sc and 'scores_line(S)' in ft and "jl('%s_scores.json' % ACT)" in ft


def entry_scores_ok(S):
    want = conv(S['REC'].scores_line(S['sc'])) if S['sc'] else None
    blk = _entry_block(S)
    got = [l for l in blk.split(NL) if l.startswith('**The scores.**')]
    return bool(want) and bool(S['sc']) and got == [want]


# ### the title by its objects (the ferry's Component 6), compared after case-folding the article alone (b706's repaired predicate, carried)
# ### the ferry's form: "the faces joined by closure at SIDE-faces-join <v0.1.0 | held at <line>>; the surgery at Q0's onsets <positive | negative>
# ### with the composite share <s>; Q0's coefficients negative from n = <n>; the axis (e) <HELD | REFUTED>; the certified list to height <h>, pairs
# ### 11 and 15 <within | outside | beyond reach> the refined law; Independence's row restated from <k> compiled terminals", adjusted to the act
# ### (the join not reached: held at the port's failing line)
TITLE_NEEDLES = ('## the faces’ join by closure at SIDE-faces-join held at DirichletC7Order.lean :501:31', '; the surgery at Q0’s onsets positive with the composite share ',
                 '; Q0’s coefficients negative from n = 48', '; the axis (e) refuted', '; the certified list to height 445, pairs 11 and 15 within the refined law',
                 '; Independence’s row restated from 18 compiled terminals')


def _fold_article(t):
    """b706's fold of the article, carried."""
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


# ### (R322)(2)(i), standing clauses v2 row (52): the trail's Defects and Resolved lines and the three trail-equality arms read THE LETTERS ENTERED
# ### BEFORE THE SEAL (S['letters_seal']: the list the seal records, tools/b712_record.py letters_at_seal) and not the defects bank as it stands
# ### -- a finding after the seal is an event in the closing's events section, not a letter (b711's three trail arms failed on the late letter (i)).
# ### Where the act is not sealed the list is None and the arms fail.
def trail_defects_ok(S):
    m = re.search(r'^\*\*Defects\*\* \(relay data/b712_defects\.txt\): (.*)\.$', trail_tail(S), re.M)
    seal = S['letters_seal']
    return seal is not None and 'THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK True' in S['gate'] and bool(m) \
        and m.group(1) == conv('; '.join(seal) or 'none')


RESOLVED = re.compile(r'^\*\*Resolved by the seat, for the author’s strike:\*\* .*\((\d+)\) the (\w+) navigator (?:miss|misses)'
                      r'(?: \(\([a-z]\)(?:, \([a-z]\))*\))? and the seat’s (\w+) defects? as lettered\.$', re.M)


def trail_resolved_ok(S):
    m = RESOLVED.search(trail_tail(S))
    if S['letters_seal'] is None:
        return False
    nav, seat = _owners(S['letters_seal'])
    return 'THE TRAIL`S RESOLVED LINE EQUAL TO THE DEFECTS BANK True' in S['gate'] and bool(m) and S['REC'].num_word(nav) == m.group(2) \
        and S['REC'].num_word(seat) == m.group(3)


def corrigendum_ok(S):
    """(R322)(2): the generated entry for b711's post-seal items landed (its line in the bank, the title at that line through conv): the five letters
    after b711's seal (g)-(k) read as events under row (52), the two events of its suite, the letters this corrigendum gives (l) and (m); the
    corrigenda bank appended at row (31) and nothing before it changed; in Component 1's commit."""
    j = S['corrj']
    e = j.get('entry_line')
    now, pre, head = S['corrigenda_tri']
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and j.get('lettered') == ['l', 'm'] and j.get('post_seal_letters') == ['g', 'h', 'i', 'j', 'k'] \
        and len(j.get('events') or []) == 2 and j.get('row') == 31 and '  (31) ' in S['corrigenda'] and '  (32) ' not in S['corrigenda'] \
        and pre is not None and (now or b'').startswith(pre) and (head or b'').startswith(pre) and 'FINDINGS :%d' % e in S['corrt'] \
        and 'data/b712_corrigendum.txt' in S['files']['c1']


def writelist_mirror_state_ok(S):
    """(R322)(2): the face's (W) row for the mirror builder names tools/mirror_prevbuild.json beside the zip and its stage; N5 reads it as the
    builder's own (the record tool's N5_RELAY_TOOLS)."""
    w = S['face'][S['face'].find('(W) THE WRITE LIST'):S['face'].find('(Z) THE NOTHINGS')]
    row = [l for l in w.split(NL) if 'mirror_build.ps1' in l]
    return bool(row) and 'tools/mirror_prevbuild.json' in NL.join(w.split(NL)[w.split(NL).index(row[0]):w.split(NL).index(row[0]) + 2]) \
        and 'mirror_prevbuild.json' in tuple(S['REC'].R.N5_RELAY_TOOLS)


def rules_row_ok(S):
    """the rules that bind this act, read where they stand: b711's row (1), the standing clauses carried by version (the ferry names v2, the bank at
    VERSION 2); b709's row (1), the carry read by diff (this act's carry banks); b708's row (1), the report tool outside the sealed list until the
    root's word, the worklist's SEALED naming no report tool. No rules bank of this act's ((R322)(9) names data/b712_rules.txt and
    data/b712_rules.txt by form alone; nothing orders a row)."""
    return '(1) THE STANDING CLAUSES CARRIED BY VERSION' in rd('b711_rules.txt') and bool(re.search(r'^VERSION: 2$', S['standing_bank'], re.M)) \
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and all(S['carry_banks'].get(n) for n in ('record', 'tests', 'checks', 'closing')) \
        and '(1) THE REPORT TOOL IS KEPT OUT OF THE SEALED LIST UNTIL THE ROOT' in rd('b708_rules.txt') and not S['rules'] \
        and not any('report' in t for t in K.SEALED) and 'b712_report.py' not in (S['sealj'].get('tools') or {})


def report_lines_ok(j, keys, n):
    """(R322)(2)(iii), standing clauses v2 row (54): the report read by the JSON bank its tool writes (data/<act>_report.json, its `lines`) and not
    by its text: n lines or more, every one a string, each key found in the lines case-insensitively (keys_ci over the lines alone). b709's
    report (data/b709_report.json) passes on b709's five keys, where the sealed needle on the text wanted RATIO in capitals and failed."""
    ls = (j or {}).get('lines')
    return isinstance(ls, list) and len(ls) >= n and all(isinstance(x, str) for x in ls) and keys_ci(NL.join(ls), keys)


REPORT_KEYS = ('JOIN', 'SURGERY', 'COEFFICIENTS', 'AXIS', 'LIST', 'FIGURES')   # ### the ferry's six report lines (Component 6)


def report_unsealed_ok(S, keys=None, n=6):
    """the report bank written by the unsealed report tool after the root's word and before the root, read by its JSON bank ((R322)(2)(iii)):
    its `at` after the lock and at or before the root's time; the tool outside the sealed list; its lines the ferry's (report_lines_ok)."""
    j = S['reportj']
    at = iso_epoch(j.get('at') or '') if j else None
    root_at = S['arj'].get('at_epoch')
    return bool(j) and S['report_tool'] and 'b712_report.py' not in K.SEALED and at is not None and S['lock_epoch'] is not None and at > S['lock_epoch'] \
        and root_at is not None and at <= root_at + S['order_slack'] and report_lines_ok(j, keys or REPORT_KEYS, n)


def keys_ci(text, keys):
    """(R322)(3), the carry-time repair of G-REPORT-UNSEALED's needle: each key read case-insensitively (b711's sealed arm wanted RATIO in capitals
    and its report printed "the twelve ratios", so the arm failed after the seal on its own needle)."""
    low = (text or '').lower()
    return all(k.lower() in low for k in keys)


def joined(text):
    """(R322)(3), the carry-time repair of G-AXIS-REGISTERED's needle: the bank read after joining its wrapped lines -- every run of white space,
    the line breaks and the continuation indents among them, read as one space (b711's registrations bank wrapped the ranking's quotation across
    its lines 12-13, so the arm's one-string needle found nothing there after the seal)."""
    return ' '.join((text or '').split())


GUARD_WRITE = "sp = os.path.join(D, 'b712_arm_seconds_%s.json' % PART)"   # ### the write's own line, stripped; matched whole, not by a needle


def guard_ok(S):
    s = S['suite'].split(NL)
    i = next((k for k, l in enumerate(s) if l.strip() == GUARD_WRITE), None)
    j = S['guardj']
    return i is not None and s[i - 1].strip() == 'if PRERUN:' and 'POST-ROOT PATH WRITES NONE' in S['guard'] \
        and (j.get('writes') or {}).get('pre-push') == [] and (j.get('writes') or {}).get('post-push') == [] \
        and (j.get('writes') or {}).get('prerun') == ['data/b712_arm_seconds_<part>.json']


def postroot_writes_none(S):
    j = S['guardj']
    w = j.get('writes') or {}
    return 'POST-ROOT PATH WRITES NONE' in S['guard'] and w.get('pre-push') == [] and w.get('post-push') == [] and bool(S['root_ct']) \
        and sorted(S['secs_ct']) == sorted(K.PARTS) and all(v is not None and v <= S['root_ct'] for v in S['secs_ct'].values())


def trail_lines_equal_defects(S):
    tail = trail_tail(S)
    dm = re.search(r'^\*\*Defects\*\* \(relay data/b712_defects\.txt\): (.*)\.$', tail, re.M)
    rm = RESOLVED.search(tail)
    bank = [m_.groups() for m_ in (re.match(r"^\(([a-z]'?)\) THE (NAVIGATOR|SEAT)'S", s) for s in (S['letters_seal'] or [])) if m_]
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


# ================================================================== THE RUNNER (this act's one run: port-b707 at its new tip, its failure read by its id; the join not dispatched)
IDENT_WF = ('secrets.', 'psinary', 'seale', 'york', 'hotmail', 'orcid', '0009-0008')


def wf_ok(S, rules_needle='(1) THE PROBE ROUTE\'S TARGET IS print_targets.txt WHOLE'):
    """b705's repaired reading over this act's one run: the workflow at port-b707's new tip b707's blob unchanged, no identifier, the hold, the
    lakefile and its cache step; the print list ABSENT at the branch, so the print step is read as not run and no grade claimed (the dispatch row
    saying so and `whole` False by it); this act's one write on the branch the one module."""
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
    """this act's one run as read by its id: at the new tip, its conclusion failure, the artifact's sha256 equal to the port bank's, the memory
    low above the hold, no STOP line, the gate NOT DERIVES with no grade claimed (the print step not run), build exit 1 with its 4 error lines; the
    row through the record tool's reader."""
    rows = S['runner_rows'].get('rows') or []
    if len(rows) != 1:
        return False
    try:
        S['REC'].read_runner_row(rows[0])
    except Exception:
        return False
    r = rows[0]
    return r.get('label') == PORT_LABEL and r.get('kernel') == K.KERNEL and r.get('ref') == K.PORT_NEW_TIP and r.get('run_id') == K.PORT_RUN and r.get('conclusion') == 'failure' \
        and re.match(r'^[0-9a-f]{64}$', r.get('artifact_sha256') or '') is not None and r.get('artifact_sha256') == (S['portj'].get('artifact') or {}).get('sha256') \
        and r.get('mem_low') is not None and r['mem_low'] >= K.HOLD and not r.get('stopped') and r.get('gate') == 'NOT DERIVES' and r.get('build_exit') == '1' \
        and len(r.get('errors') or []) == 4 and 'no grade claimed' in (r.get('note') or '')


def gate_ok(S):
    """the run's text bank: the artifact AGREE, the build's exit 1 with its error lines, no grade claimed."""
    t = S['runs'].get(PORT_LABEL) or ''
    return len(S['runs']) == 1 and re.search(r'^### the artifact: .* ; AGREE$', t, re.M) is not None and 'BUILD EXIT 1' in t and 'NO GRADE CLAIMED' in t.upper()


def merges_ok(S):
    """no merge this act: SIDE-explicit-formula's main at badaccc (one first-parent commit past v0.37), its tags unmoved; SIDE-lv-conservation's main
    and deposit unmoved, port-b707 at this act's one commit locally and at the remote and not on main, no tag made; the join kernel's main at its
    manifest commit, no tag."""
    er, lr = S['ef_remote'], S['lv_remote']
    return S['ef_main'] == K.EF_MAIN and len(S['ef_log']) == 1 and S['ef_tags'].get('v0.37') == K.EF_V037 \
        and not [t for t in S['ef_tags_all'] if t > 'v0.37' and t.startswith('v0.3')] \
        and (not er or (er.get('refs/heads/main') == K.EF_MAIN and er.get('refs/tags/v0.37^{}', er.get('refs/tags/v0.37')) == K.EF_V037)) \
        and S['lv_main'] == K.LV_MAIN and S['lv_v0100'] == K.LV_V0100 and S['lv_port'] == K.PORT_NEW_TIP and 'v0.10.0' in S['lv_tags'] and not S['lv_tip_on_main'] \
        and not [t for t in S['lv_tags'] if t.startswith('v0.1') and t > 'v0.13.0'] and S['lv_tip_tags'] == [] \
        and (not lr or (lr.get('refs/heads/main') == K.LV_MAIN and lr.get('refs/heads/' + K.PORT_BRANCH) == K.PORT_NEW_TIP)) \
        and S['join_main'] == K.JOIN_TIP and S['join_tags'] == []


# ================================================================== SCOPE, THE SEAL, THE ROOT, THE RECORD
def seal_hashes_ok(S):
    j = S['sealj']
    at = iso_epoch(j.get('at') or '')
    rec_ = j.get('tools') or {}
    return bool(rec_) and at is not None and S['lock_epoch'] is not None and S['lock_epoch'] <= at \
        and sorted(rec_) == sorted(K.SEALED) and all(S['sealnow'].get(t) == rec_[t] for t in K.SEALED)


POST_SEAL = ('b712 seal', 'b712 pre-root', 'b712 root', 'b712 record', 'b712 --', 'b712 closing', 'b712 entry')


def _component_commit(s):
    return s.startswith('b712') and not s.startswith(POST_SEAL)


def _step_phase(rows, repo, h):
    """the phase the act's step bank gives a commit (its row by repository and by the commit's abbreviated hash), None where it has no row."""
    return next((r.get('phase') for r in rows if r.get('repo') == repo and (r.get('commit') or '').startswith(h)), None)


def sealed_after_ok(S):
    """(R322)(2), a carry-time repair (b711's (i)): THE ACT'S STEP BANK (data/b712_steps.json, a row per commit by the record tool's step route,
    written after the commit: the repository, the commit, the phase the seat names from the record tool's STEP_PHASES) and not the commits'
    subjects -- b711's arm failed on two post-seal subjects outside its prefixes, their order right. Every relay and PLACE-papers commit of the
    act has its row; a row's phase is a component phase (PRE_SEAL_PHASES) exactly where its commit precedes the lock; PLACE-papers carries a
    component commit."""
    lk, rows = S['lock_epoch'], S['steps']
    if lk is None or not rows:
        return False
    pre = S['REC'].PRE_SEAL_PHASES
    for repo, log in (('relay', S['rlog']), ('pp', S['plog'])):
        for h, s, t in log:
            p = _step_phase(rows, repo, h)
            if p is None or (t < lk) != (p in pre):
                return False
    return any(_step_phase(rows, 'pp', h) in pre for h, s, t in S['plog'])


def nothing_ahead_ok(face, lock_epoch, logs, steps):
    """(R322)(3)(ii), standing clauses v3: THE GATE'S COMMIT READ FROM THE STEP BANK. A face cannot carry the hash of the commit that stamps it,
    so the gate's commit is the one step-bank row of phase `gate` (or, for an act before the repair, the row the control names), and every
    other commit at or before the lock is declared on the face by its 7-hex prefix. Pure in its arguments: logs [(hash, subject, epoch)],
    steps the step bank's rows."""
    gates = [r.get('commit') or '' for r in steps or [] if r.get('phase') == 'gate']
    if 'WHAT RAN AHEAD OF THIS SEAL' not in (face or '') or lock_epoch is None or len(gates) != 1:
        return False
    return all(h[:7] in face for h, s, t in logs if t <= lock_epoch and not gates[0].startswith(h))


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
    return _root_banked(S, 'b712', 88)


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b712_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    """the chain recomputed at commit in three parts: standing-b2a's and standing-b2b's banked quarters (b624-b641, b642-b658) and
    standing-b3's second half (b659-b712), every act AGREE, the boundary link equal, b680 read through its corrigendum row, b712 written LF."""
    ha = S['half_a'] or {}
    v = [tuple(x[:2]) for x in (ha.get('acts') or [])] + [tuple(x[:2]) for x in (S['ar_verify'] or [])]
    r = dict(ha.get('reads') or {}, **(S['ar_reads'] or {}))
    return ha.get('head') == gs(ROOT, 'rev-parse', 'HEAD') and [x[0] for x in v] == ['b%d' % i for i in range(624, 712)] \
        and all(x[1] == 'AGREE' for x in v) and (r.get('b712') or {}).get('crlf') == 0 and (r.get('b680') or {}).get('corrected') == 4 \
        and (ha.get('boundary') or {}).get('equal') is True and S['boundary'].get('equal') is True \
        and (ha.get('boundary') or {}).get('root') == S['boundary'].get('root')


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


def corpus_scope_ok(S):
    """N5: PLACE-papers' changed files within the two ledgers and the named document alone; no rename."""
    ch = S['pp_changed']
    ren = [l for l in S['pp_renames'].split(NL) if l[:1] in ('R', 'D')]
    return bool(ch) and set(ch) <= set(S['pp_allowed']) and 'FINDINGS.md' in ch and 'OPEN_TRAILS.md' in ch and not ren


ENTRY_NEEDLES = ('**The corrigendum**', '**The repairs**', '**The standing clauses**', '**The Independence supplement**', '**The port and the join**',
                 '**The surgery**', '**The coefficients**', '**The axis (e)**', '**The list and the pairs**', '**The registrations**', '**The standing arms**',
                 '**The citation check**', '**The scores.**', '**Read in mutual light**', 'strengthens', '**Carried to:**', '**Next.**', 'b712',
                 'W-ORD-LV-PORT-TAG', 'standing clauses v2', 'Q0', 'DirichletC7Order.lean :501:31')


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
        and 'THE PORT AND THE JOIN' in t and 'THE LIST AND THE PAIRS' in t and 'THE REGISTRATIONS' in t and 'THE STANDING ARMS' in t and '### THE KERNELS' in t \
        and '### THE MIRROR' in t and '### THE CARRY-TIME' in t


# ================================================================== THIS ACT'S ARMS OVER ITS OWN BANKS (Component 5)
NAV_LETTERS = ('d',)          # ### (d) the navigator's, for the author's strike; the rest the seat's; the ruling's two citation misses entered by the fact clause


def defects_ok(S):
    rows = re.findall(r"^    \(([a-z])\) THE (NAVIGATOR|SEAT)'S", S['defects'], re.M)
    want = [list(x) for x in FLOORS['defects']]
    return len(rows) >= len(want) and [list(r) for r in rows[:len(want)]] == want and all(o in ('NAVIGATOR', 'SEAT') for _l, o in rows) \
        and [l for l, o in rows if o == 'NAVIGATOR'][:len(NAV_LETTERS)] == list(NAV_LETTERS)


def repairs_ok(S):
    """(R322)(2): the repairs bank by its JSON (data/b712_tool_repairs.json): the four structural repairs (rows (52)-(55)) and the three item repairs
    ((k), (i), 468), each named; the tracked tools' diffs counted; the two carried tools' repairdiff banks present; the controls 39, one not as
    wanted (defect (d)); both banks tracked, in Component 1's commit."""
    j = S['repairsj']
    rows = [r.get('row') for r in j.get('repairs') or []]
    return rows == ['(52)', '(53)', '(54)', '(55)', '(k)', '(i)', '468'] and sorted(j.get('carried') or []) == ['checks', 'closing'] \
        and all(S['repairdiffs'].get(n) for n in j.get('carried') or []) and len(j.get('tracked') or []) == 7 \
        and j.get('controls') == 39 and j.get('not_as_wanted') == 1 and S['tracked']('data/b712_tool_repairs.txt') and S['tracked']('data/b712_repair_controls.txt') \
        and 'data/b712_tool_repairs.txt' in S['files']['c1']


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
    """the four figures banked by b706's tool over b706's roster against b711's baselines, each at or below b711's; the partners rows one copy
    per table, the figure 0."""
    j, f7 = S['figj'], jl('b711_standing_figures.json')
    figs = dict((k, (j.get(k) or {}).get('figure')) for k in ('correspondence', 'readme', 'partners', 'pins'))
    prev = dict((k, (f7.get(k) or {}).get('figure')) for k in figs)
    pr = (j.get('partners') or {}).get('rows') or []
    return all(isinstance(figs[k], int) and isinstance(prev[k], int) and figs[k] <= prev[k] for k in figs) and figs['partners'] == 0 \
        and len(pr) == 20 and all((r.get('reason') or '').startswith('ONE COPY') for r in pr) and j.get('roster') == 'b706_roster_read.json' \
        and j.get('baseline') == 'b711_standing_figures.json' and 'FIGURES AT b712' in S['figt']


# ================================================================== (R322)(2)-(7) AND N1-N3: THE ACT'S OBJECTS
def standing_v2_ok(S):
    """(R322)(2): data/standing_clauses_v2.txt at VERSION 2, read back by b711's parser (tools/b711_standing.py parse, which b712's standing tool
    imports unchanged) -- v1's 51 rows unchanged as v1 carries them, rows (52)-(55) the four deltas tagged; the control banked as wanted;
    committed alone at relay 4cb4f236 at step zero."""
    import b711_standing as SC
    b, v1 = S['standing_bank'], S['standing_v1']
    rows, rows1 = SC.parse(b), SC.parse(v1)
    c = S['standing_ctlj']
    return bool(re.search(r'^VERSION: 2$', b, re.M)) and len(rows) == 55 and [r[0] for r in rows] == list(range(1, 56)) and rows[:51] == rows1 \
        and len(rows1) == 51 and c.get('ok') is True and c.get('v1_lines_equal') is True and c.get('neg_equal') is False \
        and [r.get('n') for r in c.get('rows') or []] == [52, 53, 54, 55] and all(r.get('equal') and r.get('control_in') for r in c.get('rows') or []) \
        and files_of(ROOT, K.STANDING_COMMIT) == [STANDING_BANK]


def independence_ok(S):
    """(R322)(3): the supplement's verdict -- 19 declarations read at their tags, 18 bearing, T3'' the control object, b711's pattern's misses
    printed (0 of 19, its own hit) -- and the principle's row restated; committed alone at relay 3010867c at step zero."""
    v = unwrap(S['indep'])
    return 'DECLARATIONS READ 19 AT THEIR TAGS' in v and 'BEARING ON INDEPENDENCE 18' in v and 'THE CONTROL OBJECT True' in v \
        and 'THE b711 PATTERN HITS 0 OF 19, ITS OWN HIT True' in v and 'NOT READ 0' in v and 'COMPILED: NOT DEFINITIONS ALONE' in v \
        and sorted(files_of(ROOT, K.INDEPENDENCE_COMMIT)) == ['data/b712_independence.json', 'data/b712_independence.txt']


def repair_controls_ok(S):
    """(R322)(2), by the JSON bank: every case with its section, got, wanted and as_wanted; the seven sections present; the one case not as wanted
    the ruling's control of (2)(i) on b711's banks (defect (d), for the author's strike)."""
    cs = S['repair_ctlj'].get('cases') or []
    bad = [c for c in cs if not c.get('as_wanted')]
    return len(cs) == 39 and sorted(set(c.get('section') for c in cs)) == sorted(['i', 'ii', 'iii', 'iv', 'k', 'i/step', '468']) \
        and all(c.get('as_wanted') == (c.get('got') == c.get('wanted')) for c in cs) and len(bad) == 1 and bad[0].get('section') == 'i' \
        and "THE NAVIGATOR'S" in (re.search(r"^    \(d\) .*$", S['defects'], re.M) or [''])[0]


def membrane_ok(S):
    """(R322)(2)(ii): tools/act_membrane.py's guard read by its text (guard and guard_path, data/act_roots.txt read), the record tool's shared
    writers rebound through it, the suite's writer calling it before every write; its controls (section ii) as wanted."""
    m = strip_prose(S['membrane_src'])
    cs = [c for c in S['repair_ctlj'].get('cases') or [] if c.get('section') == 'ii']
    return 'def guard(' in m and 'def guard_path(' in m and 'act_roots.txt' in m and 'MEM.guard(ACT, name, R.ROOT_EXCLUDE)' in S['rec_src'] \
        and S['suite'].count('_membrane(') >= 8 and len(cs) == 7 and all(c['as_wanted'] for c in cs)


def port_ok(S):
    """(R322)(4): the edit as ordered (one hunk at :212, b709's form at C7OrderBounds.lean :277, the one file changed) and the one run read by its
    id, the artifact's sha256 equal to the platform's digest, 11 of 12 modules built, DirichletC7Order held at :501:31, no grade claimed; the new
    tip's parent b709's commit and its one file the module; in Component 2's commit."""
    j, e = S['portj'], S['portej']
    return e.get('ok') is True and e.get('hunks') == 1 and e.get('line') == K.PORT_LINE and e.get('base') == K.PORT_TIP and e.get('file') == K.PORT_FILE \
        and j.get('run_id') == K.PORT_RUN and (j.get('artifact') or {}).get('agree') is True \
        and (j.get('artifact') or {}).get('sha256') == (j.get('artifact') or {}).get('digest') and (j.get('run') or {}).get('headSha') == K.PORT_NEW_TIP \
        and len(j.get('built') or []) == 11 and len(j.get('modules') or []) == 12 and j.get('held') == ['DirichletC7Order'] \
        and (j.get('first_error') or '').startswith('error: SIDELvConservation/DirichletC7Order.lean:501:31:') and j.get('grade_claimed') is False \
        and j.get('complete') is False and S['lv_tip_parent'] == K.PORT_TIP and S['lv_tip_files'] == [K.PORT_FILE] \
        and 'data/b712_port.txt' in S['files']['c2'] and 'NO GRADE CLAIMED ON THE PORT' in S['portt']


def dispatches_ok(S):
    """N1: at most two runner dispatches -- the dispatch bank one row (the port), the command capture's dispatches the same one; no join dispatched."""
    rows = S['dispj'].get('rows') or []
    return len(rows) == 1 and rows[0].get('run_id') == K.PORT_RUN and rows[0].get('label') == PORT_LABEL and rows[0].get('free_mb', 0) >= K.HOLD \
        and len(S['cmdj'].get('dispatches') or []) == 1 and bool(S['cmds'])


def join_held_ok(S):
    """(R322)(4), N2: the join not reached -- the port at 11 of 12, so SIDE-faces-join's lakefile not re-pinned (its lake files equal to the
    manifest commit's blobs), its tree clean, its main at that commit, no tag, no join-grade bank; the error banked by line."""
    jl_ = S['join_lake']
    return S['join_main'] == K.JOIN_TIP and S['join_tags'] == [] and S['join_status'] == '' and not S['join_grade'] \
        and bool(jl_) and all(a == b for a, b in jl_.values()) and any(a for a, _b in jl_.values()) \
        and 'DirichletC7Order.lean:501:31' in S['portt'] and (S['portj'].get('complete') is False)


def port_tag_order_ok(S):
    """(R322)(4): W-ORD-LV-PORT-TAG entered at OPEN_TRAILS :15848 (the landing bank's line, its head through conv), no lv tag at the port's tip;
    in Component 2's PLACE-papers commit."""
    ls = S['orderj'].get('lines') or []
    ln = ls[0].get('line') if ls else None
    line = oline(S, ln) if ln else ''
    return ln == K.ORDER_LV_PORT_TAG and line.startswith(conv(ls[0].get('head') or '\x00')) and 'W-ORD-LV-PORT-TAG' in line and 'Status OPEN' in line \
        and S['lv_tip_tags'] == [] and 'OPEN_TRAILS.md' in files_of(PP, K.C2_PP)


def _verdict(t):
    m = re.search(r'^### ### \*\*(.*?)\*\*\s*$', t or '', re.M)
    return m.group(1) if m else ''


def surgery_ok(S):
    t, j, h = S['comp']['surgery']
    v = _verdict(t)
    return v.startswith('THE SURGERY HELD') and 'C1 True ; C2 True' in v and 'LAMBDA_MIN 5.7181782' in v and '3.2854063' in v \
        and '0.7395 / 0.9618 / 0.9688' in v and '0.4652 / 0.6453 / 0.6415' in v and '-- NOT FIRED' in t and bool(j) and 'data/b712_surgery.txt' in h


def coeffs_ok(S):
    t, j, h = S['comp']['coeffs']
    v = _verdict(t)
    return 'c(n) NEGATIVE FROM n = 48' in v and 'NEGATIVE COEFFICIENTS 1066 THROUGH 32532' in v and 'C1 True ; C2 True' in v \
        and 'Re rho > 1 IN THE LIST TO 325.0: NONE' in v and bool(j) and 'data/b712_coeffs.txt' in h


def axis_ok(S):
    """(R322)(6): the axis REFUTED as worded, its controls printed (C2 False, the zeta readings under the tail's resolution, printed), the
    falsifier read; the seat's unregistered check printed beside the verdict and not changing it."""
    t, j, h = S['comp']['axis']
    v = _verdict(t)
    return v.startswith('THE AXIS (e) REFUTED') and 'C1 True ; C2 False ; C3 True' in v and 'RADII READ 7 OF 7' in v \
        and 'THE FALSIFIER (:41-:44): the peak near no off-line ordinate FIRED' in t and 'NOT CHANGING IT' in t and bool(j) and 'data/b712_axis.txt' in h


def list_ok(S):
    t, j, h = S['comp']['list']
    v = _verdict(t)
    bands = (j or {}).get('bands') or []
    return 'THE LIST COMPLETE TO 445.0' in v and 'BANDS ABOVE 325 8 (COMPLETE 8)' in v and 'PAIR 11 REACHED ; PAIR 15 REACHED' in v \
        and len(bands) == 8 and all(b.get('complete') for b in bands) and (j or {}).get('top') == 445.0 and 'data/b712_list.txt' in h


def pairs_ok(S):
    """(R322)(7): pairs 11 and 15 against data/b711_registrations.txt (i), the predictions read from data/b711_fit.txt unchanged (the bank's own
    figures against the fit bank's), both WITHIN, the controls before the figures."""
    t, j, h = S['comp']['pairs']
    v = _verdict(t)
    fit = S['fit710']
    return 'pair 11 WITHIN ; pair 15 WITHIN ; THE LAW HELD' in v and 'C2 True' in v and '415: True, 445: True' in v \
        and 'F2 12294837.0' in t and 'F2 14776939.6' in t and '12294837' in fit and '14776940' in fit and '19.065093' in fit and '7.997097' in fit \
        and 'data/b712_pairs.txt' in h


def compute_alone_ok(S):
    """(R322)(5)-(7): each of the five tools writes its own bank alone -- every bank and hashes bank present and tracked; Component 3's commit
    carrying the three of (5)-(6) and Component 4's the two of (7), each tool beside its banks, nothing of another component's."""
    c3, c4 = set(S['files']['c3']), set(S['files']['c4'])
    want3 = set('data/b712_%s%s' % (n, x) for n in ('surgery', 'coeffs', 'axis') for x in ('.txt', '.json', '_hashes.txt')) | set('tools/b712_%s.py' % n for n in ('surgery', 'coeffs', 'axis'))
    want4 = set('data/b712_%s%s' % (n, x) for n in ('list', 'pairs') for x in ('.txt', '.json', '_hashes.txt')) | set('tools/b712_%s.py' % n for n in ('list', 'pairs'))
    return want3 <= c3 and want4 <= c4 and all(S['tracked'](p) for p in want3 | want4)


def controls_first_ok(S):
    """N3: each tool's controls print before its figures -- in each of the five banks the line naming THE CONTROLS stands above the first line of
    THE FIGURES, THE READINGS or THE PAIRS."""
    ok = True
    for n in ('surgery', 'coeffs', 'axis', 'pairs'):
        t = S['comp'][n][0] or ''
        i = t.find('### THE CONTROLS')
        k = min([x for x in (t.find('### THE FIGURES'), t.find('### THE READINGS'), t.find('### THE PAIRS')) if x >= 0] or [-1])
        ok = ok and 0 <= i < k
    lt = S['comp']['list'][0] or ''
    return ok and 'COMPLETE where N = on + 2 off' in lt and lt.find('COMPLETE where N = on + 2 off') < lt.find('  band [')


def registrations_unchanged_ok(S):
    """N3: every registration computed read unchanged from its commit -- data/b711_registrations.txt at b711's commit 41ff1193, at HEAD and in the
    working tree equal, the one commit touching it; data/b709_registrations.txt (the axis row) at the act's base, at HEAD and in the working tree
    equal, untouched this act; the re-read bank's JSON saying so."""
    a, b, c, log = S['regs_b711']
    a9, b9, c9, _l9 = S['regs_b709']
    j = S['regs_rereadj']
    return a is not None and cr0(a) == cr0(b) == cr0(c) and len(log) == 1 and K.REG_B710.startswith(log[0][:7]) \
        and a9 is not None and cr0(a9) == cr0(b9) == cr0(c9) and j.get('unchanged') is True and S['tracked']('data/b712_registrations_reread.txt')


def receipt_ok(S):
    """the banked ferry received in full, its ruling's end and the ferry's tail; by version (b711's repointing, carried): every "standing clauses
    v<N>" the ferry names outside a quotation read against data/standing_clauses_v<N>.txt, present at its VERSION line (this act's ferry names
    v2), and v2's control as wanted."""
    f = S['ferry']
    named = sorted(set(int(m.group(1)) for m in re.finditer(r'standing clauses v(\d+)', re.sub(r'“[^”]*”', '', ' '.join(f.split())), re.I)))
    have = all(re.search(r'^VERSION: %d$' % v, read(os.path.join(D, 'standing_clauses_v%d.txt' % v)) or '', re.M) for v in named)
    return 'RULING (R322) END' in f and f.rstrip().endswith(K.TAIL) and have and S['standing_ctlj'].get('ok') is True


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v2`s control as wanted',
     lambda S: receipt_ok(S), lambda S: put(S, 'ferry', S['ferry'].replace(K.TAIL, ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the step-zero bank: tail, lean, lake, python and claude named, the seat`s claude alone, none of the others; no task stopped, no orphan, nothing stopped by PID',
     lambda S: procs_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('python 0', 'python 1'))),
    ('G-STEPZERO-TESTS', 'the tests bank against the test files tracked before the act, every one run (the lean-running test reading banked prints, b711`s repair), run against the list the page names, the eight not clean named (three carried, five the renames` readers)',
     lambda S: tests_ok(S), lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: S['pushout'][0] == ['data/b711_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'relay`s and PLACE-papers` branch lists by the ruling`s eight names, and the branches bank with port-b707 standing',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{'D:/relay': 'push-b711'}))),
    ('G-READFIRST-CITED', 'the read-first bank: every item of the ferry`s list cited by path and line', lambda S: readfirst_ok(S),
     lambda S: put(S, 'readfirst', '')),
    ('G-ANSWERS-BANKED', 'the answers bank read at HEAD: its prompts and calls at or above the sealed floors (none before the root), each with its options and result, any call after the lock named on the face',
     lambda S: answers_ok(S), lambda S: put(S, 'answers', re.sub(r'(?m)^(### b712 -- THE AUTHOR`S ANSWERS, )(\d+)', lambda m: m.group(1) + str(int(m.group(2)) + 1),
                                                                 S['answers']))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-EXPORT-UNTRACKED', 'the navigator`s export: present, untracked, in no commit', lambda S: S['export_present'] and S['export_log'] == ''
     and S['export_index'] == '' and S['export_status'].startswith('??'), lambda S: put(S, 'export_index', EXPORT)),
    ('G-EDIT-ROUTE', 'the record tool`s one reading (tools/edit_route.py`s arms and sed in any form) over this act`s whole capture and the previous act`s after its post-push suite (b711`s own session, b701`s form), read live',
     lambda S: edit_route_ok(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -n 1p tools/b712_record.py")])),
    ('G-NO-LOCAL-LEAN', 'the act`s command capture, read live: no command of the seat runs lean or lake on this host (N1)', lambda S: no_local_lean(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd='lake env lean ChainProbe.lean')])),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line, found by conv: b711`s weight line, its head line as the closing prints it and the record`s commits beside it', lambda S: weight_ok(S), lambda S: _rl(S, 0, 1)),
    # ### ACT ARMS (Component 5)
    ('G-DRY-STEP-CLEAN', 'the gate`s record: the dry-run step CLEAN, the trail`s Defects and Resolved lines equal to the bank, the gate CLEAR',
     lambda S: dry_step_ok(S), lambda S: put(S, 'gate', '')),
    ('G-CLOSING-DRY-STEP', 'the gate`s record: the closing tool run dry before the lock, its sections read (the repairs, the standing clauses, the supplement, the port, the computations, the list, the registrations, the standing arms, the kernels), every NO VERDICT LINE row read by the bank it names ((R322)(2)(iii): the bank present and carrying no verdict line by the closing`s reader; no list of names)',
     lambda S: closing_dry_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE CLOSING DRY-RUN STEP : CLEAN', 'THE CLOSING DRY-RUN STEP : NOT CLEAN'))),
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, the two misses entered by the fact clause (the head line`s quotation, the Independence lemma`s name), the bank before the step-zero commit and that before Component 1`s',
     lambda S: citation_ok(S), lambda S: put(S, 'citation', '')),
    ('G-R322-ENTERED', 'the trail record`s ratification line', lambda S: '**(R322) ratified.**' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**(R322) ratified.**', '**(R322) read.**'))),
    ('G-ROWGEN-STEPZERO', 'the rowgen bank`s verdict line (the roster re-pointed, 8)', lambda S: rowgen_ok(S), lambda S: put(S, 'rowgen', '')),
    ('G-BRANCHES-BANKED', 'the branches bank through the record tool`s reader: eight named, deleted, merged, banked before the first delete and after the citation check; port-b707 kept at b709`s commit locally and at the remote at step zero',
     lambda S: branches_banked_ok(S), lambda S: _mut(S, 'branchj', lambda d: d['rows'].pop())),
    ('G-DELETES-ONE-BRANCH', 'the command bank: every branch delete one branch (the eight of (R322)(8) alone, port-b707 never), no glob, no variable, nothing chained after',
     lambda S: deletes_one_ok(S), lambda S: put(S, 'cmdt', '')),
    ('G-LISTINGS-BEFORE-CLAUSES', 'N3: the `--merged` listing in the capture before the first delete; every branch deleted among those banked before any delete; the step-zero bank`s listings row',
     lambda S: listings_before_ok(S), lambda S: put(S, 'first_listing_ts', 10 ** 12)),
    ('G-ANSWERS-CHECKED', 'the citation bank`s mid-act prints: the root prompt`s answer checked after the lock, with its time (no mid-act prompt this act)',
     lambda S: answers_checked_ok(S), lambda S: put(S, 'citation', '')),
    ('G-ANSWERS-BEFORE-WRITES', 'the citation bank`s check stamps: every one after the lock and at or before the root, the write it governs (no mid-act answer this act); the answers bank carrying the one prompt; the plant moving every stamp past the root ((R322)(2)(iv))',
     lambda S: answers_before_ok(S), lambda S: answers_plant(S)),
    ('G-SCORER-READS-BANKS', 'the record tool`s scorers: banks alone, no ledger line (data/b686_rules.txt row (1))', lambda S: scorer_banks_ok(S),
     lambda S: put(S, 'rec_src', '')),
    ('G-ENTRY-SCORES-EQUAL', 'the landed entry`s scores line against the scores bank', lambda S: entry_scores_ok(S), lambda S: put(S, 'sc', {})),
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title: by its objects in the ferry`s form adjusted to what the act did (the join held at the port`s line, the surgery`s sign and share, the coefficients` index, the axis, the list`s height and the pairs, Independence`s compiled terminals), compared after case-folding the article alone',
     lambda S: entry_title_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-CORRIGENDUM-ENTERED', 'the generated corrigendum for b711`s post-seal items, landed: the five letters after its seal read as events, the two events of its suite, the letters (l) and (m) it gives; the corrigenda bank appended at row (31)',
     lambda S: corrigendum_ok(S), lambda S: put(S, 'corrj', {})),
    ('G-WRITELIST-MIRROR-STATE', '(R322)(9): the face`s (W) row for the mirror builder naming tools/mirror_prevbuild.json beside the zip and its stage; the record tool`s N5 reading it as the builder`s',
     lambda S: writelist_mirror_state_ok(S), lambda S: put(S, 'face', S['face'].replace('tools/mirror_prevbuild.json', 'tools/mirror_x.json'))),
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b711`s row (1) by version (v2 at VERSION 2), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); no rules bank of this act`s ((R322)(9) names b712`s and b712`s by form)',
     lambda S: rules_row_ok(S), lambda S: put(S, 'rules', '(1) A ROW')),
    ('G-REPORT-UNSEALED', 'the report bank by the unsealed tool after the root`s word and before the root: its stamp after the lock and at or before the root`s, the ferry`s six lines by its JSON, its keys read case-insensitively, the tool unsealed',
     lambda S: report_unsealed_ok(S), lambda S: put(S, 'reportj', dict(S['reportj'], lines=(S['reportj'].get('lines') or [])[:1]))),
    ('G-GUARD-HELD', 'the suite`s writer block guarded by `if PRERUN:` and its dry run banked', lambda S: guard_ok(S), lambda S: put(S, 'guard', '')),
    ('G-POSTROOT-WRITES-NONE', 'the per-part seconds banks` commit times against the root`s', lambda S: postroot_writes_none(S), lambda S: put(S, 'guard', '')),
    ('G-TRAIL-LINES-EQUAL-DEFECTS', 'the landed trail`s Defects and Resolved lines against the owners of the letters entered before the seal ((R322)(2)(i))', lambda S: trail_lines_equal_defects(S),
     lambda S: put(S, 'letters_seal', (S['letters_seal'] or []) + ["(z) THE SEAT'S: A LETTER PLANTED BEFORE THE SEAL AND MISSING FROM THE TRAIL"])),
    ('G-TRAIL-DEFECTS-EQUAL', 'the gate`s record and the landed trail`s Defects line against the repaired reader`s rows', lambda S: trail_defects_ok(S),
     lambda S: put(S, 'gate', '')),
    ('G-TRAIL-RESOLVED-EQUAL', 'the gate`s record and the landed trail`s Resolved line against the bank`s owners', lambda S: trail_resolved_ok(S),
     lambda S: put(S, 'gate', '')),
    ('G-DEFECTS-LETTERED', 'the defects bank: the sealed floors` rows with their owners in order, every one the seat`s',
     lambda S: defects_ok(S), lambda S: put(S, 'defects', '')),
    ('G-TOOL-REPAIRS', 'the repairs bank by its JSON: the four structural repairs (rows (52)-(55)) and the three item repairs ((k), (i), 468), the tracked tools` diffs, the two carried tools` repairdiff banks, the controls 39 with one not as wanted; in Component 1`s commit',
     lambda S: repairs_ok(S), lambda S: _mut(S, 'repairsj', lambda d: d.update(not_as_wanted=0))),
    ('G-ROOTDRY-READY', 'data/b706_rules.txt row (1): the root route run dry on the pre-root tree before the lock, READY True, printed in the face`s (0)',
     lambda S: rootdry_ok(S), lambda S: _mut(S, 'rootdryj', lambda d: d.update(ready=False))),
    ('G-FIGURES-BANKED', 'the four standing figures banked by b706`s tool over b706`s roster against b711`s baselines, each at or below b711`s, the partners figure 0 with one copy per table',
     lambda S: figures_banked_ok(S), lambda S: put(S, 'figj', {})),
    ('G-READFIRST-DIFF-BANKED', 'the closure reader`s diff banked; the readfirst bank unchanged since the step-zero commit', lambda S: readfirst_diff_ok(S),
     lambda S: put(S, 'rf_diff', '')),
    ('G-STANDING-CLAUSES-V2', '(R322)(2): data/standing_clauses_v2.txt at VERSION 2, read back by its parser: v1`s 51 rows unchanged, rows (52)-(55) the four deltas, the control as wanted (its NEG differing), committed alone at step zero',
     lambda S: standing_v2_ok(S), lambda S: put(S, 'standing_bank', S['standing_bank'].replace('and no pipe in any command', 'and no pipe in a command', 1))),
    ('G-INDEPENDENCE-BANKED', '(R322)(3): the supplement`s verdict (19 declarations at their tags, 18 bearing, T3`` the control object, b711`s pattern`s misses printed) and the row restated, committed alone at step zero',
     lambda S: independence_ok(S), lambda S: put(S, 'indep', S['indep'].replace('BEARING ON INDEPENDENCE 18', 'BEARING ON INDEPENDENCE 17'))),
    ('G-REPAIR-CONTROLS', '(R322)(2): the controls bank by its JSON: 39 cases in the seven sections, each as_wanted by got against wanted, the one not as wanted the ruling`s control of (2)(i) (defect (d), the navigator`s)',
     lambda S: repair_controls_ok(S), lambda S: _mut(S, 'repair_ctlj', lambda d: d['cases'].pop())),
    ('G-MEMBRANE-WIRED', '(R322)(2)(ii): tools/act_membrane.py`s guard reading data/act_roots.txt, the record tool`s shared writers rebound through it, the suite`s writers calling it; its seven controls as wanted',
     lambda S: membrane_ok(S), lambda S: put(S, 'membrane_src', S['membrane_src'].replace('def guard_path(', 'def guard_p('))),
    ('G-PORT-BANKED', '(R322)(4): the edit as ordered (one hunk at :212, b709`s form), the one run by its id with the artifact agreeing, 11 of 12 built, DirichletC7Order held at :501:31, no grade claimed; the tip`s parent b709`s commit, one file; in Component 2`s commit',
     lambda S: port_ok(S), lambda S: _mut(S, 'portj', lambda d: d.update(built=(d.get('built') or []) + ['DirichletC7Order']))),
    ('G-DISPATCHES-AT-MOST-TWO', 'N1: at most two runner dispatches -- one this act, the port`s, in the dispatch bank and the capture alike; the join not dispatched',
     lambda S: dispatches_ok(S), lambda S: _mut(S, 'dispj', lambda d: d.update(rows=(d.get('rows') or []) * 3))),
    ('G-JOIN-HELD', '(R322)(4), N2: the join not reached (the port at 11 of 12) -- SIDE-faces-join`s lake files equal to its manifest commit`s, its tree clean, main unmoved, no tag, no join-grade bank; the error banked by line',
     lambda S: join_held_ok(S), lambda S: put(S, 'join_tags', ['v0.1.0'])),
    ('G-PORT-TAG-ORDER', '(R322)(4): W-ORD-LV-PORT-TAG entered at OPEN_TRAILS :15848 (the landing bank`s line, its head through conv), no lv tag at the port`s tip; in Component 2`s PLACE-papers commit',
     lambda S: port_tag_order_ok(S), lambda S: _mut(S, 'orderj', lambda d: d.update(lines=[dict(d['lines'][0], line=1)]))),
    ('G-SURGERY-BANKED', '(R322)(5): the surgery`s bank: the controls C1 and C2 True, the operated form positive definite at both onsets (5.7181782, 3.2854063), the composite shares, the falsifier NOT FIRED, its hashes bank',
     lambda S: surgery_ok(S), lambda S: put(S, 'comp', dict(S['comp'], surgery=(S['comp']['surgery'][0].replace('THE SURGERY HELD', 'THE SURGERY REFUTED'),) + tuple(S['comp']['surgery'][1:])))),
    ('G-COEFFS-BANKED', '(R322)(5): the coefficients` bank: negative from n = 48, 1066 negatives through 32532, no zero with Re rho > 1 in the list to 325, the controls True, its hashes bank',
     lambda S: coeffs_ok(S), lambda S: put(S, 'comp', dict(S['comp'], coeffs=(S['comp']['coeffs'][0].replace('NEGATIVE FROM n = 48', 'NEGATIVE FROM n = 72'),) + tuple(S['comp']['coeffs'][1:])))),
    ('G-AXIS-BANKED', '(R322)(6): the axis`s bank: REFUTED as worded, seven radii read, the controls printed (C2 False, the readings under the tail`s resolution named), the falsifier read, the seat`s check beside the verdict not changing it',
     lambda S: axis_ok(S), lambda S: put(S, 'comp', dict(S['comp'], axis=(S['comp']['axis'][0].replace('THE AXIS (e) REFUTED', 'THE AXIS (e) HELD'),) + tuple(S['comp']['axis'][1:])))),
    ('G-LIST-BANKED', '(R322)(7): the list`s bank: complete to 445.0, eight bands above 325 each COMPLETE by its count, both pairs` heights passed, its hashes bank',
     lambda S: list_ok(S), lambda S: _mut(S, 'comp', lambda d: d['list'][1]['bands'][0].update(complete=False))),
    ('G-PAIRS-BANKED', '(R322)(7): pairs 11 and 15 WITHIN the refined law, the predictions read from data/b711_fit.txt unchanged, the controls C1 and C2, its hashes bank',
     lambda S: pairs_ok(S), lambda S: put(S, 'comp', dict(S['comp'], pairs=(S['comp']['pairs'][0].replace('pair 15 WITHIN ; THE LAW HELD', 'pair 15 OUTSIDE ; THE LAW REFUTED'),) + tuple(S['comp']['pairs'][1:])))),
    ('G-COMPUTE-BANKS-ALONE', '(R322)(5)-(7): each of the five tools beside its own banks alone -- Component 3`s commit the three of (5)-(6), Component 4`s the two of (7), every bank tracked',
     lambda S: compute_alone_ok(S), lambda S: put(S, 'files', dict(S['files'], c4=[]))),
    ('G-CONTROLS-BEFORE-FIGURES', 'N3: in each of the five banks the controls stand above the figures (the list`s completeness rule above its bands)',
     lambda S: controls_first_ok(S), lambda S: put(S, 'comp', dict(S['comp'], pairs=(S['comp']['pairs'][0].replace('### THE CONTROLS FIRST', '### FIRST').replace('### (C2)', '### THE PAIRS (C2)'),) + tuple(S['comp']['pairs'][1:])))),
    ('G-REGISTRATIONS-UNCHANGED', 'N3: every registration computed read unchanged from its commit -- data/b711_registrations.txt at 41ff1193, HEAD and the working tree, one commit; data/b709_registrations.txt at the act`s base, HEAD and the tree; the re-read bank',
     lambda S: registrations_unchanged_ok(S), lambda S: put(S, 'regs_b711', (b'x',) + tuple(S['regs_b711'][1:]))),
    ('G-PARTS-PRERUN', 'the pre-run bank: seven parts, each named with its arms and seconds, the longest under the 590 s guard', lambda S: parts_prerun_ok(S),
     lambda S: put(S, 'prerun', '')),
    ('G-ARM-SECONDS-BANKED', 'the per-part seconds bank gathered before the seal', lambda S: arm_seconds_ok(S), lambda S: put(S, 'asec', {})),
    ('G-SPEC-PLANTED', 'tools/b712_regspec.py`s planted rows run live through the record tool`s readers, and rows of another shape refused',
     lambda S: bool(S['spec']['read']) and all(S['spec']['read']) and all(S['spec']['controls']) and any('runner' in x for x in S['spec']['shapes']),
     lambda S: _mut(S, 'spec', lambda d: d['controls'].append(False))),
    ('G-CONVERSION-ONE', 'every b712 tool`s code: no conversion defined (conv imported from b652_record); the suite importing it',
     lambda S: S['conv_bad'] == [] and 'from b712_record import conv' in S['suite'], lambda S: put(S, 'conv_bad', ['b712_checks.py'])),
    ('G-WORKFLOW-FILES', 'this act`s one run`s workflow: build-module.yml at port-b707`s new tip b707`s blob unchanged, no author identifier, no secret, the hold, the lakefile and its cache step; the print list absent at the branch so the print step is read as not run and no grade claimed (the dispatch row, `whole` False by that reading); this act`s one write on the branch the one module',
     lambda S: wf_ok(S), lambda S: _mut(S, 'wf', lambda d: d[K.KERNEL].update(text=d[K.KERNEL]['text'] + ' secrets.X'))),
    ('G-RUNNER-READ', 'this act`s one run (port-b707 at its new tip) by its id, through the record tool`s reader: at the tip, its conclusion failure, the artifact`s sha256 the port bank`s, the memory low above the hold, no STOP line, the gate NOT DERIVES with no grade claimed, build exit 1 with its 4 error lines',
     lambda S: runner_ok(S), lambda S: _mut(S, 'runner_rows', lambda d: d.update(rows=[dict(r, gate='DERIVES') for r in (d.get('rows') or [])]))),
    ('G-RUNNER-GATE', 'the run`s text bank: the artifact`s digest agreeing, build exit 1, no grade claimed',
     lambda S: gate_ok(S), lambda S: put(S, 'runs', {PORT_LABEL: ''})),
    ('G-MERGES-ON-GATE', 'no merge this act: SIDE-explicit-formula`s main at badaccc with its tags unmoved; SIDE-lv-conservation`s main and deposit unmoved, port-b707 at this act`s one commit locally and at the remote and not on main, no tag; the join kernel`s main at its manifest commit, no tag',
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
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read before the seal (SIDE-lv-conservation read with port-b707 at this act`s one commit and its checkout at main)',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b711`s to b695`s sealed tools and the earlier tools, the readers, the push tool, the act-root tool, the generators` tests, the corrigendum tools, edit_route.py, chain_page.py, the figures tools, b704`s read arm, e0_rule.py, the shared tools and b711`s report tool: before, working tree and HEAD',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'additive_shared.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at the act`s base b0d874f7 but the shared additive files (act_roots.txt and the corrigenda bank among them) and the table`s files, by blob id',
     lambda S: S['prior_bad'] == [] and S['prior_n'] > 0, lambda S: put(S, 'prior_bad', ['data/b711_stepzero.txt'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS before and now', lambda S: S['fi_pre'] is not None and (S['fi_now'] or b'').startswith(S['fi_pre']),
     lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS before and now', lambda S: S['ot_pre'] is not None and (S['ot_now'] or b'').startswith(S['ot_pre']),
     lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-NODISCLOSURE-PUBLIC', 'TECHNE-Core`s needle sets over every public byte the act writes: the ledger lines, the banks, the tools, and the workflow and module at the port branch`s new tip beside them',
     lambda S: bool(S['nd_pub']) and not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', {'method': 1})),
    ('G-OUTSIDE-NAMED-NOWHERE', 'the ledger lines appended', lambda S: S['outside'] == [], lambda S: put(S, 'outside', ['x'])),
    ('G-DELETE-FREE', 'the act`s tools` code, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='os' + '.remove(p)'))),
    ('G-PUBLISH-UNCALLED', 'the act`s tools` code: no publish call', lambda S: publish_uncalled(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='z_' + 'publish()'))),
    ('G-SEALED-AFTER-COMPONENTS', 'the lock time against every relay and PLACE-papers commit of the act by its row in the act`s step bank, data/b712_steps.json ((R322)(2); not by its subject)', lambda S: sealed_after_ok(S),
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b712 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash, the gate`s commit read from the step bank`s one `gate` row ((R322)(3)(ii))',
     lambda S: nothing_ahead_ok(S['face'], S['lock_epoch'], S['rlog'] + S['plog'], S['steps']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'b712_closing.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3), in seven parts summed',
     lambda S: S['lock_epoch'] is not None and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b711`s trail record on OPEN_TRAILS and its root in the chain', lambda S: K.B709_TRAIL_HEAD in S['ot']
     and S['rootsf'].count(NL + 'b711 ') == 1, lambda S: put(S, 'ot', S['ot'].replace('### b711 — lane two', '### b711 - lane two'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], grade_moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 88th chain row (the corrigendum row apart), the root bank and its items against the root route`s own item list (ROOT_EXCLUDE per data/b706_rules.txt row (1), the required list read against it at import), the supplement, the standing control, the repairs, the port, the five computations, the corrigendum and the report among them, no bank the route excludes',
     lambda S: root_banked_ok(S), lambda S: put(S, 'rootsf', S['rootsf'] + 'b712 x y' + NL)),
    ('G-ROOT-BANKS-COMMITTED', 'the root route`s banked reading and every named bank`s blob at the root`s recorded commit: clean and equal at HEAD, HEAD the remote main, the recorded hash carried by the recorded commit',
     lambda S: root_banks_committed_ok(S), lambda S: put(S, 'rootbanks', dict(S['rootbanks'], pushed=False))),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit in three parts by act with the suite`s own remote reads: standing-b2a`s banked b624-b641, standing-b2b`s b642-b658 and standing-b3`s b659-b712 all AGREE, the boundary link equal, b680 read through its corrigendum row (4 banks), b712 written LF',
     lambda S: verify_ok(S), lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s through conv, and its parts, the repairs, the standing clauses, the supplement, the port and the join, the five computations and the registrations among them', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line, the head through conv', lambda S: bool(S['tj'].get('line'))
     and oline(S, S['tj']['line']) == conv(S['REC'].TRAIL_HEAD()), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b712 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b712_record.py agree', 'b712_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line: b712 (R322)(11)', lambda S: '**Next:** b712' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** b712', '**Next:** b713'))),
] + [('G-N%d-SCORED' % i, 'the scores through the record tool`s reader, and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i),
      lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written since b0d874f7 and df2dd7c0 against the (W) globs, the list admitting the next act`s rules file by form',
     lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b712')" in S['suite'] and "'data/b712_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b712_closing.py: the closing sentence in the rule`s words with the plain reads named; the citation check, the record lines, the dry run, the repairs, the standing clauses, the port and the join, the list and the pairs, the registrations, the standing arms, the kernels, the mirror, the carry-time reading',
     lambda S: closing_sentence_ok(S), lambda S: put(S, 'closing_src', S['closing_src'].replace('no identifier of the author ' + 'in any outbound', 'x'))),
    ('G-LSREMOTE-ONE-PER-REPO', 'the part`s ls-remote calls per repository, read after every other arm of the part has run (OPEN_TRAILS :12703)',
     lambda S: lsr_ok(S), lambda S: put(S, 'lsr', {PP: 2})),
    ('G-CORRESPONDENCE-CURRENCY', 'every roster paper`s Correspondence rows by tools/b706_standing_figures.py (b703`s reading over b706`s roster at the unversioned names) against the kernel`s current tag and the statement at the cited tag: the changed-statement rows no more than b711`s figure',
     lambda S: fig_ok(S, 'correspondence'), lambda S: _raise_fig(S, 'correspondence')),
    ('G-README-CURRENCY', 'the PLACE-papers README`s currency rows against ls-remote by tools/b705_standing_figures.py through b706`s (the dated appends and the deposited versions excluded by their text): the stale lines no more than b711`s figure',
     lambda S: fig_ok(S, 'readme'), lambda S: _raise_fig(S, 'readme')),
    ('G-PARTNER-COPIES', 'the lines differing between the two copies of each roster paper`s Correspondence table by tools/b706_standing_figures.py: one copy per table from b706 on, the figure 0, no more than b711`s 0',
     lambda S: fig_ok(S, 'partners'), lambda S: _raise_fig(S, 'partners')),
    ('G-SISTER-PINS', 'each kernel`s lean-toolchain and Mathlib revision beside the federation`s by tools/b703_standing_figures.py through b706`s: no kernel the faces page names moved pin against the baseline',
     lambda S: sister_pins_ok(S), lambda S: _raise_fig(S, 'pins')),
    ('G-READ-RULE-STANDING', 'tools/b704_read_arm.py over the read bank at HEAD (the author`s word at b704`s sort; from b705 every call counts): no Read call of a file of two hundred lines or more without an offset, without a limit or with a limit above two hundred',
     lambda S: read_rule_standing_ok(S), lambda S: _read_plant(S)),
] + [(nm, 'tools/rule_arms.py (the author`s word on (R293)(6); (R301)(6) for four; G-RULE-SUITE-PARTS as repaired under (R302)(2) and (R322)(2); G-RULE-BINARY-HASHES as repaired under (R306)(2); G-RULE-RECUT-QUOTE`s sources as repaired under (R313)(2)) -- ' + reads,
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


def _prev_verdicts(EX):
    """(R322)(2)(iii): each arm's verdict on b711's banks beside b711's own (b711's post-push combine, data/b711_exercise.json `exercise`, its
    `live` per arm): PASS ON PREV; FAILED AS b711 FAILED it; DIVERGE where b711 passed it and it fails here; NOT RUN BY b711 where b711 has no
    row and it fails here (an arm new at b712 that cannot read b711's banks)."""
    own = C3.jl('b711_exercise.json').get('exercise') or {}
    out = dict(pass_on_prev=[], fail_as_prev=[], diverge=[], not_run_by_prev=[])
    for n, e in EX.items():
        if e['live']:
            out['pass_on_prev'].append(n)
        elif n not in own:
            out['not_run_by_prev'].append(n)
        elif (own[n] or {}).get('live') is False:
            out['fail_as_prev'].append(n)
        else:
            out['diverge'].append(n)
    return out


def neg_shown():
    """(R322)(2)(iv), standing clauses v2 row (55): the suite refuses to seal an arm whose NEG control -- the mutated copy, the POS column of a
    part's table (its planted source; the arm must FAIL on it) -- has not been shown to fail, read from the pre-run's exercise banks
    (data/b712_exercise_<part>.json, `mode` prerun, every part's): an arm with no row, whose mutated copy passed, or whose plant or predicate
    raised on it, is not shown. Returns (the arms shown failing, [(arm, why)] the arms not shown)."""
    banks = dict((p, C3.jl('b712_exercise_%s.json' % p)) for p in K.PARTS)
    shown, bad = [], []
    for a in ARMS:
        n, p = a[0], _part_of(a[0])
        j = banks.get(p) or {}
        e = (j.get('exercise') or {}).get(n)
        if j.get('mode') != 'prerun':
            bad.append((n, 'part %s: no pre-run exercise bank (mode %s)' % (p, j.get('mode'))))
        elif e is None:
            bad.append((n, 'part %s: no row in the pre-run' % p))
        elif e.get('pos'):
            bad.append((n, 'the mutated copy PASSED'))
        elif e.get('pos_raised') or not e.get('shown_failing'):
            bad.append((n, 'the mutated copy raised: %s' % e.get('pos_raised')))
        else:
            shown.append(n)
    return shown, bad


def prev_run_missing():
    """(R322)(2)(iii): the parts carrying arms whose run on b711's banks is not banked (data/b712_prevrun_exercise_<part>.json, `mode` prev)."""
    return [p for p in sorted(set(_part_of(a[0]) for a in ARMS)) if C3.jl('b712_prevrun_exercise_%s.json' % p).get('mode') != 'prev']


def seal():
    face = read(FACE)
    lock = utc_epoch(face, 'locked at (UTC)')
    p = os.path.join(D, 'b712_seal_hashes.json')
    if lock is None:
        print('### THE FACE IS NOT LOCKED -- NOTHING RECORDED')
        return 3
    if os.path.exists(p):
        print('### THE HASHES ARE RECORDED ALREADY -- NOTHING RECORDED TWICE')
        return 3
    shown, bad = neg_shown()
    missing = prev_run_missing()
    if bad or missing:
        print('### (R322)(2)(iv): %d OF %d ARMS WITHOUT THEIR NEG CONTROL SHOWN FAILING ON A MUTATED COPY IN THE PRE-RUN:' % (len(bad), len(ARMS)))
        for n, why in bad:
            print('  %-46s %s' % (n, why))
        print('### (R322)(2)(iii): THE PARTS WHOSE ARMS ARE NOT RUN ON b711`S BANKS BEFORE THE SEAL: %s' % (missing or 'NONE'))
        print('### ### **THE SEAL REFUSED -- NOTHING RECORDED.**')
        return 3
    dtext = rd('b712_defects.txt')
    now = sealed_now()
    # ### (R322)(2)(i): the letters entered before the seal, recorded with it -- the trail's lines and the three trail-equality arms read these
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), lock=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(lock)), tools=now,
             relay_head=gs(ROOT, 'rev-parse', 'HEAD'), letters=REC0.letters_of(dtext), defects_sha256=hashlib.sha256(dtext.encode('utf-8')).hexdigest(),
             neg_shown=len(shown), prev_run=dict((p_, dict((k_, len(v_)) for k_, v_ in C3.jl('b712_prevrun_exercise_%s.json' % p_).items()
                                                          if k_ in ('pass_on_prev', 'fail_as_prev', 'diverge', 'not_run_by_prev')))
                                                 for p_ in sorted(set(_part_of(a[0]) for a in ARMS))))
    b = (json.dumps(j, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    _membrane(p)
    with open(p + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(p + '.tmp', p)
    for t in K.SEALED:
        print('  %-38s %s' % (t, now[t]))
    print('  the letters entered before the seal %d: %s' % (len(j['letters']), ', '.join(s[:3] for s in j['letters']) or 'NONE'))
    print('  the arms with their NEG control shown failing %d of %d ; the runs on b711`s banks %s' % (len(shown), len(ARMS), j['prev_run']))
    print('  written: b712_seal_hashes.json')
    return 0


def _base_name(pushed):
    if PREV:
        return 'b712_prevrun.txt'
    if PRERUN:
        return 'b712_arms_prerun.txt'
    if MID and len(sys.argv) > sys.argv.index('--mid') + 1:
        return sys.argv[sys.argv.index('--mid') + 1]
    if RERUN and len(sys.argv) > sys.argv.index('--rerun-postpush') + 1:
        return sys.argv[sys.argv.index('--rerun-postpush') + 1]
    return 'b712_checks_postpush.txt' if pushed else 'b712_checks.txt'


def _part_name(base, part):
    return base.replace('.txt', '_%s.txt' % part)


def _membrane(p):
    """(R322)(2)(ii), standing clauses v2 row (53): the membrane before every bank this suite writes (tools/act_membrane.py guard_path, this act's
    ROOT_EXCLUDE): the post-push parts' banks are excluded kinds (checks*, lsr*, exercise*, chain_*); the pre-run's, the run on b711's banks and
    the seal's record are root items, refused once the root is appended."""
    import act_membrane as MEM
    MEM.guard_path('b712', p, REC0.R.ROOT_EXCLUDE)


def _write(name, lines):
    out = os.path.join(D, name)
    b = (NL.join(lines) + NL).encode('utf-8')
    _membrane(out)
    with open(out + '.tmp', 'wb') as fh:
        fh.write(b)
    os.replace(out + '.tmp', out)
    return out


def writer_plan(prerun, rerun, mid, pushed):
    """the banks the writer block at the end of a part would write, by mode -- the part bank and the ls-remote bank in every mode, the exercise
    bank in every mode, the per-part seconds bank under `if PRERUN:` alone. Read by `--guard-dry`; the writer block beneath follows this plan
    exactly (the arm G-GUARD-HELD reads the block's own text)."""
    base = 'b712_arms_prerun.txt' if prerun else ('b712_checks_postpush.txt' if (rerun or pushed) else 'b712_checks.txt')
    out = [('data/' + _part_name(base, '<part>')), ('data/' + _part_name(base, '<part>').replace('b712_arms_prerun', 'b712_lsr_prerun').replace('b712_checks', 'b712_lsr').replace('.txt', '.json')),
           'data/b712_exercise_<part>.json']
    seconds = ['data/b712_arm_seconds_<part>.json'] if prerun else []
    return out, seconds


def guard_dry():
    for mode, args in (('prerun', (True, False, False, False)), ('pre-push', (False, False, False, False)), ('post-push', (False, True, False, True))):
        out, seconds = writer_plan(*args)
        print('  MODE %-9s | the part`s banks: %s | the per-part seconds bank: %s' % (mode, ', '.join(out), ', '.join(seconds) or 'NONE'))
    print('  ### POST-ROOT PATH WRITES NONE of the root-named per-part seconds banks: the pre-push and post-push modes write no data/b712_arm_seconds_<part>.json')
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
        ex.update(jl('b712_exercise_%s.json' % part).get('exercise') or {})
    if ex and base in ('b712_checks.txt', 'b712_checks_postpush.txt'):
        e = (json.dumps(dict(exercise=ex, run=n, live_failing=fails, defective=defs, neg_failures=ng), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p_ = os.path.join(D, 'b712_exercise.json')
        _membrane(p_)
        with open(p_ + '.tmp', 'wb') as fh:
            fh.write(e)
        os.replace(p_ + '.tmp', p_)
    print(NL.join(out[3:16]))
    print('  written: %s' % base)
    return 0 if ok else 1


# ### the carried failures declared on the face by name (section (0)): G-READ-RULE-STANDING failing on defect (a)'s whole read at the opening (the
# ### harness's persisted output of 382 lines, read without an offset or a limit) and defect (i)'s thirty calls (relay data/b712_read_calls.txt);
# ### G-EDIT-ROUTE failing on defect (a)'s four sed commands at the opening (relay data/b712_commands.txt); G-RULE-HEAD-LINE-QUOTED failing on
# ### b711's closing :1 carrying its capture-name failure (b711's defect (k)), which the ruling's (1) does not quote. The combine reads them by
# ### name, and no other failure is carried.
CARRIED_FAILING = ('G-READ-RULE-STANDING', 'G-EDIT-ROUTE', 'G-RULE-HEAD-LINE-QUOTED')


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
    pushed = RERUN or (not PRERUN and not MID and not PREV and is_pushed())
    base = _base_name(pushed)
    rec('=' * 104)
    rec('b712 -- THE SUITE. ### **%s READING.** ### PART %s ### every arm exercised on both controls.' % (
        'ON b711`S BANKS ((R322)(2)(iii))' if PREV else 'PRE-SEAL (R202)(3)' if PRERUN else 'MID-ACT' if MID else 'POST-PUSH' if pushed else 'PRE-PUSH', PART))
    rec('### the host`s free memory at the part`s start %d MB (the hold %d MB)' % (fm, K.HOLD))
    if PRERUN or MID:
        rec('### run at (UTC) : %s   ### %s' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                                              'the standing line of (R202)(3): every arm run at HEAD before the face is sealed, its count printed.'
                                              if PRERUN else 'a mid-act re-run; no table regenerated.'))
    rec('=' * 104)
    S = sources(NEED[PART])
    S['pushed'] = pushed
    if PART == 'standing-b3':
        jh = _JL_OWN or jl
        a1, a2 = jh(half_bank('a1', _run_key(base))), jh(half_bank('a2', _run_key(base)))
        S['half_a'] = dict(head=a1.get('head') if a1.get('head') == a2.get('head') else None, acts=(a1.get('acts') or []) + (a2.get('acts') or []),
                           reads=dict(a1.get('reads') or {}, **(a2.get('reads') or {})), boundary=a2.get('boundary') or a1.get('boundary') or {})
    t1 = time.time()
    regen = PART == 'act' and not (RERUN or PRERUN or MID or PREV)
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
    rec('  ### (R264)(2) THE FREEZE: the standing arms (b711`s face less its own arms, the twenty-four rule arms and G-READ-RULE-STANDING among them; none added) %d ; '
        'carried here %d ; the act`s arms over its own banks %s ; arms beyond both %s' % (
            len(S['standing']), len(set(names) & set(S['standing'])), sorted(set(names) - set(S['standing'])),
            sorted(set(names) - set(S['standing']) - set(K.ACT_ARMS)) or 'NONE'))
    rec('  ### standing arms not carried here: %s' % (sorted(set(S['standing']) - set(names)) or 'NONE'))
    if 'figures' in NEED[PART]:
        rec('  ### THE FOUR STANDING FIGURES, each against the previous act`s (%s):' % S['fig_prev_name'])
        for k in ('correspondence', 'readme', 'partners', 'pins'):
            rec('  ###   %-15s live %s ; previous %s' % (k, (S['fig'].get(k) or {}).get('figure'), (S['fig_prev'].get(k) or {}).get('figure')))
        ok_, n_, off_, pre_, form_ = RDA.reading_text(S['reads_bank'])
        rec('  ### G-READ-RULE-STANDING`S READING (relay data/b712_read_calls.txt): %s ; rows %d ; offences %d %s ; the cap`s precursors %d' % (
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
            rec('  ### the reads at commit, b680: %s ; b712: %s' % (S['ar_reads'].get('b680'), S['ar_reads'].get('b712')))
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
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (this act`s one commit on %s, kept; the port run %s, %s, %d of %d modules, read by its id) ; the join kernel main %s' % (
        S['ef_main'][:12], (S['ef_tags'].get('v0.37') or '')[:12], S['lv_main'][:12], (S['lv_v0100'] or '-')[:12], (S['lv_port'] or '-')[:12], K.PORT_TIP[:12],
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
        pos_raised = None   # ### (R322)(2)(iv): a plant or a predicate that raised on the mutated copy has not SHOWN the control failing
        try:
            m = pos(copy.copy(S))
            if isinstance(m, dict):
                posv = bool(pred(m))
            else:
                posv, pos_raised = False, 'the plant returned no source'
        except Exception as e:
            posv, pos_raised = False, '%s: %s' % (type(e).__name__, str(e)[:120])
        SECS[name] = round(time.time() - ta, 4)
        if not live:
            fail.append(name)
        if neg != live:
            negfail += 1
        if posv:
            defective.append(name)
        EX[name] = dict(live=live, neg=neg, pos=posv, pos_raised=pos_raised, shown_failing=(not posv and pos_raised is None), reads=reads, secs=SECS[name])
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
    pv = _prev_verdicts(EX) if PREV else {}
    if PREV:
        rec('  ### (R322)(2)(iii) THE ARMS ON b711`S BANKS, beside b711`s own verdicts (relay data/b711_exercise.json, b711`s post-push combine):')
        for k_ in ('pass_on_prev', 'fail_as_prev', 'diverge', 'not_run_by_prev'):
            rec('  ###   %-16s %d %s' % (k_.upper(), len(pv[k_]), pv[k_] or ''))
        rec('  ### ### **ON b711`S BANKS: PASS %d ; FAILED AS b711 FAILED %d ; DIVERGE %d (b711 passed, here failed) ; NOT RUN BY b711 %d (here failed).**' % (
            len(pv['pass_on_prev']), len(pv['fail_as_prev']), len(pv['diverge']), len(pv['not_run_by_prev'])))
    secs = time.time() - t_start
    rec('  ### the arms` own seconds summed %.1f, the slowest %s' % (sum(SECS.values()), ', '.join('%s %.2f' % kv for kv in sorted(SECS.items(), key=lambda x: -x[1])[:3]) or 'NONE'))
    rec('  ### the run took %.0f s' % secs)
    rec('  ### PART %s : ARMS %d ; LIVE PASSING %d ; LIVE FAILING %d %s ; NEGATIVE-CONTROL FAILURES %d ; POSITIVE-CONTROL PASSES %d %s ; '
        'DECLARED EQ RUN %s ; %d s' % (PART, len(arms), len(arms) - len(fail), len(fail), json.dumps(fail) if fail else 'NONE', negfail, len(defective),
                                       json.dumps(defective) if defective else 'NONE', S['declared_eq_run'], int(secs)))
    rec('=' * 104)
    out = _write(_part_name(base, PART), L)
    lp = os.path.join(D, _part_name(base, PART).replace('b712_arms_prerun', 'b712_lsr_prerun').replace('b712_checks', 'b712_lsr').replace('.txt', '.json'))
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    _membrane(lp)
    with open(lp + '.tmp', 'wb') as fh:
        fh.write(lb)
    os.replace(lp + '.tmp', lp)
    ex = dict(exercise=EX, run=len(arms), live_failing=fail, defective=defective, neg_failures=negfail, part=PART,
              mode='prev' if PREV else 'prerun' if PRERUN else 'mid' if MID else 'post-push' if pushed else 'pre-push',
              at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), relay_head=gs(ROOT, 'rev-parse', 'HEAD'))
    ex.update(pv)
    ep = os.path.join(D, ('b712_prevrun_exercise_%s.json' if PREV else 'b712_exercise_%s.json') % PART)
    _membrane(ep)
    with open(ep + '.tmp', 'wb') as fh:
        fh.write((json.dumps(ex, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(ep + '.tmp', ep)
    # ### THE GUARD HELD -- the per-part seconds bank (root-named, gathered by the record tool's armsecs before the seal) is written by the pre-run
    # ### alone, as tools/b700_checks.py :1669 had it and b702 restored; the pre-push and post-push runs write no root-named bank
    if PRERUN:
        sp = os.path.join(D, 'b712_arm_seconds_%s.json' % PART)
        _membrane(sp)
        with open(sp + '.tmp', 'wb') as fh:
            fh.write((json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), part=PART, arms=SECS, phases=S['phase_secs'], run_secs=int(secs)),
                                 indent=1, ensure_ascii=False) + NL).encode('utf-8'))
        os.replace(sp + '.tmp', sp)
    print('  written: %s' % os.path.basename(out))
    if PREV:
        return 0 if not (pv['diverge'] or pv['not_run_by_prev']) else 1
    carried_only =[f for f in fail if f not in CARRIED_FAILING] == [] and not defective and negfail == 0
    return 0 if (not fail and not defective and negfail == 0) else (4 if carried_only else 1)


class _PrevWorklist(object):
    """(R322)(2)(iii): the worklist a run on b711's banks reads -- b711's value for every name b711's worklist carries, this act's for the suite's
    own structure (the arms by part, the parts, the hold, the chain's halves) and for a name b711's lacks."""
    OWN = ('ACT_ARMS', 'PARTS', 'HOLD', 'CHAIN_HALVES', 'CHAIN_QUARTERS', 'STANDING_ADDED')

    def __init__(self, own, prev):
        self._own, self._prev = own, prev

    def __getattr__(self, n):
        if n not in self.OWN and hasattr(self._prev, n):
            return getattr(self._prev, n)
        return getattr(self._own, n)


_JL_OWN = None   # defect (j): the chain halves are this run's own banks, read past the rebinding


def _prev_rebind():
    """(R322)(2)(iii), `--prev`: every bank the arms read through rd and jl under this act's prefix read as b711's (data/b712_<x> as
    data/b711_<x>), the face b711's, the worklist through _PrevWorklist, the pre-act heads b711's. The tools stay this act's; the banks alone are
    the previous act's. An arm whose source the rebinding does not reach (a literal path, a b712-only bank) reads this act's and is printed as it
    falls, beside b711's own verdict."""
    global rd, jl, FACE, K, PRE, _JL_OWN

    def pv(n):
        return ('b711_' + n[5:]) if isinstance(n, str) and n.startswith('b712_') else n

    rd0, jl0 = rd, jl
    _JL_OWN = jl0
    rd = lambda n: rd0(pv(n))   # noqa: E731
    jl = lambda n: jl0(pv(n))   # noqa: E731
    FACE = B707_FACE
    K = _PrevWorklist(K, K707)
    PRE = dict(relay=K707.PRE_RELAY, pp=K707.PRE_PP)


if PREV:
    _prev_rebind()


if __name__ == '__main__':
    sys.exit(main())
