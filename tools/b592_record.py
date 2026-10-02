# -*- coding: utf-8 -*-
"""b592_record.py -- THE ACT'S RECORD TOOL, UNDER (R202). ### ONE SUBCOMMAND PER BANK.

### ### b592: LANE THREE, ACT NINETEEN -- CP-7 ACT FOURTEEN: THE EDITION OF THE_RESIDUE_OF_RH BY THE FORM, THE §7 READING
### APPLIED; THE TWO PAGES REGENERATED AT v0.16; THE ARM-UNRUN STANDING LINE.
### Subcommands write only `data/b592_*` unless the docstring names another file. Every bank is written through `put_txt` /
### `put_json` (encode, temp file, `os.replace`). No platform call. The templates are b588_record.py and b591_record.py.
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
GSR = 'D:/SIDE-global-section'
EFK = 'D:/SIDE-explicit-formula'
LVK = 'D:/SIDE-lv-conservation'
PRE_PP = '9059169'
PRE_RELAY = '652b58d5'
STEPZERO = '24457265'
V016 = 'c404e727d7f7121b180318cca32eeb115452ed1b'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/f7dd7aec-e7f8-492c-a0db-31ef189124e6/scratchpad'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
CUR = 'phase1.5/proofs/THE_RESIDUE_OF_RH.md'
ED = 'phase1.5/proofs/THE_RESIDUE_OF_RH_v1_2.md'
WL = 'data/b558_editions/THE_RESIDUE_OF_RH.txt'
ARCH = 'archive/2026-08-24-ledger-split/OPEN_TRAILS-archive-2-historical-landings-and-programs.md'
NODES = {'zeta': 'b592_nodes.txt', 'chi': 'b592_nodes_chi.txt'}
PROBE = {'zeta': 'b592_probe_out.txt', 'chi': 'b592_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}

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


def _Q():
    import b566_record as R6
    return R6.Q


DEFECTS = [
    '(a) THE READS BANK`S FIRST RUN ASKED THE WORK-LIST FOR A LINE IT DOES NOT HAVE (:12 of an eleven-line file) and printed NO SUCH '
    'LINE; the range was corrected through the Edit tool and the bank re-written before any component used it.',
    '(b) BEFORE THE SEAL THE SEAT TOLD THE AUTHOR THAT THREE ζ CORRESPONDENCE ROWS GRADED INTERFACES WOULD GAIN THEIR PREMISES UNDER THE '
    'PREMISE CLAUSE; the regeneration prints two (pair_bound, li_identity_of_exchange). register3_of_one_lt_re`s source header reads no '
    'premise under the shared E0 rule, so the clause adds nothing to its row, as the clause says. The count put to the author was the '
    'seat`s, not measured.',
    '(c) THE GENERATOR TEST`S FIRST LABEL FOR CASE (8) PRINTED THE ζ LIST`S KEYSTONE COUNT, which the edition`s own commit changes, so the '
    'suite`s re-run would differ from the bank; the count was removed from the label through the Edit tool before the generator commit.',
    '(d) THE EDITION`S FIRST WRITE CARRIED BACKTICK POSSESSIVES IN FIVE BACK-MATTER CELLS ("§7`s", "author`s" twice, "season`s", '
    '"converse`s", "era`s"), which open stray code spans in a PLACE-papers table; the strings were corrected to ’ through the Edit tool '
    'and the uncommitted file re-written before the scan, the bank and the commit.',
    '(e) THE SCORES` FIRST RUN READ THREE PREDICATES WRONG: (S1) looked for "G-CHAIN-PAGE : FAIL" where the pre-run bank is a table; (S5) '
    'wanted the scanner`s live count to be 3 where the scanner counts the carried uses outside "live" (the face`s words are "CLEAN WITH '
    'EXACTLY THE THREE STEM USES CARRIED BY HISTORY"); (N5) swept every untracked relay data file of earlier acts into "written". Each '
    'was corrected through the Edit tool and the scores re-run before any record line used them; the first run is overwritten.',
    '(f) THE FIRST FINDINGS ENTRY AND TRAIL RECORD LEFT OUT THE GENERATOR`S TWO CLAUSES (the author`s answers 6 and 7, relay ac8257a5); '
    'both appends, uncommitted, were cut back to their banked "before" lengths (each a true prefix check against the bytes before it), '
    'the paragraph added through the Edit tool, and both re-appended at the same lines (:6780, :12196).',
]


def defects():
    put_txt('b592_defects.txt', ['### b592 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


# ================================================================================ READING (1): THE READS
RELAY = ROOT.replace('\\', '/')
READS = [
    ('relay the RESIDUE work-list, whole', RELAY, 'HEAD', WL, list(range(1, 12))),
    ('relay the CP-1b rows of THE_RESIDUE_OF_RH (1 MOVED, 6 STANDS, 0 CREDIT)', RELAY, 'HEAD', 'data/b558_cp1b.txt', [34] + list(range(309, 316))),
    ('PLACE-papers THE_RESIDUE_OF_RH: head, version line, §7, the standard table, the era annotations, the tier block, the appended lines',
     PP, PRE_PP, CUR, [1, 3, 9, 11, 17, 25] + list(range(71, 82)) + [88, 97, 108, 111, 132, 134, 147, 150, 152, 154, 184, 186, 188, 215, 228, 231, 234,
                                                                     240, 241, 243, 245, 247, 249, 251, 253]),
    ('PLACE-papers FINDINGS, b549`s §7 reading and b567`s', PP, PRE_PP, 'FINDINGS.md', [5655, 5665, 6212, 6214, 6218, 6760]),
    ('PLACE-papers OPEN_TRAILS, the form and its clauses', PP, PRE_PP, 'OPEN_TRAILS.md',
     [6642, 6764, 6766, 11864, 11902, 11904, 11906, 11908, 11930, 11932, 11934, 11954, 11956, 12044, 12172]),
    ('PLACE-papers the archived OPEN_TRAILS, the register pentagon', PP, PRE_PP, ARCH, [3476]),
    ('PLACE-papers the ζ page as it stands', PP, PRE_PP, PAGE, [1, 3, 12, 24, 25, 27, 28, 30, 32, 36, 41, 147]),
    ('PLACE-papers the χ page as it stands', PP, PRE_PP, DIR_PAGE, list(range(1, 4)) + list(range(22, 30))),
    ('PLACE-papers REGISTRY, the successor sentence', PP, PRE_PP, 'REGISTRY.md', [960]),
    ('relay the ζ node list (b569)', RELAY, 'HEAD', 'data/b569_nodes.txt', [1, 4]),
    ('relay the χ node list (b573)', RELAY, 'HEAD', 'data/b573_nodes_chi.txt', [6, 7, 25]),
    ('relay the generator`s head', RELAY, 'HEAD', 'tools/chain_page.py', [4, 22, 28, 30, 58, 444, 471, 517]),
    ('SIDE-explicit-formula v0.16 the detector', EFK, V016, 'SIDEExplicitFormula/Schema/Detector.lean', list(range(99, 103)) + [120]),
    ('SIDE-explicit-formula v0.16 the Epstein instance', EFK, V016, 'SIDEExplicitFormula/Schema/Epstein.lean', list(range(57, 60))),
    ('SIDE-explicit-formula v0.16 the residue`s own iff', EFK, V016, 'SIDEExplicitFormula/PageConverses.lean', [32, 33]),
    ('SIDE-explicit-formula v0.16 the discharge', EFK, V016, 'SIDEExplicitFormula/ResidueDischarge.lean', [41]),
    ('SIDE-lv-conservation v0.11.0 residue_irreducible', LVK, '2f71068', 'SIDELvConservation/ZeroActingPartial.lean', list(range(130, 141))),
    ('relay b591`s closing push-out, its head', RELAY, 'HEAD', 'data/b591_closing_push_out.txt', list(range(1, 6))),
]
SEARCH = 'sign-face registers'


def reads():
    L = ['b592 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev + '^{}').strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:400]))
    L += ['', '### THE b450 ITEM SEARCHED BY NAME ("%s", case-insensitive) in FINDINGS, OPEN_TRAILS and the archived ledgers @ %s:' % (SEARCH, PRE_PP)]
    hits = g(PP, 'grep', '-n', '-i', SEARCH, PRE_PP, '--', 'FINDINGS.md', 'OPEN_TRAILS.md', 'archive/').split(NL)
    hits = [h for h in hits if h.strip()]
    L += ['    %s' % h[:300] for h in hits] or ['    none']
    L.append('### hits : %d -- LOCATED: b454`s table row OPEN_TRAILS :6764 reads FOUND at the archive :3476 (the register pentagon); '
             'b450`s item OPEN_TRAILS :6642 (item 23, THE_RESIDUE_OF_RH "does not carry: the sign-face registers -- :181")' % len(hits))
    L += ['', '### THE DISCHARGE POINTER`S NAME, git grep at v0.16 (both declarations exist):']
    L += ['    %s' % x for x in g(EFK, 'grep', '-n', '-E', r'^theorem register4_positivity_liCoeff_(iff|imp)_rh', V016, '--', '*.lean').split(NL) if x.strip()]
    put_txt('b592_reads.txt', L)


# ================================================================================ COMPONENT 1: THE PAGES
def _page_lines(b):
    return b.decode('utf-8').split(NL)


def _placement(lines):
    return [l for l in lines if l.startswith('| keystone naming a node |')]


def pages_c1():
    """### the two full runs per page (scratchpad run one, PLACE-papers run two), compared byte for byte; the probe outputs banked;
    ### the Placement rows printed; the χ page`s last derived line against REGISTRY :960. Writes data/b592_page_runs.txt, the
    ### probe banks (b592_probe_out.txt, b592_chi_probe_out.txt, and their .lean.txt) and data/b592_pages.json."""
    import shutil
    L = ['### b592 -- (R202)(2): THE TWO PAGES REGENERATED AT v0.16 = c404e72 (relay tools/chain_page.py), EACH TWICE, FULL RUNS', '']
    J = {}
    reg = g(PP, 'show', 'HEAD:REGISTRY.md').split(NL)[959]
    for k in ('zeta', 'chi'):
        r1, r2 = os.path.join(SP, '%s_run1.md' % k), os.path.join(PP, PNAME[k])
        b1, b2 = open(r1, 'rb').read(), open(r2, 'rb').read()
        com = subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (PRE_PP, PNAME[k])], capture_output=True).stdout
        p1, p2 = os.path.join(SP, '%s1' % k, 'chain_page_probe_out.txt'), os.path.join(SP, '%s2' % k, 'chain_page_probe_out.txt')
        o1, o2 = open(p1, 'rb').read(), open(p2, 'rb').read()
        log1, log2 = io.open(os.path.join(SP, '%s_run1.log' % k), encoding='utf-8').read(), io.open(os.path.join(SP, '%s_run2.log' % k), encoding='utf-8').read()
        shutil.copyfile(p2, os.path.join(D, PROBE[k]))
        shutil.copyfile(os.path.join(SP, '%s2' % k, 'chain_page_probe.lean'), os.path.join(D, PROBE[k].replace('_out.txt', '.lean.txt')))
        a, c = _page_lines(com), _page_lines(b2)
        import difflib
        dl = [x for x in difflib.unified_diff(a, c, 'committed@%s' % PRE_PP, 'regenerated', lineterm='', n=0)]
        pl_old, pl_new = _placement(a), _placement(c)
        J[k] = dict(page=PNAME[k], nodes=NODES[k], identical=b1 == b2, probe_identical=o1 == o2, sha256=hashlib.sha256(b2).hexdigest(),
                    bytes=len(b2), committed_bytes=len(com), placement_old=len(pl_old), placement_new=len(pl_new),
                    added=[x for x in pl_new if x not in pl_old], gone=[x for x in pl_old if x not in pl_new], diff=dl,
                    nodes_n=len([l for l in c if re.match(r'^\d+\. `', l)]))
        L += ['### the %s page (%s), node list relay data/%s' % ('ζ' if k == 'zeta' else 'χ', PNAME[k], NODES[k]),
              '### run one (into the scratchpad):'] + ['    ' + x for x in log1.strip().split(NL)] + \
             ['### run two (into PLACE-papers):'] + ['    ' + x for x in log2.strip().split(NL)] + \
             ['### the two outputs: %s ; sha256 %s ; %d bytes ; nodes %d ; the two probe outputs %s' % (
                 'BYTE-IDENTICAL' if b1 == b2 else '### DIFFER', J[k]['sha256'], len(b2), J[k]['nodes_n'], 'byte-identical' if o1 == o2 else '### differ'),
              '### against the committed page @ %s (%d bytes): Placement rows %d -> %d ; added %d ; gone %d' % (
                  PRE_PP, len(com), len(pl_old), len(pl_new), len(J[k]['added']), len(J[k]['gone']))]
        L += ['    + ' + x for x in J[k]['added']] + ['    - ' + x for x in J[k]['gone']]
        L += ['### the unified diff against the committed page (n=0):'] + ['    ' + x[:300] for x in dl] + ['']
        if k == 'chi':
            ls = c
            i = ls.index('## Placement')
            last = [x for x in ls[:i] if x.strip()][-1]
            m = re.search(r"Supportable, the author's sentence: \*(.*?)\*", reg)
            sent = m.group(1) if m else None
            J[k]['last_line'] = last
            J[k]['registry_960'] = sent
            J[k]['last_eq_960'] = sent is not None and last == sent
            L += ['### the χ page`s last derived line (the line before its Placement heading), against REGISTRY :960`s sentence:',
                  '    page     : %s' % last[:400], '    REGISTRY : %s' % (sent or '### NOT FOUND')[:400],
                  '    ### %s' % ('BYTE FOR BYTE EQUAL' if J[k]['last_eq_960'] else 'DIFFER'), '']
            J[k]['corr'] = [x for x in ls if x.startswith('| `SIDEExplicitFormula.Schema.')]
            L += ['### the χ page`s Correspondence rows (the schema names):'] + ['    ' + x for x in J[k]['corr']] + ['']
    put_txt('b592_page_runs.txt', L)
    put_json('b592_pages.json', J)


def page_arms(tag):
    """### G-CHAIN-PAGE and G-CHAIN-PAGE-CHI run at PLACE-papers HEAD from the new lists and the v0.16 probe banks; counts printed.
    ### Writes data/b592_page_arms_<tag>.txt."""
    import g_chain_page as GCP
    L = ['### b592 -- THE TWO PAGE ARMS RUN AT PLACE-papers HEAD %s (%s), relay tools/g_chain_page.py, from-output' % (
        g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), tag)]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b592_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok']
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    put_txt('b592_page_arms_%s.txt' % tag, L)


def pages_c2():
    """### after the edition commit: each page re-emitted twice from its v0.16 probe bank (scratchpad, then PLACE-papers), the
    ### two byte-identical, the Placement-row diff against the Component 1 commit printed. Writes the two pages and
    ### data/b592_page_runs_c2.txt, data/b592_pages_c2.json."""
    import chain_page as C
    import difflib
    L = ['### b592 -- (R202)(2) and the author`s answer 2: THE PAGES RE-EMITTED AFTER THE EDITION COMMIT, TWICE EACH, FROM THE v0.16 PROBE BANKS', '']
    J = {}
    for k in ('zeta', 'chi'):
        outs = []
        for run, dest in ((1, os.path.join(SP, '%s_c2_run1.md' % k)), (2, os.path.join(PP, PNAME[k]))):
            rc, page, meta, log = C.build(os.path.join(D, NODES[k]), os.path.join(SP, '_b592_c2'), os.path.join(D, PROBE[k]))
            if rc:
                sys.exit('### %s RE-EMIT FAILED, exit %d: %s' % (k, rc, log[-3:]))
            b = page.encode('utf-8')
            open(dest + '.tmp', 'wb').write(b)
            os.replace(dest + '.tmp', dest)
            outs.append(b)
            L.append('### %s run %d -> %s (%d bytes)' % (k, run, dest, len(b)))
        prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + PNAME[k]], capture_output=True).stdout
        dl = [x for x in difflib.unified_diff(_page_lines(prev), _page_lines(outs[1]), 'HEAD', 'regenerated', lineterm='', n=0)]
        J[k] = dict(identical=outs[0] == outs[1], sha256=hashlib.sha256(outs[1]).hexdigest(), diff=dl, changed=prev != outs[1])
        L += ['### the two outputs: %s ; sha256 %s' % ('BYTE-IDENTICAL' if outs[0] == outs[1] else '### DIFFER', J[k]['sha256']),
              '### the diff against the page at PLACE-papers HEAD (n=0):'] + ['    ' + x[:300] for x in dl] + ['']
    put_txt('b592_page_runs_c2.txt', L)
    put_json('b592_pages_c2.json', J)


# ================================================================================ COMPONENT 1: THE RECORD LINES
B591_ENTRY = ('## The located-clause method: the open statement, the star of compiled equivalents, the surround classified, the ζ-leg as '
              'the worked instance, four transfers proposed')
B591_TRAIL = '### b591 — lane three, act eighteen under (R201)'


def weight_line():
    """### PLACE-papers FINDINGS: b591's weight, one appended line addressed to b591's entry."""
    Q = _Q()
    entry = Q.line_of(Q.FIND, B591_ENTRY)
    if entry != 6760:
        sys.exit('### THE ADDRESSED LINE MOVED: entry %s -- NOTHING WRITTEN' % entry)
    head = '*Appended 2026-10-02 by b592 to b591’s entry (:%d), under `(R202)`(1) -- b591 AT ITS WEIGHT:*' % entry
    Q.guard_absent(Q.FIND, head)
    text = ('\n%s THE_LOCATED_CLAUSE_METHOD.md at TECHNE-Core modules/2026-08/ beside the b257 drafts, 12e4176 local and unpushed: '
            'v0.1, 2026-10-02, sections (i)-(viii), 2,082 words of body, section (vi) 325 words, a 43-row Correspondence table every '
            'pin of which resolves, one ceiling correction in the seat’s own draft (a corpus line on the Epstein configuration beyond '
            'b590’s conclusion); H32a-H32c held; the no-disclosure arm passing; this entry and the trail carry name, location, word '
            'count and sha256 alone. The witness ratio at FINDINGS :6758 and (E3) at OPEN_TRAILS :12170, the closing item priced at '
            'b554’s C1-C2. The E0 existential-binder clause (relay 63424e13, 7 of 7) moves one reading of 1,564 (membership_load_bearing) '
            'and no grade. The suite read 64 of 66: the two page arms declared on the face failed, for causes outside that act’s '
            'changes -- the reason for the standing line of `(R202)`(3).\n' % head)
    r = Q.append_to(Q.FIND, text)
    put_json('b592_weight_line.json', dict(entry=entry, line=Q.line_of(Q.FIND, head), head=head, append=r))
    print('  weight line :%s' % Q.line_of(Q.FIND, head))


def standing_line():
    """### PLACE-papers OPEN_TRAILS: the standing line of (R202)(3), one appended line addressed to b591's record."""
    Q = _Q()
    at = Q.line_of(Q.OT, B591_TRAIL)
    if at != 12172:
        sys.exit('### THE ADDRESSED LINE MOVED: %s -- NOTHING WRITTEN' % at)
    head = ('*Appended 2026-10-02 by b592 to b591’s record (:%d), under the author’s ruling `(R202)`(3) -- THE ARM-UNRUN STANDING '
            'LINE:*' % at)
    Q.guard_absent(Q.OT, head)
    text = ('\n%s no arm is declared on a face before it has been run at HEAD in the same session and its count printed; a page arm '
            'is run after every kernel tag before the next face is sealed. The occasion is b591’s defect (a): the face declared '
            'G-CHAIN-PAGE and G-CHAIN-PAGE-CHI without running them at HEAD, and both failed as sealed (relay data/b591_defects.txt). '
            'Applied first at b592, whose suite was run at HEAD before its face was sealed (relay data/b592_arms_prerun.txt).\n' % head)
    r = Q.append_to(Q.OT, text)
    put_json('b592_standing_line.json', dict(addressed=at, line=Q.line_of(Q.OT, head), head=head, append=r))
    print('  standing line :%s' % Q.line_of(Q.OT, head))


# ================================================================================ COMPONENT 2: THE EDITION
EF = 'SIDE-explicit-formula'
PIN = {'h2_sign_iff_rh': 'v0.2 = `5c72cad`', 'li_nonneg_iff_rh': 'v0.9 = `e5a5a83`', 'arith_limit_nonneg_iff_rh': 'v0.9 = `e5a5a83`',
       'register4_positivity_liCoeff_iff_rh': 'v0.11 = `19b7d1e`'}
FQ = {'h2_sign_iff_rh': 'SIDEExplicitFormula.B321.h2_sign_iff_rh', 'li_nonneg_iff_rh': 'SIDEExplicitFormula.LiCriterionBridge.li_nonneg_iff_rh',
      'arith_limit_nonneg_iff_rh': 'SIDEExplicitFormula.LiCriterionBridge.arith_limit_nonneg_iff_rh',
      'register4_positivity_liCoeff_iff_rh': 'SIDEExplicitFormula.PageConverses.register4_positivity_liCoeff_iff_rh'}
WHERE = {'h2_sign_iff_rh': ('Seam.lean:101', 12, 8), 'li_nonneg_iff_rh': ('LiCriterionBridge.lean:179', 24, 20),
         'arith_limit_nonneg_iff_rh': ('LiCriterionBridge.lean:191', 25, 21), 'register4_positivity_liCoeff_iff_rh': ('PageConverses.lean:32', 28, 24)}
FOUR = ('`h2_sign_iff_rh` (%s v0.2 = `5c72cad`), `li_nonneg_iff_rh` (v0.9 = `e5a5a83`) with `register4_positivity_liCoeff_iff_rh` '
        '(v0.11 = `19b7d1e`) and `arith_limit_nonneg_iff_rh` (v0.9 = `e5a5a83`)' % EF)
OLD_132 = ('| ### **`h2`, the one open premise** | ### **NONE** | — | — | ### **MANUSCRIPT-RESIDENT** — monograph §27.3, register 4 | '
           '### **read §27.3; no terminal** |')
NEW_132 = ('| ### **`h2`, the one open premise, in its Weil form `h2_sign`** | `SIDE-explicit-formula` v0.2 = `5c72cad` | '
           '`SIDEExplicitFormula.B321.h2_sign_iff_rh` (the ζ page, node 8, line 12) | `{propext, Classical.choice, Quot.sound}` | '
           '### **OPEN** — the premise `h2_sign` has a terminal and is open, and its equivalence to Mathlib\'s `RiemannHypothesis` is the '
           'compiled theorem `h2_sign_iff_rh` (monograph §27.3, register 4) | `#check` and `#print axioms` of `h2_sign_iff_rh` at v0.2 |')
OLD_77 = ('- **only the conjunction is RH** — the full object, both clauses jointly over the ζ-zeros, implies RH through the named classical '
          'premises (the Weil-criterion direction; Li\'s criterion).')
NEW_77 = ('- **the conjunction implies RH, and clause 2 in full is RH** — the full object, both clauses jointly over the ζ-zeros, implies RH '
          'through the named classical premises (the Weil-criterion direction; Li\'s criterion, discharged at λ := `LiCoeff`), while clause 2 '
          'taken for every `n` is RH by three compiled faces beside this theorem, each equivalent to Mathlib\'s `RiemannHypothesis` — Weil '
          'positivity on classK by `h2_sign_iff_rh` (%s v0.2 = `5c72cad`), Li positivity by `li_nonneg_iff_rh` (v0.9 = `e5a5a83`), in the '
          'residue\'s own vocabulary `register4_positivity_liCoeff_iff_rh` (v0.11 = `19b7d1e`), and arithmetic-limit positivity by '
          '`arith_limit_nonneg_iff_rh` (v0.9 = `e5a5a83`) — and clause 1 is a candidate supplier of that positivity and not a separate '
          'necessity.' % EF)
OLD_79A = 'Neither clause alone is hard; their join is the whole of RH.'
NEW_79A = ('Neither clause alone is hard while clause 2 stops at the threshold; clause 2 in full is RH by %s, and clause 1 is a candidate '
           'supplier of it.' % FOUR)
OLD_79B = 'the difficulty is located exactly at the conjunction.'
NEW_79B = 'the difficulty is located in clause 2 in full, which is RH by the faces cited above, the conjunction implying RH.'
OLD_88 = '`residue_irreducible` is the first *compiled* instance of difficulty located at a conjunction of individually-free clauses.'
NEW_88 = ('`residue_irreducible` is the first *compiled* instance of a conjunction of individually-free clauses that implies RH, its difficulty '
          'located in clause 2 in full, which is RH by %s, and clause 1 a candidate supplier.' % FOUR)
WORKLIST = [(132, OLD_132, NEW_132)]
RULED = [(77, OLD_77, NEW_77), (79, OLD_79A, NEW_79A), (79, OLD_79B, NEW_79B), (88, OLD_88, NEW_88)]
RULED_WHY = {77: '(R202)(4): §7’s conjunction sentence, the (R177)(5) reading (FINDINGS :6218)',
             79: 'the author’s answers 3 and 5 before the seal: the marked reading extended to an unmarked sentence restating the same claim',
             88: 'the author’s answer 3 before the seal: the marked reading extended to an unmarked sentence restating the same claim'}
CREDIT = (77, '*Credit (b450 item, located at b592): the sign-face registers -- located by name at OPEN_TRAILS :6764 (b454\'s table, '
              'FOUND) and held at `%s` :3476, carried since b454 by the era annotation of v1.1 :184 -- the register pentagon, the five '
              'faces compiled as a structure, R4 the sign face and R5 the realization face, the cross-register equivalences deliberately '
              'not claimed; read against the clauses above, clause 2 is the sign face R4, whose positivity in full is RH by the compiled '
              'faces cited there, and clause 1 is the realization face R5, a candidate supplier of it, no equivalence between the two '
              'registers being claimed.*' % ARCH)
HIST = [(136, 134, '*History line, 2026-10-02 (v1.2, b592): the dated annotation above carries its 2026-08-12 wording as the record; the '
                   'object its last sentence names is a blank cell -- every row that has no kernel says so in words rather than leaving a '
                   'blank cell.*'),
        (154, 152, '*History line, 2026-10-02 (v1.2, b592): the dated annotation above carries its 2026-08-12 wording as the record; the '
                   'objects its last sentence names are missing information and a question of language -- the residue is not missing '
                   'information but a question of language, how a structure valid only on `Re s > 1` speaks about `Re s = 1/2`.*')]
VERSION = (17, '*v1.2 — 2026-10-02 (CP-7 edition (b592), written beside v1.1, which is unedited; its back matter closes the file)*')
CEILING = re.compile(r'\bprov(?:e|ed|en|es|ing)\b|\bproof\b|\bestablish\w*|RH proved|proves RH|RH-route|end-to-end|the whole of RH|only the conjunction is RH')
CARRIED = {
    21: 'negated: the record "is not a proof of RH and claims none"',
    23: 'negated: the disclaimer "Nothing in this record is proven on the zeros"',
    67: 'the chiasmus, which `(R202)`(4) has STAND as a reading: "proved" and "proves" there are the sign season’s and the inverse-spectral '
        'converse’s own results (positivity free without the zeros; the operator free given the positivity), not RH or the zeros',
    69: 'the era’s reading: "proved" names the settings where line-confinement is proved (function fields), not the ζ-zeros',
    73: '"establishes" introduces the conjuncts `residue_irreducible` compiles under its named premises (lv v0.11.0 = `2f71068`, '
        'ZeroActingPartial.lean :130); the three faces of :%d are attributed in that clause to the theorems beside it',
    81: 'negated: "Nothing here is proven on the zeros"',
    91: 'negated: "not proven-absence"',
}
BM_TAG = '<!-- b592 (R202) THE v1.2 EDITION`S BACK MATTER, 2026-10-02 -->'
OFFSET = ('+2 from :17 (the v1.2 line and a blank, above the v1.1 line); +2 more from :78 (a blank and the credit line, beneath :77); '
          '+2 more from :137 (a blank and the history line, beneath :136); +2 more from :155 (a blank and the history line, beneath '
          ':154) -- v1.1 :n sits at the edition`s :n for n < 17, :n+2 for 17 <= n <= 77, :n+4 for 78 <= n <= 136, :n+6 for 137 <= n <= 154 '
          'and :n+8 for n >= 155')
LV = ('`residue_irreducible`', 'SIDE-lv-conservation', 'v0.11.0 = `2f71068`', 'SIDELvConservation/ZeroActingPartial.lean :130')


def _segs(l):
    import b558_record as CP
    return [s for s in CP.segments(l) if s]


def _count(lines):
    return sum(len(_segs(l)) for l in lines)


def _cur():
    cur = g(PP, 'show', '%s:%s' % (PRE_PP, CUR)).split(NL)
    return cur[:-1] if cur and cur[-1] == '' else cur


def _edl(n):
    return n + (2 if n >= VERSION[0] else 0) + (2 if n > CREDIT[0] else 0) + sum(2 for a, _s, _t in HIST if n > a)


def _all_changes():
    return WORKLIST + RULED


def _status_blanks(lines):
    import b579_record as R9
    return R9._status_blanks(lines)


def edition(*a):
    """### PLACE-papers phase1.5/proofs/THE_RESIDUE_OF_RH_v1_2.md, beside the current version from its blob at 9059169; the re-pin
    ### step last. Writes the edition file and data/b592_edition.json."""
    cur = _cur()
    if g(PP, 'rev-parse', 'HEAD:' + CUR).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip():
        sys.exit('### THE CURRENT VERSION MOVED SINCE 9059169 -- NOTHING WRITTEN')
    edp = os.path.join(PP, *ED.split('/'))
    if os.path.exists(edp) and 'again' not in a:
        sys.exit('### THE EDITION FILE EXISTS -- NOTHING WRITTEN')
    if g(PP, 'ls-files', ED).strip():
        sys.exit('### THE EDITION FILE IS COMMITTED -- NOTHING WRITTEN')
    new = list(cur)
    for ln, old, rep in _all_changes():
        line = new[ln - 1]
        if line.count(old) != 1:
            sys.exit('### :%d -- THE FRAGMENT IS NOT ON ITS LINE EXACTLY ONCE (%d): %s' % (ln, line.count(old), old[:80]))
        n0 = len(_segs(line))
        new[ln - 1] = line.replace(old, rep)
        if len(_segs(new[ln - 1])) != n0:
            sys.exit('### :%d -- THE CHANGE ALTERED THE LINE`S SEGMENT COUNT %d -> %d' % (ln, n0, len(_segs(new[ln - 1]))))
    if not cur[VERSION[0] - 1].startswith('*v1.1 — 2026-07-27'):
        sys.exit('### THE VERSION ANCHOR IS NOT WHERE THE FACE SAYS')
    if not cur[CREDIT[0] - 1].startswith('- **only the conjunction is RH**'):
        sys.exit('### THE CREDIT ANCHOR IS NOT WHERE THE FACE SAYS')
    if not cur[135].startswith('> ### **THE STATUS THE EXISTING TABLE') or not cur[133].startswith('> ### **0 BLANK CELLS') \
            or not cur[153].startswith('*Provenance: `phase2/method/THE_EULER_SPECIFICATION.md`') or not cur[151].startswith('> **A sixth specification'):
        sys.exit('### A HISTORY ANCHOR IS NOT WHERE THE FACE SAYS')
    for t in [CREDIT[1], VERSION[1]] + [h[2] for h in HIST]:
        if len(_segs(t)) != 1:
            sys.exit('### AN INSERTED LINE IS NOT ONE SENTENCE (%d): %s' % (len(_segs(t)), t[:60]))
    import banned_terms as BT
    for t in [CREDIT[1], VERSION[1]] + [h[2] for h in HIST] + [x[2] for x in _all_changes()]:
        if BT.PAT.search(t):
            sys.exit('### A BANNED STEM IN AN INSERTED OR REWRITTEN TEXT: %s' % t[:80])
    rows = [r for r in jl('b558_cp1b.json')['rows'] if r['doc'] == 'RESIDUE' and r['verdict'] == 'MOVED-IN-MEANING']
    diff = []
    for r in rows:
        ln = r['line']
        k = _segs(cur[ln - 1]).index(r['sentence'])
        nw = _segs(new[ln - 1])[k]
        cites = [d for d in PIN if ('`%s`' % d) in nw and PIN[d].split(' = ')[1] in nw]
        diff.append(dict(id=r['id'], line=ln, ed_line=_edl(ln), terminal=r['terminal'], old=r['sentence'], new=nw, changed=nw != r['sentence'],
                         cites=cites, supports=r['reading'], kind='work-list'))
    for ln, old, rep in RULED:
        cites = [d for d in PIN if ('`%s`' % d) in rep]
        diff.append(dict(id='ruled:%d' % ln, line=ln, ed_line=_edl(ln), terminal='(R177)(5) reading', old=old, new=rep, changed=True, cites=cites,
                         supports=RULED_WHY[ln], kind='ruled'))
    for after, _s, t in sorted(HIST, reverse=True):
        new[after:after] = ['', t]
    new[CREDIT[0]:CREDIT[0]] = ['', CREDIT[1]]
    new[VERSION[0] - 1:VERSION[0] - 1] = [VERSION[1], '']
    body = list(new)
    changed = set(x[0] for x in _all_changes())
    if any(_edl(n) > len(body) or (n not in changed and body[_edl(n) - 1] != cur[n - 1]) for n in range(1, len(cur) + 1)):
        sys.exit('### OFFSET MODEL DOES NOT CARRY THE CURRENT VERSION')
    if body[_edl(CREDIT[0]) + 1] != CREDIT[1] or body[_edl(VERSION[0]) - 3] != VERSION[1]:
        sys.exit('### AN INSERTION IS NOT WHERE THE FACE SAYS')
    for after, _s, t in HIST:
        if body[_edl(after) + 1] != t:
            sys.exit('### A HISTORY LINE IS NOT BENEATH :%d' % after)
    inv = {_edl(n): n for n in range(1, len(cur) + 1)}
    hits = [(i, m.group(0)) for i, l in enumerate(body, 1) for m in CEILING.finditer(l)]
    stray = sorted(set(inv.get(i, -i) for i, _ in hits) - set(CARRIED) - changed)
    if stray:
        sys.exit('### A CEILING HIT IN THE BODY IS NEITHER REWRITTEN NOR CARRIED BY THE SEAT`S READ: current lines %s' % stray)
    cl = _edl(CREDIT[0]) + 2
    hl = {s: _edl(a) + 2 for a, s, _t in HIST}
    bm = ['', BM_TAG, '',
          '## Back matter of the v1.2 edition -- written 2026-10-02 by b592 under the author’s ruling `(R202)`(4), by the form of `(R187)`(5)', '',
          '*This file is v1.2 of THE_RESIDUE_OF_RH, the CP-7 edition written beside v1.1 (`%s`, unedited) from v1.1’s tier block (its :215, '
          'standing: 24 terminals, T1-lit 7, T2 17, the h2 row MOVED to `h2_sign`) and its CP-1b work-list (relay `%s`), the ζ page as its '
          'spine; it does not deposit and does not replace v1.1, and its promotion is CP-8’s. Every line cited below is this file’s own.*' % (CUR, WL), '',
          '### Removals', '', 'None: the work-list’s one row resolves to a row rewritten in place to what its compiled fact says.', '',
          '### Rewrites', '', '| this edition’s line | v1.1 wording | v1.2 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in WORKLIST:
        bm.append('| :%d | %s | %s | rewritten: the work-list’s MOVED-IN-MEANING row (h2 takes `h2_sign`, citing `h2_sign_iff_rh` at v0.2) |' % (_edl(ln), old.replace('|', '¦'), rep.replace('|', '¦')))
    for ln, old, rep in RULED:
        bm.append('| :%d | %s | %s | rewritten by the `(R177)`(5) reading: %s |' % (_edl(ln), old, rep, RULED_WHY[ln]))
    bm += ['', '### Credit lines', '', '| this edition’s line | the item | Status |', '|:--|:--|:--|',
           '| :%d | the sign-face registers (b450, OPEN_TRAILS :6642 item 23), located by name at OPEN_TRAILS :6764 and the archive :3476 | '
           'inserted beneath :%d, the §7 clause whose claim it corrects, under the placement clause (OPEN_TRAILS :11956) |' % (cl, _edl(CREDIT[0])), '',
           '### Stem uses carried by history', '', '| this edition’s history line | the dated entry | the stem’s line | Status |', '|:--|:--|:--|:--|',
           '| :%d | the CORRESPONDENCE AT THE STANDARD annotation of 2026-08-12 | :%d, carried-by-history | inserted under the history clause '
           '(OPEN_TRAILS :11908, :12044), the author’s answer before b592’s seal that an era annotation is a dated history entry |' % (hl[134], _edl(134)),
           '| :%d | the ERA ANNOTATION of 2026-08-12, bearing on the residue’s statement | :%d, carried-by-history | inserted under the history '
           'clause, as above |' % (hl[152], _edl(152)), '',
           '### Ceiling corrections', '', 'None: every ceiling-shaped sentence of the body is read below and carried, or is a rewrite above.', '',
           '### Ceiling-shaped sentences read and carried', '', '| this edition’s line | the seat’s read | Status |', '|:--|:--|:--|']
    for ln in sorted(CARRIED):
        bm.append('| :%d | ceiling read, carried: %s | carried as read |' % (_edl(ln), CARRIED[ln] % _edl(77) if '%d' in CARRIED[ln] else CARRIED[ln]))
    bm += ['', '### Fact corrections', '', 'None: every pin, toolchain and count the body states agrees with the seat’s printed read (relay `data/b592_reads.txt`).', '',
           '### The navigator’s expectations of `(R202)`(4), and the author’s answers', '', '| expectation | the read | Status |', '|:--|:--|:--|',
           '| §7’s conjunction sentence rewritten by the `(R177)`(5) reading | :%d, citing the three faces and `register4_positivity_liCoeff_iff_rh` | rewritten |' % _edl(77),
           '| the reading extended to the unmarked sentences restating the same claim (the author’s answers 3 and 5) | :%d (two sentences), :%d | rewritten; '
           ':%d’s third sentence (the residue as a self-adjoint operator realizing the zeros, the conjunction of two clauses each met apart) carries as the '
           'realization form of the residue |' % (_edl(79), _edl(88), _edl(79)),
           '| `residue_irreducible` keeps its grade in lv with the discharge pointer | the b567 line, :%d, carried unchanged; :%d cites `register4_positivity_liCoeff_iff_rh` | carried |' % (_edl(253), _edl(77)),
           '| the b450 sign-face-registers item located by name and credited | located at OPEN_TRAILS :6764 / the archive :3476 | credited at :%d |' % cl,
           '| the chiasmus and the “space is the wall” compression stand as readings | :%d | carried |' % _edl(67),
           '| the rigid threshold N₀(T) ≈ 2T² stands | :%d’s second sentence; its compiled part `detection_threshold_mono` T2 (tier block :%d), its rigidity '
           'under mollifiers with no terminal | carried |' % (_edl(79), _edl(231)),
           '| the Selberg and de Branges sentences stand as field context | :%d, :%d | carried |' % (_edl(64), _edl(65)),
           '| “proved” phrasings about the conjunction or the zeros take the ceiling clause | every hit read above; none corrected | carried as read |',
           '| the appended correspondence line of b567 carries | :%d | carried |' % _edl(253), '',
           '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
           '| this edition, v1.2 | `%s` | written at b592 |' % ED,
           '| the current version, v1.1 | `%s` | unedited |' % CUR,
           '| the spine | `%s`, regenerated at SIDE-explicit-formula v0.16 = `c404e72` by b592 | read |' % PAGE,
           '| the work-list | relay `%s` | read |' % WL,
           '| the sentence-by-sentence diff | relay `data/b592_edition_RESIDUE.txt` | banked at b592 |', '',
           '### Correspondence', '',
           '| declaration | repository | pin | the source line, and the ζ page’s line | Status |', '|:--|:--|:--|:--|:--|']
    ed_lines = {d: [i for i, l in enumerate(body, 1) if ('`%s`' % d) in l] for d in PIN}
    for d in PIN:
        src, pl, node = WHERE[d]
        bm.append('| `%s` | %s | %s | `SIDEExplicitFormula/%s`; the ζ page, node %d, line %d | cited at :%s of this edition |' % (
            FQ[d], EF, PIN[d].replace('`', ''), src, node, pl, ', :'.join(str(x) for x in ed_lines[d]) or '### NONE'))
    lv_lines = [i for i, l in enumerate(body, 1) if LV[0] in l]
    bm.append('| %s | %s | %s | `%s`; the ζ page’s Correspondence row | named at :%s of this edition |' % (
        LV[0], LV[1], LV[2].replace('`', ''), LV[3], ', :'.join(str(x) for x in lv_lines[:6]) + (', …' if len(lv_lines) > 6 else '')))
    bm.append('')
    if any('### NONE' in l for l in bm):
        sys.exit('### A CORRESPONDENCE ROW CITES NO LINE OF THE EDITION')
    full = body + bm
    b = (NL.join(full) + NL).encode('utf-8')
    open(edp + '.tmp', 'wb').write(b)
    os.replace(edp + '.tmp', edp)
    print('  written: %s (%d bytes, %d lines)' % (ED, len(b), len(full)))
    n_cur, n_body, n_full = _count(cur), _count(body), _count(full)
    put_json('b592_edition.json', dict(path=ED, cur=CUR, cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip(),
                                       lines_cur=len(cur), lines_body=len(body), lines_full=len(full),
                                       n_cur=n_cur, n_body=n_body, n_full=n_full, n_backmatter=n_full - n_body,
                                       credit=1, removals=0, ruled_citations=len(HIST), ruled_rewrites=len(RULED), version_lines=1, diff=diff,
                                       offset=OFFSET, worklist=WORKLIST, ruled=RULED, hist=[list(h) for h in HIST],
                                       credit_line=dict(after=CREDIT[0], at=cl, text=CREDIT[1]), hist_at=hl,
                                       carried={str(k): v for k, v in CARRIED.items()}, version=dict(above=VERSION[0], text=VERSION[1]),
                                       sha256=hashlib.sha256(b).hexdigest(), status_blanks=_status_blanks(full), cited_lines=ed_lines))
    print('  counts: current %d ; body %d ; whole %d ; back matter %d' % (n_cur, n_body, n_full, n_full - n_body))


def edition_bank():
    """### The diff with its offset line, the corrections, the counts, the ceiling read, the scanner's verdict, H28a-H28c."""
    E = jl('b592_edition.json')
    edp = os.path.join(PP, *ED.split('/'))
    ed = io.open(edp, encoding='utf-8').read().replace(chr(13), '').split(NL)
    if ed and ed[-1] == '':
        ed = ed[:-1]
    cut = ed.index(BM_TAG)
    scan = rd('b592_edition_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    hist_n = re.search(r'carried-by-history (\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    carried_ed = set(_edl(n) for n in CARRIED)
    rewritten_ed = set(_edl(x[0]) for x in _all_changes())
    hits = []
    for i, l in enumerate(ed, 1):
        for m in CEILING.finditer(l):
            kind = ('record' if (i > cut and l.startswith('| ')) else 'carried' if (i < cut and i in carried_ed)
                    else 'rewritten' if (i < cut and i in rewritten_ed) else 'beyond')
            hits.append(dict(line=i, hit=m.group(0), kind=kind, ctx=l[max(0, m.start() - 60):m.end() + 40]))
    beyond = [h for h in hits if h['kind'] == 'beyond']
    wl = [d for d in E['diff'] if d['kind'] == 'work-list']
    h28a_bad = [d['id'] for d in wl if not d['changed'] or not d['cites']]
    h28a = 'HELD' if not h28a_bad else 'REFUTED'
    body_dn = E['n_body'] - E['n_cur']
    allowed = E['credit'] + E['removals'] + E['ruled_citations'] + E['version_lines']
    h28b = 'HELD' if abs(body_dn) <= allowed else 'REFUTED'
    live_n = int(live.group(1)) if live else None
    h28c = 'HELD' if (clean and not beyond) else 'REFUTED'
    cur0 = _cur()
    L = ['### OFFSET FROM THE CURRENT VERSION (R190)(3): %s -- every edition line below is the final file`s own.' % OFFSET, '',
         'b592 -- COMPONENT 2: THE EDITION OF THE_RESIDUE_OF_RH, (R202)(4), BY THE FORM OF (R187)(5) AND ITS CLAUSES', '',
         '### the current version : PLACE-papers %s @ %s (blob %s), %d lines ; head :1 "%s" ; :17 "%s"' % (
             CUR, PRE_PP, E['cur_blob'][:8], E['lines_cur'], cur0[0], cur0[16][:90]),
         '### its §7 : :71-:81 ("%s" .. "%s")' % (cur0[70][:60], cur0[80][:60]),
         '### its tier block : :215 "%s" ; the totals :234 "%s"' % (cur0[214][:90], cur0[233][:90]),
         '### the b567 appended correspondence line : :253 "%s"' % cur0[252][:120],
         '### its version history : the version line :17 (v1.1, 2026-07-27; HELD_RESIDUE_v1_1.md drafted it over v1.0); the dated annotations '
         ':119-:147, :150-:154, :160-:168, :172-:211; the tier block :215-:247; the appended lines :249, :251, :253',
         '### the b450 item searched by name (relay data/b592_reads.txt): the sign-face registers -- LOCATED at OPEN_TRAILS :6764 (b454`s table) '
         'and the archive :3476',
         '### the edition : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines_full'], E['sha256']), '',
         '### THE WORK-LIST, ROW BY ROW (1 row), AND THE RULED REWRITES (%d sentences on 3 lines):' % len(RULED), '']
    for d in E['diff']:
        L += ['  %s v1.1 :%d -> v1.2 :%d `%s` -- %s ; cites %s' % (d['id'], d['line'], d['ed_line'], d['terminal'], d['kind'],
                                                                   ['%s (%s)' % (c, PIN[c].replace('`', '')) for c in d['cites']]),
              '      answers: %s' % d['supports'], '      v1.1 : %s' % d['old'], '      v1.2 : %s' % d['new'], '']
    L += ['### THE CREDIT LINE: v1.2 :%d, beneath v1.1 :77' % E['credit_line']['at'], '      %s' % E['credit_line']['text'], '',
          '### THE HISTORY LINES (the history clause, the author`s answer 4):']
    for a, s, t in HIST:
        L += ['    v1.2 :%d, beneath v1.1 :%d (the stem`s line v1.1 :%d -> v1.2 :%d, carried-by-history)' % (E['hist_at'][str(s)], a, s, _edl(s)), '      %s' % t]
    L += ['### THE CEILING CORRECTIONS: none.', '### THE CEILING-SHAPED SENTENCES READ AND CARRIED:'] + \
         ['    v1.1 :%d -> v1.2 :%d  %s' % (n, _edl(n), (CARRIED[n] % _edl(77)) if '%d' in CARRIED[n] else CARRIED[n]) for n in sorted(CARRIED)]
    L += ['### THE STEM CORRECTIONS: none in place; the three uses at v1.1 :134 and :152 carried by history.',
          '### THE FACT CORRECTIONS: none.', '### REMOVALS: none.',
          '### THE VERSION LINE: above v1.1 :%d: %s' % (E['version']['above'], E['version']['text']), '',
          '### THE COUNTS (relay tools/b558_record.py `segments`, imported): the current version %d ; the edition`s body %d (%+d) ; the back '
          'matter %d ; the edition whole %d' % (E['n_cur'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + ruled citations %d (the two history lines; the four '
          'ruled rewrites keep their lines` counts) + one version line = %d' % (body_dn, E['credit'], E['removals'], E['ruled_citations'], allowed),
          '### no blank Status cell: %s' % ('HELD' if not E['status_blanks'] else '### BLANK AT %s' % E['status_blanks']), '',
          '### THE CEILING, every hit in the edition:']
    L += ['    :%d "%s" -- %s -- ...%s...' % (h['line'], h['hit'], {'record': 'quoted in a back-matter row, read by the seat',
                                                                 'carried': 'in a sentence the seat read and carried',
                                                                 'rewritten': 'in a sentence rewritten in place',
                                                                 'beyond': '### BEYOND THE CEILING'}[h['kind']], h['ctx']) for h in hits] or ['    none']
    L += ['### sentences beyond the ceiling: %d' % len(beyond),
          '### THE SCANNER (banned_terms.py --new) on the edition: live uses %s, carried-by-history %s ; verdict %s' % (
              live_n, hist_n.group(1) if hist_n else None, 'CLEAN' if clean else 'NOT CLEAN'), '',
          '### ### **H28a %s -- every MOVED row resolves to a sentence citing a declaration on the page at its pin%s.**' % (
              h28a, '' if not h28a_bad else ' -- refuted at %s' % h28a_bad),
          '### ### **H28b %s -- final form: the body differs by %+d sentences against at most %d; the back matter %d, excluded and '
          'printed.**' % (h28b, body_dn, allowed, E['n_backmatter']),
          '### ### **H28c %s -- the scanner`s verdict %s (live uses carried by history %s); sentences beyond the ceiling %d.**' % (
              h28c, 'CLEAN' if clean else 'NOT CLEAN', hist_n.group(1) if hist_n else None, len(beyond)),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**']
    put_txt('b592_edition_RESIDUE.txt', L)
    put_json('b592_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, h28a_bad=h28a_bad, body_dn=body_dn, allowed=allowed,
                                   backmatter=E['n_backmatter'], live=live_n, history=int(hist_n.group(1)) if hist_n else None, clean=clean,
                                   beyond=len(beyond), hits=hits, held=None, n_ceils=0, n_facts=0, n_ruled=len(RULED)))
    H = jl('b592_h28.json')
    print(H['H28a'], H['H28b'], H['H28c'], 'body_dn', body_dn, 'allowed', allowed, 'beyond', H['beyond'], 'live', H['live'], 'history', H['history'])


def repin():
    """### THE RE-PIN STEP, THE FORM'S LAST (OPEN_TRAILS :11932): every line the back matter and the diff bank cite is re-read
    ### against the final file and must carry what the citation says. Writes data/b592_repin.txt."""
    E = jl('b592_edition.json')
    ed = io.open(os.path.join(PP, *ED.split('/')), encoding='utf-8').read().replace(chr(13), '').split(NL)
    cut = ed.index(BM_TAG)
    checks = []
    for d in E['diff']:
        checks.append(('diff %s -> :%d carries the v1.2 wording' % (d['id'], d['ed_line']), d['new'] in ed[d['ed_line'] - 1]))
    checks.append(('credit :%d is the credit line' % E['credit_line']['at'], ed[E['credit_line']['at'] - 1] == CREDIT[1]))
    for a, s, t in HIST:
        checks.append(('history line :%d beneath v1.1 :%d' % (E['hist_at'][str(s)], a), ed[E['hist_at'][str(s)] - 1] == t))
        checks.append(('the stem`s line :%d is v1.1 :%d unchanged' % (_edl(s), s), ed[_edl(s) - 1] == _cur()[s - 1]))
    for n in CARRIED:
        checks.append(('carried :%d holds a ceiling-shaped hit' % _edl(n), CEILING.search(ed[_edl(n) - 1]) is not None))
    for d, ls in E['cited_lines'].items():
        for x in ls:
            checks.append(('Correspondence: `%s` on :%d' % (d, x), ('`%s`' % d) in ed[x - 1] and x < cut))
    checks.append(('version line above the v1.1 line', ed[_edl(VERSION[0]) - 3] == VERSION[1]))
    bm = NL.join(ed[cut:])
    for n in sorted(set(int(x) for x in re.findall(r'\| :(\d+) \|', bm))):
        checks.append(('back-matter row :%d is a body line' % n, 0 < n < cut and ed[n - 1].strip() != ''))
    bank = rd('b592_edition_RESIDUE.txt')
    checks.append(('the diff bank`s head states the offset once', bank.startswith('### OFFSET FROM THE CURRENT VERSION') and bank.count('### OFFSET FROM') == 1))
    checks.append(('the diff bank names the final file`s sha256', E['sha256'] in bank and hashlib.sha256(
        open(os.path.join(PP, *ED.split('/')), 'rb').read()).hexdigest() == E['sha256']))
    L = ['### b592 -- THE RE-PIN STEP (OPEN_TRAILS :11932), RUN LAST: every cited line re-read against the final file %s' % ED, '']
    L += ['    %-90s %s' % (w[:90], 'OK' if ok else '### FAILS') for w, ok in checks]
    L += ['', '### ### **RE-PIN : %d of %d citations hold against the final file.**' % (sum(ok for _w, ok in checks), len(checks))]
    put_txt('b592_repin.txt', L)


# ================================================================================ COMPONENT 3: THE FORM LINES AND THE RECORD
FORM = '*Appended 2026-10-01 by b577, under the author’s ruling `(R187)`(5)–(6), to the critical path’s lane three (:11417) -- THE FORM OF AN EDITION'
HIST_CLAUSE = '*Appended 2026-10-01 by b585 to the history clause (:11908), under the author’s answer before b585’s seal -- INSIDE A DATED ENTRY'


def form_lines():
    """### PLACE-papers OPEN_TRAILS: the two clauses the author entered before b592's seal, addressed to the form (:11864), and the
    ### reading beside the history clause's dated-entry line (:12044). Three appended lines."""
    Q = _Q()
    f, h = Q.line_of(Q.OT, FORM), Q.line_of(Q.OT, HIST_CLAUSE)
    if f != 11864 or h != 12044:
        sys.exit('### THE ADDRESSED LINES MOVED: %s %s -- NOTHING WRITTEN' % (f, h))
    heads = [('*Appended 2026-10-02 by b592, under the author’s answer before b592’s seal, to the form of an edition (:%d) -- THE PAGE '
              'CLAUSE:*' % f),
             ('*Appended 2026-10-02 by b592, under the author’s answer before b592’s seal, to the form of an edition (:%d) -- THE '
              'RESTATEMENT CLAUSE:*' % f),
             ('*Appended 2026-10-02 by b592 to the history clause’s dated-entry line (:%d), under the author’s answer before b592’s seal '
              '-- AN ERA ANNOTATION IS A DATED ENTRY:*' % h)]
    for x in heads:
        Q.guard_absent(Q.OT, x)
    texts = ['\n%s an edition act regenerates every page whose Placement it changes as its last housekeeping commit before the suite, '
             'so that the page arms read clean at every closing. Applied first at b592: THE_RESIDUE_OF_RH v1.2 names nodes of both '
             'pages, and each page was re-emitted after the edition commit and committed alone (relay data/b592_page_runs_c2.txt).\n' % heads[0],
             '\n%s a marked row’s reading extends to the unmarked sentences of the same edition that restate the same claim; each is '
             'rewritten with minimal substitution, the rest unchanged, listed in the back matter with both wordings, and counted under '
             'H28b with the ruling’s rewrites. Applied first at b592 to THE_RESIDUE_OF_RH v1.1 :79 (two sentences) and :88, beside the '
             '§7 sentence of `(R202)`(4) at :77.\n' % heads[1],
             '\n%s an era annotation is a dated history entry under the line above; a banned stem inside one is carried as the dated '
             'record with a history line beneath it. Applied first at b592 to THE_RESIDUE_OF_RH v1.1 :134 (the annotation of 2026-08-12 '
             'on the correspondence standard) and :152 (the era annotation of 2026-08-12 on the residue’s statement).\n' % heads[2]]
    out = []
    for x, t in zip(heads, texts):
        r = Q.append_to(Q.OT, t)
        out.append(dict(head=x, line=Q.line_of(Q.OT, x), append=r))
    put_json('b592_form_lines.json', dict(form=f, hist_clause=h, lines=out))
    print('  form lines :%s' % [o['line'] for o in out])


SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
KERNELS = {'SIDE-explicit-formula': 'c404e727', 'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
           'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
           'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}


def scores():
    H, E, P1, P2 = jl('b592_h28.json'), jl('b592_edition.json'), jl('b592_pages.json'), jl('b592_pages_c2.json')
    a_pre, a1, a2 = rd('b592_arms_prerun.txt'), rd('b592_page_arms_c1.txt'), rd('b592_page_arms_c2.txt')
    chk = rd('b592_checks.txt')
    heads = {k: g('D:/' + k, 'rev-parse', 'main').strip() for k in KERNELS}
    kern_ok = all(heads[k].startswith(v) for k, v in KERNELS.items())
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    lock = os.path.getmtime(os.path.join(D, 'b592_lockgate.json'))
    fresh = [x for x in g(RELAY, 'ls-files', '--others', '--exclude-standard', 'data/').split(NL)
             if x.strip() and os.path.getmtime(os.path.join(ROOT, x)) >= lock - 6 * 3600]
    relay_new = sorted(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD', '--', 'data/').split(NL) + fresh)
                       if x.strip() and not os.path.basename(x).startswith(('b592_', 'audit_b592_', 'terminal_table')) and x != 'data/b591_closing_push_out.txt')
    ruled = [d for d in E['diff'] if d['kind'] == 'ruled' and d['line'] == 77]
    four = ruled and all(c in ruled[0]['cites'] for c in PIN)
    gm = re.search(r'LIVE PASSING : (\d+)', chk)
    n_run = re.search(r'ARMS RUN : (\d+)', chk)
    S = dict(
        N1=('HELD' if P1['zeta']['identical'] and P1['chi']['identical'] and P2['zeta']['identical'] and P2['chi']['identical']
            and 'PAGE ARMS PASSING : 2 of 2' in a2 and (not chk or (gm and n_run and gm.group(1) == n_run.group(1))) else 'REFUTED',
            'pages byte-identical on two runs: C1 ζ %s χ %s, C2 ζ %s χ %s ; page arms after the housekeeping commits %s ; the suite`s '
            'own count %s (read at the closing, data/b592_checks.txt, the suite reading these scores)' % (
                P1['zeta']['identical'], P1['chi']['identical'], P2['zeta']['identical'], P2['chi']['identical'],
                re.search(r'PASSING : (\d of 2)', a2).group(1) if re.search(r'PASSING : (\d of 2)', a2) else '?',
                ('%s of %s' % (gm.group(1), n_run.group(1))) if (gm and n_run) else 'not yet run')),
        N2=('HELD' if four and E['n_body'] - E['n_cur'] == E['credit'] else 'REFUTED',
            '§7 :77 cites %s ; body %+d against credits %d (history lines %d, version line 1)' % (
                ruled[0]['cites'] if ruled else None, E['n_body'] - E['n_cur'], E['credit'], E['ruled_citations'])),
        N3=('HELD' if H['H28a'] == H['H28b'] == H['H28c'] == 'HELD' and H['held'] is None else 'REFUTED',
            'H28a %s, H28b %s, H28c %s ; held: %s' % (H['H28a'], H['H28b'], H['H28c'], H['held'] or 'none')),
        N4=('HELD' if H['n_ceils'] <= 6 and H['n_facts'] == 0 else 'REFUTED', 'ceiling corrections %d ; fact corrections %d' % (H['n_ceils'], H['n_facts'])),
        N5=('HELD' if kern_ok and pp_ch == sorted(['FINDINGS.md', 'OPEN_TRAILS.md', PAGE, DIR_PAGE, ED]) and relay_new == [] else 'REFUTED',
            'nothing deposits; kernel heads %s; PLACE-papers %s; relay data beyond b592 banks %s; the ζ node list data/b592_nodes.txt and its '
            'probe bank written, the ruling`s by the author`s answer 1; tools/chain_page.py and its test, the author`s answers 6 and 7' % (
                'unmoved' if kern_ok else heads, pp_ch, relay_new or 'none')),
        S1=('HELD' if re.search(r'^  G-CHAIN-PAGE\s+FAIL\b', a_pre, re.M) and re.search(r'^  G-CHAIN-PAGE-CHI\s+FAIL\b', a_pre, re.M)
            and 'PAGE ARMS PASSING : 2 of 2' in a1 else 'REFUTED',
            'at HEAD before the seal both page arms FAIL (the standing line`s first run); after the Component 1 commits %s' % (
                re.search(r'PASSING : (\d of 2)', a1).group(1) if re.search(r'PASSING : (\d of 2)', a1) else '?')),
        S2=('HELD' if P1['chi'].get('last_eq_960') else 'REFUTED', 'the χ page`s last derived line equal to REGISTRY :960: %s' % P1['chi'].get('last_eq_960')),
        S3=('HELD' if len(P1['zeta']['added']) == 11 and not P1['zeta']['gone'] else 'REFUTED',
            'ζ Placement rows added %d, gone %d' % (len(P1['zeta']['added']), len(P1['zeta']['gone']))),
        S4=('HELD' if P2['zeta']['changed'] and P2['chi']['changed'] else 'REFUTED',
            'after the edition commit the pages moved: ζ %s, χ %s' % (P2['zeta']['changed'], P2['chi']['changed'])),
        S5=('HELD' if H['clean'] and H['history'] == 3 else 'REFUTED', 'the scanner`s verdict %s ; live uses %s ; carried-by-history %s' % (
            'CLEAN' if H['clean'] else 'NOT CLEAN', H['live'], H['history'])),
    )
    S.update(H28a=(H['H28a'], 'the work-list row cites h2_sign_iff_rh at v0.2'), H28b=(H['H28b'], 'body %+d against at most %d' % (H['body_dn'], H['allowed'])),
             H28c=(H['H28c'], 'scanner CLEAN %s ; beyond the ceiling %d' % (H['clean'], H['beyond'])))
    put_json('b592_scores.json', S)
    for k in SCORE_KEYS + ('H28a', 'H28b', 'H28c'):
        print('  %-4s %s -- %s' % (k, S[k][0], S[k][1][:170]))


TITLE = ('## CP-7, act fourteen: the edition of THE_RESIDUE_OF_RH from its tier block and work-list, §7’s two clauses read as the '
         'inequality that is RH and the realization that is a supplier; the two pages regenerated at v0.16')
TRAIL_HEAD = ('### b592 — lane three, act nineteen under (R202): CP-7 act fourteen -- the edition of THE_RESIDUE_OF_RH written beside v1.1, '
              '§7 read by the record’s reading; the two pages regenerated at v0.16; the arm-unrun standing line')


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def findings():
    Q = _Q()
    S, E, H, wl, sl, fl = (jl('b592_scores.json'), jl('b592_edition.json'), jl('b592_h28.json'), jl('b592_weight_line.json'),
                           jl('b592_standing_line.json'), jl('b592_form_lines.json'))
    P1 = jl('b592_pages.json')
    Q.guard_absent(Q.FIND, TITLE[:90])
    e = ['', TITLE, '',
         '*Filed at b592 on the author’s ruling `(R202)`. Banks: relay `data/b592_edition_RESIDUE.txt`, `data/b592_edition.json`, '
         '`data/b592_edition_termscan.txt`, `data/b592_page_runs.txt`, `data/b592_page_runs_c2.txt`, `data/b592_author_answers.txt`. '
         'Nothing deposits.*', '',
         '**The edition** (`(R202)`(4), by the form at OPEN_TRAILS :11864 and its clauses): `%s` beside v1.1, which is unedited, '
         'sha256 `%s`; the work-list’s one MOVED row (the standard table’s h2 row, v1.1 :132) rewritten to the premise in its Weil '
         'form with its compiled equivalence; §7’s conjunction sentence (v1.1 :77) rewritten by the record’s reading at :6218 -- '
         'the conjunction implies RH, clause 2 in full is RH by three compiled faces and the residue’s own iff, clause 1 a candidate '
         'supplier and not a separate necessity -- and, on the author’s answers before the seal, the same reading carried to the '
         'unmarked sentences restating the claim (v1.1 :79, two sentences; :88); the b450 sign-face-registers item located by name '
         '(OPEN_TRAILS :6764, the archive :3476) and credited beneath the clause it corrects; the two era annotations’ stems carried '
         'by history with a history line beneath each; the chiasmus, the threshold, the Selberg and de Branges sentences and the b567 '
         'line carried. Body %d sentences against %d (%+d: one credit, two history lines, one version line); back matter %d. H28a %s, '
         'H28b %s, H28c %s; no sentence held.' % (ED, E['sha256'], E['n_body'], E['n_cur'], E['n_body'] - E['n_cur'], E['n_backmatter'],
                                                   H['H28a'], H['H28b'], H['H28c']), '',
         '**The pages** (`(R202)`(2)): the ζ page regenerated at SIDE-explicit-formula v0.16 = c404e72 from relay data/b592_nodes.txt '
         '(b569’s records, the pin moved, on the author’s answer; no ζ-leg declaration added since v0.11), its Placement taking the '
         'eleven edition rows (PLACE-papers %s); the χ page from data/b592_nodes_chi.txt, the generic detector a node and the Epstein '
         'instance a Correspondence row with its premise, its last derived line REGISTRY :960 byte for byte (PLACE-papers %s); each '
         'run twice byte-identical, the probe re-banked at v0.16. After the edition commit each page was re-emitted for its new '
         'Placement row and committed alone (PLACE-papers %s, %s), the page clause the author entered at OPEN_TRAILS :%d.' % (
             _pp_commit('b592 housekeeping -- (R202)(2) the ζ page'), _pp_commit('b592 housekeeping -- (R202)(2) the χ page'),
             _pp_commit('b592 housekeeping -- the ζ page re-emitted'), _pp_commit('b592 housekeeping -- the χ page re-emitted'),
             fl['lines'][0]['line']), '',
         '**The generator** (the author’s answers before the seal): relay tools/chain_page.py, committed alone with its test (relay '
         '%s, 8 of 8) -- a Correspondence row graded INTERFACES names its premises in its tier cell (two rows of the ζ page, the Epstein '
         'row of the χ page), and a node whose short name is a plain lower-case word matches a keystone only by its qualified name or in '
         'backticks (the χ page’s ten English-word matches excluded; the ζ page’s match unchanged, checked).' % (
             g(RELAY, 'log', '-1', '--format=%h', '--', 'tools/chain_page.py').strip()), '',
         '**The record lines.** b591’s weight at FINDINGS :%d; the arm-unrun standing line at OPEN_TRAILS :%d; the restatement '
         'clause at :%d; the era-annotation reading at :%d.' % (wl['line'], sl['line'], fl['lines'][1]['line'], fl['lines'][2]['line']), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Next.** Per `(R202)`(5): BALANCE_AND_POSITIVITY, the companion that follows the fourteen, by the same form; the author '
         'rules on the closing.', '',
         '*Nothing deposits; no kernel written; THE_RESIDUE_OF_RH v1.1 unedited; README, REGISTRY and ERRATA unwritten; nothing here is '
         'a statement about RH or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    put_json('b592_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE[:90]), title=TITLE, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, TITLE[:90]))


def trail():
    Q = _Q()
    S, fj, wl, sl, fl, E = (jl('b592_scores.json'), jl('b592_findings.json'), jl('b592_weight_line.json'), jl('b592_standing_line.json'),
                            jl('b592_form_lines.json'), jl('b592_edition.json'))
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows_ = ['', TRAIL_HEAD, '',
             '**(R202) ratified.** (1) b591 at its weight. (2) The two pages regenerated at v0.16 as housekeeping. (3) The arm-unrun '
             'standing line. (4) CP-7 act fourteen, the edition of THE_RESIDUE_OF_RH. (5) The act after: BALANCE_AND_POSITIVITY.', '',
             '**Entered:** FINDINGS.md:%d (b591’s weight), :%d (the entry); OPEN_TRAILS.md:%d (the standing line), :%d (the page '
             'clause), :%d (the restatement clause), :%d (the era-annotation reading), this record; PLACE-papers `%s` (the edition).' % (
                 wl['line'], fj['entry_line'], sl['line'], fl['lines'][0]['line'], fl['lines'][1]['line'], fl['lines'][2]['line'], ED), '',
             '**Answered before the seal, by the author** (relay data/b592_author_answers.txt): the ζ page regenerates from a new node list '
             'at v0.16, b569’s list kept as the record of the v0.11 page; each page re-emitted after the edition commit and committed '
             'alone, and the page clause entered; the §7 reading carried to v1.1 :79 (two sentences) and :88, and the restatement clause '
             'entered; the era annotations read as dated entries, their stems carried by history; the generator’s two clauses, a '
             'premise named on an INTERFACES Correspondence row and the plain-word keystone rule, committed alone with their test '
             '(relay %s).' % g(RELAY, 'log', '-1', '--format=%h', '--', 'tools/chain_page.py').strip(), '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R202)`(5), BALANCE_AND_POSITIVITY by the same form; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel written; THE_RESIDUE_OF_RH v1.1 unedited; ERRATA untouched; '
             'FACES_LEDGER untouched; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    r = Q.append_to(Q.OT, NL.join(rows_))
    put_json('b592_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b592_trail.json')['line'])


def desk():
    S = jl('b592_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b592 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H28a-H28c.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in ('H28a', 'H28b', 'H28c')]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)),
          '### ### **H28a %s ; H28b %s ; H28c %s.**' % (S['H28a'][0], S['H28b'][0], S['H28c'][0]), '']
    L += rd('b592_defects.txt').rstrip(NL).split(NL)
    put_txt('b592_desk_notes.txt', L)


def components():
    S, E, fj, tj, wl, sl, fl = (jl('b592_scores.json'), jl('b592_edition.json'), jl('b592_findings.json'), jl('b592_trail.json'),
                                jl('b592_weight_line.json'), jl('b592_standing_line.json'), jl('b592_form_lines.json'))
    L = ['b592 -- THE COMPONENTS, BANKED UNDER (R202).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b591`s closing push-out relay %s ; push-b591* branches deleted by name '
         '(data/b592_branches.txt) ; the kept branches untouched' % STEPZERO,
         '### COMPONENT 1 : the χ node list extended (data/b592_nodes_chi.txt) and the ζ list at v0.16 (data/b592_nodes.txt) ; both probes '
         're-banked at v0.16 ; each page twice byte-identical and committed alone ; the two page arms (data/b592_page_arms_c1.txt) ; b591`s '
         'weight FINDINGS :%d ; the standing line OPEN_TRAILS :%d' % (wl['line'], sl['line']),
         '### COMPONENT 2 : the edition %s (sha256 %s) ; body %d vs %d ; back matter %d ; H28a %s, H28b %s, H28c %s ; no sentence held ; '
         'the pages re-emitted after the edition commit (data/b592_page_runs_c2.txt)' % (
             ED, E['sha256'][:16], E['n_body'], E['n_cur'], E['n_backmatter'], S['H28a'][0], S['H28b'][0], S['H28c'][0]),
         '### COMPONENT 3 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d, :%d, :%d (the form lines), :%d (the record) ; next: BALANCE_AND_POSITIVITY ; '
         'N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (fj['entry_line'], fl['lines'][0]['line'], fl['lines'][1]['line'], fl['lines'][2]['line'], tj['line'],
                                               S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b592_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b592_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
