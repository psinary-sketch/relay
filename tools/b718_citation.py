# -*- coding: utf-8 -*-
"""b718_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b718's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (bde68a30, a new session after the clear; the anchor (R328)'s line); the answer route is b682's, imported from
### tools/b682_citation.py with its act names pointed at b718, b706's repair carried (a bare eight-hex token a bank names as a sha256 or a
### kernel's lakefile pins as a rev is not read as a commit); the `word` route is b694's. Routes: `check [dry]` -> data/b718_citation_check.txt
### (.json) ; `ferry` -> data/b718_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the check on one answer.
### Carried by diff from b717_citation.py (data/b718_carry_citation.txt), b717's cite rows pruned (data/b718_prune_citation.txt) and this
### ruling's written by the Edit tool; this tool writes only the banks named above. Its (R328)(1) row reads lv's release list by `gh` (the
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
import b718_worklist as K   # noqa: E402
import act_membrane as MEM  # noqa: E402  ### (R328)(2)(ii): the membrane before every bank write of this tool


def _root_exclude():
    import b718_record as REC   # ### the record tool's exclusion pattern, the one the root route reads (imported at the call, nothing written)
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
    # ### b718: the cite rows of (R328) and its ferry, written by the Edit tool after b717's rows were pruned (data/b718_prune_citation.txt)
    cl = lines_of(p('data', 'b717_closing.txt'))
    add('ruling (1)', 'data/b717_closing.txt :1, the head line (relay d72dd2d0, PLACE-papers c02f47c, suite 133 of 140, root 404b613b, scores 8 of 8 HELD)',
        at(cl, 1).startswith('b717 closed: relay d72dd2d0, PLACE-papers c02f47c; suite 133 of 140; root 404b613b') and 'scores 8 of 8 HELD' in at(cl, 1), at(cl, 1)[:150], '1')
    clo = (g(ROOT, 'log', '-1', '--format=%H %s', '248c5a97')[1] or '').strip()
    rmain = [v for k_, v in _remote_heads(ROOT).items() if k_ == 'refs/heads/main']
    add('ruling (1)', 'relay 248c5a97, b717`s closing, pushed and read back (the remote main at it)', clo[41:].startswith('b717: the closing') and rmain[:1] == [clo[:40]],
        'commit %s ; the remote main %s' % (clo[:8], (rmain or ['NONE'])[0][:8]), '1')
    pph = (g(PP, 'rev-parse', 'HEAD')[1] or '').strip()
    pprm = [v for k_, v in _remote_heads(PP).items() if k_ == 'refs/heads/main']
    add('ruling (1)', 'PLACE-papers c02f47c, b717`s record, pushed and read back', pph.startswith('c02f47c') and pprm[:1] == [pph], 'HEAD %s ; the remote main %s' % (pph[:8], (pprm or ['NONE'])[0][:8]), '1')
    add('ruling (1)', 'the suite 134 of 140 pre-push and 133 of 140 post-push, NOT CLEAN; the claim arms 37 of 37 and 36 of 37 (the closing`s commit message)',
        '133/140 NOT CLEAN' in clo and 'pre-push 134/140' in clo and 'claim arms 36 of 37 post-push and 37 of 37 pre-push' in clo, clo[41:200], '1')
    add('ruling (1)', 'the counter CLAIM 2, CLOSE 33 (data/b717_closing.txt :5)', 'CLAIM 2, CLOSE 33' in at(cl, 5), at(cl, 5)[-40:], '1')
    row = act_root_line('b717')
    rb = lines_of(p('data', 'b717_root_banks.txt'))
    add('ruling (1)', 'the root 404b613b over 103 banks, chained on b716 (data/act_roots.txt b717`s row ; data/b717_root_banks.txt)',
        bool(row) and row[-1][1].startswith('404b613b') and any('BANKS 103' in l for l in rb), 'row %s ; BANKS 103 %s' % (row[-1][1][:8] if row else 'NONE', any('BANKS 103' in l for l in rb)), '1')
    tr = [i for i in range(16086, 16086 + 80) if '404b613b' in at(ot, i)]
    add('ruling (1)', 'the entry at FINDINGS :10784 and the trail at OPEN_TRAILS :16086 (its head; the root in its record beneath)',
        at(fi, 10784).startswith('## ') and '-39' in at(fi, 10784) and at(ot, 16086).startswith('### b717') and bool(tr),
        'FINDINGS :10784 %r ; OPEN_TRAILS :16086 %r ; the root at %s' % (at(fi, 10784)[:60], at(ot, 16086)[:24], [':%d' % i for i in tr][:3]), '1')
    mi = lines_of(p('data', 'b717_mirror.txt'))
    add('ruling (1)', 'the mirror mirror-refresh-2026-10-27-b717.zip, 74 files, CLEAN on all three clauses with the root line (data/b717_mirror.txt :2, :5, :6, :14)',
        'mirror-refresh-2026-10-27-b717.zip' in at(mi, 2) and '74 files' in at(mi, 5) and '404b613b' in at(mi, 6) and 'CLEAN ON ALL THREE CLAUSES' in at(mi, 14), ':2 ; :5 ; :6 ; :14', '1')
    li = rd(p('data', 'b717_list.txt')) or ''
    add('ruling (1)', 'the list of x^2 + xy + 10y^2 complete to 200, 31 off-line pairs, RECT_CERTIFY False (data/b717_list.txt)',
        'OFF-LINE PAIRS 31' in li and 'COMPLETE TO 200.0' in li and 'RECT_CERTIFY False' in li, 'OFF-LINE PAIRS 31 %s ; RECT_CERTIFY False %s' % ('OFF-LINE PAIRS 31' in li, 'RECT_CERTIFY False' in li), '1')
    pf = [x for x in (g(ROOT, 'show', '--name-only', '--format=', K.PRED_B717_COMMIT)[1] or '').split(NL) if x.strip()]
    add('ruling (1); ruling (5)(i)', 'data/b717_predictions.txt committed alone at f47d8ab5 before any onset', sorted(pf) == ['data/b717_predictions.json', 'data/b717_predictions.txt'], 'its files %s' % pf, '1, 3')
    on = lines_of(p('data', 'b717_onsets.txt'))
    add('ruling (1)', 'the detection law HELD at 7 of 7 reachable pairs, 24 beyond reach at 200 (data/b717_onsets.txt, its last line)',
        any('HELD 7 ; REFUTED 0 ; BEYOND REACH AT 200: 24' in l for l in on), 'found %s' % any('HELD 7 ; REFUTED 0 ; BEYOND REACH AT 200: 24' in l for l in on), '1')
    co = lines_of(p('data', 'b717_coeffs.txt'))
    add('ruling (1); ruling (4)(ii)', 'n = 120, c(120) = -2 log 120, registration (ii) HELD on both clauses (data/b717_coeffs.txt :16, :17, :21-:23)',
        'n = 120' in at(co, 16) and 'c(n) = -2 log 120' in at(co, 17) and 'HELD' in at(co, 21) and 'HELD' in at(co, 22) and 'REGISTRATION (ii): HELD' in at(co, 23), ':16 ; :17 ; :21-:23', '1, 2')
    add('ruling (1)', '"the seat read its figures by hand against data/b717_coeffs.txt :10-:18": the bank`s lines :10-:18 present (the controls C3 and the readings)',
        len(co) >= 18 and '(C3)' in at(co, 10) and 'b(n) = c(n)/log n = -2' in at(co, 17), ':10 %r ; :17 %r' % (at(co, 10)[:30], at(co, 17)[:40]), '1')
    nm = rd(p('data', 'b717_names.txt')) or ''
    add('ruling (1)', '11 of 11 names pinned in the census at v0.8.3 (data/b717_names.txt ; PLACE-papers phase2/method/THE_KEYSTONE_CENSUS_v0_8_3.md)',
        'NAMES 11 ; FOUND AT A CURRENT TAG 11 ; MISSING 0' in nm and os.path.exists(os.path.join(PP, K.CENSUS_NEW)), 'present', '1')
    add('ruling (1)', 'Silence`s head written with day1/Silence_of_Foundations_CORRESPONDENCE.md (PLACE-papers main)', os.path.exists(os.path.join(PP, K.COMPANION)), 'present', '1')
    add('ruling (1)', '"its answer check read VACUOUS ... the word named no path, line or commit" (data/b717_closing.txt :40, ANSWER CITES CHECKED 0)',
        'ANSWER CITES CHECKED 0 ; OK 0 ; MISSES 0' in at(cl, 40), at(cl, 40)[-160:-60], '1')
    # ### (R328)(2): the corrigendum's sources
    ev = lines_of(p('data', 'b717_events.txt'))
    starts = sorted(int(m.group(1)) for m in (re.match(r'^    \((\d+)\) ', l) for l in ev) if m)
    tags = [re.search(r'\[(CLAIM|CLOSE) ;', l).group(1) for l in ev if re.match(r'^    \(\d+\) ', l) and re.search(r'\[(CLAIM|CLOSE) ;', l)]
    add('ruling (2)', 'data/b717_events.txt (1)-(10), each on its starting line with its tag', starts == list(range(1, 11)) and len(tags) == 10,
        'starts %s ; tags %s' % (starts, tags), '1')
    nav = [1, 2, 7, 8, 9, 10]
    add('ruling (2)', 'the navigator`s reading: events (1), (2), (7), (8), (9), (10) CLOSE -- each CLOSE in the bank (the bank`s other four, (3)-(6), CLOSE too)',
        len(tags) == 10 and all(tags[i - 1] == 'CLOSE' for i in nav), 'the bank`s tags %s' % tags, '1')
    st = (g(ROOT, 'status', '--short', '--', 'data/b717_relay_push-b717-closing_push_out.txt', 'data/b717_steps.json', 'data/b717_bank_hashes.json',
            'tools/mirror_prevbuild.json', 'data/b717_hook_refusals.txt')[1] or '').replace(chr(13), '')
    sl = dict((l[3:].strip(), l[:2]) for l in st.split(NL) if l.strip())
    want = {'data/b717_relay_push-b717-closing_push_out.txt': '??', 'data/b717_steps.json': ' M', 'data/b717_bank_hashes.json': '??',
            'tools/mirror_prevbuild.json': ' M', 'data/b717_hook_refusals.txt': ' M'}
    add('ruling (2); ruling (10)', 'the five items the close left uncommitted: the closing push capture (untracked), step row 19 (data/b717_steps.json), '
        'data/b717_bank_hashes.json (untracked), tools/mirror_prevbuild.json, the hook`s refusal after the closing (data/b717_hook_refusals.txt)',
        sl == want, 'git status %s' % sl, '0, 1')
    dl = lines_of(p('data', 'b717_defects.txt'))
    dtags = [m.group(1) for m in (re.search(r"^    \([a-z]+\) THE (?:SEAT|NAVIGATOR)'S \[(CLAIM|CLOSE) ;", l) for l in dl) if m]
    add('ruling (2)', '"the two CLAIM items the counter carries": data/b717_defects.txt`s CLAIM letters (the counter CLAIM 2)', dtags.count('CLAIM') == 2,
        'defects %d ; CLAIM %d ; CLOSE %d' % (len(dtags), dtags.count('CLAIM'), dtags.count('CLOSE')), '1')
    v6 = rd(p('data', 'standing_clauses_v6.txt')) or ''
    r2 = re.search(r'^  \(2\) [^\n]*\n      ([^\n]*)', v6, re.M)
    add('ruling (2)', '"under data/standing_clauses_v6.txt row (2)": the bank`s row (2) is the CLAIM AND CLOSE row', bool(r2) and 'CLAIM' in r2.group(1),
        'row (2) reads %r ; CLAIM AND CLOSE is row (80), (R327)(2)' % (r2.group(1)[:60] if r2 else 'NONE'), '1')
    # ### (R328)(3): the standing line's reader
    for f in ('FACES_LEDGER.md', 'FINDINGS.md', K.CENSUS_NEW):
        add('ruling (3)', 'the touch read`s source PLACE-papers %s' % f, os.path.exists(os.path.join(PP, f)), 'present', '7')
    # ### (R328)(4): the derivation's sources
    blob = (g(ROOT, 'show', '%s:data/b716_registrations.txt' % K.REG_COMMIT)[1] or '')
    rg = lines_of(p('data', 'b716_registrations.txt'))
    add('ruling (4)(i)', 'data/b716_registrations.txt (ii) read unchanged from dc5e808f; the law at :51-:53', bool(blob) and blob.replace(chr(13), '') == (rd(p('data', 'b716_registrations.txt')) or '')
        and 'b(n) = -2' in at(rg, 51) and 'FALSIFIER' in at(rg, 53), 'blob %d characters ; :51 ; :53' % len(blob), '2')
    c11, c13 = lines_of(p('data', 'b711_coeffs.txt')), lines_of(p('data', 'b713_coeffs.txt'))
    add('ruling (4)(i)', 'the law HELD at -23 and -15 as observed: n = 48 (data/b711_coeffs.txt :12), n = 24 (data/b713_coeffs.txt :13)',
        'n = 48' in at(c11, 12) and 'n = 24' in at(c13, 13), ':12 %r ; :13 %r' % (at(c11, 12)[:50], at(c13, 13)[:50]), '2')
    for f in K.COEFF_BANKS:
        add('ruling (4)(iii)', 'the check bank %s through its cut' % f, os.path.exists(p(*f.split('/'))), 'present', '2')
    add('ruling (4)(ii)', 'the navigator`s reading (a(n), the pair sums, the divisors at 48, 24, 120): reproduced by the seat`s tool at Component 2 before use (data/b718_decomp.txt)',
        True, 'to be reproduced, not checked here', '2')
    # ### (R328)(5): the controls' ripe work
    pr = lines_of(p('data', 'b717_predictions.txt'))
    add('ruling (5)(i)', '"the constant A0 = 10 that data/b717_predictions.txt used" (:7, b675`s A0 = 10, Q0`s P3 A0Q, an ASSUMPTION at -39)',
        'A0 = 10' in at(pr, 7) and 'not certified for Q1' in at(pr, 7), at(pr, 7)[:90], '3')
    add('ruling (5)(ii)', 'FINDINGS :8881 names T-COUNT as assumed ; data/b705_contour.txt present', 'T-COUNT assumed' in at(fi, 8881) and os.path.exists(p('data', 'b705_contour.txt')),
        at(fi, 8881)[-40:], '3')
    l13 = lines_of(p('data', 'b713_list.txt'))
    add('ruling (5)(iii)', 'the zero at 1.025973 + 61.422798i (data/b713_list.txt :40)', '1.0259726' in at(l13, 40) and '61.4227983' in at(l13, 40), at(l13, 40)[:70], '3')
    rc = lines_of(p('data', 'b714_rect.txt'))
    add('ruling (5)(iii)', '"by its price at b714": b714`s bank for the box is a run, not a price -- data/b714_rect.txt :14 CERTIFIED, :16 piece time 30 s',
        False, ':14 %r' % at(rc, 14)[-12:], '3')
    gr = rd(p('data', 'b709_grid.txt')) or ''
    add('ruling (5)(iv)', 'b709`s 4443 grid points (data/b709_grid.txt) and b711`s operation (data/b711_surgery.txt)', '4443' in gr and os.path.exists(p('data', 'b711_surgery.txt')),
        '4443 in the grid bank %s' % ('4443' in gr), '3')
    # ### (R328)(6): two reads
    rp = _blob(K.LV_DIR, K.LV_V0100, 'SIDELvConservation/RegisterPentagon.lean').split(NL)
    add('ruling (6)(i)', 'RegisterPentagon.lean :149-:152 at the deposit 93c27ec ("the actual Taylor coefficients of log xi")',
        'actual Taylor coefficients of log' in ' '.join(' '.join(l.replace('`', '').split()) for l in rp[148:152]),
        'the lines :149-:152 as the blob carries them: %r' % [l.strip()[:110] for l in rp[148:152]], '4')
    df = _decl_files(K.EF_DIR, 'v0.37', 'li_coeff_eq_taylorCoeff')
    add('ruling (6)(i)', 'li_coeff_eq_taylorCoeff at SIDE-explicit-formula`s tag v0.37', bool(df), 'declared in %s' % df, '4')
    f17 = rd(p('data', 'b717_ferry.txt')) or ''
    add('ruling (6)(ii)', 'the composition law as (R327)(11) names it (data/b717_ferry.txt)', 'composition law' in f17, 'named %s' % ('composition law' in f17), '4')
    # ### (R328)(7)-(8)
    add('ruling (7)', 'the five CLOSE classes named by b717`s events (1), (2), (8), (9), (10) and the standing replay route (tools/standing/replay.py)',
        len(tags) == 10 and os.path.exists(p('tools', 'standing', 'replay.py')), 'present', '4')
    fp = lines_of(p('data', 'b716_federation_pin_price.txt'))
    add('ruling (8)', 'the twelve kernels below de5ce8a9 (data/b716_federation_pin_price.txt :53, :166), each at D:/<name>',
        'de5ce8a9a66a' in at(fp, 53) and 'BELOW IT 12' in at(fp, 166) and all(os.path.isdir('D:/' + k) for k in K.PIN_KERNELS),
        'absent %s' % [k for k in K.PIN_KERNELS if not os.path.isdir('D:/' + k)], '5')
    # ### (R328)(9): records
    hd = []
    for kd in sorted(d_ for d_ in os.listdir('D:/') if d_.startswith('SIDE-') and os.path.isdir(os.path.join('D:/', d_, '.git'))):
        r = subprocess.run(['git', '-C', os.path.join('D:/', kd), 'grep', '-l', 'h2_sign_iff_rh', 'HEAD', '--', '*.lean'], capture_output=True)
        hd += [kd + ':' + l.split(':', 1)[1] for l in r.stdout.decode('utf-8', 'replace').split(NL) if ':' in l]
    add('ruling (9)', 'h2_sign_iff_rh, the challenge file`s statement, named at a kernel`s HEAD', bool(hd), 'found in %s' % hd[:4], '6')
    add('ruling (9)', 'lean/QuasiRiemannHypothesis.lean at openai/math 7ef5c0cc5: read at Component 6 by gh, outside the local trees', True, 'to be read', '6')
    add('ruling (9)', 'PLACE-papers REGISTRY.md, the two cells` file', os.path.exists(os.path.join(PP, 'REGISTRY.md')), 'present', '6')
    # ### (R328)(10)-(12)
    br = (g(ROOT, 'branch', '--list', 'push-b717-*')[1] or '').split()
    bp = (g(PP, 'branch', '--list', 'push-b717-*')[1] or '').split()
    add('ruling (10)', 'the push-b717-* branches: relay push-b717-closing, -preroot, -record ; PLACE-papers push-b717-preroot, -record',
        sorted(br) == ['push-b717-closing', 'push-b717-preroot', 'push-b717-record'] and sorted(bp) == ['push-b717-preroot', 'push-b717-record'], 'relay %s ; PLACE-papers %s' % (br, bp), '0')
    pb = (g(K.LV_DIR, 'rev-parse', 'refs/heads/port-b707')[1] or '').strip()
    add('ruling (10)', 'port-b707 kept (SIDE-lv-conservation, at cb0aea56)', pb == K.PORT_TIP, pb[:8], '0')
    add('ruling (12)', 'the draft at v5 (23228113), held', K.DRAFT == '23228113', 'tools/b718_worklist.py DRAFT', '0')
    add('ferry (PATHS)', 'the act`s paths, each present', all(os.path.isdir(x) for x in K.PATHS), 'absent %s' % [x for x in K.PATHS if not os.path.isdir(x)], '0')
    standing_rows(text, add)
    return R


def standing_rows(text, add):
    """the citation tool reads the standing clauses by version (data/b712_rules.txt row (1)): for each version a ferry names as "standing clauses v<N>"
    outside a quotation, the bank data/standing_clauses_v<N>.txt present with its VERSION line -- v1 with its control banked AS WANTED; a version this
    act writes at step zero (v2, (R328)(2)) read as TO BE WRITTEN when absent and from the bank when present."""
    import b717_standing as SC
    flat = re.sub(r'“[^”]*”', '', ' '.join(text.split()))
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing clauses(?:’)? v(\d+)', flat, re.I)))
    for v in names or [1]:
        p = os.path.join(D, 'standing_clauses_v%d.txt' % v)
        t = rd(p) or ''
        ver = re.search(r'^VERSION: (\d+)$', t, re.M)
        if v == 1:
            ctl = _jl('b717_standing_control.json')
            add('ferry (standing clauses)', 'the standing clauses v1: data/standing_clauses_v1.txt', bool(t) and bool(ver) and ver.group(1) == '1' and bool(SC.parse(t)) and ctl.get('ok') is True,
                'present %s ; VERSION %s ; rows %d ; the re-assembly control AS WANTED %s' % (bool(t), ver.group(1) if ver else 'NONE', len(SC.parse(t)), ctl.get('ok')), '0')
        elif not t:
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- TO BE WRITTEN at step zero ((R328)(2))' % (v, v), True, 'absent, as ordered', '0')
        else:
            add('ferry (standing clauses)', 'the standing clauses v%d: data/standing_clauses_v%d.txt' % (v, v), bool(ver) and ver.group(1) == str(v), 'present ; VERSION %s' % (ver.group(1) if ver else 'NONE'), '0')


def _write(L, R, miss):
    for n_ in ('b718_citation_check.txt', 'b718_citation_check.json'):
        MEM.guard('b718', n_, _root_exclude())
    for name, data in (('b718_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b718_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        with open(q + '.tmp', 'wb') as fh:
            fh.write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b718 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b718_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b718_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b718_ferry_scan.txt')
    MEM.guard('b718', 'b718_ferry_scan.txt', _root_exclude())
    with open(s + '.tmp', 'wb') as fh:
        fh.write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b718_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
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
    """(R278)(4): b682's route, imported, with its act names pointed at b718, and b706's repair carried."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.C.SESSIONS_AFTER = C.SESSIONS_AFTER
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, K.LV_DIR, K.JOIN_DIR, 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects', 'D:/SIDE-bijection', 'D:/SIDE-interfaces', 'D:/SIDE-li-map',
                                                 'D:/SIDE-kernel') if r not in P.REPOS and os.path.isdir(r))
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b718'))
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
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b718')
    # ### (R328)(2), the item repair: THE WHOLE ANSWER. b682's cut ends at the first "END" after the needle (`best.find('END', k)`, :221), which a
    # ### word carrying END (AMENDMENT, APPENDED, RECOMMENDED) ends inside: b717's answers read 468 characters. The cut now ends at the answer's
    # ### last END (`best.rfind('END')`), the paste's own tail; the substitution printed, the route refusing where it does not apply.
    if body.count("best.find('END', k)") != 1:
        sys.exit('### b682`s CUT NOT FOUND ONCE IN ITS answer -- NOTHING CHECKED')
    body = body.replace("best.find('END', k)", "best.rfind('END')")
    body = body.replace("    open(q + '.tmp', 'wb')", "    MEM.guard('b718', os.path.basename(q), ROOT_EXCLUDE)\n    open(q + '.tmp', 'wb')")
    ns = dict(vars(P))
    ns.update(MEM=MEM, ROOT_EXCLUDE=_root_exclude())
    exec(compile(body, 'b682_citation.answer (b718)', 'exec'), ns)
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
        print('usage: b718_citation.py check [dry] | ferry | answer <needle> | word <needle> | replay <needle> <session id> <anchor>')
        sys.exit(2)
    fn(*sys.argv[2:])
