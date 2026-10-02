# -*- coding: utf-8 -*-
"""b591_record.py -- THE ACT'S RECORD TOOL, UNDER (R201). ### ONE SUBCOMMAND PER BANK.

### ### b591: LANE THREE, ACT EIGHTEEN -- THE LOCATED-CLAUSE METHOD DOCUMENT WRITTEN FROM THE LEDGERS AS A NEW DOCUMENT ON
### THE AUTHOR'S ASK; THE WITNESS RATIO ENTERED AT DETECTION-REGION; THE E0 RULE'S EXISTENTIAL-BINDER CLAUSE.
### Subcommands write only `data/b591_*` unless the docstring names another file. Every bank is written through `put_txt` /
### `put_json` (encode, temp file, `os.replace`). No platform call; the one network read is `gh api` on GitHub's commit
### endpoint for the Mathlib pin (H32b), a read. The templates are b590_record.py and b589_record.py.
### ### **THIS TOOL CARRIES NO BODY SENTENCE OF THE DOCUMENT.** It reads the document from the TECHNE-Core clone (or the
### seat's scratchpad draft) at run time; what reaches relay is citations, counts, positions and digests.
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
sys.path.insert(0, os.path.join(ROOT, 'tools', 'rowgen'))

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
TE = 'D:/MY-DOwnloads/TECHNE-Core'
GSR = 'D:/SIDE-global-section'
EFK = 'D:/SIDE-explicit-formula'
MATHLIB = 'D:/SIDE-explicit-formula/.lake/packages/mathlib'
PRE_PP = '40746b4'
PRE_RELAY = 'd497de0c'
PRE_TE = '29208f6'
MIRROR_PIN = '192077f'
ML_PIN = 'de5ce8a9'
V016 = 'c404e727d7f7121b180318cca32eeb115452ed1b'
DOC_REL = 'modules/2026-08/THE_LOCATED_CLAUSE_METHOD.md'
DOC = TE + '/' + DOC_REL
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/98c89dfb-f1a9-474b-afa3-5704358766ef/scratchpad'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
RESIDUE = 'phase1.5/proofs/THE_RESIDUE_OF_RH.md'
CANON = 'phase1.5/method/THE_METHOD_CANON.md'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def grc(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True).returncode


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
    import time
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _Q():
    import b566_record as R6
    return R6.Q


DEFECTS = [
    '(a) THE FACE DECLARED G-CHAIN-PAGE AND G-CHAIN-PAGE-CHI (THE SHARED ARM, BYTE FOR BYTE AGAINST THE COMMITTED PAGES) AND (S1)`S '
    '"BOTH PAGES RE-EMIT BYTE FOR BYTE" WITHOUT FIRST RUNNING THE ARM AT HEAD. Run after the clause, neither page re-emits: the ζ '
    'page`s regeneration adds eleven Placement rows -- the b578-b589 editions, each a keystone naming a node, which the generator '
    'lists and the page (b568) predates -- and the χ page`s banked probe output (b573) cannot resolve the three Schema declarations '
    'the record gained at b590 (exit 6). Under the rule before the clause and under it the re-emits are equal (data/b591_e0_regrade.txt), '
    'so the clause moves no page byte; the failures are the corpus`s drift since b574, read here and not repaired. The arms stand as '
    'sealed and fail; no page is edited.',
    '(b) H32b`S FIRST SCORING READ "EXISTS" AS "EXISTS AND IS NON-BLANK", A CONDITION NEITHER (R201)(5) NOR THE FACE CARRIES, AND '
    'REFUTED ON ζ PAGE :4 -- the blank line between the page`s head (:3) and its first node (:5), inside the document`s range '
    'citation :3-:29. The score is the ruling`s letter ("every page line it cites exists at the mirror`s pin"); the stricter figure '
    'is printed beside it in data/b591_h32.txt for the author to rule on. The document is committed and is not edited.',
]


def defects():
    put_txt('b591_defects.txt', ['### b591 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


# ================================================================================ READING (1): THE READS
RELAY = ROOT.replace('\\', '/')
CANON_HEADS = [1, 15, 24, 65, 73, 84, 90, 94, 108, 112, 119, 123, 134, 143, 160, 172, 189, 218, 231, 251, 255, 259, 263, 276, 297]
F_LINES = [4595, 4650, 4730, 4752, 6012, 6032, 6042, 6066, 6088, 6098, 6118, 6138, 6148, 6170, 6194, 6220, 6246, 6266, 6288, 6308,
           6330, 6356, 6374, 6376, 6404, 6740]
READS = [
    ('TECHNE-Core the b257 drafts` INDEX head', TE, 'HEAD', 'modules/2026-08/INDEX.md', list(range(1, 10))),
    ('relay b257`s sweep bank, the drafts written', RELAY, 'HEAD', 'data/b257_methodology_sweep.txt', list(range(82, 96))),
    ('PLACE-papers THE_METHOD_CANON`s section headings', PP, PRE_PP, CANON, CANON_HEADS),
    ('PLACE-papers the ζ page at the mirror`s pin, every node line', PP, MIRROR_PIN, PAGE, list(range(1, 32))),
    ('PLACE-papers the χ page at the mirror`s pin, every node line', PP, MIRROR_PIN, DIR_PAGE, list(range(1, 27))),
    ('PLACE-papers README, the ceiling sentences', PP, PRE_PP, 'README.md', [107, 121, 125]),
    ('PLACE-papers FINDINGS, the worked instance`s entries', PP, PRE_PP, 'FINDINGS.md', F_LINES),
    ('PLACE-papers OPEN_TRAILS, W-ORD-DETECTION-REGION', PP, PRE_PP, 'OPEN_TRAILS.md',
     [11151, 11332, 11336, 11337, 11415, 11423, 11491] + list(range(11512, 11522))),
    ('PLACE-papers THE_RESIDUE_OF_RH, the chiasmus and §7', PP, PRE_PP, RESIDUE, [67] + list(range(71, 82))),
    ('PLACE-papers SPIRAL_MAP, the translation table', PP, PRE_PP, 'SPIRAL_MAP.md', [422, 434, 435]),
    ('relay the shared E0 rule before the clause', RELAY, PRE_RELAY, 'tools/e0_rule.py', list(range(27, 50)) + list(range(102, 114))),
    ('relay b590`s witness against the bench', RELAY, 'HEAD', 'data/b590_witness_vs_bench.txt', [5, 7, 8, 9, 12, 13, 15, 21, 22]),
    ('relay the stem scanner`s stems', RELAY, 'HEAD', 'tools/banned_terms.py', [64]),
    ('relay b590`s closing push-out, its head', RELAY, 'HEAD', 'data/b590_closing_push_out.txt', list(range(1, 4))),
]


def reads():
    L = ['b591 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    L.append('### the b257 drafts` location: %s/modules/2026-08/ @ %s -- %s' % (
        TE, g(TE, 'rev-parse', '--short=8', 'HEAD').strip(), ' '.join(x.split('/')[-1] for x in g(TE, 'ls-tree', '--name-only', 'HEAD', 'modules/2026-08/').split(NL) if x.strip())))
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev + '^{}').strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    put_txt('b591_reads.txt', L)


# ================================================================================ COMPONENT 1: THE RECORD LINES
B590_ENTRY = '## The Epstein negative control: the detector theorem over a configuration with an off-line zero'
RESCOPE = '### `W-ORD-DETECTION-REGION` (the entry at :11151, the price corrected at :11491) -- RE-SCOPED ON THE MEASURED OBSTACLE'


def weight_line():
    """### PLACE-papers FINDINGS: b590's weight, one appended line addressed to b590's entry, the witness ratio a finding."""
    Q = _Q()
    entry = Q.line_of(Q.FIND, B590_ENTRY)
    if entry != 6740:
        sys.exit('### THE ADDRESSED LINE MOVED: entry %s -- NOTHING WRITTEN' % entry)
    W = jl('b590_witness_vs_bench.json')
    if (W['D'], W['kill'], W['jstar'], round(float(W['half_pre'])), round(float(W['ratio']))) != (24, 8, 24, 137278, 39196):
        sys.exit('### THE WITNESS BANK DOES NOT READ AS THE RULING CITES IT -- NOTHING WRITTEN')
    head = '*Appended 2026-10-02 by b591 to b590’s entry (:%d), under `(R201)`(1) -- b590 AT ITS WEIGHT:*' % entry
    Q.guard_absent(Q.FIND, head)
    text = ('\n%s SIDE-explicit-formula v0.16 = c404e72: the detector compiles generic and DERIVES, its base window named in the '
            'statement (the plateau at half-width 1/(4(‖γ(ρ₀)‖+1)), base_nonzero_at as witness), the power j and the coefficient '
            'list existential because j comes from Metric.tendsto_atTop over a limit with no rate (Converse.lean :171) -- b559’s '
            'H9a step again, so H31a refuted in letter at the power; epstein_not_h2_sign_cfg under one premise binder (hP : '
            'EpsteinPremises Z rhs) and the membership ρ_E ∈ Z.carrier, INTERFACES, T2-INTERFACES, ρ_E = b506’s 0.7979971571786801 '
            '+ 29.551761098629115 i; the salt-check compiled two ways (the premises hold together on the two-point configuration; '
            'the membership is load-bearing, since the empty configuration satisfies the premises and is Weil-positive), the '
            'premises’ consistency with Z_Q stated as unproved; H31b held. **The witness ratio, entered as a finding: the compiled '
            'witness is 2^D × ℓ, D from the kill set and ℓ from the excluded zero. At ρ_E the base half-width is 0.008182, the '
            'dominant off-line orbit is 16.29’s (ρ_E’s score 0.996 of it), eight on-line ordinates fall in the kill set, the '
            'kernel’s floor on the power is D = 24, and the witness’s half-width before pairing is at least 2²⁴ × 0.008182 = '
            '137,278, about 39,196 times ln 33.19: the compiled construction certifies the sign at j = 24 by its own inequality and '
            'is four orders of magnitude wider than the bench’s plateau** (relay data/b590_witness_vs_bench.txt :5, :7-:9, '
            ':12-:13, :21). H31c refuted as expected; the reading is the finding, entered at W-ORD-DETECTION-REGION as its (E3). '
            'The Day-1 W_∞ row at §I :32 and the repaired sentence at §II :45: each citation names its own object, both credit '
            'lines stand. The ferry bank redacted per the author’s answer; the sweep column filled (I 3, II 1, III 3, IV 3, V 2) '
            'in the local patent repository; no family label reached any public repository. The suite reads 68 of 68.\n' % head)
    r = Q.append_to(Q.FIND, text)
    put_json('b591_weight_line.json', dict(entry=entry, line=Q.line_of(Q.FIND, head), head=head, append=r))
    print('  weight line :%s' % Q.line_of(Q.FIND, head))


def e3_line():
    """### PLACE-papers OPEN_TRAILS: (E3) at W-ORD-DETECTION-REGION, one appended line addressed to the re-scope block."""
    Q = _Q()
    at = Q.line_of(Q.OT, RESCOPE)
    ls = io.open(Q.OT, encoding='utf-8').read().split(NL)
    if at != 11512 or not ls[11515].startswith('- **(E1)') or not ls[11516].startswith('- **(E2)') \
            or not ls[11335].startswith('- **C1**') or not ls[11336].startswith('- **C2**') or '(a)' not in ls[11422]:
        sys.exit('### THE ADDRESSED LINES MOVED -- NOTHING WRITTEN')
    head = ('*Appended 2026-10-02 by b591 to the DETECTION-REGION re-scope (:%d; (E1) :11516, (E2) :11517), under `(R201)`(2) -- '
            '(E3) THE WITNESS RATIO:*' % at)
    Q.guard_absent(Q.OT, head)
    text = ('\n%s the compiled witness is 2^D × ℓ with D from the kill set and ℓ from the excluded zero, while the bench detects at '
            'a plateau of half-width ln a ≈ 3.5; at the Epstein data D = 24 and the ratio is at least 39,196 (relay '
            'data/b590_witness_vs_bench.txt :9, :13). The factor of ~4 × 10⁴ is the price of the Tannery step and the kill set '
            'together, and (E1)’s configuration-relative rate would make D explicit but not small. The bench’s plateau family and '
            'the kernel’s power family are different windows, as b546/b550 recorded (the ruling’s citation). **The item that would '
            'close the ratio -- a compiled window of the bench’s plateau family -- priced beside (E1) and (E2), not started:** by '
            'b554’s closed-form route, the plateau-ramp window defined in the kernel with its transform in closed form (C1, :11336) '
            'and that window in classK (C2, :11337), each new and of substance, the route whole at three lemmas of substance '
            '(:11423); no new price is named.\n' % head)
    r = Q.append_to(Q.OT, text)
    put_json('b591_e3_line.json', dict(addressed=at, line=Q.line_of(Q.OT, head), head=head, append=r))
    print('  (E3) line :%s' % Q.line_of(Q.OT, head))


# ================================================================================ COMPONENT 1: THE E0 CLAUSE, THE RE-GRADE
def _e0_pair():
    """### the rule as b590 read it (relay PRE_RELAY's blob, loaded under another name) and the rule with the clause."""
    import importlib.util
    import types
    src = g(RELAY, 'show', '%s:tools/e0_rule.py' % PRE_RELAY)
    old = types.ModuleType('e0_rule_before')
    exec(compile(src, 'e0_rule_before', 'exec'), old.__dict__)
    import e0_rule as new
    return old, new


def _header_at(rev, rel, short):
    import b569_record as R9
    src = g(EFK, 'show', '%s:%s' % (rev, rel))
    head, _ = R9.header_of(src, short)
    return head


def regrade():
    """### membership_load_bearing re-read under the clause; the terminal table's theorem statements re-read before and after."""
    old, new = _e0_pair()
    L = ['b591 -- THE E0 RE-GRADE UNDER (R201)(3)`S CLAUSE, A READING. ### the rule before the clause is relay %s`s blob of '
         'tools/e0_rule.py; the rule after it is the working file, committed alone.' % PRE_RELAY, '']
    L += ['### the clause, as the rule now prints it:'] + ['    ' + x for x in new.RULE_TEXT[-2:]] + ['']
    rows = {}
    for rel, short in (('SIDEExplicitFormula/Schema/SaltCheckEpstein.lean', 'membership_load_bearing'),
                       ('SIDEExplicitFormula/Schema/Epstein.lean', 'epstein_not_h2_sign_cfg'),
                       ('SIDEExplicitFormula/Schema/SaltCheckEpstein.lean', 'epstein_hypotheses_satisfiable'),
                       ('SIDEExplicitFormula/Schema/Detector.lean', 'detector')):
        h = _header_at(V016, rel, short) or ''
        a, b = old.grade(h, 'theorem'), new.grade(h, 'theorem')
        rows[short] = dict(before=a[0], after=b[0], why_before=a[1], why_after=b[1], header=' '.join(h.split())[:400])
        L.append('    %-34s before %-10s after %-10s -- %s' % (short, a[0], b[0], b[1][:120]))
    tt = json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))
    row = [r for r in tt['rows'] if r['name'].endswith('.membership_load_bearing')]
    corr = io.open(os.path.join(GSR, 'CORRESPONDENCE.md'), encoding='utf-8').read()
    L += ['', '### the record`s grade for it: terminal table %s ; CORRESPONDENCE rows naming it: %d' % (
        [(r['grade'], len(r['grade_cells'])) for r in row], corr.count('membership_load_bearing'))]
    # ### the census: every theorem statement the terminal table carries, re-read before and after the clause.
    moved, n = [], 0
    for r in tt['rows']:
        st = r.get('statement') or ''
        m = re.match(r'^\s*(?:@\[[^\]]*\]\s*)?(?:private\s+|protected\s+)?(theorem|lemma)\s+(\S+)(.*)$', st, re.S)
        if not m:
            continue
        n += 1
        head = m.group(3).split(':=')[0]
        a, b = old.grade(head, 'theorem')[0], new.grade(head, 'theorem')[0]
        if a != b:
            moved.append(dict(repo=r['repo'], name=r['name'], before=a, after=b, table_grade=r['grade'], cells=len(r['grade_cells'])))
    L += ['', '### THE CENSUS: theorem statements in the terminal table re-read before and after the clause : %d ; readings moved : %d' % (n, len(moved))]
    L += ['    %s %s : %s -> %s (table grade %s, grade cells %d)' % (x['repo'], x['name'], x['before'], x['after'], x['table_grade'], x['cells'])
          for x in moved]
    graded_moved = [x for x in moved if x['cells'] or x['table_grade'] not in ('UNGRADED',)]
    L += ['', '### ### **NO GRADE MOVES: %s** -- a moved reading of a statement whose record holds a grade cell would be a move; '
          'the reading is corrected in this bank, not in any ledger.' % ('TRUE' if not graded_moved else '### FALSE %s' % graded_moved)]
    # ### both pages, re-emitted from their banked probe outputs by the shared arm, byte for byte.
    import g_chain_page as GCP
    pz = GCP.arm(os.path.join(D, 'b569_nodes.txt'), os.path.join(SP, '_b591_gcp'), os.path.join(D, 'b569_probe_out.txt'))
    pc = GCP.arm(os.path.join(D, 'b573_nodes_chi.txt'), os.path.join(SP, '_b591_gcp'), os.path.join(D, 'b573_chi_probe_out.txt'))
    L += ['', '### THE PAGES, re-emitted under the clause from their banked probe outputs: ζ %s ; χ %s' % (
        'BYTE FOR BYTE' if pz.get('ok') else '### DIFFERS %s' % {k: v for k, v in pz.items() if k != 'page'},
        'BYTE FOR BYTE' if pc.get('ok') else '### DIFFERS %s' % {k: v for k, v in pc.items() if k != 'page'})]
    # ### the clause isolated: each page re-emitted under the rule before the clause and under it, the two compared.
    import chain_page as C
    import difflib
    import types
    ab = {}
    for label, nodes, out, name in (('zeta', 'b569_nodes.txt', 'b569_probe_out.txt', PAGE),
                                    ('chi', 'b573_nodes_chi.txt', 'b573_chi_probe_out.txt', DIR_PAGE)):
        got = {}
        for tag, mod in (('before', old), ('after', new)):
            C.E0 = mod
            rc, page, meta, log = C.build(os.path.join(D, nodes), os.path.join(SP, '_b591_gcp'), os.path.join(D, out))
            got[tag] = (rc, page if isinstance(page, (bytes, bytearray)) else (page or '').encode('utf-8'),
                        [x for x in (log or []) if 'unresolved' in str(x)])
        C.E0 = new
        com = GCP.committed_page('HEAD', name) or b''
        diff = [l for l in difflib.unified_diff(com.decode('utf-8').split(NL), got['after'][1].decode('utf-8').split(NL), n=0, lineterm='')
                if l[:1] in '+-' and not l.startswith(('+++', '---'))]
        ab[label] = dict(rc_before=got['before'][0], rc_after=got['after'][0], equal=got['before'][1] == got['after'][1],
                         committed_equal=got['after'][1] == com, diff_added=[l[1:] for l in diff if l.startswith('+')],
                         diff_removed=len([l for l in diff if l.startswith('-')]), unresolved=[str(x)[:300] for x in got['after'][2]])
        L.append('### %s: exit before %d, after %d ; the re-emit before the clause EQUALS the re-emit after it : %s ; after = committed : %s' % (
            label, got['before'][0], got['after'][0], ab[label]['equal'], ab[label]['committed_equal']))
        if got['after'][0] == 0:
            L.append('    the re-emit against the committed page: %d lines added, %d removed --' % (len(ab[label]['diff_added']), ab[label]['diff_removed']))
            L += ['      + %s' % x[:200] for x in ab[label]['diff_added']]
        else:
            L += ['    %s' % x for x in ab[label]['unresolved']]
    L.append('### ### **THE CLAUSE MOVES NO PAGE BYTE: %s** (each page`s re-emit before the clause equals its re-emit after it); the '
             'byte-for-byte failures against the committed pages are not the clause`s.' % ('TRUE' if all(v['equal'] for v in ab.values()) else '### FALSE'))
    put_txt('b591_e0_regrade.txt', L)
    put_json('b591_e0_regrade.json', dict(rows=rows, table_row=[(r['grade'], len(r['grade_cells'])) for r in row],
                                          corr_rows=corr.count('membership_load_bearing'), census_n=n, moved=moved,
                                          no_grade_moved=not graded_moved, page_zeta=bool(pz.get('ok')), page_chi=bool(pc.get('ok')),
                                          ab=ab))


# ================================================================================ COMPONENT 2: THE DOCUMENT
# ### the four transfers' statements searched in Mathlib at de5ce8a9 (git grep over the package checkout, whose HEAD is the pin),
# ### beside the positive control, and the library objects a salt-checked statement would range over.
TRANSFERS = [
    ('BSD', r'BirchSwinnerton|Birch.?Swinnerton|\bBSD\b|analyticRank|algebraicRank|GrossZagier|Gross.Zagier|Kolyvagin'),
    ('Navier-Stokes', r'NavierStokes|Navier|BealeKatoMajda|Beale.Kato|incompressib|vorticity|Euler.?equation'),
    ('twin primes', r'TwinPrime|twin_prime|twinPrime|[Tt]win prime|parity.?(problem|obstruction|barrier)'),
    ('P versus NP', r'P_ne_NP|PneNP|P ≠ NP|P vs NP|P_neq_NP|P versus NP|NPComplete|NP.?complete|[Rr]elativi[sz]ation|[Nn]aturalProof|natural proofs'),
]
CONTROL = ('RiemannHypothesis', r'^def RiemannHypothesis\b')
OBJECTS = [
    ('BSD', 'WeierstrassCurve', r'^structure WeierstrassCurve\b'),
    ('twin primes', 'Nat.Prime', r'^def Prime \(p : ℕ\)'),
    ('P versus NP', 'TM2ComputableInPolyTime', r'^structure TM2ComputableInPolyTime\b'),
]


def _mgrep(pat, *paths):
    r = subprocess.run(['git', '-C', MATHLIB, 'grep', '-n', '-E', pat, '--'] + list(paths or ['Mathlib']), capture_output=True)
    return [l for l in r.stdout.decode('utf-8', 'replace').replace(chr(13), '').split(NL) if l.strip()]


def transfers():
    head = g(MATHLIB, 'rev-parse', 'HEAD').strip()
    L = ['b591 -- THE FOUR TRANSFERS AGAINST MATHLIB AT %s (the package checkout`s HEAD), BY git grep OVER Mathlib, Archive AND '
         'Counterexamples. ### A READING.' % head[:12], '']
    ctl = _mgrep(CONTROL[1], 'Mathlib')
    L.append('### THE POSITIVE CONTROL, %s: %d hit(s) %s' % (CONTROL[0], len(ctl), ctl[:2]))
    res = {}
    for name, pat in TRANSFERS:
        hits = _mgrep(pat, 'Mathlib', 'Archive', 'Counterexamples')
        decl = [h for h in hits if re.search(r':\d+:\s*(theorem|lemma|def|structure|class|abbrev|noncomputable def|instance)\b', h)]
        res[name] = dict(hits=len(hits), declarations=decl, sample=hits[:6])
        L.append('### %s -- the matcher %r: %d line(s), %d of them a declaration line' % (name, pat, len(hits), len(decl)))
        L += ['    %s' % h[:200] for h in hits[:8]]
    L.append('')
    objs = {}
    for t, name, pat in OBJECTS:
        h = _mgrep(pat, 'Mathlib')
        objs[name] = h[:1]
        L.append('### the library object for %s: %s -- %s' % (t, name, h[:1] or '### NOT FOUND'))
    L.append('### Navier-Stokes: no fluid object by the matcher above (the incompressibility, vorticity and Euler-equation terms included).')
    stated = [n for n, v in res.items() if v['declarations']]
    L += ['', '### ### **LIBRARY STATEMENTS FOR THE FOUR TRANSFERS AT %s: %s** -- the control found (%d)' % (
        head[:8], 'NONE' if not stated else stated, len(ctl))]
    put_txt('b591_transfers.txt', L)
    put_json('b591_transfers.json', dict(mathlib=head, control=ctl, transfers=res, objects=objs, stated=stated))


def _page_nodes(page):
    """### the node lines of a page at the mirror's pin: number, name, file, line, tag, sha, E0, tier, page line."""
    out = []
    for i, l in enumerate(g(PP, 'show', '%s:%s' % (MIRROR_PIN, page)).split(NL), 1):
        m = re.match(r'^(\d+)\. `([^`]+)` — (\S+?):(\d+) — (\S+) = (\w+)(?: \([^)]*\))? — .*? — E0: (\w+) — tier: (\S*) ', l)
        if m:
            out.append(dict(n=int(m.group(1)), name=m.group(2), file=m.group(3), line=int(m.group(4)), tag=m.group(5), sha=m.group(6),
                            e0=m.group(7), tier=m.group(8) or '—', page=page, page_line=i))
    return out


V016_ROWS = [('SIDEExplicitFormula.Schema.detector', 'SIDEExplicitFormula/Schema/Detector.lean'),
             ('SIDEExplicitFormula.Schema.not_h2_sign_cfg_of_offline', 'SIDEExplicitFormula/Schema/Detector.lean'),
             ('SIDEExplicitFormula.Schema.epstein_not_h2_sign_cfg', 'SIDEExplicitFormula/Schema/Epstein.lean')]


def corr_rows():
    """### the back matter's Correspondence rows: every node of both pages at the mirror's pin, and b590's terminals at v0.16."""
    rows = _page_nodes(PAGE) + [r for r in _page_nodes(DIR_PAGE) if r['name'] not in [x['name'] for x in _page_nodes(PAGE)]]
    tt = json.load(io.open(os.path.join(D, 'terminal_table.json'), encoding='utf-8'))
    byname = {r['name']: r for r in tt['rows'] if r['repo'] == 'SIDE-explicit-formula'}
    for name, f in V016_ROWS:
        src = g(EFK, 'show', '%s:%s' % (V016, f)).split(NL)
        short = name.split('.')[-1]
        ln = [i for i, l in enumerate(src, 1) if re.match(r'^(theorem|lemma) %s(?![\w\'])' % re.escape(short), l)]
        t = byname.get(name, {})
        tier = 'T2-INTERFACES' if t.get('grade') == 'INTERFACES' else ('T0' if t.get('grade') == 'DERIVES' else '—')
        rows.append(dict(n=None, name=name, file=f, line=ln[0] if ln else None, tag='v0.16', sha='c404e72', e0=t.get('grade'), tier=tier,
                         page=None, page_line=None, source='terminal table, CORRESPONDENCE rows 442-445'))
    put_json('b591_corr_rows.json', rows)
    for r in rows:
        print('  %-62s %s:%s %s = %s %s %s' % (r['name'][-62:], r['file'], r['line'], r['tag'], r['sha'], r['e0'], r['tier']))
    print('  rows : %d ; INTERFACES : %s' % (len(rows), [r['name'] for r in rows if r['e0'] == 'INTERFACES']))


# ### THE DOCUMENT'S READERS. ### No body sentence is printed by any of them: a hit is printed by section, line and phrase.
SECTION_RE = re.compile(r'^## \((i|ii|iii|iv|v|vi|vii|viii)\) ', re.M)
CEILING = re.compile(r'RH proved|RH is proved|h2_sign proved|λ_n ≥ 0 proved|GRH proved|GRH reduced|reduction machine-verified|proof of RH|'
                     r'proves RH|RH proves|RH proof|[Pp]roof of GRH|GRH holds|GRH (?:is )?established|RH IS SIMPLE|[Tt]he theorem is at rest|'
                     r'The proof is pointing|closes the catalogue\b|Establishes exhaustiveness|closes exhaustiveness|catalogue is exhaustive\.|'
                     r'BSD (?:is )?(?:proved|holds|established)|(?:proves?|proved|settles?|settled|resolves?|resolved) (?:BSD|the BSD|Navier|the Navier|'
                     r'the twin|twin prime|P versus NP|P ?(?:≠|!=|=) ?NP)|P ?(?:≠|!=) ?NP (?:is |was )?(?:proved|holds|established)|'
                     r'twin primes? (?:conjecture )?(?:is )?(?:proved|holds)|Navier.Stokes (?:is )?(?:solved|proved|regular)|'
                     r'(?:proves|proved|settles|resolves) (?:the )?(?:conjecture|hypothesis|Riemann)|the method proves\b|zeros? (?:all )?(?:lie|lies) on the')


def _doc_text(which):
    p = DOC if which == 'placed' else os.path.join(SP, 'located_clause_%s.md' % which)
    return io.open(p, encoding='utf-8').read().replace(chr(13), ''), p


def _sections(text):
    ms = list(SECTION_RE.finditer(text))
    out = []
    for k, m in enumerate(ms):
        end = ms[k + 1].start() if k + 1 < len(ms) else len(text)
        out.append((m.group(1), text[m.start():end]))
    return out


def _prose_sentences(text):
    """### prose sentences of the body, markdown stripped, at least 40 characters -- the no-disclosure needles."""
    body = ''.join(s for k, s in _sections(text) if k != 'viii')
    out = []
    for para in re.split(r'\n\s*\n', body):
        if para.lstrip().startswith(('|', '#', '```')):
            continue
        flat = ' '.join(re.sub(r'[*_`]', '', para).split())
        for s in re.split(r'(?<=[.;:])\s+(?=[A-Z(])', flat):
            if len(s) >= 40:
                out.append(s)
    return out


def doc_scan(which='draft1'):
    """### the ceiling read and the stem scan over a draft (scratchpad) or the committed file, the words per section, the
    ### citations per section. Banked by position and phrase; never a sentence."""
    import banned_terms as BT
    text, path = _doc_text(which)
    ls = text.split(NL)
    secs = _sections(text)
    words = {k: len(s.split()) for k, s in secs}
    body = sum(v for k, v in words.items() if k != 'viii')
    ceil, stems = [], []
    for i, l in enumerate(ls, 1):
        sec = ([k for k, s in secs if text.find(s) <= sum(len(x) + 1 for x in ls[:i - 1])] or ['head'])[-1]
        for m in CEILING.finditer(l):
            ceil.append(dict(line=i, section=sec, phrase=m.group(0)))
        for m in BT.PAT.finditer(l):
            if not any(rx.search(l) for rx, _ in BT.EXCEPT):
                stems.append(dict(line=i, section=sec, phrase=m.group(0)))
    cites = {}
    for k, s in secs:
        cites[k] = dict(
            pins=sorted(set(re.findall(r'\b(?:v0\.\d+ = [0-9a-f]{7}|[0-9a-f]{7,12})\b', s))),
            lines=sorted(set(re.findall(r'(?:ζ page|χ page|FINDINGS|OPEN_TRAILS|README|SPIRAL_MAP|RESIDUE|THE_METHOD_CANON|data/\S+?|\.lean)\s?:\d+(?:-:\d+)?', s))),
            decls=sorted(set(re.findall(r'`([A-Za-z_][\w.\']*)`', s))))
    res = dict(which=which, path=path.replace('\\', '/'), sha256=hashlib.sha256(text.encode('utf-8')).hexdigest(), words=words, body=body,
               vi=words.get('vi', 0), ceiling=ceil, stems=stems, citations=cites, sentences=len(_prose_sentences(text)))
    put_json('b591_doc_scan_%s.json' % which, res)
    L = ['b591 -- THE DOCUMENT`S READ, %s (%s). ### positions and phrases only; no sentence of the document is printed.' % (which, res['path']),
         '### sha256 %s' % res['sha256'], '### words per section: %s ; body (i)-(vii) %d ; section (vi) %d (%.1f%% of the body)' % (
             words, body, res['vi'], 100.0 * res['vi'] / max(body, 1)),
         '### the ceiling read (the editions` pattern, b586, widened with the transfers` phrases): %d hit(s) %s' % (len(ceil), ceil),
         '### the stem scan (banned_terms.PAT less its EXCEPT): %d live use(s) %s' % (len(stems), stems)]
    for k, c in cites.items():
        L.append('### (%s) citations -- pins %s ; lines %s ; declarations %d' % (k, c['pins'], c['lines'], len(c['decls'])))
    put_txt('b591_doc_scan_%s.txt' % which, L)
    for x in L[1:5]:
        print('  ' + x[:300])


# ### THE SEAT'S READ OF THE FIRST DRAFT, sentence by sentence, after the pattern: each correction by section, the phrase it
# ### removes (a phrase, never the sentence), the phrase it puts in its place, and its reason.
SEAT_READ = [
    dict(section='iii', old=', at a configuration the corpus records as RH-false (RESIDUE :87).',
         new='; it is the negative control that (R200)(4) ordered, and nothing about the zeros of the Epstein zeta function is asserted '
             'beyond its conclusion.',
         reason='the cited line calls Z_Q RH-false: a statement about the Epstein zeros beyond the INTERFACES conclusion b590 compiled '
                '(b590`s face (A) and (Z)); the ceiling clause corrects it'),
]


def ceiling_read():
    """### the seat's read banked, and the corrected draft (draft2) written into the scratchpad from draft1 by SEAT_READ."""
    t1, _ = _doc_text('draft1')
    s1 = jl('b591_doc_scan_draft1.json')
    t2, rows = t1, []
    for c in SEAT_READ:
        if t2.count(c['old']) != 1:
            sys.exit('### A CORRECTION`S OLD PHRASE IS NOT ONCE IN THE DRAFT -- NOTHING WRITTEN')
        ln = t2[:t2.index(c['old'])].count(NL) + 1
        t2 = t2.replace(c['old'], c['new'])
        rows.append(dict(section=c['section'], line=ln, phrase=re.sub(r'\s*\(.*', '', c['old']).strip(', '), reason=c['reason']))
    p2 = os.path.join(SP, 'located_clause_draft2.md')
    open(p2 + '.tmp', 'wb').write(t2.encode('utf-8'))
    os.replace(p2 + '.tmp', p2)
    L = ['b591 -- THE CEILING READ OF THE SEAT`S FIRST DRAFT, BEFORE THE SEAL (the commit). ### positions and phrases only.',
         '### the draft: sha256 %s, body %d words' % (s1['sha256'], s1['body']),
         '### (1) THE PATTERN (the editions` ceiling pattern, b586_record.py :429, widened with the four transfers` phrases): %d hit(s) ; '
         'the stem scan: %d live use(s)' % (len(s1['ceiling']), len(s1['stems'])),
         '### (2) THE SEAT`S READ OF EVERY SENTENCE, after the pattern: %d correction(s)' % len(rows)]
    L += ['    (%s) line %d -- removed: "%s" -- %s' % (r['section'], r['line'], r['phrase'], r['reason']) for r in rows]
    L.append('### ### **CORRECTIONS BEFORE THE SEAL : %d** (the pattern %d, the seat`s read %d)' % (
        len(s1['ceiling']) + len(s1['stems']) + len(rows), len(s1['ceiling']) + len(s1['stems']), len(rows)))
    put_txt('b591_doc_ceiling_read.txt', L)
    put_json('b591_doc_ceiling_read.json', dict(pattern=len(s1['ceiling']), stems=len(s1['stems']), seat=rows,
                                                corrections=len(s1['ceiling']) + len(s1['stems']) + len(rows), draft1=s1['sha256']))


def doc_table():
    """### the back matter written last: the Correspondence table of every declaration sections (i)-(vii) name, from the rows
    ### banked by corr_rows and the transfers bank's library objects; the final text into the scratchpad."""
    t2 = io.open(os.path.join(SP, 'located_clause_draft2.md'), encoding='utf-8').read().replace(chr(13), '')
    body = ''.join(s for k, s in _sections(t2) if k != 'viii')
    named = sorted(set(re.findall(r'`([A-Za-z_][\w.\']*)`', body)))
    rows = jl('b591_corr_rows.json')
    tj = jl('b591_transfers.json')
    ml = dict(WeierstrassCurve=('Mathlib/AlgebraicGeometry/EllipticCurve/Weierstrass.lean', tj['objects']['WeierstrassCurve']),
              **{'Nat.Prime': ('Mathlib/Data/Nat/Prime/Defs.lean', tj['objects']['Nat.Prime']),
                 'TM2ComputableInPolyTime': ('Mathlib/Computability/TuringMachine/Computable.lean', tj['objects']['TM2ComputableInPolyTime'])})
    out, miss = [], []
    for n in named:
        if n in ml:
            f, hit = ml[n]
            ln = int(hit[0].split(':')[1]) if hit else None
            out.append(dict(name=n, pin='Mathlib de5ce8a9', file=f, line=ln, grade='DEF', tier='—'))
            continue
        cand = [r for r in rows if r['name'] == n or r['name'].split('.')[-1] == n]
        if len(cand) != 1:
            miss.append((n, len(cand)))
            continue
        r = cand[0]
        pin = 'Mathlib de5ce8a9' if r['tag'] == 'Mathlib' else 'SIDE-explicit-formula %s = %s' % (r['tag'], r['sha'])
        f = ('Mathlib/' + r['file']) if r['tag'] == 'Mathlib' and not r['file'].startswith('Mathlib/') else r['file']
        out.append(dict(name=r['name'], pin=pin, file=f, line=r['line'], grade=r['e0'], tier=r['tier']))
    if miss:
        sys.exit('### NAMED BUT NOT RESOLVED TO ONE ROW: %s -- NOTHING WRITTEN' % miss)
    tab = ['| declaration | pin | file:line | grade | tier |', '|:--|:--|:--|:--|:--|']
    tab += ['| `%s` | %s | %s:%s | %s | %s |' % (r['name'], r['pin'], r['file'], r['line'], r['grade'], r['tier']) for r in out]
    if t2.count('CORRESPONDENCE_TABLE') != 1:
        sys.exit('### THE PLACEHOLDER IS NOT ONCE IN THE DRAFT -- NOTHING WRITTEN')
    fin = t2.replace('CORRESPONDENCE_TABLE', NL.join(tab) + NL + NL + '*Grades: DEF and DERIVES are the E0 cells of the page lines '
                     'at 192077f (ζ page :5-:29, χ page :5-:22); the v0.16 rows are CORRESPONDENCE rows 443-445 at SIDE-global-section '
                     '3528bcf, their tiers by the tier law; the Mathlib objects are definitions, graded DEF by the shared rule.*')
    fin = fin.rstrip(NL) + NL
    pf = os.path.join(SP, 'located_clause_final.md')
    open(pf + '.tmp', 'wb').write(fin.encode('utf-8'))
    os.replace(pf + '.tmp', pf)
    put_json('b591_doc_table.json', dict(named=named, rows=out))
    print('  named %d ; rows %d ; INTERFACES %s' % (len(named), len(out), [r['name'] for r in out if r['grade'] == 'INTERFACES']))


def doc_citations():
    """### the citations of each section, printed as it is written: a bank per section, cumulative, citations only."""
    s = jl('b591_doc_scan_placed.json')
    L = ['b591 -- THE DOCUMENT`S CITATIONS, SECTION BY SECTION (the placed file, sha256 %s; citations only, no sentence).' % s['sha256']]
    for k, c in s['citations'].items():
        L += ['', '### (%s) -- %d words' % (k, s['words'][k]), '    pins : %s' % ', '.join(c['pins']), '    lines: %s' % ', '.join(c['lines']),
              '    declarations: %s' % ', '.join(c['decls'])]
    put_txt('b591_doc_citations.txt', L)


def doc_place():
    """### TECHNE-Core: the corrected draft written beside the b257 drafts (the file created; the seat commits it alone)."""
    src = os.path.join(SP, 'located_clause_final.md')
    if os.path.exists(DOC):
        sys.exit('### THE FILE EXISTS AT %s -- NOTHING WRITTEN' % DOC)
    b = io.open(src, encoding='utf-8').read().replace(chr(13), '').encode('utf-8')
    open(DOC + '.tmp', 'wb').write(b)
    os.replace(DOC + '.tmp', DOC)
    print('  written: %s (%d bytes, sha256 %s)' % (DOC, len(b), hashlib.sha256(b).hexdigest()))


# ================================================================================ THE HYPOTHESES
def _resolve_row(r):
    short = r['name'].split('.')[-1]
    repo, rev = (MATHLIB, 'HEAD') if r['pin'].startswith('Mathlib') else (EFK, r['pin'].split('= ')[1])
    src = g(repo, 'show', '%s:%s' % (rev, r['file'])).split(NL)
    l = src[r['line'] - 1] if r['line'] and 0 < r['line'] <= len(src) else ''
    return re.search(r'(?<![\w.])%s(?![\w\'])' % re.escape(short), l) is not None


def h32():
    """### H32a-H32c and (N2)'s resolution, on the placed file; every pin read back at its remote."""
    text, _ = _doc_text('placed')
    s = jl('b591_doc_scan_placed.json')
    scan = rd('b591_doc_termscan.txt')
    # ### H32a
    a_ok = not s['ceiling'] and not s['stems'] and re.search(r'^\s*VERDICT\s*: CLEAN\s*$', scan, re.M) is not None \
        and re.search(r'^\s*live uses\s*: 0\s*$', scan, re.M) is not None
    # ### H32b: the pins
    pins = sorted(set(re.findall(r'\b(?:v0\.\d+ = [0-9a-f]{7}|[0-9a-f]{7,12})\b', text)))
    res = {}
    tags = {}
    for l in g(EFK, 'ls-remote', 'origin', 'refs/tags/v0.*').split(NL):
        if '\t' in l:
            sha, ref = l.split('\t')
            if ref.endswith('^{}'):
                tags[ref[len('refs/tags/'):-3]] = sha
    for p in pins:
        m = re.match(r'^(v0\.\d+) = ([0-9a-f]{7})$', p)
        if m:
            res[p] = dict(kind='kernel tag, ls-remote peeled', remote=tags.get(m.group(1), ''), ok=tags.get(m.group(1), '').startswith(m.group(2)))
        elif p in ('de5ce8a9',):
            r = subprocess.run(['gh', 'api', 'repos/leanprover-community/mathlib4/commits/%s' % p, '--jq', '.sha'], capture_output=True)
            sha = r.stdout.decode().strip()
            res[p] = dict(kind='Mathlib, gh api commit endpoint', remote=sha, ok=r.returncode == 0 and sha.startswith(p))
        elif grc(PP, 'cat-file', '-e', p + '^{commit}') == 0:
            res[p] = dict(kind='PLACE-papers, ancestor of origin/main', remote=g(PP, 'rev-parse', 'origin/main').strip(),
                          ok=grc(PP, 'merge-base', '--is-ancestor', p, 'origin/main') == 0)
        elif grc(GSR, 'cat-file', '-e', p + '^{commit}') == 0:
            res[p] = dict(kind='SIDE-global-section, ancestor of origin/main', remote=g(GSR, 'rev-parse', 'origin/main').strip(),
                          ok=grc(GSR, 'merge-base', '--is-ancestor', p, 'origin/main') == 0)
        elif grc(EFK, 'cat-file', '-e', p + '^{commit}') == 0:
            res[p] = dict(kind='SIDE-explicit-formula, ancestor of origin/main', remote=g(EFK, 'rev-parse', 'origin/main').strip(),
                          ok=grc(EFK, 'merge-base', '--is-ancestor', p, 'origin/main') == 0)
        else:
            res[p] = dict(kind='### UNRESOLVED', remote='', ok=False)
    # ### H32b: the page lines, each existing at the mirror's pin and non-blank; each table row's name on its page line there
    pl = {}
    for k, page in (('ζ', PAGE), ('χ', DIR_PAGE)):
        ls = g(PP, 'show', '%s:%s' % (MIRROR_PIN, page)).split(NL)
        cited = set()
        for a, b in re.findall(r'%s page :(\d+)(?:-:(\d+))?' % k, text):
            cited |= set(range(int(a), int(b or a) + 1))
        for m in re.finditer(r'%s page (:\d+(?:-:\d+)?(?:, :\d+(?:-:\d+)?)+)' % k, text):
            for a, b in re.findall(r':(\d+)(?:-:(\d+))?', m.group(1)):
                cited |= set(range(int(a), int(b or a) + 1))
        # ### the ruling's letter: a cited line EXISTS at the pin. The tool's first run also refused a blank line (defect (b)); the
        # ### blank lines a citation covers are printed beside, informational.
        pl[k] = dict(cited=sorted(cited), missing=[n for n in sorted(cited) if not (0 < n <= len(ls))],
                     blank=[n for n in sorted(cited) if 0 < n <= len(ls) and not ls[n - 1].strip()], length=len(ls))
    rows = jl('b591_doc_table.json')['rows']
    cr = {r['name']: r for r in jl('b591_corr_rows.json')}
    on_page = []
    for r in rows:
        c = cr.get(r['name'])
        if c and c.get('page_line'):
            ls = g(PP, 'show', '%s:%s' % (MIRROR_PIN, c['page'])).split(NL)
            on_page.append((r['name'], c['page_line'], ('`%s`' % r['name']) in ls[c['page_line'] - 1]))
    b_ok = all(v['ok'] for v in res.values()) and not any(v['missing'] for v in pl.values()) and all(x[2] for x in on_page)
    # ### (N2): every row resolves at its pin
    resolved = [(r['name'], _resolve_row(r)) for r in rows]
    # ### H32c
    c_ok = s['body'] <= 2500 and s['vi'] * 4 <= s['body']
    out = dict(H32a='HOLDS' if a_ok else 'REFUTED', H32b='HOLDS' if b_ok else 'REFUTED', H32c='HOLDS' if c_ok else 'REFUTED',
               pins=res, page_lines=pl, on_page=on_page, resolved=resolved, rows=len(rows), body=s['body'], vi=s['vi'],
               words=s['words'], sha256=s['sha256'], ceiling=s['ceiling'], stems=s['stems'])
    put_json('b591_h32.json', out)
    L = ['b591 -- (R201)(5)`S HYPOTHESES ON THE PLACED FILE (TECHNE-Core %s, sha256 %s). ### positions, pins and counts only.' % (DOC_REL, s['sha256']),
         '', '### H32a -- ceiling hits %d ; live stems %d ; the scanner`s verdict line CLEAN : %s ### **H32a %s**' % (
             len(s['ceiling']), len(s['stems']), bool(re.search(r'VERDICT\s*: CLEAN', scan)), out['H32a']),
         '### H32b -- the pins the document cites, each read back at its remote:']
    L += ['    %-22s %-44s remote %s %s' % (p, v['kind'], v['remote'][:12], 'RESOLVES' if v['ok'] else '### DOES NOT RESOLVE') for p, v in res.items()]
    L += ['    page lines at %s: ζ cited %d, missing %s (page %d lines) ; χ cited %d, missing %s (page %d lines)' % (
        MIRROR_PIN, len(pl['ζ']['cited']), pl['ζ']['missing'], pl['ζ']['length'], len(pl['χ']['cited']), pl['χ']['missing'], pl['χ']['length']),
          '    beside, the stricter predicate of the tool`s first run (a cited line non-blank, not in the ruling): blank lines inside a '
          'cited range -- ζ %s, χ %s -- under it H32b would read REFUTED (defect (b))' % (pl['ζ']['blank'], pl['χ']['blank']),
          '    table rows on their page lines at %s: %d of %d carry the name' % (MIRROR_PIN, sum(x[2] for x in on_page), len(on_page)),
          '### ### **H32b %s**' % out['H32b'],
          '### H32c -- body %d words (at most 2,500) ; section (vi) %d words, %.1f%% (at most a quarter) ### **H32c %s**' % (
              s['body'], s['vi'], 100.0 * s['vi'] / s['body'], out['H32c']),
          '', '### (N2) -- Correspondence rows %d ; resolved at their pins %d ; unresolved %s' % (
              len(rows), sum(x[1] for x in resolved), [x[0] for x in resolved if not x[1]] or 'NONE')]
    put_txt('b591_h32.txt', L)
    for x in L[2:]:
        print('  ' + x[:200])


SCORE_KEYS = ('H32a', 'H32b', 'H32c', 'N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
KERNELS = {'SIDE-explicit-formula': 'c404e72', 'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
           'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
           'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}


def scores():
    h, rg, tr, cr, tb = jl('b591_h32.json'), jl('b591_e0_regrade.json'), jl('b591_transfers.json'), jl('b591_doc_ceiling_read.json'), jl('b591_doc_table.json')
    heads = {k: g('D:/' + k, 'rev-parse', 'main').strip() for k in KERNELS}
    kern_ok = all(heads[k].startswith(v) for k, v in KERNELS.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    te_ns = [l for l in g(TE, 'diff', '--name-status', PRE_TE, 'HEAD').split(NL) if l.strip()]
    faces = [l for l in g(RELAY, 'diff', '--name-only', PRE_RELAY, '--', 'data/*_registration_*.txt').split(NL) if l.strip()]
    relay_tools = sorted(x for x in g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD', '--', 'tools/').split(NL) if x.strip())
    edited_tools = [x for x in relay_tools if not os.path.basename(x).startswith('b591_') and x != 'tools/test_e0_existential.py']
    rows = tb['rows']
    pins = h['pins']
    S = dict(
        H32a=(h['H32a'], 'ceiling hits %d, live stems %d, the scanner CLEAN' % (len(h['ceiling']), len(h['stems']))),
        H32b=(h['H32b'], '%d pins, each read back at its remote; page lines at 192077f all present; %d table rows on their page lines' % (
            len(pins), len(h['on_page']))),
        H32c=(h['H32c'], 'body %d words; section (vi) %d (%.1f%%)' % (h['body'], h['vi'], 100.0 * h['vi'] / h['body'])),
        N1=('HELD' if h['H32a'] == h['H32b'] == h['H32c'] == 'HOLDS' else 'REFUTED', 'H32a %s, H32b %s, H32c %s' % (h['H32a'], h['H32b'], h['H32c'])),
        N2=('HELD' if len(rows) >= 20 and all(x[1] for x in h['resolved']) else 'REFUTED', '%d declarations by pin, %d resolved' % (
            len(rows), sum(x[1] for x in h['resolved']))),
        N3=('HELD' if not tr['stated'] and tr['control'] else 'REFUTED', 'library statements for the four at de5ce8a9: %s; the control found %d' % (
            tr['stated'] or 'none', len(tr['control']))),
        N4=('HELD' if cr['corrections'] <= 2 else 'REFUTED', '%d correction(s) before the seal (the pattern %d, the seat`s read %d)' % (
            cr['corrections'], cr['pattern'] + cr['stems'], len(cr['seat']))),
        N5=('HELD' if kern_ok and pp_ch == ['FINDINGS.md', 'OPEN_TRAILS.md'] and te_ns == ['A\t' + DOC_REL] and not faces
            and edited_tools == ['tools/e0_rule.py'] else 'REFUTED',
            'nothing deposits; kernel heads %s; PLACE-papers %s (appends); TECHNE-Core %s; sealed faces edited %s; relay tools edited %s' % (
                'unmoved' if kern_ok else heads, pp_ch, te_ns, faces or 'none', edited_tools)),
        S1=('HELD' if len(rg['moved']) == 1 and rg['page_zeta'] and rg['page_chi'] else 'REFUTED',
            'readings moved %d (%s); pages byte for byte against the committed: ζ %s, χ %s; the clause moves no page byte: %s' % (
                len(rg['moved']), ', '.join(x['name'].split('.')[-1] for x in rg['moved']), rg['page_zeta'], rg['page_chi'],
                all(v['equal'] for v in rg['ab'].values()))),
        S2=('HELD' if cr['corrections'] == 0 else 'REFUTED', 'the first draft needed %d correction(s)' % cr['corrections']),
        S3=('HELD' if h['H32b'] == 'HOLDS' and all(v['kind'].startswith(('kernel tag', 'Mathlib', 'PLACE-papers', 'SIDE-global-section'))
                                                   for v in pins.values()) and not [p for p, v in pins.items() if v['kind'].startswith('SIDE-explicit-formula')]
            else 'REFUTED', 'every kernel pin a tag: %s' % (not [p for p, v in pins.items() if v['kind'].startswith('SIDE-explicit-formula')])),
        S4=('HELD' if 1600 <= h['body'] <= 2400 and h['vi'] * 5 < h['body'] else 'REFUTED', 'body %d; (vi) %d' % (h['body'], h['vi'])),
        S5=('HELD' if len(rows) >= 25 and [r['name'] for r in rows if r['grade'] == 'INTERFACES'] == ['SIDEExplicitFormula.Schema.epstein_not_h2_sign_cfg']
            else 'REFUTED', '%d rows; INTERFACES %s' % (len(rows), [r['name'].split('.')[-1] for r in rows if r['grade'] == 'INTERFACES'])),
    )
    put_json('b591_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-4s %s -- %s' % (k, S[k][0], S[k][1][:170]))


TITLE = ('## The located-clause method: the open statement, the star of compiled equivalents, the surround classified, the ζ-leg as '
         'the worked instance, four transfers proposed -- written beside the b257 drafts in TECHNE-Core, local-only')
TRAIL_HEAD = ('### b591 — lane three, act eighteen under (R201): the located-clause method document written from the ledgers, '
              'placed beside the b257 drafts in TECHNE-Core and not pushed; the witness ratio entered at DETECTION-REGION as (E3); '
              'the E0 rule’s existential-binder clause')


def findings():
    Q = _Q()
    S, h, wl, e3, rg = jl('b591_scores.json'), jl('b591_h32.json'), jl('b591_weight_line.json'), jl('b591_e3_line.json'), jl('b591_e0_regrade.json')
    te = g(TE, 'rev-parse', '--short=7', 'HEAD').strip()
    e0c = g(RELAY, 'log', '-1', '--format=%h', '--', 'tools/e0_rule.py').strip()
    Q.guard_absent(Q.FIND, TITLE[:90])
    e = ['', TITLE, '',
         '*Filed at b591 on the author’s ruling `(R201)`. Banks: relay `data/b591_doc_scan_placed.txt`, `data/b591_doc_citations.txt`, '
         '`data/b591_doc_ceiling_read.txt`, `data/b591_doc_termscan.txt`, `data/b591_h32.txt`, `data/b591_transfers.txt`, '
         '`data/b591_e0_regrade.txt`, `data/b591_e0_test.txt`. Nothing deposits. The document is private: this entry carries its '
         'name, location, word count and digest, and no sentence of its body.*', '',
         '**The document** (`(R201)(4)`, placed as the author answered before the seal): THE_LOCATED_CLAUSE_METHOD.md at '
         'TECHNE-Core `%s`, beside the b257 drafts, committed alone in that clone as %s and not pushed; version v0.1, 2026-10-02; '
         'sha256 `%s`; body %d words over sections (i)-(vii) (%s), section (vi) %d words; the back matter a Placement table and a '
         'Correspondence table of %d declarations, each with its pin and grade. The ruling’s path (`phase2/method/`) and its '
         '“promotion later” clause are struck as the navigator’s.' % (
             DOC_REL, te, h['sha256'], h['body'], ', '.join('%s %d' % (k, v) for k, v in h['words'].items() if k != 'viii'), h['vi'],
             h['rows']), '',
         '**The hypotheses.** H32a %s (ceiling hits 0, live stems 0, the scanner CLEAN); H32b %s (%d pins, each read back at its '
         'remote: the kernel’s tags by ls-remote, PLACE-papers and SIDE-global-section by ancestry of the remote-tracking main, '
         'Mathlib de5ce8a9 at GitHub’s commit endpoint; every page line cited present at 192077f); H32c %s. The first draft’s '
         'ceiling read: the pattern found nothing, the seat’s read one sentence beyond the ceiling (a corpus line on the Epstein '
         'zeros, removed). Section (vi): no library statement for any of the four at de5ce8a9 (the control finds RiemannHypothesis).' % (
             S['H32a'][0], S['H32b'][0], len(h['pins']), S['H32c'][0]), '',
         '**The E0 rule’s existential-binder clause** (`(R201)(3)`), relay %s, committed alone with its test (7 of 7): '
         'membership_load_bearing re-read DERIVES from INTERFACES; its record holds no grade cell, so no grade moves and the reading '
         'is corrected; of %d theorem statements in the terminal table the clause moves that reading alone. Under the rule before '
         'the clause and under it the pages re-emit equal. **Found, not repaired:** the ζ page no longer regenerates byte for byte '
         'at PLACE-papers HEAD -- its Placement table predates eleven editions (b578-b589) that name its nodes -- and the χ page’s '
         'banked probe output cannot resolve the three Schema declarations the record gained at b590; neither page is edited.' % (
             e0c, rg['census_n']), '',
         '**b590 at its weight**: FINDINGS :%d, the witness ratio entered as a finding. **(E3)** at W-ORD-DETECTION-REGION: '
         'OPEN_TRAILS :%d, the compiled window of the bench’s plateau family priced beside (E1) and (E2) at b554’s C1-C2, not '
         'started.' % (wl['line'], e3['line']), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Next.** Per `(R201)`(6): the RESIDUE edition by the form; the author rules on the closing.', '',
         '*Nothing deposits; no kernel written; no existing document edited; README, REGISTRY, ERRATA and both pages unwritten; '
         'nothing here is a statement about RH, GRH, BSD, Navier–Stokes, twin primes, P versus NP or any zero beyond the compiled '
         'statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    put_json('b591_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE[:90]), title=TITLE, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, TITLE[:90]))


def trail():
    Q = _Q()
    S, fj, wl, e3, h = jl('b591_scores.json'), jl('b591_findings.json'), jl('b591_weight_line.json'), jl('b591_e3_line.json'), jl('b591_h32.json')
    te = g(TE, 'rev-parse', '--short=7', 'HEAD').strip()
    e0c = g(RELAY, 'log', '-1', '--format=%h', '--', 'tools/e0_rule.py').strip()
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows_ = ['', TRAIL_HEAD, '',
             '**(R201) ratified.** (1) b590 at its weight. (2) The witness ratio at W-ORD-DETECTION-REGION as (E3). (3) The E0 rule’s '
             'existential-binder clause. (4) The located-clause method document. (5) H32a-H32c. (6) The act after: the RESIDUE edition.', '',
             '**Entered:** FINDINGS.md:%d (b590’s weight), :%d (the entry); OPEN_TRAILS.md:%d ((E3)), this record; relay %s (the '
             'clause and its test, alone); TECHNE-Core %s (the document, alone, not pushed: %s, sha256 %s, body %d words).' % (
                 wl['line'], fj['entry_line'], e3['line'], e0c, te, DOC_REL, h['sha256'][:16], h['body']), '',
             '**Answered before the seal, by the author:** the document is written at TECHNE-Core `%s` beside the b257 drafts, '
             'committed alone locally and not pushed; **(R201)(4)’s path and its “promotion later” clause are struck as the '
             'navigator’s and recorded here**; the FINDINGS entry and this record carry the file’s name, word count, sha256 and '
             'location and no sentence of its body; the suite’s no-disclosure arm is extended to the body.' % DOC_REL, '',
             '**Recorded, found and not repaired:** the ζ page’s regeneration at PLACE-papers HEAD adds eleven Placement rows (the '
             'b578-b589 editions), and the χ page’s banked probe output leaves the three Schema declarations of b590 unresolved; '
             'G-CHAIN-PAGE and G-CHAIN-PAGE-CHI fail as sealed (relay data/b591_e0_regrade.txt); the clause moves no page byte.', '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R201)`(6), the RESIDUE edition by the form; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel written; no existing document edited; ERRATA untouched; '
             'FACES_LEDGER untouched; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; a transfer is '
             'proposed and carries no claim.', '']
    r = Q.append_to(Q.OT, NL.join(rows_))
    put_json('b591_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b591_trail.json')['line'])


def desk():
    S = jl('b591_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b591 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### (R201)(5)`S THREE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in ('H32a', 'H32b', 'H32c')]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)),
          '### ### **(R201)(5) : H32a %s ; H32b %s ; H32c %s.**' % (S['H32a'][0], S['H32b'][0], S['H32c'][0]), '']
    L += rd('b591_defects.txt').rstrip(NL).split(NL)
    put_txt('b591_desk_notes.txt', L)


def components():
    S, h, wl, e3, fj, tj, rg = (jl('b591_scores.json'), jl('b591_h32.json'), jl('b591_weight_line.json'), jl('b591_e3_line.json'),
                                jl('b591_findings.json'), jl('b591_trail.json'), jl('b591_e0_regrade.json'))
    te = g(TE, 'rev-parse', '--short=7', 'HEAD').strip()
    e0c = g(RELAY, 'log', '-1', '--format=%h', '--', 'tools/e0_rule.py').strip()
    L = ['b591 -- THE COMPONENTS, BANKED UNDER (R201).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b590`s closing push-out relay fd42f02b ; push-b590* branches deleted by '
         'name (data/b591_branches.txt) ; the kept branches untouched',
         '### COMPONENT 1 : b590`s weight FINDINGS :%d, the witness ratio a finding ; (E3) OPEN_TRAILS :%d ; the E0 clause relay %s, '
         'alone with its test (7 of 7) ; membership_load_bearing INTERFACES -> DERIVES, no grade moved ; census %d statements, %d '
         'reading moved ; pages: the clause moves no byte, both fail byte for byte against the committed (defect (a))' % (
             wl['line'], e3['line'], e0c, rg['census_n'], len(rg['moved'])),
         '### COMPONENT 2 : the document at TECHNE-Core %s (%s, not pushed), sha256 %s, body %d words, (vi) %d ; one correction before '
         'the seal ; %d Correspondence rows ; H32a %s, H32b %s, H32c %s' % (
             DOC_REL, te, h['sha256'][:16], h['body'], h['vi'], h['rows'], S['H32a'][0], S['H32b'][0], S['H32c'][0]),
         '### COMPONENT 3 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: the RESIDUE edition by the form ; '
         'N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b591_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b591_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
