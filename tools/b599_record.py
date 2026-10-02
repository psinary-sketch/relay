# -*- coding: utf-8 -*-
"""b599_record.py -- THE ACT'S RECORD TOOL, UNDER (R209). ### ONE SUBCOMMAND PER BANK.

### ### b599: LANE THREE, ACT TWENTY-SIX -- CP-7 ACTS EIGHTEEN AND NINETEEN: THE EDITIONS OF SILENCE_STAGES_DEALIGNMENT AND
### REPARAMETERIZATION_BARRIERS BY THE FORM FROM THEIR b598 BANKS; THE SILENCE PRINCIPLE ALIAS; b394's ERRATUM.
### Subcommands write only `data/b599_*` unless the docstring names another file. Every bank is written through `put_txt` /
### `put_json` (encode, temp file, `os.replace`). No platform call. The templates are b597_record.py (the edition, the pages, the
### record) and b598_record.py (the banks this act's editions read).
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))

D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
SEC = 'D:/SIDE-structural-error-correction'
COS = 'D:/SIDE-cosmo'
SKK = 'D:/SIDE-kernel'
SSP = 'D:/SIDE-silence-principle'
PRE_PP = 'fcb498e'
PRE_RELAY = '32fdac16'
STEPZERO = '9da1209d'
ALIAS_C = 'd3f32506'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/11d35e08-0b91-42db-86b9-9969753496cd/scratchpad'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/11d35e08-0b91-42db-86b9-9969753496cd.jsonl'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
NODES = {'zeta': 'b596_nodes_faces.txt', 'chi': 'b596_nodes_chi.txt'}
PROBE = {'zeta': 'b596_probe_out.txt', 'chi': 'b596_chi_probe_out.txt'}
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
HOME = ('phase1.5/structural/SILENCE_FORMAL.md', 43)
ERR_ID = 'E-2026-10-02-1'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '')


def put_txt(name, lines):
    b = (NL.join(lines) + NL).encode('utf-8')
    p = os.path.join(D, name)
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    print('  written: %s (%d bytes)' % (name, len(b)))
    return b


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


def sha(b):
    return hashlib.sha256(b if isinstance(b, bytes) else b.encode('utf-8')).hexdigest()


def utc():
    return time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())


def _Q():
    import b566_record as R6
    return R6.Q


DEFECTS = [
    '(a) THE SEAT`S N5 PREDICATE, AS FIRST WRITTEN, COUNTED THE STEP-ZERO PUSH-OUT BANK AS A FILE BEYOND THE RULED SET: its relay file '
    'set excluded this act`s own banks and the table but not data/b598_closing_push_out.txt, which Component 0 orders committed (b598`s '
    'scorer excluded its own step-zero bank by name). Found on reading the predicate before the first scores run; corrected through the '
    'Edit tool to exclude that one path by name; no score had been banked with the defective predicate.',
    '(b) TWO PREDICATES OF THE SEAT`S OWN SUITE WERE DEFECTIVE AT THE FIRST PRE-PUSH RUN: G-MOVED-ROW refused the substring '
    '“SteaneExemplar.”, which the rewritten row legitimately carries in the file path it cites (`SIDECosmo/SteaneExemplar.lean` '
    ':72-:75); G-DEFINITIONAL-ROWS refused “no terminal |”, which the new silence row legitimately carries (“the four-domain survey '
    'having no terminal |”). Both live arms failed on true editions. Each needle narrowed through the Edit tool to the old wording it '
    'tests for (`SteaneExemplar.knill_laflamme_t1`, “— no terminal |”), the suite re-run whole; the arm list did not change.',
]


def defects():
    put_txt('b599_defects.txt', ['### b599 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


# ================================================================================ READING (1): THE READS
RELAY = ROOT.replace('\\', '/')
S_PATH = 'phase2/quantum/SILENCE_STAGES_DEALIGNMENT.md'
R_PATH = 'phase2/method/REPARAMETERIZATION_BARRIERS_v0_1.md'
READS = [
    ('relay the b598 bank of SILENCE_STAGES_DEALIGNMENT, whole', RELAY, '16919d87', 'data/b558_editions/SILENCE_STAGES_DEALIGNMENT.txt', list(range(1, 175))),
    ('relay the b598 bank of REPARAMETERIZATION_BARRIERS_v0_1, whole', RELAY, '697eb1ed', 'data/b558_editions/REPARAMETERIZATION_BARRIERS_v0_1.txt', list(range(1, 80))),
    ('PLACE-papers SILENCE_STAGES_DEALIGNMENT (current): head, version, abstract, the Silence Principle sentences, §3, §5, §9, the '
     'references, the history, the era annotation, b557`s block', PP, PRE_PP, S_PATH,
     [1, 3, 13, 15, 21, 23, 95, 97, 109, 121, 144, 146, 150, 162, 196, 198, 200, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 213, 221,
      235, 237, 241, 243, 245, 249, 256, 259, 265, 267, 280, 281, 282, 283, 284, 287]),
    ('PLACE-papers REPARAMETERIZATION_BARRIERS_v0_1 (current): head, version, abstract, §1, the schema, §6, the Correspondence, the '
     'work-orders, the history, b454`s and b557`s blocks', PP, PRE_PP, R_PATH,
     [1, 5, 6, 22, 23, 39, 40, 41, 42, 58, 59, 67, 70, 146, 180, 181, 182, 219, 223, 224, 225, 230, 236, 250, 252, 260, 266, 272, 273, 285]),
    ('PLACE-papers the home of the Silence Principle: SILENCE_FORMAL (title, role, the theorem, (A))', PP, PRE_PP, HOME[0], [1, 2, 6, 43, 44, 46, 47, 48]),
    ('PLACE-papers SILENCE_OF_FOUNDATIONS: the principle read in expository form', PP, PRE_PP, 'phase1.5/structural/SILENCE_OF_FOUNDATIONS.md', [17, 103]),
    ('PLACE-papers REGISTRY: the home`s row, the two documents` rows, the row b394 matched (each cut after its version cell)', PP, PRE_PP,
     'REGISTRY.md', [183, 184, 249, 283, 687], 140),
    ('PLACE-papers OPEN_TRAILS: b394`s block, the form, its clauses, the precedence order, b597`s and b598`s lines', PP, PRE_PP, 'OPEN_TRAILS.md',
     [4538, 4540, 11864, 11902, 11904, 11906, 11908, 11930, 11932, 11934, 11954, 11956, 12044, 12136, 12190, 12192, 12194, 12228, 12288, 12290,
      12296, 12298, 12314]),
    ('PLACE-papers FINDINGS: b598`s weight, strike items and entry', PP, PRE_PP, 'FINDINGS.md', [6898, 6900, 6902]),
    ('PLACE-papers ERRATA: the form (the head, the last two entries)', PP, PRE_PP, 'ERRATA.md', [1, 15, 16, 17, 18, 757, 759, 773, 809, 811, 815, 817]),
    ('PLACE-papers the copy b394 read: SILENCE_STAGES_DEALIGNMENT at 4cd1cd2, its §9', PP, '4cd1cd2', S_PATH, [196, 198, 200, 202, 203, 204, 205,
                                                                                                       206, 207, 208, 209, 210, 211]),
    ('PLACE-papers the ζ page at v0.17: head', PP, PRE_PP, PAGE, [1, 3, 164]),
    ('relay b558`s matcher and its alias table, the alias at step zero', RELAY, ALIAS_C, 'tools/b558_record.py', list(range(330, 344))),
    ('relay b394`s components: SILENCE_STAGES_DEALIGNMENT', RELAY, 'HEAD', 'data/b394_components.txt', list(range(75, 91))),
    ('SIDE-structural-error-correction v0.2.1 DeAlignment.lean: the six theorems', SEC, 'v0.2.1', 'SIDEStructuralErrorCorrection/DeAlignment.lean',
     [29, 62, 75, 85, 113, 118, 140, 142]),
    ('SIDE-structural-error-correction v0.2.1 Basic.lean: the definitions and the two restating theorems', SEC, 'v0.2.1',
     'SIDEStructuralErrorCorrection/Basic.lean', [36, 71, 97, 102, 103, 216, 222, 228, 233, 234, 236]),
    ('SIDE-cosmo c5cba30 SteaneExemplar.lean: the two theorems and the docstring', SEC.replace('SIDE-structural-error-correction', 'SIDE-cosmo'), 'c5cba30',
     'SIDECosmo/SteaneExemplar.lean', [72, 73, 74, 75, 76, 77, 81, 82]),
    ('SIDE-kernel 5e668b4 InvarianceBarrier.lean', SKK, '5e668b4', 'Kernel/Cascade/InvarianceBarrier.lean', [31, 39, 50, 60]),
    ('SIDE-silence-principle v0.2.0 Basic.lean: silence_universal', SSP, 'v0.2.0', 'SIDESilencePrinciple/Basic.lean', [118, 181, 182, 183]),
    ('relay b598`s closing push-out, committed at step zero', RELAY, 'HEAD', 'data/b598_closing_push_out.txt', list(range(1, 9))),
    ('relay the alias re-run, banked at step zero', RELAY, 'HEAD', 'data/b599_alias_rerun.txt', list(range(1, 14))),
]


def reads():
    L = ['b599 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for rr in READS:
        label, repo, rev, path, sel = rr[:5]
        width = rr[5] if len(rr) > 5 else 600
        if rev == 'HEAD' and repo == RELAY and not g(repo, 'ls-files', path).strip():
            sl = io.open(os.path.join(ROOT, path), encoding='utf-8').read().split(NL)
            at = 'working tree'
        else:
            sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
            at = g(repo, 'rev-parse', '--short=8', rev + '^{}').strip()
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, at, len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:width]))
    T = jl('terminal_table.json')
    L += ['', '### the terminal table at relay HEAD (%s), its rows for every cited terminal:' % g(RELAY, 'rev-parse', '--short=8', 'HEAD').strip()]
    for t in ('no_domain_covers_line', 'single_domain_fault_not_logical', 'dealigned_of_lines_injective', 'fano_dealignment_decidable_example',
              'fano_collapsed_line_rejected', 'fano_two_design', 'd_eff_formula', 'silence_yields_protection', 'steane_parameters',
              'knill_laflamme_t1', 'silence_universal', 'invariance_barrier', 'derivability_barrier'):
        rs = [r for r in T['rows'] if r['name'] == t or r['name'].endswith('.' + t)]
        L.append('    %-36s %s' % (t, ' ; '.join('%s %s grade %s profile %s present_at %s' % (r['repo'], r['name'], r['grade'], r['profile_state'],
                                                                                         r['present_at']) for r in rs) or 'NO ROW'))
    hits = [x for x in g(PP, 'grep', '-n', 'Silence Principle', PRE_PP, '--', '*.md').split(NL) if x.strip()]
    per = {}
    for h in hits:
        f = h.split(':', 2)[1]
        per[f] = per.get(f, 0) + 1
    import b558_record as CP
    roster = set(p for _k, _t, p in CP.ROSTER)
    L += ['', '### "Silence Principle" by name across PLACE-papers at %s: %d lines in %d files; the files, by count (R = a b557 roster document):'
          % (PRE_PP, len(hits), len(per))]
    L += ['    %3d %s%s' % (n, f, ' (R)' if f in roster else '') for f, n in sorted(per.items(), key=lambda x: (-x[1], x[0]))]
    L += ['### the documents STATING it (a heading or a bold statement of the principle):'] + [
        '    %s' % h[:260] for h in hits if re.search(r'(Theorem \(Silence Principle\)|\*\*Silence Principle \(informal\)\.\*\*|\*\*The Silence Principle\.\*\*|^### 2\.2 The Silence Principle)',
                                                    h.split(':', 3)[-1])]
    L += ['### the home, named in the alias: %s :%d -- the formal statement (its title “THE SILENCE PRINCIPLE / Formal Statement”, its '
          'role line :6 “presents the formal statement”, REGISTRY 1.5d-2 “Silence Principle (formal)”); the expository forms (SILENCE_OF_FOUNDATIONS '
          ':103, the deposited day1/Silence_of_Foundations.md :92) read it' % HOME,
          '### SIDE-structural-error-correction: v0.2.1 = %s ; main = %s ; files carrying `#print axioms` at v0.2.1: %s' % (
              g(SEC, 'rev-parse', '--short=7', 'v0.2.1^{commit}').strip(), g(SEC, 'rev-parse', '--short=7', 'main').strip(),
              [x for x in g(SEC, 'grep', '-l', '#print axioms', 'v0.2.1', '--').split(NL) if x.strip()] or 'none'),
          '### SIDE-cosmo SteaneExemplar.lean opens a namespace at c5cba30: %s' % bool(re.search(r'^namespace ', g(COS, 'show', 'c5cba30:SIDECosmo/SteaneExemplar.lean'), re.M)),
          '### SIDE-kernel: InvarianceBarrier.lean blob at 5e668b4 %s, v1.7 %s, main %s (= %s), v1.5 %s' % tuple(
              [g(SKK, 'rev-parse', '--short=8', '%s:Kernel/Cascade/InvarianceBarrier.lean' % r).strip() or 'ABSENT' for r in ('5e668b4', 'v1.7', 'main')]
              + [g(SKK, 'rev-parse', '--short=7', 'main').strip(), g(SKK, 'rev-parse', '--short=8', 'v1.5:Kernel/Cascade/InvarianceBarrier.lean').strip() or 'ABSENT']),
          '### SIDE-silence-principle: v0.2.0 = %s' % g(SSP, 'rev-parse', '--short=7', 'v0.2.0^{commit}').strip(),
          '### the copy b394 read, PLACE-papers 4cd1cd2: %d lines, `## 9. Correspondence` at :%s, rows :202-:211 %d' % (
              len(g(PP, 'show', '4cd1cd2:' + S_PATH).rstrip(NL).split(NL)),
              next((i + 1 for i, l in enumerate(g(PP, 'show', '4cd1cd2:' + S_PATH).split(NL)) if l.startswith('## 9. Correspondence')), None),
              sum(1 for l in g(PP, 'show', '4cd1cd2:' + S_PATH).split(NL)[201:211] if l.startswith('| '))),
          '### ERRATA ids dated 2026-10-02 at %s: %s' % (PRE_PP, re.findall(r'E-2026-10-02-\d+', g(PP, 'show', PRE_PP + ':ERRATA.md')) or 'none')]
    put_txt('b599_reads.txt', L)


# ================================================================================ COMPONENT 1: THE RECORD LINES
B598_ENTRY = '## CP-1b: the tier blocks and work-lists of SILENCE_STAGES_DEALIGNMENT and REPARAMETERIZATION_BARRIERS from b557’s tiers'
B394_LINE = '**WHAT THE THREE CARRY.** `GRH_CASCADE` carries'


def weight_line():
    """### PLACE-papers FINDINGS: b598's weight and the items ruled, two appended lines addressed to b598's entry, in (R209)(1)-(2)'s
    ### facts."""
    Q = _Q()
    entry = Q.line_of(Q.FIND, B598_ENTRY)
    if entry != 6902:
        sys.exit('### THE ADDRESSED LINE MOVED: entry %s -- NOTHING WRITTEN' % entry)
    h1 = '*Appended 2026-10-02 by b599 to b598’s entry (:%d), under `(R209)`(1) -- b598 AT ITS WEIGHT:*' % entry
    h2 = '*Appended 2026-10-02 by b599 to b598’s entry (:%d), under `(R209)`(2) -- THE ITEMS, AS RULED:*' % entry
    for h in (h1, h2):
        Q.guard_absent(Q.FIND, h)
    t1 = ('\n%s two banks under relay data/b558_editions/, each committed alone (16919d87, 697eb1ed). SILENCE_STAGES_DEALIGNMENT: 9 '
          'terminals, all T2 by b557’s tier bank -- six de-alignment theorems at SIDE-structural-error-correction v0.2.1 = 6a4f482 with no '
          'terminal-table row, that kernel writing no axioms to an artefact; two Steane theorems at SIDE-cosmo c5cba30; conservation_of_spectra '
          'by b558’s alias at :109 -- 22 work-list rows, 12 of the document’s own 13 STANDS and one MOVED-IN-MEANING, §9 :209’s Knill–Laflamme '
          'conditions against knill_laflamme_t1, which states the single-error syndrome condition (the check map’s columns nonzero and '
          'distinct), the Knill–Laflamme link in its docstring and not compiled. REPARAMETERIZATION_BARRIERS: 2 terminals, both T2, the file '
          'byte-identical at 5e668b4, v1.7 and main, absent at the deposit v1.5; 7 rows, all STANDS. One MOVED row between them, so both '
          'editions in one act. FINDINGS :6898, :6900, :6902; OPEN_TRAILS :12314; relay 32fdac16 with the closing; PLACE-papers fcb498e; '
          'TECHNE-Core untouched. The suite 63 of 63 before and after the push; no prompt. (N1), (N3), (N4) refuted -- the tier blocks at 9 '
          'and 2, the MOVED row at its own pin, b450 listing SILENCE as reconciled with no item -- the navigator’s counts, each a miss about '
          'the documents’ size and not the form. Defect (a) the seat’s, caught on read-back: b558 left five documents without a work-list, '
          'and FACES_LEDGER, THE_IDENTITY_CHAIN and THE_KEYSTONE_CENSUS still have none. Nothing deposited; no kernel touched.\n' % h1)
    t2 = ('\n%s the five Silence Principle sentences of SILENCE_STAGES take the name-and-title exception, one history line beneath the '
          'earliest citing the document that states the principle, and the alias is added to b558’s matcher naming that home by path '
          '(relay d3f32506); b394’s two record errors are corrected by one dated erratum and one history line addressed to OPEN_TRAILS '
          ':4540; §9’s two “no terminal” rows cite their definitions as T2, definitional; the SteaneExemplar. prefix and the barrier note’s '
          '“CURRENT kernel pin” take the fact clause; “We prove” and “proved, not conjectured” take the restatement clause and the ceiling; '
          'no b450 credit is owed to REPARAM. Each lands in this act’s editions and record as ruled.\n' % h2)
    out = []
    for h, t in ((h1, t1), (h2, t2)):
        r = Q.append_to(Q.FIND, t)
        out.append(dict(head=h, line=Q.line_of(Q.FIND, h), append=r))
    put_json('b599_weight_line.json', dict(entry=entry, lines=out))
    for o in out:
        print('  line :%s' % o['line'])


ERR_HEAD = ('## %s — b394’s record of SILENCE_STAGES_DEALIGNMENT says it carries no correspondence table and names another '
            'document’s registry row as its record item; the copy b394 read carries §9 with ten rows (CORPUS-FACING; NO DEPOSITED ARTIFACT IS '
            'AFFECTED)' % ERR_ID)


def erratum():
    """### PLACE-papers ERRATA.md: one dated entry appended through relay tools/errata_append.py (it refuses a duplicate id before it
    ### writes); OPEN_TRAILS: one history line appended at the end, addressed to :4540 (the author's answer: no line moves). The two
    ### files are committed alone by the seat. Writes data/b599_erratum.json."""
    import errata_append as EA
    Q = _Q()
    b4540 = Q.line_of(Q.OT, B394_LINE)
    if b4540 != 4540:
        sys.exit('### THE ADDRESSED LINE MOVED: b394 %s -- NOTHING WRITTEN' % b4540)
    ot_head = ('*Appended 2026-10-02 by b599 beneath b394’s block, addressed to :%d, under `(R209)`(2)(ii) and the author’s answer before '
               'b599’s seal (appended at the end, no line moves) -- A HISTORY LINE:*' % b4540)
    Q.guard_absent(Q.OT, ot_head)
    blk = [ERR_HEAD, '',
           '**Filed 2026-10-02 by b599, on the author’s ruling `(R209)`(2)(ii); found at b598 (relay `data/b558_editions/SILENCE_STAGES_DEALIGNMENT.txt`, '
           'its b450 section). Record affected: OPEN_TRAILS :4540, b394’s block of 2026-09-09, and the bank behind it, relay '
           '`data/b394_components.txt` :79-:87. ### NO DEPOSITED ARTIFACT IS AFFECTED BY THIS ENTRY, AND THE DOCUMENT IS NOT AFFECTED.** Both '
           'errors are in the record about the document, not in the document.',
           '',
           '**What the record says.** OPEN_TRAILS :4540: *“`SILENCE_STAGES_DEALIGNMENT` carries none”* -- no correspondence rows -- *“the answer '
           'is there is no table”*; relay `data/b394_components.txt` :79: *“IT CARRIES NO CORRESPONDENCE TABLE”*; and, as the record item '
           'matched against the document, :85-:87: *“THE RECORD -- `REGISTRY.md` line 244: | p2-24 | Dark Interface |”*.',
           '',
           '**What the copy read carries.** PLACE-papers `4cd1cd2` (b394’s own commit of 2026-09-09), `phase2/quantum/SILENCE_STAGES_DEALIGNMENT.md`: '
           '§9 “Correspondence” at :196, its ten rows at :202-:211 -- six de-alignment theorems at SIDE-structural-error-correction v0.2.1 '
           '(`6a4f482`), two Steane theorems at SIDE-cosmo (`c5cba30`), two manuscript-resident rows (relay `data/b599_reads.txt`). The heading '
           'opens “## 9.”, the shape b586 found a heading matcher can miss. The registry row b394 matched is another document’s: p2-24, '
           '`phase2/philosophy/DARK_INTERFACE.md` (now REGISTRY :249); this document’s row is p2-16 (now REGISTRY :283).',
           '',
           '**The correction, as ruled.** SILENCE_STAGES_DEALIGNMENT carried a correspondence table when b394 read it, ten rows, eight naming '
           'a terminal, as b557 tiered it at 2026-09-29; b394’s “no table” and its one record item are corrected here, and the basis of b450’s '
           'RECONCILED mark for the document (relay `data/b450_components.txt` :21) is b394’s reading as corrected.',
           '',
           '**Scope.** OPEN_TRAILS :4540 is not edited; one history line, appended at the ledger’s end and addressed to it, points here. The '
           'document is not edited by this entry; its edition of this act (v1.3) carries §9 as the table. No banked number, verdict or grade '
           'moves.',
           '',
           '**Status.** FILED.',
           '',
           '*Filed by b599 (relay `data/b599_reads.txt`, `data/b558_editions/SILENCE_STAGES_DEALIGNMENT.txt`). No deposited artifact is affected.*']
    path = os.path.join(PP, 'ERRATA.md')
    code, lines = EA.append(path, ERR_ID, blk)
    for x in lines:
        print(x)
    if code != 0:
        sys.exit('### THE ERRATUM WAS REFUSED -- NOTHING MORE WRITTEN')
    err_line = Q.line_of(path, ERR_HEAD[:60]) if hasattr(Q, 'line_of') else None
    ot_text = ('\n%s b394’s “carries none” and “there is no table” for SILENCE_STAGES_DEALIGNMENT are contradicted by the copy b394 read, '
               'PLACE-papers 4cd1cd2, whose §9 “Correspondence” at :196 carries ten rows (:202-:211); its one record item, the registry row of '
               'Dark Interface (p2-24), is another document’s. Both corrected by %s at ERRATA :%s; the block above stands as the dated record.\n'
               % (ot_head, ERR_ID, err_line))
    r = Q.append_to(Q.OT, ot_text)
    put_json('b599_erratum.json', dict(id=ERR_ID, head=ERR_HEAD, errata_line=err_line, errata_out=lines, ot_head=ot_head,
                                       ot_line=Q.line_of(Q.OT, ot_head), ot_append=r, addressed=b4540))
    print('  ERRATA :%s ; OPEN_TRAILS history line :%s' % (err_line, Q.line_of(Q.OT, ot_head)))


WORD_HEAD = ('### `W-ORD-SEC-AXIOM-ARTEFACT` -- SIDE-STRUCTURAL-ERROR-CORRECTION’S TERMINALS WITH `#print axioms` WRITTEN TO AN ARTEFACT, '
             'PRICED, NOT STARTED, appended 2026-10-02, b599, under the author’s ruling (R209)(3)')


def work_order():
    """### PLACE-papers OPEN_TRAILS: (R209)(3) W-ORD-SEC-AXIOM-ARTEFACT, its items, price, trigger and reason."""
    Q = _Q()
    Q.guard_absent(Q.OT, WORD_HEAD)
    t = ('\n%s\n\n**Items.** SIDE-structural-error-correction’s six de-alignment theorems (`DeAlignment.no_domain_covers_line`, '
         '`single_domain_fault_not_logical`, `dealigned_of_lines_injective`, `fano_dealignment_decidable_example`, '
         '`fano_collapsed_line_rejected`, `fano_two_design`) and every terminal it exports, `d_eff_formula` and `silence_yields_protection` '
         'among them, get `#print axioms` written to an artefact in the house form; the terminal table takes their rows; the tier bank '
         're-reads them.\n\n**Price:** one kernel housekeeping commit at the memory hold, one table regeneration. **Trigger:** the author’s '
         'word. **Reason:** a T2 grade with no printed profile is a grade from recall.\n' % WORD_HEAD)
    r = Q.append_to(Q.OT, t)
    put_json('b599_work_order.json', dict(head=WORD_HEAD, line=Q.line_of(Q.OT, WORD_HEAD), append=r))
    print('  W-ORD line :%s' % Q.line_of(Q.OT, WORD_HEAD))


def _word_line():
    try:
        return jl('b599_work_order.json')['line']
    except Exception:
        return None


# ================================================================================ COMPONENTS 2-3: THE EDITIONS
P_SEC = 'SIDE-structural-error-correction v0.2.1 = `6a4f482`'
NPP = 'no printed profile (the kernel writes no `#print axioms` artefact)'


def _hist21():
    return ('*History line, 2026-10-02 (v1.3, b599): the Silence Principle named above and at :{a}, :{b} and :{c} (twice) is the corpus’s own '
            'named object, its statement “Theorem (Silence Principle)” at `phase1.5/structural/SILENCE_FORMAL.md` :43 (REGISTRY 1.5d-2), whose '
            'part (A), protection across a P-dark interface, is the reading these sentences apply, and its compiled universal form there is '
            '`silence_universal`, interfacing on the named hypothesis `I.is_universal` (SIDE-silence-principle v0.2.0 = `667c254`, '
            '`SIDESilencePrinciple/Basic.lean` :181), while this document’s compiled anchor stays the de-alignment condition of §7.*')


H282 = ('*History line, 2026-10-02 (v1.3, b599): of the rows above labelled :209, :210 and :211, the first now reads in this edition’s §9 '
        '({E:209}) the single-error syndrome condition `knill_laflamme_t1` states, its Knill–Laflamme reading the docstring’s and not compiled, '
        'and the other two ({E:210}, {E:211}) cite the definitions the kernel restates at its constant S, `d_eff_formula` and '
        '`silence_yields_protection` (' + P_SEC + '), each T2 as definitional, the general bound and the four-domain survey staying '
        'manuscript-resident.*')

DOC = {
    'SILENCE': dict(
        title='SILENCE_STAGES_DEALIGNMENT', cur=S_PATH, ed='phase2/quantum/SILENCE_STAGES_DEALIGNMENT_v1_3.md', vers='v1.3', old='v1.2',
        bank='data/b558_editions/SILENCE_STAGES_DEALIGNMENT.txt', bankj='b598_bank_SILENCE.json', bank_c='16919d87',
        diffbank='b599_edition_SILENCE.txt', termscan='b599_edition_termscan_SILENCE.txt', repin='b599_repin_SILENCE.txt',
        version_anchor=(14, 15, '**v1.2, 2026-07-29** (retitle per the title law; was v1.1)'),
        VERSION='**v1.3, 2026-10-02** — *CP-7 edition (b599), written beside v1.2, which is left unedited; its back matter closes the file.*',
        WORKLIST=[
            (209, '| The Knill–Laflamme error-correction conditions | SIDE-cosmo (`c5cba30`) | `SteaneExemplar.knill_laflamme_t1` |',
             '| The single-error syndrome condition of the [[7,1,3]] check map: its seven columns nonzero and pairwise distinct '
             '(`Function.Injective H ∧ ∀ i : Fin 7, H i ≠ 0`), the t = 1 case of what the field names the Knill–Laflamme error-correction '
             'conditions (Knill and Laflamme 1997), that reading being the declaration’s docstring (`SIDECosmo/SteaneExemplar.lean` :72-:75), '
             'not compiled | SIDE-cosmo (`c5cba30`) | `knill_laflamme_t1` |',
             'the work-list’s MOVED-IN-MEANING row (`knill_laflamme_t1`), with the fact clause on its prefix ((R209)(2)(iv))'),
        ],
        CEILS=[
            (21, 'We prove: the effective distance under formation-block errors equals 2S − 1 where S is the number of non-empty formation stages.',
             'We argue, by the sketch of §3 and not by a compiled statement, that the effective distance under formation-block errors is at least '
             '2S − 1 (equal at S = 3, §2) where S is the number of non-empty formation stages, the kernel restating only its definition '
             '`d_eff := 2 * S - 1` at its constant S (`d_eff_formula`, ' + P_SEC + ').',
             '“We prove” ((R209)(2)(vi)): the general theorem is manuscript-resident (§3 {E:97}, §9 {E:210}), with the restatement clause on “equals”'),
        ],
        FACTS=[
            (198, 'All rows pinned to `SIDE-structural-error-correction` v0.2.1,',
             'All rows but the two Steane rows (pinned in the sibling kernel `SIDE-cosmo` at `c5cba30`, as the note beneath the table says) '
             'pinned to `SIDE-structural-error-correction` v0.2.1,',
             'the rows {E:208}-{E:209} cite SIDE-cosmo `c5cba30` (relay data/b599_reads.txt; the note {E:213})'),
            (208, '`SteaneExemplar.steane_parameters`', '`steane_parameters`',
             '(R209)(2)(iv): `SIDECosmo/SteaneExemplar.lean` at SIDE-cosmo c5cba30 opens no namespace; the declaration is at the root (relay data/b599_reads.txt)'),
            (210, '| none (manuscript) | proof sketch only — no terminal | n/a | manuscript-resident |',
             '| ' + 'SIDE-structural-error-correction v0.2.1 (`6a4f482`) | `SIDEStructuralErrorCorrection.d_eff_formula`, the definition '
             '`d_eff := 2 * S - 1` (`Basic.lean` :97) restated at the kernel’s constant S = 3 by `decide` (:103), the bound for every S having a '
             'sketch only (§3) | ' + NPP + ' | T2, definitional; the general bound manuscript-resident |',
             '(R209)(2)(iii): the pin the section cites carries d_eff_formula (relay data/b599_reads.txt; b598 bank, the objects)'),
            (211, '| none (manuscript) | survey — no terminal | n/a | manuscript-resident |',
             '| SIDE-structural-error-correction v0.2.1 (`6a4f482`) | `SIDEStructuralErrorCorrection.silence_yields_protection`, the definitions '
             '`num_compartments := S` (`Basic.lean` :222) and `d_eff` (:97) restated as `num_compartments = S ∧ d_eff = 2 * num_compartments - 1` '
             'by `decide` (:233), the four-domain survey having no terminal | ' + NPP + ' | T2, definitional; the survey manuscript-resident |',
             '(R209)(2)(iii): the pin carries silence_yields_protection (relay data/b599_reads.txt; b598 bank, the objects)'),
            (213, 'The Formation Distance theorem (§3) and the four-domain pattern (§4–5) carry no kernel and are manuscript-resident, exactly as §3 '
                  'and §5 already record.*',
             'The Formation Distance theorem (§3) and the four-domain pattern (§4–5) are manuscript-resident as general statements, exactly as '
             '§3 and §5 already record, their two rows citing the definitions the kernel restates at its constant S (`d_eff_formula`, '
             '`silence_yields_protection`, ' + P_SEC + '), T2 as definitional.*',
             'the rows {E:210}-{E:211} now cite the definitions at the pin (relay data/b599_reads.txt)'),
        ],
        RESTATE=[],
        NAMES={21: 'the Silence Principle, the corpus’s own named object ((R209)(2)(i))', 121: 'the same', 144: 'the same',
               162: 'the same, twice (the question and its sentence)'},
        HIST_SPEC=[(21, 'beneath the earliest sentence naming the Silence Principle ({E:21})', '(R209)(2)(i): the name-and-title exception, one '
                    'history line citing the home of the principle by path and line'),
                   (282, 'beneath b557’s tier table ({E:271}-{E:282}), for its rows {E:280}-{E:282}', 'the dated block restates the row {E:209} and '
                    'names no terminal for {E:210}-{E:211}; the history clause governs (OPEN_TRAILS :11908, :12194)')],
        CARRIED={34: 'the survey table’s system label “SIDE proof (logic)”, the name of a system, not a claim',
                 97: 'the general theorem’s “proof sketch only”, manuscript-resident with no kernel pin -- true of the bound for every S; read and carried',
                 235: '“manuscript-resident (proof sketch only …)” of the §3 general theorem, true as above',
                 237: 'the AI disclosure’s “proof strategies”',
                 245: 'the v1.0.1 dated entry, “proof sketch”, carried by history',
                 256: 'the era annotation of 2026-08-20, “proved at general q” (SIDE-global-section `KLSilence`), carried by history'},
        READ_KEPT={21: '“Silence is protection.”: the survey’s pattern, which {E:23} already carries “at manuscript grade”; not a “proved” phrasing; '
                       'carried by the letter, for the author’s strike',
                   144: '“The protection is not designed. It is derived.”: the survey’s reading, which {E:150} carries “at manuscript/correspondence '
                        'grade”; carried by the letter, for the author’s strike',
                   146: '“Error-correcting codes are not inventions …”: scoped by {E:150}’s claim-status; carried, for the author’s strike'},
        COLLISIONS=[
            (21, 'the ceiling clause (“We prove”) and the restatement clause (“equals” restating §3’s ≥), on one sentence', 'ceiling, then restatement',
             'one rewrite: the ceiling takes “We prove”, the restatement what it leaves; both wordings in the ceiling row'),
            (21, 'the name-and-title exception (“The Silence Principle provides the mechanism …”) and the ceiling clause on the line’s other sentence',
             'both, on different sentences', 'the named sentence carried, a history line beneath; the ceiling on “We prove”'),
            (144, 'the name-and-title exception (the final sentence) and the survey’s “It is derived” beside it', 'name, then read',
             'the named sentence carried; “It is derived” read and left, scoped by {E:150}'),
            (209, 'the work-list’s MOVED-IN-MEANING row and the fact clause (the `SteaneExemplar.` prefix)', 'the work-list row and the fact together',
             'one rewrite answers both: the claim cell names the syndrome condition the statement carries, the name written as declared'),
            (213, 'the fact clause (“carry no kernel”, contradicted by the rows {E:210}-{E:211} as rewritten) and the restatement clause', 'fact',
             'corrected to the definitions cited at the pin; the restatement clause has nothing left'),
            (243, 'the history clause (the v1.1 entry: “two manuscript-resident rows”) and the fact clause', 'history',
             'carried unchanged as the dated record; the rows’ new terminals stated in the history line beneath b557’s table'),
            (256, 'the history clause (the era annotation of 2026-08-20) and the ceiling clause (“proved at general q”)', 'history',
             'carried unchanged as the dated record; the object is SIDE-global-section’s `KLSilence`, not this document’s'),
            (259, 'the history clause (the era annotation) and the work-list’s Knill–Laflamme reading', 'history',
             'carried unchanged: it names the Knill–Laflamme verdict of the KL run, another object than `knill_laflamme_t1`'),
            (280, 'the history clause (b557’s tier block, dated 2026-09-29) and the restatement clause (the block’s :209 row)', 'history',
             'carried unchanged; the reading in the history line beneath the block’s table'),
            (281, 'the history clause (b557’s block, its rows {E:281}-{E:282}, “NONE … T4”) and the fact clause', 'history',
             'carried unchanged; the definitions and their T2 named in the same history line'),
        ],
        CORR=[
            ('DeAlignment.no_domain_covers_line', 'DeAlignment.no_domain_covers_line', 'SIDE-structural-error-correction', 'v0.2.1 = 6a4f482',
             'no terminal-table row (no artefact); profile b557’s probe, relay data/b557_tiers.txt :271'),
            ('DeAlignment.single_domain_fault_not_logical', 'DeAlignment.single_domain_fault_not_logical', 'SIDE-structural-error-correction', 'v0.2.1 = 6a4f482',
             'no row; relay data/b557_tiers.txt :279'),
            ('DeAlignment.dealigned_of_lines_injective', 'DeAlignment.dealigned_of_lines_injective', 'SIDE-structural-error-correction', 'v0.2.1 = 6a4f482',
             'no row; relay data/b557_tiers.txt :287'),
            ('DeAlignment.fano_dealignment_decidable_example', 'DeAlignment.fano_dealignment_decidable_example', 'SIDE-structural-error-correction',
             'v0.2.1 = 6a4f482', 'no row; relay data/b557_tiers.txt :295'),
            ('DeAlignment.fano_collapsed_line_rejected', 'DeAlignment.fano_collapsed_line_rejected', 'SIDE-structural-error-correction', 'v0.2.1 = 6a4f482',
             'no row; relay data/b557_tiers.txt :303'),
            ('DeAlignment.fano_two_design', 'DeAlignment.fano_two_design', 'SIDE-structural-error-correction', 'v0.2.1 = 6a4f482',
             'no row; relay data/b557_tiers.txt :311'),
            ('SIDEStructuralErrorCorrection.d_eff_formula', 'SIDEStructuralErrorCorrection.d_eff_formula', 'SIDE-structural-error-correction',
             'v0.2.1 = 6a4f482', 'no row, no printed profile; Basic.lean :103'),
            ('SIDEStructuralErrorCorrection.silence_yields_protection', 'SIDEStructuralErrorCorrection.silence_yields_protection',
             'SIDE-structural-error-correction', 'v0.2.1 = 6a4f482', 'no row, no printed profile; Basic.lean :233'),
            ('steane_parameters', 'steane_parameters', 'SIDE-cosmo', 'c5cba30 (main)', 'terminal table, UNGRADED; profile relay data/b557_tiers.txt :319'),
            ('knill_laflamme_t1', 'knill_laflamme_t1', 'SIDE-cosmo', 'c5cba30 (main)', 'terminal table, UNGRADED; profile relay data/b557_tiers.txt :327'),
            ('silence_universal', 'silence_universal', 'SIDE-silence-principle', 'v0.2.0 = 667c254', 'terminal table, INTERFACES; Basic.lean :181'),
        ],
        PIN={'knill_laflamme_t1': 'c5cba30', 'steane_parameters': 'c5cba30', 'd_eff_formula': '6a4f482',
             'SIDEStructuralErrorCorrection.d_eff_formula': '6a4f482', 'silence_yields_protection': '6a4f482',
             'SIDEStructuralErrorCorrection.silence_yields_protection': '6a4f482', 'silence_universal': '667c254'},
        BANKS=['`SIDECosmo/SteaneExemplar.lean` :72-:75'],
    ),
    'REPARAM': dict(
        title='REPARAMETERIZATION_BARRIERS', cur=R_PATH, ed='phase2/method/REPARAMETERIZATION_BARRIERS_v0_2.md', vers='v0.2', old='v0.1',
        bank='data/b558_editions/REPARAMETERIZATION_BARRIERS_v0_1.txt', bankj='b598_bank_REPARAM.json', bank_c='697eb1ed',
        diffbank='b599_edition_REPARAM.txt', termscan='b599_edition_termscan_REPARAM.txt', repin='b599_repin_REPARAM.txt',
        version_anchor=(5, 6, '**v0.1 — 2026-08-04 — DRAFT**'),
        VERSION='**v0.2 — 2026-10-02 — CP-7 edition (b599), written beside v0.1, which is left unedited; its back matter closes the file.**',
        WORKLIST=[],
        CEILS=[
            (41, 'proved, not conjectured, and it is proved once for the class rather than',
             'compiled as a schema (`InvarianceBarrier.invariance_barrier`, SIDE-kernel `5e668b4`), its two clauses for this domain argued in '
             'this note (§4), and it is stated once for the class rather than',
             '“proved, not conjectured” ((R209)(2)(vi)): the compiled part is the schema ({E:223}), the witness pair manuscript-resident ({E:225}-{E:229})'),
            (180, 'with both barrier clauses proved rather than',
             'with both barrier clauses shown by explicit construction (manuscript-resident, the Correspondence rows (W1)-(W5)) rather than',
             'a “proved” phrasing about the barrier ((R209)(4)): the clauses are manuscript-resident ({E:225}-{E:229})'),
        ],
        FACTS=[
            (219, '**RE-VERIFIED AS-RUN 2026-08-06 at the CURRENT kernel pin `5e668b4` (the note was drafted against v1.7 = `2957e7d`).**',
             '**RE-VERIFIED AS-RUN 2026-08-06 at the kernel pin `5e668b4`, current on that date (the note was drafted against v1.7 = `2957e7d`, '
             'and SIDE-kernel main is now `0256e9e`, `Kernel/Cascade/InvarianceBarrier.lean` the same blob `e4e8d23b` at `5e668b4`, v1.7 and '
             '`0256e9e`).**',
             '(R209)(2)(v): SIDE-kernel main 0256e9e, the file`s blob e4e8d23b unchanged at 5e668b4, v1.7 and main (relay data/b599_reads.txt)'),
        ],
        RESTATE=[],
        NAMES={},
        HIST_SPEC=[],
        CARRIED={236: 'the work-order’s “State and prove or refute a stability version”, an instruction, not a claim',
                 250: 'the AI disclosure’s “proof strategies”'},
        READ_KEPT={70: '“Both are compiled and axiom-free (SIDE-kernel v1.7; see Correspondence)”: the file is the same blob `e4e8d23b` at v1.7, '
                       '`5e668b4` and main; carried as read',
                   146: 'the manuscript theorem’s “Therefore no method in D determines P”: its two clauses manuscript-resident ({E:225}-{E:229}), the '
                        'inference compiled ({E:223}); carried as read, for the author’s strike'},
        COLLISIONS=[
            (41, 'the ceiling clause (“proved, not conjectured … proved once”) and the restatement clause, on the sentence {E:39}-{E:42}', 'ceiling, then restatement',
             'one rewrite on {E:41}: the compiled schema named, the domain clauses named as argued; {E:40} and {E:42} unchanged'),
            (219, 'the fact clause (“the CURRENT kernel pin”) and the dated re-verification note of 2026-08-06', 'fact, as (R209)(2)(v) rules',
             'the date and its re-verification kept; the pin named as current on that date, main now `0256e9e`, the blob unchanged'),
        ],
        CORR=[
            ('InvarianceBarrier.invariance_barrier', 'InvarianceBarrier.invariance_barrier', 'SIDE-kernel', '5e668b4 (blob e4e8d23b = v1.7 = main 0256e9e)',
             'terminal table, UNGRADED; profile relay data/b557_tiers.txt :560'),
            ('InvarianceBarrier.derivability_barrier', 'InvarianceBarrier.derivability_barrier', 'SIDE-kernel', '5e668b4 (blob e4e8d23b = v1.7 = main 0256e9e)',
             'terminal table, UNGRADED; profile relay data/b557_tiers.txt :568'),
        ],
        PIN={'InvarianceBarrier.invariance_barrier': '5e668b4'},
        BANKS=['`Kernel/Cascade/InvarianceBarrier.lean`'],
    ),
}
ORDER = ('SILENCE', 'REPARAM')
CEILING = re.compile(r'\bprov(?:e|ed|en|es)\b|\bproof\b|RH-core|RH proved|proves RH|end-to-end|the whole of RH')


def _segs(l):
    import b558_record as CP
    return [s for s in CP.segments(l) if s]


def _count(lines):
    return sum(len(_segs(l)) for l in lines)


def _cur(k):
    cur = g(PP, 'show', '%s:%s' % (PRE_PP, DOC[k]['cur'])).split(NL)
    return cur[:-1] if cur and cur[-1] == '' else cur


def _inserts(k):
    d = DOC[k]
    a, _n, _s = d['version_anchor']
    ins = [(a, [d['VERSION'], ''] if k == 'SILENCE' else [d['VERSION']], 'version')]
    for after, _w, _y in d['HIST_SPEC']:
        ins.append((after, ['', _hist_text(k, after)], 'history'))
    return ins


def _edl(k, n):
    d = DOC[k]
    a = d['version_anchor'][0]
    off = (2 if k == 'SILENCE' else 1) if n > a else 0
    for after, _w, _y in d['HIST_SPEC']:
        if n > after:
            off += 2
    return n + off


def _hist_text(k, after):
    if k == 'SILENCE' and after == 21:
        return _hist21().format(a=_edl(k, 121), b=_edl(k, 144), c=_edl(k, 162))
    if k == 'SILENCE' and after == 282:
        return fmt(k, H282)
    raise KeyError(after)


def fmt(k, s):
    """### a reason cell's `{E:n}` names the current version's line n by the edition's own number."""
    return re.sub(r'\{E:(\d+)\}', lambda m: ':%d' % _edl(k, int(m.group(1))), s) if isinstance(s, str) else s


def _all_changes(k):
    d = DOC[k]
    return [(x[0], x[1], x[2]) for x in d['WORKLIST'] + d['CEILS'] + d['FACTS'] + d['RESTATE']]


def _cites(k, t):
    d = DOC[k]
    return [x for x in d['PIN'] if ('`%s`' % x) in t and d['PIN'][x] in t] + [b for b in d['BANKS'] if b in t]


def _status_blanks(lines):
    import b579_record as R9
    return R9._status_blanks(lines)


def _bm_tag(k):
    return '<!-- b599 (R209) THE %s EDITION`S BACK MATTER, 2026-10-02 -->' % DOC[k]['vers']


def _offset(k):
    d = DOC[k]
    a = d['version_anchor'][0]
    if k == 'SILENCE':
        return ('+2 from :15 (the v1.3 line and a blank, above the v1.2 line); +2 more from :22 (a blank and the history line beneath :21); '
                '+2 more from :283 (a blank and the history line beneath b557’s tier table) -- the current version’s :n sits at the edition’s :n '
                'for n < 15, :n+2 for 15 <= n <= 21, :n+4 for 22 <= n <= 282, :n+6 for n >= 283')
    return ('+1 from :6 (the v0.2 line, above the v0.1 line) -- the current version’s :n sits at the edition’s :n for n < 6, :n+1 for n >= 6')


def edition(k, *a):
    """### PLACE-papers <doc>'s next version beside the current one from its blob at fcb498e; the re-pin step last (`repin`).
    ### Writes the edition file and data/b599_edition_<k>.json; `dry` writes nothing."""
    if k not in DOC:
        sys.exit('usage: edition SILENCE|REPARAM [dry]')
    d = DOC[k]
    cur = _cur(k)
    if g(PP, 'rev-parse', 'HEAD:' + d['cur']).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, d['cur'])).strip():
        sys.exit('### THE CURRENT VERSION MOVED SINCE fcb498e -- NOTHING WRITTEN')
    edp = os.path.join(PP, *d['ed'].split('/'))
    dry = 'dry' in a
    if not dry and os.path.exists(edp):
        sys.exit('### THE EDITION FILE EXISTS -- NOTHING WRITTEN')
    new = list(cur)
    for ln, old, rep in _all_changes(k):
        line = new[ln - 1]
        if line.count(old) != 1:
            sys.exit('### :%d -- THE FRAGMENT IS NOT ON ITS LINE EXACTLY ONCE (%d): %s' % (ln, line.count(old), old[:80]))
        n0 = len(_segs(line))
        new[ln - 1] = line.replace(old, rep)
        if len(_segs(new[ln - 1])) != n0:
            sys.exit('### :%d -- THE CHANGE ALTERED THE LINE`S SEGMENT COUNT %d -> %d: %s' % (ln, n0, len(_segs(new[ln - 1])), old[:60]))
    va, vn, vs = d['version_anchor']
    if cur[vn - 1] != vs:
        sys.exit('### THE VERSION ANCHOR IS NOT WHERE THE FACE SAYS: %s' % cur[vn - 1][:60])
    if k == 'SILENCE':
        if cur[13] != '' or cur[21] != '' or cur[282] != '' or not cur[281].startswith('| :211 |') or not cur[20].startswith('We identify a pattern'):
            sys.exit('### AN INSERTION ANCHOR IS NOT WHERE THE FACE SAYS')
    import banned_terms as BT
    ins = [d['VERSION']] + [_hist_text(k, x[0]) for x in d['HIST_SPEC']]
    for t in ins:
        if len(_segs(t)) != 1:
            sys.exit('### AN INSERTED LINE IS NOT ONE SENTENCE (%d): %s' % (len(_segs(t)), t[:60]))
    for t in ins + [x[2] for x in _all_changes(k)]:
        if BT.PAT.search(t):
            sys.exit('### A BANNED STEM IN AN INSERTED OR REWRITTEN TEXT: %s' % t[:80])
        if CEILING.search(t):
            sys.exit('### A CEILING-SHAPED WORD IN AN INSERTED OR REWRITTEN TEXT: %s' % CEILING.search(t).group(0))
    J = jl(d['bankj'])
    rows = [r for r in J['rows'] if r['verdict'] == 'MOVED-IN-MEANING']
    diff = []
    for r in rows:
        ln = r['line']
        sg = _segs(cur[ln - 1])
        if r['sentence'] not in sg:
            sys.exit('### THE ROW :%d`S SENTENCE IS NOT A SEGMENT OF ITS LINE' % ln)
        j = sg.index(r['sentence'])
        nw = _segs(new[ln - 1])[j]
        w = [x for x in d['WORKLIST'] if x[0] == ln]
        diff.append(dict(id='work-list:%d' % ln, line=ln, ed_line=_edl(k, ln), terminal=r['terminal'], old=r['sentence'], new=nw,
                         changed=nw != r['sentence'], cites=_cites(k, nw), supports=r['reading'], answers=w[0][3] if w else '', kind='work-list'))
    for kind, lst in (('ceiling', d['CEILS']), ('fact', d['FACTS']), ('restatement', d['RESTATE'])):
        for ln, old, rep, why in lst:
            sg0 = [s for s in _segs(cur[ln - 1]) if old in s]
            sg1 = [s for s in _segs(new[ln - 1]) if rep in s]
            diff.append(dict(id='%s:%d' % (kind, ln), line=ln, ed_line=_edl(k, ln), terminal=why, old=sg0[0] if sg0 else old,
                             new=sg1[0] if sg1 else rep, changed=True, cites=_cites(k, rep), supports=why, answers=why, kind=kind))
    for after, ls, _kk in sorted(_inserts(k), key=lambda x: -x[0]):
        new[after:after] = ls
    body = list(new)
    changed = set(x[0] for x in _all_changes(k))
    if any(_edl(k, n) > len(body) or (n not in changed and body[_edl(k, n) - 1] != cur[n - 1]) for n in range(1, len(cur) + 1)):
        sys.exit('### OFFSET MODEL DOES NOT CARRY THE CURRENT VERSION')
    hist_at = {}
    for after, _w, _y in d['HIST_SPEC']:
        t = _hist_text(k, after)
        idx = [i for i, l in enumerate(body, 1) if l == t]
        if len(idx) != 1 or idx[0] != _edl(k, after) + 2:
            sys.exit('### A HISTORY LINE IS NOT IN THE BODY ONCE, BENEATH ITS ANCHOR')
        hist_at[str(after)] = idx[0]
    ver_at = body.index(d['VERSION']) + 1
    if body[ver_at - 1 + (2 if k == 'SILENCE' else 1)] != vs:
        sys.exit('### THE VERSION LINE IS NOT ABOVE THE OLD ONE')
    inv = {_edl(k, n): n for n in range(1, len(cur) + 1)}
    hits = [(i, m.group(0)) for i, l in enumerate(body, 1) for m in CEILING.finditer(l)]
    stray = sorted(set(inv.get(i, -i) for i, _ in hits) - set(d['CARRIED']) - changed)
    if stray:
        sys.exit('### A CEILING HIT IN THE BODY IS NEITHER REWRITTEN NOR CARRIED BY THE SEAT`S READ: current lines %s' % stray)
    E = lambda n: _edl(k, n)
    wline = _word_line() or (99999 if dry else None)
    if not wline:
        sys.exit('### W-ORD-SEC-AXIOM-ARTEFACT HAS NO BANKED LINE -- COMPONENT 1 FIRST')
    bm = ['', _bm_tag(k), '',
          '## Back matter of the %s edition -- written 2026-10-02 by b599 under the author’s ruling `(R209)`(4), by the form of `(R187)`(5) '
          'and its precedence order' % d['vers'], '',
          '*This file is %s of %s, the CP-7 edition written beside %s (`%s`, unedited) from its b598 bank (relay `%s`, committed at `%s`: its '
          'tier block, its work-list, b450’s items and the objects for this edition), the ζ page at SIDE-explicit-formula v0.17 and the terminal '
          'table as its spine. The document keeps its class; the edition promotes no reading, does not deposit and does not replace %s, and '
          'its promotion is CP-8’s. Every line cited below is this file’s own.*' % (d['vers'], d['title'], d['old'], d['cur'], d['bank'], d['bank_c'],
                                                                                  d['old']), '',
          '### Removals', '', 'None: every marked sentence is rewritten in place to what its compiled fact or bank line says.', '']

    def cell(s):
        return s.replace('|', '¦')
    bm += ['### Rewrites -- the work-list', '']
    if d['WORKLIST']:
        bm += ['| this edition’s line | %s wording | %s wording | Status |' % (d['old'], d['vers']), '|:--|:--|:--|:--|']
        for ln, old, rep, why in d['WORKLIST']:
            bm.append('| :%d | %s | %s | rewritten: %s |' % (E(ln), cell(old), cell(rep), why))
    else:
        bm.append('None: the work-list carries no MOVED-IN-MEANING row (relay `%s`, every row STANDS).' % d['bank'])
    for head, lst, clause in (('### Ceiling corrections', d['CEILS'], 'ceiling correction (OPEN_TRAILS :11906)'),
                              ('### Fact corrections', d['FACTS'], 'fact correction (OPEN_TRAILS :11954)'),
                              ('### Restatement rewrites', d['RESTATE'], 'restatement clause (OPEN_TRAILS :12192)')):
        bm += ['', head, '']
        if lst:
            bm += ['| this edition’s line | %s wording | %s wording | Status |' % (d['old'], d['vers']), '|:--|:--|:--|:--|']
            for ln, old, rep, why in lst:
                bm.append('| :%d | %s | %s | %s: %s |' % (E(ln), cell(old), cell(rep), clause, why))
        else:
            bm.append('None apart from those listed with the ceiling clause, where the restatement clause applies to what the ceiling leaves.')
    bm += ['', '### Collisions resolved by the precedence order (OPEN_TRAILS :12228)', '',
           '| this edition’s line | the clauses that meet | the governing clause | Status |', '|:--|:--|:--|:--|']
    for ln, clauses, gov, why in d['COLLISIONS']:
        bm.append('| :%d | %s | %s | %s |' % (E(ln), clauses, gov, why))
    bm += ['', '### History lines', '']
    if d['HIST_SPEC']:
        bm += ['| this edition’s history line | beneath | Status |', '|:--|:--|:--|']
        for after, w, y in d['HIST_SPEC']:
            bm.append('| :%d | %s | inserted under the history clause (OPEN_TRAILS :11908): %s |' % (hist_at[str(after)], w, y))
    else:
        bm.append('None: no marked sentence sits in a dated entry.')
    bm += ['', '### Names excepted (the name-and-title exception, OPEN_TRAILS :11934)', '']
    if d['NAMES']:
        bm += ['| this edition’s line | the name | Status |', '|:--|:--|:--|']
        for ln in sorted(d['NAMES']):
            bm.append('| :%d | %s | excepted: the name carried, reached by b558’s matcher through the alias of relay `%s` |' % (E(ln), d['NAMES'][ln], ALIAS_C))
    else:
        bm.append('None.')
    bm += ['', '### Stem corrections', '', 'None: the scanner reads no live banned stem in the current version or in this edition.', '',
           '### Ceiling-shaped sentences read and carried', '', '| this edition’s line | the seat’s read | Status |', '|:--|:--|:--|']
    for ln in sorted(d['CARRIED']):
        bm.append('| :%d | ceiling read, carried: %s | carried as read |' % (E(ln), d['CARRIED'][ln]))
    bm += ['', '### Sentences read and left, for the author’s strike', '', '| this edition’s line | the seat’s read | Status |', '|:--|:--|:--|']
    for ln in sorted(d['READ_KEPT']):
        bm.append('| :%d | %s | carried as read |' % (E(ln), d['READ_KEPT'][ln]))
    bm += ['', '### The axiom profiles', '']
    if k == 'SILENCE':
        bm.append('The six de-alignment terminals are cited at ' + P_SEC + ', as §9 cites them; that kernel writes no `#print axioms` output to an '
                  'artefact, so there is no printed profile of the kernel’s own and the terminal table carries no row for them -- the profiles in '
                  '§9 are b557’s fresh probes (relay `data/b557_tiers.txt` :271-:318), and `d_eff_formula` and `silence_yields_protection` have none '
                  'printed. `W-ORD-SEC-AXIOM-ARTEFACT` (OPEN_TRAILS :%d) prices that artefact.' % wline)
    else:
        bm.append('The two schemata are cited at SIDE-kernel `5e668b4`, the blob `e4e8d23b` the same at v1.7 and at main `0256e9e`; their '
                  'profiles were re-printed on 2026-08-06 (the note’s Correspondence) and by b557’s probe (relay `data/b557_tiers.txt` :557-:571).')
    bm += ['', '### The ruling’s readings of `(R209)`', '', '| reading | the read | Status |', '|:--|:--|:--|']
    if k == 'SILENCE':
        bm += ['| (2)(i) the five Silence Principle sentences take the name-and-title exception, one history line beneath the earliest citing the '
               'principle’s home by path | :%s ; the history line :%d citing `phase1.5/structural/SILENCE_FORMAL.md` :43 | excepted, line inserted |'
               % (', :'.join(str(E(x)) for x in sorted(d['NAMES'])), hist_at['21']),
               '| (2)(iii) §9’s “no terminal” rows cite their definitions by name and pin, T2 as definitional | :%d, :%d | corrected |' % (E(210), E(211)),
               '| (2)(iv) the `SteaneExemplar.` prefix takes the plain names as the file declares them | :%d, :%d | corrected |' % (E(208), E(209)),
               '| (2)(vi) “We prove” takes the restatement clause and the ceiling | :%d | corrected |' % E(21),
               '| (4) the MOVED row names the single-error syndrome condition, the Knill–Laflamme name kept as the field’s, the docstring noted '
               'as not compiled | :%d | rewritten |' % E(209),
               '| (4) the de-alignment terminals cited at `6a4f482` with “no printed profile” stated and W-ORD-SEC-AXIOM-ARTEFACT named | the '
               'axiom profiles above | stated |']
    else:
        bm += ['| (2)(v) “CURRENT kernel pin `5e668b4`” takes the fact clause: main `0256e9e`, the blob unchanged | :%d | corrected |' % E(219),
               '| (2)(vi) “proved, not conjectured” takes the restatement clause and the ceiling | :%d | corrected |' % E(41),
               '| (2)(vii) no b450 credit owed; the two-kinds windows verdict carried since b454 | :%d | carried |' % E(258),
               '| (4) “proved” phrasings about the barrier take the ceiling | :%d, :%d | corrected |' % (E(41), E(180))]
    bm += ['', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
           '| this edition, %s | `%s` | written at b599 |' % (d['vers'], d['ed']),
           '| the current version, %s | `%s` | unedited |' % (d['old'], d['cur']),
           '| the spine | `%s`, at SIDE-explicit-formula v0.17 = `5a1630b`, and relay `data/terminal_table.md` | read |' % PAGE,
           '| the bank | relay `%s` | read |' % d['bank'],
           '| the sentence-by-sentence diff | relay `data/%s` | banked at b599 |' % d['diffbank'], '',
           '### Correspondence', '', '| declaration | repository | pin | where it is printed | Status |', '|:--|:--|:--|:--|:--|']
    ed_lines = {}
    hset = set(hist_at.values())
    for fq, needle, repo, pin, where in d['CORR']:
        ls = [i for i, l in enumerate(body, 1) if re.search(r'`(?:[A-Za-z0-9_]+\.)*' + re.escape(needle.split('.')[-1]) + r'`', l) and ('`%s`' % needle) in l]
        ls = [i for i, l in enumerate(body, 1) if ('`%s`' % needle) in l and i != ver_at]
        ed_lines[fq] = sorted(set(ls))
        bm.append('| `%s` | %s | %s | %s | cited at :%s of this edition%s |' % (fq, repo, pin, where, ', :'.join(str(x) for x in ed_lines[fq]) or '### NONE',
                                                                                  ' (a history line)' if set(ed_lines[fq]) <= hset and ed_lines[fq] else ''))
    bm.append('')
    if any('### NONE' in l for l in bm):
        sys.exit('### A CORRESPONDENCE ROW CITES NO LINE OF THE EDITION: %s' % [l for l in bm if '### NONE' in l])
    bm = [fmt(k, x) for x in bm]
    if any('{E:' in x for x in bm):
        sys.exit('### AN UNRESOLVED LINE TOKEN IN THE BACK MATTER')
    for x in diff:
        for f in ('answers', 'supports', 'terminal'):
            x[f] = fmt(k, x[f])
    full = body + bm
    b = (NL.join(full) + NL).encode('utf-8')
    n_cur, n_body, n_full = _count(cur), _count(body), _count(full)
    print('  %s counts: current %d ; body %d ; whole %d ; back matter %d' % (k, n_cur, n_body, n_full, n_full - n_body))
    if dry:
        print('  DRY: nothing written; diff rows %d' % len(diff))
        for x in diff:
            print('   %-16s :%d -> :%d cites %s' % (x['id'], x['line'], x['ed_line'], x['cites']))
        p = os.path.join(SP, os.path.basename(d['ed']))
        open(p, 'wb').write(b)
        print('  dry copy: %s' % p)
        return
    open(edp + '.tmp', 'wb').write(b)
    os.replace(edp + '.tmp', edp)
    print('  written: %s (%d bytes, %d lines)' % (d['ed'], len(b), len(full)))
    put_json('b599_edition_%s.json' % k, dict(path=d['ed'], cur=d['cur'], cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, d['cur'])).strip(),
                                              lines_cur=len(cur), lines_body=len(body), lines_full=len(full),
                                              n_cur=n_cur, n_body=n_body, n_full=n_full, n_backmatter=n_full - n_body,
                                              credit=0, removals=0, ruled_citations=len(d['HIST_SPEC']), version_lines=1, diff=diff,
                                              offset=_offset(k), hist_at=hist_at, ver_at=ver_at,
                                              collisions=[list(c) for c in d['COLLISIONS']], carried={str(x): v for x, v in d['CARRIED'].items()},
                                              n_worklist=len(d['WORKLIST']), n_ceils=len(d['CEILS']), n_facts=len(d['FACTS']), n_restate=len(d['RESTATE']),
                                              n_names=sum(len([s for s in _segs(cur[n - 1]) if 'Silence Principle' in s]) for n in d['NAMES']),
                                              sha256=hashlib.sha256(b).hexdigest(), status_blanks=_status_blanks(full), cited_lines=ed_lines,
                                              word_line=wline))


def termscan(k):
    """### the scanner (banned_terms.py --new) on the edition file, banked as data/b599_edition_termscan_<k>.txt."""
    d = DOC[k]
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'banned_terms.py'), '--new', os.path.join(PP, *d['ed'].split('/'))],
                       capture_output=True, text=True, encoding='utf-8', errors='replace', env=dict(os.environ, PYTHONIOENCODING='utf-8'))
    put_txt(d['termscan'], (r.stdout or '').rstrip(NL).split(NL))
    print([l for l in r.stdout.split(NL) if 'live uses' in l or 'VERDICT' in l])


def edition_bank(k):
    """### The diff with its offset line, the collisions, the counts, the ceiling read, the scanner's verdict, H28a-H28c."""
    d = DOC[k]
    E = jl('b599_edition_%s.json' % k)
    edp = os.path.join(PP, *d['ed'].split('/'))
    ed = io.open(edp, encoding='utf-8').read().replace(chr(13), '').split(NL)
    if ed and ed[-1] == '':
        ed = ed[:-1]
    cut = ed.index(_bm_tag(k))
    scan = rd(d['termscan'])
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    carried_ed = set(_edl(k, n) for n in d['CARRIED'])
    rewritten_ed = set(_edl(k, x[0]) for x in _all_changes(k))
    hist_ed = set(E['hist_at'].values())
    hits = []
    for i, l in enumerate(ed, 1):
        for m in CEILING.finditer(l):
            kind = ('record' if i > cut else 'carried' if i in carried_ed else 'rewritten' if i in rewritten_ed
                    else 'history' if i in hist_ed else 'beyond')
            hits.append(dict(line=i, hit=m.group(0), kind=kind, ctx=l[max(0, m.start() - 60):m.end() + 40]))
    beyond = [h for h in hits if h['kind'] == 'beyond']
    wl = [x for x in E['diff'] if x['kind'] == 'work-list']
    h28a_bad = [x['id'] for x in wl if not x['changed'] or not x['cites']]
    h28a = 'HELD' if not h28a_bad else 'REFUTED'
    body_dn = E['n_body'] - E['n_cur']
    allowed = E['credit'] + E['removals'] + E['ruled_citations'] + E['version_lines']
    h28b = 'HELD' if abs(body_dn) <= allowed else 'REFUTED'
    live_n = int(live.group(1)) if live else None
    h28c = 'HELD' if (clean and not beyond) else 'REFUTED'
    cur0 = _cur(k)
    L = ['### OFFSET FROM THE CURRENT VERSION (R190)(3): %s -- every edition line below is the final file`s own.' % _offset(k), '',
         'b599 -- COMPONENT %d: THE EDITION OF %s, (R209)(4), BY THE FORM OF (R187)(5), ITS CLAUSES AND THE PRECEDENCE ORDER' % (
             2 if k == 'SILENCE' else 3, d['title']), '',
         '### the current version : PLACE-papers %s @ %s (blob %s), %d lines ; head :1 "%s" ; version :%d "%s"' % (
             d['cur'], PRE_PP, E['cur_blob'][:8], E['lines_cur'], cur0[0][:80], d['version_anchor'][1], cur0[d['version_anchor'][1] - 1]),
         '### the bank : relay %s (committed at %s), read line by line (relay data/b599_reads.txt)' % (d['bank'], d['bank_c']),
         '### the edition : PLACE-papers %s, %d lines, sha256 %s' % (d['ed'], E['lines_full'], E['sha256']), '',
         '### EVERY REWRITTEN OR INSERTED SENTENCE, WITH THE BANK LINE IT ANSWERS AND WHAT IT CITES (%d rewritten):' % len(E['diff']), '']
    for x in E['diff']:
        L += ['  %s %s :%d -> %s :%d -- %s ; cites %s' % (x['id'], d['old'], x['line'], d['vers'], x['ed_line'], x['kind'], x['cites']),
              '      answers: %s' % (x['answers'] or x['supports']), '      %s : %s' % (d['old'], x['old']), '      %s : %s' % (d['vers'], x['new']), '']
    L += ['### THE COLLISIONS, RESOLVED BY THE PRECEDENCE ORDER WITHOUT A PROMPT (%d):' % len(E['collisions'])]
    L += ['    %s :%d -> %s :%d  %s -- governs: %s -- %s' % (d['old'], c[0], d['vers'], _edl(k, c[0]), c[1], c[2], c[3]) for c in E['collisions']]
    L += ['### THE HISTORY LINES (%d, ruled citations under H28b):' % len(d['HIST_SPEC'])]
    for a, w, y in d['HIST_SPEC']:
        L += ['    %s :%d, %s -- %s' % (d['vers'], E['hist_at'][str(a)], w, y), '      %s' % _hist_text(k, a)]
    L += ['### THE NAMES EXCEPTED (%d sentences on %d lines): %s' % (E['n_names'], len(d['NAMES']), ', '.join(':%d -> :%d' % (n, _edl(k, n)) for n in sorted(d['NAMES']))),
          '### THE VERSION LINE: %s :%d, above %s`s line: %s' % (d['vers'], E['ver_at'], d['old'], d['VERSION']),
          '### THE WORK-LIST REWRITES: %d ; THE CEILING CORRECTIONS: %d ; THE FACT CORRECTIONS: %d ; THE RESTATEMENT REWRITES: %d (beyond those '
          'joined with the ceiling) ; THE STEM CORRECTIONS: none live ; REMOVALS: none ; CREDIT LINES: none (no b450 item placed for this edition)' % (
              len(d['WORKLIST']), len(d['CEILS']), len(d['FACTS']), len(d['RESTATE'])),
          '### THE CEILING-SHAPED SENTENCES READ AND CARRIED:'] + ['    %s :%d -> %s :%d  %s' % (d['old'], n, d['vers'], _edl(k, n), d['CARRIED'][n]) for n in sorted(d['CARRIED'])]
    L += ['### READ AND LEFT, FOR THE AUTHOR`S STRIKE:'] + ['    %s :%d -> %s :%d  %s' % (d['old'], n, d['vers'], _edl(k, n), d['READ_KEPT'][n]) for n in sorted(d['READ_KEPT'])]
    L += ['', '### THE COUNTS (relay tools/b558_record.py `segments`, imported): the current version %d ; the edition`s BODY %d (%+d) ; the BACK '
          'MATTER %d, printed separately ; the edition whole %d' % (E['n_cur'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + ruled citations %d (the history lines; every '
          'rewrite keeps its line`s count) + one version line = %d' % (body_dn, E['credit'], E['removals'], E['ruled_citations'], allowed),
          '### no blank Status cell: %s' % ('HELD' if not E['status_blanks'] else '### BLANK AT %s' % E['status_blanks']), '',
          '### THE CEILING, every hit in the edition:']
    L += ['    :%d "%s" -- %s -- ...%s...' % (h['line'], h['hit'], h['kind'], h['ctx']) for h in hits] or ['    none']
    L += ['### sentences beyond the ceiling: %d' % len(beyond),
          '### THE SCANNER (banned_terms.py --new) on the edition: live uses %s ; verdict %s' % (live_n, 'CLEAN' if clean else 'NOT CLEAN'), '',
          '### ### **H28a %s -- %s.**' % (h28a, ('every MOVED row resolves to a sentence citing its compiled fact at its pin' if wl else
                                                  'VACUOUS: the work-list carries no MOVED row, so no row is there to resolve') +
                                          ('' if not h28a_bad else ' -- refuted at %s' % h28a_bad)),
          '### ### **H28b %s -- final form: the body differs by %+d sentences against at most %d; the back matter %d, excluded and '
          'printed.**' % (h28b, body_dn, allowed, E['n_backmatter']),
          '### ### **H28c %s -- the scanner`s verdict %s; sentences beyond the ceiling %d.**' % (h28c, 'CLEAN' if clean else 'NOT CLEAN', len(beyond)),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**']
    L = [fmt(k, x) for x in L]
    put_txt(d['diffbank'], L)
    put_json('b599_h28_%s.json' % k, dict(H28a=h28a, H28b=h28b, H28c=h28c, h28a_bad=h28a_bad, h28a_vacuous=not wl, body_dn=body_dn, allowed=allowed,
                                          backmatter=E['n_backmatter'], live=live_n, clean=clean, beyond=len(beyond), hits=hits, held=None,
                                          n_worklist=len(d['WORKLIST']), n_ceils=len(d['CEILS']), n_facts=len(d['FACTS']), n_restate=len(d['RESTATE']),
                                          n_collisions=len(d['COLLISIONS']), n_hist=len(d['HIST_SPEC']), n_names=E['n_names']))
    H = jl('b599_h28_%s.json' % k)
    print(k, H['H28a'], H['H28b'], H['H28c'], 'body_dn', body_dn, 'allowed', allowed, 'beyond', H['beyond'], 'live', H['live'], 'collisions', H['n_collisions'])


def repin(k):
    """### THE RE-PIN STEP, THE FORM'S LAST (OPEN_TRAILS :11932). Writes data/b599_repin_<k>.txt."""
    d = DOC[k]
    E = jl('b599_edition_%s.json' % k)
    edp = os.path.join(PP, *d['ed'].split('/'))
    ed = io.open(edp, encoding='utf-8').read().replace(chr(13), '').split(NL)
    cut = ed.index(_bm_tag(k))
    checks = []
    for x in E['diff']:
        checks.append(('diff %s -> :%d carries the %s wording' % (x['id'], x['ed_line'], d['vers']), x['new'] in ed[x['ed_line'] - 1]))
    for a, w, y in d['HIST_SPEC']:
        checks.append(('history line :%d (%s)' % (E['hist_at'][str(a)], fmt(k, w)[:40]), ed[E['hist_at'][str(a)] - 1] == _hist_text(k, a)))
    for c in d['COLLISIONS']:
        checks.append(('collision row :%d is a body line' % _edl(k, c[0]), ed[_edl(k, c[0]) - 1].strip() != ''))
    for n in d['CARRIED']:
        checks.append(('carried :%d holds a ceiling-shaped hit' % _edl(k, n), CEILING.search(ed[_edl(k, n) - 1]) is not None))
    for n in d['NAMES']:
        checks.append(('name excepted :%d names the Silence Principle' % _edl(k, n), 'Silence Principle' in ed[_edl(k, n) - 1]))
    for fq, ls in E['cited_lines'].items():
        nd = [x for x in d['CORR'] if x[0] == fq][0][1]
        for x in ls:
            checks.append(('Correspondence: `%s` on :%d' % (nd, x), ('`%s`' % nd) in ed[x - 1] and x < cut))
    va, vn, vs = d['version_anchor']
    checks.append(('version line above the %s line' % d['old'], ed[E['ver_at'] - 1] == d['VERSION'] and ed[_edl(k, vn) - 1] == vs))
    bm = NL.join(ed[cut:])
    for n in sorted(set(int(x) for x in re.findall(r'\| :(\d+) \|', bm))):
        checks.append(('back-matter row :%d is a body line' % n, 0 < n < cut and ed[n - 1].strip() != ''))
    if k == 'SILENCE':
        h = E['hist_at']['21']
        checks.append(('the history line`s :%d, :%d, :%d name the Silence Principle' % (_edl(k, 121), _edl(k, 144), _edl(k, 162)),
                       all('Silence Principle' in ed[_edl(k, n) - 1] for n in (121, 144, 162)) and (':%d' % _edl(k, 121)) in ed[h - 1]))
        checks.append(('the axiom-profile line names W-ORD-SEC-AXIOM-ARTEFACT at OPEN_TRAILS :%d' % E['word_line'],
                       ('`W-ORD-SEC-AXIOM-ARTEFACT` (OPEN_TRAILS :%d)' % E['word_line']) in bm and 'no printed profile' in bm))
    bank = rd(d['diffbank'])
    checks.append(('the diff bank`s head states the offset once', bank.startswith('### OFFSET FROM THE CURRENT VERSION') and bank.count('### OFFSET FROM') == 1))
    checks.append(('the diff bank names the final file`s sha256', E['sha256'] in bank and hashlib.sha256(open(edp, 'rb').read()).hexdigest() == E['sha256']))
    L = ['### b599 -- THE RE-PIN STEP (OPEN_TRAILS :11932), RUN LAST: every cited line re-read against the final file %s' % d['ed'], '']
    L += ['    %-100s %s' % (w[:100], 'OK' if ok else '### FAILS') for w, ok in checks]
    L += ['', '### ### **RE-PIN : %d of %d citations hold against the final file.**' % (sum(ok for _w, ok in checks), len(checks))]
    put_txt(d['repin'], L)
    print(L[-1])


# ================================================================================ COMPONENT 4: THE PAGES AFTER THE EDITIONS
def page(k):
    """### after the two edition commits: ONE page re-emitted from b596's v0.17 list and banked probe (one page per call, in the
    ### foreground); the diff against PLACE-papers HEAD printed. Writes the page only when it changed, and data/b599_page_<k>.json."""
    import chain_page as C
    import difflib
    if k not in NODES:
        sys.exit('usage: page zeta|chi')
    rc, pg, meta, log = C.build(os.path.join(D, NODES[k]), os.path.join(SP, '_b599_%s' % k), os.path.join(D, PROBE[k]))
    if rc:
        sys.exit('### %s RE-EMIT FAILED, exit %d: %s' % (k, rc, log[-3:]))
    b = pg.encode('utf-8')
    prev = subprocess.run(['git', '-C', PP, 'show', 'HEAD:' + PNAME[k]], capture_output=True).stdout
    changed = cr0(prev) != b
    if changed:
        dest = os.path.join(PP, PNAME[k])
        open(dest + '.tmp', 'wb').write(b)
        os.replace(dest + '.tmp', dest)
    dl = [x for x in difflib.unified_diff(cr0(prev).decode('utf-8').split(NL), b.decode('utf-8').split(NL), 'HEAD', 'regenerated', lineterm='', n=0)]
    added = [x for x in dl if x.startswith('+| keystone naming a node |')]
    J = dict(page=PNAME[k], nodes=NODES[k], probe=PROBE[k], rc=rc, bytes=len(b), sha256=sha(b), changed=changed, diff=dl, at=utc(),
             placement_added=len(added), keystones=meta.get('keystones') if isinstance(meta, dict) else None,
             pp_head=g(PP, 'rev-parse', '--short=7', 'HEAD').strip())
    put_json('b599_page_%s.json' % k, J)
    print('  %s : exit %d ; %d bytes ; changed against HEAD %s ; Placement rows added %d' % (k, rc, len(b), changed, len(added)))
    for x in dl:
        print('    ' + x[:260])


def cr0(b):
    return (b or b'').replace(b'\r\n', b'\n')


def page_arms(tag):
    """### both page arms at PLACE-papers HEAD from b596's v0.17 lists and probes, and the frozen control. Writes data/b599_page_arms_<tag>.txt."""
    import g_chain_page as GCP
    import test_chain_page_b596 as T
    L = ['b599 -- THE PAGE ARMS AND THE FROZEN CONTROL AT PLACE-papers %s (%s) -- %s' % (g(PP, 'rev-parse', '--short=7', 'HEAD').strip(), utc(), tag)]
    n = 0
    for arm, k in (('G-CHAIN-PAGE', 'zeta'), ('G-CHAIN-PAGE-CHI', 'chi')):
        r = GCP.arm(os.path.join(D, NODES[k]), os.path.join(SP, '_b599_gcp'), os.path.join(D, PROBE[k]))
        n += r['ok'] is True
        L.append('    %s : %s -- regeneration exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            arm, 'PASS' if r['ok'] else 'FAIL', r['rc'], r['committed_bytes'], r['regenerated_bytes'], r['first_diff']))
    L.append('### ### **PAGE ARMS PASSING : %d of 2.**' % n)
    c = T.control()
    for x in c:
        L.append('    %s %s : %s -- exit %d ; committed %d bytes ; regenerated %d bytes ; first differing line %s' % (
            T.ARM, x['list'], 'PASS' if x['ok'] else 'FAIL', x['rc'], x['committed_bytes'], x['regenerated_bytes'], x['first_diff']))
    L.append('### ### **%s PASSING : %d of 2.**' % (T.ARM, sum(x['ok'] is True for x in c)))
    put_txt('b599_page_arms_%s.txt' % tag, L)
    for l in L:
        print(l[:240])


# ================================================================================ THE PROMPTS, BANKED VERBATIM
def answers():
    """### every AskUserQuestion of this session, with question, options, recommended mark and the answer, read from the session
    ### transcript (b595's method); data/b599_author_answers.txt."""
    calls, results = [], {}
    for i, raw in enumerate(io.open(SESSION, encoding='utf-8'), 1):
        try:
            o = json.loads(raw)
        except Exception:
            continue
        m = o.get('message') or {}
        for c in (m.get('content') or []) if isinstance(m.get('content'), list) else []:
            if c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                calls.append((i, c['id'], c['input']))
            if c.get('type') == 'tool_result':
                t = c.get('content')
                t = ''.join(x.get('text', '') for x in t) if isinstance(t, list) else t
                results[c.get('tool_use_id')] = (i, t)
    L = ['### b599 -- THE AUTHOR`S ANSWERS BEFORE THE SEAL, %d prompt(s) put by the seat (2026-10-02), banked verbatim with the options and '
         'the recommended mark, as the standing line at OPEN_TRAILS :12246 orders.' % sum(len(c[2].get('questions', [])) for c in calls), '']
    k = 0
    for i, cid, inp in calls:
        L.append('### CALL tool-use id %s (session 11d35e08-0b91-42db-86b9-9969753496cd, transcript line %d)' % (cid, i))
        for q in inp.get('questions', []):
            k += 1
            L.append('### PROMPT %d (%s): %s' % (k, q.get('header'), q.get('question')))
            for j, op in enumerate(q.get('options', []), 1):
                L.append('  OPTION %d%s: %s :: %s' % (j, ' [RECOMMENDED]' if '(Recommended)' in op.get('label', '') else '', op.get('label'), op.get('description')))
        ri, rt = results.get(cid, (None, '### NO RESULT FOUND'))
        L += ['RESULT (transcript line %s): %s' % (ri, rt), '']
    put_txt('b599_author_answers.txt', L)


# ================================================================================ COMPONENT 5: THE RECORD
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')


def scores():
    E = {k: jl('b599_edition_%s.json' % k) for k in ORDER}
    H = {k: jl('b599_h28_%s.json' % k) for k in ORDER}
    Z, X = jl('b599_page_zeta.json'), jl('b599_page_chi.json')
    er, wo = jl('b599_erratum.json'), jl('b599_work_order.json')
    alias = rd('b599_alias_rerun.txt')
    kern = {k: g('D:/' + k, 'rev-parse', '--short=7', 'main').strip() for k in ('SIDE-explicit-formula', 'SIDE-kernel', 'SIDE-lv-conservation',
                                                                               'SIDE-structural-error-correction', 'SIDE-cosmo', 'SIDE-silence-principle')}
    kern_ok = kern == {'SIDE-explicit-formula': '5a1630b', 'SIDE-kernel': '0256e9e', 'SIDE-lv-conservation': '2f71068',
                       'SIDE-structural-error-correction': '6a4f482', 'SIDE-cosmo': 'c5cba30', 'SIDE-silence-principle': '667c254'}
    pp_ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD')).split(NL) if x.strip()))
    want_pp = sorted(['ERRATA.md', 'FINDINGS.md', 'OPEN_TRAILS.md'] + [DOC[k]['ed'] for k in ORDER] + [p['page'] for p in (Z, X) if p.get('changed')])
    relay_beyond = sorted(set(x for x in (g(RELAY, 'diff', '--name-only', PRE_RELAY, 'HEAD') + NL + g(RELAY, 'diff', '--name-only')).split(NL)
                              if x.strip() and not os.path.basename(x).startswith('b599_') and not os.path.basename(x).startswith('terminal_table')
                              and x != 'data/b598_closing_push_out.txt'))
    cur_same = all(g(PP, 'rev-parse', 'HEAD:' + DOC[k]['cur']).strip() == g(PP, 'rev-parse', '%s:%s' % (PRE_PP, DOC[k]['cur'])).strip() for k in ORDER)
    m = re.search(r'ALIAS HITS ON SILENCE_STAGES_DEALIGNMENT : (\d+)', alias)
    alias_n = int(m.group(1)) if m else None
    one_home = 'the same lines: True' in alias and HOME[0] in alias
    commit_err = [l for l in g(PP, 'log', '--format=%h', PRE_PP + '..HEAD', '--', 'ERRATA.md').split(NL) if l.strip()]
    err_alone = len(commit_err) == 1 and sorted(g(PP, 'show', '--name-only', '--format=', commit_err[0]).split()) == ['ERRATA.md', 'OPEN_TRAILS.md']
    S = dict(
        N1=('HELD' if one_home and alias_n == 5 else 'REFUTED',
            'the statement located by name at %s :%d (“Theorem (Silence Principle)”, REGISTRY 1.5d-2, the record whose role line :6 '
            'presents the formal statement) ; the same theorem restated at FOUNDATIONS_OF_THE_SIDE_PROGRAMME :62 (v0.2.5 :64), which that role '
            'line names as building on it, and read in expository form at SILENCE_OF_FOUNDATIONS :103 and day1 :92 (relay data/b599_reads.txt) '
            '-- printed for the author ; the five sentences reached by the alias and resolved to it: %s' % (HOME[0], HOME[1], alias_n)),
        N2=('HELD' if H['SILENCE']['n_ceils'] <= 6 and H['SILENCE']['n_facts'] <= 4 and H['REPARAM']['n_ceils'] <= 2 and H['REPARAM']['n_facts'] <= 2 else 'REFUTED',
            'SILENCE ceiling %d (at most 6), fact %d (at most 4) ; REPARAM ceiling %d (at most 2), fact %d (at most 2)' % (
                H['SILENCE']['n_ceils'], H['SILENCE']['n_facts'], H['REPARAM']['n_ceils'], H['REPARAM']['n_facts'])),
        N3=('HELD' if all(H[k]['H28a'] == H[k]['H28b'] == H[k]['H28c'] == 'HELD' and H[k]['held'] is None for k in ORDER) else 'REFUTED',
            ' ; '.join('%s H28a %s%s, H28b %s, H28c %s' % (k, H[k]['H28a'], ' (VACUOUS: no MOVED row)' if H[k]['h28a_vacuous'] else '', H[k]['H28b'],
                                                           H[k]['H28c']) for k in ORDER) + ' ; no sentence held'),
        N4=('HELD' if Z.get('placement_added') == 2 and X.get('placement_added') == 2 else 'REFUTED',
            'Placement rows gained on re-emission: ζ %s, χ %s (pages changed: ζ %s, χ %s) -- the generator`s Placement lists files naming a '
            'page node, and neither edition names one' % (Z.get('placement_added'), X.get('placement_added'), Z.get('changed'), X.get('changed'))),
        N5=('HELD' if kern_ok and cur_same and pp_ch == want_pp and relay_beyond == ['tools/b558_record.py'] else 'REFUTED',
            'nothing deposits; kernel mains %s; current versions unedited %s; PLACE-papers %s; relay files beyond the act`s own banks and the '
            'table: %s' % ('unmoved' if kern_ok else kern, cur_same, pp_ch, relay_beyond)),
        S1=('HELD' if (H['SILENCE']['n_worklist'], H['SILENCE']['n_ceils'], H['SILENCE']['n_facts'], H['SILENCE']['n_hist'], H['SILENCE']['n_names'],
                       H['SILENCE']['body_dn']) == (1, 1, 5, 2, 5, 3) else 'REFUTED',
            'SILENCE: work-list %d, ceiling %d, fact %d, history lines %d, names excepted %d, body %+d' % (
                H['SILENCE']['n_worklist'], H['SILENCE']['n_ceils'], H['SILENCE']['n_facts'], H['SILENCE']['n_hist'], H['SILENCE']['n_names'],
                H['SILENCE']['body_dn'])),
        S2=('HELD' if (H['REPARAM']['n_ceils'], H['REPARAM']['n_facts'], H['REPARAM']['n_hist'], H['REPARAM']['body_dn']) == (2, 1, 0, 1) else 'REFUTED',
            'REPARAM: ceiling %d, fact %d, history lines %d, body %+d' % (H['REPARAM']['n_ceils'], H['REPARAM']['n_facts'], H['REPARAM']['n_hist'],
                                                                        H['REPARAM']['body_dn'])),
        S3=('HELD' if Z.get('changed') is False and X.get('changed') is False else 'REFUTED',
            'pages changed by re-emission after the editions: ζ %s, χ %s' % (Z.get('changed'), X.get('changed'))),
        S4=('HELD' if alias_n == 5 and one_home else 'REFUTED', 'alias hits %s, the b598 second shape`s lines, home %s' % (alias_n, one_home)),
        S5=('HELD' if err_alone and er.get('addressed') == 4540 and er.get('ot_line') and er.get('ot_line') > 12326 else 'REFUTED',
            'the erratum and the OPEN_TRAILS line in one commit alone %s (%s) ; the line appended at :%s, addressed to :%s' % (
                err_alone, commit_err, er.get('ot_line'), er.get('addressed'))),
    )
    for k in ORDER:
        S['H28a_' + k] = (H[k]['H28a'], 'VACUOUS: no MOVED row' if H[k]['h28a_vacuous'] else 'the MOVED row cites its fact at its pin')
        S['H28b_' + k] = (H[k]['H28b'], 'body %+d against at most %d' % (H[k]['body_dn'], H[k]['allowed']))
        S['H28c_' + k] = (H[k]['H28c'], 'scanner CLEAN %s ; beyond the ceiling %d' % (H[k]['clean'], H[k]['beyond']))
    put_json('b599_scores.json', S)
    for k in SCORE_KEYS + tuple('H28%s_%s' % (x, d) for d in ORDER for x in 'abc'):
        print('  %-14s %s -- %s' % (k, S[k][0], S[k][1][:200]))


TITLE = ('## CP-7, acts eighteen and nineteen: the editions of SILENCE_STAGES_DEALIGNMENT and REPARAMETERIZATION_BARRIERS from their '
         'banks, the Knill–Laflamme sentence read against knill_laflamme_t1, the Silence Principle reached by alias, b394’s record corrected '
         'by erratum')
TRAIL_HEAD = ('### b599 — lane three, act twenty-six under (R209): CP-7 acts eighteen and nineteen -- the editions of '
              'SILENCE_STAGES_DEALIGNMENT and REPARAMETERIZATION_BARRIERS from their b598 banks; the Silence Principle alias; b394’s erratum')


def _pp_commit(prefix):
    for l in g(PP, 'log', '--format=%h %s', PRE_PP + '..HEAD').split(NL):
        if l.split(' ', 1)[-1].startswith(prefix):
            return l.split(' ', 1)[0]
    return '?'


def findings():
    Q = _Q()
    S, wl, er, wo = jl('b599_scores.json'), jl('b599_weight_line.json'), jl('b599_erratum.json'), jl('b599_work_order.json')
    E = {k: jl('b599_edition_%s.json' % k) for k in ORDER}
    H = {k: jl('b599_h28_%s.json' % k) for k in ORDER}
    Q.guard_absent(Q.FIND, TITLE[:90])
    es, ep = E['SILENCE'], E['REPARAM']
    e = ['', TITLE, '',
         '*Filed at b599 on the author’s ruling `(R209)`. Banks: relay `data/b599_edition_SILENCE.txt`, `data/b599_edition_REPARAM.txt`, '
         '`data/b599_reads.txt`, `data/b599_alias_rerun.txt`, `data/b599_repin_SILENCE.txt`, `data/b599_repin_REPARAM.txt`, '
         '`data/b599_page_arms_c4.txt`, `data/b599_author_answers.txt`. Nothing deposits.*', '',
         '**The editions** (`(R209)`(4), by the form at OPEN_TRAILS :11864, its clauses and the precedence order at :12228). `%s` beside v1.2, '
         'unedited, sha256 `%s`: §9’s Knill–Laflamme row now names the single-error syndrome condition knill_laflamme_t1 states, the check '
         'map’s seven columns nonzero and pairwise distinct, the Knill–Laflamme name kept as the field’s and its link noted as the '
         'docstring’s, not compiled; the Steane names written as the file declares them; the two “no terminal” rows cite d_eff_formula and '
         'silence_yields_protection at SIDE-structural-error-correction v0.2.1 = 6a4f482, T2 as definitional, the general bound and the survey '
         'staying manuscript-resident; the Abstract’s “We prove” read down to the §3 sketch; the five Silence Principle sentences excepted by '
         'name, one history line beneath the first citing the principle’s home; the de-alignment terminals’ profiles stated as printed by '
         'b557’s probes and by no artefact of the kernel’s own, W-ORD-SEC-AXIOM-ARTEFACT named. %d work-list rewrite, %d ceiling, %d fact '
         'corrections, %d history lines, %d collisions listed; body %d against %d (%+d), back matter %d. `%s` beside v0.1, unedited, sha256 '
         '`%s`: the barrier note’s “CURRENT kernel pin” named as current on its date, SIDE-kernel main now 0256e9e with the file’s blob '
         'unchanged; “proved, not conjectured” and “clauses proved rather than asserted” read down to the compiled schema and the '
         'manuscript-resident witness pair; %d ceiling, %d fact corrections, %d collisions; body %d against %d (%+d), back matter %d. H28a-H28c: '
         'SILENCE %s, %s, %s; REPARAM %s (VACUOUS, no MOVED row), %s, %s; no sentence held.' % (
             DOC['SILENCE']['ed'], es['sha256'], H['SILENCE']['n_worklist'], H['SILENCE']['n_ceils'], H['SILENCE']['n_facts'], H['SILENCE']['n_hist'],
             H['SILENCE']['n_collisions'], es['n_body'], es['n_cur'], es['n_body'] - es['n_cur'], es['n_backmatter'],
             DOC['REPARAM']['ed'], ep['sha256'], H['REPARAM']['n_ceils'], H['REPARAM']['n_facts'], H['REPARAM']['n_collisions'], ep['n_body'],
             ep['n_cur'], ep['n_body'] - ep['n_cur'], ep['n_backmatter'], H['SILENCE']['H28a'], H['SILENCE']['H28b'], H['SILENCE']['H28c'],
             H['REPARAM']['H28a'], H['REPARAM']['H28b'], H['REPARAM']['H28c']), '',
         '**The alias and the erratum.** b558’s matcher reads “Silence Principle” on silence_principle, its home named by path, '
         'phase1.5/structural/SILENCE_FORMAL.md :43 (relay d3f32506); re-run on SILENCE_STAGES it reaches the five sentences b598 printed. '
         '%s at ERRATA :%s corrects b394’s “no correspondence table” and its Dark Interface item against the copy b394 read (4cd1cd2, §9 '
         ':196, ten rows); its history line is appended at OPEN_TRAILS :%s, addressed to :4540, by the author’s answer before the seal (the '
         'ruling’s “beneath :4540” the navigator’s, the trails append-only).' % (ERR_ID, er.get('errata_line'), er.get('ot_line')), '',
         '**The pages.** Both re-emitted after the two edition commits, one per call: neither changed, as neither edition names a node of '
         'either page; the page arms and the frozen control 2 of 2 each (relay data/b599_page_arms_c4.txt).', '',
         '**Read in mutual light** (`(R204)`(3)(ii)-(iii)): these editions carry b598’s two banks (FINDINGS :6902) into the documents, b557’s '
         'tiers (:5870) into §9’s two definitional rows, and b394’s reconciliation (OPEN_TRAILS :4540) into a dated correction; they re-read '
         'the Silence Principle’s formal statement (SILENCE_FORMAL :43) as the home the five sentences name, and are re-read by '
         'W-ORD-SEC-AXIOM-ARTEFACT (:%s), whose landing would print the de-alignment profiles from the kernel itself. They strengthen two of the '
         'programme’s offerings: the edition form, now applied to the two keystones b578 held, and the compiled scope of the de-alignment '
         'condition, its every row cited at its pin with its profile’s source named.' % wo.get('line'), '',
         '**The record lines.** b598’s weight at FINDINGS :%d, the items as ruled at :%d; W-ORD-SEC-AXIOM-ARTEFACT at OPEN_TRAILS :%s.' % (
             wl['lines'][0]['line'], wl['lines'][1]['line'], wo.get('line')), '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Next.** Per `(R209)`(5): b600, REMAINDER 5 -- the product lemma -- as the research sequence’s second item, priced at OPEN_TRAILS '
         ':12136. The author rules on the closing.', '',
         '*Nothing deposits; no kernel written; both current versions unedited; README and REGISTRY unwritten; nothing here is a statement '
         'about RH or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    put_json('b599_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE[:90]), title=TITLE, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, TITLE[:90]))


def trail():
    Q = _Q()
    S, fj, wl, er, wo = jl('b599_scores.json'), jl('b599_findings.json'), jl('b599_weight_line.json'), jl('b599_erratum.json'), jl('b599_work_order.json')
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows_ = ['', TRAIL_HEAD, '',
             '**(R209) ratified.** (1) b598 at its weight. (2) The items, ruled. (3) W-ORD-SEC-AXIOM-ARTEFACT. (4) CP-7 acts eighteen and '
             'nineteen, the two editions in one act. (5) The act after: b600.', '',
             '**Entered:** FINDINGS.md:%d (b598’s weight), :%d (the items), :%d (the entry, with its mutual-light line); ERRATA.md %s at :%s; '
             'OPEN_TRAILS.md:%s (the history line addressed to :4540), :%s (W-ORD-SEC-AXIOM-ARTEFACT), this record; PLACE-papers `%s` and `%s`; '
             'relay tools/b558_record.py (the alias, %s).' % (
                 wl['lines'][0]['line'], wl['lines'][1]['line'], fj['entry_line'], ERR_ID, er.get('errata_line'), er.get('ot_line'), wo.get('line'),
                 DOC['SILENCE']['ed'], DOC['REPARAM']['ed'], ALIAS_C), '',
             '**Answered before the seal, by the author** (relay data/b599_author_answers.txt): b394’s history line appended at the end, '
             'addressed to :4540, committed alone with the erratum; no line moves. **Recorded as the navigator’s:** (R209)(2)(ii)’s “beneath '
             ':4540” -- the placement error of (R187)(2) at b587; the ledgers are append-only, and the form’s “beneath” is for edition files.', '',
             '**Resolved by the seat under the precedence order, for the author’s strike:** the collisions of both editions (relay '
             'data/b599_edition_SILENCE.txt, data/b599_edition_REPARAM.txt); the alias put on silence_principle, the terminal named for the '
             'principle; :198’s “All rows pinned to” v0.2.1 corrected by the fact clause (the Steane rows at SIDE-cosmo), a fifth fact '
             'correction; sentences read and left in each back matter.', '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R209)`(5), b600, REMAINDER 5 -- the product lemma -- the research sequence’s second item, priced at :12136; the '
             'author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel written; both current versions unedited; FACES_LEDGER untouched; row U1 '
             'unedited; `h2` where the deposit left it; the four lists stay OPEN.', '']
    r = Q.append_to(Q.OT, NL.join(rows_))
    put_json('b599_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b599_trail.json')['line'])


def desk():
    S = jl('b599_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    HK = tuple('H28%s_%s' % (x, d) for d in ORDER for x in 'abc')
    L = ['=' * 104, 'b599 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### H28a-H28c, each edition.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in HK]
    L += ['', '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b599_defects.txt').rstrip(NL).split(NL)
    put_txt('b599_desk_notes.txt', L)


def components():
    S, fj, tj, wl, er, wo = (jl('b599_scores.json'), jl('b599_findings.json'), jl('b599_trail.json'), jl('b599_weight_line.json'),
                             jl('b599_erratum.json'), jl('b599_work_order.json'))
    E = {k: jl('b599_edition_%s.json' % k) for k in ORDER}
    L = ['b599 -- THE COMPONENTS, BANKED UNDER (R209).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b598`s closing push-out relay %s ; push-b598* branches deleted by name '
         '(data/b599_branches.txt) ; the kept branches untouched ; the Silence Principle alias relay %s (five hits, data/b599_alias_rerun.txt) ; '
         'the suite run at HEAD before the face (data/b599_arms_prerun.txt)' % (STEPZERO, ALIAS_C),
         '### COMPONENT 1 : b598`s weight FINDINGS :%d, the items :%d ; %s at ERRATA :%s and the history line OPEN_TRAILS :%s (addressed to '
         ':4540) ; W-ORD-SEC-AXIOM-ARTEFACT :%s' % (wl['lines'][0]['line'], wl['lines'][1]['line'], ERR_ID, er.get('errata_line'), er.get('ot_line'), wo.get('line')),
         '### COMPONENT 2 : the edition %s (sha256 %s) ; body %d vs %d ; back matter %d ; H28a %s, H28b %s, H28c %s ; no sentence held' % (
             DOC['SILENCE']['ed'], E['SILENCE']['sha256'][:16], E['SILENCE']['n_body'], E['SILENCE']['n_cur'], E['SILENCE']['n_backmatter'],
             S['H28a_SILENCE'][0], S['H28b_SILENCE'][0], S['H28c_SILENCE'][0]),
         '### COMPONENT 3 : the edition %s (sha256 %s) ; body %d vs %d ; back matter %d ; H28a %s (VACUOUS), H28b %s, H28c %s ; no sentence held' % (
             DOC['REPARAM']['ed'], E['REPARAM']['sha256'][:16], E['REPARAM']['n_body'], E['REPARAM']['n_cur'], E['REPARAM']['n_backmatter'],
             S['H28a_REPARAM'][0], S['H28b_REPARAM'][0], S['H28c_REPARAM'][0]),
         '### COMPONENT 4 : both pages re-emitted after the edition commits, one per call: unchanged, nothing to commit ; page arms 2 of 2, control 2 of 2',
         '### COMPONENT 5 : FINDINGS :%d (the entry) ; OPEN_TRAILS :%d (the record) ; next: b600, REMAINDER 5 ; N1 %s, N2 %s, N3 %s, N4 %s, N5 %s' % (
             fj['entry_line'], tj['line'], S['N1'][0], S['N2'][0], S['N3'][0], S['N4'][0], S['N5'][0])]
    put_txt('b599_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b599_record.py <subcommand>')
        sys.exit(2)
    fn(*sys.argv[2:])
    sys.exit(0)
