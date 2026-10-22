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


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, defects=defects, defshort=defshort, c1=c1, span=span, mbank=mbank,
              quotectl=quotectl, repairs=repairs)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b703_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
