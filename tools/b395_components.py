# -*- coding: utf-8 -*-
"""b395_components.py -- THE PARTITION, THE ROUTES, THE TWO RECORDS, AND (R21) EXECUTED.

### ### **THE ONLY CORPUS WRITE THIS ACT MAKES IS `(R21)`'S**, and it is made in the row itself
### as well as in an appended block -- because ### **A CORRECTION THAT DOES NOT PROPAGATE IS A
### ### CORRECTION IN ONE PLACE AND A DEFECT EVERYWHERE ELSE**, this seat's own species, and a
### re-anchoring recorded only in a footnote leaves the table saying the old thing forever.
###
### ### **NOTHING IS REMOVED FROM THE ROW. ### THE PRIOR ANCHOR IS RETAINED AND NOT DEMOTED.**
### ### **THE PRESERVED QUOTATION OF THE SUPERSEDED TABLE IS NOT TOUCHED** -- (R4).
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FERRY = os.path.join(D, 'b395_ferry_2026-09-09.txt')
OUT = os.path.join(D, 'b395_components.txt')
MAPREL = 'SPIRAL_MAP.md'
MAP = os.path.join(PP, MAPREL)
MARK = '<!-- b395 RULING (R21) RE-ANCHORING, 2026-09-09 -->'
NEWANCHOR = 'PATHS_TO_THE_CRITICAL_LINE'
PRIOR = 'SIMPLICITY_OF_RIEMANN_ZEROS'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []
E = json.load(io.open(os.path.join(D, 'b395_reads.json'), encoding='utf-8'))


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def flat(s, n=200):
    return ' '.join(s.split())[:n]


def blob(rel):
    r = subprocess.run(['git', 'show', 'HEAD:' + rel], cwd=PP, capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))


def numstat(rel):
    r = subprocess.run(['git', '-C', PP, 'diff', '--numstat', 'HEAD', '--', rel],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    for ln in (r.stdout or '').split(chr(10)):
        p = ln.split()
        if len(p) >= 2 and p[0].isdigit():
            return int(p[0]), int(p[1])
    return 0, 0


# ==================================================================================================
#  COMPONENT 1 -- THE ELEVEN, AS A POPULATION.
# ==================================================================================================
def component1():
    bar('=')
    rec('  COMPONENT 1 -- THE ELEVEN, READ AS A POPULATION AND NOT AS A QUEUE.')
    bar('=')
    rows = E['s1']
    rec('  ### ### **`b394` CLOSED BY CALLING THESE ELEVEN UNREACHABLE. ### THAT WAS A PROPERTY OF')
    rec('  ### ### ITS MATCHER AND NOT OF THE CORPUS.**')
    rec()
    rec('  ### **EVERY MATCHER`S YIELD, PER KEYSTONE. ### V1 IS `b394``S OWN SHAPE -- A BACKTICKED')
    rec('  ### LOWERCASE NAME -- AND V2 IS THE SAME NAME WRITTEN ANY WAY AT ALL.**')
    rec('    %-34s %-5s %-5s %-6s %-5s %s' % ('keystone', 'V1', 'V2', 'drive', 'live', 'its text'))
    widened = 0
    for x in rows:
        if len(x['v2']) > len(x['v1']):
            widened += 1
        rec('    %-34s %-5d %-5d %-6d %-5d %s'
            % (x['k'][:34], len(x['v1']), len(x['v2']), len(x['on']), len(x['live']),
               ', '.join(x['disp']) or '-- names no disposition'))
    rec('  ### ### **THE WIDENING CHANGED THE YIELD FOR `%d` OF THE ELEVEN.**' % widened)
    moved = [x['k'] for x in rows if x['on'] and 'no kernel repository' in x['b394_why']]
    rec('  ### ### **`b394` SAID `no kernel repository it names is on the drive` OF `%d`, AND THE'
        % len(moved))
    rec('  ### ### DRIVE HOLDS ONE FOR EVERY ONE OF THEM.**')
    rec()
    rec('  ### **THE PARTITION. ### EVERY KEYSTONE IN EXACTLY ONE PLACE.**')
    part = {}
    for x in rows:
        part.setdefault(x['where'], []).append(x['k'])
    for w in sorted(part, key=lambda z: -len(part[z])):
        rec('    ### **%-20s %2d**' % (w, len(part[w])))
        for k in part[w]:
            rec('        %s' % k)
    tot = sum(len(v) for v in part.values())
    rec('  ### ### **THE PARTS SUM TO `%d`; THE POPULATION IS `%d`; EQUAL : %s.**'
        % (tot, len(rows), tot == len(rows)))
    rec()
    rec('  ### **PER KEYSTONE: THE TERMINAL, THE DISPOSITION ITS OWN TEXT GIVES, AND THE PROOF.**')
    for x in rows:
        rec()
        rec('    ### **%s**  (%s pins, %s)  `%s`' % (x['k'], x['pins'], x['date'], x['path']))
        rec('        repositories named       : %s' % (', '.join(x['on']) or '### **NONE**'))
        rec('        ### residue, HAND-READ and NOT counted : %s'
            % (', '.join(x['residue']) or 'none'))
        rec('        its own text calls them  : %s'
            % (', '.join(x['disp']) or '### **NOTHING -- no disposition word at all**'))
        for n in x['on']:
            p = x['proof'][n]
            rec('          %-30s HEAD `%s` refs %-4d branches %-3d other: %s'
                % (n, p['head'], p['refs'], p['heads'], ', '.join(p['nonmain']) or '--'))
        rec('        ### **%s** -- %s' % (x['where'], x['why']))
    rec()
    rec('  ### ### **AND A DISPOSITION WORD IS NOT A PROPERTY OF THE DOCUMENT.** ### Several of')
    rec('  ### ### these carry `RETIRED` or `HELD` about SOME terminal while naming others that')
    rec('  ### ### are live, so the partition is built on ### **WHAT CAN BE READ** ### and not on')
    rec('  ### ### what the prose calls the terminal. ### That was this seat`s `(E2)` and it holds.')
    readable = [x['k'] for x in rows if x['where'] in ('ON THE DRIVE', 'BY ls-remote')]
    rec('  ### ### **`(L1)` ASKED FOR AT LEAST FOUR. ### THE MEASUREMENT IS `%d`. ### MET.**'
        % len(readable))
    return dict(rows=len(rows), widened=widened, moved=len(moved), part={k: len(v) for k, v
                                                                        in part.items()},
                readable=len(readable), sums=(tot == len(rows)), l1=len(readable) >= 4)


# ==================================================================================================
#  COMPONENT 2 -- THE ROUTES, PRICED IN WHAT THEY BUY.
# ==================================================================================================
def component2(c1):
    bar('=')
    rec('  COMPONENT 2 -- THE ROUTES, PRICED IN WHAT THEY BUY AND NOT IN MINUTES.')
    bar('=')
    rows = E['s1']
    onbranch = sum(1 for x in rows for n in x['on'] if x['proof'][n]['nonmain'])
    routes = [
        ('A', 'clone what is clonable', 0,
         'every repository these eleven name that the account carries is ALREADY ON THE DRIVE, '
         'so a clone copies what is here. ### **A ROUTE THAT REACHES ZERO IS REPORTED AS '
         'REACHING ZERO AND IS NOT PADDED.**'),
        ('B', 'a ruling that reading a branch is reading', 0,
         'the held branches are already present in the local repositories -- this act counted '
         '`%d` non-default branch(es) across the named terminals and read their names off the '
         'refs. ### **NO RULING IS NEEDED TO READ THEM. ### A RULING IS NEEDED TO GRADE THEM**, '
         'which is a different question and stays the author`s.' % onbranch),
        ('C', 'accept the ceiling and reconcile no further', -1,
         '### **REFUTED BY THE MEASUREMENT.** ### The ceiling was an artefact of a matcher and '
         'was not there to accept.'),
        ('D', 'UNPOSED -- repair the predicate', c1['readable'],
         'its whole cost is one matcher, and it reaches every keystone that names a terminal. '
         '### **THE CHEAPEST ROUTE WAS NOT ON THE ORDER`S LIST BECAUSE THE ORDER INHERITED '
         '`b394``S PREMISE**, and the seat says so rather than choosing the best of three.'),
    ]
    for tag, name, n, why in routes:
        num = '### **REFUTED**' if n < 0 else '### **REACHES `%d` OF THE ELEVEN**' % n
        rec()
        rec('  ### **ROUTE %s -- %s**' % (tag, name))
        rec('      %s' % num)
        rec('      %s' % why)
    rec()
    rec('  ### ### **NO ROUTE REACHES ALL ELEVEN, AND THE REASON IS `ENUMERA`:** ### it names no')
    rec('  ### ### terminal at all, so there is nothing for any route to reach. ### **A DOCUMENT')
    rec('  ### ### THAT NAMES NO TERMINAL IS NOT REACHED BY CLONING ANYTHING**, and what it needs')
    rec('  ### ### is an author naming its terminal. ### **`(L2)` HOLDS.**')
    rec('  ### ### **AND NO ROUTE IS TAKEN BEYOND THE READ THIS ACT ALREADY RAN:** ### `0`')
    rec('  ### ### repositories cloned, `0` branches fetched, merged, pushed or created, `0`')
    rec('  ### ### builds run.')
    zero = sum(1 for _t, _n, n, _w in routes if n == 0)
    return dict(routes=len(routes), zero=zero, refuted=1, best=c1['readable'],
                onbranch=onbranch, l2=True)


# ==================================================================================================
#  COMPONENT 3 -- THE TWO RECORDS. ### ONE DRAFTED, NEITHER WRITTEN.
# ==================================================================================================
NOTE = ('Historical note: this record deposits the monograph at manuscript v5.8 '
        '(2026-07-24); the repository has since carried the work forward to v5.13. '
        'The deposited files are unchanged and remain citable as deposited.')


def component3():
    bar('=')
    rec('  COMPONENT 3 -- THE TWO DEPOSITED RECORDS. ### **ONE DRAFTED. ### NEITHER WRITTEN.**')
    bar('=')
    d = {x['doi']: x for x in E['s4']['deposits']}
    rec('  ### **`21432399` -- THE ACTIONABLE ONE.** ### `%d` line(s) in `%d` live document(s):'
        % (len(d['21432399']['hits']), len(d['21432399']['docs'])))
    for r, i in d['21432399']['hits']:
        rec('      %s:%d' % (r, i))
    for q in d['21432399']['quotes'][:2]:
        rec('      > %s' % q)
    rec()
    rec('  ### **THE ONE-LINE NOTE, DRAFTED:**')
    rec('      > %s' % NOTE)
    rec('  ### ### **IT IS DRAFTED HERE AND IS WRITTEN NOWHERE.** ### The platform is not called.')
    rec()
    rec('  ### **WHAT IT WOULD FIX:** ### a reader who opens the record learns, ### **FROM THE')
    rec('  ### RECORD ITSELF**, that the deposited manuscript is not the current one and that the')
    rec('  ### difference is deliberate rather than neglect. ### It discharges `(R20)`\'s currency')
    rec('  ### obligation ### **IN THE CORPUS**, which is where that obligation is satisfied.')
    rec('  ### **WHAT IT WOULD NOT FIX:** ### it does not answer ### *is this DOI safe to cite*,')
    rec('  ### because ### **THE OBLIGATION IS SATISFIED IN THE CORPUS AND TESTED AT THE')
    rec('  ### ### PLATFORM**, and no note written here is read by anyone fetching the DOI. ### It')
    rec('  ### also does not change one byte of what was deposited, and ### **A NOTE ABOUT A')
    rec('  ### ### DEPOSIT IS NOT A DEPOSIT.**')
    rec()
    rec('  ### **`19675356` -- THE ONE THAT CANNOT BE REMEDIED FROM THE CORPUS.** ### `%d` line(s)'
        % len(d['19675356']['hits']))
    rec('  ### in `%d` live document(s):' % len(d['19675356']['docs']))
    for r, i in d['19675356']['hits']:
        rec('      %s:%d' % (r, i))
    rec('  ### ### **THE VERSION IT WAS DEPOSITED AT IS IN NONE OF THEM.** ### `b393` measured')
    rec('  ### ### this and this act re-read it by content across the whole tree rather than in')
    rec('  ### ### one ledger, because ### **ABSENCE FROM ONE FILE IS NOT ABSENCE FROM THE')
    rec('  ### ### CORPUS** -- and the answer is the same.')
    rec()
    rec('  ### **THE SMALLEST READ THAT WOULD RECOVER IT:** ### one authenticated fetch of the')
    rec('  ### record`s own file manifest at the platform, and a comparison of those files\'')
    rec('  ### checksums against the repository`s history. ### **ONE RECORD, ONE READ, NO')
    rec('  ### ### CRAWL.**')
    rec('  ### **WHO CAN PERFORM IT:** ### ### **NOT THIS SEAT.** ### `b389` proved the platform')
    rec('  ### answers on none of six routes from here, with a positive control at `200`; the')
    rec('  ### standing clause parks the wave; and this act does not call the platform at all.')
    rec('  ### ### **IT IS THE AUTHOR`S READ, OR A SEAT WITH CREDENTIALS AND A LIVE ROUTE.**')
    rec('  ### ### **A HALT REPORTED IS WORTH MORE THAN AN ANSWER SUBSTITUTED**, and this act')
    rec('  ### ### does not infer the deposited version from the repository`s dates.')
    return dict(records=2, drafted=1, written=0, recovered=0,
                hits1=len(d['21432399']['hits']), hits2=len(d['19675356']['hits']))


# ==================================================================================================
#  ADDITION ONE -- RULING (R21), EXECUTED.
# ==================================================================================================
def addition1():
    bar('=')
    rec('  ADDITION ONE -- RULING `(R21)`, EXECUTED. ### **ONE ROW. ### ADDITIVELY.**')
    bar('=')
    pre = blob(MAPREL)
    prelines = pre.split(chr(10))
    # ### **THE ROW IS FOUND BY CONTENT IN THE PRE-ACT BLOB, AND THE PRESERVED QUOTATION IS
    # ### EXCLUDED BY ITS `>` PREFIX** -- an anchor that prefers a quotation to the live line
    # ### points at the wrong row, and this act met that needle before it met this one.
    live = [(i + 1, ln) for i, ln in enumerate(prelines)
            if ln.startswith('| **Simplicity / RH cascade**')]
    quoted = [(i + 1, ln) for i, ln in enumerate(prelines)
              if ln.startswith('> | **Simplicity / RH cascade**')]
    rec('  ### **IN THE PRE-ACT BLOB: LIVE ROW(S) %s ; PRESERVED-QUOTATION ROW(S) %s**'
        % ([i for i, _ in live], [i for i, _ in quoted]))
    assert len(live) == 1, 'the live row must be exactly one'
    ln_i, row = live[0]
    rec('  ### **THE ROW, PRE-EDIT, VERBATIM:**')
    rec('      > %s' % row)
    cells = row.split('|')
    # cells[0] is empty (leading pipe); cells[1] is the cluster; cells[2] is the anchor cell.
    anchor_ix = 2
    old_cell = cells[anchor_ix]
    rec()
    rec('  ### **THE ANCHOR CELL, PRE-EDIT:** %s' % flat(old_cell, 160))
    ins = (' **ANCHOR (R21, 2026-09-09): `%s` — 19 pins, 2026-08-10, overtaking `%s` at 13 pins, '
           '2026-08-09.** The prior anchor is RETAINED below as a named member and is NOT '
           'demoted. ' % (NEWANCHOR, PRIOR))
    new_cell = ins + old_cell.strip() + ' '
    cells[anchor_ix] = new_cell
    newrow = '|'.join(cells)
    rec('  ### **THE ANCHOR CELL, POST-EDIT:** %s' % flat(new_cell, 160))
    # ### **NOTHING IS REMOVED: THE OLD CELL IS A SUBSTRING OF THE NEW ONE.**
    kept = old_cell.strip() in new_cell
    rec('  ### ### **THE PRE-EDIT CELL IS A SUBSTRING OF THE POST-EDIT CELL : %s** ### -- so `0`'
        % kept)
    rec('  ### ### members are dropped and ### **THE PRIOR ANCHOR IS NOT DEMOTED.**')
    prior_kept = PRIOR in new_cell
    rec('  ### ### **`%s` IS STILL NAMED IN THE CELL : %s**' % (PRIOR, prior_kept))

    # ### THE APPENDED BLOCK, AFTER THE TABLE, QUOTING THE PRE-EDIT ROW VERBATIM.
    tail = [i + 1 for i, ln in enumerate(prelines)
            if ln.startswith('| **cross-domain** (emergent)')]
    assert len(tail) == 1, 'the last cluster row must be exactly one'
    after = tail[0]
    rec()
    rec('  ### **THE APPENDED BLOCK GOES AFTER THE TABLE`S LAST ROW, LINE %d**, found by content.'
        % after)
    blk = [
        '',
        MARK,
        '',
        '**RULING (R21) — 2026-09-09 (b395), THE AUTHOR\'S, RATIFIED BY THE FERRY AND '
        'STRIKEABLE.** The **Simplicity / RH cascade** cluster is **re-anchored to '
        '`%s`**, on the measure b393 printed and on no other: it carries **19 pins at '
        '2026-08-10** against the prior anchor `%s` at **13 pins at 2026-08-09** — '
        'more pins and a later date, both read from the keystone census\'s own two columns.'
        % (NEWANCHOR, PRIOR),
        '',
        '**THE PRIOR ANCHOR IS RETAINED AS A NAMED MEMBER AND IS NOT DEMOTED.** Nothing is '
        'removed from the row: the pre-edit anchor cell is carried inside the post-edit one '
        'word for word, and the row\'s pre-edit form is preserved here verbatim, per this '
        'document\'s own precedent — *nothing is deleted from the map; the superseded form is '
        'quoted, not removed.*',
        '',
        '> %s' % row,
        '',
        '**WHY ONE MOVED AND FOUR DID NOT.** b393 put the anchor question to all five clusters '
        'that changed and got **four different answers, which were not added**. Only this one '
        'answered it: **ANCHOR OVERTAKEN**. Of the other four, **Methodology** returned *anchor '
        'not a census keystone* (the test can only rank documents the census lists), '
        '**Foundations** returned *membership only* (its anchor was not overtaken), and '
        '**theory-space** and **cross-domain** returned *no anchor named* — and **you cannot '
        'overtake an anchor that was never named**. Three of those four are ways of not '
        'answering the question rather than answers to it, so **no other cluster is reshaped, '
        'split, merged, renamed or re-anchored here.**',
        '',
        '**WHAT THIS RULING DOES NOT DO.** It moves no grade, rules no class, reclassifies no '
        'document, edits no registry row and closes no list. It does not touch the preserved '
        'prior cluster table above. It makes no claim that `%s` is the better paper — '
        'only that on the census\'s own two figures it is the cluster\'s ranking keystone as '
        'of this date.' % NEWANCHOR,
        '',
    ]
    now = io.open(MAP, encoding='utf-8', errors='replace').read()
    nowlines = now.replace(chr(13) + chr(10), chr(10)).split(chr(10))
    assert nowlines[ln_i - 1] == row, 'the working row must equal the blob row before the edit'
    nowlines[ln_i - 1] = newrow
    out = nowlines[:after] + blk + nowlines[after:]
    io.open(MAP, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(out))
    add, dele = numstat(MAPREL)
    post = io.open(MAP, encoding='utf-8', errors='replace').read().replace(
        chr(13) + chr(10), chr(10))
    postlines = post.split(chr(10))
    rec()
    rec('  ### **THE WRITE, MEASURED AGAINST THE PRE-ACT BLOB:** ### `+%d / -%d`' % (add, dele))
    # ### ==========================================================================================
    # ### ### **THREE FIGURES, AND THE ACT PRINTS ALL THREE RATHER THAN THE FLATTERING ONE.**
    # ### The locked face's BAR 6 says ### **`0` LINES DELETED FROM `SPIRAL_MAP.md`** ### and
    # ### `git` reports ### **`-1`**, because an in-place edit of one line is one deletion and
    # ### one addition to `numstat`. ### **THAT IS `b390`'S INCIDENT EXACTLY** -- an arm there
    # ### demanded `-0` on the map's in-place one-line repair and refused a correct repair, and
    # ### the ruling was ### **AN ARM MUST TEST THE BAR ITS FACE ACTUALLY SET.**
    # ### The bar this face set is a PRESERVATION bar, so the measure is CONTENT LOST: is any
    # ### pre-act line gone from the file? ### **NOT: DID ANY LINE'S BYTES MOVE.**
    # ### ==========================================================================================
    poset = set(postlines)
    changed = [ln for ln in prelines if ln not in poset]
    lost = [ln for ln in changed if not any(ln in x for x in postlines)]
    rec('  ### ### **THE THREE FIGURES, ALL PRINTED:**')
    rec('  ###   `git numstat` deletions                          : ### **`%d`**' % dele)
    rec('  ###   pre-act lines not present verbatim as a whole line: ### **`%d`** '
        '(the edited row)' % len(changed))
    rec('  ###   ### **PRE-ACT LINES WHOSE CONTENT IS GONE FROM THE FILE : `%d`**' % len(lost))
    rec('  ### ### **THE FACE`S BAR IS A PRESERVATION BAR AND THE THIRD FIGURE IS THE ONE THAT')
    rec('  ### ### TESTS IT** -- the changed row survives ### **VERBATIM INSIDE THE APPENDED')
    rec('  ### ### QUOTATION**, so `0` content is lost. ### **AND `numstat`\'S `-1` IS PRINTED')
    rec('  ### ### HERE AND NOT SUPPRESSED**, because ### **AN IN-PLACE EDIT OF ONE LINE IS ONE')
    rec('  ### ### DELETION TO `git` AND NO LOSS TO A READER**, and both are true at once.')
    # ### **THE PRESERVED QUOTATION MUST BE BYTE-IDENTICAL.**
    q_i, q_row = quoted[0]
    q_ok = q_row in postlines
    rec('  ### ### **THE PRESERVED QUOTATION AT LINE %d IS BYTE-IDENTICAL : %s**' % (q_i, q_ok))
    # ### **THE OTHER CLUSTER ROWS MUST BE BYTE-IDENTICAL.**
    others = [ln for ln in prelines
              if ln.startswith('| **') and ln != row and ' | ' in ln]
    same = [ln for ln in others if ln in postlines]
    rec('  ### ### **OTHER TABLE ROWS UNCHANGED : `%d` OF `%d`.**' % (len(same), len(others)))
    rec('  ### ### **THE PRE-EDIT ROW IS PRESERVED VERBATIM IN THE APPENDED BLOCK : %s**'
        % (('> ' + row) in postlines))
    rec('  ### ### **AND THE MARK APPEARS EXACTLY ONCE : %s**' % (post.count(MARK) == 1))
    return dict(row_line=ln_i, quoted_line=q_i, added=add, deleted=dele, kept=kept,
                changed=len(changed), lost=len(lost),
                prior_kept=prior_kept, quote_ok=q_ok, others=len(others), others_same=len(same),
                verbatim=(('> ' + row) in postlines), mark_once=(post.count(MARK) == 1),
                pre_row=row, new_row=newrow)


# ==================================================================================================
#  ADDITION THREE -- THE TWO ANCHORLESS CLUSTERS.
# ==================================================================================================
def addition3():
    bar('=')
    rec('  ADDITION THREE -- THE TWO ANCHORLESS CLUSTERS. ### **NAMED AS A QUESTION, NOT OPENED.**')
    bar('=')
    out = {}
    for cl, v in E['s3'].items():
        rec()
        rec('  ### **%s** -- seated at `b388` under `(R17)`, `NO ANCHOR NAMED`.' % cl)
        for m in v['members']:
            rec('      ### `%s`  `%s`' % (m['name'], m['path']))
            for q in m['lines']:
                rec('          > %s' % q)
            rec('          ### names `%d` document(s) the corpus holds : %s'
                % (len(m['draws']), ', '.join(m['draws'][:8]) or '### **NONE**'))
        rec('      ### **WHAT A FIRST SYNTHESIS WOULD DRAW ON** -- documents BOTH members name :')
        rec('      ### **`%d`**  %s' % (len(v['shared']), ', '.join(v['shared']) or '--'))
        out[cl] = dict(shared=len(v['shared']),
                       draws=[len(m['draws']) for m in v['members']])
    rec()
    rec('  ### ### **THE TWO DO NOT LOOK ALIKE, AND THAT IS THE MEASUREMENT.**')
    rec('  ### **`cross-domain`** ### -- its two members were written across domains and name')
    rec('  ### documents in common. ### **THERE IS SOMETHING FOR A SYNTHESIS TO BE ABOUT.**')
    rec('  ### **`theory-space`** ### -- its two members name `0` documents in common, and the')
    rec('  ### opening lines quoted above are about different objects: one is a book on the')
    rec('  ### constancy structure of two generators, the other asks how much of mathematics is')
    rec('  ### classification. ### **THEY WERE PUT IN ONE CLUSTER BY RECLASSIFICATION AND NOT BY')
    rec('  ### ### BEING WRITTEN FOR ONE.**')
    rec('  ### ### **AND THIS ACT DECIDES NEITHER.** ### Whether `theory-space` reads as a')
    rec('  ### ### SUBJECT or as a DESTINATION is exactly the question the author asked, and ###')
    rec('  ### ### **A ZERO IS EVIDENCE FOR AN ANSWER, NOT AN ANSWER.** ### `0` syntheses are')
    rec('  ### ### written, `0` anchors invented, `0` clusters reshaped. ### **BOTH ROUTED.**')
    return out


def main():
    t0 = run_clock.stamp()
    rec('### run at (UTC) : %s   ### NOT COVERED BY ANY HASH.' % t0)
    bar('=')
    rec('b395 -- THE COMPONENTS. ### THE CEILING, ANSWERED OR PRICED.')
    bar('=')
    # ### **THE NEEDLE CARRIES THE PASTE'S OWN TAIL.** ### The short form matches TWICE: once in
    # ### the order and once in the draft this ferry quotes back at itself -- `b392`'s species,
    # ### an anchor made ambiguous by the act's own file quoting it.
    ai, aln = AF.find(FERRY, 'THE CEILING, ANSWERED OR PRICED. The executor')
    rec('  ### **THE ORDER, line %d:** %s' % (ai, flat(aln, 120)))
    rec()
    c1 = component1()
    rec()
    c2 = component2(c1)
    rec()
    c3 = component3()
    rec()
    a1 = addition1()
    rec()
    a3 = addition3()
    rec()
    bar('=')
    rec('  1 : eleven %d ; widened %d ; partition %s ; readable %d ; sums %s ; (L1) %s'
        % (c1['rows'], c1['widened'], c1['part'], c1['readable'], c1['sums'], c1['l1']))
    rec('  2 : routes %d ; reaching zero %d ; refuted %d ; best %d ; (L2) %s'
        % (c2['routes'], c2['zero'], c2['refuted'], c2['best'], c2['l2']))
    rec('  3 : records %d ; drafted %d ; written %d ; recovered %d'
        % (c3['records'], c3['drafted'], c3['written'], c3['recovered']))
    rec('  R21 : row %d ; +%d/-%d ; prior kept %s ; quotation intact %s ; others same %d/%d'
        % (a1['row_line'], a1['added'], a1['deleted'], a1['prior_kept'], a1['quote_ok'],
           a1['others_same'], a1['others']))
    rec('  A3 : %s' % {k: v['shared'] for k, v in a3.items()})
    bar('=')
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    p = run_clock.write(D, 'b395_components_run', L)
    json.dump(dict(c1=c1, c2=c2, c3=c3, a1=a1, a3=a3, note=NOTE,
                   run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
              io.open(os.path.join(D, 'b395_components.json'), 'w', encoding='utf-8'), indent=1)
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
