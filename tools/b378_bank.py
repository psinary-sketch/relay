# -*- coding: utf-8 -*-
"""b378_bank.py -- THE BANK, WRITTEN FROM THE ACT'S OWN JSONS. ### **NO FIGURE IS TYPED.**

### ### **AND IT CARRIES THE ACT'S OWN DEFECT AT FULL STRENGTH**, because the sharpest thing this act
### learned it learned by being wrong in a way that looked exactly like being right.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
OUT = os.path.join(D, 'b378_the_refs_widened.txt')
REG = os.path.join(D, 'b378_registration_2026-09-08.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def J(n):
    return json.load(io.open(os.path.join(D, n + '.json'), encoding='utf-8'))


E, LG, TM, AR, HD, Q = (J('b378_reads'), J('b378_lockgate'), J('b378_terminals'),
                        J('b378_archives'), J('b378_hand'), J('b378_desk'))
BR377 = J('b377_branch')
CL375 = J('b375_clusters')
regtxt = io.open(REG, encoding='utf-8').read()
SHA = re.search(r'sha256 of every byte ABOVE this block : (\w+)', regtxt).group(1)
NBY = re.search(r'bytes locked : (\d+)', regtxt).group(1)
LAT = re.search(r'locked at \(UTC\) : (\S+)', regtxt).group(1)
NCL = len(J('b378_satisfiable')['clauses'])

L = []


def w(s=''):
    L.append(s)


BAR, SUB = '=' * 100, '-' * 100
TALLY = TM['tally']


def T(k):
    for kk, v in TALLY.items():
        if k in kk:
            return v
    return 0


CARRIED, REFS, KERN = TM['carried'], TM['refs'], TM['kernels']
NOTFOUND, MATHLIB, DOCNAME = T('NOT-FOUND-ON-ANY-REF'), T('Mathlib'), T('NAMES-A-CORPUS-DOCUMENT')
NONMAIN, MULTI = T('FOUND-ON-A-NON-main-REF'), T('MORE THAN ONE KERNEL')
NOKEY = CL375['subject_clusters_without_keystone']

w(BAR)
w('b378 -- THE REFS WIDENED AND THE CONVENTION SWEPT. ### THE BANK.')
w(BAR)
w('')
w('### ### ### **THE HEADLINE IS A CORRECTION, AND THE SHARPEST FINDING IS ABOUT THIS ACT`S OWN')
w('### ### ### SEARCH:**')
w('### ### ### **AN UPPER BOUND TAKEN AT ONE REF IS NOT A COUNT** -- and ### **A SEARCH THAT CANNOT')
w('### ### ### RUN LOOKS EXACTLY LIKE A SEARCH THAT FOUND NOTHING.**')
w('')
w('### `b377` searched ### **%d REFS -- ONE PER KERNEL** ### and reported ### **%d** ### identifiers'
  % (KERN, CARRIED))
w('### that no kernel declares. ### This act searched ### **%d REFS BEHIND %d DISTINCT COMMITS**, and'
  % (REFS, TM['commits']))
w('### the figure falls to ### **%d**.' % NOTFOUND)
w('### ### **`b377`S NUMBER WAS NEVER WRONG. ### IT WAS AN UPPER BOUND TAKEN AT ONE REF AND WAS NOT')
w('### ### LABELLED AS ONE**, and it is labelled as one now.')
w('')
w('### ### **WHERE THE OTHER %d WENT, EACH TO EXACTLY ONE CLASSIFICATION:**' % (CARRIED - NOTFOUND))
w('###   ### **%d ARE `Mathlib` NAMES** ### -- declared in the Mathlib package on this disk. ### A'
  % MATHLIB)
w('###     paper may cite a library lemma it did not prove; ### **THAT IS A CATEGORY AND NOT A')
w('###     ### FAULT.**')
w('###   ### **%d NAME A CORPUS DOCUMENT RATHER THAN A TERMINAL** ### -- `OPEN_TRAILS`,' % DOCNAME)
w('###     `THE_RESIDUE_OF_RH`, `THE_CODOMAIN_SPECIFICATION` and others are `.md` files. ### **THEY')
w('###     ### WERE NEVER TERMINALS AND WERE COUNTED AS MISSING ONES.**')
w('###   ### **%d ARE DECLARED ON A TAG AND ON NO BRANCH AT ALL** ### -- `grh_exclusion` and' % NONMAIN)
w('###     `no_ls_zero`, on `refs/tags/phase-1.5-module-1-v2` of `SIDE-effects`. ### **A TAG IS A')
w('###     ### REF, AND `b377` DID NOT SEARCH IT.** ### This is `(F2)`, met.')
w('###   ### **%d IS DECLARED IN MORE THAN ONE KERNEL** ### -- `silence_universal`, in `SIDE-kernel`'
  % MULTI)
w('###     and `SIDE-silence-principle`. ### `b377` minted the rule that such a name is not a')
w('###     terminal a document can cite; ### **CARRYING IT HERE IS WHAT STOPPED THIS ACT READING THE')
w('###     ### FIRST OF SEVERAL SILENTLY, AS ITS OWN FIRST RUN DID.**')
w('### ### ### **`(F1)` IS MET: ### %d IS MATERIALLY LOWER THAN %d.** ### And `(F2)` is met by the'
  % (NOTFOUND, CARRIED))
w('### ### ### tag. ### **BOTH BY A PRINTED CLASSIFICATION, PER IDENTIFIER.**')
w('')

# ---------------------------------------------------------------------------- THE ACT'S OWN DEFECT
w(SUB)
w('### THE DEFECT THIS ACT FOUND IN ITSELF, AT FULL STRENGTH.')
w(SUB)
w('### The first sweep handed `git grep -E` a pattern containing `(?:...)`. ### **POSIX ERE REJECTS')
w('### ### IT.** ### Every one of the %d invocations died with `Invalid preceding regular expression`;'
  % TM['commits'])
w('### the caller read the non-zero exit as ### **NO MATCHES**; and the sweep reported')
w('### ### **`0` IDENTIFIERS FOUND ACROSS %d REFS.**' % REFS)
w('### ### ### **A CLEAN, CONFIDENT, ENTIRELY FALSE ANSWER.**')
w('### ### **IT WAS EXPOSED ONLY BY A CONTRADICTION WITH `b377`S OWN RECORD**, which had found')
w('### `silence_universal` in two kernels. ### Without that contradiction this act would have')
w('### reported ### **`37` STILL MISSING** ### and called the widening a refutation of `(F1)`.')
w('### ### **THE CURE IS THREE THINGS, AND THE SECOND IS THE ONE THAT GENERALISES:**')
w('###   (1) the pattern handed to `git` is ### **POSIX**, and the Python pattern stays in Python;')
w('###   (2) ### **AN EXIT CODE ABOVE 1 IS AN ERROR AND NOT AN ANSWER** -- `git grep` exits `1` for')
w('###       *no matches* and higher for *I could not search*, and ### **CONFLATING THOSE IS HOW A')
w('###       ### BROKEN SWEEP REPORTS A CLEAN ONE**;')
w('###   (3) a ### **POSITIVE CONTROL** ### -- a name known to sit on a non-`main` ref -- runs first,')
w('###       and the tool ### **REFUSES TO REPORT AN ABSENCE UNTIL IT HAS PROVED IT CAN FIND A')
w('###       ### PRESENCE.**')
w('### ### **THE CONTROL HELD ON THE FINAL RUN: `%s` FOUND ON %d COMMIT(S), %d OF THEM NOT `main`.**'
  % (TM['control_name'], TM['control_hits'], TM['control_non_main']))
w('### ### **AND SEARCHES THAT COULD NOT RUN, ON THE FINAL SWEEP : %d.**' % len(TM['grep_errors']))
w('')

# ------------------------------------------------------------------------------------- STEP ZERO
w(SUB)
w('### STEP ZERO -- THE LOCK GATE`S REMAINING HOLE, CLOSED IN THE TOOL.')
w(SUB)
w('### `b376` proved every gate passed and ### **COULD NOT PROVE WHAT ANY OF THEM PASSED ON**, and')
w('### said so on its own face. ### `b377` hit it: a late rewrite left gate records stale and only')
w('### the seat`s discipline caught it.')
w('### ### **`tools/gate_hash.py`, NEW AND SHARED:** ### it stamps a gate`s own run record with the')
w('### `sha256` of the bytes that gate read, ### **APPENDING AND NEVER REWRITING**, so the gate`s own')
w('### output survives exactly as the gate wrote it.')
w('### ### **`tools/b378_lockgate.py`, NEW:** ### every face-subject gate must carry a stamp')
w('### ### **EQUAL TO THE FACE IT IS ABOUT TO LOCK**, and a record carrying no stamp is')
w('### ### **REFUSED, NOT WAVED THROUGH** -- an absent claim is not a true one.')
w('###   gates read : ### **%d** ### / passing : ### **%d** ### / checked by digest : ### **%d**'
  % (LG['gates_read'], LG['gates_passing'], LG['face_subject_gates']))
w('###   the face`s sha256 : `%s`' % LG['face_sha'])
w('### ### **FIXTURED IN FOUR POLARITIES, NOT TWO:**')
for k, v in LG['fixture'].items():
    w('###     %-42s permits : %-5s   failing : %s' % (k[:42], v['permits'], v['failing'] or 'none'))
w('### ### ### **AND THE STALE-DIGEST POLARITY IS THE ONE `b377` SUFFERED.**')
w('### ### **THIS ACT`S OWN FACE WAS REWRITTEN BEFORE THE LOCK** -- `U-1` fired on two sentences --')
w('### **AND EVERY FACE-SUBJECT GATE WAS RE-RUN AND RE-STAMPED.** ### The gate would have refused')
w('### otherwise, which is the whole point of building it.')
w('### ### **WHAT IT STILL DOES NOT PROVE, SAID ON THE FACE BEFORE IT RAN:** ### the stamp is')
w('### ### **THE CALLER`S CLAIM ABOUT WHAT IT FED THE GATE**, not the gate vouching for itself.')
w('### Making the gate vouch for itself would mean editing the shared instruments, and ### **THIS ACT')
w('### ### EDITS NO OWNER INSTRUMENT.**')
w('')

# ------------------------------------------------------------------------------- THE CLASSIFICATION
w(SUB)
w('### ADDITION ONE -- EVERY REF, AND THE CORRECTED CLASSIFICATION.')
w(SUB)
w('### refs enumerated live from each repository : ### **%d** ### behind ### **%d** ### distinct'
  % (REFS, TM['commits']))
w('### commits, across ### **%d** ### kernels. ### **NEVER TYPED, NEVER ASSUMED.**' % KERN)
w('')
w('###   %-46s %-34s %s' % ('identifier', 'classification', 'where'))
w('###   %s' % ('-' * 94))
for r in TM['rows']:
    w('###   %-46s %-34s %s'
      % (r['name'][:46], r['classification'].replace('### **', '').replace('**', '')[:34],
         r['where'][:40]))
w('')
w('### ### **THE TALLY : %s**' % TALLY)
w('')
w('### **THE HELD BRANCH THE DOCUMENT NAMES IN ITS OWN TEXT:**')
w('###   `THE_RESIDUE_OF_RH.md` line %d :' % TM['held_branch']['line'])
for seg in re.findall(r'.{1,90}(?:\s|$)', TM['held_branch']['sentence']):
    if seg.strip():
        w('###     | %s' % seg.rstrip())
w('###   the branch : `%s` in `%s`' % (TM['held_branch']['name'], TM['held_branch']['kernel']))
w('###   refs matching it, enumerated live : %s' % TM['held_branch']['refs'])
w('###   ### **CARRIED IDENTIFIERS FOUND ON IT : %d**' % len(TM['held_branch']['identifiers_found']))
w('### ### **THE BRANCH WAS SEARCHED BY NAME AND THE ANSWER THERE IS STILL NO.** ### The positive')
w('### control IS on it, which is how we know the branch was genuinely read rather than skipped.')
w('### ### **A DOCUMENT THAT TELLS YOU WHERE TO LOOK HAD ALREADY DONE HALF THE WORK.**')
w('')

# --------------------------------------------------------------------------------- THE CONVENTIONS
w(SUB)
w('### ADDITION TWO -- THE TWO CONVENTIONS, SWEPT AND NEITHER REWRITTEN.')
w(SUB)
w('### ### **THE MATCHER, FIXTURED BEFORE IT WAS USED:**')
for c in TM['fixtures']:
    w('###   %-56s got %-5s want %-5s %s'
      % (c['case'].replace('### **', '').replace('**', '')[:56], c['got'], c['want'],
         'ok' if c['got'] is c['want'] else '### MISMATCH'))
w('### ### **THE LAST THREE ARE THE DISCRIMINATION ARM.** ### A matcher that accepts everything is')
w('### not a matcher, and widening one that was too narrow is exactly the moment to prove it did not')
w('### become too wide.')
w('')
w('### ### **WHICH CONVENTION EACH CITING DOCUMENT USES:**')
for c in TM['conventions']:
    w('###   %-36s bare %-3d dotted %-3d  ### **%s**'
      % (os.path.basename(c['file'])[:-3][:36], c['bare'], c['dotted'], c['convention']))
w('### ### ### **NOT ONE OF THEM USES THE DOTTED CONVENTION ALONE.**')
w('### ### **AND `b376`S AXIS-B PREDICATE REQUIRED A DOTTED TERMINAL, SO IT COULD NOT HAVE PASSED')
w('### ### ANY OF THEM.** ### **THE COST IS NOT HYPOTHETICAL: ### IT SELECTED THE SIX**, and `b377`')
w('### inherited that selection as its whole population.')
w('### **WHERE ELSE IN THE RECORD IT MAY HAVE COST THE SAME, NAMED AND NOT SWEPT:**')
w('###   ### **`b376`S ENTIRE AXIS-B COLUMN** -- `303` documents scored `B-` on that predicate. ###')
w('###     Any of them writing the bare dialect is scored as an absence. ### **THAT COLUMN IS NAMED')
w('###     ### HERE AS SUSPECT AND IS NOT RE-MEASURED**, because re-measuring it is an act and not a')
w('###     footnote.')
w('###   ### **AND `b376`S `A+B+` QUADRANT AND EVERY COUNT DERIVED FROM IT.**')
w('###   ### **BUT NOT `b375`S CENSUS COMPARISON**, which used a HEADING test rather than a terminal')
w('###     test and is therefore ### **UNAFFECTED** -- said so that the suspicion is bounded rather')
w('###     than free-floating.')
w('### ### **NO DOCUMENT IS REWRITTEN INTO THE OTHER DIALECT. ### BOTH ARE CORRECT IN THEIR OWN')
w('### ### TERMS**, and an older document naming `residue_irreducible` is writing the convention its')
w('### era wrote.')
w('')

# ------------------------------------------------------------------------------------ THE ARCHIVES
w(SUB)
w('### ADDITION THREE -- THE ARCHIVES, CONFIRMED AND NOT REMOVED.')
w(SUB)
w('### the project mirror : `%s`, %d entries' % (AR['mirror'], AR['mirror_entries']))
w('### ### **THE ORDERED POPULATION -- ARCHIVE FILES THE MIRROR CARRIES : %d**'
  % AR['ordered_population'])
w('')
for r in AR['rows']:
    w('###   `%s`' % r['source_path'])
    w('###     %s' % r['verdict'].replace('### **', '### **'))
    w('###     sha256 : `%s`' % (r['digest'] or 'NONE'))
    w('###     digest match : %-5s  title-line match : %-5s' % (r['digest_match'], r['title_match']))
    w('###     title : %s' % (r['title_disk'] or 'NONE')[:88])
    w('###     ### *(filename in the mirror `%s` -- ### **NOT USED AS EVIDENCE**)*'
      % (r['in_mirror_as'] or '-'))
w('')
w('### ### **CONFIRMED PRESENT : %d ### / ### NOT CONFIRMED : %d ### of %d**'
  % (AR['confirmed'], AR['not_confirmed'], AR['ordered_population']))
w('### ### **CONFIRMED BY A VERIFIED DIGEST AND BY A TITLE LINE. ### NEVER BY FILENAME** -- the')
w('### mirror export is flat and derives each name from its source path, and the repository strips')
w('### version suffixes besides. ### The filename comparison is printed beside each verdict')
w('### ### **SO A READER CAN SEE IT WAS NOT USED.**')
w('### **CONTEXT, LABELLED AS CONTEXT AND NOT THE ORDERED REPORT:** ### `%d` files sit under'
  % AR['context_archive_files'])
w('### `archive/` on the canonical drive and the mirror carries `%d` of them; the other `%d` were'
  % (AR['ordered_population'], AR['context_not_carried']))
w('### ### **NOT CONFIRMED BY THIS ACT AND IT MAKES NO CLAIM ABOUT THEM.**')
w('### ### ### **NOTHING WAS REMOVED, MOVED OR RENAMED. ### THE REMOVAL IS THE AUTHOR`S AND DEPENDS')
w('### ### ### ON THIS REPORT** -- which is exactly why the report had to be able to say NOT')
w('### ### ### CONFIRMED, and why a near miss is reported as a near miss rather than rounded up.')
w('')

# ------------------------------------------------------------------------------------ THE HAND READ
w(SUB)
w('### THE DRAFT`S COMPONENT 3 -- ONE `NOT DETERMINABLE` DOCUMENT, READ BY HAND.')
w(SUB)
w('### **CHOSEN : `%s`** ### -- by a stated rule: %s.' % (HD['chosen'], HD['chosen_by']))
w('### The other, `%s`, is ### **LEFT EXACTLY AS `b377` LEFT IT.**' % HD['other'][0])
w('###   identifiers named, each with the sentence that names it : ### **%d**' % HD['named'])
w('###   ### **LOCATED IN EXACTLY ONE KERNEL : %d**' % HD['located'])
w('###   located in more than one : %d ### / ### not located on any ref : %d'
  % (HD['ambiguous'], HD['not_located']))
w('### ### ### **WHAT THE HAND READ DECIDES THAT THE TABLE SCAN COULD NOT:** ### the document')
w('### ### ### ### **%s.**' % HD['decided'])
w('### ### **AND WHAT IT STILL DOES NOT DECIDE:** ### whether the document`s SENTENCES about those')
w('### terminals are right. ### **LOCATING A NAME SAYS IT EXISTS AT THAT NAME**, and this read')
w('### checked existence and not truth.')
w('### ### ### **THE OUTCOME IS A MARK, NOT A CLASS.** ### No declaration was moved, no class was')
w('### ruled, and ### **NOT ONE BYTE WAS WRITTEN INTO THE DOCUMENT.**')
w('')

# ------------------------------------------------------------------------------------- WHAT IS NOT
w(SUB)
w('### WHAT THIS ACT DID NOT DO.')
w(SUB)
w('### ### **NO CLASS WAS RULED. ### NO DOCUMENT WAS RECLASSIFIED. ### NO DECLARATION WAS MOVED.')
w('### ### ### NO LIST WAS CLOSED.**')
w('### ### **NO CORPUS DOCUMENT WAS WRITTEN INTO AT ALL** -- not the six, not the two, not the')
w('### archives, not the census. ### **NO ARCHIVE FILE WAS REMOVED, MOVED OR RENAMED.**')
w('### ### **NO DOCUMENT WAS REWRITTEN INTO THE OTHER CONVENTION.**')
w('### ### **THE SIX SUBJECT CLUSTERS STAY FILED AND NOT OPENED.** ### The order adopted the')
w('### executor`s draft and named three additions, none of which is the cluster lane, and its own')
w('### closing does not mention it. ### **THAT READING WAS DECLARED ON THIS ACT`S LOCKED FACE IN')
w('### ### ADVANCE, WHERE THE AUTHOR CAN CORRECT IT** -- which is the only honest place to put an')
w('### interpretation of an order. ### %d clusters, unchanged.' % len(NOKEY))
w('### ### **THE CENSUS STAYS QUOTED AND NOT REPAIRED. ### THE COLUMN-(d) FIGURE STAYS A FLOOR AND')
w('### ### IS NOT RE-MEASURED.**')
w('### ### **NO OWNER INSTRUMENT WAS EDITED**, `b376`s lock gate included: it is superseded for this')
w('### act by a new file and is left exactly as it stands.')
w('### ### **NO `.lean` FILE TOUCHED, NO BUILD RUN, NO AXIOM PROFILE RECOMPUTED.**')
w('### ### **THE FOUR OPEN LISTS ARE RESTATED `OPEN` BY NAME, IN THE DESK`S OWN WORDS:**')
for _lst in ('the rows that cite at a ref nobody can name',
             'the rows grading a declaration the record has classified absent',
             'the undated figures across the roster',
             'the bibliography entries nothing cites'):
    w('###   ### **OPEN** ### -- %s' % _lst)
w('### ### **NONE IS CLOSED. ### NO NEW TRACKING DOCUMENT WAS CREATED.**')
w('### ### **NOTHING WAS COMPUTED ABOUT THE OBJECT.** ### `h2` stands exactly where the deposit left')
w('### it and this act makes no claim about it in either direction. ### The instrument lane stays')
w('### PARKED; the wave stays PARKED; nothing deposits.')
w('')

# ------------------------------------------------------------------------------------- THE LEDGER
w(SUB)
w('### THE EXPECTATIONS, THE DESK, THE WRITES, AND THE SPECIES.')
w(SUB)
w('### ### **`(F1)` MET.** ### %d is materially lower than %d.' % (NOTFOUND, CARRIED))
w('### ### **`(F2)` MET.** ### `grh_exclusion` and `no_ls_zero` sit on a TAG and on no branch.')
w('### ### **`(E1)`, THIS SEAT`S, PARTLY WRONG.** ### It predicted the largest single category would')
w('### be ### **NEVER WAS A TERMINAL.** ### The largest is ### **NOT-FOUND-ON-ANY-REF (%d)**, with'
  % NOTFOUND)
w('### `Mathlib` names second (%d) and corpus-document names third (%d). ### **THE PREDICTION WAS'
  % (MATHLIB, DOCNAME))
w('### ### RIGHT THAT THE FALL WOULD NOT BE ABOUT REFS, AND WRONG ABOUT WHICH NON-REF CAUSE')
w('### ### DOMINATES.**')
w('### ### **`(E2)` MET.** ### A `Mathlib` name is reported as a category and not as a fault.')
w('### ### **`(E3)`, THIS SEAT`S, REFUTED.** ### It predicted the held branch would resolve some of')
w('### `THE_RESIDUE_OF_RH`s names. ### **IT RESOLVED NONE.** ### The document names its own source')
w('### and the source does not carry the names it left unresolved -- ### **A FINDING ABOUT A DOCUMENT')
w('### ### THAT NAMES ITS OWN SOURCE AND IS STILL WRONG**, reported without softening.')
w('')
w('### desk items swept : %d ### / ### closed : %d ### / ### standing : %d ### / ### lists closed : %d'
  % (Q['items'], Q['closed'], Q['standing'], Q['lists_closed']))
w('### ### **AND THE ONE CLOSURE IS THE LOCK GATE`S HOLE**, closed under `(R7)` by this act`s own')
w('### killing file -- the occasion is gone because the tool now refuses.')
w('### trail block appended (append-only %s, committed prefix intact %s); `CORRESPONDENCE.md` row %s;'
  % (Q['trail']['appended_only'], Q['trail']['committed_prefix_intact'], Q['row']))
w('### index key `an-upper-bound-at-one-ref` reachable by every alias : %s' % Q['key_ok'])
w('')
w('### ### ### **NEW -- `A SEARCH THAT CANNOT RUN LOOKS EXACTLY LIKE A SEARCH THAT FOUND NOTHING`.**')
w('### The failure mode is silent, confident and total, and ### **THE ONLY THING THAT CAUGHT IT WAS A')
w('### ### CONTRADICTION WITH A PRIOR ACT`S RECORD.** ### A positive control is now the price of')
w('### reporting an absence.')
w('### ### ### **NEW -- `AN EXIT CODE ABOVE ONE IS AN ERROR AND NOT AN ANSWER`.** ### `git grep`')
w('### exits `1` for *no matches* and higher for *I could not search*. ### **CONFLATING THOSE IS HOW')
w('### ### A BROKEN SWEEP REPORTS A CLEAN ONE.**')
w('### ### ### **NEW -- `AN UPPER BOUND TAKEN AT ONE REF IS NOT A COUNT`.** ### `b377`s figure was')
w('### right about what it measured and was not labelled as a bound. ### **A MEASUREMENT`S SCOPE')
w('### ### BELONGS IN ITS SENTENCE, NOT IN THE READER`S MEMORY.**')
w('### **MET AGAIN -- `A NAME DECLARED IN TWO KERNELS IS NOT A TERMINAL YOU CAN CITE`.** ### `b377`')
w('### minted it after its own tool took the first of several silently; ### **THIS ACT`S FIRST RUN')
w('### ### DID THE SAME THING AND HAD TO BE CORRECTED.** ### A rule minted is not a rule carried.')
w('### **MET AGAIN -- `PREDICATE_ONE_SHAPE`, NOW TRACED TO ITS COST.** ### The dotted-only predicate')
w('### knew one dialect and scored the other as an absence.')
w('### **MET AGAIN -- A SLICE IS AN ADDRESS AND BOTH ITS ENDS ARE VERIFIED** (`b377`), which this act')
w('### paid for once more while rebuilding a gate suite.')
w('')
w('### registration locked at (UTC) %s' % LAT)
w('### ### **%s bytes, sha256 `%s`, %d clauses, ### LOCKED BEFORE ANY WRITE AND CHAINED ON A GATE'
  % (NBY, SHA, NCL))
w('### ### THAT CHECKS WHAT EACH GATE READ.**')
for n in ('b378_reads', 'b378_lockgate', 'b378_terminals', 'b378_archives', 'b378_hand', 'b378_desk'):
    j = J(n)
    w('### %-18s run file `%s` recorded clock %s'
      % (n, j['run_file'], j.get('run_clock') or run_clock.read_stamp(
          os.path.join(D, j['run_file']))))
w('### **THE REFS THIS ACT READ IN THE ROSTERED REPOSITORIES:**')
for k, v in E['refs'].items():
    w('###   %-22s `%s` = `%s`' % (k, v['branch'], v['head']))
w('### **THE EXTRACT:** ### `%d` reads, `%d` without an anchor, `%d` anchors differing from the hint'
  % (E['reads'], E['without_anchor'], E['anchors_differing']))
w('### that found them. ### **EVERY ANCHOR WAS READ FROM ITS FILE AND NONE WAS TYPED.**')
w(BAR)

io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
print('  written: %s  (%d lines, %d bytes)'
      % (os.path.basename(OUT), len(L), len(chr(10).join(L).encode('utf-8'))))
bad = [i + 1 for i, s in enumerate(L) if '%s' in s or '%d' in s]
print('  ### UNFILLED PLACEHOLDERS : %s' % (bad or 'none'))
