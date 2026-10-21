# -*- coding: utf-8 -*-
"""b700_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b700's step zero, run before any other step
((R310)(6)); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT AUTHOR ANSWER
before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (c677eaf2); the answer route is b682's, imported from tools/b682_citation.py with its act names pointed at b700 and its commit reach
### widened to the kernels as b699 widened it; the `word` route is b694's (a bare BEGIN ... END paste read as the author's word).
### Routes: `check` -> data/b700_citation_check.txt (.json) ; `ferry` -> data/b700_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the
###         check on one answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b700 from b699_citation.py's form; this tool writes only the banks named above.
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
import b700_worklist as K   # noqa: E402

C.SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID


def continuation_sessions():
    """the act's continuation sessions (K.SESSIONS_AFTER, b671's form) as transcript paths, read by b677's helpers after the seat's session:
    the answers given after the host reboot are read in the session that received them."""
    return tuple('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid for sid, _anc in K.SESSIONS_AFTER)


C.SESSIONS_AFTER = continuation_sessions()
NL = chr(10)
PP = C.PP
C.ANCHOR, C.TAIL = K.ANCHOR, K.TAIL
ANCHOR, TAIL = C.ANCHOR, C.TAIL
g, rd, line, commit_in, subject, branch_listed, rule_clause = (C.g, C.rd, C.line, C.commit_in, C.subject, C.branch_listed, C.rule_clause)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def act_root_line(act):
    t = rd(os.path.join(D, 'act_roots.txt')) or ''
    return [l.split() for l in t.split(NL) if l.strip() and l.split()[0] == act]


def lines_of(path):
    return (rd(path) or '').split(NL)


def first(L, needle):
    return next((i + 1 for i, l in enumerate(L) if needle in l), 0)


def at(L, n):
    return L[n - 1] if n and len(L) >= n else ''


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    FI = os.path.join(PP, 'FINDINGS.md')
    ot, fi = lines_of(OT), lines_of(FI)
    # ### the ferry's read-first list
    for f in ('data/b699_closing.txt', 'data/b699_defects.txt', 'data/b699_bridge_plan.txt', 'data/b698_regularity_uses.txt', 'data/b687_p3_status.txt',
              'data/b685_count.txt', 'data/b690_reading3.txt', 'data/b683_arms_sort.txt', 'data/b672_roster_read.json', 'data/b692_circuit_dominance.txt',
              'data/b694_circuit_dominance.txt', 'data/b698_correspondence_dominance.txt', 'tools/correspondence_gen.py', 'data/b699_closing_push_out.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    cl = lines_of(p('data', 'b699_closing.txt'))
    gl = first(cl, '    (g) The defects (a)')
    add('ferry read-first', 'data/b699_closing.txt :1 and the defects line', cl[0].startswith('b699 closed:') and 'and (d), THE SEAT' in ' '.join(cl[gl - 1:gl + 1]),
        'data/b699_closing.txt :1 ; the defects line :%d-:%d' % (gl, gl + 4), '0')
    df = lines_of(p('data', 'b699_defects.txt'))
    lt = re.findall(r"^    \(([a-z])\) ", NL.join(df), re.M)
    add('ferry read-first', 'data/b699_defects.txt (rows are defects as lettered)', lt == list('abc'), 'letters %s ; (d) in the closing line alone' % ''.join(lt), '0')
    add('ferry read-first', 'OPEN_TRAILS :15332, :15334 and :15336', 'beneath `W-ORD-ONE-COPY`' in at(ot, 15332) and 'W-ORD-H2-BRIDGE-THEOREM' in at(ot, 15334)
        and at(ot, 15336).startswith('### b699'), 'OPEN_TRAILS :15332 (one-copy), :15334 (the bridge order), :15336 (b699`s trail)', '0')
    pl = lines_of(p('data', 'b699_bridge_plan.txt'))
    s1, pr = first(pl, '  S1  theorem'), first(pl, 'PRICE: 1 dispatch')
    add('ferry read-first', 'data/b699_bridge_plan.txt (rows are binders; the expected statement and price by line)', s1 > 0 and pr > 0
        and first(pl, '== 1. THE BINDERS') > 0, 'data/b699_bridge_plan.txt :%d (binders), :%d (S1), :%d (price)' % (first(pl, '== 1. THE BINDERS'), s1, pr), '0-3')
    ru = lines_of(p('data', 'b698_regularity_uses.txt'))
    add('ferry read-first', 'data/b698_regularity_uses.txt (the per-column counts by line)', 'W1 DISCHARGED 11, RE-PROVED 6, OBSTRUCTED 0' in at(ru, 85),
        'data/b698_regularity_uses.txt :85 (uses), :86 (path)', '0-2')
    ps = lines_of(p('data', 'b687_p3_status.txt'))
    add('ferry read-first', 'data/b687_p3_status.txt (the derivation`s steps by row)', bool(ps) and first(ps, 'DERIVED') > 0,
        'data/b687_p3_status.txt (%d lines ; DERIVED at :%d)' % (len(ps), first(ps, 'DERIVED')), '0-3')
    add('ferry read-first', 'data/b685_count.txt (the derivation`s steps by row)', len(lines_of(p('data', 'b685_count.txt'))) > 5,
        'data/b685_count.txt (%d lines)' % len(lines_of(p('data', 'b685_count.txt'))), '0-3')
    r3 = lines_of(p('data', 'b690_reading3.txt'))
    add('ferry read-first', 'data/b690_reading3.txt and the bank reading 2 was banked as', at(r3, 3).startswith('### rows are readings') and os.path.exists(p('data', 'b680_licensed.txt')),
        'data/b690_reading3.txt :3 ; reading 2 banked as data/b680_<name>.txt (b680_licensed, b680_correspondence, b680_orders, b680_lag, ...) -- no '
        'single reading-2 bank (data/b690_reading3.txt :3-:5)', '0-2')
    dfs = ['data/b%d_defects.txt' % a for a in range(673, 700)]
    add('ferry read-first', 'every defects bank b673 through b699', all(os.path.exists(p(*f.split('/'))) for f in dfs), '%d banks present' % sum(
        os.path.exists(p(*f.split('/'))) for f in dfs), '0-2')
    rls = [f for f in ('data/b%d_rules.txt' % a for a in range(674, 700)) if os.path.exists(p(*f.split('/')))]
    add('ferry read-first', 'every rules bank b674 through b699', len(rls) >= 15, '%d banks: %s' % (len(rls), ', '.join(os.path.basename(f)[:4] for f in rls)), '0-2')
    so = lines_of(p('data', 'b683_arms_sort.txt'))
    add('ferry read-first', 'data/b683_arms_sort.txt (the sort rule`s words by line)', first(so, 'TRACEABLE') > 0, 'data/b683_arms_sort.txt :%d' % first(so, 'TRACEABLE'), '0-2')
    rs = lines_of(p('tools', 'b698_record.py'))
    add('ferry read-first', 'the record tool`s defect_short by path and line', first(rs, 'def _defect_short(act=ACT):') == 367,
        'tools/b698_record.py :367 (def _defect_short(act=ACT)), carried by reference at tools/b699_record.py :%d' % first(
            lines_of(p('tools', 'b699_record.py')), '_defect_short, _anchor_ts = '), '0-1')
    r9 = lines_of(p('tools', 'b699_record.py'))
    add('ferry read-first', 'the root tool`s list of the banks it names by line', first(r9, 'R.ROOT_EXCLUDE = re.compile') > 0 and first(rs, 'def root_banks():') == 1291,
        'tools/b698_record.py :1291 (root_banks) ; tools/b699_record.py :%d (ROOT_EXCLUDE, b699`s, defects among the excluded)' % first(r9, 'R.ROOT_EXCLUDE = re.compile'), '0-1')
    add('ferry read-first', 'b672`s generator roster by path', os.path.exists(p('data', 'b672_roster_read.json')), 'data/b672_roster_read.json', '0-2')
    add('ferry read-first', 'the mirror roster (MANIFEST.md of the latest export)', os.path.exists(K.MIRROR_ZIP), '%s (MANIFEST.md inside)' % K.MIRROR_ZIP, '0-2')
    cg = [f for f in sorted(os.listdir(D)) if f.startswith('b692_circuit') and f.endswith('.txt')]
    add('ferry read-first', 'data/b692_circuit*.txt (the readings by row)', len(cg) >= 5, '%d banks: %s' % (len(cg), ', '.join(cg)), '0-2')
    add('ferry read-first', 'tools/correspondence_gen.py', 'read_carry' in (rd(p('tools', 'correspondence_gen.py')) or ''), 'tools/correspondence_gen.py :247', '0-2')
    po = rd(p('data', 'b699_closing_push_out.txt')) or ''
    add('ferry read-first', 'data/b699_closing_push_out.txt (commit at the start)', 'main read back at the remote: 85dd43d7' in po
        and not (g(ROOT, 'ls-files', 'data/b699_closing_push_out.txt')[1] or '').strip(), 'untracked at the working tree', '0')
    # ### (R310)(1)
    add('ruling (1)', 'the head line quoted from data/b699_closing.txt :1', cl[0] == ('b699 closed: relay 144cc457, PLACE-papers 049855a; suite 121 of 121; '
                                                                                   'root 4f7afcb30a75e63c\u2026; 4 prompts answered; 3 defects'), cl[0][:120], '1')
    add('ruling (1)', 'the closing pushed and read back at relay main 85dd43d7', 'main read back at the remote: 85dd43d7' in po, 'data/b699_closing_push_out.txt', '1')
    aj = json.loads(rd(p('data', 'b699_author_answers.json')) or '{}')
    add('ruling (1)', 'five prompts put, the root`s answer after the answers bank`s one write', len(re.findall(r'^### PROMPT ', rd(p('data', 'b699_author_answers.txt')) or '', re.M)) == 4
        and len(aj.get('calls') or []) == 3, 'data/b699_author_answers.txt (4 prompts, 3 calls) ; the fifth at the root, its check in data/b699_defects.txt :%d'
        % first(df, 'Option 1, land as composed'), '1')
    add('ruling (1)', 'b698`s weight line at FINDINGS :9710, the corrigendum at :9712', 'b698 AT ITS WEIGHT' in at(fi, 9710) and at(fi, 9712).startswith('## Corrigendum to b698'),
        'FINDINGS :9710, :9712', '1')
    co = lines_of(p('data', 'b699_corrigendum.txt'))
    add('ruling (1)', 'the corrigendum naming 2d19edd3 and 069778f6', any('2d19edd3' in l for l in co) and any('069778f6' in l for l in co), 'data/b699_corrigendum.txt', '1')
    cr = rd(p('data', 'b675_corrigenda.txt')) or ''
    add('ruling (1)', 'corrigenda rows (11)-(13)', all(('  (%d) ' % n) in cr for n in (11, 12, 13)), 'data/b675_corrigenda.txt', '1')
    cu = [l for l in lines_of(p('data', 'b699_cut.txt')) if l.strip()]   # ### the last non-empty line (the bank ends in a newline)
    add('ruling (1)', 'the re-cut: distance 1 to 0, v0.4.1, prints equal, 0 quoting lines', 'THE DISTANCE BEFORE 1, AFTER 0 ; TAG v0.4.1 ; PRINTS EQUAL ; QUOTING LINES 0' in (cu[-1] if cu else ''),
        'data/b699_cut.txt :%d' % first(lines_of(p('data', 'b699_cut.txt')), '### ### **SIDE-substrate-cluster RE-CUT'), '1')
    tp = g('D:/SIDE-substrate-cluster', 'rev-parse', '--short=7', 'v0.4.1^{commit}')[1].strip()
    add('ruling (1)', 'merged at 0c98a9a and tagged v0.4.1 naming v0.4', tp == '0c98a9a' and 'the prior tag v0.4' in g('D:/SIDE-substrate-cluster', 'tag', '-l', '-n9', 'v0.4.1')[1],
        'SIDE-substrate-cluster v0.4.1 peels %s' % tp, '1')
    pa = lines_of(os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE_v0_7.md'))
    add('ruling (1)', 'PATHS_TO_THE_CRITICAL_LINE_v0_7 :285 (v0.1.1, the profile, DERIVES)', '| SIDE-archimedean v0.1.1 |' in at(pa, 285) and '**DERIVES** —' in at(pa, 285),
        'PLACE-papers phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md :285', '1')
    add('ruling (1)', 'the partner copy differing in 24 lines against the 4 stored, OPEN_TRAILS :15332', 'differ in 24 lines' in at(ot, 15332) and 'reads 4' in at(ot, 15332),
        'OPEN_TRAILS :15332', '1')
    pz = [l for l in pl if l.strip()]   # ### the last non-empty line (the bank ends in a newline)
    add('ruling (1)', 'all 14 binders and their translations; one dispatch; nothing compiled', 'BINDERS 14 PRINTED WITH THEIR TRANSLATIONS' in (pz[-1] if pz else '')
        and 'NOTHING COMPILED' in (pz[-1] if pz else ''), 'data/b699_bridge_plan.txt :%d' % first(pl, '### ### **BINDERS 14'), '1')
    for f in ('b699_checks.txt', 'b699_checks_postpush.txt'):
        add('ruling (1)', 'suite 121 of 121 (%s)' % f, 'ARMS RUN : 121. ### LIVE PASSING : 121.' in (rd(p('data', f)) or ''), 'data/%s' % f, '1')
    sc = rd(p('data', 'b699_scores_close.json')) or ''
    add('ruling (1)', 'all eight scores HELD', sc.count('"HELD"') >= 8, 'data/b699_scores_close.json (HELD %d)' % sc.count('"HELD"'), '1')
    mi = rd(p('data', 'b699_mirror.txt')) or ''
    add('ruling (1)', 'mirror-refresh-2026-10-21-b699.zip CLEAN with the root line', 'Act root: b699 4f7afcb3' in mi and 'CLEAN ON ALL THREE CLAUSES' in mi, 'data/b699_mirror.txt', '1')
    add('ruling (1)', 'the trail at OPEN_TRAILS :15336 listing b698`s four defects', first(ot[15335:15370], "**Defects** (relay data/b699_defects.txt): (a) THE SEAT'S: A FIGURE IN A PROMPT NOT RECOUNTED") > 0,
        'OPEN_TRAILS :%d' % (15335 + first(ot[15335:15370], '**Defects** (relay data/b699_defects.txt)')), '1')
    ar = json.loads(rd(p('data', 'b699_act_root.json')) or '{}')
    named = [it.split()[0] for it in ar.get('items') or [] if it.startswith('data/')]
    add('ruling (1)', 'the root names the answers and citation banks, not the defects bank', 'data/b699_author_answers.txt' in named and 'data/b699_citation_check.txt' in named
        and 'data/b699_defects.txt' not in named, 'data/b699_act_root.json (banks %d ; the defects bank named %s)' % (len(named), 'data/b699_defects.txt' in named), '1')
    # ### (R310)(2)
    add('ruling (2)', 'the corrigenda bank', bool(cr), 'data/b675_corrigenda.txt', '1')
    add('ruling (2)', 'the sealed face and trail', os.path.exists(p(*K.B699_FACE.split('/'))) and at(ot, K.B699_TRAIL).startswith('### b699'), '%s ; OPEN_TRAILS :%d' % (K.B699_FACE, K.B699_TRAIL), '1')
    add('ruling (2)', 'data/b700_tool_repairs.txt -- TO BE WRITTEN', not os.path.exists(p('data', 'b700_tool_repairs.txt')), 'absent, as ordered', '1')
    # ### (R310)(3)
    for f in ('b680_licensed.txt', 'b680_correspondence.txt', 'b680_orders.txt', 'b680_lag.txt', 'b680_residues.txt', 'b680_methods.txt', 'b680_ceiling.txt'):
        add('ruling (3)', 'b680`s value beside (%s)' % f, os.path.exists(p('data', f)), 'data/%s' % f, '2')
    for f in ('b690_r3_licensed.txt', 'b690_r3_corr.txt', 'b690_r3_orders.txt', 'b690_r3_lag.txt', 'b690_r3_rules.txt', 'b690_r3_arms.txt', 'b690_r3_p3.txt',
              'b690_r3_onecopy.txt', 'b690_r3_pair.txt', 'b690_r3_residues.txt', 'b690_r3_methods.txt'):
        add('ruling (3)', 'b690`s value beside (%s)' % f, os.path.exists(p('data', f)), 'data/%s' % f, '2')
    add('ruling (3)', 'b691`s scope repair', os.path.exists(p('data', 'b691_tool_repairs.txt')), 'data/b691_tool_repairs.txt', '2')
    add('ruling (3)', 'the faces page`s header tag (v0.26 = 82550e4 as it prints)', 'SIDE-explicit-formula v0.26 = `82550e4`' in at(lines_of(os.path.join(PP, K.FACES_PAGE)), 3),
        'THE_CLAUSE_AND_ITS_COMPILED_FACES.md :3', '2')
    add('ruling (3)', 'SIMPLICITY 18 and PATHS 24', 'DIFFER IN 18 LINES' in (rd(p('data', 'b698_onecopy.txt')) or '') and 'DIFFER IN 24 LINES' in (rd(p('data', 'b699_onecopy.txt')) or ''),
        'data/b698_onecopy.txt :61 ; data/b699_onecopy.txt', '2')
    add('ruling (3)', 'THE_TWO_THREE_SUBSTRATE among the roster-currency rows', os.path.exists(os.path.join(PP, 'phase1.5', 'deep-structure', 'THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md')),
        'PLACE-papers phase1.5/deep-structure/THE_TWO_THREE_SUBSTRATE_AND_THE_TRIVIUM.md :210-:212', '2')
    for k, t in (('SIDE-explicit-formula', 'v0.34'), ('SIDE-li-map', 'v0.1.1'), ('SIDE-spinor', 'v0.1.2'), ('SIDE-archimedean', 'v0.1.1'), ('SIDE-interfaces', 'v0.2.1'),
                 ('SIDE-simplicity', 'v0.1.2'), ('SIDE-substrate-cluster', 'v0.4.1')):
        add('ruling (3)', 'the kernel tag %s %s' % (k, t), bool(g('D:/' + k, 'rev-parse', '--verify', '--quiet', t + '^{commit}')[1].strip()), 'local tag present (read by ls-remote at Component 2)', '2')
    rt = [l.split()[0] for l in g('D:/SIDE-rcurve', 'tag', '-l')[1].split(NL) if l.strip()]
    add('ruling (3)', 'SIDE-rcurve (no tag named in the ruling)', bool(rt), 'SIDE-rcurve tags %s ; the highest read at Component 2' % rt, '2')
    add('ruling (3)', 'SUITE-LOAD`s factor where b692 banked it', os.path.exists(p('data', 'b692_suite_load.txt')), 'data/b692_suite_load.txt', '2')
    # ### (R310)(4)
    add('ruling (4)', 'W-ORD-EPSTEIN-COUNT-LEAN', 'W-ORD-EPSTEIN-COUNT-LEAN' in (rd(OT) or ''), 'OPEN_TRAILS', '3')
    add('ruling (4)', 'b689`s form', os.path.exists(p('data', 'b689_ferry.txt')), 'data/b689_ferry.txt', '3')
    # ### (R310)(5)
    for repo, bs in K.DELETE:
        for b in bs:
            add('ruling (5)', '%s %s (local)' % (os.path.basename(repo), b), branch_listed(repo, b), 'listed at the working repository before any delete', '0')
    for repo, b in K.DELETE_REMOTE:
        add('ruling (5)', '%s %s (remote)' % (os.path.basename(repo), b), bool(g(repo, 'branch', '-r', '--list', 'origin/' + b)[1].strip()),
            'the remote-tracking ref origin/%s at the working repository' % b, '0')
    # ### (R310)(6)-(8)
    add('ruling (6)', 'the READFIRST-CLOSURE reader', 'readfirst' in (rd(p('tools', 'circuit_read.py')) or ''), 'tools/circuit_read.py', '0')
    add('ruling (7)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b699_worklist.py')) or ''), 'tools/b699_worklist.py :25', '5')
    add('ruling (8)', 'b701 and b702', True, 'acts to come', '5')
    # ### the ferry
    add('ferry C1', 'b699`s entry and trail', (line(FI, K.B699_ENTRY) or '').startswith('## ') and (line(OT, K.B699_TRAIL) or '').startswith('### b699'),
        'FINDINGS :%d ; OPEN_TRAILS :%d' % (K.B699_ENTRY, K.B699_TRAIL), '1')
    for rule, cl_, comp in (('R278', (4,), '5'), ('R251', (3,), '5'), ('R254', (2,), '4')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C4', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '4')
    add('ferry', 'data/b680_rules.txt, binary banks', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt (1)', '4')
    add('ferry C4', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '4')
    add('ferry C4', 'the chain halves as b693 drew them', "CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b693'))" in (rd(p('tools', 'b693_worklist.py')) or ''),
        'tools/b693_worklist.py :52', '4')
    add('ferry C5', 'b673`s capture names', os.path.exists(p('data', 'b699_relay_push_out.txt')), 'data/b699_relay_push_out.txt (the form carried)', '5')
    add('ferry C5', 'the b670 form of the mirror', os.path.exists(p('data', 'b699_mirror.txt')), 'data/b699_mirror.txt (the form carried)', '5')
    add('ruling; ferry', 'data/b700_readfirst.txt -- a step-zero bank', True, 'a step-zero bank (exists %s)' % os.path.exists(p('data', 'b700_readfirst.txt')), '0')
    return R


def _write(L, R, miss):
    for name, data in (('b700_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b700_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b700 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; (R310)(6)) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b700_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b700_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b700_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b700_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b700."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    # ### b698's and b699's widening carried: the commit reach includes the kernels the acts read; b682's tool unedited
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, 'D:/SIDE-lv-conservation', 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster')
                                     if r not in P.REPOS)
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b700'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b700')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b700)', 'exec'), ns)
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
        print('usage: b700_citation.py check [dry] | ferry | answer <needle> | word <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
