# -*- coding: utf-8 -*-
"""b721_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b721's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (bde68a30, a new session after the clear; the anchor (R331)'s line); the answer route is b682's, imported from
### tools/b682_citation.py with its act names pointed at b721, b706's repair carried (a bare eight-hex token a bank names as a sha256 or a
### kernel's lakefile pins as a rev is not read as a commit); the `word` route is b694's. Routes: `check [dry]` -> data/b721_citation_check.txt
### (.json) ; `ferry` -> data/b721_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the check on one answer.
### Carried by diff from b720_citation.py (data/b721_carry_citation.txt), b720's cite rows pruned (data/b721_prune_citation.txt) and this
### ruling's written by the Edit tool; this tool writes only the banks named above. Its (R331)(1) row reads lv's release list by `gh` (the
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
import b721_worklist as K   # noqa: E402
import act_membrane as MEM  # noqa: E402  ### (R331)(2)(ii): the membrane before every bank write of this tool


def _root_exclude():
    import b721_record as REC   # ### the record tool's exclusion pattern, the one the root route reads (imported at the call, nothing written)
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
    # ### b721: the cite rows of (R331) and its ferry, written by the Edit tool after b720's rows were pruned (data/b721_prune_citation.txt)
    gr = lambda repo, *a: (g(repo, *a)[1] or '').strip()   # noqa: E731
    # ### (R331)(1): b720 at its weight
    cl = lines_of(p('data', 'b720_closing.txt'))
    hq = _quote(text, '"b720 closed: relay 6d7cb5f7', '; 29 defects"')
    add('ruling (1)', 'data/b720_closing.txt :1, the head line as the ruling quotes it', bool(hq) and hq[1:] + '; 29 defects' == at(cl, 1),
        at(cl, 1)[:120], '1')
    add('ruling (1)', 'the counter CLAIM 2, CLOSE 42 (data/b720_closing.txt :5)', at(cl, 5).endswith('CLAIM 2, CLOSE 42'), at(cl, 5)[-30:], '1')
    st = _jl('b720_steps.json').get('rows') or []
    r38 = [r for r in st if (r.get('commit') or '').startswith('8834a5b6')]
    add('ruling (1)', 'the closing commit 8834a5b6 at step 38, pushed and read back', len(st) == 38 and len(r38) == 1 and r38[0].get('phase') == 'closing'
        and (_remote_heads('D:/relay').get('refs/heads/main') or '').startswith('8834a5b6'), 'rows %d ; 8834a5b6 %s ; remote main %s' % (
            len(st), [r.get('phase') for r in r38], (_remote_heads('D:/relay').get('refs/heads/main') or '')[:8]), '1')
    cf = [l for l in cl if '(R330)(2) : THE CLAIM ARMS PASSING' in l]
    add('ruling (1)', 'the suite 111 of 116 and the claim arms 36 of 38 on both runs (data/b720_closing.txt)', len(cf) == 2 and all(
        '36 OF 38' in l and '111 OF 116' in l for l in cf), '%d lines' % len(cf), '1')
    rl = [l.split() for l in lines_of(p('data', 'act_roots.txt')) if l.strip()]
    rb = lines_of(p('data', 'b720_root_banks.txt'))
    add('ruling (1)', 'the root b5a76ed9 over 103 banks, chained from 09e524a7 (data/act_roots.txt, data/b720_root_banks.txt)',
        bool(rl) and rl[-1][0] == 'b720' and rl[-1][1].startswith('b5a76ed9') and rl[-1][2].startswith('09e524a7') and any(re.search(r'\b103\b', l) for l in rb),
        'last row %s' % ' '.join(x[:8] for x in (rl[-1] if rl else [])), '1')
    ch = [l for l in lines_of(p('data', 'b720_checks_postpush_standing-b3.txt')) if 'THE ACT-ROOT CHAIN`S PART B' in l]
    add('ruling (1)', 'the root recomputed equal (the post-push chain part, b720 AGREE)', bool(ch) and 'b720 AGREE' in ch[0] and 'DIFFER' not in ch[0], '%d line' % len(ch), '1')
    sc = _jl('b720_scores_close.json')
    add('ruling (1)', 'N5 REFUTED at the close (data/b720_scores_close.json), event (12)', (sc.get('N5') or [''])[0] == 'REFUTED',
        str((sc.get('N5') or [''])[0]), '1')
    ev = lines_of(p('data', 'b720_events.txt'))
    starts = [int(m.group(1)) for m in (re.match(r'^    \((\d+)\) ', l) for l in ev) if m]
    tags = [m.group(1) for m in (re.search(r'\[(CLAIM|CLOSE) ; ', l) for l in ev if re.match(r'^    \(\d+\) ', l)) if m]
    e12 = [l for l in ev if l.startswith('    (12) ')]
    add('ruling (1)', 'event (12): the scorer counting git branch --list as a write', bool(e12) and 'git branch --list' in ' '.join(ev[ev.index(e12[0]):ev.index(e12[0]) + 9]),
        (e12 or [''])[0][:80], '1')
    dl = lines_of(p('data', 'b720_defects.txt'))
    letters = [m.group(1) for m in (re.match(r"^    \(([a-z]'?)\) ", l) for l in dl) if m]
    add('ruling (1), (2)', 'the counter over 29 defects and 15 events, each tagged (data/b720_defects.txt, data/b720_events.txt)',
        len(letters) == 29 and starts == list(range(1, 16)) and len(tags) == 15, 'letters %d ; events %s ; tagged %d' % (len(letters), starts[-1:], len(tags)), '1')
    mi = lines_of(p('data', 'b720_mirror.txt'))
    add('ruling (1)', 'the mirror mirror-refresh-2026-10-28-b720.zip, 74 files, CLEAN on all three clauses with the root line (data/b720_mirror.txt)',
        any('mirror-refresh-2026-10-28-b720.zip' in l for l in mi) and any('files 74' in l for l in mi) and any(l.endswith('Act root: b720 ' + K.B714_ROOT) for l in mi)
        and any('CLEAN ON ALL THREE CLAUSES' in l for l in mi), 'zip %s' % os.path.exists(K.MIRROR_ZIP), '1')
    add('ruling (1)', 'the FINDINGS entry at :11072 carrying the author`s title wording', at(fi, 11072).startswith('## The coefficient law at -35 and -40')
        and 'the law’s value clause REFUTED at -40 (b = -1/2), its prime clause HELD at both' in at(fi, 11072), at(fi, 11072)[:80], '1')
    add('ruling (1)', 'the trail at OPEN_TRAILS :16218', at(ot, 16218).startswith('### b720 — lane two, act one hundred and forty-seven'), at(ot, 16218)[:80], '1')
    co = lines_of(p('data', 'b720_coeffs.txt'))
    for needle in ('n0(-35) = 135, b = -2 ; n0(-40) = 100, b = -1/2', 'H-DECOMP HELD', 'PRED-35 HELD, PRED-40 HELD', 'FORCED 2 APART'):
        add('ruling (1)', 'data/b720_coeffs.txt :57: %s' % needle, needle in at(co, 57), at(co, 57)[:90], '1')
    dv = lines_of(p('data', 'b720_derivation.txt'))
    for n, needle in ((103, '## THE GRADE'), (107, 'THEOREM, WITH ITS HYPOTHESES'), (109, 'those of value -2 are R . R . R . R, R^2 . R . S, R^2 . S^2, S^3 . R'),
                      (109, 'R^2 . R^2 (-1/2)'), (114, 'THE STEP THAT REMAINS THERE, NAMED'), (118, 'Clause 2 holds at the seven'),
                      (120, 'THE -2 OF BOTH CONFIGURATIONS A THEOREM IN C2 AT OMEGA 4')):
        add('ruling (1)', 'data/b720_derivation.txt :%d: %s' % (n, needle), needle in at(dv, n), at(dv, n)[:90], '1')
    rd_ = run_numstat('D:/MY-DOwnloads/PLACE-papers', 'b92bb70a', '5872b897', 'REGISTRY.md')
    add('ruling (1)', 'REGISTRY appended at 5872b897, 0 lines removed', bool(rd_) and rd_[1] == 0, 'added %s removed %s' % (rd_ or ('-', '-')), '1')
    chl = rd(p('data', 'b720_challenge.txt')) or ''
    add('ruling (1)', 'the challenge file ELABORATES, run 40651875792 (data/b720_challenge.txt)', 'ELABORATES' in chl and '40651875792' in chl, 'the bank', '1')
    pn = lines_of(p('data', 'b720_pin.txt'))
    add('ruling (1)', 'the pin at 1 of 6 eligible (data/b720_pin.txt :7)', at(pn, 7).startswith('THE PIN AT 1 OF 6 ELIGIBLE'), at(pn, 7)[:60], '1')
    add('ruling (1)', 'defect (e) at data/b720_defects.txt :11, a CLAIM', at(dl, 11).startswith("    (e) THE SEAT'S [CLAIM ; NEW]"), at(dl, 11)[:60], '1')
    add('ruling (1)', 'b716`s registration (ii) at dc5e808f', '(ii)' in _blob('D:/relay', 'dc5e808f', 'data/b716_registrations.txt'), 'the blob at dc5e808f', '1')
    # ### (R331)(2): the corrigendum's sources and the three repairs' objects
    add('ruling (2)', 'tools/standing/ at v1.2.0 entering the act (tools/standing/VERSION); v1.2.1 to be written by (2)', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.2.0',
        at(lines_of(p('tools', 'standing', 'VERSION')), 1), '1')
    ck = rd(p('tools', 'b720_checks.py')) or ''
    add('ruling (2)(i)', 'G-FINDINGS-ENTRY and G-ENTRY-TITLE-FORM, two claim arms, and the author`s answers bank (data/b720_author_answers.txt)',
        'G-FINDINGS-ENTRY' in ck and 'G-ENTRY-TITLE-FORM' in ck and os.path.exists(p('data', 'b720_author_answers.txt')),
        'tools/b720_checks.py', '1')
    add('ruling (2)(ii)', 'the one-git-write rule (tools/rule_arms.py, G-RULE-ONE-GIT-WRITE)', 'ONE-GIT-WRITE' in (rd(p('tools', 'rule_arms.py')) or ''), 'tools/rule_arms.py', '1')
    add('ruling (2)(iii)', 'the MANIFEST control`s reference a86c9429 (tools/b720_worklist.py RECUT_MERGE), stale from b716 to b720 (events: b716-b719 and b720 (15))',
        "RECUT_MERGE = 'a86c9429" in (rd(p('tools', 'b720_worklist.py')) or '') and any(l.startswith('    (15) ') and 'NOT AS WANTED' in ' '.join(ev[ev.index(l):ev.index(l) + 4]) for l in ev),
        'tools/b720_worklist.py', '1')
    add('ruling (2)(iii)', '(R328)(7)`s toolset diff (data/b718_carry_standing.txt)', os.path.exists(p('data', 'b718_carry_standing.txt')), 'present', '1')
    # ### (R331)(3): the C2 table and b711's route
    src = rd(p('tools', 'b711_coeffs.py')) or ''
    add('ruling (3)', 'b711`s route (tools/b711_coeffs.py) through the cut 32532 with its controls C1-C3', '32532' in src and all(c_ in src for c_ in ('C1', 'C2', 'C3'))
        and bool(re.search(r'\bC1\b', src)) and bool(re.search(r'\bC3\b', src)), 'C1 %s ; C3 %s' % (bool(re.search(r'\bC1\b', src)), bool(re.search(r'\bC3\b', src))), '2')
    add('ruling (3)', 'the cut 32532 in b720`s coefficients (data/b720_coeffs.txt)', any('32532' in l for l in co), 'the bank', '2')
    add('ruling (3)(i)', 'the C2 table of data/b720_derivation.txt (step (6), the table of 20 rows)', any(l.startswith('## STEP (6)') for l in dv) and 'the table of 20 rows' in ' '.join(dv),
        'the bank', '2')
    # ### (R331)(4): the step at h > 2 and the three checks
    add('ruling (4)', 'data/b720_derivation.txt :113: -23 (C3), -39 (C4) and -47 (C5)', 'At -23 (C3), -39 (C4) and -47 (C5)' in at(dv, 113), at(dv, 113)[:80], '3')
    add('ruling (4)', 'b719`s step (1), its turns (data/b719_derivation.txt)', any(l.startswith('## STEP (1)') for l in lines_of(p('data', 'b719_derivation.txt'))), 'the bank', '3')
    # ### (R331)(5): the offset
    op = lines_of(p('data', 'b720_offset_price.txt'))
    add('ruling (5)', 'data/b720_offset_price.txt: the seventeen banked pairs, post hoc (:11)', 'THE SEVENTEEN BANKED PAIRS, POST HOC' in at(op, 11), at(op, 11)[:80], '4')
    r19 = lines_of(p('data', 'b719_registrations.txt'))
    add('ruling (5)', 'H-OFFSET`s falsifier at r(rho) <= 0.05 (data/b719_registrations.txt :53)', 'r(rho) <= 0.05' in at(r19, 53), at(r19, 53)[:80], '4')
    add('ruling (5)(ii)', 'b709`s route (tools/b709_pairs.py)', os.path.exists(p('tools', 'b709_pairs.py')), 'present', '4')
    # ### (R331)(6): the surgery
    add('ruling (6)', 'H-SHAPE at 965cb8e8 (data/b719_registrations.txt)', 'H-SHAPE' in _blob('D:/relay', '965cb8e8', 'data/b719_registrations.txt'), 'the blob at 965cb8e8', '5')
    add('ruling (6)', 'b718`s price (data/b718_surgery_price.txt)', os.path.exists(p('data', 'b718_surgery_price.txt')), 'present', '5')
    add('ferry (read first)', 'data/b719_surgery.txt :22', 'H-SHAPE REGISTERED AT 965cb8e8' in at(lines_of(p('data', 'b719_surgery.txt')), 22),
        at(lines_of(p('data', 'b719_surgery.txt')), 22)[:80], '5')
    # ### (R331)(7): the frozen line -- each wave 1 kernel's pin, its Mathlib, its workflow; the four statements at their tags
    for k_, tag_, short_ in K.WAVE1:
        kp = 'D:/' + k_
        c_ = gr(kp, 'rev-parse', '--verify', '--quiet', tag_ + '^{commit}')
        man = _blob(kp, tag_, 'lake-manifest.json')
        add('ruling (7)', '%s %s = %s, its own lake-manifest.json at the pin' % (k_, tag_, short_), c_.startswith(short_) and 'mathlib' in man,
            '%s ; manifest %d bytes' % (c_[:12], len(man)), '6')
    for k_, nm_ in K.CHECKPOINT_STATEMENTS:
        tag_ = dict((a_, b_) for a_, b_, _c in K.WAVE1)[k_]
        fs = _decl_files('D:/' + k_, tag_, nm_)
        add('ruling (7)(i)', '%s declared at %s %s' % (nm_, k_, tag_), len(fs) == 1, ', '.join(fs) or 'NOT FOUND', '6')
    add('ruling (7)(iii)', 'SIDE-explicit-formula`s workflow file (.github/workflows/build-module.yml at main)', bool(_blob(K.EF_DIR, 'main', '.github/workflows/build-module.yml')),
        'present at main', '6')
    sml = lines_of(os.path.join(PP, 'SPIRAL_MAP.md'))
    add('ruling (7)(ii)', 'SPIRAL_MAP :104`s sentence (SPIRAL_MAP.md :104, the Phase 1.2 checkpoint kernels)', 'The Phase 1.2 checkpoint kernels' in at(sml, 104), at(sml, 104)[:80], '6')
    rg = lines_of(os.path.join(PP, 'REGISTRY.md'))
    add('ferry (read first)', 'REGISTRY`s PHASE 1.2 -- FROZEN block (REGISTRY.md :711)', 'PHASE 1.2 — FROZEN' in at(rg, 711), at(rg, 711)[:60], '6')
    add('ferry (read first)', 'REGISTRY`s attribute block at 5872b897', bool(_blob('D:/MY-DOwnloads/PLACE-papers', '5872b897', 'REGISTRY.md')), 'the blob at 5872b897', '6')
    # ### (R331)(8): the federation pin at its banked state
    pj = ' '.join(pn)
    add('ruling (8)', 'SIDE-effects builds at de5ce8a9 (b718`s run, data/b720_pin.txt :9)', 'SIDE-effects' in at(pn, 9) and 'BUILDS' in at(pn, 9), at(pn, 9)[:70], '7')
    add('ruling (8)', 'SIDE-simplicity builds; SIDE-grh-transfer, SIDE-kernel, SIDE-trivium and SIDE-lv-conservation break; SIDE-interfaces on a missing Kernel.lean',
        tuple(K.PIN_BUILDS) == ('SIDE-simplicity',) and set(K.PIN_HELD) == {'SIDE-grh-transfer', 'SIDE-interfaces', 'SIDE-kernel', 'SIDE-lv-conservation', 'SIDE-trivium'}
        and 'SIDE-interfaces/Kernel.lean' in pj, 'the bank and the worklist', '7')
    lvb = gr('D:/SIDE-lv-conservation', 'rev-parse', 'pin-b718-de5ce8a9^')
    add('ruling (8)', 'SIDE-lv-conservation`s bump branch cut from main (its parent d38f3e8c)', lvb.startswith('d38f3e8c'), lvb[:12], '7')
    add('ruling (8)', 'its port at cb0aea56, tag v0.14.0, built at de5ce8a9 (b712)', gr('D:/SIDE-lv-conservation', 'rev-parse', 'v0.14.0^{commit}').startswith('cb0aea56')
        and 'de5ce8a9' in (rd(p('data', 'b712_closing.txt')) or ''), 'v0.14.0 %s' % gr('D:/SIDE-lv-conservation', 'rev-parse', 'v0.14.0^{commit}')[:8], '7')
    a15 = rd(p('data', 'b715_author_answers.txt')) or ''
    add('ruling (8)', 'the author`s answer at b715: each kernel`s pin the revision its own lake-manifest.json carries (data/b715_author_answers.txt)',
        'each kernel’s pin is the revision its own lake-manifest.json carries' in a15, 'the bank', '7')
    wo = [i + 1 for i, l in enumerate(ot) if re.search(r'THE ORDER \*\*`W-ORD-[A-Z0-9-]*(PIN|FEDERATION|BUMP|MATHLIB)', l) and 'PROSE-PINS' not in l and 'STATEMENT-PIN' not in l]
    add('ruling (8)', 'W-ORD entries for the federation pin in OPEN_TRAILS, to be annotated CLOSED', bool(wo), 'orders found %s (the pin named in trails :16056, :16124, :16142, '
        'never as an order)' % (wo or 'NONE'), '7')
    # ### (R331)(9): the carried files and branches
    for repo_, names_ in K.DELETE:
        mg = gr(repo_, 'branch', '--merged', 'main', '--list', 'push-b720-*').replace('*', '').split()
        add('ruling (9)', 'the push-b720-* branches of %s, --merged into main' % repo_.split('/')[-1], sorted(mg) == sorted(names_), ' '.join(mg) or 'NONE', '0')
    stc = gr('D:/relay', 'status', '--porcelain', '--', 'data/b720_relay_push-b720-closing_push_out.txt', 'data/b720_steps.json')
    add('ruling (9)', 'b720`s closing capture untracked and its step-38 row uncommitted', '?? data/b720_relay_push-b720-closing_push_out.txt' in stc
        and 'M data/b720_steps.json' in stc, stc.replace(NL, ' | '), '0')
    add('ruling (9)', 'port-b707 kept (SIDE-lv-conservation, at cb0aea56)', gr('D:/SIDE-lv-conservation', 'rev-parse', 'port-b707').startswith('cb0aea56'), 'local', '0')
    # ### the ferry's read-first list
    r20 = lines_of(p('data', 'b720_registrations.txt'))
    for n, needle in ((7, 'a hand reading at -40 preceded this bank'), (24, "## THE SEAT'S DECLARATION"), (32, 'the row says so'), (79, '## H-RR'),
                      (97, 'PRED-35: n0(-35) = 135')):
        add('ferry (read first)', 'data/b720_registrations.txt :%d: %s' % (n, needle), needle in at(r20, n), at(r20, n)[:80], '0')
    add('ferry (read first)', 'data/b720_derivation.txt (:95-:125)', len(dv) >= 125, 'the bank has %d lines; :95-:%d read, :%d-:125 beyond its end' % (
        len(dv), len(dv), len(dv) + 1), '0')
    add('ferry (read first)', 'data/b719_registrations.txt :46-:59, H-OFFSET', 'H-OFFSET, POST HOC' in at(r19, 46) and 'THE ORDER IT SERVES' in at(r19, 59), at(r19, 46)[:60], '0')
    add('ferry (read first)', 'data/b720_defects.txt (f)', at(dl, 12).startswith("    (f) THE SEAT'S [CLAIM ; NEW]"), at(dl, 12)[:50], '0')
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
    act writes at step zero (v2, (R331)(2)) read as TO BE WRITTEN when absent and from the bank when present."""
    import b718_standing as SC   # ### b721 carry-time repair: the shift named b720_standing, which does not exist; b720 imported b718's
    flat = re.sub(r'“[^”]*”', '', ' '.join(text.split()))
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing clauses(?:’)? v(\d+)', flat, re.I)))
    for v in names or [1]:
        p = os.path.join(D, 'standing_clauses_v%d.txt' % v)
        t = rd(p) or ''
        ver = re.search(r'^VERSION: (\d+)$', t, re.M)
        if v == 1:
            ctl = _jl('b720_standing_control.json')
            add('ferry (standing clauses)', 'the standing clauses v1: data/standing_clauses_v1.txt', bool(t) and bool(ver) and ver.group(1) == '1' and bool(SC.parse(t)) and ctl.get('ok') is True,
                'present %s ; VERSION %s ; rows %d ; the re-assembly control AS WANTED %s' % (bool(t), ver.group(1) if ver else 'NONE', len(SC.parse(t)), ctl.get('ok')), '0')
        elif not t:
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- TO BE WRITTEN at step zero ((R331)(2))' % (v, v), True, 'absent, as ordered', '0')
        else:
            add('ferry (standing clauses)', 'the standing clauses v%d: data/standing_clauses_v%d.txt' % (v, v), bool(ver) and ver.group(1) == str(v), 'present ; VERSION %s' % (ver.group(1) if ver else 'NONE'), '0')


def _write(L, R, miss):
    for n_ in ('b721_citation_check.txt', 'b721_citation_check.json'):
        MEM.guard('b721', n_, _root_exclude())
    for name, data in (('b721_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b721_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        with open(q + '.tmp', 'wb') as fh:
            fh.write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b721 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b721_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b721_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b721_ferry_scan.txt')
    MEM.guard('b721', 'b721_ferry_scan.txt', _root_exclude())
    with open(s + '.tmp', 'wb') as fh:
        fh.write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b721_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
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
    """(R278)(4): b682's route, imported, with its act names pointed at b721, and b706's repair carried."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.C.SESSIONS_AFTER = C.SESSIONS_AFTER
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, K.LV_DIR, K.JOIN_DIR, 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects', 'D:/SIDE-bijection', 'D:/SIDE-interfaces', 'D:/SIDE-li-map',
                                                 'D:/SIDE-kernel') if r not in P.REPOS and os.path.isdir(r))
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b721'))
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
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b721')
    # ### (R331)(2), the item repair: THE WHOLE ANSWER. b682's cut ends at the first "END" after the needle (`best.find('END', k)`, :221), which a
    # ### word carrying END (AMENDMENT, APPENDED, RECOMMENDED) ends inside: b720's answers read 468 characters. The cut now ends at the answer's
    # ### last END (`best.rfind('END')`), the paste's own tail; the substitution printed, the route refusing where it does not apply.
    if body.count("best.find('END', k)") != 1:
        sys.exit('### b682`s CUT NOT FOUND ONCE IN ITS answer -- NOTHING CHECKED')
    body = body.replace("best.find('END', k)", "best.rfind('END')")
    body = body.replace("    open(q + '.tmp', 'wb')", "    MEM.guard('b721', os.path.basename(q), ROOT_EXCLUDE)\n    open(q + '.tmp', 'wb')")
    ns = dict(vars(P))
    ns.update(MEM=MEM, ROOT_EXCLUDE=_root_exclude())
    exec(compile(body, 'b682_citation.answer (b721)', 'exec'), ns)
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
        print('usage: b721_citation.py check [dry] | ferry | answer <needle> | word <needle> | replay <needle> <session id> <anchor>')
        sys.exit(2)
    fn(*sys.argv[2:])
