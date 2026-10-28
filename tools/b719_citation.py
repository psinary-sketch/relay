# -*- coding: utf-8 -*-
"""b719_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b719's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (bde68a30, a new session after the clear; the anchor (R329)'s line); the answer route is b682's, imported from
### tools/b682_citation.py with its act names pointed at b719, b706's repair carried (a bare eight-hex token a bank names as a sha256 or a
### kernel's lakefile pins as a rev is not read as a commit); the `word` route is b694's. Routes: `check [dry]` -> data/b719_citation_check.txt
### (.json) ; `ferry` -> data/b719_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the check on one answer.
### Carried by diff from b718_citation.py (data/b719_carry_citation.txt), b718's cite rows pruned (data/b719_prune_citation.txt) and this
### ruling's written by the Edit tool; this tool writes only the banks named above. Its (R329)(1) row reads lv's release list by `gh` (the
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
import b719_worklist as K   # noqa: E402
import act_membrane as MEM  # noqa: E402  ### (R329)(2)(ii): the membrane before every bank write of this tool


def _root_exclude():
    import b719_record as REC   # ### the record tool's exclusion pattern, the one the root route reads (imported at the call, nothing written)
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
    # ### b719: the cite rows of (R329) and its ferry, written by the Edit tool after b718's rows were pruned (data/b719_prune_citation.txt)
    # ### (R329)(1): the author's word on f6f6df5
    dl = lines_of(p('data', 'b718_defects.txt'))
    add('ruling (1)', 'defect (b`) at data/b718_defects.txt :33 (f6f6df5`s commit message names the outside collection)',
        at(dl, 33).startswith("    (b') ") and 'f6f6df5' in at(dl, 33), at(dl, 33)[:90], '0, 1')
    msg = (g(PP, 'log', '-1', '--format=%B', 'f6f6df5')[1] or '')
    add('ruling (1)', 'the message names openai/math at 7ef5c0cc5, lean/ComparatorChallenges/QuasiRiemannHypothesis.lean, the ruling`s path '
        'lean/QuasiRiemannHypothesis.lean as "Not Found", and C6`s grading words',
        'openai/math 7ef5c0cc5' in msg and 'lean/ComparatorChallenges/QuasiRiemannHypothesis.lean' in msg and 'lean/QuasiRiemannHypothesis.lean Not Found' in msg
        and 'graded at E0' in msg, 'the message %d characters' % len(msg.strip()), '0')
    env = dict(os.environ, GIT_TERMINAL_PROMPT='0')   # ### inside the tool's own call, no shell prefix; no token, no credential helper, nothing of the author sent
    r = subprocess.run(['git', '-c', 'credential.helper=', '-c', 'core.askPass=', 'ls-remote', 'https://github.com/openai/math', 'refs/heads/main'],
                       capture_output=True, text=True, env=env, timeout=60)
    add('ruling (1)', 'ls-remote with no token and no credential helper answers refs/heads/main 7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a (public)',
        r.returncode == 0 and r.stdout.split()[:2] == ['7ef5c0cc5ca4b0e072b7a050fca09ab24bc6fa3a', 'refs/heads/main'], (r.stdout.strip() or r.stderr.strip())[:80], '0')
    hr = lines_of(p('data', 'b718_hook_refusals.txt'))
    add('ruling (1); ruling (3)', '"at 8:57 PM on 2026-10-27" (local): the read and the refusal of that minute (data/b718_hook_refusals.txt :8, an ENV refusal)',
        ' | ENV | ' in at(hr, 8) and at(hr, 8).startswith('2026-10-28T00:56'), at(hr, 8)[:40] + ' (UTC; 8:56:54 PM at UTC-4)', '0, 1')
    # ### (R329)(2): b718's close completed at step zero
    for repo, nm, short in ((ROOT, 'relay', K.B718_RELAY_HEAD), (PP, 'PLACE-papers', K.B718_PP_HEAD)):
        h = (g(repo, 'rev-parse', 'HEAD')[1] or '').strip()
        add('ruling (2)', '%s %s, b718`s head, to be pushed by tools/push_gated.sh at step zero' % (nm, short), h.startswith(short) and os.path.exists(p('tools', 'push_gated.sh')),
            'HEAD %s' % h[:8], '0')
    ti = _quote(text, '"The coefficient law derived to the step named', '". b718')[1:]
    fl = at(fi, 10858)
    add('ruling (2)', 'b718`s FINDINGS entry at :10858, its title as the ruling quotes it', fl == '## ' + ti,
        'equal %s ; equal with x^2 and 10y^2 read as x² and 10y² %s' % (fl == '## ' + ti, fl == '## ' + ti.replace('x^2', 'x²').replace('10y^2', '10y²').replace("'", '’')), '0, 7')
    add('ruling (2)', 'b718`s root [14], trail [15], desk, suites, scores close [22], mirror and closing: to be run at step zero under b718`s sealed tools',
        os.path.exists(p('data', 'b718_seal_hashes.json')) and not os.path.exists(p('data', 'b718_closing.txt')), 'the seal present, no closing yet', '0')
    # ### (R329)(3): the corrigendum's sources
    ev = lines_of(p('data', 'b718_events.txt'))
    starts = sorted(int(m.group(1)) for m in (re.match(r'^    \((\d+)\) ', l) for l in ev) if m)
    tags = [re.search(r'\[(CLAIM|CLOSE) ;', l).group(1) for l in ev if re.match(r'^    \(\d+\) ', l) and re.search(r'\[(CLAIM|CLOSE) ;', l)]
    add('ruling (3)', 'data/b718_events.txt (1)-(13), each tagged', starts == list(range(1, 14)) and len(tags) == 13, 'starts %s ; CLAIM %d ; CLOSE %d' % (starts[-1:], tags.count('CLAIM'), tags.count('CLOSE')), '1')
    e10 = next((l for l in ev if l.startswith('    (10) ')), '')
    add('ruling (3)', 'event (10): FINDINGS :10847 cites (R328)(6) where the toolset`s clause is (R328)(7)',
        'FINDINGS :10847' in e10 and '(R328)(6)' in at(fi, 10847) and 'toolset' in at(fi, 10847), at(fi, 10847)[:70], '1')
    f18 = rd(p('data', 'b718_ferry.txt')) or ''
    add('ruling (3)', '(R328)(7) is the toolset`s clause, (R328)(6) TWO READS (data/b718_ferry.txt)', '(7) THE TOOLSET' in f18 and '(6) TWO READS' in f18,
        '(7) THE TOOLSET %s ; (6) TWO READS %s' % ('(7) THE TOOLSET' in f18, '(6) TWO READS' in f18), '1')
    # ### (R329)(4): the eleven DIFFERS
    tl = lines_of(p('data', 'b718_touch.txt'))
    trows = dict((int(m.group(1)), m.group(2)) for m in (re.match(r'^  \((\d+)\) .* -- (AGREES|DIFFERS)\b', l) for l in tl) if m)
    dif = sorted(k for k, v in trows.items() if v == 'DIFFERS')
    add('ruling (4)', 'the eleven DIFFERS of data/b718_touch.txt, ten on T-COUNT among rows (298)-(309), the eleventh beyond',
        len(dif) == 11 and len([k for k in dif if 298 <= k <= 309]) == 10, 'DIFFERS at %s' % dif, '1')
    add('ruling (4)', 'data/b718_touch.txt :448, the summary', 'AGREES 402' in at(tl, 448) and 'DIFFERS 11' in at(tl, 448), at(tl, 448)[-70:], '1')
    cr = lines_of(p('data', 'b718_count_read.txt'))
    add('ruling (4); ruling (11)', 'data/b718_count_read.txt :19, b705`s contour does not discharge the count law', 'DOES NOT' in at(cr, 19), at(cr, 19)[-90:], '1, 6')
    # ### (R329)(5): the join's premise
    rp = _blob(K.LV_DIR, K.LV_V0100, 'SIDELvConservation/RegisterPentagon.lean').split(NL)
    add('ruling (5)', 'RegisterPentagon.lean :149-:152 at the deposit 93c27ec', len(rp) >= 152 and bool(''.join(rp[148:152]).strip()),
        [l.strip()[:60] for l in rp[148:152]][:2], '1')
    jp = lines_of(p('data', 'b718_join_premise.txt'))
    add('ruling (5)', 'data/b718_join_premise.txt :35, DIFFERS as worded', 'DIFFERS' in at(jp, 35), at(jp, 35)[-80:], '1')
    jt = (g(K.JOIN_DIR, 'rev-parse', 'v0.1.0^{commit}')[1] or '').strip()
    jd = _decl_files(K.JOIN_DIR, 'v0.1.0', 'faces_join')
    add('ruling (5)', 'faces_join compiled at SIDE-faces-join v0.1.0', jt == K.JOIN_TAG[2] and bool(jd), 'v0.1.0 at %s ; declared in %s' % (jt[:8], jd), '1')
    lvm = (g(K.LV_DIR, 'rev-parse', 'main')[1] or '').strip()
    add('ruling (5); N5', 'lv`s main and deposit untouched (main d38f3e8c, deposit 93c27ec)', lvm == K.LV_MAIN and bool(_blob(K.LV_DIR, K.LV_V0100, 'lakefile.toml') or rp[0:1]),
        'main %s' % lvm[:8], '1')
    # ### (R329)(6): the law at -20 and -47
    rb = (g(ROOT, 'show', '%s:%s' % (K.REG_COMMIT, K.REGISTRATIONS))[1] or '')
    rg = lines_of(p(*K.REGISTRATIONS.split('/')))
    add('ruling (6)(i), N2', 'data/b718_registrations.txt read unchanged from its commit 8146404b; -20 (h 2) and -47 (h 5) at :16-:17',
        bool(rb) and rb.replace(chr(13), '') == (rd(p(*K.REGISTRATIONS.split('/'))) or '') and '-20' in at(rg, 16) and '-47' in at(rg, 17),
        'blob %d characters ; :16 %r ; :17 %r' % (len(rb), at(rg, 16)[:40], at(rg, 17)[:40]), '2')
    # ### H-47's premise: at -47 (h 5, cyclic of prime order) the primes 2 and 3 split and are represented by no principal form, so their classes
    # ### have order 5 -- read by the forms alone (x^2 + xy + 12y^2 takes no value 2 or 3; 2x^2 + xy + 6y^2 takes 2, 3x^2 + xy + 4y^2 takes 3)
    rep = lambda a, b, c, n: any(a * x * x + b * x * y + c * y * y == n for x in range(-6, 7) for y in range(-6, 7))   # noqa: E731
    add('ruling (6)(i)', 'H-47`s premise: at -47 the classes of the prime ideals above 2 and 3 have order 5',
        not rep(1, 1, 12, 2) and not rep(1, 1, 12, 3) and rep(2, 1, 6, 2) and rep(3, 1, 4, 3) and 1 * 1 - 4 * 1 * 12 == -47,
        'principal takes 2 %s, 3 %s ; 2x^2+xy+6y^2 takes 2 %s ; 3x^2+xy+4y^2 takes 3 %s ; h 5 prime' % (rep(1, 1, 12, 2), rep(1, 1, 12, 3), rep(2, 1, 6, 2), rep(3, 1, 4, 3)), '2')
    src = rd(p('tools', 'b711_coeffs.py')) or ''
    add('ruling (6)(ii)', 'b711`s route (tools/b711_coeffs.py) through the cut 32532 with its controls C1-C3', '32532' in src and all(c in src for c in ('C1', 'C2', 'C3')),
        'cut %s ; C1-C3 %s' % ('32532' in src, all(c in src for c in ('C1', 'C2', 'C3'))), '2')
    dc = lines_of(p('data', 'b718_decomp.txt'))
    add('ruling (6)(ii)', 'data/b718_decomp.txt :42, the three read', '15' in at(dc, 42), at(dc, 42)[-80:], '2')
    # ### (R329)(7): the derivation's remaining step
    dv = lines_of(p('data', 'b718_derivation.txt'))
    add('ruling (7)', 'data/b718_derivation.txt :136, the grade and the step named', 'CLAUSE 1 NOT DERIVED' in at(dv, 136), at(dv, 136)[-90:], '3')
    for f in K.COEFF_BANKS:
        add('ruling (7)', 'the check bank %s (-23, -15, -39)' % f, os.path.exists(p(*f.split('/'))), 'present', '3')
    # ### (R329)(8): the offset
    on = lines_of(p(*K.ONSETS_B717.split('/')))
    add('ruling (8)(i)', 'b717`s seven -39 offsets (data/b717_onsets.txt, its last line: HELD 7)', any('HELD 7' in l for l in on), 'found %s' % any('HELD 7' in l for l in on), '4')
    add('ruling (8)(i)', 'the ten -15 and -23 offsets (45, 45, 59, 70, 65, 64, 65, 137, 59, 61), the navigator`s post hoc observation: read from their onset banks at Component 4',
        True, 'to be read', '4')
    # ### (R329)(9): the surgery
    add('ruling (9)', 'b709`s grid (data/b709_grid.txt) and b718`s price (data/b718_surgery_price.txt)', os.path.exists(p('data', 'b709_grid.txt')) and os.path.exists(p('data', 'b718_surgery_price.txt')),
        'present', '5')
    # ### (R329)(10): the arms retired
    at_ = _jl('arm_tags.json')
    tg = at_.get('tags', at_) if isinstance(at_, dict) else {}
    vals = [v if isinstance(v, str) else (v.get('tag') if isinstance(v, dict) else '') for v in tg.values()]
    add('ruling (10)', 'data/arm_tags.json, every arm tagged CLAIM or CLOSE', bool(vals) and all(v in ('CLAIM', 'CLOSE') for v in vals),
        'arms %d ; CLAIM %d ; CLOSE %d' % (len(vals), vals.count('CLAIM'), vals.count('CLOSE')), '6')
    # ### (R329)(11): prices and moves
    add('ruling (11)', 'W-ORD-EPSTEIN-COUNT-LEAN in OPEN_TRAILS', any('W-ORD-EPSTEIN-COUNT-LEAN' in l for l in ot), 'found %s' % any('W-ORD-EPSTEIN-COUNT-LEAN' in l for l in ot), '6')
    for f in ('b718_registry_cells_price.txt', 'b718_challenge_price.txt', 'b718_pin.txt'):
        add('ruling (11)', 'b718`s price or bank data/%s' % f, os.path.exists(p('data', f)), 'present', '6')
    lb = [k for k in K.PIN_CARRIED if (g('D:/' + k, 'branch', '--list', K.PIN_BRANCH)[1] or '').strip()]
    add('ruling (11)', 'the nine local pin branches carried (%s)' % K.PIN_BRANCH, len(lb) == 9, 'found on %d of %d' % (len(lb), len(K.PIN_CARRIED)), '6')
    # ### (R329)(12)-(13)
    st = (g(ROOT, 'status', '--short', '--', 'data/b718_steps.json')[1] or '').strip()
    add('ruling (12)', 'b718`s step-20 row uncommitted (data/b718_steps.json)', st.startswith('M'), st or 'clean', '0')
    br = (g(ROOT, 'branch', '--list', 'push-b718-*')[1] or '').split()
    bp = (g(PP, 'branch', '--list', 'push-b718-*')[1] or '').split()
    add('ruling (12)', 'the push-b718-* branches: none yet (b718 pushed nothing); made by b718`s close at step zero, deleted after it', not br and not bp,
        'relay %s ; PLACE-papers %s' % (br, bp), '0')
    pb = (g(K.LV_DIR, 'rev-parse', 'refs/heads/port-b707')[1] or '').strip()
    add('ruling (12)', 'port-b707 kept (SIDE-lv-conservation, at cb0aea56)', pb == K.PORT_TIP, pb[:8], '0')
    add('ruling (13)', 'the draft at v5 (23228113), held', K.DRAFT == '23228113', 'tools/b719_worklist.py DRAFT', '0')
    # ### the ferry: paths and the readfirst list
    add('ferry (PATHS)', 'the act`s paths, each present', all(os.path.isdir(x) for x in K.PATHS), 'absent %s' % [x for x in K.PATHS if not os.path.isdir(x)], '0')
    rf = ['data/b718_events.txt', 'data/b718_defects.txt', 'data/b718_hook_refusals.txt', 'data/b718_quote_guard.txt', 'data/b718_touch.txt', 'data/b718_count_read.txt',
          'data/b718_join_premise.txt', 'data/b718_derivation.txt', 'data/b718_decomp.txt', 'data/b718_registrations.txt', 'data/b718_a0.txt', K.ONSETS_B717,
          'data/b711_coeffs.txt', 'data/b713_coeffs.txt', 'data/b717_coeffs.txt', 'data/arm_tags.json']
    add('ferry (readfirst)', 'the readfirst list`s %d relay banks, each present' % len(rf), all(os.path.exists(p(*f.split('/'))) for f in rf),
        'absent %s' % [f for f in rf if not os.path.exists(p(*f.split('/')))], '0')
    a0 = lines_of(p('data', 'b718_a0.txt'))
    add('ferry (readfirst)', 'data/b718_a0.txt :39, A0 certified', 'CERTIFIED' in at(a0, 39), at(a0, 39)[-60:], '0')
    add('ferry (readfirst)', 'FINDINGS :10847 and :10858 in local PLACE-papers', at(fi, 10847).startswith('**The CLOSE classes') and at(fi, 10858).startswith('## '),
        ':10847 %r ; :10858 %r' % (at(fi, 10847)[:30], at(fi, 10858)[:30]), '0')
    standing_rows(text, add)
    return R


def standing_rows(text, add):
    """the citation tool reads the standing clauses by version (data/b712_rules.txt row (1)): for each version a ferry names as "standing clauses v<N>"
    outside a quotation, the bank data/standing_clauses_v<N>.txt present with its VERSION line -- v1 with its control banked AS WANTED; a version this
    act writes at step zero (v2, (R329)(2)) read as TO BE WRITTEN when absent and from the bank when present."""
    import b718_standing as SC
    flat = re.sub(r'“[^”]*”', '', ' '.join(text.split()))
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing clauses(?:’)? v(\d+)', flat, re.I)))
    for v in names or [1]:
        p = os.path.join(D, 'standing_clauses_v%d.txt' % v)
        t = rd(p) or ''
        ver = re.search(r'^VERSION: (\d+)$', t, re.M)
        if v == 1:
            ctl = _jl('b718_standing_control.json')
            add('ferry (standing clauses)', 'the standing clauses v1: data/standing_clauses_v1.txt', bool(t) and bool(ver) and ver.group(1) == '1' and bool(SC.parse(t)) and ctl.get('ok') is True,
                'present %s ; VERSION %s ; rows %d ; the re-assembly control AS WANTED %s' % (bool(t), ver.group(1) if ver else 'NONE', len(SC.parse(t)), ctl.get('ok')), '0')
        elif not t:
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- TO BE WRITTEN at step zero ((R329)(2))' % (v, v), True, 'absent, as ordered', '0')
        else:
            add('ferry (standing clauses)', 'the standing clauses v%d: data/standing_clauses_v%d.txt' % (v, v), bool(ver) and ver.group(1) == str(v), 'present ; VERSION %s' % (ver.group(1) if ver else 'NONE'), '0')


def _write(L, R, miss):
    for n_ in ('b719_citation_check.txt', 'b719_citation_check.json'):
        MEM.guard('b719', n_, _root_exclude())
    for name, data in (('b719_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b719_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        with open(q + '.tmp', 'wb') as fh:
            fh.write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b719 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b719_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b719_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b719_ferry_scan.txt')
    MEM.guard('b719', 'b719_ferry_scan.txt', _root_exclude())
    with open(s + '.tmp', 'wb') as fh:
        fh.write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b719_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
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
    """(R278)(4): b682's route, imported, with its act names pointed at b719, and b706's repair carried."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.C.SESSIONS_AFTER = C.SESSIONS_AFTER
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, K.LV_DIR, K.JOIN_DIR, 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects', 'D:/SIDE-bijection', 'D:/SIDE-interfaces', 'D:/SIDE-li-map',
                                                 'D:/SIDE-kernel') if r not in P.REPOS and os.path.isdir(r))
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b719'))
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
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b719')
    # ### (R329)(2), the item repair: THE WHOLE ANSWER. b682's cut ends at the first "END" after the needle (`best.find('END', k)`, :221), which a
    # ### word carrying END (AMENDMENT, APPENDED, RECOMMENDED) ends inside: b718's answers read 468 characters. The cut now ends at the answer's
    # ### last END (`best.rfind('END')`), the paste's own tail; the substitution printed, the route refusing where it does not apply.
    if body.count("best.find('END', k)") != 1:
        sys.exit('### b682`s CUT NOT FOUND ONCE IN ITS answer -- NOTHING CHECKED')
    body = body.replace("best.find('END', k)", "best.rfind('END')")
    body = body.replace("    open(q + '.tmp', 'wb')", "    MEM.guard('b719', os.path.basename(q), ROOT_EXCLUDE)\n    open(q + '.tmp', 'wb')")
    ns = dict(vars(P))
    ns.update(MEM=MEM, ROOT_EXCLUDE=_root_exclude())
    exec(compile(body, 'b682_citation.answer (b719)', 'exec'), ns)
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
        print('usage: b719_citation.py check [dry] | ferry | answer <needle> | word <needle> | replay <needle> <session id> <anchor>')
        sys.exit(2)
    fn(*sys.argv[2:])
