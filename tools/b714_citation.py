# -*- coding: utf-8 -*-
"""b714_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b714's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (3bbc6267, the same session as b713; the anchor (R324)'s line); the answer route is b682's, imported from
### tools/b682_citation.py with its act names pointed at b714, b706's repair carried (a bare eight-hex token a bank names as a sha256 or a
### kernel's lakefile pins as a rev is not read as a commit); the `word` route is b694's. Routes: `check [dry]` -> data/b714_citation_check.txt
### (.json) ; `ferry` -> data/b714_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the check on one answer.
### Carried by diff from b713_citation.py (data/b714_carry_citation.txt), b713's cite rows pruned (data/b714_prune_citation.txt) and this
### ruling's written by the Edit tool; this tool writes only the banks named above. Its (R324)(2) and (3)(i) rows read GitHub's repository
### listing and lv's release list by `gh` (the seat's own authenticated client, no identifier of the author in any argument). A kernel's file at a tag is read here by `git cat-file` and `git grep` inside this
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
import b714_worklist as K   # noqa: E402
import act_membrane as MEM  # noqa: E402  ### (R324)(2)(ii): the membrane before every bank write of this tool


def _root_exclude():
    import b714_record as REC   # ### the record tool's exclusion pattern, the one the root route reads (imported at the call, nothing written)
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
    # ### b714: the cite rows of (R324) and its ferry, written by the Edit tool after b713's rows were pruned (data/b714_prune_citation.txt)
    for f in ('data/b713_closing.txt', 'data/b713_defects.txt', 'data/b713_events.txt', 'data/standing_clauses_v4.txt', 'data/b713_predictions.txt',
              'tools/b713_predict.py', 'data/b713_onsets.txt', 'data/b710_registrations.txt', 'data/b711_pairs.txt', 'data/b713_list.json',
              'tools/b667_epstein_certify.py', 'data/b713_recut_additive.txt', 'data/b713_list.txt', 'data/b713_coeffs.txt', 'data/b713_source_pin.txt',
              'data/b713_report.txt', 'data/b713_scores_close.json', 'data/b713_checks.txt', 'data/b713_checks_postpush.txt', 'data/b713_mirror.txt',
              'data/b713_steps.json', 'data/b713_corrigendum.json', 'data/b713_root_banks_dry.json', 'data/b711_coeffs.txt', 'data/b709_pairs.txt',
              'data/b675_corrigenda.txt', 'data/act_roots.txt', 'tools/b713_checks.py', 'tools/b713_closing.py', 'tools/b713_record.py',
              'tools/b713_corrigendum.py', 'tools/act_close.py', 'tools/push_gated.sh', 'tools/b706_standing_figures.py', 'tools/circuit_read.py',
              'tools/mirror_prevbuild.json', 'tools/act_root.py', 'tools/act_membrane.py', 'tools/ferry_scan.py'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0')
    # ### (R324)(1): b713 at its weight
    cl = lines_of(p('data', 'b713_closing.txt'))
    q = _quote(text, 'b713 closed: relay', '”; its relay commit')
    add('ruling (1)', 'data/b713_closing.txt :1, the head line, against (R324)(1)`s quote', bool(q) and q == cl[0], 'quote %d characters, the line %d ; equal byte for byte %s' % (len(q), len(cl[0]), q == cl[0]), '0-1')
    clo = (g(ROOT, 'log', '-1', '--format=%H %s', '2f76d11c')[1] or '').strip()
    add('ruling (1)', 'the closing`s commit 2f76d11c (b713: the closing)', clo.startswith('2f76d11c') and 'b713: the closing' in clo, clo[:60], '0-1')
    ll = lines_of(p('data', 'b713_list.txt'))
    add('ruling (1)', 'the -15 list complete to 199.33082 in 14 bands, 169 on-line, 37 off-line pairs (data/b713_list.txt :74)',
        'COMPLETE TO 199.33082 ; BANDS 14 (COMPLETE 14) ; ON-LINE ZEROS 169 ; OFF-LINE PAIRS 37' in at(ll, 74), ':74 %r' % at(ll, 74)[:90], '1')
    pst = (g(ROOT, 'show', '--format=', '--name-only', K.B713_PRED_RELAY)[1] or '').split()
    anc = subprocess.run(['git', '-C', ROOT, 'merge-base', '--is-ancestor', K.B713_PRED_RELAY, K.B713_ONSETS_RELAY]).returncode == 0
    add('ruling (1); ruling (7)', 'data/b713_predictions.txt committed alone at be4db146, an ancestor of 9816b87d', sorted(pst) == ['data/b713_predictions.json', 'data/b713_predictions.txt'] and anc,
        'be4db146 files %s ; ancestor of 9816b87d %s' % (pst, anc), '1')
    on = lines_of(p('data', 'b713_onsets.txt'))
    rat = [float(m.group(1)) for l in on[11:19] for m in [re.search(r'ratio ([0-9.]+) \| HELD', l)] if m]
    add('ruling (1)', 'the law met at 8 of 8, ratios 1.000055 to 1.000885 (data/b713_onsets.txt :12-:19)', len(rat) == 8 and min(rat) == 1.000055 and max(rat) == 1.000885,
        'HELD rows %d ; ratios %s to %s' % (len(rat), min(rat) if rat else None, max(rat) if rat else None), '1')
    add('ruling (1)', '29 pairs beyond reach, owed no prediction (:20-:48; the author`s word, events (9))', sum(1 for l in on[19:48] if 'BEYOND REACH' in l and 'not computed' in l) == 29
        and 'PAIRS COMPUTED 8 ; HELD 8 ; REFUTED 0 ; BEYOND REACH 29' in at(on, 50), ':50 %r' % at(on, 50)[:70], '1')
    bp1 = lines_of(p('data', 'b711_pairs.txt'))
    add('ruling (1)', 'Q0`s pairs 11 and 15 met at b711, ratios 0.998460 and 0.998079, window [0.9, 1.1] (data/b711_pairs.txt :12-:13)',
        'n*/F2 0.998460' in at(bp1, 12) and 'WITHIN' in at(bp1, 12) and 'n*/F2 0.998079' in at(bp1, 13) and 'WITHIN' in at(bp1, 13) and 'window [0.9, 1.1]' in at(bp1, 4), ':12 ; :13 ; :4', '1')
    co = lines_of(p('data', 'b713_coeffs.txt'))
    rpt = lines_of(p('data', 'b713_report.txt'))
    add('ruling (1)', 'c(n) negative from n = 24, c(24) = -2 log 24, 90 through 3000 equal to the navigator`s value, 756 through 32532 (data/b713_coeffs.txt :13, :18; data/b713_report.txt :20)',
        'n = 24 ; c(24) = (-6) log 2 + (-2) log 3' in at(co, 13) and 'NEGATIVE FROM n = 24' in at(co, 18) and 'NEGATIVE COEFFICIENTS 756 THROUGH 32532' in at(co, 18)
        and '-2 log 24' in at(rpt, 20) and '90 beside 90 -- EQUAL' in at(rpt, 20), ':13 ; :18 ; report :20', '1')
    lj = _jl('b713_list.json')
    # ### the json's own shape: the off-line rows at its top level (`offline`, 37) and `re_over_1`; the dry form read rows under `bands` and
    # ### found none, a vacuous pass -- widened before the bank (both yields printed)
    offl = (lj.get('offline') or []) if isinstance(lj, dict) else []
    p7 = [r_ for r_ in offl if isinstance(r_, dict) and str(r_.get('re', '')).startswith('1.0259726')]
    ro1 = (lj.get('re_over_1') or []) if isinstance(lj, dict) else []
    add('ruling (1); ruling (9)', 'pair 7: Re rho 1.025973 at 61.422798, located by Newton at 200 bits, certified False (data/b713_list.json `offline` and `re_over_1`; data/b713_list.txt :22)',
        "('1.0259726162', '61.422798308')" in at(ll, 22) and len(p7) == 1 and p7[0].get('certified') is False and str(p7[0].get('im', '')).startswith('61.4227983')
        and 'Newton on point values at 200 bits' in p7[0].get('located', '') and len(ro1) == 1 and ro1[0] == p7[0],
        ':22 ; offline rows %d, with Re 1.0259726 %d, certified %s ; re_over_1 rows %d (the dry form`s `bands` matcher read 0)' % (
            len(offl), len(p7), [r_.get('certified') for r_ in p7], len(ro1)), '1')
    q0c = lines_of(p('data', 'b711_coeffs.txt'))
    add('ruling (1)', 'Q0 with no zero of Re rho > 1 in its list to 325.0 (data/b711_coeffs.txt :15)', 'NONE IN THE LIST TO 325.0' in at(q0c, 15), ':15 %r' % at(q0c, 15).strip()[:70], '1')
    spn = lines_of(p('data', 'b713_source_pin.txt'))
    add('ruling (1)', 'the genus factorization pinned at Murty-Osburn arXiv:math/0412237v1, Theorem 2.3, AGREES (data/b713_source_pin.txt :47)',
        'AGREES' in at(spn, 47) and 'math/0412237v1' in ' '.join(spn) and 'Theorem 2.3' in ' '.join(spn), ':47 %r' % at(spn, 47).strip()[:40], '1')
    fl_ = lines_of(os.path.join(PP, 'FACES_LEDGER.md'))
    fh = (g(PP, 'log', '--format=%h', '503f1ce', '-1', '--', 'FACES_LEDGER.md')[1] or '').strip()
    add('ruling (1)', 'FACES_LEDGER.md :8 restated (PLACE-papers 503f1ce touching the ledger)', fh.startswith('503f1ce'), 'log %r' % fh, '1')
    rh = _remote_heads(PP)
    rmerged = subprocess.run(['git', '-C', PP, 'merge-base', '--is-ancestor', K.RECUT_TIP, 'main']).returncode == 0
    ra = lines_of(p('data', 'b713_recut_additive.txt'))
    add('ruling (1); ruling (3)(ii)', 'the re-cut`s additive check 22 of 22 on recut-b712-silence 0aeca834, pushed and not merged (data/b713_recut_additive.txt :67)',
        'ORIGINAL LINES 22 (BLANK 12 NOT SEARCHED) ; FOUND 22 ; MISSING 0 ; IN ORDER True' in at(ra, 67),
        'the bank %d lines ; remote head %s ; merged into main %s' % (len(ra), (rh.get('refs/heads/' + K.RECUT_BRANCH) or 'ABSENT')[:8], rmerged), '1')
    add('ruling (1); ruling (3)(ii)', 'recut-b712-silence at 0aeca834 at the remote and locally, not merged into main', rh.get('refs/heads/' + K.RECUT_BRANCH) == K.RECUT_TIP
        and (g(PP, 'rev-parse', K.RECUT_BRANCH)[1] or '').strip() == K.RECUT_TIP and not rmerged, 'remote %s ; local %s ; merged %s' % (
            (rh.get('refs/heads/' + K.RECUT_BRANCH) or '')[:8], (g(PP, 'rev-parse', K.RECUT_BRANCH)[1] or '').strip()[:8], rmerged), '1-2')
    add('ruling (1)', 'the entry at FINDINGS :10440', at(fi, 10440).startswith('## The −15 control'), ':10440 %r' % at(fi, 10440)[:50], '1')
    add('ruling (1)', 'the trail at OPEN_TRAILS :15928', at(ot, 15928).startswith('### b713'), ':15928 %r' % at(ot, 15928)[:40], '1')
    row = act_root_line('b713')
    add('ruling (1); ruling (6)(ii)', 'the root d613bce6 over 114 banks chained from fa19697b (data/act_roots.txt, the 90th chain row)', bool(row) and row[0][1].startswith('d613bce6') and row[0][2].startswith('fa19697b'),
        'row b713 %s' % ([x[:8] for x in row[0][1:3]] if row else 'NONE'), '1')
    scc = _jl('b713_scores_close.json')
    verd = dict((k, (v[0] if isinstance(v, list) and v else v)) for k, v in scc.items() if re.match(r'^[NS][1-5]$', k))
    add('ruling (1)', 'N1-N5 and S1-S3 HELD at scores close', len(verd) == 8 and all(v == 'HELD' for v in verd.values()),
        'data/b713_scores_close.json verdicts %s' % ' '.join('%s %s' % kv for kv in sorted(verd.items())), '1')
    cpp, cpr = rd(p('data', 'b713_checks_postpush.txt')) or '', rd(p('data', 'b713_checks.txt')) or ''
    add('ruling (1)', 'suite 129 of 140 pre-push and post-push', all('ARMS RUN : 140. ### LIVE PASSING : 129.' in x for x in (cpp, cpr)), 'both banks', '1')
    mr = rd(p('data', 'b713_mirror.txt')) or ''
    add('ruling (1)', 'the mirror mirror-refresh-2026-10-25-b713.zip CLEAN on all three clauses with the root line', 'CLEAN ON ALL THREE CLAUSES' in mr and 'Act root: b713 d613bce6' in mr and os.path.exists(K.MIRROR_ZIP),
        'data/b713_mirror.txt ; the zip exists %s' % os.path.exists(K.MIRROR_ZIP), '1')
    dl = lines_of(p('data', 'b713_defects.txt'))
    dlet = [(m.group(1), m.group(2)) for l in dl for m in [re.match(r'^    \(([a-z])\) (THE [A-Z]+\'S)', l)] if m]
    add('ruling (1)', 'fourteen defects (a)-(n), all the seat`s', ''.join(x[0] for x in dlet) == 'abcdefghijklmn' and all(x[1] == "THE SEAT'S" for x in dlet),
        'letters %s ; owners %s' % (''.join(x[0] for x in dlet), sorted(set(x[1] for x in dlet))), '1')
    ev = lines_of(p('data', 'b713_events.txt'))
    starts = dict((int(m.group(1)), i + 1) for i, l in enumerate(ev) for m in [re.match(r'^\((\d+)\) ', l)] if m)
    add('ruling (1); ruling (5)', 'sixteen events in data/b713_events.txt, (1)-(16) each on its starting line', sorted(starts) == list(range(1, 17)),
        'starting lines %s' % [starts[k] for k in sorted(starts)], '1')
    add('ruling (1); ruling (13)', '"Nothing deposited, nothing published": the draft at v5, held', K.DRAFT == '23228113', 'tools/b714_worklist.py DRAFT', '6')
    # ### (R324)(2): the visibility map against GitHub's own listing, one call (the ruling names the author's listing; the seat reads GitHub's)
    r_ = subprocess.run(['gh', 'repo', 'list', 'psinary-sketch', '--limit', '400', '--json', 'name,visibility'], capture_output=True)
    try:
        vis = dict((x['name'], x['visibility']) for x in json.loads(r_.stdout.decode('utf-8', 'replace') or '[]'))
    except Exception:
        vis = {}
    priv = ('PLACE-papers', 'TECHNE-Core', 'PLACE-phase1.5', 'PLACE-phase2', 'SIDE-carrier-spec', 'SIDE-spinor-calibration-mathlib', 'SIDE-constants', 'glassbead-game')
    pub = ('relay', 'SIDE-faces-join', 'SIDE-lv-conservation', 'SIDE-explicit-formula')
    for n_ in priv:
        add('ruling (2)', 'PRIVATE: %s' % n_, vis.get(n_) == 'PRIVATE', 'GitHub reads %s' % vis.get(n_, 'ABSENT'), '0')
    for n_ in pub:
        add('ruling (2)', 'PUBLIC: %s' % n_, vis.get(n_) == 'PUBLIC', 'GitHub reads %s' % vis.get(n_, 'ABSENT'), '0')
    other = sorted(k for k in vis if k.startswith('SIDE-') and k not in priv + pub)
    add('ruling (2)', 'every other SIDE-* repository PUBLIC (GitHub`s listing, %d repositories)' % len(vis), bool(vis) and all(vis[k] == 'PUBLIC' for k in other),
        'other SIDE-* %d ; not PUBLIC %s' % (len(other), [k for k in other if vis[k] != 'PUBLIC']), '0')
    # ### (R324)(3)(i): the lv tag's objects
    lt = (g(K.LV_DIR, 'tag', '--list', K.LV_TAG)[1] or '').strip()
    lr = g(K.LV_DIR, 'ls-remote', '--tags', 'origin', K.LV_TAG)[1] or ''
    lpe = (g(K.LV_DIR, 'log', '-1', '--format=%h %ci', K.LV_TAG + '^{commit}')[1] or '').strip() if lt else ''
    add('ruling (3)(i)', 'v0.11.0 absent locally and at the remote (to be made at step (3)(i))', not lt and not lr.strip(),
        'local %r (peeled %s) ; remote %r ; the names taken %s' % (lt, lpe, lr.strip()[:40], (g(K.LV_DIR, 'tag', '--list', 'v0.1[1-9].*')[1] or '').split()), '2')
    lh = _remote_heads(K.LV_DIR)
    loc = (g(K.LV_DIR, 'rev-parse', K.PORT_BRANCH)[1] or '').strip()
    add('ruling (3)(i); ruling (11)', 'port-b707 at cb0aea56 locally and at the remote, NOT deleted', loc == K.PORT_TIP and lh.get('refs/heads/port-b707') == K.PORT_TIP,
        'local %s ; remote %s' % (loc[:8], (lh.get('refs/heads/port-b707') or '')[:8]), '0-2')
    lm = (g(K.LV_DIR, 'rev-parse', 'main', 'v0.10.0^{commit}')[1] or '').split()
    add('ruling (3)(i)', 'lv`s main d38f3e8c and the deposit v0.10.0 = 93c27ec', lm == [K.LV_MAIN, K.LV_V0100] and lh.get('refs/heads/main') == K.LV_MAIN,
        'local %s ; remote main %s' % ([x[:8] for x in lm], (lh.get('refs/heads/main') or '')[:8]), '2')
    rl = subprocess.run(['gh', 'release', 'list', '-R', 'psinary-sketch/SIDE-lv-conservation', '--json', 'tagName'], capture_output=True)
    try:
        rels = [x.get('tagName') for x in json.loads(rl.stdout.decode('utf-8', 'replace') or '[]')]
    except Exception:
        rels = None
    add('ruling (3)(i)', 'the release list of SIDE-lv-conservation read, no release for v0.11.0', rels is not None and K.LV_TAG not in rels, 'releases %s' % rels, '2')
    add('ruling (3)(i)', 'W-ORD-LV-PORT-TAG at OPEN_TRAILS :15848', 'W-ORD-LV-PORT-TAG' in at(ot, 15848), ':15848 %r' % at(ot, 15848)[:50], '2')
    ppm = (g(PP, 'rev-parse', 'main')[1] or '').strip()
    add('ruling (3)(ii)', 'PLACE-papers main at e284156 before the merge (b713`s trail)', ppm.startswith(K.PRE_PP), 'main %s' % ppm[:8], '2')
    # ### (R324)(4): the keystone order and the re-cut's opening
    add('ruling (4)', 'W-ORD-KEYSTONE-HEADS at OPEN_TRAILS :15454 and b703`s addition at :15496', 'W-ORD-KEYSTONE-HEADS' in at(ot, 15454) and 'W-ORD-KEYSTONE-HEADS' in at(ot, 15496),
        ':15454 ; :15496', '2')
    sd = _blob(PP, K.RECUT_TIP, K.RECUT_DOC).split(NL)
    add('ruling (4)', 'day1/Silence_of_Foundations.md at the re-cut`s tip 0aeca834 (its opening paragraph to be redrafted)', len(sd) > 20, '%d lines at 0aeca834' % len(sd), '2')
    # ### (R324)(5): the events the corrigendum letters and records, each once
    lettered = [1, 5, 10, 11, 12, 13, 14, 15, 6, 7, 8]
    records = [2, 3, 4, 9, 16]
    add('ruling (5)', 'the eleven lettered events and the five records are the sixteen, once each', sorted(lettered + records) == sorted(starts), 'lettered %s ; records %s' % (lettered, records), '1')
    for n_, needle in ((1, 'read four arms failing on real state'), (5, "G-TOOL-REPAIRS raised TypeError"), (10, 'G-NEXT-ACT-NAMED'), (11, 'G-ACTROOT-BANKED'),
                       (12, 'G-ACTROOT-VERIFY'), (13, '`--combine` was not run before the seal'), (14, 'G-CORRIGENDUM-ENTERED'), (15, 'G-ROOTDRY-READY'),
                       (6, 'THE THROUGHSTONE (b)'), (7, 'THE THROUGHSTONE (e)'), (8, "THE SEAT'S OWN WORDING")):
        add('ruling (5)', 'data/b713_events.txt (%d), the item the ruling names' % n_, needle in ' '.join(ev[starts.get(n_, 0) - 1:starts.get(n_, 0) + 1]) if n_ in starts else False,
            ':%s %r' % (starts.get(n_), at(ev, starts.get(n_, 0)).strip()[:60]), '1')
    bcl = rd(p('data', 'b713_closing.txt')) or ''
    add('ruling (5)', 'the item added here: the closing bank edited by the Edit tool after the seal (its carried item (i))', 'added to the sealed closing`s output by the Edit tool' in bcl,
        'data/b713_closing.txt carries the item %s' % ('added to the sealed closing`s output by the Edit tool' in bcl), '1')
    cg = lines_of(p('data', 'b675_corrigenda.txt'))
    last = [l for l in cg if re.match(r'^\s*\((\d+)\)', l)]
    add('ruling (5)', 'the corrigenda bank, appended only (its last row (33), b712`s record)', bool(last) and re.match(r'^\s*\(33\)', last[-1]) is not None,
        'data/b675_corrigenda.txt, last row %r' % (last[-1][:40] if last else ''), '1')
    # ### (R324)(6): the repairs' objects in b713's tools and banks
    ck = lines_of(p('tools', 'b713_checks.py'))
    add('ruling (6)(ii)', 'the carried figures in tools/b713_checks.py: :1673 `**Next:** b713`, :1657 the 89th row, :1198 a range', "'**Next:** b713'" in at(ck, 1673) and '89th' in at(ck, 1657),
        ':1673 ; :1657', '1')
    add('ruling (6)(ii)', 'b713`s banks read Next b714 (the trail :15960), the chain row 90 (data/act_roots.txt :91 with its one head row)', at(ot, 15960).startswith('**Next:** b714')
        and len([l for l in lines_of(p('data', 'act_roots.txt')) if re.match(r'^b\d+ [0-9a-f]{64} ', l)]) == 90, ':15960 ; chain rows %d' % len(
            [l for l in lines_of(p('data', 'act_roots.txt')) if re.match(r'^b\d+ [0-9a-f]{64} ', l)]), '1')
    add('ruling (6)(iii)', 'b713`s combined pre-run bank absent and its root dry run ready False', not os.path.exists(p('data', 'b713_arms_prerun.txt')) and _jl('b713_root_banks_dry.json').get('ready') is False,
        'arms_prerun exists %s ; dry ready %s' % (os.path.exists(p('data', 'b713_arms_prerun.txt')), _jl('b713_root_banks_dry.json').get('ready')), '1')
    cj = _jl('b713_corrigendum.json')
    lets = [x.get('letter') for x in (cj.get('lettered') or [])]
    add('ruling (6)(v)', 'b713`s corrigendum lettered with U+0027 where its suite reads U+2032', "a'" in lets and 'a′' in rd(p('tools', 'b713_checks.py')), 'letters %s' % lets, '1')
    add('ruling (6)(iv)', 'the seat`s project settings directory D:/.claude (the hook`s settings file to be written there)', os.path.isdir('D:/.claude'), 'D:/.claude exists %s ; settings.json %s' % (
        os.path.isdir('D:/.claude'), os.path.exists('D:/.claude/settings.json')), '0')
    add('ruling (6)(i)', 'b713`s word on (b) and (e) in data/b713_events.txt (9)', "THE AUTHOR'S WORD ON (b) AND (e)" in at(ev, starts.get(9, 0)), ':%s' % starts.get(9), '1')
    # ### (R324)(7)-(9): the law's sources
    r10 = lines_of(p('data', 'b710_registrations.txt'))
    add('ruling (7)', 'b710`s committed predictions 12294837 and 14776940 (data/b710_registrations.txt :34, :36), its (i) at :10',
        'F2 n* = 12294837' in at(r10, 34) and 'F2 n* = 14776940' in at(r10, 36) and at(r10, 10).strip().startswith('(i)'), ':10 ; :34 ; :36', '3')
    add('ruling (7)', 'the -15 tool`s evaluation at Q0: 12275846.6 and 14748496.3 (data/b713_onsets.txt :8, :9)', "n*_pred 12275846.6" in at(on, 8) and "n*_pred 14748496.3" in at(on, 9),
        ':8 ; :9', '3')
    pairs = [(m.group(1), float(m.group(2)), float(m.group(3))) for l in on[7:19] for m in [re.search(r'(pair\s+\d+).*?n\* (\d+).*?n\*_pred ([0-9.]+)', l)] if m]
    res = [round(a - b, 1) for _, a, b in pairs]
    want_ = [59.4, 60.7, 45.1, 44.9, 58.7, 70.3, 65.2, 64.3, 64.8, 137.3]
    add('ruling (8)', 'the navigator`s residuals 45.1 ... 137.3 at -15 and 59.4, 60.7 at Q0, from data/b713_onsets.txt :8-:19 to one decimal', res == want_,
        'read %s' % res, '3')
    ec = rd(p('tools', 'b667_epstein_certify.py')) or ''
    add('ruling (9)', 'tools/b667_epstein_certify.py`s interval routines (python-flint arb/acb; square_count, edge_arg, segment)', 'from flint import arb, acb' in ec and 'def square_count(' in ec and 'def edge_arg(' in ec,
        'present', '3')
    # ### (R324)(10): the Sonin face's sources
    add('ruling (10)', 'FACES_LEDGER.md :21, F2: measured margins and two imported theorems, no kernel declaration named', at(fl_, 21).startswith('| F2 |') and 'MEASURED' in at(fl_, 21) and 'IMPORTED' in at(fl_, 21)
        and '2006.13771v1' in at(fl_, 21) and not re.search(r'`[A-Za-z_]+\.[A-Za-z_.]+`', at(fl_, 21)), ':21', '4')
    add('ruling (10)', 'FACES_LEDGER.md :502, F2 at T3, imported not compiled', at(fl_, 502).startswith('| F2 |') and '**T3**' in at(fl_, 502), ':502', '4')
    h2 = _blob(K.EF_DIR, 'v0.37', 'SIDEExplicitFormula/H2Sign.lean').split(NL)
    add('ruling (10)', 'classK and h2_sign at SIDE-explicit-formula v0.37 (SIDEExplicitFormula/H2Sign.lean :24, :29)', at(h2, 24).startswith('def classK') and at(h2, 29).startswith('def h2_sign'),
        ':24 %r ; :29 %r' % (at(h2, 24)[:30], at(h2, 29)[:30]), '4')
    # ### (R324)(11): the carried files and the branches
    cpo = p('data', 'b713_closing_push_out.txt')
    add('ruling (11)', 'data/b713_closing_push_out.txt -- the name the ruling gives b713`s closing capture', os.path.exists(cpo),
        'absent ; the capture push_gated.sh wrote: data/b713_relay_push-b713-closing_push_out.txt exists %s, tracked %s' % (
            os.path.exists(p('data', 'b713_relay_push-b713-closing_push_out.txt')), bool((g(ROOT, 'ls-files', 'data/b713_relay_push-b713-closing_push_out.txt')[1] or '').strip())), '0')
    st = _jl('b713_steps.json').get('rows', [])
    s23 = st[22:23]
    add('ruling (11)', 'step 23 of data/b713_steps.json, the closing`s row (2f76d11c), uncommitted', len(st) == 23 and bool(s23) and s23[0].get('commit', '').startswith('2f76d11c')
        and s23[0].get('phase') == 'closing' and bool((g(ROOT, 'diff', '--name-only', '--', 'data/b713_steps.json')[1] or '').strip()), 'rows %d ; row 23 %s' % (
            len(st), (s23[0].get('commit', '')[:8], s23[0].get('phase')) if s23 else 'NONE'), '0')
    add('ruling (11)', 'the branch rows of data/b713_closing.txt (carried item (f))', any('push-b713* branches of relay and PLACE-papers' in l for l in cl), 'item (f)', '0')
    for repo, names in K.DELETE:
        lst = g(repo, 'branch', '--merged', 'main')[1] or ''
        for b in names:
            add('ruling (11)', '%s %s (local, listed --merged)' % (os.path.basename(repo), b), b in [x.strip(' *') for x in lst.split(NL)], 'listed by `git branch --merged main` before any delete', '0')
    mi = rd('C:/Users/echo chamber/.claude/projects/D--/memory/MEMORY.md') or ''
    add('ruling (11)', 'the seat`s memory index: its b713 line landed (nothing to restate)', 'b713 latest (closed 2026-10-26' in mi and 'feedback_b713_traps.md' in mi, 'MEMORY.md carries the b713 lines %s' % (
        'b713 latest (closed 2026-10-26' in mi), '0')
    add('ruling (11)', 'the 2,560 MB hold', K.HOLD == 2560, 'tools/b714_worklist.py HOLD', '0')
    # ### (R324)(12): the files this act writes, absent before it
    for f in ('data/standing_clauses_v5.txt', 'data/repo_visibility.txt', 'data/b714_readfirst.txt', 'data/b714_tool_repairs.txt', 'data/b714_heads_draft.txt',
              'data/b714_residual.txt', 'data/b714_sonin_price.txt', 'data/b714_rules.txt', 'data/b715_rules.txt', 'data/b714_author_words.txt',
              'tools/b714_law.py', 'tools/b714_residual.py', 'tools/b714_rect.py', 'D:/.claude/settings.json'):
        add('ruling (12)', '%s -- TO BE WRITTEN by this act' % f, not os.path.exists(f if ':' in f else p(*f.split('/'))), 'absent, as ordered', '0-6')
    add('ruling (12)', 'the READFIRST-CLOSURE reader', os.path.exists(p('tools', 'circuit_read.py')), 'tools/circuit_read.py (readfirst)', '0')
    add('ruling (12)', 'tools/mirror_prevbuild.json, the mirror builder`s state file, named in (W)', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '6')
    add('ferry C5', 'the four standing arms` figures tool and b713`s baselines', os.path.exists(p('tools', 'b706_standing_figures.py')) and os.path.exists(p('data', 'b713_standing_figures.json')),
        'tools/b706_standing_figures.py ; data/b713_standing_figures.json', '5')
    add('ferry C5', 'the chain halves as b693 drew them, b714 added to the second', K.CHAIN_HALVES[1] == ('b659', 'b714'), 'tools/b714_worklist.py CHAIN_HALVES', '5')
    add('ferry read-first', 'OPEN_TRAILS :15948, b713`s open orders', at(ot, 15948).startswith('**The open orders:**'), ':15948', '0')
    add('ruling (14)', 'the next act b715, the registrations act', K.NEXT_ACT == 'b715' and K.NEXT.startswith('b715, the registrations act'), 'tools/b714_worklist.py NEXT', '6')
    add('ferry C0', 'this act`s session transcript (the same session as b713)', os.path.exists(C.SESSION), C.SESSION, '0')
    standing_rows(text, add)
    return R


def standing_rows(text, add):
    """the citation tool reads the standing clauses by version (data/b712_rules.txt row (1)): for each version a ferry names as "standing clauses v<N>"
    outside a quotation, the bank data/standing_clauses_v<N>.txt present with its VERSION line -- v1 with its control banked AS WANTED; a version this
    act writes at step zero (v2, (R324)(2)) read as TO BE WRITTEN when absent and from the bank when present."""
    import b713_standing as SC
    flat = re.sub(r'“[^”]*”', '', ' '.join(text.split()))
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing clauses(?:’)? v(\d+)', flat, re.I)))
    for v in names or [1]:
        p = os.path.join(D, 'standing_clauses_v%d.txt' % v)
        t = rd(p) or ''
        ver = re.search(r'^VERSION: (\d+)$', t, re.M)
        if v == 1:
            ctl = _jl('b713_standing_control.json')
            add('ferry (standing clauses)', 'the standing clauses v1: data/standing_clauses_v1.txt', bool(t) and bool(ver) and ver.group(1) == '1' and bool(SC.parse(t)) and ctl.get('ok') is True,
                'present %s ; VERSION %s ; rows %d ; the re-assembly control AS WANTED %s' % (bool(t), ver.group(1) if ver else 'NONE', len(SC.parse(t)), ctl.get('ok')), '0')
        elif not t:
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- TO BE WRITTEN at step zero ((R324)(2))' % (v, v), True, 'absent, as ordered', '0')
        else:
            add('ferry (standing clauses)', 'the standing clauses v%d: data/standing_clauses_v%d.txt' % (v, v), bool(ver) and ver.group(1) == str(v), 'present ; VERSION %s' % (ver.group(1) if ver else 'NONE'), '0')


def _write(L, R, miss):
    for n_ in ('b714_citation_check.txt', 'b714_citation_check.json'):
        MEM.guard('b714', n_, _root_exclude())
    for name, data in (('b714_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b714_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        with open(q + '.tmp', 'wb') as fh:
            fh.write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b714 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b714_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b714_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b714_ferry_scan.txt')
    MEM.guard('b714', 'b714_ferry_scan.txt', _root_exclude())
    with open(s + '.tmp', 'wb') as fh:
        fh.write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b714_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
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
    """(R278)(4): b682's route, imported, with its act names pointed at b714, and b706's repair carried."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.C.SESSIONS_AFTER = C.SESSIONS_AFTER
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, K.LV_DIR, K.JOIN_DIR, 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects', 'D:/SIDE-bijection', 'D:/SIDE-interfaces', 'D:/SIDE-li-map',
                                                 'D:/SIDE-kernel') if r not in P.REPOS and os.path.isdir(r))
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b714'))
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
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b714')
    # ### (R324)(2), the item repair: THE WHOLE ANSWER. b682's cut ends at the first "END" after the needle (`best.find('END', k)`, :221), which a
    # ### word carrying END (AMENDMENT, APPENDED, RECOMMENDED) ends inside: b713's answers read 468 characters. The cut now ends at the answer's
    # ### last END (`best.rfind('END')`), the paste's own tail; the substitution printed, the route refusing where it does not apply.
    if body.count("best.find('END', k)") != 1:
        sys.exit('### b682`s CUT NOT FOUND ONCE IN ITS answer -- NOTHING CHECKED')
    body = body.replace("best.find('END', k)", "best.rfind('END')")
    body = body.replace("    open(q + '.tmp', 'wb')", "    MEM.guard('b714', os.path.basename(q), ROOT_EXCLUDE)\n    open(q + '.tmp', 'wb')")
    ns = dict(vars(P))
    ns.update(MEM=MEM, ROOT_EXCLUDE=_root_exclude())
    exec(compile(body, 'b682_citation.answer (b714)', 'exec'), ns)
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
        print('usage: b714_citation.py check [dry] | ferry | answer <needle> | word <needle> | replay <needle> <session id> <anchor>')
        sys.exit(2)
    fn(*sys.argv[2:])
