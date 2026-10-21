# -*- coding: utf-8 -*-
"""b701_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b701's step zero, run before any other step
((R311)(6)); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT AUTHOR ANSWER
before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (e5bcf1d0, a new session after the author's /clear); the answer route is b682's, imported from tools/b682_citation.py with its act names
### pointed at b701 and its commit reach widened to the kernels as b699 and b700 widened it; the `word` route is b694's.
### Routes: `check` -> data/b701_citation_check.txt (.json) ; `ferry` -> data/b701_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the
###         check on one answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b701 from b700_citation.py's form; this tool writes only the banks named above.
"""
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
import b677_citation as C   # noqa: E402  ### the helpers, imported unchanged
import b701_worklist as K   # noqa: E402

C.SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID


def continuation_sessions():
    """the act's continuation sessions (K.SESSIONS_AFTER, b671's form) as transcript paths, read by b677's helpers after the seat's session."""
    return tuple('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid for sid, _anc in K.SESSIONS_AFTER)


C.SESSIONS_AFTER = continuation_sessions()
NL = chr(10)
PP = C.PP
C.ANCHOR, C.TAIL = K.ANCHOR, K.TAIL
ANCHOR, TAIL = C.ANCHOR, C.TAIL
g, rd, line, commit_in, subject, branch_listed, rule_clause = (C.g, C.rd, C.line, C.commit_in, C.subject, C.branch_listed, C.rule_clause)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

HEAD_QUOTE = 'b700 closed: relay ac29fa81, PLACE-papers 71b23ac; suite 118 of 119; root 6f32698e1c7c0d9e\u2026; 2 prompts answered; 2 defects'


def act_root_line(act):
    t = rd(os.path.join(D, 'act_roots.txt')) or ''
    return [l.split() for l in t.split(NL) if l.strip() and l.split()[0] == act]


def lines_of(path):
    return (rd(path) or '').split(NL)


def first(L, needle):
    return next((i + 1 for i, l in enumerate(L) if needle in l), 0)


def at(L, n):
    return L[n - 1] if n and len(L) >= n else ''


def _ws(s):
    return ''.join((s or '').split())


def _show(repo, rev, path):
    return (g(repo, 'show', '%s:%s' % (rev, path))[1] or '').replace(chr(13), '')


def _reg_cols(L, prefix):
    """the regularity bank's rows (U1..U17 or P1..P17): [(id, W1, W2, W3)] read from the last three ` | ` fields of each row."""
    out = []
    for l in L:
        m = re.match(r'^  (%s\d+)\s' % prefix, l)
        if m:
            f = [x.strip() for x in l.split(' | ')]
            out.append((m.group(1), f[-3], f[-2], f[-1]))
    return out


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    FI = os.path.join(PP, 'FINDINGS.md')
    ot, fi = lines_of(OT), lines_of(FI)
    EF, LV = K.EF_DIR, K.LV_DIR
    # ### the ferry's read-first list
    for f in ('data/b700_closing.txt', 'data/b700_defects.txt', 'data/b700_reading4.txt', 'data/b700_slate.txt', 'data/b699_bridge_plan.txt',
              'data/b698_correspondence_dominance.txt', 'data/b698_regularity_uses.txt', 'tools/circuit_correspondence.py', 'data/b690_nodes_zeta.txt',
              'data/glossary.txt', 'data/b685_count.txt', 'data/b687_steps.txt', 'data/b687_p3_status.txt', 'tools/b326_windows.py', 'data/b689_plan.txt',
              'data/b700_closing_push_out.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    cl = lines_of(p('data', 'b700_closing.txt'))
    add('ferry read-first; ruling (1)', 'data/b700_closing.txt :1, the head line, against (R311)(1)`s quote after whitespace is removed', _ws(cl[0]) == _ws(HEAD_QUOTE),
        'data/b700_closing.txt :1 = %r' % cl[0][:100], '0-1')
    df = lines_of(p('data', 'b700_defects.txt'))
    lt = re.findall(r"^    \(([a-z])\) ", NL.join(df), re.M)
    add('ferry read-first', 'data/b700_defects.txt (rows are defects as lettered)', lt == list('ab'), 'letters %s, the seat`s both' % ''.join(lt), '0-1')
    r4 = lines_of(p('data', 'b700_reading4.txt'))
    added = [first(r4, nd) for nd in ('### (a) THE DEFECTS BANKS b673 THROUGH b699, BY CLASS', '### (b) THE ROSTER-CURRENCY ROWS', '### (c) THE', '### (d) THE CIRCUIT INSTRUMENT', '### (e) THE REGULARITY BANK')]
    add('ferry read-first', 'data/b700_reading4.txt (rows are readings; the five added sections by line)', at(r4, 3).startswith('### rows are readings') and all(added),
        'data/b700_reading4.txt :3 (the unit) ; the five added sections at %s' % ', '.join(':%d' % x for x in added), '0-1')
    sl = lines_of(p('data', 'b700_slate.txt'))
    add('ferry read-first', 'data/b700_slate.txt', first(sl, 'SLATE FOR b701: W-ORD-H2-BRIDGE-THEOREM 1 DISPATCH') > 0,
        'data/b700_slate.txt :%d (the verdict line)' % first(sl, 'SLATE FOR b701: W-ORD-H2-BRIDGE-THEOREM 1 DISPATCH'), '0-3')
    pl = lines_of(p('data', 'b699_bridge_plan.txt'))
    add('ferry read-first; ruling (2)', 'data/b699_bridge_plan.txt :67 (S1), :85 (the price); rows are binders', at(pl, 67).startswith('  S1  theorem') and 'PRICE: 1 dispatch' in at(pl, 85)
        and at(pl, 22).startswith('== 1. THE BINDERS'), 'data/b699_bridge_plan.txt :22 (the binders), :67 (S1), :85 (the price)', '0-2')
    cd = lines_of(p('data', 'b698_correspondence_dominance.txt'))
    b1 = first(cd, '  binder 1   | h2_sign: (k : ℝ → ℂ)')
    add('ferry read-first', 'data/b698_correspondence_dominance.txt (binder 1 by line)', b1 > 0 and 'DIFFERS' in at(cd, b1 + 2),
        'data/b698_correspondence_dominance.txt :%d-:%d (binder 1, DIFFERS)' % (b1, b1 + 2), '0-2')
    ru = lines_of(p('data', 'b698_regularity_uses.txt'))
    add('ferry read-first', 'data/b698_regularity_uses.txt :85-:86 (the W1 and W3 columns by row)', 'W1 DISCHARGED 11, RE-PROVED 6, OBSTRUCTED 0' in at(ru, 85)
        and 'W3 DISCHARGED 13, RE-PROVED 4, OBSTRUCTED 0' in at(ru, 85) and 'W1 DISCHARGED 13, RE-PROVED 4, OBSTRUCTED 0' in at(ru, 86)
        and 'W3 DISCHARGED 17, RE-PROVED 0, OBSTRUCTED 0' in at(ru, 86), 'data/b698_regularity_uses.txt :85 (uses), :86 (path)', '0-3')
    U, P = _reg_cols(ru, 'U'), _reg_cols(ru, 'P')
    nu = sum(1 for _i, w1, _w2, w3 in U if w1.startswith('RE-PROVED') or w3.startswith('RE-PROVED'))
    np_ = sum(1 for _i, w1, _w2, w3 in P if w1.startswith('RE-PROVED') or w3.startswith('RE-PROVED'))
    add('ruling (3)', 'the 10 uses and 4 path leaves RE-PROVED under W1 ∪ W3, by row', len(U) == 17 and len(P) == 17 and nu == 10 and np_ == 4,
        'data/b698_regularity_uses.txt rows U1-U17 (RE-PROVED in W1 or W3: %d), P1-P17 (%d)' % (nu, np_), '0-3')
    cc = rd(p('tools', 'circuit_correspondence.py')) or ''
    add('ferry read-first; ruling (2)', 'tools/circuit_correspondence.py (compare, from_signature, from_pi)', all(x in cc for x in ('def compare(', 'def from_signature(', 'def from_pi(')),
        'tools/circuit_correspondence.py :166 (compare), :134 (from_signature), :114 (from_pi)', '0-2')
    tt = lines_of(p('data', 'terminal_table.md'))
    h2r, lnr = first(tt, 'h2_sign_iff_rh'), first(tt, 'li_nonneg_iff_rh')
    ax = lines_of(p('data', 'b689_axioms_SIDE-explicit-formula_run1.txt'))
    add('ferry read-first', 'SIDE-explicit-formula`s v0.34 print bank: h2_sign_iff_rh and li_nonneg_iff_rh by row', h2r > 0 and lnr > 0 and first(ax, 'li_nonneg_iff_rh') > 0,
        'relay data/terminal_table.md :%d (h2_sign_iff_rh), :%d (li_nonneg_iff_rh) ; data/b689_axioms_SIDE-explicit-formula_run1.txt :%d (li_nonneg_iff_rh, the run at v0.34`s '
        'branch tip; h2_sign_iff_rh is not in print_targets.txt -- its print is the closure`s, data/b692_circuit_SIDE-explicit-formula_v0.34.1.txt)' % (h2r, lnr, first(ax, 'li_nonneg_iff_rh')), '0-2')
    h2 = lines_of(os.path.join(EF, 'SIDEExplicitFormula', 'H2Sign.lean'))
    add('ferry read-first', 'H2Sign.lean :22-:29 (classK :24-:26, h2_sign :29-:30)', at(h2, 24).startswith('def classK') and at(h2, 29).startswith('def h2_sign'),
        'SIDE-explicit-formula SIDEExplicitFormula/H2Sign.lean :24 (def classK), :29 (def h2_sign)', '0-3')
    rp = _show(LV, K.LV_V0130, 'SIDELvConservation/RegisterPentagon.lean').split(NL)
    add('ferry read-first; ruling (2)', 'SIDE-lv-conservation`s Register4_positivity at v0.13.0 by file and line', at(rp, 153).startswith('def Register4_positivity (lam : ℕ → ℝ) : Prop :=')
        and at(rp, 154).strip() == '∀ n : ℕ, 1 ≤ n → 0 ≤ lam n',
        'SIDE-lv-conservation v0.13.0 = %s SIDELvConservation/RegisterPentagon.lean :153-:154 (git show at the tag; b698 read the face at ZeroActingPartial.lean :111-:121, its '
        'binder 13 liCriterion : Register4_positivity lam → RiemannHypothesis)' % K.LV_V0130[:7], '0-2')
    rs = lines_of(os.path.join(EF, 'SIDEExplicitFormula', 'ResidueDischarge.lean'))
    add('ruling (2)', 'the restatement in the kernel`s own vocabulary: ResidueDischarge.Register4_positivity, its body lv`s', at(rs, 30).startswith('def Register4_positivity (lam : ℕ → ℝ) : Prop :=')
        and at(rs, 31).strip() == '∀ n : ℕ, 1 ≤ n → 0 ≤ lam n', 'SIDE-explicit-formula SIDEExplicitFormula/ResidueDischarge.lean :30-:31 (K3 of the plan)', '2')
    nz = lines_of(p('data', 'b690_nodes_zeta.txt'))
    add('ferry read-first; ruling (2)', 'data/b690_nodes_zeta.txt :126 (the lv-conservation Correspondence row)', at(nz, 126).startswith('@corr SIDE-lv-conservation | residue_irreducible |'),
        'data/b690_nodes_zeta.txt :126', '0-2')
    gl = lines_of(p('data', 'glossary.txt'))
    add('ferry read-first; ruling (3)', 'data/glossary.txt (the classK entry by line)', at(gl, 12).startswith('classK\t'), 'data/glossary.txt :12 (classK), :11 (h2_sign)', '0-3')
    add('ferry read-first', 'data/b685_count.txt (rows are T ranges after the constants)', 'rows are T ranges' in at(lines_of(p('data', 'b685_count.txt')), 3),
        'data/b685_count.txt :3 (the unit), :19-:25 (the constants)', '0-4')
    add('ferry read-first', 'data/b687_steps.txt (rows are steps with height, bound, computed value and margin)', 'rows are steps' in at(lines_of(p('data', 'b687_steps.txt')), 3),
        'data/b687_steps.txt :3 (the unit)', '0-4')
    ps = lines_of(p('data', 'b687_p3_status.txt'))
    add('ferry read-first', 'data/b687_p3_status.txt (rows are the premise with its readings)', 'rows are the premise' in at(ps, 4) and 'P3: DERIVED' in at(ps, 35),
        'data/b687_p3_status.txt :4 (the unit), :35 (the verdict)', '0-4')
    bw = lines_of(p('tools', 'b326_windows.py'))
    add('ferry read-first; ruling (4)', 'tools/b326_windows.py :220-:228 (kernel_q_derived, Z_Q`s bracket)', at(bw, 220).startswith('def kernel_q_derived') and 'math.sqrt(DISC)' in at(bw, 228),
        'tools/b326_windows.py :220 (def), :227-:228 (2 Re psi(1/2 + i u) - 2 log(2 pi / sqrt 23))', '0-4')
    bp = lines_of(p('data', 'b689_plan.txt'))
    add('ferry read-first; ruling (3)', 'data/b689_plan.txt (the form)', 'Rows are statements, uses, priced facts' in at(bp, 3) and first(bp, '== 8. THE RUNNER') > 0,
        'data/b689_plan.txt :3 (the unit), :%d (section 8, the runner form)' % first(bp, '== 8. THE RUNNER'), '0-3')
    po = rd(p('data', 'b700_closing_push_out.txt')) or ''
    poc = [l for l in (g(ROOT, 'log', '--format=%h', '--', 'data/b700_closing_push_out.txt')[1] or '').split(NL) if l.strip()]
    po_alone = len(poc) == 1 and [x for x in (g(ROOT, 'show', '--name-only', '--pretty=format:', poc[0])[1] or '').split(NL) if x.strip()] == ['data/b700_closing_push_out.txt']
    add('ferry read-first; ruling (5)', 'data/b700_closing_push_out.txt (commit at the start)', 'main read back at the remote: 5623191e' in po and (po_alone or not poc),
        'main read back at 5623191e ; %s' % (('committed alone at relay %s, the step`s first commit' % poc[0]) if poc else 'untracked at the working tree, to be committed alone'), '0')
    # ### (R311)(1)
    add('ruling (1)', 'the closing pushed and read back at relay main 5623191e', 'main read back at the remote: 5623191e' in po and commit_in(ROOT, '5623191e')
        and g(ROOT, 'merge-base', '--is-ancestor', '5623191e', 'HEAD')[0] == 0 and g(ROOT, 'rev-parse', '--short=8', K.PRE_RELAY)[1].strip() == '5623191e',
        'data/b700_closing_push_out.txt :5 ; relay 5623191e the main before this act (K.PRE_RELAY), an ancestor of HEAD %s' % g(ROOT, 'rev-parse', '--short=8', 'HEAD')[1].strip(), '1')
    rsm = rd(p('data', 'b700_resume.txt')) or ''
    add('ruling (1)', 'the resume: Components 0-3 done, 4 partial, 5 not started, no memory file damaged', 'COMPONENTS 0-3 DONE' in rsm and 'COMPONENT 4 PARTIAL' in rsm
        and 'COMPONENT 5 NOT STARTED' in rsm and 'MEMORY NONE DAMAGED' in rsm, 'data/b700_resume.txt (the verdict line)', '1')
    add('ruling (1)', 'the session repair in b671`s form at a7a85b41', commit_in(ROOT, 'a7a85b41') and 'session repair' in subject(ROOT, 'a7a85b41'),
        'relay a7a85b41: %s' % subject(ROOT, 'a7a85b41')[:90], '1')
    wl = rd(p('tools', 'b700_worklist.py')) or ''
    add('ruling (1)', 'the session named in the worklist`s SESSIONS_AFTER', "SESSIONS_AFTER = (('b858e03f-d343-4bf2-9bb6-16946a3c8a59', 'RESUME b700 after a host reboot'),)" in wl,
        'tools/b700_worklist.py :23', '1')
    tr = rd(p('data', 'b700_tool_repairs.txt')) or ''
    add('ruling (1)', 'repairs (7)-(9) at the carry', all(x in tr for x in ('(7) tools/b700_citation.py continuation_sessions', '(8) tools/b700_checks.py ra_sources', '(9) tools/b700_closing.py head_line')),
        'data/b700_tool_repairs.txt rows (7)-(9)', '1')
    add('ruling (1)', 'the corrigendum for b699 at FINDINGS :9752', at(fi, 9752).startswith('## Corrigendum to b699'), 'FINDINGS :9752', '1')
    add('ruling (1)', 'the record tool`s _defect_short with its act at the call, the dry run printing four from two named sources',
        'b699: DEFECTS 4 -- FROM data/b699_defects.txt 3, FROM THE CLOSING`S (g) LINE 1' in tr and 'def _defect_short(act):' in (rd(p('tools', 'b700_record.py')) or ''),
        'data/b700_tool_repairs.txt (the dry run) ; tools/b700_record.py :69', '1')
    add('ruling (1)', 'reading 4 with the b680 and b690 values beside and its five added readings', 'b690' in at(r4, 3) and 'b680' in at(r4, 3) and all(added),
        'data/b700_reading4.txt :3 ; the added sections at %s' % ', '.join(':%d' % x for x in added), '1')
    gate = rd(p('data', 'b700_reg_gate.txt')) or ''
    add('ruling (1)', 'the gate CLEAR with both dry runs CLEAN, the trail`s Defects line equal to the defects bank', 'GATE VERDICT : CLEAR' in gate and 'THE DRY-RUN STEP : CLEAN' in gate
        and 'THE CLOSING DRY-RUN STEP : CLEAN' in gate and 'THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK True' in gate, 'data/b700_reg_gate.txt', '1')
    lk = rd(p('data', 'b700_lockgate_notes.txt')) or ''
    add('ruling (1)', 'the lock gate 8 of 8', 'GATES READ : 8. ### PASSING : 8.' in lk and 'LOCK PERMITTED' in lk, 'data/b700_lockgate_notes.txt', '1')
    import hashlib as _hl
    sv = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'reg_seal.py'), '--verify', p(*K.B700_FACE.split('/'))], capture_output=True,
                        text=True, encoding='utf-8', errors='replace').stdout or ''
    add('ruling (1)', 'the face locked at ec20ccf2 (the face`s sha256 at the lock, recorded by the lock gate; the seal block appended after it)',
        'its sha256 : ec20ccf2' in lk and 'SEAL INTACT' in sv, 'data/b700_lockgate_notes.txt :13 (its sha256 : ec20ccf2...) ; reg_seal --verify: %s' % (
            ([l.strip() for l in sv.split(NL) if 'SEAL' in l] or ['### NO SEAL LINE'])[0][:80]), '1')
    for h, what in (('ecbbc502', 'ten tools` hashes'), ('a8c25b23', 'the gate`s banks committed before the lock')):
        add('ruling (1)', '%s at %s' % (what, h), commit_in(ROOT, h), 'relay %s: %s' % (h, subject(ROOT, h)[:90]), '1')
    face = rd(p(*K.B700_FACE.split('/'))) or ''
    add('ruling (1)', 'a8c25b23 named on the face', 'a8c25b23' in face, K.B700_FACE, '1')
    add('ruling (1)', 'the entry at FINDINGS :9768, the trail at OPEN_TRAILS :15370', at(fi, 9768).startswith('## Reading 4:') and at(ot, 15370).startswith('### b700'),
        'FINDINGS :9768 ; OPEN_TRAILS :15370', '1')
    ar = json.loads(rd(p('data', 'b700_act_root.json')) or '{}')
    named = [it.split()[0] for it in ar.get('items') or [] if it.startswith('data/')]
    add('ruling (1)', 'the root 6f32698e over 93 banks', (ar.get('root') or '').startswith('6f32698e') and len(named) == 93, 'data/b700_act_root.json (root %s, banks %d)' % ((ar.get('root') or '')[:8], len(named)), '1')
    chk = rd(p('data', 'b700_checks_postpush.txt')) or ''
    add('ruling (1)', 'the chain b624-b700 AGREE', 'b624 AGREE' in chk and 'b700 AGREE' in chk and 'b658 AGREE' in chk and 'b659 AGREE' in chk, 'data/b700_checks_postpush.txt (standing-b2, standing-b3)', '1')
    for f in ('b700_checks.txt', 'b700_checks_postpush.txt'):
        add('ruling (1)', 'suite 118 of 119 (%s)' % f, 'ARMS RUN : 119. ### LIVE PASSING : 118.' in (rd(p('data', f)) or '') and "['G-EDIT-ROUTE']" in (rd(p('data', f)) or ''), 'data/%s' % f, '1')
    add('ruling (1)', 'G-EDIT-ROUTE declared before the lock', '`G-EDIT-ROUTE`' in face and 'DECLARED BEFORE THE LOCK' in face, K.B700_FACE, '1')
    sc = rd(p('data', 'b700_scores_close.json')) or ''
    add('ruling (1)', 'all eight scores HELD', sc.count('"HELD"') >= 8, 'data/b700_scores_close.json (HELD %d)' % sc.count('"HELD"'), '1')
    cw = [l for l in (g(ROOT, 'log', '--format=%h', '--', 'data/b700_closing.txt')[1] or '').split(NL) if l.strip()]
    cb = g(ROOT, 'log', '-1', '--format=%B', '5623191e')[1] or ''
    add('ruling (1)', 'the closing written twice, the second carrying the scores read at the close', len(cw) >= 1 and cw[0].startswith('5623191e')
        and 'The closing written twice: first to give N4 its head line, then with the scores read at the close' in cb and 'relay data/b700_scores_close.json' in NL.join(cl),
        'relay 5623191e (the one commit carrying data/b700_closing.txt, its message naming the two writes) ; data/b700_closing.txt :62 (the scores read at the close)', '1')
    mi = rd(p('data', 'b700_mirror.txt')) or ''
    add('ruling (1)', 'mirror-refresh-2026-10-21-b700.zip CLEAN with the root line', 'Act root: b700 6f32698e' in mi and 'CLEAN ON ALL THREE CLAUSES' in mi, 'data/b700_mirror.txt', '1')
    add('ruling (1)', 'two defects, the seat`s, (a) the resume`s shell reads and (b) two whole reads entered late',
        "(a) THE SEAT'S: SHELL READS, PIPES, REDIRECTS AND A sed" in NL.join(df) and "(b) THE SEAT'S: TWO WHOLE READS" in NL.join(df), 'data/b700_defects.txt :6, :15', '1')
    add('ruling (1)', 'the author`s root answer in the carried-forward (a), its check VACUOUS', 'THE ROOT`S PROMPT AND ITS ANSWER' in NL.join(cl) and 'Option 1: W-ORD-H2-BRIDGE-THEOREM and the classK widening' in NL.join(cl)
        and 'VACUOUS' in NL.join(df), 'data/b700_closing.txt :232-:236 ; data/b700_defects.txt :43', '1')
    zips = ['D:/MY-DOwnloads/mirror-refresh-2026-10-%s-b%d.zip' % (dd, n) for n, dd in ((689, '19'), (690, '19'), (691, '19'), (692, '19'), (693, '19'), (694, '20'), (695, '20'), (696, '20'),
                                                                                       (697, '21'), (698, '21'), (699, '21'), (700, '21'))]
    add('ruling (1)', 'the b689-b700 mirror exports delivered as one set (the navigator`s sorting; the zips read here)', all(os.path.exists(z) for z in zips),
        '%d of 12 zips present under D:/MY-DOwnloads' % sum(os.path.exists(z) for z in zips), '1')
    # ### (R311)(2)
    add('ruling (2)', 'W-ORD-H2-BRIDGE-THEOREM at OPEN_TRAILS :15334', 'W-ORD-H2-BRIDGE-THEOREM' in at(ot, 15334), 'OPEN_TRAILS :15334', '2')
    v34 = g(EF, 'rev-parse', 'v0.34^{commit}')[1].strip()
    mn = g(EF, 'rev-parse', 'main')[1].strip()
    add('ruling (2)', 'v0.34`s commit read back by peeled SHA', v34 == K.EF_V034, 'SIDE-explicit-formula v0.34 peels %s (ls-remote read at step zero: the same)' % v34[:7], '2')
    add('ruling (2)', 'the branch bridge-b701 "from v0.34`s commit": v0.34`s commit is main`s tip', v34 == mn,
        'main %s is two commits past v0.34 %s -- v0.34.1 %s (b691`s EpsteinQ0 re-cut, print_targets.txt +12 names) and 4313875 (b692`s closure); the plan`s section 3 '
        '(data/b699_bridge_plan.txt :83) names "from main"; a branch from 8fbc27b that appends to print_targets.txt conflicts with v0.34.1`s append at the merge -- RAISED before Component 2' % (
            mn[:7], v34[:7], K.EF_V0341[:7]), '2')
    sm = lines_of(os.path.join(EF, 'SIDEExplicitFormula', 'Seam.lean'))
    lb = lines_of(os.path.join(EF, 'SIDEExplicitFormula', 'LiCriterionBridge.lean'))
    pc = lines_of(os.path.join(EF, 'SIDEExplicitFormula', 'PageConverses.lean'))
    add('ruling (2)', 'h2_sign_iff_rh (Seam.lean :101) and li_nonneg_iff_rh (LiCriterionBridge.lean :179) compiled at main', at(sm, 101).startswith('theorem h2_sign_iff_rh : h2_sign ↔ RiemannHypothesis')
        and at(lb, 179).startswith('theorem li_nonneg_iff_rh : (∀ n : ℕ, 0 ≤ LiCoeff n) ↔ RiemannHypothesis'), 'SIDEExplicitFormula/Seam.lean :101 ; LiCriterionBridge.lean :179', '2')
    s1 = ' '.join(at(pl, n) for n in (67, 68, 69))
    add('ruling (2)', '"composed ... from h2_sign_iff_rh and li_nonneg_iff_rh as the plan`s S1 names them": the plan`s S1 names li_nonneg_iff_rh', 'li_nonneg_iff_rh' in s1 and 'h2_sign_iff_rh' in s1,
        'the plan`s S1 (data/b699_bridge_plan.txt :67-:69) composes B321.h2_sign_iff_rh with PageConverses.register4_positivity_liCoeff_iff_rh (PageConverses.lean :32), which is '
        'li_nonneg_iff_rh at n ≥ 1 through liCoeff_zero (ResidueDischarge.lean :41-:46); li_nonneg_iff_rh is not named in S1 -- RAISED before Component 2', '2')
    add('ruling (2)', 'register4_positivity_liCoeff_iff_rh at PageConverses.lean :32', at(pc, 32).startswith('theorem register4_positivity_liCoeff_iff_rh : Register4_positivity LiCoeff ↔ RiemannHypothesis'),
        'SIDEExplicitFormula/PageConverses.lean :32', '2')
    add('ruling (2)', 'no tag v0.35 yet', not g(EF, 'tag', '-l', 'v0.35')[1].strip(), 'SIDE-explicit-formula tags: v0.35 absent, as expected before the merge', '2')
    add('ruling (2)', 'no branch bridge-b701 yet', not branch_listed(EF, 'bridge-b701'), 'absent, as expected', '2')
    add('ruling (2)', 'data/b701_faces_rows.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b701_faces_rows.txt')), 'absent, as ordered', '2')
    wf = rd(os.path.join(EF, '.github', 'workflows', 'build-module.yml')) or ''
    add('ruling (2); ferry', 'the hosted runner build-module.yml at main (ref and target inputs, the hold, the print step over print_targets.txt)', 'workflow_dispatch' in wf and 'HOLD_MB: "2560"' in wf
        and 'print_targets.txt' in wf and 'target:' in wf, 'SIDE-explicit-formula .github/workflows/build-module.yml', '2-3')
    # ### (R311)(3)
    add('ruling (3)', 'data/b701_widening_plan.txt -- TO BE WRITTEN at step zero', not os.path.exists(p('data', 'b701_widening_plan.txt')), 'absent, as ordered', '0')
    add('ruling (3)', 'no tag v0.36 and no branch widening-b701 yet', not g(EF, 'tag', '-l', 'v0.36')[1].strip() and not branch_listed(EF, 'widening-b701'), 'absent, as expected', '3')
    add('ruling (3)', 'data/b701_glossary_rows.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b701_glossary_rows.txt')), 'absent, as ordered', '3')
    add('ruling (3)', 'the explicit formula`s path threads C² as a binder (the seat`s reading for the plan)', g(EF, 'grep', '-c', 'ContDiff ℝ 2', 'main', '--', 'Zeta23/WeilEF')[1].strip() != '',
        'git grep -c "ContDiff ℝ 2" at main over Zeta23/WeilEF: %s' % ' ; '.join(x.split(':', 1)[1].replace(':', ' ') for x in g(EF, 'grep', '-c', 'ContDiff ℝ 2', 'main', '--', 'Zeta23/WeilEF')[1].split(NL) if x.strip())[:200], '3')
    # ### (R311)(4)
    add('ruling (4)', 'data/b701_epstein_plan.txt -- TO BE WRITTEN at step zero', not os.path.exists(p('data', 'b701_epstein_plan.txt')), 'absent, as ordered', '0')
    bi = lines_of(os.path.join(EF, 'SIDEExplicitFormula', 'B321Identity.lean'))
    add('ruling (4)', 'B321Identity`s three terms (poleTerm :29, primeSum :33, archTerm :37)', at(bi, 29).startswith('def poleTerm') and at(bi, 33).startswith('def primeSum') and at(bi, 37).startswith('def archTerm'),
        'SIDEExplicitFormula/B321Identity.lean :29, :33, :37', '4')
    rb = lines_of(os.path.join(EF, 'SIDEExplicitFormula', 'RestBound.lean'))
    eq = lines_of(os.path.join(EF, 'SIDEExplicitFormula', 'Schema', 'EpsteinQ0.lean'))
    add('ruling (4)', 'HCount (RestBound.lean :44), A0Q (EpsteinQ0.lean :104), Q0Count (:108)', at(rb, 44).startswith('def HCount') and at(eq, 104).startswith('def A0Q : ℝ := 10')
        and at(eq, 108).startswith('def Q0Count'), 'SIDEExplicitFormula/RestBound.lean :44 ; Schema/EpsteinQ0.lean :104, :108', '4')
    add('ruling (4)', 'data/b685_count.txt :19-:25 (the constants) and data/b687_steps.txt (the steps)', 'a = 0.432571915432' in at(lines_of(p('data', 'b685_count.txt')), 21)
        and first(lines_of(p('data', 'b687_steps.txt')), '(iv-1) the right edge') > 0, 'data/b685_count.txt :21 ; data/b687_steps.txt :7', '4')
    add('ruling (4)', 'data/b685_count_plan.txt :15-:82 (steps (1)-(9)) and data/b667_epstein_plan.txt :8-:12 (Z_Q, Λ_Q, the functional equation)',
        at(lines_of(p('data', 'b685_count_plan.txt')), 15).startswith('== 1. THE STEPS') and 'Λ_Q(s) = (2π/√23)^{−s} Γ(s) Z_Q(s)' in at(lines_of(p('data', 'b667_epstein_plan.txt')), 10),
        'data/b685_count_plan.txt :15 ; data/b667_epstein_plan.txt :10', '4')
    # ### (R311)(5)
    bb = dict(((r.get('repo'), r.get('branch')), r) for r in (json.loads(rd(p('data', 'b701_branches_before.json')) or '{}').get('rows') or []))
    for repo, bs in K.DELETE:
        for b in bs:
            r_ = bb.get((repo, b)) or {}
            listed = branch_listed(repo, b)
            add('ruling (5)', '%s %s (local)' % (os.path.basename(repo), b), listed or (bool(r_.get('tip')) and r_.get('merged') is True),
                'listed at the working repository before any delete' if listed else 'banked before the first delete at tip %s, merged, since deleted by name (data/b701_branches_before.json)' % (
                    r_.get('tip') or '-')[:12], '0')
    # ### (R311)(6)-(8)
    add('ruling (6)', 'the READFIRST-CLOSURE reader', 'readfirst' in (rd(p('tools', 'circuit_read.py')) or ''), 'tools/circuit_read.py', '0')
    add('ruling (7)', 'the draft at v5, held', "DRAFT = '23228113'" in wl, 'tools/b700_worklist.py :24', '5')
    r90, r98 = rd(p('data', 'b690_rules.txt')) or '', rd(p('data', 'b698_rules.txt')) or ''
    add('ruling (8)', 'rule (2) of data/b690_rules.txt and row (1) of data/b698_rules.txt', '(2)' in r90 and '(1)' in r98 and os.path.exists(p('data', 'b674_rules.txt')),
        'data/b690_rules.txt (2) ; data/b698_rules.txt (1) ; data/b674_rules.txt (the tie-break rule)', '5')
    # ### the ferry
    add('ferry C1', 'b700`s entry and trail', (line(FI, K.B700_ENTRY) or '').startswith('## ') and (line(OT, K.B700_TRAIL) or '').startswith('### b700'),
        'FINDINGS :%d ; OPEN_TRAILS :%d' % (K.B700_ENTRY, K.B700_TRAIL), '1')
    for rule, cl_, comp in (('R278', (4,), '5'), ('R251', (3,), '5'), ('R254', (2,), '4')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C4', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '4')
    add('ferry', 'data/b680_rules.txt, binary banks', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt (1)', '4')
    add('ferry C4', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '4')
    add('ferry C4', 'the chain halves as b693 drew them', "CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b693'))" in (rd(p('tools', 'b693_worklist.py')) or ''), 'tools/b693_worklist.py :52', '4')
    add('ferry C0', 'data/b684_rules.txt row (1), a test above 450 s its own part', '(1) A SUITE PART OVER 450 s SPLITS THE NEXT RUN' in (rd(p('data', 'b684_rules.txt')) or ''),
        'data/b684_rules.txt :5 (row (1)), applied to the test files by b700_tests.py ALONE_ABOVE', '0')
    add('ferry C5', 'b673`s capture names', os.path.exists(p('data', 'b700_relay_push_out.txt')), 'data/b700_relay_push_out.txt (the form carried)', '5')
    add('ferry C5', 'the b670 form of the mirror', os.path.exists(p('data', 'b700_mirror.txt')), 'data/b700_mirror.txt (the form carried)', '5')
    add('ruling; ferry', 'data/b701_readfirst.txt -- a step-zero bank', True, 'a step-zero bank (exists %s)' % os.path.exists(p('data', 'b701_readfirst.txt')), '0')
    return R


def _write(L, R, miss):
    for name, data in (('b701_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b701_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b701 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; (R311)(6)) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the source: the ruling and the ferry as pasted, read from the session transcript (%d characters, %r to %r); every cite checked at '
         'HEAD; rows are cites: where | what | OK or MISS | how | the component that cites it.' % (len(text), ANCHOR, TAIL), '']
    for where, what, ok, how, comp in R:
        L.append('  %-4s | %s | %s | %s | Component %s' % ('OK' if ok else 'MISS', where, what, how, comp))
    L += ['', '### THE MISSES, EACH RAISED TO THE AUTHOR BEFORE THE COMPONENT THAT CITES IT RUNS (none repaired silently):']
    L += ['  %s -- %s (Component %s)' % (what, how, comp) for _w, what, ok, how, comp in miss] or ['  NONE']
    L += ['', '### ### **CITES CHECKED %d ; OK %d ; MISSES %d.**' % (len(R), len(R) - len(miss), len(miss))]
    if 'dry' in a:
        print(NL.join(L))
        return
    _write(L, R, miss)
    print(NL.join(L[-(len(miss) + 4):]))


def ferry(*a):
    """the ferry is banked by the Write tool (data/b701_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b701_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b701_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b701_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b701."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    # ### b698's, b699's and b700's widening carried: the commit reach includes the kernels the act reads; b682's tool unedited
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, K.LV_DIR, 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster')
                                     if r not in P.REPOS)
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b701'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b701')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b701)', 'exec'), ns)
    ns['answer'](needle)


def word(needle, *a):
    """(R278)(4) on an author's word delivered as a bare BEGIN ... END paste: b694's route."""
    import b682_citation as P
    base = C._user_texts

    def marked(*k, **kw):
        return [("THE AUTHOR'S WORD " + t) if (t or '').lstrip().startswith(('BEGIN', '<pasted_content')) and 'END' in (t or '') else t
                for t in base(*k, **kw)]

    C._user_texts = marked
    P.C._user_texts = marked
    answer(needle)


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer, 'word': word}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b701_citation.py check [dry] | ferry | answer <needle> | word <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
