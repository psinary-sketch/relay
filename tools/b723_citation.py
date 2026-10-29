# -*- coding: utf-8 -*-
"""b723_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b723's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (bde68a30, a new session after the clear; the anchor (R333)'s line); the answer route is b682's, imported from
### tools/b682_citation.py with its act names pointed at b723, b706's repair carried (a bare eight-hex token a bank names as a sha256 or a
### kernel's lakefile pins as a rev is not read as a commit); the `word` route is b694's. Routes: `check [dry]` -> data/b723_citation_check.txt
### (.json) ; `ferry` -> data/b723_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the check on one answer.
### Carried by diff from b722_citation.py (data/b723_carry_citation.txt), b722's cite rows pruned (data/b723_prune_citation.txt) and this
### ruling's written by the Edit tool; this tool writes only the banks named above. Its (R333)(1) row reads lv's release list by `gh` (the
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
import b723_worklist as K   # noqa: E402
import act_membrane as MEM  # noqa: E402  ### (R333)(2)(ii): the membrane before every bank write of this tool


def _root_exclude():
    import b723_record as REC   # ### the record tool's exclusion pattern, the one the root route reads (imported at the call, nothing written)
    return REC.R.ROOT_EXCLUDE


C.SESSION = 'C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % K.SESSION_ID


def continuation_sessions():
    """the act's continuation sessions (K.SESSIONS_AFTER, b671's form) as transcript paths, read by b677's helpers after the seat's session."""
    return tuple('C:/Users/echo chamber/.claude/projects/D--/%s.jsonl' % sid for sid, _anc in K.SESSIONS_AFTER)


C.SESSIONS_AFTER = continuation_sessions()
NL = chr(10)
PP = C.PP
C.ANCHOR, C.TAIL = K.RULING_ANCHOR, K.TAIL   # ### b723 carry-time repair: the ruling's BEGIN line (pasted before the act opened); K.ANCHOR is the capture's
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
    # ### b723: the cite rows of (R333) and its ferry, written by the Edit tool after b722's rows were pruned (data/b723_prune_citation.txt)
    gr = lambda repo, *a: (g(repo, *a)[1] or '').strip()   # noqa: E731
    # ### (R333)(1): b722 at its weight
    cl = lines_of(p('data', 'b722_closing.txt'))
    # ### the fill is in the bank (data/b723_ferry.txt), the transcript's text carrying the slot: the quote read from the bank
    hq = _quote(rd(p('data', 'b723_ferry.txt')) or '', '"b722 closed: relay 65430407', '", its rows')
    add('ruling (1)', 'data/b722_closing.txt :1, the head line as the ruling quotes it (the filled slot, data/b723_ferry.txt :7)', bool(hq) and hq[1:] == at(cl, 1),
        at(cl, 1)[:120], '1')
    pub = _blob('D:/relay', '1607e994', 'data/b722_closing.txt').replace(chr(13), '').split(NL)
    rm = _remote_heads('D:/relay').get('refs/heads/main') or ''
    add('ruling (1)', 'the head line as the public relay carries it at 1607e994, its main', bool(pub) and pub[0] == at(cl, 1) and rm.startswith('1607e994'),
        'remote main %s' % rm[:8], '1')
    ev = lines_of(p('data', 'b722_events.txt'))
    starts = [int(m.group(1)) for m in (re.match(r'^    \((\d+)\) ', l) for l in ev) if m]
    dl = lines_of(p('data', 'b722_defects.txt'))
    letters = [m.group(1) for m in (re.match(r"^    \(([a-z]'?)\) ", l) for l in dl) if m]
    add('ruling (1), (2)', 'events (1)-(19) and 31 defects (data/b722_events.txt, data/b722_defects.txt)', starts == list(range(1, 20)) and len(letters) == 31,
        'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    add('ferry (read first)', 'event (19) at data/b722_events.txt :103, the reading of the twenty', at(ev, 103).startswith('    (19) ') and 'the twenty' in at(ev, 103),
        at(ev, 103)[:60], '0')
    add('ferry (read first)', 'data/b722_closing.txt :469, the carried items', at(cl, 469) == '### CARRIED FORWARD.', at(cl, 469)[:30], '0')
    # ### (R333)(2): the corrigendum and the repeat classes
    add('ruling (2)', 'tools/standing/ at v1.2.2 entering the act (tools/standing/VERSION)', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.2.2',
        at(lines_of(p('tools', 'standing', 'VERSION')), 1), '1')
    add('ruling (2)(v)', 'data/standing_clauses_v8.txt present, v9 not yet written', os.path.exists(p('data', 'standing_clauses_v8.txt'))
        and not os.path.exists(p('data', 'standing_clauses_v9.txt')), 'v8 present ; v9 %s' % os.path.exists(p('data', 'standing_clauses_v9.txt')), '1')
    stp = _jl('b722_steps.json')
    stp = stp if isinstance(stp, list) else (stp.get('rows') or [])
    lk = [i + 1 for i, s_ in enumerate(stp) if str(s_.get('subject', '')).startswith('b722 lock')]
    add('ruling (2)(iii)', 'b722`s steps bank: step 26 the lock commit, its phase "gate"', lk == [26] and stp[25].get('phase') == 'gate',
        'lock rows %s' % lk, '1')
    # ### the arm lives in the act's checks tool (tools/b722_checks.py), not in tools/standing/
    hk = [l for l in lines_of(p('tools', 'b722_checks.py')) if 'G-READFIRST-DIFF-BANKED' in l]
    add('ruling (2)(iv)', 'G-READFIRST-DIFF-BANKED named in tools/b722_checks.py (to retire)', bool(hk), '%d lines in b722_checks.py' % len(hk), '1')
    # ### (R333)(3): the open orders
    add('ruling (3)(i)', 'OPEN_TRAILS :16250, the ten open orders', at(ot, 16250).startswith('**The open orders:**') and at(ot, 16250).count('`W-ORD-') == 10,
        '%d orders' % at(ot, 16250).count('`W-ORD-'), '2')
    # ### (R333)(4): the registrations' sources
    add('ruling (4)(i)', 'FINDINGS :5667, sigma 0.9532604748', 'σ = 0.9532604748' in at(fi, 5667), at(fi, 5667)[:60], '3')
    add('ruling (4)(i)', 'FINDINGS :10206, the onsets 6.838396011 and 10.38532711', 'a = 6.838396011' in at(fi, 10206) and 'a = 10.38532711' in at(fi, 10206),
        at(fi, 10206)[:60], '3')
    a2 = lines_of(os.path.join(PP, 'archive', '2026-08-24-ledger-split', 'OPEN_TRAILS-archive-2-historical-landings-and-programs.md'))
    add('ruling (4)(i)', 'OPEN_TRAILS-archive-2 :2982, the band zero 0.79800 + 29.5518i', 'ρ ≈ 0.79800 + 29.5518i' in at(a2, 2982), at(a2, 2982)[:60], '3')
    for f_ in ('b707_onset.txt', 'b709_grid.txt', 'b711_list.json', 'b713_list.json', 'b717_list.json'):
        add('ruling (4)', 'data/%s' % f_, os.path.exists(p('data', f_)), 'present' if os.path.exists(p('data', f_)) else 'ABSENT', '3')
    # ### (R333)(6): the coefficient banks
    for f_ in K.COEFF_BANKS:
        add('ruling (6)', f_, os.path.exists(p(*f_.split('/'))), 'present' if os.path.exists(p(*f_.split('/'))) else 'ABSENT', '5')
    # ### (R333)(7) and the addendum's (4): the routes as b722's bank priced them
    adg = lines_of(p(*K.AXIOM_DIAG.split('/')))
    for n_, k_ in ((6, 'SIDE-kernel'), (13, 'SIDE-archimedean'), (22, 'SIDE-frobenius'), (30, 'SIDE-spinor'), (39, 'SIDE-rcurve')):
        add('ruling (7), addendum (4)', '%s :%d, %s`s route' % (K.AXIOM_DIAG, n_, k_), at(adg, n_).startswith('## %s -- run ' % k_), at(adg, n_)[:50], '6')
    add('addendum (4)', '%s :37, the six SIDESpinorLeg names not declared at the pin' % K.AXIOM_DIAG, at(adg, 37).count('SIDESpinorLeg.') == 6, '%d names' % at(adg, 37).count('SIDESpinorLeg.'), '6')
    fz = lines_of(p('data', 'b721_frozen_line.txt'))
    add('addendum (4)', 'data/b721_frozen_line.txt :84, SIDE-frobenius at its pin 2efe9f2', at(fz, 84).startswith('## SIDE-frobenius at v0.1.0 = 2efe9f2'), at(fz, 84)[:50], '6')
    # ### (R333)(8): the ledger split
    add('ruling (8)', 'OPEN_TRAILS :14680, W-ORD-LEDGER-SPLIT-RESOLVER and the cut FINDINGS :456-:6949', 'W-ORD-LEDGER-SPLIT-RESOLVER' in at(ot, 14680) and ':456-:6949' in at(ot, 14680),
        at(ot, 14680)[:60], '7')
    add('ruling (8)', 'data/b680_split_price.txt', os.path.exists(p('data', 'b680_split_price.txt')), 'present', '7')
    # ### the addendum's (1) and (3)
    stc = gr('D:/relay', 'status', '--porcelain', '--', 'data/b720_hook_refusals.txt', 'data/b721_hook_refusals.txt', 'data/b722_relay_push-b722-closing_push_out.txt',
             'data/b722_steps.json')
    for s_ in (' M data/b720_hook_refusals.txt', ' M data/b721_hook_refusals.txt', '?? data/b722_relay_push-b722-closing_push_out.txt', ' M data/b722_steps.json'):
        add('ruling (9), addendum (1)', 'git status: %s' % s_.strip(), s_.strip() in [l.strip() for l in stc.split(NL)], stc.replace(NL, ' | ')[:120], '0')
    rp = lines_of(p('data', 'b722_reproduce.txt'))
    add('addendum (3)', 'data/b722_reproduce.txt :143-:146, I-76 5293 against 6650', at(rp, 143).startswith('I-76   b544_probe_part') and '"count": 5293' in at(rp, 143)
        and "['6650']" in at(rp, 144) and 'M.enumerate_all()' in at(rp, 146), at(rp, 144)[:60], '1')
    # ### (R333)(9): the branches
    for repo_, names_ in K.DELETE:
        mg = gr(repo_, 'branch', '--merged', 'main', '--list', 'push-b722-*').replace('*', '').split()
        add('ruling (9)', 'the push-b722-* branches of %s, --merged into main' % repo_.split('/')[-1], sorted(mg) == sorted(names_), ' '.join(mg) or 'NONE', '0')
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (9)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (9)', 'pin-b718-de5ce8a9 as banked on %s' % k_, True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (9)', 'tools/mirror_prevbuild.json', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '7')
    standing_rows(text, add)
    return R


def run_numstat(repo, a, b, path):
    """(added, removed) of one file between two commits, by `git diff --numstat` inside the tool; None where unread."""
    r = subprocess.run(['git', '-C', repo, 'diff', '--numstat', a, b, '--', path], capture_output=True, text=True, encoding='utf-8', errors='replace')
    f = (r.stdout or '').split()
    return (int(f[0]), int(f[1])) if len(f) >= 2 and f[0].isdigit() and f[1].isdigit() else None


def standing_rows(text, add):
    """the citation tool reads the standing clauses by version (data/b712_rules.txt row (1)): for each version a ferry names as "standing clauses v<N>"
    outside a quotation, the bank data/standing_clauses_v<N>.txt present with its VERSION line -- v1 with its control banked AS WANTED; a version this
    act writes at step zero (v2, (R333)(2)) read as TO BE WRITTEN when absent and from the bank when present."""
    import b718_standing as SC   # ### b723 carry-time repair: the shift named b722_standing, which does not exist; b722 imported b718's
    flat = re.sub(r'“[^”]*”', '', ' '.join(text.split()))
    # ### b723 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b722_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
    for v in names or [1]:
        p = os.path.join(D, 'standing_clauses_v%d.txt' % v)
        t = rd(p) or ''
        ver = re.search(r'^VERSION: (\d+)$', t, re.M)
        if v == 1:
            ctl = _jl('b722_standing_control.json')
            add('ferry (standing clauses)', 'the standing clauses v1: data/standing_clauses_v1.txt', bool(t) and bool(ver) and ver.group(1) == '1' and bool(SC.parse(t)) and ctl.get('ok') is True,
                'present %s ; VERSION %s ; rows %d ; the re-assembly control AS WANTED %s' % (bool(t), ver.group(1) if ver else 'NONE', len(SC.parse(t)), ctl.get('ok')), '0')
        elif not t:
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- TO BE WRITTEN at Component 1 ((R333)(2)(v))' % (v, v), True, 'absent, as ordered', '0')
        else:
            add('ferry (standing clauses)', 'the standing clauses v%d: data/standing_clauses_v%d.txt' % (v, v), bool(ver) and ver.group(1) == str(v), 'present ; VERSION %s' % (ver.group(1) if ver else 'NONE'), '0')


def _write(L, R, miss):
    for n_ in ('b723_citation_check.txt', 'b723_citation_check.json'):
        MEM.guard('b723', n_, _root_exclude())
    for name, data in (('b723_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b723_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        with open(q + '.tmp', 'wb') as fh:
            fh.write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b723 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b723_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b723_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b723_ferry_scan.txt')
    MEM.guard('b723', 'b723_ferry_scan.txt', _root_exclude())
    with open(s + '.tmp', 'wb') as fh:
        fh.write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b723_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
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
    """(R278)(4): b682's route, imported, with its act names pointed at b723, and b706's repair carried."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.C.SESSIONS_AFTER = C.SESSIONS_AFTER
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, K.LV_DIR, K.JOIN_DIR, 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects', 'D:/SIDE-bijection', 'D:/SIDE-interfaces', 'D:/SIDE-li-map',
                                                 'D:/SIDE-kernel') if r not in P.REPOS and os.path.isdir(r))
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b723'))
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
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b723')
    # ### (R333)(2), the item repair: THE WHOLE ANSWER. b682's cut ends at the first "END" after the needle (`best.find('END', k)`, :221), which a
    # ### word carrying END (AMENDMENT, APPENDED, RECOMMENDED) ends inside: b722's answers read 468 characters. The cut now ends at the answer's
    # ### last END (`best.rfind('END')`), the paste's own tail; the substitution printed, the route refusing where it does not apply.
    if body.count("best.find('END', k)") != 1:
        sys.exit('### b682`s CUT NOT FOUND ONCE IN ITS answer -- NOTHING CHECKED')
    body = body.replace("best.find('END', k)", "best.rfind('END')")
    body = body.replace("    open(q + '.tmp', 'wb')", "    MEM.guard('b723', os.path.basename(q), ROOT_EXCLUDE)\n    open(q + '.tmp', 'wb')")
    ns = dict(vars(P))
    ns.update(MEM=MEM, ROOT_EXCLUDE=_root_exclude())
    exec(compile(body, 'b682_citation.answer (b723)', 'exec'), ns)
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
        print('usage: b723_citation.py check [dry] | ferry | answer <needle> | word <needle> | replay <needle> <session id> <anchor>')
        sys.exit(2)
    fn(*sys.argv[2:])
