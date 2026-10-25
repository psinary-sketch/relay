# -*- coding: utf-8 -*-
"""b713_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b713's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (ec2d71b5, a NEW session after the author's /clear; the anchor (R323)'s line); the answer route is b682's, imported from
### tools/b682_citation.py with its act names pointed at b713, b706's repair carried (a bare eight-hex token a bank names as a sha256 or a
### kernel's lakefile pins as a rev is not read as a commit); the `word` route is b694's. Routes: `check [dry]` -> data/b713_citation_check.txt
### (.json) ; `ferry` -> data/b713_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the check on one answer.
### Written by the Write tool at b713 from b712_citation.py's form (its engine :1-:101 and :344-:484, read at step zero), its cite rows this
### ruling's; this tool writes only the banks named above. A kernel's file at a tag is read here by `git cat-file` and `git grep` inside this
### tool (a named tool's read, its rows banked), never printed whole.
"""
import glob
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
import b713_worklist as K   # noqa: E402
import act_membrane as MEM  # noqa: E402  ### (R323)(2)(ii): the membrane before every bank write of this tool


def _root_exclude():
    import b713_record as REC   # ### the record tool's exclusion pattern, the one the root route reads (imported at the call, nothing written)
    return REC.R.ROOT_EXCLUDE


C.SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID


def continuation_sessions():
    """the act's continuation sessions (K.SESSIONS_AFTER, b671's form) as transcript paths, read by b677's helpers after the seat's session."""
    return tuple('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid for sid, _anc in K.SESSIONS_AFTER)


C.SESSIONS_AFTER = continuation_sessions()
NL = chr(10)
PP = C.PP
C.ANCHOR, C.TAIL = K.ANCHOR, K.TAIL
ANCHOR, TAIL = C.ANCHOR, C.TAIL
g, rd = C.g, C.rd
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def act_root_line(act):
    t = rd(os.path.join(D, 'act_roots.txt')) or ''
    return [l.split() for l in t.split(NL) if l.strip() and l.split()[0] == act]


def lines_of(path):
    return (rd(path) or '').split(NL)


def first(L, needle, start=1):
    return next((i + 1 for i, l in enumerate(L) if i + 1 >= start and needle in l), 0)


def at(L, n):
    return L[n - 1] if n and len(L) >= n else ''


def _ws(s):
    return ''.join((s or '').split())


def _jl(name):
    try:
        return json.loads(rd(os.path.join(D, name)) or '{}')
    except Exception:
        return {}


def _blob(repo, rev, path):
    """a file's text at a revision, read inside the tool (`git cat-file -p`), '' when absent."""
    r = subprocess.run(['git', '-C', repo, 'cat-file', '-p', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else ''


def _decl_files(repo, rev, name):
    """the .lean files at `rev` that DECLARE `name` (its last dotted component after theorem/lemma/def/structure), by git grep -l inside the tool."""
    short = name.split('.')[-1]
    r = subprocess.run(['git', '-C', repo, 'grep', '-l', '-E', r'^\s*(private\s+)?(theorem|lemma|def|structure|abbrev|instance)\s+' + re.escape(short) + r'(\s|$|:)',
                        rev, '--', '*.lean'], capture_output=True)
    return [l.split(':', 1)[1] for l in r.stdout.decode('utf-8', 'replace').split(NL) if ':' in l]


def _decl_line(text, short):
    rx = re.compile(r'^\s*(private\s+)?(theorem|lemma|def|structure|abbrev|instance)\s+' + re.escape(short) + r'(\s|$|:)')
    return next((i + 1 for i, l in enumerate(text.split(NL)) if rx.match(l)), 0)


def _remote_heads(repo):
    out = g(repo, 'ls-remote', '--heads', 'origin')[1] or ''
    return dict((l.split('\t', 1)[1].strip(), l.split('\t', 1)[0]) for l in out.split(NL) if '\t' in l)


def _quote(text, start, stop):
    """the ruling's quotation that opens with `start`, cut at `stop` (the quotation's own closing mark and the clause after it)."""
    i = text.find(start)
    if i < 0:
        return ''
    j = text.find(stop, i)
    return text[i:j] if j > 0 else ''


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    OT = os.path.join(PP, 'OPEN_TRAILS.md')
    FI = os.path.join(PP, 'FINDINGS.md')
    ot, fi = lines_of(OT), lines_of(FI)
    text = C.ferry_text()
    # ### b713: the cite rows of (R323) and its ferry, written by the Edit tool after b712's rows were pruned (data/b713_prune_citation.txt)
    for f in ('data/b712_closing.txt', 'data/b712_defects.txt', 'data/b712_events.txt', 'data/standing_clauses_v3.txt', 'data/b712_registrations.txt',
              'data/b712_genus_control.txt', 'data/b712_price.txt', 'data/b709_pairs.txt', 'data/b710_registrations.txt', 'data/b712_recut_cut.txt',
              'data/b712_recut_diff.txt', 'data/b712_closing_push_out.txt', 'data/b712_steps.json', 'data/b712_regpos.txt', 'data/b712_report.txt',
              'data/b712_mirror.txt', 'data/b712_scores_close.json', 'data/b712_checks.txt', 'data/b712_checks_postpush.txt',
              'data/b712_checks_postpush_standing-b3.txt', 'data/b712_ferry.txt', 'data/b712_standing_figures.json', 'data/b675_corrigenda.txt',
              'data/act_roots.txt', 'data/b711_steps.json', 'data/b708_rules.txt', K.B711_FACE, 'tools/b712_worklist.py', 'tools/b712_record.py',
              'tools/b712_checks.py', 'tools/b712_closing.py', 'tools/b712_citation.py', 'tools/b712_corrigendum.py', 'tools/b712_regspec.py',
              'tools/b712_reg_gate.py', 'tools/b712_tests.py', 'tools/b712_report.py', 'tools/b712_carry.py', 'tools/b712_standing.py',
              'tools/b712_genus_control.py', 'tools/b712_price.py', 'tools/b712_recut.py', 'tools/b712_locate.py', 'tools/b709_pairs.py',
              'tools/b711_list.py', 'tools/b711_pairs.py', 'tools/b711_coeffs.py', 'tools/b667_epstein_certify.py', 'tools/b706_standing_figures.py',
              'tools/circuit_read.py', 'tools/mirror_verify.py', 'tools/mirror_build.ps1', 'tools/mirror_prevbuild.json', 'tools/push_gated.sh',
              'tools/act_root.py', 'tools/act_membrane.py', 'tools/ferry_scan.py', 'tools/b682_citation.py', 'tools/b678_corrigendum.py'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    # ### (R323)(1): b712 at its weight
    cl = lines_of(p('data', 'b712_closing.txt'))
    q = _quote(text, 'b712 closed: relay', '”; “none read”')
    add('ruling (1)', 'data/b712_closing.txt :1, the head line, against (R323)(1)`s quote', q == cl[0], 'quote %d characters, the line %d ; equal byte for byte %s' % (len(q), len(cl[0]), q == cl[0]), '0-1')
    ev = lines_of(p('data', 'b712_events.txt'))
    starts = [i + 1 for i, l in enumerate(ev) if re.match(r'^    [A-Z]', l)]
    add('ruling (1)', 'events (9), no push capture: data/b712_events.txt :48', at(ev, 48).strip().startswith('NO PUSH CAPTURE'), ':48 %r' % at(ev, 48).strip()[:60], '1')
    fjl = _blob(K.JOIN_DIR, 'v0.1.0', 'FacesJoin.lean').split(NL)
    add('ruling (1)', 'faces_join at SIDE-faces-join FacesJoin.lean :29 (at v0.1.0)', 'faces_join' in at(fjl, 29) and 'h2_sign' in ' '.join(fjl[28:34]),
        'FacesJoin.lean at v0.1.0: %d lines ; :29 %r' % (len(fjl), at(fjl, 29).strip()[:70]), '1')
    jg = rd(p('data', 'b712_join_grade.txt')) or ''
    add('ruling (1)', 'run 40210894425 against cb0aea56, #print axioms the standard three, DERIVES', '40210894425' in jg and 'DERIVES' in jg and 'Quot.sound' in jg,
        'data/b712_join_grade.txt: run %s ; DERIVES %s ; Quot.sound %s' % ('40210894425' in jg, 'DERIVES' in jg, 'Quot.sound' in jg), '1')
    add('ruling (1)', 'tag object 9bf6fe65 peeled 11a472b9 (FINDINGS :10380, :10390)', 'peeled 11a472b9' in at(fi, 10380) and '11a472b9' in at(fi, 10390) and 'faces_join' in at(fi, 10380),
        'FINDINGS :10380 %s ; :10390 %s' % ('peeled 11a472b9' in at(fi, 10380), '11a472b9' in at(fi, 10390)), '1')
    jt = (g(K.JOIN_DIR, 'rev-parse', 'v0.1.0', 'v0.1.0^{}')[1] or '').split()
    add('ruling (1)', 'v0.1.0: tag object 9bf6fe65, peeled 11a472b9 (local)', len(jt) == 2 and jt[0] == K.JOIN_TAG[1] and jt[1] == K.JOIN_TAG[2], 'rev-parse %s' % [x[:8] for x in jt], '1')
    fl_ = lines_of(os.path.join(PP, 'FACES_LEDGER.md'))
    add('ruling (1); ruling (2)', 'FACES_LEDGER :547, faces_join`s row', 'faces_join' in at(fl_, 547) and 'Register4_positivity' in at(fl_, 547) and 'DERIVES' in at(fl_, 547),
        'FACES_LEDGER.md :547 %r' % at(fl_, 547)[:60], '1')
    rpo = lines_of(p('data', 'b712_regpos.txt'))
    add('ruling (1)', 'Register4_positivity equal by statement at 93c27ec and cb0aea56 (data/b712_regpos.txt)', 'LINES 152 AND 152' in at(rpo, 13) and '0 lines' in at(rpo, 10),
        ':10 %r ; :13 %r' % (at(rpo, 10)[:60], at(rpo, 13)[:60]), '1')
    add('ruling (1)', 'the port at 12 of 12 modules (FINDINGS :10388)', '12 of 12 modules' in at(fi, 10388), 'FINDINGS :10388', '1')
    rp_ = rd(p('data', 'b712_report.txt')) or ''
    add('ruling (1)', 'the throughstone (a)-(d) EQUAL (data/b712_report.txt :7, DIFFERS NONE, REGRADE NONE)', 'THROUGHSTONE' in at(rp_.split(NL), 7) and 'DIFFERS NONE' in rp_ and 'REGRADE NONE' in rp_,
        ':7 ; DIFFERS NONE %s ; REGRADE NONE %s' % ('DIFFERS NONE' in rp_, 'REGRADE NONE' in rp_), '1')
    reg = (g(ROOT, 'log', '--format=%H', '--', K.REGISTRATIONS)[1] or '').split()
    add('ruling (1); ruling (5); N2', 'data/b712_registrations.txt committed alone at 67a02388, its one commit', reg == [K.REG_COMMIT]
        and (g(ROOT, 'show', '--stat', '--format=', K.REG_COMMIT)[1] or '').count('data/') == 3, 'its commits %s' % [x[:8] for x in reg], '1')
    gc = lines_of(p('data', 'b712_genus_control.txt'))
    add('ruling (1)', 'the genus control as wanted (data/b712_genus_control.txt :43, :45)', at(gc, 43).strip() == 'THE MISSES THROUGH n = 400: 0' and 'PLANTED CONTROLS BOTH F' in at(gc, 45),
        ':43 %r' % at(gc, 43).strip(), '1')
    pr_ = lines_of(p('data', 'b712_price.txt'))
    add('ruling (1); ruling (5)', 'the price: tier one 0.51 h, tier two 0.74 h, the act budget 7.0 h, the cut n <= 32532 (data/b712_price.txt :39, :43, :53; FINDINGS :10394)',
        'the first tier 0.51 hours ; the second tier 0.74 hours' in at(pr_, 39) and 'about 7.0 foreground hours' in at(pr_, 43) and 'n <= 32532' in at(pr_, 53) and 'n ≤ 32532' in at(fi, 10394),
        ':39 ; :43 ; :53 ; FINDINGS :10394', '1')
    add('ruling (1)', 'the re-cut on recut-b712-silence f5ea57cb, its distance 19 to 1 (data/b712_recut_cut.txt :73)', 'BEFORE 19, AFTER 1' in at(lines_of(p('data', 'b712_recut_cut.txt')), 73)
        and (g(PP, 'rev-parse', K.RECUT_BRANCH)[1] or '').strip() == K.RECUT_COMMIT, 'branch tip %s' % (g(PP, 'rev-parse', K.RECUT_BRANCH)[1] or '').strip()[:8], '1')
    add('ruling (1)', 'the trail at OPEN_TRAILS :15890 carrying the root fa19697b', at(ot, 15890).startswith('### b712') and 'fa19697bc8f13f4c' in at(ot, 15896), 'OPEN_TRAILS :15890 ; :15896', '1')
    row = act_root_line('b712')
    add('ruling (1)', 'the root fa19697b in data/act_roots.txt, chained from b711`s afa0d8f9', bool(row) and row[0][1].startswith('fa19697b') and row[0][2].startswith('afa0d8f9'),
        'row b712 %s' % (row[0][1:3] if row else 'NONE'), '1')
    b3 = rd(p('data', 'b712_checks_postpush_standing-b3.txt')) or ''
    add('ruling (1)', 'the act-root chain b624-b712 AGREE', 'b624 AGREE' in rd(p('data', 'b712_checks_postpush_standing-b2a.txt')) and 'b712 AGREE' in b3 and 'DISAGREE' not in b3,
        'data/b712_checks_postpush_standing-b2a.txt, -b3.txt', '1')
    scc = _jl('b712_scores_close.json')
    verd = dict((k, (v[0] if isinstance(v, list) and v else v)) for k, v in scc.items() if re.match(r'^[NS][1-5]$', k))
    add('ruling (1)', 'N1-N4 and S1-S3 HELD, N5 REFUTED at scores close', len(verd) == 8 and verd.get('N5') == 'REFUTED' and all(v == 'HELD' for k, v in verd.items() if k != 'N5'),
        'data/b712_scores_close.json verdicts %s' % ' '.join('%s %s' % kv for kv in sorted(verd.items())), '1')
    cpp, cpr = rd(p('data', 'b712_checks_postpush.txt')) or '', rd(p('data', 'b712_checks.txt')) or ''
    fl = re.search(r'LIVE FAILING : \d+ (\[.*?\])', cpp)
    want = {'G-PRIORBANK-UNCHANGED', 'G-READ-RULE-STANDING', 'G-NOTHING-RAN-AHEAD', 'G-ROOTDRY-READY', 'G-TRAIL-LINES-EQUAL-DEFECTS'}
    add('ruling (1)', 'suite 137 of 142 pre-push and post-push, the two carried arms and G-NOTHING-RAN-AHEAD, G-ROOTDRY-READY, G-TRAIL-LINES-EQUAL-DEFECTS',
        'LIVE PASSING : 137' in cpp and 'LIVE PASSING : 137' in cpr and 'ARMS RUN : 142' in cpp and bool(fl) and set(re.findall(r"'([A-Z0-9-]+)'", fl.group(1))) == want,
        'failing post-push %s' % (fl.group(1) if fl else 'NONE'), '1')
    mr = rd(p('data', 'b712_mirror.txt')) or ''
    add('ruling (1)', 'the mirror mirror-refresh-2026-10-25-b712.zip (sha256 5406583e…) CLEAN on all three clauses over 70 files with the root line',
        'sha256 5406583e' in mr and 'CLEAN ON ALL THREE CLAUSES' in mr and 'Act root: b712 fa19697b' in mr and 'files 70' in mr and os.path.exists(K.MIRROR_ZIP),
        'data/b712_mirror.txt ; the zip exists %s' % os.path.exists(K.MIRROR_ZIP), '1')
    dl = lines_of(p('data', 'b712_defects.txt'))
    lets = ''.join(m.group(1) for l in dl for m in [re.match(r'^    \(([a-z])\) ', l)] if m)
    add('ruling (1)', 'twenty-two defects (a)-(v) lettered before the seal', lets == 'abcdefghijklmnopqrstuv', 'data/b712_defects.txt letters %s' % lets, '1')
    add('ruling (1); ruling (3)', 'nine events in data/b712_events.txt (each event`s starting line, four spaces and a capital)', starts == [3, 10, 18, 28, 32, 36, 41, 44, 48],
        'starting lines %s' % starts, '1')
    add('ruling (1); ruling (9)', '"Nothing deposited": the draft at v5, held', K.DRAFT == '23228113', 'tools/b713_worklist.py DRAFT', '6')
    # ### (R323)(2): the three items of OPEN_TRAILS :15920
    r920 = at(ot, 15920)
    add('ruling (2)', 'OPEN_TRAILS :15920, its items (1) N5`s identity, (2) the faces ledger`s head :8, (3) the re-cut and the Correspondence header',
        r920.startswith('**Resolved by the seat') and '(1) N5’s' in r920 and '(2) the faces ledger head’s :8' in r920 and '(3) the re-cut alters' in r920, ':15920 %r' % r920[:60], '1')
    add('ruling (2)(ii)', 'FACES_LEDGER.md :8 closing on "and the record states none" (the clause the Edit replaces, once in the line)',
        at(fl_, 8).endswith('and the record states none.') and at(fl_, 8).count('and the record states none') == 1, ':8 ends %r' % at(fl_, 8)[-40:], '1')
    rc = _blob(PP, K.RECUT_COMMIT + '^', K.RECUT_DOC).split(NL)
    add('ruling (2)(iii)', 'the original Correspondence section and its ADDITIVE ONLY header (the re-cut`s base, f5ea57cb^)', any('ADDITIVE ONLY' in l for l in rc),
        'base %d lines ; header at :%s' % (len(rc), [i + 1 for i, l in enumerate(rc) if 'ADDITIVE ONLY' in l]), '1')
    rh = _remote_heads(PP)
    add('ruling (2)(iii)', 'recut-b712-silence not at the remote (to be pushed in branch mode, not merged)', 'refs/heads/recut-b712-silence' not in rh, 'remote heads naming it %s' % [k for k in rh if 'recut' in k], '1')
    # ### (R323)(3): the corrigendum's nine starting lines, lettered and records
    lettered, records = [3, 10, 28, 32, 36, 44, 48], [18, 41]
    add('ruling (3)', 'the seven lettered starting lines and the two records are the events` nine, once each', sorted(lettered + records) == starts,
        'lettered %s ; records %s ; the bank`s %s' % (lettered, records, starts), '1')
    for n, needle in ((3, 'THE GATE IN TWO COMMITS'), (10, 'N5 REFUTED BY THE SCORER'), (18, 'THE ROOT\'S PROMPT AND THE THROUGHSTONE'), (28, 'THE ROOT ROUTE\'S DRY RUN RUN AGAIN'),
                      (32, 'TWO SEALED TOOLS ON (h)\'S OWNER'), (36, 'THE COMPONENTS ROUTE MISSED'), (41, 'THE AUTO-MODE NOTE A SEVENTH TIME'), (44, 'N4\'S CLOSE CLAUSE'),
                      (48, 'NO PUSH CAPTURE')):
        add('ruling (3)', 'data/b712_events.txt :%d, the item the ruling names there' % n, needle in at(ev, n), ':%d %r' % (n, at(ev, n).strip()[:60]), '1')
    f12 = rd(p('data', 'b712_ferry.txt')) or ''
    # ### the needle is the ruling's fragment as the ferry carries it ("the act’s step bank row marked gate"); the dry form's needle opened
    # ### "the step bank row" and read MISS -- a matcher defect, corrected before the bank (both figures printed, the defects bank)
    w11 = at(f12.split(NL), 11)   # ### at() counts from 1: the first bank read :10 (0 times) -- the same defect, corrected
    add('ruling (3)', '(R322)(3)(ii)`s wording "the step bank row marked gate" (data/b712_ferry.txt :11, "the act’s step bank row marked gate", one row in the singular)',
        w11.count('step bank row marked gate') == 1, ':11 carries it %d time(s) ; the dry needle "the step bank row marked gate" %d' % (
            w11.count('step bank row marked gate'), w11.count('the step bank row marked gate')), '1')
    cg = lines_of(p('data', 'b675_corrigenda.txt'))
    last = [l for l in cg if re.match(r'^\s*\((\d+)\)', l)]
    add('ruling (3)', 'the corrigenda bank, appended only (its last row (32), b712`s)', bool(last) and re.match(r'^\s*\(32\)', last[-1]) is not None,
        'data/b675_corrigenda.txt, last row %r' % (last[-1][:40] if last else ''), '1')
    # ### (R323)(4): the six repairs' objects
    st = _jl('b712_steps.json').get('rows', [])
    gate = [r_ for r_ in st if r_.get('commit', '')[:8] in ('afe3903a', 'dcb3b286')]
    add('ruling (4)(ii)', 'b712`s gate in two commits afe3903a and dcb3b286 in its step bank', len(gate) == 2, 'rows %s' % [(r_['commit'][:8], r_.get('phase')) for r_ in gate], '1')
    rec = rd(p('tools', 'b712_record.py')) or ''
    add('ruling (4)(i)', 'the scorer`s own list N5_RELAY_DATA (tools/b712_record.py :59) omitting data/b711_steps.json', "R.N5_RELAY_DATA = ('act_roots.txt', 'b711_closing_push_out.txt', 'b675_corrigenda.txt')" in at(rec.split(NL), 59),
        ':59', '1')
    add('ruling (4)(v)', 'tools/push_gated.sh writing a capture only where PUSH_GATED_LOG is set (:40)', 'if [ -n "${PUSH_GATED_LOG:-}" ]; then' in at(lines_of(p('tools', 'push_gated.sh')), 40), ':40', '1')
    ck = rd(p('tools', 'b712_checks.py')) or ''
    add('ruling (4)(vi)', 'the checks tool`s is_pushed wanting data/b712_components.txt at HEAD (tools/b712_checks.py :192-:195)', "'data/b712_components.txt' in gs(ROOT, 'show'" in ' '.join(ck.split(NL)[191:195]), ':192-:195', '1')
    for f in ('data/standing_clauses_v4.txt', 'data/b713_tool_repairs.txt', 'data/b713_recut_additive.txt', 'data/b713_predictions.txt', 'data/b713_source_pin.txt',
              'data/b713_readfirst.txt', 'data/b713_rules.txt', 'data/b714_rules.txt', 'tools/b713_list.py', 'tools/b713_predict.py', 'tools/b713_onsets.py', 'tools/b713_coeffs.py'):
        add('ruling (2)-(8)', '%s -- TO BE WRITTEN by this act' % f, not os.path.exists(p(*f.split('/'))), 'absent, as ordered', '0-6')
    # ### (R323)(5)-(6): the research act's sources
    r10 = lines_of(p('data', 'b710_registrations.txt'))
    add('ruling (5); ferry read-first', 'data/b710_registrations.txt (i), the refined law (:10-:43), its falsifier at :43', at(r10, 10).strip().startswith('(i) THE REFINED DETECTION LAW') and at(r10, 43).strip().startswith('FALSIFIER'),
        ':10 ; :43', '3')
    rg = lines_of(p(*K.REGISTRATIONS.split('/')))
    add('ruling (5)', 'the registrations (i) the forms, (ii) the refined law at -15, (iii) the coefficient observation (data/b712_registrations.txt :11, :28, :54)',
        at(rg, 11).strip().startswith('(i) THE FORMS') and at(rg, 28).strip().startswith('(ii) THE REFINED DETECTION LAW AT -15') and at(rg, 54).strip().startswith('(iii) THE COEFFICIENT OBSERVATION'),
        ':11 ; :28 ; :54', '2-4')
    add('ruling (5)', 'the registered pairs` record, 0.800011 + 12.038599 i and 0.9274609 + 15.496634 i (data/b712_registrations.txt :44)', '0.800011 + 12.038599 i' in at(rg, 44) and '0.9274609 + 15.496634 i' in at(rg, 44),
        ':44', '2-3')
    bp = lines_of(p('data', 'b709_pairs.txt'))
    add('ruling (5); ferry read-first', 'data/b709_pairs.txt and the form of its bands', len(bp) > 5 and any('band' in l.lower() for l in bp), 'data/b709_pairs.txt %d lines' % len(bp), '2')
    for f in ('tools/b709_pairs.py', 'tools/b711_list.py', 'tools/b711_coeffs.py'):
        add('ruling (5)', 'b709`s form: %s' % f, os.path.exists(p(*f.split('/'))), 'present', '2-4')
    add('ruling (6)', 'the source pin priced at b712 (data/b712_price.txt :47-:51)', 'THE SOURCE PIN FOR b713' in at(pr_, 47), ':47', '4')
    # ### (R323)(7): the carried files and the branches
    cpo = lines_of(p('data', 'b712_closing_push_out.txt'))
    add('ruling (7)', 'data/b712_closing_push_out.txt, the closing push`s capture (untracked, to be committed alone)', 'push-b712-closing' in at(cpo, 2) and not (g(ROOT, 'ls-files', 'data/b712_closing_push_out.txt')[1] or '').strip(),
        ':2 ; tracked %s' % bool((g(ROOT, 'ls-files', 'data/b712_closing_push_out.txt')[1] or '').strip()), '0')
    # ### a step is its row's place in the bank (the rows carry no step field; the record tool prints "step <place>"): the dry form read a
    # ### `step` key and found no row -- a matcher defect, corrected before the bank
    s25 = st[24:25]
    add('ruling (7)', 'step 25 of data/b712_steps.json, the closing`s row (1290446c), its 25th row of %d' % len(st), len(st) == 25 and bool(s25) and s25[0].get('commit', '').startswith('1290446c')
        and s25[0].get('phase') == 'closing', 'row 25 %s %s ; the dry form`s `step` key rows %d' % (s25[0].get('commit', '')[:8] if s25 else 'NONE', s25[0].get('phase') if s25 else '',
                                                                                             len([r_ for r_ in st if 'step' in r_])), '0')
    add('ruling (7)', 'the branch rows of data/b712_closing.txt (:388)', 'push-b712* branches of relay and PLACE-papers' in at(cl, 388) and 'push-b712-join' in at(cl, 388), ':388', '0')
    for repo, names in K.DELETE:
        lst = g(repo, 'branch', '--merged', 'main')[1] or ''
        for b in names:
            add('ruling (7)', '%s %s (local, listed --merged)' % (os.path.basename(repo), b), b in [x.strip(' *') for x in lst.split(NL)], 'listed by `git branch --merged main` before any delete', '0')
    loc = (g(K.LV_DIR, 'rev-parse', 'port-b707')[1] or '').strip()
    lh = _remote_heads(K.LV_DIR)
    add('ruling (7)', 'port-b707 at cb0aea56 locally and at the remote, NOT deleted (one ls-remote of SIDE-lv-conservation)', loc == K.PORT_TIP and lh.get('refs/heads/port-b707') == K.PORT_TIP,
        'local %s ; remote %s' % (loc[:8], (lh.get('refs/heads/port-b707') or '')[:8]), '0')
    add('ruling (7)', 'recut-b712-silence at f5ea57cb, NOT deleted', (g(PP, 'rev-parse', K.RECUT_BRANCH)[1] or '').strip() == K.RECUT_COMMIT, 'local tip', '0')
    add('ruling (7)', 'the 2,560 MB hold', K.HOLD == 2560, 'tools/b713_worklist.py HOLD', '0')
    # ### (R323)(8)-(10) and the ferry's standing references
    add('ruling (8)', 'the READFIRST-CLOSURE reader', os.path.exists(p('tools', 'circuit_read.py')), 'tools/circuit_read.py (readfirst)', '0')
    add('ruling (8)', 'tools/mirror_prevbuild.json, the mirror builder`s state file, named in (W)', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'tools/mirror_prevbuild.json', '5')
    add('ferry C5', 'the four standing arms` figures tool and b712`s baselines', os.path.exists(p('tools', 'b706_standing_figures.py')) and os.path.exists(p('data', 'b712_standing_figures.json')),
        'tools/b706_standing_figures.py ; data/b712_standing_figures.json', '5')
    add('ferry C5', 'the chain halves as b693 drew them, b713 added to the second', K.CHAIN_HALVES[1] == ('b659', 'b713'), 'tools/b713_worklist.py CHAIN_HALVES', '5')
    add('ruling (10)', 'W-ORD-KEYSTONE-HEADS (OPEN_TRAILS :15454) and W-ORD-LV-PORT-TAG (:15848) for b714', 'W-ORD-KEYSTONE-HEADS' in at(ot, 15454) and 'W-ORD-LV-PORT-TAG' in at(ot, 15848),
        ':15454 ; :15848', '6')
    add('ferry read-first', 'OPEN_TRAILS :15914, b712`s open orders', at(ot, 15914).startswith('**The open orders:**'), ':15914', '0')
    add('ferry C0', 'this act`s session transcript (the same session as b712)', os.path.exists(C.SESSION), C.SESSION, '0')
    standing_rows(text, add)
    return R


def standing_rows(text, add):
    """the citation tool reads the standing clauses by version (data/b712_rules.txt row (1)): for each version a ferry names as "standing clauses v<N>"
    outside a quotation, the bank data/standing_clauses_v<N>.txt present with its VERSION line -- v1 with its control banked AS WANTED; a version this
    act writes at step zero (v2, (R323)(2)) read as TO BE WRITTEN when absent and from the bank when present."""
    import b712_standing as SC
    flat = re.sub(r'“[^”]*”', '', ' '.join(text.split()))
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing clauses(?:’)? v(\d+)', flat, re.I)))
    for v in names or [1]:
        p = os.path.join(D, 'standing_clauses_v%d.txt' % v)
        t = rd(p) or ''
        ver = re.search(r'^VERSION: (\d+)$', t, re.M)
        if v == 1:
            ctl = _jl('b712_standing_control.json')
            add('ferry (standing clauses)', 'the standing clauses v1: data/standing_clauses_v1.txt', bool(t) and bool(ver) and ver.group(1) == '1' and bool(SC.parse(t)) and ctl.get('ok') is True,
                'present %s ; VERSION %s ; rows %d ; the re-assembly control AS WANTED %s' % (bool(t), ver.group(1) if ver else 'NONE', len(SC.parse(t)), ctl.get('ok')), '0')
        elif not t:
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- TO BE WRITTEN at step zero ((R323)(2))' % (v, v), True, 'absent, as ordered', '0')
        else:
            add('ferry (standing clauses)', 'the standing clauses v%d: data/standing_clauses_v%d.txt' % (v, v), bool(ver) and ver.group(1) == str(v), 'present ; VERSION %s' % (ver.group(1) if ver else 'NONE'), '0')


def _write(L, R, miss):
    for n_ in ('b713_citation_check.txt', 'b713_citation_check.json'):
        MEM.guard('b713', n_, _root_exclude())
    for name, data in (('b713_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b713_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        with open(q + '.tmp', 'wb') as fh:
            fh.write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b713 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the source: the ruling and the ferry as pasted, read from the session transcript (%d characters, %r to %r); every cite checked at '
         'HEAD; rows are cites: where | what | OK or MISS | how | the component that cites it.' % (len(text), ANCHOR, TAIL), '']
    for where, what, ok, how, comp in R:
        L.append('  %-4s | %s | %s | %s | Component %s' % ('OK' if ok else 'MISS', where, what, how, comp))
    L += ['', '### THE MISSES, EACH RAISED TO THE AUTHOR OR ENTERED BY THE FACT CLAUSE BEFORE THE COMPONENT THAT CITES IT RUNS (none repaired silently):']
    L += ['  %s -- %s (Component %s)' % (what, how, comp) for _w, what, ok, how, comp in miss] or ['  NONE']
    L += ['', '### ### **CITES CHECKED %d ; OK %d ; MISSES %d.**' % (len(R), len(R) - len(miss), len(miss))]
    if 'dry' in a:
        print(NL.join(L))
        return
    _write(L, R, miss)
    print(NL.join(L[-(len(miss) + 4):]))


def ferry(*a):
    """the ferry is banked by the Write tool (data/b713_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b713_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b713_ferry_scan.txt')
    MEM.guard('b713', 'b713_ferry_scan.txt', _root_exclude())
    with open(s + '.tmp', 'wb') as fh:
        fh.write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b713_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
        len(banked), len(text), eq, r.returncode))
    if not eq:
        i = next((k for k in range(min(len(banked), len(text))) if banked[k] != text[k]), min(len(banked), len(text)))
        print('  the first difference at %d: banked %r ; transcript %r' % (i, banked[i - 20:i + 40], text[i - 20:i + 40]))


# ### b706's repair of the answer checker (b705 defect (n)), carried: a token that a bank's row names as a sha256 -- the root list, a hashes
# ### bank's row, a bank line carrying "sha256" -- or that a kernel's lakefile or manifest pins as a rev, is not a commit.
_HEX8 = re.compile(r'(?<![0-9a-f])([0-9a-f]{8})(?![0-9a-f])')


def _sha_rows():
    out = {}
    for q in [os.path.join(D, 'act_roots.txt')] + sorted(glob.glob(os.path.join(D, '*.txt')), reverse=True):   # ### the later act's row named first
        t = rd(q) or ''
        if 'sha256' not in t and not q.endswith('act_roots.txt') and not q.endswith('_hashes.txt'):
            continue
        for i, l in enumerate(t.split(NL), 1):
            if 'sha256' in l or q.endswith('act_roots.txt') or q.endswith('_hashes.txt'):
                for m in re.finditer(r'(?<![0-9a-f])([0-9a-f]{64})(?![0-9a-f])', l):
                    out.setdefault(m.group(1)[:8], ('data/' + os.path.basename(q), i))
    for kd in sorted(d_ for d_ in os.listdir('D:/') if d_.startswith('SIDE-') and os.path.isdir(os.path.join('D:/', d_, '.git'))):
        for f in ('lakefile.toml', 'lakefile.lean', 'lake-manifest.json'):
            t = rd(os.path.join('D:/', kd, f)) or ''
            for i, l in enumerate(t.split(NL), 1):
                for m in re.finditer(r'(?:rev\s*=\s*"|"rev"\s*:\s*"|@\s*"|rev\s+")([0-9a-f]{40})"', l):
                    out.setdefault(m.group(1)[:8], ('%s/%s' % (kd, f), i))
    return out


def answer(needle, *a):
    """(R278)(4): b682's route, imported, with its act names pointed at b713, and b706's repair carried."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.C.SESSIONS_AFTER = C.SESSIONS_AFTER
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, K.LV_DIR, K.JOIN_DIR, 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects', 'D:/SIDE-bijection', 'D:/SIDE-interfaces', 'D:/SIDE-li-map',
                                                 'D:/SIDE-kernel') if r not in P.REPOS and os.path.isdir(r))
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b713'))
    shas = _sha_rows()
    base = P.C._user_texts

    def masked(*k, **kw):
        out = []
        for t in base(*k, **kw):
            if t and needle in t:
                for m in _HEX8.finditer(t):
                    h8 = m.group(1)
                    if h8 in shas:
                        print('  ### SHA256 PREFIX %s... NAMED BY %s :%d -- a root or file hash by its bank`s row, not a commit; OK, masked from the commit reading' % (h8, shas[h8][0], shas[h8][1]))
                        t = t.replace(h8, 'SHA-' + h8[:4] + '-' + h8[4:])
            out.append(t)
        return out

    P.C._user_texts = masked
    src = open(os.path.join(T, 'b682_citation.py'), encoding='utf-8').read()
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b713')
    # ### (R323)(2), the item repair: THE WHOLE ANSWER. b682's cut ends at the first "END" after the needle (`best.find('END', k)`, :221), which a
    # ### word carrying END (AMENDMENT, APPENDED, RECOMMENDED) ends inside: b712's answers read 468 characters. The cut now ends at the answer's
    # ### last END (`best.rfind('END')`), the paste's own tail; the substitution printed, the route refusing where it does not apply.
    if body.count("best.find('END', k)") != 1:
        sys.exit('### b682`s CUT NOT FOUND ONCE IN ITS answer -- NOTHING CHECKED')
    body = body.replace("best.find('END', k)", "best.rfind('END')")
    body = body.replace("    open(q + '.tmp', 'wb')", "    MEM.guard('b713', os.path.basename(q), ROOT_EXCLUDE)\n    open(q + '.tmp', 'wb')")
    ns = dict(vars(P))
    ns.update(MEM=MEM, ROOT_EXCLUDE=_root_exclude())
    exec(compile(body, 'b682_citation.answer (b713)', 'exec'), ns)
    ns['answer'](needle)


def replay(needle, session_id, anchor, *a):
    """`replay <needle> <session id> <anchor>`: the repair's control, print only -- b682's selection (:210-:219, the latest user text after the
    anchor carrying the needle and an answer's mark) over the named session, then its cut two ways: b682's (`best.find('END', k)`) and the
    repaired (`best.rfind('END')`); each cut's length and its last 60 characters printed; nothing written."""
    import b682_citation as P
    P.C.SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % session_id
    P.C.SESSIONS_AFTER = ()
    best, seen = None, False
    for t in P.C._user_texts():
        if anchor in t:
            seen = True
        u = t.replace('\u2019', "'")
        if seen and needle in t and ("NAVIGATOR'S ANSWER" in u or "NAVIGATOR'S NOTE" in u or "AUTHOR'S" in u or 'The user answered' in u
                                     or 'user has answered' in u):
            best = t
    if best is None:
        print('  ### NO ANSWER CARRYING %r AFTER %r IN SESSION %s' % (needle, anchor, session_id))
        return
    k = best.find(needle)
    out = {}
    for label, e0 in (('b682', best.find('END', k)), ('repaired', best.rfind('END'))):
        b0 = best.rfind('BEGIN', 0, k)
        cut = best[b0:e0 + 3] if b0 >= 0 and e0 > k else best
        out[label] = cut
        print('  %-8s cut: %d characters ; ends %r' % (label, len(cut), cut[-60:]))
    print('  the whole answer %d characters ; the repaired cut equal to the text from its BEGIN to its last END: %s' % (
        len(best), out['repaired'] == best[best.rfind('BEGIN', 0, k):best.rfind('END') + 3]))
    return dict((k_, len(v)) for k_, v in out.items())


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
    fn = {'check': check, 'ferry': ferry, 'answer': answer, 'word': word, 'replay': replay}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b713_citation.py check [dry] | ferry | answer <needle> | word <needle> | replay <needle> <session id> <anchor>')
        sys.exit(2)
    fn(*sys.argv[2:])
