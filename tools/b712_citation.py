# -*- coding: utf-8 -*-
"""b712_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b712's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (ec2d71b5, a NEW session after the author's /clear; the anchor (R322)'s line); the answer route is b682's, imported from
### tools/b682_citation.py with its act names pointed at b712, b706's repair carried (a bare eight-hex token a bank names as a sha256 or a
### kernel's lakefile pins as a rev is not read as a commit); the `word` route is b694's. Routes: `check [dry]` -> data/b712_citation_check.txt
### (.json) ; `ferry` -> data/b712_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the check on one answer.
### Written by the Write tool at b712 from b711_citation.py's form (its engine :1-:101 and :344-:484, read at step zero), its cite rows this
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
import b712_worklist as K   # noqa: E402
import act_membrane as MEM  # noqa: E402  ### (R322)(2)(ii): the membrane before every bank write of this tool


def _root_exclude():
    import b712_record as REC   # ### the record tool's exclusion pattern, the one the root route reads (imported at the call, nothing written)
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
    # ### b712: the cite rows of (R322) and its ferry, written by the Edit tool after b711's rows were pruned (data/b712_prune_citation.txt)
    for f in ('data/b711_closing.txt', 'data/b711_defects.txt', 'data/b711_events.txt', 'data/standing_clauses_v2.txt', 'data/b711_port.txt',
              'data/b711_buildlog_SIDE-lv-conservation_port.txt', 'data/b711_report.txt', 'data/b711_steps.json', 'data/b710_registrations.txt',
              'data/b711_closing_push_out.txt', 'data/b670_licensed_table.txt', 'data/b703_rules.txt', 'data/b708_cut.txt', 'data/b708_tie.txt',
              'data/b711_pairs.txt', 'data/b711_coeffs.txt', 'data/b711_surgery.txt', 'data/b711_axis.txt', 'data/b711_list.txt', 'data/b711_independence.txt',
              'data/b711_mirror.txt', 'data/b711_scores_close.json', 'data/b711_scores.json', 'data/b711_regspec_run.txt', 'data/b711_author_answers.txt',
              'data/b711_commands.json', 'data/b711_root_banks.txt', 'data/b711_checks.txt', 'data/b711_checks_postpush.txt', 'data/b711_standing_figures.json',
              'data/b675_corrigenda.txt', 'data/act_roots.txt', 'data/b675_rules.txt', 'data/b684_rules.txt', K.B711_FACE, 'tools/b711_worklist.py',
              'tools/b711_record.py', 'tools/b711_checks.py', 'tools/b711_closing.py', 'tools/b711_citation.py', 'tools/b711_corrigendum.py', 'tools/b711_regspec.py',
              'tools/b711_reg_gate.py', 'tools/b711_tests.py', 'tools/b711_report.py', 'tools/b711_carry.py', 'tools/b711_standing.py', 'tools/b710_standing.py',
              'tools/b706_standing_figures.py', 'tools/circuit_read.py', 'tools/mirror_verify.py', 'tools/mirror_build.ps1', 'tools/mirror_prevbuild.json',
              'tools/push_gated.sh', 'tools/act_root.py', 'tools/act_membrane.py', 'tools/ferry_scan.py', 'tools/b682_citation.py', 'tools/b678_corrigendum.py'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    # ### (R322)(1): b711 at its weight
    cl = lines_of(p('data', 'b711_closing.txt'))
    q = _quote(text, 'b711 closed: relay', '”; its prompt count')
    add('ruling (1)', 'data/b711_closing.txt :1, the head line, against (R322)(1)`s quote', q == cl[0], 'quote %d characters, the line %d ; equal byte for byte %s' % (len(q), len(cl[0]), q == cl[0]), '0-1')
    ev = lines_of(p('data', 'b711_events.txt'))
    starts = [i + 1 for i, l in enumerate(ev) if re.match(r'^    [A-Z]', l)]
    add('ruling (1)', 'events :79, the head line`s prompt count and its missing score', 'THE CLOSING\'S HEAD LINE: NO SCORE' in at(ev, 79), 'data/b711_events.txt :79 %r' % at(ev, 79).strip()[:70], '1')
    pr = lines_of(p('data', 'b711_pairs.txt'))
    add('ruling (1)', 'pair 11 ratio 0.998460 and pair 15 ratio 0.998079', 'n*/F2 0.998460' in at(pr, 12) and 'n*/F2 0.998079' in at(pr, 13), 'data/b711_pairs.txt :12, :13', '1')
    reg = (g(ROOT, 'log', '--format=%h', '--', 'data/b710_registrations.txt')[1] or '').split()
    add('ruling (1)', 'each prediction read unchanged at 41ff1193 (the bank`s one commit)', reg == ['41ff1193'], 'git log of data/b710_registrations.txt: %s' % reg, '1')
    co = lines_of(p('data', 'b711_coeffs.txt'))
    add('ruling (1)', 'Q0`s coefficients negative from n = 48, c(48) = -8 log 2 - 2 log 3 = -2 log 48', 'NEGATIVE FROM n = 48 (c = (-8) log 2 + (-2) log 3)' in at(co, 18) and '-2 log 48' in at(co, 13),
        'data/b711_coeffs.txt :18, :13', '1')
    add('ruling (1)', 'the surgery HELD', 'THE SURGERY HELD' in at(lines_of(p('data', 'b711_surgery.txt')), 36), 'data/b711_surgery.txt :36', '1')
    add('ruling (1)', 'the axis (e) REFUTED', 'THE AXIS (e) REFUTED' in at(lines_of(p('data', 'b711_axis.txt')), 60), 'data/b711_axis.txt :60', '1')
    li = lines_of(p('data', 'b711_list.txt'))
    on_off = re.findall(r'on-line (\d+) \| off-line (\d+)', ' '.join(li[:16]))
    add('ruling (1)', 'the certified list complete to 445, 170 on-line and 23 off-line zeros added above 325', 'THE LIST COMPLETE TO 445.0' in at(li, 19)
        and sum(int(a) for a, _b in on_off) == 170 and sum(int(b) for _a, b in on_off) == 23, 'data/b711_list.txt :19 ; the bands` rows :1-:16 sum on-line %d, off-line %d over %d bands' % (
            sum(int(a) for a, _b in on_off), sum(int(b) for _a, b in on_off), len(on_off)), '1')
    add('ruling (1)', 'the Independence supplement in data/b711_independence.txt', '**' in (rd(p('data', 'b711_independence.txt')) or ''), 'data/b711_independence.txt', '1')
    rp_ = lines_of(p('data', 'b711_report.txt'))
    add('ruling (1)', 'the throughstone report 21 of 21 EQUAL', 'THE COMPARISONS (21)' in at(rp_, 16) and '0 DIFFERS' in at(rp_, 21), 'data/b711_report.txt :16, :21', '1')
    po = lines_of(p('data', 'b711_port.txt'))
    add('ruling (1); ruling (4)', 'the port at 11 of 12, held at DirichletC7Order.lean :501:31 (data/b711_port.txt :11)', 'DirichletC7Order.lean:501:31' in at(po, 11) and 'StrongFEPair.Λ_eq' in at(po, 11)
        and re.search(r'\b11 of 12\b', ' '.join(po)) is not None, 'data/b711_port.txt :11 ; "11 of 12" in the bank %s' % (re.search(r'\b11 of 12\b', ' '.join(po)) is not None), '1-2')
    add('ruling (1)', 'the entry at FINDINGS :10306', at(fi, 10306).startswith('## '), 'FINDINGS :10306 %r' % at(fi, 10306)[:80], '1')
    add('ruling (1)', 'the trail at OPEN_TRAILS :15850 carrying the root afa0d8f9', at(ot, 15850).startswith('### b711') and 'afa0d8f9' in ' '.join(ot[15849:15890]),
        'OPEN_TRAILS :15850 %r ; afa0d8f9 in its record %s' % (at(ot, 15850)[:50], 'afa0d8f9' in ' '.join(ot[15849:15890])), '1')
    row = act_root_line('b711')
    rb = ' '.join(lines_of(p('data', 'b711_root_banks.txt')))
    add('ruling (1)', 'the root afa0d8f9 over 122 banks', bool(row) and row[0][1].startswith('afa0d8f9') and 'BANKS 122' in rb,
        'data/act_roots.txt row b711 %s ; data/b711_root_banks.txt BANKS 122 %s' % (row[0][1][:16] if row else 'NONE', 'BANKS 122' in rb), '1')
    scc = _jl('b711_scores_close.json')
    flat = json.dumps(scc)
    # ### the verdict is each score's first field (its reading the second): the first form of this row counted the word REFUTED anywhere and
    # ### read S3's reading (:12, "the axis (e) REFUTED") as a score -- a defect of the matcher, corrected before the bank (both figures printed)
    verd = dict((k, (v[0] if isinstance(v, list) and v else v)) for k, v in scc.items() if re.match(r'^[NS][1-5]$', k))
    add('ruling (1)', 'N1-N5 and S1-S3 HELD at scores close', len(verd) == 8 and all(v == 'HELD' for v in verd.values()),
        'data/b711_scores_close.json verdicts %s ; the words in the whole bank: HELD %d, REFUTED %d (the reading of :12)' % (
            ' '.join('%s %s' % kv for kv in sorted(verd.items())), flat.count('"HELD"'), flat.count('REFUTED')), '1')
    mr = rd(p('data', 'b711_mirror.txt')) or ''
    add('ruling (1)', 'the mirror mirror-refresh-2026-10-25-b711.zip (sha256 f01cb32d…) CLEAN on all three clauses with the root line',
        'f01cb32d' in mr and 'CLEAN ON ALL THREE CLAUSES' in mr and 'afa0d8f9' in mr and os.path.exists(K.MIRROR_ZIP),
        'data/b711_mirror.txt: f01cb32d %s ; CLEAN %s ; the root line afa0d8f9 %s ; the zip exists %s' % ('f01cb32d' in mr, 'CLEAN ON ALL THREE CLAUSES' in mr, 'afa0d8f9' in mr, os.path.exists(K.MIRROR_ZIP)), '1')
    cpp, cpr = rd(p('data', 'b711_checks_postpush.txt')) or '', rd(p('data', 'b711_checks.txt')) or ''
    fl = re.search(r'LIVE FAILING : \d+ (\[.*?\])', cpp)
    add('ruling (1)', 'suite 138 of 143 pre-push and post-push, NOT CLEAN, the three carried and G-ANSWERS-BANKED and G-NOTHING-RAN-AHEAD',
        'LIVE PASSING : 138' in cpp and 'LIVE PASSING : 138' in cpr and 'ARMS RUN : 143' in cpp and bool(fl) and 'G-ANSWERS-BANKED' in fl.group(1) and 'G-NOTHING-RAN-AHEAD' in fl.group(1),
        'data/b711_checks.txt, data/b711_checks_postpush.txt: failing post-push %s' % (fl.group(1) if fl else 'NONE'), '1')
    dl = lines_of(p('data', 'b711_defects.txt'))
    lets = ''.join(m.group(1) for l in dl for m in [re.match(r'^    \(([a-z])\) ', l)] if m)
    add('ruling (1)', 'ten defects (a)-(j) lettered before the seal', lets == 'abcdefghij', 'data/b711_defects.txt letters %s' % lets, '1')
    add('ruling (1); ruling (2)', 'sixteen events in data/b711_events.txt (each event`s starting line, four spaces and a capital)', len(starts) == 16,
        'starting lines %s' % starts, '1')
    add('ruling (1); ruling (10)', '"Nothing deposited": the draft at v5, held', K.DRAFT == '23228113', 'tools/b712_worklist.py DRAFT', '6')
    # ### (R322)(2): the corrigendum's sixteen starting lines, lettered and records
    lettered, records = [3, 11, 15, 22, 46, 61, 66, 75, 79], [29, 39, 43, 51, 55, 58, 71]
    add('ruling (2)', 'the nine lettered starting lines and the seven records are the events` sixteen, once each', sorted(lettered + records) == starts,
        'lettered %s ; records %s ; the bank`s %s' % (lettered, records, starts), '1')
    for n, needle in ((3, 'FOUR PIPES AT COMPONENT 5'), (11, 'QUESTION COUNT'), (15, 'REPORT TOOL'), (22, 'S2 NOT SCORABLE'), (46, 'PORT CLAUSE'), (61, 'POST-SEAL PROMPT'),
                      (66, 'AHEAD OF THE LOCK'), (75, 'MIRROR BANKED ONCE'), (79, 'HEAD LINE'), (29, 'THE AUTHOR\'S WORD ON S2'), (39, 'CITES'), (43, 'AUTO-MODE NOTE'),
                      (51, 'MEMORY HOLD'), (55, 'RE-READ'), (58, 'RESUMED'), (71, 'THE SUITE AND THE SCORES')):
        add('ruling (2)', 'data/b711_events.txt :%d, the item the ruling names there' % n, needle in at(ev, n), ':%d %r' % (n, at(ev, n).strip()[:70]), '1')
    mp = (g(ROOT, 'log', '-1', '--format=%h %s', '--', 'tools/mirror_prevbuild.json')[1] or '').strip()
    cs = [i + 1 for i, l in enumerate(cl) if 'mirror_prevbuild.json' in l and 'committed with this closing' in l]
    add('ruling (2)', 'the closing`s sentence "committed with this closing" for tools/mirror_prevbuild.json, its blob unchanged since b707', mp.split(' ', 1)[-1].startswith('b707') and bool(cs),
        'the file`s last commit %r ; data/b711_closing.txt lines carrying the sentence %s' % (mp[:70], cs), '1')
    cg = lines_of(p('data', 'b675_corrigenda.txt'))
    last = [l for l in cg if re.match(r'^\s*\((\d+)\)', l)]
    add('ruling (2)', 'the corrigenda bank, appended only (its last row (31), b711`s)', bool(last) and re.match(r'^\s*\(31\)', last[-1]) is not None,
        'data/b675_corrigenda.txt, last row %r' % (last[-1][:40] if last else ''), '1')
    # ### (R322)(3): the five faces' objects
    fc = lines_of(p(*K.B711_FACE.split('/')))
    ck = rd(p('tools', 'b711_checks.py')) or ''
    add('ruling (3)(i)', 'the face`s "POST-SEAL PROMPTS NAMED: NONE" (data/b711_registration_2026-10-25.txt :96) and G-ANSWERS-BANKED in the suite',
        at(fc, 96) == '### POST-SEAL PROMPTS NAMED: NONE' and "'G-ANSWERS-BANKED'" in ck, ':96 %r' % at(fc, 96), '1')
    st = _jl('b711_steps.json').get('rows', [])
    gate = [r_ for r_ in st if r_.get('commit', '').startswith('85c26c1c')]
    add('ruling (3)(ii)', 'the gate`s commit 85c26c1c in b711`s step bank (the row`s subject names "the gate before the lock"; the bank carries no field marked gate)',
        bool(gate) and 'the gate before the lock' in gate[0].get('subject', '') and "'G-NOTHING-RAN-AHEAD'" in ck,
        'data/b711_steps.json row %s phase %r' % (gate[0]['commit'][:8] if gate else 'NONE', gate[0].get('phase') if gate else ''), '1')
    aa = rd(p('data', 'b711_author_answers.txt')) or ''
    add('ruling (3)(iii)', 'b711`s answers bank holds one prompt (the root`s)', len(re.findall(r'^### PROMPT \d+', aa, re.M)) == 1, 'data/b711_author_answers.txt PROMPT rows %d' % len(re.findall(r'^### PROMPT \d+', aa, re.M)), '1')
    add('ruling (3)(iv)', 'b711`s mirror sequence (events :75: mbuild, mverify, mbank, then mroot)', 'mroot route had not run' in ' '.join(ev[74:78]), 'data/b711_events.txt :75-:78', '1')
    rs = lines_of(p('data', 'b711_regspec_run.txt'))
    add('ruling (3)(v)', 'b711`s stale bank ANYPIPES 7 (data/b711_regspec_run.txt :61) and the fresh bank`s eight (events :3-:4)', at(rs, 61).split() == ['ANYPIPES', '7'] and 'eight commands' in ' '.join(ev[2:5]),
        ':61 %r' % at(rs, 61), '1')
    add('ruling (3)', 'the throughstone report`s four footings KERNEL, CERTIFIED, REGISTERED, HELD (data/b711_report.txt :3)', '(KERNEL, CERTIFIED, REGISTERED, HELD)' in at(rp_, 3), ':3', '1')
    for f in ('data/standing_clauses_v3.txt', 'data/b712_registrations.txt'):
        add('ruling (3); ruling (6)', '%s -- written and committed alone at step zero' % f, os.path.exists(p(*f.split('/'))), 'present', '0')
    for f in ('data/b712_tool_repairs.txt', 'data/b712_report.txt', 'data/b712_port.txt', 'data/b712_join_grade.txt', 'data/b712_price.txt', 'data/b712_readfirst.txt',
              'data/b712_rules.txt', 'data/b713_rules.txt'):
        add('ruling (3)-(9)', '%s -- TO BE WRITTEN by this act' % f, not os.path.exists(p(*f.split('/'))), 'absent, as ordered', '0-6')
    # ### (R322)(4): the port and the join
    loc = (g(K.LV_DIR, 'rev-parse', 'port-b707')[1] or '').strip()
    add('ruling (4)', 'port-b707 at b711`s one commit be3052ac (the edit`s base)', loc == K.PORT_TIP, 'local port-b707 %s' % loc[:8], '2')
    blob = _blob(K.LV_DIR, K.PORT_TIP, K.PORT_MODULE).split(NL)
    add('ruling (4)', 'the module at the port`s tip, its line 501 carrying StrongFEPair.Λ_eq', 'StrongFEPair.Λ_eq' in at(blob, 501), '%s at be3052ac: %d lines ; :501 carries the name %s' % (K.PORT_MODULE, len(blob), 'StrongFEPair.Λ_eq' in at(blob, 501)), '2')
    rpn = _blob(K.LV_DIR, K.LV_V0100, 'SIDELvConservation/RegisterPentagon.lean')
    add('ruling (4)', 'Register4_positivity at 93c27ec', 'Register4_positivity' in rpn, 'SIDELvConservation/RegisterPentagon.lean at 93c27ec :%d' % first(rpn.split(NL), 'Register4_positivity'), '2')
    lv_tags = (g(K.LV_DIR, 'tag', '--points-at', K.LV_V0100)[1] or '').split()
    add('ruling (4)', '93c27ec the deposit v0.10.0', 'v0.10.0' in lv_tags, 'tags at 93c27ec: %s' % lv_tags, '2')
    jl = rd(os.path.join(K.JOIN_DIR, 'lakefile.lean')) or rd(os.path.join(K.JOIN_DIR, 'lakefile.toml')) or ''
    add('ruling (4)', 'SIDE-faces-join`s lakefile requiring SIDE-lv-conservation by revision', 'SIDE-lv-conservation' in jl or 'sideLvConservation' in jl, 'the lakefile names lv %s' % ('SIDE-lv-conservation' in jl or 'sideLvConservation' in jl), '2')
    fj = (g(K.JOIN_DIR, 'grep', '-l', '-w', 'faces_join', 'HEAD', '--', '*.lean')[1] or '').strip()
    add('ruling (4)', 'faces_join at SIDE-faces-join', bool(fj), 'files %s' % fj, '2')
    wf = os.path.exists(os.path.join(K.LV_DIR, '.github', 'workflows', 'build-module.yml')) and os.path.exists(os.path.join(K.JOIN_DIR, '.github', 'workflows', 'build-module.yml'))
    add('ruling (4)', 'the two workflows the dispatches run (lv`s at the port branch and the join`s build-module.yml)', wf, 'both present at the working trees %s' % wf, '2')
    jt = (g(K.JOIN_DIR, 'tag', '-l')[1] or '').split()
    add('ruling (4)', 'SIDE-faces-join untagged (v0.1.0 only on DERIVES)', not jt, 'tags %s' % jt, '2')
    add('ruling (4); ferry read-first', 'W-ORD-LV-FORWARD-PORT at OPEN_TRAILS :15686, its latest open-orders row :15876, W-ORD-LV-CLOSURE-JOIN :15452, W-ORD-LV-PORT-TAG :15848',
        'W-ORD-LV-FORWARD-PORT' in at(ot, 15686) and 'W-ORD-LV-FORWARD-PORT' in at(ot, 15876) and ':501:31' in at(ot, 15876) and 'W-ORD-LV-CLOSURE-JOIN' in at(ot, 15452) and 'W-ORD-LV-PORT-TAG' in at(ot, 15848),
        'OPEN_TRAILS :15686, :15876, :15452, :15848', '2')
    later = [i + 1 for i, l in enumerate(ot) if i + 1 > 15876 and 'W-ORD-LV-FORWARD-PORT' in l]
    add('ferry read-first', ':15876 the latest open-orders row naming W-ORD-LV-FORWARD-PORT', not later, 'later lines naming it %s' % later, '0')
    # ### (R322)(5)-(7)
    fl_ = lines_of(os.path.join(PP, 'FACES_LEDGER.md'))
    add('ruling (5); ferry read-first', 'the faces ledger (PLACE-papers FACES_LEDGER.md) and its rows', len([l for l in fl_ if l.startswith('|')]) > 2,
        'FACES_LEDGER.md %d lines, table rows %d' % (len(fl_), len([l for l in fl_ if l.startswith('|')])), '3')
    r10 = lines_of(p('data', 'b710_registrations.txt'))
    add('ruling (6)', 'data/b710_registrations.txt (i), the refined law (:10-:43), its falsifier at :43', at(r10, 10).strip().startswith('(i) THE REFINED DETECTION LAW') and at(r10, 43).strip().startswith('FALSIFIER'),
        ':10 ; :43', '0, 3')
    first_c = (g(ROOT, 'rev-list', '--reverse', '%s..HEAD' % K.PRE_RELAY)[1] or '').split()
    add('ruling (6); N3', 'data/b712_registrations.txt committed alone, the act`s first commit', bool(first_c) and first_c[0] == K.REG_COMMIT,
        'the first commit after %s: %s' % (K.PRE_RELAY, first_c[0][:8] if first_c else 'NONE'), '0')
    lt = lines_of(p('data', 'b670_licensed_table.txt'))
    add('ruling (7)', 'the bank holding the licensed table, data/b670_licensed_table.txt, its agenda (:89-:123)', at(lt, 89).startswith('### B. PER AGENDA DOCUMENT') and 'AGENDA DOCUMENTS 33' in at(lt, 123),
        ':89 ; :123', '4')
    r3 = lines_of(p('data', 'b703_rules.txt'))
    add('ruling (7)', 'the keystone form, the author`s word of 2026-10-21 (data/b703_rules.txt row (1) :6-:9)', 'THE STEPS TO COMPILE BEFORE THE WRITE-UPS' in at(r3, 6) and '2026-10-21' in at(r3, 6) and 'back matter' in at(r3, 7),
        ':6 ; :7', '4')
    add('ruling (7)', 'the last re-cut of the table (b708: day1/Spectral_Inertness.md)', 'day1/Spectral_Inertness.md' in at(lines_of(p('data', 'b708_cut.txt')), 3), 'data/b708_cut.txt :3', '4')
    # ### (R322)(8): the carried files and the branches
    c1 = (g(ROOT, 'log', '--format=%h', '--', 'data/b711_closing_push_out.txt')[1] or '').split()
    add('ruling (8)', 'data/b711_closing_push_out.txt committed alone at step zero', c1 == [K.STEPZERO[:8]], 'its commits %s' % c1, '0')
    c2 = (g(ROOT, 'show', '--stat', '--format=%h', K.STEPZERO_STEPS)[1] or '')
    add('ruling (8)', 'the closing`s step row in data/b711_steps.json committed alone at step zero', '1 file changed' in c2 and 'data/b711_steps.json' in c2, 'commit %s' % K.STEPZERO_STEPS[:8], '0')
    merged = g(ROOT, 'branch', '--merged', 'main')[1] or ''
    mpp = g(PP, 'branch', '--merged', 'main')[1] or ''
    for repo, names in K.DELETE:
        lst = merged if repo == 'D:/relay' else mpp
        for b in names:
            add('ruling (8)', '%s %s (local, listed --merged)' % (os.path.basename(repo), b), b in [x.strip(' *') for x in lst.split(NL)], 'listed by `git branch --merged main` before any delete', '0')
    push711 = sorted(x.strip(' *') for x in merged.split(NL) if x.strip(' *').startswith('push-b711')) + sorted(x.strip(' *') for x in mpp.split(NL) if x.strip(' *').startswith('push-b711'))
    add('ruling (8)', 'the push-b711 branches of the relay and of PLACE-papers are the seven the worklist names (data/b711_closing.txt :452)', len(push711) == 7 == sum(len(n) for _r, n in K.DELETE)
        and 'push-b711' in at(cl, 452), 'listed %s' % push711, '0')
    lh = _remote_heads(K.LV_DIR)
    add('ruling (8)', 'port-b707 at be3052ac locally and at the remote, NOT deleted (one ls-remote of SIDE-lv-conservation)', loc == K.PORT_TIP and lh.get('refs/heads/port-b707') == K.PORT_TIP,
        'local %s ; remote %s' % (loc[:8], (lh.get('refs/heads/port-b707') or '')[:8]), '0')
    add('ruling (8)', 'the 2,560 MB hold', K.HOLD == 2560, 'tools/b712_worklist.py HOLD', '0')
    # ### (R322)(9)-(11) and the ferry's standing references
    add('ruling (9)', 'the READFIRST-CLOSURE reader', os.path.exists(p('tools', 'circuit_read.py')), 'tools/circuit_read.py (readfirst)', '0')
    add('ruling (9)', 'tools/mirror_prevbuild.json, the mirror builder`s state file, named in (W)', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'tools/mirror_prevbuild.json', '5')
    add('ferry C5', 'the four standing arms` figures tool and b711`s baselines', os.path.exists(p('tools', 'b706_standing_figures.py')) and os.path.exists(p('data', 'b711_standing_figures.json')),
        'tools/b706_standing_figures.py ; data/b711_standing_figures.json', '5')
    add('ferry C0', 'data/b684_rules.txt row (1), a test file over 450 s its own part', os.path.exists(p('data', 'b684_rules.txt')), 'data/b684_rules.txt :5', '0')
    add('ferry C5', 'the chain halves as b693 drew them, b712 added to the second', K.CHAIN_HALVES[1] == ('b659', 'b712'), 'tools/b712_worklist.py CHAIN_HALVES', '5')
    add('ferry C0', 'this act`s session transcript (a new session) and b711`s', os.path.exists(C.SESSION) and os.path.exists('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.PREV_SESSION), C.SESSION, '0')
    standing_rows(text, add)
    return R


def standing_rows(text, add):
    """the citation tool reads the standing clauses by version (data/b711_rules.txt row (1)): for each version a ferry names as "standing clauses v<N>"
    outside a quotation, the bank data/standing_clauses_v<N>.txt present with its VERSION line -- v1 with its control banked AS WANTED; a version this
    act writes at step zero (v2, (R322)(2)) read as TO BE WRITTEN when absent and from the bank when present."""
    import b711_standing as SC
    flat = re.sub(r'“[^”]*”', '', ' '.join(text.split()))
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing clauses(?:’)? v(\d+)', flat, re.I)))
    for v in names or [1]:
        p = os.path.join(D, 'standing_clauses_v%d.txt' % v)
        t = rd(p) or ''
        ver = re.search(r'^VERSION: (\d+)$', t, re.M)
        if v == 1:
            ctl = _jl('b711_standing_control.json')
            add('ferry (standing clauses)', 'the standing clauses v1: data/standing_clauses_v1.txt', bool(t) and bool(ver) and ver.group(1) == '1' and bool(SC.parse(t)) and ctl.get('ok') is True,
                'present %s ; VERSION %s ; rows %d ; the re-assembly control AS WANTED %s' % (bool(t), ver.group(1) if ver else 'NONE', len(SC.parse(t)), ctl.get('ok')), '0')
        elif not t:
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- TO BE WRITTEN at step zero ((R322)(2))' % (v, v), True, 'absent, as ordered', '0')
        else:
            add('ferry (standing clauses)', 'the standing clauses v%d: data/standing_clauses_v%d.txt' % (v, v), bool(ver) and ver.group(1) == str(v), 'present ; VERSION %s' % (ver.group(1) if ver else 'NONE'), '0')


def _write(L, R, miss):
    for n_ in ('b712_citation_check.txt', 'b712_citation_check.json'):
        MEM.guard('b712', n_, _root_exclude())
    for name, data in (('b712_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b712_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        with open(q + '.tmp', 'wb') as fh:
            fh.write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b712 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b712_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b712_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b712_ferry_scan.txt')
    MEM.guard('b712', 'b712_ferry_scan.txt', _root_exclude())
    with open(s + '.tmp', 'wb') as fh:
        fh.write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b712_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
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
    """(R278)(4): b682's route, imported, with its act names pointed at b712, and b706's repair carried."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.C.SESSIONS_AFTER = C.SESSIONS_AFTER
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, K.LV_DIR, K.JOIN_DIR, 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects', 'D:/SIDE-bijection', 'D:/SIDE-interfaces', 'D:/SIDE-li-map',
                                                 'D:/SIDE-kernel') if r not in P.REPOS and os.path.isdir(r))
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b712'))
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
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b712')
    # ### (R322)(2), the item repair: THE WHOLE ANSWER. b682's cut ends at the first "END" after the needle (`best.find('END', k)`, :221), which a
    # ### word carrying END (AMENDMENT, APPENDED, RECOMMENDED) ends inside: b711's answers read 468 characters. The cut now ends at the answer's
    # ### last END (`best.rfind('END')`), the paste's own tail; the substitution printed, the route refusing where it does not apply.
    if body.count("best.find('END', k)") != 1:
        sys.exit('### b682`s CUT NOT FOUND ONCE IN ITS answer -- NOTHING CHECKED')
    body = body.replace("best.find('END', k)", "best.rfind('END')")
    body = body.replace("    open(q + '.tmp', 'wb')", "    MEM.guard('b712', os.path.basename(q), ROOT_EXCLUDE)\n    open(q + '.tmp', 'wb')")
    ns = dict(vars(P))
    ns.update(MEM=MEM, ROOT_EXCLUDE=_root_exclude())
    exec(compile(body, 'b682_citation.answer (b712)', 'exec'), ns)
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
        print('usage: b712_citation.py check [dry] | ferry | answer <needle> | word <needle> | replay <needle> <session id> <anchor>')
        sys.exit(2)
    fn(*sys.argv[2:])
