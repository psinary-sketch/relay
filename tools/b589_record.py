# -*- coding: utf-8 -*-
"""b589_record.py -- THE ACT'S RECORD TOOL, UNDER (R199). ### ONE SUBCOMMAND PER BANK.

### ### b589: LANE THREE, ACT SEVENTEEN -- THE COMPREHENSIVE HOUSEKEEPING ACT: E_DIFFICULTY_THEOREM'S TABLE AND EDITION; THE
### CONSTELLATION RE-READ; THE EXTRACTION SWEEP TWO (HELD at the missing file, drafted to the patent repo); THE THREE-WAY BENCH,
### THE KEIPER READ, THE lv RE-MEASURE; THE PRODUCT LEMMA PRICED. Subcommands write only `data/b589_*` unless the docstring names
### another file. Every bank is written through `put_txt` / `put_json` (encode, temp file, `os.replace`). No platform call.
### The template is b588_record.py.
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
KER = 'D:/SIDE-kernel'
EFK = 'D:/SIDE-explicit-formula'
LVK = 'D:/SIDE-lv-conservation'
MATHLIB = 'D:/SIDE-explicit-formula/.lake/packages/mathlib'
PRE_PP = 'b378167'
MIRROR_PIN = '192077f'
CUR = 'phase2/method/E_DIFFICULTY_THEOREM.md'
ED = 'phase2/method/E_DIFFICULTY_THEOREM_v1_0_4.md'
TECHNE_ED = 'phase1.5/method/TECHNE_TOOLKIT_v8_3.md'
WL = 'data/b558_editions/E_DIFFICULTY_THEOREM.txt'
ARCH = 'archive/2026-08-24-ledger-split/OPEN_TRAILS-archive-2-historical-landings-and-programs.md'
ARCH_DIR = 'archive/2026-08-24-ledger-split'
SWEEP_FILE = 'SWEEP_TWO_2026-10-01.md'
WT = 'D:/b589-lv-remeasure'

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
    '(a) THE PRE-SEAL SEARCH FOR THE PROVISIONAL SPECIFICATION WAS INCOMPLETE, AND THE FACE STATES IT TOO STRONGLY: the `find` over '
    'D:/MY-DOwnloads passed the foreground limit, was moved to the background, and its output was read as empty; the face says the file '
    'is "on no reachable drive". The reads bank`s walk (data/b589_reads.txt) finds D:/MY-DOwnloads/PROV1_FORMATION_VERIFICATION_ARCHITECTURE.docx '
    '-- a .docx of the name, not the .md the ruling names. Component 3 stays HELD as the author answered; the .docx was not opened or '
    'edited, and the closing puts it before the author.',
    '(b) THE FIRST RE-PRINT LOOKED FOR `sieve_ceiling_semantic` IN SieveCeiling.lean ONLY and printed NOT FOUND at v1.4 and v1.7; it is '
    'declared in Kernel/Cascade/SieveCeilingSemantic.lean :48 at both tags. The tool was corrected through the Edit tool and the bank '
    're-written before the edition, whose guard refuses a row for a terminal that did not re-print.',
    '(c) THE CONSTELLATION TOOL`S FIRST RUNS READ RESOLUTION LIMITS AS MOVED CELLS: candidate kernels too narrow (b586`s column only), the '
    'first resolving pin taken, structure fields unread, rowgen`s prefix rule reading `1 - σ` as the literal 1, branch-held pins compared '
    'with main, b556`s tier block not stopped, nested sections read twice. Each was corrected through the Edit tool (the federation index, '
    'every cited pin in turn, fields, the README`s literal-constant definition, the branch head as the current pin, every cascade tier '
    'block stopped, each line read once), six non-terminal names hand-read with reasons, and all twenty documents re-run with the final '
    'tool; the earlier banks were overwritten by the re-run.',
    '(d) COMPONENT 5`S BANK WAS WRITTEN WHILE COMPONENT 4(c)`S FIRST BUILD RAN IN THE BACKGROUND -- out of the written order by one bank; '
    'no input of either touches the other.',
    '(e) THE THREE-WAY BANK`S FIRST RUN RAISED ON A FORMAT OF A TUPLE BEFORE WRITING; corrected through the Edit tool and re-run.',
    '(f) THE FIRST lv BUILD RAN WITHOUT A MEMORY WATCHDOG: Genus5.lean elaborated for 22 minutes and lean.exe passed the 2.5 GB hold '
    '(2361 MB resident, 7611 MB committed, free memory 1650 MB) before the seat stopped lean, both lakes and the runner by PID; the runner '
    'then gained a watchdog (lean`s committed memory over 3000 MB or free memory under 1500 MB stops the build and records it), and the '
    'remaining modules ran under it one per call; the module importing Genus5 was not re-run.',
    '(g) THAT WATCHDOG READ THE WRONG MEASURE: lean`s committed memory reaches 3.5-3.8 GB on Windows from importing Mathlib alone, so a '
    '3000 MB committed cap stopped every module during its import (most after 16 seconds) and measured nothing; the criterion became '
    'lean`s resident set over 3000 MB or free memory under 1500 MB, and the twenty-three modules were re-run, their logs overwritten.',
    '(h) THE FREE-MEMORY FLOOR OF 1500 MB STILL STOPPED SIX MODULES AT THEIR MATHLIB IMPORT (lean resident about 2.7 GB, free 1.36-1.49 '
    'GB, most after 32 seconds), the import footprint of this machine and not a module`s growth; those six were re-run with the floor '
    'at 900 MB and the resident cap at 3500 MB, set from the measured footprint. Genus5 stays as stopped: it grew to 7611 MB committed '
    'over 22 minutes.',
    '(i) THE SUITE`S FIRST RUN FAILED G-EDIFF-TABLE LIVE ON ITS OWN ARM, NOT ON THE TABLE: the arm`s name list filtered the tier terminals '
    'on a throwaway variable that held the pins, so it counted the contentful ceiling beside the four tier-block terminals; the arm was '
    'corrected through the Edit tool to filter on the row, and the suite re-run whole.',
]


def defects():
    put_txt('b589_defects.txt', ['### b589 -- THIS ACT`S OWN DEFECTS (the seat`s), as they occur.'] + (['    ' + d for d in DEFECTS] or ['    NONE']))


RELAY = ROOT.replace('\\', '/')
READS = [
    ('relay the E_DIFFICULTY_THEOREM work-list, whole', RELAY, 'HEAD', WL, list(range(1, 16))),
    ('PLACE-papers E_DIFFICULTY_THEOREM, whole', PP, PRE_PP, CUR, list(range(1, 259))),
    ('PLACE-papers INVARIANCE_BARRIERS v1.4, the house form of a Correspondence table (its header and a row)', PP, PRE_PP,
     'phase1.5/method/INVARIANCE_BARRIERS_v1_4.md', [499, 500, 501, 502, 503]),
    ('relay b586`s corroboration census, the roster tables and the list of 19', RELAY, 'HEAD', 'data/b586_corroboration.txt', list(range(7, 35))),
    ('relay rowgen`s README, its modes', RELAY, 'HEAD', 'tools/rowgen/README.md', list(range(1, 40))),
    ('PLACE-papers OPEN_TRAILS, b454`s ledger table and the verdict`s index line', PP, PRE_PP, 'OPEN_TRAILS.md', [773] + list(range(6755, 6767))),
    ('PLACE-papers the archived landing, the verdict whole', PP, PRE_PP, ARCH, list(range(8837, 8848))),
    ('relay b454`s shapes, fixed at its registration', RELAY, 'HEAD', 'data/b454_registration_2026-09-14.txt', list(range(79, 92))),
    ('PLACE-papers VERIFICATION_LOOM, the provisional specifications register', PP, PRE_PP, 'VERIFICATION_LOOM.md', list(range(3209, 3217))),
    ('PLACE-papers TECHNE_TOOLKIT v8.3, the credit beneath its :240', PP, PRE_PP, TECHNE_ED, [242]),
    ('relay b257`s methodology sweep, its head', RELAY, 'HEAD', 'data/b257_methodology_sweep.txt', list(range(1, 12))),
    ('PLACE-papers BALANCE_AND_POSITIVITY, the channel map, C.7`s headings and the validation table', PP, PRE_PP,
     'phase1.5/spectral/BALANCE_AND_POSITIVITY.md', [86, 88, 283, 287, 289, 291, 292, 293, 294, 295, 477, 489, 498, 516]),
    ('relay b562`s drift bank, table (i)', RELAY, 'HEAD', 'data/b562_drift.txt', list(range(10, 28))),
    ('relay b563`s per-n bank', RELAY, 'HEAD', 'data/b563_per_n.txt', list(range(1, 25))),
    ('relay b557`s tier block for E_DIFFICULTY', RELAY, 'HEAD', 'data/b557_tiers.txt', list(range(591, 632))),
    ('PLACE-papers OPEN_TRAILS, the toolchain item, the research items, W-ORD-GRH-WEIL`s remainders, the form`s clauses', PP, PRE_PP,
     'OPEN_TRAILS.md', [11232, 11373, 11664, 11703, 11704, 11796, 11798, 11800, 11802, 11864, 11904, 11906, 11908, 11930, 11932, 11934,
                        11954, 11956, 12082, 12086, 12090, 12112]),
    ('PLACE-papers REGISTRY, the deposited pin and the citation rule', PP, PRE_PP, 'REGISTRY.md', [700, 962]),
    ('SIDE-explicit-formula the schema`s fields at main', EFK, 'main', 'SIDEExplicitFormula/Schema/Config.lean', list(range(23, 37))),
    ('relay b588`s closing push-out, its head', RELAY, 'HEAD', 'data/b588_closing_push_out.txt', list(range(1, 4))),
]


def reads():
    L = ['b589 -- READING (1): THE READS, CITED BY PATH AND LINE, EACH PRINTED FROM ITS BLOB AT ITS PIN', '']
    for label, repo, rev, path, sel in READS:
        sl = g(repo, 'show', '%s:%s' % (rev, path)).split(NL)
        L.append('### %s -- %s @ %s (%d lines cited)' % (label, path, g(repo, 'rev-parse', '--short=8', rev).strip(), len(sel)))
        for n in sel:
            L.append('    :%-6d %s' % (n, (sl[n - 1] if 0 < n <= len(sl) else '### NO SUCH LINE')[:300]))
    L.append('### THE PROVISIONAL SPECIFICATION, SEARCHED (the seat`s routes before the seal, re-run here):')
    for repo in (PP, PAT):
        L.append('    %s history for *PROV1_FORMATION_VERIFICATION* : %d commit(s)' % (repo, len([x for x in g(repo, 'log', '--all', '--oneline', '--',
                                                                                                         '*PROV1_FORMATION_VERIFICATION*').split(NL) if x.strip()])))
    hits = []
    for base in ('D:/MY-DOwnloads', 'D:/relay', 'D:/HERITAGE'):
        for dp, dn, fn in os.walk(base):
            dn[:] = [d for d in dn if d not in ('.git', '.lake', 'node_modules')]
            hits += [os.path.join(dp, f) for f in fn if 'PROV1_FORMATION_VERIFICATION' in f.upper()]
    ctl = os.path.exists(os.path.join(PAT, 'PROVISIONAL_A_SPECIFICATION.md'))
    L.append('    the walk of D:/MY-DOwnloads, D:/relay, D:/HERITAGE : %d file(s) %s ; the positive control (PROVISIONAL_A_SPECIFICATION.md '
             'in the patent repo) %s ; mounted drives : %s' % (len(hits), hits, 'FOUND' if ctl else '### NOT FOUND',
                                                               [d for d in 'CDEFGH' if os.path.exists(d + ':/')]))
    put_txt('b589_reads.txt', L)


# ================================================================================ THE RECORD LINES OF (R199)(1)
B588_ENTRY = '## CP-7, act thirteen: the edition of TECHNE_TOOLKIT'


def weight_lines():
    """### PLACE-papers FINDINGS: b588's weight, and the TECHNE v8.3 credit re-read against the verdict's text (no byte of v8.3 changes)."""
    Q = _Q()
    entry = Q.line_of(Q.FIND, B588_ENTRY)
    if entry != 6694:
        sys.exit('### THE ADDRESSED LINE MOVED: entry %s -- NOTHING WRITTEN' % entry)
    tl = g(PP, 'show', '%s:%s' % (PRE_PP, TECHNE_ED)).split(NL)[241]
    inside = 'lies inside that side and is not of the kind F-7 formalizes' in tl and 'outside' not in tl
    weight = '*Appended 2026-10-01 by b589 to b588’s entry (:%d), under `(R199)`(1) -- b588 AT ITS WEIGHT:*' % entry
    reread = '*Appended 2026-10-01 by b589 to b588’s entry (:%d), under the author’s answer before b589’s seal -- THE TECHNE CREDIT RE-READ:*' % entry
    Q.guard_absent(Q.FIND, weight)
    out = [Q.append_to(Q.FIND, '\n%s TECHNE_TOOLKIT v8.3 beside v8.2 unedited, over its §XIII table: the three rows on :414 rewritten in two '
                                 'sentences citing ch_iff_rh and h2_sign_iff_rh with the Routes from relay b540_tiers.json :437; the cross-link '
                                 'credit beneath :239; two ceiling, three stem and one fact correction; b450’s “THERE IS NO TABLE” superseded '
                                 'by §XIII at :504-:521; H28a, H28b (+2 against 2) and H28c held; the scanner CLEAN; (N4) refuted in its letter '
                                 'on the one text cell. The census / totality pair at THE_METHOD_CANON §XX :297 in the seat’s 57-word draft, '
                                 'the author rewording or striking at leisure. The ferry’s “b450_batch.json :172-:173” was the navigator’s; the '
                                 'items are at relay data/b450_components.txt :172-:173. The suite reads 70 of 70.\n' % weight)]
    out.append(Q.append_to(Q.FIND, '\n%s v8.3 :242 reads “%s” -- the verdict’s own words at the archived landing :8845 (the difficulty of the '
                                    'premise inside the in-scope, decidable side, not of the kind formalized); %s The wording “outside the kind” '
                                    'was the navigator’s at b588’s answer and is not in the file.\n' % (
                                        reread, 'lies inside that side and is not of the kind F-7 formalizes',
                                        'it agrees, and no correction is made.' if inside else '### IT DOES NOT AGREE.')))
    lines = dict(weight=Q.line_of(Q.FIND, weight), reread=Q.line_of(Q.FIND, reread))
    put_json('b589_weight_lines.json', dict(entry=entry, lines=lines, heads=dict(weight=weight, reread=reread), techne_242=tl, inside=inside,
                                            appends=out))
    print(lines, 'inside', inside)


# ================================================================================ COMPONENT 1 -- E_DIFFICULTY: THE TERMINALS, THE TABLE, THE EDITION
TERMS = [  # (row, name, pins to re-print at)
    (162, 'sieve_ceiling', ('v1.1', 'v1.4', 'v1.7')),
    (163, 'proof_dichotomy', ('v1.1', 'v1.7')),
    (164, 'e_difficulty', ('v1.1', 'v1.4', 'v1.7')),
    (165, 'e_difficulty_xi', ('v1.1', 'v1.7')),
    (0, 'sieve_ceiling_semantic', ('v1.4', 'v1.7')),
]
SC_FILE = 'Kernel/Cascade/SieveCeiling.lean'
TERM_FILE = {'sieve_ceiling_semantic': 'Kernel/Cascade/SieveCeilingSemantic.lean'}


def _decl(repo, pin, path, name, maxl=14):
    src = g(repo, 'show', '%s:%s' % (pin, path)).split(NL)
    rx = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(?:(?:private|protected|noncomputable)\s+)*(theorem|lemma|def|abbrev|structure|instance)\s+%s\b' % re.escape(name))
    for i, l in enumerate(src):
        if rx.match(l):
            j = i
            while j > 0 and src[j - 1].strip() and (src[j - 1].lstrip().startswith(('/-', '-', '--')) or src[j - 1].rstrip().endswith('-/')
                                                      or not src[j - 1].strip().startswith(('theorem', 'def', 'lemma'))):
                j -= 1
                if src[j].lstrip().startswith('/--'):
                    break
            k = i
            while k < len(src) - 1 and k - i < maxl and ':=' not in src[k]:
                k += 1
            return i + 1, src[j:i], src[i:k + 1]
    return None, [], []


def ed_terms():
    """### Each tier-block terminal re-printed at its pins by `git show`, before its table row is written."""
    L = ['b589 -- COMPONENT 1 (a): E_DIFFICULTY_THEOREM`S TERMINALS RE-PRINTED AT THEIR PINS, SIDE-kernel %s (git show, no elaboration)' % SC_FILE, '']
    for t in ('v1.1', 'v1.4', 'v1.7'):
        L.append('### tag %s = %s (remote %s)' % (t, g(KER, 'rev-parse', '--short=7', t + '^{}').strip(),
                                                  (g(KER, 'ls-remote', 'origin', 'refs/tags/%s^{}' % t).split('\t') or [''])[0][:7]))
    out = {}
    for row, name, pins in TERMS:
        L.append('')
        L.append('### %s `%s`' % (':%d' % row if row else '(the contentful ceiling the update paragraph names)', name))
        for pin in pins:
            fpath = TERM_FILE.get(name, SC_FILE)
            ln, doc, sig = _decl(KER, pin, fpath, name)
            out.setdefault(name, {})[pin] = dict(line=ln, doc=doc, sig=sig, file=fpath)
            L.append('    @ %s : %s' % (pin, ('%s :%d' % (fpath, ln)) if ln else '### NOT FOUND'))
            for d in doc[-6:]:
                L.append('        | %s' % d[:200])
            for s in sig:
                L.append('        > %s' % s[:200])
    put_txt('b589_ediff_terms.txt', L)
    put_json('b589_ediff_terms.json', out)


EF = 'SIDE-kernel'
TABLE_HEAD = '| claim | kernel pin | terminal | profile | Status |'
TABLE_ROWS = [
    ('§VII :162 — `sieve_ceiling`: dark-factored proofs cannot reach universal statements', 'SIDE-kernel v1.7 = `2957e7d`', '`sieve_ceiling`',
     'axiom-free (b557, relay `data/b557_tiers.txt` :596)',
     'Compiled, T2-SHELL (b557’s tier block :242): abstract bookkeeping over the file’s own `Proof`; SCAFFOLDING by its docstring at v1.4 and '
     'v1.7 (:598), the contentful ceiling `sieve_ceiling_semantic`'),
    ('§VII :163 — `proof_dichotomy`: every proof is either dark-factored or has bright access', 'SIDE-kernel v1.7 = `2957e7d`', '`proof_dichotomy`',
     'axiom-free (b557, :604)', 'Compiled, T2 (b557’s tier block :243): excluded middle over the file’s `StepAccess` lists (:606)'),
    ('§VII :164 — `e_difficulty`: decidability iff a domain Ostrowski', 'SIDE-kernel v1.7 = `2957e7d`', '`e_difficulty`',
     '`{propext, Quot.sound}` (b557, :612)', 'Compiled, T2 (b557’s tier block :244): at v1.1 = `e0a8ba0` with `classes ≥ 1` (:611); from v1.4 = '
     '`f374174` it reads its system, for every conserved `DeterminedSystem` (:613), over the file’s own types (:614)'),
    ('§VII :165 — `e_difficulty_xi`: the smoke test at the ξ system', 'SIDE-kernel v1.7 = `2957e7d`', '`e_difficulty_xi`',
     '`{propext, Quot.sound}` (b557, :620)', 'Compiled, T2 (b557’s tier block :245): at the file’s own `xi_system` (:622)'),
]

REWRITES = [
    (162, '- `sieve_ceiling` — dark-factored proofs cannot reach universal statements',
     '- `sieve_ceiling` — dark-factored proofs cannot reach universal statements; from SIDE-kernel v1.4 = `f374174` its docstring labels it '
     'SCAFFOLDING, the contentful ceiling being `sieve_ceiling_semantic`, T2-SHELL (relay `data/b557_tiers.txt` :598)'),
    (164, '- `e_difficulty` — for systems with `classes ≥ 1`, IsDecidable iff Nonempty (DomainOstrowski)',
     '- `e_difficulty` — at SIDE-kernel v1.1 = `e0a8ba0`, for systems with `classes ≥ 1`, IsDecidable iff Nonempty (DomainOstrowski) (relay '
     '`data/b557_tiers.txt` :611); from v1.4 = `f374174`, through v1.7 = `2957e7d`, it reads its system, for every conserved '
     '`DeterminedSystem` IsDecidable iff Nonempty (DomainOstrowski) (relay `data/b557_tiers.txt` :613), T2 over the file’s own types (:614)'),
]
CEIL_RECORD = 'ceiling correction record:'
CARRY_RECORD = 'ceiling read, carried:'
FACT_RECORD = 'fact correction record:'
CEILS = [
    (24, 'The method has been applied successfully to ξ(s) yielding the Riemann Hypothesis, to Dirichlet L-functions yielding GRH,',
     'The method has been applied to ξ(s), yielding the reduction of the Riemann Hypothesis to the open premise `h2`, to Dirichlet '
     'L-functions, yielding the reduction of GRH to its premise,'),
    (48, 'This direction was already demonstrated for ξ(s) and instantiated across the catalogue.',
     'This direction was already demonstrated for ξ(s) at each stage of the formation count, its completeness at the ξ interface being the '
     'open premise `h2`, and instantiated across the catalogue.'),
    (136, 'The programme did not invent a new proof technique for the Riemann Hypothesis.',
     'The programme did not invent a new technique for the reduction of the Riemann Hypothesis.'),
    (136, 'appear in every proof of RH, whether the proof recognizes them or not.',
     'appear in every reduction of RH, whether the reduction recognizes them or not.'),
    (138, 'The 167-year delay was not a failure of effort.', 'The 167 years without a proof were not a failure of effort.'),
    (138, 'Once the darkness is named, the route becomes visible.', 'Once the darkness is named, the route to the one open premise `h2` becomes visible.'),
    (177, 'Retroactively: the success of SIDE on ξ(s) was not luck or technique-choice;',
     'Retroactively: the reduction SIDE located on ξ(s), to the one open premise `h2`, was not luck or technique-choice;'),
]
FACTS = [
    (203, 'Current: SIDE-kernel v1.3, version DOI 10.5281/zenodo.21417776, concept DOI 10.5281/zenodo.19674312',
     'Deposited: SIDE-kernel v1.5 = `0e5233f`, version DOI 10.5281/zenodo.21520474 (REGISTRY :962); the earlier record SIDE-kernel v1.3, '
     'version DOI 10.5281/zenodo.21417776, concept DOI 10.5281/zenodo.19674312'),
]
CEILING = re.compile(r'yielding the Riemann Hypothesis|yielding GRH|proof technique for the Riemann Hypothesis|every proof of RH|167-year delay|'
                     r'success of SIDE|already demonstrated for ξ|RH proved|proves RH|proof of RH|RH proof|route becomes visible')
CARRIED = {}
CREDIT = (183, '*Credit (b450 item, located at b588): the E-Difficulty cross-link verdict `DISTINCT` -- located by name at OPEN_TRAILS :773 '
               '(the index line of the `S6` crossing landing, 2026-08-12) and held whole at `%s` :8839-:8847 -- reads that E-Difficulty '
               'measures catalogue-closeability, that the dichotomy’s own census note places RH on the in-scope, decidable side, and that '
               '`h2`’s difficulty is a difficulty inside that side and is not of the kind the dichotomy formalizes.*' % ARCH)
VERSION = (6, '**v1.0.4, 2026-10-01** — *CP-7 edition (b589), written beside v1.0.3, which is unedited; its back matter closes the file.*')
BM_TAG = '<!-- b589 (R199) THE v1.0.4 EDITION`S BACK MATTER, 2026-10-01 -->'
BANKROWS = (('b557_tiers.txt', 598), ('b557_tiers.txt', 611), ('b557_tiers.txt', 613))
LEDGERS = (('OPEN_TRAILS :773', 'PLACE-papers `OPEN_TRAILS.md`', 'the index line of the S6 crossing landing, the verdict by name'),
           ('`%s` :8839-:8847' % ARCH, 'PLACE-papers archive', 'the landing`s section 2, the verdict whole'),
           ('REGISTRY :962', 'PLACE-papers `REGISTRY.md`', 'the deposited pin and the citation rule'))
OFFSET = ('+1 from :6 (the v1.0.4 line, above the v1.0.3 line); +2 more from :184 (a blank and the credit line, beneath :183) -- v1.0.3 :n '
          'sits at the edition`s :n for n < 6, at :n+1 for 6 <= n <= 183 and at :n+3 for n >= 184')
READING_NAME = {1: '(e) the terminal says what it states at its pin'}


def _segs(l):
    import b558_record as CP
    return [s for s in CP.segments(l) if s]


def _count(lines):
    return sum(len(_segs(l)) for l in lines)


def _rows():
    return [r for r in jl('b558_cp1b.json')['rows'] if r['doc'] == 'EDIFF' and r['verdict'] == 'MOVED-IN-MEANING']


def _status_blanks(lines):
    import b579_record as R9
    return R9._status_blanks(lines)


def _cur():
    cur = g(PP, 'show', '%s:%s' % (PRE_PP, CUR)).split(NL)
    return cur[:-1] if cur and cur[-1] == '' else cur


def _edl(n):
    return n + (1 if n >= VERSION[0] else 0) + (2 if n > CREDIT[0] else 0)


def _all_changes():
    return REWRITES + CEILS + FACTS


def edition(*a):
    """### PLACE-papers phase2/method/E_DIFFICULTY_THEOREM_v1_0_4.md beside the current version from its blob at b378167; the table in the
    ### back matter's Correspondence; the re-pin step last."""
    cur = _cur()
    if g(PP, 'rev-parse', 'HEAD:' + CUR).strip() != g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip():
        sys.exit('### THE CURRENT VERSION MOVED SINCE b378167 -- NOTHING WRITTEN')
    T = jl('b589_ediff_terms.json') if 'dry' not in a else json.loads(a[a.index('dry') + 1]) if len(a) > a.index('dry') + 1 else {}
    edp = os.path.join(PP, *ED.split('/'))
    if os.path.exists(edp) and 'again' not in a:
        sys.exit('### THE EDITION FILE EXISTS -- NOTHING WRITTEN')
    if g(PP, 'ls-files', ED).strip():
        sys.exit('### THE EDITION FILE IS COMMITTED -- NOTHING WRITTEN')
    if 'dry' not in a and not all(T.get(n, {}).get(p, {}).get('line') for _, n, ps in TERMS for p in ps):
        sys.exit('### A TERMINAL DID NOT RE-PRINT AT ITS PIN -- NO ROW IS WRITTEN')
    new = list(cur)
    for ln, old, rep in _all_changes():
        line = new[ln - 1]
        if line.count(old) != 1:
            sys.exit('### :%d -- THE FRAGMENT IS NOT ON ITS LINE EXACTLY ONCE (%d): %s' % (ln, line.count(old), old[:80]))
        n0 = len(_segs(line))
        new[ln - 1] = line.replace(old, rep)
        if len(_segs(new[ln - 1])) != n0:
            sys.exit('### :%d -- THE CHANGE ALTERED THE LINE`S SEGMENT COUNT %d -> %d' % (ln, n0, len(_segs(new[ln - 1]))))
    if not cur[VERSION[0] - 1].startswith('**v1.0.3, 2026-07-23**') or not cur[CREDIT[0] - 1].startswith('*Census note (demarcation line).'):
        sys.exit('### AN ANCHOR IS NOT WHERE THE FACE SAYS')
    for t in (CREDIT[1], VERSION[1]):
        if len(_segs(t)) != 1:
            sys.exit('### AN INSERTED LINE IS NOT ONE SENTENCE (%d): %s' % (len(_segs(t)), t[:60]))
    diff = []
    for r in _rows():
        ln = r['line']
        k = _segs(cur[ln - 1]).index(r['sentence'])
        nw = _segs(new[ln - 1])[k]
        banks = ['%s:%d' % (b, n) for b, n in BANKROWS if ('relay `data/%s` :%d' % (b, n)) in nw]
        diff.append(dict(id=r['id'], line=ln, ed_line=_edl(ln), terminal=r['terminal'], old=r['sentence'], new=nw, changed=nw != r['sentence'],
                         reading=1, cites=[], banks=banks, supports=r['reading']))
    new[CREDIT[0]:CREDIT[0]] = ['', CREDIT[1]]
    new[VERSION[0] - 1:VERSION[0] - 1] = [VERSION[1]]
    body = list(new)
    changed = set(x[0] for x in _all_changes())
    if any(_edl(n) > len(body) or (n not in changed and body[_edl(n) - 1] != cur[n - 1]) for n in range(1, len(cur) + 1)):
        sys.exit('### OFFSET MODEL DOES NOT CARRY THE CURRENT VERSION')
    inv = {_edl(n): n for n in range(1, len(cur) + 1)}
    hits = [(i, m.group(0)) for i, l in enumerate(body, 1) for m in CEILING.finditer(l)]
    stray = sorted(set(inv.get(i, -i) for i, _ in hits) - set(CARRIED) - changed)
    if stray:
        sys.exit('### A CEILING HIT IN THE BODY IS NEITHER CORRECTED, REWRITTEN NOR CARRIED: current lines %s' % stray)
    bm = ['', BM_TAG, '',
          '## Back matter of the v1.0.4 edition -- written 2026-10-01 by b589 under the author’s ruling `(R199)`(2), by the form of `(R187)`(5)', '',
          '*This file is v1.0.4 of E_DIFFICULTY_THEOREM, the CP-7 edition written beside v1.0.3 (`%s`, unedited) from v1.0.3’s tier block (its '
          ':236, standing: 4 rows, every terminal T2, one T2-SHELL) and its CP-1b work-list (relay `%s`); its Correspondence table, written at '
          'b589 from the tier block’s terminals, stands under Correspondence below; it does not deposit and does not replace v1.0.3, and its '
          'promotion is CP-8’s. Every line cited below is this file’s own.*' % (CUR, WL), '',
          '### Removals', '', 'None: both work-list rows resolve to a sentence rewritten in place to what its compiled fact says.', '',
          '### Credit lines', '', '| this edition’s line | the item | Status |', '|:--|:--|:--|',
          '| :%d | the E-Difficulty cross-link verdict `DISTINCT` (b450, relay `data/b450_batch.json` :966), located by name at OPEN_TRAILS :773 '
          '| inserted beneath :%d, the census note whose placement the verdict reads, the author’s answer before b589’s seal |' % (
              _edl(CREDIT[0]) + 2, _edl(CREDIT[0])), '',
          '### Ceiling corrections', '', '| this edition’s line | v1.0.3 wording | v1.0.4 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in CEILS:
        bm.append('| :%d | %s %s | %s | corrected under the ceiling clause by the census / totality pair, the author’s answer before b589’s seal |' % (
            _edl(ln), CEIL_RECORD, old, rep))
    bm += ['', '### Ceiling-shaped sentences read and carried', '',
           'None beyond the corrections: the definitional uses at :%d (“the Riemann Hypothesis (‘every zero lies on the critical line’)”) and '
           ':%d (Theorem 34’s density statement) name the statement and a measured density, not a claim that it holds.' % (_edl(62), _edl(76)), '',
           '### Stem corrections', '', 'None: the scanner finds no use of a banned stem in v1.0.3.', '',
           '### Fact corrections', '', '| this edition’s line | v1.0.3 wording | v1.0.4 wording | Status |', '|:--|:--|:--|:--|']
    for ln, old, rep in FACTS:
        bm.append('| :%d | %s %s | %s | corrected under the fact clause: REGISTRY :962 prints the deposit at v1.5 = `0e5233f` (record 21520474) and '
                  'the rule that a sentence citing SIDE-kernel for the deposit cites v1.5; the v1.3 record kept in the sentence as the earlier '
                  'record, the author’s answer before b589’s seal |' % (_edl(ln), FACT_RECORD, old, rep))
    bm += ['', '### The history entries', '',
           'The dated version entries at :%d-:%d carry as dated records under the history clause; their grade words (“DERIVES” at v1.0.3) are '
           'the era’s, and the tier block and the table below give the tier law’s reading.' % (_edl(8), _edl(12)), '',
           '### The navigator’s expectations of `(R199)`(2)', '', '| expectation | the read | Status |', '|:--|:--|:--|',
           '| the Correspondence table written from the tier block’s terminals, each re-printed at its pin first | 4 rows; relay '
           '`data/b589_ediff_terms.txt` | written below |',
           '| the cross-link verdict `DISTINCT` credited beneath the sentence it corrects | OPEN_TRAILS :773, archive :8839-:8847 | credited '
           'beneath :%d |' % _edl(CREDIT[0]),
           '| b450’s “THERE IS NO TABLE” superseded by the new table | the table below | superseded |',
           '', '### Placement', '', '| object | path | Status |', '|:--|:--|:--|',
           '| this edition, v1.0.4 | `%s` | written at b589 |' % ED,
           '| the current version, v1.0.3 | `%s` | unedited |' % CUR,
           '| the work-list | relay `%s` | read |' % WL,
           '| the terminals re-printed | relay `data/b589_ediff_terms.txt` | banked at b589 |',
           '| the sentence-by-sentence diff | relay `data/b589_edition_EDIFF.txt` | banked at b589 |',
           '', '### Correspondence', '',
           '**The table, written at b589 by the house form from the tier block’s terminals (v1.0.3 :236), each terminal re-printed at its pin '
           'before its row (relay `data/b589_ediff_terms.txt`).** b450’s line “THERE IS NO TABLE” for this document (relay '
           '`data/b450_components.txt` :174; `data/b450_batch.json` :961) is superseded by it.', '',
           TABLE_HEAD, '|:--|:--|:--|:--|:--|']
    bm += ['| %s |' % ' | '.join(r) for r in TABLE_ROWS]
    bm += ['', '| declaration, bank line or ledger line | repository | pin | the page’s line | Status |', '|:--|:--|:--|:--|:--|']
    bank_lines = {}
    for bank, n in BANKROWS:
        at = [i for i, l in enumerate(body, 1) if ('relay `data/%s` :%d' % (bank, n)) in l]
        bank_lines['%s:%d' % (bank, n)] = at
        bm.append('| `data/%s` :%d | relay | the tier law`s read | not on the page | cited at :%s of this edition |' % (
            bank, n, ', :'.join(str(x) for x in at) or '### NONE'))
    ledger_lines = {}
    for needle, repo, what in LEDGERS:
        at = [i for i, l in enumerate(body, 1) if needle in l]
        ledger_lines[needle] = at
        bm.append('| %s | %s | %s | not on the page | cited at :%s of this edition |' % (needle, repo, what, ', :'.join(str(x) for x in at) or '### NONE'))
    bm.append('')
    if any('### NONE' in l for l in bm):
        sys.exit('### A CORRESPONDENCE ROW CITES NO LINE OF THE EDITION')
    full = body + bm
    b = (NL.join(full) + NL).encode('utf-8')
    open(edp + '.tmp', 'wb').write(b)
    os.replace(edp + '.tmp', edp)
    print('  written: %s (%d bytes, %d lines)' % (ED, len(b), len(full)))
    n_cur, n_body, n_full = _count(cur), _count(body), _count(full)
    put_json('b589_edition.json', dict(path=ED, cur=CUR, cur_blob=g(PP, 'rev-parse', '%s:%s' % (PRE_PP, CUR)).strip(),
                                       lines_cur=len(cur), lines_body=len(body), lines_full=len(full),
                                       n_cur=n_cur, n_body=n_body, n_full=n_full, n_backmatter=n_full - n_body,
                                       credit=1, removals=0, ruled_citations=0, version_lines=1, diff=diff, offset=OFFSET,
                                       ceils=CEILS, facts=FACTS, rewrites=REWRITES, table=TABLE_ROWS,
                                       credit_line=dict(after=CREDIT[0], at=_edl(CREDIT[0]) + 2, text=CREDIT[1]),
                                       version=dict(above=VERSION[0], text=VERSION[1]),
                                       sha256=hashlib.sha256(b).hexdigest(), status_blanks=_status_blanks(full),
                                       bank_lines=bank_lines, ledger_lines=ledger_lines))
    print('  counts: current %d ; body %d ; whole %d ; back matter %d' % (n_cur, n_body, n_full, n_full - n_body))


def edition_bank():
    """### The diff with its offset line, the corrections, the counts, the ceiling read, the scanner's verdict, H28a-H28c."""
    E = jl('b589_edition.json')
    ed = io.open(os.path.join(PP, *ED.split('/')), encoding='utf-8').read().replace(chr(13), '').split(NL)
    if ed and ed[-1] == '':
        ed = ed[:-1]
    cut = ed.index(BM_TAG)
    scan = rd('b589_edition_termscan.txt')
    live = re.search(r'live uses\s*:\s*(\d+)', scan)
    clean = re.search(r'^\s*VERDICT\s*: CLEAN', scan, re.M) is not None
    corrected_ed = set(_edl(x[0]) for x in CEILS)
    hits = []
    for i, l in enumerate(ed, 1):
        for m in CEILING.finditer(l):
            kind = ('record' if (i > cut and l.startswith('| :') and CEIL_RECORD in l) else 'corrected' if (i < cut and i in corrected_ed) else 'beyond')
            hits.append(dict(line=i, hit=m.group(0), kind=kind, ctx=l[max(0, m.start() - 60):m.end() + 40]))
    beyond = [h for h in hits if h['kind'] == 'beyond']
    h28a_bad = [d['id'] for d in E['diff'] if not d['changed'] or not (d['cites'] or d['banks'])]
    h28a = 'HELD' if not h28a_bad else 'REFUTED'
    body_dn = E['n_body'] - E['n_cur']
    allowed = E['credit'] + E['removals'] + E['ruled_citations'] + E['version_lines']
    h28b = 'HELD' if abs(body_dn) <= allowed else 'REFUTED'
    live_n = int(live.group(1)) if live else None
    h28c = 'HELD' if (live_n == 0 and clean and not beyond) else 'REFUTED'
    cur0 = _cur()
    reg = g(PP, 'show', '%s:REGISTRY.md' % PRE_PP).split(NL)[961]
    L = ['### OFFSET FROM THE CURRENT VERSION (R190)(3): %s -- every edition line below is the final file`s own.' % OFFSET, '',
         'b589 -- COMPONENT 1: THE EDITION OF E_DIFFICULTY_THEOREM, (R199)(2), BY THE FORM OF (R187)(5) AND ITS CLAUSES, ITS TABLE WRITTEN FIRST', '',
         '### the current version : PLACE-papers %s @ %s (blob %s), %d lines ; head :1 "%s" ; :6 "%s"' % (
             CUR, PRE_PP, E['cur_blob'][:8], E['lines_cur'], cur0[0], cur0[5][:90]),
         '### its tier block : :236 "%s"' % cur0[235][:110],
         '### its version history : the version line :6 (v1.0.3; was v1.0.2, v1.0.1, v1.0); the dated entries :8-:12; b450`s annotation :223-:231; '
         'b557`s tier block :234-:256; b558`s line :258',
         '### the edition : PLACE-papers %s, %d lines, sha256 %s' % (ED, E['lines_full'], E['sha256']), '',
         '### THE CORRESPONDENCE TABLE, WRITTEN FIRST (%d rows), each terminal re-printed at its pin (relay data/b589_ediff_terms.txt):' % len(E['table']),
         '    ' + TABLE_HEAD]
    L += ['    | %s |' % ' | '.join(r) for r in E['table']]
    L += ['', '### THE WORK-LIST, ROW BY ROW (2 rows, 2 sentences, 2 lines):', '']
    for d in E['diff']:
        L += ['  %s v1.0.3 :%d -> v1.0.4 :%d `%s` -- %s ; banks %s' % (d['id'], d['line'], d['ed_line'], d['terminal'], READING_NAME[d['reading']], d['banks']),
              '      work-list: %s' % d['supports'], '      v1.0.3 : %s' % d['old'], '      v1.0.4 : %s' % d['new'], '']
    L += ['### THE CREDIT LINE (the author`s answer): v1.0.4 :%d, beneath v1.0.3 :183' % E['credit_line']['at'], '      %s' % E['credit_line']['text'], '']
    L += ['### THE CEILING CORRECTIONS (%d), the author`s answer:' % len(E['ceils'])]
    L += ['    v1.0.3 :%d -> v1.0.4 :%d  "%s" -> "%s"' % (c[0], _edl(c[0]), c[1], c[2]) for c in E['ceils']]
    L += ['### THE FACT CORRECTIONS (%d), the author`s answer:' % len(E['facts'])]
    L += ['    v1.0.3 :%d -> v1.0.4 :%d  "%s" -> "%s"' % (c[0], _edl(c[0]), c[1], c[2]) for c in E['facts']]
    L += ['      the source: PLACE-papers REGISTRY.md :962 @ %s "%s"' % (PRE_PP, reg[:300])]
    L += ['### THE STEM CORRECTIONS: none. ### REMOVALS: none.',
          '### THE VERSION LINE: above v1.0.3 :%d: %s' % (E['version']['above'], E['version']['text']), '',
          '### THE COUNTS (relay tools/b558_record.py `segments`, imported): the current version %d ; the edition`s body %d (%+d) ; the back '
          'matter %d ; the edition whole %d' % (E['n_cur'], E['n_body'], body_dn, E['n_backmatter'], E['n_full']),
          '### H28b, final form: the body differs by %+d against CREDIT %d + removals %d + ruled citations %d + one version line = %d' % (
              body_dn, E['credit'], E['removals'], E['ruled_citations'], allowed),
          '### no blank Status cell: %s' % ('HELD' if not E['status_blanks'] else '### BLANK AT %s' % E['status_blanks']), '',
          '### THE CEILING, every hit in the edition:']
    L += ['    :%d "%s" -- %s -- ...%s...' % (h['line'], h['hit'], {'record': 'quoted in a back-matter record, read by the seat',
                                                                 'corrected': 'in a sentence corrected under the ceiling clause',
                                                                 'beyond': '### BEYOND THE CEILING'}[h['kind']], h['ctx']) for h in hits] or ['    none']
    L += ['### sentences beyond the ceiling: %d' % len(beyond),
          '### THE SCANNER (banned_terms.py) on the edition: live uses %s ; verdict %s' % (live_n, 'CLEAN' if clean else 'NOT CLEAN'), '',
          '### ### **H28a %s -- every MOVED row resolves to a sentence citing its terminal`s statement by bank line at its pin%s.**' % (
              h28a, '' if not h28a_bad else ' -- refuted at %s' % h28a_bad),
          '### ### **H28b %s -- final form: the body differs by %+d sentences against at most %d; the back matter %d, excluded and '
          'printed.**' % (h28b, body_dn, allowed, E['n_backmatter']),
          '### ### **H28c %s -- the scanner`s live count %s and verdict %s; sentences beyond the ceiling %d.**' % (
              h28c, live_n, 'CLEAN' if clean else 'NOT CLEAN', len(beyond)),
          '### ### **THE EDITION LANDS: NO SENTENCE HELD.**']
    put_txt('b589_edition_EDIFF.txt', L)
    put_json('b589_h28.json', dict(H28a=h28a, H28b=h28b, H28c=h28c, h28a_bad=h28a_bad, body_dn=body_dn, allowed=allowed,
                                   backmatter=E['n_backmatter'], live=live_n, clean=clean, beyond=len(beyond), hits=hits, held=None,
                                   n_ceils=len(E['ceils']), n_facts=len(E['facts']), table_rows=len(E['table'])))
    H = jl('b589_h28.json')
    print(H['H28a'], H['H28b'], H['H28c'], 'body_dn', body_dn, 'allowed', allowed, 'beyond', H['beyond'], 'live', H['live'],
          'ceils', H['n_ceils'], 'facts', H['n_facts'], 'rows', H['table_rows'])


# ================================================================================ COMPONENT 3 -- THE EXTRACTION SWEEP TWO (HELD at the missing file)
INSTRUMENTS = [  # (instrument, act of origin, test, relay path)
    ('the E0 rule file (a statement`s E0 grade from its premises, shared by every reader)', 'b568 (relay 09f7f60e); class-membership clause b570',
     'tools/test_e0_rule.py', 'tools/e0_rule.py'),
    ('the tier law, its two axes (premise profile and conclusion form; the weakest link sets a row`s tier)',
     'b540-b547 (FINDINGS :4805, :4819, :5812, :5868)', 'the tier blocks re-read at pin (b557) and the census (b558)', 'data/b540_tiers.json, data/b557_tiers.txt'),
    ('the four supersession forms and the CONFLICT refusal (a grade cell superseded by a dated ledger line; distinct grades quoted, never chosen)',
     'b496 (relay d5069e3a); supersession rule b553; synonym map b554', 'tools/test_row_sort.py; the suite`s G-TABLE-GRADES-UNMOVED',
     'tools/terminal_table.py, tools/table_gate.py'),
    ('chain_page.py and G-CHAIN-PAGE (the compiled chain generated from a node list, regenerated byte for byte)', 'b568 (relay 3b3152f4); repair b574',
     'tools/test_chain_page.py, tools/test_g_chain_page.py', 'tools/chain_page.py'),
    ('the as-of commit lines (every repository`s main read back against its remote, appended after the closing push)', 'b569 (relay 54cc6f9c)',
     'tools/test_asof.py', 'tools/asof_lines.py'),
    ('the tag-after-read-back script (main pushed from a push branch and read back before any tag is made)', 'b561; tag-making b568 (relay f35256d8)',
     'tools/test_push_gated.sh', 'tools/push_gated.sh'),
    ('the sealed face with addendum forms (the registration hashed and locked before any component; addenda refused unless the clause names the file)',
     'b263 (relay c78275bf); lock gate b378; addendum form b567 (relay 0e50bd19)', 'tools/test_addenda_writelist.py, tools/test_addenda_licence.py',
     'tools/reg_seal.py, tools/b378_lockgate.py, tools/gate_hash.py, tools/addenda.py'),
    ('the edition form and its ten clauses (form, H28b, stem, ceiling, history, re-pin, name-and-title, fact, placement, table rule)',
     'b577-b587 (OPEN_TRAILS :11864, :11930, :11904, :11906, :11908, :11932, :11934, :11954, :11956, :12084)', 'each act`s suite (G-EDITION-* arms)',
     'tools/b588_record.py (the latest edition tool)'),
    ('the ceiling census and the corroboration census (phrase and object per sentence; the tables naming a terminal per document)',
     'b584 (ceiling), b586 (corroboration)', 'the banks` own controls', 'data/b584_ceiling_census.txt, data/b586_corroboration.txt'),
    ('the scanner`s exception read (an edition`s back matter read for excepted names and carried-by-history lines)', 'b586 (relay 3746a2a0)',
     'tools/test_banned_terms_backmatter.py', 'tools/banned_terms.py'),
    ('the lemma walk (a vendored library walked lemma by lemma for a named proportion; priced)', 'b584 (its items, relay data/b584_ferry.txt :48)',
     'none (a priced item)', 'tools/b584_record.py :166'),
    ('the two-seat relay with hypotheses fixed before computation (the navigator`s expectations and the seat`s own registered on a sealed face, '
     'scored on the banks)', 'b185 (registration gate, relay 9372f8cf); satisfiability b265; the expectations` form b583', 'every act`s suite (G-N*-SCORED)',
     'tools/registration_gate.py, tools/reg_satisfiable.py, tools/b5NN_regspec.py'),
]
B257_DRAFTS = ['SIGNEDNESS.md', 'BANKED_MEANINGS_ENGINE.md', 'IMPORT_LEDGER.md', 'HARNESS_LORE.md', 'DISCRIMINATOR_PROTOCOL.md',
               'FACE_OFF_PROTOCOL.md', 'DECISION_CARD_FORMAT.md', 'RENDER_AS_E0.md']


def sweep():
    """### patent-package-BACKUP-2026-08-29/SWEEP_TWO_2026-10-01.md (created; the author's answer) and relay data/b589_sweep.txt (counts and
    ### the pointer only). PROV1_FORMATION_VERIFICATION_ARCHITECTURE.md is not written: it is absent (HELD)."""
    p = os.path.join(PAT, SWEEP_FILE)
    if os.path.exists(p):
        sys.exit('### THE SWEEP FILE EXISTS -- NOTHING WRITTEN')
    tdir = 'D:/MY-DOwnloads/TECHNE-Core/modules/2026-08'
    L = ['# TECHNE extraction sweep two -- 2026-10-01', '',
         '*Drafted at b589 under the author`s ruling (R199)(4), for appending to PROV1_FORMATION_VERIFICATION_ARCHITECTURE.md as a dated section. '
         'That file is not on this machine under its .md name (the seat`s search, relay data/b589_reads.txt; a .docx of the same name stands '
         'at D:/MY-DOwnloads/PROV1_FORMATION_VERIFICATION_ARCHITECTURE.docx and was not opened or edited); the component is HELD there, and '
         'this file is written beside the SEALE-PROV1-2026 export as the author answered, for the author to append to the project copy.*', '',
         '*No judgement of patentability is made here; that is counsel`s. The claim families are the navigator`s reading at the b588 closing, '
         'which is not in the seat`s hands; each row leaves that column for the author`s paste.*', '',
         '## The instruments since b257', '',
         '| instrument | act of origin | its test | its relay path | claim family (the navigator`s, b588 closing) |', '|:--|:--|:--|:--|:--|']
    for ins, act, test, path in INSTRUMENTS:
        L.append('| %s | %s | %s | %s | (not in the seat`s hands; the author`s paste) |' % (ins, act, test, path))
    L += ['', '## The b257 drafts, cited beside', '',
          'The extraction sweep of b257 (relay data/b257_methodology_sweep.txt) drafted eight modules, now at `%s/`: %s, with `INDEX.md` '
          'grading each row AIM.' % (tdir, ', '.join('`%s`' % d for d in B257_DRAFTS)), '',
          '*Written 2026-10-01 by b589; committed alone in this local-only repository.*', '']
    b = (NL.join(L) + NL).encode('utf-8')
    open(p + '.tmp', 'wb').write(b)
    os.replace(p + '.tmp', p)
    present = [d for d in B257_DRAFTS if os.path.exists(os.path.join(tdir, d))]
    put_txt('b589_sweep.txt', ['b589 -- COMPONENT 3: THE EXTRACTION SWEEP TWO, (R199)(4). ### HELD at the missing file; COUNTS AND THE POINTER ONLY '
                               '(the author`s answer).', '',
                               '### the named target: PROV1_FORMATION_VERIFICATION_ARCHITECTURE.md -- not on any reachable drive under that name '
                               '(relay data/b589_reads.txt); a .docx of that name at D:/MY-DOwnloads, not opened ; HELD',
                               '### the pointer: patent-package-BACKUP-2026-08-29/%s (local-only repository), %d bytes, sha256 %s' % (
                                   SWEEP_FILE, len(b), hashlib.sha256(b).hexdigest()),
                               '### the counts: instruments listed %d ; b257 drafts cited %d of %d present at their path ; claim-family cells left '
                               'for the author %d' % (len(INSTRUMENTS), len(present), len(B257_DRAFTS), len(INSTRUMENTS)),
                               '### ### **COMPONENT 3 HELD AT THE MISSING FILE; THE DRAFT LANDED IN THE PATENT REPOSITORY.**'])
    put_json('b589_sweep.json', dict(file=SWEEP_FILE, bytes=len(b), sha256=hashlib.sha256(b).hexdigest(), instruments=len(INSTRUMENTS),
                                     drafts_present=len(present), held=True))


# ================================================================================ COMPONENT 6 -- THE WORK-ORDER LINES, THE SCORES, THE RECORD
WO = dict(
    constellation=('W-ORD-CONSTELLATION-RERUN', 12090, '(R199)(3)', 'STARTED AND LANDED'),
    threeway=('W-ORD-LI-THREE-WAY', 11703, '(R199)(5)(a)', 'RUN, H30a SCORED'),
    keiper=('W-ORD-KEIPER-FACE', 11704, '(R199)(5)(b)', 'RE-PRICED ON THE MATHLIB READ'),
    toolchain=('the toolchain item', 11664, '(R199)(5)(c)', 'RE-MEASURED AGAINST de5ce8a9'),
    product=('W-ORD-GRH-WEIL', 11373, '(R199)(6)', 'REMAINDER 5, A PRICED ITEM, NOT STARTED, THE PRODUCT LEMMA'),
)


def _wo_texts():
    C = jl('b589_constellation_summary.json')
    T = jl('b589_three_way.json')
    K = jl('b589_keiper_read.json')
    V = jl('b589_lv_remeasure.json')
    P = jl('b589_product_price.json')
    lv = V['meta'].get('price', '')
    return dict(
        constellation='twenty tables read at the current pins (the nineteen of relay data/b586_corroboration.txt and E_DIFFICULTY_THEOREM`s '
                      'new table), the current version and the edition where one exists, one bank per table (relay data/b589_constellation_*.txt); '
                      '%d cells moved, superseded in the table`s own row form inside the banks and carried into each document at its next '
                      'edition; b454`s table re-searched case-insensitively at its own fixed ledgers, %d rows newly located (%s). The '
                      'rounded-profile check was not exercised (source only).' % (C['moved'], len(C['newly']), '; '.join(C['newly'])),
        threeway='run under the author`s ruling: the zero sum (relay data/b562_drift.txt), the arithmetic limit (data/b563_per_n.txt) and '
                 'Keiper`s expansion through the Stieltjes constants agree within the sum of their floors at every n up to twelve, H30a %s '
                 '(relay data/b589_three_way.txt); a bench, graded READING.' % T['H30a'],
        keiper='re-priced at two lemmas of substance on the Mathlib read at de5ce8a9 (relay data/b589_keiper_read.txt): Mathlib holds the '
               'pole of riemannZeta at 1, its constant term and the pole-plus-entire split, and no Stieltjes constant beyond the zeroth by '
               'name; the kernel holds the derivative form (li_coeff_eq_taylorCoeff, v0.9); the two lemmas are the Keiper-Taylor identity '
               'and computable bounds for the constants it consumes. Trigger unchanged, now met by the three-way bench.',
        toolchain='re-measured in a scratch worktree removed after its bank (relay data/b589_lv_remeasure.txt): %s The branch is kept, '
                  'unedited; nothing merged.' % lv,
        product='for two configurations of the schema, the sum (carrier union, multiplicities added, rhs added, targets conjoined) is a '
                'configuration, and its criterion is the conjunction of the two by h2_sign_cfg_iff_target; priced at one lemma of substance, '
                'the summed explicit formula, and bookkeeping; the instance ζ · L(s, χ_d) as the Dedekind zeta of a quadratic field priced '
                'beside it as a separate item (relay data/b589_product_price.txt). Trigger: the author`s word.')


def workorder_lines():
    """### PLACE-papers OPEN_TRAILS: one appended line per work-order the act moved."""
    Q = _Q()
    t = _wo_texts()
    lines = {}
    out = []
    for k, (name, at, rule, title) in WO.items():
        h = '*Appended 2026-10-01 by b589 to %s (:%d), under the author’s ruling `(R199)`%s -- %s:*' % (name, at, rule[6:], title)
        Q.guard_absent(Q.OT, h)
        out.append(Q.append_to(Q.OT, '\n%s %s\n' % (h, t[k])))
        lines[k] = Q.line_of(Q.OT, h)
    put_json('b589_workorders.json', dict(lines=lines, appends=out))
    print(lines)


SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7', 'S1', 'S2', 'S3', 'S4', 'S5')
V015 = '21c8c522bfc8c7bff4bf7b4c4ddeb66e10eaf3dc'
PRE_HEADS = {'SIDE-kernel': '0256e9e1', 'SIDE-lv-conservation': '2f71068a', 'SIDE-effects': 'ef4cff77',
             'SIDE-silence-principle': '667c2548', 'SIDE-compression': 'e9a5a368', 'SIDE-structural-error-correction': '6a4f4829',
             'SIDE-cosmo': 'c5cba30c', 'SIDE-grh-transfer': '858cbf6', 'SIDE-rcurve': 'd5f33b4'}


def scores():
    H, C, T, K, V, P = (jl('b589_h28.json'), jl('b589_constellation_summary.json'), jl('b589_three_way.json'), jl('b589_keiper_read.json'),
                        jl('b589_lv_remeasure.json'), jl('b589_product_price.json'))
    E = jl('b589_edition.json')
    ch = sorted(set(x for x in (g(PP, 'diff', '--name-only', PRE_PP) + NL + g(PP, 'diff', '--name-only', PRE_PP, 'HEAD') + NL +
                                g(PP, 'ls-files', '--others', '--exclude-standard', 'phase1.5', 'phase2')).split(NL) if x.strip()))
    kmain = g(EFK, 'rev-parse', 'main').strip()
    heads_ok = all(g('D:/' + r, 'rev-parse', 'main').strip().startswith(h) for r, h in PRE_HEADS.items())
    trial = g(LVK, 'rev-parse', '--short=7', 'toolchain-trial-b551').strip()
    cur_same = g(PP, 'hash-object', CUR).strip() == E['cur_blob']
    faces = [l for l in g(ROOT, 'diff', '--name-only', '83571aab', '--', 'data/').split(NL) if re.search(r'b5\d\d_registration', l)
             and 'b589_' not in l]
    h28 = H['H28a'] == H['H28b'] == H['H28c'] == 'HELD' and H['held'] is None
    stiel = K['patterns']['the Stieltjes constants by name']
    nt_stiel = [h for h in stiel['hits'] if 'NumberTheory' in h]
    laurent = [h for h in K['patterns']['the residue / Laurent expansion of riemannZeta at 1']['hits'] if 'riemannZeta_residue_one' in h
               or 'tendsto_riemannZeta_sub_one_div' in h]
    first = V.get('first_error')
    order = V['meta']['order']
    gb = 'SIDELvConservation.GammaBounds'
    n5 = first is not None and gb in order and order.index(first) <= order.index(gb)
    priced_one = 'ONE LEMMA OF SUBSTANCE' in ' '.join(P['price'])
    S = dict(
        N1=('HELD' if H['table_rows'] <= 6 and h28 else 'REFUTED', 'the table has %d rows; H28a %s, H28b %s (+%d against %d), H28c %s; no '
            'sentence held' % (H['table_rows'], H['H28a'], H['H28b'], H['body_dn'], H['allowed'], H['H28c'])),
        N2=('HELD' if C['moved'] < 10 and len(C['newly']) >= 1 else 'REFUTED', '%d cells moved across %d tables (the one AMC row, in the '
            'current version and the edition); b454`s table, rows newly located %d %s' % (C['moved'], C['tables'], len(C['newly']), C['newly'])),
        N3=('HELD' if T['H30a'] == 'HOLDS' else 'REFUTED', 'H30a %s, misses %s' % (T['H30a'], T['misses'] or 'none')),
        N4=('HELD' if laurent and not nt_stiel else 'REFUTED', 'the Laurent disjunct, read: Mathlib holds the pole at 1, the constant term '
            'and the pole-plus-entire split (%s), not the higher coefficients; the Stieltjes constants by name: none in NumberTheory; '
            'the Keiper face re-prices at two lemmas of substance' % ', '.join(sorted(set(re.sub(r':.*', '', h) for h in laurent))[:2])),
        N5=('HELD' if n5 else 'REFUTED', 'the first module whose own source errs: %s (GammaBounds is %s in the order), its dependents %d; '
            'stopped at the memory hold before any error could be counted: %d modules' % (
                first, 'position %d' % (order.index(gb) + 1) if gb in order else 'absent', len(V.get('first_error_dependents', [])),
                len(V.get('stopped', [])))),
        N6=('HELD' if priced_one else 'REFUTED', 'one lemma of substance, the summed explicit formula, and bookkeeping; the criterion free by '
            'h2_sign_cfg_iff_target; the Dedekind identification of the instance priced beside as a separate item'),
        N7=('HELD' if kmain == V015 and heads_ok and trial == 'f22ff35' and cur_same and not faces and set(ch) <= {'FINDINGS.md', 'OPEN_TRAILS.md', ED}
            else 'REFUTED', 'nothing deposits; kernel mains %s; the trial branch at %s; the current version %s; sealed faces changed %s; '
            'PLACE-papers changed at %s' % ('unmoved' if kmain == V015 and heads_ok else '### MOVED', trial, 'unedited' if cur_same else '### EDITED',
                                            faces or 'none', ch)),
        S1=('HELD' if H['table_rows'] == 4 and H['body_dn'] == 2 == H['allowed'] else 'REFUTED', 'four rows; the body +2 against 2'),
        S2=('HELD' if 'the E-Difficulty cross-link verdict DISTINCT' in C['newly'] else 'REFUTED', 'the cross-link row newly located at OPEN_TRAILS :773'),
        S3=('HELD' if T['H30a'] == 'HOLDS' and max(T['rows'], key=lambda r: max(r['r_zk'], r['r_ak'], r['r_az']))['r_ak'] ==
            max(max(r['r_zk'], r['r_ak'], r['r_az']) for r in T['rows']) else 'REFUTED', 'H30a holds; the arithmetic route the closest to its floor'),
        S4=('HELD' if laurent and not nt_stiel else 'REFUTED', 'the residue held (`riemannZeta_residue_one`); no Stieltjes constant by name'),
        S5=('HELD' if (set(ch) | {'OPEN_TRAILS.md'}) == {'FINDINGS.md', 'OPEN_TRAILS.md', ED} and kmain == V015 and heads_ok else 'REFUTED',
            'the PLACE-papers files changed are FINDINGS, OPEN_TRAILS (the work-order lines and the record, which follow or precede this '
            'scoring) and the edition; no kernel main moves (changed at scoring: %s)' % ch),
    )
    put_json('b589_scores.json', S)
    for k in SCORE_KEYS:
        print('  %-4s %s -- %s' % (k, S[k][0], S[k][1][:180]))


TITLE_HEAD = ('## The comprehensive housekeeping act: E_DIFFICULTY_THEOREM`s table and edition; the constellation re-read; the TECHNE '
              'extraction sweep two; the three-way λ_n table; the Keiper read; the lv re-measure; the product lemma priced')
TRAIL_HEAD = ('### b589 — lane three, act seventeen under (R199): the comprehensive housekeeping act -- E_DIFFICULTY_THEOREM`s table and '
              'edition, the constellation re-read, the sweep (HELD), the three research items, the product lemma priced')


def records_pp():
    Q = _Q()
    S, H, C, T, V, WL_, W1 = (jl('b589_scores.json'), jl('b589_h28.json'), jl('b589_constellation_summary.json'), jl('b589_three_way.json'),
                              jl('b589_lv_remeasure.json'), jl('b589_workorders.json'), jl('b589_weight_lines.json'))
    title = TITLE_HEAD.replace('the constellation re-read', 'the constellation re-read over %d tables with %d cells moved' % (C['tables'], C['moved'])) \
        .replace('the TECHNE extraction sweep two', 'the TECHNE extraction sweep two HELD at the missing file')
    Q.guard_absent(Q.FIND, title[:80])
    e = ['', title, '',
         '*Filed at b589 on the author’s ruling `(R199)`. Banks: relay `data/b589_edition_EDIFF.txt`, `data/b589_ediff_terms.txt`, '
         '`data/b589_constellation_summary.txt` and one bank per table, `data/b589_constellation_b454.txt`, `data/b589_sweep.txt`, '
         '`data/b589_three_way.txt`, `data/b589_keiper_read.txt`, `data/b589_lv_remeasure.txt`, `data/b589_product_price.txt`. Nothing deposits.*', '',
         '**E_DIFFICULTY_THEOREM** (`(R199)(2)`): its four tier-block terminals re-printed at SIDE-kernel v1.1, v1.4 and v1.7 and its '
         'Correspondence table written from them by the house form (four rows, b450’s “THERE IS NO TABLE” superseded); then `%s`, v1.0.4, '
         'beside v1.0.3 unedited: the two bullets say what `sieve_ceiling` and `e_difficulty` state at their pins; the cross-link verdict '
         'credited beneath the census note in its own words; seven ceiling corrections by the census / totality pair and one fact correction '
         '(the deposit pin by REGISTRY :962), as the author answered. H28a %s · H28b %s (%+d against %d) · H28c %s.' % (
             ED, H['H28a'], H['H28b'], H['body_dn'], H['allowed'], H['H28c']), '',
         '**The constellation re-read** (`(R199)(3)`): %d tables, %d cells moved -- one AMC row whose three per-conjecture terminals are '
         'retired to a comment at SIDE-effects main, as the row already says -- superseded inside the banks; b454’s table re-searched '
         'case-insensitively, %d rows newly located.' % (C['tables'], C['moved'], len(C['newly'])), '',
         '**The extraction sweep two** (`(R199)(4)`): HELD at the missing file; drafted into the local-only patent repository, as the author '
         'answered; a .docx of the specification’s name stands at D:/MY-DOwnloads, not opened (defect (a)).', '',
         '**The three research items** (`(R199)(5)`): H30a %s; the Keiper face re-priced at two lemmas of substance; the lv re-measure: %s' % (
             T['H30a'], V['meta'].get('price', '')), '',
         '**The product lemma** (`(R199)(6)`): priced at one lemma of substance, the summed explicit formula, and bookkeeping; nothing built.', '',
         '**The scores.** ' + ', '.join('(%s) %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.', '',
         '**Next.** Per `(R199)(7)`: the next edition in the order (SIMPLICITY held, then RESIDUE, then the two companions), or '
         'SIMPLICITY-FACE on the author’s word; the author rules at the closing.', '',
         '*Nothing deposits; no kernel main touched; v1.0.3, README, REGISTRY, ERRATA and both pages unwritten; nothing here is a statement '
         'about RH, GRH or any zero beyond the compiled statements’ own words or a measurement’s own numbers.*', '']
    r = Q.append_to(Q.FIND, NL.join(e))
    Q.guard_absent(Q.OT, TRAIL_HEAD)
    rows_ = ['', TRAIL_HEAD, '',
             '**(R199) ratified.** (1) b588 at its weight. (2) E_DIFFICULTY_THEOREM’s table and edition in one act. (3) The constellation '
             're-read. (4) The extraction sweep two. (5) The three research items. (6) The product lemma priced. (7) The act after.', '',
             '**Entered:** FINDINGS.md:%d (b588’s weight), :%d (the TECHNE credit re-read), :%d (the entry); OPEN_TRAILS.md:%s (the work-order '
             'lines), this record; PLACE-papers `%s` (created); the patent repository’s `%s` (created, committed alone).' % (
                 W1['lines']['weight'], W1['lines']['reread'], Q.line_of(Q.FIND, title[:80]), ', :'.join(str(v) for v in WL_['lines'].values()),
                 ED, SWEEP_FILE), '',
             '**Answered before the seal, by the author:** the sweep HELD at the missing file and drafted into the patent repository; the '
             'ceiling clause at :24, :48, :136, :138, :177 by the census / totality pair and the fact clause at :203; the credit beneath the '
             'census note :183 in the verdict’s own words, TECHNE v8.3’s credit re-read against the same text (it agrees); the supersessions in '
             'the banks only.', '',
             '**HELD:** Component 3, at the missing `PROV1_FORMATION_VERIFICATION_ARCHITECTURE.md`; a `.docx` of that name stands at '
             'D:/MY-DOwnloads, found after the seal by the reads bank’s walk, not opened -- for the author.', '',
             '**' + ' · '.join('(%s) %s' % (k, S[k][0]) for k in SCORE_KEYS) + '.**', '',
             '**Next:** per `(R199)(7)`, the next edition in the order -- SIMPLICITY held, then RESIDUE, then BALANCE_AND_POSITIVITY and '
             'FACES_OF_H2 -- or SIMPLICITY-FACE on the author’s word; the author rules on the closing.', '',
             '**No `sorry` on any `main`.** Nothing deposits; no kernel main touched; the pages untouched; row U1 unedited; the four lists stay '
             'OPEN; nothing here is a statement about RH, GRH or any zero.', '']
    r2 = Q.append_to(Q.OT, NL.join(rows_))
    put_json('b589_findings.json', dict(entry_line=Q.line_of(Q.FIND, title[:80]), title=title, append=r))
    put_json('b589_trail.json', dict(line=Q.line_of(Q.OT, TRAIL_HEAD), head=TRAIL_HEAD, append=r2))
    print(jl('b589_findings.json')['entry_line'], jl('b589_trail.json')['line'])


def desk():
    S = jl('b589_scores.json')
    NK = ('N1', 'N2', 'N3', 'N4', 'N5', 'N6', 'N7')
    SK = ('S1', 'S2', 'S3', 'S4', 'S5')
    L = ['=' * 104, 'b589 -- THE DESK. ### **THE EXPECTATIONS, SCORED ON THE BANKS.**', '=' * 104, '',
         '### THE NAVIGATOR`S SEVEN.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in NK]
    L += ['', '### THE SEAT`S FIVE.', '-' * 104] + ['  **(%s)** ### **%s.** -- %s' % (k, S[k][0], S[k][1]) for k in SK]
    L += ['', '### ### **THE NAVIGATOR`S : HELD %d ; REFUTED %d.** ### ### **THE SEAT`S : HELD %d ; REFUTED %d.**' % (
        sum(S[k][0] == 'HELD' for k in NK), sum(S[k][0] == 'REFUTED' for k in NK),
        sum(S[k][0] == 'HELD' for k in SK), sum(S[k][0] == 'REFUTED' for k in SK)), '']
    L += rd('b589_defects.txt').rstrip(NL).split(NL)
    put_txt('b589_desk_notes.txt', L)


def components():
    S, H, C, T, V, W1, WL_, fj, tj = (jl('b589_scores.json'), jl('b589_h28.json'), jl('b589_constellation_summary.json'), jl('b589_three_way.json'),
                                      jl('b589_lv_remeasure.json'), jl('b589_weight_lines.json'), jl('b589_workorders.json'),
                                      jl('b589_findings.json'), jl('b589_trail.json'))
    L = ['b589 -- THE COMPONENTS, BANKED UNDER (R199).', '',
         '### COMPONENT 0 : the process listing (no orphan) ; b588`s closing push-out relay 0b552b52 ; push-b588* branches deleted by name '
         '(data/b589_branches.txt) ; the kept branches untouched',
         '### (R199)(1) : b588`s weight FINDINGS :%d ; the TECHNE credit re-read :%d (agrees)' % (W1['lines']['weight'], W1['lines']['reread']),
         '### COMPONENT 1 : E_DIFFICULTY -- terminals re-printed (data/b589_ediff_terms.txt) ; the table, %d rows ; the edition %s ; H28a %s H28b %s '
         'H28c %s ; N1 %s' % (H['table_rows'], ED, H['H28a'], H['H28b'], H['H28c'], S['N1'][0]),
         '### COMPONENT 2 : the constellation re-read, %d tables, %d cells moved ; b454`s table, %d rows newly located ; N2 %s' % (
             C['tables'], C['moved'], len(C['newly']), S['N2'][0]),
         '### COMPONENT 3 : the extraction sweep two -- HELD at the missing file ; drafted to the patent repository (data/b589_sweep.txt)',
         '### COMPONENT 4 : the three-way bench, H30a %s (N3 %s) ; the Keiper read, re-priced at two lemmas (N4 %s) ; the lv re-measure, first '
         'own error %s, %d dependents, %d modules stopped at the memory hold (N5 %s)' % (
             T['H30a'], S['N3'][0], S['N4'][0], V.get('first_error'), len(V.get('first_error_dependents', [])), len(V.get('stopped', [])), S['N5'][0]),
         '### COMPONENT 5 : the product lemma priced, one lemma of substance (N6 %s)' % S['N6'][0],
         '### COMPONENT 6 : FINDINGS :%d ; OPEN_TRAILS :%d (the record) ; the work-order lines :%s ; next: per (R199)(7), the author`s choice '
         'awaiting the closing ; N7 %s' % (fj['entry_line'], tj['line'], ', :'.join(str(v) for v in WL_['lines'].values()), S['N7'][0])]
    put_txt('b589_components.txt', L)


if __name__ == '__main__':
    cmd = sys.argv[1] if len(sys.argv) > 1 else ''
    fn = globals().get(cmd)
    if not callable(fn) or cmd.startswith('_'):
        print('usage: b589_record.py <subcommand>')
        sys.exit(2)
    sys.exit(fn(*sys.argv[2:]) or 0)
