# -*- coding: utf-8 -*-
"""b590_record.py -- THE ACT'S RECORD TOOL, UNDER (R200). ### ONE SUBCOMMAND PER BANK.

### ### b590: LANE TWO, ACT FOURTEEN -- THE EPSTEIN NEGATIVE CONTROL: THE DETECTOR THEOREM, THE EPSTEIN INSTANCE AT
### INTERFACES, THE WITNESS WINDOW AGAINST THE BENCH; THE SWEEP'S CLAIM-FAMILY COLUMN FILLED; THE DAY-1 SECTION SETTLED.
### Subcommands write only `data/b590_*` unless the docstring names another file. Every bank is written through `put_txt` /
### `put_json` (encode, temp file, `os.replace`). No platform call. The templates are b589_record.py and b573_record.py.
### ### **THIS TOOL CARRIES NO FAMILY TEXT OF (R200)(2).** It reads the family lists from the local-only paste at run time;
### what reaches relay is the count per family.
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
PAT = 'D:/MY-DOwnloads/patent-package-BACKUP-2026-08-29'
GSR = 'D:/SIDE-global-section'
EFK = 'D:/SIDE-explicit-formula'
PRE_PP = '53961af'
PRE_PAT = '433ae01'
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
BRANCH = 'epstein-b590'
SWEEP_FILE = 'SWEEP_TWO_2026-10-01.md'
PASTE_FILE = 'PASTE_b590_R200_2026-10-02.txt'
ARCH = 'archive/2026-08-24-ledger-split/OPEN_TRAILS-archive-2-historical-landings-and-programs.md'
BALPOS = 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md'
DAY1_PIN, DAY1_MD5 = '0b8f435', '1989c5d6650a57728e9ddff25430c9be'
SURR_ED = 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND_v0_5.md'
INDEX_ED = 'phase1.5/proofs/INDEX_ARITY_AT_THE_CRITICAL_LINE_v0_19.md'

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
    '(a) THE REGSPEC GENERATOR`S BLANKET RENAME TURNED TWO CARRIED REFERENCES INTO THIS ACT`S ("EVERY CLAUSE CARRIED FROM b589`s SPEC" '
    'and "the faces of b566-b589"); both were corrected through the Edit tool before the gate first ran, before the seal.',
    '(b) THE FACE`S FIRST DRAFT READ "the Day-1 document", WHICH U-1`S COUNTER READS AS "1 document" (one prediction found); it was '
    'rephrased ("the document the ruling calls Day-1") and the gates re-run before the lock.',
    '(c) THE SWEEP FILL`S FIRST RUNS: two raised before writing (a family marker and the end marker of the paste`s (R200)(2) body sit '
    'at line breaks); the third wrote each family`s whole list into every cell, the paste separating a family`s name from its list '
    'by an em dash where the tool split on " -- ". The file -- the seat`s own uncommitted write -- was restored from its HEAD '
    '(433ae01) by `git checkout --` on its name, the split corrected through the Edit tool, and the fill re-run; the column was '
    'committed once (dc47e76).',
    '(d) THE SALT-CHECK FILE FAILED ITS FIRST THREE BUILDS ON THE SEAT`S PROOF TACTICS, NOT ON A FIELD: a Finite instance not found '
    'for the set literal (and a cascade from the empty configuration`s field), then a Finite argument, then a rewrite against the '
    'unfolded window. Each was corrected in the file and the module rebuilt one per call; the fourth landed. The statements were '
    're-printed (data/b590_statements_salt_final.txt) beside the first print: every header unchanged, one theorem added '
    '(toy_finite). The four logs stand in data/b590_build_salt.txt.',
    '(e) ROWGEN`S DEFINITION-ENCODED FLAG FIRED ON `detector`, reading `baseWidth := 1 / (4 * ...)` as the literal 1 by its prefix rule '
    '(`^(True|False|0|1)\\b`) -- b589`s `1 - σ` again. Its README defines the flag as a body that IS a literal constant; this act`s '
    'tool applies that definition and prints rowgen`s raw flag beside it (data/b590_rowgen_records.txt); rowgen is not edited.',
    '(f) THE FIRST ROWS RUN WROTE ROWS 443-445 AND NOT 442: the act row`s formula carried `|` and corr_row.py refused it before '
    'writing ("THE ROW WOULD LAND AS 8 CELLS, NOT 6"). The uncommitted CORRESPONDENCE.md -- the seat`s own appends -- was restored '
    'from its HEAD (8c392fe) by `git checkout --` on its name, the formula written with `‖`, and all four rows written in order; the '
    'first run`s json is kept in the seat`s scratchpad, its result printed here.',
]


def defects():
    put_txt('b590_defects.txt', ['### b590 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


# ================================================================================ READING (1): THE READS
RELAY = ROOT.replace('\\', '/')
READS = [
    ('SIDE-explicit-formula the schema`s structure and fields', EFK, 'v0.15', 'SIDEExplicitFormula/Schema/Config.lean', list(range(24, 35))),
    ('SIDE-explicit-formula the converse`s witness construction', EFK, 'v0.15', 'SIDEExplicitFormula/Schema/Converse.lean',
     list(range(161, 176)) + list(range(235, 267))),
    ('SIDE-explicit-formula the base width`s witness, the dominant, the tie and kill sets', EFK, 'v0.15', 'SIDEExplicitFormula/PowerWindow.lean',
     [121, 122, 129, 130, 274, 275, 276, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396, 398, 401]),
    ('SIDE-explicit-formula the window, its setup and the coefficients`s degree (L7e as PowerLimit carries it)', EFK, 'v0.15',
     'SIDEExplicitFormula/PowerLimit.lean', list(range(105, 126)) + list(range(245, 253)) + [266, 271, 274, 277, 280, 445] +
     list(range(658, 691))),
    ('SIDE-explicit-formula the plateau', EFK, 'v0.15', 'SIDEExplicitFormula/TwoPropertyWindow.lean', list(range(56, 58))),
    ('SIDE-explicit-formula the count', EFK, 'v0.15', 'SIDEExplicitFormula/RestBound.lean', [44, 45]),
    ('SIDE-explicit-formula the zero configuration and the transform', EFK, 'v0.15', 'Zeta23/Defs.lean', [60, 121, 124] + list(range(136, 147)) + [161]),
    ('relay b554`s sign pattern, the plateau at 33.19', RELAY, 'HEAD', 'data/b554_sign_pattern.txt', list(range(78, 85))),
    ('relay b511`s zero-list loader', RELAY, 'HEAD', 'tools/b511_families.py', [49, 50, 51, 52, 54]),
    ('relay b514`s pair, Q0`s zero at 16.29', RELAY, 'HEAD', 'tools/b514_window.py', [29]),
    ('relay b559`s desk, H9a and H9c', RELAY, 'HEAD', 'data/b559_desk_notes.txt', [7, 9]),
    ('PLACE-papers the literature lines, Bombieri-Lagarias and Weil 1952', PP, PRE_PP, BALPOS, [422, 542]),
    ('PLACE-papers FACES_LEDGER, F7', PP, PRE_PP, 'FACES_LEDGER.md', [26]),
    ('PLACE-papers OPEN_TRAILS, Q0 recorded', PP, PRE_PP, 'OPEN_TRAILS.md', [9789]),
    ('PLACE-papers the document the ruling calls Day-1, at its md5 pin', PP, DAY1_PIN, BALPOS, [1, 3, 19, 32, 43, 45]),
    ('PLACE-papers the archived ledger, Day-1 §II should read', PP, PRE_PP, ARCH, [8755, 8763, 8770]),
    ('PLACE-papers THE_DAY1_IMPLICATIONS, the md5 read', PP, PRE_PP, 'phase2/method/THE_DAY1_IMPLICATIONS.md', [18, 30, 65]),
    ('PLACE-papers SIGN_ARRANGEMENT_RECONCILIATION, the Day-1 row', PP, PRE_PP, 'phase2/method/SIGN_ARRANGEMENT_RECONCILIATION.md', [16]),
    ('PLACE-papers the credit lines', PP, PRE_PP, SURR_ED, [143]),
    ('PLACE-papers the credit lines (INDEX_ARITY)', PP, PRE_PP, INDEX_ED, [61]),
    ('PLACE-papers FINDINGS, the tier law`s programme-premise clause and b589`s entry', PP, PRE_PP, 'FINDINGS.md', [5812, 6718]),
    ('the patent repository, the sweep`s head and table head', PAT, PRE_PAT, SWEEP_FILE, [1, 5, 9, 10]),
    ('relay b589`s closing push-out, its head', RELAY, 'HEAD', 'data/b589_closing_push_out.txt', list(range(1, 4))),
]


def reads():
    L = ['b590 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev + '^{}').strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    put_txt('b590_reads.txt', L)


# ================================================================================ COMPONENT 1: THE RECORD LINES, THE COLUMN, THE SECTION
B589_ENTRY = '## The comprehensive housekeeping act: E_DIFFICULTY_THEOREM'


def weight_line():
    """### PLACE-papers FINDINGS: b589's weight, one appended line addressed to b589's entry."""
    Q = _Q()
    entry = Q.line_of(Q.FIND, B589_ENTRY)
    if entry != 6718:
        sys.exit('### THE ADDRESSED LINE MOVED: entry %s -- NOTHING WRITTEN' % entry)
    head = '*Appended 2026-10-02 by b590 to b589’s entry (:%d), under `(R200)`(1) -- b589 AT ITS WEIGHT:*' % entry
    Q.guard_absent(Q.FIND, head)
    text = ('\n%s the act landed on six of its seven components, the extraction sweep two HELD at the missing .md and written '
            'into the local-only patent repository (433ae01), its claim-family column then blank. E_DIFFICULTY_THEOREM: a four-row '
            'Correspondence table from the tier block’s terminals re-printed at SIDE-kernel v1.1, v1.4 and v1.7 '
            '(sieve_ceiling_semantic at SieveCeilingSemantic.lean :48), superseding b450’s “THERE IS NO TABLE”; the v1.0.4 '
            'edition beside v1.0.3 with the cross-link credit beneath :183, seven ceiling and one fact correction, H28a-H28c held, '
            'the scanner CLEAN. The constellation re-read: 20 tables, 2 cells moved, both the one AMC row whose no_conspiracy '
            'terminals are retired to a comment at SIDE-effects main, as the row says; b454’s table yields three rows newly located '
            'case-insensitively (the cross-link verdict, Face E / keyhole, the Day-1 attribution). **The three-way bench, entered '
            'as a finding: the three definitions of λ_n the kernel proves equal -- the zero sum, the arithmetic limit and Keiper’s '
            'expansion -- are equal on the bench, within floor at every n ≤ 12, 36 of 36 (H30a held).** The Keiper read: Mathlib '
            'holds riemannZeta_residue_one, the constant term γ and the pole-plus-entire split, no Stieltjes constant beyond γ by '
            'name; the Keiper face at two lemmas of substance. The lv re-measure: GammaBounds :177:8 the source error (a rewrite '
            'pattern), 11 dependents failing on it, five modules clean, seven unfinished for memory (4.6 GB free against 2.7 GB '
            'for Mathlib alone), their errors uncounted; the price re-entered. The product lemma: one lemma of substance (the '
            'summed explicit formula) plus bookkeeping, the conjunction free by the schema, the Dedekind naming priced beside; '
            'REMAINDER 5 at OPEN_TRAILS :12136. The PROV1 .docx stands at D:/MY-DOwnloads and was not opened; the find’s timeout '
            'read as silence is b589’s defect (a). The suite reads 78 of 78.\n' % head)
    r = Q.append_to(Q.FIND, text)
    put_json('b590_weight_line.json', dict(entry=entry, line=Q.line_of(Q.FIND, head), head=head, append=r))
    print('  weight line :%s' % Q.line_of(Q.FIND, head))


ROMAN = ('I', 'II', 'III', 'IV', 'V')
# ### each sweep row's instrument, by keys drawn from the row's own instrument cell (public since b589's sweep tool); the
# ### family is the one whose list in the local paste names a key -- read at run time, never written here.
ROW_KEYS = [
    ('the E0 rule file', ['e0 rule file']),
    ('the tier law', ['tier law']),
    ('the four supersession forms and the CONFLICT refusal', ['supersession forms', 'conflict refusal']),
    ('chain_page.py and G-CHAIN-PAGE', ['chain_page.py', 'g-chain-page']),
    ('the as-of commit lines', ['as-of commit lines']),
    ('the tag-after-read-back script', ['tag made after read-back']),
    ('the sealed face with addendum forms', ['sealed face with addendum forms']),
    ('the edition form and its ten clauses', ['edition form']),
    ('the ceiling census and the corroboration census', ['ceiling and corroboration census']),
    ('the scanner`s exception read', ['exception read']),
    ('the lemma walk', ['lemma walk']),
    ('the two-seat relay with hypotheses fixed before computation', ['two-seat relay', 'hypotheses fixed before computation']),
]
CELL_OLD = '(not in the seat`s hands; the author`s paste)'


def _norm(s):
    return re.sub(r'\s+', ' ', s.replace('`', "'").replace('’', "'").lower())


def _families():
    """### the five families' texts from the local paste's (R200)(2) body, keyed by numeral; and the body's digest."""
    t = io.open(os.path.join(PAT, PASTE_FILE), encoding='utf-8').read().replace(chr(13), '')
    body = t[t.index('(2) THE FIVE CLAIM FAMILIES'):t.index('(3) THE DAY-1 SECTION NUMBER.')]
    fam = {}
    at = {r: re.search(r'\(%s\)\s' % r, body).start() for r in ROMAN}
    for i, r in enumerate(ROMAN):
        a = at[r]
        b = at[ROMAN[i + 1]] if i + 1 < len(ROMAN) else re.search(r'No\s+judgement\s+of\s+patentability', body).start()
        fam[r] = ' '.join(body[a:b].split()).rstrip(';').strip()
    return fam, hashlib.sha256(body.encode('utf-8')).hexdigest(), body


def sweep_fill():
    """### patent-package-BACKUP-2026-08-29/SWEEP_TWO_2026-10-01.md: the column filled in place, the families' legend beneath
    ### the table, a dated line; committed alone there by the seat. Relay data/b590_sweep.txt / .json: the count per family."""
    fam, sha, body = _families()
    p = os.path.join(PAT, SWEEP_FILE)
    src = io.open(p, encoding='utf-8').read().replace(chr(13), '')
    lines = src.split(NL)
    rows = [i for i, l in enumerate(lines) if l.startswith('| ') and l.rstrip().endswith(CELL_OLD + ' |')]
    if len(rows) != len(ROW_KEYS):
        sys.exit('### ROWS %d, KEYS %d -- NOTHING WRITTEN' % (len(rows), len(ROW_KEYS)))
    assign = []
    for i, (name, keys) in zip(rows, ROW_KEYS):
        got =[r for r in ROMAN if any(k in _norm(fam[r]) for k in keys)]
        if not got:
            sys.exit('### NO FAMILY NAMES %s -- NOTHING WRITTEN' % name)
        cell = '; '.join('(%s) %s' % (r, re.split(r' — | -- ', fam[r])[0][len('(%s) ' % r):].strip()) for r in got)
        lines[i] = lines[i][:lines[i].rindex(CELL_OLD)] + cell + ' |'
        assign.append(dict(row=name, families=got))
    tbl_end = max(rows) + 1
    legend = ['', '## The families, as the author supplied them at (R200)(2)', '',
              '*The navigator`s reading at the b588 closing, supplied by the author`s ruling (R200)(2) at b590 (2026-10-02) for this '
              'column, quoted from the paste (`%s`); no judgement of patentability is made here; that is counsel`s.*' % PASTE_FILE, '']
    legend += ['- %s' % ' '.join(fam[r].split()) for r in ROMAN]
    legend += ['', '*Column filled at b590 (2026-10-02) under (R200)(2): each instrument row given the family or families whose list '
               'in the ruling names it. Committed alone in this local-only repository.*']
    out = lines[:tbl_end] + legend + lines[tbl_end:]
    b = NL.join(out).encode('utf-8')
    if not b.endswith(b'\n'):
        b += b'\n'
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    counts = {r: sum(1 for a in assign if r in a['families']) for r in ROMAN}
    per_row = [len(a['families']) for a in assign]
    put_txt('b590_sweep.txt', ['b590 -- COMPONENT 1: THE SWEEP`S CLAIM-FAMILY COLUMN, (R200)(2). ### THE COUNT PER FAMILY ONLY (reading (ii)).', '',
                               '### the file: patent-package-BACKUP-2026-08-29/%s (local-only), %d bytes, sha256 %s' % (
                                   SWEEP_FILE, len(b), hashlib.sha256(b).hexdigest()),
                               '### the paste`s (R200)(2) body, read there at run time: sha256 %s' % sha,
                               '### instruments %d ; per family %s ; families per instrument: min %d, max %d' % (
                                   len(assign), ' '.join('(%s) %d' % (r, counts[r]) for r in ROMAN), min(per_row), max(per_row)),
                               '### ### **EVERY INSTRUMENT IN AT LEAST ONE FAMILY: %s ; NONE IN ALL FIVE: %s ; EACH IN EXACTLY ONE: %s.**' % (
                                   min(per_row) >= 1, max(per_row) < 5, min(per_row) == max(per_row) == 1)])
    put_json('b590_sweep.json', dict(file=SWEEP_FILE, bytes=len(b), sha256=hashlib.sha256(b).hexdigest(), body_sha256=sha,
                                     instruments=len(assign), counts=counts, per_row=per_row))


def day1():
    """### the document the ruling calls Day-1, at its md5 pin: the headings, the row, the repaired sentence; the ledger's
    ### line; the credit lines. Relay data/b590_day1.txt / .json."""
    blob = subprocess.run(['git', '-C', PP, 'show', '%s:%s' % (DAY1_PIN, BALPOS)], capture_output=True).stdout
    md5 = hashlib.md5(blob).hexdigest()
    ls = blob.decode('utf-8').split(NL)
    heads = [(i + 1, l) for i, l in enumerate(ls) if l.startswith('## ')]

    def sec(n):
        return [h for h in heads if h[0] <= n][-1]
    row = [i + 1 for i, l in enumerate(ls) if l.startswith('| W_∞ (digamma/Γ)') and 'positive (provable)' in l]
    dom = [i + 1 for i, l in enumerate(ls) if 'the positive archimedean term dominates the indefinite' in l]
    arch = g(PP, 'show', '%s:%s' % (PRE_PP, ARCH)).split(NL)[8769]
    surr = g(PP, 'show', '%s:%s' % (PRE_PP, SURR_ED)).split(NL)[142]
    idx = g(PP, 'show', '%s:%s' % (PRE_PP, INDEX_ED)).split(NL)[60]
    phrase = 'Day-1 BALANCE_AND_POSITIVITY §I attributed the positivity to the archimedean term alone, its `W_∞` row reading'
    row_sec, dom_sec = sec(row[0]) if row else None, sec(dom[0]) if dom else None
    L = ['b590 -- COMPONENT 1: THE DAY-1 SECTION, (R200)(3) -- READ AT THE DOCUMENT`S md5 PIN', '',
         '### the document: PLACE-papers %s @ %s ; md5 of the blob %s ; the pin THE_DAY1_IMPLICATIONS :18 records %s ; %s' % (
             BALPOS, DAY1_PIN, md5, DAY1_MD5, 'EQUAL' if md5 == DAY1_MD5 else '### DIFFERENT'),
         '### its headings (level 2):'] + ['    :%-5d %s' % h for h in heads[:9]] + [
         '### the W_∞ row: %s' % ['    :%d %s' % (n, ls[n - 1]) for n in row],
         '###   under :%d %s' % row_sec if row_sec else '### ROW NOT FOUND',
         '### the sentence the ledger`s repair rewrites: %s' % ['    :%d %s' % (n, ls[n - 1][:240]) for n in dom],
         '###   under :%d %s' % dom_sec if dom_sec else '### SENTENCE NOT FOUND',
         '### the archived ledger :8770 (at %s): %s' % (PRE_PP, arch[:400]),
         '### the credit lines: SURROUND v0.5 :143 carries "§I ... W_∞ row": %s ; INDEX_ARITY v0.19 :61 carries it: %s' % (
             phrase in surr, phrase in idx),
         '', '### ### **THE READING: the row is in %s and the repaired sentence in %s; b450`s "section I" names the row and the ledger`s '
             '"§II" names the sentence -- EACH CITATION NAMES ITS OWN OBJECT; neither is a mis-citation. The credit lines attribute the '
             'row to §I, where it stands: no correction.**' % (row_sec[1] if row_sec else '?', dom_sec[1] if dom_sec else '?')]
    put_txt('b590_day1.txt', L)
    put_json('b590_day1.json', dict(md5=md5, md5_ok=md5 == DAY1_MD5, row=row, row_section=row_sec, sentence=dom, sentence_section=dom_sec,
                                    surr_credit=phrase in surr, index_credit=phrase in idx, arch=arch,
                                    corrected=False))


# ================================================================================ COMPONENTS 2-3: THE STATEMENTS, BEFORE THE BUILD
KFILES = dict(detector='SIDEExplicitFormula/Schema/Detector.lean', epstein='SIDEExplicitFormula/Schema/Epstein.lean',
              salt='SIDEExplicitFormula/Schema/SaltCheckEpstein.lean')
DECL = re.compile(r'^(theorem|def|structure|noncomputable def|abbrev) (\S+)')


def _headers(text):
    """### each declaration's header: from its keyword line to the line holding `:=` or `where` (the statement), printed whole."""
    ls = text.split(NL)
    out = []
    for i, l in enumerate(ls):
        m = DECL.match(l)
        if not m:
            continue
        h = [l]
        j = i
        while not re.search(r':=|\bwhere\b', ls[j]) and j + 1 < len(ls):
            j += 1
            h.append(ls[j])
        out.append(dict(kind=m.group(1), name=m.group(2), line=i + 1, head=NL.join(h)))
    return out


def statements(key, suffix=''):
    """### the statements of one kernel file as written in the working tree of the branch, printed before its build;
    ### data/b590_statements_<key><suffix>.txt / .json, with the time and the file's sha256. With a suffix, a re-print after the
    ### file changed, the first print kept and the headers compared."""
    rel = KFILES[key]
    b = open(os.path.join(EFK, rel), 'rb').read()
    hs = _headers(b.decode('utf-8'))
    L = ['b590 -- THE STATEMENTS OF %s, PRINTED %s (reading (%s))' % (
        rel, 'BEFORE THE BUILD' if not suffix else 'AGAIN AFTER THE FILE CHANGED (the first print kept beside)', 'v' if key == 'detector' else 'vi'), '']
    if suffix:
        first = {d['name']: d['head'] for d in jl('b590_statements_%s.json' % key)['decls']}
        now = {d['name']: d['head'] for d in hs}
        L += ['### against the first print: headers unchanged %s ; changed %s ; added %s ; gone %s' % (
            sorted(n for n in now if first.get(n) == now[n]), sorted(n for n in now if n in first and first[n] != now[n]),
            sorted(set(now) - set(first)), sorted(set(first) - set(now))), '']
    L += [
         '### written at (UTC) %s ; the branch %s (checked out: %s) ; the file`s sha256 %s ; its bytes %d' % (
             utc(), BRANCH, g(EFK, 'branch', '--show-current').strip(), hashlib.sha256(b).hexdigest(), len(b)), '']
    for h in hs:
        L.append('### :%d %s %s' % (h['line'], h['kind'], h['name']))
        L += ['    ' + x for x in h['head'].split(NL)]
    put_txt('b590_statements_%s%s.txt' % (key, suffix), L)
    put_json('b590_statements_%s%s.json' % (key, suffix), dict(file=rel, sha256=hashlib.sha256(b).hexdigest(), at=utc(), decls=hs))


STD3 = ['propext', 'Classical.choice', 'Quot.sound']
NS = 'SIDEExplicitFormula.Schema.'


def prints(key, logpath):
    """### the Lean output of a print run (the watchdog's log, its `  | ` lines), banked as data/b590_prints_<key>.txt / .json."""
    import b569_record as R9
    src = io.open(logpath, encoding='utf-8').read().replace(chr(13), '')
    out = [l[4:] for l in src.split(NL) if l.startswith('  | ')]
    ex = [l for l in src.split(NL) if l.startswith('### EXIT')]
    txt = NL.join(out)
    ax = R9.prints_axioms(txt)
    L = ['b590 -- THE PRINTS (%s): `lake env lean` at SIDE-explicit-formula %s (checked out: %s, HEAD %s), the watchdog`s run' % (
        key, BRANCH, g(EFK, 'branch', '--show-current').strip(), g(EFK, 'rev-parse', '--short=7', 'HEAD').strip()),
         '### %s' % (ex[-1] if ex else '### NO EXIT LINE'), ''] + out
    put_txt('b590_prints_%s.txt' % key, L)
    put_json('b590_prints_%s.json' % key, dict(axioms=ax, sorry=[n for n, a in ax.items() if 'sorryAx' in a],
                                               std3=all(set(a) <= set(STD3) for a in ax.values()), exit=ex[-1] if ex else None,
                                               errors=sum(1 for l in out if ': error' in l or l.startswith('error')), text=txt))
    print('  prints', len(ax), 'std3', all(set(a) <= set(STD3) for a in ax.values()))


def e0(key, pkey=None):
    """### every declaration of one kernel file graded by the shared E0 rule (tools/e0_rule.py) at the branch tip, its print."""
    import b569_record as R9
    import e0_rule as E0
    st = jl('b590_statements_%s_final.json' % key) if os.path.exists(os.path.join(D, 'b590_statements_%s_final.json' % key)) \
        else jl('b590_statements_%s.json' % key)
    P0 = jl('b590_prints_%s.json' % (pkey or key))['axioms']
    tip = g(EFK, 'rev-parse', BRANCH).strip()
    src = g(EFK, 'show', '%s:%s' % (tip, st['file']))
    rows = {}
    L = ['b590 -- THE E0 READ OF %s AT THE BRANCH TIP %s (%s)' % (st['file'], tip[:7], BRANCH)] + E0.RULE_TEXT + [
        '### the file at the tip is the one printed before the build: %s' % (hashlib.sha256(src.encode('utf-8')).hexdigest() == st['sha256']), '']
    for d in st['decls']:
        n = NS + ('SaltCheckEpstein.' if key == 'salt' else '') + d['name']
        kind = 'theorem' if d['kind'] == 'theorem' else 'def'
        head, _ln = R9.header_of(src, d['name'])
        gr, why, _b = E0.grade(head or '', kind)
        ax = P0.get(n)
        rows[n] = dict(grade=gr, why=why, axioms=ax, std3=ax is not None and set(ax) <= set(STD3), head=head, kind=kind)
        L.append('    %-34s %-10s %s  -- %s' % (d['name'], gr, 'std3' if rows[n]['std3'] else ax, (why or '')[:140]))
    gate = all(r['std3'] for r in rows.values()) and all(r['head'] is not None or r['kind'] == 'def' for r in rows.values())
    L.append('### ### **THE GATE: %s** -- declarations %d, theorems %d (DERIVES %d, INTERFACES %d)' % (
        'PASS' if gate else 'FAIL', len(rows), sum(1 for r in rows.values() if r['kind'] == 'theorem'),
        sum(1 for r in rows.values() if r['grade'] == 'DERIVES'), sum(1 for r in rows.values() if r['grade'] == 'INTERFACES')))
    put_txt('b590_e0_%s.txt' % key, L)
    put_json('b590_e0_%s.json' % key, dict(rows=rows, gate=gate, tip=tip, file=st['file'], same_file=hashlib.sha256(src.encode('utf-8')).hexdigest() == st['sha256']))


def h31a():
    """### H31a by the face's predicate (reading (v)): compiled at the standard three, no sorryAx, AND every parameter of the witness
    ### window a named term; refuted by a parameter the statement can only quantify, drawn from a non-constructive step."""
    e = jl('b590_e0_detector.json')
    st = [d for d in jl('b590_statements_detector.json')['decls'] if d['name'] == 'detector'][0]
    det = e['rows'][NS + 'detector']
    conv = g(EFK, 'show', 'v0.15:SIDEExplicitFormula/Schema/Converse.lean').split(NL)
    named_base = 'detectorBase ρ₀' in st['head'] and 'baseWidth ρ₀' in st['head']
    quantified = [p for p in ('(a : List ℝ)', '(j : ℕ)') if p in st['head'] and '∃' in st['head']]
    step = conv[170]
    nonconstr = 'Metric.tendsto_atTop' in step
    compiled = det['std3'] and det['grade'] == 'DERIVES'
    verdict = 'HOLDS' if compiled and named_base and not quantified else 'REFUTED'
    L = ['b590 -- COMPONENT 2: H31a, SCORED BY THE FACE`S PREDICATE (reading (v))', '',
         '### compiled: `detector` prints %s ; E0 %s' % (det['axioms'], det['grade']),
         '### the base named in the statement: %s (detectorBase ρ₀, its half-width baseWidth ρ₀ = 1 / (4 (‖gammaOf ρ₀‖ + 1)))' % named_base,
         '### the parameters the statement can only quantify: %s' % (quantified or 'NONE'),
         '### the step the power comes from: Converse.lean :171 at v0.15 reads `%s` -- %s' % (
             step.strip(), 'Metric.tendsto_atTop over a limit with no rate, the step b559`s H9a found at PowerLimit :1092' if nonconstr else '### NOT THE STEP'),
         '### the list a: coeffList of Pof H (Q j), Q chosen by `choose` from coeffs_exist (Converse.lean :166), its power index the same j',
         '', '### ### **H31a %s%s.**' % (verdict, ' -- in its letter, at the power: the theorem compiles at the standard three and grades '
                                                    'DERIVES with the base width named, and the power and the coefficient list stay '
                                                    'existential' if verdict == 'REFUTED' and compiled else '')]
    put_txt('b590_h31a.txt', L)
    put_json('b590_h31a.json', dict(H31a=verdict, compiled=compiled, named_base=named_base, quantified=quantified, step=step,
                                    nonconstructive=nonconstr))


def h31b():
    """### H31b by the face's predicate (reading (vi)): both salt-check theorems compile at the standard three, the conclusion's
    ### print names `epsteinConfig` and `rhoE`; the conclusion graded INTERFACES by the shared rule. data/b590_h31b.txt / .json."""
    ee, es = jl('b590_e0_epstein.json'), jl('b590_e0_salt.json')
    pr = jl('b590_prints_all.json')
    txt = pr['text']
    sat = es['rows'].get(NS + 'SaltCheckEpstein.epstein_hypotheses_satisfiable', {})
    lb = es['rows'].get(NS + 'SaltCheckEpstein.membership_load_bearing', {})
    con = ee['rows'].get(NS + 'epstein_not_h2_sign_cfg', {})
    i = txt.find(NS + 'epstein_not_h2_sign_cfg :')
    chk = txt[i:i + 700] if i >= 0 else ''
    chk = chk.split(NL + NS)[0]
    names = 'epsteinConfig' in chk and 'rhoE' in chk
    ok = sat.get('std3') and lb.get('std3') and con.get('std3') and con.get('grade') == 'INTERFACES' and names
    L = ['b590 -- COMPONENT 3: H31b, THE SALT-CHECK, SCORED BY THE FACE`S PREDICATE (reading (vi))', '',
         '### epstein_hypotheses_satisfiable : %s (%s) -- the hypotheses of the conclusion hold together: a configuration of rhoE and '
         'its reflection, multiplicity one, its arithmetic side its own zero side, the count with A0 = 2' % (sat.get('axioms'), sat.get('grade')),
         '### membership_load_bearing : %s (%s) -- the empty configuration satisfies the premises and is Weil-positive on classK, so '
         'the conclusion needs the membership' % (lb.get('axioms'), lb.get('grade')),
         '### epstein_not_h2_sign_cfg : %s ; E0 %s -- %s' % (con.get('axioms'), con.get('grade'), con.get('why')),
         '### its #check names epsteinConfig and rhoE: %s' % names] + ['    ' + l for l in chk.split(NL)] + [
         '### the tier: T2-INTERFACES by the weakest link -- the count premise the programme`s own bench reading, the explicit-formula '
         'premise T1-lit (FINDINGS :5812); the premise bundle`s consistency with the actual Z_Q unproved in the kernel.',
         '', '### ### **H31b %s.**' % ('HOLDS' if ok else 'REFUTED')]
    put_txt('b590_h31b.txt', L)
    put_json('b590_h31b.json', dict(H31b='HOLDS' if ok else 'REFUTED', satisfiable=sat, load_bearing=lb, conclusion=con, names=names, check=chk))


# ================================================================================ COMPONENT 5: ROWGEN, THE ROWS, THE SCORES, THE RECORD
TERMS = [('443', 'detector', 'SIDEExplicitFormula/Schema/Detector.lean'),
         ('444', 'not_h2_sign_cfg_of_offline', 'SIDEExplicitFormula/Schema/Detector.lean'),
         ('445', 'epstein_not_h2_sign_cfg', 'SIDEExplicitFormula/Schema/Epstein.lean')]
ROW_ACT = '442'
GRADE_CELL = {
    'detector': '`detector` DERIVES',
    'not_h2_sign_cfg_of_offline': '`not_h2_sign_cfg_of_offline` DERIVES',
    'epstein_not_h2_sign_cfg': '`epstein_not_h2_sign_cfg` INTERFACES on EpsteinPremises (the explicit-formula premise T1-lit, cited; the '
                               'count premise the bench`s); tier T2-INTERFACES by the weakest link (FINDINGS :5812)'}


def rowgen_records():
    """### rowgen's own source-side functions (b560_record.rowgen_record, IMPORTED) over the terminals of record at the branch tip."""
    Q = _Q()
    tip = g(EFK, 'rev-parse', BRANCH).strip()
    pr = jl('b590_prints_all.json')['text']
    recs, ctl = [], (True,)
    for rn, n, rel in TERMS:
        r, ctl = Q.rowgen_record([NS + n], rel, tip, pr)
        recs += r
    # ### rowgen's prefix rule (`^(True|False|0|1)\b`) reads `1 / (4 * ...)` as the literal 1, as b589 found it read `1 - σ`;
    # ### its README defines the flag as a body that IS a literal constant (tools/rowgen/README.md :13-:14). The README's
    # ### definition is applied here, rowgen's raw flag kept beside it; rowgen is not edited.
    for r in recs:
        r['defenc_raw'] = r['defenc']
        rhs = r['defenc_why'].split(':=', 1)[1].strip() if ':=' in r['defenc_why'] else ''
        r['defenc'] = bool(r['defenc_raw']) and rhs in ('0', '1', 'true', 'false', 'True', 'False')
    L = ['b590 -- THE ROWGEN RECORD OF THE TERMINALS OF RECORD AT %s (%s), rowgen`s source-side functions IMPORTED' % (tip[:7], BRANCH),
         '### defenc by the README`s literal-constant definition (a body that IS a literal constant), rowgen`s raw prefix flag beside it', '']
    L += ['    %-30s defenc %-5s (rowgen raw %-5s %s) | check %s' % (r['name'].split('.')[-1], r['defenc'], r['defenc_raw'], r['defenc_why'],
                                                                 bool(r['check'])) for r in recs]
    L += ['### the definition-encoded control on a stub: %s' % (ctl[0],)]
    put_txt('b590_rowgen_records.txt', L)
    put_json('b590_rowgen_records.json', dict(rowgen=recs, control=ctl[0], tip=tip))


def rows():
    """### SIDE-global-section CORRESPONDENCE rows 442-445 through relay tools/corr_row.py (the act row and a row per terminal)."""
    Q = _Q()
    tip = g(EFK, 'rev-parse', 'main').strip()
    tag = g(EFK, 'rev-parse', 'v0.16^{}').strip()
    if tag != tip or not tip.startswith(g(EFK, 'rev-parse', BRANCH).strip()[:7]):
        sys.exit('### main %s, v0.16 %s, the branch %s: NOT LANDED -- NO ROW' % (tip[:7], tag[:7], g(EFK, 'rev-parse', BRANCH).strip()[:7]))
    ee = dict(jl('b590_e0_detector.json')['rows'], **jl('b590_e0_epstein.json')['rows'])
    pr = jl('b590_prints_all.json')['axioms']
    for rn, n, rel in TERMS:
        want = 'INTERFACES' if n.startswith('epstein') else 'DERIVES'
        if ee[NS + n]['grade'] != want or not ee[NS + n]['std3']:
            sys.exit('### %s not graded %s at the standard three: no row' % (n, want))
    for rn in (ROW_ACT,) + tuple(t[0] for t in TERMS):
        if [l for l in Q.rd(Q.CORR).split(NL) if l.startswith('| %s |' % rn)]:
            sys.exit('### ROW %s ALREADY PRESENT' % rn)
    out = []
    act = [ROW_ACT,
           '**THE EPSTEIN NEGATIVE CONTROL** (b590, under (R200)(4)). SIDE-explicit-formula v0.16 = %s: the detector theorem -- for a '
           'configuration of the schema with a point off the line, a window in classK, its base named (the plateau at half-width '
           '1/(4(‖gammaOf ρ₀‖+1))), whose zero side has negative real part, its coefficient list and power existential; and the '
           'Epstein configuration of Z_Q (disc −23) at INTERFACES, its explicit-formula and count fields named premises, the bench`s '
           'off-line zero 0.7979971571786801 + 29.551761098629115 i a membership hypothesis, the configuration not Weil-positive on '
           'classK; the premise bundle`s consistency with the actual Z_Q unproved in the kernel. Nothing here proves RH or GRH or '
           'locates any zero.' % tip[:7],
           'SIDE-explicit-formula SIDEExplicitFormula/Schema/{Detector,Epstein,SaltCheckEpstein}.lean (v0.16 = %s)' % tip[:7],
           '%d declarations print within [propext, Classical.choice, Quot.sound], no sorryAx (relay data/b590_prints_all.txt)' % len(pr),
           ' ; '.join(GRADE_CELL[t[1]] for t in TERMS),
           'LANDED at v0.16 = %s; the salt-check compiled (relay data/b590_h31b.txt); nothing deposits.' % tip[:7]]
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'corr_row.py'), Q.CORR] + act, capture_output=True, text=True, encoding='utf-8')
    out.append(dict(row=ROW_ACT, exit=r.returncode, tail=(r.stdout + r.stderr)[-300:]))
    for rn, n, rel in TERMS:
        head = ' '.join((ee[NS + n]['head'] or '').split()).replace('|', '‖')
        cells = [rn, '**%s** (b590, under (R200)(4)), SIDE-explicit-formula v0.16 = %s: `%s%s %s`.' % (n, tip[:7], NS, n, head),
                 '`SIDE-explicit-formula/%s` (v0.16 = %s) : `%s%s`' % (rel, tip[:7], NS, n),
                 '\'%s%s\' depends on axioms: [%s] (relay data/b590_prints_all.txt)' % (NS, n, ', '.join(pr.get(NS + n) or [])),
                 GRADE_CELL[n],
                 'LANDED at v0.16 = %s; the E0 read at the branch tip (relay data/b590_e0_%s.txt).' % (
                     tip[:7], 'epstein' if n.startswith('epstein') else 'detector')]
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'corr_row.py'), Q.CORR] + cells, capture_output=True, text=True,
                           encoding='utf-8')
        out.append(dict(row=rn, exit=r.returncode, tail=(r.stdout + r.stderr)[-300:]))
    put_json('b590_rows.json', dict(rows=out, act=act))
    print('  rows', [(o['row'], o['exit']) for o in out])


def rowgen_diff():
    """### the terminal rows (443-445) read by rowgen.diff (IMPORTED) against the records."""
    Q = _Q()
    import rowgen as RG
    recs = jl('b590_rowgen_records.json').get('rowgen', [])
    for r in recs:
        r['exists'] = bool(r.get('check'))
        r['axioms'] = ("'%s' depends on axioms: [%s]" % (r['name'], ', '.join(r['axioms'] or []))
                       if isinstance(r.get('axioms'), list) else (r.get('axioms') or ''))
    L = ['b590 -- THE ROWGEN DIFF (rowgen.diff IMPORTED) OF THE RECORDS AGAINST CORRESPONDENCE ROWS 443-445', '']
    res = {}
    for rn, n, rel in TERMS:
        rowtxt = [l for l in Q.rd(Q.CORR).split(NL) if l.startswith('| %s |' % rn)]
        out = RG.diff(recs, NL.join(rowtxt))
        mine = [list(x) for x in out if isinstance(x, tuple) and x[0] == NS + n]
        res[rn] = dict(found=len(rowtxt) == 1, mine=mine)
        L.append('### row %s found: %s' % (rn, len(rowtxt) == 1))
        L += ['    ' + str(x) for x in out]
    ok = all(v['found'] and v['mine'] and all(m[1] == ['ok'] for m in v['mine']) for v in res.values())
    L += ['', '### ### **THE ROWGEN DIFF : %s on all %d rows.**' % ('CLEAN' if ok else 'NOT CLEAN', len(TERMS))]
    put_txt('b590_rowgen.txt', L)
    put_json('b590_rowgen.json', dict(rows=res, clean=ok))


SCORE_KEYS = ('H31a', 'H31b', 'H31c', 'N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'S1', 'S2', 'S3', 'S4', 'S5')
KEPT = {'detection-region-b559': '8faf7de', 'grh-weil-b562': 'de1f175', 'grh-weil-b564': '6ec71b3', 'grh-weil-b567': '6baed63',
        'li-weil-b561': '2df46d7', 'li-weil-b563': '1e4a007', 'residue-discharge-b567': 'fee0781',
        'vendor-bulka-backport-b566': '76c1f11', 'vendor-bulka-forward-b566': 'e5a5a83', 'grh-weil-b569': '19b7d1e',
        'grh-weil-b569-held': '0fdbe65', 'grh-weil-b570': '141e844', 'grh-weil-b571': 'ac157c1', 'grh-weil-b572': '4dce7b9',
        'grh-weil-b573': '21c8c52'}


def scores():
    a, b, W, dy, sw = jl('b590_h31a.json'), jl('b590_h31b.json'), jl('b590_witness_vs_bench.json'), jl('b590_day1.json'), jl('b590_sweep.json')
    kns = [l for l in g(EFK, 'diff', '--name-status', V015, 'main').split(NL) if l.strip()]
    kept = {l.split()[0]: l.split()[1] for l in g(EFK, 'branch', '--format=%(refname:short) %(objectname:short)').split(NL) if l.strip()}
    kept_ok = all(kept.get(k, '').startswith(h) for k, h in KEPT.items())
    added_only = bool(kns) and all(x.startswith('A\t') for x in kns)
    main_tip = g(EFK, 'rev-parse', 'main').strip()
    half, ratio = W['half_pre'], float(W['ratio'])
    dom_16 = abs(float(W['dominant'][1]) - 16.290215720390393) < 1e-6
    S = dict(
        H31a=(a['H31a'], 'the detector compiles at the standard three and grades DERIVES with the base width named; the power and the '
                         'coefficient list stay existential, the power drawn from Metric.tendsto_atTop (Converse.lean :171)'),
        H31b=(b['H31b'], 'both salt-check theorems at the standard three; epstein_not_h2_sign_cfg INTERFACES; its check names '
                         'epsteinConfig and rhoE'),
        H31c=(W['H31c'], 'the witness`s pre-pairing half-width at least 2^D w = %s with D = %d, %s times ln 33.19' % (
            half[:12], W['D'], ('%.6g' % ratio))),
        N1=('REFUTED' if dy['row_section'] and dy['sentence_section'] and dy['row_section'][1].startswith('## I.')
            and dy['sentence_section'][1].startswith('## II.') else 'NOT SCORABLE',
            'the W_∞ row is in §I (:%s), as expected; the ledger`s "§II" names the repaired sentence at :%s, which IS in §II -- '
            'not a mis-citation' % (dy['row'][0], dy['sentence'][0])),
        N2=('HELD' if a['H31a'] == 'HOLDS' else 'REFUTED', 'H31a %s' % a['H31a']),
        N3=('HELD' if b['H31b'] == 'HOLDS' else 'REFUTED', 'H31b %s; the Epstein conclusion grades %s' % (b['H31b'], b['conclusion'].get('grade'))),
        N4=('HELD' if W['H31c'] == 'REFUTED' and ratio > 10 else 'REFUTED', 'H31c %s; the kernel`s half-width at least %s times the bench`s' % (
            W['H31c'], '%.6g' % ratio)),
        N5=('HELD' if min(sw['per_row']) >= 1 and max(sw['per_row']) < 5 else 'REFUTED', 'per family %s; families per instrument %d-%d' % (
            sw['counts'], min(sw['per_row']), max(sw['per_row']))),
        N6=('HELD' if added_only and kept_ok else 'REFUTED', 'nothing deposits; v0.15 against main %s: %s; kept branches %s; nothing about '
                                                              'Epstein`s zeros beyond the INTERFACES conclusion' % (
            main_tip[:7], 'added files only' if added_only else kns, 'unmoved' if kept_ok else '### MOVED')),
        S1=('HELD' if dy['row_section'][1].startswith('## I.') and dy['sentence_section'][1].startswith('## II.') and dy['surr_credit']
            and dy['index_credit'] and not dy['corrected'] else 'REFUTED', 'each citation names its own object; no credit line corrected'),
        S2=('HELD' if a['H31a'] == 'REFUTED' and a['compiled'] and a['named_base'] else 'REFUTED',
            'H31a refuted in its letter at the power; DERIVES with the base width named'),
        S3=('HELD' if b['H31b'] == 'HOLDS' else 'REFUTED', 'both salt-check theorems compile; the conclusion INTERFACES'),
        S4=('HELD' if W['H31c'] == 'REFUTED' and ratio > 10 and dom_16 else 'REFUTED',
            'refuted from below by D alone (ratio %s); the dominant orbit %s, not rhoE`s' % ('%.6g' % ratio, W['dominant'][1][:10])),
        S5=('HELD' if min(sw['per_row']) == max(sw['per_row']) == 1 else 'REFUTED', 'every instrument in exactly one family'),
    )
    put_json('b590_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-4s %s -- %s' % (k, S[k][0], S[k][1][:170]))


TITLE = ('## The Epstein negative control: the detector theorem over a configuration with an off-line zero, the Epstein instance at '
         'INTERFACES, the witness window against the bench’s plateau')
TRAIL_HEAD = ('### b590 — lane two, act fourteen under (R200): the Epstein negative control -- the detector theorem, the Epstein '
              'instance at INTERFACES, the witness window against the bench; the sweep’s column filled; the Day-1 section settled')


def findings():
    Q = _Q()
    S, W, sw, wl = jl('b590_scores.json'), jl('b590_witness_vs_bench.json'), jl('b590_sweep.json'), jl('b590_weight_line.json')
    tip = g(EFK, 'rev-parse', 'main').strip()
    Q.guard_absent(Q.FIND, TITLE[:90])
    e = ['', TITLE, '',
         '*Filed at b590 on the author’s ruling `(R200)`. Banks: relay `data/b590_statements_detector.txt`, `data/b590_prints_all.txt`, '
         '`data/b590_e0_detector.txt`, `data/b590_e0_epstein.txt`, `data/b590_e0_salt.txt`, `data/b590_h31a.txt`, `data/b590_h31b.txt`, '
         '`data/b590_witness_vs_bench.txt`, `data/b590_day1.txt`, `data/b590_sweep.txt`, `data/b590_rowgen.txt`. Nothing deposits; '
         'nothing about the zeros of any Epstein zeta function is asserted beyond the compiled statements’ own words and the bench’s '
         'own numbers.*', '',
         '**The detector theorem** (`(R200)(4)(a)`), SIDE-explicit-formula v0.16 = `%s`, Schema/Detector.lean: for any configuration '
         'of the schema with a point off the line, there are a coefficient list and a power such that the window built on the '
         'kernel’s plateau -- ramp fraction 1/2, half-width 1/(4(|gammaOf ρ₀| + 1)), the witness of base_nonzero_at written into the '
         'statement -- is in classK, its pre-pairing factor supported within 2^j times that half-width, and its zero side of negative '
         'real part. The base is named; the list and the power are not: the power comes from Metric.tendsto_atTop over a limit with '
         'no rate (Converse.lean :171), the step b559 found. H31a %s in its letter at the power.' % (tip[:7], S['H31a'][0]), '',
         '**The Epstein instance** (`(R200)(4)(b)`), Schema/Epstein.lean: Mathlib at de5ce8a9 holds no Epstein zeta and no Hecke '
         'L-function of a class-group character, so Z_Q (x² + xy + 6y², disc −23) enters as named premises -- the explicit formula '
         '(T1-lit, cited at BALANCE_AND_POSITIVITY :542 and :422; the corpus holds no line naming an Epstein- or Hecke-specific '
         'explicit formula) and the local count (the bench’s zero list) -- with the bench’s off-line zero 0.7979971571786801 + '
         '29.551761098629115 i as a membership hypothesis; under them the configuration is not Weil-positive on classK, at the '
         'standard three, the premises passed through, its tier T2-INTERFACES by the weakest link. The salt-check compiled: the '
         'hypotheses hold together on a two-point configuration, and the membership is load-bearing (the empty configuration is '
         'Weil-positive). H31b %s. The premise bundle’s consistency with the actual Z_Q is not proved in the kernel.' % S['H31b'][0], '',
         '**The witness against the bench** (`(R200)(4)(c)`, a READING): at the Epstein data the base half-width is %s; the dominant '
         'off-line orbit at that width is the one at %s, not rhoE’s; the kill set holds %d on-line ordinates, so the power’s floor '
         'read off coeffs_exist is D = %d and the witness’s pre-pairing half-width is at least 2^D times the base, %s -- %s times '
         'b522’s plateau half-width ln 33.19. H31c %s. The least power at which the converse’s own inequality certifies the zero '
         'side negative on the bench is %s.' % (W['w'][:12], W['dominant'][1][:9], W['kill'], W['D'], W['half_pre'][:10],
                                                 '%.4g' % float(W['ratio']), S['H31c'][0], W['jstar']), '',
         '**The sweep’s column** (`(R200)(2)`): filled in the local-only patent repository (dc47e76), every instrument in exactly '
         'one family; the paste’s family text held there (15dd193) and absent from every public bank. **The Day-1 section** '
         '(`(R200)(3)`): the W_∞ row is in §I and the sentence the ledger’s repair rewrites is in §II; each citation names its own '
         'object; the credit lines stand. **b589 at its weight**: FINDINGS :%d.' % wl['line'], '',
         '**The scores.** ' + ', '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Next.** Per `(R200)`(6): b591, the located-clause method document, then the editions resume at RESIDUE.', '',
         '*Nothing deposits; no existing kernel statement changed; v0.15’s files unedited; README, REGISTRY, ERRATA and both pages '
         'unwritten; nothing here is a statement about RH, GRH or any zero beyond the compiled statements’ own words or the bench’s '
         'own numbers.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    put_json('b590_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE[:90]), title=TITLE, append=r))
    print('  FINDINGS entry :%s' % Q.line_of(Q.FIND, TITLE[:90]))


def trail():
    Q = _Q()
    S, fj, wl = jl('b590_scores.json'), jl('b590_findings.json'), jl('b590_weight_line.json')
    tip = g(EFK, 'rev-parse', 'main').strip()
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows_ = ['', TRAIL_HEAD, '',
             '**(R200) ratified.** (1) b589 at its weight. (2) The five claim families supplied for the sweep’s column. (3) The Day-1 '
             'section number. (4) The Epstein negative control: (a) the detector theorem, (b) the Epstein instance at INTERFACES, '
             '(c) the witness window against the bench. (5) The gates. (6) The act after: b591.', '',
             '**Entered:** FINDINGS.md:%d (b589’s weight), :%d (the entry); this record; SIDE-explicit-formula main = **v0.16** = `%s` '
             '(Schema/Detector.lean, Schema/Epstein.lean, Schema/SaltCheckEpstein.lean, AxiomCheckEpstein.lean, added), the branch '
             'epstein-b590 pushed by name; SIDE-global-section CORRESPONDENCE rows 442-445; the local-only patent repository’s paste '
             '(15dd193) and the sweep’s column (dc47e76).' % (wl['line'], fj['entry_line'], tip[:7]), '',
             '**Answered before the seal, by the author:** the relay bank carries the paste verbatim except (R200)(2)’s body, replaced '
             'by a pointer with its digest and location; the whole paste committed alone to the local patent repository. **The '
             'navigator’s placement of claim-family text in a published ferry is recorded as the navigator’s. STANDING, the author’s '
             'line: claim-family text travels in a separate local-only paste from now on.**', '',
             '**Recorded at no cost ((R193)(2)):** (R200)(3)’s reading had no object -- the Day-1 W_∞ row is in §I and the sentence '
             'the archived ledger’s “§II should read” repairs is in §II, so neither citation is a mis-citation; the credit lines stand. '
             'The ruling’s “29.551761 + 0.798i” is b506’s 0.7979971571786801 + 29.551761098629115 i, its parts’ order the navigator’s.', '',
             '**' + ' · '.join('%s %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R200)`(6), b591: the located-clause method document -- a new document, explicitly asked, written from the '
             'ledgers as the method as it was done on the ζ-leg, placed beside the b257 drafts, its title naming the object; then the '
             'editions resume at RESIDUE.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no existing statement changed; no Zeta23 or vendored file edited or added; '
             'ERRATA untouched; FACES_LEDGER untouched; row U1 unedited; `h2` where the deposit left it; the four lists stay OPEN; '
             'nothing here is a statement about RH, GRH or any zero beyond the compiled statements’ own words.', '']
    r = Q.append_to(Q.OT, NL.join(rows_))
    put_json('b590_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r))
    print('  OPEN_TRAILS record :%s' % jl('b590_trail.json')['line'])


def desk():
    S = jl('b590_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5', 'N6')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b590 -- THE DESK. ### **THE HYPOTHESES AND THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### (R200)(4)`S THREE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k.upper(), S[k][0], S[k][1]) for k in ('H31a', 'H31b', 'H31c')]
    L += ['', '### THE NAVIGATOR`S SIX.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)),
          '### ### **(R200)(4) : H31a %s ; H31b %s ; H31c %s.**' % (S['H31a'][0], S['H31b'][0], S['H31c'][0]), '']
    L += rd('b590_defects.txt').rstrip(NL).split(NL)
    put_txt('b590_desk_notes.txt', L)


def components():
    S, W, sw, wl, fj, tj, dy = (jl('b590_scores.json'), jl('b590_witness_vs_bench.json'), jl('b590_sweep.json'), jl('b590_weight_line.json'),
                                jl('b590_findings.json'), jl('b590_trail.json'), jl('b590_day1.json'))
    tip = g(EFK, 'rev-parse', 'main').strip()
    L = ['b590 -- THE COMPONENTS, BANKED UNDER (R200).', '',
         '### COMPONENT 0 : the process listing (two orphan grep monitors stopped by PID) ; b589`s closing push-out relay 0b2cd9f6 ; '
         'push-b589* branches deleted by name (data/b590_branches.txt) ; the kept branches untouched ; the paste held local (15dd193)',
         '### COMPONENT 1 : b589`s weight FINDINGS :%d ; the sweep`s column, per family %s, committed alone (dc47e76) ; the Day-1 '
         'section: the row in %s, the repaired sentence in %s, the credit lines stand ; N1 %s, N5 %s' % (
             wl['line'], sw['counts'], dy['row_section'][1], dy['sentence_section'][1], S['N1'][0], S['N5'][0]),
         '### COMPONENT 2 : the detector theorem on epstein-b590 (58b912a), 8 declarations at the standard three, detector DERIVES ; '
         'H31a %s ; N2 %s' % (S['H31a'][0], S['N2'][0]),
         '### COMPONENT 3 : the Epstein instance (c404e72), the conclusion INTERFACES at the standard three, tier T2-INTERFACES ; the '
         'salt-check compiled (the shared rule reads the salt-check`s membership_load_bearing INTERFACES on the binder inside its '
         'existential, a reading of the rule`s text) ; H31b %s ; N3 %s' % (S['H31b'][0], S['N3'][0]),
         '### COMPONENT 4 : the witness against the bench, D = %d, the half-width at least %s, %s times ln 33.19 ; the dominant orbit '
         '%s ; j* = %s ; H31c %s ; N4 %s' % (W['D'], W['half_pre'][:10], '%.4g' % float(W['ratio']), W['dominant'][1][:9], W['jstar'],
                                              S['H31c'][0], S['N4'][0]),
         '### COMPONENT 5 : main = v0.16 = %s by fast-forward, the tag by the push script ; CORRESPONDENCE rows 442-445 ; FINDINGS :%d ; '
         'OPEN_TRAILS :%d (the record) ; next: b591, the located-clause method document ; N6 %s' % (
             tip[:7], fj['entry_line'], tj['line'], S['N6'][0])]
    put_txt('b590_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b590_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
