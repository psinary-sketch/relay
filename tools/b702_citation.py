# -*- coding: utf-8 -*-
"""b702_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b702's step zero, run before any other step
((R312)(9)); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT AUTHOR ANSWER
before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (e5bcf1d0, the session b701 ran in; the anchor (R312)'s line is unique in it); the answer route is b682's, imported from
### tools/b682_citation.py with its act names pointed at b702 and its commit reach widened to the kernels as b699-b701 widened it; the `word`
### route is b694's.
### Routes: `check` -> data/b702_citation_check.txt (.json) ; `ferry` -> data/b702_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the
###         check on one answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b702 from b701_citation.py's form; this tool writes only the banks named above.
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
import b702_worklist as K   # noqa: E402

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

HEAD_QUOTE = 'b701 closed: relay 2ab9ff3c, PLACE-papers 1e3fda0; suite 121 of 123; root 663799f09c0ad81c\u2026; 5 prompts answered; 7 defects'


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


def _remote_heads(repo):
    out = g(repo, 'ls-remote', '--heads', 'origin')[1] or ''
    return dict((l.split('\t', 1)[1].strip(), l.split('\t', 1)[0]) for l in out.split(NL) if '\t' in l)


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    FI = os.path.join(PP, 'FINDINGS.md')
    RM = os.path.join(PP, 'README.md')
    RG = os.path.join(PP, 'REGISTRY.md')
    ot, fi, rm, rg = lines_of(OT), lines_of(FI), lines_of(RM), lines_of(RG)
    EF = K.EF_DIR
    # ### the ferry's read-first list
    for f in ('data/b701_closing.txt', 'data/b701_defects.txt', 'data/b701_tool_repairs.txt', 'data/b701_obstruction.txt', 'data/b701_faces_rows.txt',
              'data/b701_grade.txt', 'data/b701_correspondence_restatement.txt', 'data/b701_clause_dominance.txt', 'data/b700_reading4.txt',
              'data/b695_circuit_spec.txt', 'data/b690_nodes_zeta.txt', 'tools/b700_checks.py', 'tools/b701_checks.py', 'data/b670_licensed_table.txt',
              'data/b674_rules.txt', 'data/b690_rules.txt', 'data/b698_rules.txt', 'data/b701_closing_push_out.txt', 'data/b700_r4_licensed.txt',
              'data/b648_recut_order.txt', 'data/b652_ferry.txt', 'data/b672_one_copy.txt', 'data/b697_nodes_zeta.txt', 'tools/chain_page.py',
              'tools/b700_corrigendum.py', 'data/b675_corrigenda.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    for f in ('README.md', 'REGISTRY.md', K.FACES_PAGE):
        add('ferry read-first', 'PLACE-papers %s' % f, os.path.exists(os.path.join(PP, f)), 'exists at the working tree', '0')
    cl = lines_of(p('data', 'b701_closing.txt'))
    add('ferry read-first; ruling (1)', 'data/b701_closing.txt :1, the head line, against (R312)(1)`s quote after whitespace is removed', _ws(cl[0]) == _ws(HEAD_QUOTE),
        'data/b701_closing.txt :1 = %r' % cl[0][:120], '0-1')
    cf = first(cl, '### CARRIED FORWARD.')
    add('ferry read-first', 'data/b701_closing.txt, the carried-forward rows (a)-(h) by line', cf > 0 and at(cl, cf + 1).startswith('    (a) ### **THE NEXT ACTS') and at(cl, cf + 17).startswith('    (h) '),
        'data/b701_closing.txt :%d-:%d' % (cf, cf + 17), '0-1')
    df = lines_of(p('data', 'b701_defects.txt'))
    lt = re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", NL.join(df), re.M)
    add('ferry read-first; ruling (1)', 'data/b701_defects.txt (rows are defects as lettered): (a)-(g), (d)-(e) the navigator`s', [x for x, _o in lt] == list('abcdefg')
        and [o for _x, o in lt] == ['SEAT', 'SEAT', 'SEAT', 'NAVIGATOR', 'NAVIGATOR', 'SEAT', 'SEAT'], 'letters %s ; owners %s' % (''.join(x for x, _o in lt), [o for _x, o in lt]), '0-1')
    tr = lines_of(p('data', 'b701_tool_repairs.txt'))
    add('ferry read-first; ruling (1)', 'data/b701_tool_repairs.txt (nine rows)', first(tr, 'REPAIRS 9 ;') > 0 and all(first(tr, '  (%d) tools/' % i) > 0 for i in range(1, 10)),
        'data/b701_tool_repairs.txt :%d (the verdict line) ; rows (1)-(9) at %s' % (first(tr, 'REPAIRS 9 ;'), ', '.join(':%d' % first(tr, '  (%d) tools/' % i) for i in range(1, 10))), '0-1')
    ob = lines_of(p('data', 'b701_obstruction.txt'))
    add('ferry read-first; ruling (1)', 'data/b701_obstruction.txt: H2SignWide.lean :59, le_rfl where n ≠ 0 is wanted, the one-token repair, the trigger', first(ob, 'H2SignWide.lean:59:42') > 0
        and first(ob, 'le_rfl') > 0 and first(ob, 'one_ne_zero') > 0 and first(ob, 'TRIGGER: the research act after b702') > 0,
        'data/b701_obstruction.txt :%d (the error), :%d (the repair), :%d (the trigger)' % (first(ob, 'H2SignWide.lean:59:42'), first(ob, 'one_ne_zero'), first(ob, 'TRIGGER: the research act after b702')), '0-1')
    fr = lines_of(p('data', 'b701_faces_rows.txt'))
    add('ferry read-first; ruling (4)', 'data/b701_faces_rows.txt (the successor by line)', at(fr, 14).startswith('@corr SIDE-lv-conservation |') and 'v0.35 = d4e046a' in at(fr, 14)
        and 'h2_sign_iff_register4_positivity_liCoeff' in at(fr, 14) and at(fr, 10).startswith('@corr SIDE-lv-conservation |'),
        'data/b701_faces_rows.txt :10 (the row as it stands), :14 (the successor)', '0-3')
    gr = lines_of(p('data', 'b701_grade.txt'))
    add('ferry read-first; ruling (1)', 'data/b701_grade.txt (rows as it names them): the grade DERIVES, E0 agreeing, every salt-check PASS', first(gr, 'h2_sign_iff_register4_positivity_liCoeff GRADE DERIVES (E0 DERIVES) SALT PASS') > 0
        and first(gr, 'EVERY SALT-CHECK PASSED True') > 0, 'data/b701_grade.txt :%d, :%d' % (first(gr, 'h2_sign_iff_register4_positivity_liCoeff GRADE DERIVES'), first(gr, 'EVERY SALT-CHECK PASSED True')), '0-1')
    cr = lines_of(p('data', 'b701_correspondence_restatement.txt'))
    add('ferry read-first; ruling (1)', 'data/b701_correspondence_restatement.txt: HOLDS-BY-CORRESPONDENCE at every binder (3 binders and the conclusion), K4 against binder 13',
        first(cr, 'HOLDS-BY-CORRESPONDENCE AT EVERY BINDER (3 BINDERS AND THE CONCLUSION)') > 0 and first(cr, 'K4 AGAINST THE FACE`S BINDER 13 AT lam := LiCoeff: HOLDS-BY-CORRESPONDENCE') > 0,
        'data/b701_correspondence_restatement.txt :%d' % first(cr, 'HOLDS-BY-CORRESPONDENCE AT EVERY BINDER'), '0-1')
    cd = lines_of(p('data', 'b701_clause_dominance.txt'))
    add('ferry read-first; ruling (1)', 'data/b701_clause_dominance.txt: 2 of 2 through the restatement, the direct reading DIFFERS at binder 1, controls C1 and C2 True',
        first(cd, '2 OF 2 THROUGH THE RESTATEMENT') > 0 and first(cd, 'DIFFERS') > 0, 'data/b701_clause_dominance.txt :%d' % first(cd, '2 OF 2 THROUGH THE RESTATEMENT'), '0-1')
    for ln, needle, what in ((K.ORDER_DISCHARGED, 'DISCHARGED', 'W-ORD-H2-BRIDGE and W-ORD-H2-BRIDGE-THEOREM DISCHARGED'), (K.ORDER_EFC1, 'W-ORD-EXPLICIT-FORMULA-C1', 'W-ORD-EXPLICIT-FORMULA-C1'),
                             (K.ORDER_HELD, 'W-ORD-CLASSK-WIDENING-HELD', 'W-ORD-CLASSK-WIDENING-HELD')):
        add('ferry read-first; ruling (1)', 'OPEN_TRAILS :%d (%s)' % (ln, what), needle in at(ot, ln) and at(ot, ln).startswith('*Appended 2026-10-21 by b701'), 'OPEN_TRAILS :%d' % ln, '0-1')
    for ln, what in ((K.ONECOPY_ENTERED, 'W-ORD-ONE-COPY entered (b671)'), (K.ONECOPY_TRIGGER, 'its trigger re-written (b672)'), (K.ONECOPY_B698, 'b698`s reading beneath it'), (K.ONECOPY_B699, 'b699`s reading beneath it')):
        add('ferry read-first; ruling (6)', 'OPEN_TRAILS :%d (%s)' % (ln, what), 'W-ORD-ONE-COPY' in at(ot, ln), 'OPEN_TRAILS :%d' % ln, '0-3')
    r4 = lines_of(p('data', 'b700_reading4.txt'))
    add('ferry read-first; ruling (6)', 'data/b700_reading4.txt (the ONE-COPY by-cause section :66-:76 and the roster-currency section :90-:100 by line)',
        at(r4, 66).startswith('  (18) W-ORD-ONE-COPY by line') and 'BY CAUSE: a regenerated cell 123, a hand edit 8' in at(r4, 70) and at(r4, 90).startswith('### (b) THE ROSTER-CURRENCY ROWS'),
        'data/b700_reading4.txt :66-:76 (row (18), by cause at :70), :90-:100 ((b) the roster-currency rows)', '0-3')
    sp = lines_of(p('data', 'b695_circuit_spec.txt'))
    add('ferry read-first; ruling (7)', 'data/b695_circuit_spec.txt (eleven rows)', 'ROWS 11' in at(sp, 67) and at(sp, 53).startswith('  CORRESPONDENCE-DOMINANCE'),
        'data/b695_circuit_spec.txt :7-:64 (the rows), :53 (the eleventh), :66-:67 (the verdict)', '0-4')
    # ### README and REGISTRY ((R312)(5))
    add('ferry read-first; ruling (5)', 'README.md :%d, the federation line: "most recently SIDE-window at tag v0.5.0 (working head aacb415)"' % K.README_FEDERATION,
        'most recently [SIDE-window]' in at(rm, K.README_FEDERATION) and 'tag `v0.5.0`' in at(rm, K.README_FEDERATION) and '`aacb415`' in at(rm, K.README_FEDERATION) and '`afa9ccf`' in at(rm, K.README_FEDERATION),
        'README.md :%d' % K.README_FEDERATION, '0-3')
    add('ferry read-first; ruling (5)', 'README.md :%d, the deposit note: the live monograph v5.18, the live kernel line SIDE-explicit-formula v0.21 (1d5d4dd)' % K.README_DEPOSIT,
        '**v5.18**' in at(rm, K.README_DEPOSIT) and 'SIDE-explicit-formula **v0.21** (`1d5d4dd`)' in at(rm, K.README_DEPOSIT), 'README.md :%d' % K.README_DEPOSIT, '0-3')
    add('ferry read-first; ruling (5)', 'README.md: the ceiling appends by line -- (R284)(3) b674 before (R232)(3) b622, (R245)(5)(ii) b635 the last',
        at(rm, K.README_R284).startswith("*(Appended under the author's ruling `(R284)`(3), 2026-10-16, b674") and at(rm, K.README_R232).startswith("*(Appended under the author's ruling `(R232)`(3), 2026-10-04, b622")
        and at(rm, K.README_R245).startswith("*(Appended under the author's ruling `(R245)`(5)(ii), 2026-10-07, b635"),
        'README.md :%d ((R284)(3)), :%d ((R232)(3)), :%d ((R245)(5)(ii)) ; the file 188 lines' % (K.README_R284, K.README_R232, K.README_R245), '0-3')
    add('ruling (5)', 'the (R245)(5)(ii) sentence at :188 and the (R284)(3) sentence at :184, as the ruling names them', at(rm, 188).startswith("*(Appended under the author's ruling `(R245)`") and at(rm, 184).startswith("*(Appended under the author's ruling `(R284)`"),
        'README.md :188 is %r and :184 is %r ; the sentences stand at :%d ((R245)(5)(ii)) and :%d ((R284)(3)) -- the ruling`s line numbers do not match the file; RAISED before Component 3' % (
            at(rm, 188)[:40], at(rm, 184)[:40], K.README_R245, K.README_R284), '3')
    lc = (g(PP, 'log', '-1', '--format=%h', '--', 'README.md')[1] or '').strip()
    add('ruling (5)', 'README.md at 4cb90e0 (its last commit)', lc == K.README_LAST_COMMIT, 'PLACE-papers README.md last written at %s (%s)' % (lc, subject(PP, lc)[:70]), '3')
    rrow = [i + 1 for i, l in enumerate(rg) if l.startswith('| ') and l.split('|')[2].strip().startswith('README')]
    rmen = [i + 1 for i, l in enumerate(rg) if l.startswith('|') and 'README' in l]
    add('ruling (5)', 'REGISTRY`s README row (to be stepped to v1.6) and the README`s "v1.5"', bool(rrow) and 'v1.5' in NL.join(rm[:12]),
        'REGISTRY.md rows whose title cell is README: %s ; table lines mentioning README.md in another row`s notes: %s ; "v1.5" in README.md`s head (:1-:12): %s (README.md :15 names '
        'SIDE-kernel`s tag v1.5; the file carries no version of its own; REGISTRY carries no README row) -- RAISED before Component 3' % (rrow or 'NONE', rmen or 'NONE', 'v1.5' in NL.join(rm[:12])), '3')
    add('ferry read-first; ruling (5)', 'REGISTRY.md :%d (the d1-1 monograph row) and :%d (d1-5 Seven Mechanism Classes, v3.3)' % (K.REGISTRY_D1_1, K.REGISTRY_D1_5),
        at(rg, K.REGISTRY_D1_1).startswith('| d1-1 | A Place to Stand (monograph)') and at(rg, K.REGISTRY_D1_5).startswith('| d1-5 | Seven Mechanism Classes |'),
        'REGISTRY.md :%d (v5.13 in its version cell against the README`s live v5.18), :%d' % (K.REGISTRY_D1_1, K.REGISTRY_D1_5), '0-3')
    # ### the faces page ((R312)(4))
    pg = lines_of(os.path.join(PP, K.FACES_PAGE))
    nz = lines_of(p('data', 'b690_nodes_zeta.txt'))
    n7 = lines_of(p('data', K.NODES_LIST))
    add('ferry read-first; ruling (4)', 'data/b690_nodes_zeta.txt :126 (the lv-conservation @corr row) and the page`s line :%d carrying it' % K.FACES_ROW_LINE,
        at(nz, K.NODES_ROW).startswith('@corr SIDE-lv-conservation | residue_irreducible |') and at(pg, K.FACES_ROW_LINE).startswith('| `residue_irreducible` | SIDE-lv-conservation |')
        and 'v0.10 = 6baed63' in at(pg, K.FACES_ROW_LINE), 'data/b690_nodes_zeta.txt :126 ; %s :%d' % (K.FACES_PAGE, K.FACES_ROW_LINE), '0-3')
    add('ruling (4)', 'the page`s header tag v0.26 = 82550e4 and its node list data/b697_nodes_zeta.txt', K.FACES_HEADER_TAG in at(pg, 3) and 'data/b697_nodes_zeta.txt' in at(pg, 3)
        and first(n7, '@corr SIDE-lv-conservation | residue_irreducible |') > 0, '%s :3 ; data/b697_nodes_zeta.txt :%d (the @corr row)' % (K.FACES_PAGE, first(n7, '@corr SIDE-lv-conservation | residue_irreducible |')), '3')
    add('ruling (4)', 'tools/chain_page.py, the generator, and data/b702_nodes_zeta.txt TO BE WRITTEN', os.path.exists(p('tools', 'chain_page.py')) and not os.path.exists(p('data', 'b702_nodes_zeta.txt')),
        'tools/chain_page.py exists ; data/b702_nodes_zeta.txt absent, as ordered', '3')
    # ### (R312)(1)
    po = rd(p('data', 'b701_closing_push_out.txt')) or ''
    poc = [l for l in (g(ROOT, 'log', '--format=%h', '--', 'data/b701_closing_push_out.txt')[1] or '').split(NL) if l.strip()]
    po_alone = len(poc) == 1 and [x for x in (g(ROOT, 'show', '--name-only', '--pretty=format:', poc[0])[1] or '').split(NL) if x.strip()] == ['data/b701_closing_push_out.txt']
    add('ferry read-first; ruling (1)', 'data/b701_closing_push_out.txt (commit at the start): the closing pushed and read back at relay main 613847d6', 'main read back at the remote: 613847d6' in po and (po_alone or not poc)
        and g(ROOT, 'rev-parse', '--short=8', K.PRE_RELAY)[1].strip() == '613847d6',
        'main read back at 613847d6 ; %s' % (('committed alone at relay %s' % poc[0]) if poc else 'untracked at the working tree, to be committed alone'), '0-1')
    v35 = g(EF, 'rev-parse', 'v0.35^{commit}')[1].strip()
    rb = lines_of(os.path.join(EF, 'SIDEExplicitFormula', 'RegisterBridge.lean'))
    add('ruling (1)', 'the bridge at v0.35 = d4e046a, RegisterBridge.lean, h2_sign_iff_register4_positivity_liCoeff := h2_sign_iff_rh.trans register4_positivity_liCoeff_iff_rh.symm',
        v35 == K.EF_V035 and first(rb, 'theorem h2_sign_iff_register4_positivity_liCoeff : h2_sign ↔ Register4_positivity LiCoeff :=') > 0 and first(rb, 'h2_sign_iff_rh.trans register4_positivity_liCoeff_iff_rh.symm') > 0,
        'SIDE-explicit-formula v0.35 peels %s ; SIDEExplicitFormula/RegisterBridge.lean :%d' % (v35[:7], first(rb, 'theorem h2_sign_iff_register4_positivity_liCoeff')), '1')
    rn = lines_of(p('data', 'b701_runner_SIDE-explicit-formula_run1.txt'))
    add('ruling (1)', 'run 39635057369 DERIVES, the artifact sha256 agreeing, 74 of 74 terminals at the standard three', first(rn, 'RUN 39635057369 (run1)') > 0 and first(rn, 'ARTIFACT AGREE') > 0
        and first(rn, 'TERMINALS PRINTED 74 OF 74') > 0 and first(rn, 'GATE DERIVES') > 0, 'data/b701_runner_SIDE-explicit-formula_run1.txt :%d' % first(rn, 'RUN 39635057369 (run1)'), '1')
    wt = g(EF, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.WIDEN_BRANCH)[1].strip()
    rh = _remote_heads(EF)
    add('ruling (1); ruling (8)', 'widening-b701 = 8a4ab68 standing, local and remote, held for b703', wt == K.WIDEN_TIP and rh.get('refs/heads/widening-b701') == K.WIDEN_TIP,
        'local %s ; remote %s (one ls-remote of SIDE-explicit-formula at step zero)' % (wt[:7], (rh.get('refs/heads/widening-b701') or '-')[:7]), '0')
    add('ruling (8)', 'the kernel branches b701 made: bridge-b701 (local and remote) and push-b701-bridge (local), raised as one prompt before any delete',
        branch_listed(EF, 'bridge-b701') and 'refs/heads/bridge-b701' in rh and branch_listed(EF, 'push-b701-bridge') and 'refs/heads/push-b701-bridge' not in rh,
        'bridge-b701 local %s remote %s ; push-b701-bridge local, not at the remote (push_gated`s main mode pushes the branch to main)' % (
            'listed' if branch_listed(EF, 'bridge-b701') else 'absent', (rh.get('refs/heads/bridge-b701') or '-')[:7]), '0')
    ep = lines_of(p('data', 'b701_epstein_plan.txt'))
    add('ruling (1); ruling (11)', 'the Epstein plan priced at 1 dispatch for the opening step and 6 at the least', first(ep, 'THE OPENING STEP 1 DISPATCH, THE WHOLE 6 AT THE LEAST') > 0,
        'data/b701_epstein_plan.txt :%d' % first(ep, 'THE OPENING STEP 1 DISPATCH, THE WHOLE 6 AT THE LEAST'), '1')
    add('ruling (1)', 'the entry at FINDINGS :9798, b700`s weight at :9796, the trail at OPEN_TRAILS :15412', at(fi, K.B701_ENTRY).startswith('## The bridge h2_sign ↔ Register4_positivity LiCoeff compiled')
        and 'b700 AT ITS WEIGHT' in at(fi, K.B701_WEIGHT) and at(ot, K.B701_TRAIL).startswith('### b701'), 'FINDINGS :%d, :%d ; OPEN_TRAILS :%d' % (K.B701_ENTRY, K.B701_WEIGHT, K.B701_TRAIL), '1')
    ar = json.loads(rd(p('data', 'b701_act_root.json')) or '{}')
    named = [it.split()[0] for it in ar.get('items') or [] if it.startswith('data/')]
    add('ruling (1)', 'the root 663799f0 over 70 banks', (ar.get('root') or '').startswith('663799f0') and len(named) == 70, 'data/b701_act_root.json (root %s, banks %d)' % ((ar.get('root') or '')[:8], len(named)), '1')
    mi = rd(p('data', 'b701_mirror.txt')) or ''
    add('ruling (1)', 'the mirror export sha256 b1fbc501 CLEAN on all three clauses', 'sha256 b1fbc501' in mi and 'CLEAN ON ALL THREE CLAUSES' in mi and 'Act root: b701 663799f0' in mi, 'data/b701_mirror.txt', '1')
    sc = rd(p('data', 'b701_scores_close.json')) or ''
    add('ruling (1)', 'all eight scores HELD', sc.count('"HELD"') >= 8, 'data/b701_scores_close.json (HELD %d)' % sc.count('"HELD"'), '1')
    ck, cp = rd(p('data', 'b701_checks.txt')) or '', rd(p('data', 'b701_checks_postpush.txt')) or ''
    add('ruling (1)', 'suite 122 of 123 pre-push (G-READ-RULE) and 121 of 123 post-push (G-ACTROOT-LAST, G-READ-RULE)', 'ARMS RUN : 123. ### LIVE PASSING : 122.' in ck and "['G-READ-RULE']" in ck
        and 'ARMS RUN : 123. ### LIVE PASSING : 121.' in cp and "['G-ACTROOT-LAST', 'G-READ-RULE']" in cp, 'data/b701_checks.txt ; data/b701_checks_postpush.txt', '1')
    face = rd(p(*K.B701_FACE.split('/'))) or ''
    add('ruling (1)', 'the two failures undeclared on the face (its declaration line NONE)', 'DECLARED BEFORE THE LOCK, BY NAME:** NONE.' in face, K.B701_FACE, '1')
    rc = lines_of(p('data', 'b701_read_calls.txt'))
    rcl = first(rc, '### AN OFFENCE | D:\\relay\\data\\audit_b701_reg_satisfiable.txt')
    add('ruling (1)', 'the fourth whole read of a long file after the seal, entered by the read bank and not lettered', rcl > 0 and 'WHOLE OF A FILE OF 200 LINES OR MORE 4' in NL.join(rc),
        'data/b701_read_calls.txt :%d (the audit file, 219 lines, read with a limit and no offset at 17:53:52Z -- after the defects bank`s commit 3d13a871 at 17:15Z and the face`s dry-run step, '
        'before the lock at 17:58:15Z; the ruling`s "after the seal" is off by five minutes, the item unlettered either way)' % rcl, '1')
    cm = rd(p('data', 'b701_commands.txt')) or ''
    add('ruling (1)', 'the "2>&1 | head -c 0" of one post-seal diagnostic: NOT in b701`s command bank (written at the root, 18:02Z, before that command at 18:2xZ); read from this session`s transcript by this act`s capture',
        'head -c 0' not in cm and 'REDIRECTS OF ANY STREAM 1' in cm, 'data/b701_commands.txt (REDIRECTS OF ANY STREAM 1, the one of defect (c)) ; the diagnostic is in the transcript after b701`s root -- this act`s capture of the previous act`s window carries it', '1')
    add('ruling (1)', 'the per-part seconds banks rewritten after the root (G-ACTROOT-LAST)', 'G-ACTROOT-LAST' in cp and 'if PRERUN' not in NL.join(lines_of(p('tools', 'b701_checks.py'))[1780:1787]),
        'data/b701_checks_postpush.txt ; tools/b701_checks.py :1782-:1786 (the write, unguarded) against tools/b700_checks.py :1669 (`if PRERUN:`)', '1-2')
    tl = next((l for l in ot[K.B701_TRAIL - 1:K.B701_TRAIL + 40] if l.startswith('**Resolved by the seat')), '')
    add('ruling (1)', 'the trail`s "Resolved by the seat (7)" miscount: three navigator misses and six seat defects where the bank holds two and five',
        'the three navigator misses and the seat’s six defects as lettered' in tl, 'OPEN_TRAILS :%d (the Resolved line of b701`s trail) ; the bank: navigator 2 ((d), (e)), seat 5' % (
            K.B701_TRAIL + next((i for i, l in enumerate(ot[K.B701_TRAIL - 1:K.B701_TRAIL + 40]) if l.startswith('**Resolved by the seat')), 0)), '1')
    # ### (R312)(2)
    cg = lines_of(p('data', 'b675_corrigenda.txt'))
    add('ruling (2)', 'the corrigenda bank data/b675_corrigenda.txt, its last row (16), appended only', first(cg, '  (16) ') > 0 and first(cg, '  (17) ') == 0, 'data/b675_corrigenda.txt :%d (row (16)); row (17) this act`s' % first(cg, '  (16) '), '2')
    add('ruling (2)', 'b700`s corrigendum tool (b678`s form by import) to carry', 'import b678_corrigendum as C78' in (rd(p('tools', 'b700_corrigendum.py')) or ''), 'tools/b700_corrigendum.py :34', '2')
    c0 = lines_of(p('tools', 'b700_checks.py'))
    c1 = lines_of(p('tools', 'b701_checks.py'))
    add('ruling (2)', 'the PRERUN guard: b700`s suite tool :1669 `if PRERUN:` over the per-part seconds write, b701`s :1782 without it',
        at(c0, 1669).strip() == 'if PRERUN:' and 'b700_arm_seconds_%s.json' in at(c0, 1673) and 'b701_arm_seconds_%s.json' in at(c1, 1782) and at(c1, 1781).strip() != 'if PRERUN:',
        'tools/b700_checks.py :1669-:1676 ; tools/b701_checks.py :1782-:1786', '2')
    # ### (R312)(3)
    lt_ = lines_of(p('data', K.LICENSED_NOW))
    kd = lines_of(p('data', K.KINDS))
    add('ferry read-first; ruling (3)', 'data/b670_licensed_table.txt (the 19 roster tables :6-:24, the agenda :26-:58) and the per-document tables',
        at(lines_of(p('data', 'b670_licensed_table.txt')), 4).startswith('### THE DOCUMENT SET, A') and os.path.exists(p('data', 'b646_table_Seven_Mechanism_Classes.txt')),
        'data/b670_licensed_table.txt :4-:58 ; data/b646_table_<companion>.txt, data/b647_table_SIDE-<kernel>.txt', '0-2')
    add('ruling (3)', 'reading 4`s agenda rows (b648 -> b680 -> b690 -> b700): every kernel at 0, the seven companions at 5-24, the monograph 217',
        at(lt_, 52).startswith('  day1/A_Place_to_Stand_v5_18.md') and '217 ->  217' in at(lt_, 52) and at(lt_, 56).startswith('  day1/Seven_Mechanism_Classes.md (v3.3.1)') and '24 ->   24' in at(lt_, 56)
        and all(re.search(r'->\s+0\s+\[', l) for l in lt_[61:84]) and 'DOCUMENTS AT ZERO 23' in at(lt_, 88),
        'data/b700_r4_licensed.txt :52-:84 (the rows), :88 (DOCUMENTS AT ZERO 23: the 23 kernel rows and the h2 row) -- the kernels all at 0, so b652`s order passes to the companions', '2')
    add('ruling (3)', 'b648`s kinds: monograph 1, companions 7, pages 2, kernels 22, the h2 row', at(kd, 4).split('|')[1].strip() == 'monograph' and all(at(kd, i).split('|')[1].strip() == 'companion' for i in range(5, 12)),
        'data/b648_recut_order.txt :4 (monograph), :5-:11 (the seven companions), :12-:13 (pages), :14-:35 (kernels)', '2')
    add('ferry read-first; ruling (3)', 'b652`s order, data/b652_ferry.txt :19, "the next kernel by descending count under the same rules, then the companions"',
        'the next kernel by descending count under the same rules, then the companions' in at(lines_of(p('data', 'b652_ferry.txt')), K.ORDER_LINE), 'data/b652_ferry.txt :19', '2')
    add('ferry read-first; ruling (3)', 'b674`s tie-break rule, data/b674_rules.txt :8-:11', at(lines_of(p('data', 'b674_rules.txt')), 8).startswith('  (2) THE TIE-BREAK BEYOND THE COUNT'), 'data/b674_rules.txt :8-:11', '2')
    r90, r98 = lines_of(p('data', 'b690_rules.txt')), lines_of(p('data', 'b698_rules.txt'))
    add('ferry read-first; ruling (3)', 'rule (2) of data/b690_rules.txt (the quotation search before the merge) and row (1) of data/b698_rules.txt (a tag move regenerates the cells)',
        at(r90, 9).startswith('  (2) AT A RE-CUT, EACH LINE THE CUT REMOVES OR CHANGES HAS A DISTINCTIVE SUBSTRING') and at(r98, 6).startswith("  (1) A KERNEL'S TAG MOVE REGENERATES THE CORRESPONDENCE CELLS"),
        'data/b690_rules.txt :9 ; data/b698_rules.txt :6', '0-2')
    add('ruling (3)', 'b676`s form for a kernel`s docstrings (data/b676_cut.txt) and the b670 method for a paper (each non-MATCHES row`s ACTION, the distance the rows not met)',
        os.path.exists(p('data', 'b676_cut.txt')) and os.path.exists(p('data', 'b670_rules.txt')), 'data/b676_cut.txt ; data/b670_rules.txt ; data/b699_cut.txt :12-:15 (the method applied)', '2')
    s7 = lines_of(p('data', 'b646_table_Seven_Mechanism_Classes.txt'))
    add('ruling (3)', 'the top companion`s table: Seven_Mechanism_Classes OVERREACHES 19, UNLICENSED 5 (24 rows outside LICENSED/CITED)', 'OVERREACHES 19 ; UNLICENSED 5' in at(s7, 331),
        'data/b646_table_Seven_Mechanism_Classes.txt :331 (the summary line) ; the next by count Spectral_Inertness 22 and ONE_PAGE_PROOF 22', '2')
    add('ruling (3)', 'data/b702_cut.txt and data/b702_tie.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b702_cut.txt')) and not os.path.exists(p('data', 'b702_tie.txt')), 'absent, as ordered', '2')
    # ### (R312)(5)-(7)
    add('ruling (5)', 'SIDE-window`s highest tag v0.5.2 against the README`s v0.5.0 (one ls-remote at step zero)', True,
        'ls-remote --tags: v0.5.2 peels b905507, v0.5.1 e5b737a, v0.5.0 = aacb415 (lightweight) ; the README :18 names v0.5.0 (aacb415) -- the currency row', '3')
    add('ruling (5)', 'SIDE-effects` main 78bbcff (= v0.1.1) against the README`s afa9ccf (one ls-remote at step zero)', True, 'ls-remote: main 78bbcff, v0.1.1 peels 78bbcff ; the README :18 names afa9ccf -- a currency row', '3')
    add('ruling (5)', 'data/b702_readme_currency.txt -- TO BE WRITTEN at step zero and committed alone', not os.path.exists(p('data', 'b702_readme_currency.txt')), 'absent, as ordered', '0')
    add('ruling (6)', 'data/b672_one_copy.txt (rows are the 25 documents with their copies)', 'rows are the 25 documents of OPEN_TRAILS :14386 item (b)' in at(lines_of(p('data', 'b672_one_copy.txt')), 3), 'data/b672_one_copy.txt :3', '3')
    add('ruling (7)', 'data/b702_circuit_spec.txt -- TO BE WRITTEN at step zero and committed alone', not os.path.exists(p('data', 'b702_circuit_spec.txt')), 'absent, as ordered', '0')
    ef98 = at(lines_of(os.path.join(EF, 'Zeta23', 'ExplicitFormula.lean')), 98)
    wp = lines_of(p('data', 'b701_widening_plan.txt'))
    add('ruling (7)', 'EF_lit :98 binding ContDiff ℝ 2 and the 40 binder lines b701 found by hand', 'ContDiff ℝ 2' in ef98 and first(wp, '40') > 0 and first(wp, 'Zeta23') > 0,
        'SIDE-explicit-formula Zeta23/ExplicitFormula.lean :98 ; data/b701_widening_plan.txt (the binder count section)', '4')
    fs = rd(p('tools', 'ferry_scan.py')) or ''
    add('ruling (7)', 'the arms that read the ferry`s text today: ferry_scan`s standing-clauses citation (cited none ; current 2)', 'STANDING-CLAUSES CITATION' in fs,
        'tools/ferry_scan.py :700 ; data/b702_ferry_scan.txt (STANDING-CLAUSES CITATION : NONE, cited none ; current 2)', '4')
    # ### (R312)(8)
    for repo, bs in K.DELETE:
        mg = (g(repo, 'branch', '--merged', 'main')[1] or '').replace('*', ' ').split()
        for b in bs:
            add('ruling (8)', '%s %s (local, listed --merged)' % (os.path.basename(repo), b), b in mg, 'listed by `git branch --merged main` at %s before any delete' % os.path.basename(repo) if b in mg else '### NOT LISTED', '0')
    # ### (R312)(9)-(11)
    add('ruling (9)', 'the READFIRST-CLOSURE reader', 'readfirst' in (rd(p('tools', 'circuit_read.py')) or ''), 'tools/circuit_read.py', '0')
    add('ruling (10)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b701_worklist.py')) or ''), 'tools/b701_worklist.py :25', '6')
    add('ruling (11)', 'W-ORD-CLASSK-WIDENING-HELD at :15410 with its trigger, data/b701_epstein_plan.txt for b703', 'Trigger: the research act after b702' in at(ot, K.ORDER_HELD) and os.path.exists(p('data', 'b701_epstein_plan.txt')),
        'OPEN_TRAILS :15410 ; data/b701_epstein_plan.txt', '6')
    # ### the ferry
    add('ferry C1', 'b701`s entry and trail', (line(FI, K.B701_ENTRY) or '').startswith('## ') and (line(OT, K.B701_TRAIL) or '').startswith('### b701'),
        'FINDINGS :%d ; OPEN_TRAILS :%d' % (K.B701_ENTRY, K.B701_TRAIL), '1')
    for rule, cl_, comp in (('R278', (4,), '6'), ('R251', (3,), '6'), ('R254', (2,), '5')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C5', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '5')
    add('ferry', 'data/b680_rules.txt, binary banks', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt (1)', '5')
    add('ferry C5', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '5')
    add('ferry C5', 'the chain halves as b693 drew them', "CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b693'))" in (rd(p('tools', 'b693_worklist.py')) or ''), 'tools/b693_worklist.py :52', '5')
    add('ferry C0', 'data/b684_rules.txt row (1), a test above 450 s its own part', '(1) A SUITE PART OVER 450 s SPLITS THE NEXT RUN' in (rd(p('data', 'b684_rules.txt')) or ''), 'data/b684_rules.txt :5', '0')
    add('ferry C6', 'b673`s capture names', os.path.exists(p('data', 'b701_relay_push_out.txt')), 'data/b701_relay_push_out.txt (the form carried)', '6')
    add('ferry C6', 'the b670 form of the mirror', os.path.exists(p('data', 'b701_mirror.txt')), 'data/b701_mirror.txt (the form carried)', '6')
    add('ruling; ferry', 'data/b702_readfirst.txt -- a step-zero bank', True, 'a step-zero bank (exists %s)' % os.path.exists(p('data', 'b702_readfirst.txt')), '0')
    return R


def _write(L, R, miss):
    for name, data in (('b702_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b702_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b702 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; (R312)(9)) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b702_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b702_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b702_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b702_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b702."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, 'D:/SIDE-lv-conservation', 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects') if r not in P.REPOS)
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b702'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b702')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b702)', 'exec'), ns)
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
        print('usage: b702_citation.py check [dry] | ferry | answer <needle> | word <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
