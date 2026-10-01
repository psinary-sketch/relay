# -*- coding: utf-8 -*-
"""b577_record.py -- THE ACT'S RECORD TOOL, UNDER (R187). ### ONE SUBCOMMAND PER BANK.

### ### b577: LANE THREE, ACT FIVE -- CP-7 ACT TWO. Subcommands write only `data/b577_*` unless the
### docstring names a ledger. Every bank is written through `put_txt` / `put_json` (encode first, then a temp file, then
### `os.replace`). This act makes no platform call.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
PRE_PP = '192077f'
MIRROR = 'outputs/DEPOSITED-v1.1.2/'
REG = os.path.join(PP, 'REGISTRY.md')
SPM = os.path.join(PP, 'SPIRAL_MAP.md')
ERR = os.path.join(PP, 'ERRATA.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def gb(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout if r.returncode == 0 else None


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def put_json(name, obj):
    b = (json.dumps(obj, indent=1, ensure_ascii=False) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))


def jl(name):
    return json.load(io.open(os.path.join(D, name), encoding='utf-8'))


def rd(name):
    p = os.path.join(D, name)
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def utc():
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def md5(b):
    return 'md5:' + hashlib.md5(b).hexdigest() if b is not None else None


DEFECTS = [
    '(a) THE PURPOSE BLOCK`S SUPERSEDES LINE WAS WRITTEN AS :6449 AND ITS HEADING LANDED AT :6448: the line count took split()`s '
    'empty element past the file`s final newline as a line, and the tool checked the landing after the append instead of before. '
    'The block was this act`s uncommitted append; the one number was corrected in it before any commit (the committed prefix read '
    'intact), and the tool`s arithmetic repaired. The bank is written from the block as it stands (purpose_bank).',
    '(b) THE FIRST PUSHES WERE REFUSED BY THE NETWORK, NOT THE GATE: "Could not resolve host: github.com" for both repositories at '
    '19:30Z; the table gate had passed and nothing was pushed (relay data/b577_push_out_attempt1.txt, _relay_push_out_attempt1.txt). '
    'ls-remote and a name lookup succeeded a minute later; both pushes were re-run and read back.',
]


def defects():
    put_txt('b577_defects.txt', ['### b577 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


def _Q():
    import b566_record as R6
    return R6.Q


RELAY = ROOT.replace('\\', '/')
CENSUS = 'phase2/method/THE_KEYSTONE_CENSUS.md'
READS = [
    ('relay b576`s drafts (Draft B and its fragments)', RELAY, 'HEAD', 'data/b576_purpose_drafts.txt', '### DRAFT B'),
    ('PLACE-papers README, the register sentence and (R145)(2)`s form', PP, PRE_PP, 'README.md', [106, 107, 113]),
    ('PLACE-papers FINDINGS, the head declarations and the earliest entry', PP, PRE_PP, 'FINDINGS.md', [7, 9, 434, 440, 450, 456]),
    ('PLACE-papers THE_KEYSTONE_CENSUS, the v0.2 table and :272', PP, PRE_PP, CENSUS, list(range(253, 273))),
    ('relay b567`s ferry, (R177)(3)', RELAY, 'HEAD', 'data/b567_ferry.txt', list(range(50, 62))),
    ('relay tools/addenda.py, the form', RELAY, 'HEAD', 'tools/addenda.py', list(range(1, 16))),
]


def reads():
    L = ['b577 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        if isinstance(sel, list):
            lines = sel
        else:
            a = [i for i, l in enumerate(sl, 1) if l.startswith(sel)][0]
            lines = list(range(a, a + 3))
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev).strip(), len(lines)))
        for n in lines:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    L.append('### relay data/b558_editions.json and data/b558_cp1b.json `per_document` are read whole by `order`.')
    put_txt('b577_reads.txt', L)


# ================================================================================ COMPONENT 1
def addendum_bank():
    """### The addendum line as written, its verdict by the form, the test, and the re-run at b576's push."""
    import addenda as ADD
    t = rd('b576_writelist_addendum.txt')
    v = ADD.writelist_addenda(t, ADD.paste_reader(D))
    import io as _io
    c4 = ADD.clause(_io.open(os.path.join(D, 'b577_ferry.txt'), encoding='utf-8').read(), 'R187', '4')
    rr = rd('b577_b576_rerun.txt')
    wt_head = g('D:/b577-rerun-b576', 'rev-parse', 'HEAD').strip()
    L = ['b577 -- COMPONENT 1: THE WRITE-LIST ADDENDUM AND THE ARM RE-RUN, (R187)(4)', '',
         '### relay data/b576_writelist_addendum.txt, as ruled:', '    ' + t.strip(), '',
         '### the form (relay tools/addenda.py, (R177)(3)(g)) on it:']
    L += ['    %s -> %s ; accepted %s' % (a['line'], a['why'], a['accepted']) for a in v]
    L += ['    (R186)(5)`s clause, read from relay data/b576_ferry.txt: "%s"' % (v[0]['clause'][:400] if v else ''),
          '    (R187)(4)`s clause, which names the file: "%s"' % c4[:300], '',
          '### the test (relay data/b577_test_rerun.txt): %s' % [l.strip() for l in rd('b577_test_rerun.txt').split(NL) if 'cases as wanted' in l],
          '### the re-run of b576`s suite at b576`s push -- worktree D:\\b577-rerun-b576 at %s (b576`s closing commit 2eae0499), the edited '
          'suite (relay cc4215d9) and the addendum bank placed in it:' % wt_head[:8]]
    L += ['    ' + l.strip() for l in rr.split(NL) if 'ARMS RUN' in l or 'VERDICT' in l or 'uncovered' in l or 'ADDENDUM' in l]
    acc = any(a['accepted'] for a in v)
    n = __import__('re').search(r'LIVE PASSING : (\d+)', rr)
    L += ['', '### ### **THE RULED LINE IS %s; THE RE-RUN READS %s OF 69.**' % ('ACCEPTED' if acc else 'REFUSED', n.group(1) if n else '?')]
    put_txt('b577_addendum.txt', L)
    put_json('b577_addendum.json', dict(accepted=acc, why=[a['why'] for a in v], rerun_passing=int(n.group(1)) if n else None,
                                        worktree_head=wt_head, c4_names=bool(c4 and 'mirror_prevbuild' in c4)))
    print(jl('b577_addendum.json'))


CORRECTIONS = [
    '(R153) names no observation document: CP-7’s working name is the author’s (relay `data/b543_ferry.txt` :63-:67).',
    'The three layers are `(R157)`(1)’s (relay `data/b547_ferry.txt` :8-:21), not `(R153)`’s.',
    'The register sentence is supportable with the clause named as `h2_sign` beside it (README :113, `(R145)`(2)).',
    '“A tracking document” is the project instructions’ phrase and no earlier ruling’s.',
]


def b576_lines():
    """### PLACE-papers OPEN_TRAILS (lines addressed to b576`s trail record) and FINDINGS (b576`s weight)."""
    Q = _Q()
    A = jl('b577_addendum.json')
    tr = Q.line_of(Q.OT, '### b576 — lane three, act four under (R186)')
    h = '*Appended 2026-10-01 by b577 to b576’s record (:%s), under the author’s ruling `(R187)`' % tr
    Q.guard_absent(Q.OT, h + '(4)')
    out = []
    out.append(Q.append_to(Q.OT, '\n%s(4) -- THE WRITE-LIST ADDENDUM:* WRITE-LIST ADDENDUM: tools/mirror_prevbuild.json, carried by (R186)(5). '
                                 'Read by the form of `(R177)`(3)(g) (relay `tools/addenda.py`): %s -- `(R186)`(5) names neither the file nor its '
                                 'stem; the clause that names it is `(R187)`(4). b576’s suite, wired to read the form (relay cc4215d9), re-run at '
                                 'b576’s push, reads %s of 69 (relay `data/b577_b576_rerun.txt`).\n'
                                 % (h, 'ACCEPTED' if A['accepted'] else 'REFUSED', A['rerun_passing'])))
    out.append(Q.append_to(Q.OT, '\n%s(4) -- THE MIRROR BUILDER’S WRITE LIST:* from b577 on, a face whose act builds the mirror names relay '
                                 '`tools/mirror_prevbuild.json` beside the zip in the builder’s (W) row; the builder rewrites it at every build.\n' % h))
    for i, c in enumerate(CORRECTIONS, 1):
        out.append(Q.append_to(Q.OT, '\n%s(1) -- THE NAVIGATOR’S CORRECTION %d, ENTERED AS THE NAVIGATOR’S:* %s\n' % (h, i, c)))
    e = Q.line_of(Q.FIND, '## CP-7, act one: the observation document’s purpose statement drafted')
    hw = '*Appended 2026-10-01 by b577 to b576’s entry (:%s), under `(R187)`(1) -- b576 AT ITS WEIGHT:*' % e
    Q.guard_absent(Q.FIND, hw)
    out.append(Q.append_to(Q.FIND, '\n%s the lv record 21539068 carries E-2026-09-25-3’s two replacement sentences as one appended paragraph, '
                                    'fetch-back MATCH, E-2026-10-01-2; SPIRAL_MAP :44 beneath :43 states what E-2026-07-13-1 says, '
                                    'E-2026-10-01-3 corpus-facing; the mirror mirror-refresh-2026-10-01.zip, 44 files with both pages, MANIFEST '
                                    'md5 5c3d6afd23e377efcda7357f8c448d37, source 192077f, CLEAN on three clauses, now the project’s currency '
                                    'authority; the seat’s memory rewritten (105 to 91 entries). The suite read 68 of 69, the one arm failing '
                                    'correctly on tools/mirror_prevbuild.json.\n' % hw))
    text = Q.rd(Q.OT).split(NL)
    lines = [i for i, l in enumerate(text, 1) if l.startswith(h)]
    put_json('b577_b576_lines.json', dict(trail=tr, ot_lines=lines, weight=Q.line_of(Q.FIND, hw), appends=out))
    print(jl('b577_b576_lines.json'))


# ================================================================================ COMPONENT 2
FRAGS = [
    ('Its object: the kernel\'s declarations at pins, the bench\'s banked numbers, the field at its pins.', 'Draft B, unchanged'),
    ('Its layer, the observational: relay banks, the four ledgers, the two generated pages, the terminal table, the censuses — '
     'append-only, dated, the record of what was done and measured.', 'Draft B, "the two generated pages" added by (R187)(3)'),
    ('Its readers: the editions and the monograph, which cite it and do not restate it, written from the observational layer at '
     'checkpoints.', 'Draft B, unchanged'),
    ('It is not a claim: RH reduced to a single located clause, the clause named as h2_sign, reduction machine-verified; neither RH '
     'nor h2_sign is proved; it is written without narrative; it is not a tracking document: an audit of a conclusion\'s standing is '
     'not its documentation.', 'Draft B, the claim clause completed by (R187)(3) in README :113`s form'),
]


def _text():
    return ' '.join(f for f, _ in FRAGS)


def _draft_b():
    t = rd('b576_purpose_drafts.txt').split(NL)
    i = [k for k, l in enumerate(t) if l.startswith('### DRAFT B --')][0]
    return t[i + 2].strip()


def purpose():
    """### PLACE-papers FINDINGS.md: the purpose statement appended at the end as its own dated block, with the SUPERSEDES line."""
    Q = _Q()
    text = _text()
    B = _draft_b()
    want = B.replace('relay banks, the four ledgers, the terminal table', 'relay banks, the four ledgers, the two generated pages, the terminal table') \
            .replace('It is not a claim: neither is proved;', 'It is not a claim: RH reduced to a single located clause, the clause named as h2_sign, '
                     'reduction machine-verified; neither RH nor h2_sign is proved;')
    if text != want:
        sys.exit('### THE AMENDED TEXT IS NOT DRAFT B WITH THE TWO RULED AMENDMENTS -- NOTHING WRITTEN.\n%s\n%s' % (text, want))
    head = '## THE PURPOSE OF THIS RECORD — written 2026-10-01 at b577 under the author’s ruling `(R187)`(2)–(3)'
    Q.guard_absent(Q.FIND, head)
    # ### the file ends with a newline, so split() carries one empty element past the last line (defect (a)): the last line is
    # ### n_before - 1, the block's leading blank lands on n_before, and its heading on n_before + 1 -- written below as n_before + 2
    # ### with n_before counted one short of the elements.
    n_before = len(Q.rd(Q.FIND).split(NL)) - 1
    block = ['', head, '',
             '> ' + text, '',
             '**The observation document** (`(R187)`(2)) is this file with the two generated pages: FINDINGS, the record of the acts -- what '
             'was done and measured, grown by append, dated -- and THE_CLAUSE_AND_ITS_COMPILED_FACES.md with '
             'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md, the record of the kernel -- what is compiled, at which pin, with one open node each. '
             'No new file is made.', '',
             'SUPERSEDES FINDINGS :7 for the purpose statement: present, at :%d' % (n_before + 2), '',
             '*The block is appended at the end, the head placement of `(R187)`(2) struck by the author before b577’s seal; FINDINGS :7 '
             '(“NO PURPOSE STATEMENT -- the absence is the finding”) and :9 (the PURPOSE line) stand as written. Draft B of relay '
             '`data/b576_purpose_drafts.txt`, amended at the two places `(R187)`(3) names and nowhere else; its sources are printed at relay '
             '`data/b577_purpose.txt`.*', '']
    r = Q.append_to(Q.FIND, NL.join(block))
    hl = Q.line_of(Q.FIND, head)
    if hl != n_before + 2:
        sys.exit('### THE HEADING LANDED AT :%s, NOT :%s -- THE SUPERSEDES LINE IS WRONG' % (hl, n_before + 2))
    open(os.path.join(D, 'b577_purpose_block.txt.tmp'), 'wb').write((NL.join(block) + NL).encode('utf-8'))
    os.replace(os.path.join(D, 'b577_purpose_block.txt.tmp'), os.path.join(D, 'b577_purpose_block.txt'))
    k = len(block)
    L = ['b577 -- COMPONENT 2: THE PURPOSE STATEMENT, (R187)(2)-(3), APPENDED AT FINDINGS` END', '',
         '### the text, each sentence with its source:']
    L += ['    %s  [%s]' % (f, s) for f, s in FRAGS]
    L += ['', '### Draft B as banked at b576 (relay data/b576_purpose_drafts.txt):', '    ' + B,
          '### the amended text equals Draft B with exactly the two ruled amendments: %s' % (text == want),
          '### README :113 (the clause named as h2_sign; "Not supportable: RH proved; h2_sign proved"): %s'
          % g(PP, 'show', PRE_PP + ':README.md').split(NL)[112][:260],
          '', '### the block at FINDINGS :%d-:%d ; its heading :%d ; the SUPERSEDES line names :%d' % (n_before + 1, n_before + k, hl, n_before + 2),
          '### the head placement, struck: inserted above :456 the block (%d lines) would have moved every later line by %d -- about '
          '115 line citations of FINDINGS in the corpus and 874 in relay.' % (k, k),
          '### the append: %s' % r]
    put_txt('b577_purpose.txt', L)
    put_json('b577_purpose.json', dict(text=text, heading_line=hl, block_lines=k, first=n_before + 1, k=k, append=r))
    print(jl('b577_purpose.json')['heading_line'], k)


def purpose_bank():
    """### Component 2`s bank, read from the block as it stands in FINDINGS (defect (a))."""
    Q = _Q()
    t = Q.rd(Q.FIND).split(NL)
    head = '## THE PURPOSE OF THIS RECORD — written 2026-10-01 at b577 under the author’s ruling `(R187)`(2)–(3)'
    hl = [i for i, l in enumerate(t, 1) if l == head][0]
    sup = [i for i, l in enumerate(t, 1) if l.startswith('SUPERSEDES FINDINGS :7 for the purpose statement: present, at :')][0]
    end = len(t) if t[-1] != '' else len(t) - 1
    block = t[hl - 2:end]
    open(os.path.join(D, 'b577_purpose_block.txt.tmp'), 'wb').write((NL.join(block) + NL).encode('utf-8'))
    os.replace(os.path.join(D, 'b577_purpose_block.txt.tmp'), os.path.join(D, 'b577_purpose_block.txt'))
    text = _text()
    B = _draft_b()
    want = B.replace('relay banks, the four ledgers, the terminal table', 'relay banks, the four ledgers, the two generated pages, the terminal table') \
            .replace('It is not a claim: neither is proved;', 'It is not a claim: RH reduced to a single located clause, the clause named as h2_sign, '
                     'reduction machine-verified; neither RH nor h2_sign is proved;')
    k = len(block)
    L = ['b577 -- COMPONENT 2: THE PURPOSE STATEMENT, (R187)(2)-(3), APPENDED AT FINDINGS` END', '',
         '### the text, each sentence with its source:']
    L += ['    %s  [%s]' % (f, s_) for f, s_ in FRAGS]
    L += ['', '### Draft B as banked at b576 (relay data/b576_purpose_drafts.txt):', '    ' + B,
          '### the amended text equals Draft B with exactly the two ruled amendments: %s ; the text in the block: %s' % (text == want, ('> ' + text) in block),
          '### README :113 (the clause named as h2_sign; "Not supportable: RH proved; h2_sign proved"): %s'
          % g(PP, 'show', PRE_PP + ':README.md').split(NL)[112][:260],
          '', '### the block at FINDINGS :%d-:%d ; its heading :%d ; the SUPERSEDES line at :%d names :%s' % (hl - 1, end, hl, sup, t[sup - 1].split(':')[-1]),
          '### the head placement, struck by the author: inserted above :456 the block (%d lines) would have moved every later line by '
          '%d -- about 115 line citations of FINDINGS in the corpus and 874 in relay.' % (k, k)]
    put_txt('b577_purpose.txt', L)
    put_json('b577_purpose.json', dict(text=text, heading_line=hl, supersedes_line=sup, names=int(t[sup - 1].split(':')[-1]),
                                       block_lines=k, first=hl - 1, last=end, amended_ok=(text == want)))
    print(jl('b577_purpose.json')['heading_line'], jl('b577_purpose.json')['names'], k)


# ================================================================================ COMPONENT 3
CENSUS_ORDER = ['PATHS_TO_THE_CRITICAL_LINE', 'SIMPLICITY_OF_RIEMANN_ZEROS', 'THE_UNCONDITIONAL_SURROUND', 'GRH_CASCADE', 'R_CURVE_CRITERION',
                'INDEX_ARITY_AT_THE_CRITICAL_LINE', 'FOUNDATIONS_OF_THE_SIDE_PROGRAMME', 'TECHNE_TOOLKIT', 'THE_RESIDUE_OF_RH',
                'ADDITIVE_MULTIPLICATIVE_CONSPIRACY', 'SILENCE_STAGES_DEALIGNMENT', 'EXHAUSTIVENESS_LICENSE', 'INVARIANCE_BARRIERS',
                'REPARAMETERIZATION_BARRIERS_v0_1', 'E_DIFFICULTY_THEOREM', 'ENUMERA']
OUTSIDE = ['A_Place_to_Stand', 'BALANCE_AND_POSITIVITY', 'FACES_OF_H2_AT_FINITE_INSTANCE']


def order():
    """### The keystones with a work-list, by MOVED-IN-MEANING rows descending, ties by census position; the three outside listed."""
    E = jl('b558_editions.json')
    PD = jl('b558_cp1b.json')['per_document']
    cen = g(PP, 'show', PRE_PP + ':' + CENSUS).split(NL)
    pos = {}
    for i, l in enumerate(cen[252:272], 253):
        m = re.match(r'^\| `([A-Za-z0-9_]+)` \|', l)
        if m:
            pos[m.group(1)] = (len(pos) + 1, i)
    rows = []
    for key, v in E['lists'].items():
        name = v['file'].split('/')[-1][:-4]
        c = PD.get(key, {})
        rows.append(dict(key=key, name=name, moved=v['rows'], lines=v['lines'], stands=c.get('STANDS'), credit=c.get('CREDIT'),
                         moved_doc=c.get('MOVED-IN-MEANING'), census=pos.get(name)))
    kept = sorted([r for r in rows if r['census']], key=lambda r: (-r['moved'], r['census'][0]))
    out = [r for r in rows if not r['census']]
    L = ['b577 -- COMPONENT 3: THE EDITION ORDER, (R187)(5) -- PRINTED FOR THE AUTHOR TO STRIKE OR REORDER AT THE CLOSING', '',
         '### MOVED-IN-MEANING = the work-list`s rows (relay data/b558_editions.json `rows`, one per sentence x terminal), its distinct',
         '### lines beside it; STANDS and CREDIT from b558_cp1b.json `per_document`; census position from THE_KEYSTONE_CENSUS :255-:270.', '',
         '    %-3s %-36s %6s %6s %7s %7s %s' % ('#', 'keystone', 'MOVED', 'lines', 'STANDS', 'CREDIT', 'census position (line)')]
    for i, r in enumerate(kept, 1):
        L.append('    %-3d %-36s %6d %6d %7s %7s %s' % (i, r['name'], r['moved'], r['lines'], r['stands'], r['credit'],
                                                       '%d (:%d)' % r['census']))
    L += ['', '### OUTSIDE THE KEYSTONE CLASS (THE_KEYSTONE_CENSUS :272), listed separately for the author to place:']
    for r in sorted(out, key=lambda r: -r['moved']):
        L.append('        %-36s %6d %6d %7s %7s %s' % (r['name'], r['moved'], r['lines'], r['stands'], r['credit'],
                                                     '-- the monograph: its edition is CP-8`s v6, (R153)(4)' if r['name'] == 'A_Place_to_Stand' else ''))
    nowl = [n for n in CENSUS_ORDER if n not in [r['name'] for r in rows]]
    L += ['', '### keystones of the census with no work-list (b558 `none`): %s' % nowl,
          '### THE_IDENTITY_CHAIN: no work-list (b558 `none`: IDC).',
          '', '### ### **THE HEAD OF THE ORDER: %s (%d rows). CP-7 ACT THREE, b578, IS ITS EDITION ON THE AUTHOR`S RULING OF THIS ORDER.**'
          % (kept[0]['name'], kept[0]['moved'])]
    put_txt('b577_edition_order.txt', L)
    put_json('b577_edition_order.json', dict(order=[r['name'] for r in kept], rows=kept, outside=out, no_worklist=nowl, head=kept[0]['name']))
    print([(r['name'], r['moved']) for r in kept][:5])


def form():
    """### PLACE-papers OPEN_TRAILS: the edition form entered at lane three (:11417) as the standing form for CP-7."""
    Q = _Q()
    lane = Q.line_of(Q.OT, "> LANE THREE — THE CLARIFIED LAYER, after lane two's (a) and (b) at least")
    h = '*Appended 2026-10-01 by b577, under the author’s ruling `(R187)`(5)–(6), to the critical path’s lane three (:%s) -- THE FORM OF AN EDITION, STANDING FOR CP-7:*' % lane
    Q.guard_absent(Q.OT, h)
    r = Q.append_to(Q.OT, '\n%s one keystone per act, in the order printed at relay `data/b577_edition_order.txt` as the author rules it. The '
                          'edition is the keystone’s next version written beside the current one, the current unedited; written from its tier '
                          'block and its CP-1b work-list, the page its objects sit on as its spine; STANDS sentences carried unchanged; '
                          'MOVED-IN-MEANING sentences rewritten to say what the compiled fact says, citing the declaration by name and pin as '
                          'the page prints it; CREDIT lines inserted where the work-list places them; a marked sentence the compiled facts do '
                          'not support removed and its removal recorded in back matter, not reworded; Placement and Correspondence in back '
                          'matter; no blank Status cell; the title naming objects and conditions; 0 live banned stems; nothing beyond the '
                          'ceiling; the edition diffed sentence by sentence against the work-list and the diff banked. It does not deposit '
                          'and does not move into a phase repository; promotion is CP-8’s. Every edition act scores H28a, H28b and H28c as '
                          '`(R187)`(6) fixes them (relay `data/b577_ferry.txt`).\n' % h)
    put_json('b577_form.json', dict(line=Q.line_of(Q.OT, h), lane=lane, append=r))
    print(jl('b577_form.json'))


# ================================================================================ THE SCORING AND THE RECORD
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'S1', 'S2', 'S3')
EF = 'D:/SIDE-explicit-formula'
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c'}


def scores():
    A, O, P = jl('b577_addendum.json'), jl('b577_edition_order.json'), jl('b577_purpose.json')
    ch = sorted(set(x for x in g(PP, 'diff', '--name-only', PRE_PP).split(NL) if x.strip()))
    kmain = g(EF, 'rev-parse', 'main').strip()
    heads_ok = all(g('D:/' + r, 'rev-parse', 'main').strip().startswith(h) for r, h in PRE_HEADS.items())
    edited_tools = [x for x in g(ROOT, 'log', '--name-only', '--pretty=format:', '9cac0572..HEAD', '--', 'tools/b576_checks.py').split(NL) if x.strip()]
    S = dict(
        N1=('HELD' if A['accepted'] and A['rerun_passing'] == 69 else 'REFUTED',
            'the form refuses the ruled line -- %s: (R186)(5) names neither tools/mirror_prevbuild.json nor its stem; (R187)(4) names it. '
            'b576`s suite, wired to read the form, re-run at b576`s push (worktree at 2eae0499), reads %d of 69 (relay '
            'data/b577_b576_rerun.txt)' % (A['why'][0], A['rerun_passing'])),
        N2=('HELD' if O['head'] in ('PATHS_TO_THE_CRITICAL_LINE', 'THE_RESIDUE_OF_RH', 'THE_IDENTITY_CHAIN') else 'REFUTED',
            'the head of the keystone order is %s at %d rows; the monograph, outside the keystone class, carries 31; THE_IDENTITY_CHAIN '
            'has no work-list (relay data/b577_edition_order.txt)' % (O['head'], O['rows'][0]['moved'])),
        N3=('NOT SCORABLE', 'no edition is begun at this act: (R187)(5) and (7) govern, by the author`s answer before the seal; '
                            'H28a-H28c are scored at b578'),
        N4=('HELD' if (set(ch) <= {'FINDINGS.md', 'OPEN_TRAILS.md'} and kmain == V015 and heads_ok and not edited_tools) else 'REFUTED',
            'nothing deposits; no kernel touched; no keystone and no edition file written; PLACE-papers changed at %s only, the purpose '
            'block appended at FINDINGS` end (the head placement struck by the author) -- but b576`s suite was edited (relay cc4215d9) '
            'and the addendum bank and a worktree were made for the re-run (1)(4) orders, which the expectation`s list does not name' % ch),
        S1=('HELD' if not A['accepted'] and A['rerun_passing'] == 68 else 'REFUTED', 'the ruled line REFUSED; the re-run reads 68 of 69'),
        S2=('HELD' if O['head'] == 'PATHS_TO_THE_CRITICAL_LINE' and O['rows'][0]['moved'] == 29 else 'REFUTED',
            'PATHS heads at 29; the monograph, outside the class, would head at 31'),
        S3=('HELD', '(N3) NOT SCORABLE, no edition begun; (N4) refuted in letter by the suite edit, the addendum bank and the worktree'),
        counts=dict(order=O['order'], head=O['head'], purpose_line=P['heading_line'], k=P['k'] if 'k' in P else P['block_lines'],
                    pp_changed=ch),
    )
    put_json('b577_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s' % (k, S[k][0]))


TITLE = ('## CP-7, act two: the purpose statement appended to FINDINGS; the observation document identified with FINDINGS and the two '
         'pages; the write-list addendum refused by its form; the edition order and the edition form')


def records_pp():
    Q = _Q()
    S = jl('b577_scores.json')
    P, O, A, F, B = jl('b577_purpose.json'), jl('b577_edition_order.json'), jl('b577_addendum.json'), jl('b577_form.json'), jl('b577_b576_lines.json')
    Q.guard_absent(Q.FIND, TITLE)
    e = ['', TITLE, '',
         '*Filed at b577 on the author’s ruling `(R187)`. Banks: relay `data/b577_purpose.txt`, `data/b577_addendum.txt`, '
         '`data/b577_b576_rerun.txt`, `data/b577_edition_order.txt`. Nothing deposits.*', '',
         '**The purpose statement** (`(R187)`(2)–(3)), at :%d: Draft B amended at the two ruled places and nowhere else, appended as its '
         'own dated block; it names the observation document as this file with the two generated pages, and supersedes :7 for the '
         'purpose statement. The head placement was struck by the author before the seal: inserted above the earliest entry (:456) the '
         'block’s %d lines would have moved every later line, against about 115 line citations of FINDINGS in the corpus and 874 in '
         'relay. :7 and :9 stand as written.' % (P['heading_line'], P['block_lines']), '',
         '**The write-list addendum** (`(R187)`(4)), written as ruled at b576’s record: the form of `(R177)`(3)(g) refuses it -- '
         '`(R186)`(5) does not name tools/mirror_prevbuild.json; `(R187)`(4) does. b576’s suite, wired to read the form, re-run at '
         'b576’s push, reads %d of 69. The mirror builder’s write list names the file from b577 on.' % A['rerun_passing'], '',
         '**The edition order** (`(R187)`(5)), by MOVED-IN-MEANING rows among the census’s keystones that carry a work-list: %s. The '
         'monograph (31), BALANCE_AND_POSITIVITY (14) and FACES_OF_H2 (1) sit outside the keystone class (THE_KEYSTONE_CENSUS :272) and '
         'are listed for the author to place. The form of an edition is entered on the trails (OPEN_TRAILS :%d).'
         % (', '.join('%s %d' % (r['name'], r['moved']) for r in O['rows'][:5]) + ', …', F['line']), '',
         '**The edition** was not begun: `(R187)`(5) and (7) place it in the act after this one, against the navigator’s Component 4, '
         'which is withdrawn by the author’s answer before the seal.', '',
         '**The scores.** (N1) %s, (N2) %s, (N3) %s, (N4) %s; the seat’s (S1) %s, (S2) %s, (S3) %s.' % tuple(S[k][0] for k in SCORE_KEYS), '',
         '**Next.** Per `(R187)`(7): CP-7 act three, b578 -- the edition of PATHS_TO_THE_CRITICAL_LINE on the author’s ruling of the order.', '',
         '*Nothing deposits; no kernel touched; no keystone, edition, README, REGISTRY or page byte written; nothing here is a statement '
         'about RH, GRH or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    head = ('### b577 — lane three, act five under (R187): CP-7 act two -- the purpose statement appended to FINDINGS; the write-list '
            'addendum; the edition order and form')
    Q.guard_absent(Q.OT, head)
    rows = ['', head, '',
            '**(R187) ratified.** (1) b576 at its weight. (2) The observation document identified with FINDINGS and the two pages. (3) '
            'The purpose statement, Draft B amended. (4) The write-list addendum. (5) The editions, the order and the form. (6) The '
            'hypotheses. (7) The act after.', '',
            '**Entered:** FINDINGS.md:%d (b576’s weight), :%d (the purpose statement), :%d (the entry); OPEN_TRAILS.md:%s (b576’s record: '
            'the addendum, the builder’s write list, the four corrections), :%d (the edition form), this record. Relay: b576’s suite '
            'reads the addendum form (cc4215d9); the re-run in the worktree D:\\b577-rerun-b576, kept.'
            % (B['weight'], P['heading_line'], Q.line_of(Q.FIND, TITLE), ', :'.join(str(x) for x in B['ot_lines']), F['line']), '',
            '**Struck and withdrawn, recorded:** the head placement of `(R187)`(2), struck by the author before the seal -- inserted above '
            ':456 the block (%d lines) would have moved every later line by %d; the navigator’s Component 4 (the edition begun at b577), '
            'withdrawn by the author’s answer -- `(R187)`(5) and (7) put the edition in the act after this one, and they govern.'
            % (P['block_lines'], P['block_lines']), '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s.' % tuple(S[k][0] for k in SCORE_KEYS), '',
            '**For the author:** the addendum as ruled is refused by its own form; the clause that names the file is `(R187)`(4). The '
            'order’s head is PATHS_TO_THE_CRITICAL_LINE; the three outside the keystone class await placement.', '',
            '**Next:** per `(R187)`(7), CP-7 act three, b578 -- the edition of PATHS_TO_THE_CRITICAL_LINE by the form, H28a-H28c scored, on '
            'the author’s ruling of the order at this closing.', '',
            '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; the pages untouched; row U1 unedited; the four lists stay '
            'OPEN; nothing here is a statement about RH, GRH or any zero.', '']
    r2 = Q.append_to(Q.OT, NL.join(rows))
    put_json('b577_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE), title=TITLE, append=r))
    put_json('b577_trail.json', dict(line=Q.line_of(Q.OT, head), head=head, append=r2))
    print(jl('b577_findings.json')['entry_line'], jl('b577_trail.json')['line'])


def desk():
    S = jl('b577_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4')
    L = ['=' * 104, 'b577 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FOUR.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S THREE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in ('S1', 'S2', 'S3')]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d ; NOT SCORABLE %d.** ### ### **THE SEAT`S : HELD %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK), sum(S[k][0] == 'NOT SCORABLE' for k in NK),
        sum(S[k][0] == 'HELD' for k in ('S1', 'S2', 'S3'))), '']
    L += rd('b577_defects.txt').rstrip(NL).split(NL)
    put_txt('b577_desk_notes.txt', L)


def components():
    S = jl('b577_scores.json')
    fj, tj, B, P, A, F = (jl('b577_findings.json'), jl('b577_trail.json'), jl('b577_b576_lines.json'), jl('b577_purpose.json'),
                          jl('b577_addendum.json'), jl('b577_form.json'))
    L = ['b577 -- THE COMPONENTS, BANKED UNDER (R187).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b576`s closing push-out relay 9cac0572 ; push-b576* branches deleted by '
         'name (data/b577_branches.txt) ; the kept branches untouched',
         '### COMPONENT 1 : the addendum as ruled, REFUSED by its form ; b576`s suite reads the form (cc4215d9, test 5 of 5) ; the re-run '
         'at b576`s push %d of 69 ; OPEN_TRAILS %s ; b576`s weight FINDINGS :%d ; N1 %s' % (A['rerun_passing'], B['ot_lines'], B['weight'], S['N1'][0]),
         '### COMPONENT 2 : the purpose statement at FINDINGS :%d (appended; the SUPERSEDES line names :%d) ; banned-stem scan CLEAN'
         % (P['heading_line'], P['names']),
         '### COMPONENT 3 : the order (data/b577_edition_order.txt), head %s ; the form OPEN_TRAILS :%d ; N2 %s' % (S['counts']['head'], F['line'], S['N2'][0]),
         '### COMPONENT 4 : WITHDRAWN -- the edition is b578 ((R187)(5), (7)) ; N3 %s' % S['N3'][0],
         '### COMPONENT 5 : FINDINGS :%d ; OPEN_TRAILS :%d (the record) ; next: the edition of PATHS_TO_THE_CRITICAL_LINE ; N4 %s'
         % (fj['entry_line'], tj['line'], S['N4'][0])]
    put_txt('b577_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b577_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
