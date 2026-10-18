# -*- coding: utf-8 -*-
"""b682_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b682's step zero; the ferry banked after
it; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged (the transcript reader with both apostrophes, git, the line
### reader, the rule-clause reader), its anchor pointed at this act's ruling; the rows, the banks and the routes are b682's: once
### data/act_roots.txt carries b682's root, an answer's print goes to data/b682_defects.txt and to no root-named bank ((R282)(2) row 1);
### each answer cut from BEGIN to END around its needle; a word naming no path, line or commit printed VACUOUS and banked so ((R292)'s ferry).
### Routes: `check` -> data/b682_citation_check.txt (.json) ; `ferry` -> data/b682_ferry_scan.txt (the ferry banked by the Write tool) ;
###         `answer <needle>` -> the check on one answer, appended to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b682 from b681_citation.py's form; this tool writes only the banks named above.
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

NL = chr(10)
PP, KE, TD = C.PP, C.KE, C.TD
C.ANCHOR, C.TAIL = 'RULING (R292) BEGIN', 'FERRY END (part 1 of 1)'
ANCHOR, TAIL = C.ANCHOR, C.TAIL
g, rd, line, commit_in, subject, branch_listed, rule_clause, grep_lines = (C.g, C.rd, C.line, C.commit_in, C.subject, C.branch_listed,
                                                                           C.rule_clause, C.grep_lines)
REPOS = C.REPOS + ('D:/SIDE-silence-principle', 'D:/SIDE-bijection', 'D:/SIDE-window', 'D:/SIDE-trivium')
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
FOUND = 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md'


def act_root_line(act):
    t = rd(os.path.join(D, 'act_roots.txt')) or ''
    return [l.split() for l in t.split(NL) if l.strip() and l.split()[0] == act]


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
    # ### the ferry's read-first list
    for f in ('data/b681_closing.txt', 'data/b681_defects.txt', 'data/b681_narrow.txt', 'data/b670_work_orders.txt', 'tools/correspondence_gen.py',
              'tools/test_correspondence_gen.py', 'data/b672_gen_test.txt', 'data/b672_correspondence_diff.txt', 'data/b674_cut.txt',
              'data/b676_cut.txt', 'data/b678_cut.txt', 'data/b672_one_copy.txt', 'data/b670_licensed_table.txt', 'data/b674_rules.txt',
              'data/b681_closing_push_out.txt', 'data/b675_rules.txt', 'data/b678_rules.txt', 'data/b680_rules.txt', 'data/b680_rules_arms.txt',
              'data/b677_map_plan.txt', 'data/b677_tolerance.txt', 'data/b672_roster_read.json'):
        add('ferry read-first; ruling', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-5')
    # ### the runner print banks themselves, by path (the runner bank and its axioms bank, before and after)
    for act, k in (('b674', 'SIDE-window'), ('b676', 'SIDE-trivium'), ('b678', 'SIDE-silence-principle')):
        for kind in ('runner', 'axioms'):
            for lab in ('before', 'after'):
                f = 'data/%s_%s_%s_%s.txt' % (act, kind, k, lab)
                add('ferry read-first; ruling (2)-(3)', f, os.path.exists(p(*f.split('/'))), 'the runner print bank by path', '2')
    for act, f, n, needle in (('b674', 'data/b674_cut.txt', 19, 'data/b674_axioms_SIDE-window_before.txt'), ('b674', 'data/b674_cut.txt', 21, 'tag v0.5.1'),
                              ('b676', 'data/b676_cut.txt', 25, 'data/b676_axioms_SIDE-trivium_before.txt'), ('b676', 'data/b676_cut.txt', 28, 'tag v0.1.1'),
                              ('b678', 'data/b678_cut.txt', 29, 'data/b678_axioms_SIDE-silence-principle_before.txt'),
                              ('b678', 'data/b678_cut.txt', 33, 'tag v0.2.1')):
        lt = line(p(*f.split('/')), n) or ''
        add('ruling (3)', '%s :%d "%s"' % (f, n, needle), needle in lt, lt[:90], '2')
    for f, needle in (('data/b674_runner_SIDE-window_after.txt', 'ref input 22bf840167dcb646ebe1bd1ac452eec3e8eddcfb'),
                      ('data/b676_runner_SIDE-trivium_after.txt', 'ref input db315fe4c69bf00d62980938b888643b5b70189e'),
                      ('data/b678_runner_SIDE-silence-principle_after.txt', 'ref input 8829bcc89e7824ac4b6e8a1db9e240ebcfa448ce')):
        add('ruling (3)', '%s header :3 "%s"' % (f, needle[:30]), needle in (line(p(*f.split('/')), 3) or ''), 'the dispatch line of the header', '2')
    # ### (R292)(1): b681 at its weight
    head = (rd(p('data', 'b681_closing.txt')) or '').split(NL)[0]
    add('ruling (1)', 'the head line at data/b681_closing.txt :1', head.startswith('b681 closed: relay aa5a33a7, PLACE-papers 837ba79; suite 90 of 90; root 13735beb')
        and '1 prompt answered; 1 defect' in head, head[:110], '1')
    po = rd(p('data', 'b681_closing_push_out.txt')) or ''
    add('ruling (1)', 'the closing pushed and read back at relay f17fef29', 'aa5a33a7..f17fef29' in po and 'read back at the remote: f17fef29' in po,
        'data/b681_closing_push_out.txt :4-:5', '0-1')
    for repo, nm, sha, needle in ((ROOT, 'relay', 'aa5a33a7', 'b681 record'), (ROOT, 'relay', 'f17fef29', 'b681 closing'),
                                  (PP, 'PLACE-papers', '837ba79', 'b681 record')):
        s = subject(repo, sha)
        add('ruling (1)', '%s %s' % (nm, sha), commit_in(repo, sha) and s.startswith(needle), s[:80], '0-1')
    nt = rd(p('data', 'b681_narrow.txt')) or ''
    add('ruling (1)', 'data/b681_narrow.txt: 163 of 163 at 1e-30, 68 parts, 27693 s, the longest 471 s, bar misses 0',
        'NARROWED TO 1e-30 163 OF 163 ; FORMS AS b671`S True ; PARTS 68, 27693 s ; THE LONGEST PART 471 s ; BESSEL BAR MISSES 0' in nt, 'its verdict line', '1')
    add('ruling (1)', '146 on-line by the sign change, 17 off-line by the quarter count',
        len(re.findall(r'^  ON +\d+ +form M-on', nt, re.M)) == 146 and len(re.findall(r'^  OFF +\d+ +form M-off', nt, re.M)) == 17, 'the point rows', '1')
    add('ruling (1)', 'the 88,128 segment units', '88,128 off-line units' in (rd(p('data', 'b681_hypotheses.txt')) or ''), 'data/b681_hypotheses.txt :18', '1')
    add('ruling (1)', 'C1 10 of 10 inside, C2 refused', 'C1 10 OF 10 NARROWED TO 1e-30 AND INSIDE ; C2 REFUSED True' in (rd(p('data', 'b681_narrow_controls.txt')) or ''),
        'data/b681_narrow_controls.txt', '1')
    hb = rd(p('data', 'b681_epstein_zeros_narrowed_hashes.txt')) or ''
    add('ruling (1)', 'the new bank`s hashes chaining from b671`s', '51d9e6322510b738' in hb and os.path.exists(p('data', 'b671_epstein_zeros_narrowed.json.gz')),
        'data/b681_epstein_zeros_narrowed_hashes.txt; b671`s bank beside it', '1')
    add('ruling (1)', 'the corrigendum row for b680 and b681`s root chained from b680`s',
        any(r[:2] == ['corrigendum', 'b680'] for r in (l.split() for l in (rd(p('data', 'act_roots.txt')) or '').split(NL) if l.strip()))
        and any(r[1].startswith('13735beb') and r[2].startswith('764d21d6') for r in act_root_line('b681')), 'data/act_roots.txt', '1')
    add('ruling (1)', 'the chain AGREE b624 to b680, 57 of 57', len(re.findall(r'b6[2-8]\d AGREE', rd(p('data', 'b681_chain_verify_standing-b.txt')) or '')) >= 57,
        'data/b681_chain_verify_standing-b.txt', '1')
    add('ruling (1)', 'G-ROOT-BANKS-COMMITTED in the sealed suite', "('G-ROOT-BANKS-COMMITTED'," in (rd(p('tools', 'b681_checks.py')) or ''), 'tools/b681_checks.py', '1, 5')
    for n, needle in ((14712, 'W-ORD-EPSTEIN-BALL-WIDTH'), (14714, 'W-ORD-MAP-ANGLE-FORM'), (14716, '### b681'), (14648, 'W-ORD-CORRESPONDENCE-RUNNER-BANKS'),
                      (14620, 'Correspondence')):
        lt = line(OT, n) or ''
        add('ruling (1)-(2)', 'OPEN_TRAILS :%d' % n, needle in lt, lt[:70], '1-3')
    for n, needle in ((9108, 'b680'), (9110, '## The 163 certified zeros')):
        lt = line(FIND, n) or ''
        add('ruling (1)', 'FINDINGS :%d' % n, needle in lt, lt[:70], '1')
    dl = rd(p('data', 'b681_defects.txt')) or ''
    letters = re.findall(r"^    \(([a-z])\) THE ([A-Z']+?)'S", dl, re.M)
    add('ruling (1)', 'one defect (a), the seat`s', letters == [('a', 'SEAT')], 'data/b681_defects.txt :5', '1')
    mz = 'D:/MY-DOwnloads/mirror-refresh-2026-10-18-b681.zip'
    add('ruling (1)', 'the b681 mirror made: %s' % mz, os.path.exists(mz) and 'VERDICT: CLEAN ON ALL THREE CLAUSES' in (rd(p('data', 'b681_mirror_verify.txt')) or ''),
        'the zip and data/b681_mirror_verify.txt', '0')
    # ### (R292)(2): the object
    ob = rd(p('data', 'b670_work_orders.txt')) or ''
    add('ruling (2)', 'W-ORD-CORRESPONDENCE-RUNNER-BANKS`s row', 'W-ORD-CORRESPONDENCE-RUNNER-BANKS            :14648  b679   0     OPEN' in ob,
        'data/b670_work_orders.txt :272', '2-3')
    fl = [line(os.path.join(PP, FOUND), n) or '' for n in (628, 629, 630)]
    add('ruling (2)', FOUND + ' :628-:630, SIDE-silence-principle v0.2.0, two cells NO PRINT BANK AT v0.2.0',
        all('SIDE-silence-principle v0.2.0' in x for x in fl) and sum('NO PRINT BANK AT v0.2.0' in x for x in fl) == 2, 'the three rows', '2-3')
    add('ruling (2)', 'b678 named 5 cells there', 'CELLS CHANGED 5, every one in' in (rd(p('data', 'b678_cut.txt')) or ''), 'data/b678_cut.txt :63', '2')
    oc = rd(p('data', 'b672_one_copy.txt')) or ''
    add('ferry read-first', 'REGISTRY names the unversioned copy (row 1.5f-4); data/b672_one_copy.txt :259-:260 names it with its versioned copy',
        '`phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md`' in (rd(os.path.join(PP, 'REGISTRY.md')) or '')
        and '=== phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md' in oc,
        'REGISTRY :205; the bank`s "copy of record" is its highest versioned copy, v0_2_5, the roster`s file (partner not identical)', '2-3')
    gen = rd(p('tools', 'correspondence_gen.py')) or ''
    add('ruling (3)', 'the generator`s reader: BANK_NAME and read_banks', 'BANK_NAME = re.compile' in gen and 'def read_banks(tags)' in gen, 'tools/correspondence_gen.py', '2')
    tt = rd(p('tools', 'test_correspondence_gen.py')) or ''
    add('ruling (3)', 'the four planted cases of b672', 'PLANTED CASES 4 ; AS WANTED 4 ; PASS' in (rd(p('data', 'b672_gen_test.txt')) or '') and bool(tt),
        'data/b672_gen_test.txt; tools/test_correspondence_gen.py', '2')
    try:
        ro = json.load(open(p('data', 'b672_roster_read.json'), encoding='utf-8'))
    except Exception:
        ro = {'tables': []}
    nfiles = len(set(t['path'] for t in ro['tables']))
    add('ruling (3)', 'the 13 roster files', nfiles == 13, 'data/b672_roster_read.json: %d tables in %d files' % (len(ro['tables']), nfiles), '2')
    # ### (R292)(4)-(5)
    ca = rd(p('data', 'b680_correspondence.txt')) or ''
    add('ruling (4)', 'b680`s 55 and 0', 'BEHIND BY b670`S METHOD 55 AGAINST 54' in ca and 'AT THE GENERATOR`S CLAIM 0 AGAINST 0' in ca, 'data/b680_correspondence.txt :14', '3')
    add('ruling (5)', 'b674`s tie-break rule', 'THE TIE-BREAK BEYOND THE COUNT' in (line(p('data', 'b674_rules.txt'), 8) or ''), 'data/b674_rules.txt :8', '4')
    add('ruling (5)', 'b652`s order', 'the next kernel by descending count' in (line(p('data', 'b652_ferry.txt'), 19) or ''), 'data/b652_ferry.txt :19', '4')
    # ### this act's banks, to be written
    for b in ('b682_readfirst.txt', 'b682_gen_test.txt', 'b682_correspondence_diff.txt', 'b682_cut.txt', 'b682_tool_repairs.txt'):
        sz = b == 'b682_readfirst.txt'
        add('ruling; ferry', 'data/%s -- TO BE WRITTEN, not a cite' % b, sz or not os.path.exists(p('data', b)),
            ('a step-zero bank, written after the check`s first run (exists %s)' % os.path.exists(p('data', b))) if sz else 'absent, as ordered', '0-5')
    # ### (R292)(6): branches
    for repo, nm, bs in (('D:/relay', 'relay', ('push-b681-root', 'push-b681', 'push-b681-closing')), (PP, 'PLACE-papers', ('push-b681-root', 'push-b681'))):
        for b in bs:
            add('ruling (6)', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    add('ruling (6)', 'data/b681_closing_push_out.txt untracked, to be committed', g(ROOT, 'ls-files', '--error-unmatch', 'data/b681_closing_push_out.txt')[0] != 0,
        'not tracked', '0')
    add('ruling (8)', 'the draft at v5, held', "DRAFT = '23228113'" in (rd(p('tools', 'b681_worklist.py')) or ''), 'tools/b681_worklist.py', '6')
    add('ruling (9)', 'the 24 rules without arms', 'NONE 24' in (rd(p('data', 'b680_rules_arms.txt')) or ''), 'data/b680_rules_arms.txt', '6')
    for rule, cl_, comp in (('R278', (4,), '6'), ('R251', (3,), '6'), ('R254', (2,), '1')):
        ok, how = rule_clause(rule, cl_)
        add('ruling; ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ferry C5', 'data/b678_rules.txt row 1, the suite in three parts', '(1) THE STANDING ARMS IN TWO FOREGROUND PARTS' in (line(p('data', 'b678_rules.txt'), 5) or ''),
        'data/b678_rules.txt :5', '5')
    add('ferry C5', 'data/b675_rules.txt row 1, the closing a gate step', bool(re.search(r'\(1\)', rd(p('data', 'b675_rules.txt')) or '')), 'data/b675_rules.txt', '5')
    add('ferry', 'data/b680_rules.txt, binary banks beside a text hashes bank', 'A BINARY BANK IS ROOTED THROUGH A TEXT HASHES BANK' in (rd(p('data', 'b680_rules.txt')) or ''),
        'data/b680_rules.txt row (1)', '6')
    return R


def _write(L, R, miss):
    for name, data in (('b682_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b682_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b682 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662), RUN BEFORE THE FERRY IS BANKED (%s)' % time.strftime(
        '%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b682_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b682_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b682_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b682_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), banked == text.rstrip(NL), r.returncode))


def after_root():
    return bool(act_root_line('b682'))


def answer(needle, *a):
    """(R278)(4): the latest session text carrying `needle` after this act's ruling, cut from BEGIN to END around it; its relay paths, ledger
    lines and commits checked at HEAD; the print appended to the citation bank, or after the root to the defects bank."""
    best, seen = None, False
    for t in C._user_texts():
        if ANCHOR in t:
            seen = True
        u = t.replace('\u2019', "'")
        if seen and needle in t and ("NAVIGATOR'S ANSWER" in u or "NAVIGATOR'S NOTE" in u or "AUTHOR'S" in u or 'The user answered' in u
                                     or 'user has answered' in u):
            best = t
    if best is None:
        sys.exit('### NO ANSWER CARRYING %r IN THE SESSION AFTER THE RULING -- NOTHING WRITTEN' % needle)
    k = best.find(needle)
    b0, e0 = best.rfind('BEGIN', 0, k), best.find('END', k)
    if b0 >= 0 and e0 > k:
        best = best[b0:e0 + 3]
    rows_ = []
    for pth in sorted(set(re.findall(r'\b((?:data|tools)/[\w./-]+\.[a-z]{2,5})\b', best))):
        ex = os.path.exists(os.path.join(ROOT, *pth.split('/')))
        if not ex and re.match(r'^(data|tools)/b682_', pth):
            rows_.append(('path, this act`s bank or tool the answer orders written -- TO BE WRITTEN, not a cite', pth, True))
        else:
            rows_.append(('path', pth, ex))
    for m in re.finditer(r'\b(FINDINGS|OPEN_TRAILS)\b((?:[^:\n]{0,20}:\d{3,5})+(?:(?:,|;| and|,? or)\s*:\d{3,5})*)', best):
        for n in sorted(set(re.findall(r':(\d{3,5})', m.group(2)))):
            rows_.append(('line', '%s :%s' % (m.group(1), n), line(os.path.join(PP, m.group(1) + '.md'), int(n)) is not None))
    for h in sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', best))):
        if re.search(r'[a-f]', h) and re.search(r'\d', h):
            rows_.append(('commit', h, any(commit_in(r_, h) for r_ in REPOS)))
    miss = [r for r in rows_ if not r[2]]
    q = os.path.join(D, 'b682_defects.txt' if after_root() else 'b682_citation_check.txt')
    old = (rd(q) or '').rstrip(NL)
    L = ['', '### (R278)(4) THE MID-ACT CHECK (%s): the answer carrying %r, %d characters; its cites checked at HEAD before the seat '
         'acts on it%s:' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), needle, len(best),
                            ' (after the root: printed to the defects bank, (R282)(2) row 1)' if after_root() else '')]
    L += ['  %-4s | %s | %s' % ('OK' if ok else 'MISS', k_, w) for k_, w, ok in rows_] or ['  (no path, ledger line or commit named)']
    L += ['### ### **ANSWER CITES CHECKED %d ; OK %d ; MISSES %d%s.**%s' % (len(rows_), len(rows_) - len(miss), len(miss),
                                                                         (' -- RAISED: ' + ', '.join(w for _k, w, _o in miss)) if miss else '',
                                                                         ' -- VACUOUS: the word names no path, line or commit to check.' if not rows_ else '')]
    open(q + '.tmp', 'wb').write((old + NL + NL.join(L) + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    print(NL.join(L))


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b682_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
