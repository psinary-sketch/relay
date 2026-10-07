# -*- coding: utf-8 -*-
"""b638_worklist.py -- THE ACT'S DATA, UNDER (R248). ### DATA AND READ-ONLY HELPERS ONLY; NOTHING HERE WRITES.

### ### b638: LANE THREE, ACT SIXTY-FIVE -- THE KEYSTONE CENSUS AT v0.6 UNDER THE READER'S CLAUSE: A PLAIN OPENING, A SHARED GLOSSARY,
### PROVENANCE UNDER THE UPSTREAM EXCLUSION, THE PREMISE TABLE AT 50 HEADS WITH ITS UNNAMED RESIDUE; THE PWSetup MOVES HELD TO A FIELD
### PRINT; THE MIRROR REBUILT ON THE 73-FILE ROSTER. Here: the pins before the act; the lists in force and the lists this act writes for the
### pages; the glossary's source and mark; the census paths; the structure types among b637's 93 moves with their declarations; the ledger
### lines; the mirror's name; the sealed tools; the next act.
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
GS = 'D:/SIDE-global-section'
PRE_PP = '5c4247b'          # ### PLACE-papers main before the act (b637's correction beneath its record)
PRE_RELAY = '2aa41700'      # ### relay main before the act (b637's closing)
STEPZERO = 'c4134e30'       # ### relay: b637's closing push-out bank, committed at step zero
DATE = '2026-10-07'
SP = 'C:/Users/ECHOCH~1/AppData/Local/Temp/claude/D--/b8acf12c-00ee-4167-9344-809d3aa94847/scratchpad'
PLANTED_DIR = SP + '/b637_planted'   # ### b637's planted module, copied here whole (B637Planted.lean sha256 735629f5...)

PAGE = 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md'
DIR_PAGE = 'THE_CLAUSE_AT_THE_DIRICHLET_INSTANCE.md'
PNAME = {'zeta': PAGE, 'chi': DIR_PAGE}
OLD_NODES = {'zeta': 'b632_nodes_zeta.txt', 'chi': 'b632_nodes_chi.txt'}     # ### the lists in force before this act (since b632)
NODES = {'zeta': 'b638_nodes_zeta.txt', 'chi': 'b638_nodes_chi.txt'}         # ### the lists in force from Component 3: b632's with the mark
PROBE = {'zeta': 'b635_probe_out_zeta.txt', 'chi': 'b635_probe_out_chi.txt'}  # ### the probes in force since b635 (its Pages answer)
LOCAL_BANK = 'data/b628_intake_crank_v0_5.txt'
TABLE_FILES = ['terminal_table.md', 'terminal_table.json', 'terminal_table_prior.json', 'terminal_table_run.txt', 'terminal_table_diff.json']

# ### (R248)(4): THE GLOSSARY -- one shared source, relay data/glossary.txt, written through the Write tool at Component 1 and committed alone;
# ### the generator prints it beneath a page's head line when the page's list carries the mark (a list without the mark emits as before,
# ### so the frozen controls' old lists still re-emit byte for byte); the census at v0.6 prints the same block through the generator's own
# ### renderer, so the three read byte for byte alike.
GLOSSARY = 'data/glossary.txt'
GLOSSARY_MARK = '# glossary'

# ### the census
CEN6 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_6.md'
CEN5 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_5.md'
CEN4 = 'phase2/method/THE_KEYSTONE_CENSUS_v0_4.md'
SIEVE6 = 'phase2/method/THE_FINDINGS_AS_THEY_STAND_v0_6.md'
MONO = 'day1/A_Place_to_Stand_v5_18.md'
CEN5_PREMISES = (689, 740)  # ### the census at v0.5: the 42 named premises, their table and its two notes
CEN5_TAG = '<!-- b633 (R243) THE v0.5 EDITION’S BACK MATTER, 2026-10-06 -->'

# ### (R248)(2): THE STRUCTURE TYPES AMONG b637's 93 MOVES (relay data/b637_rerun.txt), each at its declaration, read by git at its pin;
# ### its parameters as the declaration binds them and the section variables in force (the context the rule's typing reads a field in).
EF, EF_PIN = 'D:/SIDE-explicit-formula', '8c51431'
LV, LV_PIN = 'D:/SIDE-lv-conservation', '2f71068'
STRUCTS = [
    dict(name='PWSetup', repo=EF, kernel='SIDE-explicit-formula', pin=EF_PIN, path='SIDEExplicitFormula/PowerLimit.lean', line=245,
         ctx={'Z': 'Zeta23.ZeroConfig', 'g0': 'ℝ → ℝ', 'L': 'ℝ', 'M': 'ℝ'}),
    dict(name='TailHyp', repo=EF, kernel='SIDE-explicit-formula', pin=EF_PIN, path='Zeta23/Tail.lean', line=288,
         ctx={'Z': 'ZeroConfig', 'P': 'Params', 'T': 'ℝ', 'A₀': 'ℝ', 'C₁': 'ℝ'}),
    dict(name='BlockInputs', repo=EF, kernel='SIDE-explicit-formula', pin=EF_PIN, path='Zeta23/Assembly/Inputs.lean', line=58,
         ctx={'Z': 'ZeroConfig', 'P': 'Params', 'T': 'ℝ'}),
    dict(name='TailInputs', repo=EF, kernel='SIDE-explicit-formula', pin=EF_PIN, path='Zeta23/Assembly/Inputs.lean', line=73,
         ctx={'Z': 'ZeroConfig', 'P': 'Params', 'T': 'ℝ', 'θ₀': 'ℝ'}),
    dict(name='PaperInputs', repo=EF, kernel='SIDE-explicit-formula', pin=EF_PIN, path='Zeta23/Hypotheses.lean', line=163,
         ctx={'Z': 'ZeroConfig'}),
    dict(name='RiemannVonMangoldt', repo=EF, kernel='SIDE-explicit-formula', pin=EF_PIN, path='Zeta23/Hypotheses.lean', line=83,
         ctx={'Z': 'ZeroConfig'}),
    dict(name='SelfDualFE', repo=LV, kernel='SIDE-lv-conservation', pin=LV_PIN, path='SIDELvConservation/FieldLayer.lean', line=56,
         ctx={'K': 'Type*', 'q': 'K', 'g': 'ℕ', 'p': 'ℕ → K'}),
    dict(name='ZeroActingPairing', repo=LV, kernel='SIDE-lv-conservation', pin=LV_PIN, path='SIDELvConservation/ZeroActingPairing.lean', line=41,
         ctx={'lam_A': 'ℕ → ℝ', 'lam_Z': 'ℕ → ℝ', 'ledger': 'ℕ → ℝ'}),
]
B632_G036 = ('data/b632_reader_answers.txt', 36)    # ### the second reader's G036 reading at b632
B632_KEY_G036 = ('data/b632_key.txt', 38)

# ### the ledger lines the act reads and addresses
B637_ENTRY = 7833           # ### FINDINGS: b637's entry
B637_WEIGHT_PRIOR = 7831    # ### FINDINGS: b636 at its weight (b637's line)
B637_RECORD = 13339         # ### OPEN_TRAILS: b637's trail record
B637_CORRECTION = 13363     # ### OPEN_TRAILS: b637's correction beneath its record
FORM = 11864                # ### OPEN_TRAILS: the form of an edition, its title clause ("the title naming objects and conditions")
NAME_TITLE = 11934          # ### OPEN_TRAILS: the name-and-title exception, beside the form's clauses
PRECEDENCE = 12228          # ### OPEN_TRAILS: the precedence order
PAGE_CLAUSE = 12190         # ### OPEN_TRAILS: an edition naming page nodes changes both pages' Placement
LOAD_BEARING = 12699        # ### OPEN_TRAILS: the load-bearing clause
CRITERION = 12955           # ### OPEN_TRAILS: the domain-condition criterion
UNLISTED_LINE = 13221       # ### OPEN_TRAILS: PREDICATE-UNLISTED, standing (b633)
UPSTREAM_LINE = 13335       # ### OPEN_TRAILS: the upstream clause, standing (b637)
NAME_LINE = 13337           # ### OPEN_TRAILS: the name clause, standing (b637)
BUILD_CLAUSE = 12356        # ### OPEN_TRAILS: the build clause, standing (b600)
SEAL_RULE = 13307           # ### OPEN_TRAILS: the seal rule, standing (b636)
FERRY_LINES = (11864, 12228, 12354, 12356, 12799, 13167, 13363)

# ### THE MIRROR -- built after the act's last PLACE-papers push by the unedited builder on the 73-file roster; the name through -DateTag
# ### (the builder deletes a same-named zip and stage, and mirror-refresh-2026-10-07.zip is b635's)
ROSTER = 'tools/mirror_roster.json'
BUILDER = 'tools/mirror_build.ps1'
MIRROR_TAG = '2026-10-07-b638'
MIRROR_ZIP = 'D:/MY-DOwnloads/mirror-refresh-%s.zip' % MIRROR_TAG
MIRROR_PREV = 'D:/MY-DOwnloads/mirror-refresh-2026-10-07.zip'   # ### b635's build, on the 70-file roster
ROSTER_FILES = 73

# ### THE SEALED TOOLS -- this act's own tools that take no edit by any means until the act closes (OPEN_TRAILS :13307); their sha256
# ### recorded at the seal by the suite (`--seal`, data/b638_seal_hashes.json) and recomputed at the close by G-SEAL-HASHES
SEALED = ('b638_worklist.py', 'b638_tests.py', 'b638_record.py', 'b638_checks.py', 'b638_closing.py', 'b638_reg_gate.py', 'b638_regspec.py')

NEXT_ROUTES = [('b639, on the author`s word: the deposit -- the author`s own act on the (R110) route, the mirror rebuilt at b638`s close and '
                'the deposit bank refreshed to the census at v0.6, the seat preparing and depositing nothing; or, the deposit held, the '
                'per-cluster fact-item editions of Phase 1.2 under the reader`s clause', [])]


def show(path, rev=PRE_PP, repo=PP):
    r = subprocess.run(['git', '-C', repo, 'show', '%s:%s' % (rev, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13), '') if r.returncode == 0 else None


def lines_of(t):
    l = (t or '').split(NL)
    return l[:-1] if l and l[-1] == '' else l
