# -*- coding: utf-8 -*-
"""b722_checks.py -- THE SUITE OF b722, UNDER (R332): b721'S CLOSE COMPLETED; THE CORRIGENDUM, THE DIFFERS AND ERRATA; THE LAW AT -20 AND
-47; THE DERIVATION'S REMAINING STEP; THE OFFSET, POST HOC; THE SURGERY CARRIED; THE ARMS RETIRED; THE COUNT LAW'S ROUTE PRICED; THE TOUCH
READ; SEVEN PARTS AS b706 SPLIT THEM.

### ### Component 7 (the Edit tool): the act's sources, predicates and arms over this act's banks replace b721's (b721's decomposition, A0,
### count read, box, two reads, toolset, pin and records, read from banks this act does not write, not carried) -- see the act section: the
### registrations first, the coefficients' law, the derivation graded, the offset post hoc, the surgery carried, the arms retired, the count
### route priced, the DIFFERS and ERRATA entries, the touch read, the arms' tags. (R332)(10): the arm list is tools/standing/arms.py
### run_list(ARMS), the retired arms out of every part, the seal and the tallies; the claim arms' figure printed beside the suite's.

### ### **EVERY ARM IS A PREDICATE OVER A SUPPLIED SOURCE**, run three ways: LIVE on the sources, NEG on an unmutated copy (it
### must agree with LIVE), POS on a mutated copy (it must FAIL). ### **AN ARM THAT PASSES ITS POSITIVE CONTROL IS DEFECTIVE.**
### ### **NO ARM READS ONLY THE FACE.** An arm that cannot read its source FAILS; it is never skipped.
### ### The arm set is the sealed face's (G2) block (G-ARMS-DECLARED-EQ-RUN). `--prerun` (R202)(3): every arm run at HEAD before the face is
### sealed. `--seal`: the sealed tools' sha256 recorded. Every remote read once per run (OPEN_TRAILS :12703). THE SUITE CALLS NO PLATFORM.
### ### data/b684_rules.txt row (1) and b706's split, carried: every run in SEVEN foreground parts, each its own call in its own message --
### `--part standing-a`, `--part standing-c` (G-PRIORBANK-UNCHANGED, G-NODISCLOSURE-PUBLIC, G-WRITELIST-KINDS, the four standing figures and
### G-READ-RULE-STANDING), `--part standing-b1` (the shared additive files), `--part standing-b2a` (the act-root chain over b624-b641, its
### verdicts banked, NO ARM), `--part standing-b2b` (b642-b658, banked, NO ARM), `--part standing-b3` (the second half, b659-b722, and
### G-ACTROOT-VERIFY once over every banked verdict), `--part act` (the act's arms over this act's banks, the table regenerated in a closing run);
### each under the 590 s guard, NOT RUN beneath the 2,560 MB hold; `--combine <bank>` writes the bank. The chain halves as b693 drew them with
### b722 added to the second (the ferry's Component 5).
### ### (R264)(2), THE FREEZE: the standing arms are b721's face's (G2) arms less b721's own arms over b721's banks, carried, the twenty-four rule
### arms of tools/rule_arms.py and G-READ-RULE-STANDING among them; NO standing arm is added (N5). THE REPAIRS (R332)(3) ORDERS, each a diff in
### relay data/b722_tool_repairs.txt with its controls (data/b722_repair_controls.txt, 16 cases): G-REPORT-UNSEALED's key read case-insensitively
### (keys_ci) and G-AXIS-REGISTERED's bank read after joining wrapped lines (joined), both helpers here and the report arm reading through keys_ci;
### the lock gate's argument required; the lean-running test reading banked prints. G-RECEIPT-IN-FULL repointed to read the standing clauses by
### version ((R332)(4)). This suite carried by tools/b722_carry.py from tools/b721_checks.py (the act names substituted) and its act sections
### written by the Edit tool at the spans b721's repair diff names (data/b721_repairdiff_checks.txt): the sources over this act's banks and the
### arms over them (the weight and readings lines, the repairs, the standing clauses, reading 5, the moves record, the registrations, the fit)
### in place of b721's (the grid, the pairs, the port, the axis).
### The four standing figures read by tools/b706_standing_figures.py (unedited, over b706's roster) against b721's baselines
### (data/b721_standing_figures.json), each by b703's fig_ok. The standing runner arms (G-WORKFLOW-FILES, G-RUNNER-READ, G-RUNNER-GATE,
### G-MERGES-ON-GATE) read b721'S ONE RUN as banked -- no dispatch this act ((R332)(7)) -- port-b707 at b721's one commit (run 40123142437), its
### conclusion failure (11 of 12 modules, no grade claimed), the branch held, no main moved, no tag made, no merge.
### ### The PRERUN guard held: the per-part seconds bank is written under `if PRERUN:` alone, so no root-named bank is written by the pre-push or
### post-push run; `--guard-dry` prints, for each run mode, what the writer block would write, writing nothing.
### ### Every look-up of a landed line goes through the one conversion (imported from tools/b652_record.py through tools/b722_record.py).
### ### The harness is b568's to b721's, written by the Write tool from tools/b721_checks.py, its pure helpers imported from tools/b703_checks.py
### ### (sealed at b703 and unedited); the sources, predicates and arms over this act's banks are b722's (the act's arms over this act's banks,
### ### the b721 arms over b721's objects not carried). data/b686_rules.txt row (1): the act arm G-ENTRY-SCORES-EQUAL reads the landed entry; no
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
import b722_worklist as K     # noqa: E402
import b722_record as REC0    # noqa: E402  ### imported before b721's and b703's suites: b698's record tool is then rebound to b722 once
from b722_record import conv  # noqa: E402
import b721_worklist as K707  # noqa: E402  ### the previous act's worklist (its arms, its sealed tools, its heads for --prev)
import b712_worklist as KR    # noqa: E402  ### the act whose runs the standing runner arms read as banked (b712's three; none since, N1)
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
import act_close as AC        # noqa: E402  ### (R332)(4): the close's shared functions, one form for every tool (a repair at b722)
import act_letters as AL      # noqa: E402  ### (R332)(6)(v), v5 row (78): the one lettering, the corrigendum tool's and this suite's
from standing import arms as STA    # noqa: E402  ### (R332)(4)(i): the previous act's longest phase from its root-named part banks
from standing import close as STC   # noqa: E402  ### (R332)(4)(ii), (vi): the withheld field from the ruling, neg_shown's three lists


def _owners(rows):
    """(R332)(4)(iii), standing clauses v4 row (64), ONE COUNTER: (navigator, seat) from tools/act_close.py defect_owners, the one function
    every tool imports -- b703's _owners counted the seat as every row not the navigator's (22 at b721) where the trail arm counted THE SEAT'S
    alone (21); both now read the one count (a repair at b722, banked by diff)."""
    o = AC.defect_owners(rows)
    return o['NAVIGATOR'], o['SEAT']
_post_seal_named, edit_route_ok, PART_FOOT, KIND = C3._post_seal_named, C3.edit_route_ok, C3.PART_FOOT, C3.KIND

NL = chr(10)
PP = K.PP
EF = K.EF_DIR                 # ### SIDE-explicit-formula, read unmoved this act
LV = K.LV_DIR                 # ### the kernel this act wrote: port-b707 given one commit, held; no main moved
KI = K.JOIN_DIR               # ### the join kernel, read unmoved
FACE = os.path.join(D, 'b722_registration_%s.txt' % K.DATE)
B707_FACE = os.path.join(ROOT, *K.B711_FACE.split('/'))   # ### the previous act's face (b721's, data/b721_registration_2026-10-25.txt), the standing arms' source
PRE = dict(relay=K.PRE_RELAY, pp=K.PRE_PP)
EXPORT = K.EXPORT
RERUN = '--rerun-postpush' in sys.argv
MID = '--mid' in sys.argv
PRERUN = '--prerun' in sys.argv
SEAL = '--seal' in sys.argv
COMBINE = '--combine' in sys.argv
GUARD_DRY = '--guard-dry' in sys.argv
# ### (R332)(2)(iii), standing clauses v2 row (54): `--prev --part <p>` runs every arm of the part on the PREVIOUS ACT'S banks before the seal --
# ### the banks' act prefix, the face, the worklist and the pre-act heads read as b721's (_prev_rebind, at the foot) -- and banks each arm's
# ### verdict beside b721's own (data/b721_exercise.json): an arm passes there unless b721 failed it. ACTN is the act whose banks the run reads.
PREV = '--prev' in sys.argv
# ### standing clauses v5 (ii): the act's figures from one source, read at run time from the step bank and the chain (tools/act_close.py
# ### act_figures) -- the act, the next act, the chain rows and the root check's range; none is carried as a constant (b721's (e)-(h))
AF = AC.act_figures()
ACT_NOW, NEXT_ACT, PREV_ACT = AF['act'], AF['next_act'], 'b%d' % (int(AF['act'][1:]) - 1)
ACTN = PREV_ACT if PREV else ACT_NOW
PART =sys.argv[sys.argv.index('--part') + 1] if '--part' in sys.argv and len(sys.argv) > sys.argv.index('--part') + 1 else None
L = []
# ### the sealed figures, the floors the count arms read at HEAD (standing from (R291)(3)): one prompt -- the root's ((R332)(8): "the root's
# ### prompt once"; no prompt before the seal this act), one call, its answer checked once per (R278)(4); the letters at the seal, every one the
# ### seat's (set at the seal from the defects bank)
FLOORS = dict(prompts=1, calls=1, checks=1, defects=tuple((c, 'NAVIGATOR' if c in 'de' else 'SEAT') for c in 'abcdefghijklmnopqrstuvwxyz'))   # ### (a)-(z) at the seal, (d) and (e) the navigator's, every other the seat's


def _bank_utc(text):
    """the UTC stamp a bank's head line carries, '(YYYY-MM-DDTHH:MM:SSZ)', as an epoch; None where absent."""
    m = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', NL.join((text or '').split(NL)[:2]))
    return iso_epoch(m.group(1)) if m else None


REPAIRED_TOOLS = K.REPAIRED_TOOLS
NEW_TOOLS = K.NEW_TOOLS
# ### the instruments read unedited: b703's list with b703's figures tool, b695's to b721's sealed tools, their new and repaired tools (b721's two
# ### shared tools and the roster among them, unedited this act), less this act's sealed tools
INST_BASE = tuple(C3.INST_BASE) + ('b703_standing_figures.py',)
INST = tuple(sorted((set(INST_BASE) | set(K695.SEALED) | set(K696.SEALED) | set(K697.SEALED) | set(K698.SEALED) | set(K699.SEALED) | set(K700.SEALED)
                     | set(K701.SEALED) | set(K702.SEALED) | set(K703.SEALED) | set(K704.SEALED) | set(K704.NEW_TOOLS) | set(K704.REPAIRED_TOOLS)
                     | set(K705.SEALED) | set(K705.NEW_TOOLS) | set(K705.REPAIRED_TOOLS) | set(K706.SEALED) | set(K706.REPAIRED_TOOLS)
                     | set(KR.SEALED) | set(getattr(KR, 'NEW_TOOLS', ())) | set(getattr(KR, 'REPAIRED_TOOLS', ()))
                     | set(p[6:] if p.startswith('tools/') else p for p in getattr(KR, 'REPAIRED_DATA', ()))
                     | set(K707.SEALED) | set(getattr(K707, 'NEW_TOOLS', ())) | set(getattr(K707, 'REPAIRED_TOOLS', ()))
                     | set(p[6:] if p.startswith('tools/') else p for p in getattr(K707, 'REPAIRED_DATA', ())))
                    - set(K.SEALED) - set(REPAIRED_TOOLS) - set(NEW_TOOLS) - {'b722_report.py'}))


def _renamed():
    return dict((r['versioned'], r['unversioned']) for r in (jl('b706_partners.json').get('rows') or []) if r.get('versioned') and r.get('unversioned'))


# ### the corpus documents this act does not write: b703's list at the files of record after (R316)(3); no document is cut this act
CURRENTS = tuple(p for p in dict.fromkeys(_renamed().get(p, p) for p in C3.CURRENTS) if p not in K.PP_EDITED)   # ### less the files (R332)(5)(iii)-(iv) edits on main
TABLE_FILES = K.TABLE_FILES
WF, PT = '.github/workflows/build-module.yml', 'print_targets.txt'
PORT_LABEL = KR.PORT_LABEL    # ### b712's runs, read as banked by the standing runner arms (no dispatch at b721 or this act)
CARRIED_NAMES = ('record', 'checks', 'closing', 'reg_gate', 'regspec', 'corrigendum', 'citation', 'worklist', 'standing', 'report')   # ### b722's carry banks (no tests tool carried: (R332)'s Component 0 runs no test)
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
NEXT_RULES_GLOB = 'relay/data/b722_rules.txt'   # ### (R332)(12): data/b722_rules.txt and data/b722_rules.txt named by form; this act writes no rules bank
# ### (R315)(2)(b), b705's repaired predicate, carried: the root bank's items read against the root route's own item list, and the required list
# ### read against ROOT_EXCLUDE here, at import (b706's (j)); the binary banks (.gz) are not root items (data/b680_rules.txt row (1)), their hashes banks are
# ### this act's banks by its components, set by the Edit tool after the lock, before the seal, in place of b721's carried names (the DIFFERS,
# ### ERRATA, the offset read, the surgery, the arm history and retirement, the count price: no bank of this act's) (events (4))
# ### Component 8, the Edit tool: this act's banks by its components, in place of b721's carried names (its coefficients, challenge, pin, price)
REQUIRED_BANKS = ('data/b722_corrigendum.txt', 'data/b722_standing_v122.txt', 'data/b722_coeffs_controls.json', 'data/b722_coeffs.txt',
                  'data/b722_walk.txt', 'data/b722_c2_statement.txt', 'data/b722_c2_price.txt', 'data/b722_instruments.txt',
                  'data/b722_instrument_entries.json', 'data/b722_reproduce.txt', 'data/b722_reproduce.json', 'data/b722_propagation.txt',
                  'data/b722_propagation_landing.json', 'data/b722_axiom_diag.txt', 'data/b722_llm_line_drafts.txt',
                  'data/b722_address_scan.txt', 'data/b722_touch.txt',
                  'data/b722_standing_figures.txt', 'data/b722_stepzero.txt', 'data/b722_report.txt',
                  'data/b722_citation_check.txt', 'data/b722_readfirst.txt', 'data/b722_kernels_face.json')
STANDING_BANK = 'data/standing_clauses_v7.txt'   # ### a shared bank by version, outside the act's prefix, named apart: v7 binds the act whole, v8 from 0ff64911 ((R332)(8))
from standing import rootbanks as STR   # noqa: E402  ### the class repair (3)(vi): the import check made one standing function
STR.guard(REQUIRED_BANKS, REC0.R.ROOT_EXCLUDE)


def rec(s=''):
    L.append(s)
    print(s)


def _act_code(path):
    """the act's code in a tool: the whole file for this act's own tools; for a shared tool the ruling orders edited ((R332)(3)-(4)) the lines
    this act added to it alone (`git diff` from the act's base, its `+` lines) -- the shared tool's earlier code is its own act's, read by that
    act's arms (b378's fixture cleans its temporary directory, a line this act did not write)."""
    if os.path.basename(path) not in REPAIRED_TOOLS:
        return read(path)
    d = gs(ROOT, 'diff', PRE['relay'], '--', 'tools/' + os.path.basename(path))
    return NL.join(l[1:] for l in d.split(NL) if l.startswith('+') and not l.startswith('+++'))


def is_pushed():
    return (gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')
            and gs(ROOT, 'log', '-1', '--pretty=%s').startswith(ACT_NOW)
            and 'data/%s_components.txt' % ACT_NOW in gs(ROOT, 'show', '--name-only', '--pretty=format:', 'HEAD'))


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
    """tools/rule_arms.py's sources over the seat's session from (R332)'s anchor, its call trace extended by any continuation session's
    (K.SESSIONS_AFTER, none so far) through rule_arms.transcript."""
    R_ = RA.sources(ACT_NOW, SESSION, K.ANCHOR, K.PARTS, lock, PRE['relay'], PRE['pp'])
    for sid, anc in K.SESSIONS_AFTER:
        R_['calls'] = list(R_.get('calls') or []) + RA.transcript('%s/%s.jsonl' % (PROJ, sid), anc)
    # ### (R332)(4)(i): G-RULE-LONG-PHASE-SPLIT's figures from the previous act's part banks, each read against its root's sha256 (the
    # ### combined bank rule_arms.py :305 reads is one no act writes); a refused bank is counted apart and never read
    pl = STA.prev_longest(PREV_ACT, K.PARTS)
    R_['prev_longest'], R_['prev_parts'], R_['prev_refused'] = pl['longest'], pl['parts_read'], pl['refused']
    return R_


def conv_alone():
    P = 'p' + 'oss('
    toks = ['def _' + P, 'def ' + P, '._' + P, '.' + P, ' ' + P, '(' + P, '=' + P, 'Q.' + 'line_of', 'Q.' + 'guard_absent', 'Q.' + 'append_to',
            'def ' + 'conv(']
    bad = []
    for f in sorted(os.listdir(T)):
        if (f.startswith('b722_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS:
            t = strip_prose(read(os.path.join(T, f)))
            if any(x in t for x in toks):
                bad.append(f)
    return bad


def spec_planted():
    import b722_regspec as SPEC
    P = SPEC.planted()
    ctl = [ok for _w, ok in SPEC.controls()]
    return dict(read=[ok for _s, ok, _w in P], controls=ctl, shapes=[s for s, _o, _w in P])


def _deps(ax):
    return REC0._deps(ax)


def _tag_peel(repo, tag):
    return gs(repo, 'rev-parse', '--verify', '--quiet', 'refs/tags/%s^{commit}' % tag)


def _rebuild_state():
    """(R332)(7)(iii), N5: each wave 1 kernel's rebuild branch -- its local tip, its remote tip (the tracking ref the push wrote), whether the tip is
    the pin or descends from it, whether it is on main, the tags pointing at the tip, the pin's tag peeled, and main now."""
    out = {}
    for k, tag, p in K.WAVE1:
        repo = 'D:/' + k
        pin = gs(repo, 'rev-parse', '--verify', '--quiet', p + '^{commit}')
        tip = gs(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.REBUILD_BRANCH)
        out[k] = dict(pin=pin, tip=tip, remote=gs(repo, 'rev-parse', '--verify', '--quiet', 'refs/remotes/origin/' + K.REBUILD_BRANCH),
                      from_pin=bool(tip) and subprocess.run(['git', '-C', repo, 'merge-base', '--is-ancestor', pin, tip]).returncode == 0,
                      on_main=bool(tip) and subprocess.run(['git', '-C', repo, 'merge-base', '--is-ancestor', tip, 'main']).returncode == 0,
                      tip_tags=[x for x in gs(repo, 'tag', '--points-at', tip).split(NL) if x.strip()] if tip else [],
                      tag_peel=_tag_peel(repo, tag), main=gs(repo, 'rev-parse', 'main'),
                      count=gs(repo, 'rev-list', '--count', '%s..%s' % (pin, tip)) if tip else '',
                      wf_main=bool(read_blob(repo, 'main:.github/workflows/build-module.yml')),
                      wf_tip=read_blob(repo, '%s:.github/workflows/build-module.yml' % tip) if tip else None,
                      author=gs(repo, 'log', '--format=%an <%ae>', '%s..%s' % (pin, tip)) if tip else '')
    return out


def wf_state():
    """b721's runs at two kernels, read as banked (N1: no dispatch this act, b710's form over b709's run): at SIDE-lv-conservation the workflow at
    port-b707's tip equal to the workflow at b709's commit, written before b721; the lakefile and its Mathlib requirement; the print list ABSENT at
    the branch; b721's two commits on the branch each the one module. At SIDE-faces-join the workflow at main equal to the manifest commit's; the
    lakefile's Mathlib requirement; the print list present (FacesJoin); b721's one write the lakefile. The constants b721's (K707)."""
    out = {}
    for kern, repo, tip, base, writes, want in ((K.KERNEL, LV, KR.PORT_NEW_TIP, KR.PORT_BASE, (KR.PORT_EDIT1, KR.PORT_NEW_TIP), [KR.PORT_FILE]),
                                                ('SIDE-faces-join', KI, KR.JOIN_NEW_TIP, KR.JOIN_TIP, (KR.JOIN_NEW_TIP,), ['lakefile.toml'])):
        src = read_blob(repo, '%s:%s' % (tip, WF)) or ''
        before = read_blob(repo, '%s:%s' % (base, WF)) or ''
        lf = read_blob(repo, '%s:lakefile.lean' % tip) or read_blob(repo, '%s:lakefile.toml' % tip) or ''
        req = re.search(r'(?is)require\s+(?:"?mathlib"?|\[\[require\]\]\s*name\s*=\s*"mathlib")', lf)
        pt = read_blob(repo, '%s:%s' % (tip, PT)) or ''
        wrote = gs(repo, 'log', '-1', '--format=%H', tip, '--', WF)
        act_writes = [[x for x in gs(repo, 'diff-tree', '--no-commit-id', '--name-only', '-r', c).split(NL) if x.strip()] for c in writes]
        out[kern] = dict(text=src, before=before, wrote=wrote, wrote_before_act=bool(wrote) and wrote not in writes,
                         lakefile=bool(lf.strip()), mathlib=bool(req), targets=[l.strip() for l in pt.split(NL) if l.strip()], print_list_absent=not pt.strip(),
                         act_writes=act_writes, want=[want] * len(writes))
    return out


STANDING = sorted((set(g2_of(B707_FACE)) - set(K707.ACT_ARMS)) | set(K.STANDING_ADDED))
TESTS = ('test_no_sorry_main.py', 'test_axiom_claim.py', 'test_module_header.py', 'test_conversion_b652.py')


# ================================================================== THE CHAIN SPLIT BY ACT (b693's halves, b722 added; the first half in two quarters)
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
    return base.replace('b722_', '').replace('.txt', '')


def half_bank(i, key):
    """i is 'a1', 'a2' (the first half's quarters) or 'b' (the second half)."""
    return 'b722_chain_half_%s_%s.json' % (i, key)


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


def _addr_live():
    """(R332)(9)(i): the address scan run live (no --bank: it writes nothing), its two counts read from its foot; the address and the name are
    held by the tool alone and never reach this suite."""
    p = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b722_address_scan.py'), 'scan'], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    m = re.search(r'\*\*PREVIOUS ADDRESS: (\d+) ; THE AUTHOR`S NAME: (\d+) ;', p.stdout)
    return dict(rc=p.returncode, addr=int(m.group(1)) if m else None, name=int(m.group(2)) if m else None, out=p.stdout)


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
    lockn = sorted(f for f in os.listdir(D) if f.startswith('b722_lockgate_notes'))
    tools = sorted(os.path.join(T, f) for f in os.listdir(T) if (f.startswith('b722_') and f.endswith('.py')) or f in REPAIRED_TOOLS or f in NEW_TOOLS)
    local = os.path.join(ROOT, *K.LOCAL_BANK.split('/'))
    cit = jl('b722_citation_check.json')
    try:
        REC.R._defect_short()
        refuses = False
    except TypeError:
        refuses = True
    t0 = time.time()
    cmds = capture_now()
    ranking = (rd('b705_i6_ranking.txt') or '').split(NL)
    gz_g, gz_p = os.path.join(D, 'b722_grid.json.gz'), os.path.join(D, 'b722_pairs.json.gz')
    S = dict(
        REC=REC, ER=ER, face=face, ferry=rd('b722_ferry.txt'), scan=rd('b722_ferry_scan.txt'), stepz=rd('b722_stepzero.txt'),
        readfirst=rd('b722_readfirst.txt'), defects=rd('b722_defects.txt'),
        lock=read(os.path.join(D, lockn[-1])) if lockn else '', lock_epoch=utc_epoch(face, 'locked at (UTC)'),
        seal=subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'reg_seal.py'), '--verify', FACE], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout,
        answers=rd('b722_author_answers.txt'), answersj=jl('b722_author_answers.json'), prerun=rd('b722_arms_prerun.txt'), rl=jl('b722_record_lines.json'),
        tests=jl('b722_tests_stepzero.json'), testst=rd('b722_tests_stepzero.txt'), withheld=jl('b722_tests_withheld.json'),
        tracked_tests=sorted(os.path.basename(x) for x in gs(ROOT, 'ls-tree', '--name-only', PRE['relay'], 'tools/').split(NL)
                             if re.match(r'^test_.*\.(py|sh)$', os.path.basename(x))),
        sealj=jl('b722_seal_hashes.json'), sealnow=sealed_now(), cmds=cmds, prev_cmds=prev_now(), cmdj=jl('b722_commands.json'),
        cmdt=rd('b722_commands.txt'), reads_bank=rd('b722_read_calls.txt'), reads_json=jl('b722_read_calls.json'),
        planted={t: run_test(t) for t in TESTS}, spec=spec_planted(), conv_bad=conv_alone(), suite=read(os.path.join(T, 'b722_checks.py')),
        citation=rd(K.CITATION_BANK), cit_at=iso_epoch(cit.get('at') or ''), cit_misses=cit.get('misses') or [],
        gate=rd('b722_reg_gate.txt'), rowgen=rd('b722_rowgen_stepzero.txt'),
        branch_lists=dict((repo, gs(repo, 'branch', '--list', *bs)) for repo, bs in K.DELETE),
        kept_tips=dict((b, gs(repo, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + b)) for repo, b in K.KEPT_BRANCHES),
        repairdiffs=dict((n_, rd('b722_repairdiff_%s.txt' % n_)) for n_ in CARRIED_NAMES), carry_banks=dict((n_, rd('b722_carry_%s.txt' % n_)) for n_ in CARRIED_NAMES),
        spans=rd('b722_carry_spans.txt'), rec_src=read(os.path.join(T, 'b722_record.py')),
        closing_src=read(os.path.join(T, 'b722_closing.py')),
        defshort=dict(prev=len(REC._defect_short(PREV_ACT)), refuses=refuses),
        defshort_b722=REC._defect_short(ACTN), letters_seal=REC.letters_at_seal(ACTN),
        corrj=jl('b722_corrigendum.json'), corrt=rd('b722_corrigendum.txt'), corrigenda=rd('b675_corrigenda.txt'),
        corrigenda_tri=tri(ROOT, 'data/b675_corrigenda.txt', PRE['relay']),
        guard=rd('b722_guard_dry.txt'), guardj=jl('b722_guard_dry.json'),
        rootdry=rd('b722_root_banks_dry.txt'), rootdryj=jl('b722_root_banks_dry.json'),
        figj=jl('b722_standing_figures.json'), figt=rd('b722_standing_figures.txt'),
        # ### the standing clauses v6 (written at this act's step zero, (R332)(2)) and its control, this act's bank
        standing_bank=read(os.path.join(ROOT, *STANDING_BANK.split('/'))), standing_v4=read(os.path.join(ROOT, *K.DATA_STANDING_V4.split('/'))),
        standing_v4_pre=cr0(blob(ROOT, '%s:%s' % (PRE['relay'], K.DATA_STANDING_V4))),
        standing_ctlj=jl('b722_standing_control.json'), standing_ctl=rd('b722_standing_control.txt'),
        visibility=read(os.path.join(ROOT, *K.REPO_VISIBILITY.split('/'))),
        membrane_src=read(os.path.join(T, 'act_membrane.py')), act_close_src=read(os.path.join(T, 'act_close.py')),
        letters_src=read(os.path.join(T, 'act_letters.py')), corr_src=read(os.path.join(T, 'b722_corrigendum.py')),
        hook_src=read(os.path.join(T, 'standing', 'hook.py')), hook_ctl=rd('b722_hook_control.txt'), hook_refusals=rd('b722_hook_refusals.txt'),
        settings=read('D:/.claude/settings.json'),
        # ### (R332)(3)-(11): the act's figures and the arms' tags; the corrigendum's companions (the DIFFERS entry, ERRATA's); b722's
        # ### registrations at each of their four commits and at HEAD, the prediction, the controls and the coefficients; the derivation; the
        # ### offset read; the surgery; the arms' history and retirement, the standing run list; the count route's price; the touch read
        act_cur=jl('act_current.json'), act_cur_z=_s(blob(ROOT, '%s:%s' % (K.ACT_CURRENT_COMMIT, K.ACT_CURRENT))),
        arm_tags=jl('arm_tags.json'), verifier_src=read(os.path.join(T, 'mirror_verify.py')),
        differs=rd('b722_differs.txt'), errata=rd('b722_errata.txt'), errata_pp=read(os.path.join(PP, 'ERRATA.md')),
        # ### (R332)(3)-(12), Component 8, the Edit tool (b721's keys over b721's objects in git at b721's suite): b721's registrations at
        # ### HEAD against their commits; the computation banks of (3)-(5); the instruments, their entries and the reproduction run (6)-(7);
        # ### v8 and the propagation read (8); the address scan (9); the axiom diagnosis (10); the LLM-contribution line (12); the ancestry each
        # ### arm reads
        reg_blobs=dict((p, (_s(blob(ROOT, '%s:%s' % (c, p))) or None, _s(blob(ROOT, 'HEAD:' + p)) or None)) for p, c in K.REG_COMMITS),
        reg_b721=(_s(blob(ROOT, '%s:%s' % (K.REG_C3, K.REGISTRATIONS))), _s(blob(ROOT, 'HEAD:' + K.REGISTRATIONS))),
        anc=dict((k, subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', a, b]).returncode == 0)
                 for k, a, b in (('reg_c3', K.REG_C3, K.C3_RELAY), ('reg_walk', K.REG_WALK, K.C3_RELAY), ('ctl_c3', K.C2_CTL, K.C3_RELAY),
                                 ('stmt_price', K.C4_STMT, K.C4_RELAY), ('rule_entries', K.C5_RULE, K.C5_RELAY), ('v8_prop', K.STANDING_COMMIT, K.C6_RELAY))),
        coeffs=rd('b722_coeffs.txt'), coeffs_ctl=jl('b722_coeffs_controls.json'), walk=rd('b722_walk.txt'),
        c2_stmt=rd('b722_c2_statement.txt'), c2_price=rd('b722_c2_price.txt'),
        instruments=rd('b722_instruments.txt'), entries=jl('b722_instrument_entries.json'), reproduce=rd('b722_reproduce.txt'),
        reproducej=jl('b722_reproduce.json'), instr_now=read(os.path.join(PP, K.INSTRUMENTS)),
        instr_pre=_s(blob(PP, '%s:%s' % (PRE['pp'], K.INSTRUMENTS))), instr_c5=_s(blob(PP, '%s:%s' % (K.C5_PP, K.INSTRUMENTS))),
        v8=read(os.path.join(ROOT, *K.DATA_STANDING_V8.split('/'))), v7=read(os.path.join(ROOT, *K.DATA_STANDING_V7.split('/'))),
        propagation=rd('b722_propagation.txt'), prop_landing=jl('b722_propagation_landing.json'), propj=json.loads(rd('b722_propagation.json') or '[]'),
        address=rd('b722_address_scan.txt'), addr_live=_addr_live(), axiom_diag=rd('b722_axiom_diag.txt'), axiom_diagj=json.loads(rd('b722_axiom_diag.json') or '[]'),
        llm=rd('b722_llm_line_drafts.txt'), llmj=jl('b722_llm_line_drafts.json'),
        # ### the standing runner arms read b721's rebuild as banked (no dispatch this act, N1): its bank, its rows, each wave 1 kernel's
        # ### rebuild-b721 branch, main and tags
        rebuild=rd('b721_rebuild.txt'), rebuild_rows=json.loads(rd('b721_rebuild_rows.json') or '[]'), rebuild_state=_rebuild_state(),
        retired=list(STA.retired()), arms_src=read(os.path.join(T, 'standing', 'arms.py')),
        arms_src_now=cr0(raw(os.path.join(T, 'standing', 'arms.py'))), arms_src_pre=cr0(blob(ROOT, '%s:tools/standing/arms.py' % PRE['relay'])),
        count_route=rd('b719_count_route_price.txt'), count_route_now=cr0(raw(os.path.join(D, 'b719_count_route_price.txt'))),
        count_route_pre=cr0(blob(ROOT, '%s:data/b719_count_route_price.txt' % PRE['relay'])),
        errata_pp_now=cr0(raw(os.path.join(PP, 'ERRATA.md'))),
        standing_v7_now=cr0(raw(os.path.join(ROOT, *STANDING_BANK.split('/')))), standing_v7_pre=cr0(blob(ROOT, '%s:%s' % (PRE['relay'], STANDING_BANK))),
        arm_tags_raw=cr0(raw(os.path.join(D, 'arm_tags.json'))), arm_tags_pre=cr0(blob(ROOT, '%s:data/arm_tags.json' % PRE['relay'])),
        errata_pp_pre=cr0(blob(PP, '%s:ERRATA.md' % PRE['pp'])),
        version=read(os.path.join(T, 'standing', 'VERSION')),
        touch=rd('b722_touch.txt'),
        author_words_pre=rd('b722_author_words_preseal.txt'), author_words=rd('b722_author_words.txt'),
        # ### N1: no dispatch at b721 or this act -- b712's runs read as banked (b721's form): its dispatch bank, its runner rows, its run banks
        port1j=jl('b712_port_port1.json'), port2j=jl('b712_port_port2.json'), dispj=jl('b712_dispatches.json'),
        runner_rows=jl('b712_runner_rows.json'), disp_now=os.path.exists(os.path.join(D, 'b722_dispatches.json')),
        runs={'port1': rd('b712_port_port1.txt'), 'port2': rd('b712_port_port2.txt'), 'join': rd('b712_runner_SIDE-faces-join_join.txt')},
        lv_wf_tip=read_blob(LV, '%s:%s' % (K.PORT_NEW_TIP, WF)) or '',
        lv_tip_on_main=subprocess.run(['git', '-C', LV, 'merge-base', '--is-ancestor', K.PORT_NEW_TIP, 'main']).returncode == 0,
        lv_main=gs(LV, 'rev-parse', 'main'), lv_v0100=_tag_peel(LV, 'v0.10.0'), lv_port=gs(LV, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.PORT_BRANCH),
        lv_tags=[t for t in gs(LV, 'tag', '--list').split(NL) if t.strip()], lv_tip_tags=[t for t in gs(LV, 'tag', '--points-at', K.PORT_NEW_TIP).split(NL) if t.strip()],
        lv_remote={},
        join_files=[x for x in gs(KI, 'diff', '--name-only', KR.JOIN_TIP, KR.JOIN_NEW_TIP).split(NL) if x.strip()] if os.path.isdir(KI) else [],
        pp_remote_recut=None,
        rules=rd('b722_rules.txt'),
        report=rd('b722_report.txt'), reportj=jl('b722_report.json'), report_tool=os.path.exists(os.path.join(T, 'b722_report.py')),
        ef_main=gs(EF, 'rev-parse', 'main'), ef_tags=dict((t, _tag_peel(EF, t)) for t in ('v0.37', 'v0.1', 'v0.2')),
        ef_log=[l for l in gs(EF, 'log', '--first-parent', '--format=%H', K.EF_V037 + '..main').split(NL) if l.strip()],
        ef_tags_all=[t for t in gs(EF, 'tag', '--list').split(NL) if t.strip()], ef_remote={},
        join_main=gs(KI, 'rev-parse', 'main') if os.path.isdir(KI) else '', join_tags=[t for t in gs(KI, 'tag', '--list').split(NL) if t.strip()] if os.path.isdir(KI) else [],
        rf_diff=rd('b722_readfirst_diff.txt'), rf_hand_now=blob(ROOT, 'HEAD:data/b722_readfirst.txt'),
        rf_hand_z=blob(ROOT, '%s:data/b722_readfirst.txt' % K.STEPZERO_BANKS) if K.STEPZERO_BANKS else None,
        asec=jl('b722_arm_seconds.json'), asect=rd('b722_arm_seconds.txt'),
        shared=dict((p, (cr0(blob(ROOT, '%s:%s' % (PRE['relay'], p))), cr0(raw(os.path.join(ROOT, *p.split('/')))), cr0(blob(ROOT, 'HEAD:' + p))))
                    for p in K.SHARED_APPENDED),
        t=dict(c1=_ct(ROOT, K.C1_RELAY), c1pp=_ct(PP, K.C1_PP), c2ctl=_ct(ROOT, K.C2_CTL), c3=_ct(ROOT, K.C3_RELAY), c4stmt=_ct(ROOT, K.C4_STMT),
               c4=_ct(ROOT, K.C4_RELAY), c5rule=_ct(ROOT, K.C5_RULE), c5=_ct(ROOT, K.C5_RELAY), c5pp=_ct(PP, K.C5_PP), v8=_ct(ROOT, K.STANDING_COMMIT),
               c6=_ct(ROOT, K.C6_RELAY), c6pp=_ct(PP, K.C6_PP), c7=_ct(ROOT, K.C7_RELAY), reg=_ct(ROOT, K.REG_COMMIT), stepzero=_ct(ROOT, K.STEPZERO_BANKS),
               actcur=_ct(ROOT, K.ACT_CURRENT_COMMIT)),
        files=dict(stepzero=files_of(ROOT, K.STEPZERO_BANKS) if K.STEPZERO_BANKS else [], c1=files_of(ROOT, K.C1_RELAY), c1pp=files_of(PP, K.C1_PP),
                   c2ctl=files_of(ROOT, K.C2_CTL), c3=files_of(ROOT, K.C3_RELAY), c4stmt=files_of(ROOT, K.C4_STMT), c4=files_of(ROOT, K.C4_RELAY),
                   c5rule=files_of(ROOT, K.C5_RULE), c5=files_of(ROOT, K.C5_RELAY), c5pp=files_of(PP, K.C5_PP), v8=files_of(ROOT, K.STANDING_COMMIT),
                   c6=files_of(ROOT, K.C6_RELAY), c6pp=files_of(PP, K.C6_PP), c7=files_of(ROOT, K.C7_RELAY),
                   reg=files_of(ROOT, K.REG_COMMIT), actcur=files_of(ROOT, K.ACT_CURRENT_COMMIT)),
        tracked=lambda p: bool(gs(ROOT, 'ls-files', '--', p).strip()),
        standing=STANDING, wf=wf_state(),
        export_present=os.path.exists(os.path.join(ROOT, *EXPORT.split('/'))), export_log=gs(ROOT, 'log', '--all', '--format=%h', '--', EXPORT),
        export_index=gs(ROOT, 'ls-files', '--', EXPORT), export_status=gs(ROOT, 'status', '--porcelain', '--', EXPORT),
        local_present=os.path.exists(local), local_log=gs(ROOT, 'log', '--all', '--format=%h', '--', K.LOCAL_BANK),
        local_index=gs(ROOT, 'ls-files', '--', K.LOCAL_BANK), local_status=gs(ROOT, 'status', '--porcelain', '--', K.LOCAL_BANK),
        arj=jl('b722_act_root.json'), arj0=jl('b721_act_root.json'), art=rd('b722_act_root.txt'), rootsf=rd('act_roots.txt'),
        rootbanks=jl('b722_root_banks.json'), route_list=REC.root_banks(),
        pushout=(files_of(ROOT, K.STEPZERO) if K.STEPZERO else [], bool(K.STEPZERO) and subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.STEPZERO, 'HEAD']).returncode == 0),
        inst={f: (cr0(blob(ROOT, PRE['relay'] + ':tools/' + f)), cr0(raw(os.path.join(T, *f.split('/')))), cr0(blob(ROOT, 'HEAD:tools/' + f)))
              for f in INST},
        find=read(os.path.join(PP, 'FINDINGS.md')), ot=read(os.path.join(PP, 'OPEN_TRAILS.md')),
        currents={p: tri(PP, p, PRE['pp']) for p in CURRENTS},
        pp_renames=gs(PP, 'diff', '--name-status', '-M', PRE['pp'], 'HEAD'),
        ot_pre=cr0(blob(PP, PRE['pp'] + ':OPEN_TRAILS.md')), ot_now=cr0(raw(os.path.join(PP, 'OPEN_TRAILS.md'))),
        fi_pre=cr0(blob(PP, PRE['pp'] + ':FINDINGS.md')), fi_now=cr0(raw(os.path.join(PP, 'FINDINGS.md'))),
        page_changed=[x for x in (gs(PP, 'diff', '--name-only', PRE['pp'], 'HEAD', '--', K.FACES_PAGE) + NL + gs(PP, 'diff', '--name-only', '--', K.FACES_PAGE)).split(NL) if x.strip()],
        kern_face=(jl('b722_kernels_face.json').get('kernels') or {}), kerns_read=list(dict.fromkeys(REC._kerns())) + ['SIDE-faces-join'],
        tools=tools, tooltext={f: strip_prose(_act_code(f)) for f in tools},
        artefacts=gs(ROOT, 'ls-files', 'data/anthropic-zeta23'),
        mustfail=not os.path.exists(os.path.join(D, 'b722_mustnotexist.txt')),
        steps=jl('b722_steps.json').get('rows') or [],
        fj=jl('b722_findings.json'), tj=jl('b722_trail.json'), sc=jl('b722_scores.json'), desk=rd('b722_desk_notes.txt'), tfj=jl('b722_table_final.json'),
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
        S['pp_remote_recut'] = git(PP, 'ls-remote', 'origin', 'refs/heads/' + K.RECUT_BRANCH)[1].strip()   # ### (R332)(2)(iii): the branch at its tip
    if 'lvremote' in need:
        refs = {}
        for l in git(LV, 'ls-remote', 'origin')[1].split(NL):
            if '\t' in l:
                sha, ref = l.split('\t', 1)
                refs[ref.strip()] = sha.strip()
        S['lv_remote'] = refs
    S['root_at_commit'] = _root_named_at_commit(S['arj'])
    S['secs_ct'] = dict((p, _ct(ROOT, gs(ROOT, 'log', '-1', '--format=%H', '--', 'data/b722_arm_seconds_%s.json' % p))) for p in K.PARTS)
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
        base = jl('b721_standing_figures.json')
        S['fig'] = SF6.all_figures(baseline=((base.get('pins') or {}).get('rows') or {}), remote=KC0.remote_refs)
        S['fig_prev'] = base
        S['fig_prev_name'] = 'b721_standing_figures.json (b721`s figures; the readers over b706`s roster, data/b706_roster_read.json)'
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
            if f.startswith(('b722_', 'audit_b722_')) and os.path.isfile(os.path.join(D, f)) and not f.endswith(('.gz', '.png', '.jsonl')):
                pub.append(read(os.path.join(D, f)))
        pub += [read(f) for f in tools]
        pub += [S['lv_wf_tip'] or '']
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


# ### the eight test files not clean at step zero: the three b706 carried and the five readers the renames of (R316)(3) broke (data/b722_defects.txt, the events);
# ### test_chain_page.py TIMED OUT at 580 s twice at this act's step zero (data/b722_stepzero.txt :56), no case read, so its failing list is empty
STEPZERO_FAILING = {'test_chain_page.py': [], 'test_chain_page_b629.py': ['(8)'], 'test_chain_page_b638.py': ['(4)', '(5)', '(6)', '(7)'],
                    'test_composer_b646.py': ['(10)', '(11)', '(17)', '(19)'], 'test_composer_b647.py': ['(4)', '(5)', '(7)', '(9)', '(17)', '(18)'],
                    'test_composer_b649.py': [], 'test_g_chain_page.py': ['(1)'], 'test_name_b649.py': ['(5)']}


def tests_ok(S):
    """Component 8, the Edit tool: this act's step zero ran no test (data/b722_stepzero.txt :63-:64, N1: no lean on the host) -- its tests
    section saying so, no tests bank of this act's written, nothing withheld; b721's run of the tracked test files (tests_ok_b721) not carried."""
    return 'not run at this step zero' in S['stepz'] and 'N1: no lean on the host' in S['stepz'] and not S['tests'] and not S['testst'] \
        and not S['withheld']


def tests_ok_b721(S):
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
    """(R331)(3)(i): the face's row `### POST-SEAL PROMPTS NAMED: <n>[ (the root`s prompt)]` read as n; NONE or no row reads 0."""
    m = re.search(r'### POST-SEAL PROMPTS NAMED: (NONE|\d+)', face or '')
    return 0 if not m or m.group(1) == 'NONE' else int(m.group(1))


def answers_bank_ok(a, answersj, lock_epoch, face, act, floors):
    """the answers bank's form for <act>, pure in its arguments: its prompt count the bank's own, each prompt with two options or more and its
    result, the calls at or above the floors, and every call after the lock named on the face's post-seal row ((R331)(3)(i))."""
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
    return answers_bank_ok(S['answers'], S['answersj'], S['lock_epoch'], S['face'], ACTN, FLOORS)


def no_local_lean(S):
    return bool(S['cmds']) and not [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and S['REC'].local_lean(r['cmd'])]


# ================================================================== (R332) STEP ZERO: THE CITATION CHECK, THE BRANCHES, THE READ-FIRST BANK
# ### the ferry's read-first list (data/b722_ferry.txt :47) by its banked rows (data/b722_readfirst.txt :16-:33), the act's own beyond it :36-:39
# ### Component 8, the Edit tool: the readfirst bank's rows as b722's step zero wrote them (b721's needles, carried by the substitution, named
# ### banks of b719's and b718's under b721's name)
# ### b722's read-first bank's items by path (Component 8, the Edit tool: the carried needles were b721's items)
READFIRST_NEEDLES = ('relay data/b721_closing.txt |', 'relay data/b721_events.txt |', 'relay data/b721_defects.txt |',
                     'relay data/b721_registrations.txt |', 'relay data/b721_derivation.txt |', 'relay data/b721_offset_read.txt |',
                     'relay data/b721_offset_tier.txt |', 'relay data/b721_frozen_line.txt |', 'relay data/b721_rebuild.txt |',
                     'relay data/b718_count_read.txt |', 'PLACE-papers phase1.5/method/INSTRUMENTS.md |', 'relay data/b722_ferry.txt | whole |',
                     'relay data/b722_citation_check.txt | whole |', 'relay tools/b711_coeffs.py |', 'relay tools/e0_rule.py |',
                     'PLACE-papers day1/A_Place_to_Stand.md |', 'relay data/standing_clauses_v7.txt |')
NAMED_PUSH = sorted(b for _r, bs in K.DELETE for b in bs)   # ### (R332)(8): five refs, relay's three (closing, preroot, record) and PLACE-papers' two
SCRATCH = ()                  # ### no scratch branch deleted this act: port-b707 kept ((R332)(7))
from standing import allow as STW   # noqa: E402  ### (R331)(3)(i): the allowances read from the ruling and the author's words, not floors in the code


def readfirst_ok(S):
    z = unwrap(S['readfirst'])
    return bool(z) and all(x in z for x in READFIRST_NEEDLES) and "THE FERRY'S READ-FIRST LIST" in z and "THE ACT'S OWN BEYOND THE LIST" in z


def branches_ok(S):
    """(R332)(7): the three refs gone from relay's and PLACE-papers' lists (push-b721-closing and push-b721-record on relay, push-b721-record on
    PLACE-papers), each named in the step-zero bank's branch row with its tip; port-b707 kept at its tip cb0aea56."""
    z = unwrap(S['stepz'])
    left = dict((r, sorted(x.strip() for x in v.split(NL) if x.strip())) for r, v in S['branch_lists'].items())
    return all(v == [] for v in left.values()) and len(left) == 2 and len(NAMED_PUSH) == 5 and all(b in z for b in NAMED_PUSH) \
        and 'port-b707' in z and 'KEPT' in z and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP


def branches_banked_ok(S):
    """the deletes recorded in the step-zero bank (its branch row names each branch, its repository and its tip), the bank in the step-zero
    banks' commit; the citation check before the first delete; port-b707 kept at its tip."""
    z = unwrap(S['stepz'])
    fd = S['first_delete_ts']
    tips = re.findall(r'push-b721-\w+ \(([0-9a-f]{7,8})', z)
    return len(tips) >= len(NAMED_PUSH) == 5 and 'data/b722_stepzero.txt' in S['files']['stepzero'] and bool(fd) \
        and bool(S['cit_at']) and S['cit_at'] < fd and S['kept_tips'].get(K.PORT_BRANCH) == K.PORT_TIP


def deletes_one_ok(S):
    """every branch delete of the act one branch, no glob, no variable, nothing chained after; (R331)(3)(i): each delete's branch read against the
    ruling's own delete clauses and the author's words through tools/standing/allow.py (deletes_read), not a list in this code -- port-b707,
    the ruling's NOT deleted, refused there; every branch the step-zero list names deleted."""
    sh_ = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell')]
    shapes = [(S['REC'].delete_shape(r['cmd']), S['REC'].chained_after(r['cmd'])) for r in sh_]
    shapes = [(s, c) for s, c in shapes if s[0]]
    got = sorted(x for (d, _g, _v), _c in shapes for x in d)
    rd_ = STW.deletes_read([('-', b) for b in got], S['ferry'], STW.words_of(ACTN))
    # ### Component 8: (R332)(9) writes "port-b707 kept;", which allow.py's NOT-deleted reader (b721's wording) does not take; read as written
    return bool(shapes) and all(len(d) == 1 and not gl and not vs and not c for (d, gl, vs), c in shapes) \
        and rd_['ok'] and all(b in got for b in NAMED_PUSH) and K.PORT_BRANCH not in got \
        and (K.PORT_BRANCH in rd_['kept'] or ('%s kept;' % K.PORT_BRANCH) in S['ferry']) \
        and ('BRANCH DELETES OF ONE BRANCH, NO GLOB, NO VARIABLE AND NOTHING CHAINED AFTER %d OF %d' % (len(shapes), len(shapes))) in S['cmdt']


def listings_before_ok(S):
    """the listing `git branch --merged` printed in the capture before the first delete; every branch deleted named in the step-zero bank's row
    as merged (no branches bank this act)."""
    z = unwrap(S['stepz'])
    return bool(S['first_listing_ts']) and bool(S['first_delete_ts']) and S['first_listing_ts'] < S['first_delete_ts'] \
        and 'each listed by --merged first' in z and all(b in z for b in NAMED_PUSH)


def dry_step_ok(S):
    g = S['gate']
    return '--- THE DRY-RUN STEP ((R267)(2))' in g and 'ENTRY : table cells NONE ; screens QUIET' in g and 'TRAIL : table cells NONE ; screens QUIET' in g \
        and 'THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK True' in g and 'THE TRAIL`S RESOLVED LINE EQUAL TO THE DEFECTS BANK True' in g \
        and '### ### **THE DRY-RUN STEP : CLEAN**' in g and '### ### **GATE VERDICT : CLEAR**' in g


# ### (R332)(2)(iii), standing clauses v2 row (54), ARMS READ STRUCTURE: the gate's '### NO VERDICT LINE' rows read by the bank each row names and
# ### not by a list of names -- b709's and b721's lists named their own acts' banks, and the carry's substitution turned b721's entry into a bank
# ### that does not exist (data/b721_prints_v0.17.txt for b708's data/b708_prints_v0.17.txt). A row passes where its bank exists, is not empty and
# ### carries no verdict line by the closing tool's own reader (tools/b722_closing.py VLINE); a row naming no bank, an absent or empty bank, or a
# ### verdict-bearing bank printed without its verdict fails. The gate writes no JSON bank, so its text is read (data/b722_repair_controls.txt (iii)).
# ### b722's repair before the seal (defect (q)): the reader is the one that printed the row -- the closing's section rows print by its `vtail`
# ### (tools/b722_closing.py :99-:101, a verdict at the line's first column), not by `vline` (:91, any indent), which the comment above named;
# ### an indented bank foot (data/b722_pins_census.txt's controls line) read as a verdict the closing never prints.
NO_VERDICT_ROW = re.compile(r'\(relay (data/[^\s)]+)\): ### NO VERDICT LINE')
VLINE_FORM = re.compile(r'(?ms)^### ### \*\*(.*?)\*\*\s*$')


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


# ### b722's closing sections (tools/b722_closing.py act_sections), each title read in the gate's record and in the closing's source
CLOSING_SECTIONS = ('CORRIGENDUM ((R332)(1)-(2))', 'DISCRIMINANTS -31 AND -55 ((R332)(3))', 'FOURTEEN FIELDS ((R332)(4))', 'C2 STATEMENT ((R332)(5))',
                    'RESEARCH INSTRUMENTS ((R332)(6)-(7))', 'PROPAGATION READ (standing clauses v8 row (82), (R332)(8))', 'NAME AND ADDRESS ((R332)(9))',
                    'AXIOM STEP ((R332)(10))', 'LLM-CONTRIBUTION LINE ((R332)(12))', 'TOUCH READ (standing clauses v8)')


def closing_dry_ok(S):
    g = S['gate']
    return '--- THE CLOSING DRY-RUN STEP (b675 rules row 1)' in g and '### ### **THE CLOSING DRY-RUN STEP : CLEAN**' in g \
        and ('%s closed:' % ACT_NOW) in g and all(('THE %s' % s) in g for s in CLOSING_SECTIONS) and 'THE STANDING REPORT' in g \
        and '): ### NOT FOUND' not in g \
        and '### THE STANDING ARMS' in g and '### THE KERNELS' in g and 'CLAIM ' in g and no_verdict_line_ok(g)


def citation_ok(S):
    """the citation check's bank: every cite checked, OK and misses summing (90 = 88 + 2; the two misses -- b711's route with C1-C3 (C3
    False), b721's closing :389-:430 beyond its end at :413 -- in the JSON bank's misses, each raised or entered before the component citing
    it); the bank written before the step-zero banks' commit and that commit before Component 1's (Component 8, the Edit tool: the carried
    78 = 75 + 3 were b721's own)."""
    c = S['citation']
    m = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', c)
    return bool(m) and int(m.group(1)) == int(m.group(2)) + int(m.group(3)) > 0 and 'A GATE STEP AT STEP ZERO' in c \
        and int(m.group(3)) == len(S['cit_misses']) == 2 and int(m.group(1)) == 90 \
        and bool(S['cit_at']) and bool(S['t'].get('stepzero')) \
        and S['cit_at'] < S['t']['stepzero'] and bool(S['t'].get('c1')) and S['t']['stepzero'] <= S['t']['c1']


def rowgen_ok(S):
    return '### ### **CONSTELLATION EXIT 0 ; ROWGEN DIFF EXIT 0 ; TABLES 19 ; RE-POINTED 8.**' in S['rowgen']


def weight_ok(S):
    # ### this act's needles: b721's head line as its closing prints it (data/b721_closing.txt :1) and the record's commits the repaired builder read
    # ### (Component 8, the Edit tool: the carried needles were b720's figures under b721's name)
    return landed(S, 0, ['b721 AT ITS WEIGHT', 'suite 112 of 116; root c6e2079dbe1c904f…', 'the closing’s 30c0b3c8', '27 defects'])


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


# ### no word of the author's before the seal this act (no data/b722_author_words_preseal.txt): every check stamp is the root prompt's
PRESEAL_NEEDLES = ()


def answers_before_ok(S):
    """(R331)(3)(i): the prompts the answers bank carries read against the allowance tools/standing/allow.py reads from the ruling ("the root's
    prompt put once") and the author's-words heads (prompts_read), not a floor in this code -- every prompt allowed, none unbanked; each check
    stamp after the lock and at or before the root (data/b722_act_root.json, within the chain's order slack), one at least."""
    st = re.findall(r'### \(R278\)\(4\) THE MID-ACT CHECK \((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\): the (?:navigator`s )?answer carrying \'([^\']+)\'', S['citation'])
    lk = S['lock_epoch']
    root_at = S['arj'].get('at_epoch')
    pre = [(iso_epoch(t), n) for t, n in st if n in PRESEAL_NEEDLES]
    post = [iso_epoch(t) for t, n in st if n not in PRESEAL_NEEDLES]
    pr = STW.prompts_read(S['answers'], S['ferry'], STW.words_of(ACTN))
    return pr['ok'] and len(pr['rows']) >= 1 and lk is not None and root_at is not None and len(post) >= 1 and None not in post \
        and not pre and all(lk <= x <= root_at + S['order_slack'] for x in post)


CHECK_STAMP = re.compile(r'(### \(R278\)\(4\) THE MID-ACT CHECK \()\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ(\))')


def answers_plant(S):
    """(R332)(2)(iv), standing clauses v2 row (55): G-ANSWERS-BEFORE-WRITES given a control that fails -- every check stamp in the citation bank
    moved after the write it governs, the landing and the lock and the root among them (to 2099-01-01T00:00:00Z), so the mutated copy carries
    an answer checked after it was acted on. b721's plant appended a prompt to the answers bank where the predicate reads one prompt or more,
    so the mutated copy passed and the control could not fire (b721's events; data/b722_repair_controls.txt (iv))."""
    return put(S, 'citation', CHECK_STAMP.sub(r'\g<1>2099-01-01T00:00:00Z\2', S['citation']))


# ================================================================== (R332)(1)-(2): THE RECORD LINES, THE CORRIGENDUM, THE WRITE LIST
def scorer_banks_ok(S):
    n = ''.join(strip_prose(_fn_src(S['rec_src'], f)) for f in ('_n1', '_n2', '_n3', '_n4'))
    sc = strip_prose(_fn_src(S['rec_src'], 'scores'))
    ft = strip_prose(_fn_src(S['rec_src'], '_finding_text'))
    # ### Component 7: b722's scorers read the command bank and the pin's rows (N1), the derivation (N2-N3), the seal and step banks (N4); N3
    # ### reads the act's findings BANK (data/b722_findings.json, `_findings.json`), not the ledger, so the bank's name is read apart
    return bool(n) and '_commands.json' in n and '_pin_rows.json' in n and '_derivation.txt' in n \
        and '_seal_hashes.json' in n and '_steps.json' in n and 'jl(HASHES)' in n \
        and not re.search(r'\b(FIND|OT)\b|FINDINGS|OPEN_TRAILS|(?<!_)findings|entry_line', n) \
        and "os.path.isfile(os.path.join(D, '%s_scores.json' % ACT))" in sc and 'scores_line(S)' in ft and "jl('%s_scores.json' % ACT)" in ft


def entry_scores_ok(S):
    want = conv(S['REC'].scores_line(S['sc'])) if S['sc'] else None
    blk = _entry_block(S)
    got = [l for l in blk.split(NL) if l.startswith('**The scores.**')]
    return bool(want) and bool(S['sc']) and got == [want]


# ### the title by its objects (the ferry's Component 6), compared after case-folding the article alone (b706's repaired predicate, carried):
# ### b722's objects (the ferry's Component 7 form, adjusted to what the act did): the least negative index and b(n) at each discriminant, the
# ### law on its clauses; H-24 (refuted on the pair, its two readings) and H-47; the derivation to the step named; the offset post hoc with its
# ### hypothesis; the surgery carried; the arms retired
# ### b722's title by its objects (the record tool's _title, printed by a scratch script writing nothing), set by the Edit tool after the lock,
# ### before the seal, in place of b721's carried needles (events (4))
# ### Component 8, the Edit tool: b722's title (the ferry's Component 8 form adjusted to what the act did), from the banks as they stand
TITLE_NEEDLES = ('## the C2 table at the discriminants its rule would choose: none -- every class-number-2 field’s least negative index at -2 '
                 'or -1/2, the halt proved', '; the table over h = 3, 4, 5 written and checked, two predictions registered (n0 = 80 at -31, 224 '
                 'at -55)', '; the offset’s post hoc rows, H-OFFSET refuted on its own first rows, and 0 new pairs registered', '; the surgery carried',
                 '; the frozen line’s statements quoted, its drafts for the release sitting', '; 6 of 6 wave 1 kernels build at their own pins, one '
                 'with a sorry', '; the federation pin closed')


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


# ### (R332)(2)(i), standing clauses v2 row (52): the trail's Defects and Resolved lines and the three trail-equality arms read THE LETTERS ENTERED
# ### BEFORE THE SEAL (S['letters_seal']: the list the seal records, tools/b722_record.py letters_at_seal) and not the defects bank as it stands
# ### -- a finding after the seal is an event in the closing's events section, not a letter (b721's three trail arms failed on the late letter (i)).
# ### Where the act is not sealed the list is None and the arms fail.
def trail_defects_ok(S):
    m = re.search(r'^\*\*Defects\*\* \(relay data/b722_defects\.txt\): (.*)\.$', trail_tail(S), re.M)
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
    """(R332)(2): the generated entry for b721's fifteen events and twenty-seven defects landed (its line in the bank, the title at that line
    through conv): the events by row (1)-(15), the defects by the one lettering ((a)-(z), (a`)), no memory item; every item tagged CLAIM or
    CLOSE and NEW or REPEAT, the tags summing (CLAIM 5, CLOSE 37 over 42, REPEAT 24); the CLAIM items defects (d), (g), (i), (k) and (u); the
    three repairs at tools/standing/ v1.2.2 with their twelve cases; the corrigenda bank appended at row (42) and nothing before it changed; in
    Component 1's commit (Component 8, the Edit tool: the carried figures were b721's corrigendum's, of b720's record)."""
    j = S['corrj']
    e = j.get('entry_line')
    now, pre, head = S['corrigenda_tri']
    evs, dfs = j.get('events') or [], j.get('defects') or []
    try:
        lets = AL.read([d.get('letter') for d in dfs])   # ### the one lettering: b721's defects' letters as the corrigendum names them
    except ValueError:
        return False
    items = evs + dfs
    claims = sorted(['e%d' % x['row'] for x in evs if x.get('tag') == 'CLAIM'] + [d['letter'] for d in dfs if d.get('tag') == 'CLAIM'])
    return bool(e) and fline(S, e) == conv(j.get('title') or '\x00') and [x.get('row') for x in evs] == list(range(1, 16)) \
        and len(lets) == len(dfs) == 27 and len(items) == j.get('items') == 42 and j.get('row') == 42 \
        and all(x.get('tag') in ('CLAIM', 'CLOSE') for x in items) and j.get('claim') + j.get('close') == 42 \
        and sum(1 for x in items if x.get('tag') == 'CLAIM') == j.get('claim') == 5 and claims == ['d', 'g', 'i', 'k', 'u'] \
        and sum(1 for x in items if (x.get('column') or '').startswith('REPEAT')) == j.get('repeat') == 24 \
        and all(x.get('column') == 'NEW' or (x.get('column') or '').startswith('REPEAT') for x in items) \
        and (j.get('repairs') or {}).get('version') == 'v1.2.2' and (j.get('repairs') or {}).get('cases') == 12 \
        and '  (42) ' in S['corrigenda'] and '  (43) ' not in S['corrigenda'] \
        and pre is not None and (now or b'').startswith(pre) and (head or b'').startswith(pre) and 'FINDINGS :%d' % e in S['corrt'] \
        and 'data/b722_corrigendum.txt' in S['files']['c1']


def writelist_mirror_state_ok(S):
    """(R332)(2): the face's (W) row for the mirror builder names tools/mirror_prevbuild.json beside the zip and its stage; N5 reads it as the
    builder's own (the record tool's N5_RELAY_TOOLS)."""
    w = S['face'][S['face'].find('(W) THE WRITE LIST'):S['face'].find('(Z) THE NOTHINGS')]
    row = [l for l in w.split(NL) if 'mirror_build.ps1' in l]
    return bool(row) and 'tools/mirror_prevbuild.json' in NL.join(w.split(NL)[w.split(NL).index(row[0]):w.split(NL).index(row[0]) + 2]) \
        and 'mirror_prevbuild.json' in tuple(S['REC'].R.N5_RELAY_TOOLS)


def rules_row_ok(S):
    """the rules that bind this act, read where they stand: b710's row (1), the standing clauses carried by version (the ferry names v3, the bank at
    VERSION 3); b709's row (1), the carry read by diff (this act's carry banks); b708's row (1), the report tool outside the sealed list, the
    worklist's SEALED naming no report tool. This act's rules banks (data/b722_rules.txt and data/b723_rules.txt, by form in (R332)(11)) are
    written where an author's word orders a row: b722's carries row (1), (R332)(1)'s rule, in Component 1's commit and no other row;
    b723's does not exist (Component 8, the Edit tool: the carry's substitution named b722's twice and b721's rule (1))."""
    r1 = rd('b722_rules.txt')
    return '(1) THE STANDING CLAUSES CARRIED BY VERSION' in rd('b710_rules.txt') and bool(re.search(r'^VERSION: 7$', S['standing_bank'], re.M)) \
        and '(1) THE CARRY IS READ BY DIFF' in rd('b709_rules.txt') and all(S['carry_banks'].get(n) for n in ('record', 'checks', 'closing')) \
        and '(1) THE REPORT TOOL IS KEPT OUT OF THE SEALED LIST UNTIL THE ROOT' in rd('b708_rules.txt') \
        and '  (1) NOTHING EDITED AFTER THE LOCK GATE; A RESTORE IS AN EDIT.' in r1 and not re.search(r'(?m)^  \((?!1\))\d+\) ', r1) \
        and 'data/b722_rules.txt' in S['files']['c1'] and not os.path.exists(os.path.join(D, 'b723_rules.txt')) \
        and not any('report' in t for t in K.SEALED) and 'b722_report.py' not in (S['sealj'].get('tools') or {})


def report_lines_ok(j, keys, n):
    """(R332)(2)(iii), standing clauses v2 row (54): the report read by the JSON bank its tool writes (data/<act>_report.json, its `lines`) and not
    by its text: n lines or more, every one a string, each key found in the lines case-insensitively (keys_ci over the lines alone). b709's
    report (data/b709_report.json) passes on b709's five keys, where the sealed needle on the text wanted RATIO in capitals and failed."""
    ls = (j or {}).get('lines')
    return isinstance(ls, list) and len(ls) >= n and all(isinstance(x, str) for x in ls) and keys_ci(NL.join(ls), keys)


# ### the standing report's lines in footing order -- KERNEL (the rebuild, each run by its id), CERTIFIED (the table over h = 3, 4, 5; the C2
# ### rule's output NONE), REGISTERED (the h = 3, 4 predictions; the fourteen blind), HELD (the offset post hoc, the frozen line, the draft) --
# ### each read by a phrase its line carries; set by the Edit tool at Component 8, in place of b721's carried keys
REPORT_KEYS = ('KERNEL -- THE REBUILD AT EACH WAVE 1 KERNEL`S OWN PIN', 'CERTIFIED -- THE TABLE OVER CYCLIC h = 3, 4, 5 AT OMEGA 1-6',
               'CERTIFIED -- THE C2 RULE`S OUTPUT NONE', 'REGISTERED -- THE h = 3 AND h = 4 PREDICTIONS',
               'REGISTERED -- THE TABLE`S PREDICTIONS AT THE FOURTEEN UNUSED', 'HELD -- THE OFFSET, POST HOC', 'HELD -- THE FROZEN LINE',
               'HELD -- the draft at v5')
FOOTINGS = ['KERNEL', 'CERTIFIED', 'REGISTERED', 'HELD']


def report_unsealed_ok(S, keys=None, n=8):
    """the report bank written by the unsealed report tool before the root, read by its JSON bank ((R332)(2)(iii)): its `at` after the lock and at
    or before the root's time; the tool outside the sealed list; its lines the ferry's (report_lines_ok), its footings in the order (R332)(3)
    names, every source seated; the scores line not in the bank (printed after the root, written nowhere)."""
    j = S['reportj']
    at = iso_epoch(j.get('at') or '') if j else None
    root_at = S['arj'].get('at_epoch')
    return bool(j) and S['report_tool'] and 'b722_report.py' not in K.SEALED and at is not None and S['lock_epoch'] is not None and at > S['lock_epoch'] \
        and root_at is not None and at <= root_at + S['order_slack'] and report_lines_ok(j, keys or REPORT_KEYS, n) \
        and list(j.get('footing') or {}) == FOOTINGS and j.get('unseated') == [] and 'SCORES' not in NL.join(j.get('lines') or []).upper()


def keys_ci(text, keys):
    """(R332)(3), the carry-time repair of G-REPORT-UNSEALED's needle: each key read case-insensitively (b721's sealed arm wanted RATIO in capitals
    and its report printed "the twelve ratios", so the arm failed after the seal on its own needle)."""
    low = (text or '').lower()
    return all(k.lower() in low for k in keys)


def joined(text):
    """(R332)(3), the carry-time repair of G-AXIS-REGISTERED's needle: the bank read after joining its wrapped lines -- every run of white space,
    the line breaks and the continuation indents among them, read as one space (b721's registrations bank wrapped the ranking's quotation across
    its lines 12-13, so the arm's one-string needle found nothing there after the seal)."""
    return ' '.join((text or '').split())


GUARD_WRITE = "sp = os.path.join(D, 'b722_arm_seconds_%s.json' % PART)"   # ### the write's own line, stripped; matched whole, not by a needle


def guard_ok(S):
    s = S['suite'].split(NL)
    i = next((k for k, l in enumerate(s) if l.strip() == GUARD_WRITE), None)
    j = S['guardj']
    return i is not None and s[i - 1].strip() == 'if PRERUN:' and 'POST-ROOT PATH WRITES NONE' in S['guard'] \
        and (j.get('writes') or {}).get('pre-push') == [] and (j.get('writes') or {}).get('post-push') == [] \
        and (j.get('writes') or {}).get('prerun') == ['data/b722_arm_seconds_<part>.json']


def postroot_writes_none(S):
    j = S['guardj']
    w = j.get('writes') or {}
    return 'POST-ROOT PATH WRITES NONE' in S['guard'] and w.get('pre-push') == [] and w.get('post-push') == [] and bool(S['root_ct']) \
        and sorted(S['secs_ct']) == sorted(K.PARTS) and all(v is not None and v <= S['root_ct'] for v in S['secs_ct'].values())


def trail_lines_equal_defects(S):
    tail = trail_tail(S)
    dm = re.search(r'^\*\*Defects\*\* \(relay data/b722_defects\.txt\): (.*)\.$', tail, re.M)
    rm = RESOLVED.search(tail)
    bank = [b_ for b_ in AC.defect_owners(S['letters_seal'] or [])['by'] if b_[1] in ('NAVIGATOR', 'SEAT')]
    want = _owners(S['letters_seal'] or [])   # ### (R332)(4)(iii): the one counter (a repair at b722)
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


# ================================================================== THE RUNNER (this act's three runs: the port's two on port-b707, the join's one at its re-pinned main)
IDENT_WF = ('secrets.', 'psinary', 'seale', 'york', 'hotmail', 'orcid', '0009-0008')


def wf_ok(S, rules_needle='(1) THE PROBE ROUTE\'S TARGET IS print_targets.txt WHOLE'):
    """b705's repaired reading over this act's runs: each workflow its base's blob unchanged and written before b722, no identifier, the hold, the
    lakefile and its cache step; at the port the print list ABSENT at the branch, so the print step is read as not run and no grade claimed (the
    port's dispatch rows saying so, `whole` False by it); at the join the print list FacesJoin, the join's row `whole` True printing its one
    module; this act's writes each the one file wanted."""
    for k, v in S['wf'].items():
        t = v['text'].lower()
        if not v['text'] or v['text'] != v['before'] or not v['wrote_before_act'] or any(w in t for w in IDENT_WF):
            return False
        if 'workflow_dispatch' not in t or 'hold_mb: "2560"' not in t:
            return False
        if not v['lakefile'] or (('lake exe cache get' in t) != v['mathlib']):
            return False
        if v['act_writes'] != v['want']:
            return False
    rows = S['dispj'].get('rows') or []
    port, join = [r for r in rows if r.get('label') == PORT_LABEL], [r for r in rows if r.get('label') == 'join']
    lv, ki = S['wf'].get(K.KERNEL) or {}, S['wf'].get('SIDE-faces-join') or {}
    return sorted(S['wf']) == sorted([K.KERNEL, 'SIDE-faces-join']) and lv.get('print_list_absent') is True and not lv.get('targets') \
        and ki.get('targets') == ['faces_join'] and len(port) == 2 and all(r.get('whole') is False and 'ABSENT' in (r.get('print_list') or '') for r in port) \
        and len(join) == 1 and join[0].get('whole') is True and join[0].get('print_modules') == ['FacesJoin'] \
        and rd('b705_rules.txt').count(rules_needle) == 1 and rebuild_wf_ok(S)


def rebuild_wf_ok(S):
    """(R332)(7)(iii), b722: the workflow at each rebuild branch's tip -- five kernels carrying build-module.yml on main and their branch at the
    pin (the workflow read from main); SIDE-frobenius none on main, its tip's workflow SIDE-explicit-formula's with the author's two lines (the
    push trigger to the branch, the target fixed) and nothing else, no identifier of the author, no secret, the hold kept."""
    import difflib
    st = S['rebuild_state'] or {}
    fr = st.get('SIDE-frobenius') or {}
    src = read_blob(EF, 'HEAD:.github/workflows/build-module.yml') or ''
    tip = fr.get('wf_tip') or ''
    d = [x for x in difflib.unified_diff(src.split(NL), tip.split(NL), lineterm='', n=0) if x[:1] in '+-' and x[:3] not in ('+++', '---')]
    return all(v['wf_main'] for k, v in st.items() if k != 'SIDE-frobenius') and fr.get('wf_main') is False \
        and d == ['+  push: { branches: [%s] }' % K.REBUILD_BRANCH, '-      TARGET: ${{ inputs.target }}', '+      TARGET: SIDEFrobenius'] \
        and not any(w in tip.lower() for w in IDENT_WF) and 'hold_mb: "2560"' in tip.lower()


def runner_ok(S):
    """(R332)(7)(iii), N1: the rebuild read by its run ids -- one run per wave 1 kernel, six, each the worklist's, each read once with the build
    exit read from its artifact; the bank's head figures equal to its rows (pushed 6, runs 6, read 6, builds 6, held 0, unread 0); the one
    sorry printed by its axiom line (SIDE-lv-conservation, sorryAx in T3_perClass_to_combinations) and graded "builds and is not complete";
    SIDE-frobenius's refused dispatch printed, its trigger-only halt with its control, and its push run on the author's two lines."""
    t, rows = S['rebuild'] or '', S['rebuild_rows'] or []
    reads = dict((r['kernel'], r) for r in rows if r.get('kind') == 'read')
    disp = dict((r['kernel'], r) for r in rows if r.get('kind') == 'dispatch')
    runs = dict(K.REBUILD_RUNS)
    return sorted(reads) == sorted(runs) == sorted(k for k, _t, _p in K.WAVE1) and all(str(reads[k]['run']) == str(runs[k]) == str(disp[k]['run']) for k in runs) \
        and all(r['verdict'] == 'BUILDS' and r['build_exit'] == '0' for r in reads.values()) \
        and 'PUSHED 6 ; DISPATCHED 6 (six at most) ; DISPATCH REFUSED 1 ; READ 6 ; BUILDS 6 OF 6 ; HELD (BREAKS) 0 ; NOT READ 0' in t \
        and [k for k, r in reads.items() if r['sorry_warnings']] == ['SIDE-lv-conservation'] \
        and "sorryAx in ['SIDELvConservation.T3.T3_perClass_to_combinations']" in t and 'builds and is not complete' in t \
        and 'DISPATCH REFUSED' in t and 'HALTED: no trigger-only change can build' in t and 'THE AUTHOR`S SECOND WORD' in t \
        and disp['SIDE-frobenius'].get('via') == 'push' and _verdict(t).startswith('6 OF 6 WAVE 1 KERNELS BUILD AT THEIR OWN PINS')


# ### the rebuild's routes as run: a command's head running the tool (the capture also holds refused commands naming them in their text)
REBUILD_ROUTE = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*tools/b722_rebuild\.py (push|dispatch|push_run|plan)\b', re.M)


def gate_ok(S):
    """N1, N4, over b721's rebuild as banked (Component 8, the Edit tool: no rebuild this act, (R332)(10) reads b721's runs by their ids):
    every push, dispatch and read row of b721's with the host's free memory at or above the hold; per kernel its push before its run and its
    run before its read; b721's dispatches its worklist's cap, the refused one counted apart; and this act's command capture running no
    rebuild route at all (b721's tool or a b722 one) and no dispatch."""
    rows = S['rebuild_rows'] or []
    order = True
    for k, _t, _p in K.WAVE1:
        seq = [r.get('kind') for r in rows if r.get('kernel') == k and r.get('kind') in ('push', 'push2', 'dispatch', 'read')]
        order = order and bool(seq) and seq[0] == 'push' and seq[-1] == 'read' and seq.count('dispatch') == 1 \
            and seq.index('dispatch') < seq.index('read')
    mem = [r for r in rows if r.get('kind') in ('push', 'push2', 'dispatch', 'dispatch_refused', 'read')]
    route = re.compile(r'(?:^|&&\s*|;\s*)python(?:\s+-[A-Za-z]+(?:\s+utf8)?)*\s+\S*tools/b72[12]_rebuild\.py (push|dispatch|push_run|plan)\b', re.M)
    cmds = [r for r in S['cmds'] if r['tool'] in ('Bash', 'PowerShell') and route.search(r['cmd'])]
    return bool(mem) and all((r.get('free_mb') or 0) >= K.HOLD for r in mem) and order \
        and sum(1 for r in rows if r.get('kind') == 'dispatch') == K707.MAX_DISPATCHES and sum(1 for r in rows if r.get('kind') == 'dispatch_refused') == 1 \
        and bool(S['cmds']) and cmds == [] and K.MAX_DISPATCHES == 0


def merges_ok(S):
    """no kernel merge and no tag this act: each wave 1 kernel's rebuild branch at its pin or descending from it, not on main, no tag at its tip,
    its local tip equal to its remote-tracking tip, the pin's tag still peeling to the pin; the branch commits beyond a pin SIDE-frobenius's
    two alone, each by the seat's neutral identity; SIDE-explicit-formula's main and v0.37 unmoved; SIDE-lv-conservation's main, deposit and
    port-b707 unmoved, its tags as they stood; the join kernel's main and its one tag."""
    st = S['rebuild_state'] or {}
    beyond = dict((k, v['count']) for k, v in st.items() if v['count'] not in ('0', ''))
    tag = dict((k, t) for k, t, _p in K.WAVE1)
    # ### a branch at its pin is the tagged commit already on main, carrying the pin's one tag; a branch beyond its pin is off main, untagged
    # ### (the predicate's first form wanted every branch off main and untagged, which no branch at its pin can be -- refused by the probe)
    at_pin_ok = lambda k, v: v['tip'] == v['pin'] and v['on_main'] and v['tip_tags'] == [tag[k]]
    beyond_ok = lambda v: v['tip'] != v['pin'] and not v['on_main'] and not v['tip_tags']
    return sorted(st) == sorted(tag) \
        and all(v['tip'] and v['from_pin'] and v['remote'] == v['tip'] and v['tag_peel'] == v['pin']
                and (at_pin_ok(k, v) if v['count'] == '0' else beyond_ok(v)) for k, v in st.items()) \
        and beyond == {'SIDE-frobenius': '2'} and set(st['SIDE-frobenius']['author'].split(NL)) == {'b721 rebuild seat <b721-rebuild@relay.invalid>'} \
        and S['ef_main'] == K.EF_MAIN and S['ef_tags'].get('v0.37') == K.EF_V037 \
        and S['lv_main'] == K.LV_MAIN and S['lv_v0100'] == K.LV_V0100 and S['lv_port'] == K.PORT_NEW_TIP and not S['lv_tip_on_main'] \
        and [t for t in S['lv_tags'] if t.startswith('v0.1') and t > 'v0.13.0'] == [K.LV_TAG] \
        and S['join_main'] == K.JOIN_NEW_TIP and S['join_tags'] == [K.JOIN_TAG[0]]


# ================================================================== SCOPE, THE SEAL, THE ROOT, THE RECORD
def seal_hashes_ok(S):
    j = S['sealj']
    at = iso_epoch(j.get('at') or '')
    rec_ = j.get('tools') or {}
    return bool(rec_) and at is not None and S['lock_epoch'] is not None and S['lock_epoch'] <= at \
        and sorted(rec_) == sorted(K.SEALED) and all(S['sealnow'].get(t) == rec_[t] for t in K.SEALED)


POST_SEAL = tuple('%s %s' % (ACT_NOW, w) for w in ('seal', 'pre-root', 'root', 'record', '--', 'closing', 'entry'))


def _component_commit(s):
    return s.startswith(ACT_NOW) and not s.startswith(POST_SEAL)


def _step_phase(rows, repo, h):
    """the phase the act's step bank gives a commit (its row by repository and by the commit's abbreviated hash), None where it has no row.
    (R332)(4)(ii), v4 row (63): a row's every commit read through tools/act_close.py step_commits (a repair at b722)."""
    return next((r.get('phase') for r in rows if r.get('repo') == repo and any(c.startswith(h) for c in AC.step_commits([r]))), None)


def sealed_after_ok(S):
    """(R332)(2), a carry-time repair (b721's (i)): THE ACT'S STEP BANK (data/b722_steps.json, a row per commit by the record tool's step route,
    written after the commit: the repository, the commit, the phase the seat names from the record tool's STEP_PHASES) and not the commits'
    subjects -- b721's arm failed on two post-seal subjects outside its prefixes, their order right. Every relay and PLACE-papers commit of the
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


def nothing_ahead_ok(face, lock_epoch, logs, steps, face_first=None):
    """(R331)(3)(ii), standing clauses v3: THE GATE'S COMMIT READ FROM THE STEP BANK. A face cannot carry the hash of the commit that stamps it,
    so the gate's commit is the one step-bank row of phase `gate` (or, for an act before the repair, the row the control names), and every
    other commit at or before the lock is declared on the face by its 7-hex prefix. Pure in its arguments: logs [(hash, subject, epoch)],
    steps the step bank's rows.
    (R332)(4)(ii), standing clauses v4 row (63), EVERY COMMIT OF A STEP: the gate's commits are every commit of the step-bank rows of phase
    `gate` (tools/act_close.py step_commits), one or more; b721's arm wanted exactly one row and read its one commit, and so read the gate's
    second commit dcb3b286 undeclared (a repair at b722, banked by diff)."""
    gates = AC.step_commits(steps, phase='gate')
    if 'WHAT RAN AHEAD OF THIS SEAL' not in (face or '') or lock_epoch is None or not gates:
        return False
    # ### Component 8, after the lock and before the seal (an event): the face cannot carry the hash of the commit that first adds it, nor of
    # ### any commit after that one; b721 phased those `gate`, b722 phased its face commit and three after it `component 8`. A commit from the
    # ### face's first commit to the lock is read from the step bank, any phase; every commit before the face's first commit stays declared by
    # ### its hash on the face, as before.
    stepped = AC.step_commits(steps)
    fe = [t for h, s, t in logs if face_first and (h.startswith(face_first[:7]) or face_first.startswith(h[:7]))]
    fe = min(fe) if fe else None
    return all(h[:7] in face for h, s, t in logs if t <= lock_epoch and not any(gc.startswith(h[:7]) for gc in gates)
               and not (fe is not None and t >= fe and any(c.startswith(h[:7]) for c in stepped)))


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
    return _root_banked(S, ACT_NOW, AF['own_row'])   # ### v5 (ii): the act's own row the chain's next, read at run time


def root_last_ok(S):
    j = S['arj']
    at = j.get('at_epoch')
    items = [it.split()[0] for it in j.get('items') or [] if it.startswith('data/')]
    return at is not None and 'data/b722_seal_hashes.json' in items and len(S['bank_mtimes']) == len(items) \
        and all(m <= at + S['order_slack'] for m in S['bank_mtimes'].values())


def verify_ok(S):
    """the chain recomputed at commit in three parts: standing-b2a's and standing-b2b's banked quarters (b624-b641, b642-b658) and
    standing-b3's second half (b659-b722), every act AGREE, the boundary link equal, b680 read through its corrigendum row, b722 written LF."""
    ha = S['half_a'] or {}
    v = [tuple(x[:2]) for x in (ha.get('acts') or [])] + [tuple(x[:2]) for x in (S['ar_verify'] or [])]
    r = dict(ha.get('reads') or {}, **(S['ar_reads'] or {}))
    af = AC.act_figures(act=ACT_NOW)   # ### v5 (ii): the range read now, through the act's own row where it stands (b721's literal stale)
    return ha.get('head') == gs(ROOT, 'rev-parse', 'HEAD') and [x[0] for x in v] == ['b%d' % i for i in af['range']] \
        and all(x[1] == 'AGREE' for x in v) and (r.get('b%d' % af['range_last']) or {}).get('crlf') == 0 and (r.get('b680') or {}).get('corrected') == 4 \
        and (ha.get('boundary') or {}).get('equal') is True and S['boundary'].get('equal') is True \
        and (ha.get('boundary') or {}).get('root') == S['boundary'].get('root')


def unedited_all(S):
    return all(a is not None and a == b == c for a, b, c in S['currents'].values()) and len(S['currents']) == len(CURRENTS)


def corpus_scope_ok(S):
    """N5: PLACE-papers' changed files on main within K.PP_WRITTEN (FINDINGS, OPEN_TRAILS and INSTRUMENTS.md), both ledgers changed; no rename."""
    ch = S['pp_changed']
    ren = [l for l in S['pp_renames'].split(NL) if l[:1] in ('R', 'D')]
    return bool(ch) and set(ch) <= set(S['pp_allowed']) and 'FINDINGS.md' in ch and 'OPEN_TRAILS.md' in ch and not ren


# ### the face's dry-run needles for the entry ((G1), THE DRY-RUN NEEDLES -- ENTRY, 24), set by the Edit tool at Component 8 from the record
# ### tool's b722 composer, in place of b721's carried needles (the coefficients, the REGISTRY cells, the challenge, the pin)
ENTRY_NEEDLES = ('**The corrigendum and the repairs**', '**The C2 table’s test**', '**The table over h = 3, 4, 5 and two predictions**',
                 '**The offset, post hoc**', '**The surgery**', '**The frozen line**', '**The rebuild**', '**The federation pin, closed**',
                 '**The touch read**', '**The standing arms**', '**The citation check**', '**The scores.**', '**Read in mutual light**',
                 '**Carried to:**', '**Next.**', 'data/b722_registrations.txt', 'data/b722_derivation.txt', 'data/b722_offset_read.txt',
                 'data/b722_offset_tier.txt', 'data/b722_surgery_carry.txt', 'data/b722_frozen_line_drafts.txt', 'data/b722_rebuild.txt',
                 'data/b722_touch.txt', 'The act’s counter CLAIM ')


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
        and '### THE CITATION CHECK' in t and '### THE RECORD LINES' in t and '### THE DRY RUN' in t \
        and all(('THE %s' % s) in t for s in CLOSING_SECTIONS) \
        and 'THE STANDING ARMS' in t and 'counter_line()' in t and 'claim_figure(' in t \
        and '### THE KERNELS' in t and 'author_words_section' in t \
        and '### THE MIRROR' in t and '### THE CARRY`S DIFFS' in t


# ================================================================== THIS ACT'S ARMS OVER ITS OWN BANKS (Component 5)
NAV_LETTERS = ('d', 'e')      # ### (d) event (12)'s cause as (R332)(1)-(2) names it, (e) (R332)(2)'s "at step zero" against the ferry's order; every other the seat's


def defects_ok(S):
    rows = re.findall(r"^    \(([a-z])\) THE (NAVIGATOR|SEAT|CARRIED)\b", S['defects'], re.M)
    want = [list(x) for x in FLOORS['defects']]
    return len(rows) >= len(want) and [list(r) for r in rows[:len(want)]] == want and all(o in ('NAVIGATOR', 'SEAT', 'CARRIED') for _l, o in rows) \
        and [l for l, o in rows if o == 'NAVIGATOR'] == list(NAV_LETTERS)


def repairs_ok(S):
    """(R332)(3): every change diffed in data/b722_tool_repairs.txt by tools/standing/repairs.py -- (A) the extraction, 17 pairs against their
    sources and none not found; (B) the standing files without a pair; (C) the act's edits to its carried tools since its step zero and the
    shared edit of data/act_current.json (tools/mirror_verify.py), one diff per tool, their count the foot's; (D) the toolset's own repairs since
    b721's close, ten files changed, three new (allow.py, rootbanks.py, words.py); fourteen standing files; in Component 2's commit, re-banked
    before the lock."""
    t = S['repairs']
    m = re.search(r'^### ### \*\*PAIRS 17 ; NOT FOUND 0\s+; STANDING FILES 14 ; THE ACT`S CARRIED TOOLS EDITED (\d+) ; THE TOOLSET`S FILES CHANGED 10 \(NEW 3\)\.\*\*', t, re.M)
    c = t.split('## (C) ', 1)[1].split('## (D) ', 1)[0] if '## (C) ' in t else ''
    diffs = re.findall(r'^diff --git a/(\S+) b/', c, re.M)
    news = re.findall(r'^### tools/standing/(\S+) : NEW,', t, re.M)
    return '## (A) THE EXTRACTION' in t and '## (B) ' in t and '## (D) ' in t and bool(m) and int(m.group(1)) == len(diffs) \
        and all(('tools/' + f) in diffs for f in K.REPAIRED_TOOLS) and all(p.startswith('tools/') for p in diffs) \
        and sorted(news) == ['allow.py', 'rootbanks.py', 'words.py'] \
        and len(re.findall(r'^### PAIR tools/standing/', t, re.M)) == 17 and S['tracked']('data/b722_tool_repairs.txt') \
        and 'data/b722_tool_repairs.txt' in S['files']['c2']


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
    """the four figures banked by b706's tool over b706's roster against b721's baselines, each at or below b721's; the partners rows one copy
    per table, the figure 0."""
    j, f7 = S['figj'], jl('b721_standing_figures.json')
    figs = dict((k, (j.get(k) or {}).get('figure')) for k in ('correspondence', 'readme', 'partners', 'pins'))
    prev = dict((k, (f7.get(k) or {}).get('figure')) for k in figs)
    pr = (j.get('partners') or {}).get('rows') or []
    return all(isinstance(figs[k], int) and isinstance(prev[k], int) and figs[k] <= prev[k] for k in figs) and figs['partners'] == 0 \
        and len(pr) == 20 and all((r.get('reason') or '').startswith('ONE COPY') for r in pr) and j.get('roster') == 'b706_roster_read.json' \
        and j.get('baseline') == 'b721_standing_figures.json' and 'FIGURES AT b722' in S['figt']


# ================================================================== (R332)(2)-(7) AND N1-N3: THE ACT'S OBJECTS
def act_current_ok(S):
    """(R331)(3)(ii): the act's figures from one source -- data/act_current.json naming this act, the previous and the next, its ruling, the
    chain's row and its parts, the withheld field empty and the shared edits as the worklist names them; committed alone at step zero
    (4cabf3b7), the figures there the same in the keys read."""
    j = S['act_cur']
    try:
        z = json.loads(S['act_cur_z'] or '{}')
    except ValueError:
        z = {}
    keep = ('act', 'prev', 'next', 'ruling', 'prev_ruling', 'pre_relay', 'pre_pp', 'chain_row', 'prev_root', 'parts', 'withheld', 'replay')
    return j.get('act') == ACTN and j.get('prev') == PREV_ACT and j.get('next') == K.NEXT_ACT and j.get('ruling') == 'R332' \
        and j.get('chain_row') == AF['own_row'] and list(j.get('parts') or []) == list(K.PARTS) and j.get('withheld') == [] \
        and list(j.get('shared_edits') or []) == ['tools/' + f for f in K.REPAIRED_TOOLS] and bool(z) and all(z.get(k) == j.get(k) for k in keep) \
        and S['files']['actcur'] == [K.ACT_CURRENT]


COEFFS_FOOT = re.compile(r'\*\*n0\(-35\) = (\d+), b = (-?[\d/]+) ; n0\(-40\) = (\d+), b = (-?[\d/]+) ; ROWS (\d+): HELD (\d+), REFUTED (\d+), NOT SCORABLE (\d+) ; '
                         r'THE LAW (HELD|REFUTED) ; H-DECOMP (HELD|REFUTED) ; PRED-35 (HELD|REFUTED), PRED-40 (HELD|REFUTED) ; FORCED (\d+) APART ;')
COEFF_ROW = re.compile(r'(?m)^  (THE LAW clause [12](?: \(strong\))?|PRED-(?:35|40)|H-DECOMP T\(-\d+, \d\)|H-DECOMP \(overall\)|H-RR at -(?:35|40) \(NOT BLIND\))'
                       r'\s+(-\d+)?\s+(HELD|REFUTED|NOT SCORABLE)\s')
FORCED_ROW = re.compile(r'(?m)^  H-DECOMP F\(-\d+, \d\)\s+-\d+\s+FORCED, AS FORCED\s')
DERIV_FOOT = re.compile(r'\*\*CHECKS (\d+) STEPS x (\d+) DISCRIMINANTS AND THE C2 TABLE: ALL AS WANTED ; PLANTS: ALL FAIL AS WANTED ; THE GRADE: THE -2 OF BOTH '
                        r'CONFIGURATIONS A THEOREM IN C2 AT OMEGA 4 WITH ITS HYPOTHESES, -40`S -1/2 FROM THE SAME TABLE ; CLAUSE 1 REFUTED AT -40 ; THE STEP THAT '
                        r'REMAINS AT h > 2 NAMED ;')
PIN_HEAD = re.compile(r'THE PIN AT (\d+) OF (\d+) ELIGIBLE \(BUILDS\) ; PUSHED (\d+) ; DISPATCHED (\d+) ; READ (\d+) ; HELD \(BREAKS\) (\d+) ; NOT READ (\d+) ; '
                      r'EXCLUDED (\d+) ;')
import b719_arms as ARH   # noqa: E402  ### b719's guards (its Component 6), read unedited: no retirement this act ((R332), the run list of 116 binds); the carry's shift named b721_arms, which does not exist, set back at Component 8
GUARD_ARMS = tuple(sorted(ARH.GUARDS))
OAI = ('openai', 'OpenAI', 'Quasi-Riemann', 'QuasiRiemann', 'seven_eighths', 'Comparator')   # ### tools/b641_record.py OAI_NEEDLES, read there
CHALLENGE_FILE = 'SIDEExplicitFormula/Challenge/H2SignIffRH.lean'


def registrations_first_ok(S):
    """(R332)(3)-(4), N2 (Component 8, the Edit tool, over b722's objects): every computation at -31 and -55 names e8c3dff4 as its registration
    (data/b722_coeffs.txt) and every computation at the fourteen names H-C2-WALK at 15cb6cc4 (data/b722_walk.txt), each registration's commit
    an ancestor of the computation's commit (C3_RELAY); b721's registrations at HEAD equal to their blob at e8c3dff4, and b716's to b721's at
    their commits; the controls (data/b722_coeffs_controls.json, with the tool) committed at C2_CTL before the figures' commit, neither figure
    bank in it, and each figure bank printing its controls before its first field; no registration bank of b722."""
    c, w = S['coeffs'] or '', S['walk'] or ''
    return 'e8c3dff4' in c and 'H-C3-31' in c and 'H-C4-55' in c and '15cb6cc4' in w and 'H-C2-WALK' in w \
        and all(S['anc'].get(k) is True for k in ('reg_c3', 'reg_walk', 'ctl_c3')) \
        and S['reg_b721'][0] is not None and S['reg_b721'][0] == S['reg_b721'][1] \
        and all(a is not None and a == b for a, b in S['reg_blobs'].values()) \
        and 'data/b722_coeffs_controls.json' in S['files']['c2ctl'] and not [x for x in S['files']['c2ctl'] if x in ('data/b722_coeffs.txt', 'data/b722_walk.txt')] \
        and _ctl_first(c, '### THE CONTROLS FIRST', '## D = -31') and _ctl_first(w, 'THE CONTROLS FIRST', '## D = -15') \
        and not os.path.exists(os.path.join(D, 'b722_registrations.txt'))


def prediction_first_ok(S):
    """(R332)(9)(i), N5, the scan arm (the name the frozen run list carries; Component 8, the Edit tool): tools/b722_address_scan.py run live
    over every commit of the act (relay and PLACE-papers, fields, messages and added lines), the working trees' added lines and the untracked
    banks, the previous address read from history and held in memory -- its count 0, the author's name 0, its three controls as wanted; the
    bank's count the same; the address never printed (the tool refuses its own output where it would carry it)."""
    a = S['addr_live'] or {}
    return a.get('rc') == 0 and a.get('addr') == 0 and a.get('name') == 0 and 'CONTROLS 3 OF 3 AS WANTED' in (a.get('out') or '') \
        and re.search(r'\*\*PREVIOUS ADDRESS: 0 ; THE AUTHOR`S NAME: 0 ;', S['address'] or '') is not None


def coeffs_law_ok(S):
    """(R332)(3)-(4), N3 (Component 8, the Edit tool, over b722's objects): -31 and -55 and the fourteen, each row read on its own clauses --
    the controls json all as wanted (C1 exact, C2 reproducing b711's -23, C3 the planted coefficient failing); -31 and -55 each a row HELD or
    REFUTED with its prime clause, the foot equal to the rows; the fourteen each a row, the foot's counts equal to the rows', the control row
    -15 beside them; the walk's grade at its end naming the exhaustion over the list cited and Python, not compiled; both banks in C3_RELAY."""
    c, w = S['coeffs'] or '', S['walk'] or ''
    cc = S['coeffs_ctl'] or {}
    r34 = re.findall(r'(?m)^  (H-C[34]-\d+)\s+(-\d+)\s+(HELD|REFUTED)\s+computed .* the prime clause: ', c)
    rw = re.findall(r'(?m)^  (?:H-C2-WALK|CONTROL -15)\s+(-\d+)\s+()(HELD|REFUTED|NOT SCORABLE)\s+computed ', w)
    fw = re.search(r'\*\*H-C2-WALK: (\d+) OF 14 HELD, REFUTED (\d+), NOT SCORABLE (\d+) ; THE CONTROL ROW -15 (HELD|REFUTED) ;', w)
    fc = re.search(r'\*\*n0\(-31\) = \d+, b = \S+ ; n0\(-55\) = \d+, b = \S+ ; H-C3-31 (HELD|REFUTED) ; H-C4-55 (HELD|REFUTED) ;', c)
    g = w[w.rfind('### THE GRADE: '):]
    rows14 = [r for r in rw if int(r[0]) in set(K.WALK_DISCRIMINANTS)]
    return cc.get('ok') is True and cc.get('c1') is True and len(r34) == 2 and bool(fc) and [x[2] for x in r34] == [fc.group(1), fc.group(2)] \
        and bool(fw) and len(rows14) == 14 and sum(1 for r in rows14 if r[2] == 'HELD') == int(fw.group(1)) \
        and sum(1 for r in rows14 if r[2] == 'REFUTED') == int(fw.group(2)) and [r[2] for r in rw if r[0] == '-15'] == [fw.group(4)] \
        and 'by exhaustion' in g and 'cited and not compiled' in g and 'in Python, not compiled' in g \
        and all(x in S['files']['c3'] for x in ('data/b722_coeffs.txt', 'data/b722_walk.txt'))


def derivation_graded_ok(S):
    """(R332)(5), N3 (Component 8, the Edit tool, over b722's objects): the C2 statement's text committed alone (C4_STMT, the statement bank and
    its tool) before its grade and price (C4_RELAY), the text at HEAD equal to its blob there; THE GRADE read by E0 the foot's grade (E0's
    printed reading), the scope beside the statement naming Baker and Stark, cited; the statement true as written in Python at 18 of 18; the
    price per field at 18 rows by both routes, the foot at the bank's end; no Lean file and no dispatch (the price a count)."""
    p, st = S['c2_price'] or '', S['c2_stmt'] or ''
    g = re.search(r'(?m)^  THE GRADE: (\w+) -- ', p)
    f = re.search(r'\*\*THE C2 STATEMENT: E0 (\w+) ; SCOPE BESIDE IT \(Baker 1971, Stark 1975, cited\) ; AS WRITTEN, TRUE IN PYTHON AT (\d+) OF (\d+) ;', p)
    rows = re.findall(r'(?m)^  -\d+\s+\d+\s+\| .* \| .*\s(YES|NO)$', p)
    last = [l for l in p.split(NL) if l.strip()][-1:] or ['']
    return bool(st) and _own(S['files']['c4stmt']) == ['data/b722_c2_statement.txt', 'tools/b722_c2.py'] and S['anc'].get('stmt_price') is True \
        and _s(blob(ROOT, '%s:data/b722_c2_statement.txt' % K.C4_STMT)) == _s(blob(ROOT, 'HEAD:data/b722_c2_statement.txt')) \
        and bool(g) and bool(f) and g.group(1) == f.group(1) and f.group(2) == f.group(3) == '18' and len(rows) == 18 \
        and last[0].startswith('### ### **THE C2 STATEMENT') and 'data/b722_c2_price.txt' in S['files']['c4'] \
        and 'NOTHING RUNS LEAN, NOTHING IS DISPATCHED' in p


def offset_post_hoc_ok(S):
    """(R332)(6), N2 (the name the frozen run list carries; Component 8, the Edit tool, over b722's instruments): the rule printed before any
    tool is named (its line before the first act-numbered tool's); the output's count in the foot equal to the entries' (I-41 on, in order);
    INSTRUMENTS.md at PLACE-papers' act base a byte prefix of the file at the entries' commit C5_PP and the file now equal to it, I-41 the first
    new head, every entry head I-41 to I-<40+m> once, each with the six fields of b618's form; each validated case's needle at its bank and
    line; the entries composed after the rule's commit (C5_RULE an ancestor of C5_RELAY)."""
    it, E = S['instruments'] or '', (S['entries'] or {}).get('entries') or []
    m = re.search(r'\*\*THE RULE`S OUTPUT: (\d+) INSTRUMENTS \((\d+) NEW, TO BE ENTERED AS I-41 TO I-(\d+)\)', it)
    L = it.split(NL)
    rule_at = next((i for i, l in enumerate(L) if l.startswith('THE RULE ((R332)(6)), printed before any tool is named')), None)
    tool_at = next((i for i, l in enumerate(L) if re.search(r'\bb\d{3}_[a-z]\w*', l)), None)
    pre, c5, now = S['instr_pre'] or '', S['instr_c5'] or '', S['instr_now'] or ''
    new = c5[len(pre):] if c5.startswith(pre) else ''
    heads = re.findall(r'(?m)^## (I-\d+) — ', new)
    n = int(m.group(1)) if m else -1
    want = ['I-%d' % i for i in range(41, 41 + n)]
    fields = all(new.count(w) >= n for w in ('**Reads.**', '**Decides.**', '**Controls.**', '**Validated case.**', '**Range limits.**', '**Entered.**'))
    needles = []
    for x in E:
        v = x.get('validated') or {}
        bl = (rd(os.path.basename(v.get('bank') or '')) or '').split(NL)
        needles.append(0 < (v.get('line') or 0) <= len(bl) and (v.get('needle') or '\0') in bl[v['line'] - 1])
    return bool(m) and rule_at is not None and tool_at is not None and rule_at < tool_at and [x.get('id') for x in E] == want \
        and int(m.group(3)) == 40 + n and bool(pre) and c5.startswith(pre) and now == c5 and heads == want and fields \
        and len(needles) == n and all(needles) and S['anc'].get('rule_entries') is True and S['files']['c5pp'] == [K.INSTRUMENTS]


def surgery_carried_ok(S):
    """(R332)(8), the name the frozen run list carries (Component 8, the Edit tool, over b722's v8 and its propagation read): v8 at VERSION 8,
    v7's lines :10-:195 in it byte for byte, row (82) the quotation of the ferry's :23, its commit (STANDING_COMMIT) the one file and an
    ancestor of the propagation read's; the read's hits equal to the foot's count, UNREAD 0, its notes (each READS WRONG and DATED hit) the
    foot's figure; the notes landed in one block at FINDINGS K.PROPAGATION_LINE, the line its head, in Component 6's PLACE-papers commit alone."""
    v8, v7, p = S['v8'] or '', S['v7'] or '', S['propagation'] or ''
    L8, L7 = v8.split(NL), v7.split(NL)
    row82 = re.search(r'"(When the record corrects a statement, [^"]*)"', S['ferry'] or '')
    J = S['propj'] or []
    f = re.search(r'HITS (\d+) ; .* NOTES TO WRITE (\d+) ; UNREAD (\d+) ;', _verdict(p))
    land = ((S['prop_landing'] or {}).get('lines') or [{}])[0]
    return 'VERSION: 8' in L8[:4] and len(L8) > 195 and L8[9:195] == L7[9:195] and bool(row82) and ('      ' + row82.group(1)) in L8 \
        and 'ROWS 82 ;' in _verdict(v8) and S['files']['v8'] == [K.DATA_STANDING_V8] and S['anc'].get('v8_prop') is True \
        and _s(blob(ROOT, '%s:%s' % (K.STANDING_COMMIT, K.DATA_STANDING_V8))) == v8 and bool(f) and int(f.group(1)) == len(J) and f.group(3) == '0' \
        and int(f.group(2)) == sum(1 for x in J if x.get('grade') in ('READS WRONG', 'DATED')) \
        and str(land.get('line')) == str(K.PROPAGATION_LINE) and fline(S, K.PROPAGATION_LINE) == land.get('head') and S['files']['c6pp'] == ['FINDINGS.md'] \
        and all(x in S['files']['c6'] for x in ('data/b722_propagation.txt', 'data/b722_propagation.json', 'data/b722_propagation_landing.json'))


def arms_retired_ok(S):
    """(R332)(7): no arm retired this act, b721's run list of 116 binds with the one arm the ruling adds -- tools/standing/arms.py byte-equal
    to its blob at the act's base, its RETIRED as b721 left it and arm_tags.json's retired record equal to it, none a guard; this suite's run
    list 117 arms, without them, G-RESEARCH-REPRODUCES among them once (Component 8, the Edit tool: 116 before)."""
    rec_ = ((S['arm_tags'].get('retired') or {}).get('arms') or []) if isinstance(S['arm_tags'], dict) else []
    names = [a[0] for a in ARMS]
    return K.RETIRED_COUNT == 0 and S['arms_src_now'] == S['arms_src_pre'] and bool(S['arms_src_now']) and sorted(S['retired']) == sorted(rec_) \
        and not set(S['retired']) & set(GUARD_ARMS) and not set(S['retired']) & set(names) and len(ARMS) == 117 \
        and K.STANDING_ADDED == ('G-RESEARCH-REPRODUCES',) and names.count('G-RESEARCH-REPRODUCES') == 1


def count_route_priced_ok(S):
    """(R332)(10) and (12), the name the frozen run list carries (Component 8, the Edit tool): the axiom step diagnosed at the five pins by
    b721's runs read by their ids (the bank's rows the worklist's AXIOM_RUNS, in order, each classed, each priced), the foot's classes summing
    to five and NOTHING COMMITTED, PUSHED OR DISPATCHED; the LLM-contribution line's drafts -- the controls as wanted, the foot's SAME, DIFFERS
    and ABSENT the rows' and DRAFTS their DIFFERS and ABSENT, NOTHING EDITED (the monograph at HEAD its blob at the act's base); both banks in
    Component 7's commit."""
    A, lj, ft = S['axiom_diagj'] or [], S['llmj'] or {}, _verdict(S['axiom_diag'])
    runs = [(x.get('kernel'), int(x.get('run') or 0)) for x in A]
    cl = re.findall(r'(?:TARGETS ABSENT AT THE PIN|BUILD TARGET NOT COVERING THE AXIOM FILE`S IMPORTS|STEP NOT THE PIN`S OWN|OTHER) (\d+)', ft)
    rows = lj.get('rows') or []
    g = dict((w, sum(1 for r in rows if r.get('grade') == w)) for w in ('SAME', 'DIFFERS', 'ABSENT'))
    lf = re.search(r': SAME (\d+) ; DIFFERS (\d+) ; ABSENT (\d+) ; DRAFTS (\d+) ; NOTHING EDITED ;', _verdict(S['llm']))
    mono = 'day1/A_Place_to_Stand.md'
    return runs == [(k, int(r)) for k, r in K.AXIOM_RUNS] and all(x.get('class') and x.get('price') for x in A) and len(cl) == 4 \
        and sum(int(c) for c in cl) == len(A) == 5 and 'NOTHING COMMITTED, PUSHED OR DISPATCHED' in ft \
        and all(c[2] == c[3] for c in (lj.get('controls') or [])) and len(lj.get('controls') or []) == 3 and bool(lf) \
        and [int(x) for x in lf.groups()] == [g['SAME'], g['DIFFERS'], g['ABSENT'], g['DIFFERS'] + g['ABSENT']] \
        and _s(blob(PP, 'HEAD:' + mono)) == _s(blob(PP, '%s:%s' % (PRE['pp'], mono))) \
        and all(x in S['files']['c7'] for x in ('data/b722_axiom_diag.txt', 'data/b722_axiom_diag.json', 'data/b722_llm_line_drafts.txt', 'data/b722_llm_line_drafts.json'))


def research_reproduces_ok(S):
    """(R332)(7), the standing arm G-RESEARCH-REPRODUCES (Component 8, the Edit tool): tools/research/reproduce.py's run banked -- one row per
    instrument, the rows' ids the entries' (I-41 on, in order); each row REPRODUCES, DIFFERS or NOT RUN; each run row's planted wrong figure
    graded DIFFERS (as wanted); each NOT RUN row with its reason and its price (more than 60 s or a dispatch or network read); the json's
    counts and the bank's foot the rows'; the tool at HEAD its blob at the run's commit (C5_RELAY) and the working tree's."""
    j = S['reproducej'] or {}
    R = j.get('rows') or []
    ids = [x.get('id') for x in ((S['entries'] or {}).get('entries') or [])]
    run = [r for r in R if r.get('grade') in ('REPRODUCES', 'DIFFERS')]
    nr = [r for r in R if r.get('grade') == 'NOT RUN']
    c = dict((g, sum(1 for r in R if r.get('grade') == g)) for g in ('REPRODUCES', 'DIFFERS', 'NOT RUN'))
    f = re.search(r'ROWS (\d+) ; REPRODUCES (\d+) ; DIFFERS (\d+) ; NOT RUN (\d+) ; PLANTED CONTROLS AS WANTED (\d+) OF (\d+) ;', _verdict(S['reproduce']))
    tool = 'tools/research/reproduce.py'
    src = _s(blob(ROOT, 'HEAD:' + tool))
    return bool(R) and [r.get('id') for r in R] == ids and len(run) + len(nr) == len(R) \
        and all(str(r.get('planted_as_wanted')) == 'True' and r.get('planted_grade') == 'DIFFERS' for r in run) \
        and all(re.match(r'(MORE THAN 60 s|A DISPATCH|A NETWORK READ): ', r.get('why') or '') and 'priced' in (r.get('why') or '') for r in nr) \
        and j.get('counts') == c and bool(f) and [int(x) for x in f.groups()] == [len(R), c['REPRODUCES'], c['DIFFERS'], c['NOT RUN'], len(run), len(run)] \
        and bool(src) and src == _s(blob(ROOT, '%s:%s' % (K.C5_RELAY, tool))) and src == (read(os.path.join(ROOT, *tool.split('/'))) or '')


def differs_errata_ok(S):
    """(R332)(1)-(2): no DIFFERS entry and no ERRATA entry this act -- ERRATA.md byte-equal to its blob at the act's base, no b722 differs or
    errata bank, the worklist naming no line or id for either; the weight line and the corrigendum at FINDINGS in Component 1's PLACE-papers
    commit, FINDINGS the one file there."""
    return S['errata_pp_now'] == S['errata_pp_pre'] and bool(S['errata_pp_now']) and not S['differs'] and not S['errata'] \
        and K.DIFFERS_LINE is None and K.ERRATA_LINE is None and K.ERRATA_ID is None and S['files']['c1pp'] == ['FINDINGS.md'] \
        and 'weight' in fline(S, K.WEIGHT_LINE).lower()


def touch_read_ok(S):
    """standing clauses v8 ((R332)(8): "The touch read of v8 is banked before the root"), N4: the touch read banked as data/b722_touch.txt by hand before the root -- its rows each marked AGREES or DIFFERS
    (no row unmarked), at least one row; no touch tool built (no tools/b722_touch.py)."""
    rows = [l for l in (S['touch'] or '').split(NL) if re.match(r'^  \(\d+\) ', l)]
    return bool(rows) and all(re.search(r'\b(AGREES|DIFFERS)\b', l) for l in rows) and not os.path.exists(os.path.join(T, 'b722_touch.py'))


def arm_tags_ok(S):
    """b721's tags read: every arm of the suite (the whole list, the retired among it) tagged CLAIM or CLOSE in data/arm_tags.json, no tag naming
    an arm the suite does not carry, every tag one of the two words; the claim arms thirty-eight; the file byte-equal to its blob at the act's
    base (outside (R332)(8)'s (W) list)."""
    tags = (S['arm_tags'].get('tags') or {}) if isinstance(S['arm_tags'], dict) else {}
    names = [a[0] for a in ARMS_ALL]
    # ### the act shift the file cannot take this act (outside (R332)(9)'s (W) list): the file last written at b719 names G-R329-ENTERED, the
    # ### suite carries G-R332-ENTERED -- the one difference allowed, both ways, the old name CLOSE; the closing's tally counts G-R332-ENTERED
    # ### apart as untagged (Component 8, the Edit tool: the carry's substitution had made the file's name G-R331-ENTERED, which it does not carry)
    # ### (R332)(7)'s arm, G-RESEARCH-REPRODUCES, is new and the file is outside the (W) list: it stands untagged beside the act shift and the
    # ### closing's tally counts it apart (Component 8, the Edit tool)
    shift = (sorted(set(names) - set(tags)), sorted(set(tags) - set(names)))
    return bool(tags) and shift == (['G-R332-ENTERED', 'G-RESEARCH-REPRODUCES'], ['G-R329-ENTERED']) and tags.get('G-R329-ENTERED') == 'CLOSE' \
        and set(tags.values()) <= {'CLAIM', 'CLOSE'} and sum(1 for v in tags.values() if v == 'CLAIM') == 38 and S['arm_tags_raw'] == S['arm_tags_pre']


def hook_wired_ok(S):
    """v5 row (77): the hook in the seat's project settings (D:/.claude/settings.json) on Read|Bash|PowerShell naming the standing toolset's
    tools/standing/hook.py (the act read from data/act_current.json at each call), unedited through v1.2.0 (its blob at the act's base the same);
    b715's offline control 16 of 16 over the four refusal kinds, read where b715 banked it (data/b715_hook_control.txt; the carry's act shift
    named a b721 bank that does not exist, repaired at Component 6); this act's refusals written to its own bank."""
    st = S['settings'] or ''
    hc = rd('b715_hook_control.txt')
    return 'PreToolUse' in st and 'standing/hook.py' in st.replace('\\\\', '/') and 'Read|Bash|PowerShell' in st \
        and 'def judge(' in (S['hook_src'] or '') and 'act_current.json' in (S['hook_src'] or '') \
        and cr0(blob(ROOT, '%s:tools/standing/hook.py' % PRE['relay'])) == cr0(raw(os.path.join(T, 'standing', 'hook.py'))) \
        and '### ### **CASES 16 ; AS WANTED 16 ; REFUSAL KINDS ENV,PIPE,READ,REDIR ; ALLOWED CASES 6 ; ALL AS WANTED True**' in hc \
        and bool(S['hook_refusals'])


def lettering_one_ok(S):
    """v5 row (78): one lettering -- tools/act_letters.py defining the sequence and its reader, this suite importing it, the corrigendum arm
    reading its letters through it. (R332)(3) orders tags, not letters: this act's corrigendum tool letters nothing (b721's defects keep their
    letters (a)-(r), its events their rows), so it carries no lettering of its own -- no `after(` and no letter sequence built in its code
    (the carried clause "the corrigendum tool importing it" read b721's tool, which lettered b715's events; repaired at Component 6)."""
    ls, cs, su = strip_prose(S['letters_src'] or ''), strip_prose(S['corr_src'] or ''), strip_prose(S['suite'] or '')
    return 'def read(' in ls and 'def after(' in ls and 'import act_letters as AL' in su \
        and not re.search(r'\bafter\(|ascii_lowercase|chr\(ord\(', cs) and 'AL.read(' in strip_prose(_fn_src(S['suite'], 'corrigendum_ok'))


def membrane_ok(S):
    """the carried membrane: tools/act_membrane.py's guard read by its text (guard and guard_path, data/act_roots.txt read), the record tool's
    shared writers rebound through it, the suite's writer calling it before every write."""
    m = strip_prose(S['membrane_src'])
    return 'def guard(' in m and 'def guard_path(' in m and 'act_roots.txt' in m and 'MEM.guard(ACT, name, R.ROOT_EXCLUDE)' in S['rec_src'] \
        and S['suite'].count('_membrane(') >= 8


def no_dispatch_ok(S):
    """N1: no runner dispatch and no lean process this act -- no dispatch bank of b722's, the command capture's dispatches none and its local lean
    none (the record tool's command bank), the capture read live non-empty."""
    return not S['disp_now'] and bool(S['cmdj']) and (S['cmdj'].get('dispatches') or []) == [] and not S['cmdj'].get('local_lean') and bool(S['cmds'])


def _s(x):
    return x.decode('utf-8', 'replace') if isinstance(x, bytes) else (x or '')


def _verdict(t):
    """a bank's verdict: the `### ### **...**` line, its continuation lines (each `### `-led) joined by one space -- the offset read's and the
    count route's verdicts wrap across three and two lines (a carry-time repair of this act's own reader, Component 7)."""
    m = re.search(r'^### ### \*\*(.*?)\*\*[ \t]*$', t or '', re.M | re.S)
    return ' '.join(re.sub(r'(?m)^### ', '', m.group(1)).split()) if m else ''


def _own(files):
    """a component commit's files less the step bank, whose row for the commit before rides in it (the record tool's step route)."""
    return [f for f in files if f != 'data/b722_steps.json']


def _ctl_first(t, ctl, fig):
    """a bank's controls section printed before its figures section, both present."""
    i, j = (t or '').find(ctl), (t or '').find(fig)
    return 0 <= i < j



def receipt_ok(S):
    """the banked ferry received in full, its ruling's end and the ferry's tail; by version (b721's repointing, carried): every "standing clauses
    v<N>" the ferry names outside a quotation read against data/standing_clauses_v<N>.txt, present at its VERSION line (this act's ferry names
    v7, which binds unchanged: no standing control written this act), and v7 byte-equal to its blob at the act's base."""
    f = S['ferry']
    named = sorted(set(int(m.group(1)) for m in re.finditer(r'standing clauses v(\d+)', re.sub(r'“[^”]*”', '', ' '.join(f.split())), re.I)))
    have = all(re.search(r'^VERSION: %d$' % v, read(os.path.join(D, 'standing_clauses_v%d.txt' % v)) or '', re.M) for v in named)
    # ### Component 8, the Edit tool: b722's ferry names no "standing clauses v<N>" outside a file name (it names data/standing_clauses_v8.txt
    # ### and v8 by row), so the carried `7 in named` read nothing; v7 is read by its bytes below and v8 by G-SURGERY-CARRIED
    return 'RULING (R332) END' in f and f.rstrip().endswith(K.TAIL) and have \
        and bool(S['standing_v7_now']) and S['standing_v7_now'] == S['standing_v7_pre']


ARMS_ALL = [
    ('G-RECEIPT-IN-FULL', 'the banked ferry, the standing clauses read by version: each version the ferry names read against its bank, v7 unchanged from 30c0b3c8',
     lambda S: receipt_ok(S), lambda S: put(S, 'ferry', S['ferry'].replace(K.TAIL, ''))),
    ('G-SCAN-CLEAN', 'the ferry scan`s verdict line', lambda S: re.search(r'^\s*### VERDICT: ### \*\*0 HIT\(S\) REPORTED', S['scan'], re.M) is not None,
     lambda S: put(S, 'scan', S['scan'].replace('0 HIT(S)', '1 HIT(S)'))),
    ('G-PROCS-LISTED', 'the step-zero bank: tail, lean, lake, python and claude named, the seat`s claude alone, none of the others; no task stopped, no orphan, nothing stopped by PID',
     lambda S: procs_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('python 0', 'python 1'))),
    ('G-STEPZERO-TESTS', 'the step-zero bank`s tests section: not run at this step zero, N1 (no lean on the host); no tests bank of this act`s, nothing withheld (b721`s run of the tracked test files not carried)',
     lambda S: tests_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('not run at this step zero', 'run at this step zero'))),
    ('G-PUSHOUT-COMMITTED', 'the step-zero commit`s files and ancestry', lambda S: S['pushout'][0] == ['data/b721_relay_push-b721-closing_push_out.txt'] and S['pushout'][1],
     lambda S: put(S, 'pushout', (['data/x'], True))),
    ('G-BRANCHES-DELETED', 'relay`s and PLACE-papers` branch lists by the five push-b721* names, the step-zero bank`s branch row, port-b707 and recut-b712-silence standing at their tips',
     lambda S: branches_ok(S), lambda S: put(S, 'branch_lists', dict(S['branch_lists'], **{'D:/relay': 'push-b721'}))),
    ('G-READFIRST-CITED', 'the read-first bank: every item of the ferry`s list cited by path and line', lambda S: readfirst_ok(S),
     lambda S: put(S, 'readfirst', '')),
    ('G-ANSWERS-BANKED', 'the answers bank read at HEAD: its prompts and calls at or above the sealed floors (none before the root), each with its options and result, any call after the lock named on the face',
     lambda S: answers_ok(S), lambda S: put(S, 'answers', re.sub(r'(?m)^(### b722 -- THE AUTHOR`S ANSWERS, )(\d+)', lambda m: m.group(1) + str(int(m.group(2)) + 1),
                                                                 S['answers']))),
    ('G-LOCAL-BANK-UNTRACKED', 'b628`s local intake bank: present, untracked, in no commit', lambda S: S['local_present'] and S['local_log'] == ''
     and S['local_index'] == '' and S['local_status'].startswith('??'), lambda S: put(S, 'local_log', 'abc1234')),
    ('G-EXPORT-UNTRACKED', 'the navigator`s export: present, untracked, in no commit', lambda S: S['export_present'] and S['export_log'] == ''
     and S['export_index'] == '' and S['export_status'].startswith('??'), lambda S: put(S, 'export_index', EXPORT)),
    ('G-EDIT-ROUTE', 'the record tool`s one reading (tools/edit_route.py`s arms and sed in any form) over this act`s whole capture and the previous act`s after its post-push suite (b721`s own session, b701`s form), read live',
     lambda S: edit_route_ok(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd="sed -n 1p tools/b722_record.py")])),
    ('G-NO-LOCAL-LEAN', 'the act`s command capture, read live: no command of the seat runs lean or lake on this host (N1)', lambda S: no_local_lean(S),
     lambda S: put(S, 'cmds', S['cmds'] + [dict(n=0, tool='Bash', ts='', src='planted', cmd='lake env lean ChainProbe.lean')])),
    ('G-WEIGHT-LINE', 'FINDINGS at the record-lines bank`s line, found by conv: b721`s weight line, its head line as the closing prints it and the record`s commits beside it', lambda S: weight_ok(S), lambda S: _rl(S, 0, 1)),
    # ### (R332)(7): the standing arm the ruling adds, the run list 117 (Component 8, the Edit tool)
    ('G-RESEARCH-REPRODUCES', '(R332)(7): tools/research/reproduce.py`s run -- one row per instrument I-41 on, each REPRODUCES, DIFFERS or NOT RUN, each run row`s planted wrong figure graded DIFFERS, each NOT RUN with its reason and price; the counts and the foot the rows`; the tool sealed at its run`s commit',
     lambda S: research_reproduces_ok(S), lambda S: _mut(S, 'reproducej', lambda d: (d.get('rows') or [{}])[0].update(planted_as_wanted='False'))),
    # ### ACT ARMS (Component 5)
    ('G-DRY-STEP-CLEAN', 'the gate`s record: the dry-run step CLEAN, the trail`s Defects and Resolved lines equal to the bank, the gate CLEAR',
     lambda S: dry_step_ok(S), lambda S: put(S, 'gate', '')),
    ('G-CLOSING-DRY-STEP', 'the gate`s record: the closing tool run dry before the lock, its sections read (the corrigendum and the repairs, the standing clauses and the hook, the tier moves, the head, the readings, the pilot and its one line, the standing report, the standing arms, the kernels), every NO VERDICT LINE row read by the bank it names ((R332)(2)(iii): the bank present and carrying no verdict line by the closing`s reader; no list of names)',
     lambda S: closing_dry_ok(S), lambda S: put(S, 'gate', S['gate'].replace('THE CLOSING DRY-RUN STEP : CLEAN', 'THE CLOSING DRY-RUN STEP : NOT CLEAN'))),
    ('G-CITATION-CHECKED', 'the citation bank: every cite checked at step zero, 90 = 88 OK + 2 misses (each raised or entered before the component citing it), the bank before the step-zero commit and that before Component 1`s',
     lambda S: citation_ok(S), lambda S: put(S, 'citation', '')),
    ('G-R332-ENTERED', 'the trail record`s ratification line', lambda S: '**(R332) ratified.**' in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**(R332) ratified.**', '**(R332) read.**'))),
    ('G-ROWGEN-STEPZERO', 'the rowgen bank`s verdict line (the roster re-pointed, 8)', lambda S: rowgen_ok(S), lambda S: put(S, 'rowgen', '')),
    ('G-BRANCHES-BANKED', 'the step-zero bank`s branch row (no branches bank this act): the five refs named with their tips, in the step-zero commit, the citation check before the first delete; the one kept branch at its tip',
     lambda S: branches_banked_ok(S), lambda S: put(S, 'stepz', S['stepz'].replace('push-b721-closing (30c0b3c8)', 'push-b721-closing'))),
    ('G-DELETES-ONE-BRANCH', '(R331)(3)(i): the command capture`s branch deletes, each one branch, no glob, no variable, nothing chained after, each allowed by the ruling`s own delete clauses read through tools/standing/allow.py (port-b707 the ruling`s NOT deleted); the command bank`s count',
     lambda S: deletes_one_ok(S), lambda S: put(S, 'ferry', S['ferry'].replace('the push-b721-* branches of relay and PLACE-papers deleted by name', 'the push-b721-* branches of relay and PLACE-papers kept by name'))),
    ('G-LISTINGS-BEFORE-CLAUSES', 'N3: the `--merged` listing in the capture before the first delete; every branch deleted among those banked before any delete; the step-zero bank`s listings row',
     lambda S: listings_before_ok(S), lambda S: put(S, 'first_listing_ts', 10 ** 12)),
    ('G-ANSWERS-CHECKED', 'the citation bank`s mid-act prints: the first prompt`s answer and the root prompt`s, each with its time, the root`s after the lock',
     lambda S: answers_checked_ok(S), lambda S: put(S, 'citation', '')),
    ('G-ANSWERS-BEFORE-WRITES', '(R331)(3)(i): the answers bank`s prompts read against the ruling`s "root`s prompt put once" and the banked words through tools/standing/allow.py, none unbanked; every check stamp after the lock and at or before the root; the plant moving every stamp past the root',
     lambda S: answers_before_ok(S), lambda S: answers_plant(S)),
    ('G-SCORER-READS-BANKS', 'the record tool`s scorers: banks alone, no ledger line (data/b686_rules.txt row (1))', lambda S: scorer_banks_ok(S),
     lambda S: put(S, 'rec_src', '')),
    ('G-ENTRY-SCORES-EQUAL', 'the landed entry`s scores line against the scores bank', lambda S: entry_scores_ok(S), lambda S: put(S, 'sc', {})),
    ('G-ENTRY-TITLE-FORM', 'the landed entry`s title by its objects (the C2 rule choosing none, the halt proved; the table over h = 3, 4, 5 and the predictions at -31 and -55; the offset post hoc, 0 new pairs; the surgery carried; the frozen line and its drafts; 6 of 6 wave 1 kernels building, one with a sorry; the federation pin closed), compared after case-folding the article alone',
     lambda S: entry_title_ok(S), lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-CORRIGENDUM-ENTERED', '(R332)(2): the generated corrigendum for b721`s record, landed at FINDINGS :11218: its fifteen events and twenty-seven defects, 42 items each CLAIM or CLOSE and NEW or REPEAT, CLAIM 5 CLOSE 37, REPEAT 24; v1.2.2`s repairs, 12 cases; the corrigenda bank appended at row (42)',
     lambda S: corrigendum_ok(S), lambda S: put(S, 'corrj', {})),
    ('G-WRITELIST-MIRROR-STATE', '(R332)(9): the face`s (W) row for the mirror builder naming tools/mirror_prevbuild.json beside the zip and its stage; the record tool`s N5 reading it as the builder`s',
     lambda S: writelist_mirror_state_ok(S), lambda S: put(S, 'face', S['face'].replace('tools/mirror_prevbuild.json', 'tools/mirror_x.json'))),
    ('G-RULES-ROW-ENTERED', 'the rules that bind this act read where they stand: b710`s row (1) by version (v7 at VERSION 7), b709`s carry row (the carry banks), b708`s report row (no report tool sealed); this act`s rules bank carrying (R332)(1)`s row alone, in Component 1`s commit; no b723 rules bank',
     lambda S: rules_row_ok(S), lambda S: put(S, 'standing_bank', S['standing_bank'].replace('VERSION: 7', 'VERSION: 6'))),
    ('G-REPORT-UNSEALED', 'the standing report bank by the unsealed tool before the root: its stamp after the lock and at or before the root`s, its eight lines by its JSON in footing order (KERNEL, CERTIFIED, REGISTERED, HELD), every source seated, its keys read case-insensitively, no scores line in it, the tool unsealed',
     lambda S: report_unsealed_ok(S), lambda S: put(S, 'reportj', dict(S['reportj'], lines=(S['reportj'].get('lines') or [])[:1]))),
    ('G-GUARD-HELD', 'the suite`s writer block guarded by `if PRERUN:` and its dry run banked', lambda S: guard_ok(S), lambda S: put(S, 'guard', '')),
    ('G-POSTROOT-WRITES-NONE', 'the per-part seconds banks` commit times against the root`s', lambda S: postroot_writes_none(S), lambda S: put(S, 'guard', '')),
    ('G-TRAIL-LINES-EQUAL-DEFECTS', 'the landed trail`s Defects and Resolved lines against the owners of the letters entered before the seal ((R332)(2)(i))', lambda S: trail_lines_equal_defects(S),
     lambda S: put(S, 'letters_seal', (S['letters_seal'] or []) + ["(z) THE SEAT'S: A LETTER PLANTED BEFORE THE SEAL AND MISSING FROM THE TRAIL"])),
    ('G-TRAIL-DEFECTS-EQUAL', 'the gate`s record and the landed trail`s Defects line against the repaired reader`s rows', lambda S: trail_defects_ok(S),
     lambda S: put(S, 'gate', '')),
    ('G-TRAIL-RESOLVED-EQUAL', 'the gate`s record and the landed trail`s Resolved line against the bank`s owners', lambda S: trail_resolved_ok(S),
     lambda S: put(S, 'gate', '')),
    ('G-DEFECTS-LETTERED', 'the defects bank: the sealed floors` rows with their owners in order, every one the seat`s',
     lambda S: defects_ok(S), lambda S: put(S, 'defects', '')),
    ('G-ROOTDRY-READY', 'data/b706_rules.txt row (1): the root route run dry on the pre-root tree before the lock, READY True, printed in the face`s (0)',
     lambda S: rootdry_ok(S), lambda S: _mut(S, 'rootdryj', lambda d: d.update(ready=False))),
    ('G-FIGURES-BANKED', 'the four standing figures banked by b706`s tool over b706`s roster against b721`s baselines, each at or below b721`s, the partners figure 0 with one copy per table',
     lambda S: figures_banked_ok(S), lambda S: put(S, 'figj', {})),
    ('G-READFIRST-DIFF-BANKED', 'the closure reader`s diff banked; the readfirst bank unchanged since the step-zero commit', lambda S: readfirst_diff_ok(S),
     lambda S: put(S, 'rf_diff', '')),
    ('G-MEMBRANE-WIRED', 'the carried membrane: tools/act_membrane.py`s guard reading data/act_roots.txt, the record tool`s shared writers rebound through it, the suite`s writers calling it',
     lambda S: membrane_ok(S), lambda S: put(S, 'membrane_src', S['membrane_src'].replace('def guard_path(', 'def guard_p('))),
    ('G-HOOK-WIRED', 'v5 row (77): the PreToolUse hook in D:/.claude/settings.json on Read|Bash|PowerShell naming tools/standing/hook.py, unedited through v1.2.0; b715`s offline control 16 of 16 (data/b715_hook_control.txt); this act`s refusals in its own bank',
     lambda S: hook_wired_ok(S), lambda S: put(S, 'settings', (S['settings'] or '').replace('standing/hook.py', 'b722_hook.py'))),
    ('G-LETTERING-ONE', 'v5 row (78): tools/act_letters.py the one lettering, imported by this suite, the corrigendum arm reading through it; the corrigendum tool lettering nothing of its own ((R332)(3): tags, not letters)',
     lambda S: lettering_one_ok(S), lambda S: put(S, 'corr_src', (S['corr_src'] or '') + NL + 'X = AL.after(PREV_LETTERS, 9)')),
    ('G-ACT-CURRENT', '(R332)(3): data/act_current.json naming b722, b721, b722, R332, the chain row act_figures reads, the seven parts, withheld empty, the shared edit; committed alone at step zero, its figures unchanged since',
     lambda S: act_current_ok(S), lambda S: _mut(S, 'act_cur', lambda d: d.update(withheld=['G-X']))),
    # ### the act arms' names frozen with the run list; each description, predicate and plant over b722's objects (Component 8, the Edit tool)
    ('G-REGISTRATIONS-FIRST', '(R332)(3)-(4), N2: every computation at -31 and -55 naming e8c3dff4 and every computation at the fourteen naming H-C2-WALK at 15cb6cc4, each an ancestor of the figures` commit 6afe03bf; b721`s registrations at HEAD their blob at e8c3dff4; the controls committed at 417ced62 before the figures, each bank printing its controls before its first field',
     lambda S: registrations_first_ok(S), lambda S: put(S, 'coeffs', (S['coeffs'] or '').replace('e8c3dff4', '00000000'))),
    ('G-PREDICTION-FIRST', '(R332)(9)(i), N5, the scan arm: tools/b722_address_scan.py run live over every commit of the act, the working trees` added lines and the untracked banks -- PREVIOUS ADDRESS 0, the author`s name 0, three controls as wanted, the bank`s count the same; the address never printed',
     lambda S: prediction_first_ok(S), lambda S: _mut(S, 'addr_live', lambda d: d.update(addr=1))),
    ('G-COEFFS-LAW', '(R332)(3)-(4), N3: -31 and -55 each HELD or REFUTED with its prime clause, the foot the rows; the fourteen each a row, the foot`s counts the rows`, the control row -15 beside them; the controls json all as wanted; the walk`s grade at its end naming the exhaustion over the cited list in Python, not compiled',
     lambda S: coeffs_law_ok(S), lambda S: put(S, 'walk', (S['walk'] or '').replace('by exhaustion', 'by sampling'))),
    ('G-DERIVATION-GRADED', '(R332)(5), N3: the C2 statement committed with its tool at 50397f61 before its grade and price at 14190fe4, the text at HEAD its blob there; THE GRADE E0`s printed reading and the foot`s; the scope beside it citing Baker and Stark; true as written in Python at 18 of 18, priced at 18 rows; nothing runs Lean, nothing dispatched',
     lambda S: derivation_graded_ok(S), lambda S: put(S, 'c2_price', (S['c2_price'] or '').replace('  THE GRADE: ', '  A GRADE: '))),
    ('G-OFFSET-POST-HOC', '(R332)(6), N2: the instruments` rule printed before any tool is named (f52ea31b, an ancestor of 3e4415fb); the output`s count the entries` I-41 on; INSTRUMENTS.md at 2b194142 a byte prefix of the file at 4af48e1e and the file now equal to it, each head once with b618`s six fields, each validated case at its bank`s line',
     lambda S: offset_post_hoc_ok(S), lambda S: put(S, 'instr_now', (S['instr_now'] or '') + NL + '## I-999 — A PLANTED ENTRY')),
    ('G-SURGERY-CARRIED', '(R332)(8): v8 at VERSION 8, v7`s :10-:195 byte for byte and row (82) the ferry`s :23, alone at 0ff64911 before the propagation read; the read`s hits the foot`s 431, UNREAD 0, its notes each READS WRONG and DATED hit; landed in one block at FINDINGS :11284 in f127660c alone',
     lambda S: surgery_carried_ok(S), lambda S: put(S, 'propj', (S['propj'] or [])[:-1])),
    ('G-ARMS-RETIRED', '(R332)(7): no arm retired this act, b721`s run list of 116 binds with G-RESEARCH-REPRODUCES added -- tools/standing/arms.py byte-equal at 30c0b3c8, its RETIRED equal to arm_tags.json`s retired record, none a guard; this suite`s run list 117 arms without them',
     lambda S: arms_retired_ok(S), lambda S: put(S, 'retired', list(S['retired']) + ['G-SEAL-VERIFIES'])),
    ('G-COUNT-ROUTE-PRICED', '(R332)(10) and (12): the axiom step diagnosed at the five pins by b721`s runs read by their ids, each classed and priced, NOTHING COMMITTED, PUSHED OR DISPATCHED; the LLM-contribution line`s controls as wanted, its SAME, DIFFERS, ABSENT and DRAFTS the rows`, the monograph unedited; both in 93f20fce',
     lambda S: count_route_priced_ok(S), lambda S: put(S, 'axiom_diag', (S['axiom_diag'] or '').replace('NOTHING COMMITTED, PUSHED OR DISPATCHED', 'A RUN DISPATCHED'))),
    ('G-DIFFERS-ERRATA', '(R332)(1)-(2): no DIFFERS entry and no ERRATA entry this act -- ERRATA.md byte-equal at 2b194142, no b722 differs or errata bank, the worklist naming none; the weight line and the corrigendum in Component 1`s PLACE-papers commit cbb3b47f, FINDINGS the one file there',
     lambda S: differs_errata_ok(S), lambda S: put(S, 'differs', '### a planted DIFFERS bank')),
    ('G-TOUCH-READ', 'standing clauses v8 ((R332)(8)), N4: data/b722_touch.txt by hand before the root, every row AGREES or DIFFERS; no touch tool built',
     lambda S: touch_read_ok(S), lambda S: put(S, 'touch', (S['touch'] or '') + NL + '  (99) an unmarked row')),
    ('G-ARM-TAGS', 'the tags read: data/arm_tags.json tagging every arm of the suite CLAIM or CLOSE but the act shift (G-R332-ENTERED in the suite, G-R329-ENTERED CLOSE in the file) and (R332)(7)`s new arm, untagged; the claim arms thirty-eight; the file byte-equal at 30c0b3c8 (outside the (W) list)',
     lambda S: arm_tags_ok(S), lambda S: _mut(S, 'arm_tags', lambda d: (d.get('tags') or {}).pop('G-ARM-TAGS', None))),
    ('G-PARTS-PRERUN', 'the pre-run bank: seven parts, each named with its arms and seconds, the longest under the 590 s guard', lambda S: parts_prerun_ok(S),
     lambda S: put(S, 'prerun', '')),
    ('G-ARM-SECONDS-BANKED', 'the per-part seconds bank gathered before the seal', lambda S: arm_seconds_ok(S), lambda S: put(S, 'asec', {})),
    ('G-SPEC-PLANTED', 'tools/b722_regspec.py`s planted rows run live through the record tool`s readers, and rows of another shape refused',
     lambda S: bool(S['spec']['read']) and all(S['spec']['read']) and all(S['spec']['controls']) and any('runner' in x for x in S['spec']['shapes']),
     lambda S: _mut(S, 'spec', lambda d: d['controls'].append(False))),
    ('G-CONVERSION-ONE', 'every b722 tool`s code: no conversion defined (conv imported from b652_record); the suite importing it',
     lambda S: S['conv_bad'] == [] and 'from b722_record import conv' in S['suite'], lambda S: put(S, 'conv_bad', ['b722_checks.py'])),
    ('G-WORKFLOW-FILES', 'b712`s runs` workflows, read as banked (no dispatch at either kernel since; this act`s one dispatch, at SIDE-effects, read by G-PIN-READ): build-module.yml at port-b707`s new tip and at SIDE-faces-join`s re-pinned main, each its base`s blob unchanged, no author identifier, no secret, the hold, the lakefile and its cache step; at the port the print list absent (the print step read as not run, no grade claimed, the dispatch rows `whole` False), at the join the print list faces_join, its module FacesJoin; this act`s writes the one module twice and the one lakefile',
     lambda S: wf_ok(S), lambda S: _mut(S, 'wf', lambda d: d[K.KERNEL].update(text=d[K.KERNEL]['text'] + ' secrets.X'))),
    # ### event (8), before the seal, the Edit tool: both plants and descriptions carried b721's challenge and pin objects (no key this act);
    # ### the descriptions now the predicates' own, the plants on the rebuild bank and its rows
    ('G-RUNNER-READ', 'N1, b721`s rebuild as banked (no rebuild this act): one run per wave 1 kernel, six, each read once with its build exit; the head`s figures equal to its rows; the one sorry printed by its axiom line and graded builds and is not complete; SIDE-frobenius`s refused dispatch, its halt with its control, and its push run on the author`s two lines',
     lambda S: runner_ok(S), lambda S: put(S, 'rebuild', (S['rebuild'] or '').replace('builds and is not complete', 'builds'))),
    ('G-RUNNER-GATE', 'N1, N4: b721`s rebuild`s order and hold as banked -- free memory at or above 2,560 MB at every push, dispatch and read; per kernel push before run before read; b721`s cap, the refused one apart; this act`s capture running no rebuild route and no dispatch',
     lambda S: gate_ok(S), lambda S: put(S, 'rebuild_rows', [dict(r, free_mb=100) for r in (S['rebuild_rows'] or [])])),
    ('G-MERGES-ON-GATE', 'no kernel merge and no tag this act: each wave 1 kernel`s rebuild-b721, kept, at its pin (the tagged commit, its one tag) or, SIDE-frobenius alone, two commits beyond it by b721`s neutral identity, off main and untagged, each equal to its remote; SIDE-explicit-formula`s main at badaccc and v0.37 unmoved; SIDE-lv-conservation`s main, deposit, port-b707 and v0.14.0 unmoved; the join kernel`s main and its one tag v0.1.0',
     # ### Component 8, the Edit tool: the plant a tag at SIDE-frobenius's rebuild tip (the carried plant moved ef_log, which the repaired
     # ### predicate no longer reads, and passed -- the probe's POS PASS)
     lambda S: merges_ok(S), lambda S: put(S, 'rebuild_state', dict(S['rebuild_state'], **{'SIDE-frobenius': dict(S['rebuild_state']['SIDE-frobenius'], tip_tags=['v0.0.0-plant'])}))),
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
    ('G-PP-SCOPE', 'PLACE-papers` changed files on main against the two ledgers and INSTRUMENTS.md alone ((R332)(6)); no rename (N5)',
     # ### the plant a file outside the act's allowed set (b721's planted day1/ONE_PAGE_PROOF.md, which (R332)(6) allows this act, left the arm
     # ### passing on the mutated copy and the seal refused on it; repaired after the lock and before the seal, events (5))
     lambda S: corpus_scope_ok(S), lambda S: put(S, 'pp_changed', S['pp_changed'] + ['README.md'])),
    ('G-CURRENTS-UNEDITED', 'the map, the census, the monograph, the Dirichlet page, the surround, SIMPLICITY, FOUNDATIONS, INSTRUMENTS, PATHS, the substrate pages, the companions, the README, the faces page, REGISTRY and the archives, each at its file of record: working tree, before and HEAD',
     lambda S: unedited_all(S), lambda S: put(S, 'currents', dict(S['currents'], **{'ERRATA.md': (b'x', b'y', b'y')}))),
    ('G-KERNELS-UNTOUCHED', 'every kernel`s main, tags, branches and tracked status against the face read before the seal (SIDE-lv-conservation read with port-b707 at b712`s commit, its tag v0.14.0 the act`s one tier-one move, and its checkout at main; SIDE-faces-join at its re-pinned main and tag)',
     lambda S: kernels_untouched(S), lambda S: put(S, 'kern_now', {})),
    ('G-INSTRUMENTS-UNEDITED', 'b721`s to b695`s sealed tools and the earlier tools, the readers, the push tool, the act-root tool, the generators` tests, the corrigendum tools, edit_route.py, chain_page.py, the figures tools, b704`s read arm, e0_rule.py, the shared tools and b721`s report tool: before, working tree and HEAD',
     lambda S: instruments_ok(S), lambda S: put(S, 'inst', dict(S['inst'], **{'additive_shared.py': (b'a', b'b', b'b')}))),
    ('G-SHARED-ADDITIVE', 'tools/additive_shared.py over the shared data files', lambda S: bool(S['additive']) and all(rc == [] for _p, _h, rc in S['additive']),
     lambda S: put(S, 'additive', [('data/glossary.txt', 'x', [('changed', [])])])),
    ('G-PRIORBANK-UNCHANGED', 'every relay data bank tracked at the act`s base 248c5a97 but the shared additive files (act_roots.txt and the corrigenda bank among them) and the table`s files, by blob id',
     lambda S: S['prior_bad'] == [] and S['prior_n'] > 0, lambda S: put(S, 'prior_bad', ['data/b721_stepzero.txt'])),
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
    ('G-SEALED-AFTER-COMPONENTS', 'the lock time against every relay and PLACE-papers commit of the act by its row in the act`s step bank, data/b722_steps.json ((R332)(2); not by its subject)', lambda S: sealed_after_ok(S),
     lambda S: put(S, 'plog', S['plog'] + [('deadbee', 'b722 record', 1)])),
    ('G-NOTHING-RAN-AHEAD', 'section (0) and the logs before the lock: every commit before it declared by its hash, the gate`s commit read from the step bank`s one `gate` row ((R331)(3)(ii))',
     lambda S: nothing_ahead_ok(S['face'], S['lock_epoch'], S['rlog'] + S['plog'], S['steps'],
                                (gs(ROOT, 'log', '--diff-filter=A', '--format=%H', '--', 'data/' + os.path.basename(FACE)).split() or [''])[-1]),
     lambda S: put(S, 'rlog', S['rlog'] + [('deadbeef', 'x', 1)])),
    ('G-LOCKGATE-EIGHT', 'the lock gate`s verdict line', lambda S: 'GATES READ : 8. ### PASSING : 8.' in S['lock'] and 'VERDICT : LOCK PERMITTED' in S['lock'],
     lambda S: put(S, 'lock', S['lock'].replace('PASSING : 8.', 'PASSING : 7.'))),
    ('G-SEAL-VERIFIES', 'reg_seal --verify', lambda S: any('SEAL INTACT' in l for l in S['seal'].split(NL)), lambda S: put(S, 'seal', '')),
    ('G-SEAL-HASHES', 'the seal bank against the sealed tools now', lambda S: seal_hashes_ok(S),
     lambda S: put(S, 'sealnow', dict(S['sealnow'], **{'b722_closing.py': 'x'}))),
    ('G-ARMS-PRERUN', 'the pre-run bank: every arm run at HEAD before the lock, its count printed (R202)(3), in seven parts summed',
     lambda S: S['lock_epoch'] is not None and re.search(r'ARMS RUN : %d\.' % len(ARMS), S['prerun']) is not None and 'PRE-SEAL (R202)(3)' in S['prerun'],
     lambda S: put(S, 'prerun', '')),
    # ### b721's trail head as OPEN_TRAILS :16044 carries it (counted once on OPEN_TRAILS by the Grep tool's count mode at Component 6); the
    # ### carried literal named b714's head ("act one hundred and forty-one, the keystone heads act") under b721's ruling, a head no act wrote
    # ### b722's carry kept b718's head ("act one hundred and forty-five, the derivation act"); b721's own head at OPEN_TRAILS :16172 set here
    # ### by the Edit tool after the lock, before the seal (the pre-run's standing-a part, events (1))
    ('G-PRIOR-CLOSED-PUSHED', 'b721`s trail record on OPEN_TRAILS (:16264) and its root in the chain', lambda S: '### b721 — lane two, act one hundred and forty-eight, the table act under (R331)' in S['ot']
     and S['rootsf'].count(NL + PREV_ACT + ' ') == 1, lambda S: put(S, 'ot', S['ot'].replace('### b721 — lane two', '### b721 - lane two'))),
    ('G-TABLE-FINAL', 'the final table bank', lambda S: table_final_ok(S), lambda S: put(S, 'tfj', dict(S['tfj'], grade_moved=[['x', 'y']]))),
    ('G-ACTROOT-BANKED', 'data/act_roots.txt`s chain row for the act at the row act_figures reads (the corrigendum row apart), the root bank and its items against the root route`s own item list (ROOT_EXCLUDE per data/b706_rules.txt row (1), the required list read against it at import), the repairs, the corrigendum, the closure, the scan, the replay, the coverage, the controls, the hook, the roster, the pins, the chain rows, the census diff and the report among them, no bank the route excludes',
     lambda S: root_banked_ok(S), lambda S: put(S, 'rootsf', S['rootsf'] + ACT_NOW + ' x y' + NL)),
    ('G-ROOT-BANKS-COMMITTED', 'the root route`s banked reading and every named bank`s blob at the root`s recorded commit: clean and equal at HEAD, HEAD the remote main, the recorded hash carried by the recorded commit',
     lambda S: root_banks_committed_ok(S), lambda S: put(S, 'rootbanks', dict(S['rootbanks'], pushed=False))),
    ('G-ACTROOT-LAST', 'every bank the root names, its write time against the root`s', lambda S: root_last_ok(S),
     lambda S: put(S, 'bank_mtimes', dict(S['bank_mtimes'], **{'data/x': 10 ** 12}))),
    ('G-ACTROOT-VERIFY', 'the chain recomputed at commit in three parts by act with the suite`s own remote reads: standing-b2a`s banked b624-b641, standing-b2b`s b642-b658 and standing-b3`s b659-b722 all AGREE, the boundary link equal, b680 read through its corrigendum row (4 banks), b722 written LF',
     lambda S: verify_ok(S), lambda S: put(S, 'ar_verify', (S['ar_verify'] or [])[:-1])),
    ('G-FINDINGS-ENTRY', 'FINDINGS at the findings bank`s line, its title the record tool`s through conv, and its parts, the corrigendum, the standing toolset, the replay, the class repairs, the roster, the pins census and the census rows among them', lambda S: finding_ok(S),
     lambda S: put(S, 'fj', dict(S['fj'], entry_line=1))),
    ('G-TRAIL-RECORD', 'OPEN_TRAILS from the trail bank`s line, the head through conv', lambda S: bool(S['tj'].get('line'))
     and oline(S, S['tj']['line']) == conv(S['REC'].TRAIL_HEAD()), lambda S: put(S, 'tj', dict(S['tj'], line=1))),
    ('G-TRAIL-CARRIES-ROOT', 'the trail record and the root bank', lambda S: bool(S['arj'].get('root')) and ('b722 `%s`' % S['arj'].get('root')) in trail_tail(S),
     lambda S: put(S, 'arj', dict(S['arj'], root='0' * 64))),
    ('G-TRAIL-CARRIES-SEAL', 'the trail record`s sealed-tools line', lambda S: all(('%s agree' % t) in trail_tail(S) for t in K.SEALED),
     lambda S: put(S, 'ot', S['ot'].replace('b722_record.py agree', 'b722_record.py differ'))),
    ('G-NEXT-ACT-NAMED', 'the trail record`s next line naming the next act as act_figures reads it (v5 (ii); b721`s needle named its own act)',
     lambda S: ('**Next:** %s' % NEXT_ACT) in trail_tail(S),
     lambda S: put(S, 'ot', S['ot'].replace('**Next:** %s' % NEXT_ACT, '**Next:** %s' % ACT_NOW))),
] + [('G-N%d-SCORED' % i, 'the scores through the record tool`s reader, and the desk', (lambda k: lambda S: scored(S, k))('N%d' % i),
      lambda S: put(S, 'desk', '')) for i in range(1, 6)] + [
    ('G-SEAT-EXPECTATIONS-SCORED', 'the scores and the desk', lambda S: all(scored(S, k) for k in ('S1', 'S2', 'S3')), lambda S: put(S, 'desk', '')),
    ('G-WRITELIST-KINDS', 'every tracked file written since 248c5a97 and c02f47c1 against the (W) globs, the list admitting the next act`s rules file by form',
     lambda S: wl_ok(S), lambda S: put(S, 'written', S['written'] + ['relay/tools/x.py'])),
    ('G-ARMS-DECLARED-EQ-RUN', 'the (G2) block against this suite`s arm list', lambda S: S['declared_eq_run'], lambda S: put(S, 'declared_eq_run', False)),
    ('G-ARMS-NO-LIVE-LIMB', 'the harness`s own positive-control results', lambda S: S.get('no_live_limb', True), lambda S: put(S, 'no_live_limb', False)),
    ('G-MUSTFAIL', 'a file that must not exist', lambda S: S['mustfail'], lambda S: put(S, 'mustfail', False)),
    ('G-ARTEFACTS-NOT-COMMITTED', 'relay`s tracked files', lambda S: S['artefacts'] == '', lambda S: put(S, 'artefacts', 'data/anthropic-zeta23/x')),
    ('G-PUSHED-PREDICATE-THREE-CLAUSED', 'this suite`s own text', lambda S: ("gs(ROOT, 'rev-parse', 'origin/main') == gs(ROOT, 'rev-parse', 'HEAD')" in S['suite']
                                                                            and ".startswith(ACT_NOW)" in S['suite'] and "'data/%s_components.txt' % ACT_NOW in" in S['suite']),
     lambda S: put(S, 'suite', '')),
    ('G-CLOSING-SENTENCE', 'tools/b722_closing.py: the closing sentence in the rule`s words with the plain reads named; the citation check, the record lines, the dry run, the corrigendum, the derivation, the controls` ripe work, the two reads, the toolset at v1.2.0, the federation pin, the records, the touch read, the standing arms, the kernels, the author`s word from its bank, the mirror, the carry`s diffs',
     lambda S: closing_sentence_ok(S), lambda S: put(S, 'closing_src', S['closing_src'].replace('no identifier of the author ' + 'in any outbound', 'x'))),
    ('G-LSREMOTE-ONE-PER-REPO', 'the part`s ls-remote calls per repository, read after every other arm of the part has run (OPEN_TRAILS :12703)',
     lambda S: lsr_ok(S), lambda S: put(S, 'lsr', {PP: 2})),
    ('G-CORRESPONDENCE-CURRENCY', 'every roster paper`s Correspondence rows by tools/b706_standing_figures.py (b703`s reading over b706`s roster at the unversioned names) against the kernel`s current tag and the statement at the cited tag: the changed-statement rows no more than b721`s figure',
     lambda S: fig_ok(S, 'correspondence'), lambda S: _raise_fig(S, 'correspondence')),
    ('G-README-CURRENCY', 'the PLACE-papers README`s currency rows against ls-remote by tools/b705_standing_figures.py through b706`s (the dated appends and the deposited versions excluded by their text): the stale lines no more than b721`s figure',
     lambda S: fig_ok(S, 'readme'), lambda S: _raise_fig(S, 'readme')),
    ('G-PARTNER-COPIES', 'the lines differing between the two copies of each roster paper`s Correspondence table by tools/b706_standing_figures.py: one copy per table from b706 on, the figure 0, no more than b721`s 0',
     lambda S: fig_ok(S, 'partners'), lambda S: _raise_fig(S, 'partners')),
    ('G-SISTER-PINS', 'each kernel`s lean-toolchain and Mathlib revision beside the federation`s by tools/b703_standing_figures.py through b706`s: no kernel the faces page names moved pin against the baseline',
     lambda S: sister_pins_ok(S), lambda S: _raise_fig(S, 'pins')),
    ('G-READ-RULE-STANDING', 'tools/b704_read_arm.py over the read bank at HEAD (the author`s word at b704`s sort; from b705 every call counts): no Read call of a file of two hundred lines or more without an offset, without a limit or with a limit above two hundred',
     lambda S: read_rule_standing_ok(S), lambda S: _read_plant(S)),
] + [(nm, 'tools/rule_arms.py (the author`s word on (R293)(6); (R301)(6) for four; G-RULE-SUITE-PARTS as repaired under (R302)(2) and (R332)(2); G-RULE-BINARY-HASHES as repaired under (R306)(2); G-RULE-RECUT-QUOTE`s sources as repaired under (R313)(2)) -- ' + reads,
      (lambda p: lambda S: p(S['ra']))(pred), (lambda pl: lambda S: put(S, 'ra', pl(S['ra'])))(plant)) for nm, reads, pred, plant in RA.ARMS]
# ### (R332)(10): the run list -- the whole list less tools/standing/arms.py RETIRED; every part, the (G2) block, the seal and the tallies read
# ### ARMS; G-ARM-TAGS reads the whole list (the retired keep their tags)
ARMS = STA.run_list(ARMS_ALL)


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
    """(R332)(2)(iii): each arm's verdict on b721's banks beside b721's own (b721's post-push combine, data/b721_exercise.json `exercise`, its
    `live` per arm): PASS ON PREV; FAILED AS b721 FAILED it; DIVERGE where b721 passed it and it fails here; NOT RUN BY b721 where b721 has no
    row and it fails here (an arm new at b722 that cannot read b721's banks)."""
    own = C3.jl('b721_exercise.json').get('exercise') or {}
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


# ### (R332)(4)(ii): the withheld field read from the ruling (data/act_current.json `withheld`, empty this act: G-RULE-LONG-PHASE-SPLIT sealed,
# ### its input repaired by (4)(i)), each entry withheld only while its condition holds (tools/standing/close.py withheld_entries)
WITHHELD = tuple(STC.withheld_entries(C3.jl('act_current.json').get('withheld') or []))


def neg_shown():
    """(R332)(2)(iv), standing clauses v2 row (55): the suite refuses to seal an arm whose NEG control -- the mutated copy, the POS column of a
    part's table (its planted source; the arm must FAIL on it) -- has not been shown to fail, read from the pre-run's exercise banks
    (data/b722_exercise_<part>.json, `mode` prerun, every part's). (R332)(4)(vi): by tools/standing/close.py neg_shown, its three lists read
    by name (shown, bad, withheld), the withheld entries those of the ruling's field whose condition holds."""
    banks = dict((p, C3.jl('b722_exercise_%s.json' % p)) for p in K.PARTS)
    r = STC.neg_shown([(a[0], _part_of(a[0])) for a in ARMS], banks, list(WITHHELD))
    return r.shown, r.bad, r.withheld


def prev_run_missing():
    """(R332)(2)(iii): the parts carrying arms whose run on b721's banks is not banked (data/b722_prevrun_exercise_<part>.json, `mode` prev)."""
    return [p for p in sorted(set(_part_of(a[0]) for a in ARMS)) if C3.jl('b722_prevrun_exercise_%s.json' % p).get('mode') != 'prev']


def seal():
    face = read(FACE)
    lock = utc_epoch(face, 'locked at (UTC)')
    p = os.path.join(D, 'b722_seal_hashes.json')
    if lock is None:
        print('### THE FACE IS NOT LOCKED -- NOTHING RECORDED')
        return 3
    if os.path.exists(p):
        print('### THE HASHES ARE RECORDED ALREADY -- NOTHING RECORDED TWICE')
        return 3
    shown, bad, withheld = neg_shown()
    missing = prev_run_missing()
    for n, why in withheld:
        print('  WITHHELD, NOT EXERCISABLE: %-46s %s' % (n, why))
    if bad or missing:
        print('### (R332)(2)(iv): %d OF %d ARMS WITHOUT THEIR NEG CONTROL SHOWN FAILING ON A MUTATED COPY IN THE PRE-RUN:' % (len(bad), len(ARMS)))
        for n, why in bad:
            print('  %-46s %s' % (n, why))
        print('### (R332)(2)(iii): THE PARTS WHOSE ARMS ARE NOT RUN ON b721`S BANKS BEFORE THE SEAL: %s' % (missing or 'NONE'))
        print('### ### **THE SEAL REFUSED -- NOTHING RECORDED.**')
        return 3
    dtext = rd('b722_defects.txt')
    now = sealed_now()
    # ### (R332)(2)(i): the letters entered before the seal, recorded with it -- the trail's lines and the three trail-equality arms read these
    j = dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), lock=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime(lock)), tools=now,
             relay_head=gs(ROOT, 'rev-parse', 'HEAD'), letters=REC0.letters_of(dtext), defects_sha256=hashlib.sha256(dtext.encode('utf-8')).hexdigest(),
             neg_shown=len(shown), withheld=[dict(arm=n, reason=why) for n, why in withheld], prev_run=dict((p_, dict((k_, len(v_)) for k_, v_ in C3.jl('b722_prevrun_exercise_%s.json' % p_).items()
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
    print('  the arms with their NEG control shown failing %d of %d ; withheld, not exercisable, %d (%s) ; the runs on b721`s banks %s' % (
        len(shown), len(ARMS), len(withheld), ', '.join(n for n, _w in withheld) or 'NONE', j['prev_run']))
    print('  written: b722_seal_hashes.json')
    return 0


def _base_name(pushed):
    if PREV:
        return 'b722_prevrun.txt'
    if PRERUN:
        return 'b722_arms_prerun.txt'
    if MID and len(sys.argv) > sys.argv.index('--mid') + 1:
        return sys.argv[sys.argv.index('--mid') + 1]
    if RERUN and len(sys.argv) > sys.argv.index('--rerun-postpush') + 1:
        return sys.argv[sys.argv.index('--rerun-postpush') + 1]
    return 'b722_checks_postpush.txt' if pushed else 'b722_checks.txt'


def _part_name(base, part):
    return base.replace('.txt', '_%s.txt' % part)


def _membrane(p):
    """(R332)(2)(ii), standing clauses v2 row (53): the membrane before every bank this suite writes (tools/act_membrane.py guard_path, this act's
    ROOT_EXCLUDE): the post-push parts' banks are excluded kinds (checks*, lsr*, exercise*, chain_*); the pre-run's, the run on b721's banks and
    the seal's record are root items, refused once the root is appended."""
    import act_membrane as MEM
    MEM.guard_path(ACT_NOW, p, REC0.R.ROOT_EXCLUDE)


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
    base = 'b722_arms_prerun.txt' if prerun else ('b722_checks_postpush.txt' if (rerun or pushed) else 'b722_checks.txt')
    out = [('data/' + _part_name(base, '<part>')), ('data/' + _part_name(base, '<part>').replace('b722_arms_prerun', 'b722_lsr_prerun').replace('b722_checks', 'b722_lsr').replace('.txt', '.json')),
           'data/b722_exercise_<part>.json']
    seconds = ['data/b722_arm_seconds_<part>.json'] if prerun else []
    return out, seconds


def guard_dry():
    for mode, args in (('prerun', (True, False, False, False)), ('pre-push', (False, False, False, False)), ('post-push', (False, True, False, True))):
        out, seconds = writer_plan(*args)
        print('  MODE %-9s | the part`s banks: %s | the per-part seconds bank: %s' % (mode, ', '.join(out), ', '.join(seconds) or 'NONE'))
    print('  ### POST-ROOT PATH WRITES NONE of the root-named per-part seconds banks: the pre-push and post-push modes write no data/b722_arm_seconds_<part>.json')
    return 0


def withheld_field():
    """the author's word (7): the arms in the seal record's withheld field (data/b722_seal_hashes.json `withheld`, written by seal()); before
    the seal, none. Every tally the suite writes after the seal reads it."""
    return [w.get('arm') for w in (C3.jl('b722_seal_hashes.json').get('withheld') or [])]


def _tally(EX, W):
    """the author's word (7): a part's figures from its exercise rows -- an arm in the withheld field W counted neither among the passes nor
    among the live failures (nor the controls' figures); every other arm as before. Returns (live failing, positive-control passes,
    negative-control failures, withheld)."""
    fail = [n for n, e in EX.items() if n not in W and not e['live']]
    defective = [n for n, e in EX.items() if n not in W and e['pos']]
    negfail = sum(1 for n, e in EX.items() if n not in W and e['neg'] != e['live'])
    return fail, defective, negfail, [n for n in EX if n in W]


ARM_ROW = re.compile(r'^  (G-[\w-]+)\s+(PASS|FAIL)\s+(PASS|FAIL)\s+(PASS|FAIL)\s+[\d.]+\s+(.*)$', re.M)


def _combine_tally(parts, W):
    """the author's word (7): the combine's figures summed from the parts' footers, an arm in the withheld field W taken out by its row -- a
    part written before the field (the pre-run's) counted it as it fell, so its row's LIVE, NEG and POS are taken off the sums; a part written
    after prints the row WITHHELD and its footer left it out. Returns (arms, passing, failing, neg failures, pos passes, failing names,
    pos-pass names, withheld names). By tools/standing/close.py combine_tally (the coverage table's [7], [17], [20]; replayed EQUAL)."""
    return STC.combine_tally(parts, W)


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
    n, lp, lf, ng, pc, fails, defs, wh = _combine_tally(parts, withheld_field())
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
        '  ### ### **ARMS RUN : %d. ### LIVE PASSING : %d. ### LIVE FAILING : %d %s. ### WITHHELD, NOT EXERCISABLE : %d %s.**' % (
            n, lp, lf, fails or '', len(wh), wh or ''),
        '  ### ### **NEGATIVE-CONTROL FAILURES : %d. ### POSITIVE-CONTROL PASSES : %d %s.**' % (ng, pc, defs or ''),
        '  ### ### **VERDICT : %s%s**' % ('ALL ARMS PASS AND EVERY CONTROL BEHAVES' if (ok and not fails) else
                                         'EVERY ARM PASSES BUT THE CARRIED FAILURE DECLARED ON THE FACE, AND EVERY CONTROL BEHAVES' if ok else 'NOT CLEAN',
                                         ' ; WITHHELD, NOT EXERCISABLE, COUNTED NEITHER PASSING NOR FAILING: %s' % ', '.join(wh) if wh else ''),
        '=' * 104, '']
    for p, _m, t in parts:
        out += ['### THE PART BANK %s, WHOLE:' % _part_name(base, p)] + t.rstrip(NL).split(NL) + ['']
    _write(base, out)
    ex = {}
    for part in K.PARTS:
        ex.update(jl('b722_exercise_%s.json' % part).get('exercise') or {})
    if ex and base in ('b722_checks.txt', 'b722_checks_postpush.txt'):
        e = (json.dumps(dict(exercise=ex, run=n, live_failing=fails, defective=defs, neg_failures=ng, withheld=wh), indent=1, ensure_ascii=False) + NL).encode('utf-8')
        p_ = os.path.join(D, 'b722_exercise.json')
        _membrane(p_)
        with open(p_ + '.tmp', 'wb') as fh:
            fh.write(e)
        os.replace(p_ + '.tmp', p_)
    print(NL.join(out[3:16]))
    print('  written: %s' % base)
    return 0 if ok else 1


# ### the carried failures declared on the face by name (section (0)), read off the mid-act run before the face is written. b722's one:
# ### G-DELETES-ONE-BRANCH, wanting port-b707 among the ruling's kept branches as tools/standing/allow.py reads them (a clause saying NOT
# ### deleted) where the ferry's Component 0 says "port-b707 kept" (data/b722_ferry.txt :26) -- the ruling's wording and the carried reader in
# ### conflict, as at b721, printed for the author; the arm not edited. b721's G-BRANCHES-BANKED is not carried: b722's step-zero bank stands
# ### in its step-zero banks' commit (e3b3de12). And G-DELETE-FREE, the standing arm over the act's tools' code, on tools/b722_challenge.py's
# ### os.remove of its own temporary index (:148, :155) -- defect (m), the tool committed as it ran (41a0adcf), not edited after; the arm not edited.
CARRIED_FAILING = ('G-DELETES-ONE-BRANCH', 'G-DELETE-FREE')


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
    rec('b722 -- THE SUITE. ### **%s READING.** ### PART %s ### every arm exercised on both controls.' % (
        'ON b721`S BANKS ((R332)(2)(iii))' if PREV else 'PRE-SEAL (R202)(3)' if PRERUN else 'MID-ACT' if MID else 'POST-PUSH' if pushed else 'PRE-PUSH', PART))
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
    rec('  ### (R264)(2) THE FREEZE: the standing arms (b721`s face less its own arms and the arms (R332)(10) retired; none added) %d ; '
        'carried here %d ; the act`s arms over its own banks %s ; arms beyond both %s' % (
            len(S['standing']), len(set(names) & set(S['standing'])), sorted(set(names) - set(S['standing'])),
            sorted(set(names) - set(S['standing']) - set(K.ACT_ARMS)) or 'NONE'))
    rec('  ### standing arms not carried here: %s' % (sorted(set(S['standing']) - set(names)) or 'NONE'))
    if 'figures' in NEED[PART]:
        rec('  ### THE FOUR STANDING FIGURES, each against the previous act`s (%s):' % S['fig_prev_name'])
        for k in ('correspondence', 'readme', 'partners', 'pins'):
            rec('  ###   %-15s live %s ; previous %s' % (k, (S['fig'].get(k) or {}).get('figure'), (S['fig_prev'].get(k) or {}).get('figure')))
        ok_, n_, off_, pre_, form_ = RDA.reading_text(S['reads_bank'])
        rec('  ### G-READ-RULE-STANDING`S READING (relay data/b722_read_calls.txt): %s ; rows %d ; offences %d %s ; the cap`s precursors %d' % (
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
            rec('  ### the reads at commit, b680: %s ; %s: %s' % (S['ar_reads'].get('b680'), ACT_NOW, S['ar_reads'].get(ACT_NOW)))
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
    rec('  ### PLACE-papers` changed files on main %d against the allowed %d (FINDINGS, OPEN_TRAILS and INSTRUMENTS.md): beyond %s' % (
        len(S['pp_changed']), len(S['pp_allowed']), sorted(set(S['pp_changed']) - set(S['pp_allowed'])) or 'NONE'))
    rec('  ### SIDE-explicit-formula: main %s ; v0.37 %s (unmoved) ; SIDE-lv-conservation main %s, v0.10.0 %s, port-b707 %s (b721`s tip, kept, no commit this act) ; the join kernel main %s ; runner dispatches this act %d (N1: none; (R332)(10) reads b721`s runs by their ids; -1 the command bank not yet written)' % (
        S['ef_main'][:12], (S['ef_tags'].get('v0.37') or '')[:12], S['lv_main'][:12], (S['lv_v0100'] or '-')[:12], (S['lv_port'] or '-')[:12],
        (S['join_main'] or '-')[:12], len(S['cmdj'].get('dispatches') or []) if S['cmdj'] else -1))
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
    W = withheld_field()
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
        pos_raised = None   # ### (R332)(2)(iv): a plant or a predicate that raised on the mutated copy has not SHOWN the control failing
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
                                                 'WITHHELD, NOT EXERCISABLE' if name in W else
                                                 'OK' if (live and neg and not posv) else ('### POS PASSES -- DEFECTIVE' if posv else
                                                                                           '### FAILS -- THE CARRIED FAILURE DECLARED ON THE FACE' if name in CARRIED_FAILING else '### FAILS')))
    if not arms:
        rec('  (no arm in this part)')
    fail, defective, negfail, wh = _tally(EX, W)
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
        rec('  ### (R332)(2)(iii) THE ARMS ON b721`S BANKS, beside b721`s own verdicts (relay data/b721_exercise.json, b721`s post-push combine):')
        for k_ in ('pass_on_prev', 'fail_as_prev', 'diverge', 'not_run_by_prev'):
            rec('  ###   %-16s %d %s' % (k_.upper(), len(pv[k_]), pv[k_] or ''))
        rec('  ### ### **ON b721`S BANKS: PASS %d ; FAILED AS b721 FAILED %d ; DIVERGE %d (b721 passed, here failed) ; NOT RUN BY b721 %d (here failed).**' % (
            len(pv['pass_on_prev']), len(pv['fail_as_prev']), len(pv['diverge']), len(pv['not_run_by_prev'])))
    secs = time.time() - t_start
    rec('  ### the arms` own seconds summed %.1f, the slowest %s' % (sum(SECS.values()), ', '.join('%s %.2f' % kv for kv in sorted(SECS.items(), key=lambda x: -x[1])[:3]) or 'NONE'))
    rec('  ### the run took %.0f s' % secs)
    rec('  ### PART %s : ARMS %d ; LIVE PASSING %d ; LIVE FAILING %d %s ; NEGATIVE-CONTROL FAILURES %d ; POSITIVE-CONTROL PASSES %d %s ; '
        'DECLARED EQ RUN %s ; %d s ; WITHHELD, NOT EXERCISABLE %d %s' % (PART, len(arms), len(arms) - len(fail) - len(wh), len(fail), json.dumps(fail) if fail else 'NONE',
                                                                      negfail, len(defective), json.dumps(defective) if defective else 'NONE', S['declared_eq_run'],
                                                                      int(secs), len(wh), json.dumps(wh) if wh else 'NONE'))
    rec('=' * 104)
    out = _write(_part_name(base, PART), L)
    lp = os.path.join(D, _part_name(base, PART).replace('b722_arms_prerun', 'b722_lsr_prerun').replace('b722_checks', 'b722_lsr').replace('.txt', '.json'))
    lb = (json.dumps(dict(run=os.path.basename(out), lsr=lsr), indent=1, ensure_ascii=False) + NL).encode('utf-8')
    _membrane(lp)
    with open(lp + '.tmp', 'wb') as fh:
        fh.write(lb)
    os.replace(lp + '.tmp', lp)
    ex = dict(exercise=EX, run=len(arms), live_failing=fail, defective=defective, neg_failures=negfail, withheld=wh, part=PART,
              mode='prev' if PREV else 'prerun' if PRERUN else 'mid' if MID else 'post-push' if pushed else 'pre-push',
              at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), relay_head=gs(ROOT, 'rev-parse', 'HEAD'))
    ex.update(pv)
    ep = os.path.join(D, ('b722_prevrun_exercise_%s.json' if PREV else 'b722_exercise_%s.json') % PART)
    _membrane(ep)
    with open(ep + '.tmp', 'wb') as fh:
        fh.write((json.dumps(ex, indent=1, ensure_ascii=False) + NL).encode('utf-8'))
    os.replace(ep + '.tmp', ep)
    # ### THE GUARD HELD -- the per-part seconds bank (root-named, gathered by the record tool's armsecs before the seal) is written by the pre-run
    # ### alone, as tools/b700_checks.py :1669 had it and b702 restored; the pre-push and post-push runs write no root-named bank
    if PRERUN:
        sp = os.path.join(D, 'b722_arm_seconds_%s.json' % PART)
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
    """(R332)(2)(iii): the worklist a run on b721's banks reads -- b721's value for every name b721's worklist carries, this act's for the suite's
    own structure (the arms by part, the parts, the hold, the chain's halves) and for a name b721's lacks. The components' commits are this
    act's too: b721's worklist reuses the names in other shapes (its C5_RELAY a pair, its C6_RELAY one commit), and only the act's own arms
    read them (sources, the ancestry pairs, the times and the files) -- found after the lock, before the seal, by the first `--prev` run's
    crash in sources (a tuple handed to git merge-base); an event of the seat's, not a letter."""
    OWN = ('ACT_ARMS', 'PARTS', 'HOLD', 'CHAIN_HALVES', 'CHAIN_QUARTERS', 'STANDING_ADDED',
           'C1_RELAY', 'C1_PP', 'C2_REG', 'C2_PRED', 'C2_CTL', 'C2_RELAY', 'C3_RELAY', 'C4_REG', 'C4_RELAY', 'C5_REG', 'C5_RELAY', 'C6_RELAY')

    def __init__(self, own, prev):
        self._own, self._prev = own, prev

    def __getattr__(self, n):
        if n not in self.OWN and hasattr(self._prev, n):
            return getattr(self._prev, n)
        return getattr(self._own, n)


_JL_OWN = None   # defect (j): the chain halves are this run's own banks, read past the rebinding


def _prev_rebind():
    """(R332)(2)(iii), `--prev`: every bank the arms read through rd and jl under this act's prefix read as b721's (data/b722_<x> as
    data/b721_<x>), the face b721's, the worklist through _PrevWorklist, the pre-act heads b721's. The tools stay this act's; the banks alone are
    the previous act's. An arm whose source the rebinding does not reach (a literal path, a b722-only bank) reads this act's and is printed as it
    falls, beside b721's own verdict."""
    global rd, jl, FACE, K, PRE, _JL_OWN

    def pv(n):
        return ('b721_' + n[5:]) if isinstance(n, str) and n.startswith('b722_') else n

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
