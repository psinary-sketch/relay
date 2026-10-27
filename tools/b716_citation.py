# -*- coding: utf-8 -*-
"""b716_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b716's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (bde68a30, a new session after the clear; the anchor (R326)'s line); the answer route is b682's, imported from
### tools/b682_citation.py with its act names pointed at b716, b706's repair carried (a bare eight-hex token a bank names as a sha256 or a
### kernel's lakefile pins as a rev is not read as a commit); the `word` route is b694's. Routes: `check [dry]` -> data/b716_citation_check.txt
### (.json) ; `ferry` -> data/b716_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the check on one answer.
### Carried by diff from b715_citation.py (data/b716_carry_citation.txt), b715's cite rows pruned (data/b716_prune_citation.txt) and this
### ruling's written by the Edit tool; this tool writes only the banks named above. Its (R326)(1) row reads lv's release list by `gh` (the
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
import b716_worklist as K   # noqa: E402
import act_membrane as MEM  # noqa: E402  ### (R326)(2)(ii): the membrane before every bank write of this tool


def _root_exclude():
    import b716_record as REC   # ### the record tool's exclusion pattern, the one the root route reads (imported at the call, nothing written)
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
    # ### b716: the cite rows of (R326) and its ferry, written by the Edit tool after b715's rows were pruned (data/b716_prune_citation.txt)
    for f in K.PATHS:
        add('ruling PATHS', f, os.path.isdir(f), 'present' if os.path.isdir(f) else 'ABSENT', '0')
    for f in ('data/b715_closing.txt', 'data/b715_events.txt', 'data/b715_defects.txt', 'data/b715_toolset_coverage.txt', 'data/b715_replay.txt',
              'data/b715_author_words_preseal.txt', 'data/b715_author_answers.txt', 'data/b715_pins_census.txt', 'data/b714_heads_draft.txt',
              'data/b714_pilot.txt', 'data/b714_residual.txt', 'data/b714_law.txt', 'data/b713_source_pin.txt', 'data/b712_genus_control.txt',
              'data/b710_registrations.txt', 'data/standing_clauses_v5.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    add('ferry read-first', 'the census on main by its rows: PLACE-papers phase2/method/THE_KEYSTONE_CENSUS_v0_8_2.md',
        os.path.exists(os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS_v0_8_2.md')), 'exists at the working tree', '0')
    law = lines_of(p('data', 'b714_law.txt'))
    add('ferry read-first', '"the law-identity bank of b714 (7)": data/b714_law.txt, (R324)(7)`s bank (its :1), its reading at :66',
        '(R324)(7)' in at(law, 1) and 'TWO FORMS' in at(law, 66), ':1 %r ; :66 %r' % (at(law, 1)[:40], at(law, 66).strip()[:40]), '0')
    # ### (R326)(1): b715 at its weight
    cl = lines_of(p('data', 'b715_closing.txt'))
    q = _quote(text, 'b715 closed: relay', '”; its relay commit')
    add('ruling (1)', 'data/b715_closing.txt :1, the head line, against (R326)(1)`s quote', bool(q) and q == cl[0],
        'quote %d characters, the line %d ; equal byte for byte %s' % (len(q), len(cl[0]), q == cl[0]), '1')
    rec_s = (g(ROOT, 'log', '-1', '--format=%H %s', 'fdddea13')[1] or '').strip()
    clo_s = (g(ROOT, 'log', '-1', '--format=%H %s', 'cf51ee95')[1] or '').strip()
    rmain = (g(ROOT, 'ls-remote', 'origin', 'refs/heads/main')[1] or '').split()
    add('ruling (1)', 'its relay commit the record`s (fdddea13, "b715 record"), the closing`s cf51ee95 ("b715: the closing"), the remote main',
        rec_s[41:].startswith('b715 record') and clo_s[41:].startswith('b715: the closing') and rmain[:1] == [clo_s[:40]],
        '%s ; %s ; remote main %s' % (rec_s[:52], clo_s[:58], (rmain or ['NONE'])[0][:8]), '1')
    sdir = p('tools', 'standing')
    sfiles = sorted(f for f in os.listdir(sdir) if os.path.isfile(os.path.join(sdir, f))) if os.path.isdir(sdir) else []
    scan = rd(p('data', 'b715_standing_scan.txt')) or ''
    add('ruling (1)', 'tools/standing/ at v1.0.0, 11 files, act literals in the code 0 (VERSION ; data/b715_standing_scan.txt)',
        (rd(os.path.join(sdir, 'VERSION')) or '').strip() == 'v1.0.0' and len(sfiles) == 11 and 'LITERALS IN THE CODE 0' in scan,
        'VERSION %r ; files %d ; the scan`s figure %s' % ((rd(os.path.join(sdir, 'VERSION')) or '').strip(), len(sfiles), 'LITERALS IN THE CODE 0' in scan), '1')
    cov = lines_of(p('data', 'b715_toolset_coverage.txt'))
    add('ruling (1)', 'the coverage table at 1 of 25 STANDING ([18]), the core inside [3], [7], [8], [17], [20], [25] (data/b715_toolset_coverage.txt :36)',
        'STEPS 25 ; STANDING 1 ([18])' in at(cov, 36) and 'AT [3], [7], [8], [17], [20], [25]' in at(cov, 36), ':36', '1')
    rp = lines_of(p('data', 'b715_replay.txt'))
    add('ruling (1)', 'the replay 11 of 12 EQUAL, the one DIFFERS the old tool`s F-2, F-1 the seal`s head (data/b715_replay.txt :77, :80, :87)',
        'OBJECTS 12 ; EQUAL 11 ; DIFFERS 1' in at(rp, 87) and 'F-2' in at(rp, 77) and at(rp, 80).strip().startswith('F-1') and 'SEAL' in at(rp, 80),
        ':87 ; :77 ; :80', '1')
    sh = _jl('b715_seal_hashes.json')
    add('ruling (1)', 'G-RULE-LONG-PHASE-SPLIT sealed, not withheld (data/b715_seal_hashes.json `withheld`)', sh.get('withheld') == [],
        'withheld %r' % sh.get('withheld'), '1')
    ros5 = rd(p('data', 'b715_roster.txt')) or ''
    mv = rd(p('data', 'b715_mirror_verify.txt')) or ''
    add('ruling (1)', 'the roster from main, the census v0.8 and v0.8.1 joined (data/b715_roster.txt); the verification NOT CLEAN (data/b715_mirror_verify.txt)',
        'THE_KEYSTONE_CENSUS_v0_8.md' in ros5 and 'THE_KEYSTONE_CENSUS_v0_8_1.md' in ros5 and 'NOT CLEAN' in mv,
        'joins named %s ; NOT CLEAN in the verify bank %s' % ('THE_KEYSTONE_CENSUS_v0_8_1.md' in ros5, 'NOT CLEAN' in mv), '1')
    pc = lines_of(p('data', 'b715_pins_census.txt'))
    allrows = [l for l in pc if l.startswith('--- ')]
    pub = [l for l in allrows if 'visibility PUBLIC' in l]
    prv = [l.split()[1] for l in allrows if 'visibility PRIVATE' in l]
    revs = [l for l in pc if l.strip().startswith('MATHLIB UPSTREAM PIN')]
    add('ruling (1)', 'the pins census at 39 public repositories, 0 hard failures, upstream Mathlib at five revs (data/b715_pins_census.txt)',
        len(pub) == 39 and any(l.strip() == '### REPOS HARD-FAILING : 0' for l in pc) and len(revs) == 5,
        'repository rows %d (the bank`s :2 "ALL 39 REPOS") ; PUBLIC %d ; PRIVATE %d %s (b714`s four) ; HARD-FAILING 0 %s ; Mathlib revs %d' % (
            len(allrows), len(pub), len(prv), prv, any(l.strip() == '### REPOS HARD-FAILING : 0' for l in pc), len(revs)), '1')
    add('ruling (1)', 'the suite 135 of 140 pre-push and 136 of 140 post-push (data/b715_closing.txt :260, :262)',
        'ARMS RUN : 140. ### LIVE PASSING : 135.' in at(cl, 260) and 'ARMS RUN : 140. ### LIVE PASSING : 136.' in at(cl, 262), ':260 ; :262', '1')
    row = act_root_line('b715')
    add('ruling (1)', 'the root c0e86c02 (data/act_roots.txt, b715`s row)', bool(row) and row[-1][1].startswith('c0e86c02'),
        'row b715 %s' % (row[-1][1][:8] if row else 'NONE'), '1')
    ev = lines_of(p('data', 'b715_events.txt'))
    starts = dict((int(m.group(1)), i + 1) for i, l in enumerate(ev) for m in [re.match(r'^\((\d+)\) ', l)] if m)
    add('ruling (1); ruling (2)', 'eleven events in data/b715_events.txt, (1)-(11) each on its starting line', sorted(starts) == list(range(1, 12)),
        'starting lines %s' % [starts[k] for k in sorted(starts)], '1')
    dl = lines_of(p('data', 'b715_defects.txt'))
    dlet = [(m.group(1), m.group(2), m.group(3)) for l in dl for m in [re.match(r"^    \(([a-z])\) (THE [A-Z]+'S):? ?(.*)", l)] if m]
    nav = [x[0] for x in dlet if x[1] == "THE NAVIGATOR'S"]
    add('ruling (1)', 'seventeen defects (a)-(q), (d) the navigator`s (data/b715_defects.txt)', ''.join(x[0] for x in dlet) == 'abcdefghijklmnopq' and nav == ['d'],
        'letters %s ; the navigator`s %s' % (''.join(x[0] for x in dlet), nav), '1')
    add('ruling (1); ruling (9)', '"Nothing deposited, nothing published": the draft at v5, held', K.DRAFT == '23228113', 'tools/b716_worklist.py DRAFT', '1')
    # ### (R326)(2): the corrigendum's sources
    add('ruling (2)', 'the corrigendum tool to carry (tools/b715_corrigendum.py) and the one lettering (tools/act_letters.py)',
        os.path.exists(p('tools', 'b715_corrigendum.py')) and os.path.exists(p('tools', 'act_letters.py')), 'present', '1')
    cg = lines_of(p('data', 'b675_corrigenda.txt'))
    last = [l for l in cg if re.match(r'^\s*\((\d+)\)', l)]
    add('ruling (2)', 'the corrigenda bank, appended only (its last row (35), b715`s)', bool(last) and re.match(r'^\s*\(35\)', last[-1]) is not None,
        'data/b675_corrigenda.txt, last row %r' % (last[-1][:40] if last else ''), '1')
    refused = [x[0] for x in dlet if 'REFUSED' in x[2]]
    add('ruling (2)', 'the defects whose head names a hook refusal ("REFUSED"), the hook`s held rule (data/b715_defects.txt)', len(refused) >= 1,
        'heads naming REFUSED: %s' % ''.join(refused), '1')
    # ### (R326)(3): the toolset's repairs, their record instances
    ans = lines_of(p('data', 'b715_author_answers.txt'))
    prompts = [l for l in ans if l.startswith('### PROMPT ')]
    import b715_worklist as K5
    dels = [b for _r, names in K5.DELETE for b in names]
    add('ruling (3)(i)', 'b715`s six named deletes (tools/b715_worklist.py DELETE) and four prompts (data/b715_author_answers.txt `### PROMPT` rows); events (7), (8)',
        len(dels) == 6 and len(prompts) == 4 and 7 in starts and 8 in starts, 'deletes %d ; prompts %d ; events (7) :%s (8) :%s' % (len(dels), len(prompts), starts.get(7), starts.get(8)), '2')
    s4 = (g(ROOT, 'log', '-1', '--format=%s', '4e4c4759')[1] or '').strip()
    add('ruling (3)(ii)', 'the seal`s recorded head c5370fca and the seal commit 4e4c4759 (data/b715_seal_hashes.json relay_head ; event (1))',
        str(sh.get('relay_head', '')).startswith('c5370fca') and bool(s4) and 1 in starts, 'relay_head %s ; 4e4c4759 %r' % (str(sh.get('relay_head', ''))[:8], s4[:50]), '2')
    mvp = lines_of(p('tools', 'mirror_verify.py'))
    add('ruling (3)(iii)', 'the verifier`s own roster: tools/mirror_verify.py :70 ROSTER (event (10))', 'ROSTER' in at(mvp, 70) and 'mirror_roster.json' in at(mvp, 70) and 10 in starts,
        ':70 %r' % at(mvp, 70).strip()[:70], '2')
    aw = lines_of(p('data', 'b715_author_words_preseal.txt'))
    heads = [l for l in aw if re.match(r'^## \(\d+\) ', l)]
    add('ruling (3)(iv)', 'the author`s-words bank`s "## (n)" heads (data/b715_author_words_preseal.txt), three before the seal and the root`s word in the answers bank (event (3))',
        len(heads) == 3 and 3 in starts, 'heads %d at %s' % (len(heads), [i + 1 for i, l in enumerate(aw) if re.match(r'^## \(\d+\) ', l)]), '2')
    add('ruling (3)(v)', 'events (4) and (6), the entry`s and the trail`s carried clauses (data/b715_events.txt)', 4 in starts and 6 in starts,
        '(4) :%s ; (6) :%s' % (starts.get(4), starts.get(6)), '2')
    r5 = rd(p('tools', 'b715_record.py')) or ''
    add('ruling (3)(vi)', 'defect (j): the exclusion narrowed to `chain_half_` in tools/b715_record.py', any(x[0] == 'j' for x in dlet) and 'chain_half_' in r5,
        'defect (j) %s ; chain_half_ in the record tool %s' % (any(x[0] == 'j' for x in dlet), 'chain_half_' in r5), '2')
    for f in ('data/b716_toolset_coverage.txt', 'data/b716_tool_repairs.txt', 'data/b716_replay.txt', 'data/b716_readfirst.txt', 'data/b716_rules.txt'):
        add('ruling (3); ruling (8)', '%s -- TO BE WRITTEN by this act' % f, not os.path.exists(p(*f.split('/'))), 'absent, as ordered', '0-2')
    # ### (R326)(4): the -39 registration's sources
    sp = rd(p('data', 'b713_source_pin.txt')) or ''
    add('ruling (4)(i)', 'Murty-Osburn arXiv:math/0412237v1 Theorem 2.3 as pinned at b713 (data/b713_source_pin.txt, sha256 5de0ba03)',
        'arXiv:math/0412237v1' in sp and 'Theorem 2.3' in sp and '5de0ba0368f3c627' in sp, 'the text, the theorem and the sha256 named', '0')
    gc = lines_of(p('data', 'b712_genus_control.txt'))
    add('ruling (4)(i)', 'b712`s control, run before its commit (data/b712_genus_control.txt :43, :45)', 'MISSES THROUGH n = 400: 0' in at(gc, 43) and 'MISSES 0' in at(gc, 45),
        ':43 ; :45', '0')
    c11, c13 = lines_of(p('data', 'b711_coeffs.txt')), lines_of(p('data', 'b713_coeffs.txt'))
    add('ruling (4)(ii)', 'the observation at Q0 and -15: least negative index 48 (b711_coeffs :12) and 24 (b713_coeffs :13), each c = -2 log n',
        'n = 48 ; c(48) = (-8) log 2 + (-2) log 3' in at(c11, 12) and 'n = 24 ; c(24) = (-6) log 2 + (-2) log 3' in at(c13, 13), ':12 ; :13', '0')
    r10, r12 = lines_of(p('data', 'b710_registrations.txt')), lines_of(p('data', 'b712_registrations.txt'))
    add('ruling (4)(iii)', 'the refined law of b710 (i) (:21, the first-order form) and the window [0.99, 1.01]: b712 (ii) :46-:48 carried b710 (i) unchanged with it; b710 (i)`s own F2 window [0.9, 1.1] (:43)',
        'r n* = 4 log(4C) + 8 log(n* + 1)' in at(r10, 21) and '[0.99, 1.01]' in at(r12, 48) and '[0.9, 1.1]' in at(r10, 43),
        ':21 ; b712 :48 ; :43 -- the ruling`s window the first-order form`s (b714 (7) :70), not F2`s', '0')
    for f in ('data/b716_registrations.txt', 'data/b716_genus_control.txt', 'data/b716_price.txt'):
        add('ruling (4)', '%s -- TO BE WRITTEN by this act' % f, not os.path.exists(p(*f.split('/'))), 'absent, as ordered', '0-4')
    # ### (R326)(5): the keystone items
    hd = lines_of(p('data', 'b714_heads_draft.txt'))
    add('ruling (5)(i)', 'the heads draft`s sections II and III (data/b714_heads_draft.txt :33, :66)', at(hd, 33).startswith('## II.') and at(hd, 66).startswith('## III.'),
        ':33 %r ; :66 %r' % (at(hd, 33)[:30], at(hd, 66)[:30]), '5')
    pl = lines_of(p('data', 'b714_pilot.txt'))
    add('ruling (5)(ii)', 'the six lint hits FOR THE AUTHOR (data/b714_pilot.txt :94)', '(P2) HITS 7: AS DESIGNED 1 ; FOR THE AUTHOR 6' in at(pl, 94), ':94', '5')
    sil = (g(PP, 'show', 'main:day1/Silence_of_Foundations.md')[1] or '').split(NL)
    smeta = _blob(K.META_DIR, 'v0.1.0', 'SIDEMeta/Meta/SIDESystem.lean').split(NL)
    add('ruling (5)(iii)', 'Silence :212 names SIDESystem on main; SIDE-meta SIDEMeta/Meta/SIDESystem.lean :99 a structure at the tag v0.1.0 (6bb7b23, v0.3 the same commit)',
        'SIDESystem' in at(sil, 212) and at(smeta, 99).startswith('structure SIDESystem'), ':212 %r ; :99 %r' % (at(sil, 212)[:50], at(smeta, 99)[:40]), '3')
    add('ruling (5)(iv)', 'the 19 names with no pin (data/b714_pilot.txt :66, (P1))', 'NO PIN STATED 19' in at(pl, 66), ':66', '3')
    add('ruling (5)(v)', 'the census v0.8.2 rows of (R325)(7) as b715`s banks state them (data/b715_chain_rows.txt ; the census diff)',
        os.path.exists(p('data', 'b715_chain_rows.txt')) and os.path.exists(p('data', 'b715_census_diff.txt')), 'present', '3')
    # ### (R326)(6): the prices' sources
    for f in ('data/b716_federation_pin_price.txt', 'data/b716_epstein_count_price.txt'):
        add('ruling (6)', '%s -- TO BE WRITTEN by this act' % f, not os.path.exists(p(*f.split('/'))), 'absent, as ordered', '4')
    # ### (R326)(7): the carried files and the branches
    dirty = (g(ROOT, 'diff', '--name-only')[1] or '').split()
    add('ruling (7)', 'data/b715_relay_push-b715-closing_push_out.txt, untracked', os.path.exists(p('data', 'b715_relay_push-b715-closing_push_out.txt'))
        and not (g(ROOT, 'ls-files', 'data/b715_relay_push-b715-closing_push_out.txt')[1] or '').strip(), 'present, untracked', '0')
    st = _jl('b715_steps.json').get('rows', [])
    add('ruling (7)', 'step row 21 of data/b715_steps.json (the closing`s, cf51ee95), uncommitted', len(st) == 21 and str(st[20].get('commit', '')).startswith('cf51ee95')
        and 'data/b715_steps.json' in dirty, 'rows %d ; row 21 %s' % (len(st), (str(st[20].get('commit', ''))[:8], st[20].get('phase')) if len(st) >= 21 else 'NONE'), '0')
    for f in ('data/b715_hook_refusals.txt', 'data/b714_hook_refusals.txt', 'data/b715_bank_hashes.json', 'tools/mirror_prevbuild.json'):
        add('ruling (7)', '%s, modified at the working tree and uncommitted' % f, f in dirty, 'in `git diff --name-only`', '0')
    for repo, names in K.DELETE:
        lst = g(repo, 'branch', '--merged', 'main')[1] or ''
        for b in names:
            add('ruling (7)', '%s %s (local, listed --merged)' % (os.path.basename(repo), b), b in [x.strip(' *') for x in lst.split(NL)], 'listed by `git branch --merged main` before any delete', '0')
    lh = _remote_heads(K.LV_DIR)
    loc = (g(K.LV_DIR, 'rev-parse', K.PORT_BRANCH)[1] or '').strip()
    add('ruling (7)', 'port-b707 at cb0aea56 locally and at the remote, NOT deleted', loc == K.PORT_TIP and lh.get('refs/heads/port-b707') == K.PORT_TIP,
        'local %s ; remote %s' % (loc[:8], (lh.get('refs/heads/port-b707') or '')[:8]), '0')
    add('ruling (7)', 'the 2,560 MB hold', K.HOLD == 2560, 'tools/b716_worklist.py HOLD', '0')
    # ### the ferry
    add('ferry', 'the hook in D:/.claude/settings.json is the standing one (tools/standing/hook.py)', 'standing/hook.py' in (rd('D:/.claude/settings.json') or ''), 'D:/.claude/settings.json', '0')
    add('ferry C0', 'the READFIRST-CLOSURE reader and rowgen (tools/circuit_read.py)', os.path.exists(p('tools', 'circuit_read.py')), 'present', '0')
    add('ferry C6', 'the chain halves as b693 drew them, b716 added to the second', K.CHAIN_HALVES[1] == ('b659', 'b716'), 'tools/b716_worklist.py CHAIN_HALVES', '5')
    add('ferry C0', 'this act`s session transcript (a new session after the clear)', os.path.exists(C.SESSION), C.SESSION, '0')
    standing_rows(text, add)
    return R


def standing_rows(text, add):
    """the citation tool reads the standing clauses by version (data/b712_rules.txt row (1)): for each version a ferry names as "standing clauses v<N>"
    outside a quotation, the bank data/standing_clauses_v<N>.txt present with its VERSION line -- v1 with its control banked AS WANTED; a version this
    act writes at step zero (v2, (R326)(2)) read as TO BE WRITTEN when absent and from the bank when present."""
    import b715_standing as SC
    flat = re.sub(r'“[^”]*”', '', ' '.join(text.split()))
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing clauses(?:’)? v(\d+)', flat, re.I)))
    for v in names or [1]:
        p = os.path.join(D, 'standing_clauses_v%d.txt' % v)
        t = rd(p) or ''
        ver = re.search(r'^VERSION: (\d+)$', t, re.M)
        if v == 1:
            ctl = _jl('b715_standing_control.json')
            add('ferry (standing clauses)', 'the standing clauses v1: data/standing_clauses_v1.txt', bool(t) and bool(ver) and ver.group(1) == '1' and bool(SC.parse(t)) and ctl.get('ok') is True,
                'present %s ; VERSION %s ; rows %d ; the re-assembly control AS WANTED %s' % (bool(t), ver.group(1) if ver else 'NONE', len(SC.parse(t)), ctl.get('ok')), '0')
        elif not t:
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- TO BE WRITTEN at step zero ((R326)(2))' % (v, v), True, 'absent, as ordered', '0')
        else:
            add('ferry (standing clauses)', 'the standing clauses v%d: data/standing_clauses_v%d.txt' % (v, v), bool(ver) and ver.group(1) == str(v), 'present ; VERSION %s' % (ver.group(1) if ver else 'NONE'), '0')


def _write(L, R, miss):
    for n_ in ('b716_citation_check.txt', 'b716_citation_check.json'):
        MEM.guard('b716', n_, _root_exclude())
    for name, data in (('b716_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b716_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        with open(q + '.tmp', 'wb') as fh:
            fh.write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b716 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b716_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b716_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b716_ferry_scan.txt')
    MEM.guard('b716', 'b716_ferry_scan.txt', _root_exclude())
    with open(s + '.tmp', 'wb') as fh:
        fh.write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b716_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
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
    """(R278)(4): b682's route, imported, with its act names pointed at b716, and b706's repair carried."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.C.SESSIONS_AFTER = C.SESSIONS_AFTER
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, K.LV_DIR, K.JOIN_DIR, 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects', 'D:/SIDE-bijection', 'D:/SIDE-interfaces', 'D:/SIDE-li-map',
                                                 'D:/SIDE-kernel') if r not in P.REPOS and os.path.isdir(r))
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b716'))
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
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b716')
    # ### (R326)(2), the item repair: THE WHOLE ANSWER. b682's cut ends at the first "END" after the needle (`best.find('END', k)`, :221), which a
    # ### word carrying END (AMENDMENT, APPENDED, RECOMMENDED) ends inside: b715's answers read 468 characters. The cut now ends at the answer's
    # ### last END (`best.rfind('END')`), the paste's own tail; the substitution printed, the route refusing where it does not apply.
    if body.count("best.find('END', k)") != 1:
        sys.exit('### b682`s CUT NOT FOUND ONCE IN ITS answer -- NOTHING CHECKED')
    body = body.replace("best.find('END', k)", "best.rfind('END')")
    body = body.replace("    open(q + '.tmp', 'wb')", "    MEM.guard('b716', os.path.basename(q), ROOT_EXCLUDE)\n    open(q + '.tmp', 'wb')")
    ns = dict(vars(P))
    ns.update(MEM=MEM, ROOT_EXCLUDE=_root_exclude())
    exec(compile(body, 'b682_citation.answer (b716)', 'exec'), ns)
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
        print('usage: b716_citation.py check [dry] | ferry | answer <needle> | word <needle> | replay <needle> <session id> <anchor>')
        sys.exit(2)
    fn(*sys.argv[2:])
