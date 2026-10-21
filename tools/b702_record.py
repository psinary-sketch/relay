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


# ================================================================================ COMPONENT 2: THE NAMING, (R312)(3) (b699's tie route, rewritten for the kinds)
ROW4 = re.compile(r'^  (\S.*?)\s+(\d+) ->\s+(\d+) ->\s+(\d+) ->\s+(\d+)\s+\[(.*?)\]$')
CSUM = re.compile(r'^### ### \*\*([\w-]+): CLAIMS (\d+) ; SKIPPED LINES \d+ ; MATCHES (\d+) ; UNDERSTATES (\d+) ; OVERREACHES (\d+) ; UNLICENSED (\d+) ;')


def read_companion_sum(l):
    """a companion's table summary line (data/b646_table_<companion>.txt): returns (name, claims, matches, understates, overreaches, unlicensed)."""
    m = CSUM.match(l or '')
    if not m:
        raise ValueError('companion table summary of another shape: %r' % (l,))
    return (m.group(1),) + tuple(int(x) for x in m.groups()[1:])


READERS += ['read_companion_sum']


def _kinds():
    out = {}
    for l in rdn(K.KINDS).split(NL):
        p = [x.strip() for x in l.split('|')]
        if len(p) == 7 and p[1] in ('monograph', 'companion', 'page', 'kernel', 'h2 row'):
            out[p[0]] = p[1]
    return out


def tie(*a):
    """b652's order (data/b652_ferry.txt :19) and b674's rule (data/b674_rules.txt :8-:11) printed verbatim first; then every agenda row of
    reading 4 (data/b700_r4_licensed.txt :52-:84, b648 -> b680 -> b690 -> b700) with its kind from data/b648_recut_order.txt; the kernels by
    descending count; where the top kernel count is 0 the order passes to the companions, read by descending count; at the top count b674's
    rule applied in its written order, each step printed; and only then the document named. data/b702_tie.txt (.json)."""
    order = rdn('b652_ferry.txt').split(NL)[K.ORDER_LINE - 1]
    if 'the next kernel by descending count under the same rules, then the companions' not in order:
        sys.exit('### data/b652_ferry.txt :%d DOES NOT CARRY b652`s ORDER -- NOTHING WRITTEN' % K.ORDER_LINE)
    rl = rdn('b674_rules.txt').split(NL)[K.RULE_LINES[0] - 1:K.RULE_LINES[1]]
    if not rl or not rl[0].startswith('  (2) THE TIE-BREAK BEYOND THE COUNT'):
        sys.exit('### data/b674_rules.txt :%d DOES NOT CARRY ROW (2) -- NOTHING WRITTEN' % K.RULE_LINES[0])
    kinds = _kinds()
    rows = []
    for i, l in enumerate(rdn(K.LICENSED_NOW).split(NL), 1):
        m = ROW4.match(l)
        if m:
            doc = m.group(1).strip()
            rows.append(dict(document=doc, kind=kinds.get(doc, '### NO KIND'), line=i, row=l.strip(), now=int(m.group(5)), source=m.group(6)))
    unk = [r['document'] for r in rows if r['kind'] == '### NO KIND']
    if len(rows) != 33 or unk:
        sys.exit('### READING 4 READ AS %d ROWS, KINDS MISSING FOR %s -- NOTHING WRITTEN' % (len(rows), unk))
    kern = sorted([r for r in rows if r['kind'] == 'kernel'], key=lambda r: -r['now'])
    comp = sorted([r for r in rows if r['kind'] == 'companion'], key=lambda r: -r['now'])
    ktop = kern[0]['now'] if kern else 0
    pool = kern if ktop > 0 else comp
    top = [r for r in pool if r['now'] == pool[0]['now']] if pool and pool[0]['now'] > 0 else []
    for r in top:
        if r['kind'] == 'companion':
            sl = [x for x in rdn(os.path.basename(r['source'])).split(NL) if x.startswith('### ### **') and ': CLAIMS ' in x]
            _n, cl, mt, us, ov, ul = read_companion_sum(sl[0] if sl else '')
            r.update(table_rows=cl, overreaches=ov, unlicensed=ul, understates=us, any_kind=us + ov + ul, summary=sl[0] if sl else '',
                     name=_n, path=r['document'].split(' (')[0])
    steps, cand = [], list(top)
    if len(cand) > 1:
        mo = max(r['overreaches'] for r in cand)
        steps.append('(i) THE OVERREACHES COUNTS: %s ; the greatest %d ; standing %s' % (
            ', '.join('%s %d' % (r['document'], r['overreaches']) for r in cand), mo, [r['document'] for r in cand if r['overreaches'] == mo]))
        cand = [r for r in cand if r['overreaches'] == mo]
    if len(cand) > 1:
        ma = max(r['any_kind'] for r in cand)
        steps.append('(ii) EQUAL OVERREACHES: THE ROWS OUTSIDE LICENSED/CITED OF ANY KIND (UNDERSTATES COUNTED): %s ; the greatest %d ; standing %s' % (
            ', '.join('%s %d' % (r['document'], r['any_kind']) for r in cand), ma, [r['document'] for r in cand if r['any_kind'] == ma]))
        cand = [r for r in cand if r['any_kind'] == ma]
    if len(cand) > 1:
        mr = max(r['table_rows'] for r in cand)
        steps.append('(iii) EQUAL OF ANY KIND: THE LARGER TABLE: %s ; the largest %d ; standing %s' % (
            ', '.join('%s %d claims' % (r['document'], r['table_rows']) for r in cand), mr, [r['document'] for r in cand if r['table_rows'] == mr]))
        cand = [r for r in cand if r['table_rows'] == mr]
    named = cand[0] if len(cand) == 1 else None
    L = ['%s -- COMPONENT 2, (R312)(3): THE LICENSED TABLE`S NEXT DOCUMENT, b652`S ORDER AND b674`S TIE-BREAK RULE PRINTED BEFORE IT IS NAMED (%s)' % (ACT, utc()), '',
         '### b652`S ORDER, VERBATIM FROM relay data/b652_ferry.txt :%d:' % K.ORDER_LINE, '    ' + order, '',
         '### b674`S TIE-BREAK RULE, VERBATIM FROM relay data/b674_rules.txt :%d-:%d:' % K.RULE_LINES] + rl + [
         '', '### THE AGENDA`S ROWS, VERBATIM (reading 4, relay data/%s, b648 -> b680 -> b690 -> b700), EACH WITH ITS KIND FROM relay data/%s;'
         % (K.LICENSED_NOW, K.KINDS), '### rows are documents: the count now | the kind | the row (its line):']
    L += ['  %3d | %-9s | %s (:%d)' % (r['now'], r['kind'], r['row'], r['line']) for r in rows]
    L += ['', '### THE KERNELS BY DESCENDING COUNT: the top count %d ; kernels at 0 %d of %d -- %s' % (
        ktop, sum(1 for r in kern if r['now'] == 0), len(kern),
        'the order passes to the companions ("then the companions")' if ktop == 0 else 'the order stays with the kernels')]
    if ktop == 0:
        L += ['### THE COMPANIONS BY DESCENDING COUNT: %s' % '; '.join('%s %d' % (r['document'], r['now']) for r in comp)]
    L += ['### THE TOP COUNT %s ; the documents standing at it %s ; b674`s rule %s' % (
        pool[0]['now'] if pool else '### NONE', [r['document'] for r in top] or 'NONE',
        'NOT REACHED (one document at the top count, no tie)' if len(top) == 1 else 'REACHED: %d documents at the top count' % len(top))]
    L += ['### the tables of the documents at the top count, their summary lines verbatim:'] + ['    relay %s : %s' % (r['source'], r.get('summary', ''))
                                                                                                for r in top]
    L += ['### b674`s rule, step by step in its written order:'] + (['    ' + s for s in steps] or ['    NOT REACHED: no step taken'])
    L += ['', '### ### **THE NEXT DOCUMENT BY b652`S ORDER AND b674`S TIE-BREAK: %s (A COMPANION ; THE TOP COUNT %d, %d DOCUMENT%s AT IT ; %s ; '
          'THE NEXT BY COUNT %s).**' % (named['document'], named['now'], len(top), '' if len(top) == 1 else 'S',
                                         'DECIDED AT STEP %s' % ['(i)', '(ii)', '(iii)'][len(steps) - 1] if steps else 'NO TIE',
                                         '; '.join('%s %d' % (r['document'], r['now']) for r in pool if r not in top and r['now'] == max(
                                             [x['now'] for x in pool if x not in top] or [0]))) if named else '### ### **NO DOCUMENT NAMED -- RAISED.**']
    if 'dry' in a:
        print(NL.join(L))
        return
    put_txt('%s_tie.txt' % ACT, L)
    put_json('%s_tie.json' % ACT, dict(at=utc(), rule=rl, order=order, rows=rows, steps=steps, kernels_top=ktop,
                                       named=named.get('name') if named else None, path=named.get('path') if named else None))
    print(NL.join(L))


# ================================================================================ COMPONENT 2: THE QUOTATION SEARCH BEFORE THE COMMIT (data/b690_rules.txt row (2))
# ### one needle per line the cut removes or changes, checked to stand in its own removed line before it is searched; the second shape shorter
# ### and case-insensitive. A paper has no merge: the search runs over PLACE-papers' tracked working tree after the edits and before the cut's
# ### commit; the control at HEAD (the base), where every removed line stands.
QUOTE_NEEDLES = (
    ('The formation count is machine-checked in Lean 4', 'formation count is machine-checked'),
    ('The distributive interface is likewise spectrally inert', 'likewise spectrally inert'),
    ('qualify as essential and universal', 'qualify as essential'),       # ### tightened once: 'essential and universal' hit 25 lines of the term
    ('All four summands of the formation now have domain Ostrowskis', 'now have domain ostrowskis'),   # ### tightened once: 'domain ostrowskis' hit 40
    ('no class, however defined, produces off-line zeros', 'independent empirical evidence for exhaustiveness'),
    ('| ξ(s) | Ostrowski + Tate + algebra + bipartition | 7 | This work |', 'ostrowski + tate + algebra + bipartition | 7'),
    ('is the catalogue on which the proof of Theorem (RH) rests', 'the proof follows as a syllogism'),
    ('The formation count and supporting infrastructure are compiled', 'supporting infrastructure are compiled'),
    ('Seven per-class identifications of σ = 1/2', 'per-class identifications of'),
    ('135+ theorems in the core subset', 'core subset relevant to this paper'),
    ('five bridge files compile against Mathlib in a separate project', 'five bridge files compile'),
    ('This paper develops one component of a proof of Theorem (RH)', 'one component of a proof of theorem (rh)'),
    ('no pair of classes produces the coincidence an off-line zero would need', 'coincidence an off-line zero would need'),
)


def _removed_lines(base_text, now_text):
    import difflib
    a, b = base_text.split(NL), now_text.split(NL)
    out = []
    for tag, i1, i2, _j1, _j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag in ('replace', 'delete'):
            out += [(i + 1, a[i]) for i in range(i1, i2) if a[i].strip()]
    return out


def quote(*a):
    """data/b702_quote.txt (.json): every line the cut removes or changes (difflib, autojunk off, the base blob at PLACE-papers HEAD against the
    working tree), one needle each by containment, refused where a removed line carries none or a needle stands in no removed line; each needle
    searched with git grep -n -F across PLACE-papers' tracked working tree in two shapes; every hit printed with its quoting line and entered as a
    residue; the control at HEAD. Run after the edits and before the cut's commit."""
    base = _show(PP, 'HEAD', K.CUT_DOC) or ''
    now = rd(os.path.join(PP, *K.CUT_DOC.split('/'))).replace('\r', '')
    removed = _removed_lines(base.replace('\r', ''), now)
    rows, unassigned = [], []
    for ln, l in removed:
        nd = [(n, w) for n, w in QUOTE_NEEDLES if n in l]
        if len(nd) != 1:
            unassigned.append((ln, len(nd)))
            continue
        n, w = nd[0]
        if w.lower() not in l.lower():
            unassigned.append((ln, 'second shape'))
        rows.append(dict(base_line=ln, line=l, needle=n, wide=w))
    unused = [n for n, _w in QUOTE_NEEDLES if not any(r['needle'] == n for r in rows)]
    if unassigned or unused:
        sys.exit('### A REMOVED LINE WITHOUT EXACTLY ONE NEEDLE %s OR A NEEDLE IN NO REMOVED LINE %s -- NOTHING WRITTEN' % (unassigned, unused))
    hits = []
    for r in rows:
        r['hits'] = [x for x in g(PP, 'grep', '-n', '-F', r['needle'], '--').split(NL) if x.strip()]
        r['hits_wide'] = [x for x in g(PP, 'grep', '-n', '-i', '-F', r['wide'], '--').split(NL) if x.strip()]
        r['control'] = (len([x for x in g(PP, 'grep', '-n', '-F', r['needle'], 'HEAD', '--').split(NL) if x.strip()]),
                        len([x for x in g(PP, 'grep', '-n', '-i', '-F', r['wide'], 'HEAD', '--').split(NL) if x.strip()]))
        hits += [h for h in r['hits_wide'] if h not in hits]
        hits += [h for h in r['hits'] if h not in hits]
    q = sorted(set((h.split(':', 2)[0], int(h.split(':', 2)[1])) for h in hits))
    L = ['%s -- THE QUOTATION SEARCH BEFORE THE CUT`S COMMIT, data/b690_rules.txt row (2), OVER PLACE-papers (%s)' % (ACT, utc()), '',
         '### the cut: %s, the base its blob at PLACE-papers HEAD %s against the working tree (difflib, autojunk off); the lines it removes or changes %d ;'
         % (K.CUT_DOC, g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), len(rows)),
         '### one needle each, checked to stand in its own removed line; each searched with git grep -n -F across the tracked working tree. Rows are',
         '### removed lines: the base line | needle | hits ; the second shape | hits | the removed line (its head):']
    for r in rows:
        L.append('  :%-4d %-60r %d hit(s) ; %-46r %d hit(s) | %s' % (r['base_line'], r['needle'][:60], len(r['hits']), r['wide'], len(r['hits_wide']),
                                                                    r['line'].strip()[:90]))
        L += ['      %s' % h[:220] for h in sorted(set(r['hits'] + r['hits_wide']))]
    L += ['', '### THE CONTROL: each needle at HEAD (the base), where the removed line stands (base line ; case-exact hits ; case-insensitive hits):']
    L += ['  :%-4d ; %d ; %d' % (r['base_line'], r['control'][0], r['control'][1]) for r in rows]
    L += ['### the control %s' % ('FIRES FOR EVERY NEEDLE IN BOTH SHAPES' if all(r['control'][0] and r['control'][1] for r in rows) else '### DOES NOT FIRE FOR EVERY NEEDLE')]
    L += ['', '### THE QUOTING LINES, DISTINCT (file :line): %s' % (', '.join('%s :%d' % x for x in q) or 'NONE'),
          '### the yields: the case-exact shape %d hit(s) ; the case-insensitive shape %d hit(s) ; distinct lines %d' % (
              sum(len(r['hits']) for r in rows), sum(len(r['hits_wide']) for r in rows), len(q)),
          '', '### ### **REMOVED OR CHANGED LINES %d ; NEEDLES SEARCHED %d IN TWO SHAPES ; QUOTING LINES %d -- EACH ENTERED AS A RESIDUE.**' % (
              len(rows), len(rows), len(q))]
    if 'dry' in a:
        print(NL.join(L))
        return
    put_txt('%s_quote.txt' % ACT, L)
    put_json('%s_quote.json' % ACT, dict(at=utc(), document=K.CUT_DOC, base=g(PP, 'rev-parse', 'HEAD').strip(), rows=rows, quoting=[list(x) for x in q]))
    print(NL.join(L))


# ================================================================================ COMPONENT 2: THE CUT'S DISTANCE BY THE b670 METHOD ((R312)(3), N3)
FULL_ROW = re.compile(r'^  :(\d+) (OVERREACHES|UNLICENSED|UNDERSTATES) -- STATED "(.*)"$')
# ### N3: no Correspondence cell by hand -- the two rows standing in the paper's Correspondence table (base :280-:285), the paper off the
# ### roster so no generator writes its cells; held, each named with its reason, and counted in the distance after
HELD = {282: 'a cell of the paper`s Correspondence table (base :280-:285); N3: no Correspondence cell by hand, and the paper is off the 19-table '
             'roster, so no generator writes it',
        283: 'a cell of the paper`s Correspondence table (base :280-:285); N3: no Correspondence cell by hand, and the paper is off the 19-table '
             'roster, so no generator writes it'}
STALE = ((7, 'the record line of v3.3.1 (b644): "The text otherwise stands as it stood." -- stale once the cut lands; the ruling orders the cut on '
             'the rows alone, so it is named here and not written'),
         (272, 'the Correspondence heading: "ADDITIVE ONLY: no claim, argument, or sentence above this line is altered" -- stale once the cut lands; '
               'named here and not written'))


def _norm(t):
    return ' '.join((t or '').split())


def cut(*a):
    """data/b702_cut.txt (.json): each non-MATCHES row of the paper's table (data/b646_table_Seven_Mechanism_Classes.txt, the full rows), its
    STATED text searched whitespace-normalized in the document at the base (PLACE-papers HEAD before the cut's commit, or the commit's parent
    once committed) and now (the working tree); a row met where its text no longer stands; the distance the rows not met. The table's pinned
    sha256 checked against the base first. The residues from data/b702_quote.json; the two held cells and the two stale record lines named."""
    import hashlib
    tl = rdn(K.CUT_TABLE).split(NL)
    pin = re.search(r'at (\w+), (\d+) lines, sha256 (\w+)', tl[2])
    committed = bool(K.CUT_COMMIT)
    base_rev = (K.CUT_COMMIT + '^') if committed else 'HEAD'
    base = (_show(PP, base_rev, K.CUT_DOC) or '').replace('\r', '')
    now = rd(os.path.join(PP, *K.CUT_DOC.split('/'))).replace('\r', '')
    sha = hashlib.sha256(base.encode('utf-8')).hexdigest()
    if not pin or pin.group(3) != sha:
        sys.exit('### THE TABLE`S PIN %s IS NOT THE BASE`S sha256 %s -- NOTHING WRITTEN' % (pin and pin.group(3), sha))
    i0 = tl.index('### THE ROWS READING OVERREACHES OR UNLICENSED, IN FULL:')
    rows = []
    for i in range(i0 + 1, len(tl)):
        m = FULL_ROW.match(tl[i])
        if not m:
            continue
        act = tl[i + 2].strip() if i + 2 < len(tl) else ''
        ln, verdict, q = int(m.group(1)), m.group(2), m.group(3)
        sb, sn = _norm(q) in _norm(base), _norm(q) in _norm(now)
        rows.append(dict(line=ln, verdict=verdict, quote=q, action=act[:160], table_line=i + 1, applied=ln not in HELD, held=HELD.get(ln),
                         met_at_base=not sb, met_at_head=not sn))
    before = sum(1 for r in rows if not r['met_at_base'])
    after = sum(1 for r in rows if not r['met_at_head'])
    qj = jl('%s_quote.json' % ACT)
    residues = [list(x) for x in (qj.get('quoting') or [])]
    L = ['%s -- COMPONENT 2, (R312)(3): THE RE-CUT OF %s, ITS DISTANCE, ITS RESIDUES (%s)' % (ACT, K.CUT_DOC, utc()), '',
         '### the document: %s (v3.3.1), named by b652`s order passing to the companions at every kernel 0, one document at the top count 24, b674`s'
         % K.CUT_DOC, '### rule printed and not reached (relay data/b702_tie.txt). Its table: relay data/%s, pinned at %s, %s lines, sha256 %s =' % (
             K.CUT_TABLE, pin.group(1), pin.group(2), pin.group(3)[:16]),
         '### the base`s (PLACE-papers %s). The cut: each non-MATCHES row`s ACTION applied by the Edit tool, the paper`s own straight apostrophes kept; ' % base_rev,
         '### no tag moves for a paper (data/b698_rules.txt row (1) not reached); nothing moved or renamed.', '',
         '### THE DISTANCE BY THE b670 METHOD: each non-MATCHES row`s STATED text searched whitespace-normalized in the document at the base and now,',
         '### the row met where it no longer stands. Rows: base line | verdict | applied or HELD | stands at the base | stands now | the STATED text:']
    for r in rows:
        L.append('  :%-4d | %-11s | %-7s | base %-5s | now %-5s | %s' % (r['line'], r['verdict'], 'applied' if r['applied'] else 'HELD', not r['met_at_base'],
                                                                         not r['met_at_head'], r['quote'][:110]))
        if r['held']:
            L.append('        HELD: %s' % r['held'])
    L += ['', '### THE RESIDUES (data/b690_rules.txt row (2); relay data/b702_quote.txt, two shapes, the search run before the cut`s commit): each quoting',
          '### line, file :line. The second shape tightened once at two needles (:142 "essential and universal" 25 hits -> "qualify as essential" 2;',
          '### :155 "domain ostrowskis" 40 hits -> "now have domain ostrowskis" 2), every line of the tightened yield read by hand: the paper`s frozen',
          '### copies (outputs/DEPOSITED-v1.1.2, archive/2026-08-27-trim-backfill), the monograph`s eleven-programme sentence (v5.18 :996 and its',
          '### earlier copies) and the five companions` closing sentence the cut changed at :265 (each carried by its own table):']
    L += ['  %s :%d' % (f, n) for f, n in residues]
    L += ['', '### THE RECORD LINES THE CUT MAKES STALE, NAMED AND NOT WRITTEN:'] + ['  :%d %s' % s for s in STALE]
    L += ['', '### ### **%s RE-CUT: THE DISTANCE BEFORE %d, AFTER %d ; ROWS APPLIED %d, MET %d ; HELD %d (CORRESPONDENCE CELLS) ; QUOTING LINES %d ; '
          'STALE RECORD LINES %d ; NO TAG ; NOTHING MOVED.**' % (K.CUT_NAME, before, after, sum(1 for r in rows if r['applied']),
                                                                 sum(1 for r in rows if r['applied'] and r['met_at_head']), len(HELD), len(residues), len(STALE))]
    ok = len(rows) == 24 and before == 24 and all(r['met_at_head'] for r in rows if r['applied']) and all(not r['met_at_head'] for r in rows if not r['applied'])
    if not ok:
        L[-1] = '### ### **THE CUT IS NOT AS READ: rows %d, before %d, after %d -- SEE ABOVE**' % (len(rows), before, after)
    if 'dry' in a or not ok:
        print(NL.join(L))
        return
    put_txt('%s_cut.txt' % ACT, L)
    put_json('%s_cut.json' % ACT, dict(at=utc(), document=K.CUT_DOC, base=base_rev, before=before, after=after, applied=before - after, rows=rows,
                                       residues=residues, stale=[list(s) for s in STALE], held=sorted(HELD)))
    print(NL.join(L))


# ================================================================================ COMPONENT 3: THE FACES ROW ON THE AUTHOR'S WORD "regenerate" ((R312)(4); b697's form)
PROBE_OUT = 'b643_probe_out_zeta.txt'
THIRD_LINE = 191
THIRD_TEXT = '| keystone naming a node | `day1/Seven_Mechanism_Classes.md` |'


def _gen(nodes, out):
    pd = os.path.join(K.SP, 'faces-b702')
    os.makedirs(pd, exist_ok=True)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'chain_page.py'), '--nodes', os.path.join(D, nodes), '--probe-dir', pd,
                        '--out', out, '--from-output', os.path.join(D, PROBE_OUT)], capture_output=True, text=True, encoding='utf-8', errors='replace',
                       cwd=ROOT)
    return r.returncode, (r.stdout or '') + (r.stderr or '')


def faces(*a):
    """data/b702_faces.txt (.json) and data/b702_faces_diff.txt: the new list checked against b697's (every line equal but :126, which is b701's
    successor, data/b701_faces_rows.txt :14); the control (tools/chain_page.py --from-output on b697's list re-emitting the page byte for byte,
    its sha256 printed beside the file's); the new emission diffed against the page; the page written by the generator only where the lines
    differing are :3 and :732 alone. `dry`: nothing written to the page."""
    import hashlib
    import difflib
    old = rdn(K.NODES_LIST).split(NL)
    new = rdn('b702_nodes_zeta.txt').split(NL)
    succ = rdn('b701_faces_rows.txt').split(NL)[13]
    diff_lines = [i + 1 for i in range(max(len(old), len(new))) if (old[i] if i < len(old) else None) != (new[i] if i < len(new) else None)]
    if diff_lines != [K.NODES_ROW] or new[K.NODES_ROW - 1] != succ or not succ.startswith(old[K.NODES_ROW - 1]):
        sys.exit('### THE NEW LIST IS NOT b697`S WITH :126 THE SUCCESSOR (lines differing %s) -- NOTHING WRITTEN' % diff_lines)
    page = os.path.join(PP, K.FACES_PAGE)
    pb = open(page, 'rb').read()
    hb = (_show(PP, 'HEAD', K.FACES_PAGE) or '').encode('utf-8')
    sp = os.path.join(K.SP, 'faces-b702')
    c_out, n_out = os.path.join(sp, 'control.md'), os.path.join(sp, 'new.md')
    rc0, o0 = _gen(K.NODES_LIST, c_out)
    cb = open(c_out, 'rb').read() if os.path.exists(c_out) else b''
    control = rc0 == 0 and cb == pb
    rc1, o1 = _gen('b702_nodes_zeta.txt', n_out)
    nb = open(n_out, 'rb').read() if os.path.exists(n_out) else b''
    a_, b_ = pb.decode('utf-8').split(NL), nb.decode('utf-8').split(NL)
    ops = [op for op in difflib.SequenceMatcher(None, a_, b_, autojunk=False).get_opcodes() if op[0] != 'equal']
    changed = sorted(set(i + 1 for t, i1, i2, _j1, _j2 in ops for i in range(i1, i2)))
    same_shape = all(t == 'replace' and i2 - i1 == j2 - j1 for t, i1, i2, j1, j2 in ops)
    ud = list(difflib.unified_diff(a_, b_, 'committed', 'b702', n=0, lineterm=''))
    # ### the author's word on the raise (2026-10-21T21:12Z, "regenerate, three lines"): the control is b697's list re-emitting the page plus the
    # ### one Placement line the cut a1d5d59 propagates (:191), that line alone; the new emission's opcodes exactly :3 replaced, :191 inserted,
    # ### the row replaced
    c_ = cb.decode('utf-8').split(NL)
    cops0 = [op for op in difflib.SequenceMatcher(None, a_, c_, autojunk=False).get_opcodes() if op[0] != 'equal']
    third = c_[THIRD_LINE - 1] if len(c_) >= THIRD_LINE else ''
    control_plus = rc0 == 0 and [(t, i1, i2, j1, j2) for t, i1, i2, j1, j2 in cops0] == [('insert', THIRD_LINE - 1, THIRD_LINE - 1, THIRD_LINE - 1, THIRD_LINE)] \
        and third == THIRD_TEXT and len(cb) - len(pb) == len((third + NL).encode('utf-8'))
    want_ops = [('replace', 2, 3, 2, 3), ('insert', THIRD_LINE - 1, THIRD_LINE - 1, THIRD_LINE - 1, THIRD_LINE),
                ('replace', K.FACES_ROW_LINE - 1, K.FACES_ROW_LINE, K.FACES_ROW_LINE, K.FACES_ROW_LINE + 1)]
    same_shape = [tuple(op) for op in ops] == want_ops
    control = control_plus
    ok = control and rc1 == 0 and same_shape and K.FACES_HEADER_TAG in nb.decode('utf-8').split(NL)[2]
    wrote = False
    if ok and 'dry' not in a:
        rc2, o2 = _gen('b702_nodes_zeta.txt', page)
        wrote = rc2 == 0 and open(page, 'rb').read() == nb
    L = ['%s -- COMPONENT 3, (R312)(4): THE lv-CONSERVATION ROW THROUGH THE GENERATOR, ON THE AUTHOR`S WORD "regenerate" (%s)' % (ACT, utc()), '',
         '### the generator: relay tools/chain_page.py --from-output relay data/%s (no elaboration; no lean on this host)' % PROBE_OUT,
         '### the new list: relay data/b702_nodes_zeta.txt, written by the Write tool -- every line of data/%s but :%d, which is data/b701_faces_rows.txt :14 '
         '(the successor) ; lines differing %s ; the row as it stood a prefix of the successor True' % (K.NODES_LIST, K.NODES_ROW, diff_lines),
         '### the control: b697`s list re-emits the page plus the one Placement line the cut a1d5d59 propagates (:%d "%s"), that line alone: %s '
         '(exit %d ; %d bytes against the page`s %d, the difference %d bytes, the line with its newline %d bytes ; sha256 %s against the file`s %s ; the '
         'file equal to HEAD`s blob %s)' % (THIRD_LINE, THIRD_TEXT, control, rc0, len(cb), len(pb), len(cb) - len(pb), len((THIRD_TEXT + NL).encode('utf-8')),
                                            hashlib.sha256(cb).hexdigest()[:16], hashlib.sha256(pb).hexdigest()[:16], pb == hb),
         '### the third line`s cause, on the author`s word (2026-10-21T21:12Z): this act`s cut (PLACE-papers a1d5d59) wrote h2_sign_iff_rh and ch_iff_rh '
         'into day1/Seven_Mechanism_Classes.md at its :199 and :265, and the generator lists every keystone naming a node -- the cut propagating as '
         'designed, not drift',
         '### the new emission: exit %d, %d bytes, sha256 %s ; the page`s lines replaced %s, and :%d inserted (the third line) -- the three the author`s '
         'word names: :3 the list`s name, :%d the Placement row, :%d the row (now :%d) ; the opcodes exactly those %s ; the header tag "%s" kept %s' % (
             rc1, len(nb), hashlib.sha256(nb).hexdigest()[:16], [':%d' % x for x in changed], THIRD_LINE, THIRD_LINE, K.FACES_ROW_LINE, K.FACES_ROW_LINE + 1,
             same_shape, K.FACES_HEADER_TAG,
             K.FACES_HEADER_TAG in nb.decode('utf-8').split(NL)[2]),
         '### the diff (relay data/b702_faces_diff.txt)', '',
         '### the page written by the generator and read back equal to the emission: %s' % (wrote if 'dry' not in a else 'NOT WRITTEN (dry)'), '',
         '### ### **CONTROL THE PAGE PLUS THE THIRD LINE ALONE %s ; LINES CHANGED THREE (:3 REPLACED, :%d INSERTED, :%d REPLACED) %s ; PAGE WRITTEN %s.**' % (
             control, THIRD_LINE, K.FACES_ROW_LINE, same_shape, wrote if 'dry' not in a else 'dry')]
    if not ok:
        L.append('### ### **A LINE BEYOND :3 AND :%d DIFFERS OR THE CONTROL FAILED -- RAISED, NOTHING WRITTEN TO THE PAGE.** %s' % (K.FACES_ROW_LINE, (o0 + o1)[-400:]))
    c_ = cb.decode('utf-8').split(NL)
    cops = [op for op in difflib.SequenceMatcher(None, a_, c_, autojunk=False).get_opcodes() if op[0] != 'equal']
    L += ['', '### THE CONTROL`S OWN DIFF AGAINST THE PAGE (b697`s list now, committed -> control), by opcode: %s' % (
        '; '.join('%s :%d-:%d -> :%d-:%d' % (t, i1 + 1, i2, j1 + 1, j2) for t, i1, i2, j1, j2 in cops) or 'NONE')]
    for t, i1, i2, j1, j2 in cops:
        L += ['    - :%d %s' % (i + 1, a_[i][:300]) for i in range(i1, i2)] + ['    + :%d %s' % (j + 1, c_[j][:300]) for j in range(j1, j2)]
    L += ['### THE NEW EMISSION`S OPCODES AGAINST THE PAGE: %s' % '; '.join('%s :%d-:%d -> :%d-:%d' % (t, i1 + 1, i2, j1 + 1, j2) for t, i1, i2, j1, j2 in ops)]
    print(NL.join(L))
    print(NL.join(ud)[:1500])
    if 'dry' in a:
        return
    put_txt('%s_faces_diff.txt' % ACT, ud)
    put_txt('%s_faces.txt' % ACT, L)
    put_json('%s_faces.json' % ACT, dict(at=utc(), outcome='regenerated' if wrote else 'not written', control=control, changed_lines=len(changed),
                                         changed=changed, page_sha=hashlib.sha256(open(page, 'rb').read()).hexdigest(), prompt_at='2026-10-21T20:52:17Z'))


# ================================================================================ COMPONENT 3: THE README ON THE AUTHOR'S WORD "apply, sharpened append" ((R312)(5))
README_READS = (('SIDE-window', 'refs/tags/v0.5.2^{}', 'b9055074f9653ed825b32baadbef49ff958bf438'),
                ('SIDE-effects', 'refs/heads/main', '78bbcff533b7273b2d26accd0726b126c961e401'),
                ('SIDE-explicit-formula', 'refs/tags/v0.35^{}', 'd4e046adbb84a53c489015a97cf3d996af8164ac'))   # ### one ls-remote each, 21:18Z, in sequence


def readme(*a):
    """data/b702_readme.txt (.json) and data/b702_readme_diff.txt: the README's edits by the Edit tool against its blob at PLACE-papers HEAD (difflib,
    autojunk off), the three currency values re-read before the edits (one ls-remote each, in sequence, as the author's word orders), the
    sharpened append beneath :131 as the sentence of record and the drafted form not taken; REGISTRY not written (no README row; the author's word)."""
    import difflib
    base = (_show(PP, 'HEAD', 'README.md') or '').replace('\r', '').split(NL)
    now = rd(os.path.join(PP, 'README.md')).replace('\r', '').split(NL)
    ud = list(difflib.unified_diff(base, now, 'README.md at HEAD', 'README.md (b702)', n=0, lineterm=''))
    ops = [op for op in difflib.SequenceMatcher(None, base, now, autojunk=False).get_opcodes() if op[0] != 'equal']
    rg = g(PP, 'status', '--porcelain', '--', 'REGISTRY.md').strip()
    L = ['%s -- COMPONENT 3, (R312)(5): THE README ON THE AUTHOR`S WORD "apply, with the sharpened append" (%s)' % (ACT, utc()), '',
         '### the currency values re-read before the edits, one ls-remote of each repository in sequence (the author`s word): ' +
         '; '.join('%s %s = %s' % (r, ref, sha[:7]) for r, ref, sha in README_READS) + ' -- each equal to relay data/b702_c3_print.txt',
         '### the edits by the Edit tool, the named values alone: :18 SIDE-window `v0.5.0` (working head `aacb415`) -> `v0.5.2` (`b905507`); :18 SIDE-effects '
         '(`afa9ccf`) -> (`78bbcff`); :160 SIDE-explicit-formula **v0.21** (`1d5d4dd`) -> **v0.35** (`d4e046a`); the audit caveat at :18 kept as written',
         '### the append beneath :131: the sharpened form of the author`s mid-act words (B), the author`s sentence of record, its words verbatim in the '
         'README`s form (italics, the ruling ids and the hash in backticks, straight apostrophes), <the date applied> written 2026-10-21; the drafted '
         'form (relay data/b702_readme_currency.txt :23) NOT TAKEN',
         '### REGISTRY.md not written (no README row; adding one needs its own ruling, the author`s word): its status %s' % (rg or 'clean'),
         '### the opcodes against HEAD: %s' % '; '.join('%s :%d-:%d -> :%d-:%d' % (t, i1 + 1, i2, j1 + 1, j2) for t, i1, i2, j1, j2 in ops),
         '### the diff: relay data/b702_readme_diff.txt', '',
         '### ### **README APPLIED: CURRENCY LINES 2 (:18, :160) ; THE SHARPENED APPEND BENEATH :131 ; REGISTRY UNWRITTEN ; THE README`S OWN LAST COMMIT THE '
         'CURRENCY, AS MANIFEST READS IT AT THE NEXT EXPORT.**']
    print(NL.join(L))
    print(NL.join(ud)[:1200])
    if 'dry' in a:
        return
    put_txt('%s_readme_diff.txt' % ACT, ud)
    put_txt('%s_readme.txt' % ACT, L)
    put_json('%s_readme.json' % ACT, dict(at=utc(), outcome='applied', form='sharpened', prompt_at='2026-10-21T20:52:17Z', reads=[list(r) for r in README_READS],
                                          ops=[list(op) for op in ops]))


# ================================================================================ COMPONENT 3: THE TWO ORDERS OF (R312)(4) AND (6), APPENDED TO OPEN_TRAILS
FP_H = ('*Appended 2026-10-21 by b702 beneath `W-ORD-CLASSK-WIDENING-HELD` (:15410), under `(R312)`(4) and the author’s word at the faces prompt -- '
        'THE ORDER **`W-ORD-FACES-PROBE-CURRENT`**, ENTERED:*')
FP_B = (' the faces page (PLACE-papers THE_CLAUSE_AND_ITS_COMPILED_FACES.md) regenerated at b702 by relay tools/chain_page.py --from-output on b643’s '
        'banked probe, from relay data/b702_nodes_zeta.txt (PLACE-papers 65a8367: the lv-conservation row carrying the bridge '
        'h2_sign_iff_register4_positivity_liCoeff by tag v0.35 = d4e046a, and the Placement row for day1/Seven_Mechanism_Classes.md that the cut a1d5d59 '
        'propagated; relay data/b702_faces.txt), its header still naming SIDE-explicit-formula v0.26 = `82550e4`. THE ORDER: the chain’s `#print sig` '
        're-probed at v0.35 on one dispatch, the page regenerated from the new probe with every changed line named with its cause, the diff reviewed '
        'before the commit. Price one dispatch and one review of the diff. Trigger: the re-cut act b704. Status OPEN.')
PC_H = ('*Appended 2026-10-21 by b702 in place of `W-ORD-ONE-COPY` (:14386; its trigger re-written at :14450; read at :15296 and :15332), under '
        '`(R312)`(6) and the author’s word at the partner-copies prompt -- THE ORDER **`W-ORD-PAPER-PARTNER-COPIES`**, ENTERED:*')
PC_B = (' the object: for each roster paper, the unversioned file REGISTRY names as the file of record and its versioned copy. The condition: which '
        'copy the generator and the re-cut acts write, and which copy the Project mirror and the keystone census read. The unit of every figure here: '
        'lines differing between the two copies of one paper. Reading 4’s counts (relay data/b700_reading4.txt :66-:76): 17 pairs; 131 lines '
        'differing; by cause a regenerated cell 123, a hand edit 8, a re-cut 0, an archive-split artefact 0 -- the figures the disposition is priced '
        'from. The three resolutions raised as one prompt with their prices (relay data/b702_c3_print.txt): (i) the versioned copies the files of '
        'record; (ii) both partners written at each write; (iii) the unversioned copy retired and the versioned one renamed in place. THE DISPOSITION, '
        'the author’s word: (iii), rename in place. At that act, for each of the 17 pairs: the 8 hand-edited lines read side by side first, each '
        'entered as carried by the versioned side, carried by the unversioned side, or both differing and raised; the generator run once over the 123 '
        'regenerated-cell lines into the versioned copy; the pair diffed to zero; the unversioned copy retired to archive/ by git mv with its history, '
        'and the versioned copy renamed by git mv to the unversioned name; REGISTRY’s row keeping the version as its tag, so the readers and the 102 '
        'standing reader hits keep their names; each paper one commit, each commit alone; the Project mirror’s roster names changed at the next mirror '
        'sort after b706, entered there. Nothing moved, renamed or written to a paper at b702. Trigger: the re-cut act b706. Status OPEN.')
PCO_H = '*Appended 2026-10-21 by b702 beneath `W-ORD-ONE-COPY` (:14386), under `(R312)`(6):*'
PCO_B = (' the order `W-ORD-ONE-COPY` (:14386; its trigger at :14450; its readings at :15296 and :15332) stands as written, superseded by '
         'W-ORD-PAPER-PARTNER-COPIES (entered directly above, its disposition (iii) on the author’s word, trigger the re-cut act b706).')


def c3orders(*a):
    """OPEN_TRAILS: W-ORD-FACES-PROBE-CURRENT ((R312)(4)), then W-ORD-PAPER-PARTNER-COPIES with the old order's line annotated superseded beneath it
    ((R312)(6)), appended through the guarded landing; data/b702_partners.txt (.json) the disposition as the author's word gives it."""
    dry = 'dry' in a
    chk = [('OPEN_TRAILS.md', 14386, '*Appended 2026-10-14 by b671 under `(R281)`(8)'), ('OPEN_TRAILS.md', 15410, '*Appended 2026-10-21 by b701 beneath `W-ORD-EXPLICIT-FORMULA-C1`')]
    land([('OPEN_TRAILS.md', FP_H, NL + FP_H + FP_B + NL)], '%s_faces_order_line.json' % ACT, 'faces_order', entry=None, check=chk, dry=dry)
    land([('OPEN_TRAILS.md', PC_H, NL + PC_H + PC_B + NL), ('OPEN_TRAILS.md', PCO_H, NL + PCO_H + PCO_B + NL)], '%s_partners_line.json' % ACT,
         'partners', entry=None, check=chk, dry=dry)
    if dry:
        return
    L = ['%s -- COMPONENT 3, (R312)(6): W-ORD-PAPER-PARTNER-COPIES, THE DISPOSITION ON THE AUTHOR`S WORD (%s)' % (ACT, utc()), '',
         '### the three resolutions raised as one prompt (relay data/b702_c3_print.txt, the prompt at 2026-10-21T20:52:17Z; data/b702_author_answers.txt);',
         '### the author`s word: (iii), rename in place, trigger "the re-cut act b706"; the order landed at OPEN_TRAILS (data/b702_partners_line.json),',
         '### the old line annotated superseded beneath it; nothing moved, renamed or written to a paper.', '',
         '### ### **RESOLUTION (iii) ; TRIGGER THE RE-CUT ACT b706 ; 17 PAIRS, 131 LINES (123 REGENERATED, 8 BY HAND) ; NOTHING MOVED.**']
    put_txt('%s_partners.txt' % ACT, L)
    put_json('%s_partners.json' % ACT, dict(at=utc(), resolution='(iii)', trigger='the re-cut act b706', prompt_at='2026-10-21T20:52:17Z'))
    print(L[-1])


# ================================================================================ COMPONENT 4: THE ORDERS OF (R312)(7) AND OF THE AUTHOR'S MID-ACT WORDS (A)-(C)
SC_H = ('*Appended 2026-10-21 by b702 beneath `W-ORD-PAPER-PARTNER-COPIES` (:15446), under `(R312)`(7) -- THE ORDER **`W-ORD-STANDING-CLAUSES-BANK`**, '
        'ENTERED:*')
SC_B = (' the ferry’s standing procedural paragraph banked once as a versioned rules bank that the ferry names by version and the arms read, the '
        'paragraph then carried by reference and its deltas alone. Priced by the readers of the ferry’s text today: relay tools/ferry_scan.py’s scan '
        'and its standing-clauses citation (:697-:703; on this ferry “cited none ; current 2”, relay data/b702_ferry_scan.txt), the suite’s '
        'G-RECEIPT-IN-FULL over the banked ferry, and the citation tool’s check over the ruling and the ferry (relay tools/b702_citation.py) -- one '
        'bank written once and those three readers pointed at its version; no arm added. Trigger: the reading act b710. Status OPEN.')
LJ_H = ('*Appended 2026-10-21 by b702 beside `W-ORD-STANDING-CLAUSES-BANK` (directly above), under the author’s mid-act words of 2026-10-21 (A), '
        '“ordering the closure join” -- THE ORDER **`W-ORD-LV-CLOSURE-JOIN`**, ENTERED:*')
LJ_B = (' the object: a third kernel requiring SIDE-explicit-formula and SIDE-lv-conservation at one shared Lean and Mathlib pin and stating '
        'h2_sign ↔ Register4_positivity LiCoeff against lv-conservation’s own declaration of Register4_positivity, so that the join is read by Lean’s '
        'closure and not by the correspondence reader. The condition: lv-conservation’s deposited v0.10.0 = 93c27ec and its lakefile unchanged, the '
        'third kernel the one place both are required. The price: unknown until read. The opening step, at b703’s step zero, a read and no build: '
        'each kernel’s lean-toolchain and lake-manifest.json at its current tag read through the Read tool, the Lean versions and Mathlib revisions '
        'printed side by side, and the pin-alignment price stated in dispatches with its cause by line. Nothing built and no lakefile edited for it at '
        'b702. Trigger: the research act b703. Status OPEN.')
KH_H = ('*Appended 2026-10-21 by b702, under the author’s mid-act words of 2026-10-21 (B), “advance the prose with beauty and clarity sharpening '
        'conclusions and results” -- THE ORDER **`W-ORD-KEYSTONE-HEADS`**, ENTERED:*')
KH_B = (' at each re-cut act from b704, beside the cut, the cut document’s opening paragraph redrafted to state its results as results at the '
        'ceiling, each sentence carrying its terminal by tag or its status by name, drafted as the author’s sentence for the author’s strike and '
        'written on the word. Priced at one paragraph per re-cut act. At b702 the word applied to the prose b702 writes alone (the README’s '
        'sharpened append; the FINDINGS entry’s head line); no paper’s prose written for this order. Trigger: the re-cut act b704. Status OPEN.')
SA_H = ('*Appended 2026-10-21 by b702, under the author’s mid-act words of 2026-10-21 (C) and N5 (no standing arm added at b702) -- THE ORDER '
        '**`W-ORD-STANDING-ARMS-B703`**, ENTERED:*')
SA_B = (' four standing arms added at b703 on the author’s word “add needed arms”, each a reading arm that prints its figure every act and fails on a '
        'regression from the previous act’s figure, not on the figure itself: G-CORRESPONDENCE-CURRENCY (every roster paper’s Correspondence rows read '
        'against REGISTRY’s current tag and the print bank at the cited tag, one line per paper -- rows current, behind, at a moved tag with a changed '
        'statement; fails when the changed-statement count rises); G-README-CURRENCY (the PLACE-papers README’s tags and counts read against ls-remote; '
        'fails when a stale line is added); G-PARTNER-COPIES (lines differing between the two copies of each roster paper; fails when the total rises, '
        'until W-ORD-PAPER-PARTNER-COPIES is resolved); G-SISTER-PINS (each kernel’s lean-toolchain and Mathlib revision printed beside the '
        'federation’s; fails when a kernel the faces page names moves pin without a ruling). G-BINDER-PROVENANCE enters when its tool exists, under '
        '`(R312)`(7) (relay data/b702_circuit_spec.txt, the twelfth row). Trigger: the research act b703. Status OPEN.')


def orders(*a):
    """OPEN_TRAILS: W-ORD-STANDING-CLAUSES-BANK ((R312)(7)), then the author's three of the mid-act words -- W-ORD-LV-CLOSURE-JOIN (A),
    W-ORD-KEYSTONE-HEADS (B), W-ORD-STANDING-ARMS-B703 (C) -- appended through the guarded landing, in that order."""
    land([('OPEN_TRAILS.md', SC_H, NL + SC_H + SC_B + NL), ('OPEN_TRAILS.md', LJ_H, NL + LJ_H + LJ_B + NL), ('OPEN_TRAILS.md', KH_H, NL + KH_H + KH_B + NL),
          ('OPEN_TRAILS.md', SA_H, NL + SA_H + SA_B + NL)], '%s_orders_line.json' % ACT, 'orders', entry=None,
         check=[('OPEN_TRAILS.md', 15446, '*Appended 2026-10-21 by b702 in place of `W-ORD-ONE-COPY`')], dry='dry' in a)


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, defects=defects, defshort=defshort, c1=c1, guard=guard, repairs=repairs, tie=tie,
              quote=quote, cut=cut, faces=faces, readme=readme, c3orders=c3orders, orders=orders)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b702_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
