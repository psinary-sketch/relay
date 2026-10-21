# -*- coding: utf-8 -*-
"""b702_record.py -- THE ACT'S RECORD TOOL, b702 under (R312).

### b698's record tool is IMPORTED (tools/b698_record.py, sealed at b698 and unedited) with its act names rebound to b702 -- its worklist
### module K, ACT and PREV, and EVERY import-time constant b699's traps named (SESSION, SUBAGENTS, the previous act's window, FACE, the mirror
### names, ROOT_EXCLUDE, _standins) rebound here explicitly, the original _anchor_ts captured before the wrapper (b701's trap); b700's repaired
### _defect_short (the act PASSED AT THE CALL) carried by copy; b701's late routes carried by copy with b702's names. The re-cut routes -- the
### tie over kernels and companions, the paper's cut by the b670 method, the quotation search over the papers' tree -- are written here afresh
### on b699's forms; the faces, README and partner-copies routes are this act's. Every python child is started as `python -X utf8`.
### Written by the Write tool at b702 in stages: stage one, step zero's routes; Components 1-6 by the Edit tool.
### Routes: `python tools/b702_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
### are read (data/b690_rules.txt row (1)); no commit is amended at any point (data/b692_rules.txt row (1)).
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

import b702_worklist as K          # noqa: E402
import b698_record as R            # noqa: E402  ### b698's routes, imported unedited
import b701_worklist as K701       # noqa: E402  ### data only

ACT, PREV = 'b702', 'b701'
R.K, R.ACT, R.PREV, R.SP = K, ACT, PREV, K.SP
conv = R.conv                      # ### (R262)(2): the one conversion, b652's, through b698's module
PP, FIND, OT = R.PP, R.FIND, R.OT
utc, rd, rdn, put_json, put_txt, jl, g, grc, land, _show = R.utc, R.rd, R.rdn, R.put_json, R.put_txt, R.jl, R.g, R.grc, R.land, R._show
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'

# ================================================================================ THE IMPORT-TIME CONSTANTS, REBOUND (b699's traps 2 and 4)
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
SUBAGENTS = '%s/%s/subagents' % (PROJ, K.SESSION_ID)
R.SESSION, R.SUBAGENTS = SESSION, SUBAGENTS
# ### the previous act's window: b701 ran and closed in THIS session (e5bcf1d0), so its window is b690's form -- from its anchor to this
# ### act's anchor; its post-push stretch from its post-push combine to (R312)'s line
R.PREV_ACT, R.PREV_SESSION, R.PREV_ANCHOR = PREV, K.SESSION_ID, K.PREV_ANCHOR
R.PREV_SESSION_PATH = SESSION
R.PREV_SUBAGENTS = SUBAGENTS
FACE = os.path.join(D, 'b702_registration_2026-10-21.txt')
FACE_REL = 'data/b702_registration_2026-10-21.txt'
R.FACE, R.FACE_REL = FACE, FACE_REL
R.MIRROR_TAG = '%s-%s' % (K.DATE, ACT)
R.ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % R.MIRROR_TAG
R.STAGE = os.path.join(os.environ.get('TEMP', K.SP), 'mirror-build-%s' % R.MIRROR_TAG)
R.N5_RELAY_DATA = ('act_roots.txt', 'b701_closing_push_out.txt', 'b675_corrigenda.txt')
R.N5_RELAY_TOOLS = ()
R.ROOT_EXCLUDE = re.compile(r'^b702_(defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|chain_.*|'
                            r'act_root.*|root_arm.*|root_banks.*|.*push_out.*|scanfile_.*|seal_check_.*|census_closing|faces_census_closing|pins_closing|'
                            r'commands|mirror.*|close_sentence|read_calls)\.?(txt|json|md|jsonl|)$')

_R_anchor_ts = R._anchor_ts   # ### the original, captured before the rebinding beneath (b701's trap: the wrapper calling R._anchor_ts recursed)


def _anchor_ts(anchor, session=None):
    """b698's _anchor_ts bound its session at definition (b699's trap 1): this one reads this act's session unless another is named."""
    return _R_anchor_ts(anchor, session or SESSION)


R._anchor_ts = _anchor_ts


def _standins():
    """(R267)(2), standing: the stand-ins a dry run reads for the banks not yet written before the lock -- every value marked as a stand-in,
    none a number any bank carries; a stand-in run writes no bank."""
    sk = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')
    return {
        '%s_scores.json' % ACT: dict((k, ['NOT SCORED', 'a stand-in for the dry run']) for k in sk),
        '%s_findings.json' % ACT: dict(entry_line=99999, title='stand-in'),
        '%s_trail.json' % ACT: dict(line=99999),
        '%s_act_root.json' % ACT: dict(root='0' * 64, previous='663799f0' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
    }


R._standins = _standins
READERS = ['read_branch_row', 'read_defect_row', 'read_runner_row', 'read_score_row', 'read_head']
read_branch_row, read_runner_row, _deps = R.read_branch_row, R.read_runner_row, R._deps
read_score_row, read_head = R.read_score_row, R.read_head

# ================================================================================ (R310)(2), CARRIED: THE DEFECTS ROW READER, ITS ACT PASSED AT THE CALL
DEFECT_ROW = R.DEFECT_ROW


def read_defect_row(L, i):
    """one lettered defect row of a defects bank, its continuation lines joined: returns '(x) HEAD' -- the row's text to its first full stop."""
    j = i + 1
    while j < len(L) and L[j].startswith('    ') and not DEFECT_ROW.match(L[j]) and not L[j].startswith('    ###'):
        j += 1
    m = re.match(r"^\(([a-z]'?)\) (.*?)\.(?= |$)", ' '.join(x.strip() for x in L[i:j]))
    return m.group(0)[:-1] if m else None


def _defect_short(act):
    """b700's repair, carried: the act PASSED AT THE CALL -- no default, so nothing is bound at import."""
    if not re.match(r'^b\d{3}$', act or ''):
        raise ValueError('### _defect_short NEEDS THE ACT AT THE CALL, read %r' % (act,))
    L = rdn('%s_defects.txt' % act).split(NL)
    return [s for s in (read_defect_row(L, i) for i, l in enumerate(L) if DEFECT_ROW.match(l)) if s]


R._defect_short = _defect_short
CLOSING_DEFECT = re.compile(r"and \(([a-z])\), (THE [A-Z']+), entered here[^:]*: (.*?) -- ")


def closing_defects(act):
    """b700's route, carried: the defects an act's closing enters in its (g) line and not in its defects bank."""
    L = rdn('%s_closing.txt' % act).split(NL)
    i = next((k for k, l in enumerate(L) if l.startswith('    (g) ')), None)
    if i is None:
        return []
    j = i + 1
    while j < len(L) and L[j].startswith('        '):
        j += 1
    text = ' '.join(x.strip() for x in L[i:j])
    return [('(%s) %s: %s' % (m.group(1), m.group(2), m.group(3)), 'data/%s_closing.txt :%d-:%d' % (act, i + 1, j)) for m in CLOSING_DEFECT.finditer(text)]


def defshort(*a):
    act = a[0] if a else ''
    out = [(s, 'data/%s_defects.txt' % act) for s in _defect_short(act)]
    nb = len(out)
    out += closing_defects(act)
    for s, src in out:
        print('  %s   [%s]' % (s, src))
    print('### ### **%s: DEFECTS %d -- FROM data/%s_defects.txt %d, FROM THE CLOSING`S (g) LINE %d.**' % (act, len(out), act, nb, len(out) - nb))


# ================================================================================ STEP ZERO: ROWGEN, ANSWERS, DEFECTS (b698's routes, carried)
rowgen = R.rowgen
MIDACT = 'MID-ACT, %s, the author' % ACT
PART_HEAD = re.compile(r'^(RESUME\.|\([A-Z]\) [A-Z][A-Z ,\-]*\.)')


def midact_words():
    """the author's mid-act words delivered as a paste with a lead line before BEGIN (b698's route reads a BEGIN only at the text's start): every
    user text of this session after the anchor carrying MIDACT, cut from its first line-initial BEGIN to its last line-initial END, its parts named
    by their line-initial heads (RESUME. and (A)-(Z))."""
    out, seen = [], set()
    for i, o, st, sid in R._session_rows():
        if o.get('type') != 'user' or o.get('isCompactSummary') or i <= st:
            continue
        cs = (o.get('message') or {}).get('content')
        texts = [cs] if isinstance(cs, str) else [c.get('text', '') for c in (cs or []) if isinstance(c, dict) and c.get('type') == 'text']
        for t in texts:
            t = (t or '').replace('\r', '')
            if MIDACT not in t:
                continue
            b = re.search(r'(?m)^BEGIN$', t)
            e = [m for m in re.finditer(r'(?m)^END$', t)]
            if not b or not e or e[-1].start() < b.end():
                continue
            w = t[b.end():e[-1].start()].strip(NL)
            if w in seen:
                continue
            seen.add(w)
            parts = [m.group(1).rstrip('.') for m in (PART_HEAD.match(l) for l in w.split(NL)) if m]
            out.append((i, o.get('timestamp'), w, parts))
    return out


def answers(*a):
    """b698's route, then the mid-act words b698's matcher cannot see appended verbatim, each with its parts named (the author's paste of
    2026-10-21: "banked in the act's answers bank verbatim with this paste's three parts named")."""
    mw = midact_words()
    if 'dry' in a:
        R.answers(*a)
        for i, ts, w, parts in mw:
            print('  mid-act word at transcript line %s (%s): %d characters ; parts %s' % (i, ts, len(w), parts))
        return
    R.answers(*a)
    t = rdn('%s_author_answers.txt' % ACT).rstrip(NL)
    L = t.split(NL)
    m = re.search(r'and (\d+) word\(s\) of the author', L[0])
    if mw and m:
        L[0] = L[0].replace(m.group(0), 'and %d word(s) of the author' % (int(m.group(1)) + len(mw)))
    for i, ts, w, parts in mw:
        named = [p for p in parts if p.startswith('(')]
        L += ['', '### THE AUTHOR`S WORD, MID-ACT (transcript line %s, %s), answers to no raised prompt, BEGIN to END, verbatim; its lead RESUME '
              'and its %d parts named: %s' % (i, ts, len(named), '; '.join(named))] + w.split(NL)
    put_txt('%s_author_answers.txt' % ACT, L + [''])
    print('  mid-act words appended %d: %s' % (len(mw), ['line %s, parts %s' % (i, p) for i, _t, _w, p in mw]))


def defects(*a):
    t = rdn('%s_defects.txt' % ACT)
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('%s_defects.json' % ACT, dict(at=utc(), defects=ds, short=_defect_short(ACT)))
    print('  defects %d' % len(ds))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R312)(8); b701's form)
def branches(*a):
    """`branches before`: data/b702_branches_before.json -- b698's route, carried (every branch (R312)(8) names, its tip resolved, merged into
    main by ancestry, the remote's heads read once per repository; written before any delete). `branches`: data/b702_branches.txt (.json) --
    each branch's fate read now against the tips banked before, in (R312)(8)'s words; the kernel branches raised and widening-b701 kept."""
    if a and a[0] == 'before':
        return R.branches('before')
    before = jl('%s_branches_before.json' % ACT).get('rows') or []
    if not before:
        sys.exit('### data/b702_branches_before.json IS NOT WRITTEN -- NOTHING READ')
    rows = []
    for r in before:
        if r['where'] == 'local':
            gone = not g(r['repo'], 'branch', '--list', r['branch']).strip()
        else:
            gone = r['branch'] not in R._remote_heads(r['repo'])
        rows.append(dict(repo=r['repo'], branch=r['branch'], where=r['where'], tip=r['tip'], merged=r['merged'], fate='DELETED' if gone else 'KEPT'))
    # ### the kernel branches raised as one prompt and deleted on the author's word (data/b702_author_answers.txt): their tips as b701 banked
    # ### them (bridge-b701 = b701's BRIDGE_TIP, merged at v0.35; push-b701-bridge = v0.35's commit), their fate read now
    rh = R._remote_heads(K.KERNEL_DIR)
    for repo, b, where in K.KERNEL_BRANCHES_RAISED:
        tip = K701.BRIDGE_TIP if b == 'bridge-b701' else K.EF_V035
        rows.append(dict(repo=repo, branch=b, where='local', tip=tip, merged=True, fate='DELETED' if not g(repo, 'branch', '--list', b).strip() else 'KEPT'))
        if 'remote' in where:
            rows.append(dict(repo=repo, branch=b, where='remote', tip=tip, merged=True, fate='DELETED' if b not in rh else 'KEPT'))
    for r in rows:
        read_branch_row(r)
    L = ['%s -- STEP ZERO, (R312)(8): THE BRANCHES, READ BEFORE ANY DELETE AND AFTER (%s)' % (ACT, utc()), '',
         '### rows are branches: repository | branch | where | the tip before the delete (data/b702_branches_before.json, read before any delete) |',
         '### merged into main by ancestry | the fate read now. Each delete one branch per command, each its own message, nothing chained after;',
         '### the listing `git branch --merged main` per repository with no pattern. The kernel branches b701 made (bridge-b701, push-b701-bridge)',
         '### raised as one prompt before any delete and deleted on the author`s word alone; widening-b701 = %s KEPT, local and remote, under' % K.WIDEN_TIP[:7],
         '### W-ORD-CLASSK-WIDENING-HELD (deleted under no answer).']
    L += ['  %-22s | %-28s | %-6s | %s | merged %s | %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    wt = g(K.KERNEL_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.WIDEN_BRANCH).strip()
    L += ['', '### widening-b701 at the close of step zero: local %s ; %s' % (wt[:7] or 'ABSENT', 'STANDS' if wt == K.WIDEN_TIP else '### MOVED OR ABSENT')]
    L += ['', '### ### **BRANCHES NAMED %d ; DELETED %d ; KEPT %d ; EVERY TIP MERGED %s ; widening-b701 %s.**' % (
        len(rows), sum(1 for r in rows if r['fate'] == 'DELETED'), sum(1 for r in rows if r['fate'] == 'KEPT'), all(r['merged'] for r in rows),
        'STANDS' if wt == K.WIDEN_TIP else '### MOVED OR ABSENT')]
    put_txt('%s_branches.txt' % ACT, L)
    put_json('%s_branches.json' % ACT, dict(at=utc(), rows=rows, extra=[], widening=wt))
    print(NL.join(L[7:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R312)(1)
WH = ('*Appended 2026-10-21 by b702 to b701’s entry (:9798), under `(R312)`(1) -- b701 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b701_closing.txt):*')
WB = (' “b701 closed: relay 2ab9ff3c, PLACE-papers 1e3fda0; suite 121 of 123; root 663799f09c0ad81c…; 5 prompts answered; 7 defects” '
      '(data/b701_closing.txt :1), the closing 613847d6 pushed and read back at relay main (data/b701_closing_push_out.txt). The bridge compiled '
      'at SIDE-explicit-formula v0.35 = d4e046a, RegisterBridge.lean, h2_sign_iff_register4_positivity_liCoeff : h2_sign ↔ Register4_positivity '
      'LiCoeff := h2_sign_iff_rh.trans register4_positivity_liCoeff_iff_rh.symm; run 39635057369 DERIVES with the artifact’s sha256 agreeing, 74 '
      'of 74 terminals at the standard three (data/b701_runner_SIDE-explicit-formula_run1.txt :95); the grade DERIVES with E0 agreeing and every '
      'salt-check PASS (data/b701_grade.txt :41). The restatement read HOLDS-BY-CORRESPONDENCE at every binder, 3 binders and the conclusion, and '
      'K4 against the face’s binder 13 at lam := LiCoeff, before the theorem was written (data/b701_correspondence_restatement.txt :57); '
      'CLAUSE-DOMINANCE by correspondence 2 of 2 through the restatement, the direct reading DIFFERS at binder 1 as b698 read it, controls C1 and '
      'C2 True (data/b701_clause_dominance.txt :58); W-ORD-H2-BRIDGE and W-ORD-H2-BRIDGE-THEOREM annotated DISCHARGED in the author’s words '
      '(OPEN_TRAILS :15406). The widening HELD: widening-b701 = 8a4ab68 built every other module and failed at one token, H2SignWide.lean :59 '
      'passing le_rfl where Mathlib at the pin wants n ≠ 0 for ContDiff.differentiable, no third dispatch under N1, no merge, no v0.36, nothing at '
      'main, the error, the goal and the one-token repair banked (data/b701_obstruction.txt :11-:26); W-ORD-EXPLICIT-FORMULA-C1 entered '
      '(OPEN_TRAILS :15408, the W1 converse’s re-port, 7 dispatches at the least) and W-ORD-CLASSK-WIDENING-HELD (:15410, the repair and one '
      'dispatch, trigger “the research act after b702”). The Epstein count’s opening step priced at 1 dispatch, the whole at 6 at the least '
      '(data/b701_epstein_plan.txt :163). The entry at FINDINGS :9798, b700’s weight at :9796, the trail at OPEN_TRAILS :15412; the root '
      '663799f0 over 70 banks with the chain b624-b701 AGREE (data/b701_act_root.json); mirror-refresh-2026-10-21-b701.zip sha256 b1fbc501 CLEAN '
      'on all three clauses with the root line (data/b701_mirror.txt); all eight scores HELD (data/b701_scores_close.json). Suite 122 of 123 '
      'pre-push and 121 of 123 post-push, G-READ-RULE and G-ACTROOT-LAST failing on real state, undeclared on the face (its declaration line '
      'NONE) and declared in their commits alone; four items un-lettered -- the fourth whole read of a long file (data/b701_read_calls.txt :54), '
      'a “2>&1 | head -c 0” in one diagnostic after the root, the six per-part seconds banks rewritten after the root by the sealed suite that '
      'lost b700’s PRERUN guard at the carry, and the trail’s Resolved line counting three navigator misses and six seat defects where the bank '
      'holds two and five (OPEN_TRAILS :15436) -- each answered by this act’s corrigendum; nine carry-time repairs (data/b701_tool_repairs.txt), '
      'four found by the pre-run; seven defects (a)-(g), (d)-(e) the navigator’s (data/b701_defects.txt :6-:50). Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B701_ENTRY,
         check=[('FINDINGS.md', K.B701_ENTRY, '## The bridge h2_sign ↔ Register4_positivity LiCoeff compiled'), ('OPEN_TRAILS.md', K.B701_TRAIL, '### b701')], dry=dry)


# ================================================================================ COMPONENT 1: THE GUARD'S DRY RUN AND THE REPAIRS ((R312)(2))
BLOCK = ("out = _write(_part_name(base, PART), L)", "print('  written: %s' % os.path.basename(out))")


def _block(src):
    """the suite's writer block at the end of a part: from its part-bank write to its `written:` print, both lines included."""
    L = src.split(NL)
    i = next((k for k, l in enumerate(L) if BLOCK[0] in l), None)
    j = next((k for k, l in enumerate(L) if BLOCK[1] in l and i is not None and k > i), None)
    return L[i:j + 1] if i is not None and j is not None else []


def guard(*a):
    """data/b702_guard_dry.txt (.json): the suite's `--guard-dry` run in its own process (it writes nothing), its print banked verbatim; the
    writes by mode read from the suite's own writer_plan; the writer block's `if PRERUN:` line read from the suite's text by number."""
    import b702_checks as CH
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b702_checks.py'), '--guard-dry'], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', cwd=ROOT)
    src = rd(os.path.join(T, 'b702_checks.py')).split(NL)
    k = next((i for i, l in enumerate(src) if l.strip() == CH.GUARD_WRITE), None)
    k1 = next((i for i, l in enumerate(rd(os.path.join(T, 'b701_checks.py')).split(NL)) if l.strip() == CH.GUARD_WRITE.replace('b702', 'b701')), None)
    writes = {}
    for mode, args in (('prerun', (True, False, False, False)), ('pre-push', (False, False, False, False)), ('post-push', (False, True, False, True))):
        writes[mode] = CH.writer_plan(*args)[1]
    ok = r.returncode == 0 and k is not None and src[k - 1].strip() == 'if PRERUN:' and writes['pre-push'] == [] and writes['post-push'] == [] \
        and writes['prerun'] == ['data/b702_arm_seconds_<part>.json'] and 'POST-ROOT PATH WRITES NONE' in r.stdout
    L = ['%s -- COMPONENT 1, (R312)(2): THE PRERUN GUARD RESTORED, ITS DRY RUN (%s)' % (ACT, utc()), '',
         '### the suite`s `--guard-dry` run in its own process, writing nothing; its print verbatim beneath. The guard: tools/b702_checks.py :%d `%s`,'
         % (k, src[k - 1].strip() if k else '?'),
         '### the line above the per-part seconds write at :%d -- as tools/b700_checks.py :1669 had it; tools/b701_checks.py :%d wrote it unguarded.' % (
             (k or 0) + 1, (k1 or 0) + 1),
         '### The diff against b701`s writer block: data/b702_tool_repairs.txt row (1).', '', '### THE PRINT, VERBATIM (exit %d):' % r.returncode]
    L += [x for x in r.stdout.rstrip(NL).split(NL)]
    L += ['', '### THE WRITES BY MODE, READ FROM THE SUITE`S writer_plan: %s' % '; '.join('%s %s' % (m, w or 'NONE') for m, w in writes.items()), '',
          '### ### **%s**' % ('THE GUARD RESTORED ; THE POST-ROOT PATH WRITES NONE OF THE PER-PART SECONDS BANKS ; THE PRE-RUN WRITES THEM ALONE'
                               if ok else '### THE GUARD IS NOT AS READ -- SEE ABOVE')]
    if 'dry' not in a:
        put_txt('%s_guard_dry.txt' % ACT, L)
        put_json('%s_guard_dry.json' % ACT, dict(at=utc(), writes=writes, guard_line=k, exit=r.returncode, ok=ok))
    print(NL.join(L))


REPAIR_ROWS = [
    ('(1) tools/b702_checks.py, the writer block`s per-part seconds write under `if PRERUN:` -- ANSWERS (R312)(2) and b701`s defect (j) (relay '
     'data/b702_corrigendum.txt; data/b675_corrigenda.txt row (20)): b701`s carry dropped b700`s guard (tools/b700_checks.py :1669), so its pre-push '
     'run rewrote six root-named banks after the root and G-ACTROOT-LAST failed post-push. The guard restored; writer_plan and the `--guard-dry` '
     'route new, printing for each run mode what the block would write (data/b702_guard_dry.txt). The block`s diff against b701`s, then the two new '
     'functions.', ('b701_checks.py', 'block'), ('b702_checks.py', 'block'), ('b702_checks.py', ('writer_plan', 'guard_dry'))),
    ('(2) tools/b702_record.py, the answers route -- ANSWERS the author`s mid-act words of 2026-10-21 (transcript line 4681): b698`s matcher reads '
     'a BEGIN only at a text`s start or after `="`, and the paste carries a lead line before its BEGIN, so the route banked one word where two were '
     'given. b698`s route runs unedited; midact_words then reads every user text carrying the mid-act lead, cut from its line-initial BEGIN to its '
     'last line-initial END, its parts named by their line-initial heads, appended verbatim.', None, None, ('b702_record.py', ('midact_words', 'answers'))),
]


def repairs(*a):
    """data/b702_tool_repairs.txt: the carry-time repairs, each with the defect or order it answers, its diff written by this route (difflib,
    autojunk off through the plain unified_diff of whole lines: b697's trap read; the old block from relay HEAD's sealed b701 tool)."""
    import difflib
    L = ['%s -- THE CARRY-TIME READING: THE REPAIRS (%s)' % (ACT, utc()), '',
         '### rows are repairs with the defect or order they answer: the tool and its part ; what it answers ; the form. Each diff beneath its',
         '### row, written by this route (difflib over the block`s or the function`s source, relay HEAD`s sealed tool against this act`s).', '']
    n = 0
    for text, old_ref, new_ref, new_fns in REPAIR_ROWS:
        L += ['  ' + text, '']
        if old_ref:
            old = _block(_show(ROOT, 'HEAD', 'tools/' + old_ref[0]) or '')
            new = _block(rd(os.path.join(T, new_ref[0])))
            d = list(difflib.unified_diff(old, new, 'tools/%s the writer block (sealed)' % old_ref[0], 'tools/%s the writer block (this act)' % new_ref[0],
                                          lineterm=''))
            n += len(d)
            L += ['      ' + x for x in d] + ['']
        tool, fns = new_fns
        for fn in fns:
            new = R._fn_src(rd(os.path.join(T, tool)), fn).split(NL)
            d = list(difflib.unified_diff([], new, '(none)', 'tools/%s %s (this act)' % (tool, fn), lineterm=''))
            n += len(d)
            L += ['      ' + x for x in d] + ['']
    L += ['### ### **REPAIRS %d ; NO SHARED TOOL EDITED ; DIFF LINES %d ; NO FROZEN BANK EDITED.**' % (len(REPAIR_ROWS), n)]
    if 'dry' not in a:
        put_txt('%s_tool_repairs.txt' % ACT, L)
    print(NL.join(L) if 'dry' in a else L[-1])


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, defects=defects, defshort=defshort, c1=c1, guard=guard, repairs=repairs)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b702_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
