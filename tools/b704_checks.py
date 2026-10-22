# -*- coding: utf-8 -*-
"""b704_checks.py -- THE SUITE OF b704, UNDER (R314): b703 AT ITS WEIGHT; THE UNLETTERED READ BY CORRIGENDUM AND THE READ RULE SORTED INTO AN
ARM; THE FACES CHAIN RE-PROBED AT v0.37 ON ONE DISPATCH WITH TWO NODES; THE CORRESPONDENCE CELLS OF A MOVED TAG READ; THE README, THE GLOSSARY
COMPANIONS AND THE NEXT DOCUMENT RE-CUT; SIX PARTS, THE CHAIN SPLIT BY ACT.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### data/b684_rules.txt row (1) and b693's split: every run in SIX foreground parts, each its own call in its own message -- `--part
### standing-a`, `--part standing-c` (G-PRIORBANK-UNCHANGED, G-NODISCLOSURE-PUBLIC, G-WRITELIST-KINDS, the four standing figures and
### G-READ-RULE-STANDING), `--part standing-b1` (the shared additive files), `--part standing-b2` (the act-root chain's first half, b624-b658, its
### verdicts banked, NO ARM), `--part standing-b3` (the second half, b659-b704, and G-ACTROOT-VERIFY once over both halves' verdicts), `--part act`
### (the act's arms over this act's banks, the table regenerated in a closing run); each under the 590 s guard, NOT RUN beneath the 2,560 MB hold;
### `--combine <bank>` writes the bank. The chain halves as b693 drew them with b704 added to the second (the ferry's Component 5).
### ### (R264)(2), THE FREEZE: the standing arms are b703's face's (G2) arms less b703's own arms over b703's banks, carried, the twenty-four rule
### arms of tools/rule_arms.py among them; and the one standing arm (R314)(2) adds on the author's word, G-READ-RULE-STANDING (tools/b704_read_arm.py
### over the repaired read bank), which FAILS at b704 on defects (i) and (o) and is declared on the face as a carried failure; G-README-CURRENCY
### fails on README :135, the append written on the author's word (defect (n)), and is declared beside it. The four standing figures
### read against b703's (data/b703_standing_figures.json). The standing runner arms (G-WORKFLOW-FILES, G-RUNNER-READ, G-RUNNER-GATE,
### G-MERGES-ON-GATE) read THIS ACT'S ONE RUN, the faces probe on the scratch branch probe-b704 (run 39721668586), and SIDE-explicit-formula's
### main unmoved at v0.37: no merge this act.
### ### The PRERUN guard held: the per-part seconds bank is written under `if PRERUN:` alone, so no root-named bank is written by the pre-push or
### post-push run; `--guard-dry` prints, for each run mode, what the writer block would write, writing nothing.
### ### Every look-up of a landed line goes through the one conversion (imported from tools/b652_record.py through tools/b704_record.py).
### ### The harness is b568's to b703's, written by the Write tool from tools/b703_checks.py, its pure helpers imported from it (tools/b703_checks.py,
### ### sealed at b703 and unedited); the sources, predicates and arms over this act's banks are b704's. data/b686_rules.txt row (1): the act arm
### ### G-ENTRY-SCORES-EQUAL reads the landed entry; no scorer reads a ledger line.
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
import b704_worklist as K     # noqa: E402
import b704_record as REC0    # noqa: E402  ### imported before b703's suite: b703's record tool is then imported once, by b704's, and rebound
from b704_record import conv  # noqa: E402
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
root_banks_committed_ok, kernels_untouched, corpus_scope, lsr_ok, g2_names, no_delete, publish_uncalled = (
    C3.root_banks_committed_ok, C3.kernels_untouched, C3.corpus_scope, C3.lsr_ok, C3.g2_names, C3.no_delete, C3.publish_uncalled)
_rl, _mut, _live, _planted, _raise_fig, fig_ok, sister_pins_ok, wl_ok = C3._rl, C3._mut, C3._live, C3._planted, C3._raise_fig, C3.fig_ok, C3.sister_pins_ok, C3.wl_ok
_post_seal_named, edit_route_ok, PART_FOOT, KIND = C3._post_seal_named, C3.edit_route_ok, C3.PART_FOOT, C3.KIND

NL = chr(10)
PP = K.PP
KI = K.KERNEL_DIR             # ### the kernel this act probed: SIDE-explicit-formula (nothing written on its main)
FACE = os.path.join(D, 'b704_registration_2026-10-21.txt')
B703_FACE = os.path.join(D, 'b703_registration_2026-10-21.txt')
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
FLOORS = dict(prompts=12, calls=8, checks=12, defects=(('a', 'SEAT'), ('b', 'SEAT'), ('c', 'SEAT'), ('d', 'SEAT'), ('e', 'SEAT'), ('f', 'NAVIGATOR'),
                                                      ('g', 'NAVIGATOR'), ('h', 'SEAT'), ('i', 'SEAT'), ('j', 'SEAT'), ('k', 'NAVIGATOR'), ('l', 'SEAT'),
                                                      ('m', 'SEAT'), ('n', 'NAVIGATOR'), ('o', 'SEAT'), ('p', 'SEAT')))
REPAIRED_TOOLS = K.REPAIRED_TOOLS
NEW_TOOLS = K.NEW_TOOLS
# ### the instruments read unedited: b703's list with tools/rule_arms.py (repaired at b703, unedited at b704), b695's to b703's sealed tools,
# ### b703's new and repaired tools, less this act's sealed tools
INST_BASE = tuple(C3.INST_BASE) + ('rule_arms.py', 'b703_standing_figures.py')
INST = tuple(sorted((set(INST_BASE) | set(K695.SEALED) | set(K696.SEALED) | set(K697.SEALED) | set(K698.SEALED) | set(K699.SEALED) | set(K700.SEALED)
                     | set(K701.SEALED) | set(K702.SEALED) | set(K703.SEALED) | set(K703.NEW_TOOLS) | set(K703.REPAIRED_TOOLS))
                    - set(K.SEALED) - set(REPAIRED_TOOLS) - set(NEW_TOOLS)))
# ### the corpus documents this act does not write: b703's list less the three this act writes (the README, the faces page, One Page Proof)
CURRENTS = tuple(p for p in C3.CURRENTS if p not in ('README.md', 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md', 'day1/ONE_PAGE_PROOF.md'))
TABLE_FILES = K.TABLE_FILES
WF, PT = '.github/workflows/build-module.yml', 'print_targets.txt'
B1_ARMS = ('G-SHARED-ADDITIVE',)        # ### standing-b1: the shared additive files
B2_ARMS = ()                            # ### standing-b2: the chain's first half, its verdicts banked, no arm
B3_ARMS = ('G-ACTROOT-VERIFY',)         # ### standing-b3: the chain's second half and the arm over both halves
C_ARMS = ('G-PRIORBANK-UNCHANGED', 'G-NODISCLOSURE-PUBLIC', 'G-WRITELIST-KINDS', 'G-CORRESPONDENCE-CURRENCY', 'G-README-CURRENCY', 'G-PARTNER-COPIES',
          'G-SISTER-PINS') + K.STANDING_ADDED   # ### standing-c: the written files, the four figures and the read arm
NEED = {'standing-a': ('live', 'rules'), 'standing-c': ('written', 'figures'), 'standing-b1': ('additive',), 'standing-b2': ('chain_a',),
        'standing-b3': ('chain_b',), 'act': ('efremote',)}
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
STD3 = ('Classical.choice', 'Quot.sound', 'propext')
PROBE_LABEL = 'probe'
GONE = ('probe-b704', 'widening-b701', 'epstein-b703')   # ### the three kernel branches this act deleted, local and remote


def rec(s=''):
    L.append(s)
    print(s)


def is_pushed():
    return (gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith('b704')
            and 'data/b704_components.txt' in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    """tools/rule_arms.py's sources over the seat's session from (R314)'s anchor, its call trace extended by any continuation session's
    (K.SESSIONS_AFTER, none so far) through rule_arms.transcript."""
    R_ = RA.sources('b704', SESSION, K.ANCHOR, K.PARTS, lock, PRE['relay'], PRE['pp'])
    for sid, anc in K.SESSIONS_AFTER:
        R_['calls'] = list(R_.get('calls') or []) + RA.transcript('%s/%s.jsonl' % (PROJ, sid), anc)
    return R_


def conv_alone():
    P = 'p' + 'oss('
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to',
            'def ' + 'conv(']
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b704_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks):
                bad.append(f)
    return bad


def spec_planted():
    import b704_regspec as SPEC
    P = SPEC.planted()
    ctl = [ok for _w, ok in SPEC.controls()]
    return dict(read=[ok for _s, ok, _w in P], controls=ctl, shapes=[s for s, _o, _w in P])


def _deps(ax):
    return REC0._deps(ax)


def _tag_peel(tag):
    return gs(KI, 'rev-parse', '--verify', '--quiet', 'refs/tags/%s^{commit}' % tag)


def wf_state():
    """the kernel this act probed: its workflow at main against the commit that last wrote it (before the act), its lakefile's Mathlib requirement,
    its print list against the probe run's print bank, the files this act wrote on its main (none)."""
    t = read_blob(KI, 'main:' + WF)
    wrote = gs(KI, 'log', '-1', '--format=%H', 'main', '--', WF)
    lf = read_blob(KI, 'main:lakefile.toml') + read_blob(KI, 'main:lakefile.lean')
    req = re.search(r'(?im)^\s*require\b[^\n]*mathlib', lf) or re.search(r'(?is)\[\[require\]\][^\[]*name\s*=\s*"mathlib"', lf)
    pt = read_blob(KI, 'main:' + PT)
    return {K.KERNEL: dict(text=t, before=read_blob(KI, '%s:%s' % (wrote, WF)) if wrote else '', wrote=wrote,
                           wrote_before_act=bool(wrote) and git(KI, 'merge-base', '--is-ancestor', wrote, K.EF_MAIN_BEFORE)[0] == 0,
                           lakefile=bool(lf.strip()), mathlib=bool(req), targets=[l.strip() for l in pt.split(NL) if l.strip()],
                           printed=len(_deps(rd('b704_axioms_%s_%s.txt' % (K.KERNEL, PROBE_LABEL)))),
                           act_writes=sorted(set(x for x in gs(KI, 'diff', '--name-only', K.EF_MAIN_BEFORE, 'main').split(NL) if x.strip())),
                           want=[])}


def _ef_sorry_code():
    """`sorry` tokens OUTSIDE comments and strings in every module under SIDEExplicitFormula/ at main, through tools/no_sorry_main.py's lean_code."""
    import no_sorry_main as NSM
    out = []
    for f in gs(KI, 'ls-tree', '-r', '--name-only', 'main', '--', 'SIDEExplicitFormula').split(NL):
        if f.strip().endswith('.lean'):
            out += ['%s:%d: %s' % (f.strip(), ln, t.strip()) for ln, t in NSM.sorry_hits(read_blob(KI, 'main:' + f.strip()))]
    return NL.join(out)


STANDING = sorted((set(g2_of(B703_FACE)) - set(K703.ACT_ARMS)) | set(K.STANDING_ADDED))
TESTS = ('test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py')


# ================================================================== THE CHAIN SPLIT BY ACT (b693's, the halves as b693 drew them, b704 added)
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
    return base.replace('b704_', '').replace('.txt', '')


def half_bank(i, key):
    return 'b704_chain_half_%s_%s.json' % ('ab'[i], key)


def write_half(i, key, verdicts, reads):
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), head=gs(ROOT, 'rev-parse', 'HEAD'), half='%s-%s' % K.CHAIN_HALVES[i],
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
    rule arms' trace), 'written' (the written files, the public bytes, the prior banks), 'figures' (the four standing figures), 'chain_a' and
    'chain_b' (the act-root chain's two halves), 'additive' (the shared files), 'efremote' (one ls-remote of the kernel this act probed, the act
    part alone: v0.36, v0.37, main and the three deleted branches at the remote)."""
    import b616_record as R6
    import edit_route as ER
    import b641_record as R41
    import additive_shared as ADD
    REC = REC0
    face = read(FACE)
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b704_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if (f.startswith('b704_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS)
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    cit = jl('b704_citation_check.json')
    try:
        REC.R._defect_short()
        refuses = False
    except TypeError:
        refuses = True
    t0 = time.time()
    cmds = capture_now()
    S = dict(
        REC=REC, ER=ER, face=face, ferry=rd('b704_ferry.txt'), scan=rd('b704_ferry_scan.txt'), stepz=rd('b704_stepzero.txt'),
        readfirst=rd('b704_readfirst.txt'), defects=rd('b704_defects.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        answers=rd('b704_author_answers.txt'), answersj=jl('b704_author_answers.json'), prerun=rd('b704_arms_prerun.txt'), rl=jl('b704_record_lines.json'),
        tests=jl('b704_tests_stepzero.json'), testst=rd('b704_tests_stepzero.txt'), withheld=jl('b704_tests_withheld.json'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b704_seal_hashes.json'), sealnow=sealed_now(), cmds=cmds, prev_cmds=prev_now(), cmdj=jl('b704_commands.json'),
        cmdt=rd('b704_commands.txt'), reads_bank=rd('b704_read_calls.txt'), reads_json=jl('b704_read_calls.json'), read_sort=rd('b704_read_sort.txt'), read_ctl=rd('b704_read_arm_control.txt'),
        planted={t: run_test(t) for t in TESTS}, spec=spec_planted(), conv_bad=conv_alone(), suite=read(os.path.join(T, 'b704_checks.py')),
        citation=rd(K.CITATION_BANK), cit_at=iso_epoch(cit.get('at') or ''), cit_misses=cit.get('misses') or [],
        gate=rd('b704_reg_gate.txt'), rowgen=rd('b704_rowgen_stepzero.txt'),
        branchj=jl('b704_branches.json'), branchbj=jl('b704_branches_before.json'), branchest=rd('b704_branches.txt'),
        branch_lists=dict((repo, gs(repo, 'branch', '--list', *bs)) for repo, bs in K.DELETE),
        repairs=rd('b704_tool_repairs.txt'), rec_src=read(os.path.join(T, 'b704_record.py')),
        closing_src=read(os.path.join(T, 'b704_closing.py')),
        defshort=dict(b703=len(REC._defect_short('b703')), refuses=refuses),
        defshort_b704=REC._defect_short('b704'),
        corrj=jl('b704_corrigendum.json'), corrt=rd('b704_corrigendum.txt'), corrigenda=rd('b675_corrigenda.txt'),
        corrigenda_tri=tri(ROOT, 'data/b675_corrigenda.txt', PRE['relay']),
        guard=rd('b704_guard_dry.txt'), guardj=jl('b704_guard_dry.json'),
        nodes=rd('b704_nodes_zeta.txt'), nodesdiff=rd('b704_nodes_diff.txt'), probediff=rd('b704_probe_diff.txt'),
        probet=rd('b704_runner_%s_%s.txt' % (K.KERNEL, PROBE_LABEL)), probej=jl('b704_runner_%s_%s.json' % (K.KERNEL, PROBE_LABEL)),
        probeax=rd('b704_axioms_%s_%s.txt' % (K.KERNEL, PROBE_LABEL)), dispj=jl('b704_dispatches.json'),
        facesj=jl('b704_faces_diff.json'), facest=rd('b704_faces_diff.txt'),
        faces_now=read(os.path.join(PP, K.FACES_PAGE)), faces_head=read_blob(PP, 'HEAD:' + K.FACES_PAGE),
        cellsdry=rd('b704_correspondence_dry.txt'), cellsrun=rd('b704_correspondence_run.txt'), reach=rd('b704_cells_reach.txt'),
        readme_bank=rd('b704_readme.txt'), readme_now=read(os.path.join(PP, 'README.md')), gloss=rd('b704_glossary.txt'),
        tie=rd('b704_tie.txt'), tiew=jl('b704_tie_word.json'), quotej=jl('b704_quote.json'), quotet=rd('b704_quote.txt'),
        cutj=jl('b704_cut.json'), cutt=rd('b704_cut.txt'), orders_line=jl('b704_orders_line.json'),
        order_readme=((jl('b704_order_readme.json').get('lines') or [{}])[0]),
        figj=jl('b704_standing_figures.json'), figt=rd('b704_standing_figures.txt'),
        glossary_tri=tri(ROOT, 'data/glossary.txt', PRE['relay']),
        ef_main=gs(KI, 'rev-parse', 'main'),
        ef_log=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
                gs(KI, 'log', '--reverse', '--first-parent', '--format=%H %ct %s', K.EF_MAIN_BEFORE + '..main').split(NL) if l.strip()],
        ef_tags=dict((t, _tag_peel(t)) for t in ('v0.36', 'v0.37')),
        ef_branches=sorted(x for x in gs(KI, 'branch', '--format=%(refname:short)').split(NL) if x.strip()),
        ef_sorry=_ef_sorry_code(), ef_remote={},
        rf_diff=rd('b704_readfirst_diff.txt'), rf_hand_now=blob(ROOT, 'HEAD:data/b704_readfirst.txt'),
        rf_hand_z=blob(ROOT, '%s:data/b704_readfirst.txt' % K.STEPZERO_BANKS) if K.STEPZERO_BANKS else None,
        asec=jl('b704_arm_seconds.json'), asect=rd('b704_arm_seconds.txt'),
        shared=dict((p, (cr0(blob(ROOT, '%s:%s' % (PRE['relay'], p))), cr0(raw(os.path.join(ROOT, *p.split('/')))), cr0(blob(ROOT, 'HEAD:' + p))))
                    for p in K.SHARED_APPENDED),
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), c2=_ct(ROOT, K.C2_RELAY), c2pp=_ct(PP, K.C2_PP), c3=_ct(ROOT, K.C3_RELAY[0]),
               c3pp=[_ct(PP, x) for x in K.C3_PP], c4=_ct(ROOT, K.C4_RELAY), c4pp=_ct(PP, K.C4_PP), stepzero=_ct(ROOT, K.STEPZERO_BANKS)),
        files=dict(stepzero=files_of(ROOT, K.STEPZERO_BANKS) if K.STEPZERO_BANKS else [], c1=files_of(ROOT, K.C1_RELAY), c2=files_of(ROOT, K.C2_RELAY),
                   c2pp=files_of(PP, K.C2_PP), c3pp=[files_of(PP, x) for x in K.C3_PP], c4pp=files_of(PP, K.C4_PP)),
        subj=dict(c4pp=gs(PP, 'log', '-1', '--format=%s', K.C4_PP)),
        standing=STANDING, wf=wf_state(),
        export_present=os.path.exists(os.path.join(ROOT, *EXPORT.split('/'))), export_log=gs(ROOT, 'log', '--all', '--format=%h', '--', EXPORT),
        export_index=gs(ROOT, 'ls-files', '--', EXPORT), export_status=gs(ROOT, 'status', '--porcelain', '--', EXPORT),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b704_act_root.json'), arj0=jl('b703_act_root.json'), art=rd('b704_act_root.txt'), rootsf=rd('act_roots.txt'),
        rootbanks=jl('b704_root_banks.json'),
        pushout=(files_of(ROOT, K.STEPZERO) if K.STEPZERO else [], bool(K.STEPZERO) and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, *f.split('/')))), cr0(blob(ROOT, 'HEAD:tools/' + f)))
              for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        pp_renames=gs(PP, 'diff', '--name-status', '-M', PRE['pp'], 'HEAD'),
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        kern_face=(jl('b704_kernels_face.json').get('kernels') or {}), kerns_read=list(dict.fromkeys(REC._kerns())),
        tools=tools, tooltext={f: strip_prose(read(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mustfail=not os.path.exists(os.path.join(D, 'b704_mustnotexist.txt')),
        fj=jl('b704_findings.json'), tj=jl('b704_trail.json'), sc=jl('b704_scores.json'), desk=rd('b704_desk_notes.txt'), tfj=jl('b704_table_final.json'),
        lsr=None,
        rlog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(ROOT, 'log', '--reverse', '--format=%h %ct %s', PRE['relay'] + '..HEAD').split(NL) if l.strip()],
        plog=[(l.split(' ', 2)[0], l.split(' ', 2)[2] if l.count(' ') >= 2 else '', int(l.split(' ', 2)[1])) for l in
              gs(PP, 'log', '--reverse', '--format=%h %ct %s', PRE['pp'] + '..HEAD').split(NL) if l.strip()],
    )
    S['probe_delete_ts'] = _first_ts(cmds, lambda c: 'probe-b704' in c and REC.delete_shape(c)[0])
    S['first_delete_ts'] = _first_ts(cmds, lambda c: bool(REC.delete_shape(c)[0]))
    S['probe_branch_ts'] = _first_ts(cmds, lambda c: 'probe-b704' in c and not REC.delete_shape(c)[0])
    if 'efremote' in need:
        refs = {}
        for l in git(KI, 'ls-remote', 'origin')[1].split(NL):
            if '\t' in l:
                sha, ref = l.split('\t', 1)
                refs[ref.strip()] = sha.strip()
        S['ef_remote'] = refs
    S['root_at_commit'] = _root_named_at_commit(S['arj'])
    S['secs_ct'] = dict((p, _ct(ROOT, gs(ROOT, 'log', '-1', '--format=%H', '--', 'data/b704_arm_seconds_%s.json' % p))) for p in K.PARTS)
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
    if 'figures' in need:
        import b703_standing_figures as SF
        base = jl('b703_standing_figures.json')
        S['fig'] = SF.all_figures(baseline=((base.get('pins') or {}).get('rows') or {}), remote=KC0.remote_refs)
        S['fig_prev'] = base
        S['fig_prev_name'] = 'b703_standing_figures.json (b703`s figures)'
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
            if f.startswith(('b704_', 'audit_b704_')) and os.path.isfile(os.path.join(D, f)) and not f.endswith(('.gz', '.png', '.jsonl')):
                pub.append(read(os.path.join(D, f)))
        pub += [read(f) for f in tools]
        pub.append(appended(cr0(blob(ROOT, PRE['relay'] + ':data/glossary.txt')) or b'', cr0(raw(os.path.join(D, 'glossary.txt'))) or b''))
        for p in ('README.md', K.FACES_PAGE, 'day1/ONE_PAGE_PROOF.md'):
            pub.append(read(os.path.join(PP, *p.split('/'))))
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


STEPZERO_FAILING = {'test_chain_page.py': ['(1)', '(9)', '(14)'], 'test_chain_page_b638.py': ['(4)', '(5)', '(6)', '(7)'], 'test_g_chain_page.py': ['(1)']}


def tests_ok(S):
    j = S['tests']
    names = sorted(S['tracked_tests'])
    nf = dict((n, x['failing']) for n, x in j.items() if x['rc'] != 0 or x['failing'])
    return bool(names) and sorted(j) == sorted(set(names) - {'test_elab_reader_b634.py'}) and nf == STEPZERO_FAILING \
        and 'b702_nodes_zeta.txt' in (j.get('test_chain_page.py') or {}).get('args', []) \
        and 'test_elab_reader_b634.py' in S['withheld'] \
        and ('TEST FILES %d ; RUN %d ; WITHHELD 1 ; NOT CLEAN 3' % (len(names), len(names) - 1)) in unwrap(S['testst'])


UNANSWERED = "The user doesn't want to proceed with this tool use"


def answers_ok(S):
    a = S['answers']
    m = re.search(r'^### b704 -- THE AUTHOR`S ANSWERS, (\d+) prompt\(s\)', a, re.M)
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


# ================================================================== (R314) STEP ZERO: THE CITATION CHECK, THE BRANCHES, THE READ-FIRST BANK
READFIRST_NEEDLES = ('relay data/b703_closing.txt | :1 ; :5-:17 ; :88-:161 ; :290-:306', 'relay data/b703_defects.txt | :6-:73 ; :75-:79',
                     'relay data/b703_widening_grade.txt | :1-:40 ; :180-:210', 'relay data/b703_closing_push_out.txt | :1-:6',
                     'relay data/b701_glossary_rows.txt | :1-:17', 'relay data/b702_nodes_zeta.txt | :1-:174',
                     'PLACE-papers OPEN_TRAILS.md | :15444 ; :15454 ; :15496 ; :15506 ; :15492-:15540', 'PLACE-papers README.md | :1-:190 (:133 ; :162)',
                     'relay data/b670_licensed_table.txt | :1-:286', 'relay data/b702_tie.txt | :1-:57', 'relay data/b674_rules.txt | :1-:15',
                     'relay data/b690_rules.txt | :1-:16', 'relay data/b698_rules.txt | :1-:13', 'relay tools/circuit_read.py | :379-:458')
NAMED_PUSH = sorted(b for _r, bs in K.DELETE for b in bs)
NAMED_KERNEL = sorted(list(K.KERNEL_BRANCHES_PROMPT) * 2 + ['probe-b704'] * 2)   # ### each deleted locally and at the remote


def readfirst_ok(S):
    z = unwrap(S['readfirst'])
    return bool(z) and all(x in z for x in READFIRST_NEEDLES) and 'ITEMS 23 ;' in z


def branches_ok(S):
    z = S['branchest']
    left = dict((r, sorted(x.strip() for x in v.split(NL) if x.strip())) for r, v in S['branch_lists'].items())
    return all(v == [] for v in left.values()) and len(left) == 3 and all(b in z for b in NAMED_PUSH) \
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
    sh_ = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell')]
    shapes = [(S['REC'].delete_shape(r['cmd']), S['REC'].chained_after(r['cmd'])) for r in sh_]
    shapes = [(s, c) for s, c in shapes if s[0]]
    return bool(shapes) and all(len(d) == 1 and not gl and not vs and not c for (d, gl, vs), c in shapes) \
        and sorted(x for (d, _g, _v), _c in shapes for x in d) == sorted(NAMED_PUSH + NAMED_KERNEL) \
        and 'BRANCH DELETES OF ONE BRANCH, NO GLOB, NO VARIABLE AND NOTHING CHAINED AFTER 14 OF 14' in S['cmdt']


def kernel_branches_gone_ok(S):
    """(R314)(8) and the author's word: widening-b701 and epstein-b703 gone locally and at the remote, v0.36 and v0.37 peeled where they stood."""
    r = S['ef_remote']
    return bool(r) and not [b for b in K.KERNEL_BRANCHES_PROMPT if ('refs/heads/' + b) in r or b in S['ef_branches']] \
        and r.get('refs/tags/v0.36^{}') == K.EF_V036 and r.get('refs/tags/v0.37^{}') == K.EF_V037 \
        and S['ef_tags'].get('v0.36') == K.EF_V036 and S['ef_tags'].get('v0.37') == K.EF_V037


def dry_step_ok(S):
    g = S['gate']
    return '--- THE DRY-RUN STEP ((R267)(2))' in g and 'ENTRY : table cells NONE ; screens QUIET' in g and 'TRAIL : table cells NONE ; screens QUIET' in g \
        and 'THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK True' in g and 'THE TRAIL`S RESOLVED LINE EQUAL TO THE DEFECTS BANK True' in g \
        and '### ### **THE DRY-RUN STEP : CLEAN**' in g and '### ### **GATE VERDICT : CLEAR**' in g


def closing_dry_ok(S):
    g = S['gate']
    return '--- THE CLOSING DRY-RUN STEP (b675 rules row 1)' in g and '### ### **THE CLOSING DRY-RUN STEP : CLEAN**' in g \
        and 'b704 closed:' in g and '### THE CORRIGENDUM AND THE READ RULE' in g and '### THE FACES PROBE' in g and '### THE CELLS' in g \
        and '### THE README' in g and '### THE GLOSSARY' in g and '### THE RE-CUT' in g and '### THE STANDING ARMS' in g and '### THE ORDERS' in g \
        and '### THE KERNELS' in g and '(g) The defects (a)' in g and '### NO VERDICT LINE' not in g


def citation_ok(S):
    """the citation check's bank: every cite checked, OK and misses summing, its two misses the two the defects bank letters as the navigator's
    ((f), (g)); the bank written before the step-zero banks' commit and that commit before Component 1's."""
    c = S['citation']
    m = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', c)
    nav = re.findall(r"^    \(([a-z])\) THE NAVIGATOR'S", S['defects'], re.M)
    return bool(m) and int(m.group(1)) == int(m.group(2)) + int(m.group(3)) > 0 and 'A GATE STEP AT STEP ZERO' in c \
        and int(m.group(3)) == len(S['cit_misses']) == 2 and 'f' in nav and 'g' in nav and bool(S['cit_at']) and bool(S['t'].get('stepzero')) \
        and S['cit_at'] < S['t']['stepzero'] and bool(S['t'].get('c1')) and S['t']['stepzero'] <= S['t']['c1']


def rowgen_ok(S):
    return '### ### **CONSTELLATION EXIT 0 ; ROWGEN DIFF EXIT 0 ; TABLES 19.**' in S['rowgen']


def weight_ok(S):
    return landed(S, 0, ['b703 AT ITS WEIGHT', '295e53f0'])


# ### the answers whose checks govern a step, and the step: (a needle of the checked answer, the time of the step it governs)
def answers_checked_ok(S):
    """the citation bank's mid-act prints read at HEAD, at or above the sealed floor, each OK; the last before the cut's commit (the next
    document's answer the last acted on before the seal); the probe route's before the probe branch was made."""
    c = S['citation']
    stamps = re.findall(r'### \(R278\)\(4\) THE MID-ACT CHECK \((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\): the (?:navigator`s )?answer carrying \'([^\']+)\'', c)
    figs = re.findall(r'ANSWER CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)(?: -- RAISED: ([^*]*?))?\.\*\*', c)
    ts = [iso_epoch(t_) for t_, _n in stamps]
    probe = [iso_epoch(t_) for t_, n in stamps if 'Probe route' in n]
    readme = [iso_epoch(t_) for t_, n in stamps if 'README arm' in n]
    # ### a miss stands only where it names a bank of a later act, the answer naming where that act's work will go (the defects bank's event)
    later = all(m_ == '0' or all(re.match(r'^data/b70[5-9]_\S+$', x.strip()) for x in (r_ or '').split(';') if x.strip()) and r_ for _c, _o, m_, r_ in figs)
    lk = S['lock_epoch'] or 10 ** 12
    return len(stamps) >= max(FLOORS['checks'], 1) and len(figs) >= len(stamps) and later \
        and all(x and (x < S['t']['c4pp'] or x in readme) for x in ts) and bool(S['t'].get('c4pp')) \
        and bool(probe) and bool(S['probe_branch_ts']) and max(probe) < S['probe_branch_ts'] and bool(readme) and max(readme) < lk \
        and 'W-ORD-README-FIGURE-SCOPE' in oline(S, S['order_readme'].get('line'))


# ================================================================== (R314)(1)-(2): THE CORRIGENDUM AND THE READ RULE
def scorer_banks_ok(S):
    n = ''.join(strip_prose(_fn_src(S['rec_src'], f)) for f in ('_n1', '_n2', '_n3', '_n4'))
    sc = strip_prose(_fn_src(S['rec_src'], 'scores'))
    ft = strip_prose(_fn_src(S['rec_src'], '_finding_text'))
    return bool(n) and '_commands.json' in n and '_dispatches.json' in n and '_faces_diff.json' in n and '_cut.json' in n \
        and not re.search(r'\b(FIND|OT)\b|FINDINGS|OPEN_TRAILS|findings|entry_line', n) \
        and "os.path.isfile(os.path.join(D, '%s_scores.json' % ACT))" in sc and 'scores_line(S)' in ft and "jl('%s_scores.json' % ACT)" in ft


def entry_scores_ok(S):
    want = conv(S['REC'].scores_line(S['sc'])) if S['sc'] else None
    blk = _entry_block(S)
    got = [l for l in blk.split(NL) if l.startswith('**The scores.**')]
    return bool(want) and bool(S['sc']) and got == [want]


def entry_title_ok(S):
    e = S['fj'].get('entry_line')
    t = S['REC']._title()
    return bool(e) and fline(S, e) == conv(t) and t.startswith('## ') and 'The faces page at v0.37' in t \
        and 'Correspondence cells regenerated at v0.37' in t and 'the README’s kernel line and the v0.36–v0.37 append' in t \
        and 'One Page Proof re-cut' in t


def trail_tail(S):
    t = S['ot']
    i = t.find(conv(S['REC'].TRAIL_HEAD()))
    return t[i:] if i >= 0 else ''


def trail_defects_ok(S):
    m = re.search(r'^\*\*Defects\*\* \(relay data/b704_defects\.txt\): (.*)\.$', trail_tail(S), re.M)
    return 'THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK True' in S['gate'] and bool(m) \
        and m.group(1) == conv('; '.join(S['defshort_b704']) or 'none')


RESOLVED = re.compile(r'^\*\*Resolved by the seat, for the author’s strike:\*\* .*\((\d+)\) the (\w+) navigator (?:miss|misses)'
                      r'(?: \(\([a-z]\)(?:, \([a-z]\))*\))? and the seat’s (\w+) defects? as lettered\.$', re.M)


def trail_resolved_ok(S):
    m = RESOLVED.search(trail_tail(S))
    nav, seat = _owners(S['defshort_b704'])
    return 'THE TRAIL`S RESOLVED LINE EQUAL TO THE DEFECTS BANK True' in S['gate'] and bool(m) and S['REC'].num_word(nav) == m.group(2) \
        and S['REC'].num_word(seat) == m.group(3)


def corrigendum_ok(S):
    """(R314)(1)-(2): the generated entry landed (its line in the bank, the title at that line through conv), lettering (m); the corrigenda bank
    appended at row (24) and nothing before it changed; the push capture committed alone at step zero."""
    j = S['corrj']
    e = j.get('entry_line')
    now, pre, head = S['corrigenda_tri']     # ### tri() gives (the working tree, the base, HEAD)
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and j.get('lettered') == ['m'] \
        and '  (24) ' in S['corrigenda'] and '  (25) ' not in S['corrigenda'] \
        and pre is not None and (now or b'').startswith(pre) and (head or b'').startswith(pre) and 'FINDINGS :%d' % e in S['corrt'] \
        and 'data/b704_corrigendum.txt' in S['files']['c1']


GUARD_WRITE = "sp = os.path.join(D, 'b704_arm_seconds_%s.json' % PART)"   # ### the write's own line, stripped; matched whole, not by a needle


def guard_ok(S):
    """the suite's writer block guarded (`if PRERUN:` the line above the per-part seconds write, read from this tool's own text), the guard's
    dry run printing no write on the pre-push and post-push paths and the write on the pre-run path, banked."""
    s = S['suite'].split(NL)
    i = next((k for k, l in enumerate(s) if l.strip() == GUARD_WRITE), None)
    j = S['guardj']
    return i is not None and s[i - 1].strip() == 'if PRERUN:' and 'POST-ROOT PATH WRITES NONE' in S['guard'] \
        and (j.get('writes') or {}).get('pre-push') == [] and (j.get('writes') or {}).get('post-push') == [] \
        and (j.get('writes') or {}).get('prerun') == ['data/b704_arm_seconds_<part>.json']


def postroot_writes_none(S):
    j = S['guardj']
    w = j.get('writes') or {}
    return 'POST-ROOT PATH WRITES NONE' in S['guard'] and w.get('pre-push') == [] and w.get('post-push') == [] and bool(S['root_ct']) \
        and sorted(S['secs_ct']) == sorted(K.PARTS) and all(v is not None and v <= S['root_ct'] for v in S['secs_ct'].values())


def trail_lines_equal_defects(S):
    tail = trail_tail(S)
    dm = re.search(r'^\*\*Defects\*\* \(relay data/b704_defects\.txt\): (.*)\.$', tail, re.M)
    rm = RESOLVED.search(tail)
    bank = re.findall(r"^    \(([a-z])\) THE (NAVIGATOR|SEAT)'S", S['defects'], re.M)
    want = (sum(1 for _x, o in bank if o == 'NAVIGATOR'), sum(1 for _x, o in bank if o == 'SEAT'))
    if not dm or not rm or not bank:
        return False
    got_d = KIND.findall(dm.group(1))
    have_d = (sum(1 for _x, o in got_d if o == 'NAVIGATOR'), sum(1 for _x, o in got_d if o == 'SEAT'))
    have_r = (rm.group(2), rm.group(3))
    return have_d == want and have_r == (S['REC'].num_word(want[0]), S['REC'].num_word(want[1]))


def read_sort_ok(S):
    return '### ### **BREACHES 15 ; TRACEABLE 14 ((k) 13, (l) 1) ; NOT IN A BANK 1 ((m) 1) ; THE COMMAND BANK TRACES 0.**' in S['read_sort'] \
        and 'data/b704_read_sort.txt' in S['files']['stepzero']


def read_arm_controls_ok(S):
    c = unwrap(S['read_ctl'])
    return 'EVERY CONTROL AS WANTED True' in c and 'THE REAL READING: FAIL (ROWS' in c and 'OFFENCES 1 ; PRECURSORS 2' in c


def read_bank_repaired_ok(S):
    """the repaired read bank: each call's offset and limit values, the cap's word read from the session, the precursors printed; the record
    tool's `reads` carrying the repair (the cap and the word); the arm reading the bank in its form."""
    b = S['reads_bank']
    _ok, n, _off, pre, form = RDA.reading_text(b)
    rs = strip_prose(_fn_src(S['rec_src'], 'reads'))
    return form and n > 0 and len(pre) == 2 and 'THE WORD AT 2026-10-22T03:31:12' in b and '_cap_word_at' in rs and '_read_verdict' in rs \
        and 'offset' in (S['reads_json'].get('rows') or [{}])[0] and S['reads_json'].get('cap') == 200


def read_rule_standing_ok(S):
    """G-READ-RULE-STANDING (the author's word at the read rule's sort, (R314)(2)): every Read call of a file of two hundred lines or more made
    at or after the word carries an offset and a limit of two hundred or below; a bank not in the repaired form fails."""
    return RDA.reading_text(S['reads_bank'])[0]


# ================================================================== (R314)(3): THE FACES PROBE AT v0.37
def probe_one_path_ok(S):
    return 'PATHS CHANGED 1 ; THE ONE PATH THE ROOT FILE CircuitClosure.lean True ; THE MODULES` TREE v0.37`S True' in S['probediff']


def probe_read_ok(S):
    t, j = S['probet'], S['probej']
    m = re.search(r'the memory log: LOW (\d+) MB ; the hold (\d+) ; STOP lines (\w+)', t)
    return j.get('run_id') == K.PROBE_RUN and j.get('conclusion') == 'success' and bool(j.get('artifact_sha256')) and j.get('ok') is True \
        and ('the ref built (out/ref.txt): %s' % K.PROBE_TIP) in t and bool(m) and int(m.group(1)) >= K.HOLD and m.group(3) == 'False' \
        and 'PROBE CELLS 568 OF 568 ; MISSING 0' in t and re.search(r'^### the artifact: .* ; AGREE$', t, re.M) is not None


def probe_branch_gone_ok(S):
    """the scratch branch deleted by name locally and at the remote after its bank was committed (Component 2's commit before the first delete)."""
    r = S['ef_remote']
    return bool(r) and 'refs/heads/probe-b704' not in r and 'probe-b704' not in S['ef_branches'] and bool(S['probe_delete_ts']) \
        and bool(S['t'].get('c2')) and S['t']['c2'] < S['probe_delete_ts'] and 'data/b704_runner_SIDE-explicit-formula_probe.txt' in S['files']['c2']


def dispatch_one_ok(S):
    rows = S['dispj'].get('rows') or []
    return len(rows) == 1 and rows[0].get('ref') == K.PROBE_TIP and rows[0].get('run_id') == K.PROBE_RUN and rows[0].get('label') == PROBE_LABEL \
        and len(S['cmdj'].get('dispatches') or []) == 1 and S['cmdj'].get('local_lean') == []


def nodes_ok(S):
    n = S['nodes']
    return 'RECORD LINES b702 73 ; b704 73 ; EQUAL True' in S['nodesdiff'] and 'CHANGES OUTSIDE COMMENT LINES 0' in S['nodesdiff'] \
        and '# pin: v0.37' in n and all(re.search(r'^SIDEExplicitFormula\.B321\.%s \| kernel \| added: \(R314\)\(3\), probe run 39721668586' % re.escape(x), n, re.M)
                                        for x in K.NODES_NEW)


def faces_diff_ok(S):
    j = S['facesj']
    return len(j.get('rows') or []) == 6 and j.get('no_cause') == 0 and j.get('head_v037') is True and all(r.get('cause') for r in j.get('rows') or []) \
        and 'CHANGED LINES 6 ; WITH A CAUSE 6 ; WITHOUT 0' in S['facest']


def faces_page_ok(S):
    """the faces page at HEAD and in the tree alike, written by the generator twice (each commit the page alone): its head at v0.37, both nodes
    and both glossary companions in it."""
    p = S['faces_now']
    return bool(p) and p == S['faces_head'] and 'v0.37' in p.split(NL)[2] and all(x in p for x in K.NODES_NEW) \
        and "h2_sign'" in p and 'h2_sign_sum' in p and S['files']['c2pp'] == [K.FACES_PAGE] and S['files']['c3pp'][1] == [K.FACES_PAGE]


# ================================================================== (R314)(4)-(6): THE CELLS, THE README, THE GLOSSARY
def cells_run_ok(S):
    return 'CELLS CHANGED 0 ; FILES CHANGED 0' in S['cellsrun'] and 'THE GENERATOR`S CELLS CHANGED 0 ; NOTHING WRITTEN' in S['cellsdry'] \
        and 'IN A KERNEL CELL THE GENERATOR PARSES 0' in S['cellsdry']


def cells_reach_ok(S):
    return '### ### **MENTIONS READ 15 (LINES 11) ; EQUAL 4 ; DIFFERS 0 ; NO PRINT BANK AT THE TAG 9 ; NO THEOREM OR NO TAG 2 ; RAISED BEFORE THE CLOSING 11 ; NOTHING WRITTEN.**' \
        in S['reach'] and len(re.findall(r' \| (unbanked|differs)', S['reach'])) == 11


def readme_ok(S):
    ls = S['readme_now'].split(NL)
    return 'THE KERNEL LINE AT :164 ; THE APPEND AT :135 ; AS ORDERED True' in S['readme_bank'] and len(ls) > 164 \
        and 'v0.37' in ls[163] and '38e2734' in ls[163] and '2026-10-22' in ls[134] and S['files']['c3pp'][0] == ['README.md']


def glossary_ok(S):
    """(R314)(6): the glossary appended by one comment line and two entries, h2_sign' and h2_sign_sum, nothing before them changed; the check
    printed before (both DERIVES under E0 and by hand)."""
    now, pre, head = S['glossary_tri']
    add = appended(pre, now) if pre else ''
    ent = [l for l in add.split(NL) if l.strip() and not l.startswith('#')]
    return pre is not None and (now or b'').startswith(pre) and now == head and len(ent) == 2 and ent[0].startswith("h2_sign'\t") \
        and ent[1].startswith('h2_sign_sum\t') and 'BOTH DERIVES UNDER E0 AND BY HAND True' in S['gloss']


# ================================================================== (R314)(7): THE TIE, THE SEARCH, THE CUT
def tie_ok(S):
    w = S['tiew']
    return w.get('pick') == 'day1/ONE_PAGE_PROOF.md' == S['cutj'].get('document') and 'OVERREACHES 21 against 14' in (w.get('word') or '') \
        and 'THE AUTHOR`S WORD' in S['tie'] and 'MISSES 0' in (w.get('checked') or '')


def quote_before_cut_ok(S):
    q = iso_epoch((S['quotej'].get('at') or '')[:19] + 'Z')
    return bool(q) and bool(S['t'].get('c4pp')) and q < S['t']['c4pp'] and 'QUOTING LINES 80' in S['quotet'] and 'SEARCHED BEFORE THE CUT`S COMMIT' in S['quotet']


def cut_distance_ok(S):
    c = S['cutj']
    return c.get('before') == 22 and c.get('after') == 2 and c['after'] <= c['before'] and S['files']['c4pp'] == ['day1/ONE_PAGE_PROOF.md'] \
        and S['subj']['c4pp'].startswith('b704 ') and 'BEFORE 22, AFTER 2' in S['cutt']


ORDER_NAMES = ('W-ORD-FACES-PROBE-CURRENT', 'W-ORD-WORKFLOW-PROBE-STEP', 'W-ORD-CORRESPONDENCE-EF-REACH', 'W-ORD-E0-MET-CLASSK')


def orders_ok(S):
    ls = S['orders_line'].get('lines') or []
    return len(ls) == 4 and all(n in oline(S, x.get('line')) for n, x in zip(ORDER_NAMES, ls)) \
        and all('the re-cut act b706' in oline(S, ls[i].get('line')) for i in (1, 2)) \
        and 'companion rows taken up at b704 under (R314)(6), the grade settled at b703' in oline(S, ls[3].get('line')) \
        and 'W-ORD-README-FIGURE-SCOPE' in oline(S, S['order_readme'].get('line')) and 'Trigger: b705 at carry time' in oline(S, S['order_readme'].get('line'))


def figures_banked_ok(S):
    j = S['figj']
    return all(k in j and isinstance((j[k] or {}).get('figure'), int) for k in ('correspondence', 'readme', 'partners', 'pins')) \
        and 'SIDE-explicit-formula NOT AMONG THEM' in S['figt'] and 'SIDE-explicit-formula' not in ((j.get('reach') or {}).get('tabled') or ['SIDE-explicit-formula'])


def readfirst_diff_ok(S):
    return 'THE HAND LIST 34 PATHS ; THE TEXT CITES 24 ; BOTH 18 ; LINES DIFFERING 22' in S['rf_diff'] \
        and 'data/b704_readfirst_diff.txt' in S['files']['stepzero'] and S['rf_hand_now'] is not None and S['rf_hand_now'] == S['rf_hand_z']


REPAIRS_WANT = 2


def repairs_ok(S):
    return ('REPAIRS %d ;' % REPAIRS_WANT) in S['repairs'] and 'NO FROZEN BANK EDITED' in S['repairs'] and '  (1) tools/b704_record.py `reads`' in S['repairs'] \
        and '  (2) tools/b704_record.py `capture`' in S['repairs']


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


# ================================================================== THE RUNNER (this act's one run, the faces probe; SIDE-explicit-formula's main unmoved)
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
    """the probe run as read by its id: the branch tip built, success, the artifact's sha256, the memory low above the hold, no STOP line."""
    return probe_read_ok(S) and (S['dispj'].get('rows') or [{}])[0].get('kernel') == K.KERNEL


def gate_ok(S):
    t = S['probet']
    return 'BUILD EXIT 0 ; ERROR LINES 0' in t and 'the build: exit 0 ; error lines 0' in t and 'sorryAx' not in S['probeax'] and bool(S['probeax']) \
        and re.search(r'^### the artifact: .* ; AGREE$', t, re.M) is not None and 'error lines 0 ; cells parsed 568' in t


def merges_ok(S):
    """no merge this act: SIDE-explicit-formula's main at v0.37 as b703 left it, its first-parent line past it empty, no sorry in code on main."""
    return S['ef_main'] == K.EF_V037 and S['ef_log'] == [] and S['ef_tags'].get('v0.37') == K.EF_V037 and not S['ef_sorry'].strip()


# ================================================================== SCOPE, THE SEAL, THE ROOT, THE RECORD
def seal_hashes_ok(S):
    j = S['sealj']
    at = iso_epoch(j.get('at') or '')
    rec_ = j.get('tools') or {}
    return bool(rec_) and at is not None and S['lock_epoch'] is not None and S['lock_epoch'] <= at \
        and sorted(rec_) == sorted(K.SEALED) and all(S['sealnow'].get(t) == rec_[t] for t in K.SEALED)


POST_SEAL = ('b704 seal', 'b704 pre-root', 'b704 root', 'b704 record', 'b704 --', 'b704 closing', 'b704 entry')


def _component_commit(s):
    return s.startswith('b704') and not s.startswith(POST_SEAL)


def sealed_after_ok(S):
    lk = S['lock_epoch']
    if lk is None:
        return False
    return all((t < lk) == _component_commit(s) for h, s, t in S['rlog']) and all((t < lk) == _component_commit(s) for h, s, t in S['plog']) \
        and any(_component_commit(s) for h, s, t in S['plog'])


def root_banked_ok(S):
    import act_root as AR
    j, j0 = S['arj'], S['arj0']
    rows = _chain_rows(S)
    items = j.get('items') or []
    return bool(j) and len(rows) == 81 and rows[80][:3] == ['b704', j.get('root'), j0.get('root')] \
        and AR.root_of(items, j.get('previous', '')) == j.get('root') and ('root %s' % j.get('root')) in S['art'] \
        and sorted(j['reads']['heads']) == sorted(AR.repositories('HEAD')) and S['roots_pre'] is not None \
        and (S['roots_now'] or b'').startswith(S['roots_pre']) \
        and not [it for it in items if 'b628_intake_crank' in it or 'b647_navigator_memory' in it or 'b705_' in it or 'mirror' in it
                 or 'chain_' in it or 'units' in it or it.split()[0].endswith(('.gz', '.png', '.jsonl'))] \
        and any(it.startswith('data/b704_faces_diff.txt ') for it in items) and any(it.startswith('data/b704_cut.txt ') for it in items) \
        and any(it.startswith('data/b704_corrigendum.txt ') for it in items) and any(it.startswith('data/b704_read_calls.txt ') for it in items) \
        and (j.get('commit') or {}).get('relay')


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b704_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    ha = S['half_a'] or {}
    v = [tuple(x[:2]) for x in (ha.get('acts') or [])] + [tuple(x[:2]) for x in (S['ar_verify'] or [])]
    r = dict(ha.get('reads') or {}, **(S['ar_reads'] or {}))
    return ha.get('head') == gs(ROOT, 'rev-parse', 'HEAD') and [x[0] for x in v] == ['b%d' % i for i in range(624, 705)] \
        and all(x[1] == 'AGREE' for x in v) and (r.get('b704') or {}).get('crlf') == 0 and (r.get('b680') or {}).get('corrected') == 4 \
        and (ha.get('boundary') or {}).get('equal') is True and S['boundary'].get('equal') is True \
        and (ha.get('boundary') or {}).get('root') == S['boundary'].get('root')


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


ENTRY_NEEDLES = ('**The corrigendum**', '**The read rule**', '**The faces page**', '**The cells**', '**The README**', '**The glossary**',
                 '**The re-cut**', '**The orders**', '**The standing arms**', '**The citation check**', '**The scores.**', '**Read in mutual light**',
                 'strengthens', '**Carried to:**', '**Next.**', 'b705', 'the cap of two hundred', 'h2_sign_sum_iff_rh')


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
        and '### THE CITATION CHECK' in t and '### THE RECORD LINES' in t and '### THE DRY RUN' in t and 'THE CORRIGENDUM AND THE READ RULE' in t \
        and 'THE FACES PROBE' in t and 'THE CELLS' in t and 'THE README' in t and 'THE GLOSSARY' in t and 'THE RE-CUT' in t \
        and 'THE STANDING ARMS' in t and 'THE ORDERS' in t and '### THE KERNELS' in t and '### THE MIRROR' in t and '### THE CARRY-TIME' in t


def _read_plant(S):
    return put(S, 'reads_bank', S['reads_bank'] + NL + '  99999 | 2099-01-01T00:00:00Z | 500 | offset None | limit None | WHOLE | planted.py')


ARMS = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry', lambda S: 'RULING (R314) END' in S['ferry'] and S['ferry'].rstrip().endswith(K.TAIL),
     lambda S: put(S, 'ferry', S['ferry'].replace(K.TAIL, ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the step-zero bank: tail, lean, lake, python and claude named, the seat`s claude alone, none of the others; no task stopped, no orphan, nothing stopped by PID',
     lambda S: procs_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('python 0', 'python 1'))),
    ('G-STEPZERO-TESTS', 'the tests bank against the test files tracked before the act, test_elab_reader_b634.py withheld (no lean on this host), run against the list the page names, the three not clean named',
     lambda S: tests_ok(S), lambda S: put(S, 'tracked_tests', S['tracked_tests'] + ['test_x.py'])),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: S['pushout'][0] == ['data/b703_closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'relay`s, PLACE-papers` and SIDE-explicit-formula`s branch lists by the ruling`s eight names, and the branches bank',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{'D:/relay': 'push-b703'}))),
    ('G-READFIRST-CITED', 'the read-first bank: every item of the ferry`s list cited by path and line', lambda S: readfirst_ok(S),
     lambda S: put(S, 'readfirst', '')),
    ('G-ANSWERS-BANKED', 'the answers bank read at HEAD: its prompts and calls at or above the sealed floors, each with its options and result, any call after the lock named on the face',
     lambda S: answers_ok(S), lambda S: put(S, 'answers', re.sub(r'(?m)^(### b704 -- THE AUTHOR`S ANSWERS, )(\d+)', lambda m: m.group(1) + str(int(m.group(2)) + 1),
                                                                 S['answers']))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-EXPORT-UNTRACKED', 'the navigator`s export: present, untracked, in no commit', lambda S: S['export_present'] and S['export_log'] == ''
     and S['export_index'] == '' and S['export_status'].startswith('??'), lambda S: put(S, 'export_index', EXPORT)),
    ('G-EDIT-ROUTE', 'the record tool`s one reading (tools/edit_route.py`s arms and sed in any form) over this act`s whole capture and the previous act`s after its post-push suite, read live',
     lambda S: edit_route_ok(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -n 1p tools/b704_record.py")])),
    ('G-NO-LOCAL-LEAN', 'the act`s command capture, read live: no command runs lean or lake on this host (N1)', lambda S: no_local_lean(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd='lake env lean SIDEExplicitFormula/H2SignWide.lean')])),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line, found by conv', lambda S: weight_ok(S), lambda S: _rl(S, 0, 1)),
    ('G-DRY-STEP-CLEAN', 'the gate`s record: the dry-run step run, the entry and the trail record quiet under their screens, the trail`s Defects and Resolved lines equal to the defects bank, CLEAN printed, the gate CLEAR',
     lambda S: dry_step_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE DRY-RUN STEP : CLEAN', 'THE DRY-RUN STEP : NOT CLEAN'))),
    ('G-CLOSING-DRY-STEP', 'the gate`s record: the closing run dry before the lock, its head line and its sections -- the corrigendum and the read rule, the faces probe, the cells, the README, the glossary, the re-cut, the standing arms, the orders, the kernels -- and the defects row printed (b675 rules row 1)',
     lambda S: closing_dry_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE CLOSING DRY-RUN STEP : CLEAN', 'THE CLOSING DRY-RUN STEP : NOT CLEAN'))),
    ('G-CITATION-CHECKED', 'the citation check`s bank (the gate step at step zero): every cite checked, its two misses the navigator`s (f) and (g) as the defects bank letters them, its bank written before the step-zero banks` commit and that commit before Component 1',
     lambda S: citation_ok(S), lambda S: put(S, 'cit_misses', S['cit_misses'] + ['planted'])),
    ('G-R314-ENTERED', 'the ferry and the trail', lambda S: 'RULING (R314) END' in S['ferry'] and S['ot'].count('**(R314) ratified') == 1,
     lambda S: put(S, 'ot', S['ot'].replace('**(R314) ratified', '**(R3140) ratified'))),
    ('G-ROWGEN-STEPZERO', 'the rowgen bank: constellation and the build-free diff over the 19 roster tables, both exit 0 (b670 rules row 3)',
     lambda S: rowgen_ok(S), lambda S: put(S, 'rowgen', S['rowgen'].replace('ROWGEN DIFF EXIT 0', 'ROWGEN DIFF EXIT 1'))),
    ('G-BRANCHES-BANKED', 'the branches banks: every tip banked before the first delete and the citation check before it (b695 (a)), the eight rows through the record tool`s reader, each merged and deleted',
     lambda S: branches_banked_ok(S), lambda S: _mut(S, 'branchbj', lambda d: d.update(at='2099-01-01T00:00:00Z'))),
    ('G-DELETES-ONE-BRANCH', 'the command capture by the record tool`s reader and the command bank: each branch delete naming one branch, no glob and no variable in any half, nothing chained after (data/b694_rules.txt row (1)), the ruling`s eight and the three kernel branches twice each exactly',
     lambda S: deletes_one_ok(S), lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="git branch -d push-b703; echo EXIT $?")])),
    ('G-KERNEL-BRANCHES-GONE', 'one ls-remote of SIDE-explicit-formula in this part and its local branch list: widening-b701 and epstein-b703 gone at both, v0.36 and v0.37 peeled where they stood ((R314)(8), the author`s word)',
     lambda S: kernel_branches_gone_ok(S), lambda S: put(S, 'ef_branches', S['ef_branches'] + ['widening-b701'])),
    ('G-ANSWERS-CHECKED', 'the citation bank`s mid-act prints read at HEAD, each OK or missing only a later act`s bank, each before the step it governs: the probe route`s before the probe branch was made, the README figure`s before the lock and its order landed, the rest before the cut`s commit',
     lambda S: answers_checked_ok(S), lambda S: put(S, 't', dict(S['t'], c4pp=1))),
    ('G-SCORER-READS-BANKS', 'tools/b704_record.py`s code, prose stripped: the N1-N4 scorers reading banks and commits and no ledger, the scores bank written once, the entry`s scores line from it',
     lambda S: scorer_banks_ok(S), lambda S: put(S, 'rec_src', S['rec_src'].replace("def _n2():", "def _n2():\n    _x = rd(FIND)"))),
    ('G-ENTRY-SCORES-EQUAL', 'FINDINGS at the findings bank`s line and the scores bank: the entry`s scores line equal to the line composed from the bank',
     lambda S: entry_scores_ok(S), lambda S: _mut(S, 'sc', lambda d: d.update(N1=['REFUTED', 'planted']))),
    ('G-ENTRY-TITLE-FORM', 'FINDINGS at the findings bank`s line and the record tool`s title from the banks: the ferry`s form, titled by its objects, adjusted to what the act did',
     lambda S: entry_title_ok(S), lambda S: put(S, 'find', S['find'].replace('The faces page at v0.37', 'The faces page at v0.36'))),
    ('G-CORRIGENDUM-ENTERED', 'the generated corrigendum entry at FINDINGS (its bank`s line, the title through conv), (m) lettered, Component 1`s commit carrying its bank; the corrigenda bank appended at row (24) and nothing before it changed ((R314)(2))',
     lambda S: corrigendum_ok(S), lambda S: _mut(S, 'corrj', lambda d: d.update(lettered=['l']))),
    ('G-GUARD-HELD', 'this suite`s own text at the per-part seconds write (the line above it `if PRERUN:`) and the guard`s dry-run bank: no write on the pre-push and post-push paths, the write on the pre-run path alone',
     lambda S: guard_ok(S), lambda S: put(S, 'suite', S['suite'].replace("if PRERUN:\n        sp = os.path.join(D, 'b704_arm_seconds_%s.json' % PART)", "sp = os.path.join(D, 'b704_arm_seconds_%s.json' % PART)"))),
    ('G-POSTROOT-WRITES-NONE', 'the guard`s dry-run bank and the log: no write on the post-root path, and every per-part seconds bank`s last commit at or before the root`s recorded commit',
     lambda S: postroot_writes_none(S), lambda S: put(S, 'secs_ct', dict(S['secs_ct'], **{K.PARTS[0]: (S['root_ct'] or 0) + 1}))),
    ('G-TRAIL-LINES-EQUAL-DEFECTS', 'OPEN_TRAILS from the trail`s head and data/b704_defects.txt at HEAD: the Defects line and the Resolved line, each counted by kind, equal the bank counted by kind',
     lambda S: trail_lines_equal_defects(S), lambda S: put(S, 'defects', S['defects'] + NL + "    (z) THE NAVIGATOR'S: A PLANTED ROW.")),
    ('G-READ-SORT-BANKED', 'the read rule`s sort bank, committed at step zero: b703`s fifteen breaches sorted by trace, (k) thirteen and (l) one in its read bank, (m) in none ((R314)(2))',
     lambda S: read_sort_ok(S), lambda S: put(S, 'read_sort', S['read_sort'].replace('TRACEABLE 14', 'TRACEABLE 0'))),
    ('G-READ-ARM-CONTROLS', 'the read arm`s control bank: the arm over the real bank FAIL on its one offence, its two precursors printed, every mutated control as wanted ((R314)(2), the author`s word)',
     lambda S: read_arm_controls_ok(S), lambda S: put(S, 'read_ctl', S['read_ctl'].replace('AS WANTED True', 'AS WANTED False'))),
    ('G-READ-BANK-REPAIRED', 'the read bank in its repaired form (each call`s offset and limit values, the word`s time, two precursors) read by the arm`s own parser, and the record tool`s `reads` carrying the cap and the word (the carry-time repair (1))',
     lambda S: read_bank_repaired_ok(S), lambda S: put(S, 'reads_bank', re.sub(r'\| offset \S+ \| limit \S+ \|', '|', S['reads_bank']))),
    ('G-PROBE-ONE-PATH', 'the probe diff bank: probe-b704`s one commit against v0.37 changing the root CircuitClosure.lean alone, the modules` tree v0.37`s ((R314)(3))',
     lambda S: probe_one_path_ok(S), lambda S: put(S, 'probediff', S['probediff'].replace('PATHS CHANGED 1', 'PATHS CHANGED 2'))),
    ('G-PROBE-READ', 'the probe`s runner bank, read by its run id: the branch tip built, success, the artifact`s sha256 agreeing, the memory low above the hold, 568 of 568 cells, none missing (N1, N2)',
     lambda S: probe_read_ok(S), lambda S: put(S, 'probet', S['probet'].replace('MISSING 0', 'MISSING 1'))),
    ('G-PROBE-BRANCH-GONE', 'one ls-remote of SIDE-explicit-formula in this part, its local branch list, the command capture and Component 2`s commit: probe-b704 deleted at both after its bank was committed (the author`s word)',
     lambda S: probe_branch_gone_ok(S), lambda S: put(S, 'ef_remote', dict(S['ef_remote'], **{'refs/heads/probe-b704': K.PROBE_TIP}))),
    ('G-DISPATCH-ONE', 'the dispatches bank and the command bank: one dispatch, the probe branch`s tip, read by its run id; no lean on this host (N1)',
     lambda S: dispatch_one_ok(S), lambda S: _mut(S, 'dispj', lambda d: d.update(rows=(d.get('rows') or []) * 2))),
    ('G-NODES-ROWS-UNCHANGED', 'the node list against b702`s (every record row unchanged but its tag) and the list now: the pin v0.37 and the two nodes on the author`s word, each naming the probe run',
     lambda S: nodes_ok(S), lambda S: put(S, 'nodes', S['nodes'].replace('# pin: v0.37', '# pin: v0.26'))),
    ('G-FACES-DIFF-CAUSED', 'the faces diff banks: six changed lines over the act, each with its cause, none without, the head at v0.37 (N2)',
     lambda S: faces_diff_ok(S), lambda S: _mut(S, 'facesj', lambda d: d.update(no_cause=1))),
    ('G-FACES-PAGE-GENERATED', 'the faces page in the tree and at HEAD and its two commits: equal, each commit the page alone, its head at v0.37, both nodes and both glossary companions in it',
     lambda S: faces_page_ok(S), lambda S: put(S, 'faces_now', S['faces_now'] + 'x')),
    ('G-CELLS-RUN-ZERO', 'the generator`s dry run and run banks: 0 cells written, no kernel cell naming SIDE-explicit-formula parsed, nothing written ((R314)(4), N3)',
     lambda S: cells_run_ok(S), lambda S: put(S, 'cellsrun', S['cellsrun'].replace('CELLS CHANGED 0', 'CELLS CHANGED 1'))),
    ('G-CELLS-REACH', 'the reach bank: the 15 prose mentions read against the probe, 4 equal, none differing, 11 raised each with its one-word cause, nothing written (the author`s word)',
     lambda S: cells_reach_ok(S), lambda S: put(S, 'reach', S['reach'].replace('DIFFERS 0', 'DIFFERS 1'))),
    ('G-README-APPLIED', 'the README bank and PLACE-papers` README in the tree and its commit: the kernel line at :164 naming v0.37 (38e2734), the append at :135 dated 2026-10-22, the commit the README alone ((R314)(5))',
     lambda S: readme_ok(S), lambda S: put(S, 'readme_now', S['readme_now'].replace('38e2734', 'd4e046a'))),
    ('G-GLOSSARY-COMPANIONS', 'the glossary before, now and at HEAD and its check bank: two entries appended, h2_sign` and h2_sign_sum, nothing before them changed, both DERIVES under E0 and by hand ((R314)(6))',
     lambda S: glossary_ok(S), lambda S: put(S, 'glossary_tri', (b'x' + (S['glossary_tri'][0] or b''),) + tuple(S['glossary_tri'][1:]))),
    ('G-TIE-ON-WORD', 'the tie bank, the author`s word banked with its check and the cut bank: day1/ONE_PAGE_PROOF.md on the word, b674`s measures in their written order, OVERREACHES 21 against 14',
     lambda S: tie_ok(S), lambda S: _mut(S, 'tiew', lambda d: d.update(pick='day1/Spectral_Inertness.md'))),
    ('G-QUOTE-BEFORE-CUT', 'the quotation search`s bank and the cut`s PLACE-papers commit: the search before the commit, 80 quoting lines entered as residues (data/b690_rules.txt row (2), N4)',
     lambda S: quote_before_cut_ok(S), lambda S: _mut(S, 'quotej', lambda d: d.update(at='2099-01-01T00:00:00Z'))),
    ('G-CUT-DISTANCE', 'the cut bank and its commit: 22 rows outside LICENSED/CITED to 2 by the b670 method, the commit the paper alone, its subject the act`s (N4)',
     lambda S: cut_distance_ok(S), lambda S: _mut(S, 'cutj', lambda d: d.update(after=23))),
    ('G-ORDERS-ENTERED', 'OPEN_TRAILS at the five landing lines: the discharge, the two orders with the trigger b706, W-ORD-E0-MET-CLASSK`s annotation in the author`s words, and W-ORD-README-FIGURE-SCOPE with the trigger b705 at carry time',
     lambda S: orders_ok(S), lambda S: _mut(S, 'orders_line', lambda d: d.update(lines=(d.get('lines') or [])[:3]))),
    ('G-FIGURES-BANKED', 'the standing figures bank at b704: the four figures against b703`s, and G-CORRESPONDENCE-CURRENCY`s reach, SIDE-explicit-formula not among its parsed kernels (the author`s word at the cells prompt)',
     lambda S: figures_banked_ok(S), lambda S: _mut(S, 'figj', lambda d: d.pop('pins', None))),
    ('G-READFIRST-DIFF-BANKED', 'the readfirst diff bank and the step-zero commit, and the hand list`s blob at HEAD against step zero`s: the diff banked, no bank rewritten',
     lambda S: readfirst_diff_ok(S), lambda S: put(S, 'rf_hand_now', b'x')),
    ('G-TOOL-REPAIRS', 'the repairs bank`s verdict: the carry-time repairs, each by the word or carry it answers, the read bank first, no frozen bank edited',
     lambda S: repairs_ok(S), lambda S: put(S, 'repairs', S['repairs'].replace('REPAIRS %d ;' % REPAIRS_WANT, 'REPAIRS 0 ;'))),
    ('G-PARTS-PRERUN', 'the pre-run bank`s six parts with their seconds, named in the form the parts arm reads',
     lambda S: parts_ok(S), lambda S: put(S, 'prerun', S['prerun'].replace('PART standing-b3', 'PART standing-x'))),
    ('G-ARM-SECONDS-BANKED', 'the per-arm seconds bank: every standing arm clocked at the pre-run, the three slowest named, each part`s seconds',
     lambda S: arm_seconds_ok(S), lambda S: _mut(S, 'asec', lambda d: d.update(clocked=0))),
    ('G-DEFECTS-LETTERED', 'the defects bank read at HEAD: the sealed letters its prefix, consecutive letters, owners the seat or the navigator',
     lambda S: defects_ok(S), lambda S: put(S, 'defects', S['defects'].replace("(a) THE SEAT'S", "(a) THE AUTHOR'S"))),
    ('G-READ-RULE-STANDING', 'tools/b704_read_arm.py over the read bank at HEAD (the author`s word at the read rule`s sort, (R314)(2)): no Read call of a file of two hundred lines or more without an offset, without a limit or with a limit above two hundred, from the word on',
     lambda S: read_rule_standing_ok(S), lambda S: _read_plant(S)),
    ('G-TRAIL-DEFECTS-EQUAL', 'the gate`s record and OPEN_TRAILS from the trail`s head: the trail`s Defects line equal to the defects bank in the dry run and as landed',
     lambda S: trail_defects_ok(S), lambda S: put(S, 'defshort_b704', list(S['defshort_b704']) + ['(z) THE SEAT`S: A PLANTED ROW'])),
    ('G-TRAIL-RESOLVED-EQUAL', 'the gate`s record and OPEN_TRAILS from the trail`s head: the trail`s Resolved line`s last item counting the navigator`s and the seat`s defects as the bank letters them, in the dry run and as landed',
     lambda S: trail_resolved_ok(S), lambda S: put(S, 'defshort_b704', list(S['defshort_b704']) + ["(z) THE NAVIGATOR'S: A PLANTED ROW"])),
    ('G-SPEC-PLANTED', 'tools/b704_regspec.py`s planted rows run live through the record tool`s readers, and rows of another shape refused',
     lambda S: bool(S['spec']['read']) and all(S['spec']['read']) and all(S['spec']['controls']) and any('runner' in x for x in S['spec']['shapes']),
     lambda S: _mut(S, 'spec', lambda d: d['controls'].append(False))),
    ('G-CONVERSION-ONE', 'every b704 tool`s code: no conversion defined (conv imported from b652_record); the suite importing it',
     lambda S: S['conv_bad'] == [] and 'from b704_record import conv' in S['suite'], lambda S: put(S, 'conv_bad', ['b704_checks.py'])),
    ('G-WORKFLOW-FILES', 'SIDE-explicit-formula`s workflow at main: equal to its last write and that write before the act, no author identifier, no secret, the hold, the cache step for its Mathlib lakefile, the print step over its list, every listed name printed by the probe run, no file this act wrote on main',
     lambda S: wf_ok(S), lambda S: _mut(S, 'wf', lambda d: d[K.KERNEL].update(text=d[K.KERNEL]['text'] + ' secrets.X'))),
    ('G-RUNNER-READ', 'this act`s one run (the faces probe) read by its id: at the probe branch`s tip, success, the artifact`s sha256, the memory low above the hold, no STOP line',
     lambda S: runner_ok(S), lambda S: put(S, 'probet', S['probet'].replace('STOP lines False', 'STOP lines True'))),
    ('G-RUNNER-GATE', 'the probe run`s reading: build exit 0, no build error line, no sorryAx in the print step, the closure log parsed whole with no error line, the artifact`s digest agreeing (the print step`s unknown names are G-WORKFLOW-FILES`s, defect (p))',
     lambda S: gate_ok(S), lambda S: put(S, 'probeax', S['probeax'] + NL + 'sorryAx')),
    ('G-MERGES-ON-GATE', 'SIDE-explicit-formula`s main: no merge this act -- main at v0.37 (38e2734) as b703 left it, its first-parent line past it empty, no sorry in code on main',
     lambda S: merges_ok(S), lambda S: put(S, 'ef_log', [('deadbeef', 'x', 1)])),
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
    ('G-PP-SCOPE', 'PLACE-papers` changed files against the five named (FINDINGS, OPEN_TRAILS, the README, the faces page, One Page Proof) (N5)',
     lambda S: corpus_scope(S), lambda S: put(S, 'pp_changed', S['pp_changed'] + ['day1/Spectral_Inertness.md'])),
    ('G-CURRENTS-UNEDITED', 'the map, the census, the monograph, the Dirichlet page, the surround, both SIMPLICITY copies, REGISTRY, FOUNDATIONS and its partner, INSTRUMENTS, both PATHS copies, the substrate pages, the companions this act does not cut and the archives: working tree, before and HEAD',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'ERRATA.md': (b'x', b'y', b'y')}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read before the seal (read after the probe branch`s deletes)',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b703`s to b695`s sealed tools and the earlier tools, the readers, the push tool, the act-root tool, the generators and their tests, the corrigendum tools, edit_route.py, chain_page.py, e0_rule.py, rule_arms.py, b703`s figures tool and the shared tools: before, working tree and HEAD',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'additive_shared.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at 295e53f0 but the shared additive files (act_roots.txt, the corrigenda bank and the glossary among them), by blob id',
     lambda S: S['prior_bad'] == [] and S['prior_n'] > 0, lambda S: put(S, 'prior_bad', ['data/b703_stepzero.txt'])),
    ('G-FINDINGS-APPEND-ONLY', 'FINDINGS before and now', lambda S: S['fi_pre'] is not None and (S['fi_now'] or b'').startswith(S['fi_pre']),
     lambda S: put(S, 'fi_now', b'x' + (S['fi_now'] or b''))),
    ('G-TRAIL-APPEND-ONLY', 'OPEN_TRAILS before and now', lambda S: S['ot_pre'] is not None and (S['ot_now'] or b'').startswith(S['ot_pre']),
     lambda S: put(S, 'ot_now', b'x' + (S['ot_now'] or b''))),
    ('G-NODISCLOSURE-PUBLIC', 'TECHNE-Core`s needle sets over every public byte the act writes: the ledger lines, the banks, the tools, the glossary`s appended bytes, the README, the faces page and the cut paper',
     lambda S: bool(S['nd_pub']) and not any(S['nd_pub'].values()), lambda S: put(S, 'nd_pub', {'method': 1})),
    ('G-OUTSIDE-NAMED-NOWHERE', 'the ledger lines appended', lambda S: S['outside'] == [], lambda S: put(S, 'outside', ['x'])),
    ('G-DELETE-FREE', 'the act`s tools` code, prose stripped', lambda S: no_delete(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='os' + '.remove(p)'))),
    ('G-PUBLISH-UNCALLED', 'the act`s tools` code: no publish call', lambda S: publish_uncalled(S),
     lambda S: put(S, 'tooltext', dict(S['tooltext'], x='z_' + 'publish()'))),
    ('G-SEALED-AFTER-COMPONENTS', 'the lock time against every relay and PLACE-papers commit of the act by its subject', lambda S: sealed_after_ok(S),
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b704 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash',
     lambda S: 'WHAT RAN AHEAD OF THIS SEAL' in S['face'] and S['lock_epoch'] is not None
     and all(h[:7] in S['face'] for h, s, t in S['rlog'] + S['plog'] if t <= S['lock_epoch']),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'b704_closing.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3), in six parts summed',
     lambda S: S['lock_epoch'] is not None and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    ('G-PRIOR-CLOSED-PUSHED', 'b703`s trail record on OPEN_TRAILS and its root in the chain', lambda S: K.B703_TRAIL_HEAD in S['ot']
     and S['rootsf'].count(NL + 'b703 ') == 1, lambda S: put(S, 'ot', S['ot'].replace('### b703 — lane two', '### b703 - lane two'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], grade_moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s 81st chain row (the corrigendum row apart), the root bank and its items, the faces diff, the cut, the corrigendum and the read bank among them, no binary, mirror, chain-half or untracked bank',
     lambda S: root_banked_ok(S), lambda S: put(S, 'rootsf', S['rootsf'] + 'b705 x y' + NL)),
    ('G-ROOT-BANKS-COMMITTED', 'the root route`s banked reading and every named bank`s blob at the root`s recorded commit: clean and equal at HEAD, HEAD the remote main, the recorded hash carried by the recorded commit',
     lambda S: root_banks_committed_ok(S), lambda S: put(S, 'rootbanks', dict(S['rootbanks'], pushed=False))),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit in two halves by act with the suite`s own remote reads: standing-b2`s banked b624-b658 and standing-b3`s b659-b704 all AGREE, the boundary link equal, b680 read through its corrigendum row (4 banks), b704 written LF',
     lambda S: verify_ok(S), lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s through conv, and its parts, the read rule`s arm and the finite-sum node among them', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line, the head through conv', lambda S: bool(S['tj'].get('line'))
     and oline(S, S['tj']['line']) == conv(S['REC'].TRAIL_HEAD()), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b704 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b704_record.py agree', 'b704_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line: b705', lambda S: '**Next:** b705' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** b705', '**Next:** b706'))),
] + [('G-N%d-SCORED' % i, 'the scores through the record tool`s reader, and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i),
      lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written since 295e53f0 and 1532695 against the (W) globs',
     lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith('b704')" in S['suite'] and "'data/b704_components.txt' in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b704_closing.py: the closing sentence in the rule`s words with the plain reads named; the citation check, the record lines, the dry run, the corrigendum and the read rule, the faces probe, the cells, the README, the glossary, the re-cut, the standing arms, the orders, the kernels, the mirror, the carry-time reading',
     lambda S: closing_sentence_ok(S), lambda S: put(S, 'closing_src', S['closing_src'].replace('no identifier of the author ' + 'in any outbound', 'x'))),
    ('G-LSREMOTE-ONE-PER-REPO', 'the part`s ls-remote calls per repository, read after every other arm of the part has run (OPEN_TRAILS :12703)',
     lambda S: lsr_ok(S), lambda S: put(S, 'lsr', {PP: 2})),
    ('G-CORRESPONDENCE-CURRENCY', 'every roster paper`s Correspondence rows by tools/b703_standing_figures.py against the kernel`s current tag and the statement at the cited tag: the changed-statement rows no more than the previous act`s figure (its reach printed: the 16 kernels the generator parses, SIDE-explicit-formula not among them)',
     lambda S: fig_ok(S, 'correspondence'), lambda S: _raise_fig(S, 'correspondence')),
    ('G-README-CURRENCY', 'the PLACE-papers README`s tags and counts against ls-remote by tools/b703_standing_figures.py: the stale lines no more than the previous act`s figure',
     lambda S: fig_ok(S, 'readme'), lambda S: _raise_fig(S, 'readme')),
    ('G-PARTNER-COPIES', 'the lines differing between the two copies of each roster paper`s Correspondence table by tools/b703_standing_figures.py: no more than the previous act`s figure, until b706`s disposition',
     lambda S: fig_ok(S, 'partners'), lambda S: _raise_fig(S, 'partners')),
    ('G-SISTER-PINS', 'each kernel`s lean-toolchain and Mathlib revision beside the federation`s by tools/b703_standing_figures.py: no kernel the faces page names moved pin against the baseline',
     lambda S: sister_pins_ok(S), lambda S: _raise_fig(S, 'pins')),
] + [(nm, 'tools/rule_arms.py (the author`s word on (R293)(6); (R301)(6) for four; G-RULE-SUITE-PARTS as repaired under (R302)(2); G-RULE-BINARY-HASHES as repaired under (R306)(2); G-RULE-RECUT-QUOTE`s sources as repaired under (R313)(2)) -- ' + reads,
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
    p = os.path.join(D, 'b704_seal_hashes.json')
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
    print('  written: b704_seal_hashes.json')
    return 0


def _base_name(pushed):
    if PRERUN:
        return 'b704_arms_prerun.txt'
    if MID and len(sys.argv) > sys.argv.index('--mid') + 1:
        return sys.argv[sys.argv.index('--mid') + 1]
    if RERUN and len(sys.argv) > sys.argv.index('--rerun-postpush') + 1:
        return sys.argv[sys.argv.index('--rerun-postpush') + 1]
    return 'b704_checks_postpush.txt' if pushed else 'b704_checks.txt'


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
    base = 'b704_arms_prerun.txt' if prerun else ('b704_checks_postpush.txt' if (rerun or pushed) else 'b704_checks.txt')
    out = [('data/' + _part_name(base, '<part>')), ('data/' + _part_name(base, '<part>').replace('b704_arms_prerun', 'b704_lsr_prerun').replace('b704_checks', 'b704_lsr').replace('.txt', '.json')),
           'data/b704_exercise_<part>.json']
    seconds = ['data/b704_arm_seconds_<part>.json'] if prerun else []
    return out, seconds


def guard_dry():
    """for each run mode, what the writer block would write; nothing written by this route, the record tool banks it."""
    for mode, args in (('prerun', (True, False, False, False)), ('pre-push', (False, False, False, False)), ('post-push', (False, True, False, True))):
        out, seconds = writer_plan(*args)
        print('  MODE %-9s | the part`s banks: %s | the per-part seconds bank: %s' % (mode, ', '.join(out), ', '.join(seconds) or 'NONE'))
    print('  ### POST-ROOT PATH WRITES NONE of the root-named per-part seconds banks: the pre-push and post-push modes write no data/b704_arm_seconds_<part>.json')
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
    out = ['=' * 104, heads[0].replace('PART standing-a', 'SIX PARTS SUMMED'), '=' * 104] + [
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
        ex.update(jl('b704_exercise_%s.json' % part).get('exercise') or {})
    if ex and base in ('b704_checks.txt', 'b704_checks_postpush.txt'):
        e = (json.dumps(dict(exercise=ex, run=n, live_failing=fails, defective=defs, neg_failures=ng), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p_ = os.path.join(D, 'b704_exercise.json')
        with open(p_ + '.tmp', 'wb') as fh:
            fh.write(e)
        os.replace(p_ + '.tmp', p_)
    print(NL.join(out[3:15]))
    print('  written: %s' % base)
    return 0 if ok else 1


# ### the standing arm the author's word adds fails at b704 on defects (i) and (o), and G-README-CURRENCY on the ordered append at README :135 (defect
# ### (n), the author's word at the README-figure prompt) -- each declared on the face, section (G2), as a carried failure; the combine reads
# ### them by name, and no other failure is carried
CARRIED_FAILING = ('G-READ-RULE-STANDING', 'G-README-CURRENCY', 'G-WORKFLOW-FILES')   # ### the third on defect (p), found by the pre-run


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
    rec('b704 -- THE SUITE. ### **%s READING.** ### PART %s ### every arm exercised on both controls.' % (
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
    rec('  ### (R264)(2) THE FREEZE: the standing arms (b703`s face less its own arms, the twenty-four rule arms among them, and the one (R314)(2) adds) %d ; '
        'carried here %d ; the act`s arms over its own banks %s ; arms beyond both %s' % (
            len(S['standing']), len(set(names) & set(S['standing'])), sorted(set(names) - set(S['standing'])),
            sorted(set(names) - set(S['standing']) - set(K.ACT_ARMS)) or 'NONE'))
    rec('  ### standing arms not carried here: %s' % (sorted(set(S['standing']) - set(names)) or 'NONE'))
    if 'figures' in NEED[PART]:
        rec('  ### THE FOUR STANDING FIGURES, each against the previous act`s (%s):' % S['fig_prev_name'])
        for k in ('correspondence', 'readme', 'partners', 'pins'):
            rec('  ###   %-15s live %s ; previous %s' % (k, (S['fig'].get(k) or {}).get('figure'), (S['fig_prev'].get(k) or {}).get('figure')))
        ok_, n_, off_, pre_, form_ = RDA.reading_text(S['reads_bank'])
        rec('  ### G-READ-RULE-STANDING`S READING (relay data/b704_read_calls.txt): %s ; rows %d ; offences %d %s ; the cap`s precursors, printed and not counted, %d %s' % (
            'PASS' if ok_ else 'FAIL', n_, len(off_), [RDA._show(r) for r in off_], len(pre_), [RDA._show(r) for r in pre_]))
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
            rec('  ### the reads at commit, b680: %s ; b704: %s' % (S['ar_reads'].get('b680'), S['ar_reads'].get('b704')))
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
    rec('  ### PLACE-papers` changed files %d against the allowed %d (the two ledgers, the README, the faces page, the cut paper): beyond %s' % (
        len(S['pp_changed']), len(S['pp_allowed']), sorted(set(S['pp_changed']) - set(S['pp_allowed'])) or 'NONE'))
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s ; first-parent commits past v0.37 %d ; the probe run %s' % (
        S['ef_main'][:12], (S['ef_tags'].get('v0.37') or '')[:12], len(S['ef_log']), S['probej'].get('run_id')))
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
    lp = os.path.join(D, _part_name(base, PART).replace('b704_arms_prerun', 'b704_lsr_prerun').replace('b704_checks', 'b704_lsr').replace('.txt', '.json'))
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    with open(lp + '.tmp', 'wb') as fh:
        fh.write(lb)
    os.replace(lp + '.tmp', lp)
    ex = dict(exercise=EX, run=len(arms), live_failing=fail, defective=defective, neg_failures=negfail, part=PART)
    ep = os.path.join(D, 'b704_exercise_%s.json' % PART)
    with open(ep + '.tmp', 'wb') as fh:
        fh.write((json.dumps(ex, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(ep + '.tmp', ep)
    # ### THE GUARD HELD -- the per-part seconds bank (root-named, gathered by the record tool's armsecs before the seal) is written by the pre-run
    # ### alone, as tools/b700_checks.py :1669 had it and b702 restored; the pre-push and post-push runs write no root-named bank
    if PRERUN:
        sp = os.path.join(D, 'b704_arm_seconds_%s.json' % PART)
        with open(sp + '.tmp', 'wb') as fh:
            fh.write((json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), part=PART, arms=SECS, phases=S['phase_secs'], run_secs=int(secs)),
                                 indent=1, ensure_ascii=False) + NL).encode('utf-8'))
        os.replace(sp + '.tmp', sp)
    print('  written: %s' % os.path.basename(out))
    carried_only = [f for f in fail if f not in CARRIED_FAILING] == [] and not defective and negfail == 0
    return 0 if (not fail and not defective and negfail == 0) else (4 if carried_only else 1)


if __name__ == '__main__':
    sys.exit(main())
