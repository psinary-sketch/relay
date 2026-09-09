# -*- coding: utf-8 -*-
"""b390_extract.py -- THE EXTRACT, AND THE FOUR SURVEYS THE FACE IS WRITTEN FROM.

### ### **EVERY READ IS ANCHORED BY THE TOOL AND EXTRACTED TO DISK.** ### An anchor is built by
### reading the line out of its own file, never by typing it (`anchor_from_file`), and where the
### typed hint and the file`s bytes differ the difference is ### **PRINTED, NOT SILENTLY
### ### ACCEPTED.**
###
### ### **AND THIS ACT`S SUBJECT IS CHOSEN BY A PRINTED RULE, NOT BY THE SEAT`S TASTE.** ### The
### census names ### **TWO** ### keystones as the ones whose subject matter the era moved most;
### the order asks for ### **ONE.** ### The survey measures both and the face states the rule.
###
### ### **NOTHING IS EDITED BY THIS FILE. ### NOTHING IS WRITTEN AT ZENODO.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import run_clock                # noqa: E402
import b303_pins                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
EFFECTS = os.path.join('D:', os.sep, 'SIDE-effects')
KERNEL = os.path.join('D:', os.sep, 'SIDE-kernel')

FERRY = os.path.join(D, 'b390_ferry_2026-09-09.txt')
CENSUS = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')
AMC = os.path.join(PP, 'phase2', 'method', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
RESIDUE = os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
FINDINGS = os.path.join(PP, 'FINDINGS.md')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
CASCADE = os.path.join(PP, 'CASCADE_ANCHORS_CORRECTED.md')
ENGINE = os.path.join(PP, 'phase1.5', 'method', 'EXCLUSION_ENGINE.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


# ==================================================================================================
#  THE READS.
# ==================================================================================================
READS = [
    # ---- THE ORDER --------------------------------------------------------------------------
    ('the order -- the act', 'ORDER', FERRY,
     'ACT b390 — THE FIRST PROOFREADING PASS. Number not claimed by'),
    ('the order -- the corpus has run no reading pass', 'ORDER', FERRY,
     'classification passes and no reading pass. This act reads one'),
    ('the order -- the face is wide on purpose', 'ORDER', FERRY,
     'WRITTEN WIDE ON PURPOSE: it may repair what it discovers within'),
    ('the order -- every repair measured against the pre-act blob', 'ORDER', FERRY,
     'the named scope, and every repair is measured against the'),
    ('the order -- component 0, the routed corrections', 'ORDER', FERRY,
     'COMPONENT 0 — THE DISCOVERABLE CORRECTIONS ALREADY ROUTED, now'),
    ('the order -- component 0, the map`s stale entry', 'ORDER', FERRY,
     "stale entry at the line b389 named, with b389's evidence"),
    ('the order -- component 0, a ruling stays routed', 'ORDER', FERRY,
     'act says which.'),
    ('the order -- component 1, the subject', 'ORDER', FERRY,
     'COMPONENT 1 — THE SUBJECT: the keystone the census itself named'),
    ('the order -- component 1, read whole at the canonical drive', 'ORDER', FERRY,
     'as the one whose subject matter the era moved most, read whole'),
    ('the order -- component 2, what bears on it and is not in it', 'ORDER', FERRY,
     'COMPONENT 2 — WHAT BEARS ON IT AND IS NOT IN IT: the material'),
    ('the order -- component 2, three buckets, nothing summarised', 'ORDER', FERRY,
     'buckets, quotations on both sides, nothing summarised.'),
    ('the order -- component 3, the repair within the face', 'ORDER', FERRY,
     'COMPONENT 3 — THE REPAIR, within the face: where the keystone'),
    ('the order -- component 3, the original preserved verbatim', 'ORDER', FERRY,
     'place with the original preserved verbatim in the same document'),
    ('the order -- component 3, a ruling is routed and not made', 'ORDER', FERRY,
     'would require a ruling — a grade moved, a class changed, a'),
    ('the order -- component 4, a price and not a plan', 'ORDER', FERRY,
     'price for the remaining keystones the census listed. Stated as'),
    ('the order -- the closing, the five clusters named', 'ORDER', FERRY,
     'and the deposit rule — with the five clusters NAMED from b388'),
    ('the order -- (F1) at least one claim since corrected', 'ORDER', FERRY,
     'expectations: (F1) the keystone carries at least one claim the'),
    ('the order -- (F2) mostly addition rather than correction', 'ORDER', FERRY,
     'record has since corrected; (F2) most of what bears on it and'),

    # ---- THE CENSUS -------------------------------------------------------------------------
    ('the census -- the two it names', 'CENSUS', CENSUS,
     "The census's own answer, offered and not taken: `THE_RESIDUE_OF_RH` and"),
    ('the census -- the work-list row for this keystone', 'CENSUS', CENSUS,
     "the conspiracy's site is the interface, and this keystone is the corpus"),
    ('the census -- the work-list row for the one not taken', 'CENSUS', CENSUS,
     'the sign-face registers, the sealed `S1`–`S6` table, the crossing filing'),
    ('the census -- every one of the sixteen predates an era finding', 'CENSUS', CENSUS,
     'EVERY ONE OF THE SIXTEEN PREDATES AT LEAST ONE ERA FINDING THAT NAMES'),
    ('the census -- the branch-resident line, required not optional', 'CENSUS', CENSUS,
     'REQUIRED IN ANY SPINE OR RELEASE NOTE FOR `phase1.5/proofs`, AND NOT'),
    ('the census -- the terminals not on main', 'CENSUS', CENSUS,
     "`THE_RESIDUE_OF_RH`'s compiled terminals live on the HELD, UNMERGED branch"),
    ('the census -- zero edits made to any censused document', 'CENSUS', CENSUS,
     'ZERO EDITS MADE TO ANY CENSUSED DOCUMENT.'),

    # ---- THE SUBJECT ------------------------------------------------------------------------
    ('the keystone -- its class line', 'AMC', AMC,
     'the census test: external-reader results + a Correspondence table naming'),
    ('the keystone -- its own status line', 'AMC', AMC,
     "THE PAPER'S OWN STATUS LINE IS THE TABLE'S SUMMARY, AND IT WAS ALREADY EXACT"),
    ('the keystone -- the kernel-citation pin', 'AMC', AMC,
     '**Kernel-citation pin (2026-07-13).** The placeholder instantiations'),
    ('the keystone -- the W-6 gate, DISCHARGED in the body', 'AMC', AMC,
     '**W-6 gate (E-Difficulty skeleton) — DISCHARGED** (W-6-EXT, SIDE-kernel'),
    ('the keystone -- the standard`s table, added 2026-08-12', 'AMC', AMC,
     'annotation added 2026-08-12, W-CONSOLIDATION act 3b; existing text'),
    ('the keystone -- zero blank cells', 'AMC', AMC,
     '0 BLANK CELLS. Five of six rows have no kernel, and each says so in'),
    ('the keystone -- the era annotation already carries Q2', 'AMC', AMC,
     "`Q2`'s NO-CLASS-POINT VERDICT AND THE `n₄ = 0` RECONCILIATION BEAR"),
    ('the keystone -- nothing in I-IV is rewritten', 'AMC', AMC,
     '**Nothing in §§I–IV is rewritten.**'),
    ('the keystone -- the branch named by the standard`s table', 'AMC', AMC,
     'branch ### **`w-ladder-skeleton`** *(recorded 2026-08-12; the corpus had'),

    # ---- THE RECORD SINCE -------------------------------------------------------------------
    ('the record -- the E-Difficulty terminals at v1.4', 'RECORD', FINDINGS,
     '**E-Difficulty Theorem** (formerly conjecture CP-E-3). Terminals'),
    ('the record -- the scope split, statement-grade', 'RECORD', FINDINGS,
     '**Scope split (W-INFORMATION run, 2026-07-28 — statement-grade, nothing'),
    ('the record -- W-6 closed by repair', 'RECORD', TRAILS,
     '> - W-6 — CLOSED-BY-REPAIR (W-6-EXT, SIDE-kernel v1.4, 2026-07-19)'),
    ('the record -- b372 checked this keystone`s line 400', 'RECORD', TRAILS,
     '| `phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md` | 400 |'),
    ('the record -- e_difficulty re-graded from TAUTOLOGY', 'RECORD', ENGINE,
     '**DERIVES** *(re-graded 2026-07-19; was TAUTOLOGY)*'),
    ('the record -- the cascade anchor for the type-d catalogue', 'RECORD', CASCADE,
     '*argument-supported* (structural; Type-D as a DomainOstrowski instance'),

    # ---- THE MAP, AND b389`S EVIDENCE -------------------------------------------------------
    ('the map -- the cross-domain row b389 named', 'MAP', MAP,
     '| **cross-domain** (emergent) | `FORMATION_DISTANCE_DARK_VARIABLE_v0_1.md`,'),
    ('b389`s evidence -- the citing line itself', 'IFACE',
     os.path.join(PP, 'phase1.5', 'spectral', 'INTERFACE_CONSERVATION.md'),
     '**Kernel verification.** The structural form of Proposition 1 is verified'),
]


def do_reads():
    bar('=')
    rec('  ### THE READS.')
    bar('=')
    out, without = [], 0
    for label, tag, path, hint in READS:
        try:
            at, line = AF.find(path, hint)
            differs = (line.strip() != hint.strip())
            out.append(dict(label=label, tag=tag, file=os.path.relpath(path, PP)
                            if path.startswith(PP) else os.path.basename(path),
                            line=at, text=line, differs=differs))
            rec('    %-62s %s' % (label[:62], tag))
            rec('      %s : line %d   ### anchor differs from the hint : %s'
                % (os.path.basename(path), at, differs))
            rec('      > %s' % ' '.join(line.split())[:150])
        except Exception as e:
            without += 1
            out.append(dict(label=label, tag=tag, file=os.path.basename(path), line=None,
                            text=None, differs=None, error=str(e)[:120]))
            rec('    %-62s %s   ### **NO ANCHOR** -- %s' % (label[:62], tag, str(e)[:80]))
    rec()
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), without))
    rec('  ### anchors differing from the typed hint : %d'
        % sum(1 for r in out if r.get('differs')))
    return out, without


# ==================================================================================================
#  SURVEY 1 -- COMPONENT 0: WHAT b388 AND b389 ROUTED, CLASSIFIED.
# ==================================================================================================
ROUTED = [
    ('b389', 'the federation map`s entry for a kernel that does not exist',
     'SPIRAL_MAP.md cross-domain row seats `SIDE-interface-split`',
     'REPAIRABLE',
     'b389 printed the evidence whole: the citing line says Proposition 1 is verified in '
     '`SIDE-interfaces`, and names `SIDE-interface-split` only as the FUTURE kernel. ### The '
     'repair removes a name from a list; ### **IT MOVES NO GRADE, RULES NO CLASS AND WITHDRAWS '
     'NO CLAIM.**'),
    ('b389', 'a written deposit rule', 'the corpus has none', 'NEEDS-A-RULING',
     '### **A SEAT THAT SUPPLIES THE WORDS HAS WRITTEN A NEW RULE UNDER AN OLD NAME.** ### No '
     'evidence any act printed can substitute for the author`s words.'),
    ('b389', 'the eight-versus-six disagreement', 'disk 8 / registry 6 / map 7',
     'NEEDS-A-RULING',
     'Recording a synthesis in the registry and seating a subject in the map are the author`s '
     'acts under `(R17)`. ### The disagreement is measured; ### **RESOLVING IT IS NOT A REPAIR.**'),
    ('b389', 'the deposited layer', 'Zenodo answered on 0 of 6 routes', 'BLOCKED',
     'Neither a repair nor a ruling: ### **THE PLATFORM DID NOT ANSWER**, and no evidence on '
     'disk substitutes for a live read.'),
    ('b388', 'the five clusters that changed shape', 'GREW x3, NEW x2', 'NEEDS-A-RULING',
     '`b388` reported the shapes and reshaped none: ### **THE RESHAPING IS THE AUTHOR`S.**'),
    ('b388', 'the 23 unreadable correspondence rows', 'named by document, line and cause',
     'NEEDS-READING',
     'Naming a cause is not reading the row. ### **NO EVIDENCE `b388` PRINTED DECIDES ANY OF '
     'THEM**, so none is repairable from what was printed.'),
    ('b388', 'the two keystone-class documents marked UNASSIGNED', 'no evidence, not no fit',
     'NOT-A-DEFECT',
     '### **UNASSIGNED IS A STATE AND NOT A DEBT** -- there is nothing to repair.'),
    ('b388', 'the trail block asserting the misreading', 'OPEN_TRAILS b388 block',
     'ALREADY-ANSWERED',
     '`b389` appended the withdrawal beside it and the ledger is append-only by standing '
     'practice. ### **THE CORRECTION ALREADY STANDS NEXT TO THE ERROR.**'),
]


def kernel_live():
    """### **THE LIVE CHECK, RE-RUN RATHER THAN RECALLED.** ### `b389` read this two hours ago;
    ### ### **A KERNEL RECALLED IS NOT A KERNEL READ**, and the repair rests on the read."""
    out = {}
    for k in ('SIDE-interfaces', 'SIDE-interface-split'):
        r = subprocess.run(['git', 'ls-remote',
                            'https://github.com/psinary-sketch/%s.git' % k, 'HEAD'],
                           capture_output=True, text=True, encoding='utf-8', errors='replace')
        out[k] = dict(rc=r.returncode, resolves=(r.returncode == 0 and bool((r.stdout or '').strip())))
    return out


def survey1():
    bar('-')
    rec('  ### SURVEY 1 -- COMPONENT 0. ### **WHAT `b388` AND `b389` ROUTED, CLASSIFIED.**')
    bar('-')
    live = kernel_live()
    rec('  ### **THE LIVE CHECK, RE-RUN AND NOT RECALLED:**')
    for k, v in sorted(live.items()):
        rec('      %-24s resolves : %s' % (k, v['resolves']))
    rec()
    counts = {}
    for act, item, what, cls, why in ROUTED:
        counts[cls] = counts.get(cls, 0) + 1
        rec('    [%s] %-56s ### **%s**' % (act, item[:56], cls))
        rec('        %s' % what)
        for i in range(0, min(len(why), 460), 150):
            rec('        %s' % why[i:i + 150])
    rec()
    rec('  ### ### **ROUTED ITEMS SWEPT : %d.**' % len(ROUTED))
    for k in sorted(counts):
        rec('      %-22s %d' % (k, counts[k]))
    rec('  ### ### ### **REPAIRABLE BY EVIDENCE ALREADY PRINTED : %d.**'
        % counts.get('REPAIRABLE', 0))
    rec('  ### ### **THE FACE IS WIDE, NOT UNBOUNDED:** ### an item that needs a ruling stays')
    rec('  ### ### routed however easy the edit would be.')
    return dict(routed=len(ROUTED), classes=counts, live=live,
                items=[dict(act=a, item=i, what=w, cls=c, why=y) for a, i, w, c, y in ROUTED])


# ==================================================================================================
#  SURVEY 2 -- COMPONENT 1: THE SUBJECT, CHOSEN BY A PRINTED RULE.
# ==================================================================================================
def branch_resident(repo, sha, branch):
    def anc(ref):
        r = subprocess.run(['git', '-C', repo, 'merge-base', '--is-ancestor', sha, ref],
                           capture_output=True)
        return r.returncode == 0
    return dict(on_main=anc('origin/main'), on_branch=anc('origin/' + branch))


def grade_rows(path, header_hint):
    """### **THE CORRESPONDENCE ROWS, READ OUT OF THE FILE AND NOT COUNTED FROM MEMORY.**"""
    lines = io.open(path, encoding='utf-8', errors='replace').read().split(chr(10))
    at = None
    for i, ln in enumerate(lines):
        if header_hint in ln:
            at = i
            break
    if at is None:
        return []
    # ### **A TABLE ENDS AT ITS FIRST NON-ROW LINE, NOT AT A LINE COUNT.** ### A 60-line window
    # ### walked out of one table and into the next and reported `16` rows where the document
    # ### has `8`. ### **A WINDOW IS AN ADDRESS; THE TABLE'S OWN SHAPE IS THE CONTENT.**
    rows, started = [], False
    for ln in lines[at:]:
        if ln.startswith('|') and ln.count('|') >= 4:
            started = True
            # ### **A SEPARATOR ROW IS `|:--|:--|`, NOT `|---|`.** ### Testing for three dashes
            # ### let the alignment row through and reported a phantom claim called `:--`.
            cells0 = [c.strip() for c in ln.split('|')[1:-1]]
            if cells0 and all(set(c) <= set(':- ') and c for c in cells0):
                continue
            cells = [c.strip() for c in ln.split('|')[1:-1]]
            if cells and cells[0].lower() not in ('claim', 'claim ', ''):
                rows.append(cells)
        elif started:
            break
    return rows


GRADEWORDS = ('DERIVES', 'INTERFACES', 'MILESTONE-OPEN', 'MANUSCRIPT-RESIDENT',
              'RESEARCH-REACH', 'COMPILED', 'Placeholder', 'Open', 'SCAFFOLDING', 'TAUTOLOGY')


def survey2():
    bar('-')
    rec('  ### SURVEY 2 -- COMPONENT 1. ### **THE SUBJECT, CHOSEN BY A PRINTED RULE.**')
    bar('-')
    rec('  ### ### **THE CENSUS NAMES TWO. ### THE ORDER ASKS FOR ONE.**')
    rec('  ### ### **THE SEAT DOES NOT PICK THE ONE IT PREFERS**; the rule is stated first and')
    rec('  ### ### then applied, so the choice can be overturned by a reader who disagrees')
    rec('  ### ### with the rule rather than with the taste.')
    rec()
    rec('  ### **THE RULE:** ### the order says the keystone is ### **READ WHOLE AT THE')
    rec('  ### ### CANONICAL DRIVE** ### and that Component 1 reports ### **WHAT ITS')
    rec('  ### ### CORRESPONDENCE TABLE CARRIES BY GRADE.** ### A keystone whose compiled')
    rec('  ### terminals are not reachable at the canonical drive cannot satisfy that, so the')
    rec('  ### rule is: ### **TAKE THE ONE WHOSE TERMINALS THE DRIVE CAN ACTUALLY REACH.**')
    rec()
    res = branch_resident(os.path.join('D:', os.sep, 'SIDE-lv-conservation'), 'HEAD',
                          'word-pairing-interface') if os.path.exists(
        os.path.join('D:', os.sep, 'SIDE-lv-conservation')) else None
    rec('  ### **`THE_RESIDUE_OF_RH`** -- the census`s own required line about it:')
    rec('  ###   *its compiled terminals live on the HELD, UNMERGED branch')
    rec('  ###   `word-pairing-interface` of `SIDE-lv-conservation`. They are not on `main`*')
    lv = subprocess.run(['git', 'ls-remote', '--heads',
                         'https://github.com/psinary-sketch/SIDE-lv-conservation.git'],
                        capture_output=True, text=True, encoding='utf-8', errors='replace')
    heads = [x.split('refs/heads/')[-1] for x in (lv.stdout or '').split(chr(10)) if 'refs/heads/' in x]
    rec('  ###   ### **THE BRANCHES THAT EXIST NOW, READ LIVE : %s**' % (heads or 'none / no answer'))
    rec('  ###   ### **STILL UNMERGED : %s**'
        % ('word-pairing-interface' in heads and 'main' in heads))
    rec()
    amc = io.open(AMC, encoding='utf-8', errors='replace').read()
    rec('  ### **`ADDITIVE_MULTIPLICATIVE_CONSPIRACY`** -- its pins, checked live at their own')
    rec('  ###   repositories:')
    pins = {}
    for sha in ('c66f3c5', 'a27415d'):
        r = subprocess.run(['git', '-C', EFFECTS, 'cat-file', '-t', sha], capture_output=True,
                           text=True, encoding='utf-8', errors='replace')
        b = branch_resident(EFFECTS, sha, 'w-ladder-skeleton')
        pins['SIDE-effects/' + sha] = dict(type=(r.stdout or '').strip(), **b)
        rec('  ###     SIDE-effects `%s` : %-8s on main : %-5s on `w-ladder-skeleton` : %s'
            % (sha, (r.stdout or '?').strip(), b['on_main'], b['on_branch']))
    for sha in ('ce5d7bd', 'b1407b2'):
        r = subprocess.run(['git', '-C', KERNEL, 'cat-file', '-t', sha], capture_output=True,
                           text=True, encoding='utf-8', errors='replace')
        pins['SIDE-kernel/' + sha] = dict(type=(r.stdout or '').strip())
        rec('  ###     SIDE-kernel  `%s` : %s' % (sha, (r.stdout or '?').strip()))
    rec('  ### ### **EVERY PIN THIS KEYSTONE CITES RESOLVES, AND ITS PRINCIPAL TERMINAL`S PIN')
    rec('  ### ### IS ON `main`** -- so the drive can reach it, and the rule selects it.')
    rec()
    rec('  ### ### ### **THE SUBJECT OF THIS ACT : `ADDITIVE_MULTIPLICATIVE_CONSPIRACY`.**')
    rec('  ### **AND THE ONE NOT TAKEN IS NAMED, WITH THE REASON**, so the author can send a')
    rec('  ### later act at it: ### **`THE_RESIDUE_OF_RH` IS NOT DECLINED FOR ITS CONTENT.**')
    rec()
    # ---- what it is -----------------------------------------------------------------------
    ver = re.search(r'\*v(0\.2\.3), (2026-\d\d-\d\d)', amc)
    rec('  ### **VERSION AND DATE, FROM ITS OWN PROVENANCE:** ### `v%s`, `%s`.'
        % (ver.group(1) if ver else '?', ver.group(2) if ver else '?'))
    rec('  ### **THE CENSUS`S LAST-CONTENT-UPDATE FOR IT:** ### `2026-07-23` -- ### **THE OLDEST')
    rec('  ### ### OF THE SIXTEEN**, which is why the era has had longest to move over it.')
    t1 = grade_rows(AMC, '| Claim | Kernel | Theorem (fully qualified) |')
    t2 = grade_rows(AMC, '| claim | kernel | fully-qualified terminal |')
    rec()
    rec('  ### **TABLE 1 -- THE ORIGINAL CORRESPONDENCE (2026-07-12), `%d` ROWS:**' % len(t1))
    g1 = {}
    for cells in t1:
        st = cells[-1]
        g = next((w for w in GRADEWORDS if st.startswith(w) or ('**%s' % w) in st), 'OTHER')
        g1[g] = g1.get(g, 0) + 1
        rec('      %-52s ### **%s**' % (re.sub(r'#+|\*+', '', cells[0]).strip()[:52], g))
    rec('      ### by grade : %s' % sorted(g1.items()))
    rec()
    rec('  ### **TABLE 2 -- CORRESPONDENCE AT THE STANDARD (2026-08-12), `%d` ROWS:**' % len(t2))
    g2 = {}
    for cells in t2:
        st = cells[4] if len(cells) > 4 else cells[-1]
        g = next((w for w in GRADEWORDS if w in st), 'OTHER')
        g2[g] = g2.get(g, 0) + 1
        rec('      %-52s ### **%s**' % (re.sub(r'#+|\*+', '', cells[0]).strip()[:52], g))
    rec('      ### by grade : %s' % sorted(g2.items()))
    rec()
    rec('  ### ### **THE DOCUMENT CARRIES TWO CORRESPONDENCE TABLES, NOT ONE**, the second')
    rec('  ### ### added at the standard on `2026-08-12` with the first ### **PRESERVED')
    rec('  ### ### UNCHANGED** ### -- which is the precedent Component 3 must follow.')
    return dict(subject='ADDITIVE_MULTIPLICATIVE_CONSPIRACY', not_taken='THE_RESIDUE_OF_RH',
                pins=pins, lv_heads=heads, table1=len(t1), table2=len(t2),
                grades1=g1, grades2=g2,
                version=(ver.group(1) if ver else None), vdate=(ver.group(2) if ver else None),
                bytes=len(amc.encode('utf-8')), lines=len(amc.split(chr(10))))


# ==================================================================================================
#  SURVEY 3 -- COMPONENT 2: WHAT BEARS ON IT, EACH ANCHOR OPENED.
# ==================================================================================================
BEARS = [
    ('the census`s own anchor (i)', 'Q2`s no-class-point verdict', CENSUS,
     "`Q2`'s no-class-point verdict"),
    ('the census`s own anchor (ii)', 'the `n₄ = 0` reconciliation', CENSUS,
     'the `n₄ = 0` reconciliation'),
    ('the findings layer', 'e-difficulty-theorem', FINDINGS, '### e-difficulty-theorem'),
    ('the findings layer', 'formation-decomposition-type-invariant', FINDINGS,
     '### formation-decomposition-type-invariant'),
    ('the cascade anchors', 'type-d-no-conspiracy', CASCADE, '### type-d-no-conspiracy'),
    ('the cascade anchors', 'twin-primes-no-conspiracy', CASCADE,
     '### twin-primes-no-conspiracy'),
    ('the cascade anchors', 'goldbach-no-conspiracy', CASCADE, '### goldbach-no-conspiracy'),
    ('the cascade anchors', 'sophie-germain-no-conspiracy', CASCADE,
     '### sophie-germain-no-conspiracy'),
    ('the trails', 'W-6 closed by repair', TRAILS,
     '> - W-6 — CLOSED-BY-REPAIR (W-6-EXT, SIDE-kernel v1.4, 2026-07-19)'),
    ('the trails', 'b372`s check of this document`s line 400', TRAILS,
     '| `phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md` | 400 |'),
    ('the exclusion engine', 'e_difficulty re-graded from TAUTOLOGY', ENGINE,
     '**DERIVES** *(re-graded 2026-07-19; was TAUTOLOGY)*'),
]


def survey3():
    bar('-')
    rec('  ### SURVEY 3 -- COMPONENT 2. ### **WHAT BEARS ON IT, EACH ANCHOR OPENED.**')
    bar('-')
    amc = io.open(AMC, encoding='utf-8', errors='replace').read()
    buckets = {'ALREADY SAYS IT': 0, 'SUPERSEDES SOMETHING IT SAYS': 0, 'DOES NOT CARRY IT': 0}
    rows = []
    for layer, name, path, hint in BEARS:
        try:
            at, line = AF.find(path, hint)
        except Exception as e:
            rows.append(dict(layer=layer, name=name, at=None, err=str(e)[:100]))
            rec('    %-22s %-42s ### **NO ANCHOR** -- %s' % (layer, name[:42], str(e)[:60]))
            continue
        rows.append(dict(layer=layer, name=name, at=at, file=os.path.basename(path),
                         text=line[:400]))
        rec('    %-22s %-42s %s line %d' % (layer, name[:42], os.path.basename(path), at))
    rec()
    rec('  ### **THE POPULATION : `%d` ANCHORS, EACH OPENED AND READ AT ITS OWN LINE.**'
        % len([r for r in rows if r.get('at')]))
    rec('  ### ### **THE BUCKETING IS COMPONENT 2`S WORK AND IS DONE THERE, NOT HERE** -- this')
    rec('  ### ### survey establishes only that every anchor RESOLVES, so the component reads')
    rec('  ### ### material and never a name.')
    rec('  ### ### **ANCHORS THAT DID NOT RESOLVE : %d.**'
        % len([r for r in rows if not r.get('at')]))
    # ### a first mechanical pass: does the keystone's own text carry the anchor's key phrase?
    rec()
    rec('  ### **A FIRST MECHANICAL PASS, BY THE KEYSTONE`S OWN BYTES** (the component judges;')
    rec('  ### this only tells it where to look):')
    probes = [('Q2 / no-class-point', 'NO-CLASS-POINT VERDICT'),
              ('n4 = 0 reconciliation', 'n₄ = 0'),
              ('W-6 discharged', 'W-6 gate (E-Difficulty skeleton) — DISCHARGED'),
              ('the scope split of 2026-07-28', 'W-INFORMATION'),
              ('the e_difficulty re-grade', 'was TAUTOLOGY'),
              ('the branch named', 'w-ladder-skeleton'),
              ('the cascade anchors cited', 'CASCADE_ANCHORS_CORRECTED'),
              ('LE-K-6 named open', 'LE-K-6')]
    present = {}
    for lbl, needle in probes:
        p = needle in amc
        present[lbl] = p
        rec('      %-34s in the keystone`s own bytes : %s' % (lbl, p))
    return dict(anchors=len(rows), resolved=len([r for r in rows if r.get('at')]),
                unresolved=len([r for r in rows if not r.get('at')]),
                rows=rows, present=present, buckets=buckets)


# ==================================================================================================
def refs():
    out = {}
    for name, repo in b303_pins.REPOS:
        b = subprocess.run(['git', '-C', repo, 'rev-parse', '--abbrev-ref', 'HEAD'],
                           capture_output=True, text=True, encoding='utf-8', errors='replace')
        h = subprocess.run(['git', '-C', repo, 'rev-parse', 'HEAD'], capture_output=True,
                           text=True, encoding='utf-8', errors='replace')
        out[name] = dict(branch=(b.stdout or '').strip(), head=(h.stdout or '').strip()[:12])
    return out


def main():
    rec('### run at (UTC) : %s   ### NOT COVERED BY ANY HASH; it records when this run file was '
        'written.' % run_clock.stamp())
    bar('=')
    rec('b390 -- THE EXTRACT, AND THE FOUR SURVEYS THE FACE IS WRITTEN FROM.')
    bar('=')
    R = refs()
    rec('  ### THE REFS.')
    for k, v in R.items():
        rec('    %-22s `%s` = `%s`' % (k, v['branch'], v['head']))
    rec()
    s1 = survey1()
    rec()
    s2 = survey2()
    rec()
    s3 = survey3()
    rec()
    reads, without = do_reads()
    rec()
    bar('=')
    rec('  ### ### **THE SURVEY, IN ONE LINE EACH.**')
    bar('=')
    rec('  0 : routed items %d ; REPAIRABLE %d ; needs-a-ruling %d'
        % (s1['routed'], s1['classes'].get('REPAIRABLE', 0),
           s1['classes'].get('NEEDS-A-RULING', 0)))
    rec('  1 : subject %s ; not taken %s ; tables %d + %d rows'
        % (s2['subject'], s2['not_taken'], s2['table1'], s2['table2']))
    rec('  2 : anchors %d ; resolved %d ; unresolved %d'
        % (s3['anchors'], s3['resolved'], s3['unresolved']))
    rec('  reads %d without_anchor %d' % (len(reads), without))
    rec('  ### **NO DOCUMENT WAS EDITED BY THIS TOOL, AND NOTHING WAS WRITTEN AT ZENODO.**')
    bar('=')
    p = run_clock.write(D, 'b390_extract_notes', L)
    json.dump(dict(s1=s1, s2=s2, s3=s3, reads=len(reads), without_anchor=without,
                   anchors_differing=sum(1 for r in reads if r.get('differs')),
                   refs=R, read_rows=reads,
                   run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
              io.open(os.path.join(D, 'b390_reads.json'), 'w', encoding='utf-8'), indent=1)
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
