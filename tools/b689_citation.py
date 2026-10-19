# -*- coding: utf-8 -*-
"""b689_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b689's step zero; the ferry banked before
it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (2c300355, a new session); the answer route is b682's, imported from tools/b682_citation.py with its act names pointed at b689.
### Routes: `check` -> data/b689_citation_check.txt (.json) ; `ferry` -> data/b689_ferry_scan.txt ; `answer <needle>` -> the check on one
###         answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b689 from b688_citation.py's form; this tool writes only the banks named above.
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
import b689_worklist as K   # noqa: E402

C.SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
NL = chr(10)
PP = C.PP
C.ANCHOR, C.TAIL = 'RULING (R299) BEGIN', 'FERRY END (part 1 of 1)'
ANCHOR, TAIL = C.ANCHOR, C.TAIL
g, rd, line, commit_in, subject, branch_listed, rule_clause = (C.g, C.rd, C.line, C.commit_in, C.subject, C.branch_listed, C.rule_clause)
LM, SP, EF = 'D:/SIDE-li-map', 'D:/SIDE-spinor', K.KERNEL
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def act_root_line(act):
    t = rd(os.path.join(D, 'act_roots.txt')) or ''
    return [l.split() for l in t.split(NL) if l.strip() and l.split()[0] == act]


def peel(repo, tag):
    return g(repo, 'rev-parse', '--short', '%s^{commit}' % tag)[1].strip()


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
    # ### the ferry's read-first list
    for f in ('data/b688_closing.txt', 'data/b688_defects.txt', 'data/b688_citation_check.txt', 'tools/b678_corrigendum.py',
              'data/b679_strip_plan.txt', 'data/b676_strip_uses.txt', 'data/b679_q0_membership.txt', 'data/b687_p3_status.txt',
              'data/b688_closing_push_out.txt', 'data/b679_runner_run39064453563.txt', 'data/b679_axioms_run39064453563.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    dl = rd(p('data', 'b688_defects.txt')) or ''
    add('ferry read-first', 'data/b688_defects.txt (f) by line', (line(p('data', 'b688_defects.txt'), 34) or '').startswith('    (f) THE SEAT'),
        'data/b688_defects.txt :34', '0-1')
    for n, sha in ((96, 'b515e6b'), (107, '9e02bc0'), (116, 'aca59d1')):
        add('ferry read-first; ruling (2)', 'the commit-cite row %s' % sha, (line(p('data', 'b688_citation_check.txt'), n) or '').strip() == 'MISS | commit | %s' % sha,
            'data/b688_citation_check.txt :%d, its tested-directly note beneath' % n, '1')
    add('ferry read-first; ruling (1)-(2)', 'FINDINGS :9314 the b688 entry', (line(FIND, K.B688_ENTRY) or '').startswith('## SIDE-li-map re-cut'),
        (line(FIND, K.B688_ENTRY) or '')[:60], '1')
    add('ruling (2)', 'the entry`s figure "two commit cites" (FINDINGS :9320, the citation sentence of the :9314 entry)',
        'two commit cites outside the route’s repositories tested directly' in (line(FIND, K.B688_CITE_SENTENCE) or ''), 'FINDINGS :9320', '1')
    add('ferry read-first; ruling (2)', 'the trail record`s defects line for b688', (line(OT, K.B688_TRAIL_DEFECTS) or '').startswith('**Defects** (relay data/b688_defects.txt)')
        and 'THE CITATION BANK TESTS THREE' in (line(OT, K.B688_TRAIL_DEFECTS) or ''), 'OPEN_TRAILS :14946 (its (f) gives the figure three)', '1')
    add('ruling (2)', 'the corrigenda bank (data/b675_corrigenda.txt)', 'THE CORRIGENDA' in (line(p('data', 'b675_corrigenda.txt'), 1) or ''),
        'data/b675_corrigenda.txt :1, rows (1)-(2)', '1')
    add('ruling (2)', 'tools/b678_corrigendum.py`s routes and its landing through b678_record', 'def main(route)' in (rd(p('tools', 'b678_corrigendum.py')) or '')
        and 'REC.land' in (rd(p('tools', 'b678_corrigendum.py')) or ''), 'tools/b678_corrigendum.py :143-:167 (dry | land), :82 _quote', '1')
    add('ferry read-first; ruling (2)', 'the shared tool holding G-RULE-HEAD-LINE-QUOTED', (line(p(*K.ARM_TOOL.split('/')), K.ARM_LINE) or '').strip()
        == "if name == 'G-RULE-HEAD-LINE-QUOTED':", 'tools/rule_arms.py :387-:391 (the reading), :466 (the planted case), :228-:229 (the inputs)', '1')
    # ### (R299)(1): b688 at its weight
    head = (rd(p('data', 'b688_closing.txt')) or '').split(NL)[0]
    add('ruling (1)', 'the head line quoted from data/b688_closing.txt :1', head == ('b688 closed: relay 4bee98dc, PLACE-papers c3af808; suite 116 of 117; root '
                                                                                   'f168527e8655305c\u2026; 4 prompts answered; 6 defects'), head[:120], '1')
    po = rd(p('data', 'b688_closing_push_out.txt')) or ''
    add('ruling (1)', 'the closing at relay 007d4ead read back', '4bee98dc..007d4ead' in po and 'read back at the remote: 007d4ead' in po,
        'data/b688_closing_push_out.txt', '0-1')
    add('ruling (1)', 'SIDE-li-map 14 prints equal', 'PRINTS BEFORE 14 LINES ; AFTER 14 LINES ; DIFFERING 0 ; EQUAL LINE FOR LINE True' in (rd(p('data', 'b688_prints_SIDE-li-map.txt')) or ''),
        'data/b688_prints_SIDE-li-map.txt, its verdict line', '1')
    add('ruling (1)', 'SIDE-li-map merged at 9e02bc0, v0.1.1; b515e6b v0.1 without a tag', peel(LM, 'v0.1.1') == '9e02bc0' and commit_in(LM, 'b515e6b')
        and not g(LM, 'tag', '--list', 'v0.1')[1].strip(), 'git -C D:/SIDE-li-map rev-parse v0.1.1^{commit} ; tag --list v0.1 empty', '1')
    add('ruling (1)', 'the pin row beneath the licensed table', 'PIN ROW -- appended by b688' in (line(p('data', 'b670_licensed_table.txt'), 285) or ''),
        'data/b670_licensed_table.txt :285', '1')
    ct = rd(p('data', 'b688_cut.txt')) or ''
    add('ruling (1)', 'the two SIDE-li-map residues carried', 'PrimeLedgerPositivity.lean :29' in ct and 'NonnegStream' in ct, 'data/b688_cut.txt (residues)', '1')
    add('ruling (1)', 'W-ORD-CORRESPONDENCE-CARRIED-AT at OPEN_TRAILS :14922', 'W-ORD-CORRESPONDENCE-CARRIED-AT' in (line(OT, 14922) or ''), 'OPEN_TRAILS :14922', '1')
    add('ruling (1)', 'both dry runs banked', os.path.exists(p('data', 'b688_correspondence_dry.txt')) and os.path.exists(p('data', 'b688_correspondence_dry_2.txt')),
        'data/b688_correspondence_dry.txt, data/b688_correspondence_dry_2.txt', '1')
    sl = g(SP, 'show', 'v0.1.2:SIDESpinor/SpinorLeg.lean')[1].split(NL)
    add('ruling (1)', 'R4: "(salt-checked)" struck at SpinorLeg.lean :21, v0.1.2 at 7e570ee', peel(SP, 'v0.1.2') == '7e570ee' and len(sl) > 20
        and '(salt-checked)' not in sl[20], 'git -C D:/SIDE-spinor show v0.1.2:SIDESpinor/SpinorLeg.lean :21', '1')
    add('ruling (1)', 'SIDE-spinor 15 prints equal', 'PRINTS BEFORE 15 LINES ; AFTER 15 LINES ; DIFFERING 0 ; EQUAL LINE FOR LINE True' in (rd(p('data', 'b688_prints_SIDE-spinor.txt')) or ''),
        'data/b688_prints_SIDE-spinor.txt, its verdict line', '1')
    add('ruling (1)', 'the faces line amended "the local count T-COUNT (P3) derived"', 'the local count T-COUNT (P3) derived' in (rd(os.path.join(PP, 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md')) or ''),
        'THE_CLAUSE_AND_ITS_COMPILED_FACES.md', '1')
    add('ruling (1)', 'the lattice route: three-point overlap 3 of 3, six consuming rows', 'THE THREE-POINT CHECK OVERLAP 3 OF 3 ; THE ROWS THAT CONSUMED IT 6' in (rd(p('data', 'b688_lattice_route.txt')) or ''),
        'data/b688_lattice_route.txt, its verdict line', '1')
    for f in ('b688_checks.txt', 'b688_checks_postpush.txt'):
        add('ruling (1)', 'suite 116 of 117, G-RULE-HEAD-LINE-QUOTED declared (%s)' % f, "ARMS RUN : 117. ### LIVE PASSING : 116. ### LIVE FAILING : 1 ['G-RULE-HEAD-LINE-QUOTED']"
            in (rd(p('data', f)) or ''), 'data/%s' % f, '1')
    sc = json.load(open(p('data', 'b688_scores_close.json'), encoding='utf-8'))
    add('ruling (1)', 'all eight scores HELD', all(sc[k][0] == 'HELD' for k in ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')), 'data/b688_scores_close.json', '1')
    add('ruling (1)', 'root f168527e over 61 banks', any(r[1].startswith('f168527e8655305c') for r in act_root_line('b688'))
        and 'BANKS 61 ; CLEAN AND EQUAL AT HEAD 61' in (rd(p('data', 'b688_root_banks.txt')) or ''), 'data/act_roots.txt; data/b688_root_banks.txt', '1')
    add('ruling (1)', 'the b688 mirror CLEAN with the root line', os.path.exists('D:/MY-DOwnloads/mirror-refresh-2026-10-19-b688.zip')
        and 'VERDICT: CLEAN ON ALL THREE CLAUSES' in (rd(p('data', 'b688_mirror_verify.txt')) or '')
        and 'Act root: b688 f168527e' in (rd(p('data', 'b688_mirror.txt')) or ''), 'the zip; data/b688_mirror_verify.txt; data/b688_mirror.txt', '1')
    add('ruling (1)', 'six defects (a)-(f), every one the seat`s', re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", dl, re.M) == [
        ('a', 'SEAT'), ('b', 'SEAT'), ('c', 'SEAT'), ('d', 'SEAT'), ('e', 'SEAT'), ('f', 'SEAT')], 'data/b688_defects.txt :5-:40', '1')
    # ### (R299)(3): the research question, from the banks
    spt = rd(p(*K.STRIP_PLAN.split('/'))) or ''
    add('ruling (3); ferry', 'data/b679_strip_plan.txt section 11 (:224-:239)', (line(p('data', 'b679_strip_plan.txt'), 224) or '').startswith('== 11. THE AUTHOR')
        and 'S5\'\' over WideConfig with ρ ≠ 0 alone' in spt, 'data/b679_strip_plan.txt :224, :227', '2')
    su = rd(p(*K.STRIP_USES.split('/'))) or ''
    add('ruling (3); ferry', 'data/b676_strip_uses.txt, 22 rows (:9-:30)', len([l for l in su.split(NL)[8:30] if l.startswith('  Li')]) == 22
        and 'USES 22 (V5 12, THE COMPOSITION 10)' in su, 'data/b676_strip_uses.txt :9-:30, :46', '2')
    cv = g(EF, 'show', 'v0.33:SIDEExplicitFormula/Schema/Wide/Converse.lean')[1].split(NL)
    cf = g(EF, 'show', 'v0.33:SIDEExplicitFormula/Schema/Wide/Config.lean')[1].split(NL)
    add('ruling (3); ferry', 'v0.33 Wide.li_nonneg_cfg_imp_online', len(cv) > 191 and cv[190].startswith('theorem li_nonneg_cfg_imp_online (Z : WideConfig)'),
        'SIDEExplicitFormula/Schema/Wide/Converse.lean :191-:192 at v0.33', '2')
    add('ruling (3); ferry', 'v0.33 HExcl "every real point has Re > 0"', len(cf) > 54 and cf[53] == 'def HExcl (Z : WideConfig) : Prop := ∀ ρ ∈ Z.carrier, ρ.im = 0 → 0 < ρ.re',
        'SIDEExplicitFormula/Schema/Wide/Config.lean :54 at v0.33', '2')
    add('ferry', 'v0.33 WideConfig', any(l.startswith('structure WideConfig') for l in cf), 'SIDEExplicitFormula/Schema/Wide/Config.lean (structure WideConfig)', '2')
    add('ruling (4)', 'v0.33 peeled at 95f8dc8, main at it', peel(EF, 'v0.33') == K.V033 and g(EF, 'rev-parse', '--short', 'main')[1].strip() == K.V033,
        'git -C D:/SIDE-explicit-formula rev-parse v0.33^{commit} ; main', '3')
    add('ruling (4)', 'v0.34 free; the branch strip-free-b689 absent', not g(EF, 'tag', '--list', 'v0.34')[1].strip() and not branch_listed(EF, K.BRANCH),
        'tag --list v0.34 ; branch --list strip-free-b689', '3')
    rb = rd(p('data', 'b679_runner_run39064453563.txt')) or ''
    add('ferry read-first; ruling (3)', 'the v0.33 print bank and C2, C2b by row', 'Wide.c2_not_excl' in (line(p('data', 'b679_runner_run39064453563.txt'), 66) or '')
        and 'Wide.c2b_nonneg_offline' in (line(p('data', 'b679_runner_run39064453563.txt'), 68) or '') and 'DERIVES' in rb,
        'data/b679_runner_run39064453563.txt :66, :68 (run at 46ee9a4, merged as 95f8dc8)', '2')
    qm = rd(p('data', 'b679_q0_membership.txt')) or ''
    add('ferry read-first; ruling (5)', 'b679`s HExcl check at Q0 (Z_Q negative on (−1/2, 0], Z_Q(0) = −1)', 'HExcl (no real point in (-1/2, 0])   HOLDS' in qm
        and 'BALLS 35 ; EXCLUDING 0 35 ; NEGATIVE 35' in qm and 'Z_Q(0) -1.0000000' in qm, 'data/b679_q0_membership.txt :19, the verdict line', '4')
    add('ruling (5)', 'T-COUNT as P3 DERIVED', 'AFTER:  DERIVED' in (rd(p('data', 'b687_p3_status.txt')) or ''), 'data/b687_p3_status.txt :8', '4')
    add('ruling (4)', 'n*` and the constants at v0.33 (b679`s onset bank)', 'n*' in (rd(p('data', 'b679_onset.txt')) or ''), 'data/b679_onset.txt', '3')
    # ### (R299)(6): branches
    for repo, bs in K.DELETE:
        for b in bs:
            add('ruling (6)', '%s %s' % (os.path.basename(repo), b), branch_listed(repo, b), 'git branch --list', '0')
    add('ruling (6)', 'data/b688_closing_push_out.txt untracked, to be committed', g(ROOT, 'ls-files', '--error-unmatch', 'data/b688_closing_push_out.txt')[0] != 0,
        'not tracked', '0')
    # ### (R299)(8)-(9)
    add('ruling (8)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b688_worklist.py')) or ''), 'tools/b688_worklist.py', '6')
    lt = rd(p('data', 'b670_licensed_table.txt')) or ''
    add('ruling (9)', 'SIDE-archimedean and SIDE-rcurve tied at 2', 'SIDE-archimedean docstrings (read at 8019d9d)                     2 ->    2' in lt
        and 'SIDE-rcurve docstrings (read at d5f33b4)                          2 ->    2' in lt, 'data/b670_licensed_table.txt :100, :113', '6')
    add('ruling (9)', 'b674`s tie-break rule', '(2) THE TIE-BREAK BEYOND THE COUNT' in (line(p('data', 'b674_rules.txt'), 8) or ''), 'data/b674_rules.txt :8-:11', '6')
    for rule, cl_, comp in (('R278', (4,), '6'), ('R251', (3,), '6'), ('R254', (2,), '5')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C5', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '5')
    add('ferry', 'data/b680_rules.txt, binary banks', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt (1)', '5')
    add('ferry', 'the four parts (data/b684_rules.txt row (1))', 'A SUITE PART OVER 450 s SPLITS THE NEXT RUN' in (rd(p('data', 'b684_rules.txt')) or ''), 'data/b684_rules.txt :5', '5')
    add('ferry C5', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '5')
    for b in ('b689_readfirst.txt', 'b689_plan.txt', 'b689_tool_repairs.txt', 'b689_grade.txt', 'b689_obstruction.txt', 'b689_q0_reread.txt',
              'b689_faces_rows.txt'):
        sz = b == 'b689_readfirst.txt'
        add('ruling; ferry', 'data/%s -- TO BE WRITTEN, not a cite' % b, sz or not os.path.exists(p('data', b)),
            ('a step-zero bank (exists %s)' % os.path.exists(p('data', b))) if sz else 'absent, as ordered', '0-5')
    return R


def _write(L, R, miss):
    for name, data in (('b689_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b689_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b689 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the source: the ruling and the ferry as pasted, read from the session transcript (%d characters, %r to %r); every cite checked at '
         'HEAD; rows are cites: where | what | OK or MISS | how | the component that cites it.' % (len(text), ANCHOR, TAIL), '']
    for where, what, ok, how, comp in R:
        L.append('  %-4s | %s | %s | %s | Component %s' % ('OK' if ok else 'MISS', where, what, how, comp))
    L += ['', '### THE MISSES, EACH RAISED TO THE AUTHOR BEFORE THE COMPONENT THAT CITES IT RUNS (none repaired silently):']
    L += ['  %s -- %s (Component %s)' % (what, how, comp) for _w, what, ok, how, comp in miss] or ['  NONE']
    L += ['', '### ### **CITES CHECKED %d ; OK %d ; MISSES %d.**' % (len(R), len(R) - len(miss), len(miss))]
    _write(L, R, miss)
    print(NL.join(L[-(len(miss) + 4):]))


def ferry(*a):
    """the ferry is banked by the Write tool (data/b689_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b689_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b689_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b689_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b689."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b689'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b689')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b689)', 'exec'), ns)
    ns['answer'](needle)


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b689_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
