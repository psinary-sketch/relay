# -*- coding: utf-8 -*-
"""b717_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b717's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (bde68a30, a new session after the clear; the anchor (R327)'s line); the answer route is b682's, imported from
### tools/b682_citation.py with its act names pointed at b717, b706's repair carried (a bare eight-hex token a bank names as a sha256 or a
### kernel's lakefile pins as a rev is not read as a commit); the `word` route is b694's. Routes: `check [dry]` -> data/b717_citation_check.txt
### (.json) ; `ferry` -> data/b717_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the check on one answer.
### Carried by diff from b716_citation.py (data/b717_carry_citation.txt), b716's cite rows pruned (data/b717_prune_citation.txt) and this
### ruling's written by the Edit tool; this tool writes only the banks named above. Its (R327)(1) row reads lv's release list by `gh` (the
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
import b717_worklist as K   # noqa: E402
import act_membrane as MEM  # noqa: E402  ### (R327)(2)(ii): the membrane before every bank write of this tool


def _root_exclude():
    import b717_record as REC   # ### the record tool's exclusion pattern, the one the root route reads (imported at the call, nothing written)
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
    # ### b717: the cite rows of (R327) and its ferry, written by the Edit tool after b716's rows were pruned (data/b717_prune_citation.txt)
    for f in K.PATHS:
        add('ruling PATHS', f, os.path.isdir(f), 'present' if os.path.isdir(f) else 'ABSENT', '0')
    for f in ('data/b716_closing.txt', 'data/b716_events.txt', 'data/b716_defects.txt', 'data/b716_registrations.txt', 'data/b716_genus_control.txt',
              'data/b716_price.txt', 'data/b716_federation_pin_price.txt', 'data/b716_epstein_count_price.txt', 'data/b716_correspondence_pins.txt',
              'data/b716_author_answers.txt', 'data/b714_heads_draft.txt', 'data/b714_pilot.txt', 'data/b714_law.txt', 'data/b714_residual.txt',
              'data/b713_list.json', 'data/b709_pairs.txt', 'data/standing_clauses_v5.txt', 'data/b716_toolset_coverage.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    add('ferry read-first', '"the author`s-words bank": data/b716_author_words.txt, the closing`s "NONE RECEIVED" (data/b716_closing.txt :83)',
        not os.path.exists(p('data', 'b716_author_words.txt')) and 'NONE RECEIVED' in at(lines_of(p('data', 'b716_closing.txt')), 83),
        'absent at the working tree ; :83 names it NONE RECEIVED -- the words of b716 are the answers bank`s (:10, :13)', '0')
    add('ferry read-first', 'the census on main by its rows: PLACE-papers phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md',
        os.path.exists(os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS_v0_8_2.md')), 'exists at the working tree', '0')
    law = lines_of(p('data', 'b714_law.txt'))
    add('ferry read-first', '"the law-identity bank of b714 (7)": data/b714_law.txt, (R324)(7)`s bank (its :1), its reading at :66',
        '(R324)(7)' in at(law, 1) and 'TWO FORMS' in at(law, 66), ':1 %r ; :66 %r' % (at(law, 1)[:40], at(law, 66).strip()[:40]), '0')
    hd = lines_of(p('data', 'b714_heads_draft.txt'))
    add('ferry read-first', 'the heads draft`s sections II and III (data/b714_heads_draft.txt :33, :66)', at(hd, 33).startswith('## II.') and at(hd, 66).startswith('## III.'),
        ':33 %r ; :66 %r' % (at(hd, 33)[:30], at(hd, 66)[:30]), '5')
    pl = lines_of(p('data', 'b714_pilot.txt'))
    add('ferry read-first', 'data/b714_pilot.txt (P2): the six lint hits FOR THE AUTHOR (:94)', '(P2) HITS 7: AS DESIGNED 1 ; FOR THE AUTHOR 6' in at(pl, 94), ':94', '5')
    # ### (R327)(1): b716 at its weight
    cl = lines_of(p('data', 'b716_closing.txt'))
    q = _quote(text, 'b716 closed: relay', '”; the closing’s commit')
    add('ruling (1)', 'data/b716_closing.txt :1, the head line, against (R327)(1)`s quote', bool(q) and q == cl[0],
        'quote %d characters, the line %d ; equal byte for byte %s' % (len(q), len(cl[0]), q == cl[0]), '1')
    clo_s = (g(ROOT, 'log', '-1', '--format=%H %s', '983dcbe2')[1] or '').strip()
    rec_s = (g(ROOT, 'log', '-1', '--format=%H %s', '78866b19')[1] or '').strip()
    rmain = (g(ROOT, 'ls-remote', 'origin', 'refs/heads/main')[1] or '').split()
    add('ruling (1)', 'the closing`s commit 983dcbe2 ("b716: the closing"), the record 78866b19 ("b716 record"), the remote main at the closing',
        clo_s[41:].startswith('b716: the closing') and rec_s[41:].startswith('b716 record') and rmain[:1] == [clo_s[:40]],
        '%s ; %s ; remote main %s' % (clo_s[:58], rec_s[:52], (rmain or ['NONE'])[0][:8]), '1')
    dc = (g(ROOT, 'show', '--name-only', '--format=%s', K.REG_COMMIT)[1] or '').split(NL)
    first_after = (g(ROOT, 'rev-list', '--reverse', 'cf51ee95..983dcbe2')[1] or '').split()
    add('ruling (1); ruling (4)', 'data/b716_registrations.txt committed alone at the act`s opening commit dc5e808f, its count control beside it',
        bool(first_after) and first_after[0] == K.REG_COMMIT and 'data/b716_registrations.txt' in dc,
        'b716`s first commit after cf51ee95 %s ; its files %s' % ((first_after or ['NONE'])[0][:8], [x for x in dc[1:] if x.strip()]), '1')
    gc = lines_of(p('data', 'b716_genus_control.txt'))
    add('ruling (1)', 'its count control at 0 misses (data/b716_genus_control.txt :46, :49)', 'THROUGH n = 400: 0' in at(gc, 46) and 'MISSES 0' in at(gc, 49) and 'NOTHING OF THE ZEROS COMPUTED' in at(gc, 49),
        ':46 ; :49', '1')
    sdir = p('tools', 'standing')
    cov = lines_of(p('data', 'b716_toolset_coverage.txt'))
    add('ruling (1)', 'the toolset at v1.1.0, 2 of 25 steps STANDING ([8], [18]) (tools/standing/VERSION ; data/b716_toolset_coverage.txt :48)',
        (rd(os.path.join(sdir, 'VERSION')) or '').strip() == 'v1.1.0' and 'STEPS 25 ; STANDING 2 ([8], [18])' in at(cov, 48),
        'VERSION %r ; :48' % (rd(os.path.join(sdir, 'VERSION')) or '').strip(), '1')
    rp = lines_of(p('data', 'b716_replay.txt'))
    add('ruling (1)', 'the replay over b715, b714 and b713 at 17 of 18 EQUAL, the one DIFFERS b713`s old tool, F-2 (data/b716_replay.txt :107, :117)',
        'OBJECTS 18 ; EQUAL 17 ; DIFFERS 1 [\'b713 (6)\']' in at(rp, 117) and 'F-2' in at(rp, 107), ':107 ; :117', '1')
    mi = lines_of(p('data', 'b716_mirror.txt'))
    add('ruling (1)', 'the mirror mirror-refresh-2026-10-27-b716.zip CLEAN on all three clauses, its manifest control NOT AS WANTED (data/b716_mirror.txt :2, :13, :14)',
        'mirror-refresh-2026-10-27-b716.zip' in at(mi, 2) and 'NOT AS WANTED' in at(mi, 13) and 'CLEAN ON ALL THREE CLAUSES' in at(mi, 14), ':2 ; :13 ; :14', '1')
    ev = lines_of(p('data', 'b716_events.txt'))
    starts = dict((int(m.group(1)), i + 1) for i, l in enumerate(ev) for m in [re.match(r'^    \((\d+)\) ', l)] if m)
    add('ruling (1)', '"against a carried reference, event (17)": data/b716_events.txt (17) names b715`s merge a86c9429 as the control`s reference',
        17 in starts and 18 in starts and any('a86c9429' in at(ev, i) for i in range(starts[17], starts[18])), '(17) :%s-:%s' % (starts.get(17), (starts.get(18) or 1) - 1), '1')
    sil = (g(PP, 'show', 'main:day1/Silence_of_Foundations.md')[1] or '').split(NL)
    add('ruling (1)', 'Silence :212 corrected to SIDE-meta (PLACE-papers main day1/Silence_of_Foundations.md :212)', 'SIDE-meta' in at(sil, 212),
        ':212 %r' % at(sil, 212)[:80], '1')
    cp = lines_of(p('data', 'b716_correspondence_pins.txt'))
    carried = [l for l in cp[23:34] if l.startswith('  ') and ' census ' in l]
    add('ruling (1); ruling (6)', '8 of 19 unpinned names pinned, 11 carried (data/b716_correspondence_pins.txt :23-:34, :36)',
        at(cp, 23).startswith('## LISTED AND CARRIED, 11') and len(carried) == 11 and 'NAMES 19 ; PINNED FROM THE CENSUS 8' in at(cp, 36) and 'LISTED AND CARRIED 11' in at(cp, 36),
        ':23 %r ; rows :24-:34 %d ; :36' % (at(cp, 23)[:30], len(carried)), '1')
    cen = (g(PP, 'log', '--format=%h %s', '-1', '--', 'phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md')[1] or '').strip()
    add('ruling (1)', 'the census v0.8.2`s 24 chain rows written at b715 (PLACE-papers 332710b, the census`s last commit)', cen.startswith('332710b') and '24 rows' in cen,
        '%r' % cen[:70], '1')
    for f, n, needle in (('b716_price.txt', 80, 'NOTHING OF -39 COMPUTED'), ('b716_federation_pin_price.txt', 166, 'NOTHING BUILT'), ('b716_epstein_count_price.txt', 152, 'NOTHING BUILT')):
        L = lines_of(p('data', f))
        add('ruling (1)', 'the price data/%s :%d, its foot' % (f, n), needle in at(L, n) and at(L, n).startswith('### ###'), ':%d %r' % (n, at(L, n)[:50]), '1')
    ans = lines_of(p('data', 'b716_author_answers.txt'))
    add('ruling (1); ruling (5)', 'the author`s two root words banked verbatim (data/b716_author_answers.txt :4, :7 the two prompts ; :10 the result ; :13 the BEGIN-END word)',
        at(ans, 4).startswith('### PROMPT 1') and at(ans, 7).startswith('### PROMPT 2') and at(ans, 10).startswith('RESULT') and at(ans, 12).startswith('### THE AUTHOR`S WORD'),
        ':4 ; :7 ; :10 ; :12-:13', '1')
    row = act_root_line('b716')
    add('ruling (1)', 'the root 4df4ddac (data/act_roots.txt, b716`s row)', bool(row) and row[-1][1].startswith('4df4ddac'), 'row b716 %s' % (row[-1][1][:8] if row else 'NONE'), '1')
    add('ruling (1); ruling (3)', 'nineteen events in data/b716_events.txt, (1)-(19) each on its starting line', sorted(starts) == list(range(1, 20)),
        'starting lines %s' % [starts[k] for k in sorted(starts)], '1')
    dl = lines_of(p('data', 'b716_defects.txt'))
    dlet = [(m.group(1), m.group(2)) for l in dl for m in [re.match(r"^    \(([a-z])\) (THE [A-Z]+'S)", l)] if m]
    add('ruling (1); ruling (3)', 'eighteen defects in data/b716_defects.txt, (a)-(r)', ''.join(x[0] for x in dlet) == 'abcdefghijklmnopqr',
        'letters %s ; the navigator`s %s' % (''.join(x[0] for x in dlet), [x[0] for x in dlet if x[1] == "THE NAVIGATOR'S"]), '1')
    add('ruling (1); ruling (10)', '"Nothing deposited, nothing published": the draft at v5, held', K.DRAFT == '23228113', 'tools/b717_worklist.py DRAFT', '1')
    # ### (R327)(2)-(3): claim and close; the corrigendum
    for f in ('data/standing_clauses_v6.txt', 'data/arm_tags.json', 'data/b717_corrigendum.txt', 'data/b717_readfirst.txt'):
        add('ruling (2); ruling (3); ruling (9)', '%s -- TO BE WRITTEN by this act' % f, not os.path.exists(p(*f.split('/'))), 'absent, as ordered', '0-1')
    add('ruling (3)', 'the corrigendum tool to carry (tools/b716_corrigendum.py) and the one lettering (tools/act_letters.py)',
        os.path.exists(p('tools', 'b716_corrigendum.py')) and os.path.exists(p('tools', 'act_letters.py')), 'present', '1')
    cg = lines_of(p('data', 'b675_corrigenda.txt'))
    last = [l for l in cg if re.match(r'^\s*\((\d+)\)', l)]
    add('ruling (3)', 'the corrigenda bank, appended only (its last row (36), b716`s)', bool(last) and re.match(r'^\s*\(36\)', last[-1]) is not None,
        'data/b675_corrigenda.txt, last row %r' % (last[-1][:40] if last else ''), '1')
    # ### (R327)(4): the test at -39
    blob = (g(ROOT, 'show', '%s:data/b716_registrations.txt' % K.REG_COMMIT)[1] or '')
    add('ruling (4)', 'data/b716_registrations.txt read unchanged from dc5e808f (the working tree`s bytes against the commit`s blob)',
        bool(blob) and blob.replace(chr(13), '') == (rd(p('data', 'b716_registrations.txt')) or ''), 'blob %d characters ; equal %s' % (len(blob), blob.replace(chr(13), '') == (rd(p('data', 'b716_registrations.txt')) or '')), '2-4')
    rg = lines_of(p('data', 'b716_registrations.txt'))
    add('ruling (4)(ii)', '"the form b714 (7) read": registration (iii) carries the first-order form with C per pair (data/b716_registrations.txt :67-:69 ; b714_law :70)',
        'THE FIRST-ORDER' in at(rg, 67) and 'FORM WITH C PER PAIR' in at(rg, 68), ':67-:68', '3')
    rs = lines_of(p('data', 'b714_residual.txt'))
    add('ruling (4)(iii)', '"the additive offset onset minus prediction ... as b714 (8) printed it": data/b714_residual.txt (registration (iii) :78-:79)',
        bool(rs) and 'b714_residual' in at(rg, 79), ':79 %r' % at(rg, 79)[:60], '3')
    add('ruling (4)(iv)', 'the cut 32532 (data/b716_price.txt :69) and registration (ii) on its two clauses (b(n) = -2 ; a prime outside the principal class, :51-:53)',
        'n <= 32532' in at(lines_of(p('data', 'b716_price.txt')), 69) and 'b(n) = -2' in at(rg, 51) and 'FALSIFIER' in at(rg, 53), ':69 ; :51 ; :53', '4')
    add('ruling (4)(i)', '"base and tiers [0, 100] and [100, 200]": the price`s tiers (data/b716_price.txt :40-:53, :61)',
        'the first tier' in at(lines_of(p('data', 'b716_price.txt')), 40) and 'the second tier band [ 190.0,  200.0]' in at(lines_of(p('data', 'b716_price.txt')), 53), ':40 ; :53', '2')
    for t_ in ('b713_list.py', 'b713_predict.py', 'b713_onsets.py', 'b713_coeffs.py'):
        add('ruling (4); price (1)', 'tools/%s, the -15 form the -39 tool is carried from' % t_, os.path.exists(p('tools', t_)), 'present', '2-4')
    add('price (1)', 'the price`s named tools tools/b713_epstein_certify.py and tools/b713_pairs.py (data/b716_price.txt :8)',
        os.path.exists(p('tools', 'b713_epstein_certify.py')) and os.path.exists(p('tools', 'b713_pairs.py')),
        'present %s, %s -- b713`s list route is tools/b713_list.py' % (os.path.exists(p('tools', 'b713_epstein_certify.py')), os.path.exists(p('tools', 'b713_pairs.py'))), '2')
    for f in ('tools/b717_list.py', 'tools/b717_predict.py', 'tools/b717_onsets.py', 'tools/b717_coeffs.py', 'data/b717_predictions.txt',
              'data/b717_list.txt', 'data/b717_onsets.txt', 'data/b717_coeffs.txt'):
        add('ruling (4)', '%s -- TO BE WRITTEN by this act' % f, not os.path.exists(p(*f.split('/'))), 'absent, as ordered', '2-4')
    wsc = os.path.join(PP, 'day1', 'Which_Structure_Confines.md')
    add('ruling (11)', 'Which_Structure_Confines (PLACE-papers day1/Which_Structure_Confines.md)', os.path.exists(wsc), 'present', '6')
    add('ruling (11)', 'the gates G1, G4 and G5 of the paper path: no relay or PLACE-papers bank the seat reads names them by these labels',
        False, 'the navigator`s labels, not found in a bank the act reads -- entered by the fact clause', '6')
    # ### (R327)(5): the author's words
    add('ruling (5)(i)', 'the banked word on (R326)(5)(i) names section II`s paragraph (data/b716_author_answers.txt :10)',
        'section II’s paragraph replaces :15 with its brackets removed' in at(ans, 10), ':10', '5')
    add('ruling (5)(i)', 'Silence_of_Foundations :15 on main, a paragraph', len(at(sil, 15).strip()) > 200, ':15 %d characters, %r' % (len(at(sil, 15)), at(sil, 15)[:50]), '5')
    add('ruling (5)(i)', 'day1/Silence_of_Foundations_CORRESPONDENCE.md -- TO BE WRITTEN by this act', not os.path.exists(os.path.join(PP, 'day1', 'Silence_of_Foundations_CORRESPONDENCE.md')),
        'absent, as ordered', '5')
    add('ruling (5)(ii)', 'the banked word on (R326)(5)(ii): (1), (2), (5) kept AS DESIGNED ; (3), (4), (6) reworded (data/b716_author_answers.txt :13)',
        'marked AS DESIGNED' in at(ans, 13) and '(3) Exhaustive_Enumeration :92' in at(ans, 13) and '(4) ONE_PAGE_PROOF :1' in at(ans, 13) and '(6) Third_Identity_Element :78' in at(ans, 13),
        ':13', '5')
    for f, n, needle in (('day1/Exhaustive_Enumeration.md', 92, 'but gaps were discovered and repaired over the following two decades'),
                         ('day1/ONE_PAGE_PROOF.md', 1, 'Proof of the Riemann Hypothesis via SIDE Exclusion'),
                         ('day1/Third_Identity_Element.md', 78, 'the gap from 4 to 8 breaks the consecutive chain')):
        L = (g(PP, 'show', 'main:' + f)[1] or '').split(NL)
        add('ruling (5)(ii)', 'main %s :%d carries the words the author`s word replaces' % (f, n), needle in at(L, n), ':%d %r' % (n, at(L, n)[:60]), '5')
    # ### (R327)(6): the eleven names
    add('ruling (6)', 'the census v0.8.3 on main -- TO BE WRITTEN by this act', not os.path.exists(os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS_v0_8_3.md')),
        'absent, as ordered', '5')
    # ### (R327)(7): scheduled, nothing built
    fp = lines_of(p('data', 'b716_federation_pin_price.txt'))
    add('ruling (7)(i)', 'the federation pin: 12 kernels below de5ce8a9, 12 dispatches, 3.1 runner hours, the halt "no ref carries the bump" (data/b716_federation_pin_price.txt :166)',
        'THE TARGET de5ce8a9a66a ; BELOW IT 12 ; DISPATCHES PRICED 12, 3.1 RUNNER HOURS' in at(fp, 166) and 'NO REF CARRIES THE BUMP' in at(fp, 166), ':166', '0')
    ep = lines_of(p('data', 'b716_epstein_count_price.txt'))
    add('ruling (7)(ii)', 'the Lean count: [160, 170] at Q0, 15 zeros, 90-180 dispatches, 115-230 hours, four constructions, DERIVES (data/b716_epstein_count_price.txt :152)',
        'THE BAND [160, 170] AT Q0, N 15, ALL ON THE LINE' in at(ep, 152) and '90-180 DISPATCHES, 115-230 FOREGROUND HOURS' in at(ep, 152) and 'THE GRADE DERIVES' in at(ep, 152), ':152', '5')
    ecl = [i + 1 for i, l in enumerate(ot) if '`W-ORD-EPSTEIN-COUNT-LEAN`' in l and l.startswith('*Appended')]
    add('ruling (7)(ii)', 'W-ORD-EPSTEIN-COUNT-LEAN in OPEN_TRAILS: the order`s existing rows (an *Appended* row naming it)', True,
        'rows %s -- (7)(ii) enters it at its price beside them' % ecl, '5')
    # ### (R327)(8): the carried files and the branches
    dirty = (g(ROOT, 'diff', '--name-only')[1] or '').split()
    add('ruling (8)', 'data/b716_relay_push-b716-closing_push_out.txt, untracked', os.path.exists(p('data', 'b716_relay_push-b716-closing_push_out.txt'))
        and not (g(ROOT, 'ls-files', 'data/b716_relay_push-b716-closing_push_out.txt')[1] or '').strip(), 'present, untracked', '0')
    st = _jl('b716_steps.json').get('rows', [])
    add('ruling (8)', 'step row 18 of data/b716_steps.json (the closing`s, 983dcbe2), uncommitted', len(st) == 18 and str(st[17].get('commit', '')).startswith('983dcbe2')
        and 'data/b716_steps.json' in dirty, 'rows %d ; row 18 %s' % (len(st), (str(st[17].get('commit', ''))[:8], st[17].get('phase')) if len(st) >= 18 else 'NONE'), '0')
    for repo, names in K.DELETE:
        lst = g(repo, 'branch', '--merged', 'main')[1] or ''
        for b in names:
            add('ruling (8)', '%s %s (local, listed --merged)' % (os.path.basename(repo), b), b in [x.strip(' *') for x in lst.split(NL)], 'listed by `git branch --merged main` before any delete', '0')
    lh = _remote_heads(K.LV_DIR)
    loc = (g(K.LV_DIR, 'rev-parse', K.PORT_BRANCH)[1] or '').strip()
    add('ruling (8)', 'port-b707 at cb0aea56 locally and at the remote, NOT deleted', loc == K.PORT_TIP and lh.get('refs/heads/port-b707') == K.PORT_TIP,
        'local %s ; remote %s' % (loc[:8], (lh.get('refs/heads/port-b707') or '')[:8]), '0')
    add('ruling (8)', 'the 2,560 MB hold', K.HOLD == 2560, 'tools/b717_worklist.py HOLD', '0')
    # ### the ferry
    add('ferry', 'the close runs each step as data/b716_toolset_coverage.txt marks it (STANDING [8], [18])', '[8]  the seal' in at(cov, 17) and '| STANDING |' in at(cov, 17) and '| STANDING |' in at(cov, 27),
        ':17 ; :27', '6')
    add('ferry', 'the hook in D:/.claude/settings.json is the standing one (tools/standing/hook.py)', 'standing/hook.py' in (rd('D:/.claude/settings.json') or ''), 'D:/.claude/settings.json', '0')
    add('ferry C0', 'the READFIRST-CLOSURE reader and rowgen (tools/circuit_read.py)', os.path.exists(p('tools', 'circuit_read.py')), 'present', '0')
    add('ferry C6', 'the chain halves as b693 drew them, b717 added to the second', K.CHAIN_HALVES[1] == ('b659', 'b717'), 'tools/b717_worklist.py CHAIN_HALVES', '6')
    add('ferry C0', 'this act`s session transcript (a new session after the clear)', os.path.exists(C.SESSION), C.SESSION, '0')
    standing_rows(text, add)
    return R


def standing_rows(text, add):
    """the citation tool reads the standing clauses by version (data/b712_rules.txt row (1)): for each version a ferry names as "standing clauses v<N>"
    outside a quotation, the bank data/standing_clauses_v<N>.txt present with its VERSION line -- v1 with its control banked AS WANTED; a version this
    act writes at step zero (v2, (R327)(2)) read as TO BE WRITTEN when absent and from the bank when present."""
    import b716_standing as SC
    flat = re.sub(r'“[^”]*”', '', ' '.join(text.split()))
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing clauses(?:’)? v(\d+)', flat, re.I)))
    for v in names or [1]:
        p = os.path.join(D, 'standing_clauses_v%d.txt' % v)
        t = rd(p) or ''
        ver = re.search(r'^VERSION: (\d+)$', t, re.M)
        if v == 1:
            ctl = _jl('b716_standing_control.json')
            add('ferry (standing clauses)', 'the standing clauses v1: data/standing_clauses_v1.txt', bool(t) and bool(ver) and ver.group(1) == '1' and bool(SC.parse(t)) and ctl.get('ok') is True,
                'present %s ; VERSION %s ; rows %d ; the re-assembly control AS WANTED %s' % (bool(t), ver.group(1) if ver else 'NONE', len(SC.parse(t)), ctl.get('ok')), '0')
        elif not t:
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- TO BE WRITTEN at step zero ((R327)(2))' % (v, v), True, 'absent, as ordered', '0')
        else:
            add('ferry (standing clauses)', 'the standing clauses v%d: data/standing_clauses_v%d.txt' % (v, v), bool(ver) and ver.group(1) == str(v), 'present ; VERSION %s' % (ver.group(1) if ver else 'NONE'), '0')


def _write(L, R, miss):
    for n_ in ('b717_citation_check.txt', 'b717_citation_check.json'):
        MEM.guard('b717', n_, _root_exclude())
    for name, data in (('b717_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b717_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        with open(q + '.tmp', 'wb') as fh:
            fh.write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b717 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b717_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b717_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b717_ferry_scan.txt')
    MEM.guard('b717', 'b717_ferry_scan.txt', _root_exclude())
    with open(s + '.tmp', 'wb') as fh:
        fh.write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b717_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
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
    """(R278)(4): b682's route, imported, with its act names pointed at b717, and b706's repair carried."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.C.SESSIONS_AFTER = C.SESSIONS_AFTER
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, K.LV_DIR, K.JOIN_DIR, 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects', 'D:/SIDE-bijection', 'D:/SIDE-interfaces', 'D:/SIDE-li-map',
                                                 'D:/SIDE-kernel') if r not in P.REPOS and os.path.isdir(r))
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b717'))
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
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b717')
    # ### (R327)(2), the item repair: THE WHOLE ANSWER. b682's cut ends at the first "END" after the needle (`best.find('END', k)`, :221), which a
    # ### word carrying END (AMENDMENT, APPENDED, RECOMMENDED) ends inside: b716's answers read 468 characters. The cut now ends at the answer's
    # ### last END (`best.rfind('END')`), the paste's own tail; the substitution printed, the route refusing where it does not apply.
    if body.count("best.find('END', k)") != 1:
        sys.exit('### b682`s CUT NOT FOUND ONCE IN ITS answer -- NOTHING CHECKED')
    body = body.replace("best.find('END', k)", "best.rfind('END')")
    body = body.replace("    open(q + '.tmp', 'wb')", "    MEM.guard('b717', os.path.basename(q), ROOT_EXCLUDE)\n    open(q + '.tmp', 'wb')")
    ns = dict(vars(P))
    ns.update(MEM=MEM, ROOT_EXCLUDE=_root_exclude())
    exec(compile(body, 'b682_citation.answer (b717)', 'exec'), ns)
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
        print('usage: b717_citation.py check [dry] | ferry | answer <needle> | word <needle> | replay <needle> <session id> <anchor>')
        sys.exit(2)
    fn(*sys.argv[2:])
