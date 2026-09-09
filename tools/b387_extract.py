# -*- coding: utf-8 -*-
"""b387_extract.py -- EXTRACT-TO-DISK, AND THE TABLE SURVEY THE FACE IS WRITTEN FROM.

### ### **THE SURVEY RUNS BEFORE THE LOCK BECAUSE THE FACE IS WRITTEN FROM A SURVEY, NEVER FROM A
### ### BELIEF ABOUT THE TERRAIN** -- the standing clause this act carries, minted from `b385` and
### `b386`.
###
### ### **AND THE SURVEY FOUND ITS OWN PREDICATE WRONG TWICE, WHICH IS WHY IT RUNS EARLY.** ### A
### first pass required the heading `## Correspondence` and located ### **7 OF 14.** ### A second
### asked for the FRONT DOOR's own columns -- claim, kernel, theorem, axiom profile, status -- and
### located `8`, missing `R_CURVE_CRITERION`, whose column is headed ### **`Grade`** ### and not
### `Status`. ### `Grade` is the union's own word (*fourteen GRADED Correspondence tables*), so the
### third pass accepts either. ### **A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE**, and this
### act met that species twice inside one component before the lock rather than after it.
###
### ### **THE TABLES ARE FOUND BY SHAPE AND NOT BY HEADING**, which is `(R2)`: by content, never by
### address. ### A document whose table sits under `# Kernel Correspondence`, or under an appendix,
### is found; a document with no such table is ### **REPORTED ABSENT WITH ITS NEAR-MISSES PRINTED**,
### because an absence needs a proved search (`b378`).
###
### ### **NOTHING IS RECONCILED HERE.** ### Where the union's list and the disk disagree, the
### disagreement is the finding.
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

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


FERRY = d('b387_ferry_2026-09-09.txt')
UNION = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
FRONT = os.path.join(PP, 'README.md')
TAX = os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
MONO = os.path.join(PP, 'day1', 'A_Place_to_Stand.md')

# ### ### **THE SET, AS THE UNION NAMES IT** -- tag and the document the union points at, read off
# ### the union's own keystone-set line and not chosen by this seat.
SET = [
    ('MONO', 'day1/A_Place_to_Stand.md', 'day1/A_Place_to_Stand §25.8'),
    ('SIMP', 'phase1.5/simplicity/SIMPLICITY_OF_RIEMANN_ZEROS.md', 'SIMPLICITY_OF_RIEMANN_ZEROS'),
    ('GRH', 'phase1.5/spectral/GRH_CASCADE.md', 'GRH_CASCADE'),
    ('FOUND', 'phase1.5/structural/FOUNDATIONS_OF_THE_SIDE_PROGRAMME.md',
     'FOUNDATIONS_OF_THE_SIDE_PROGRAMME'),
    ('SURR', 'phase1.5/proofs/THE_UNCONDITIONAL_SURROUND.md', 'THE_UNCONDITIONAL_SURROUND'),
    ('LIC', 'phase1.5/method/EXHAUSTIVENESS_LICENSE.md', 'EXHAUSTIVENESS_LICENSE'),
    ('RCURVE', 'phase1.5/rcurve/R_CURVE_CRITERION.md', 'R_CURVE_CRITERION'),
    ('PATHS', 'phase1.5/proofs/PATHS_TO_THE_CRITICAL_LINE.md', 'PATHS_TO_THE_CRITICAL_LINE'),
    ('ENGINE', 'phase1.5/method/EXCLUSION_ENGINE.md', 'EXCLUSION_ENGINE'),
    ('DOM', 'phase1.5/spectral/DOMAIN_OSTROWSKI_UNIVERSALITY_v0_1.md',
     'DOMAIN_OSTROWSKI_UNIVERSALITY'),
    ('IFACE', 'phase1.5/spectral/INTERFACE_CONSERVATION.md', 'INTERFACE_CONSERVATION'),
    ('SEVEN', 'phase1.5/spectral/SEVEN_DISCRIMINANTS_AND_TRIVIUM_v0_1.md', 'SEVEN_DISCRIMINANTS'),
    ('CNA', 'phase1.5/deep-structure/CLASS_NUMBER_ANOMALY.md', 'CLASS_NUMBER_ANOMALY'),
    ('BALPOS', 'phase1.5/spectral/BALANCE_AND_POSITIVITY.md', 'BALANCE_AND_POSITIVITY'),
]

READS = [
    ('the order -- the act', 'ORDER', FERRY,
     "ACT b387 — WHAT THE KEYSTONES' TABLES ACTUALLY CARRY. Number"),
    ('the order -- a read and a count, no ruling', 'ORDER', FERRY,
     'not claimed by any unclosed ferry. A READ and a COUNT; no'),
    ('the order -- the face from a survey, not a belief', 'ORDER', FERRY,
     'gate; the face is written from a survey, never from a belief'),
    ('the ruling (R16) -- the untracked hook copies stay', 'RULING', FERRY,
     'strikeable: THE UNTRACKED HOOK COPIES STAY. The repository'),
    ('the ruling (R16) -- the configuration already makes the source run', 'RULING', FERRY,
     'configuration already makes the tracked source the one that'),
    ('the ruling (R16) -- removing a working fallback buys nothing', 'RULING', FERRY,
     'runs, and the untracked copies are a fallback; removing a'),
    ('the ruling (R16) -- recorded so a later survey does not read divergence', 'RULING', FERRY,
     'with its reason so a later survey does not read them as'),
    ('the order -- component 1, the set from the record not a predicate', 'ORDER', FERRY,
     'COMPONENT 1 — THE SET, from the record and not from a'),
    ('the order -- component 1, report the disagreement and do not reconcile', 'ORDER', FERRY,
     'documents on disk disagree, report the disagreement and do not'),
    ('the order -- component 2, every row counted by what backs it', 'ORDER', FERRY,
     'COMPONENT 2 — EVERY ROW COUNTED BY WHAT BACKS IT: per document'),
    ('the order -- component 2, unreadable rather than assigned', 'ORDER', FERRY,
     'unreadable rather than assigned. Quote the front door\'s status'),
    ('the order -- component 3, answered from practice not ruled', 'ORDER', FERRY,
     'COMPONENT 3 — THE QUESTION ANSWERED FROM PRACTICE, not ruled:'),
    ('the order -- component 3, nothing recommended', 'ORDER', FERRY,
     'borderline dispositions quoted and NOTHING recommended.'),
    ('the order -- component 4, the seat`s own memory', 'ORDER', FERRY,
     "COMPONENT 4 — THE SEAT'S OWN MEMORY: the memory file was over"),
    ('the order -- component 4, against the prior blob not from recall', 'ORDER', FERRY,
     'through a pointer, if anything, checked against the file\'s own'),
    ('the order -- the lore gains the survey clause', 'ORDER', FERRY,
     'gains "the face is written from a survey, not from a belief'),
    ('the order -- (F1), a material fraction not machine-verified', 'ORDER', FERRY,
     'the keystones already carry a material fraction of rows that'),
    ('the order -- (F2), nothing was lost from the memory file', 'ORDER', FERRY,
     'are not machine-verified and are labelled as such; (F2) nothing'),

    # ---- THE UNION ---------------------------------------------------------------------------
    ('the union -- the keystone set heading', 'UNION', UNION,
     '## The keystone set (14 graded Correspondence tables)'),
    ('the union -- the fourteen named', 'UNION', UNION,
     'MONO (`day1/A_Place_to_Stand` §25.8) · SIMP (`SIMPLICITY_OF_RIEMANN_ZEROS`)'),
    ('the union -- the day-1 companions and the §25.8 carrier', 'UNION', UNION,
     'Day-1 companions name terminals in prose; the §25.8 concordance is their carrier.'),

    # ---- THE FRONT DOOR`S STATUS VOCABULARY ---------------------------------------------------
    ('the front door -- what a row maps', 'FRONTDOOR', FRONT,
     'Each row maps a claim the paper makes to the artifact that verifies it'),
    ('the front door -- the five columns', 'FRONTDOOR', FRONT,
     'kernel · fully-qualified theorem name · axiom profile · status'),
    ('the front door -- where no kernel exists the status says so in words', 'FRONTDOOR', FRONT,
     'exists, the status says so in words — *manuscript-resident* or *research-reach* —'),
    ('the front door -- rather than being omitted', 'FRONTDOOR', FRONT,
     'rather than being omitted. Every keystone carrying a Correspondence table closes'),
    ('the front door -- the audit surface', 'FRONTDOOR', FRONT,
     'A Correspondence table is the paper’s audit surface. A reader who wants to check a'),

    # ---- THE MONOGRAPH`S §25.8, WHICH THE UNION NAMES AS MONO`S CARRIER -----------------------
    ('the monograph -- the §25.8 concordance`s first row', 'MONO', MONO,
     '| Route 1 — structural exhaustiveness, unconditional in Lean | `structural_exhaustiveness_proved` |'),

    # ---- THE STANDARD`S BORDERLINE DISPOSITIONS, FOR COMPONENT 3 -------------------------------
    ('the standard -- Tier K may be cited as certification', 'STANDARD', TAX,
     '**Tier K — Keystone-certified.**'),
    ('the standard -- Tier C is never cited as certification', 'STANDARD', TAX,
     '**Tier C — Cluster-synthesis.**'),
    ('the standard -- the CATALOGOS borderline', 'STANDARD', TAX, '- **CATALOGOS**'),
    ('the standard -- the UNIVERSALITY borderline', 'STANDARD', TAX, '- **UNIVERSALITY.md**'),
    ('the standard -- the THE_SUBSTRATE borderline', 'STANDARD', TAX,
     '- **THE_SUBSTRATE** — **Tier K** (its Correspondence table is pinned terminals)'),
    ('the standard -- the borderlines are author-ruled', 'STANDARD', TAX,
     '**Borderlines — author-ruled 2026-07-28'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.strip()


SEP = re.compile(r'^\s*\|[\s:|-]+\|\s*$')


def cells(line):
    s = line.strip()
    if s.startswith('|'):
        s = s[1:]
    if s.endswith('|'):
        s = s[:-1]
    return [c.strip() for c in s.split('|')]


def shaped(hdr):
    """### THE FRONT DOOR`S OWN COLUMNS, LOOSELY ON WORDING AND STRICTLY ON SHAPE. ### A status
    ### column -- or a `grade` column, which is the UNION`s own word for the same thing -- plus at
    ### least one verification column."""
    low = [re.sub(r'[*`]', '', h).lower() for h in hdr]
    st = any(('status' in h) or ('grade' in h) for h in low)
    vf = any(('kernel' in h) or ('theorem' in h) or ('axiom' in h) or ('terminal' in h)
             for h in low)
    return st, vf, [re.sub(r'[*`]', '', h).lower() for h in hdr]


def tables_in(path):
    lines = io.open(path, encoding='utf-8', errors='replace').read().split('\n')
    out, near, i = [], [], 0
    while i < len(lines) - 1:
        if lines[i].strip().startswith('|') and SEP.match(lines[i + 1]):
            st, vf, cols = shaped(cells(lines[i]))
            j, n = i + 2, 0
            while j < len(lines) and lines[j].strip().startswith('|'):
                n += 1
                j += 1
            head = ''
            for k in range(i, max(-1, i - 80), -1):
                if lines[k].lstrip().startswith('#'):
                    head = lines[k].strip()
                    break
            rec_ = dict(line=i + 1, rows=n, heading=head[:90], cols=cols)
            (out if (st and vf) else near).append(rec_)
            i = j
            continue
        i += 1
    return out, near, lines


def main():
    rec('=' * 100)
    rec("b387_extract.py -- EXTRACT-TO-DISK, AND THE TABLE SURVEY.")
    rec('=' * 100)
    rec('')
    rec('-' * 100)
    rec('  ### THE REFS.')
    rec('-' * 100)
    refs = {}
    for name, repo in b303_pins.REPOS:
        refs[name] = dict(branch=git(repo, 'rev-parse', '--abbrev-ref', 'HEAD'),
                          head=git(repo, 'rev-parse', 'HEAD')[:12],
                          dirty=bool(git(repo, 'status', '--porcelain')))
        rec('    %-22s ref `%s` = `%s`   ### tree dirty : %s'
            % (name, refs[name]['branch'], refs[name]['head'], refs[name]['dirty']))

    rec('')
    rec('-' * 100)
    rec('  ### THE SURVEY. ### **THE UNION NAMES FOURTEEN; THE DISK IS ASKED WHAT IT HAS.**')
    rec('-' * 100)
    rec('  ### Tables are located ### **BY SHAPE, NOT BY HEADING** ### -- `(R2)`, by content and')
    rec('  ### never by address. ### A `status` OR a `grade` column, plus a verification column.')
    survey, total = [], 0
    for tag, rel, named in SET:
        p = os.path.join(PP, rel.replace('/', os.sep))
        exists = os.path.exists(p)
        hits, near, _ = tables_in(p) if exists else ([], [], [])
        rows = sum(h['rows'] for h in hits)
        total += rows
        survey.append(dict(tag=tag, rel=rel, union_names=named, exists=exists,
                           tables=hits, near=near, rows=rows))
        rec('')
        rec('  [%-6s] union names `%s`' % (tag, named))
        rec('           on disk : `%s` ### exists : %s' % (rel, exists))
        if not hits:
            rec('           ### ### **NO CORRESPONDENCE-SHAPED TABLE.** ### tables of any shape in'
                ' the file : %d' % len(near))
            for nb in near[:3]:
                rec('               near-miss line %-6d rows=%-3d cols: %s'
                    % (nb['line'], nb['rows'], ' | '.join(nb['cols'])[:88]))
        for h in hits:
            rec('           line %-6d rows=%-3d under %s' % (h['line'], h['rows'], h['heading']))
            rec('               cols: %s' % ' | '.join(h['cols'])[:96])
    withtab = [s for s in survey if s['tables']]
    without = [s for s in survey if not s['tables']]
    rec('')
    rec('  ### ### **THE UNION NAMES `%d`. ### DOCUMENTS CARRYING A CORRESPONDENCE-SHAPED TABLE : '
        '`%d`. ### CARRYING NONE : `%d`.**' % (len(SET), len(withtab), len(without)))
    rec('  ### ### **ROWS IN ALL LOCATED TABLES : `%d`.**' % total)
    rec('  ### ### **CARRYING NONE, BY NAME : %s**'
        % ', '.join('`%s`' % s['tag'] for s in without))

    # ### **THE MONOGRAPH`S CARRIER IS CHECKED AGAINST WHAT THE UNION SAYS IT IS.**
    rec('')
    rec('  ### ### **AND THE UNION POINTS `MONO` AT `§25.8`, SO `§25.8` IS READ.**')
    mono_lines = io.open(MONO, encoding='utf-8', errors='replace').read().split('\n')
    h258 = next((i for i, ln in enumerate(mono_lines) if ln.strip() == '## 25.8 Kernel Concordance'),
                None)
    t258 = None
    if h258 is not None:
        for i in range(h258, min(h258 + 60, len(mono_lines) - 1)):
            if mono_lines[i].strip().startswith('|') and SEP.match(mono_lines[i + 1]):
                st, vf, cols = shaped(cells(mono_lines[i]))
                j, n = i + 2, 0
                while j < len(mono_lines) and mono_lines[j].strip().startswith('|'):
                    n += 1
                    j += 1
                t258 = dict(line=i + 1, rows=n, cols=cols, graded=st, verification=vf)
                break
    rec('  ###   `## 25.8 Kernel Concordance` at line %s' % (h258 + 1 if h258 else '### ABSENT'))
    if t258:
        rec('  ###   its table : line %d, %d rows, cols: %s'
            % (t258['line'], t258['rows'], ' | '.join(t258['cols'])))
        rec('  ###   ### ### **IT CARRIES A STATUS OR GRADE COLUMN : %s.**' % t258['graded'])
    rec('')
    rec('-' * 100)
    rec('  ### THE READS. ### **HINT TYPED -> ANCHOR READ FROM THE FILE -> NEEDLE PULLED.**')
    rec('-' * 100)
    out, noanchor, differing, bytag = [], 0, 0, {}
    for lbl, tag, path, hint in READS:
        rec('')
        rec('  [%-9s] %s' % (tag, lbl))
        try:
            n, line = AF.find(path, hint)
        except Exception as e:  # noqa: BLE001
            noanchor += 1
            rec('      ### ### **NO ANCHOR** -- %s' % str(e)[:150])
            out.append(dict(label=lbl, tag=tag, file=os.path.basename(path), path=path,
                            line=None, text=None, error=str(e)[:200]))
            continue
        diff = (line.rstrip(chr(10)) != hint)
        differing += 1 if diff else 0
        bytag[tag] = bytag.get(tag, 0) + 1
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.basename(path), n, diff))
        rec('      | %s' % line.strip()[:230])
        out.append(dict(label=lbl, tag=tag, file=os.path.basename(path), path=path,
                        line=n, text=line.rstrip(chr(10))))
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), noanchor))
    rec('  ### ### **BY TAG : %s**' % bytag)
    rec('  ### **NO DOCUMENT WAS EDITED BY THIS TOOL AND NO ROW WAS TOUCHED.**')
    rec('=' * 100)
    pth = run_clock.write(D, 'b387_extract_notes', LINES)
    io.open(d('b387_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(reads=len(READS), without_anchor=noanchor, anchors_differing=differing,
                        by_tag=bytag, refs=refs, built=out, survey=survey,
                        union_names=len(SET), with_table=len(withtab),
                        without_table=len(without),
                        without_table_tags=[s['tag'] for s in without],
                        rows_total=total, mono_258=t258,
                        run_file=os.path.basename(pth),
                        run_clock=run_clock.read_stamp(pth)), indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(pth))
    return 0 if noanchor == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
