# -*- coding: utf-8 -*-
"""b579_record.py -- THE ACT'S RECORD TOOL, UNDER (R189). ### ONE SUBCOMMAND PER BANK.

### ### b579: LANE THREE, ACT SEVEN -- CP-7 ACT FOUR, THE EDITION OF FOUNDATIONS_OF_THE_SIDE_PROGRAMME. Subcommands write only
### `data/b579_*` unless the docstring names another file. Every bank is written through `put_txt` / `put_json` (encode
### first, then a temp file, then `os.replace`). This act makes no platform call. ### The template is b578_record.py.
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
PRE_PP = '292c25b'
MIRROR_PIN = '192077f'
CUR = 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md'
ED = 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md'
PATHS7 = 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md'
PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
WL = 'data/b558_editions/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.txt'

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
    '(a) THE SUITE`S FIRST PRE-PUSH RUN READ 65 OF 66 ON AN ARM OF ITS OWN BUILDING: G-PATHS-VERSION-LINE modelled PATHS v0.7 as ending '
    'in two newlines after the appended section, where the writer ends it, as the section`s last line is blank, in one; the file was read '
    'as written and the arm`s model corrected (its trailing newline dropped). Nothing else changed.',
]


def defects():
    put_txt('b579_defects.txt', ['### b579 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


RELAY = ROOT.replace('\\', '/')
ROWLINES = [354, 355, 357, 358, 360, 361, 368, 370, 373, 376, 382, 383, 384, 386, 389, 390]
READS = [
    ('relay the FOUNDATIONS work-list, whole', RELAY, 'HEAD', WL, list(range(1, 86))),
    ('PLACE-papers FOUNDATIONS, its head', PP, PRE_PP, CUR, list(range(1, 31))),
    ('PLACE-papers FOUNDATIONS, the marked and the ceiling lines', PP, PRE_PP, CUR, [36, 80, 109, 127, 321, 323, 455, 477, 563]),
    ('PLACE-papers FOUNDATIONS, the Correspondence', PP, PRE_PP, CUR, list(range(617, 641))),
    ('PLACE-papers FOUNDATIONS, the Version History and the tier block`s head', PP, PRE_PP, CUR, list(range(651, 666))),
    ('PLACE-papers the zeta page at the mirror`s pin, its pin line and nodes 7, 8, 20', PP, MIRROR_PIN, PAGE, [3, 11, 12, 24]),
    ('PLACE-papers the zeta page, Correspondence rows', PP, MIRROR_PIN, PAGE, [138, 144]),
    ('relay the CP-1b bank, its head and the 16 rows', RELAY, 'HEAD', 'data/b558_cp1b.txt', list(range(1, 9)) + ROWLINES),
    ('PLACE-papers OPEN_TRAILS, b576`s record, the form, b578`s record', PP, PRE_PP, 'OPEN_TRAILS.md', [11836, 11864, 11886]),
    ('PLACE-papers FINDINGS, b578`s entry', PP, PRE_PP, 'FINDINGS.md', [6478]),
    ('relay b578`s edition bank, its head', RELAY, 'HEAD', 'data/b578_edition_PATHS.txt', list(range(1, 9))),
    ('relay tools/banned_terms.py, the stems', RELAY, 'HEAD', 'tools/banned_terms.py', list(range(1, 50))),
    ('relay b578`s closing push-out, its head', RELAY, 'HEAD', 'data/b578_closing_push_out.txt', list(range(1, 4))),
    ('PLACE-papers PATHS v0.7, its version line', PP, PRE_PP, PATHS7, list(range(17, 21))),
]


def reads():
    L = ['b579 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev).strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    put_txt('b579_reads.txt', L)


# ================================================================================ COMPONENT 1 -- THE RESTATEMENTS
H28B_TEXT = ('the edition’s BODY sentence count differs from the current version’s by at most the CREDIT count plus the removals plus '
             'the citations a ruling orders; the back matter is excluded from the count and its own sentence count is printed beside it')
STEM_TEXT = ('a banned stem in a sentence the work-list does not mark is replaced by the object the sentence names (not a synonym for '
             'the stem), the sentence otherwise unchanged, each listed in the back matter with line and both wordings; H28c is scored '
             'on the edition’s text')
CEIL_TEXT = ('a sentence the work-list does not mark that speaks beyond the README ceiling (README :106-:121) takes the object it '
             'names, the rest of the sentence unchanged, each listed in the back matter as a ceiling correction with line and both '
             'wordings; H28c is scored on the edition’s text')
HIST_TEXT = ('dated history entries are superseded beneath, not rewritten: a marked sentence in a dated history entry carries '
             'unchanged as a dated record, and the next version’s history line directly beneath it states what the compiled fact '
             'says, citing it; the row is resolved as MOVED-IN-MEANING by that line, and the line is counted under H28b as a ruled '
             'citation')
FORM_HEAD = '*Appended 2026-10-01 by b577, under the author’s ruling `(R187)`(5)–(6), to the critical path’s lane three'
B576_HEAD = '### b576 — lane three, act four under (R186)'
B578_TRAIL = '### b578 — lane three, act six under (R188)'
B578_ENTRY = '## CP-7, act three: the edition of PATHS_TO_THE_CRITICAL_LINE'


def c1_lines():
    """### PLACE-papers OPEN_TRAILS (four clauses at the form, b576`s score line, the navigator`s wording at b578`s record) and
    ### FINDINGS (b578`s weight)."""
    Q = _Q()
    form = Q.line_of(Q.OT, FORM_HEAD)
    b576 = Q.line_of(Q.OT, B576_HEAD)
    b578 = Q.line_of(Q.OT, B578_TRAIL)
    entry = Q.line_of(Q.FIND, B578_ENTRY)
    if not (form == 11864 and b576 == 11836 and b578 == 11886 and entry == 6478):
        sys.exit('### THE ADDRESSED LINES MOVED: form %s b576 %s b578 %s entry %s -- NOTHING WRITTEN' % (form, b576, b578, entry))
    heads = dict(
        h28b='*Appended 2026-10-01 by b579, under the author’s ruling `(R189)`(2), to the form of an edition (:%d) -- H28b, RESTATED FOR EVERY EDITION ACT:*' % form,
        stem='*Appended 2026-10-01 by b579, under the author’s ruling `(R189)`(3), to the form of an edition (:%d) -- THE STEM CLAUSE, STANDING:*' % form,
        ceil='*Appended 2026-10-01 by b579, under the author’s answer before b579’s seal, to the form of an edition (:%d), beside the stem clause -- THE CEILING CLAUSE:*' % form,
        hist='*Appended 2026-10-01 by b579, under the author’s answer before b579’s seal, to the form of an edition (:%d), beside the stem and ceiling clauses -- THE HISTORY CLAUSE:*' % form,
        b576='*Appended 2026-10-01 by b579 to b576’s record (:%d), under the author’s ruling `(R189)`(4) -- b576’S RE-RUN, CLOSED:*' % b576,
        nav='*Appended 2026-10-01 by b579 to b578’s record (:%d), under the author’s ruling `(R189)`(2):*' % b578,
        weight='*Appended 2026-10-01 by b579 to b578’s entry (:%d), under `(R189)`(1) -- b578 AT ITS WEIGHT:*' % entry,
    )
    for k, h in heads.items():
        Q.guard_absent(Q.FIND if k == 'weight' else Q.OT, h)
    out = []
    out.append(Q.append_to(Q.OT, '\n%s %s.\n' % (heads['h28b'], H28B_TEXT)))
    out.append(Q.append_to(Q.OT, '\n%s %s.\n' % (heads['stem'], STEM_TEXT)))
    out.append(Q.append_to(Q.OT, '\n%s %s. Applied at b579 to FOUNDATIONS_OF_THE_SIDE_PROGRAMME :109, :127 and :477 (“the programme’s RH '
                                 'argument”) and :563 (“RH-core”, as its :621 names it); the navigator’s reading, recorded at b579’s record.\n'
                                 % (heads['ceil'], CEIL_TEXT)))
    out.append(Q.append_to(Q.OT, '\n%s %s. Applied at b579 to FOUNDATIONS_OF_THE_SIDE_PROGRAMME :653 (the v0.2.4 entry).\n' % (heads['hist'], HIST_TEXT)))
    h28b_line = Q.line_of(Q.OT, heads['h28b'])
    out.append(Q.append_to(Q.OT, '\n%s b576’s score is the count at its push, 68 of 69, with the one arm answered by the `(R187)`(4) addendum '
                                 '(:11882); the 66 of 69 re-run of b578 is banked with its causes (relay `data/b578_rerun_diagnosis.txt`) and is '
                                 'not a score; no further re-run is ordered. A reading, not an instrument order: the suite of a sealed act reads '
                                 'the live trees of repositories its as-of lines do not cover (PLACE-papers HEAD among them), so a later re-run '
                                 'is not that act’s score; a sealed act’s suite is reproducible exactly when every tree it reads is pinned by an '
                                 'as-of line, and extending the as-of lines to every read is a priced item for the author’s word, not this act.\n'
                                 % heads['b576']))
    out.append(Q.append_to(Q.OT, '\n%s the wording of `(R187)`(6) for H28b -- the edition’s sentence count against the CREDIT count plus the '
                                 'removals -- is recorded as the navigator’s; H28b stands restated on the body at :%d.\n' % (heads['nav'], h28b_line)))
    out.append(Q.append_to(Q.FIND, '\n%s `phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md` beside v0.6 unedited: 29 work-list rows '
                                   'resolved as 20 sentences, each citing a zeta-page declaration at its pin (or the b538 census line for R3); '
                                   'the pentagon read as the star; ANNEX A :359 standing with the Li equivalence beside it; two CREDIT lines; '
                                   'five stem corrections naming their objects, listed with both wordings; no removals; the diff banked. H28a '
                                   'and H28c held; H28b refuted in letter (34 against 2) with the body up by 3 -- two credits and the ruled '
                                   'citation -- and the back matter the form itself requires adding 31. The navigator’s three readings covered '
                                   '27 of 29. The suite reads 67 of 67.\n' % heads['weight']))
    lines = {k: Q.line_of(Q.FIND if k == 'weight' else Q.OT, h) for k, h in heads.items()}
    put_json('b579_c1_lines.json', dict(form=form, b576=b576, b578=b578, entry=entry, lines=lines, heads=heads, appends=out))
    print(lines)


# ================================================================================ COMPONENT 2 -- THE EDITION
PIN = {  # ### the declaration, and its pin AS THE ZETA PAGE PRINTS IT (reading (v))
    'ch_iff_rh': 'v0.1 = `baed4df`', 'h2_sign_iff_rh': 'v0.2 = `5c72cad`', 'li_nonneg_iff_rh': 'v0.9 = `e5a5a83`',
    'mellin_Phi_eq_zero_of_re_le_one': 'v0.11 = `19b7d1e`', 'silence_universal_restated': 'v0.11 = `19b7d1e`',
}
NS = {'ch_iff_rh': 'B321', 'h2_sign_iff_rh': 'B321', 'li_nonneg_iff_rh': 'LiCriterionBridge',
      'mellin_Phi_eq_zero_of_re_le_one': 'RegisterDepth', 'silence_universal_restated': 'RegisterDepth'}
PAGE_NODE = {'ch_iff_rh': 7, 'h2_sign_iff_rh': 8, 'li_nonneg_iff_rh': 20}
PAGE_ROW = {'mellin_Phi_eq_zero_of_re_le_one': 138, 'silence_universal_restated': 144}
EF = 'SIDE-explicit-formula'
H2 = '`h2_sign_iff_rh`, %s %s' % (EF, PIN['h2_sign_iff_rh'])
CH = '`ch_iff_rh`, %s %s' % (EF, PIN['ch_iff_rh'])
LI = '`li_nonneg_iff_rh`, %s %s' % (EF, PIN['li_nonneg_iff_rh'])
MP = '`mellin_Phi_eq_zero_of_re_le_one`, %s at the page’s pin %s' % (EF, PIN['mellin_Phi_eq_zero_of_re_le_one'])
SU = '`silence_universal_restated`, %s at the page’s pin %s' % (EF, PIN['silence_universal_restated'])
COS = '`∀ s : ℤ, (1 : ℚ) ^ s = 1`'
CPB = 'relay `data/b558_cp1b.txt` :%d'
SDARK = ('The arithmetic s-darkness content is **manuscript-resident** at `ProductFormula.conservation_of_spectra` (SIDE-kernel, the '
         'Conservation-of-Spectra chapter), not in this model — cite that terminal for content.')


def sdark(n):
    return ('The arithmetic s-darkness content is **manuscript-resident** (the Conservation-of-Spectra chapter), in neither this model '
            'nor `ProductFormula.conservation_of_spectra` (SIDE-kernel), which states only %s, T2 (%s) — no terminal carries it.' % (COS, CPB % n))


# ### (line, the fragment of the line replaced, its replacement) -- a table row keeps its cells; the fragment is the cell text moved
REWRITES = [
    (26, 'with the universal form `silence_universal` machine-verified in MetaKernel.lean (Kernel/SilenceTheorem.lean);',
     'with the universal form `silence_universal` compiled in MetaKernel.lean (Kernel/SilenceTheorem.lean) under the programme’s own '
     'premise `I.is_universal` (T2-INTERFACES), whose truth the programme has still to establish, and restated as %s, which concludes '
     '`I.kappa_zero` from that premise alone;' % SU),
    (26, 'Spectral Inertness is formally verified in Lean 4 against Mathlib (terminal `ProductFormula.conservation_of_spectra`, '
         '`{propext, Classical.choice, Quot.sound}`; supported by the ProductFormula chain)',
     'Spectral Inertness is manuscript-resident: the terminal cited for it, `ProductFormula.conservation_of_spectra` (`{propext, '
     'Classical.choice, Quot.sound}`), states only %s, T2, and mentions no Euler product and no zeta (%s)' % (COS, CPB % 355)),
    (30, 'RH holds here only **under the same single open premise** `h2` (§VI.5;',
     'RH holds here only **under the same single open premise**, `h2_sign`, and `h2_sign` is equivalent to RH (%s), so the condition is '
     'RH itself (§VI.5;' % H2),
    (36, "which is the programme's single open premise `h2` (goal ⇐ h1 ∧ h2, h1 complete at Φ, only h2 open; explained not counted at §VI.5).",
     "which is the programme's single open premise `h2_sign`, equivalent to RH (%s), so the condition is RH itself, while lv’s goal "
     "state `goal ⇐ h1 ∧ h2` (h1 complete at Φ) closes nothing on the strip, its h2 at Φ, `mellin Φ (s/2) ≠ 0`, being false at every s "
     "with re s ≤ 1 (%s; explained not counted at §VI.5)." % (H2, MP)),
    (80, "but `T3prime` also requires `h2` — that Φ's Mellin factor is nonvanishing off the line, i.e. that the catalogue is exhaustive "
         "at the interface — and `h2` is the single open premise, carried openly, not supplied by Determination.",
     "but `T3prime` also requires lv’s `h2` — that Φ's Mellin factor `mellin Φ (s/2)` is nonvanishing — and that hypothesis is false "
     "at every s with re s ≤ 1 (%s), so the single open premise, carried openly and not supplied by Determination, is `h2_sign`, "
     "equivalent to RH (%s)." % (MP, H2)),
    (80, 'So the joint exclusion closes **under `h2`** — goal ⇐ h1 ∧ h2, only h2 open — not outright.',
     'So the joint exclusion does not close on the strip under lv’s goal state `goal ⇐ h1 ∧ h2`, its h2 at Φ being false there (%s), '
     'and the clause it turns on is `h2_sign`, equivalent to RH (%s).' % (MP, H2)),
    (321, "This is `h2` — **the premise that every ξ-zero forces the Euler balance at some prime** (the conservation register; "
          "equivalently realization-totality at the ξ interface, the R4 positivity face, or the goal state's `mellin Φ (s/2) ≠ 0`; "
          "one premise in §27.3's five registers).",
     "This is `h2_sign`, equivalent to RH (%s), and the forms once named beside it are separate statements, not one premise: **the "
     "premise that every ξ-zero forces the Euler balance at some prime** (the conservation register, the deposit’s Route 3 clause) is RH "
     "restated (%s, E-2026-09-25-1), the R4 positivity face is RH in the Li form (%s), and the goal state's `mellin Φ (s/2) ≠ 0` is "
     "false at every s with re s ≤ 1 (%s)." % (H2, CH, LI, MP)),
    (323, 'h2 leaves it open (goal ⇐ h1 ∧ h2, only h2 open).',
     'the clause `h2_sign` leaves it open, being equivalent to RH (%s), while lv’s goal state `goal ⇐ h1 ∧ h2` closes nothing on the '
     'strip (%s).' % (H2, MP)),
    (455, '— provides Conservation of Spectra ($n_4 = 0$) via `ProductFormula.conservation_of_spectra`, and',
     '— provides `ProductFormula.conservation_of_spectra`, which states only %s, T2 (%s), Conservation of Spectra ($n_4 = 0$) being '
     'manuscript-resident, and' % (COS, CPB % 373)),
    (563, 'Conservation of Spectra ($n_4 = 0$) via `ProductFormula.conservation_of_spectra`;',
     'Conservation of Spectra ($n_4 = 0$) manuscript-resident, the terminal cited for it, `ProductFormula.conservation_of_spectra`, '
     'stating only %s, T2 (%s);' % (COS, CPB % 376)),
    (626, SDARK, sdark(382)),
    (627, SDARK, sdark(383)),
    (628, SDARK, sdark(384)),
    (628, '| SIDE-silence-principle v0.1.0 |',
     '| SIDE-silence-principle v0.1.0 (`silence_principle`), v0.2.0 = `667c254` (`Universal.silence_universal`, absent at v0.1.0, %s) |'
     % (CPB % 386)),
    (634, '| DERIVES — Compiled |',
     '| DERIVES its own statement only, %s, T2 (%s) — Spectral Inertness / Conservation is manuscript-resident |' % (COS, CPB % 389)),
]
# ### reading (viii), the author's answer: :653 carries; the history line directly beneath it
HISTORY = (653, '*v0.2.5 — 2026-10-01 (the CP-7 edition, b579, beneath the v0.2.4 entry above, which stays as a dated record): the '
                'arithmetic content is manuscript-resident, and `ProductFormula.conservation_of_spectra` states %s, T2 (%s).*' % (COS, CPB % 390))
# ### reading (vii), the author's answer: the version line above the previous one
VERSION = (17, '*v0.2.5 — 2026-10-01*')
# ### reading (vi), the author's answer: each takes the object the sentence names
CEILS = [
    (109, 'load-bearing for the RH proof —', "load-bearing for the programme's RH argument —"),
    (127, 'load-bearing instance for the RH proof.', "load-bearing instance for the programme's RH argument."),
    (477, "**The RH proof's structural logic", "**The programme's RH argument's structural logic"),
    (563, '— RH proof core;', '— RH-core;'),
]
# ### reading (x): the seat's hand-read, by row id -- 1 (a) h2, 2 (b) conservation_of_spectra, 3 (c) Route 3, 0 none
ASSIGN = {'FOUND:26:301': 0, 'FOUND:26:302': 2, 'FOUND:30:304': 1, 'FOUND:36:305': 1, 'FOUND:80:307': 1, 'FOUND:80:308': 1,
          'FOUND:321:315': 1, 'FOUND:323:317': 1, 'FOUND:455:320': 2, 'FOUND:563:323': 2, 'FOUND:626:329': 2, 'FOUND:627:330': 2,
          'FOUND:628:331': 2, 'FOUND:628:333': 0, 'FOUND:634:336': 2, 'FOUND:653:337': 2}
ALSO_C = {'FOUND:321:315'}
READING_NAME = {0: 'none -- resolved by the form', 1: '(a) h2 takes its compiled name', 2: '(b) conservation_of_spectra rewritten to what it states',
                3: '(c) the Route 3 clause'}
MATCHER = {1: r'`h2`|\bh2\b', 2: r'conservation_of_spectra[\s\S]*(?:[Cc]ompiled|verified)|(?:[Cc]ompiled|verified)[\s\S]*conservation_of_spectra'}
CEILING = re.compile(r'RH proved|RH is proved|h2_sign proved|λ_n ≥ 0 proved|GRH reduced|GRH proved|reduction machine-verified|proof of RH|proves RH|RH proof')
CEIL_RECORD = 'ceiling correction record:'
BM_TAG = '<!-- b579 (R189) THE v0.2.5 EDITION`S BACK MATTER, 2026-10-01 -->'


def _cp():
    import b558_record as CP
    return CP


def _segs(l):
    return [s for s in _cp().segments(l) if s]


def _count(lines):
    return sum(len(_segs(l)) for l in lines)


def _rows():
    return [r for r in jl('b558_cp1b.json')['rows'] if r['doc'] == 'FOUND' and r['verdict'] == 'MOVED-IN-MEANING']


def _status_blanks(lines):
    """### every table whose header names a Status column, read cell by cell: the line of each blank Status cell."""
    out, hdr = [], None
    for i, l in enumerate(lines, 1):
        s = l.strip()
        if not s.startswith('|'):
            hdr = None
            continue
        cells = [c.strip() for c in s.strip('|').split('|')]
        if hdr is None:
            hdr = [c.lower().strip('* ') for c in cells]
            continue
        if set(s.replace('|', '').replace(':', '').replace('-', '').strip()) == set():
            continue
        for k, h in enumerate(hdr):
            if h.startswith('status') and (k >= len(cells) or not cells[k]):
                out.append(i)
    return out


def _cur():
    cur = g(PP, 'show', '%s:%s' % (PRE_PP, CUR)).split(NL)
    return cur[:-1] if cur and cur[-1] == '' else cur


def edition(*a):
    """### PLACE-papers phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME_v0_2_5.md, created beside the current version from
    ### its blob at 292c25b. ### `again` rewrites an edition this act already wrote (never a committed one)."""
    cur = _cur()
    if g(PP, 'rev-parse', 'HEAD:' + CUR).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip():
        sys.exit('### THE CURRENT VERSION MOVED SINCE 292c25b -- NOTHING WRITTEN')
    edp = os.path.join(PP, *ED.split('/'))
    if os.path.exists(edp) and 'again' not in a:
        sys.exit('### THE EDITION FILE EXISTS -- NOTHING WRITTEN')
    if g(PP, 'ls-files', ED).strip():
        sys.exit('### THE EDITION FILE IS COMMITTED -- NOTHING WRITTEN')
    new = list(cur)
    for ln, old, rep in REWRITES:
        line = new[ln - 1]
        if line.count(old) != 1:
            sys.exit('### :%d -- THE FRAGMENT IS NOT ON ITS LINE EXACTLY ONCE (%d): %s' % (ln, line.count(old), old[:80]))
        n0 = len(_segs(line))
        new[ln - 1] = line.replace(old, rep)
        if len(_segs(new[ln - 1])) != n0:
            sys.exit('### :%d -- THE REWRITE CHANGED THE LINE`S SEGMENT COUNT %d -> %d' % (ln, n0, len(_segs(new[ln - 1]))))
    for ln, old, rep in CEILS:
        line = new[ln - 1]
        if line.count(old) != 1:
            sys.exit('### :%d -- THE CEILING FRAGMENT IS NOT ON ITS LINE EXACTLY ONCE: %s' % (ln, old))
        n0 = len(_segs(line))
        new[ln - 1] = line.replace(old, rep)
        if len(_segs(new[ln - 1])) != n0:
            sys.exit('### :%d -- THE CEILING CORRECTION CHANGED THE SEGMENT COUNT' % ln)
    if len(_segs(HISTORY[1])) != 1 or len(_segs(VERSION[1])) != 1:
        sys.exit('### THE HISTORY OR VERSION LINE IS NOT ONE SEGMENT')
    if not cur[VERSION[0] - 1].startswith('*v0.2.4 — 2026-07-29*') or not cur[HISTORY[0] - 1].startswith('*v0.2.4 — 2026-07-29 (Correspondence'):
        sys.exit('### THE VERSION OR HISTORY ANCHOR IS NOT WHERE THE FACE SAYS')
    rows = _rows()
    diff = []
    for r in rows:
        ln = r['line']
        olds = _segs(cur[ln - 1])
        k = olds.index(r['sentence'])
        if ln == HISTORY[0]:
            nw, carried = HISTORY[1], True
        else:
            nw, carried = _segs(new[ln - 1])[k], False
        cites = [d for d in PIN if ('`%s`' % d) in nw and PIN[d] in nw]
        banks = re.findall(r'relay `data/[^`]+` :\d+', nw)
        diff.append(dict(id=r['id'], line=ln, terminal=r['terminal'], old=r['sentence'], new=nw, changed=nw != r['sentence'],
                         carried=carried, reading=ASSIGN[r['id']], also_c=r['id'] in ALSO_C,
                         matcher=[m for m, p in MATCHER.items() if re.search(p, r['sentence'])],
                         cites=cites, banks=banks, supports=r['reading']))
    # ### the insertions, bottom up so the line numbers above stay the current version's
    new[HISTORY[0]:HISTORY[0]] = ['', HISTORY[1]]
    new[VERSION[0] - 1:VERSION[0] - 1] = [VERSION[1], '']
    body = list(new)
    ed_lines = {d: [i for i, l in enumerate(body, 1) if ('`%s`' % d) in l and PIN[d] in l] for d in PIN}
    bank_lines = sorted(set(int(x) for l in body for x in re.findall(r'relay `data/b558_cp1b\.txt` :(\d+)', l)))
    bm = ['', BM_TAG, '',
          '## Back matter of the v0.2.5 edition -- written 2026-10-01 by b579 under the author’s ruling `(R189)`(5), by the form of `(R187)`(5)',
          '',
          '*This file is v0.2.5 of FOUNDATIONS_OF_THE_SIDE_PROGRAMME, the CP-7 edition written beside v0.2.4 (`%s`, unedited) from v0.2.4’s '
          'tier block (its :663) and its CP-1b work-list (relay `%s`), the zeta page as its spine; it does not deposit and does not replace '
          'v0.2.4, and its promotion is CP-8’s.*' % (CUR, WL), '',
          '### Removals', '',
          'None: every one of the 16 work-list rows resolves to a sentence that says what its compiled fact says -- 14 sentences rewritten '
          'in place, and the v0.2.4 history entry (:653) carried as a dated record with the v0.2.5 history line beneath it.', '',
          '### Stem corrections', '',
          'None: the banned-stem scan of v0.2.4 reads 0 live uses, so the stem clause has no use in this edition.', '',
          '### Ceiling corrections', '',
          '| v0.2.4 line | v0.2.4 wording | v0.2.5 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in CEILS:
        bm.append('| :%d | %s %s | %s | corrected under the author’s answer before b579’s seal (the ceiling clause) |' % (ln, CEIL_RECORD, old, rep))
    bm += ['', '### History', '',
           '| v0.2.4 line | entry | v0.2.5 | Status |', '|:--|:--|:--|:--|',
           '| :653 | the v0.2.4 entry, 2026-07-29 | carried unchanged as a dated record; the v0.2.5 history line directly beneath it cites '
           'relay `data/b558_cp1b.txt` :390 | superseded beneath, not rewritten (the history clause) |',
           '| :17 | the version line, v0.2.4 -- 2026-07-29 | kept beneath the v0.2.5 version line, as history | the author’s answer before '
           'b579’s seal |',
           '', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
           '| this edition, v0.2.5 | `%s` | written at b579 |' % ED,
           '| the current version, v0.2.4 | `%s` | unedited |' % CUR,
           '| the spine | `%s` at PLACE-papers `%s` | read, unedited |' % (PAGE, MIRROR_PIN),
           '| the work-list | relay `%s` | read |' % WL,
           '| the CP-1b readings | relay `data/b558_cp1b.txt` | read |',
           '| the sentence-by-sentence diff | relay `data/b579_edition_FOUNDATIONS.txt` | banked at b579 |',
           '', '### Correspondence', '',
           '| declaration or bank line | repository | pin as the zeta page prints it | the page’s line | Status |', '|:--|:--|:--|:--|:--|']
    for d in PIN:
        where = ('node %d, line %d' % (PAGE_NODE[d], PAGE_NODE[d] + 4)) if d in PAGE_NODE else ('Correspondence row, line %d' % PAGE_ROW[d])
        bm.append('| `SIDEExplicitFormula.%s.%s` | %s | %s | %s | cited at :%s of this edition |' % (
            NS[d], d, EF, PIN[d].replace('`', ''), where, ', :'.join(str(x) for x in ed_lines[d]) or '### NONE'))
    for n in bank_lines:
        at = [i for i, l in enumerate(body, 1) if ('relay `data/b558_cp1b.txt` :%d' % n) in l]
        bm.append('| `data/b558_cp1b.txt` :%d | relay | the CP-1b bank (b558) | not on the page | cited at :%s of this edition |' % (
            n, ', :'.join(str(x) for x in at)))
    bm.append('')
    full = body + bm
    b = (NL.join(full) + NL).encode('utf-8')
    open(edp + '.tmp', 'wb').write(b)
    os.replace(edp + '.tmp', edp)
    print('  written: %s (%d bytes, %d lines)' % (ED, len(b), len(full)))
    n_cur, n_body, n_full = _count(cur), _count(body), _count(full)
    put_json('b579_edition.json', dict(path=ED, cur=CUR, cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip(),
                                       lines_cur=len(cur), lines_body=len(body), lines_full=len(full),
                                       n_cur=n_cur, n_body=n_body, n_full=n_full, n_backmatter=n_full - n_body,
                                       credit=0, removals=0, ruled_citations=1, version_lines=1, diff=diff,
                                       ceils=CEILS, history=dict(after=HISTORY[0], text=HISTORY[1]), version=dict(above=VERSION[0], text=VERSION[1]),
                                       sha256=hashlib.sha256(b).hexdigest(), status_blanks=_status_blanks(full),
                                       cited_lines=ed_lines, bank_lines=bank_lines))
    print('  counts: current %d ; body %d ; whole %d ; back matter %d' % (n_cur, n_body, n_full, n_full - n_body))


def edition_bank():
    """### The sentence-by-sentence diff, the ceiling corrections, the counts, the ceiling read, H28a-H28c: data/b579_edition_FOUNDATIONS.txt."""
    E = jl('b579_edition.json')
    edp = os.path.join(PP, *ED.split('/'))
    ed = io.open(edp, encoding='utf-8').read().replace(chr(13), '').split(NL)
    scan = rd('b579_edition_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    hits = []
    for i, l in enumerate(ed, 1):
        for m in CEILING.finditer(l):
            rec_row = l.startswith('| :') and CEIL_RECORD in l
            hits.append(dict(line=i, hit=m.group(0), ctx=l[max(0, m.start() - 60):m.end() + 20], record=rec_row))
    beyond = [h for h in hits if not h['record']]
    h28a_bad = [d['id'] for d in E['diff'] if not d['changed'] or not (d['cites'] or d['banks'])]
    h28a = 'HELD' if not h28a_bad else 'REFUTED'
    body_dn = E['n_body'] - E['n_cur']
    allowed = E['credit'] + E['removals'] + E['ruled_citations']
    h28b = 'HELD' if abs(body_dn) <= allowed else 'REFUTED'
    h28c = 'HELD' if (live and int(live.group(1)) == 0 and clean and not beyond) else 'REFUTED'
    cur0 = g(PP, 'show', '%s:%s' % (PRE_PP, CUR)).split(NL)
    L = ['b579 -- COMPONENT 2: THE EDITION OF FOUNDATIONS_OF_THE_SIDE_PROGRAMME, (R189)(5), BY THE FORM OF (R187)(5)', '',
         '### the current version : PLACE-papers %s @ %s (blob %s), %d lines ; head :1 "%s" ; :17 "%s"' % (
             CUR, PRE_PP, E['cur_blob'][:8], E['lines_cur'], cur0[0], cur0[16]),
         '### its tier block : :663 "%s"' % cur0[662][:110],
         '### the edition : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines_full'], E['sha256']), '',
         '### THE WORK-LIST, ROW BY ROW (16 rows, 15 sentences, 13 lines) -- each row: the line, the terminal, the reading it falls '
         'under (the seat`s hand-read), the declarations or bank lines its sentence cites, the sentence before and after.', '']
    for d in E['diff']:
        L += ['  %s :%d `%s` -- %s%s ; cites %s%s%s' % (d['id'], d['line'], d['terminal'], READING_NAME[d['reading']],
                                                       ' and (c) the Route 3 clause' if d['also_c'] else '',
                                                       ['%s (%s)' % (c, PIN[c].replace('`', '')) for c in d['cites']],
                                                       (' ; bank ' + ', '.join(d['banks'])) if d['banks'] else '',
                                                       ' ; CARRIED, the history line beneath it (the author`s answer)' if d['carried'] else ''),
              '      work-list: %s' % d['supports'],
              '      v0.2.4 : %s' % d['old'], '      v0.2.5 : %s' % d['new'], '']
    cov = [d for d in E['diff'] if d['reading']]
    mat = [d for d in E['diff'] if d['matcher']]
    L += ['### (N1) COVERAGE BY THE READINGS OF (R189)(5), the seat`s hand-read: %d of %d rows -- (a) %d, (b) %d, (c) within (a) %d ; '
          'uncovered %s, resolved by the form' % (len(cov), len(E['diff']), sum(d['reading'] == 1 for d in E['diff']),
                                                  sum(d['reading'] == 2 for d in E['diff']), sum(d['also_c'] for d in E['diff']),
                                                  [':%d `%s`' % (d['line'], d['terminal']) for d in E['diff'] if not d['reading']]),
          '### the matcher`s yield, printed as lineage and not the count: %d of %d rows (a bare h2 for (a); the words compiled or verified '
          'beside the terminal for (b), the ruling`s letter) -- (a) %d, (b) %d' % (
              len(mat), len(E['diff']), sum(1 in d['matcher'] for d in E['diff']), sum(2 in d['matcher'] for d in E['diff'])),
          '', '### THE CEILING CORRECTIONS (reading (vi), the author`s answer):']
    L += ['    :%d  "%s" -> "%s"' % tuple(s) for s in E['ceils']]
    L += ['### THE STEM CORRECTIONS: none (0 live uses in v0.2.4).',
          '### THE VERSION LINE (reading (vii)): above v0.2.4 :%d: %s' % (E['version']['above'], E['version']['text']),
          '### THE HISTORY LINE (reading (viii)): beneath v0.2.4 :%d: %s' % (E['history']['after'], E['history']['text']),
          '### CREDIT LINES: none (CREDIT 0). ### REMOVALS: none.', '',
          '### THE COUNTS (relay tools/b558_record.py `segments`, imported): the current version %d ; the edition`s body %d (%+d: the '
          'version line 1 and the history line 1) ; the back matter %d ; the edition whole %d' % (
              E['n_cur'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b as restated (R189)(2): the body differs by %+d against CREDIT %d + removals %d + ruled citations %d = %d ; the version '
          'line is the author`s ruled line and is not a citation' % (body_dn, E['credit'], E['removals'], E['ruled_citations'], allowed),
          '### no blank Status cell: %s' % ('HELD' if not E['status_blanks'] else '### BLANK AT %s' % E['status_blanks']),
          '', '### THE CEILING (reading (xii)), every hit in the edition:']
    L += ['    :%d "%s" -- %s -- ...%s...' % (h['line'], h['hit'], 'quoted in a ceiling correction record of the back matter, read by the seat'
                                          if h['record'] else '### BEYOND THE CEILING', h['ctx']) for h in hits] or ['    none']
    L += ['### sentences beyond the ceiling: %d' % len(beyond),
          '### the banned-stem scan of the edition (relay data/b579_edition_termscan.txt): live uses %s ; verdict %s' % (
              live.group(1) if live else '?', 'CLEAN' if clean else 'NOT CLEAN'), '',
          '### ### **H28a %s -- every MOVED row resolves to a sentence citing a declaration on the page at its pin, or a bank line%s.**' % (
              h28a, '' if not h28a_bad else ' -- refuted at %s' % h28a_bad),
          '### ### **H28b %s -- as restated, the body differs by %+d sentences against at most %d; the back matter %d, excluded and '
          'printed%s.**' % (h28b, body_dn, allowed, E['n_backmatter'],
                            '' if h28b == 'HELD' else ' -- refuted in letter by the ruled version line'),
          '### ### **H28c %s -- live banned stems %s, sentences beyond the ceiling %d.**' % (h28c, live.group(1) if live else '?', len(beyond)),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**']
    put_txt('b579_edition_FOUNDATIONS.txt', L)
    put_json('b579_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, h28a_bad=h28a_bad, body_dn=body_dn, allowed=allowed,
                                   backmatter=E['n_backmatter'], live=int(live.group(1)) if live else None, beyond=len(beyond), hits=hits,
                                   covered=len(cov), matcher=len(mat), uncovered=[d['id'] for d in E['diff'] if not d['reading']], held=None))
    H = jl('b579_h28.json')
    print(H['H28a'], H['H28b'], H['H28c'], 'covered', H['covered'], 'body_dn', body_dn, 'beyond', H['beyond'])


# ================================================================================ COMPONENT 2, reading (vii): PATHS v0.7's version line
P7_OLD19 = 'Version **v0.6 — 2026-07-24**'
P7_LINE = 'Version **v0.7 — 2026-10-01**'
P7_TAG = '<!-- b579 THE v0.7 VERSION LINE, 2026-10-01 -->'


def paths_version():
    """### PLACE-papers phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE_v0_7.md: the version line above :19 and one back-matter section."""
    p = os.path.join(PP, *PATHS7.split('/'))
    committed = g(PP, 'show', '%s:%s' % (PRE_PP, PATHS7))
    now = io.open(p, encoding='utf-8', newline='').read()
    if now != committed:
        sys.exit('### PATHS v0.7 DIFFERS FROM ITS BLOB AT 292c25b -- NOTHING WRITTEN')
    ls = committed.split(NL)
    if not ls[18].startswith(P7_OLD19) or P7_TAG in committed or not committed.endswith('|' + NL + NL):
        sys.exit('### :19 IS NOT THE v0.6 VERSION LINE, OR THE SECTION EXISTS -- NOTHING WRITTEN')
    new = ls[:18] + [P7_LINE, ''] + ls[18:]
    if new[-1] == '':
        new = new[:-1]
    add = [P7_TAG, '', '### Version line', '',
           '| line | before | after | Status |', '|:--|:--|:--|:--|',
           '| :19 | the version line read v0.6 (“%s ...”) | “%s” inserted above it, with a blank line; the v0.6 line kept beneath it as '
           'history, now at :21 | corrected 2026-10-01 by b579 under the author’s answer before b579’s seal |' % (P7_OLD19, P7_LINE), '',
           '*Every line of this edition from the v0.6 version line on now sits two lines lower than it did when b578 wrote it; the line '
           'numbers cited in the Correspondence table above, and in relay `data/b578_edition_PATHS.txt`, are those of the edition as b578 '
           'wrote it.*', '']
    full = new + add
    b = NL.join(full).encode('utf-8') + (b'' if full[-1] == '' else NL.encode())
    if not b.endswith(NL.encode()):
        b += NL.encode()
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    after = io.open(p, encoding='utf-8').read().split(NL)
    L = ['b579 -- COMPONENT 2, READING (vii): PATHS v0.7`S VERSION LINE, AS THE AUTHOR ANSWERED', '',
         '### PLACE-papers %s @ %s (blob %s), %d lines; :19 read "%s ..."' % (PATHS7, PRE_PP, g(PP, 'rev-parse', '%s:%s' % (PRE_PP, PATHS7)).strip()[:8],
                                                                         len(ls), ls[18][:40]),
         '### written: :19 "%s", :20 blank, :21 "%s ..." (the v0.6 line, kept as history)' % (after[18], after[20][:40]),
         '### the section appended at the end:'] + ['    ' + x for x in add] + [
         '### lines before %d ; after %d ; sha256 %s' % (len(ls), len(after), hashlib.sha256(b).hexdigest())]
    put_txt('b579_paths_version.txt', L)
    put_json('b579_paths_version.json', dict(path=PATHS7, before_lines=len(ls), after_lines=len(after), line19=after[18], line21=after[20],
                                             added=add, sha256=hashlib.sha256(b).hexdigest()))


# ================================================================================ THE SCORING AND THE RECORD
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3', 'S4', 'S5')
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c'}


def scores():
    H, E = jl('b579_h28.json'), jl('b579_edition.json')
    ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'ls-files', '--others', '--exclude-standard', 'phase1.5')).split(NL) if x.strip()))
    kmain = g('D:/SIDE-explicit-formula', 'rev-parse', 'main').strip()
    heads_ok = all(g('D:/' + r, 'rev-parse', 'main').strip().startswith(h) for r, h in PRE_HEADS.items())
    cur_same = g(PP, 'hash-object', CUR).strip() == E['cur_blob']
    n2 = H['H28a'] == 'HELD' and H['H28b'] == 'HELD' and H['H28c'] == 'HELD'
    n3 = H['held'] is None
    n4 = H['body_dn'] == E['credit']
    n5_core = kmain == V015 and heads_ok and cur_same
    extra = [x for x in ch if x not in ('FINDINGS.md', 'OPEN_TRAILS.md', ED)]
    S = dict(
        N1=('HELD' if H['covered'] >= 11 else 'REFUTED', 'the readings of (R189)(5) cover %d of the 16 MOVED rows by the seat`s hand-read; '
            'uncovered %s, resolved by the form; the matcher`s yield %d, printed as lineage' % (H['covered'], H['uncovered'], H['matcher'])),
        N2=('HELD' if n2 else 'REFUTED', 'H28a %s, H28c %s; H28b as restated %s (the body %+d against at most %d)%s' % (
            H['H28a'], H['H28c'], H['H28b'], H['body_dn'], H['allowed'],
            '' if n2 else ' -- refuted in letter by the version line the author ruled, which is not a citation')),
        N3=('HELD' if n3 else 'REFUTED', 'the edition lands; no sentence HELD'),
        N4=('HELD' if n4 else 'REFUTED', 'the body grows by %+d; CREDIT %d; the growth is the ruled version line and the ruled history line'
            % (H['body_dn'], E['credit'])),
        N5=('HELD' if (n5_core and not extra) else 'REFUTED', 'nothing deposits; no kernel touched (%s); the current FOUNDATIONS unedited (%s); '
            'PLACE-papers changed at %s -- %s' % ('held' if kmain == V015 and heads_ok else '### MOVED', 'held' if cur_same else '### EDITED', ch,
                                                  'PATHS v0.7 gained its version line and one back-matter section, as the author answered, '
                                                  'which the expectation`s list does not name' if extra else 'nothing beyond the list')),
        S1=('HELD' if H['covered'] == 14 and H['uncovered'] == ['FOUND:26:301', 'FOUND:628:333'] else 'REFUTED',
            '14 of 16; uncovered the silence_universal rows at :26 and :628'),
        S2=('HELD' if (H['H28a'] == 'HELD' and H['H28c'] == 'HELD' and H['H28b'] == 'REFUTED' and H['body_dn'] == 2 and H['allowed'] == 1) else 'REFUTED',
            'H28a and H28c held; H28b refuted in letter, +2 against 1'),
        S3=('HELD' if n3 else 'REFUTED', 'the edition lands, no sentence held'),
        S4=('HELD' if (not n4 and H['body_dn'] == 2) else 'REFUTED', '(N4) refuted: +2, the version line and the history line'),
        S5=('HELD' if (n5_core and extra == [PATHS7]) else 'REFUTED', '(N5) refuted in letter by PATHS v0.7`s version line; its other clauses hold'),
        counts=dict(pp_changed=ch, body_dn=H['body_dn'], covered=H['covered']),
    )
    put_json('b579_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-5s %s' % (k, S[k][0]))


TITLE_HEAD = '## CP-7, act four: the edition of FOUNDATIONS_OF_THE_SIDE_PROGRAMME from its tier block and work-list'
TITLE = TITLE_HEAD + '; written as v0.2.5 beside v0.2.4, no sentence held'
TRAIL_HEAD = ('### b579 — lane three, act seven under (R189): CP-7 act four -- the edition of FOUNDATIONS_OF_THE_SIDE_PROGRAMME written '
              'beside the current; H28b restated on the body; the stem, ceiling and history clauses standing; b576’s re-run closed')
NAV_READING = ('the ceiling clause -- an unmarked sentence beyond the README ceiling takes the object it names, listed in the back matter '
               '-- is the navigator’s reading, entered at the author’s answer before b579’s seal')


def records_pp():
    Q = _Q()
    S, H, E, C1, PV = jl('b579_scores.json'), jl('b579_h28.json'), jl('b579_edition.json'), jl('b579_c1_lines.json'), jl('b579_paths_version.json')
    ln = C1['lines']
    Q.guard_absent(Q.FIND, TITLE_HEAD)
    e = ['', TITLE, '',
         '*Filed at b579 on the author’s ruling `(R189)`. Banks: relay `data/b579_edition_FOUNDATIONS.txt` (the sentence-by-sentence diff), '
         '`data/b579_edition.json`, `data/b579_paths_version.txt`. Nothing deposits.*', '',
         '**The edition** (`(R189)`(5)): `%s`, v0.2.5, written beside v0.2.4 (`%s`, unedited) from v0.2.4’s tier block and its CP-1b '
         'work-list, the zeta page as its spine. The 16 work-list rows resolve to 15 sentences on 13 lines: 14 are rewritten in place to '
         'what their compiled facts say -- `h2` named by its compiled name `h2_sign` and cited to the equivalence with RH; lv’s h2 at Phi '
         'said false on the strip; the conservation terminal said to state only its one-line identity, cited to the CP-1b bank by line; the '
         'Route 3 clause cited as RH restated; the universal Silence form cited to its restatement on the page under its own premise -- and '
         'the v0.2.4 history entry carries as a dated record with the v0.2.5 history line beneath it. Four unmarked sentences that spoke '
         'beyond the ceiling take the object each names. No CREDIT line (CREDIT 0); no stem correction (0 live); no sentence removed and '
         'none held.' % (ED, CUR), '',
         '**The counts.** v0.2.4 %d sentences; v0.2.5 %d (the body %d, the back matter %d); the body differs by %+d against CREDIT plus '
         'removals plus ruled citations, %d.' % (E['n_cur'], E['n_full'], E['n_body'], E['n_backmatter'], H['body_dn'], H['allowed']), '',
         '**H28a %s · H28b %s · H28c %s.** Coverage of the 16 rows by the readings of `(R189)`(5): %d.' % (H['H28a'], H['H28b'], H['H28c'], H['covered']), '',
         '**The restatements** (`(R189)`(2)-(4)): H28b restated on the body (OPEN_TRAILS :%d); the stem clause standing (:%d); the ceiling '
         'clause (:%d) and the history clause (:%d), the author’s answers; b576’s score 68 of 69 at its push, the re-run closed, the '
         'reproducibility reading (:%d); the navigator’s wording (:%d). **PATHS v0.7** gains its version line, as the author answered '
         '(:19, the v0.6 line kept beneath it at :21; relay `data/b579_paths_version.txt`).' % (
             ln['h28b'], ln['stem'], ln['ceil'], ln['hist'], ln['b576'], ln['nav']), '',
         '**A reading, the navigator’s:** %s.' % NAV_READING, '',
         '**The scores.** (N1) %s, (N2) %s, (N3) %s, (N4) %s, (N5) %s; the seat’s (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
         % tuple(S[k][0] for k in SCORE_KEYS), '',
         '**Next.** Per `(R189)`(6): the edition of ADDITIVE_MULTIPLICATIVE_CONSPIRACY by the same form; the author rules on the closing.', '',
         '*Nothing deposits; no kernel touched; v0.2.4, README, REGISTRY and both pages unwritten; nothing here is a statement about RH, GRH '
         'or any zero beyond the compiled statements’ own words.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows = ['', TRAIL_HEAD, '',
            '**(R189) ratified.** (1) b578 at its weight. (2) H28b restated on the body. (3) The stem clause standing. (4) b576’s re-run '
            'closed. (5) The edition of FOUNDATIONS_OF_THE_SIDE_PROGRAMME by the form, four readings entered. (6) The act after.', '',
            '**Entered:** FINDINGS.md:%d (b578’s weight), :%d (the entry); OPEN_TRAILS.md:%d (H28b restated), :%d (the stem clause), :%d '
            '(the ceiling clause), :%d (the history clause), :%d (at b576’s record: the re-run closed), :%d (at b578’s record: the '
            'navigator’s wording), this record; PLACE-papers `%s` (created); `%s` (its version line and one back-matter section).' % (
                ln['weight'], Q.line_of(Q.FIND, TITLE_HEAD), ln['h28b'], ln['stem'], ln['ceil'], ln['hist'], ln['b576'], ln['nav'], ED, PATHS7), '',
            '**Answered before the seal, by the author:** the four unmarked sentences beyond the ceiling take the object each names; the '
            'edition is v0.2.5, its version line above the v0.2.4 line, and PATHS v0.7 takes its own version line the same way; the dated '
            'v0.2.4 history entry carries, superseded beneath. **Recorded as the navigator’s:** %s.' % NAV_READING, '',
            '**(N1) %s · (N2) %s · (N3) %s · (N4) %s · (N5) %s.** The seat’s own: (S1) %s, (S2) %s, (S3) %s, (S4) %s, (S5) %s.'
            % tuple(S[k][0] for k in SCORE_KEYS), '',
            '**For the author:** H28b as restated bounds the body by CREDIT plus removals plus ruled citations (here 1, the history line); '
            'the body grows by %+d, the second sentence being the v0.2.5 version line the author ruled, which is not a citation, so H28b is '
            'refuted in letter by it. PATHS v0.7’s lines from :19 on sit two lower than its own Correspondence column cites; the appended '
            'section says so.' % H['body_dn'], '',
            '**Next:** per `(R189)`(6), CP-7 act five, b580 -- the edition of ADDITIVE_MULTIPLICATIVE_CONSPIRACY by the same form, H28a-H28c '
            'scored; the author rules on the closing.', '',
            '**No `sorry` on any `main`.** Nothing deposits; no kernel touched; the pages untouched; row U1 unedited; the four lists stay '
            'OPEN; nothing here is a statement about RH, GRH or any zero.', '']
    r2 = Q.append_to(Q.OT, NL.join(rows))
    put_json('b579_findings.json', dict(entry_line=Q.line_of(Q.FIND, TITLE_HEAD), title=TITLE, append=r))
    put_json('b579_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r2))
    print(jl('b579_findings.json')['entry_line'], jl('b579_trail.json')['line'])


def desk():
    S = jl('b579_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b579 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b579_defects.txt').rstrip(NL).split(NL)
    put_txt('b579_desk_notes.txt', L)


def components():
    S, H, E, C1, fj, tj = (jl('b579_scores.json'), jl('b579_h28.json'), jl('b579_edition.json'), jl('b579_c1_lines.json'),
                           jl('b579_findings.json'), jl('b579_trail.json'))
    ln = C1['lines']
    L = ['b579 -- THE COMPONENTS, BANKED UNDER (R189).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b578`s closing push-out relay 4b7eda1f ; push-b578* branches deleted by '
         'name (data/b579_branches.txt) ; the kept branches untouched',
         '### COMPONENT 1 : OPEN_TRAILS :%d (H28b restated), :%d (the stem clause), :%d (the ceiling clause), :%d (the history clause), '
         ':%d (b576`s re-run closed), :%d (the navigator`s wording) ; b578`s weight FINDINGS :%d' % (
             ln['h28b'], ln['stem'], ln['ceil'], ln['hist'], ln['b576'], ln['nav'], ln['weight']),
         '### COMPONENT 2 : the edition %s ; 14 sentences rewritten, 1 carried with its history line, 4 ceiling corrections, the version '
         'line, 0 credit lines, 0 stem corrections, 0 removals ; data/b579_edition_FOUNDATIONS.txt ; H28a %s H28b %s H28c %s ; N1 %s N2 %s '
         'N3 %s N4 %s ; PATHS v0.7`s version line (data/b579_paths_version.txt)' % (ED, H['H28a'], H['H28b'], H['H28c'], S['N1'][0], S['N2'][0],
                                                                                 S['N3'][0], S['N4'][0]),
         '### COMPONENT 3 : FINDINGS :%d ; OPEN_TRAILS :%d (the record) ; next: the edition of ADDITIVE_MULTIPLICATIVE_CONSPIRACY ; N5 %s'
         % (fj['entry_line'], tj['line'], S['N5'][0])]
    put_txt('b579_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b579_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
