# -*- coding: utf-8 -*-
"""b720_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b720's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (bde68a30, a new session after the clear; the anchor (R330)'s line); the answer route is b682's, imported from
### tools/b682_citation.py with its act names pointed at b720, b706's repair carried (a bare eight-hex token a bank names as a sha256 or a
### kernel's lakefile pins as a rev is not read as a commit); the `word` route is b694's. Routes: `check [dry]` -> data/b720_citation_check.txt
### (.json) ; `ferry` -> data/b720_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the check on one answer.
### Carried by diff from b719_citation.py (data/b720_carry_citation.txt), b719's cite rows pruned (data/b720_prune_citation.txt) and this
### ruling's written by the Edit tool; this tool writes only the banks named above. Its (R330)(1) row reads lv's release list by `gh` (the
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
import b720_worklist as K   # noqa: E402
import act_membrane as MEM  # noqa: E402  ### (R330)(2)(ii): the membrane before every bank write of this tool


def _root_exclude():
    import b720_record as REC   # ### the record tool's exclusion pattern, the one the root route reads (imported at the call, nothing written)
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
    # ### b720: the cite rows of (R330) and its ferry, written by the Edit tool after b719's rows were pruned (data/b720_prune_citation.txt)
    gr = lambda repo, *a: (g(repo, *a)[1] or '').strip()   # noqa: E731
    # ### (R330)(1): b719 at its weight
    cl = lines_of(p('data', 'b719_closing.txt'))
    hq = _quote(text, '"b719 closed: relay fa268307', '; 18 defects"')
    add('ruling (1)', 'data/b719_closing.txt :1, the head line as the ruling quotes it', bool(hq) and hq[1:] + '; 18 defects' == at(cl, 1),
        at(cl, 1)[:120], '1')
    add('ruling (1)', 'the counter CLAIM 2, CLOSE 26 (data/b719_closing.txt :5)', at(cl, 5).endswith('CLAIM 2, CLOSE 26'), at(cl, 5)[-30:], '1')
    st = _jl('b719_steps.json').get('rows') or []
    r33 = [r for r in st if (r.get('commit') or '').startswith('ef648cb9')]
    add('ruling (1)', 'the closing commit ef648cb9 at step 33, pushed and read back', len(st) == 33 and len(r33) == 1 and r33[0].get('phase') == 'closing'
        and (_remote_heads('D:/relay').get('refs/heads/main') or '').startswith('ef648cb9'), 'rows %d ; ef648cb9 %s ; remote main %s' % (
            len(st), [r.get('phase') for r in r33], (_remote_heads('D:/relay').get('refs/heads/main') or '')[:8]), '1')
    cf = [l for l in cl if '(R329)(2) : THE CLAIM ARMS PASSING' in l]
    add('ruling (1)', 'the claim arms 38 of 38 on both suite runs (data/b719_closing.txt)', len(cf) == 2 and all('38 OF 38' in l for l in cf), '%d lines' % len(cf), '1')
    mi = lines_of(p('data', 'b719_mirror.txt'))
    add('ruling (1)', 'the mirror mirror-refresh-2026-10-28-b719.zip, 74 files, CLEAN with the root line, built at PLACE-papers b92bb70',
        'mirror-refresh-2026-10-28-b719.zip' in at(mi, 2) and 'files 74' in at(mi, 3) and 'b92bb70' in at(mi, 4) and at(mi, 6).endswith('Act root: b719 ' + K.B714_ROOT)
        and any('CLEAN ON ALL THREE CLAUSES' in l for l in mi), 'zip %s ; root line %s' % (os.path.exists(K.MIRROR_ZIP), at(mi, 6)[-20:]), '1')
    ch = [l for l in lines_of(p('data', 'b719_checks_postpush_standing-b3.txt')) if 'THE ACT-ROOT CHAIN`S PART B' in l]
    add('ruling (1)', 'the root chain agreeing from b624 to b719 (the post-push chain parts)', bool(ch) and 'b719 AGREE' in ch[0] and 'DIFFER' not in ch[0], '%d line' % len(ch), '1')
    sc = _jl('b719_scores_close.json')
    add('ruling (1)', 'N4 REFUTED as the author ruled (data/b719_scores_close.json)', (sc.get('N4') or [''])[0] == 'REFUTED', str((sc.get('N4') or [''])[0]), '1')
    for f, n, needle in (('b719_coeffs.txt', 45, 'n0(-20) = 36, b = -2 ; n0(-47) = 168, b = -2'), ('b719_coeffs.txt', 45, 'H-24 REFUTED ; H-47 REFUTED'),
                         ('b719_derivation.txt', 70, 'CLAUSE 1 NOT DERIVED, ITS STEP NAMED'), ('b719_offset_read.txt', 121, '+54.9 TO +161.7'),
                         ('b719_offset_read.txt', 123, 'H-OFFSET, REGISTERED'), ('b719_surgery.txt', 22, 'H-SHAPE REGISTERED AT 965cb8e8'),
                         ('b719_arm_retire.txt', 12, 'RETIRED 25 CLOSE ARMS ; THE RUN LIST 141 -> 116'), ('b719_count_route_price.txt', 44, '19,852 UNIT BANDS'),
                         ('b719_count_route_price.txt', 44, '44 TO ~2,700 FOREGROUND HOURS'), ('b719_touch.txt', 104, 'ROWS 73 ; AGREES 73')):
        add('ruling (1)', 'data/%s :%d: %s' % (f, n, needle), needle in at(lines_of(p('data', f)), n), at(lines_of(p('data', f)), n)[:90], '1')
    add('ruling (1)', 'H-SHAPE committed at 965cb8e8 (data/b719_registrations.txt)', 'H-SHAPE' in _blob('D:/relay', '965cb8e8', 'data/b719_registrations.txt'),
        'the blob at 965cb8e8', '1')
    # ### (R330)(2): the corrigendum's sources
    ev = lines_of(p('data', 'b719_events.txt'))
    starts = [int(m.group(1)) for m in (re.match(r'^    \((\d+)\) ', l) for l in ev) if m]
    tags = [m.group(1) for m in (re.search(r'\[(CLAIM|CLOSE) ; ', l) for l in ev if re.match(r'^    \(\d+\) ', l)) if m]
    add('ruling (2)', 'data/b719_events.txt (1)-(10), each tagged', starts == list(range(1, 11)) and len(tags) == 10,
        'starts %s ; CLAIM %d ; CLOSE %d' % (starts[-1:], tags.count('CLAIM'), tags.count('CLOSE')), '1')
    dl = lines_of(p('data', 'b719_defects.txt'))
    add('ruling (2)', 'data/b719_defects.txt present, its letters (a)-(r)', any(re.match(r'^\s*\(r\) ', l) for l in dl) and not any(re.match(r'^\s*\(s\) ', l) for l in dl),
        '%d lines' % len(dl), '1')
    add('ruling (2)(i)', 'dbea2e3f is b718`s leftover commit and has no row in data/b719_steps.json', bool(gr('D:/relay', 'rev-parse', '--verify', '--quiet', 'dbea2e3f^{commit}'))
        and not any((r.get('commit') or '').startswith('dbea2e3f') for r in st), 'rows naming it %d' % sum(1 for r in st if (r.get('commit') or '').startswith('dbea2e3f')), '0')
    e9 = [l for l in ev if l.startswith('    (9) ')]
    add('ruling (2)(ii)', 'event (9): the MANIFEST control against a86c9429 on day1/Silence_of_Foundations.md', bool(e9) and 'NOT AS' in e9[0], (e9 or [''])[0][:90], '1')
    add('ruling (2)(ii)', 'the control`s reference K.RECUT_MERGE (tools/b719_worklist.py) is a86c9429', 'RECUT_MERGE = \'a86c9429' in rd(p('tools', 'b719_worklist.py')),
        'tools/b719_worklist.py', '1')
    add('ruling (2)(iii)', 'the memory file overwritten (feedback_b719_traps.md) and its earlier text restored to feedback_b719_stepzero_traps.md',
        os.path.exists('C:/Users/echo chamber/.claude/projects/D--/memory/feedback_b719_stepzero_traps.md'), 'restored at b720`s opening', '1')
    # ### (R330)(3): the registration's discriminants, by their class number and forms alone (the ruling's allowance)
    def forms(dd):
        out = []
        a = 1
        while 3 * a * a <= -dd:
            for b in range(-a + 1, a + 1):
                if (b * b - dd) % (4 * a) == 0:
                    c = (b * b - dd) // (4 * a)
                    if c >= a and not (b < 0 and (a == c)) and __import__('math').gcd(__import__('math').gcd(a, abs(b)), c) == 1:
                        out.append((a, b, c))
            a += 1
        return out

    def kron(dd, q):
        if dd % q == 0:
            return 0
        if q == 2:
            return 1 if dd % 8 in (1, 7) else -1
        return 1 if pow(dd % q, (q - 1) // 2, q) == 1 else -1
    for dd, want2, want3 in ((-35, -1, 1), (-40, 0, -1)):
        fm = forms(dd)
        fund = (dd % 4 == 1 and all(dd % (q * q) for q in range(3, 8, 2))) or (dd % 4 == 0 and (dd // 4) % 4 in (2, 3) and all((dd // 4) % (q * q) for q in range(3, 8, 2)))
        add('ruling (3)', '%d: class number 2, fundamental; 2 %s and 3 %s' % (dd, {-1: 'inert', 0: 'ramifies', 1: 'splits'}[want2], {-1: 'inert', 0: 'ramifies', 1: 'splits'}[want3]),
            len(fm) == 2 and fund and kron(dd, 2) == want2 and kron(dd, 3) == want3, 'forms %s ; (d/2) %d ; (d/3) %d ; fundamental %s' % (fm, kron(dd, 2), kron(dd, 3), fund), '2')
    for f, c in K.REG_COMMITS:
        b = _blob('D:/relay', c, f)
        add('ruling (3); N2', '%s read unchanged from its commit %s' % (f, c[:8]), bool(b) and b.replace(chr(13), '') == (rd(p(*f.split('/'))) or ''), '%d bytes at the commit' % len(b), '2')
    b6 = _blob('D:/relay', 'dc5e808f', 'data/b716_registrations.txt')
    add('ruling (3)(iii)', 'data/b716_registrations.txt (ii) at dc5e808f, the law', '(ii) THE PREDICTION' in b6, 'the blob at dc5e808f', '2')
    src = rd(p('tools', 'b711_coeffs.py'))
    add('ruling (3)', 'b711`s route (tools/b711_coeffs.py) through the cut 32532 with its controls C1-C3', '32532' in src and all(c_ in src for c_ in ('C1', 'C2', 'C3')),
        'tools/b711_coeffs.py', '2')
    for f in ('b718_derivation.txt', 'b719_derivation.txt'):
        add('ruling (3)(i); ruling (4)', 'the shape rule`s and the derivation`s bank data/%s' % f, os.path.exists(p('data', f)), 'present', '2, 3')
    for f in ('b711_coeffs.txt', 'b713_coeffs.txt', 'b717_coeffs.txt', 'b719_coeffs.txt'):
        add('ruling (3)(ii); ruling (4)', 'the five banked cases` bank data/%s' % f, os.path.exists(p('data', f)), 'present', '2, 3')
    # ### (R330)(5): wave 1's groundwork
    rg = lines_of(os.path.join(PP, 'REGISTRY.md'))
    add('ruling (5)(i)', 'REGISTRY`s phase attribute block (REGISTRY.md :772)', at(rg, 772).startswith('## PHASE ATTRIBUTE'), at(rg, 772)[:60], '4')
    add('ruling (5)(iii)', 'REGISTRY`s PHASE 1.2 -- FROZEN block (REGISTRY.md :711)', 'PHASE 1.2 — FROZEN' in at(rg, 711), at(rg, 711)[:60], '6')
    for doc in ('THE_CLAUSE_AND_ITS_COMPILED_FACES.md', 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md', 'FACES_LEDGER.md', 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md',
                'phase1.5/proofs/THE_RESIDUE_OF_RH.md', 'phase2/method/FACES_OF_H2_AT_FINITE_INSTANCE.md'):
        add('ruling (5)(i)', 'the sign core`s document %s on PLACE-papers main' % doc, bool(gr(PP, 'ls-tree', '--name-only', 'main', '--', doc)), 'tracked at main', '4')
    add('ruling (5)(ii)', 'b718`s challenge price (data/b718_challenge_price.txt)', os.path.exists(p('data', 'b718_challenge_price.txt')), 'present', '5')
    hd = _decl_files(K.EF_DIR, 'main', 'h2_sign_iff_rh')
    add('ruling (5)(ii)', 'h2_sign_iff_rh declared in SIDE-explicit-formula at main', len(hd) >= 1, '%s' % hd, '5')
    add('ruling (5)(i)', 'b718`s registry cells price (data/b718_registry_cells_price.txt)', os.path.exists(p('data', 'b718_registry_cells_price.txt')), 'present', '4')
    add('ruling (5)(iii)', 'b718`s pin (data/b718_pin.txt) and the federation price (data/b716_federation_pin_price.txt)',
        os.path.exists(p('data', 'b718_pin.txt')) and os.path.exists(p('data', 'b716_federation_pin_price.txt')), 'present', '6')
    lb = [k for k in K.PIN_CARRIED if gr('D:/' + k, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.PIN_BRANCH)]
    add('ruling (5)(iii)', 'the nine local bump branches (%s)' % K.PIN_BRANCH, len(lb) == 9, 'found on %d of %d' % (len(lb), len(K.PIN_CARRIED)), '6')
    cw = ' '.join(rd(f_) or '' for f_ in glob.glob('D:/SIDE-cosmo/.github/workflows/*.yml'))
    add('ruling (5)(iii)', 'SIDE-cosmo`s workflow carries pages: write', 'pages: write' in cw, '%d workflow bytes' % len(cw), '6')
    # ### (R330)(6)
    add('ruling (6)', 'b709`s grid (data/b709_grid.txt) and b718`s surgery price (data/b718_surgery_price.txt)',
        os.path.exists(p('data', 'b709_grid.txt')) and os.path.exists(p('data', 'b718_surgery_price.txt')), 'present', '6')
    # ### (R330)(7): the carried files and branches
    s1 = gr('D:/relay', 'status', '--porcelain', '--', 'data/b719_relay_push-b719-closing_push_out.txt')
    s2 = gr('D:/relay', 'status', '--porcelain', '--', 'data/b719_steps.json')
    add('ruling (7)', 'b719`s closing capture untracked and its step-33 row uncommitted', s1.startswith('??') and s2.startswith('M'), '%s / %s' % (s1, s2), '0')
    for repo, names in K.DELETE:
        mg = gr(repo, 'branch', '--merged', 'main', '--list', 'push-b719-*').replace('*', ' ').split()
        add('ruling (7)', 'the push-b719-* branches of %s merged into main: %s' % (repo, ', '.join(names)), sorted(mg) == sorted(names), 'merged %s' % mg, '0')
    pb = gr(K.LV_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.PORT_BRANCH)
    add('ruling (7)', 'port-b707 kept (SIDE-lv-conservation, at cb0aea56)', pb == K.PORT_TIP, pb[:8], '0')
    # ### (R330)(8)-(9) and the ferry
    add('ruling (9)', 'the draft at v5 (23228113), held', K.DRAFT == '23228113', 'tools/b720_worklist.py DRAFT', '0')
    add('ferry (PATHS)', 'the act`s paths, each present', all(os.path.isdir(x) for x in K.PATHS), 'absent %s' % [x for x in K.PATHS if not os.path.isdir(x)], '0')
    rf = ['b719_closing.txt', 'b719_events.txt', 'b719_defects.txt', 'b719_coeffs.txt', 'b719_derivation.txt', 'b718_derivation.txt', 'b719_registrations.txt',
          'b718_registrations.txt', 'b716_registrations.txt', 'b719_offset_read.txt', 'b719_surgery.txt', 'b718_challenge_price.txt', 'b718_registry_cells_price.txt',
          'b718_pin.txt', 'b716_federation_pin_price.txt']
    add('ferry (readfirst)', 'the readfirst list`s %d relay banks, each present' % len(rf), all(os.path.exists(p('data', f)) for f in rf),
        'absent %s' % [f for f in rf if not os.path.exists(p('data', f))], '0')
    vt = rd(p('tools', 'standing', 'VERSION')) or ''
    add('ferry', 'tools/standing/ at v1.2.0', 'v1.2.0' in vt or '1.2.0' in vt, vt.strip()[:20], '7')
    try:
        sys.path.insert(0, os.path.join(T, 'standing'))
        import arms as SA
        run = getattr(SA, 'run_list', None)
        n_run = len(run()) if callable(run) else None
    except Exception as e:
        n_run = 'unread: %s' % type(e).__name__
    add('ferry', 'b719`s run list of 116 arms (data/b719_checks.txt)', any('ARMS RUN : 116.' in l for l in lines_of(p('data', 'b719_checks.txt'))),
        'b719`s combine ; the standing run list %s' % n_run, '7')
    standing_rows(text, add)
    return R


def standing_rows(text, add):
    """the citation tool reads the standing clauses by version (data/b712_rules.txt row (1)): for each version a ferry names as "standing clauses v<N>"
    outside a quotation, the bank data/standing_clauses_v<N>.txt present with its VERSION line -- v1 with its control banked AS WANTED; a version this
    act writes at step zero (v2, (R330)(2)) read as TO BE WRITTEN when absent and from the bank when present."""
    import b718_standing as SC   # ### b720 carry-time repair: the shift named b719_standing, which does not exist; b719 imported b718's
    flat = re.sub(r'“[^”]*”', '', ' '.join(text.split()))
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing clauses(?:’)? v(\d+)', flat, re.I)))
    for v in names or [1]:
        p = os.path.join(D, 'standing_clauses_v%d.txt' % v)
        t = rd(p) or ''
        ver = re.search(r'^VERSION: (\d+)$', t, re.M)
        if v == 1:
            ctl = _jl('b719_standing_control.json')
            add('ferry (standing clauses)', 'the standing clauses v1: data/standing_clauses_v1.txt', bool(t) and bool(ver) and ver.group(1) == '1' and bool(SC.parse(t)) and ctl.get('ok') is True,
                'present %s ; VERSION %s ; rows %d ; the re-assembly control AS WANTED %s' % (bool(t), ver.group(1) if ver else 'NONE', len(SC.parse(t)), ctl.get('ok')), '0')
        elif not t:
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- TO BE WRITTEN at step zero ((R330)(2))' % (v, v), True, 'absent, as ordered', '0')
        else:
            add('ferry (standing clauses)', 'the standing clauses v%d: data/standing_clauses_v%d.txt' % (v, v), bool(ver) and ver.group(1) == str(v), 'present ; VERSION %s' % (ver.group(1) if ver else 'NONE'), '0')


def _write(L, R, miss):
    for n_ in ('b720_citation_check.txt', 'b720_citation_check.json'):
        MEM.guard('b720', n_, _root_exclude())
    for name, data in (('b720_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b720_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        with open(q + '.tmp', 'wb') as fh:
            fh.write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b720 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b720_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b720_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b720_ferry_scan.txt')
    MEM.guard('b720', 'b720_ferry_scan.txt', _root_exclude())
    with open(s + '.tmp', 'wb') as fh:
        fh.write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b720_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
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
    """(R278)(4): b682's route, imported, with its act names pointed at b720, and b706's repair carried."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.C.SESSIONS_AFTER = C.SESSIONS_AFTER
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, K.LV_DIR, K.JOIN_DIR, 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects', 'D:/SIDE-bijection', 'D:/SIDE-interfaces', 'D:/SIDE-li-map',
                                                 'D:/SIDE-kernel') if r not in P.REPOS and os.path.isdir(r))
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b720'))
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
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b720')
    # ### (R330)(2), the item repair: THE WHOLE ANSWER. b682's cut ends at the first "END" after the needle (`best.find('END', k)`, :221), which a
    # ### word carrying END (AMENDMENT, APPENDED, RECOMMENDED) ends inside: b719's answers read 468 characters. The cut now ends at the answer's
    # ### last END (`best.rfind('END')`), the paste's own tail; the substitution printed, the route refusing where it does not apply.
    if body.count("best.find('END', k)") != 1:
        sys.exit('### b682`s CUT NOT FOUND ONCE IN ITS answer -- NOTHING CHECKED')
    body = body.replace("best.find('END', k)", "best.rfind('END')")
    body = body.replace("    open(q + '.tmp', 'wb')", "    MEM.guard('b720', os.path.basename(q), ROOT_EXCLUDE)\n    open(q + '.tmp', 'wb')")
    ns = dict(vars(P))
    ns.update(MEM=MEM, ROOT_EXCLUDE=_root_exclude())
    exec(compile(body, 'b682_citation.answer (b720)', 'exec'), ns)
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
        print('usage: b720_citation.py check [dry] | ferry | answer <needle> | word <needle> | replay <needle> <session id> <anchor>')
        sys.exit(2)
    fn(*sys.argv[2:])
