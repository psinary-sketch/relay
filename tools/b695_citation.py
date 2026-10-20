# -*- coding: utf-8 -*-
"""b695_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b695's step zero; the ferry banked before
it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (b97f6790); the answer route is b682's, imported from tools/b682_citation.py with its act names pointed at b695; the `word` route
### is b694's (a bare BEGIN ... END paste read as the author's word).
### Routes: `check` -> data/b695_citation_check.txt (.json) ; `ferry` -> data/b695_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the
###         check on one answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b695 from b694_citation.py's form; this tool writes only the banks named above.
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
import b695_worklist as K   # noqa: E402

C.SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
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


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    FI = os.path.join(PP, 'FINDINGS.md')
    # ### the ferry's read-first list
    for f in ('data/b694_closing.txt', 'data/b694_defects.txt', 'data/b694_witness.txt', 'data/b694_witness_plan.txt',
              'data/b694_witness_concentration.txt', 'data/b694_circuit_dominance.txt', 'data/b694_faces_rows.txt', 'data/b690_nodes_zeta.txt',
              'data/b692_circuit_spec.txt', 'data/b694_circuit_SIDE-lv-conservation_v0.13.0_png_hashes.txt',
              'data/b694_circuit_SIDE-lv-conservation_v0.13.0.png', 'data/b670_licensed_table.txt', 'data/b674_rules.txt', 'data/b690_rules.txt',
              'data/b692_rules.txt', 'data/b694_rules.txt', 'tools/correspondence_gen.py', 'tools/chain_page.py', 'data/b694_closing_push_out.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    # ### (R305)(1)
    cl = (rd(p('data', 'b694_closing.txt')) or '').split(NL)
    add('ruling (1)', 'the head line quoted from data/b694_closing.txt :1', cl[0] == ('b694 closed: relay 0c1287a2, PLACE-papers 4a21fa9; suite 122 of 124; '
                                                                                   'root 012ffed645f69af6\u2026; 6 prompts answered; 12 defects'), cl[0][:120], '1')
    po = rd(p('data', 'b694_closing_push_out.txt')) or ''
    add('ruling (1)', 'the closing commit 6e451686 pushed and read back at relay main', 'main read back at the remote: 6e451686' in po,
        'data/b694_closing_push_out.txt :5', '0-1')
    wt = (rd(p('data', 'b694_witness.txt')) or '').split(NL)
    add('ruling (1)', 'FOUND at every width a = 32 to 192, the narrowest margin at a = 32, -7.7752874967979 +- 1.43e-18', len(wt) > 34
        and 'S -7.7752874967979 +- 1.43e-18' in wt[14] and 'FOUND AT WIDTHS 32, 48, 64, 96, 128, 192' in wt[33], 'data/b694_witness.txt :15, :34', '1')
    add('ruling (1)', 'positive at 14.1, 16 and 24', len(wt) > 31 and 'positive at a = 14.106736, 16 and 24' in wt[30], 'data/b694_witness.txt :31', '1')
    add('ruling (1)', 'the identity over 182 certified zeros', len(wt) > 8 and 'Z over 182 zeros below 151.59' in wt[7], 'data/b694_witness.txt :8', '1')
    zs = [float(x) for x in re.findall(r'identity AGREE \(Z - S (-?[\d.]+e-\d+)', '\n'.join(wt))]
    add('ruling (1)', 'the identity to between 1e-13 and 1e-25 (the N and C rows)', zs and max(abs(z) for z in zs) < 1e-12 and min(abs(z) for z in zs) > 1e-26,
        'data/b694_witness.txt :12-:28, |Z - S| from %.2e to %.2e over %d rows' % (min(abs(z) for z in zs), max(abs(z) for z in zs), len(zs)) if zs else 'none read', '1')
    wc = rd(p('data', 'b694_witness_controls.txt')) or ''
    add('ruling (1)', 'the identity control at all 34 cells ; the zeta control at all 16', '34 OF 34' in wc.upper() or '34 of 34' in wc, 'data/b694_witness_controls.txt', '1')
    add('ruling (1)', 'the centred family positive at every width', all('NONNEGATIVE BEYOND ITS BOUND' in l for l in wt[20:28]), 'data/b694_witness.txt :21-:28', '1')
    rn = rd(p('data', 'b694_runner_SIDE-lv-conservation_after.txt')) or ''
    add('ruling (1)', 'the closure step at d38f3e8, run 39465780735, eight terminals at the standard three', 'RUN 39465780735' in rn
        and 'TERMINALS PRINTED 8 OF 8' in rn and 'OUTSIDE THE STANDARD THREE 0' in rn, 'data/b694_runner_SIDE-lv-conservation_after.txt :30', '1')
    dm = (rd(p('data', 'b694_circuit_dominance.txt')) or '').split(NL)
    add('ruling (1)', 'CLAUSE-DOMINANCE 1 of 2 faces kernels', len(dm) > 12 and 'CLAUSE-DOMINANCE 1 OF 2 FACES KERNELS' in dm[11], 'data/b694_circuit_dominance.txt :12', '1')
    add('ruling (1)', 'SIDE-lv-conservation absent, the clause reaching it through the Correspondence row', len(dm) > 8 and dm[7].strip().startswith('SIDE-lv-conservation')
        and '| ABSENT |' in dm[7] and '@corr SIDE-lv-conservation' in dm[7], 'data/b694_circuit_dominance.txt :8 (the row cites data/b690_nodes_zeta.txt :126 @corr)', '1')
    add('ruling (1)', 'b693`s weight line at FINDINGS :9540', (line(FI, 9540) or '').startswith('*Appended 2026-10-20 by b694 to b693'), (line(FI, 9540) or '')[:70], '1')
    add('ruling (1)', 'the corrigendum at FINDINGS :9542', 'orrigendum' in (line(FI, 9542) or '')[:200], (line(FI, 9542) or '')[:70], '1')
    add('ruling (1)', 'the deletes rule at data/b694_rules.txt row (1)', '(1) A DELETE COMMAND STANDS ALONE' in (line(p('data', 'b694_rules.txt'), 6) or ''),
        'data/b694_rules.txt :6', '1')
    for f, n in (('b694_checks.txt', 123), ('b694_checks_postpush.txt', 122)):
        t = rd(p('data', f)) or ''
        add('ruling (1)', 'suite %d of 124 (%s)' % (n, f), 'ARMS RUN : 124. ### LIVE PASSING : %d.' % n in t, 'data/%s' % f, '1')
    df = (rd(p('data', 'b694_defects.txt')) or '').split(NL)
    add('ruling (1)', 'defect (k) G-RULE-BINARY-HASHES by line', len(df) > 43 and df[42].startswith('    (k) THE SEAT'), 'data/b694_defects.txt :43-:51', '1-2')
    add('ruling (1)', 'defect (l) G-RULE-ONE-GIT-WRITE by line, at 18:38:58Z', len(df) > 52 and df[51].startswith('    (l) THE SEAT') and '18:38:58' in ' '.join(df[51:58]),
        'data/b694_defects.txt :52-:58', '1-2')
    add('ruling (1)', 'twelve defects (a)-(l)', re.findall(r"^    \(([a-z])\) THE ", NL.join(df), re.M) == list('abcdefghijkl'), 'data/b694_defects.txt', '1')
    sc = rd(p('data', 'b694_scores_close.json')) or ''
    add('ruling (1)', 'all eight scores HELD', sc.count('"HELD"') >= 8, 'data/b694_scores_close.json', '1')
    add('ruling (1)', 'sealed tools 11 of 11', len(cl) > 17 and 'AGREE 11 of 11' in cl[16], 'data/b694_closing.txt :17', '1')
    ar = act_root_line('b694')
    add('ruling (1)', 'root 012ffed6 over 77 banks', ar and ar[0][1].startswith('012ffed6') and 'BANKS 77' in (rd(p('data', 'b694_root_banks.txt')) or ''),
        'data/act_roots.txt :72 ; data/b694_root_banks.txt :83', '1')
    add('ruling (1)', 'mirror-refresh-2026-10-20-b694.zip CLEAN with the root line', os.path.exists('D:/MY-DOwnloads/mirror-refresh-2026-10-20-b694.zip')
        and 'Act root: b694 012ffed6' in (rd(p('data', 'b694_mirror.txt')) or '') and 'CLEAN ON ALL THREE CLAUSES' in (rd(p('data', 'b694_mirror.txt')) or ''),
        'the zip; data/b694_mirror.txt', '1')
    add('ruling (1)', 'left as they stand under data/b692_rules.txt row (1)', '(1) A COMMIT MADE AFTER THE SEAL THAT FAILS AN ARM IS LEFT AS IT STANDS'
        in (line(p('data', 'b692_rules.txt'), 5) or ''), 'data/b692_rules.txt :5', '1-2')
    # ### (R305)(2)
    ph = (rd(p('data', 'b694_circuit_SIDE-lv-conservation_v0.13.0_png_hashes.txt')) or '').split(NL)
    add('ruling (2)', 'the hashes bank`s PNG path as written (b692`s) and the file`s sha256 beside', len(ph) > 4
        and ph[3].strip().startswith('data/b692_circuit_SIDE-lv-conservation_v0.13.0.png | 148025d5'), 'data/b694_..._png_hashes.txt :4', '1-2')
    import hashlib
    pb = open(p('data', 'b694_circuit_SIDE-lv-conservation_v0.13.0.png'), 'rb').read() if os.path.exists(p('data', 'b694_circuit_SIDE-lv-conservation_v0.13.0.png')) else b''
    add('ruling (2)', 'the PNG as it should read, data/b694_..., its sha256 148025d5', hashlib.sha256(pb).hexdigest().startswith('148025d5'),
        'sha256 of data/b694_circuit_SIDE-lv-conservation_v0.13.0.png %s' % hashlib.sha256(pb).hexdigest()[:16], '1-2')
    for f, sha in (('b694_relay_push_out.txt', '0c1287a2'), ('b694_pp_push_out.txt', '4a21fa9')):
        add('ruling (2)', 'the three writes` read-backs (%s)' % f, 'main read back at the remote: %s' % sha in (rd(p('data', f)) or ''), 'data/%s' % f, '1-2')
    add('ruling (2)', 'the corrigenda bank (additive)', os.path.exists(p('data', 'b675_corrigenda.txt')), 'data/b675_corrigenda.txt', '1')
    # ### (R305)(3)
    add('ruling (3)', 'data/b670_licensed_table.txt', os.path.exists(p('data', 'b670_licensed_table.txt')), 'data/b670_licensed_table.txt', '2')
    add('ruling (3)', 'b652`s order', 'the next kernel by descending count' in (line(p('data', 'b652_ferry.txt'), 19) or ''), 'data/b652_ferry.txt :19', '2')
    add('ruling (3)', 'b674`s tie-break rule', 'THE TIE-BREAK BEYOND THE COUNT' in (line(p('data', 'b674_rules.txt'), 8) or ''), 'data/b674_rules.txt :8-:11', '2')
    add('ruling (3)', 'the per-document tables: reading 3`s rows and the cut banks since', os.path.exists(p('data', 'b690_r3_licensed.txt'))
        and 'SIDE-archimedean RE-CUT: THE DISTANCE BEFORE 2, AFTER 0' in (rd(p('data', 'b693_cut.txt')) or ''), 'data/b690_r3_licensed.txt :41-:76 ; data/b693_cut.txt', '2')
    add('ruling (3)', 'b676`s form', os.path.exists(p('data', 'b676_cut.txt')), 'data/b676_cut.txt', '2')
    add('ruling (3)', 'rule (2) of data/b690_rules.txt', 'HAS A DISTINCTIVE SUBSTRING SEARCHED WITH GIT GREP' in (line(p('data', 'b690_rules.txt'), 9) or ''),
        'data/b690_rules.txt :9', '2')
    add('ruling (3)', 'tools/correspondence_gen.py as repaired at b691 (carried-at)', 'read_carry' in (rd(p('tools', 'correspondence_gen.py')) or ''),
        'tools/correspondence_gen.py', '2')
    # ### (R305)(4)
    fr = (rd(p('data', 'b694_faces_rows.txt')) or '').split(NL)
    add('ruling (4)', 'the drafted row of data/b694_faces_rows.txt', len(fr) > 16 and fr[7].strip().startswith('(1) DRAFTED'), 'data/b694_faces_rows.txt :8-:16', '3')
    nz = (rd(p('data', 'b690_nodes_zeta.txt')) or '').split(NL)
    add('ruling (4)', 'the Li-face line at Q0 as the page carries it (the b690 node list`s row)', len(nz) > 167 and nz[166].startswith('# backmatter:')
        and 'the Li face over the widened class' in nz[166], 'data/b690_nodes_zeta.txt :167', '3')
    add('ruling (4)', 'tools/chain_page.py`s backmatter channel', 'backmatter' in (rd(p('tools', 'chain_page.py')) or ''), 'tools/chain_page.py', '3')
    ol = line(OT, 15166) or ''
    add('ruling (4)', 'W-ORD-WITNESS-TAIL-BALLS`s line and trigger', 'W-ORD-WITNESS-TAIL-BALLS' in ol and 'before any faces-page row carrying the witness is regenerated' in ol,
        'OPEN_TRAILS :15166', '3')
    add('ruling (4)', 'W-ORD-B518-FLOAT`s line', 'W-ORD-B518-FLOAT' in (line(OT, 15168) or ''), 'OPEN_TRAILS :15168', '3')
    add('ruling (4)', 'data/b695_nodes_zeta.txt -- TO BE WRITTEN where the word is regenerate', not os.path.exists(p('data', 'b695_nodes_zeta.txt')), 'absent, as ordered', '3')
    # ### (R305)(5)
    sp = (rd(p('data', 'b692_circuit_spec.txt')) or '').split(NL)
    add('ruling (5)', 'data/b692_circuit_spec.txt`s ten rows', len(sp) > 54 and 'ROWS 10' in sp[53], 'data/b692_circuit_spec.txt :7-:52, :54', '3')
    hb = line(OT, 10257) or ''
    add('ruling (5)', 'W-ORD-H2-BRIDGE ((R128)(2)) at OPEN_TRAILS', 'W-ORD-H2-BRIDGE' in hb and hb.startswith('(2)'), 'OPEN_TRAILS :10257 (filed under (R128)(2))', '3')
    ok, how = rule_clause('R128', (2,))
    add('ruling (5)', '(R128)(2)', ok, how, '3')
    # ### (R305)(6): branches -- deleted at step zero before this check ran (data/b695_branches.txt; data/b695_defects.txt (a))
    br = rd(p('data', 'b695_branches.txt')) or ''
    for repo, bs in K.DELETE:
        for b in bs:
            add('ruling (6)', '%s %s (local)' % (os.path.basename(repo), b), not branch_listed(repo, b) and b in br,
                'deleted at step zero, listed --merged before (data/b695_branches.txt)', '0')
    add('ruling (6)', 'data/b694_closing_push_out.txt committed at the start', commit_in(ROOT, '12c223b1')
        and (g(ROOT, 'show', '--name-only', '--format=', '12c223b1')[1] or '').split() == ['data/b694_closing_push_out.txt'], 'relay 12c223b1', '0')
    # ### (R305)(7)-(9)
    add('ruling (8)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b695_worklist.py')) or ''), 'tools/b695_worklist.py', '5')
    for nm in ('W-ORD-WITNESS-TAIL-BALLS', 'W-ORD-EPSTEIN-COUNT-LEAN'):
        add('ruling (9)', nm, nm in (rd(OT) or ''), 'OPEN_TRAILS', '5')
    add('ruling (9)', 'the regularity-uses bank', 'REGULARITY-USES BANK' in (rd(p('data', 'b692_candidates_priced.txt')) or ''), 'data/b692_candidates_priced.txt', '5')
    for rule, cl_, comp in (('R278', (4,), '5'), ('R251', (3,), '5'), ('R254', (2,), '4')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C4', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '4')
    add('ferry', 'data/b680_rules.txt, binary banks', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt (1)', '2-4')
    add('ferry C4', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '4')
    add('ferry C4', 'the chain halves as b693 drew them', "CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b693'))" in (rd(p('tools', 'b693_worklist.py')) or ''),
        'tools/b693_worklist.py :52', '4')
    add('ferry C5', 'b673`s capture names', os.path.exists(p('data', 'b673_closing_push_out.txt')) or os.path.exists(p('data', 'b694_relay_push_out.txt')),
        'data/b694_relay_push_out.txt (the form carried)', '5')
    for b in ('b695_readfirst.txt', 'b695_tool_repairs.txt', 'b695_cut.txt', 'b695_circuit_spec.txt'):
        sz = b == 'b695_readfirst.txt'
        add('ruling; ferry', 'data/%s -- TO BE WRITTEN, not a cite' % b, sz or not os.path.exists(p('data', b)),
            ('a step-zero bank (exists %s)' % os.path.exists(p('data', b))) if sz else 'absent, as ordered', '0-4')
    return R


def _write(L, R, miss):
    for name, data in (('b695_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b695_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b695 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b695_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b695_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b695_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b695_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b695."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b695'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b695')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b695)', 'exec'), ns)
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
        print('usage: b695_citation.py check [dry] | ferry | answer <needle> | word <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
