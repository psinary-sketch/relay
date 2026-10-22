# -*- coding: utf-8 -*-
"""b703_record.py -- THE ACT'S RECORD TOOL, b703 under (R313).

### b698's record tool is IMPORTED (tools/b698_record.py, sealed at b698 and unedited) with its act names rebound to b703 -- its worklist
### module K, ACT and PREV, and EVERY import-time constant b699's traps named (SESSION, SUBAGENTS, the previous act's window, FACE, the mirror
### names, ROOT_EXCLUDE, _standins) rebound here explicitly, the original _anchor_ts captured before the wrapper (b701's trap); b700's repaired
### _defect_short (the act PASSED AT THE CALL) carried by copy; b702's late routes carried by copy with b703's names. The compile routes, the
### pins, the registrations and the standing arms' baselines are this act's. Every python child is started as `python -X utf8`.
### Written by the Write tool at b703 in stages: stage one, step zero's routes; Components 1-6 by the Edit tool.
### Routes: `python tools/b703_record.py <route> [dry]`. After the seal this tool's own print is how the entry, the dry entry and the trail
### are read (data/b690_rules.txt row (1)); no commit is amended at any point (data/b692_rules.txt row (1)).
"""
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

import b703_worklist as K          # noqa: E402
import b698_record as R            # noqa: E402  ### b698's routes, imported unedited

ACT, PREV = 'b703', 'b702'
R.K, R.ACT, R.PREV, R.SP = K, ACT, PREV, K.SP
conv = R.conv                      # ### (R262)(2): the one conversion, b652's, through b698's module
PP, FIND, OT = R.PP, R.FIND, R.OT
utc, rd, rdn, put_json, put_txt, jl, g, grc, land, _show = R.utc, R.rd, R.rdn, R.put_json, R.put_txt, R.jl, R.g, R.grc, R.land, R._show
PROJ = 'C:/Users/echo chamber/.claude/projects/D--'

# ================================================================================ THE IMPORT-TIME CONSTANTS, REBOUND (b699's traps 2 and 4)
SESSION = '%s/%s.jsonl' % (PROJ, K.SESSION_ID)
SUBAGENTS = '%s/%s/subagents' % (PROJ, K.SESSION_ID)
R.SESSION, R.SUBAGENTS = SESSION, SUBAGENTS
# ### the previous act's window: b702 ran and closed in THIS session (e5bcf1d0), so its window is b690's form -- from its anchor to this
# ### act's anchor; its post-push stretch from its post-push combine to (R313)'s line
R.PREV_ACT, R.PREV_SESSION, R.PREV_ANCHOR = PREV, K.SESSION_ID, K.PREV_ANCHOR
R.PREV_SESSION_PATH = SESSION
R.PREV_SUBAGENTS = SUBAGENTS
FACE = os.path.join(D, 'b703_registration_2026-10-21.txt')
FACE_REL = 'data/b703_registration_2026-10-21.txt'
R.FACE, R.FACE_REL = FACE, FACE_REL
R.MIRROR_TAG = '%s-%s' % (K.DATE, ACT)
R.ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % R.MIRROR_TAG
R.STAGE = os.path.join(os.environ.get('TEMP', K.SP), 'mirror-build-%s' % R.MIRROR_TAG)
R.N5_RELAY_DATA = ('act_roots.txt', 'b702_closing_push_out.txt', 'b675_corrigenda.txt')
R.N5_RELAY_TOOLS = ('tools/rule_arms.py',)
R.ROOT_EXCLUDE = re.compile(r'^b703_(defects|scores.*|desk_notes|components|checks.*|lsr.*|exercise.*|findings|trail|closing.*|chain_.*|'
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
        '%s_act_root.json' % ACT: dict(root='0' * 64, previous='56312178' + '0' * 56, reads=dict(heads=['x'], tags=['x'], banks=['x'])),
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


def defshort(*a):
    act = a[0] if a else ''
    out = [(s, 'data/%s_defects.txt' % act) for s in _defect_short(act)]
    for s, src in out:
        print('  %s   [%s]' % (s, src))
    print('### ### **%s: DEFECTS %d -- FROM data/%s_defects.txt.**' % (act, len(out), act))


# ================================================================================ STEP ZERO: ROWGEN, ANSWERS, DEFECTS (b698's routes, carried)
rowgen = R.rowgen
answers = R.answers


def defects(*a):
    t = rdn('%s_defects.txt' % ACT)
    ds = [l.strip() for l in t.split(NL) if DEFECT_ROW.match(l)]
    put_json('%s_defects.json' % ACT, dict(at=utc(), defects=ds, short=_defect_short(ACT)))
    print('  defects %d' % len(ds))


# ================================================================================ STEP ZERO: THE BRANCHES BANK ((R313)(9); b702's form)
def branches(*a):
    """`branches before`: data/b703_branches_before.json -- b698's route, carried (every branch (R313)(9) names, its tip resolved, merged into
    main by ancestry, the remote's heads read once per repository; written before any delete). `branches`: data/b703_branches.txt (.json) --
    each branch's fate read now against the tips banked before; widening-b701 kept."""
    if a and a[0] == 'before':
        return R.branches('before')
    before = jl('%s_branches_before.json' % ACT).get('rows') or []
    if not before:
        sys.exit('### data/b703_branches_before.json IS NOT WRITTEN -- NOTHING READ')
    rows = []
    for r in before:
        if r['where'] == 'local':
            gone = not g(r['repo'], 'branch', '--list', r['branch']).strip()
        else:
            gone = r['branch'] not in R._remote_heads(r['repo'])
        rows.append(dict(repo=r['repo'], branch=r['branch'], where=r['where'], tip=r['tip'], merged=r['merged'], fate='DELETED' if gone else 'KEPT'))
    for r in rows:
        read_branch_row(r)
    L = ['%s -- STEP ZERO, (R313)(9): THE BRANCHES, READ BEFORE ANY DELETE AND AFTER (%s)' % (ACT, utc()), '',
         '### rows are branches: repository | branch | where | the tip before the delete (data/b703_branches_before.json, read before any delete) |',
         '### merged into main by ancestry | the fate read now. Each delete one branch per command, each its own message, nothing chained after;',
         '### the listing `git branch --merged main` per repository with no pattern. widening-b701 = %s KEPT, local and remote, used by (R313)(3)' % K.WIDEN_TIP[:7],
         '### and deleted under no answer this act.']
    L += ['  %-22s | %-28s | %-6s | %s | merged %s | %s' % (os.path.basename(r['repo']), r['branch'], r['where'], r['tip'], r['merged'], r['fate'])
          for r in rows]
    wt = g(K.KERNEL_DIR, 'rev-parse', '--verify', '--quiet', 'refs/heads/' + K.WIDEN_BRANCH).strip()
    L += ['', '### widening-b701 at the close of step zero: local %s ; %s' % (wt[:7] or 'ABSENT', 'STANDS' if wt == K.WIDEN_TIP else '### MOVED OR ABSENT')]
    L += ['', '### ### **BRANCHES NAMED %d ; DELETED %d ; KEPT %d ; EVERY TIP MERGED %s ; widening-b701 %s.**' % (
        len(rows), sum(1 for r in rows if r['fate'] == 'DELETED'), sum(1 for r in rows if r['fate'] == 'KEPT'), all(r['merged'] for r in rows),
        'STANDS' if wt == K.WIDEN_TIP else '### MOVED OR ABSENT')]
    put_txt('%s_branches.txt' % ACT, L)
    put_json('%s_branches.json' % ACT, dict(at=utc(), rows=rows, extra=[], widening=wt))
    print(NL.join(L[6:]))


# ================================================================================ COMPONENT 1: THE RECORD LINES, (R313)(1)
WH = ('*Appended 2026-10-21 by b703 to b702’s entry (:9840), under `(R313)`(1) -- b702 AT ITS WEIGHT, AS ITS CLOSING PRINTS (relay '
      'data/b702_closing.txt):*')
WB = (' “b702 closed: relay ca46b729, PLACE-papers 79266e3; suite 126 of 127; root 5631217833cd6085…; 7 prompts answered; 9 defects” '
      '(data/b702_closing.txt :1); the closing commit 8773acc9 pushed after the line was written and read back equal at the remote '
      '(data/b702_closing_push_out.txt :7). day1/Seven_Mechanism_Classes.md re-cut at PLACE-papers a1d5d59 by the b670 method, its rows outside '
      'LICENSED/CITED 24 to 2, 22 rows applied and met, its Correspondence cells :282 and :283 held under N3, 46 quoting lines entered as residues, '
      'record lines :7 and :272 named stale and not written (data/b702_cut.txt; data/b702_quote.txt); the faces page regenerated by the generator at '
      'three lines on the author’s word (PLACE-papers 65a8367), the third :191’s Placement row, the cut propagating through the generator '
      '(data/b702_faces.txt); the README’s three stale tags current and its sharpened ceiling append (PLACE-papers d5f8a03), its blob c72e8edb read '
      'back at the remote and equal (data/b702_readme_readback.txt :9); W-ORD-FACES-PROBE-CURRENT, W-ORD-PAPER-PARTNER-COPIES with disposition (iii) '
      'and trigger “the re-cut act b706” (W-ORD-ONE-COPY annotated superseded), and the four orders of the author’s mid-act words '
      '(W-ORD-STANDING-CLAUSES-BANK, W-ORD-LV-CLOSURE-JOIN, W-ORD-KEYSTONE-HEADS, W-ORD-STANDING-ARMS-B703) at OPEN_TRAILS :15444-:15456; the '
      'spec’s twelfth row BINDER-PROVENANCE (data/b702_circuit_spec.txt). b701’s two undeclared failures, four un-lettered items and trail miscount '
      'answered by the generated corrigendum at FINDINGS :9826 (corrigenda rows (17)-(21)); b701’s weight at :9824; the PRERUN guard restored, its '
      'dry run printing no write on the post-root path (data/b702_guard_dry.txt). The entry at FINDINGS :9840, the trail at OPEN_TRAILS :15458; the '
      'root 56312178 over 77 banks chained from 663799f0 (data/b702_act_root.json); suite 126 of 127 pre-push and post-push, G-RULE-RECUT-QUOTE '
      'carried and declared on the face (data/b702_checks.txt; data/b702_checks_postpush.txt); all eight scores held (data/b702_scores_close.json); '
      'the citation check 112 cites, 110 OK, the ruling’s two misses answered on the author’s word; nine defects (a)-(i), (d) and (e) the '
      'navigator’s (data/b702_defects.txt); the mirror mirror-refresh-2026-10-21-b702.zip, sha256 b4ded385, CLEAN on all three clauses over 83 '
      'files, built after PLACE-papers 79266e3 (data/b702_mirror.txt). Two items after the root, entered by this act’s corrigendum: the mirror '
      'bank’s span line naming b697’s export, and the closing push’s opening call given the repository’s name. Nothing deposited.')


def c1(*a):
    dry = 'dry' in a
    land([('FINDINGS.md', WH, NL + WH + WB + NL)], '%s_record_lines.json' % ACT, 'c1', entry=K.B702_ENTRY,
         check=[('FINDINGS.md', K.B702_ENTRY, '## Seven Mechanism Classes re-cut: 24 rows outside LICENSED/CITED to 2'), ('OPEN_TRAILS.md', K.B702_TRAIL, '### b702')],
         dry=dry)


# ================================================================================ COMPONENT 1: THE TWO REPAIRS AND THEIR CONTROLS, (R313)(2)
def _last_export(act):
    """the mirror bank chain: the latest act before `act` with a mirror bank (data/bNNN_mirror.json), and the zip that bank names."""
    n = int(act[1:])
    for k in range(n - 1, 600, -1):
        j = jl('b%d_mirror.json' % k)
        if j.get('zip'):
            return 'b%d' % k, j['zip']
    return None, None


def span_line(act):
    last, z = _last_export(act)
    return '### THE SPAN: every roster and ledger change of %s (the last export %s`s, %s)' % (act, last or '### NONE', z or '### NONE')


def span(*a):
    """the repaired span line's dry run: read from the mirror bank chain, not carried as wording; no mirror bank written -- its print banked as
    data/b703_span_dry.txt unless `dry`."""
    L = ['%s -- COMPONENT 1, (R313)(2): THE MIRROR SPAN LINE READ FROM THE MIRROR BANK CHAIN, ITS DRY RUN (%s)' % (ACT, utc()), '',
         '  b698`s carried line (tools/b698_record.py :2041): ### THE SPAN: every roster and ledger change of b698 (the last export b697`s, ...)',
         '  the line for b702, read from the chain:  %s' % span_line('b702'),
         '  the line for b703, read from the chain:  %s' % span_line('b703'), '',
         '### ### **THE LAST EXPORT BEFORE b703`S READ AS %s`S FROM THE CHAIN: %s.**' % (_last_export('b703')[0], _last_export('b703')[0] == 'b702')]
    if 'dry' not in a:
        put_txt('%s_span_dry.txt' % ACT, L)
    print(NL.join(L))


def mbank(*a):
    """b698's route carried by copy with b703's names, its span line read from the mirror bank chain ((R313)(2), the repair) -- every other
    line as b698's writes it."""
    import hashlib as _hl
    import zipfile
    import b616_record as R6
    ZIP = R.ZIP
    z = zipfile.ZipFile(ZIP)
    names = sorted(z.namelist())
    man = z.read('MANIFEST.md')
    ls = man.decode('utf-8-sig').replace(chr(13), '').split(NL)
    rootl = [l for l in ls if l.startswith('Act root: ')]
    rosterl = [l for l in ls if l.startswith('ROSTER')]
    commits = sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', NL.join(l for l in ls if '|' in l))))
    zb = open(ZIP, 'rb').read()
    clean = 'VERDICT: CLEAN ON ALL THREE CLAUSES' in rdn('%s_mirror_verify.txt' % ACT)
    nd = R6.nd_hits(NL.join(names), R6.nd_sets())[0]
    files_ = [n for n in names if n != 'MANIFEST.md']
    pp_head = g(PP, 'rev-parse', '--short=7', 'HEAD').strip()
    L = ['%s -- THE MIRROR-REFRESH EXPORT, BUILT AFTER THE ROOT AND THE LAST PLACE-papers PUSH BY THE UNEDITED BUILDER, banked %s' % (ACT, utc()),
         '### THE ZIP : %s ; %d bytes ; md5 %s ; sha256 %s' % (ZIP, len(zb), _hl.md5(zb).hexdigest(), _hl.sha256(zb).hexdigest()),
         '### THE MANIFEST : md5 %s ; entries in the zip %d (files %d + MANIFEST)' % (_hl.md5(man).hexdigest(), len(names), len(files_)),
         '### PLACE-papers HEAD AT THE BUILD : %s ; the last commit carried in MANIFEST`s rows %s' % (pp_head, pp_head in commits),
         '### THE ROSTER LINE : %s' % (' / '.join(rosterl) or '### NONE'), '### THE ROOT LINE : %s' % (rootl[0] if rootl else '### NONE'),
         span_line(ACT),
         '### THE VERIFICATION : %s' % ('CLEAN ON ALL THREE CLAUSES' if clean else '### NOT CLEAN'),
         '### THE NO-DISCLOSURE ARM OVER THE FILE LIST: %s' % dict(nd), '### THE FILE LIST:'] + ['    %s' % n for n in names]
    put_txt('%s_mirror.txt' % ACT, L)
    put_json('%s_mirror.json' % ACT, dict(at=utc(), zip=ZIP, zip_md5=_hl.md5(zb).hexdigest(), zip_sha256=_hl.sha256(zb).hexdigest(), bytes=len(zb),
                                         manifest_md5=_hl.md5(man).hexdigest(), entries=len(names), files=len(files_), roster_line=rosterl,
                                         root_line=rootl[0] if rootl else '', clean=clean, nd=dict(nd), pp_head=pp_head, last_commit_in_manifest=pp_head in commits,
                                         span=span_line(ACT)))
    for l in L[:9]:
        print(l[:240])


def _quote_reading(only=None):
    """G-RULE-RECUT-QUOTE's reading over the repaired sources, the quote banks restricted to `only` (an act) where named."""
    import importlib
    import rule_arms as RA
    importlib.reload(RA)
    S = RA.sources(ACT, None, K.ANCHOR, K.PARTS, pre_relay=None, pre_pp=None)
    if only is not None:
        S = dict(S)
        S['quotes'] = [q for q in S['quotes'] if q['act'] == only]
        S['cut_banks'] = dict((k, v) for k, v in S['cut_banks'].items() if k == only)
    return S, RA.reading('G-RULE-RECUT-QUOTE', S)


def quotectl(*a):
    """data/b703_quote_control.txt: the repaired arm read over every quote bank from b691, then over b702's paper cut alone and b697's kernel
    cut alone -- each as wanted (passing); and a planted copy of b702's paper row with its search after its commit -- as wanted (failing)."""
    L = ['%s -- COMPONENT 1, (R313)(2): G-RULE-RECUT-QUOTE BRANCHED ON THE KIND OF CUT, ITS CONTROL (%s)' % (ACT, utc()), '',
         '### rows are readings of the repaired arm (tools/rule_arms.py, the sources block): over | the quote banks read (bank, kind, its merge or',
         '### commit, the search before it, unentered lines) | the reading (ok, rows, failing, note) | as wanted.', '']
    allok = True
    for label, only, want in (('every quote bank from b691 (this act`s HEAD)', None, True), ('b702`s paper cut alone (data/b702_quote.json)', 702, True),
                              ('b697`s kernel cut alone (data/b697_quote_simplicity.json)', 697, True)):
        S, rdg = _quote_reading(only)
        qs = ['%s %s merge %s search-before %s unentered %d' % (q['bank'], q.get('kind', 'kernel'), (q['merge'] or ['-'])[0][:7],
                                                                bool(q['merge'] and q['at'] and q['at'] < q['merge'][1]), len(q['unentered'])) for q in S['quotes']]
        ok = bool(rdg[0]) == want
        allok = allok and ok
        L += ['  %s' % label, '      banks: %s' % ('; '.join(qs) or 'NONE'), '      reading %s ; as wanted (%s) %s' % (rdg, 'passing' if want else 'failing', ok)]
    S, _r = _quote_reading(702)
    S = dict(S)
    S['quotes'] = [dict(q, at=q['merge'][1] + 60) for q in S['quotes']] if S['quotes'] and S['quotes'][0].get('merge') else S['quotes']
    import rule_arms as RA
    rdg = RA.reading('G-RULE-RECUT-QUOTE', S)
    ok = not rdg[0]
    allok = allok and ok
    L += ['  b702`s paper row planted with its search a minute after its commit', '      reading %s ; as wanted (failing) %s' % (rdg, ok)]
    L += ['', '### ### **THE ARM PASSES ON b702`S PAPER CUT AND b697`S KERNEL CUT ALIKE, AND FAILS THE PLANTED LATE SEARCH: %s.**' % allok]
    if 'dry' not in a:
        put_txt('%s_quote_control.txt' % ACT, L)
    print(NL.join(L))


REPAIR_ROWS = [
    ('(1) tools/rule_arms.py, G-RULE-RECUT-QUOTE`s sources -- ANSWERS (R313)(2) and b702`s carried failure (relay data/b702_checks.txt, '
     'data/b702_checks_postpush.txt: G-RULE-RECUT-QUOTE failing, declared on b702`s face): the arm read quote banks in b676`s kernel form alone '
     '(data/b<act>_quote_*.json, a kernel, a tip, a merge on the kernel`s main), so b702`s paper cut -- its search banked as data/b702_quote.json in '
     'the b670 form, a document and no merge -- read as an act with a cut bank and no search. The sources now branch on the kind of cut: a paper '
     'cut`s search read beside the kernel cuts`, its "merge" the cut`s own PLACE-papers commit, its quoting lines entered where the cut bank`s '
     'residues carry them; the predicate unchanged. A shared tool, edited on the ruling`s word. The control: data/b703_quote_control.txt (the arm '
     'passing over every quote bank from b691, over b702`s paper cut alone and b697`s kernel cut alone, failing a planted late search).',
     'rule_arms.py', None),
    ('(2) tools/b703_record.py, the mirror bank`s span line -- ANSWERS (R313)(2) and b702`s (j) (relay data/b703_corrigendum.txt; '
     'data/b675_corrigenda.txt row (22)): b698`s mbank (tools/b698_record.py :2041) carries the span line as wording, so every act importing it '
     'banked "the last export b697`s". b698`s tool stays sealed and unedited; b703`s record tool carries mbank by copy with the span line read '
     'from the mirror bank chain (_last_export, span_line), every other line as b698`s writes it; its dry run (`span`) printing b702 as the last '
     'export before b703`s. The diff of b698`s mbank against b703`s, then the new functions.', None, ('mbank', ('_last_export', 'span_line', 'span'))),
    ('(3) tools/b703_record.py _deps, the runner`s axioms reader -- ANSWERS b703`s defect (f) (relay data/b703_defects.txt): b698`s reader read a '
     'printed name by `\'([^\']+)\'`, which stops at a prime, so the first reading of run 39700585515 read 83 of 89 printed and the gate NOT DERIVES '
     'while the artifact printed all 89 at the standard three. The name now read lazily to the quote the verdict follows; b698`s sealed tool '
     'unedited, R._deps rebound in b703`s tool; its control data/b703_deps_control.txt; the run read again by its id as run1r, no second dispatch. '
     'The diff of b698`s _deps against b703`s, then the control route.', None, ('_deps', ('depsctl',))),
    ('(4) tools/b703_record.py _self_eq, the salt-check`s "no X = X" clause -- ANSWERS b703`s defect (g): b701`s clause `(\\w+)\\s*=\\s*\\1` (its grade '
     'route, carried into b703`s grade) read rQ_zero`s conclusion `rQ 0 = 0` as X = X and failed the clause. The clause now compares the two whole '
     'sides of a top-level `=`; both grades re-run, every salt-check PASS. The new function.', None, (None, ('_self_eq',))),
    ('(5) tools/b703_record.py _thm_sig, the grade`s statement reader -- ANSWERS the Epstein grade`s first run: b701`s reader took a statement to a '
     '`:= by` or a line ending `:=`, and the module`s one-line theorems (`:= fun ...`, `:= by norm_num` on the theorem`s own line) read as no '
     'statement. The reader now takes the statement from the `theorem NAME` line to the first `:=` after it. The new function.', None, (None, ('_thm_sig',))),
]


def repairs(*a):
    """data/b703_tool_repairs.txt: the carry-time repairs, each with the defect or order it answers, its diff written by this route (difflib,
    autojunk off through the plain unified_diff of whole lines: b697's trap read; the old text from relay HEAD's tracked tool)."""
    import difflib
    L = ['%s -- THE CARRY-TIME READING: THE REPAIRS (%s)' % (ACT, utc()), '',
         '### rows are repairs with the defect or order they answer: the tool and its part ; what it answers ; the form. Each diff beneath its',
         '### row, written by this route (difflib over the file`s or the function`s source, relay HEAD`s tool against this act`s).', '']
    n = 0
    for text, whole, fns in REPAIR_ROWS:
        L += ['  ' + text, '']
        if whole:
            old = (_show(ROOT, 'HEAD', 'tools/' + whole) or '').replace('\r', '').split(NL)
            new = rd(os.path.join(T, whole)).replace('\r', '').split(NL)
            d = list(difflib.unified_diff(old, new, 'tools/%s (relay HEAD)' % whole, 'tools/%s (this act)' % whole, lineterm=''))
            n += len(d)
            L += ['      ' + x for x in d] + ['']
        if fns:
            main_fn, extra = fns
            if main_fn:
                old = R._fn_src(rd(os.path.join(T, 'b698_record.py')), main_fn).split(NL)
                new = R._fn_src(rd(os.path.join(T, 'b703_record.py')), main_fn).split(NL)
                d = list(difflib.unified_diff(old, new, 'tools/b698_record.py %s (sealed)' % main_fn, 'tools/b703_record.py %s (this act)' % main_fn, lineterm=''))
                n += len(d)
                L += ['      ' + x for x in d] + ['']
            for fn in extra:
                new = R._fn_src(rd(os.path.join(T, 'b703_record.py')), fn).split(NL)
                d = list(difflib.unified_diff([], new, '(none)', 'tools/b703_record.py %s (this act)' % fn, lineterm=''))
                n += len(d)
                L += ['      ' + x for x in d] + ['']
    L += ['### ### **REPAIRS %d ; SHARED TOOLS EDITED 1 (tools/rule_arms.py, on (R313)(2)) ; DIFF LINES %d ; NO FROZEN BANK EDITED.**' % (len(REPAIR_ROWS), n)]
    if 'dry' not in a:
        put_txt('%s_tool_repairs.txt' % ACT, L)
    print(NL.join(L) if 'dry' in a else L[-1])


# ================================================================================ COMPONENT 2: THE DISPATCH, THE RUNNER, THE PRINTS (b698's routes; b701's runner by copy)
EF = K.KERNEL_DIR
dispatch, runstatus = R.dispatch, R.runstatus
STD3 = ('Classical.choice', 'Quot.sound', 'propext')
_deps_698 = R._deps
DEPS = re.compile(r"^'(.+?)' (depends on axioms: \[[^\]]*\]|does not depend on any axioms)", re.M)


def _deps(ax):
    """the axioms output read per terminal: [(name, [axioms] or [] for 'does not depend on any axioms')], wrapped lists rejoined -- b698's
    reader with its name read lazily up to the quote that the verdict follows, so a name carrying a prime (`classK'`, `h2_sign'_imp_rh`) is read;
    b698's `'([^']+)'` stopped at the prime and read the six primed names of widening-b701 as not printed (relay data/b703_runner_SIDE-explicit-
    formula_run1.txt, 83 of 89, the artifact itself printing 89; b703's defect (f))."""
    out = []
    for n, d in DEPS.findall(re.sub(r'\n(?=[ \t]*[A-Za-z_.]+[,\]])', ' ', ax)):
        out.append((n, [x.strip() for x in d.split('[', 1)[1].rstrip(']').split(',') if x.strip()] if d.startswith('depends') else []))
    return out


R._deps = _deps


def depsctl(*a):
    """data/b703_deps_control.txt: the axioms reader's control -- b698's reader and the repaired one over this act's run1 artifact bank (89
    printed, six primed) and over b701's run1 bank (74 printed, none primed); the repaired reader as wanted where it reads every printed name
    and agrees with b698's wherever no name carries a prime."""
    rows = []
    for bank in ('b703_axioms_SIDE-explicit-formula_run1.txt', 'b701_axioms_SIDE-explicit-formula_run1.txt'):
        ax = rdn(bank)
        lines = len(re.findall(r"^'", ax, re.M))
        old, new = _deps_698(ax), _deps(ax)
        primed = [n for n, _d in new if "'" in n]
        rows.append((bank, lines, len(old), len(new), primed, [n for n, _d in old if "'" not in n] == [n for n, _d in new if "'" not in n]))
    ok = rows[0][3] == rows[0][1] and rows[0][2] == rows[0][1] - len(rows[0][4]) and rows[1][2] == rows[1][3] == rows[1][1] and all(r[5] for r in rows)
    L = ['%s -- COMPONENT 2: THE AXIOMS READER`S REPAIR, ITS CONTROL (%s)' % (ACT, utc()), '',
         '### rows are banks: the artifact`s axioms bank | the lines opening a printed name | read by b698`s reader | by the repaired reader | the primed',
         '### names | the two readers equal on every unprimed name.', '']
    L += ['  relay data/%s | printed %d | b698 %d | repaired %d | primed %s | equal off the primes %s' % r for r in rows]
    L += ['', '### ### **THE REPAIRED READER READS EVERY PRINTED NAME, b698`S MISSING THE PRIMED ALONE, THE TWO EQUAL ON b701`S UNPRIMED BANK: %s.**' % ok]
    if 'dry' not in a:
        put_txt('%s_deps_control.txt' % ACT, L)
    print(NL.join(L))


def runner(*a):
    """`runner <kernel> <run id> <ref> <label> <note...>`: b698's route carried by copy (b701's form) with this act's name in its bank text."""
    import hashlib
    import io as _io
    import zipfile
    kernel, run_id, ref, label, note = a[0], int(a[1]), a[2], a[3], ' '.join(a[4:])
    repo = 'psinary-sketch/' + kernel
    rc, out, err = R._gh('run', 'view', str(run_id), '-R', repo, '--json', 'status,conclusion,headSha,headBranch,createdAt,updatedAt,url,event,workflowName')
    run = json.loads(out or b'{}')
    rc, out, err = R._gh('api', 'repos/%s/actions/runs/%d/artifacts' % (repo, run_id))
    arts = (json.loads(out or b'{}').get('artifacts') or [])
    art = arts[0] if arts else {}
    row = dict(kernel=kernel, label=label, ref=ref, run_id=run_id, conclusion=run.get('conclusion'), artifact_sha256=None, mem_low=None,
               stopped=False, build_exit=None, errors=[], axioms_sha256=None)
    L = ['%s -- THE HOSTED RUNNER FOR %s, %s, READ BY ITS RUN ID (%s)' % (ACT, kernel, label.upper(), utc()), '',
         '### the dispatch: %s ; the ref input %s' % (note, ref),
         '### the run: id %s ; %s ; status %s ; conclusion %s ; head %s on %s ; %s to %s' % (
             run_id, run.get('url'), run.get('status'), run.get('conclusion'), run.get('headSha'), run.get('headBranch'), run.get('createdAt'),
             run.get('updatedAt'))]
    T_ = {}
    if art:
        rz = subprocess.run(['gh', 'api', 'repos/%s/actions/artifacts/%d/zip' % (repo, art['id'])], capture_output=True)
        sha = hashlib.sha256(rz.stdout).hexdigest()
        digest = (art.get('digest') or '').replace('sha256:', '')
        L.append('### the artifact: id %s ; %s ; %s bytes ; sha256 %s ; the platform`s digest %s ; %s' % (
            art['id'], art.get('name'), art.get('size_in_bytes'), sha, digest or '### NONE GIVEN',
            'AGREE' if digest and digest == sha else '### NOTHING READ FROM IT'))
        if digest and digest == sha:
            row['artifact_sha256'] = sha
            with zipfile.ZipFile(_io.BytesIO(rz.stdout)) as z:
                for n in z.namelist():
                    T_[n] = z.read(n).decode('utf-8', 'replace').replace(chr(13), '')
    else:
        L.append('### the artifact: ### NONE LISTED')
    mem = T_.get('mem.log', '')
    low = re.findall(r'^LOW (\d+)', mem, re.M)
    row['mem_low'] = int(low[-1]) if low else None
    row['stopped'] = any(l.startswith('STOP ') for l in mem.split(NL))
    blog = T_.get('build.log', '')
    row['build_exit'] = T_.get('build_exit.txt', '').strip() or None
    row['errors'] = [l for l in blog.split(NL) if ': error' in l or l.startswith('error:')]
    ax = T_.get('axioms.txt', '').rstrip(NL)
    row['axioms_sha256'] = hashlib.sha256(ax.encode('utf-8')).hexdigest() if ax else None
    deps = _deps(ax)
    tg = [l.strip() for l in T_.get('print_targets.txt', '').split(NL) if l.strip()]
    printed = [n for n, _d in deps]
    unmatched = [n for n in tg if n not in printed]
    outside = [(n, d) for n, d in deps if not set(d) <= set(STD3)]
    L += ['### the ref built (out/ref.txt): %s' % ' '.join(T_.get('ref.txt', '### UNREAD').split()),
          '### the memory log: LOW %s MB ; the hold %d ; STOP lines %s' % (row['mem_low'], K.HOLD, row['stopped']),
          '### the build: exit %s ; error lines %d:' % (row['build_exit'], len(row['errors']))] + ['    ' + l for l in row['errors'][:40]] + [
          '### the log`s last lines:'] + ['    ' + l for l in blog.rstrip(NL).split(NL)[-8:]] + [
          '### the print step: the list (out/print_targets.txt) %d names ; terminals printed %d ; every name printed once %s ; axiom-free %d ; '
          'sorryAx %d ; outside the standard three %d ; refused %s' % (
              len(tg), len(deps), not unmatched and len(printed) == len(set(printed)) == len(tg), sum(1 for _n, d in deps if not d),
              sum(1 for _n, d in deps if 'sorryAx' in d), len(outside), T_.get('axioms_refused.txt', '').strip() or 'NONE'),
          '### rows are terminals: name | the axioms printed | within the standard three:']
    L += ['  %-62s %s %s' % (n, d, 'STD3' if set(d) <= set(STD3) else '### OUTSIDE') for n, d in deps]
    L += ['  %-62s ### NOT PRINTED' % n for n in unmatched]
    ok = run.get('conclusion') == 'success' and row['artifact_sha256'] and row['build_exit'] == '0' and not row['errors'] and not row['stopped'] \
        and row['mem_low'] is not None and row['mem_low'] >= K.HOLD and deps and not unmatched and not outside
    row['gate'] = 'DERIVES' if ok else 'NOT DERIVES'
    L += ['', '### ### **RUN %s (%s) ; CONCLUSION %s ; ARTIFACT %s ; BUILD EXIT %s ; ERROR LINES %d ; TERMINALS PRINTED %d OF %d ; SORRYAX %d ; '
          'OUTSIDE THE STANDARD THREE %d ; GATE %s.**' % (
              run_id, label, run.get('conclusion'), 'AGREE' if row['artifact_sha256'] else '### UNREAD', row['build_exit'], len(row['errors']),
              len(deps), len(tg), sum(1 for _n, d in deps if 'sorryAx' in d), len(outside), row['gate'])]
    read_runner_row(row)
    put_txt('%s_runner_%s_%s.txt' % (ACT, kernel, label), L)
    if row['artifact_sha256']:
        put_txt('%s_axioms_%s_%s.txt' % (ACT, kernel, label), ax.split(NL) if ax else ['### EMPTY'])
        put_txt('%s_buildlog_%s_%s.txt' % (ACT, kernel, label), blog.rstrip(NL).split(NL))
    j = jl('%s_runner_rows.json' % ACT) if os.path.isfile(os.path.join(D, '%s_runner_rows.json' % ACT)) else {}
    rows = [r for r in (j.get('rows') or []) if (r.get('kernel'), r.get('label')) != (kernel, label)] + [row]
    put_json('%s_runner_rows.json' % ACT, dict(rows=rows))
    print(NL.join(L[:14] + L[-3:]))


# ================================================================================ COMPONENT 2: THE GRADE AND THE SALT-CHECK (b701's route; its statement reader taking one-line theorems)
def _thm_sig(src, name):
    """a theorem's statement: from its `theorem NAME` line to the first `:=` after it (a one-line theorem's `:= fun ...` and a tactic proof's
    `:= by` alike -- b701's reader looked for `:= by` or a line ending `:=` and could not read the one-line theorems)."""
    L = src.split(NL)
    i = next(k for k, l in enumerate(L) if l.startswith('theorem %s ' % name))
    j = next(k for k in range(i, len(L)) if ':=' in L[k])
    st = NL.join(L[i:j + 1])
    head = st.split('theorem %s' % name, 1)[1].split(':=', 1)[0]
    return i + 1, j + 1, ' '.join(head.split()).lstrip(': ').strip(), st


WF = 'SIDEExplicitFormula/H2SignWide.lean'
NS = 'SIDEExplicitFormula.B321.'
# ### the seat's reading of each statement's binders by hand, BEFORE the E0 check (b689's form): name -> (file, ns, [(binder, class, why)], grade, premise)
GRADES = {
    'acDeriv_of_contDiff_two': (WF, NS, [('f', 'ℝ → ℂ', 'the function, data'), ('hf', 'ContDiff ℝ 2 f', 'Mathlib`s predicate, the antecedent of the stated implication'),
                                         ('hs', 'HasCompactSupport f', 'Mathlib`s predicate, the antecedent')], 'DERIVES',
                                'NONE (a general lemma: C² with compact support gives acDeriv; its hypotheses Mathlib`s, the antecedents of what is stated)'),
    "classK_subset_classK'": (WF, NS, [('k', 'ℝ → ℂ', 'the window, data'), ('hk', 'classK k', 'the inclusion`s antecedent (H2Sign.lean :24)')], 'DERIVES',
                              'NONE (an inclusion of classes; hk the antecedent of the stated inclusion)'),
    'classK_subset_classKsum': (WF, NS, [('k', 'ℝ → ℂ', 'the window, data'), ('hk', 'classK k', 'the inclusion`s antecedent')], 'DERIVES',
                                'NONE (an inclusion of classes)'),
    "classKsum_subset_classK'": (WF, NS, [('k', 'ℝ → ℂ', 'the window, data'), ('hk', 'classKsum k', 'the inclusion`s antecedent (H2SignWide.lean :43)')],
                                 'DERIVES', 'NONE (an inclusion of classes)'),
    "h2_sign'_imp_h2_sign": (WF, NS, [], 'DERIVES', 'NONE (no binder; an implication between two closed propositions of this kernel)'),
    "h2_sign'_imp_rh": (WF, NS, [], 'DERIVES', 'NONE (no binder; h2_sign’ the antecedent, RH the consequent)'),
    'paperFT_finset_sum': (WF, NS, [('ι', 'Type*', 'the index type, data'), ('s', 'Finset ι', 'data'), ('f', 'ι → ℝ → ℂ', 'data'),
                                    ('hf', '∀ i ∈ s, Continuous (f i)', 'a hypothesis, not discharged in the theorem`s closure (discharged at its use, :131-:133)'),
                                    ('hs', '∀ i ∈ s, HasCompactSupport (f i)', 'a hypothesis, not discharged in the theorem`s closure'), ('z', 'ℂ', 'data')],
                           'INTERFACES', 'hf : ∀ i ∈ s, Continuous (f i) and hs : ∀ i ∈ s, HasCompactSupport (f i) -- on the author`s word at the '
                           'classK’ prompt (2026-10-22T01:03Z): a binder that is a hypothesis not discharged in the theorem`s closure is its premise; the '
                           'first hand reading DERIVES withdrawn'),
    'rh_imp_h2_sign_sum': (WF, NS, [], 'DERIVES', 'NONE (no binder; RH the antecedent of the stated implication)'),
    'h2_sign_sum_imp_h2_sign': (WF, NS, [], 'DERIVES', 'NONE (no binder)'),
    'h2_sign_sum_iff_rh': (WF, NS, [], 'DERIVES', 'NONE (no binder; an equivalence of two closed propositions)'),
}
def _self_eq(concl):
    """the salt-check's "no X = X": a top-level `=` of the conclusion whose two whole sides are one term -- b701's clause matched a word
    against the next (`(\\w+)\\s*=\\s*\\1`) and read `rQ 0 = 0` as X = X (the 0 on both sides of the sign), a value at 0 and not a self-equation."""
    s, depth, cut = ' '.join((concl or '').split()), 0, []
    for i, ch in enumerate(s):
        if ch in '([{⦃⟨':
            depth += 1
        elif ch in ')]}⦄⟩':
            depth -= 1
        elif ch == '=' and depth == 0 and s[i - 1:i] not in ('<', '>', '≠', ':', '=') and s[i + 1:i + 2] not in ('=', '>'):
            cut.append(i)
    return len(cut) == 1 and s[:cut[0]].strip() == s[cut[0] + 1:].strip()


EZ = 'SIDEExplicitFormula/Schema/EpsteinZQ.lean'
NSS = 'SIDEExplicitFormula.Schema.'
_ZQP = ('ZQPremises zq Z c (EpsteinZQ.lean, the bundle): the continuation and functional equation, the zeros of Λ_Q as Z, the log-derivative '
        'series, the explicit formula and Wide.HCount Z A0Q -- each stated, not proved; open')
GRADES.update({
    'four_mul_Q0form': (EZ, NSS, [('m n', 'ℤ', 'data')], 'DERIVES', 'NONE (an identity of integers)'),
    'Q0form_nonneg': (EZ, NSS, [('m n', 'ℤ', 'data')], 'DERIVES', 'NONE (an inequality of integers)'),
    'rQ_zero': (EZ, NSS, [], 'DERIVES', 'NONE (no binder; the definition`s value at 0)'),
    'zqZeros_ne_zero': (EZ, NSS, [('zq', 'ℂ → ℂ', 'data'), ('Z', 'WideConfig', 'data'),
                                  ('h', 'ZQZeros zq Z', 'a structure of premises about the configuration of Λ_Q`s zeros, not derived')],
                        'INTERFACES', 'ZQZeros zq Z (EpsteinZQ.lean, (Z2)): the carrier is Λ_Q`s zeros, the multiplicities their orders -- stated, not proved; open'),
    'zq_count': (EZ, NSS, [('zq', 'ℂ → ℂ', 'data'), ('Z', 'WideConfig', 'data'), ('c', 'ℕ → ℝ', 'data'), ('h', 'ZQPremises zq Z c', 'the bundle of premises')],
                 'INTERFACES', _ZQP),
    'zq_explicit_formula': (EZ, NSS, [('zq', 'ℂ → ℂ', 'data'), ('Z', 'WideConfig', 'data'), ('c', 'ℕ → ℝ', 'data'), ('h', 'ZQPremises zq Z c', 'the bundle of premises'),
                                      ('k', 'ℝ → ℂ', 'the window, data'), ('hk hs he', 'ContDiff ℝ 2 k, HasCompactSupport k, k even', 'class restrictions on k')],
                            'INTERFACES', _ZQP),
    'zq_li_nonneg_imp_online': (EZ, NSS, [('zq', 'ℂ → ℂ', 'data'), ('Z', 'WideConfig', 'data'), ('c', 'ℕ → ℝ', 'data'), ('h', 'ZQPremises zq Z c', 'the bundle of premises')],
                                'INTERFACES', _ZQP),
})
EZ_PREMISES = ('ZQContinuation', 'ZQZeros', 'ZQExplicitFormula', 'ZQPremises')
EZ_DEFS = ('Q0form', 'rQ', 'ZQ', 'qBase', 'LambdaQZeros', 'zeroSideQ', 'primeTermQ', 'bracketQ', 'archTermQ') + EZ_PREMISES


def _block_of(src, kind, name):
    """the declaration `kind name` read from its line to the line before the next blank line or declaration, verbatim, with its line span."""
    L = src.split(NL)
    i = next(k for k, l in enumerate(L) if l.startswith('%s %s ' % (kind, name)) or l.startswith('%s %s(' % (kind, name)))
    j = i
    while j + 1 < len(L) and L[j + 1].strip() and not re.match(r'^(def|theorem|structure|/--|/-!|end|namespace)\b', L[j + 1]):
        j += 1
    return i + 1, j + 1, NL.join(L[i:j + 1])


E0_EXTENSION = {'h2_sign': ('prop', 'SIDE-explicit-formula SIDEExplicitFormula/H2Sign.lean :29'),
                'ZQZeros': ('prop', 'SIDE-explicit-formula SIDEExplicitFormula/Schema/EpsteinZQ.lean (Z2)'),
                'ZQPremises': ('prop', 'SIDE-explicit-formula SIDEExplicitFormula/Schema/EpsteinZQ.lean (the bundle)'),
                'WideConfig': ('data', 'SIDE-explicit-formula SIDEExplicitFormula/Schema/Wide/Config.lean :28'),
                'classK': ('prop', 'SIDE-explicit-formula SIDEExplicitFormula/H2Sign.lean :24'),
                "classK'": ('prop', 'SIDE-explicit-formula SIDEExplicitFormula/H2SignWide.lean :33'),
                "h2_sign'": ('prop', 'SIDE-explicit-formula SIDEExplicitFormula/H2SignWide.lean :39'),
                'classKsum': ('prop', 'SIDE-explicit-formula SIDEExplicitFormula/H2SignWide.lean :43'),
                'h2_sign_sum': ('prop', 'SIDE-explicit-formula SIDEExplicitFormula/H2SignWide.lean :49'),
                'acDeriv': ('prop', 'SIDE-explicit-formula SIDEExplicitFormula/H2SignWide.lean :28'),
                'RiemannHypothesis': ('prop', 'Mathlib RiemannHypothesis')}


_UNL = ('PREDICATE-UNLISTED: (R243)(2) (tools/e0_rule.py :298-:307) -- the binder`s type a named predicate applied to the statement`s own '
        'quantified variable k, the name neither a RESTRICTIONS head (:278-:295) nor in MET (:308-:315), so _named_on_quantified (:330-:354) '
        'returns it and unlisted_case (:319-:322) reads it; the shared lexicon`s extension in this tool (E0_EXTENSION) does not reach MET -- E0`s '
        'list not yet holding the predicate, and not a reading of the statement')
_UNL_GROUND = ('the binder restricts the universally quantified window k to the class the inclusion is about, its conclusion naming k: a class '
               'restriction, (R180)(2)(f) and (R235)(2)(iii) (tools/e0_rule.py :34-:36, :258-:262); no named premise of a fixed kernel object')
E0_DIVERGENCE = [
    ("classK_subset_classK'", _UNL, _UNL_GROUND),
    ('classK_subset_classKsum', _UNL, _UNL_GROUND),
    ("classKsum_subset_classK'", _UNL, _UNL_GROUND),
    ('paperFT_finset_sum',
     'INTERFACES: domain_case (tools/e0_rule.py :407-:412) finds no domain form -- strip_range (:380-:386) reads each binder`s body, Continuous (f i) '
     'and HasCompactSupport (f i); CLASS_PREDS_B625 (:275-:276) takes a bare variable as its last token and (f i) ends in a parenthesis, class_case '
     '(:174-:179, CLASS_PREDS :91) lists neither on an application; so both read as hypotheses that are premises',
     'INTERFACES on hf and hs, on the author`s word: each is a hypothesis of the lemma, not data and not discharged in its own closure (the closure '
     'takes them as hypotheses; their discharge is at the use in rh_imp_h2_sign_sum, H2SignWide.lean :131-:133, by weilTest_contDiff and '
     'weilTest_hasCompactSupport); the first hand reading DERIVES withdrawn'),
]


def grade(*a):
    """`grade <rev> <stem> <name> [<name> ...]`: data/b703_<stem>_grade.txt -- each theorem's statement verbatim from the branch at rev, the seat's
    reading of its binders by hand and the grade it gives, the shared E0 rule's grade as the check (its lexicon extended here, the shared file not
    edited), the salt-check of REGISTRY.md :544 clause by clause, the runner's print of the name ((R313)(3)'s bank data/b703_widening_grade.txt)."""
    import e0_rule as E
    rev, stem, names = a[0], a[1], list(a[2:])
    E.LEXICON.update(E0_EXTENSION)
    rows_ = jl('%s_runner_rows.json' % ACT).get('rows') or []
    full = g(EF, 'rev-parse', rev).strip()
    run = next((r for r in reversed(rows_) if (r.get('ref') or '') == full), None)   # ### the latest reading of the ref's run
    ax = rdn('%s_axioms_%s_%s.txt' % (ACT, run['kernel'], run['label'])) if run else ''
    AX = dict(_deps(ax))
    L = ['%s -- THE GRADE OF EACH THEOREM, READ FROM ITS STATEMENT, AND THE SALT-CHECK, (R313)(3)-(4) (%s)' % (ACT, utc()), '',
         '### rows are, per theorem: the statement verbatim, the binders with their class read by hand, the grade they give, the E0 rule`s check, and',
         '### the salt-check`s clauses with their readings. The statements at SIDE-explicit-formula %s (%s); the profile from run %s (gate %s).' % (
             rev[:7], full[:7], run['run_id'] if run else '### NO RUN', run['gate'] if run else '-'), '']
    allok, summ = True, []
    for name in names:
        fpath, ns, hand, hgrade, hprem = GRADES[name]
        i, j, head, st = _thm_sig(_show(EF, rev, fpath), name)
        eg, why, read = E.grade(' ' + head + ' ', 'theorem')
        prof = AX.get(ns + name)
        concl = E.conclusion(E.statement_only(' ' + head + ' ')) or head
        salt = [('no True-typed conclusion, no uniformly-True predicate', not re.search(r'\bTrue\b', concl), 'the conclusion %r' % concl.strip()[:90]),
                ('no X = X', not _self_eq(concl), 'no equation of a term with itself in the conclusion (its two whole sides compared)'),
                ('no hypothesis that is the claim', all(concl.strip() not in (t or '') for _n, t in read) if read else True, 'hypotheses %s' % ([n for n, _t in read] or 'none')),
                ('no fabricated witness', '∃' not in concl, 'the conclusion constructs nothing' if '∃' not in concl else 'an existential in the conclusion'),
                ('hypotheses named', all(n for n, _t in read) if read else True, ', '.join('%s : %s' % x for x in read) or 'no binder'),
                ('#print axioms profiled after the first three', prof is not None and set(prof) <= set(STD3), 'run %s: %s' % (run['run_id'] if run else '### NO RUN', prof))]
        ok = all(s[1] for s in salt)
        allok = allok and ok and eg == hgrade
        L += ['== %s (%s :%d-:%d):' % (name, fpath, i, j)] + ['    ' + l for l in st.split(NL)]
        L += ['  THE BINDERS, READ BY HAND (the seat`s reading, before the check): %s' % ('NONE -- a closed statement' if not hand else '')]
        L += ['    %-12s : %-34s %s' % b for b in hand]
        L += ['  THE GRADE READ FROM THE STATEMENT: %s ; THE NAMED PREMISE: %s' % (hgrade, hprem),
              '  THE CHECK: relay tools/e0_rule.py`s grade() on the header, its LEXICON extended in this tool (E0_EXTENSION; the shared file not edited):',
              '    E0 GRADE %s ; its reason: %s ; the hypotheses it read: %s' % (eg, why, read),
              '    THE HAND READING AND THE CHECK %s' % ('AGREE' if eg == hgrade else '### DIFFER (%s against %s)' % (hgrade, eg)),
              '  THE SALT-CHECK (REGISTRY.md :544), clause by clause:']
        L += ['    %-55s %s -- %s' % (c, 'PASS' if ok_ else '### FAIL', how) for c, ok_, how in salt]
        L += ['  PROFILE %s ; SALT-CHECK %s' % (prof, 'PASS' if ok else '### FAIL'), '']
        summ.append('%s GRADE %s (E0 %s) SALT %s PROFILE %s' % (name, hgrade, eg, 'PASS' if ok else 'FAIL', 'STD3' if prof is not None and set(prof) <= set(STD3) else prof))
    if stem == 'widening':
        L += ['== THE E0 DIVERGENCE, FOUR ROWS (the author`s word at the classK’ prompt, 2026-10-22T01:03Z): each theorem`s statement whole with its',
              '   binders, E0`s grade and its reason by line in relay tools/e0_rule.py, the hand grade and its ground.']
        for name, why_e0, ground in E0_DIVERGENCE:
            fpath, ns_, hand, hgrade, hprem = GRADES[name]
            i, j, head, st = _thm_sig(_show(EF, rev, fpath), name)
            eg, why, read = E.grade(' ' + head + ' ', 'theorem')
            L += ['  (%s) %s (%s :%d-:%d): %s' % (E0_DIVERGENCE.index((name, why_e0, ground)) + 1, name, fpath, i, j, ' '.join(st.split()).split(':= ')[0].strip()),
                  '      binders: %s' % ('; '.join('%s : %s' % (b[0], b[1]) for b in hand) or 'none'),
                  '      E0 %s -- %s' % (eg, why_e0),
                  '      THE HAND GRADE %s -- %s' % (hgrade, ground),
                  '      %s' % ('THE TWO READINGS AGREE' if eg == hgrade else 'THE TWO READINGS DIFFER: the hand grade stands, E0`s outcome beside it')]
        L += ['  THE ORDER FOR b705: MET (tools/e0_rule.py :308-:315) extended by ruling with classK and classKsum (and classK’ and acDeriv, the',
              '  widened class`s own predicates) -- W-ORD-E0-MET-CLASSK, entered at OPEN_TRAILS; e0_rule.py not edited this act.', '']
    if stem == 'epstein':
        src = _show(EF, rev, EZ)
        L += ['== THE NAMED PREMISES, EACH STATEMENT VERBATIM BESIDE ITS NAME ((R313)(4)), with the zero set it names:']
        for nm_ in ('LambdaQZeros',) + EZ_PREMISES:
            kind = 'def' if nm_ == 'LambdaQZeros' else 'structure'
            bi, bj, bt = _block_of(src, kind, nm_)
            L += ['  %s (%s :%d-:%d), profile %s:' % (nm_, EZ, bi, bj, AX.get(NSS + nm_))] + ['      ' + x for x in bt.split(NL)]
        wsrc = _show(EF, 'v0.35', 'SIDEExplicitFormula/Schema/Wide/Config.lean')
        wi, wj, wt = _block_of(wsrc, 'structure', 'WideConfig')
        L += ['', '== THE STRIP-FREE CONFIGURATION THE PREMISES RANGE OVER (the author`s word at the zero-sum prompt): WideConfig`s fields at v0.35,',
              '   read through the Read tool before the module was written (SIDEExplicitFormula/Schema/Wide/Config.lean :%d-:%d):' % (wi, wj)] + [
            '      ' + x for x in wt.split(NL)]
        L += ['', '   it carries Λ_Q`s zeros: none on Re s >= 3/2 (|Z_Q(s) - 2| <= Z_Q(3/2) - 2 < 2, relay data/b685_count_plan.txt :26-:27), none on',
              '   Re s <= -1/2 by the reflection, the trivial zeros at -1, -2, ... outside; the residue: b590`s EpsteinPremises (Schema/Epstein.lean',
              '   :41-:44) sums the closed strip alone, which Davenport-Heilbronn makes false for Z_Q -- no link to it stated.', '',
              '### the definitions printed beside (no grade: a definition states nothing): %s' % '; '.join('%s %s' % (n, AX.get(NSS + n)) for n in EZ_DEFS), '']
    defs = [n for n, d in _deps(ax) if n.startswith(ns) and n[len(ns):] in ('acDeriv', "classK'", "h2_sign'", 'classKsum', 'h2_sign_sum')]
    if stem == 'widening':
        L += ['### the definitions printed beside (no grade: a definition states nothing): %s' % (
            '; '.join('%s %s' % (n, AX.get(n)) for n in defs) or '### NONE PRINTED'), '']
    L += ['### ### **THEOREMS %d ; %s ; EVERY SALT-CHECK PASSED AND EVERY CHECK AGREEING %s.**' % (len(names), ' ; '.join(summ), allok)]
    put_txt('%s_%s_grade.txt' % (ACT, stem), L)
    put_json('%s_%s_grade.json' % (ACT, stem), dict(at=utc(), rev=full, run=run['run_id'] if run else None, ok=allok, rows=summ))
    print(NL.join(L[-3:]))


def wdiff(*a):
    """data/b703_widening_diff.txt: the widening's one-token repair, widening-b701 8a4ab68 against aa9a543 -- the unified diff and the word diff
    of H2SignWide.lean, the files the commit touched, the tokens changed counted ((R313)(3), N2: one token at :59)."""
    base, tip = K.WIDEN_TIP, 'aa9a543f2144de0eee791ec00e904416567d68b8'
    files = [x for x in g(EF, 'diff', '--name-only', base, tip).split(NL) if x.strip()]
    ud = g(EF, 'diff', '-U0', base, tip, '--', 'SIDEExplicitFormula/H2SignWide.lean').rstrip(NL).split(NL)
    wd = g(EF, 'diff', '--word-diff=porcelain', '-U0', base, tip, '--', 'SIDEExplicitFormula/H2SignWide.lean').rstrip(NL).split(NL)
    minus = [l[1:] for l in wd if l.startswith('-') and not l.startswith('---')]
    plus = [l[1:] for l in wd if l.startswith('+') and not l.startswith('+++')]
    ok = files == ['SIDEExplicitFormula/H2SignWide.lean'] and minus == ['le_rfl)'] and plus == ['one_ne_zero)'] and any(l.startswith('@@ -59 +59 @@') for l in ud)
    L = ['%s -- COMPONENT 2, (R313)(3): THE WIDENING`S REPAIR, ITS DIFF (%s)' % (ACT, utc()), '',
         '### SIDE-explicit-formula widening-b701 %s -> %s (the one commit, by the Edit tool); files touched %s' % (base[:7], tip[:7], files), '',
         '### the unified diff (git diff -U0):'] + ['    ' + l for l in ud] + ['', '### the word diff (git diff --word-diff=porcelain -U0):'] + ['    ' + l for l in wd]
    L += ['', '### ### **ONE FILE ; ONE LINE (:59) ; ONE TOKEN: le_rfl -> one_ne_zero (the argument ContDiff.differentiable takes for n ≠ 0) ; NOTHING ELSE TOUCHED: %s.**' % ok]
    put_txt('%s_widening_diff.txt' % ACT, L)
    print(L[-1])


# ================================================================================ COMPONENTS 2-4: THE ORDERS AND ANNOTATIONS AT OPEN_TRAILS
WD_H = ('*Appended 2026-10-22 by b703 beneath `W-ORD-CLASSK-WIDENING-HELD` (:15410), under `(R313)`(3) -- THE ORDER '
        '**`W-ORD-CLASSK-WIDENING-HELD`** DISCHARGED:*')
WD_B = (' the one-token repair named in relay data/b701_obstruction.txt applied by the Edit tool at H2SignWide.lean :59 (le_rfl -> one_ne_zero, '
        'ContDiff.differentiable`s n ≠ 0; relay data/b703_widening_diff.txt), one commit aa9a543 on widening-b701, one dispatch, run 39700585515 '
        'DERIVES with the artifact`s sha256 agreeing and 89 of 89 terminals at the standard three (read by the repaired axioms reader, relay '
        'data/b703_runner_SIDE-explicit-formula_run1r.txt); the ten theorems graded from their statements (relay data/b703_widening_grade.txt: '
        'eight DERIVES, paperFT_finset_sum INTERFACES on its continuity and support hypotheses, E0 reading PREDICATE-UNLISTED at the three '
        'inclusions); merged --no-ff at dfadc8c and tagged v0.36 naming v0.35, the peel read back; the glossary`s classK’ row written on the '
        'author`s word. Status DISCHARGED.')
LJA_H = ('*Appended 2026-10-22 by b703 beneath `W-ORD-LV-CLOSURE-JOIN` (:15452), under `(R313)`(5) -- THE OPENING STEP READ:*')
LJA_B = (' the pins read through the Read tool and printed side by side (relay data/b703_pins.txt): SIDE-explicit-formula v0.37 at Lean '
         'v4.34.0-rc1 and Mathlib de5ce8a9 (2026-08-11); SIDE-lv-conservation at Lean v4.29.1 and Mathlib 5e932f97 (2026-04-17), the deposit '
         'v0.10.0 and the current tag v0.13.0 alike. explicit-formula`s pin governs (the condition forbids editing lv-conservation); the third '
         'kernel rebuilds lv`s 15 files at it, 116 days of Mathlib later. THE PRICE: 1 dispatch to read whether lv`s deposit compiles at that pin; '
         'a failing lv module blocks the join under the condition and is priced then as an lv forward-port at a new tag. Nothing built, no '
         'lakefile edited. Status OPEN.')
KHM_H = ('*Appended 2026-10-22 by b703 beneath `W-ORD-KEYSTONE-HEADS` (:15454), under `(R313)`(8) -- THE TRIGGER MOVED:*')
KHM_B = (' in the author`s words of 2026-10-21, “do the steps to compile, before write ups” (relay data/b703_rules.txt row (1)): the trigger moved '
         'from “the re-cut act b704” to “the re-cut act after the widening, the Epstein count and the closure join have landed”; the order '
         'otherwise as written; no paper`s prose written for it at b703. Status OPEN.')
QB_H = ('*Appended 2026-10-22 by b703, under `(R313)`(6)(i) -- THE ORDER **`W-ORD-Q0-BAND-CONTROL`**, ENTERED AND DISCHARGED:*')
QB_B = (' registered before any number (relay data/b703_registrations.txt, committed alone at b8a36309); the named reader '
        'tools/b703_q0_zeros_read.py opened b681`s certified zeros of Q0 after both sha256 equalled the hashes bank and counted them by real part '
        '(relay data/b703_q0_band.txt): 163 rows (the control agreeing with the stated 163, and ρ₀ read at Re 0.95326047479466068625), 17 off the '
        'line and 146 on it; in (1/2, 0.6] 0, (0.6, 0.75] 5, (0.75, 7/8] 10, (7/8, 1) 2 -- the hypothesis met, 15 in (1/2, 7/8], the lowest-height '
        '0.79799715717868013876 + 29.55176109862911459913 i. No witness and no Li coefficient computed. It feeds the detection law and the band '
        'witness registered at b705. Status DISCHARGED.')
QW_H = ('*Appended 2026-10-22 by b703, under `(R313)`(6)(iii) -- THE ORDER **`W-ORD-QUASI-RH-FIELD-WATCH`**, ENTERED:*')
QW_B = (' the I-5 field-watch record (PLACE-papers phase1.5/method/INSTRUMENTS.md :74-:91, the record form of the inaugural entry :113-:117) on the '
        'claimed zero-free half-plane for ζ and the Dirichlet L-functions (7/8, and the 11/12 companion), the registered question at which step, by '
        'page and line, the argument spends multiplicativity (the Euler product, the bounded coefficients μ(n)χ(n) of the reciprocal, a Hecke '
        'eigenproperty), its control the Davenport–Heilbronn discriminator (the step must fail for Q0, ρ₀ at Re 0.953), its verdict WATCH or '
        'DISMISSED with its clause; beside it the reciprocal-side read at statement grade against rh_iff_nb (SIDE-explicit-formula v0.24) and '
        'NymanBeurlingPremise, the literature read before any statement is drafted, no claim (relay data/b703_registrations.txt (iii)). Trigger: '
        'when the manuscripts are in hand. Status OPEN.')
P3_H = ('*Appended 2026-10-22 by b703, under the author`s word at the zero-sum prompt, “Davenport–Heilbronn zeros beyond the strip” -- THE ORDER '
        '**`W-ORD-P3-CONTOUR-SIGMA`**, ENTERED:*')
P3_B = (' read the b685-b687 derivation banks for the σ range of the contour whose argument principle gives P3, and the b696 tail-ball tool for the σ '
        'range its zero-tail bound assumes; print whether each encloses every zero of Λ_Q, including any with Re ρ > 1 above the certified list`s '
        'height. Nothing is recomputed and no figure is restated until that read is banked. Its occasion: the Epstein step`s zero sum stated over '
        'the strip-free Wide.WideConfig (SIDE-explicit-formula v0.37, Schema/EpsteinZQ.lean), b590`s EpsteinPremises link not stated, a residue -- '
        'its explicit formula sums the closed strip alone, which Davenport–Heilbronn makes false for Z_Q. Trigger: b705 step zero. Status OPEN.')
E0M_H = ('*Appended 2026-10-22 by b703, under the author`s word at the classK’ prompt -- THE ORDER **`W-ORD-E0-MET-CLASSK`**, ENTERED:*')
E0M_B = (' the E0 rule`s MET (relay tools/e0_rule.py :308-:315) extended by ruling with classK and classKsum, and classK’ and acDeriv beside them: at '
         'b703 E0 read PREDICATE-UNLISTED at the three inclusions classK_subset_classK’, classK_subset_classKsum and classKsum_subset_classK’ '
         '(relay data/b703_widening_grade.txt, the divergence rows), the hand grade DERIVES standing; e0_rule.py not edited at b703. With it, at '
         'b705, the companion glossary rows h2_sign’ and h2_sign_sum raised with their compiled relations, once that grade is settled, and the '
         'question whether an E0 disagreement holds a merge (the merge at b703 made on “the gate`s reading” while E0 disagreed) for the navigator to '
         'rule. Trigger: b705. Status OPEN.')
SAD_H = ('*Appended 2026-10-22 by b703 beneath `W-ORD-STANDING-ARMS-B703` (:15456), under `(R313)`(7) and the author`s word “add needed arms” -- THE '
         'ORDER DISCHARGED:*')
SAD_B = (' the four standing arms added at b703 -- G-CORRESPONDENCE-CURRENCY, G-README-CURRENCY, G-PARTNER-COPIES, G-SISTER-PINS -- each a reading arm '
         'printing its figure every act from relay tools/b703_standing_figures.py, its baseline b703`s figure (relay data/b703_standing_figures.json), '
         'failing from b704 on a regression from the previous act`s figure, each with a control on a mutated copy that raises the figure; '
         'G-BINDER-PROVENANCE enters when its tool exists. Status DISCHARGED.')


def orders(*a):
    """OPEN_TRAILS: the four annotations beneath standing orders (the widening discharged, the closure join's opening read, KEYSTONE-HEADS's trigger
    moved, STANDING-ARMS-B703 discharged) and the four orders entered (Q0-BAND-CONTROL discharged, QUASI-RH-FIELD-WATCH, P3-CONTOUR-SIGMA,
    E0-MET-CLASSK), appended through the guarded landing in that order."""
    land([('OPEN_TRAILS.md', WD_H, NL + WD_H + WD_B + NL), ('OPEN_TRAILS.md', LJA_H, NL + LJA_H + LJA_B + NL), ('OPEN_TRAILS.md', KHM_H, NL + KHM_H + KHM_B + NL),
          ('OPEN_TRAILS.md', SAD_H, NL + SAD_H + SAD_B + NL), ('OPEN_TRAILS.md', QB_H, NL + QB_H + QB_B + NL), ('OPEN_TRAILS.md', QW_H, NL + QW_H + QW_B + NL),
          ('OPEN_TRAILS.md', P3_H, NL + P3_H + P3_B + NL), ('OPEN_TRAILS.md', E0M_H, NL + E0M_H + E0M_B + NL)], '%s_orders_line.json' % ACT, 'orders', entry=None,
         check=[('OPEN_TRAILS.md', K.ORDER_HELD, 'W-ORD-CLASSK-WIDENING-HELD'), ('OPEN_TRAILS.md', 15454, 'W-ORD-KEYSTONE-HEADS'),
                ('OPEN_TRAILS.md', 15452, 'W-ORD-LV-CLOSURE-JOIN'), ('OPEN_TRAILS.md', 15456, 'W-ORD-STANDING-ARMS-B703')], dry='dry' in a)


# ================================================================================ COMPONENT 4: THE FOUR STANDING ARMS' BASELINE ((R313)(7))
def figures(*a):
    """data/b703_standing_figures.txt (.json): the four figures by relay tools/b703_standing_figures.py, each with its rows -- b703's figures the
    baseline the arms read; each reader's seconds printed (a part over 450 s splits at the next run)."""
    import b703_standing_figures as SF
    t0 = time.time()
    c, cr = SF.correspondence()
    t1 = time.time()
    r, rr = SF.readme()
    t2 = time.time()
    p, pr = SF.partners()
    t3 = time.time()
    s, sr = SF.pins(None)
    t4 = time.time()
    L = ['%s -- COMPONENT 4, (R313)(7): THE FOUR STANDING ARMS` FIGURES, b703`S THE BASELINE (%s)' % (ACT, utc()), '',
         '### by relay tools/b703_standing_figures.py; each arm prints its figure every act and fails from b704 on a regression from the previous',
         '### act`s figure; rows beneath each figure. Seconds: correspondence %.1f ; README %.1f ; partners %.1f ; pins %.1f.' % (t1 - t0, t2 - t1, t3 - t2, t4 - t3), '',
         '== G-CORRESPONDENCE-CURRENCY: FIGURE %d (rows at a moved tag with a changed statement) ; rows are papers: current | behind | changed | unread' % c]
    L += ['  %-40s %3d | %3d | %3d | %3d %s%s' % (x['paper'], x['current'], x['behind'], x['changed'], x['unread'], ('; ' + x['reason']) if x['reason'] else '',
                                               ('; changed: ' + '; '.join(x['changed_rows'][:8])) if x['changed_rows'] else '') for x in cr]
    L += ['', '== G-README-CURRENCY: FIGURE %d (README lines carrying a stale tag or count) ; rows are reads: line | kernel | cited | highest | state' % r]
    L += ['  :%-4d %-30s %-8s %-8s %s' % (x['line'], x['kernel'], x['cited'], x['highest'] or '-', x['state']) for x in rr]
    L += ['', '== G-PARTNER-COPIES: FIGURE %d (lines differing, summed) ; rows are papers: lines differing | the copy | its partner' % p]
    L += ['  %-40s %4s | %s | %s%s' % (x['paper'], x['differing'] if x['differing'] is not None else '-', x['path'], x['partner'],
                                        (' ; table not found: %s' % x['reason']) if x.get('reason') else '') for x in pr]
    L += ['', '== G-SISTER-PINS: FIGURE %d (the faces page`s kernels whose pin moved against the baseline -- b703`s own, so 0) ; the federation`s pin %s ;'
          % (s, sr['federation']), '   the faces page`s kernels %s ; rows are kernels: Lean | Mathlib' % ', '.join(sr['faces'])]
    L += ['  %-34s %-28s %s' % (k, v[0] or '-', v[1] or '-') for k, v in sorted(sr['rows'].items())]
    L += ['', '### ### **FIGURES: CORRESPONDENCE %d ; README %d ; PARTNERS %d ; PINS %d -- b703`S BASELINE.**' % (c, r, p, s)]
    if 'dry' not in a:
        put_txt('%s_standing_figures.txt' % ACT, L)
        put_json('%s_standing_figures.json' % ACT, dict(at=utc(), correspondence=dict(figure=c, papers=cr), readme=dict(figure=r, rows=rr),
                                                        partners=dict(figure=p, rows=pr), pins=dict(figure=s, rows=dict((k, list(v)) for k, v in sr['rows'].items()),
                                                                                                    federation=list(sr['federation'] or []), faces=sr['faces'])))
    print(NL.join(L))


# ================================================================================ COMPONENT 2: THE CELLS A MOVED TAG NAMES (data/b698_rules.txt row (1)), THE DRY RUN
ROSTER_ALL = 'b672_roster_read.json'


def cells(*a):
    """`cells dry`: data/b703_correspondence_dry.txt -- the generator run dry (full) on b672's roster, nothing written by it; the cells naming
    SIDE-explicit-formula it would change (its tag moved v0.35 -> v0.36 -> v0.37 this act) printed for the prompt before any write."""
    r = subprocess.run([sys.executable, '-X', 'utf8', '-B', os.path.join(T, 'correspondence_gen.py'), 'dry', os.path.join(D, ROSTER_ALL), 'full'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace', cwd=ROOT, timeout=580)
    out = ((r.stdout or '') + (r.stderr or '')).replace(chr(13), '')
    diff = [l for l in out.split(NL) if re.match(r'^    \S+ :\d+ \| ', l)]
    ef = [l for l in diff if 'SIDE-explicit-formula' in l]
    verdict = [l for l in out.split(NL) if l.startswith('### ### **TABLES')]
    L = ['%s -- COMPONENT 2, (R313)(3): THE CORRESPONDENCE GENERATOR RUN DRY OVER THE CELLS NAMING SIDE-explicit-formula (%s)' % (ACT, utc()), '',
         '### the run, nothing written by it: `python -X utf8 -B tools/correspondence_gen.py dry data/%s full` (exit %d), the local clones` tags read, '
         'no remote call; SIDE-explicit-formula`s tag moved this act v0.35 -> v0.36 (dfadc8c) -> v0.37 (38e2734).' % (ROSTER_ALL, r.returncode), '',
         '### THE DIFF (rows are cells changed; document :line ; column ; kernel ; old ; new), verbatim:'] + (diff or ['    NONE'])
    L += ['### its verdict line, verbatim:'] + (verdict or ['    ### NOT READ'])
    tabs = [t['doc'] for t in (jl(ROSTER_ALL).get('tables') or []) if 'SIDE-explicit-formula' in (t.get('kernels') or [])]
    L += ['', '### THE POSITIVE CONTROL, FROM THE ROSTER ITSELF (relay data/%s, each table`s `kernels`): the tables naming SIDE-explicit-formula %d -- %s ;'
              % (ROSTER_ALL, len(tabs), ', '.join(tabs) or 'NONE'),
          '### the generator read them (TABLES and SHAPED in its verdict) and changed none; its print gives the held cells by category alone (ABSENT, NO',
          '### PRINT BANK, NOT PRINTED, DEPOSIT PIN, MULTI), not by kernel, so which category holds each of the kernel`s cells is not read here.']
    named = [l for l in out.split(NL) if 'SIDE-explicit-formula' in l]
    L += ['', '### THE CONTROL: every line of the generator`s own print naming SIDE-explicit-formula (%d), verbatim -- the cells it read for the kernel '
              'and the category that holds each, so a 0 is not a reader that never reached the kernel:' % len(named)] + ['    ' + l.strip()[:260] for l in named] + (
        [] if named else ['    ### NONE: THE GENERATOR`S PRINT NAMES NO SIDE-explicit-formula CELL'])
    L += ['', '### ### **CELLS NAMING SIDE-explicit-formula THE GENERATOR WOULD CHANGE %d ; CELLS CHANGED ON THE ROSTER %d ; LINES OF ITS PRINT NAMING THE '
              'KERNEL %d ; NOTHING WRITTEN.**' % (len(ef), len(diff), len(named))]
    put_txt('%s_correspondence_dry.txt' % ACT, L)
    print(NL.join(L))


# ================================================================================ COMPONENT 5: THE GUARD'S DRY RUN (b702's route, carried with b703's names)
def guard(*a):
    """data/b703_guard_dry.txt (.json): the suite's `--guard-dry` run in its own process (it writes nothing), its print banked verbatim; the
    writes by mode read from the suite's own writer_plan; the writer block's `if PRERUN:` line read from the suite's text by number."""
    import b703_checks as CH
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'b703_checks.py'), '--guard-dry'], capture_output=True, text=True, encoding='utf-8',
                       errors='replace', cwd=ROOT)
    src = rd(os.path.join(T, 'b703_checks.py')).split(NL)
    k = next((i for i, l in enumerate(src) if l.strip() == CH.GUARD_WRITE), None)
    writes = {}
    for mode, args in (('prerun', (True, False, False, False)), ('pre-push', (False, False, False, False)), ('post-push', (False, True, False, True))):
        writes[mode] = CH.writer_plan(*args)[1]
    ok = r.returncode == 0 and k is not None and src[k - 1].strip() == 'if PRERUN:' and writes['pre-push'] == [] and writes['post-push'] == [] \
        and writes['prerun'] == ['data/b703_arm_seconds_<part>.json'] and 'POST-ROOT PATH WRITES NONE' in r.stdout
    L = ['%s -- COMPONENT 5: THE PRERUN GUARD HELD AT THE CARRY, ITS DRY RUN (%s)' % (ACT, utc()), '',
         '### the suite`s `--guard-dry` run in its own process, writing nothing; its print verbatim beneath. The guard: tools/b703_checks.py :%d `%s`,'
         % (k, src[k - 1].strip() if k else '?'), '### the line above the per-part seconds write at :%d -- as b702 restored it.' % ((k or 0) + 1), '',
         '### THE PRINT, VERBATIM (exit %d):' % r.returncode]
    L += [x for x in r.stdout.rstrip(NL).split(NL)]
    L += ['', '### THE WRITES BY MODE, READ FROM THE SUITE`S writer_plan: %s' % '; '.join('%s %s' % (m, w or 'NONE') for m, w in writes.items()), '',
          '### ### **%s**' % ('THE GUARD HELD ; THE POST-ROOT PATH WRITES NONE OF THE PER-PART SECONDS BANKS ; THE PRE-RUN WRITES THEM ALONE'
                               if ok else '### THE GUARD IS NOT AS READ -- SEE ABOVE')]
    if 'dry' not in a:
        put_txt('%s_guard_dry.txt' % ACT, L)
        put_json('%s_guard_dry.json' % ACT, dict(at=utc(), writes=writes, guard_line=k, exit=r.returncode, ok=ok))
    print(NL.join(L))


# ================================================================================ THE LATE ROUTES (b702's, carried with b703's names)
import edit_route as ER            # noqa: E402


def capture():
    """b701's capture: the seat's session from K.ANCHOR, then each continuation (K.SESSIONS_AFTER) from its own anchor."""
    rows = ER.capture(SESSION, K.ANCHOR, SUBAGENTS)
    for sid, anc in K.SESSIONS_AFTER:
        more = ER.capture('%s/%s.jsonl' % (PROJ, sid), anc, '%s/%s/subagents' % (PROJ, sid))
        if not more:
            sys.exit('### THE CONTINUATION SESSION %s READ NO COMMAND (the anchor %r not found as a user line) -- NOTHING WRITTEN' % (sid, anc))
        rows += [dict(r, src=r['src'] + ' ' + sid[:8]) for r in more]
    rows.sort(key=lambda r: r['ts'])
    bg = R._bg_calls()
    for i, r in enumerate(rows):
        r['n'] = i + 1
        r['bg'] = (r.get('ts'), r.get('cmd')) in bg
    return rows


R.capture = capture
prev_capture = R.prev_capture


def reads(*a):
    """b701's route (data/b698_rules.txt row (2)) over the seat's session from the anchor."""
    rows = []
    for i, o, _st, sid in R._session_rows():
        if o.get('type') != 'assistant':
            continue
        for c in (o.get('message') or {}).get('content') or []:
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'Read':
                inp = c.get('input') or {}
                p = inp.get('file_path') or ''
                rows.append(dict(line=i if sid == K.SESSION_ID else '%s:%d' % (sid[:8], i), ts=o.get('timestamp'), path=p, offset='offset' in inp,
                                 limit='limit' in inp, lines=R._lines_now(p)))
    whole = [r for r in rows if not (r['offset'] and r['limit'])]
    bad = [r for r in whole if r['lines'] is None or r['lines'] >= 200]
    L = ['%s -- THE READ CALLS SINCE THE ANCHOR, BY data/b698_rules.txt ROW (2) (%s)' % (ACT, utc()), '',
         '### the rule: whole where the file is under two hundred lines, by offset and limit otherwise. Rows are Read calls without both offset and',
         '### limit: transcript line | time | the file`s lines read now | WITHIN THE RULE or ### AN OFFENCE | path']
    L += ['  %s | %s | %s | %s | %s' % (r['line'], r['ts'], r['lines'], '### AN OFFENCE' if r in bad else 'WITHIN THE RULE', r['path']) for r in whole] or ['  NONE']
    L += ['', '### ### **READ CALLS %d ; WITH OFFSET AND LIMIT %d ; WHOLE %d ; WHOLE OF A FILE OF 200 LINES OR MORE %d.**' % (
        len(rows), len(rows) - len(whole), len(whole), len(bad))]
    if 'dry' not in a:
        put_txt('%s_read_calls.txt' % ACT, L)
    print(NL.join(L[-1 - len(bad):]) if bad else L[-1])
    for r in bad:
        print('  OFFENCE transcript line %s %s %s lines' % (r['line'], r['path'], r['lines']))


R.reads = reads
edit_route_offences = R.edit_route_offences
QUOTED, REDIRECT_NULL, REDIRECT_ANY, PIPE_FILTER, PY_PRINT_READ, MOVE_OR_DELETE, SED_KIND = (
    R.QUOTED, R.REDIRECT_NULL, R.REDIRECT_ANY, R.PIPE_FILTER, R.PY_PRINT_READ, R.MOVE_OR_DELETE, R.SED_KIND)
local_lean, delete_shape, chained_after, seal_hashes, root_banks_state = R.local_lean, R.delete_shape, R.chained_after, R.seal_hashes, R.root_banks_state
root_banks, rootbanks, root, root_arm, table_final = R.root_banks, R.rootbanks, R.root, R.root_arm, R.table_final
_iso_epoch, _git_ct, _files_of, _ledger_adds, _amended_after = R._iso_epoch, R._git_ct, R._files_of, R._ledger_adds, R._amended_after
DISPATCH_CMD = re.compile(r'(^|&&\s*|;\s*)gh workflow run\b|_record\.py dispatch\b(?![^\n]*\bdry\b)', re.M)


def commands(*a):
    """b702's route with b703's names: the act's command capture, G-EDIT-ROUTE's reading over it and over the previous act's window, the
    local lean reading (N1), the dispatches (two ordered, one per branch), the detached runs, sed, the redirects, the pipes, the one-line
    programs, the moves and deletes by shape, the outbound requests. data/b703_commands.txt (.json)."""
    rows = capture()
    if not rows:
        sys.exit('### THE COMMAND CAPTURE READ NO COMMAND -- NOTHING WRITTEN')
    hits = edit_route_offences(rows)
    prev = prev_capture()
    phits = edit_route_offences(prev)
    sh_ = [r for r in rows if r['tool'] in ('Bash', 'PowerShell')]
    lean = [r for r in sh_ if local_lean(r['cmd'])]
    mv = [r for r in sh_ if MOVE_OR_DELETE.search(QUOTED.sub('""', r['cmd']))]
    disp = [r for r in sh_ if DISPATCH_CMD.search(QUOTED.sub('""', r['cmd']))]
    detach = [r for r in sh_ if (r.get('bg') or re.search(r'Start-Process|\bnohup\b|run_in_background', QUOTED.sub('""', r['cmd'])))]
    seds = [r for r in sh_ if R.sed_cmd(r['cmd'])]
    nulls = [r for r in sh_ if REDIRECT_NULL.search(QUOTED.sub('""', r['cmd']))]
    redir = [r for r in sh_ if REDIRECT_ANY.search(QUOTED.sub('""', r['cmd']))]
    pipes = [r for r in sh_ if PIPE_FILTER.search(QUOTED.sub('""', r['cmd']))]
    anypipe = [r for r in sh_ if '|' in QUOTED.sub('""', r['cmd']).replace('||', '')]
    pyreads = [r for r in sh_ if PY_PRINT_READ.search(r['cmd'])]
    shapes = [(r['n'],) + delete_shape(r['cmd']) for r in mv if delete_shape(r['cmd'])[0]]
    chained = [r['n'] for r in mv if delete_shape(r['cmd'])[0] and chained_after(r['cmd'])]
    halves = dict((r['n'], len([x for x in re.split(r'&&|\|\||;|\|', QUOTED.sub('""', r['cmd'])) if x.strip()])) for r in mv)
    ob = R.outbound()
    L = ['%s -- THE ACT`S COMMAND BANK, G-EDIT-ROUTE`S READING, THE LOCAL LEAN READING (N1), THE DISPATCHES, THE MOVES AND DELETES, THE OUTBOUND REQUESTS (%s)' % (ACT, utc()), '',
         '### the source: the seat`s session %s from its first user line carrying %r, with its subagents` transcripts%s' % (
             K.SESSION_ID, K.ANCHOR, ''.join('; the continuation %s from its first user line carrying %r' % (s[:8], a_) for s, a_ in K.SESSIONS_AFTER)),
         '### commands read: %d' % len(rows), '', '### THE OFFENDING COMMANDS, EACH PRINTED WHOLE (%d):' % len(hits)]
    for r, o in hits:
        L += ['  #%d %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not hits:
        L.append('  NONE')
    L += ['', '### THE PREVIOUS ACT`S CAPTURE AFTER ITS POST-PUSH SUITE (%s, session %s): %d commands from %s, its offences printed whole (%d):' % (
        PREV, R.PREV_SESSION[:8], len(prev), prev[0]['ts'] if prev else '-', len(phits))]
    for r, o in phits:
        L += ['  #%s %s %s %s -- %s' % (r['n'], r['ts'], r['src'], r['tool'], '; '.join(k for k, _ in o))] + ['      ' + x for x in r['cmd'].split(NL)]
    if not phits:
        L.append('  NONE')
    L += ['', '### THE COMMANDS THAT RUN lean OR lake ON THIS HOST (%d):' % len(lean)] + (['  #%d %s' % (r['n'], r['cmd'][:200]) for r in lean] or ['  NONE'])
    L += ['', '### THE RUNNER DISPATCHES (two ordered this act, N1: one per branch tip) (%d):' % len(disp)] + (
        ['  #%d %s' % (r['n'], r['cmd'][:240]) for r in disp] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT START A DETACHED RUN, BY THEIR TEXT OR THE TOOL`S run_in_background PARAMETER (%d):' % len(
        detach)] + (['  #%d %s%s' % (r['n'], '[run_in_background] ' if r.get('bg') else '', r['cmd'][:240]) for r in detach] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING sed IN ANY FORM (data/b685_rules.txt row (2)) (%d):' % len(seds)] + (
        ['  #%d %s' % (r['n'], r['cmd'][:240]) for r in seds] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A REDIRECT ONTO /dev/null, read outside quoted strings (%d):' % len(nulls)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], r['cmd'].split(NL)[0][:200]) for r in nulls] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A REDIRECT OF ANY STREAM, read outside quoted strings (%d):' % len(redir)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in redir] or ['  NONE'])
    L += ['', '### THE COMMANDS PIPING INTO A SHELL FILTER (head, tail, wc, grep and the like), read outside quoted strings (%d):' % len(pipes)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in pipes] or ['  NONE'])
    L += ['', '### THE COMMANDS CARRYING A PIPE OF ANY KIND, read outside quoted strings (%d):' % len(anypipe)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:200]) for r in anypipe] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT RUN AN INTERPRETER`S ONE-LINE PROGRAM (python -c), each its first line (%d):' % len(pyreads)] + (
        ['  #%d %s %s' % (r['n'], r['ts'], ' '.join(r['cmd'].split())[:220]) for r in pyreads] or ['  NONE'])
    L += ['', '### THE COMMANDS THAT MOVE OR DELETE A FILE OR A BRANCH, EACH PRINTED WHOLE (%d):' % len(mv)]
    for r in mv:
        L += ['  #%d %s %s' % (r['n'], r['ts'], r['tool'])] + ['      ' + x for x in r['cmd'].split(NL)]
    if not mv:
        L.append('  NONE')
    L += ['', '### THE BRANCH DELETES BY SHAPE ((R313)(9) and data/b694_rules.txt row (1): one branch per command, no glob and no variable in any half, '
              'nothing chained after): ' + ('; '.join('#%d deletes %s, halves %d, globs %s, variables %s, chained after %s' % (
                  n, d, halves.get(n, 0), gl or 'none', vs or 'none', n in chained) for n, d, gl, vs in shapes) or 'NONE')]
    L += ['', '### THE OUTBOUND REQUESTS OTHER THAN git AND gh (web searches, subagent prompts and fetches), each with the author`s identifiers found '
              'in it (%d):' % len(ob)]
    L += ['  line %s | %s | %s | identifiers %s | %s' % (r['line'], r['tool'], r['ts'], r['identifiers'] or 'NONE', ' '.join(r['text'].split())[:200]) for r in ob] or ['  NONE']
    L += ['', '### EVERY COMMAND (n | time | source | tool | first line, 160 characters):']
    L += ['  #%d | %s | %s | %s | %s' % (r['n'], r['ts'], r['src'], r['tool'], r['cmd'].split(NL)[0][:160]) for r in rows]
    good = sum(1 for n, d, gl, vs in shapes if len(d) == 1 and not gl and not vs and n not in chained)
    L += ['', '### ### **COMMANDS %d ; G-EDIT-ROUTE OFFENCES %d (SED IN ANY FORM AMONG THEM %d) ; THE PREVIOUS ACT AFTER ITS POST-PUSH SUITE %d '
              'COMMANDS, OFFENCES %d ; LOCAL lean OR lake COMMANDS %d ; DISPATCHES %d ; DETACHED RUNS %d ; sed COMMANDS %d ; REDIRECTS ONTO /dev/null %d ; '
              'REDIRECTS OF ANY STREAM %d ; PIPES INTO A SHELL FILTER %d ; PIPES OF ANY KIND %d ; ONE-LINE PROGRAMS %d ; MOVE OR DELETE COMMANDS %d ; '
              'BRANCH DELETES OF ONE BRANCH, NO GLOB, NO VARIABLE AND NOTHING CHAINED AFTER %d OF %d ; OUTBOUND REQUESTS %d, AN IDENTIFIER IN %d.**' % (
                  len(rows), len(hits), sum(1 for _r, o in hits if any(k == SED_KIND or k.startswith('S sed') for k, _ in o)), len(prev), len(phits),
                  len(lean), len(disp), len(detach), len(seds), len(nulls), len(redir), len(pipes), len(anypipe), len(pyreads), len(mv), good,
                  len(shapes), len(ob), sum(1 for r in ob if r['identifiers']))]
    if 'dry' in a:
        print(L[-1])
        for r, o in hits:
            print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
        return
    put_txt('%s_commands.txt' % ACT, [l.replace('\r', '') for l in L])
    put_json('%s_commands.json' % ACT, dict(at=utc(), anchor=K.ANCHOR, rows=rows,
                                           offences=[dict(n=r['n'], kinds=[k for k, _ in o]) for r, o in hits],
                                           prev=dict(act=PREV, session=R.PREV_SESSION, rows=len(prev),
                                                     offences=[dict(n=r['n'], ts=r['ts'], kinds=[k for k, _ in o]) for r, o in phits]),
                                           local_lean=[r['n'] for r in lean], dispatches=[r['n'] for r in disp], detached=[r['n'] for r in detach],
                                           seds=[r['n'] for r in seds], null_redirects=[r['n'] for r in nulls], redirects=[r['n'] for r in redir],
                                           pipes=[r['n'] for r in pipes], any_pipes=[r['n'] for r in anypipe], py_programs=[r['n'] for r in pyreads],
                                           moves_deletes=[r['n'] for r in mv],
                                           delete_shapes=[dict(n=n, deletes=d, globs=gl, variables=vs, halves=halves.get(n), chained=n in chained)
                                                          for n, d, gl, vs in shapes],
                                           outbound=ob))
    print(L[-1])
    for r, o in hits:
        print('  OFFENCE #%d %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))
    for r, o in phits:
        print('  PREVIOUS-ACT OFFENCE #%s %s: %s' % (r['n'], '; '.join(k for k, _ in o), r['cmd'].split(NL)[0][:200]))


_KERNS_698 = R._kerns


def _kerns():
    return _KERNS_698() + ['SIDE-substrate-cluster']     # ### b700's list, carried by b701 and b702, carried


R._kerns = _kerns


def kernels(*a):
    ks = list(dict.fromkeys(_kerns()))
    import b633_record as R3
    put_json('%s_kernels_face.json' % ACT, dict(at=utc(), kernels=R3.kern_state(ks)))
    print('  kernels read: %d (read after Component 2`s merges and tags; no kernel written after this read)' % len(ks))


def _standing():
    import b702_worklist as K702
    return sorted((set(R._g2_of(os.path.join(ROOT, *K.B702_FACE.split('/')))) - set(K702.ACT_ARMS)) | set(K.STANDING_ADDED))


R._standing = _standing


def standing(*a):
    st = _standing()
    print('  STANDING %d: %s' % (len(st), ' '.join(st)))


armsecs = R.armsecs
desk, gatebanks, mbuild, mroot, mverify = R.desk, R.gatebanks, R.mbuild, R.mroot, R.mverify


def _one_git_write():
    return R._one_git_write()


# ================================================================================ THE SCORES: (N1)-(N5) OF (R313)'S FERRY, THE SEAT'S (S1)-(S3)
# ### data/b686_rules.txt row (1), standing: a scorer reads banks and commits and not the entry; the entry reads the scorer's bank. `scores`
# ### writes data/b703_scores.json once, before `findings`; a reading that waits on a later bank stands PENDING there and is read at the close.
NK, SK, SCORE_KEYS = R.NK, R.SK, R.SCORE_KEYS
N5_RELAY_DATA = ('act_roots.txt', 'b702_closing_push_out.txt', 'b675_corrigenda.txt', 'glossary.txt')
N5_RELAY_TOOLS = ('tools/rule_arms.py',)
MERGED = (('v0.36', 'aa9a543f2144de0eee791ec00e904416567d68b8', 'v0.35'), ('v0.37', '5f8961b00191957d67b960fd760ce5013e412d2a', 'v0.36'))


def _s_scores():
    return dict((k, (v[0], v[1].replace('b698_', ACT + '_'))) for k, v in R._s_scores().items())


def _latest_runs():
    out = {}
    for r in jl('%s_runner_rows.json' % ACT).get('rows') or []:
        out[r.get('ref')] = r
    return out


def _n1():
    """N1: no lean process on this host; two runner dispatches, one per branch tip, each read by its run id with its artifact's sha256 verified."""
    cm = jl('%s_commands.json' % ACT)
    dj = jl('%s_dispatches.json' % ACT).get('rows') or []
    lr = _latest_runs()
    read = [(d.get('ref'), d.get('run_id'), (lr.get(d.get('ref')) or {}).get('run_id'), bool((lr.get(d.get('ref')) or {}).get('artifact_sha256'))) for d in dj]
    ok = bool(cm) and not cm.get('local_lean') and len(cm.get('dispatches') or []) == 2 and len(dj) == 2 and len(set(d.get('ref') for d in dj)) == 2 \
        and all(a_ == b_ and s for _r, a_, b_, s in read)
    return ('HELD' if ok else 'REFUTED'), (
        'commands of this act that run lean or lake on this host: %s; runner dispatches in the capture: %s (relay data/b703_commands.json); the '
        'dispatches bank (relay data/b703_dispatches.json): %s -- each ref, its run, the run read for it, its artifact`s sha256 verified' % (
            cm.get('local_lean') if cm else 'unread', cm.get('dispatches') if cm else 'unread', ['%s run %s read %s sha256 %s' % (r_[:7], a_, b_, s) for r_, a_, b_, s in read]))


def _peel(tag):
    return g(EF, 'rev-parse', '--verify', '--quiet', 'refs/tags/%s^{commit}' % tag).strip()


def _n2():
    """N2: the widening's diff one token at H2SignWide.lean :59; its grade every new name at the standard three; v0.36 tagged on the gate's
    reading (the merge's second parent the built tip, the merged tree the built tree)."""
    wd = rdn('%s_widening_diff.txt' % ACT)
    wj = jl('%s_widening_grade.json' % ACT)
    one = 'ONE TOKEN: le_rfl -> one_ne_zero' in wd and 'NOTHING ELSE TOUCHED: True' in wd
    std3 = len(wj.get('rows') or []) == 10 and all('PROFILE STD3' in r for r in wj.get('rows') or [])
    m = _peel('v0.36')
    par = g(EF, 'log', '-1', '--format=%P', m).split() if m else []
    gate = (_latest_runs().get(MERGED[0][1]) or {}).get('gate')
    tagged = bool(m) and len(par) == 2 and par[1] == MERGED[0][1] and g(EF, 'rev-parse', m + '^{tree}').strip() == g(EF, 'rev-parse', MERGED[0][1] + '^{tree}').strip() \
        and gate == 'DERIVES'
    ok = one and std3 and tagged
    return ('HELD' if ok else 'REFUTED'), (
        'the diff one token at :59, nothing else touched: %s (relay data/b703_widening_diff.txt); every graded name at the standard three: %s (relay '
        'data/b703_widening_grade.json, %d rows); v0.36 = %s, its parents %s, the built tip %s, the gate %s: tagged on the gate`s reading %s' % (
            one, std3, len(wj.get('rows') or []), m[:7] or 'ABSENT', [p[:7] for p in par], MERGED[0][1][:7], gate, tagged))


EZ_ZERO = ('zqZeros_ne_zero', 'zq_count', 'zq_explicit_formula', 'zq_li_nonneg_imp_online')


def _n3():
    """N3: the Epstein step states nothing about a zero as proved -- every theorem naming the zeros INTERFACES on its premises, no sorry in the
    module at v0.37; every premise structure printed beside its name in the grade bank."""
    ej = jl('%s_epstein_grade.json' % ACT)
    et = rdn('%s_epstein_grade.txt' % ACT)
    rows = ej.get('rows') or []
    zr = [r for r in rows if r.split(' ')[0] in EZ_ZERO]
    inter = len(zr) == len(EZ_ZERO) and all(' GRADE INTERFACES ' in r for r in zr)
    src = _show(EF, 'v0.37', EZ) or ''
    code = re.sub(r'--[^\n]*', '', re.sub(r'/-[\s\S]*?-/', '', src))
    prem = all(('  %s (%s' % (n, EZ)) in et for n in EZ_PREMISES)
    ok = ej.get('ok') is True and inter and bool(src) and 'sorry' not in code and prem
    return ('HELD' if ok else 'REFUTED'), (
        'the theorems naming Λ_Q`s zeros, each INTERFACES on its premises: %s (%s); no sorry in %s at v0.37: %s; every premise printed beside its '
        'name (%s): %s; every check agreeing and every salt-check passed: %s (relay data/b703_epstein_grade.json)' % (
            inter, '; '.join(zr), EZ, bool(src) and 'sorry' not in code, ', '.join(EZ_PREMISES), prem, ej.get('ok')))


def _n4():
    """N4: the registrations committed alone before the band bank was written; the reader's count 163, ρ₀ at Re 0.95326047479466068625; no
    witness or Li coefficient computed."""
    reg_ct = _git_ct(ROOT, K.REGS_COMMIT)
    reg_files = _files_of(ROOT, K.REGS_COMMIT)
    qt = rdn('%s_q0_band.txt' % ACT)
    m = re.search(r'\((\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ)\)', qt.split(NL)[0])
    band_at = _iso_epoch(m.group(1)) if m else None
    cnt = 'ROWS 163 (THE CONTROL AGREES)' in qt and 'ρ₀ READ True' in qt and K.RHO0_RE in qt
    nw = 'NO WITNESS COMPUTED' in qt
    ok = reg_files == ['data/b703_registrations.txt'] and bool(reg_ct) and bool(band_at) and reg_ct < band_at and cnt and nw
    return ('HELD' if ok else 'REFUTED'), (
        'the registrations committed alone at %s (%s) at %s, before the band bank`s stamp %s: %s; the count 163 and ρ₀ at Re %s read: %s; no witness '
        'computed: %s (relay data/b703_registrations.txt, data/b703_q0_band.txt)' % (
            K.REGS_COMMIT, reg_files, R.time.strftime('%Y-%m-%dT%H:%M:%SZ', R.time.gmtime(reg_ct)) if reg_ct else '-', m.group(1) if m else '-',
            bool(reg_ct and band_at and reg_ct < band_at), K.RHO0_RE, cnt, nw))


def _n5():
    import rule_arms as RA
    import b633_record as R3
    import b702_worklist as K702
    face = jl('%s_kernels_face.json' % ACT).get('kernels') or {}
    now = R3.kern_state(list(face)) if face else {}
    k_ok = bool(face) and all(now[k] == list(v) for k, v in face.items())
    ef_main = g(EF, 'rev-parse', 'main').strip()
    merges_ok = ef_main == _peel('v0.37') and g(EF, 'rev-list', '--first-parent', '--count', K.EF_MAIN_BEFORE + '..main').strip() == '2'
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', K.PRE_PP) + NL + g(PP, 'diff', '--name-only', K.PRE_PP, 'HEAD')).split(NL) if x.strip()))
    pp_beyond = [x for x in pp_ch if x not in K.PP_WRITTEN]
    renames = [l for l in g(PP, 'diff', '--name-status', '-M', K.PRE_PP, 'HEAD').split(NL) if l[:1] in ('R', 'D')]
    relay_ch = sorted(set(x for x in (g(ROOT, 'diff', '--name-only', K.PRE_RELAY, 'HEAD') + NL + g(ROOT, 'diff', '--name-only')).split(NL) if x.strip()))
    shared_tools = [x for x in relay_ch if x.startswith('tools/') and not re.match(r'^tools/b703_', x) and x not in N5_RELAY_TOOLS]
    kinds_beyond = [x for x in relay_ch if not (re.match(r'^(data|tools)/(b703_|audit_b703_)', x) or re.match(r'^data/terminal_table', x)
                                                or (x.startswith('data/') and x[5:] in N5_RELAY_DATA) or x in N5_RELAY_TOOLS)]
    _r, _n, sh = seal_hashes()
    differ = [t for t, v in sh if v != 'agree']
    added = sorted(set(R._g2_of(FACE)) - set(R._g2_of(os.path.join(ROOT, *K.B702_FACE.split('/')))) - set(K.ACT_ARMS))
    arms_ok = added == sorted(K.STANDING_ADDED)
    lock = _iso_epoch((re.search(r'locked at \(UTC\) : (\S+)', rd(FACE)) or [None, ''])[1])
    amended = (_amended_after(ROOT, lock) + _amended_after(PP, lock) + _amended_after(EF, lock)) if lock else []
    ob = jl('%s_commands.json' % ACT).get('outbound') or []
    ident = [r for r in ob if r.get('identifiers')]
    chained = [d['n'] for d in (jl('%s_commands.json' % ACT).get('delete_shapes') or []) if d.get('chained')]
    gw_ok, gw_note = _one_git_write()
    pre_gl = (_show(ROOT, K.PRE_RELAY, 'data/glossary.txt') or '').replace('\r', '')
    now_gl = R.rd(os.path.join(D, 'glossary.txt')).replace('\r', '')
    gl = now_gl.startswith(pre_gl) and len([l for l in now_gl[len(pre_gl):].split(NL) if l.strip() and not l.startswith('#')]) == 1
    lake = [x for x in g(EF, 'diff', '--name-only', K.EF_MAIN_BEFORE, 'main').split(NL) if x.strip().startswith('lake')]
    ok = k_ok and merges_ok and not pp_beyond and not renames and not kinds_beyond and not shared_tools and not differ and arms_ok and not amended \
        and not ident and not chained and gw_ok and gl and not lake
    return (('HELD' if ok else 'REFUTED'),
            'nothing deposits: the deposit route untouched (draft %s, v5, unpublished); every kernel as the face read it after the merges: %s; '
            'SIDE-explicit-formula`s main the v0.37 merge, two first-parent commits past v0.35: %s; the standing arms added beyond b702`s face, the act '
            'arms apart: %s (the four of (R313)(7) alone: %s); shared tools edited beyond rule_arms.py: %s; sealed tools not agreeing: %s; commits '
            'amended after the seal: %s; deletes with anything chained after: %s; one git write per message (%s): %s; PLACE-papers beyond the named '
            'files: %s; papers moved or renamed: %s; relay files of a kind beyond the act`s banks and tools, the table, the root list, the corrigenda '
            'bank, the glossary and b702`s push-out bank: %s; the glossary appended by one entry alone: %s; lakefiles edited: %s; outbound requests '
            'other than git and gh %d, an identifier of the author in %s' % (
                K.DRAFT, k_ok, merges_ok, added or 'NONE', arms_ok, shared_tools or 'NONE', differ or 'NONE', amended or 'NONE', chained or 'NONE',
                gw_note, gw_ok, pp_beyond or 'NONE', renames or 'NONE', kinds_beyond or 'NONE', gl, lake or 'NONE', len(ob), [r['line'] for r in ident] or 'NONE'))


def scores(*a):
    """`scores [dry]` writes data/b703_scores.json ONCE, before the entry (it refuses where the bank exists); `scores close` reads the readings
    that waited into data/b703_scores_close.json."""
    close = 'close' in a
    S = dict([('N1', _n1()), ('N2', _n2()), ('N3', _n3()), ('N4', _n4()), ('N5', _n5())] + list(_s_scores().items()))
    for k2 in SCORE_KEYS:
        read_score_row(k2, list(S[k2]))
    for k2 in SCORE_KEYS:
        print('  %-5s %s -- %s' % (k2, S[k2][0], str(S[k2][1])[:900]))
    if 'dry' in a:
        return
    if close:
        put_json('%s_scores_close.json' % ACT, dict((k2, list(v)) for k2, v in S.items()))
        return
    if os.path.isfile(os.path.join(D, '%s_scores.json' % ACT)):
        sys.exit('### THE SCORES BANK IS WRITTEN ONCE, BEFORE THE ENTRY (data/b686_rules.txt row (1)) -- NOTHING WRITTEN; `scores close` at the close')
    put_json('%s_scores.json' % ACT, dict((k2, list(v)) for k2, v in S.items()))


_sv, scores_line = R._sv, R.scores_line
_calls, _rl_lines = R._calls, R._rl_lines
NUM = ('none', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
       'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty')


def num_word(n):
    return NUM[n] if 0 <= n < len(NUM) else str(n)


# ================================================================================ THE RECORD: THE ENTRY BEFORE THE ROOT, THE TRAIL CARRYING IT
def TRAIL_HEAD():
    return ('### b703 — lane two, act one hundred and thirty, the research act under (R313): b702 at its weight; its post-root items by corrigendum, '
            'the quote arm and the span line repaired; classK widened at one token (v0.36); the Epstein zeta of x² + xy + 6y² a Lean object (v0.37); '
            'the pins priced; Q0’s off-line zeros counted by real part; four registrations and four standing arms')


R.TRAIL_HEAD = TRAIL_HEAD


def _figs():
    co = jl('%s_corrigendum.json' % ACT)
    ol = [x.get('line') for x in jl('%s_orders_line.json' % ACT).get('lines') or []]
    qt = rdn('%s_q0_band.txt' % ACT)
    qm = re.search(r'IN \(1/2, 7/8\] (\d+)', qt)
    om = re.search(r'OFF THE LINE (\d+), ON IT (\d+)', qt)
    fj_ = jl('%s_standing_figures.json' % ACT)
    tags = dict((t, _peel(t)[:7]) for t, _tip, _p in MERGED)
    return dict(corr_line=co.get('entry_line', '-'), orders=ol + ['-'] * 8, band=qm.group(1) if qm else '-', off=om.group(1) if om else '-',
                on=om.group(2) if om else '-', v036=tags.get('v0.36') or '', v037=tags.get('v0.37') or '',
                figs=dict((k, (fj_.get(k) or {}).get('figure', '-')) for k in ('correspondence', 'readme', 'partners', 'pins')))


def _title():
    f = _figs()
    return ('## classK widened at SIDE-explicit-formula %s; the Epstein zeta of x² + xy + 6y² a Lean object %s; the pins of the closure join and the '
            'interval library priced; Q0’s certified off-line zeros binned by real part, %s in (1/2, 7/8]' % (
                'v0.36' if f['v036'] else 'held at its line', 'v0.37' if f['v037'] else 'held', f['band']))


def _owners_now():
    rows = _defect_short(ACT)
    nav = [r for r in rows if "THE NAVIGATOR'S" in r]
    return rows, nav


def _for_author():
    rows, nav = _owners_now()
    seat = len(rows) - len(nav)
    letters = ', '.join(re.match(r'^\(([a-z])\)', r).group(0) for r in nav)
    return ('(1) paperFT_finset_sum graded INTERFACES on its continuity and support hypotheses where the first hand reading said DERIVES, on the '
            'author’s word at the classK’ prompt; (2) the merge to v0.36 made on the gate’s reading while E0 read PREDICATE-UNLISTED at the three '
            'inclusions, the question entered for b705 under W-ORD-E0-MET-CLASSK; (3) Z_Q’s zero sum stated over the strip-free WideConfig and not '
            'b701’s plan’s closed strip, b590’s EpsteinPremises link a residue; (4) the runner’s first reading of the widening NOT DERIVES on a reader '
            'blind to primes, read again by its run id after the repair, no second dispatch; (5) the companion glossary rows h2_sign’ and h2_sign_sum '
            'not added, raised at b705; (6) the interval library’s pin read from a shallow clone of its main, its price waiting on BINDER-PROVENANCE; '
            '(7) the %s navigator %s (%s) and the seat’s %s defect%s as lettered' % (num_word(len(nav)), 'miss' if len(nav) == 1 else 'misses', letters,
                                                                                   num_word(seat), '' if seat == 1 else 's'))


def _finding_text():
    """the FINDINGS entry, composed before the root: its head line the result sentence; its scores line from the scores bank alone (data/b686_rules.txt
    row (1)); the root carried by the trail record."""
    S = jl('%s_scores.json' % ACT)
    f = _figs()
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    cc = re.search(r'(?<!ANSWER )CITES CHECKED (\d+) ; OK (\d+) ; MISSES (\d+)', rdn(K.CITATION_BANK))
    checks = len(re.findall(r'^### \(R278\)\(4\) THE MID-ACT CHECK ', rdn(K.CITATION_BANK), re.M))
    e = ['', _title(), '',
         'The widened class classK’ now compiles: at SIDE-explicit-formula %s (%s) the sign clause over the wider window class implies h2_sign and so RH, '
         'and h2_sign_sum is equivalent to RH, every new name at the standard three. The Epstein zeta of Q0 = x² + xy + 6y² is a Lean object at %s (%s): its '
         'lattice sum, its completed function, its zeros as a configuration with no strip, its explicit formula’s three terms and the count, each '
         'stated as a named premise and none proved. Of b681’s 163 certified zeros of Q0, %s lie off the line, %s of them with real part in (1/2, 7/8], '
         'the lowest at 0.79799715717868013876 + 29.55176109862911459913 i; the two faces kernels sit at Lean v4.34.0-rc1 and v4.29.1, so the closure '
         'join costs one dispatch at explicit-formula’s pin.' % (f['v036'] and 'v0.36' or 'its line', f['v036'], f['v037'] and 'v0.37' or 'its line', f['v037'],
                                                                f['off'], f['band']), '',
         '*Filed at b703 on the author’s ruling `(R313)` and the author’s words at its prompts; %d question%s put. Banks: relay '
         '`data/b703_widening_grade.txt`, `data/b703_epstein_grade.txt`, `data/b703_pins.txt`, `data/b703_q0_band.txt`, `data/b703_registrations.txt`, '
         '`data/b703_standing_figures.txt`, `data/b703_corrigendum.txt`, `data/b703_tool_repairs.txt`.*' % (n_ans, '' if n_ans == 1 else 's'), '',
         '**The corrigendum** (`(R313)`(1)-(2)): b702 entered at its weight (FINDINGS :%s); the generated entry at FINDINGS :%s letters (j) the mirror '
         'bank’s span line naming b697’s export and (k) the closing push’s first call given the repository’s name; the corrigenda bank appended at '
         'rows (22)-(23); the sealed face, the trail and the root-named banks unedited.' % (c1_[0], f['corr_line']), '',
         '**The repairs** (`(R313)`(2)): G-RULE-RECUT-QUOTE branched on the kind of cut, passing on b702’s paper cut and b697’s kernel cut and failing '
         'a planted late search (relay data/b703_quote_control.txt); the mirror bank’s span line read from the mirror bank chain, b702 the last export '
         '(relay data/b703_span_dry.txt); the runner’s axioms reader reading primed names (relay data/b703_deps_control.txt).', '',
         '**The widening** (`(R313)`(3), N2): H2SignWide.lean :59 le_rfl -> one_ne_zero, one token (relay data/b703_widening_diff.txt); run 39700585515 '
         'DERIVES, 89 of 89 at the standard three; ten theorems graded, eight DERIVES, paperFT_finset_sum INTERFACES on hf and hs, E0 reading '
         'PREDICATE-UNLISTED at the three inclusions; merged --no-ff and tagged v0.36 naming v0.35; the glossary’s classK’ row written on the author’s word.', '',
         '**The Epstein step** (`(R313)`(4), N3): Schema/EpsteinZQ.lean on epstein-b703, run 39703864050 DERIVES, 109 of 109; the premises ZQContinuation, '
         'ZQZeros, ZQExplicitFormula and ZQPremises printed beside their names over Wide.WideConfig, whose open strip (-1/2, 3/2) holds every zero of '
         'Λ_Q; nothing about a zero stated as proved; merged and tagged v0.37 naming v0.36. W-SIGN-7’s Epstein arm closed at “no accessible explicit '
         'ordinates” for x² + xy + 6y², own-computation its unblock path -- that path met by b671-b681’s certified zeros and now carried by a Lean object.', '',
         '**The pins** (`(R313)`(5)): SIDE-explicit-formula at Lean v4.34.0-rc1 and Mathlib de5ce8a9; SIDE-lv-conservation at v4.29.1 and 5e932f97 '
         '(v0.10.0 and v0.13.0 alike); girving/interval at v4.34.1 and d13f23b7. The closure join 1 dispatch at explicit-formula’s pin; the interval '
         'vendoring 1 dispatch, waiting on BINDER-PROVENANCE (relay data/b703_pins.txt); nothing built, edited or vendored.', '',
         '**The count** (`(R313)`(6)(i), N4): the named reader over b681’s bank after both hashes agreed: 163 rows, %s off the line and %s on it; the '
         'bins (1/2, 0.6] 0, (0.6, 0.75] 5, (0.75, 7/8] 10, (7/8, 1) 2; the hypothesis met; the control 163 and ρ₀ at Re 0.95326047479466068625; no '
         'witness computed (relay data/b703_q0_band.txt).' % (f['off'], f['on']), '',
         '**The registrations** (`(R313)`(6)): four written and committed alone before any number (relay b8a36309): the band control (computed here), the '
         'detection law and the cover axis (b705), the field-watch (when the manuscripts are in hand).', '',
         '**The standing arms** (`(R313)`(7)): G-CORRESPONDENCE-CURRENCY, G-README-CURRENCY, G-PARTNER-COPIES and G-SISTER-PINS, b703’s figures the '
         'baseline -- %s, %s, %s, %s (relay data/b703_standing_figures.txt).' % (f['figs']['correspondence'], f['figs']['readme'], f['figs']['partners'],
                                                                                 f['figs']['pins']), '',
         '**The orders** (`(R313)`(3)-(8)): W-ORD-CLASSK-WIDENING-HELD discharged (OPEN_TRAILS :%s); W-ORD-LV-CLOSURE-JOIN`s opening read (:%s); '
         'W-ORD-KEYSTONE-HEADS`s trigger moved (:%s, relay data/b703_rules.txt row (1)); W-ORD-STANDING-ARMS-B703 discharged (:%s); W-ORD-Q0-BAND-CONTROL '
         '(:%s), W-ORD-QUASI-RH-FIELD-WATCH (:%s), W-ORD-P3-CONTOUR-SIGMA (:%s) and W-ORD-E0-MET-CLASSK (:%s) entered.' % tuple(f['orders'][:8]), '',
         '**The citation check** (the gate step from b662): %s cites checked at HEAD, %s OK, %s missed; %d answer check%s, each before its answer was '
         'acted on.' % (cc.group(1) if cc else '-', cc.group(2) if cc else '-', cc.group(3) if cc else '-', checks, '' if checks == 1 else 's'), '',
         scores_line(S), '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): the widening and the Epstein object meet at one clause -- the same sign clause that implies RH '
         'over classK’ is the one an Epstein zeta with off-line zeros must fail, and Q0’s fifteen band zeros are where b705 tests it. It strengthens the '
         'programme’s offering of a located clause: the discriminator is now a compiled object beside its certified zeros, not a citation.', '',
         '**Carried to:** b704 (W-ORD-FACES-PROBE-CURRENT); b705 (the detection law, the band witness, the I-6 ranking, W-ORD-P3-CONTOUR-SIGMA, '
         'W-ORD-E0-MET-CLASSK); b706 (W-ORD-PAPER-PARTNER-COPIES); b710 (W-ORD-STANDING-CLAUSES-BANK, reading 5); W-ORD-LV-CLOSURE-JOIN and '
         'W-ORD-KEYSTONE-HEADS on their triggers; the draft held at v5.', '',
         '**Next.** %s.' % K.NEXT, '',
         '*Nothing here is a statement that RH or GRH holds or locates any zero.*', '']
    return _title(), NL.join(e)


def _trail_text():
    S, J = jl('%s_scores.json' % ACT), jl('%s_act_root.json' % ACT)
    fj = jl('%s_findings.json' % ACT)
    n_ans = len(re.findall(r'^### PROMPT ', rdn('%s_author_answers.txt' % ACT), re.M))
    _r, _n, sh = seal_hashes()
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    f = _figs()
    rows_ = ['', TRAIL_HEAD(), '',
             '**(R313) ratified.** (1) b702 at its weight. (2) The corrigendum and the repairs. (3) The widening. (4) The Epstein step. (5) The pins. (6) The '
             'registrations. (7) The standing arms. (8) The format and the heads. (9) The branches. (10) The readfirst bank. (11) The draft held at v5. '
             '(12) The acts after.', '',
             '**Entered:** FINDINGS.md:%s (b702`s weight), :%s (the corrigendum), :%s (the entry); OPEN_TRAILS.md:%s-:%s (the four annotations and the '
             'four orders); this record.' % (c1_[0], f['corr_line'], fj.get('entry_line'), f['orders'][0], f['orders'][7]), '',
             '**Act root:** b703 `%s` (previous `%s`, b702`s; relay data/act_roots.txt), computed after the last bank it names, every one of them LF '
             'and committed and pushed at the commit it records (G-ROOT-BANKS-COMMITTED).' % (J.get('root'), J.get('previous')), '',
             '**Prompts to the author:** %d question%s in %d call%s before the root (relay data/b703_author_answers.txt); the root`s own prompt, its '
             'answer in the closing line.' % (n_ans, '' if n_ans == 1 else 's', len(_calls()), '' if len(_calls()) == 1 else 's'), '',
             '**The widening:** classK’ at SIDE-explicit-formula v0.36 = %s, one token at H2SignWide.lean :59, run 39700585515 DERIVES (relay '
             'data/b703_widening_grade.txt).' % f['v036'], '',
             '**The Epstein step:** Schema/EpsteinZQ.lean at v0.37 = %s, run 39703864050 DERIVES, the premises named (relay data/b703_epstein_grade.txt).' % f['v037'], '',
             '**The pins:** the closure join 1 dispatch, the interval vendoring 1 dispatch waiting on BINDER-PROVENANCE (relay data/b703_pins.txt).', '',
             '**The count:** 163 rows, %s off the line, %s in (1/2, 7/8] (relay data/b703_q0_band.txt).' % (f['off'], f['band']), '',
             '**The kernels:** SIDE-explicit-formula written on two branches and merged twice; no lean or lake on this host; two dispatches; widening-b701 '
             'and epstein-b703 standing.', '',
             '**The mirror:** the export made after this root in the b670 form, its name in the closing (relay data/b703_closing.txt).', '',
             '**The open orders:** `W-ORD-EXPLICIT-FORMULA-C1`; `W-ORD-EPSTEIN-COUNT-LEAN`; `W-ORD-FACES-PROBE-CURRENT`; `W-ORD-PAPER-PARTNER-COPIES`; '
             '`W-ORD-STANDING-CLAUSES-BANK`; `W-ORD-LV-CLOSURE-JOIN`; `W-ORD-KEYSTONE-HEADS`; `W-ORD-QUASI-RH-FIELD-WATCH`; `W-ORD-P3-CONTOUR-SIGMA`; '
             '`W-ORD-E0-MET-CLASSK`.', '',
             '**The sealed tools at the record:** %s.' % ', '.join('%s %s' % (t_, v) for t_, v in sh), '',
             '**Resolved by the seat, for the author’s strike:** %s.' % _for_author(), '',
             '**Defects** (relay data/b703_defects.txt): %s.' % ('; '.join(_defect_short(ACT)) or 'none'), '',
             '**' + ' · '.join('%s %s' % (k2, _sv(S, k2)) for k2 in NK + SK) + '.** (the scores bank; the readings that waited, at the close)', '',
             '**Next:** %s.' % K.NEXT, '']
    return NL.join(rows_)


def components(*a):
    S, fj, tj, J = (jl(n_) for n_ in ('%s_scores.json' % ACT, '%s_findings.json' % ACT, '%s_trail.json' % ACT, '%s_act_root.json' % ACT))
    if not fj.get('entry_line') or not tj.get('line'):
        sys.exit('### THE FINDINGS OR TRAIL BANK IS NOT WRITTEN -- RUN `findings` AND `trail` FIRST -- NOTHING WRITTEN')
    c1_ = _rl_lines('%s_record_lines.json' % ACT) + ['-']
    f = _figs()
    L = ['%s -- THE COMPONENTS, BANKED UNDER (R313).' % ACT, '',
         '### COMPONENT 0 : the citation check (data/b703_citation_check.txt), step zero (data/b703_ferry.txt, data/b703_readfirst.txt, data/b703_stepzero.txt, '
         'data/b703_tests_stepzero.txt, data/b703_rowgen_stepzero.txt, data/b703_branches.txt, data/b703_wsign7.txt, data/b703_registrations.txt) ; N1 %s' % S['N1'][0],
         '### COMPONENT 1 : b702`s weight FINDINGS :%s ; the corrigendum FINDINGS :%s ; the repairs (data/b703_quote_control.txt, data/b703_span_dry.txt, '
         'data/b703_tool_repairs.txt)' % (c1_[0], f['corr_line']),
         '### COMPONENT 2 : the widening v0.36 = %s (data/b703_widening_grade.txt) ; the glossary`s classK’ row ; the Epstein step v0.37 = %s '
         '(data/b703_epstein_grade.txt) ; the generator`s dry run (data/b703_correspondence_dry.txt) ; N2 %s ; N3 %s' % (f['v036'], f['v037'], S['N2'][0], S['N3'][0]),
         '### COMPONENT 3 : the pins (data/b703_pins.txt) ; the count (data/b703_q0_band.txt), %s in (1/2, 7/8] ; N4 %s' % (f['band'], S['N4'][0]),
         '### COMPONENT 4 : the four standing arms (data/b703_standing_figures.txt) ; data/b703_rules.txt ; the orders OPEN_TRAILS :%s-:%s' % (f['orders'][0], f['orders'][7]),
         '### COMPONENT 5 : the carry-time reading (data/b703_tool_repairs.txt), the dry-run steps (data/b703_reg_gate.txt), the seal '
         '(data/b703_seal_hashes.json), the suite in six parts, the per-part seconds (data/b703_arm_seconds.txt) ; S3 %s' % S['S3'][0],
         '### COMPONENT 6 : FINDINGS :%s ; the root %s ; OPEN_TRAILS :%s ; the mirror after the root ; N5 %s' % (
             fj.get('entry_line'), (J.get('root') or '')[:16], tj.get('line'), S['N5'][0])]
    put_txt('%s_components.txt' % ACT, L)
    print(NL.join(L[2:]))


def findings(*a):
    t, e = _finding_text()
    e = R.conv(e)
    dry = 'dry' in a
    cells_, fired = R.screens([('FINDINGS.md', t, e)], 'entry', dry)
    if dry:
        print(e)
        print('  cells %s' % cells_)
        return
    if not os.path.isfile(os.path.join(D, '%s_scores.json' % ACT)):
        sys.exit('### THE SCORES BANK IS NOT WRITTEN -- THE ENTRY READS IT (data/b686_rules.txt row (1)) -- NOTHING WRITTEN')
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = R._land_one(FIND, t, e, '%s_findings.json' % ACT, dict(title=t))
    j = jl('%s_findings.json' % ACT)
    j['entry_line'] = ln
    put_json('%s_findings.json' % ACT, j)
    print('  FINDINGS entry :%s' % ln)


def trail(*a):
    e = R.conv(_trail_text())
    dry = 'dry' in a
    cells_, fired = R.screens([('OPEN_TRAILS.md', TRAIL_HEAD(), e)], 'trail', dry)
    if dry:
        print(e[:9000])
        print('  cells %s' % cells_)
        return
    if cells_ or fired:
        sys.exit('### A SCREEN FIRED -- NOTHING WRITTEN')
    ln = R._land_one(OT, TRAIL_HEAD(), e, '%s_trail.json' % ACT, {})
    print('  OPEN_TRAILS record :%s' % ln)


def _trail_defects(text):
    m = re.search(r'^\*\*Defects\*\* \(relay data/%s_defects\.txt\): (.*)\.$' % ACT, text, re.M)
    return m.group(1) if m else None


def _trail_resolved(text):
    m = re.search(r'^\*\*Resolved by the seat, for the author’s strike:\*\* .*\((\d+)\) the (\w+) navigator (?:miss|misses)(?: \(\([a-z]\)(?:, \([a-z]\))*\))? '
                  r'and the seat’s (\w+) defects? as lettered\.$', text, re.M)
    return (m.group(2), m.group(3)) if m else None


def drycheck(*a):
    """(R267)(2), STANDING FROM b657: the FINDINGS entry and the trail record composed as the record tool composes them, converted by conv and run
    through the screens their landing runs, the needles the face names read in each; the trail's Defects line AND its Resolved line read against
    the defects bank. Writes no bank."""
    face = rd(a[0] if a and not a[0] == 'standin' else FACE)
    ok = True
    for which, (head, text) in (('ENTRY', _finding_text()), ('TRAIL', (TRAIL_HEAD(), _trail_text()))):
        t = R.conv(text)
        print('  %s (the screens):' % which)
        cells_, fired = R.screens([('FINDINGS.md' if which == 'ENTRY' else 'OPEN_TRAILS.md', head, t)], 'dry_' + which.lower(), True)
        nd = R._face_needles(face, which)
        miss = [n for n in nd if n not in t]
        clean = not cells_ and not fired and nd and not miss
        if which == 'TRAIL':
            got = _trail_defects(text)
            want = '; '.join(_defect_short(ACT)) or 'none'
            eq = got == want
            print('  THE TRAIL`S DEFECTS LINE: %s' % got)
            print('  THE DEFECTS BANK`S ROWS (relay data/%s_defects.txt, by the repaired reader): %s' % (ACT, want))
            print('  ### THE TRAIL`S DEFECTS LINE EQUAL TO THE DEFECTS BANK %s' % eq)
            rows, nav = _owners_now()
            gr = _trail_resolved(t)
            wr = (num_word(len(nav)), num_word(len(rows) - len(nav)))
            eqr = gr == wr
            print('  THE TRAIL`S RESOLVED LINE`S COUNTS: %s ; THE BANK`S OWNERS (navigator, seat): %s' % (gr, wr))
            print('  ### THE TRAIL`S RESOLVED LINE EQUAL TO THE DEFECTS BANK %s' % eqr)
            clean = clean and eq and eqr
        ok = ok and clean
        print('  %s : table cells %s ; screens %s ; the face`s needles %d, found %d%s ; %s' % (
            which, cells_ or 'NONE', 'FIRED' if fired else 'QUIET', len(nd), len(nd) - len(miss), (' -- missing %s' % miss) if miss else '',
            'CLEAN' if clean else 'NOT CLEAN'))
    print('  ### ### **DRY-RUN STEP : %s**' % ('CLEAN' if ok else 'NOT CLEAN'))
    if not ok:
        sys.exit(1)


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, defects=defects, defshort=defshort, c1=c1, span=span, mbank=mbank, cells=cells, wdiff=wdiff, orders=orders, figures=figures,
              quotectl=quotectl, repairs=repairs, dispatch=dispatch, runstatus=runstatus, runner=runner, grade=grade, depsctl=depsctl, guard=guard,
              commands=commands, reads=reads, rootbanks=rootbanks, root=root, root_arm=root_arm, table_final=table_final, kernels=kernels, standing=standing,
              armsecs=armsecs, desk=desk, gatebanks=gatebanks, mbuild=mbuild, mroot=mroot, mverify=mverify, scores=scores, components=components,
              findings=findings, trail=trail, drycheck=drycheck)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b703_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
