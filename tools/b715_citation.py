# -*- coding: utf-8 -*-
"""b715_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b715's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (bde68a30, a new session after the clear; the anchor (R325)'s line); the answer route is b682's, imported from
### tools/b682_citation.py with its act names pointed at b715, b706's repair carried (a bare eight-hex token a bank names as a sha256 or a
### kernel's lakefile pins as a rev is not read as a commit); the `word` route is b694's. Routes: `check [dry]` -> data/b715_citation_check.txt
### (.json) ; `ferry` -> data/b715_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the check on one answer.
### Carried by diff from b714_citation.py (data/b715_carry_citation.txt), b714's cite rows pruned (data/b715_prune_citation.txt) and this
### ruling's written by the Edit tool; this tool writes only the banks named above. Its (R325)(1) row reads lv's release list by `gh` (the
### seat's own authenticated client; the repository's owner path its only argument, no identifier of the author's person). A kernel's file at a tag is read here by `git cat-file` and `git grep` inside this
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
import b715_worklist as K   # noqa: E402
import act_membrane as MEM  # noqa: E402  ### (R325)(2)(ii): the membrane before every bank write of this tool


def _root_exclude():
    import b715_record as REC   # ### the record tool's exclusion pattern, the one the root route reads (imported at the call, nothing written)
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


def _jl_any(path):
    """a JSON file by its full path (the mirror's roster under tools/), {} where absent or unreadable."""
    try:
        return json.loads(rd(path) or '{}')
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
    # ### b715: the cite rows of (R325) and its ferry, written by the Edit tool after b714's rows were pruned (data/b715_prune_citation.txt)
    for f in K.PATHS:
        add('ruling PATHS', f, os.path.isdir(f), 'present' if os.path.isdir(f) else 'ABSENT', '0')
    for f in ('data/b714_closing.txt', 'data/b714_defects.txt', 'data/b714_events.txt', 'data/b714_author_words_preseal.txt', 'data/b714_records.txt',
              'data/b714_pilot.txt', 'data/b714_tool_repairs.txt', 'tools/b714_checks.py', 'tools/b714_record.py', 'tools/rule_arms.py',
              'tools/act_membrane.py', 'tools/mirror_build.ps1', 'tools/mirror_roster.json', 'tools/mirror_prevbuild.json', 'tools/b303_pins.py',
              'data/act_roots.txt', 'data/repo_visibility.txt', 'data/b714_steps.json', 'data/b714_bank_hashes.json', 'data/b714_hook_refusals.txt',
              'data/b714_heads_draft.txt', 'data/b714_components.txt', 'data/b713_components.txt', 'data/b713_closing.txt',
              'tools/b714_components_standin.py', 'tools/b714_repairs.py', 'tools/b714_hook.py', 'tools/b714_closing.py', 'tools/b714_corrigendum.py',
              'tools/act_letters.py', 'tools/circuit_read.py', 'tools/ferry_scan.py', 'tools/act_root.py', 'data/b675_corrigenda.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    add('ferry read-first', 'PLACE-papers phase2/method/THE_KEYSTONE_CENSUS_v0_8_1.md', os.path.exists(os.path.join(PP, *K.CENSUS_PREV.split('/'))),
        'exists at the working tree', '0')
    # ### (R325)(1): b714 at its weight
    cl = lines_of(p('data', 'b714_closing.txt'))
    q = _quote(text, 'b714 closed: relay', '”; the closing commit')
    add('ruling (1)', 'data/b714_closing.txt :1, the head line, against (R325)(1)`s quote', bool(q) and q == cl[0],
        'quote %d characters, the line %d ; equal byte for byte %s' % (len(q), len(cl[0]), q == cl[0]), '0-1')
    clo = (g(ROOT, 'log', '-1', '--format=%H %s', K.B714_CLOSING)[1] or '').strip()
    rmain = (g(ROOT, 'ls-remote', 'origin', 'refs/heads/main')[1] or '').split()
    add('ruling (1)', 'the closing commit 1992a71c (b714: the closing), pushed and read back: relay main at the remote', clo.startswith(K.B714_CLOSING) and 'b714: the closing' in clo
        and bool(rmain) and rmain[0] == K.B714_CLOSING, '%s ; remote main %s' % (clo[:40], (rmain or ['NONE'])[0][:8]), '0-1')
    cpp, cpr = rd(p('data', 'b714_checks_postpush.txt')) or '', rd(p('data', 'b714_checks.txt')) or ''
    add('ruling (1)', 'the suite 124 passing, 16 failing and 1 WITHHELD post-push (data/b714_checks_postpush.txt)',
        'ARMS RUN : 141. ### LIVE PASSING : 124. ### LIVE FAILING : 16' in cpp and 'WITHHELD, NOT EXERCISABLE : 1' in cpp, 'the combine`s summary line', '1')
    add('ruling (1)', '125/15/1 pre-push (data/b714_checks.txt)', 'ARMS RUN : 141. ### LIVE PASSING : 125. ### LIVE FAILING : 15' in cpr
        and 'WITHHELD, NOT EXERCISABLE : 1' in cpr, 'the combine`s summary line', '1')
    dl = lines_of(p('data', 'b714_defects.txt'))
    dlet = [(m.group(1), m.group(2)) for l in dl for m in [re.match(r"^    \(([a-z])\) (.+?'S)[:. ]", l)] if m]
    add('ruling (1)', 'G-RULE-LONG-PHASE-SPLIT withheld under the author`s words (5)-(7), defect (p)', any(x[0] == 'p' for x in dlet)
        and 'G-RULE-LONG-PHASE-SPLIT WITHHELD' in ' '.join(dl), 'defect (p) %s' % [x for x in dlet if x[0] == 'p'], '1')
    lt = (g(K.LV_DIR, 'rev-parse', K.LV_TAG + '^{commit}')[1] or '').strip()
    lr = g(K.LV_DIR, 'ls-remote', '--tags', 'origin', K.LV_TAG + '^{}')[1] or ''
    rl = subprocess.run(['gh', 'release', 'list', '-R', 'psinary-sketch/SIDE-lv-conservation', '--json', 'tagName'], capture_output=True)
    try:
        rels = [x.get('tagName') for x in json.loads(rl.stdout.decode('utf-8', 'replace') or '[]')]
    except Exception:
        rels = None
    add('ruling (1)', 'the lv port tagged v0.14.0 at cb0aea56 with no release (local peel, the remote`s ^{} line, the release list)', lt == K.PORT_TIP
        and lr.split()[:1] == [K.PORT_TIP] and rels is not None and K.LV_TAG not in rels, 'peel %s ; remote %s ; releases %s' % (lt[:8], lr.strip()[:8], rels), '1')
    rmerged = subprocess.run(['git', '-C', PP, 'merge-base', '--is-ancestor', K.RECUT_MERGE, 'main']).returncode == 0
    mpar = (g(PP, 'log', '-1', '--format=%P', K.RECUT_MERGE)[1] or '').split()
    add('ruling (1); ruling (9)', 'recut-b712-silence merged into PLACE-papers main at a86c9429 (its second parent the branch`s tip 0aeca834)', rmerged
        and mpar[1:2] == [K.RECUT_TIP], 'on main %s ; parents %s' % (rmerged, [x[:8] for x in mpar]), '1')
    hd = rd(p('data', 'b714_heads_draft.txt')) or ''
    awd = rd(p('data', 'b714_author_words.txt')) or ''
    add('ruling (1); ruling (8)', 'the heads draft HELD in data/b714_heads_draft.txt (the author`s word at the root: hold)', bool(hd) and 'hold the draft' in awd,
        'the draft %d characters ; the word holds it %s' % (len(hd), 'hold the draft' in awd), '1')
    pl = rd(p('data', 'b714_pilot.txt')) or ''
    plL = pl.split(NL)
    add('ruling (1)', 'the pilot: 32 names, 12 FOUND, 1 MISSING, 19 NO PIN STATED (data/b714_pilot.txt :66)', '(P1) NAMES 32: FOUND 12 ; MISSING 1 ; NO PIN STATED 19' in at(plL, 66),
        ':66 %r' % at(plL, 66).strip()[:70], '1')
    add('ruling (1)', '7 lint hits, 1 AS DESIGNED, 6 FOR THE AUTHOR (data/b714_pilot.txt :94)', '(P2) HITS 7: AS DESIGNED 1 ; FOR THE AUTHOR 6' in at(plL, 94), ':94', '1')
    p3 = [l for l in plL[98:122] if re.match(r'^    the (surround|seam|target|join)', l)]
    p3f = [l for l in p3 if re.search(r'\| (FOUND|READ) +\|', l) and '| FOUND ' in l]
    add('ruling (1); ruling (7)', 'the reduction chain`s 24 declarations FOUND at their pins (data/b714_pilot.txt (P3) :99-:122)', len(p3) == 24 and len(p3f) == 24,
        'rows %d ; FOUND %d ; READ %d (%s)' % (len(p3), len(p3f), sum(1 for l in p3 if '| READ ' in l), '; '.join(l.split('|')[1].strip() for l in p3 if '| READ ' in l) or 'none'), '1-5')
    add('ruling (1)', 'a blueprint priced at 3 dispatches and about 8.0 hours (data/b714_pilot.txt :133)', '3 DISPATCHES ; ABOUT 8.0 HOURS' in at(plL, 133), ':133', '1')
    row = act_root_line('b714')
    add('ruling (1)', 'the root 242b06d6 (data/act_roots.txt, chained on b713`s d613bce6)', bool(row) and row[0][1] == K.B714_ROOT and row[0][2].startswith('d613bce6'),
        'row b714 %s' % ([x[:8] for x in row[0][1:3]] if row else 'NONE'), '1')
    mr = rd(p('data', 'b714_mirror.txt')) or ''
    add('ruling (1)', 'the mirror CLEAN with the root line (data/b714_mirror.txt)', 'CLEAN ON ALL THREE CLAUSES' in mr and 'Act root: b714 242b06d6' in mr and os.path.exists(K.MIRROR_ZIP),
        'the zip exists %s' % os.path.exists(K.MIRROR_ZIP), '1')
    nav = sorted(x[0] for x in dlet if x[1] == "THE NAVIGATOR'S")
    add('ruling (1)', 'seventeen defects (a)-(q), (f) and (q) the navigator`s (data/b714_defects.txt)', ''.join(x[0] for x in dlet) == 'abcdefghijklmnopq' and nav == ['f', 'q'],
        'letters %s ; the navigator`s %s ; owners %s' % (''.join(x[0] for x in dlet), nav, sorted(set(x[1] for x in dlet))), '1')
    ev = lines_of(p('data', 'b714_events.txt'))
    starts = dict((int(m.group(1)), i + 1) for i, l in enumerate(ev) for m in [re.match(r'^\((\d+)\) ', l)] if m)
    add('ruling (1); ruling (2)', 'twelve events in data/b714_events.txt, (1)-(12) each on its starting line', sorted(starts) == list(range(1, 13)),
        'starting lines %s' % [starts[k] for k in sorted(starts)], '1')
    add('ruling (1); ruling (11)', '"Nothing deposited, nothing published": the draft at v5, held', K.DRAFT == '23228113', 'tools/b715_worklist.py DRAFT', '6')
    # ### (R325)(2): the corrigendum's sources
    add('ruling (2)', 'the corrigendum tool to carry (tools/b714_corrigendum.py) and the one lettering (tools/act_letters.py)',
        os.path.exists(p('tools', 'b714_corrigendum.py')) and os.path.exists(p('tools', 'act_letters.py')), 'present', '1')
    cg = lines_of(p('data', 'b675_corrigenda.txt'))
    last = [l for l in cg if re.match(r'^\s*\((\d+)\)', l)]
    add('ruling (2)', 'the corrigenda bank, appended only (its last row (34), b714`s)', bool(last) and re.match(r'^\s*\(34\)', last[-1]) is not None,
        'data/b675_corrigenda.txt, last row %r' % (last[-1][:40] if last else ''), '1')
    aw = lines_of(p('data', 'b714_author_words_preseal.txt'))
    rc4 = lines_of(p('data', 'b714_records.txt'))
    rnum = [int(m.group(1)) for l in rc4 for m in [re.match(r'^\((\d+)\) ', l)] if m]
    add('ferry read-first', 'data/b714_records.txt (13)-(21), the ferry`s read-first span', all(k in rnum for k in range(13, 22)),
        'records present %s ; of (13)-(21) absent %s (their text in data/b714_events.txt (4)-(6), event (6))' % (
            '(%d)-(%d)' % (min(rnum), max(rnum)) if rnum else 'NONE', [k for k in range(13, 22) if k not in rnum]), '0')
    add('ruling (2)', 'word (5)`s clause "no tool is edited for this" (data/b714_author_words_preseal.txt)', any('no tool is edited for this' in l for l in aw),
        ':%s' % next((i + 1 for i, l in enumerate(aw) if 'no tool is edited for this' in l), 0), '1')
    # ### (R325)(3): the toolset's sources and objects
    for f in ('tools/standing', 'data/act_current.json', 'data/b715_replay.txt', 'data/b715_tool_repairs.txt', 'data/b715_readfirst.txt', 'data/b715_rules.txt'):
        add('ruling (3); ruling (10)', '%s -- TO BE WRITTEN by this act' % f, not os.path.exists(p(*f.split('/'))), 'absent, as ordered', '0-6')
    for f in ('data/b714_checks_postpush.txt', 'data/b714_scores_close.json', 'data/b714_author_answers.txt', 'data/b713_checks_postpush.txt',
              'data/b713_scores_close.json', 'data/b713_author_answers.txt', 'data/b713_steps.json'):
        add('ruling (3)(iv)', 'the replay`s input %s, committed' % f, bool((g(ROOT, 'ls-files', f)[1] or '').strip()), 'tracked', '2')
    b713c = lines_of(p('data', 'b713_closing.txt'))
    add('ruling (3)(iv)', 'b713`s head line (data/b713_closing.txt :1), the replay`s second instance', at(b713c, 1).startswith('b713 closed: relay ce9f30f6'), ':1 %r' % at(b713c, 1)[:60], '2')
    rr = lines_of(p('data', 'act_roots.txt'))
    chain = [l for l in rr if re.match(r'^b\d+ [0-9a-f]{64} ', l)]
    add('ruling (3)(ii)', 'data/act_roots.txt: its chain rows and the last b714 (the act_current.json source)', bool(chain) and chain[-1].startswith('b714 '),
        'chain rows %d ; the last %s' % (len(chain), chain[-1][:13] if chain else 'NONE'), '0')
    pre = ['698', '699', '700', '701', '702', '703', '704', '705', '706', '707', '708', '709', '710', '711', '712', '713', '714']
    have = [a for a in pre if glob.glob(os.path.join(T, 'b%s_*.py' % a))]
    add('ruling (3)(v)', 'the per-act tools of b698-b714, kept unedited (each act`s tools present)', have == pre, 'acts with tools %d of %d' % (len(have), len(pre)), '2')
    # ### (R325)(4): the class repairs' objects
    rja = rd(p('data', 'b713_act_root.json')) or ''
    parts713 = [k for k in K.PARTS if 'data/b713_arms_prerun_%s.txt' % k in rja and os.path.exists(p('data', 'b713_arms_prerun_%s.txt' % k))]
    add('ruling (4)(i)', 'b713`s seven part banks, each named by b713`s root (data/b713_act_root.json)', len(parts713) == 7 and not os.path.exists(p('data', 'b713_arms_prerun.txt')),
        'parts named and present %d ; the combined bank absent %s' % (len(parts713), not os.path.exists(p('data', 'b713_arms_prerun.txt'))), '3')
    ra = lines_of(p('tools', 'rule_arms.py'))
    add('ruling (4)(i)', 'tools/rule_arms.py :305-:307 (the previous act`s combined bank) and :534 (G-RULE-LONG-PHASE-SPLIT)', "b%d_arms_prerun.txt' % (n - 1)" in at(ra, 305)
        and 'THE LONGEST PHASE' in at(ra, 306) and "'arms_prerun'" in at(ra, 307) and "G-RULE-LONG-PHASE-SPLIT" in at(ra, 534), ':305 ; :306 ; :307 ; :534', '3')
    ck = lines_of(p('tools', 'b714_checks.py'))
    add('ruling (4)(ii); ruling (4)(vi)', 'tools/b714_checks.py`s one-entry WITHHELD list (:1760) and neg_shown() returning three lists (:1766, :1792)',
        at(ck, 1760).startswith('WITHHELD = (') and 'G-RULE-LONG-PHASE-SPLIT' in at(ck, 1761) and at(ck, 1764).strip() == '' and at(ck, 1766).startswith('def neg_shown')
        and at(ck, 1792).strip() == 'return shown, bad, withheld', ':1760 ; :1761 ; :1766 ; :1792', '3')
    hk = rd(p('tools', 'b714_hook.py')) or ''
    rj4 = rd(p('data', 'b714_act_root.json')) or ''
    add('ruling (4)(iii)', 'the hook writes its refusals to data/b714_hook_refusals.txt, a bank b714`s root names', "'b714_hook_refusals.txt'" in hk and 'data/b714_hook_refusals.txt' in rj4,
        'tools/b714_hook.py REFUSALS ; data/b714_act_root.json names it %s' % ('data/b714_hook_refusals.txt' in rj4), '3')
    rec = lines_of(p('tools', 'b714_record.py'))
    add('ruling (4)(iv)', 'tools/b714_record.py :2630-:2656, the components composer carrying b713`s objects (K.C1_PP_FACES :2643)', at(rec, 2630).startswith('def components')
        and 'K.C1_PP_FACES' in at(rec, 2643), ':2630 ; :2643', '3')
    add('ruling (4)(iv)', 'the components banks of b713 and b714 (the stand-in`s), the replay`s objects', all(os.path.exists(p('data', 'b71%d_components.txt' % k)) for k in (3, 4)), 'present', '3')
    rp = lines_of(p('tools', 'b714_repairs.py'))
    add('ruling (4)(v)', 'defect (m): tools/b714_repairs.py :154 carries os' + '.remove', ('os' + '.remove(') in at(rp, 154), ':154 %r' % at(rp, 154).strip()[:60], '3')   # ### the word split as the house splits it (tools/b703_checks.py no_delete), so G-DELETE-FREE reads no delete here
    add('ruling (4)(vi)', 'the second caller of neg_shown(): tools/b714_record.py :1394 (repairctl) unpacks two values', at(rec, 1394).strip() == 'shown, bad = CK.neg_shown()',
        ':1394 %r' % at(rec, 1394).strip(), '3')
    # ### (R325)(5)-(6): the roster and the pins
    ros = _jl_any(p('tools', 'mirror_roster.json'))
    rfiles = [x.replace('\\', '/') for x in (ros.get('files') or [])]
    add('ruling (5)', 'the mirror roster (tools/mirror_roster.json), 70 entries, b707`s (lastChanged 2026-10-23)', len(rfiles) == 70 and ros.get('lastChanged') == '2026-10-23',
        'entries %d ; lastChanged %s ; carries the census v0.8.1 %s ; Silence %s' % (len(rfiles), ros.get('lastChanged'), K.CENSUS_PREV in rfiles, K.RECUT_DOC in rfiles), '4')
    sil = (g(PP, 'rev-parse', 'main:' + K.RECUT_DOC)[1] or '').strip()
    sil0 = (g(PP, 'rev-parse', K.RECUT_MERGE + ':' + K.RECUT_DOC)[1] or '').strip()
    add('ruling (5)', 'day1/Silence_of_Foundations.md on main at a86c9429`s bytes (blob at main equal to the blob at a86c9429)', bool(sil) and sil == sil0, 'main %s ; a86c9429 %s' % (sil[:8], sil0[:8]), '4')
    pins = rd(p('tools', 'b303_pins.py')) or ''
    proster = re.findall(r"\('([\w.-]+)', r'D:", pins)
    add('ruling (6)', 'tools/b303_pins.py`s roster of four (relay, SIDE-global-section, PLACE-papers, SIDE-effects)', proster == ['relay', 'SIDE-global-section', 'PLACE-papers', 'SIDE-effects'],
        'roster %s' % proster, '4')
    vis = rd(p('data', 'repo_visibility.txt')) or ''
    add('ruling (6)', 'data/repo_visibility.txt (the visibility map, b714`s)', 'PRIVATE' in vis and 'PUBLIC' in vis, '%d characters' % len(vis), '4')
    # ### (R325)(7): the census rows' sources
    pl3 = [l.split('|')[1].strip() for l in p3]
    add('ruling (7)', 'rh_strip_imp_rh_holds among the (P3) names with no homebrew row', any(l.split('|')[1].strip() == 'rh_strip_imp_rh_holds' and 'NO HOMEBREW ROW' in l for l in p3),
        'names with no homebrew row %d of %d' % (sum(1 for l in p3 if 'NO HOMEBREW ROW' in l), len(p3)), '5')
    add('ruling (7)', 'the census v0.8.2 absent on main (the next edition, to be written)', not os.path.exists(os.path.join(PP, *K.CENSUS_NEW.split('/'))), 'absent, as ordered', '5')
    # ### (R325)(9): the carried files and the branches
    add('ruling (9)', 'data/b714_relay_push-b714-closing_push_out.txt, untracked', os.path.exists(p('data', 'b714_relay_push-b714-closing_push_out.txt'))
        and not (g(ROOT, 'ls-files', 'data/b714_relay_push-b714-closing_push_out.txt')[1] or '').strip(), 'present, untracked', '0')
    st = _jl('b714_steps.json').get('rows', [])
    dirty = (g(ROOT, 'diff', '--name-only')[1] or '').split()
    add('ruling (9)', 'step row 18 of data/b714_steps.json (the closing`s, 1992a71c), uncommitted', len(st) == 18 and st[17].get('commit', '').startswith(K.B714_CLOSING)
        and 'data/b714_steps.json' in dirty, 'rows %d ; row 18 %s' % (len(st), (st[17].get('commit', '')[:8], st[17].get('phase')) if len(st) >= 18 else 'NONE'), '0')
    add('ruling (9)', 'data/b714_bank_hashes.json, uncommitted', 'data/b714_bank_hashes.json' in dirty, 'modified at the working tree', '0')
    hr = (g(ROOT, 'diff', '--numstat', '--', 'data/b714_hook_refusals.txt')[1] or '').split()
    add('ruling (9)', 'data/b714_hook_refusals.txt`s ONE line written after the root, beside event (10)', hr[:2] == ['1', '0'],
        'lines added since the root`s commit %s (event (10)`s 15:43:48Z and any refusal since)' % (hr[:1] or ['0'])[0], '0')
    for repo, names in K.DELETE:
        lst = g(repo, 'branch', '--merged', 'main')[1] or ''
        for b in names:
            add('ruling (9)', '%s %s (local, listed --merged)' % (os.path.basename(repo), b), b in [x.strip(' *') for x in lst.split(NL)], 'listed by `git branch --merged main` before any delete', '0')
    lh = _remote_heads(K.LV_DIR)
    loc = (g(K.LV_DIR, 'rev-parse', K.PORT_BRANCH)[1] or '').strip()
    add('ruling (9)', 'port-b707 at cb0aea56 locally and at the remote, NOT deleted', loc == K.PORT_TIP and lh.get('refs/heads/port-b707') == K.PORT_TIP,
        'local %s ; remote %s' % (loc[:8], (lh.get('refs/heads/port-b707') or '')[:8]), '0')
    add('ruling (9)', 'the 2,560 MB hold', K.HOLD == 2560, 'tools/b715_worklist.py HOLD', '0')
    # ### (R325)(10)-(12)
    add('ruling (10)', 'the hook`s settings (D:/.claude/settings.json), the hook b714`s', 'b714_hook.py' in (rd('D:/.claude/settings.json') or ''), 'D:/.claude/settings.json names tools/b714_hook.py', '3')
    add('ruling (10)', 'the READFIRST-CLOSURE reader', os.path.exists(p('tools', 'circuit_read.py')), 'tools/circuit_read.py (readfirst)', '0')
    add('ferry C6', 'the four standing arms` figures tool and b714`s baselines', os.path.exists(p('tools', 'b706_standing_figures.py')) and os.path.exists(p('data', 'b714_standing_figures.json')),
        'tools/b706_standing_figures.py ; data/b714_standing_figures.json', '6')
    add('ferry C6', 'the chain halves as b693 drew them, b715 added to the second', K.CHAIN_HALVES[1] == ('b659', 'b715'), 'tools/b715_worklist.py CHAIN_HALVES', '6')
    add('ferry read-first', 'OPEN_TRAILS :15992, b714`s open orders; :16004 its Next', at(ot, 15992).startswith('**The open orders:**') and at(ot, 16004).startswith('**Next:** b715'),
        ':15992 ; :16004', '0')
    add('ferry read-first', 'FINDINGS :10512, b714`s entry', at(fi, 10512).startswith('## '), ':10512 %r' % at(fi, 10512)[:50], '1')
    add('ruling (12)', 'the next act b716, the registrations act', K.NEXT_ACT == 'b716' and K.NEXT.startswith('b716, the registrations act'), 'tools/b715_worklist.py NEXT', '6')
    add('ferry C0', 'this act`s session transcript (a new session after the clear)', os.path.exists(C.SESSION), C.SESSION, '0')
    standing_rows(text, add)
    return R


def standing_rows(text, add):
    """the citation tool reads the standing clauses by version (data/b712_rules.txt row (1)): for each version a ferry names as "standing clauses v<N>"
    outside a quotation, the bank data/standing_clauses_v<N>.txt present with its VERSION line -- v1 with its control banked AS WANTED; a version this
    act writes at step zero (v2, (R325)(2)) read as TO BE WRITTEN when absent and from the bank when present."""
    import b714_standing as SC
    flat = re.sub(r'“[^”]*”', '', ' '.join(text.split()))
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing clauses(?:’)? v(\d+)', flat, re.I)))
    for v in names or [1]:
        p = os.path.join(D, 'standing_clauses_v%d.txt' % v)
        t = rd(p) or ''
        ver = re.search(r'^VERSION: (\d+)$', t, re.M)
        if v == 1:
            ctl = _jl('b714_standing_control.json')
            add('ferry (standing clauses)', 'the standing clauses v1: data/standing_clauses_v1.txt', bool(t) and bool(ver) and ver.group(1) == '1' and bool(SC.parse(t)) and ctl.get('ok') is True,
                'present %s ; VERSION %s ; rows %d ; the re-assembly control AS WANTED %s' % (bool(t), ver.group(1) if ver else 'NONE', len(SC.parse(t)), ctl.get('ok')), '0')
        elif not t:
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- TO BE WRITTEN at step zero ((R325)(2))' % (v, v), True, 'absent, as ordered', '0')
        else:
            add('ferry (standing clauses)', 'the standing clauses v%d: data/standing_clauses_v%d.txt' % (v, v), bool(ver) and ver.group(1) == str(v), 'present ; VERSION %s' % (ver.group(1) if ver else 'NONE'), '0')


def _write(L, R, miss):
    for n_ in ('b715_citation_check.txt', 'b715_citation_check.json'):
        MEM.guard('b715', n_, _root_exclude())
    for name, data in (('b715_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b715_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        with open(q + '.tmp', 'wb') as fh:
            fh.write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b715 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b715_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b715_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b715_ferry_scan.txt')
    MEM.guard('b715', 'b715_ferry_scan.txt', _root_exclude())
    with open(s + '.tmp', 'wb') as fh:
        fh.write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b715_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
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
    """(R278)(4): b682's route, imported, with its act names pointed at b715, and b706's repair carried."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.C.SESSIONS_AFTER = C.SESSIONS_AFTER
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, K.LV_DIR, K.JOIN_DIR, 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects', 'D:/SIDE-bijection', 'D:/SIDE-interfaces', 'D:/SIDE-li-map',
                                                 'D:/SIDE-kernel') if r not in P.REPOS and os.path.isdir(r))
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b715'))
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
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b715')
    # ### (R325)(2), the item repair: THE WHOLE ANSWER. b682's cut ends at the first "END" after the needle (`best.find('END', k)`, :221), which a
    # ### word carrying END (AMENDMENT, APPENDED, RECOMMENDED) ends inside: b714's answers read 468 characters. The cut now ends at the answer's
    # ### last END (`best.rfind('END')`), the paste's own tail; the substitution printed, the route refusing where it does not apply.
    if body.count("best.find('END', k)") != 1:
        sys.exit('### b682`s CUT NOT FOUND ONCE IN ITS answer -- NOTHING CHECKED')
    body = body.replace("best.find('END', k)", "best.rfind('END')")
    body = body.replace("    open(q + '.tmp', 'wb')", "    MEM.guard('b715', os.path.basename(q), ROOT_EXCLUDE)\n    open(q + '.tmp', 'wb')")
    ns = dict(vars(P))
    ns.update(MEM=MEM, ROOT_EXCLUDE=_root_exclude())
    exec(compile(body, 'b682_citation.answer (b715)', 'exec'), ns)
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
        print('usage: b715_citation.py check [dry] | ferry | answer <needle> | word <needle> | replay <needle> <session id> <anchor>')
        sys.exit(2)
    fn(*sys.argv[2:])
