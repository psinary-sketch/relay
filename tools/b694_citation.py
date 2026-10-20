# -*- coding: utf-8 -*-
"""b694_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b694's step zero; the ferry banked before
it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (b97f6790); the answer route is b682's, imported from tools/b682_citation.py with its act names pointed at b694.
### Routes: `check` -> data/b694_citation_check.txt (.json) ; `ferry` -> data/b694_ferry_scan.txt ; `answer <needle>` -> the check on one
###         answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b694 from b693_citation.py's form; this tool writes only the banks named above.
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
import b694_worklist as K   # noqa: E402

C.SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID
NL = chr(10)
PP = C.PP
C.ANCHOR, C.TAIL = K.ANCHOR, K.TAIL
ANCHOR, TAIL = C.ANCHOR, C.TAIL
g, rd, line, commit_in, subject, branch_listed, rule_clause = (C.g, C.rd, C.line, C.commit_in, C.subject, C.branch_listed, C.rule_clause)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
EF = 'D:/SIDE-explicit-formula'


def act_root_line(act):
    t = rd(os.path.join(D, 'act_roots.txt')) or ''
    return [l.split() for l in t.split(NL) if l.strip() and l.split()[0] == act]


def jload(n):
    try:
        return json.load(open(os.path.join(D, n), encoding='utf-8'))
    except Exception:
        return {}


def shown(repo, rev, path):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '').split(NL) if r.returncode == 0 else []


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    FI = os.path.join(PP, 'FINDINGS.md')
    # ### the ferry's read-first list
    for f in ('data/b693_closing.txt', 'data/b693_defects.txt', 'data/b693_cut.txt', 'data/b693_tool_repairs.txt', 'tools/b693_closing.py',
              'tools/push_gated.sh', 'data/b692_circuit_spec.txt', 'data/b692_circuit_dominance.txt', 'data/b692_circuit_SIDE-explicit-formula_v0.34.1.txt',
              'tools/circuit_read.py', 'data/b690_nodes_zeta.txt', 'data/b681_epstein_zeros_narrowed_hashes.txt', 'data/b681_epstein_zeros_narrowed.json.gz',
              'data/b677_tolerance.txt', 'data/b675_li_bench.txt', 'data/b518_report.txt', 'data/b518_cells.jsonl', 'data/b693_closing_push_out.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    # ### (R304)(1)
    cl = (rd(p('data', 'b693_closing.txt')) or '').split(NL)
    add('ruling (1)', 'the head line quoted from data/b693_closing.txt :1', cl[0] == ('b693 closed: relay a96d5c38, PLACE-papers dba03d2; suite 121 of 122; '
                                                                                   'root eb2323dc6295a480\u2026; 4 prompts answered; 8 defects'), cl[0][:120], '1')
    po = rd(p('data', 'b693_closing_push_out.txt')) or ''
    add('ruling (1)', 'the closing pushed and read back at relay main 48ca2540', 'main read back at the remote: 48ca2540' in po,
        'data/b693_closing_push_out.txt :5', '0-1')
    for name, sha in (('C0-C3 done at 0574078e', '0574078e'), ('data/b693_resume.txt committed alone at 91c2df0c', '91c2df0c')):
        add('ruling (1)', name, commit_in(ROOT, sha), 'relay %s (%s)' % (sha, (subject(ROOT, sha) or '')[:70]), '1')
    files91 = (g(ROOT, 'show', '--name-only', '--format=', '91c2df0c')[1] or '').split()
    add('ruling (1)', 'the resume bank alone in its commit', files91 == ['data/b693_resume.txt'], 'git show --name-only 91c2df0c: %s' % files91, '1')
    wl = line(FI, 9498) or ''
    add('ruling (1)', 'b692`s weight line with both triage figures (FINDINGS :9498)', wl.startswith('*Appended 2026-10-19 by b693 to b692')
        and 'CARRY 11, DISCHARGED-BY-READING 24' in wl and 'CARRIED 12, DISCHARGED BY READING 23' in wl, wl[:70], '1')
    rx = rd(p('data', 'b693_range_exercise.txt')) or ''
    add('ruling (1)', 'the closing tool reading its defects range from the bank, "(a)–(m)" on b692`s', '(a)\u2013(m)' in rx or '(a)-(m)' in rx,
        'data/b693_range_exercise.txt', '1')
    cc = rd(p('data', 'b693_chain_control.txt')) or ''
    add('ruling (1)', 'the whole-chain control 70 of 70 AGREE, the boundary equal, the three equal', 'AGREE 70' in cc and 'EQUAL True' in cc,
        'data/b693_chain_control.txt', '1')
    rb = rd(p('data', 'b693_root_branch_push_out.txt')) or ''
    add('ruling (1)', 'push-b693-root pushed alone by the branch mode and read back at 59de04e1', 'branch push-b693-root read back at the remote: 59de04e1' in rb,
        'data/b693_root_branch_push_out.txt :9', '1')
    add('ruling (1)', 'main pushed from it', 'main read back at the remote: 59de04e1' in (rd(p('data', 'b693_root_push_out.txt')) or ''),
        'data/b693_root_push_out.txt', '1')
    add('ruling (1)', 'the re-cut`s document SIDE-archimedean, its rows, tag and quotation hits (data/b693_cut.txt)',
        'SIDE-archimedean' in (rd(p('data', 'b693_cut.txt')) or '') and 'v0.1.1' in (rd(p('data', 'b693_cut.txt')) or ''), 'data/b693_cut.txt', '1')
    for f in ('b693_checks.txt', 'b693_checks_postpush.txt'):
        t = rd(p('data', f)) or ''
        add('ruling (1)', 'suite 121 of 122, G-DELETES-ONE-BRANCH failing (%s)' % f, 'ARMS RUN : 122. ### LIVE PASSING : 121.' in t
            and 'G-DELETES-ONE-BRANCH' in t, 'data/%s' % f, '1')
    df = (rd(p('data', 'b693_defects.txt')) or '').split(NL)
    add('ruling (1)', 'defect (f): the eight deletes chained with "; echo EXIT $?"', len(df) > 35 and df[32].startswith('    (f) THE SEAT')
        and 'echo EXIT $?' in ' '.join(df[32:39]), 'data/b693_defects.txt :33-:39', '1')
    add('ruling (1)', 'defect (h): the closing row read under D:\\relay, the reads stored under D:/relay', len(df) > 50 and df[46].startswith('    (h) THE SEAT')
        and '`D:\\relay`' in ' '.join(df[46:54]) and '`D:/relay`' in ' '.join(df[46:54]), 'data/b693_defects.txt :47-:54', '1')
    add('ruling (1)', 'the closing`s push-b693-root row printing ABSENT', len(cl) > 225 and 'relay push-b693-root' in cl[225] and 'ABSENT' in cl[225],
        'data/b693_closing.txt :226', '1')
    src = (rd(p('tools', 'b693_closing.py')) or '').split(NL)
    add('ruling (1)', 'the sealed closing tool`s look-up: remote_refs(ROOT), ROOT by os.path', len(src) > 294 and 'remote_refs(ROOT)' in src[293]
        and src[23].startswith('ROOT = os.path.dirname'), 'tools/b693_closing.py :24, :294', '1')
    add('ruling (1)', 'its reads stored under D:/relay', len(src) > 274 and "paths = ['D:/' + r for r in REPOS]" in src[269] and 'p not in _REMOTE' in src[165],
        'tools/b693_closing.py :270, :166-:167', '1')
    ev = rd(p('data', 'b693_defects.txt')) or ''
    add('ruling (1)', 'the transient empty remote read of SIDE-fano-darkness, an event', 'SIDE-fano-darkness' in ev and 'EVENTS, NOT DEFECTS' in ev,
        'data/b693_defects.txt :123-:135', '1')
    add('ruling (1)', 'eight defects, (a)-(h), lettered', re.findall(r"^    \(([a-z])\) THE ", ev, re.M) == list('abcdefgh'), 'data/b693_defects.txt', '1')
    add('ruling (1)', 'the b693 mirror CLEAN with the root line', os.path.exists('D:/MY-DOwnloads/mirror-refresh-2026-10-19-b693.zip')
        and 'Act root: b693 eb2323dc' in (rd(p('data', 'b693_mirror.txt')) or ''), 'the zip; data/b693_mirror.txt', '1')
    # ### (R304)(2)
    po2 = (rd(p('data', 'b693_root_branch_push_out.txt')) or '').split(NL)
    add('ruling (2); ferry', 'THE ONE PATH FORM THE PUSH TOOL STORES, the closing`s reads to be looked up under it',
        len(po2) > 1 and 'push_gated: repo D:/relay' in po2[1],
        'the push tool stores the repository as given, "/d/relay" (data/b693_root_branch_push_out.txt :2; tools/push_gated.sh :118, :144); the closing '
        'tool`s reads are stored under "D:/relay" (tools/b693_closing.py :270, :274) and looked up under "D:\\relay" (:294): the form the reads are '
        'stored under is the closing tool`s own, not the push tool`s', '1')
    add('ruling (2)', 'G-DELETES-ONE-BRANCH an arm of b693`s suite', 'G-DELETES-ONE-BRANCH' in (rd(p('tools', 'b693_checks.py')) or ''), 'tools/b693_checks.py', '1')
    add('ruling (2)', 'the corrigenda bank (additive)', os.path.exists(p('data', 'b675_corrigenda.txt')), 'data/b675_corrigenda.txt', '1')
    # ### (R304)(3)
    sp = rd(p('data', 'b692_circuit_spec.txt')) or ''
    add('ruling (3); ferry', 'the faces kernels b692 carried, by name from data/b692_circuit_spec.txt`s CARRIED ROW', 'SIDE-lv-conservation' in sp,
        'data/b692_circuit_spec.txt names no kernel and carries no carried row (rows are readings, :7-:52); the carried kernel is named at '
        'data/b692_closure_step.txt :44-:46 and data/b692_circuit_dominance.txt :7, SIDE-lv-conservation', '2')
    cs = rd(p('data', 'b692_closure_step.txt')) or ''
    add('ruling (3)', 'the carried faces kernel by name in the closure-step bank and the b692 closing', 'SIDE-lv-conservation' in cs
        and 'SIDE-lv-conservation' in (rd(p('data', 'b692_closing.txt')) or ''), 'data/b692_closure_step.txt :44-:46 ; data/b692_closing.txt', '2')
    add('ruling (3)', '(R302)(3)(a)`s form: the script and step alone on main, one dispatch per tree state, the gz beside its hashes bank',
        'THE SCRIPT AND THE STEP' in cs and os.path.exists(p('data', 'b692_circuit_SIDE-explicit-formula_v0.34.1_4313875_hashes.txt')),
        'data/b692_closure_step.txt :7-:13 ; the hashes bank', '2')
    add('ruling (3)', 'b676`s form (each commit alone on main)', os.path.exists(p('data', 'b676_cut.txt')), 'data/b676_cut.txt', '2')
    dm = rd(p('data', 'b692_circuit_dominance.txt')) or ''
    add('ruling (3)', 'b692`s fraction: CLAUSE-DOMINANCE 1 OF 1 FACES KERNELS REACHED', 'CLAUSE-DOMINANCE 1 OF 1 FACES KERNELS REACHED' in dm,
        'data/b692_circuit_dominance.txt :21', '2')
    cr = (rd(p('data', 'b692_circuit_SIDE-explicit-formula_v0.34.1.txt')) or '').split(NL)
    add('ruling (3)', 'WIDTH`s pairs by name (rows are pairs)', len(cr) > 623 and cr[621].startswith('## WIDTH') and 'at or under the bar 25' in cr[622],
        'data/b692_circuit_SIDE-explicit-formula_v0.34.1.txt :622-:648', '2')
    add('ruling (3)', 'LOAD`s three highest', len(cr) > 706 and 'LOAD`S THREE HIGHEST Zeta23.reflect (825)' in cr[706] and cr[692].startswith('## LOAD'),
        'data/b692_circuit_SIDE-explicit-formula_v0.34.1.txt :693, :707', '2')
    nz = (rd(p('data', 'b690_nodes_zeta.txt')) or '').split(NL)
    add('ruling (3)', 'the faces page`s generator input: the faces kernels by row', len(nz) > 126 and nz[125].startswith('@corr SIDE-lv-conservation')
        and nz[93].startswith('SIDEExplicitFormula.B321.classK') and nz[94].startswith('SIDEExplicitFormula.B321.h2_sign |'),
        'data/b690_nodes_zeta.txt :94-:164 (SIDE-explicit-formula`s kernel rows), :126 (SIDE-lv-conservation by @corr), :95 the face', '2')
    add('ruling (3)', 'tools/circuit_read.py`s routes', 'def readfirst' in (rd(p('tools', 'circuit_read.py')) or ''), 'tools/circuit_read.py', '2')
    # ### (R304)(4)
    hb = rd(p('data', 'b681_epstein_zeros_narrowed_hashes.txt')) or ''
    add('ruling (4)', 'b681`s balls: the hashes bank and the gz', 'f6613564e9d7fcd534534d0c33e418229bf32dbc0567c951ee8750438b11eb5a' in hb,
        'data/b681_epstein_zeros_narrowed_hashes.txt :3', '3')
    add('ruling (4)', 'data/b677_tolerance.txt :90', (line(p('data', 'b677_tolerance.txt'), 90) or '').startswith('### ### **P1 WIDTHS 19'),
        (line(p('data', 'b677_tolerance.txt'), 90) or '')[:70], '3')
    h2 = shown(EF, 'v0.34', 'SIDEExplicitFormula/H2Sign.lean')
    add('ruling (4)', 'H2Sign.lean :22-:29 at v0.34: classK', len(h2) > 30 and h2[23].startswith('def classK') and h2[21].startswith('/-- The class K'),
        'v0.34:SIDEExplicitFormula/H2Sign.lean :22-:27 (the def at :24)', '3')
    add('ruling (4); ferry', 'H2Sign.lean :22-:29 at v0.34: h2_sign', len(h2) > 30 and h2[28].startswith('/-- **h2, as one Prop') and h2[29].startswith('def h2_sign'),
        'v0.34:SIDEExplicitFormula/H2Sign.lean :29 its docstring, :30-:31 the def (one line past the range)', '3')
    add('ruling (4); ferry', 'THE ARCHIMEDEAN TERM BY THE KERNEL`S OWN DEFINITION READ FROM H2Sign.lean', any(l.startswith('def archTerm') for l in h2),
        'H2Sign.lean defines no archTerm; it is B321Identity.lean :36-:38 at v0.34 (b321`s A, (1/2pi) INT paperFT k r * EF.gammaBracket r dr), '
        'and its bracket is the zeta gamma factor`s, Re psi(1/4 + i r/2) - log pi (:36): at Q0 the bracket is Z_Q`s own', '3')
    bi = shown(EF, 'v0.34', 'SIDEExplicitFormula/B321Identity.lean')
    add('ruling (4)', 'the three terms` definitions at v0.34', len(bi) > 38 and bi[28].startswith('def poleTerm') and bi[32].startswith('def primeSum')
        and bi[36].startswith('def archTerm'), 'v0.34:SIDEExplicitFormula/B321Identity.lean :29, :33, :37', '3')
    lb = rd(p('data', 'b675_closing.txt')) or ''
    add('ruling (4)', 'b675`s Li-face bank (the form and price)', os.path.exists(p('data', 'b675_li_bench.txt')) and 'b675' in lb,
        'data/b675_li_bench.txt ; data/b675_closing.txt :26', '3')
    rp = (rd(p('data', 'b518_report.txt')) or '').split(NL)
    add('ruling (4)', 'b518`s two-property family at Q0: 119 widths, none negative beyond its bound', len(rp) > 130
        and 'P - PR + A negative beyond B (verified) : NONE ; positive 119' in rp[126], 'data/b518_report.txt :126-:127', '3')
    add('ruling (4)', 'b518`s 95 of 119 at the zeta control', len(rp) > 255 and 'VERIFIED-EST 95 of 119' in rp[252], 'data/b518_report.txt :253-:254', '3')
    # ### (R304)(5): branches
    for repo, bs in K.DELETE:
        for b in bs:
            add('ruling (5)', '%s %s (local)' % (os.path.basename(repo), b), branch_listed(repo, b), 'git branch --list', '0')
    add('ruling (5)', 'data/b693_closing_push_out.txt to be committed at the start', g(ROOT, 'ls-files', '--error-unmatch', 'data/b693_closing_push_out.txt')[0] != 0,
        'untracked before step zero`s first write', '0')
    # ### (R304)(6)-(8)
    add('ruling (7)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b694_worklist.py')) or ''), 'tools/b694_worklist.py', '5')
    add('ruling (8)', 'b652`s order', 'the next kernel by descending count' in (line(p('data', 'b652_ferry.txt'), 19) or ''), 'data/b652_ferry.txt :19', '5')
    add('ruling (8)', 'b674`s tie-break rule', 'THE TIE-BREAK BEYOND THE COUNT' in (line(p('data', 'b674_rules.txt'), 8) or ''), 'data/b674_rules.txt :8', '5')
    add('ruling (8)', 'rule (2) of data/b690_rules.txt', 'HAS A DISTINCTIVE SUBSTRING SEARCHED WITH GIT GREP' in (line(p('data', 'b690_rules.txt'), 9) or ''),
        'data/b690_rules.txt :9', '5')
    add('ruling (8)', 'W-ORD-EPSTEIN-COUNT-LEAN and the regularity-uses bank', 'W-ORD-EPSTEIN-COUNT-LEAN' in (rd(p('data', 'b692_candidates_priced.txt')) or '')
        and 'REGULARITY-USES BANK' in (rd(p('data', 'b692_candidates_priced.txt')) or ''), 'data/b692_candidates_priced.txt :1, :18', '5')
    for rule, cl_, comp in (('R278', (4,), '5'), ('R251', (3,), '5'), ('R254', (2,), '4'), ('R302', (3,), '2')):
        ok, how = rule_clause(rule, cl_)
        add('ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C4', 'data/b675_rules.txt row 1', "(1) THE CLOSING TOOL'S DRY RUN, A GATE STEP" in (line(p('data', 'b675_rules.txt'), 5) or ''), 'data/b675_rules.txt :5', '4')
    add('ferry', 'data/b680_rules.txt, binary banks', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''), 'data/b680_rules.txt (1)', '2-4')
    add('ferry C4', 'the score order b686 fixed', 'scorer -> scores bank -> entry -> trail' in (rd(p('data', 'b686_rules.txt')) or ''), 'data/b686_rules.txt :7-:8', '4')
    add('ferry C4', 'the chain halves as b693 drew them', "CHAIN_HALVES = (('b624', 'b658'), ('b659', 'b693'))" in (rd(p('tools', 'b693_worklist.py')) or ''),
        'tools/b693_worklist.py :52', '4')
    for b in ('b694_readfirst.txt', 'b694_tool_repairs.txt', 'b694_rules.txt', 'b694_witness_plan.txt', 'b694_circuit_dominance.txt', 'b694_witness.txt'):
        sz = b == 'b694_readfirst.txt'
        add('ruling; ferry', 'data/%s -- TO BE WRITTEN, not a cite' % b, sz or not os.path.exists(p('data', b)),
            ('a step-zero bank (exists %s)' % os.path.exists(p('data', b))) if sz else 'absent, as ordered', '0-4')
    return R


def _write(L, R, miss):
    for name, data in (('b694_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b694_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b694 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b694_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b694_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b694_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b694_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b694."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b694'))
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b694')
    ns = dict(vars(P))
    exec(compile(body, 'b682_citation.answer (b694)', 'exec'), ns)
    ns['answer'](needle)


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b694_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
