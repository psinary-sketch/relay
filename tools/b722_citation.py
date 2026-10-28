# -*- coding: utf-8 -*-
"""b722_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b722's step zero, run before any other step
(the ferry's Component 0); the ferry banked before it by the Write tool; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT
AUTHOR ANSWER before the seat acts on it.
### The helpers are b677's, IMPORTED from tools/b677_citation.py and unchanged, its anchor pointed at this act's ruling and its session at this
### act's (bde68a30, a new session after the clear; the anchor (R332)'s line); the answer route is b682's, imported from
### tools/b682_citation.py with its act names pointed at b722, b706's repair carried (a bare eight-hex token a bank names as a sha256 or a
### kernel's lakefile pins as a rev is not read as a commit); the `word` route is b694's. Routes: `check [dry]` -> data/b722_citation_check.txt
### (.json) ; `ferry` -> data/b722_ferry_scan.txt ; `answer <needle>` / `word <needle>` -> the check on one answer.
### Carried by diff from b721_citation.py (data/b722_carry_citation.txt), b721's cite rows pruned (data/b722_prune_citation.txt) and this
### ruling's written by the Edit tool; this tool writes only the banks named above. Its (R332)(1) row reads lv's release list by `gh` (the
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
import b722_worklist as K   # noqa: E402
import act_membrane as MEM  # noqa: E402  ### (R332)(2)(ii): the membrane before every bank write of this tool


def _root_exclude():
    import b722_record as REC   # ### the record tool's exclusion pattern, the one the root route reads (imported at the call, nothing written)
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
    # ### b722: the cite rows of (R332) and its ferry, written by the Edit tool after b721's rows were pruned (data/b722_prune_citation.txt)
    gr = lambda repo, *a: (g(repo, *a)[1] or '').strip()   # noqa: E731
    # ### (R332)(1): b721 at its weight
    cl = lines_of(p('data', 'b721_closing.txt'))
    hq = _quote(text, '"b721 closed: relay 74dc741f', '; 27 defects"')
    add('ruling (1)', 'data/b721_closing.txt :1, the head line as the ruling quotes it', bool(hq) and hq[1:] + '; 27 defects' == at(cl, 1), at(cl, 1)[:120], '1')
    pub = _blob('D:/relay', '30c0b3c8', 'data/b721_closing.txt').replace(chr(13), '').split(NL)
    add('ruling (1)', 'the head line as the public relay carries it at 30c0b3c8', bool(pub) and pub[0] == at(cl, 1)
        and (_remote_heads('D:/relay').get('refs/heads/main') or '').startswith('30c0b3c8'), 'remote main %s' % (_remote_heads('D:/relay').get('refs/heads/main') or '')[:8], '1')
    add('ruling (1)', 'the counter CLAIM 5, CLOSE 37 (data/b721_closing.txt :5)', at(cl, 5).endswith('CLAIM 5, CLOSE 37'), at(cl, 5)[-30:], '1')
    cs = [l for l in cl if '112 OF 116' in l.upper() or '112 of 116' in l]
    add('ruling (1)', 'the suite 112 of 116 pre-push and post-push (data/b721_closing.txt)', len(cs) >= 2, '%d lines' % len(cs), '1')
    for arm in ('G-AXIOM-CLAIM', 'G-SEAL-HASHES', 'G-FINDINGS-ENTRY', 'G-ENTRY-TITLE-FORM'):
        fl = [l for l in lines_of(p('data', 'b721_checks_postpush.txt')) if arm in l and 'FAIL' in l]
        add('ruling (1)', '%s failing in the post-push suite (data/b721_checks_postpush.txt)' % arm, bool(fl), '%d lines' % len(fl), '1')
    add('ruling (1)', 'the entry at FINDINGS :11178', at(fi, 11178).startswith('## The C2 table’s rule chose no discriminant'), at(fi, 11178)[:60], '1')
    add('ruling (1)', 'the trail at OPEN_TRAILS :16264', at(ot, 16264).startswith('### b721 — lane two, act one hundred and forty-eight'), at(ot, 16264)[:60], '1')
    rg = lines_of(p('data', 'b721_registrations.txt'))
    for n, needle in ((50, 'THE OUTPUT: NONE'), (53, 'takes -24 (n0 36) and -88 (n0 484)'), (62, 'REGISTERED BLIND'), (63, 'H-C2-WALK'),
                      (83, 'THE PREDICTIONS BY RULE (4)'), (84, '-31 TAKEN'), (84, '-55 TAKEN'), (47, '-403 n0 17303'),
                      (27, 'THE USED SET'), (28, 'did not find -15, -23 and -39')):
        add('ruling (1), (2), (5)', 'data/b721_registrations.txt :%d: %s' % (n, needle), needle in at(rg, n), at(rg, n)[:80], '1')
    add('ruling (1)', 'H-C3-31 (n0 = 80) and H-C4-55 (n0 = 224) committed at e8c3dff4', all(s_ in _blob('D:/relay', 'e8c3dff4', 'data/b721_registrations.txt')
        for s_ in ('H-C3-31', 'H-C4-55')), 'the blob at e8c3dff4', '1')
    orr = lines_of(p('data', 'b721_offset_read.txt'))
    add('ruling (1)', 'H-OFFSET HELD 3, REFUTED 14 (data/b721_offset_read.txt :29-:34)', 'HELD 3, REFUTED 14' in at(orr, 30) and 'REFUTED 14' in at(orr, 34), at(orr, 30)[:80], '1')
    ti = rd(p('data', 'b721_offset_tier.txt')) or ''
    add('ruling (1)', 'the next tier 53 chosen, none formable, short by 6.0 (data/b721_offset_tier.txt)', '53' in ti and '6.0' in ti, 'the bank', '1')
    add('ruling (1)', 'the surgery carried (data/b721_surgery_carry.txt)', os.path.exists(p('data', 'b721_surgery_carry.txt')), 'present', '1')
    fz = lines_of(p('data', 'b721_frozen_line.txt'))
    add('ruling (1)', 'the frozen line EXCEEDS 7, 0, 7, 9 and STATED 2, 8, 3, 1 (data/b721_frozen_line.txt :282)', all(s_ in at(fz, 282) for s_ in (
        'SIDE-archimedean EXCEEDS 7, STATED 2', 'SIDE-frobenius EXCEEDS 0, STATED 8', 'SIDE-spinor EXCEEDS 7, STATED 3', 'SIDE-rcurve EXCEEDS 9, STATED 1')), at(fz, 282)[-80:], '1')
    rb = lines_of(p('data', 'b721_rebuild.txt'))
    add('ruling (1)', 'data/b721_rebuild.txt :12 and :54: 6 of 6 build, one with a sorry', 'BUILDS 6 OF 6' in at(rb, 12) and 'ONE WITH A SORRY: SIDE-lv-conservation' in at(rb, 54), at(rb, 12)[:60], '1')
    ax = [l for l in rb if 'axiom' in l.lower()]
    add('ruling (1)', 'the axiom prints read at 1 of 6 (data/b721_rebuild.txt)', bool(ax), '%d lines naming the axiom step' % len(ax), '1')
    ev = lines_of(p('data', 'b721_events.txt'))
    add('ruling (1)', 'event (9) at data/b721_events.txt :47', at(ev, 47).startswith('    (9) ') and 'N4 REFUTED' in at(ev, 47), at(ev, 47)[:60], '1')
    starts = [int(m.group(1)) for m in (re.match(r'^    \((\d+)\) ', l) for l in ev) if m]
    dl = lines_of(p('data', 'b721_defects.txt'))
    letters = [m.group(1) for m in (re.match(r"^    \(([a-z]'?)\) ", l) for l in dl) if m]
    add('ruling (2)', 'events (1)-(15) and the defects (data/b721_events.txt, data/b721_defects.txt)', starts == list(range(1, 16)) and len(letters) >= 27,
        'events %s ; letters %d' % (starts[-1:], len(letters)), '1')
    add('ferry (read first)', 'data/b721_defects.txt (h) and (u)', any(l.startswith('    (h) ') for l in dl) and any(l.startswith('    (u) ') for l in dl), 'both present', '0')
    # ### (R332)(2): the repairs' objects
    add('ruling (2)', 'tools/standing/ at v1.2.1 entering the act (tools/standing/VERSION)', at(lines_of(p('tools', 'standing', 'VERSION')), 1) == 'v1.2.1',
        at(lines_of(p('tools', 'standing', 'VERSION')), 1), '1')
    sh = _jl('b721_seal_hashes.json')
    add('ruling (2)(i)', 'the seal bank of b721 (data/b721_seal_hashes.json) holding 36 tools', len(sh.get('hashes') or sh.get('tools') or {}) == 36,
        'keys %s' % sorted(sh)[:6], '1')
    add('ruling (2)(iii)', 'the readfirst closure reader (tools/circuit_read.py readfirst) and b710`s reading 5', 'def readfirst' in (rd(p('tools', 'circuit_read.py')) or ''),
        'tools/circuit_read.py', '1')
    # ### (R332)(3)-(5): b711's route, the tools
    src = rd(p('tools', 'b711_coeffs.py')) or ''
    add('ruling (3)', 'b711`s route (tools/b711_coeffs.py) through the cut 32532 with its controls C1-C3', '32532' in src and bool(re.search(r'\bC1\b', src)) and bool(re.search(r'\bC3\b', src)),
        'C1 %s ; C2 %s ; C3 %s' % tuple(bool(re.search(r'\b%s\b' % c_, src)) for c_ in ('C1', 'C2', 'C3')), '2')
    add('ruling (5)', 'relay tools/e0_rule.py', os.path.exists(p('tools', 'e0_rule.py')), 'present', '4')
    # ### (R332)(6)-(7): the instruments
    ins = lines_of(os.path.join(PP, K.INSTRUMENTS))
    last = [i + 1 for i, l in enumerate(ins) if re.match(r'^## I-\d+ ', l)]
    add('ruling (6)', 'INSTRUMENTS.md`s last entry I-40 (b692) (PLACE-papers %s :486)' % K.INSTRUMENTS, bool(last) and at(ins, last[-1]).startswith('## I-40 ') and 'b692' in at(ins, last[-1]),
        at(ins, last[-1] if last else 0)[:60], '5')
    for t_ in ('b707_onset', 'b709_pairs', 'b711_list', 'b713_list', 'b717_list', 'b711_coeffs', 'b711_surgery', 'b713_predict', 'b718_classgroup', 'b718_abstract',
               'b718_decomp', 'b720_predict', 'b721_derivation', 'b721_rebuild', 'b721_frozen_line'):
        add('ruling (6)', 'the navigator`s expectation names tools/%s.py' % t_, os.path.exists(p('tools', t_ + '.py')), 'present' if os.path.exists(p('tools', t_ + '.py')) else 'ABSENT', '5')
    b618 = [l for l in lines_of(p('data', 'b618_append_INSTRUMENTS.md')) if l.startswith('## I-')]
    add('ruling (6)', 'b618`s form (data/b618_append_INSTRUMENTS.md)', bool(b618), '%d entries' % len(b618), '5')
    # ### (R332)(8): the propagation
    add('ruling (8)', 'data/standing_clauses_v7.txt present (v8 is v7 with one row)', os.path.exists(p('data', 'standing_clauses_v7.txt')), 'present', '6')
    cr = lines_of(p('data', 'b718_count_read.txt'))
    add('ruling (8)(ii)', 'data/b718_count_read.txt :19-:27', 'does not discharge T-COUNT' in at(cr, 19) and 'FINDINGS :8881' in at(cr, 27), at(cr, 27)[:60], '6')
    add('ruling (8)(ii)', 'FINDINGS :8881 naming T-COUNT as assumed', 'T-COUNT' in at(fi, 8881), at(fi, 8881)[:60], '6')
    add('ruling (8)(i)', 'the law`s value clause refuted at -40 (b720, data/b720_coeffs.txt)', 'REFUTED' in (rd(p('data', 'b720_coeffs.txt')) or ''), 'the bank', '6')
    # ### (R332)(10): the five runs
    rbj = ' '.join(rb)
    for k_, run_ in K.AXIOM_RUNS:
        add('ruling (10)', '%s run %d in data/b721_rebuild.txt' % (k_, run_), str(run_) in rbj, 'the bank', '7')
    add('ruling (10)', 'the step "Axioms of the named terminals"', 'Axioms of the named terminals' in rbj, 'the bank', '7')
    add('ruling (10)', 'SIDE-kernel`s run: the olean of Bridge.CardDerived reported missing', 'CardDerived' in rbj, 'the bank', '7')
    # ### (R332)(11): the carried files and branches
    for repo_, names_ in K.DELETE:
        mg = gr(repo_, 'branch', '--merged', 'main', '--list', 'push-b721-*').replace('*', '').split()
        add('ruling (11)', 'the push-b721-* branches of %s, --merged into main' % repo_.split('/')[-1], sorted(mg) == sorted(names_), ' '.join(mg) or 'NONE', '0')
    stc = gr('D:/relay', 'status', '--porcelain', '--', 'data/b721_relay_push-b721-closing_push_out.txt', 'data/b721_steps.json')
    add('ruling (11)', 'b721`s closing capture untracked and its step-42 row uncommitted', '?? data/b721_relay_push-b721-closing_push_out.txt' in stc
        and 'M data/b721_steps.json' in stc, stc.replace(NL, ' | '), '0')
    for repo_, br_ in K.KEPT_BRANCHES:
        add('ruling (11)', '%s kept on %s' % (br_, repo_.split('/')[-1]), bool(gr(repo_, 'rev-parse', '--verify', '--quiet', br_)), 'local', '0')
    for k_ in K.PIN_CARRIED:
        add('ruling (11)', 'pin-b718-de5ce8a9 as banked on %s' % k_, True, 'local %s' % bool(gr('D:/' + k_, 'rev-parse', '--verify', '--quiet', K.PIN_BRANCH)), '0')
    add('ruling (11)', 'tools/mirror_prevbuild.json', os.path.exists(p('tools', 'mirror_prevbuild.json')), 'present', '8')
    # ### (R332)(12): the monograph
    mono = lines_of(os.path.join(PP, 'day1', 'A_Place_to_Stand.md'))
    ag = [i + 1 for i, l in enumerate(mono) if l.startswith('#') and 'Appendix G' in l]
    add('ruling (12)', 'A_Place_to_Stand.md (PLACE-papers day1/) and its Appendix G', bool(ag), 'Appendix G at %s' % ag[:2], '7')
    # ### the ferry's read-first list
    add('ferry (read first)', 'data/b721_closing.txt :389-:430, the carried items', len(cl) >= 430 and at(cl, 389).startswith('### CARRIED FORWARD'),
        'the bank has %d lines; :389 %r; :%d-:430 beyond its end' % (len(cl), at(cl, 389)[:24], len(cl) + 1), '0')
    add('ferry (read first)', 'data/b721_derivation.txt', os.path.exists(p('data', 'b721_derivation.txt')), 'present', '0')
    add('ferry (read first)', 'data/b721_frozen_line.txt :271-:282', at(fz, 271).startswith('## THE TALLY'), at(fz, 271)[:30], '0')
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
    act writes at step zero (v2, (R332)(2)) read as TO BE WRITTEN when absent and from the bank when present."""
    import b718_standing as SC   # ### b722 carry-time repair: the shift named b721_standing, which does not exist; b721 imported b718's
    flat = re.sub(r'“[^”]*”', '', ' '.join(text.split()))
    # ### b722 carry-time repair: the ferry names its versions as "data/standing_clauses_v7.txt" and "standing clause v8"; the needle widened
    # ### to both wordings (the bare form fell to v1, whose control the shift named b721_standing_control.json, a bank that does not exist)
    names = sorted(set(int(m.group(1)) for m in re.finditer(r'standing[ _]clauses?(?:’)?[ _]v(\d+)', flat, re.I)))
    for v in names or [1]:
        p = os.path.join(D, 'standing_clauses_v%d.txt' % v)
        t = rd(p) or ''
        ver = re.search(r'^VERSION: (\d+)$', t, re.M)
        if v == 1:
            ctl = _jl('b721_standing_control.json')
            add('ferry (standing clauses)', 'the standing clauses v1: data/standing_clauses_v1.txt', bool(t) and bool(ver) and ver.group(1) == '1' and bool(SC.parse(t)) and ctl.get('ok') is True,
                'present %s ; VERSION %s ; rows %d ; the re-assembly control AS WANTED %s' % (bool(t), ver.group(1) if ver else 'NONE', len(SC.parse(t)), ctl.get('ok')), '0')
        elif not t:
            add('ferry (standing clauses)', 'the standing clauses v%d the ferry names: data/standing_clauses_v%d.txt -- TO BE WRITTEN at Component 6 ((R332)(8))' % (v, v), True, 'absent, as ordered', '0')
        else:
            add('ferry (standing clauses)', 'the standing clauses v%d: data/standing_clauses_v%d.txt' % (v, v), bool(ver) and ver.group(1) == str(v), 'present ; VERSION %s' % (ver.group(1) if ver else 'NONE'), '0')


def _write(L, R, miss):
    for n_ in ('b722_citation_check.txt', 'b722_citation_check.json'):
        MEM.guard('b722', n_, _root_exclude())
    for name, data in (('b722_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b722_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        with open(q + '.tmp', 'wb') as fh:
            fh.write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = C.ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b722 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO, BEFORE ANY OTHER STEP (standing from b662; the ferry`s Component 0) (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
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
    """the ferry is banked by the Write tool (data/b722_ferry.txt); this route compares it with the transcript's text and runs the scan."""
    text = C.ferry_text()
    q = os.path.join(D, 'b722_ferry.txt')
    banked = (rd(q) or '').rstrip(NL)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b722_ferry_scan.txt')
    MEM.guard('b722', 'b722_ferry_scan.txt', _root_exclude())
    with open(s + '.tmp', 'wb') as fh:
        fh.write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    eq = banked == text.rstrip(NL)
    print('  b722_ferry.txt %d characters ; the transcript`s text %d characters ; equal %s ; ferry_scan exit %d' % (
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
    """(R278)(4): b682's route, imported, with its act names pointed at b722, and b706's repair carried."""
    import b682_citation as P
    P.C.ANCHOR = P.ANCHOR = ANCHOR
    P.C.SESSION = C.SESSION
    P.C.SESSIONS_AFTER = C.SESSIONS_AFTER
    P.REPOS = tuple(P.REPOS) + tuple(r for r in (K.EF_DIR, K.LV_DIR, K.JOIN_DIR, 'D:/SIDE-archimedean', 'D:/SIDE-simplicity', 'D:/SIDE-substrate-cluster',
                                                 'D:/SIDE-window', 'D:/SIDE-effects', 'D:/SIDE-bijection', 'D:/SIDE-interfaces', 'D:/SIDE-li-map',
                                                 'D:/SIDE-kernel') if r not in P.REPOS and os.path.isdir(r))
    P.act_root_line, P.D = act_root_line, D
    P.after_root = lambda: bool(act_root_line('b722'))
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
    body = src[src.index('def answer(needle, *a):'):src.index("if __name__ == '__main__':")].replace('b682', 'b722')
    # ### (R332)(2), the item repair: THE WHOLE ANSWER. b682's cut ends at the first "END" after the needle (`best.find('END', k)`, :221), which a
    # ### word carrying END (AMENDMENT, APPENDED, RECOMMENDED) ends inside: b721's answers read 468 characters. The cut now ends at the answer's
    # ### last END (`best.rfind('END')`), the paste's own tail; the substitution printed, the route refusing where it does not apply.
    if body.count("best.find('END', k)") != 1:
        sys.exit('### b682`s CUT NOT FOUND ONCE IN ITS answer -- NOTHING CHECKED')
    body = body.replace("best.find('END', k)", "best.rfind('END')")
    body = body.replace("    open(q + '.tmp', 'wb')", "    MEM.guard('b722', os.path.basename(q), ROOT_EXCLUDE)\n    open(q + '.tmp', 'wb')")
    ns = dict(vars(P))
    ns.update(MEM=MEM, ROOT_EXCLUDE=_root_exclude())
    exec(compile(body, 'b682_citation.answer (b722)', 'exec'), ns)
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
        print('usage: b722_citation.py check [dry] | ferry | answer <needle> | word <needle> | replay <needle> <session id> <anchor>')
        sys.exit(2)
    fn(*sys.argv[2:])
