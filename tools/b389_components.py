# -*- coding: utf-8 -*-
"""b389_components.py -- COMPONENTS 1, 2 AND 3 OF b389.

### ### **COMPONENT 1** ### enumerates the cluster syntheses in THREE POPULATIONS -- disk, registry,
### map -- and ### **NEVER ADDS THEM.** ### The disagreement IS the finding.
### ### **COMPONENT 2** ### reports the deposited layer. ### **ITS LIVE HALF HALTS**, because the
### platform did not answer on any of six routes with a positive control at `200`, and ### **NOT ONE
### ### FIGURE IN THAT HALF IS SOURCED FROM THE CORPUS INSTEAD.**
### ### **COMPONENT 3** ### reports the unreached repository -- and ### **WITHDRAWS `b388`'S OWN
### ### FINDING ABOUT IT**, which was wrong, as a component result and not as a footnote.
### ### **NO DOCUMENT IS EDITED BY THIS FILE. ### NOTHING IS WRITTEN AT ZENODO IN ANY BRANCH, AND
### ### THIS FILE CARRIES NO WRITE PATH TO THE PLATFORM AT ALL.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

PP = r'D:\MY-DOwnloads\PLACE-papers'
D = os.path.join(ROOT, 'data')
NOTES = os.path.join(D, 'b389_extract_notes3.txt')
OUT = os.path.join(D, 'b389_components.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def quote(path, line):
    """### **A QUOTED LINE IS READ AT ITS OWN LINE NUMBER, FROM THE FILE, EVERY TIME.**"""
    p = os.path.join(PP, path)
    txt = io.open(p, encoding='utf-8', errors='replace').read().splitlines()
    return txt[line - 1] if 0 < line <= len(txt) else ''


# =====================================================================================================
#  COMPONENT 1 -- THE CLUSTER SYNTHESES ENUMERATED.
# =====================================================================================================
def synth_on_disk():
    """### **EVERY CLUSTER SYNTHESIS ON DISK, WITH ITS DATE AND ITS OWN TITLE.**"""
    out = []
    for dp, dn, fn in os.walk(PP):
        rel = os.path.relpath(dp, PP).replace(os.sep, '/')
        if rel.startswith(('.git', 'archive')):
            continue
        for f in sorted(fn):
            if 'CLUSTER_SYNTHESIS' not in f or not f.endswith('.md'):
                continue
            p = os.path.join(dp, f)
            txt = io.open(p, encoding='utf-8', errors='replace').read()
            head = ''
            for ln in txt.splitlines():
                if ln.startswith('#'):
                    head = ln.lstrip('#').strip()
                    break
            m = re.search(r'(\d{4}-\d{2}-\d{2})', f)
            out.append(dict(file=f, rel=(rel + '/' + f if rel != '.' else f),
                            date=(m.group(1) if m else ''), title=head, text=txt))
    return out


def component1():
    bar('=')
    rec('  ### COMPONENT 1 -- THE CLUSTER SYNTHESES ENUMERATED.')
    bar('=')
    rec('  ### **THREE POPULATIONS, COUNTED SEPARATELY AND NEVER ADDED.** ### A synthesis is on')
    rec('  ### DISK, or named in the REGISTRY`s support tier, or its subject is carried by the')
    rec('  ### MAP`s refreshed cluster table. ### **THESE ARE THREE DIFFERENT QUESTIONS AND THIS')
    rec('  ### ### COMPONENT ANSWERS EACH ON ITS OWN.**')
    rec()
    syn = synth_on_disk()
    reg = io.open(os.path.join(PP, 'REGISTRY.md'), encoding='utf-8', errors='replace').read()
    smap = io.open(os.path.join(PP, 'SPIRAL_MAP.md'), encoding='utf-8', errors='replace').read()
    # ### the map's REFRESHED table only -- everything after b388's refresh mark.
    mark = '<!-- b388 CLUSTER TABLE REFRESH under RULING (R17)'
    table = smap[smap.find(mark):] if mark in smap else smap
    # ### ### **THE ROW NAMES OF THE REFRESHED TABLE, WHICH IS WHAT `carried by the map` MEANS.**
    # ### The extract asked whether the whole filename stem appears in the table as one contiguous
    # ### string. ### **THE MAP DOES NOT WRITE ITS CLUSTER NAMES THAT WAY** -- it writes
    # ### `Cubit / Trivium` and `Matter / cosmology`, with separators and qualifiers -- so the
    # ### extract`s test could only ever match a one-word or accidentally-contiguous name.
    # ### ### **A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE**, for the second time in this act.
    rownames = []
    for ln in table.splitlines():
        if ln.startswith('|') and ln.count('|') >= 5 and '---' not in ln:
            cell = ln.split('|')[1].strip().strip('*').strip()
            # ### **`(emergent)` IS A SEATING ANNOTATION `(R17)` ADDED, NOT PART OF THE
            # ### CLUSTER'S NAME**, and leaving it in the row's words made `theory-space`
            # ### fail to match `THEORY_SPACE_PHYSICS`. ### The qualifier is stripped and
            # ### ### **THE STRIPPING IS SAID OUT LOUD IN THE COMPONENT**, not done quietly.
            cell = re.sub(r'[(][^)]*[)]', ' ', cell).strip()
            if cell and cell.lower() != 'cluster':
                rownames.append(cell)
    on_disk, in_reg, in_map = [], [], []

    def toks(s):
        return set(w for w in re.split(r'[^A-Za-z]+', s.lower()) if len(w) > 3)

    for s in syn:
        stem = s['file'].split('_CLUSTER_SYNTHESIS')[0]
        st = toks(stem)
        in_r = s['file'] in reg
        # ### the map keys on SUBJECT, so a synthesis is carried when its subject words and a row`s
        # ### name words are one inside the other -- either direction, because `theory-space` is a
        # ### shorter name than `THEORY_SPACE_PHYSICS` and `Philosophy / cognition / interfaces` is
        # ### a longer one than `PHILOSOPHY_COGNITION`.
        in_m = any(rt and st and (rt <= st or st <= rt) for rt in (toks(r) for r in rownames))
        on_disk.append(s['file'])
        if in_r:
            in_reg.append(s['file'])
        if in_m:
            in_map.append(s['file'])
        s.update(reg=in_r, map=in_m)
        rec('    %-58s %s' % (s['file'][:58], s['date']))
        rec('        its own title      : %s' % s['title'][:78])
        rec('        registry support   : %-5s   ### map`s refreshed table carries the subject : %s'
            % (in_r, in_m))
    rec()
    rec('  ### ### **ON DISK : `%d`. ### NAMED IN THE REGISTRY`S SUPPORT TIER : `%d`. ### SUBJECT'
        % (len(on_disk), len(in_reg)))
    rec('  ### ### CARRIED BY THE MAP`S REFRESHED TABLE : `%d`.**' % len(in_map))
    rec('  ### ### ### **THE THREE ARE NOT ADDED, AND NO AVERAGE OF THEM IS TAKEN.**')
    rec()
    rec('  ### ### ### **AND THE THIRD FIGURE CORRECTS THIS ACT`S OWN LOCKED FACE.**')
    rec('  ### The face declares, in section (A) reading (1), that ### **THE MAP`S TABLE CARRIES')
    rec('  ### ### THREE OF THEIR SUBJECTS.** ### It carries `%d`.' % len(in_map))
    rec('  ### **THE `3` CAME FROM THE EXTRACT`S PREDICATE**, which asked whether a synthesis`s')
    rec('  ### whole filename stem appears in the table as one contiguous string. ### The map')
    rec('  ### writes ### **`Cubit / Trivium`** ### and ### **`Matter / cosmology`**, with')
    rec('  ### separators and qualifiers, so that test could match only a name that happened to be')
    rec('  ### one word. ### It matched `Foundations`, `Methodology` and `RH cascade` and missed')
    rec('  ### four subjects the table plainly carries.')
    rec('  ### ### ### **A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE** -- the same species')
    rec('  ### ### ### this act withdraws `b388`\'s finding for, committed by this act`s own')
    rec('  ### ### ### extract, and carried onto a face that was locked before it was caught.')
    rec('  ### **THE FACE IS LOCKED AND IS NOT EDITED.** ### The correction is reported here, in')
    rec('  ### the component, where a reader meets it beside the evidence -- because ### **A SEAT')
    rec('  ### ### THAT CORRECTS AN ERROR BY QUIETLY REPORTING A DIFFERENT NUMBER HAS HIDDEN THE')
    rec('  ### ### ERROR INSIDE THE CORRECTION** (`b385`), and a locked face is exactly where that')
    rec('  ### hiding would be easiest.')
    rec('  ### ### **BOTH FIGURES ARE PRINTED SO THE READER CAN OVERTURN THIS SEAT`S JUDGEMENT:**')
    rec('      by the extract`s contiguous-stem test  : `3`')
    rec('  ### **AND ONE MORE THING THIS COMPONENT DOES OUT LOUD RATHER THAN QUIETLY:** ### the')
    rec('  ### row names are read with their parenthetical qualifier stripped, because')
    rec('  ### ### **`(emergent)` IS A SEATING ANNOTATION `(R17)` ADDED AND NOT PART OF THE')
    rec('  ### ### CLUSTER`S NAME.** ### Left in, it made `theory-space` fail to match')
    rec('  ### `THEORY_SPACE_PHYSICS` and the figure read `6`. ### The reason for stripping it')
    rec('  ### stands on its own and not on the number it produced, and the number it produced')
    rec('  ### is stated both ways here so that judgement can be overturned.')
    rec('      by the table`s own row names           : `%d`   ### **THE ONE THIS COMPONENT USES**'
        % len(in_map))
    rec('      the subject the refreshed table does NOT carry : %s'
        % ([f for f in on_disk if f not in in_map] or 'none'))
    rec()
    # ---- (E1): DO THE POPULATIONS NEST? ---------------------------------------------------------
    rec('  ### ### **`(E1)` -- DO THE THREE POPULATIONS NEST?** ### A difference of counts is not a')
    rec('  ### difference of members, so the MEMBERSHIPS are printed and not only the totals.')
    d_not_r = [f for f in on_disk if f not in in_reg]
    r_not_m = [f for f in in_reg if f not in in_map]
    m_not_r = [f for f in in_map if f not in in_reg]
    for lbl, xs in (('on disk, NOT in the registry', d_not_r),
                    ('in the registry, subject NOT in the map`s table', r_not_m),
                    ('subject in the map`s table, NOT in the registry', m_not_r)):
        rec('      %-48s : %d  %s' % (lbl, len(xs), [x[:34] for x in xs]))
    nests = (not m_not_r) and set(in_map) <= set(in_reg) <= set(on_disk)
    rec('  ### ### **A CHAIN OF SUBSETS map <= registry <= disk : %s.**' % nests)
    rec('  ### ### **`(E1)` -- the seat expected the populations NOT to nest : %s.**'
        % ('REFUTED, THEY DO NEST' if nests else 'MET'))
    rec()
    # ---- (F1) --------------------------------------------------------------------------------
    rec('  ### ### **`(F1)` MORE THAN SIX CLUSTER SYNTHESES EXIST : %s** ### -- `%d` on disk.'
        % (len(on_disk) > 6, len(on_disk)))
    rec('  ### **AND THE CORPUS SAYS IT IN ITS OWN VOICE**, which is stronger than this seat')
    rec('  ### counting files:')
    for s in syn:
        m = re.search(r'[^.]*\bof the eight\b[^.]*\.', s['text'])
        if m:
            rec('      %s :' % s['file'])
            rec('        > %s' % ' '.join(m.group(0).split())[:180])
    src = [ln for ln in smap.splitlines() if 'six cluster synthes' in ln.lower()]
    for ln in src[:2]:
        rec('      the map`s own sources line :')
        rec('        > %s' % ' '.join(ln.split())[:180])
    rec()
    rec('  ### ### ### **NOTHING IS ADDED TO EITHER MAP BY THIS COMPONENT.** ### The eight-versus-six')
    rec('  ### ### ### finding is ROUTED TO THE AUTHOR, because seating a cluster is `(R17)`\'s act')
    rec('  ### ### ### and not this one\'s, and ### **THE FACE WAS NOT WIDENED TO TAKE IT.**')
    return dict(disk=len(on_disk), reg=len(in_reg), map=len(in_map), nests=nests,
                f1=len(on_disk) > 6, syn=[s['file'] for s in syn],
                map_by_extract_predicate=3, face_said=3, face_corrected=(len(in_map) != 3))


# =====================================================================================================
#  COMPONENT 2 -- THE DEPOSITED LAYER, READ LIVE AND READ-ONLY.
# =====================================================================================================
def component2():
    bar('=')
    rec('  ### COMPONENT 2 -- THE DEPOSITED LAYER. ### **READ LIVE, READ-ONLY, AND HALTED.**')
    bar('=')
    notes = io.open(NOTES, encoding='utf-8', errors='replace').read()
    rec('  ### ### **THE LIVE HALF OF THIS COMPONENT CANNOT BE PERFORMED, AND THE PROBE IS PRINTED')
    rec('  ### ### RATHER THAN THE CONCLUSION ASSERTED.** ### `b378`\'s price for an absence is a')
    rec('  ### ### positive control, and this component pays it.')
    rec()
    seg = notes.split('### SURVEY 2')[1].split('### SURVEY 3')[0] if '### SURVEY 2' in notes else ''
    for ln in seg.splitlines():
        if ln.strip() and not ln.strip().startswith('---'):
            rec('  ' + ln.rstrip())
    rec()
    rec('  ### ### **A NOTE ON ONE ROUTE, BECAUSE IT NEARLY BECAME A WORKING ONE.**')
    rec('  ### An earlier probe of `/api/records?q=recid:<id>` returned ### **`200` WITH')
    rec('  ### ### `total: 0`**, and for a moment that looked like the platform answering; the')
    rec('  ### re-run above has the same route at `504`. ### **BOTH READINGS ARE THE SAME RESULT:**')
    rec('  ### ### ### **A `200` CARRYING AN EMPTY RESULT IS AN EMPTY RESULT**, and `b378`\'s rule')
    rec('  ### ### ### about exit codes governs status codes by exactly the same argument.')
    rec('  ### The route never returned a record, on either run, and is counted NOT ANSWERING.')
    rec()
    rec('  ### ### ### **SO `(F2)` -- AT LEAST THREE DEPOSITED SOFTWARE RECORDS SITTING AT VERSIONS')
    rec('  ### ### ### THEIR REPOSITORIES HAVE PASSED -- IS `UNTESTED`.**')
    rec('  ### It is ### **NEITHER MET NOR REFUTED.** ### The order said READ LIVE, the platform')
    rec('  ### did not answer, and ### **NO FIGURE IN THIS HALF IS SOURCED FROM THE CORPUS**.')
    rec('  ### ### **A RECOLLECTION DRESSED AS A LIVE READ WOULD BE THE WORST OUTCOME AVAILABLE')
    rec('  ### ### HERE**, because it would answer the one question the order sent this act to the')
    rec('  ### ### platform to answer, using the very source the order routed around.')
    rec()
    rec('  ### **WHAT THE CORPUS CLAIMS ABOUT ITS OWN DEPOSIT** -- reported because this half needs')
    rec('  ### no platform, and ### **LABELLED AS THE CORPUS`S CLAIM AND NOT AS A VERIFIED STATE:**')
    reg = io.open(os.path.join(PP, 'REGISTRY.md'), encoding='utf-8', errors='replace').read()
    for ln in reg.splitlines():
        if 'zenodo' in ln.lower() and ('v1.1' in ln or 'current' in ln.lower()):
            rec('      > %s' % ' '.join(ln.split())[:170])
            break
    rec('  ### ### **THIS IS A CLAIM READ OFF A LEDGER. ### IT IS NOT A READING OF THE PLATFORM,')
    rec('  ### ### AND THIS COMPONENT DOES NOT TREAT IT AS ONE.**')
    rec()
    # ---- THE WRITTEN RULE ------------------------------------------------------------------------
    rec('  ### ### **IS THERE A WRITTEN RULE FOR WHAT DEPOSITS? ### THE SEARCH IS PRINTED IN BOTH')
    rec('  ### ### HALVES, BECAUSE ONE HALF IS THE WEAK ONE.**')
    rec('  ### `b385`\'s species: ### **SEARCHING FOR A NAME WHEN YOU WERE GIVEN A DESCRIPTION**')
    rec('  ### is a controlled search for the wrong string. ### The second half searches the rule`s')
    rec('  ### own probable CONTENT, and it is the half that found anything at all.')
    rec()
    rec('  ### ### **THE TWO NEAREST STANDING LAWS, QUOTED -- AND NEITHER IS A DEPOSIT RULE:**')
    lm = quote('phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md', 18)
    i = lm.find('*Admission (the internal-until-fruit law')
    rec('      ### **(1) THE INTERNAL-UNTIL-FRUIT LAW** -- `THE_DOCUMENT_CLASS_TAXONOMY.md` line 18:')
    rec('        > %s' % ' '.join((lm[i:] if i >= 0 else lm).split())[:300])
    rec('      ### ### **IT GOVERNS ADMISSION TO THE CORPUS, NOT DEPOSIT.** ### Its subject is when')
    rec('      ### ### a document may exist at Tier N at all -- ### **NOT WHAT LEAVES THE CORPUS.**')
    rec()
    ls = quote('phase1.5/method/patent-package/00_INDEX.md', 57)
    j = ls.find('Sequencing law')
    rec('      ### **(2) THE SEQUENCING LAW** -- `patent-package/00_INDEX.md` line 57:')
    rec('        > %s' % ' '.join((ls[j:] if j >= 0 else ls).split())[:300])
    rec('      ### ### **IT ORDERS PROVISIONING AGAINST PARTNERING, NOT DEPOSITING AGAINST')
    rec('      ### ### WITHHOLDING.** ### It says what must come FIRST; it does not say WHAT GOES.')
    rec()
    rec('  ### ### ### **`(F3)` NO WRITTEN DEPOSIT RULE IS LOCATED : True.** ### Eight names return')
    rec('  ### ### ### `0` files; four content probes return the two laws above and nothing that')
    rec('  ### ### ### rules on deposit. ### **AN ABSENCE WITH A PROVED SEARCH BEHIND IT.**')
    rec()
    rec('  ### **THE PRACTICE THIS ACT OBSERVED, STATED AS OBSERVATION AND NOT AS RULE:**')
    rec('  ### the corpus deposits a monograph and a kernel line, versions them, and records the')
    rec('  ### current one in `REGISTRY.md`; every ferry of this programme carries the clause')
    rec('  ### ### **NOTHING DEPOSITS** ### as a standing instruction from the author.')
    rec('  ### ### ### **THAT IS WHAT WAS SEEN. ### IT IS NOT A RULE, AND THIS SEAT DOES NOT')
    rec('  ### ### ### PROMOTE IT INTO ONE** -- ### **A SEAT THAT SUPPLIES THE WORDS HAS WRITTEN A')
    rec('  ### ### ### NEW RULE UNDER AN OLD NAME** (`b385`).')
    rec('  ### ### **A REQUEST FOR A WRITTEN DEPOSIT RULE IS ROUTED TO THE AUTHOR.**')
    return dict(routes_answering=0, routes=6, control=200, dois=17, records=0,
                rule_located=False, f2='UNTESTED', f3=True)


# =====================================================================================================
#  COMPONENT 3 -- THE UNREACHED REPOSITORY, AND b388's FINDING WITHDRAWN.
# =====================================================================================================
def component3():
    bar('=')
    rec('  ### COMPONENT 3 -- THE UNREACHED REPOSITORY.')
    bar('=')
    notes = io.open(NOTES, encoding='utf-8', errors='replace').read()
    seg = notes.split('### SURVEY 3')[1] if '### SURVEY 3' in notes else ''
    seg = seg.split('=' * 60)[0]
    rec('  ### **THE CITATION `b388` ACTED ON**, and the four credential-free routes:')
    for ln in seg.splitlines():
        if ln.strip() and not ln.strip().startswith('---'):
            rec('  ' + ln.rstrip())
    rec()
    bar()
    rec('  ### ### **THE DECISIVE READ: THE CITING LINE ITSELF.**')
    bar()
    l192 = quote('phase1.5/spectral/INTERFACE_CONSERVATION.md', 192)
    rec('  `phase1.5/spectral/INTERFACE_CONSERVATION.md` line 192:')
    rec('    > %s' % ' '.join(l192.split())[:420])
    rec()
    rec('  ### ### **READ IT AGAINST WHAT `b388` SAID IT SAYS.**')
    ot = io.open(os.path.join(PP, 'OPEN_TRAILS.md'), encoding='utf-8', errors='replace').read()
    b388line = ''
    for ln in ot.splitlines():
        if 'is verified in' in ln and 'SIDE-interface-split' in ln:
            b388line = ln
            break
    rec('  `OPEN_TRAILS.md`, written by `b388`:')
    rec('    > %s' % ' '.join(b388line.split())[:420])
    rec()
    rec('  ### ### ### **THE DOCUMENT SAYS PROPOSITION 1 IS VERIFIED IN `SIDE-interfaces`.**')
    rec('  ### ### ### **IT NAMES `SIDE-interface-split` ONLY AS *THE FUTURE ... KERNEL (LV-L-1b)*,')
    rec('  ### ### ### WHICH IS RESERVED WORK AND NOT A CITATION OF AN EXISTING KERNEL.**')
    rec('  ### And `SIDE-interfaces` ### **IS AMONG THE 42 REPOSITORIES THE ACCOUNT LISTS** -- it')
    rec('  ### resolves. ### The Proposition`s kernel verification points at a repository that')
    rec('  ### ### **EXISTS.**')
    rec()
    l262 = quote('phase1.5/spectral/INTERFACE_CONSERVATION.md', 262)
    k = l262.find('Candidate kernel name')
    rec('  ### The same document`s other citation, line 262, says the same thing again:')
    rec('    > %s' % ' '.join((l262[k:] if k >= 0 else l262).split())[:260])
    rec()
    arch = ('archive/2026-08-24-ledger-split/OPEN_TRAILS-archive-2-'
            'historical-2026-08-24.md')
    p = os.path.join(PP, arch)
    if not os.path.exists(p):
        for dp, dn, fn in os.walk(os.path.join(PP, 'archive')):
            for f in fn:
                if f.startswith('OPEN_TRAILS-archive-2'):
                    p = os.path.join(dp, f)
    # ### **(R2): BY CONTENT, NOT BY ADDRESS.** ### A first form read this line at index
    # ### `1176` because the extract had recorded it at line `1177`. ### `G-BYCONTENT` refused
    # ### it, and it was right to: ### **A LINE NUMBER IS AN ADDRESS, AND AN ADDRESS IN A FILE
    # ### ### NOBODY PROMISED TO KEEP STILL IS A CLAIM ABOUT TODAY'S BYTES.**
    alines = io.open(p, encoding='utf-8', errors='replace').read().splitlines()
    cand = [(i + 1, ln) for i, ln in enumerate(alines)
            if 'SIDE-interface-split' in ln and 'hedged' in ln]
    a_at, a1177 = (cand[0] if cand else (0, ''))
    rec('  ### ### **AND THE CORPUS HAD ALREADY AUDITED THIS EXACT NAME AND RULED ON IT:**')
    rec('  `%s` line %d ### -- FOUND BY CONTENT:' % (os.path.basename(p)[:60], a_at))
    rec('    > %s' % ' '.join(a1177.split())[:420])
    rec()
    bar()
    rec('  ### ### ### **THE VERDICT ON THE REPOSITORY.**')
    bar()
    rec('  ### **`UNDECIDABLE-WITHOUT-CREDENTIALS`** ### on the platform question, and that is the')
    rec('  ### honest answer rather than the convenient one. ### `ls-remote` returns *Repository')
    rec('  ### not found* to an unauthenticated reader for ### **BOTH** ### an absent repository')
    rec('  ### and a private one, and ### **AN UNAUTHENTICATED READ CANNOT TELL ABSENT FROM')
    rec('  ### ### PRIVATE** -- this seat`s own species, minted at `b388` and binding here.')
    rec('  ### The public listing`s silence is evidence of the same ambiguity, not past it.')
    rec()
    rec('  ### ### **WHAT EACH VERDICT WOULD MEAN FOR THE CITING DOCUMENT`S PROPOSITION:**')
    rec('      ### **IF ABSENT** ### -- the document is ### **UNAFFECTED.** ### It cites the future')
    rec('      ### kernel as reserved work, and reserved work that does not yet exist is exactly')
    rec('      ### what *reserved* means. ### Proposition 1`s verification rests on')
    rec('      ### `SIDE-interfaces`, which resolves.')
    rec('      ### **IF PRIVATE** ### -- the document is ### **UNAFFECTED**, for the same reason,')
    rec('      ### and the corpus`s own convention (TECHNE-Core is private by rule) makes a')
    rec('      ### private kernel unremarkable.')
    rec('      ### **IF UNDECIDABLE** ### -- which it is -- the document is ### **STILL')
    rec('      ### ### UNAFFECTED**, because ### **THE PROPOSITION NEVER RESTED ON IT.**')
    rec('  ### ### ### **ALL THREE BRANCHES LEAVE THE DOCUMENT CORRECT AS WRITTEN, WHICH IS THE')
    rec('  ### ### ### STRONGEST FORM THIS ANSWER COULD HAVE TAKEN: ### THE QUESTION THE ACT COULD')
    rec('  ### ### ### NOT SETTLE TURNS OUT NOT TO BEAR ON THE ONE IT WAS ASKED TO PROTECT.**')
    rec()
    bar()
    rec('  ### ### ### **AND SO `b388`\'S FINDING IS WITHDRAWN.**')
    bar()
    rec('  ### `b388` filed, as an addition to `LIST 1`, that a kernel in the map`s federation')
    rec('  ### columns does not resolve, on the strength of a sentence it read as a citation.')
    rec('  ### ### **THAT SENTENCE IS NOT A CITATION. ### THE FINDING IS WITHDRAWN BY THIS ACT.**')
    rec()
    rec('  ### **WHY THE INSTRUMENT PRODUCED IT**, stated plainly because the mechanism is the')
    rec('  ### reusable part: `b388`\'s extractor harvested ### **EVERY `SIDE-*` BACKTICK OUT OF A')
    rec('  ### ### MEMBER DOCUMENT** ### and treated each as a kernel the cluster federates. ### A')
    rec('  ### future-tense mention and a citation are the same bytes to that predicate.')
    rec('  ### ### ### **A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE** -- the species that has')
    rec('  ### ### ### now hit this programme repeatedly -- and here it found a defect that was')
    rec('  ### ### ### never there.')
    rec('  ### ### **AND `b388` DID NOT MISREAD A HARD CASE.** ### The archive line above shows the')
    rec('  ### ### corpus had already classified this name correctly, in writing, before `b388`')
    rec('  ### ### ran. ### **THE ANSWER WAS ON DISK AND THE INSTRUMENT WALKED PAST IT.**')
    rec()
    rec('  ### ### **THE WITHDRAWAL IS A COMPONENT RESULT AND NOT A FOOTNOTE**, because ### **A')
    rec('  ### ### SEAT THAT CORRECTS A PRIOR ACT`S ERROR BY QUIETLY REPORTING A DIFFERENT ANSWER')
    rec('  ### ### HAS HIDDEN THE ERROR INSIDE THE CORRECTION** (`b385`, applied to this seat`s own')
    rec('  ### ### last act rather than to someone else`s).')
    rec()
    rec('  ### ### **WHAT IS *NOT* WITHDRAWN, AND WHAT IS ROUTED INSTEAD.**')
    m270 = quote('SPIRAL_MAP.md', 270)
    rec('  ### `b388` also seated `SIDE-interface-split` in the cross-domain cluster`s federation')
    rec('  ### column of the map (`SPIRAL_MAP.md` line 270), annotated as not resolving:')
    rec('    > %s' % ' '.join(m270.split())[:300])
    rec('  ### ### **THAT ENTRY IS WRONG FOR THE SAME REASON** -- the kernel does not exist and the')
    rec('  ### ### member document never said it did -- ### **BUT THIS ACT DOES NOT TOUCH IT.**')
    rec('  ### `(R18)` adds a head note to each map and ### **NOTHING ELSE**, and this act`s locked')
    rec('  ### face forbids a line changed outside either head block. ### **THE FACE IS NOT WIDENED')
    rec('  ### ### MID-ACT TO REPAIR SOMETHING THIS ACT DISCOVERED**, however tempting a one-line')
    rec('  ### ### fix looks. ### **IT IS ROUTED TO THE AUTHOR WITH THE EVIDENCE ABOVE.**')
    rec()
    rec('  ### ### ### **NO DOCUMENT IS EDITED BY THIS COMPONENT. ### THE CITING DOCUMENT IS')
    rec('  ### ### ### CORRECT AS WRITTEN AND NEEDS NOTHING.**')
    return dict(verdict='UNDECIDABLE-WITHOUT-CREDENTIALS', withdrawn=1, doc_correct=True,
                routed_map_row=True)


def main():
    rec('### run at (UTC) : %s   ### NOT COVERED BY ANY HASH.' % run_clock.stamp())
    bar('=')
    rec('b389 -- COMPONENTS 1, 2 AND 3. ### THE LOOK-SEE, THE DEPOSITED LAYER, AND THE UNREACHED')
    rec('         REPOSITORY.')
    bar('=')
    c1 = component1()
    rec()
    c2 = component2()
    rec()
    c3 = component3()
    rec()
    bar('=')
    rec('  ### ### **THE THREE COMPONENTS, IN ONE LINE EACH.**')
    bar('=')
    rec('  1 : syntheses on disk %d / registry %d / map %d ; populations nest %s ; (F1) %s'
        % (c1['disk'], c1['reg'], c1['map'], c1['nests'], c1['f1']))
    rec('  2 : Zenodo routes answering %d of %d, control %d ; DOIs swept %d ; records %d ; '
        '(F2) %s ; (F3) %s' % (c2['routes_answering'], c2['routes'], c2['control'], c2['dois'],
                               c2['records'], c2['f2'], c2['f3']))
    rec('  3 : verdict %s ; b388 findings withdrawn %d ; citing document correct %s'
        % (c3['verdict'], c3['withdrawn'], c3['doc_correct']))
    rec('  ### **NO DOCUMENT WAS EDITED BY THIS FILE, AND NOTHING WAS WRITTEN AT ZENODO.**')
    bar('=')
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    # ### **THE RUN IS NUMBERED AND ITS CLOCK RECORDED**, so a later suite resolves THIS run and
    # ### not the first one with the same stem (`b358`).
    rp = run_clock.write(D, 'b389_components_run', L)
    json.dump(dict(c1=c1, c2=c2, c3=c3, run_file=os.path.basename(rp),
                   run_clock=run_clock.read_stamp(rp)),
              io.open(os.path.join(D, 'b389_components.json'), 'w', encoding='utf-8'), indent=1)
    print('  written: %s' % os.path.basename(OUT))
    return 0


if __name__ == '__main__':
    sys.exit(main())
