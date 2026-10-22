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
    "h2_sign'_imp_rh": (WF, NS, [], 'DERIVES', 'NONE (no binder; h2_sign` the antecedent, RH the consequent)'),
    'paperFT_finset_sum': (WF, NS, [('ι', 'Type*', 'the index type, data'), ('s', 'Finset ι', 'data'), ('f', 'ι → ℝ → ℂ', 'data'),
                                    ('hf', '∀ i ∈ s, Continuous (f i)', 'a hypothesis, not discharged in the theorem`s closure (discharged at its use, :131-:133)'),
                                    ('hs', '∀ i ∈ s, HasCompactSupport (f i)', 'a hypothesis, not discharged in the theorem`s closure'), ('z', 'ℂ', 'data')],
                           'INTERFACES', 'hf : ∀ i ∈ s, Continuous (f i) and hs : ∀ i ∈ s, HasCompactSupport (f i) -- on the author`s word at the '
                           'classK` prompt (2026-10-22T01:03Z): a binder that is a hypothesis not discharged in the theorem`s closure is its premise; the '
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
        L += ['== THE E0 DIVERGENCE, FOUR ROWS (the author`s word at the classK` prompt, 2026-10-22T01:03Z): each theorem`s statement whole with its',
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
        L += ['  THE ORDER FOR b705: MET (tools/e0_rule.py :308-:315) extended by ruling with classK and classKsum (and classK` and acDeriv, the',
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


ROUTES = dict(rowgen=rowgen, branches=branches, answers=answers, defects=defects, defshort=defshort, c1=c1, span=span, mbank=mbank, cells=cells, wdiff=wdiff,
              quotectl=quotectl, repairs=repairs, dispatch=dispatch, runstatus=runstatus, runner=runner, grade=grade, depsctl=depsctl)

if __name__ == '__main__':
    fn = ROUTES.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b703_record.py %s [dry]' % ' | '.join(sorted(ROUTES)))
        sys.exit(2)
    fn(*sys.argv[2:])
