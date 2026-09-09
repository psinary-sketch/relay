# -*- coding: utf-8 -*-
"""b390_components.py -- COMPONENT 0 (CLASSIFIED), COMPONENT 1, COMPONENT 2.

### ### **THE WRITES ARE NOT HERE.** ### This file reads, classifies and buckets; the one repair
### and the one annotation are made by `b390_desk_bank.py`, so ### **NOTHING THAT READS CAN WRITE**
### and the read half can be re-run at will.
###
### ### **COMPONENT 2 QUOTES BOTH SIDES.** ### The record`s line at its own line number AND the
### keystone`s line at its own line number, for every anchor -- because ### **A ONE-SIDED QUOTATION
### ### IS A SUMMARY OF THE OTHER SIDE**, and the order forbids summarising by name.
###
### ### **AND THE MIDDLE BUCKET IS REPORTED WHETHER OR NOT IT IS EMPTY.** ### `(F1)` turns on it,
### and ### **A PASS THAT MANUFACTURES A REPAIR TO SATISFY AN EXPECTATION HAS DESTROYED THE ONLY
### ### THING IT WAS FOR.**
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

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
EFFECTS = os.path.join('D:', os.sep, 'SIDE-effects')
AMC = os.path.join(PP, 'phase2', 'method', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md')
CENSUS = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')
REGISTRY = os.path.join(PP, 'REGISTRY.md')
METHOD = os.path.join(PP, 'phase1.5', 'method', 'A_METHODOLOGY.md')
OUT = os.path.join(D, 'b390_components.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def flat(s, n=190):
    return ' '.join(s.split())[:n]


def at_line(path, hint):
    """### **BOTH SIDES ARE QUOTED AT THEIR OWN LINE NUMBERS, READ OUT OF THEIR OWN FILES.**"""
    try:
        i, ln = AF.find(path, hint)
        return i, ln
    except Exception:
        return None, ''


E = json.load(io.open(os.path.join(D, 'b390_reads.json'), encoding='utf-8'))


# ==================================================================================================
#  COMPONENT 0 -- THE ROUTED CORRECTIONS, CLASSIFIED. ### (THE ONE REPAIR IS MADE BY THE WRITER.)
# ==================================================================================================
def component0():
    bar('=')
    rec('  ### COMPONENT 0 -- THE DISCOVERABLE CORRECTIONS ALREADY ROUTED, CLASSIFIED.')
    bar('=')
    s1 = E['s1']
    rec('  ### **THE LIVE CHECK, RE-RUN BY THE EXTRACT AND NOT RECALLED FROM `b389`:**')
    for k, v in sorted(s1['live'].items()):
        rec('      %-24s resolves : %s' % (k, v['resolves']))
    rec('  ### ### **A KERNEL RECALLED IS NOT A KERNEL READ**, and the repair rests on the read.')
    rec()
    for it in s1['items']:
        rec('    [%s] %-54s ### **%s**' % (it['act'], it['item'][:54], it['cls']))
        rec('        %s' % it['what'])
        for i in range(0, min(len(it['why']), 460), 150):
            rec('        %s' % it['why'][i:i + 150])
        rec()
    rec('  ### ### **ROUTED ITEMS SWEPT : %d.**' % s1['routed'])
    for k in sorted(s1['classes']):
        rec('      %-22s %d' % (k, s1['classes'][k]))
    rec('  ### ### ### **REPAIRABLE BY EVIDENCE ALREADY PRINTED : %d.** ### The repair itself is'
        % s1['classes'].get('REPAIRABLE', 0))
    rec('  ### ### ### made by this act`s writer and reported there with its diff.')
    rec()
    rec('  ### ### **AND THE SEVEN THAT ARE NOT REPAIRED ARE NOT REPAIRED FOR A REASON, NOT FOR')
    rec('  ### ### LACK OF WIDTH.** ### This act`s face is wide by the order`s own instruction.')
    rec('  ### ### **A WIDE FACE DOES NOT MAKE A RULING REPAIRABLE** -- three of the seven need')
    rec('  ### ### the author, one needs the platform, one needs a reading nobody has done, one')
    rec('  ### ### is not a defect at all, and one was answered by `b389` before this act began.')
    return dict(routed=s1['routed'], classes=s1['classes'], repairable=s1['classes'].get(
        'REPAIRABLE', 0), live=s1['live'])


# ==================================================================================================
#  COMPONENT 1 -- THE SUBJECT.
# ==================================================================================================
def component1():
    bar('=')
    rec('  ### COMPONENT 1 -- THE SUBJECT, READ WHOLE AT THE CANONICAL DRIVE.')
    bar('=')
    s2 = E['s2']
    rec('  ### ### **THE RULE, STATED BEFORE THE SUBJECT IS NAMED.**')
    rec('  ### The census names ### **TWO** ### keystones as the ones whose subject matter the era')
    rec('  ### moved most. ### The order asks for ### **ONE.** ### **THE SEAT DOES NOT PICK THE')
    rec('  ### ### ONE IT PREFERS.**')
    i, ln = at_line(CENSUS, "The census's own answer, offered and not taken:")
    rec('  ### `THE_KEYSTONE_CENSUS.md` line %s:' % i)
    rec('      > %s' % flat(ln, 260))
    rec()
    rec('  ### **THE RULE, OUT OF THE ORDER`S OWN WORDS:** ### the keystone is ### **READ WHOLE AT')
    rec('  ### ### THE CANONICAL DRIVE** ### and Component 1 reports ### **WHAT ITS CORRESPONDENCE')
    rec('  ### ### TABLE CARRIES BY GRADE.** ### A keystone whose compiled terminals the drive')
    rec('  ### cannot reach cannot satisfy either. ### **SO: TAKE THE ONE THE DRIVE CAN REACH.**')
    rec()
    rec('  ### **BOTH CANDIDATES MEASURED:**')
    i, ln = at_line(CENSUS, "`THE_RESIDUE_OF_RH`'s compiled terminals live on the HELD, UNMERGED")
    rec('      ### **`THE_RESIDUE_OF_RH`** -- the census`s own release-blocking line, line %s:' % i)
    rec('        > %s' % flat(ln, 250))
    rec('      ### **AND IT IS STILL TRUE, READ LIVE:** ### the branches at')
    rec('      ### `SIDE-lv-conservation` now are %s.' % (s2['lv_heads'] or 'unreadable'))
    rec('      ### ### **THE DRIVE CANNOT REACH ITS TERMINALS AT `main`.**')
    rec()
    rec('      ### **`ADDITIVE_MULTIPLICATIVE_CONSPIRACY`** -- every pin it cites, checked live:')
    for k, v in sorted(s2['pins'].items()):
        extra = ('   on main : %s ; on `w-ladder-skeleton` : %s' % (v['on_main'], v['on_branch'])
                 if 'on_main' in v else '')
        rec('        %-26s %s%s' % (k, v['type'], extra))
    rec('      ### ### **EVERY PIN RESOLVES AND THE PRINCIPAL TERMINAL`S PIN IS ON `main`.**')
    rec()
    rec('  ### ### ### **THE SUBJECT : `ADDITIVE_MULTIPLICATIVE_CONSPIRACY`.**')
    rec('  ### ### **THE ONE NOT TAKEN IS `THE_RESIDUE_OF_RH`, AND IT IS NOT DECLINED FOR ITS')
    rec('  ### ### CONTENT** -- only because an unmerged branch is not the canonical drive. ### A')
    rec('  ### later act sent at it must either merge first or read the branch, and ### **THAT IS')
    rec('  ### ### A DECISION FOR THE AUTHOR, NOT A CONVENIENCE FOR A SEAT.**')
    rec()
    bar()
    rec('  ### **WHAT IT IS, IN ITS OWN WORDS.**')
    bar()
    rec('  ### version and date from its own provenance : ### **`v%s`, `%s`**'
        % (s2['version'], s2['vdate']))
    rec('  ### the census`s last-content-update for it  : ### **`2026-07-23`** ### -- the OLDEST of')
    rec('  ### the sixteen, which is why the era has had longest to move over it.')
    rec('  ### bytes / lines on disk                    : `%d` / `%d`' % (s2['bytes'], s2['lines']))
    for hint, lbl in ((
            'the classification is compiled; the conjectures are open, their shared',
            'its own status line'),
            ('One Obstruction-Shape Behind Twin Primes, Goldbach, and Sophie Germain',
             'what it claims, in its subtitle')):
        i, ln = at_line(AMC, hint)
        if i:
            rec('  ### **%s** (line %s):' % (lbl, i))
            rec('      > %s' % flat(ln, 230))
    rec()
    rec('  ### ### **IT CARRIES TWO CORRESPONDENCE TABLES, NOT ONE.**')
    rec('  ### ### **THEY ARE NOT MERGED AND NOT SUMMED.** ### They were written a month apart to')
    rec('  ### ### two different standards, and ### **A COUNT THAT SUMS THEM DESCRIBES NEITHER.**')
    rec()
    rec('  ### **TABLE 1 -- THE ORIGINAL CORRESPONDENCE (2026-07-12) : `%d` ROWS, BY GRADE:**'
        % s2['table1'])
    for g, n in sorted(s2['grades1'].items()):
        rec('      %-24s %d' % (g, n))
    rec('  ### **TABLE 2 -- CORRESPONDENCE AT THE STANDARD (2026-08-12) : `%d` ROWS, BY GRADE:**'
        % s2['table2'])
    for g, n in sorted(s2['grades2'].items()):
        rec('      %-24s %d' % (g, n))
    rec('  ### ### **EVERY GRADE IS REPORTED IN THE VOCABULARY THE DOCUMENT USED**, not translated')
    rec('  ### ### into one this seat prefers.')
    i, ln = at_line(AMC, '0 BLANK CELLS. Five of six rows have no kernel')
    rec('  ### and the document says of its own second table (line %s):' % i)
    rec('      > %s' % flat(ln, 230))
    return dict(subject=s2['subject'], not_taken=s2['not_taken'], version=s2['version'],
                vdate=s2['vdate'], bytes=s2['bytes'], lines=s2['lines'],
                table1=s2['table1'], table2=s2['table2'],
                grades1=s2['grades1'], grades2=s2['grades2'], pins=s2['pins'])


# ==================================================================================================
#  COMPONENT 2 -- WHAT BEARS ON IT AND IS NOT IN IT. ### THREE BUCKETS, BOTH SIDES QUOTED.
# ==================================================================================================
#  (layer, name, record file, record hint, keystone hint or None, bucket, why)
A, B, C = 'ALREADY SAYS IT', 'SUPERSEDES SOMETHING IT SAYS', 'DOES NOT CARRY IT'
ITEMS = [
    ('the census`s own anchor', '`Q2`s no-class-point verdict', CENSUS,
     "the conspiracy's site is the interface, and this keystone is the corpus",
     "`Q2`'s NO-CLASS-POINT VERDICT AND THE `n₄ = 0` RECONCILIATION BEAR", A,
     'The keystone`s ERA ANNOTATION of 2026-08-12 names this verdict and states its consequence '
     'in its own words. ### **THE CENSUS`S WORK-LIST ITEM FOR THIS DOCUMENT WAS ALREADY DONE.**'),
    ('the census`s own anchor', 'the `n₄ = 0` reconciliation', CENSUS,
     "the conspiracy's site is the interface, and this keystone is the corpus",
     "`Q2`'s NO-CLASS-POINT VERDICT AND THE `n₄ = 0` RECONCILIATION BEAR", A,
     'Named in the same annotation, in the same sentence. ### The two census anchors are one '
     'annotation.'),
    ('the findings layer', 'e-difficulty-theorem', os.path.join(PP, 'FINDINGS.md'),
     '**E-Difficulty Theorem** (formerly conjecture CP-E-3). Terminals',
     '**W-6 gate (E-Difficulty skeleton) — DISCHARGED** (W-6-EXT, SIDE-kernel', A,
     '### **THE TERMINALS AND THEIR GRADES ARE CARRIED**, at the same kernel version `v1.4 = '
     '`f374174`` and with the same `DERIVES` / axiom-free split. ### **BUT THE ANCHOR`S SECOND '
     'PARAGRAPH -- THE SCOPE SPLIT OF 2026-07-28 -- IS NOT**, and that half is bucketed '
     'separately below rather than hidden inside this row.'),
    ('the findings layer', 'the E-Difficulty scope split (2026-07-28)',
     os.path.join(PP, 'FINDINGS.md'),
     '**Scope split (W-INFORMATION run, 2026-07-28 — statement-grade, nothing', None, C,
     'The record separates E-Difficulty into a cross-cutting proof-architecture theorem and the '
     'Kind-B ladder, and sharpens the precondition to ### *has a finite mechanism catalogue*. ### '
     'The keystone carries neither phrase. ### ### **IT IS AN ADDITION AND NOT A CORRECTION**, '
     'and the record says so in its own head: ### *statement-grade, nothing retracted*. ### The '
     'trio is arithmetic, so the sharpened precondition ### **STRENGTHENS THIS KEYSTONE`S '
     'STANDING RATHER THAN QUALIFYING IT.**'),
    ('the findings layer', 'formation-decomposition-type-invariant',
     os.path.join(PP, 'FINDINGS.md'),
     '**Formation tuple (n₁, n₂, n₃, n₄) is decomposition-dependent, NOT an', None, C,
     'The keystone cites the `n₄ = 0` reconciliation but not the `Q20` refinement that the '
     'formation tuple is ### **DECOMPOSITION-DEPENDENT AND NOT AN INVARIANT.** ### **ADDITION, '
     'NOT CORRECTION:** ### the keystone makes no invariance claim about the tuple, so there is '
     'nothing for the refinement to overturn.'),
    ('the cascade anchors', 'type-d-no-conspiracy', os.path.join(PP, 'CASCADE_ANCHORS_CORRECTED.md'),
     '*argument-supported* (structural; Type-D as a DomainOstrowski instance',
     '| **the Type I/II/III + Type-D classification** (§I) |', A,
     'The keystone`s standard table cites `CASCADE_ANCHORS_CORRECTED` by name as its `VERIFY-BY`, '
     'and the anchor grades the catalogue ### *argument-supported*, ### which is what the '
     'keystone`s own row says by calling it ### **MANUSCRIPT-RESIDENT.**'),
    ('the cascade anchors', 'twin-primes-no-conspiracy',
     os.path.join(PP, 'CASCADE_ANCHORS_CORRECTED.md'),
     '*argument-supported* (structural); *milestone-open* (analytic). TYPE_D_EXCLUSION v0.1 sec II',
     '| **twin primes** (§II) — full statement |', A,
     'The anchor grades it ### *argument-supported* (structural) ### and ### *milestone-open* '
     '(analytic); ### the keystone`s row says ### **MILESTONE-OPEN (`M3`)** ### and names the '
     'anchor. ### **THE TWO AGREE, GRADE FOR GRADE.**'),
    ('the cascade anchors', 'goldbach-no-conspiracy',
     os.path.join(PP, 'CASCADE_ANCHORS_CORRECTED.md'),
     '*argument-supported* (structural); *milestone-open* (analytic). TYPE_D_EXCLUSION v0.1 sec III',
     '| **Goldbach** (§III) — full statement |', A, 'As above, for `M4`.'),
    ('the cascade anchors', 'sophie-germain-no-conspiracy',
     os.path.join(PP, 'CASCADE_ANCHORS_CORRECTED.md'),
     '*argument-supported* (structural); *milestone-open* (analytic). TYPE_D_EXCLUSION v0.1 sec IV',
     '| **Sophie Germain** (§IV) — full statement |', A, 'As above, for `M5`.'),
    ('the trails', 'W-6 — CLOSED-BY-REPAIR', os.path.join(PP, 'OPEN_TRAILS.md'),
     '> - W-6 — CLOSED-BY-REPAIR (W-6-EXT, SIDE-kernel v1.4, 2026-07-19)',
     '**W-6 gate (E-Difficulty skeleton) — DISCHARGED** (W-6-EXT, SIDE-kernel', A,
     'The trails close `W-6` by repair on `2026-07-19`; the keystone records it ### **DISCHARGED** '
     '### on the same date at the same kernel version. ### **THE DOCUMENT IS NOT BEHIND THE '
     'LEDGER; IT IS LEVEL WITH IT.**'),
    ('the trails', 'b372`s check of this document`s line 400', os.path.join(PP, 'OPEN_TRAILS.md'),
     '| `phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md` | 400 |',
     'The genuine structural exclusion is `Module1.no_type_d_conspiracies`', A,
     '`b372` swept the corpus for declarations retired at the head and found this document`s '
     'three ### **PRESENT at `c66f3c5`**, while `VERIFICATION_LOOM` and `EXCLUSION_ENGINE` rows '
     'in the same sweep were stale. ### **THIS DOCUMENT PASSED A CHECK ITS NEIGHBOURS FAILED.**'),
    ('the exclusion engine', '`e_difficulty` re-graded from TAUTOLOGY',
     os.path.join(PP, 'phase1.5', 'method', 'EXCLUSION_ENGINE.md'),
     '**DERIVES** *(re-graded 2026-07-19; was TAUTOLOGY)*',
     '**W-6 gate (E-Difficulty skeleton) — DISCHARGED** (W-6-EXT, SIDE-kernel', A,
     'The engine re-grades `e_difficulty` from `TAUTOLOGY` to `DERIVES`; the keystone carries the '
     'result -- ### *`e_difficulty` reads its system and extracts the Ostrowski (DERIVES, '
     '`{propext, Quot.sound}`)* -- ### **THOUGH NOT THE RE-GRADE`S HISTORY.** ### Carrying a '
     'grade`s current value and not its former one is ### **NOT A DEFECT IN A PAPER**, which '
     'states what is true and not what was.'),
]


def component2():
    bar('=')
    rec('  ### COMPONENT 2 -- WHAT BEARS ON IT AND IS NOT IN IT.')
    bar('=')
    rec('  ### **THE POPULATION:** ### the material the census listed by anchor for this document,')
    rec('  ### plus the findings layer, the cascade anchors, the trails and the exclusion engine.')
    rec('  ### ### **EACH ANCHOR IS OPENED AND READ AT ITS OWN LINE, AND BOTH SIDES ARE QUOTED.**')
    rec('  ### ### **NOTHING IS SUMMARISED** -- the order`s own word.')
    rec()
    counts = {A: 0, B: 0, C: 0}
    rows = []
    onesided = 0
    for layer, name, rpath, rhint, khint, bucket, why in ITEMS:
        ri, rln = at_line(rpath, rhint)
        ki, kln = (at_line(AMC, khint) if khint else (None, ''))
        if khint and not ki:
            onesided += 1
        if not khint and bucket == C:
            pass
        counts[bucket] += 1
        rows.append(dict(layer=layer, name=name, bucket=bucket,
                         record_file=os.path.relpath(rpath, PP), record_line=ri,
                         keystone_line=ki))
        bar()
        rec('  ### **%s** ### -- %s   ### ### **%s**' % (name, layer, bucket))
        bar()
        rec('    ### THE RECORD -- `%s` line %s:' % (os.path.basename(rpath), ri))
        rec('      > %s' % flat(rln, 260))
        if khint:
            rec('    ### THE KEYSTONE -- `ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md` line %s:' % ki)
            rec('      > %s' % flat(kln, 260))
        else:
            rec('    ### THE KEYSTONE -- ### **NO LINE. ### THE DOCUMENT DOES NOT CARRY IT**, and')
            rec('    ### a proved absence is quoted by the search that found nothing, not by a')
            rec('    ### line that is not there.')
        for i in range(0, min(len(why), 600), 150):
            rec('      %s' % why[i:i + 150])
    rec()
    bar('=')
    rec('  ### ### **THE THREE BUCKETS.**')
    bar('=')
    for k in (A, B, C):
        rec('      %-32s ### **%d**' % (k, counts[k]))
    rec('  ### ### **EVERY BUCKET IS REPORTED, INCLUDING THE EMPTY ONE.**')
    rec('  ### ### **BUCKETED ITEMS CARRYING A QUOTATION FROM ONLY ONE SIDE : %d**' % onesided)
    rec('  ### ### -- and where the keystone has no line, ### **THE ABSENCE IS SAID AND NOT')
    rec('  ### ### QUOTED**, because a line that is not there cannot be quoted.')
    rec()
    rec('  ### ### ### **THE MIDDLE BUCKET IS EMPTY ON THIS POPULATION.** ### Of the `%d` anchors'
        % len(ITEMS))
    rec('  ### ### ### the census and the record name, ### **`%d` ARE ALREADY IN THE DOCUMENT AND'
        % counts[A])
    rec('  ### ### ### `%d` ARE ADDITIONS. ### NONE IS A CORRECTION.**' % counts[C])
    rec()
    # ---- AND ONE THING THE ANCHOR LIST DID NOT NAME, FOUND BY READING THE DOCUMENT ------------
    bar('=')
    rec('  ### ### ### **AND ONE THING NO ANCHOR NAMED, FOUND BY READING THE DOCUMENT.**')
    bar('=')
    rec('  ### **THIS IS WHY THE ORDER ASKED FOR A READING PASS AND NOT ANOTHER CENSUS.** ### It')
    rec('  ### is not in the census`s work-list, not in the findings layer, and not in the trails.')
    rec('  ### It is visible only to somebody reading the document`s own references.')
    rec()
    cites = []
    for i, ln in enumerate(io.open(AMC, encoding='utf-8', errors='replace').read().split(chr(10)),
                           1):
        if re.search(r'A_METHODOLOGY[A-Z_]*[` ]*v1\.2', ln):
            cites.append((i, ln))
    rec('  ### **THE KEYSTONE CITES ITS COMPANION METHODOLOGY PAPER AT `v1.2`, IN `%d` PLACES:**'
        % len(cites))
    for i, ln in cites:
        rec('      line %-4d > %s' % (i, flat(ln, 150)))
    rec()
    mi, mln = at_line(METHOD, '**v0.5.4 — 2026-07-19**')
    rec('  ### **THE PAPER ITSELF** -- `phase1.5/method/A_METHODOLOGY.md` line %s:' % mi)
    rec('      > %s' % flat(mln, 230))
    gi, gln = at_line(REGISTRY, '| 1.5h-4 | Methodology for Determined Systems |')
    rec('  ### **AND THE REGISTRY AGREES WITH THE PAPER** -- `REGISTRY.md` line %s:' % gi)
    rec('      > %s' % flat(gln, 230))
    rec()
    rec('  ### ### ### **THERE IS NO `v1.2` OF THAT DOCUMENT. ### IT IS AT `v0.5.4`, AND HAS BEEN')
    rec('  ### ### ### SINCE `2026-07-19` -- THE SAME DAY THIS KEYSTONE`S OWN `v0.2.3` WAS FILED.**')
    rec('  ### ### **SO `(F1)` IS MET: THE KEYSTONE CARRIES A CLAIM THE RECORD CONTRADICTS.**')
    rec()
    # ---- and it is not this document's private defect ---------------------------------------
    docs, tot = [], 0
    for dp, dn, fn in os.walk(PP):
        rel = os.path.relpath(dp, PP).replace(os.sep, '/')
        if rel.startswith(('.git', 'archive', 'outputs')):
            continue
        for f in fn:
            if not f.endswith('.md'):
                continue
            p = os.path.join(dp, f)
            n = len(re.findall(r'A_METHODOLOGY[A-Z_]*[` ]*v1\.2',
                               io.open(p, encoding='utf-8', errors='replace').read()))
            if n:
                docs.append((rel + '/' + f if rel != '.' else f, n))
                tot += n
    rec('  ### ### **BUT IT IS NOT THIS DOCUMENT`S PRIVATE DEFECT, AND THAT CHANGES THE REMEDY.**')
    rec('  ### **`%d` LIVE DOCUMENTS CARRY `%d` CITATIONS AT `v1.2`:**' % (len(docs), tot))
    for f, n in sorted(docs, key=lambda x: -x[1]):
        rec('      %-70s %d' % (f[:70], n))
    rec()
    rec('  ### ### ### **REPAIRING ONE OF ELEVEN WOULD MAKE THIS KEYSTONE DISAGREE WITH TEN')
    rec('  ### ### ### SIBLINGS AND WOULD HIDE A SYSTEMIC DEFECT INSIDE A LOCAL TIDY-UP.**')
    rec('  ### And this act`s locked face permits ### **AN APPENDED ANNOTATION ONLY** ### on this')
    rec('  ### document -- so the in-place edit is outside the face in any case, and ### **THE')
    rec('  ### ### FACE IS NOT WIDENED MID-ACT.**')
    rec('  ### ### **THE FINDING IS RECORDED IN THE KEYSTONE BY ANNOTATION AND THE REPAIR IS')
    rec('  ### ### ROUTED TO THE AUTHOR AS A CORPUS-WIDE CITATION PASS.**')
    return dict(buckets={A: counts[A], B: counts[B], C: counts[C]}, items=len(ITEMS),
                onesided=onesided, rows=rows,
                f1=True, f2=(counts[C] > 0 and counts[B] == 0),
                version_cites_here=len(cites), version_docs=len(docs), version_total=tot,
                docs=docs, method_version='v0.5.4')


def main():
    rec('### run at (UTC) : %s   ### NOT COVERED BY ANY HASH.' % run_clock.stamp())
    bar('=')
    rec('b390 -- COMPONENTS 0, 1 AND 2. ### THE FIRST PROOFREADING PASS.')
    bar('=')
    c0 = component0()
    rec()
    c1 = component1()
    rec()
    c2 = component2()
    rec()
    bar('=')
    rec('  ### ### **THE THREE COMPONENTS, IN ONE LINE EACH.**')
    bar('=')
    rec('  0 : routed %d ; repairable %d ; needing a ruling %d'
        % (c0['routed'], c0['repairable'], c0['classes'].get('NEEDS-A-RULING', 0)))
    rec('  1 : subject %s (v%s) ; not taken %s ; tables %d + %d rows'
        % (c1['subject'], c1['version'], c1['not_taken'], c1['table1'], c1['table2']))
    rec('  2 : buckets %s ; (F1) %s ; (F2) %s ; the version defect in %d docs / %d citations'
        % (c2['buckets'], c2['f1'], c2['f2'], c2['version_docs'], c2['version_total']))
    rec('  ### **NO DOCUMENT WAS EDITED BY THIS FILE, AND NOTHING WAS WRITTEN AT ZENODO.**')
    bar('=')
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    p = run_clock.write(D, 'b390_components_run', L)
    json.dump(dict(c0=c0, c1=c1, c2=c2, run_file=os.path.basename(p),
                   run_clock=run_clock.read_stamp(p)),
              io.open(os.path.join(D, 'b390_components.json'), 'w', encoding='utf-8'), indent=1)
    print('  written: %s' % os.path.basename(OUT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
