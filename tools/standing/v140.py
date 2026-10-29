# -*- coding: utf-8 -*-
"""standing/v140.py -- THE CONTROLS OF v1.4.0 ((R334)(2)): for each of the ten repeat classes and the root route, the class's last banked
instance replayed through the route as it stood at HEAD before the repair (the blob read from git, or the literal the template carried) and
through the repaired route; AS WANTED where the old route fails the instance and the new passes it. Both instances printed. Written at b724
by the Write tool.

  python -X utf8 tools/standing/v140.py control [i|ii|...|x|root ...] [--bank]
        runs the named controls (all where none is named); --bank writes data/<act>_standing_v140.txt (the act read from
        data/act_current.json) with every control run, nothing else.

The old routes are read at BASE (the commit before v1.4.0's, given in the bank's head), each into a temporary directory removed on exit;
nothing in the tree is written but the bank.
"""
import hashlib
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time

T = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RELAY = os.path.dirname(T)
D = os.path.join(RELAY, 'data')
S = os.path.join(T, 'standing')
NL = '\n'
PP = 'D:/MY-DOwnloads/PLACE-papers'
for p_ in (S, T):
    if p_ not in sys.path:
        sys.path.insert(0, p_)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import act as A                 # noqa: E402
import hook as H                # noqa: E402
import standing.repeat as RP    # noqa: E402

BASE = 'HEAD'   # ### the routes before the repair: v1.4.0's files are uncommitted when the controls run, so HEAD carries v1.3.0's
TMP = tempfile.mkdtemp(prefix='v140_')


def _git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace').stdout


def blob(rel, rev=None, repo=RELAY):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev or BASE, rel)], capture_output=True)
    return r.stdout if r.returncode == 0 else None


def old_module(rel, name):
    """the module at BASE, loaded from a temporary copy under its own name (the live module untouched)"""
    p = os.path.join(TMP, name + '.py')
    with open(p, 'wb') as f:
        f.write(blob(rel))
    spec = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def case(L, cls, what, old, new, old_fails, new_passes):
    ok = bool(old_fails) and bool(new_passes)
    L += ['  (%s) %s' % (cls, what), '      BEFORE (v1.3.0): %s -> %s' % (old, 'FAILS' if old_fails else 'DOES NOT FAIL'),
          '      AFTER  (v1.4.0): %s -> %s' % (new, 'PASSES' if new_passes else 'DOES NOT PASS'),
          '      %s' % ('AS WANTED' if ok else 'NOT AS WANTED')]
    return ok


def _run(argv):
    r = subprocess.run([sys.executable, '-X', 'utf8'] + argv, capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=RELAY)
    return r.returncode, (r.stdout or '') + (r.stderr or '')


# ================================================================================ (i) HOOK REFUSALS: THE READER'S MISSING VERBS
def control_i():
    """v1.3.0's (ii) control classed three b721-b722 refusals COVERED IN PART: a tally (b721 :6), a python -c read of a JSON bank (b721 :7)
    and a read by byte offset (b722 :9). Each replayed through peek.py at BASE and now."""
    L = ['### (i) HOOK REFUSALS -- tools/standing/peek.py`s tally, json and bytes verbs; instances data/b721_hook_refusals.txt :6, :7 and '
         'data/b722_hook_refusals.txt :9 (v1.3.0`s three COVERED IN PART rows)']
    old = os.path.join(TMP, 'peek_old.py')
    with open(old, 'wb') as f:
        f.write(blob('tools/standing/peek.py'))
    calls = (('b721 :6, `grep -on K.* | sort | uniq -c`', ['tally', 'tools/b721_record.py', '--pattern', r'K\.[A-Z][A-Z0-9_]*', '--max', '3']),
             ('b721 :7, `python -c` over data/arm_tags.json', ['json', 'data/arm_tags.json', 'tags', '--len']),
             ('b722 :9, body[229845:241338] of tools/b722_record.py', ['bytes', 'tools/b722_record.py', '--offset', '229845', '--bytes', '11493']))
    g = n = 0
    for what, argv in calls:
        r0, o0 = _run([old] + argv)
        r1, o1 = _run([os.path.join(S, 'peek.py')] + argv)
        shell = 'python -X utf8 tools/standing/peek.py ' + ' '.join('"%s"' % a if ' ' in a or '|' in a else a for a in argv)
        allowed = H.judge('Bash', {'command': shell}) is None
        n += 1
        g += case(L, 'i', what, 'exit %d (%d lines)' % (r0, len(o0.strip().split(NL))), 'exit %d (%d lines) ; the hook allows the call %s' % (
            r1, len(o1.strip().split(NL)), allowed), r0 != 0, r1 == 0 and allowed)
    return L, g, n


# ================================================================================ (ii) A READ WITH A LIMIT AND NO OFFSET ON 200+ LINES
def control_ii():
    """b723 (b'): 27 of 327 Read calls offended the offset rule (data/b723_read_calls.txt), the hook refusing only a limit above 200. Every
    offence of a limit with no offset on a file of 200+ lines, its file present now, judged by hook.py at BASE and now."""
    L = ['### (ii) READ WITH A LIMIT AND NO OFFSET -- tools/standing/hook.py judge(); instance b723 (b`) (data/b723_read_calls.txt, its offence rows)']
    H0 = old_module('tools/standing/hook.py', 'hook_v130')
    rows = []
    for l in open(os.path.join(D, 'b723_read_calls.txt'), encoding='utf-8').read().split(NL):
        p = [x.strip() for x in l.split('|')]
        if len(p) >= 7 and p[3] == 'offset None' and p[4].startswith('limit ') and 'WITHIN' not in p[5]:
            rows.append((p[0], int(p[4].split()[1]), p[6]))
    over = [r for r in rows if r[1] > H.LIMIT]   # ### a limit above 200: refused by v1.3.0 already, outside this class
    rows = [r for r in rows if r[1] <= H.LIMIT]
    L.append('  offence rows whose limit was above 200 (v1.3.0 refused them already; not this class`s instance): %d' % len(over))
    present = [r for r in rows if os.path.isfile(r[2]) and H.lines_of(r[2]) >= H.LIMIT]
    old_allow = sum(1 for _ln, lim, path in present if H0.judge('Read', {'file_path': path, 'limit': lim}) is None)
    new_refuse = sum(1 for _ln, lim, path in present if (H.judge('Read', {'file_path': path, 'limit': lim}) or ('',))[0] == 'READ')
    with_off = sum(1 for _ln, lim, path in present if H.judge('Read', {'file_path': path, 'offset': 1, 'limit': min(lim, 200)}) is None)
    L.append('  offence rows with a limit and no offset: %d ; their file present now at 200+ lines: %d' % (len(rows), len(present)))
    ok = case(L, 'ii', 'the %d calls, each as logged' % len(present), 'allowed %d of %d' % (old_allow, len(present)),
              'refused READ %d of %d ; the same calls given an offset allowed %d of %d' % (new_refuse, len(present), with_off, len(present)),
              bool(present) and old_allow == len(present), bool(present) and new_refuse == len(present) and with_off == len(present))
    return L, int(ok), 1


# ================================================================================ (iii) HAND-KEPT NAME LISTS
def control_iii():
    L = ['### (iii) HAND-KEPT NAME LISTS -- CARRIED_FAILING, the record-committed pre-push reading, the seal`s list, --prev`s OWN']
    g = n = 0
    # ### (a) b723 (g'): the template's literal against the face's declaration
    tpl0 = blob('tools/standing/fold/checks.tpl').decode('utf-8')
    lit = re.search(r"^CARRIED_FAILING = (\(.*\))$", tpl0, re.M).group(1)
    old = tuple(re.findall(r"'(G-[A-Z0-9-]+)'", lit))
    face = open(os.path.join(D, 'b723_registration_2026-10-29.txt'), encoding='utf-8').read()
    decl = RP.carried_failing(face)
    n += 1
    g += case(L, 'iii', 'b723 (g`): CARRIED_FAILING against b723`s face (data/b723_registration_2026-10-29.txt, its DECLARED line %s)' % (decl,),
              'the template literal %s' % (old,), 'read from the face: %s' % (RP.carried_failing(face),), old != decl, RP.carried_failing(face) == decl and bool(decl))
    # ### (b) b723 event (16): a part run with no mode after the record commit read PRE-PUSH and wrote over the committed bank
    committed = RP.record_committed('b723', RELAY)
    try:
        RP.prepush_after_record('b723', RELAY, False, False)
        refused = False
    except SystemExit:
        refused = True
    n += 1
    g += case(L, 'iii', 'b723 event (16): `fold.py checks --part act` after the record commit (data/b723_components.txt at HEAD %s), read PRE-PUSH' % committed,
              'main ran the part pre-push and wrote data/b723_checks_act.txt over its committed bank', 'part_guards refuses: %s' % refused,
              committed, refused)
    # ### (c) b722 event (12): the seal's own list against the worklist
    sj = json.load(open(os.path.join(D, 'b722_seal_hashes.json'), encoding='utf-8'))
    seal_tools = sorted(sj.get('tools') or {})
    import close as C
    wl = C.worklist_sealed('b722')
    grown = [t for t in wl if t.startswith('standing/') and t not in seal_tools]
    wl = [t for t in wl if t not in grown]   # ### tools/standing/ has grown since b722's seal (b722's worklist lists the directory at import)
    L.append('  tools/standing/ files added since b722`s seal, read out of both sides: %d' % len(grown))
    m0, x0 = RP.seal_against_worklist(seal_tools, wl)
    m1, x1 = RP.seal_against_worklist([t for t in C.worklist_sealed('b722') if t not in grown], wl)
    n += 1
    g += case(L, 'iii', 'b722 event (12): the seal`s tools against b722`s worklist SEALED (%d)' % len(wl),
              'b722`s seal (sealed_list`s rule, %d): missing %s extra %s' % (len(seal_tools), m0, x0),
              'the seal route reads the worklist (worklist_sealed, v1.3.0): missing %s extra %s' % (m1, x1), bool(m0 or x0), not (m1 or x1))
    # ### (d) b722 events (8)-(10): `--prev` at b723 over b722's worklist, names b722's sets to None
    import b722_worklist as W722
    import b723_worklist as W723
    nones = sorted(k for k in dir(W722) if k.isupper() and getattr(W722, k) is None and getattr(W723, k, None) is not None)
    own0 = ('ACT_ARMS', 'PARTS', 'HOLD', 'CHAIN_HALVES', 'CHAIN_QUARTERS', 'STANDING_ADDED')
    old_none = [k for k in nones if k not in own0 and hasattr(W722, k)]
    new_none = [k for k in nones if k not in own0 and RP.prev_carries(W722, W723, k)]
    n += 1
    g += case(L, 'iii', 'b722 events (8)-(10): --prev`s worklist, the %d names b722`s sets to None where b723`s carries a value (%s)' % (
        len(nones), ', '.join(nones[:8])), 'hasattr: %d read as b722`s None' % len(old_none), 'prev_carries: %d read as None' % len(new_none),
        bool(old_none), not new_none)
    return L, g, n


# ================================================================================ (iv) THE LOCK PHASE AND THE STEP RECORDER'S PHASES
def control_iv():
    L = ['### (iv) THE LOCK PHASE -- the step recorder`s phases and G-SEALED-AFTER-COMPONENTS over b723`s step bank and commits']
    g = n = 0
    tpl0 = blob('tools/standing/fold/record.tpl').decode('utf-8')
    pre0 = re.search(r"^PRE_SEAL_PHASES = (\(.*?\))", tpl0, re.M).group(1)
    pre1, post1 = RP.phases(RELAY)
    n += 1
    g += case(L, 'iv', 'the phase `lock` (data/act_current.json`s Component 6 names it before `seal`) among the recorder`s pre-seal phases',
              'the template`s literal: `lock` %s' % ("'lock'" in pre0), 'read from act_current: `lock` %s ; %s' % ('lock' in pre1, ', '.join(pre1)),
              "'lock'" not in pre0, 'lock' in pre1 and 'seal' in post1)
    rows = json.load(open(os.path.join(D, 'b723_steps.json'), encoding='utf-8'))['rows']

    def log(repo, a, b):
        out = _git(repo, 'log', '--format=%H%x09%s%x09%ct', '%s..%s' % (a, b))
        return [(x.split('\t')[0], x.split('\t')[1], int(x.split('\t')[2])) for x in out.split(NL) if x.strip()]
    rlog = log(RELAY, '1607e994dd6c98250428d8197665bf440950e5ca', 'b8334f17')
    plog = log(PP, '1553808a9278e28e2e819e4f39008bd3df37d54b', '698fe441')
    pre723 = tuple(re.findall(r"'([^']+)'", pre0)) + ('lock',)   # ### b723's own phases (the BASE literal, its components 7 and 8), `lock` its override's
    ok0, why0 = RP.sealed_after(rows, rlog, plog, pre723, lambda repo, h: [], 'b723')
    ok1, why1 = RP.sealed_after(rows, rlog, plog, pre723, RP.files_of(RELAY, PP), 'b723')
    n += 1
    g += case(L, 'iv', 'b723`s G-SEALED-AFTER-COMPONENTS (relay 1607e994..b8334f17, %d commits; PLACE-papers ..698fe441, %d)' % (len(rlog), len(plog)),
              'no bookkeeping exemption: %s (%s)' % (ok0, why0), 'the bookkeeping-only commit exempt: %s%s' % (ok1, (' (%s)' % why1) if why1 else ''),
              not ok0, ok1)
    return L, g, n


# ================================================================================ (v) ROUTES READING RETIRED BANKS OR UNWRITTEN TOOL FILES
def control_v():
    L = ['### (v) RETIRED READS -- every template line reading a retired bank or a tools/<act>_<tool>.py the fold does not write, over b724`s names']
    import fold as F
    old = new = 0
    det = []
    for tool in F.TOOLS:
        rel = 'tools/standing/fold/%s.tpl' % tool
        t0 = blob(rel).decode('utf-8').replace(chr(0x27EA) + 'ACT' + chr(0x27EB), 'b724')
        t1 = open(os.path.join(RELAY, *rel.split('/')), encoding='utf-8').read().replace(chr(0x27EA) + 'ACT' + chr(0x27EB), 'b724')
        h0, h1 = RP.retired_reads(t0, 'b724', T), RP.retired_reads(t1, 'b724', T)
        old, new = old + len(h0), new + len(h1)
        det += ['      %s :%d %s' % (tool, i, w) for w, i in h0]
    L += ['  the reads at BASE:'] + det
    ok = case(L, 'v', 'the seven templates read with b724`s names', 'reads %d' % old, 'reads %d (the text through standing/repeat.py src, the run through argv)' % new,
              old > 0, new == 0)
    return L, int(ok), 1


# ================================================================================ (vi) THE CHAIN PHASE ABOVE 450 S
def control_vi():
    L = ['### (vi) THE CHAIN PHASE -- b2a re-cut where b723`s banked first-parent walks halve; seconds PROJECTED from b723`s timings by walk share']
    reads = {}
    for h in ('a1', 'a2'):
        reads.update(json.load(open(os.path.join(D, 'b723_chain_half_%s_checks.json' % h), encoding='utf-8'))['reads'])
    secs = {}
    for part in ('b2a', 'b2b'):
        j = json.load(open(os.path.join(D, 'b723_arm_seconds_standing-%s.json' % part), encoding='utf-8'))
        secs[part] = float(j.get('run_secs') or 0)
    q_old = (('b624', 'b641'), ('b642', 'b658'))
    q_new = RP.quarters(reads, 'b624', 'b658')

    def walk(a, b):
        return sum(int(r.get('later', 0)) for k, r in reads.items() if a <= k <= b)
    w_a1, w_a2 = walk(*q_old[0]), walk(*q_old[1])
    # ### a part's seconds as a fixed cost (the part's own reads, the same in each) and a cost per walk, solved from b723's two measured parts
    per = (secs['b2a'] - secs['b2b']) / (w_a1 - w_a2)
    fixed = secs['b2b'] - per * w_a2
    proj = [fixed + per * walk(*q) for q in q_new]
    wl = __import__('b724_worklist')
    L.append('  b723 measured: b2a %.0f s over walks %d (%s-%s) ; b2b %.0f s over walks %d ; fixed %.0f s + %.3f s a walk ; the worklist`s CHAIN_QUARTERS now %s' % (
        secs['b2a'], w_a1, q_old[0][0], q_old[0][1], secs['b2b'], w_a2, fixed, per, wl.CHAIN_QUARTERS))
    ok = case(L, 'vi', 'the chain`s first half in two parts against the 450 s guard',
              'quarters %s: b2a %.0f s MEASURED' % (q_old, secs['b2a']),
              'quarters %s: b2a %.0f s, b2b %.0f s PROJECTED (walks %d and %d)' % (q_new, proj[0], proj[1], walk(*q_new[0]), walk(*q_new[1])),
              secs['b2a'] > 450, all(p < 450 for p in proj) and tuple(map(tuple, wl.CHAIN_QUARTERS)) == tuple(q_new))
    return L, int(ok), 1


# ================================================================================ (vii) SUITE PARTS RUN CONCURRENTLY
def control_vii():
    L = ['### (vii) CONCURRENT PARTS -- b723 event (13): act and standing-a started while standing-b2a ran; the process table replayed']
    table = [(1001, 'python -X utf8 -u tools/standing/fold.py checks --part standing-b2a'),
             (1002, 'python -X utf8 tools/standing/fold.py checks --part act')]
    old_seen = []   # ### v1.3.0's main read no process table
    new_seen = RP.others_running(table, {1002})
    live = RP.others_running(RP.process_table(), {os.getpid(), os.getppid()})
    g = case(L, 'vii', 'part act (pid 1002) starting beside standing-b2a (pid 1001)', 'parts seen running %s: the part ran' % old_seen,
             'parts seen running %s: refused ; the live table now %s' % (new_seen, live or 'none (a part may start)'), not old_seen, bool(new_seen) and not live)
    return L, int(g), 1


# ================================================================================ (viii) THE PREVIOUS ACT'S WINDOW
def control_viii():
    L = ['### (viii) THE PREVIOUS ACT`S WINDOW -- G-EDIT-ROUTE`s window over b723, read in this one session: to the session`s end (the carried own-session form) '
         'and to b724`s anchor']
    import edit_route as ER
    import b724_worklist as K
    proj = os.path.join(os.path.expanduser('~'), '.claude', 'projects', 'D--')
    sess = os.path.join(proj, K.SESSION_ID + '.jsonl')
    subs = os.path.join(proj, K.SESSION_ID, 'subagents')
    rows = ER.capture(sess, K.PREV_ANCHOR, subs)
    own = ER.capture(sess, K.ANCHOR, subs)
    first = [r['ts'] for r in rows if 'b723_checks_postpush' in r['cmd'] and '--combine' in r['cmd']]
    anchor = min(r['ts'] for r in own) if own else None
    f0 = first[0] if first else ''
    old = [r for r in rows if f0 <= r['ts']]
    new = [r for r in rows if f0 <= r['ts'] < anchor] if anchor else []
    old_own = sum(1 for r in old if anchor and r['ts'] >= anchor)
    new_own = sum(1 for r in new if r['ts'] >= anchor)
    L.append('  b723`s post-push combine at %s ; b724`s anchor at %s ; b724`s commands %d' % (f0 or '-', anchor or '-', len(own)))
    L.append('  NOTE: the template at BASE already ends the window at the act`s anchor (record.tpl prev_capture, a carry-time repair of b723`s); '
             'BEFORE below is the carried own-session form (to the session`s end) that bound replaced, not a v1.3.0 line -- no v1.4.0 edit')
    g = case(L, 'viii', 'the window`s rows that are b724`s own commands', 'to the session`s end: %d rows, %d of them b724`s' % (len(old), old_own),
             'to b724`s anchor: %d rows, %d of them b724`s' % (len(new), new_own), bool(first) and old_own > 0, bool(first) and new_own == 0 and bool(new))
    return L, int(g), 1


# ================================================================================ (ix) THE CARRY'S ACT-NAME SUBSTITUTION
def control_ix():
    L = ['### (ix) THE CARRY`S SUBSTITUTION -- b724 (d): tools/b723_address_scan.py carried to b724 named b723_llm_line, which no act wrote']
    src = blob('tools/b723_address_scan.py', rev='HEAD')
    src = src.decode('utf-8') if src else open(os.path.join(T, 'b723_address_scan.py'), encoding='utf-8').read()
    subs = (('b723', 'b724'), ('b722', 'b723'), ('R333', 'R334'), ('R332', 'R333'))
    out = src
    for a, b in subs:
        out = out.replace(a, b)
    shifted = RP.shifted_missing(src, out, T)
    tmp_dst = os.path.join(TMP, 'carry_dst.py')
    rc, o = _run([os.path.join(S, 'carry.py'), 'tools/b723_address_scan.py', tmp_dst,
                  'v140probe', '--subs', ','.join('%s:%s' % s for s in subs)])
    written = os.path.exists(tmp_dst)
    g = case(L, 'ix', 'the b723 -> b724 carry of tools/b723_address_scan.py', 'tools/b724_carry.py`s substitute wrote it, shifted names unread (%s)' % (
        ', '.join(':%d %s' % s for s in shifted) or 'none'), 'tools/standing/carry.py: exit %d, written %s ; %s' % (
        rc, written, (o.strip().split(NL) or [''])[0][:110]), bool(shifted), rc != 0 and not written and 'PAST WHAT EXISTS -- NOTHING WRITTEN' in o)
    return L, int(g), 1


# ================================================================================ (x) A FIXED GRADE SENTENCE BEFORE ITS CHECK
def control_x():
    L = ['### (x) A FIXED GRADE -- b721 (i): tools/b721_derivation.py printed "READ BY IT AS WANTED" as fixed text while its check (4) read NOT AS WANTED']
    check4 = False   # ### b721 (i): check (4) at -47 read NOT AS WANTED
    old = 'READ BY IT AS WANTED'
    new = RP.grade(check4, 'READ BY IT AS WANTED', 'NOT AS WANTED')
    try:
        RP.grade(None, 'READ BY IT AS WANTED', 'NOT AS WANTED')
        unread = 'composed'
    except (ValueError, SystemExit, TypeError) as e:
        unread = 'refused (%s)' % type(e).__name__
    g = case(L, 'x', 'the grade sentence with its check (4) False', 'fixed text: "%s"' % old, 'repeat.grade: "%s" ; an unread check %s' % (new, unread),
             old != 'NOT AS WANTED', new == 'NOT AS WANTED' and unread.startswith('refused'))
    return L, int(g), 1


# ================================================================================ THE ROOT ROUTE
def control_root():
    """b723's root named data/b723_bank_hashes.json at 133004c8, a blob no commit carries; b723's root banks were committed at f585420f.
    The replay at f585420f: every named relay bank's recorded hash against its blob there, with the hashes bank named (the route as it was)
    and excluded (the route repaired, record.tpl's head declaration read)."""
    L = ['### THE ROOT ROUTE -- b723`s root items replayed at f585420f (b723`s root banks` commit)']
    import act_root as AR
    J = json.load(open(os.path.join(D, 'b723_act_root.json'), encoding='utf-8'))
    items = [it for it in J['items'] if it.startswith('data/')]
    decl = re.findall(r'^### UNTRACKED WRITE: data/(?:\u27eaACT\u27eb|b72\d)_(\S+)', open(os.path.join(S, 'fold', 'record.tpl'), encoding='utf-8').read(), re.M)
    excluded = ['data/b723_' + d for d in decl]

    def at(rev, its):
        bad = []
        for it in its:
            path, h = it.split()[:2]
            b = blob(path, rev=rev)
            if b is None or hashlib.sha256(b).hexdigest() != h:
                bad.append(path)
        return bad
    bad0 = at('f585420f', items)
    kept = [it for it in items if it.split()[0] not in excluded]
    bad1 = at('f585420f', kept)
    r1 = AR.root_of([it for it in J['items'] if it.split()[0] not in excluded], J['previous'])
    L.append('  the template`s head declares %s ; named relay banks %d, %d with the hashes bank excluded' % (excluded, len(items), len(kept)))
    L.append('  the root over the remaining items (printed only, not recorded): %s ; b723`s recorded root %s' % (r1, J['root']))
    g = case(L, 'root', 'b723`s named banks at f585420f', 'the hashes bank named: %d DISAGREE (%s)' % (len(bad0), ', '.join(bad0[:4])),
             'excluded: %d disagree%s' % (len(bad1), (' (%s)' % ', '.join(bad1[:4])) if bad1 else ' -- AGREE'), bool(bad0), not bad1 and bool(kept))
    return L, int(g), 1


CONTROLS = dict(i=control_i, ii=control_ii, iii=control_iii, iv=control_iv, v=control_v, vi=control_vi, vii=control_vii, viii=control_viii,
                ix=control_ix, x=control_x, root=control_root)
ORDER = ('i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'root')


def main(argv):
    if not argv or argv[0] != 'control':
        sys.exit(__doc__)
    names = [a for a in ORDER if a in argv[1:]] or list(ORDER)
    act = A.current().get('act')
    out = ['%s -- THE CONTROLS OF tools/standing/ v1.4.0, (R334)(2): THE TEN REPEAT CLASSES AND THE ROOT ROUTE (%s)' % (
        act, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
           '### the routes before the repair read at %s (%s); each case its instance through both' % (BASE, _git(RELAY, 'rev-parse', '--short=8', BASE).strip()), '']
    tg = tn = 0
    try:
        for k in names:
            try:
                L, g, n = CONTROLS[k]()
            except Exception as e:  # noqa: BLE001
                L, g, n = ['### (%s) THE CONTROL RAISED %s: %s -- NOT AS WANTED' % (k, type(e).__name__, e)], 0, 1
            out += L + ['']
            tg, tn = tg + g, tn + n
    finally:
        shutil.rmtree(TMP, ignore_errors=True)
    out.append('### ### **v1.4.0: CONTROLS %s ; CASES %d ; AS WANTED %d ; %s.**' % (
        ', '.join('(%s)' % k for k in names), tn, tg, 'ALL AS WANTED' if tg == tn else 'NOT ALL AS WANTED'))
    print(NL.join(out))
    if '--bank' in argv:
        p = os.path.join(D, '%s_standing_v140.txt' % act)
        with open(p + '.tmp', 'wb') as f:
            f.write((NL.join(out) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
        print('written data/%s_standing_v140.txt' % act)


if __name__ == '__main__':
    main(sys.argv[1:])
