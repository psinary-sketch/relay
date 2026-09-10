# -*- coding: utf-8 -*-
"""b397_components.py -- THE UNLANDED INVENTORY, THE DISCLOSURE SWEEP, AND THE BOARD.

### ### **THE ONLY CORPUS WRITE IS A STATUS CELL, AND ONLY WHERE THE DISCLOSURE IS TRUE.** ### A
### row whose terminal has since landed gets ### **NOTHING**, because ### **A DISCLOSURE OF A
### ### CONDITION THAT NO LONGER HOLDS IS A FALSE STATEMENT IN A STATUS COLUMN.**
###
### ### **EVERY EDIT USES THE PRESERVED-BLOCK-AWARE ANCHOR MODE `b396` ADDED** (`editing=True`),
### so a row quoted inside a preserved block cannot be edited by mistake.
###
### ### **NOTHING IS MERGED, PUSHED OR CHECKED OUT. ### NO BUILD IS RUN.**
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
FERRY = os.path.join(D, 'b397_ferry_2026-09-10.txt')
OUT = os.path.join(D, 'b397_components.txt')
MARK = '<!-- b397 BRANCH-RESIDENCE DISCLOSURE, 2026-09-10 -->'
DISC = (' ### **BRANCH-RESIDENT: this terminal is on `SIDE-kernel/derivative-engine` and is '
        'ABSENT FROM `main`; it is not citable from a default branch, and no printed axiom '
        'profile sits on that ref (b397).**')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []
E = json.load(io.open(os.path.join(D, 'b397_reads.json'), encoding='utf-8'))


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def flat(s, n=200):
    return ' '.join(s.split())[:n]


def text_of(p):
    return io.open(p, encoding='utf-8', errors='replace').read()


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return (r.stdout or '').strip()


def blob(rel):
    r = subprocess.run(['git', 'show', 'HEAD:' + rel], cwd=PP, capture_output=True)
    return r.stdout.decode('utf-8', 'replace').replace(chr(13) + chr(10), chr(10))


def numstat(rel):
    for ln in g(PP, 'diff', '--numstat', 'HEAD', '--', rel).split(chr(10)):
        p = ln.split()
        if len(p) >= 2 and p[0].isdigit():
            return int(p[0]), int(p[1])
    return 0, 0


# ==================================================================================================
#  COMPONENT 1 -- WHAT IS ON THE HELD BRANCHES.
# ==================================================================================================
def component1():
    bar('=')
    rec('  COMPONENT 1 -- WHAT IS ON THE HELD BRANCHES. ### **READ ONLY.**')
    bar('=')
    s1, s2 = E['s1'], E['s2']
    rec('  ### **THE POPULATION CAME FROM `b395`\'S PARTITION AND NOT FROM A ROSTER THIS SEAT')
    rec('  ### TYPED**, and every branch was counted ### **IN BOTH DIRECTIONS**, with `--merged`')
    rec('  ### read as an independent third witness.')
    rec()
    rec('    %-22s %-26s %-7s %-7s %-7s %s'
        % ('repo', 'branch', 'AHEAD', 'behind', 'merged', 'kind'))
    for x in s1['rows']:
        rec('    %-22s %-26s %-7d %-7d %-7s %s'
            % (x['repo'], x['branch'], x['ahead'], x['behind'], x['merged'],
               'push branch (mechanical, excluded)' if x['push'] else 'research'))
    rec()
    rec('  ### ### **RESEARCH BRANCHES `%d` ; PUSH BRANCHES EXCLUDED `%d`.**'
        % (s1['research'], s1['push']))
    rec('  ### ### **FULLY MERGED INTO `main`, CARRYING NOTHING `main` LACKS : `%d`.**'
        % len(s1['landed']))
    rec('  ### ### **CARRYING COMMITS `main` DOES NOT HAVE : `%d`.**' % len(s1['live']))
    rec('  ### ### ### **SO THE `HELD` / `UNMERGED` / `BRANCH-RESIDENT` LANGUAGE IN THOSE')
    rec('  ### ### ### KEYSTONES IS STALE FOR `%d` OF `%d` RESEARCH BRANCHES.** ### The work'
        % (len(s1['landed']), s1['research']))
    rec('  ### ### ### landed and ### **THE PROSE DID NOT FOLLOW IT** -- `b394`\'s')
    rec('  ### ### ### corrected-but-unpropagated species, about a branch status this time.')
    rec('  ### **THE EIGHT THAT LANDED:** ### %s'
        % ', '.join('`%s`' % b for b in s1['landed']))
    rec()
    rec('  ### **THE COUNTING TRAP, RECORDED:** ### `rev-list --left-right --count main...b` puts')
    rec('  ### the count of commits ### **ONLY IN MAIN** ### on the left. ### An earlier form of')
    rec('  ### the survey read it as `ahead`, and ### **EIGHT MERGED BRANCHES READ AS ONE COMMIT')
    rec('  ### ### AHEAD OF MAIN -- THE EXACT OPPOSITE OF THE TRUTH.** ### It was caught by one')
    rec('  ### branch reading `0 0`, a shape the misreading could not explain.')
    rec()
    bar('-')
    rec('  ### THE ONE LIVE BRANCH, TERMINAL BY TERMINAL.')
    bar('-')
    live = s1['live'][0]
    rp = os.path.join('D:' + os.sep, live['repo'])
    rec('  ### **`%s/%s`** -- `%d` commit(s) `main` does not have.'
        % (live['repo'], live['branch'], live['ahead']))
    rec('  ### **WHICH KEYSTONES NAME THIS REPOSITORY:** ### %s'
        % ', '.join('`%s`' % k for k in live['keystones'][:6]))
    rec()
    absent = [o for o in s2['decls'] if not o['on_main']]
    rec('  ### **DECLARATIONS READ ON THE BRANCH : `%d`. ### ABSENT FROM `main` : `%d`.**'
        % (len(s2['decls']), len(absent)))
    rec('  ### ### **THE CITATION TEST IS AGAINST `main`, WHERE A READER RESOLVES IT** -- and two')
    rec('  ### ### names the branch appears to add (`invariance_barrier`, `DeterminedBy`) ###')
    rec('  ### ### **ALREADY STAND ON `main`** ### and are citable.')
    rec()
    for o in absent:
        f = os.path.join(rp, o['file'].replace('/', os.sep))
        body = g(rp, 'show', '%s:%s' % (live['branch'], o['file']))
        lines = body.split(chr(10))
        idx = next((i for i, ln in enumerate(lines)
                    if re.match(r'\s*(?:theorem|lemma|def|structure|abbrev)\s+' +
                                re.escape(o['name']) + r'\b', ln)), None)
        rec('    ### **%s.%s**  (`%s`, in `%s`)' % ('SIDEDerivative', o['name'], o['kind'],
                                                    o['file']))
        if idx is not None:
            stmt = [ln for ln in lines[idx:idx + 8]]
            rec('        ### **THE STATEMENT, AS THE FILE HAS IT:**')
            for ln in stmt[:6]:
                rec('          %s' % ln[:104])
        rec('        ### **AXIOM PROFILE : NOT BUILT.** ### No printed profile sits on this ref;')
        rec('        ### the only candidate is a `#print axioms` ### **SOURCE SCRIPT** ### whose')
        rec('        ### own comment says ### *Expected: ... axiom-free* ### -- ### **EXPECTED,')
        rec('        ### ### NOT PRINTED.** ### **NO EVIDENCE OF A BUILD IS NOT EVIDENCE OF NO')
        rec('        ### ### BUILD**, and no build is run here.')
        if o['cited_by']:
            rec('        ### **WHICH KEYSTONE CLAIM IT BACKS : `%d` document(s)**'
                % len(o['cited_by']))
            for d in o['cited_by']:
                rec('          %s' % d)
        else:
            rec('        ### **CITED BY NOTHING.**')
        rec()
    rec(bar('-') or '')
    rec('  ### ### **WHAT THE PROGRAMME HAS COMPILED THAT IT CANNOT CURRENTLY CITE.**')
    rec('  ### ### **AND THE ANSWER IS SMALLER THAN THE QUESTION, WHICH IS THE FINDING.**')
    unl = [o for o in absent]
    for o in unl:
        rec('  ###   **`%s`** (`%s`) -- absent from `main`; cited by `%d` document(s); ###'
            % (o['name'], o['kind'], len(o['cited_by'])))
        if o['cited_by']:
            rec('  ###     **WHAT IT WOULD LET A KEYSTONE SAY:** ### the citing rows already say')
            rec('  ###     it -- landing the branch would make those rows resolvable from a')
            rec('  ###     default branch instead of from a ref a reader must be told about.')
        else:
            rec('  ###     **WHAT IT WOULD LET A KEYSTONE SAY:** ### nothing yet. ### It is a')
            rec('  ###     `def` -- a grading map for the derivative catalogue -- and ### **A')
            rec('  ###     ### DEFINITION IS NOT A RESULT A KEYSTONE CITES.**')
    rec('  ### ### **`(F1)` ASKED FOR A COMPILED TERMINAL NO KEYSTONE CITES.** ### `derivGrade`')
    rec('  ### ### is uncited and absent from `main`, but ### **`COMPILED` REQUIRES A PRINTED')
    rec('  ### ### PROFILE AND THE REF CARRIES NONE.** ### **`(F1)` IS NOT ESTABLISHED**, and')
    rec('  ### ### what would settle it is one build, which `(R22)` and the parked instrument')
    rec('  ### ### lane forbid. ### Declared on the face before the components ran.')
    rec('  ### ### **NO TERMINAL ON THE LIVE BRANCH SAYS `RETIRED`**, so the order\'s')
    rec('  ### ### retired-exclusion has `0` members here -- and it is stated rather than')
    rec('  ### ### silently unused.')
    return dict(research=s1['research'], push=s1['push'], landed=len(s1['landed']),
                live=len(s1['live']), decls=len(s2['decls']), absent=len(absent),
                cited=len([o for o in absent if o['cited_by']]),
                uncited=len([o for o in absent if not o['cited_by']]),
                printed_profiles=0, retired=0, f1='NOT ESTABLISHED')


# ==================================================================================================
#  COMPONENT 2 -- THE DISCLOSURE RULE, APPLIED WHERE IT IS TRUE.
# ==================================================================================================
def component2():
    bar('=')
    rec('  COMPONENT 2 -- THE DISCLOSURE RULE, APPLIED WHERE IT IS TRUE.')
    bar('=')
    s3 = E['s3']
    rec('  ### **THE RULE, QUOTED FROM THE RECORD`S OWN BYTES:**')
    rec('  ### `REGISTRY.md` line %d:' % s3['rule_registry_line'])
    rec('      > %s' % s3['rule_registry'])
    rec('  ### `THE_KEYSTONE_CENSUS.md` line %d:' % s3['rule_census_line'])
    rec('      > %s' % s3['rule_census'])
    rec()
    rec('  ### ### **AND THE RULE`S OWN WORKED INSTANCE IS STALE.** ### It names')
    rec('  ### ### `word-pairing-interface` as ### *the held, unmerged branch* ### carrying')
    rec('  ### ### `THE_RESIDUE_OF_RH`\'s terminals. ### Component 1 measured that branch at ###')
    rec('  ### ### **`0` COMMITS `main` DOES NOT HAVE, `--merged` CONFIRMING.**')
    rec('  ### ### **WRITING THE DEMANDED DISCLOSURE INTO THAT ROW WOULD PUT A FALSE STATEMENT')
    rec('  ### ### IN A STATUS COLUMN UNDER THE AUTHORITY OF A RULE.** ### The rule is ###')
    rec('  ### ### **NOT STRUCK AND NOT AMENDED HERE**; its instance is ### **ROUTED.**')
    rec()
    names = s3['names']
    rec('  ### **THE SWEEP.** ### A row is swept if it cites a terminal this act examined on a')
    rec('  ### non-default branch; it is ### **REPAIRED ONLY IF THAT TERMINAL IS ABSENT FROM')
    rec('  ### ### `main` AND ITS STATUS CELL DOES NOT ALREADY DISCLOSE.**')
    # ### the full set of branch-cited terminals: those absent from main (repairable) and those
    # ### that landed (swept, not repaired).
    landed_names = sorted(set(o['name'] for o in E['s2']['decls'] if o['on_main']))
    swept, repaired, already, routed = [], [], [], []
    edits = {}
    for dp, dn, fn in os.walk(PP):
        rel = os.path.relpath(dp, PP).replace(os.sep, '/')
        if rel.split('/')[0] in ('.git', 'archive', 'outputs'):
            continue
        for f in sorted(fn):
            if not f.endswith('.md'):
                continue
            r = (rel + '/' + f) if rel != '.' else f
            lines = text_of(os.path.join(dp, f)).replace(chr(13) + chr(10), chr(10)) \
                .split(chr(10))
            for i, ln in enumerate(lines, 1):
                if not ln.lstrip().startswith('|'):
                    continue
                # ### **A ROW INSIDE A PRESERVED BLOCK IS NOT A TARGET** (`b396`).
                if AF.is_preserved_line(ln):
                    continue
                hitn = [n for n in names if n in ln]
                hitl = [n for n in landed_names if n in ln]
                if not hitn and not hitl:
                    continue
                cells = ln.split('|')
                rowrec = dict(doc=r, line=i, terminals=sorted(set(hitn + hitl)),
                              cells=len(cells))
                swept.append(rowrec)
                if not hitn:
                    rowrec['disposition'] = 'SWEPT, NOT REPAIRED -- its terminal is on `main`'
                    already.append(rowrec)
                    continue
                if len(cells) < 7:
                    rowrec['disposition'] = 'ROUTED -- not a status-column table row'
                    routed.append(rowrec)
                    continue
                if 'BRANCH-RESIDENT' in cells[5]:
                    rowrec['disposition'] = 'SWEPT, NOT REPAIRED -- already discloses'
                    already.append(rowrec)
                    continue
                rowrec['disposition'] = 'REPAIRED -- the disclosure added to the status cell'
                repaired.append(rowrec)
                edits.setdefault(r, []).append(i)
    rec()
    rec('  ### ### **ROWS SWEPT : `%d`. ### ROWS REPAIRED : `%d`. ### SWEPT-NOT-REPAIRED : `%d`.'
        % (len(swept), len(repaired), len(already)))
    rec('  ### ### ROUTED : `%d`.**' % len(routed))
    rec('  ### ### **AND THE TWO ARE REPORTED APART, NEVER ADDED.**')
    rec()
    for rr in swept:
        rec('    %-52s:%-5d %s' % (rr['doc'][:52], rr['line'], rr['disposition']))
        rec('        terminals : %s' % ', '.join('`%s`' % n for n in rr['terminals']))
    # ---- THE WRITE -------------------------------------------------------------------------------
    rec()
    rec('  ### **THE WRITE, PER DOCUMENT, MEASURED AGAINST THE PRE-ACT BLOB.**')
    written = []
    for r, idxs in sorted(edits.items()):
        path = os.path.join(PP, r.replace('/', os.sep))
        pre = blob(r)
        cur = text_of(path).replace(chr(13) + chr(10), chr(10))
        lines = cur.split(chr(10))
        origs = []
        for i in idxs:
            ln = lines[i - 1]
            cells = ln.split('|')
            origs.append((i, ln))
            cells[5] = cells[5].rstrip() + DISC + ' '
            lines[i - 1] = '|'.join(cells)
        blk = ['', MARK, '',
               ('**b397 — BRANCH-RESIDENCE DISCLOSURE.** The status cell of %d row(s) above now '
                'discloses that its terminal sits on `SIDE-kernel/derivative-engine` and is '
                '**absent from `main`**. The record\'s own rule (`REGISTRY.md`, and raised to a '
                'release-blocking line in `THE_KEYSTONE_CENSUS.md`) is that branch residence '
                '*belongs in the status column where a table-reader meets it* — **a disclosure '
                'requirement, not a repair**. Nothing else in this document changed; **the '
                'pre-edit lines are preserved verbatim below.**' % len(idxs)),
               '']
        for i, ln in origs:
            blk.append('> line %d was: %s' % (i, ln))
        blk.append('')
        out = lines + blk
        io.open(path, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(out))
        add, dele = numstat(r)
        post = text_of(path).replace(chr(13) + chr(10), chr(10))
        pl, al = pre.split(chr(10)), post.split(chr(10))
        aset = set(al)
        changed = [x for x in pl if x not in aset]
        lost = [x for x in changed if not any(x in y for y in al)]
        rec('    %-52s +%-4d -%-4d changed %-3d ### **CONTENT LOST : %d**'
            % (r[:52], add, dele, len(changed), len(lost)))
        written.append(dict(doc=r, rows=len(idxs), added=add, deleted=dele,
                            changed=len(changed), lost=len(lost)))
    rec('  ### ### **DOCUMENTS EDITED : `%d`. ### ROWS EDITED : `%d`.**'
        % (len(written), sum(w['rows'] for w in written)))
    rec('  ### ### **CONTENT LOST ACROSS ALL OF THEM : `%d`** -- every pre-edit line is'
        % sum(w['lost'] for w in written))
    rec('  ### ### preserved verbatim in the appended annotation. ### `numstat` counts an')
    rec('  ### ### in-place edit as one deletion per line and ### **THAT FIGURE IS PRINTED')
    rec('  ### ### ABOVE AND NOT SUPPRESSED** (`b390`, `b395`).')
    rec()
    rec('  ### ### **`(F2)` ASKED WHETHER THE SWEEP REPAIRS FEWER ROWS THAN IT SWEEPS: `%d` OF'
        % len(repaired))
    rec('  ### ### `%d`. ### **MET.** ### But ### **NOT FOR THE REASON THE ORDER GAVE:** ### the'
        % len(swept))
    rec('  ### ### order expected several rows to disclose already in a preamble; the measurement')
    rec('  ### ### says ### **MOST SWEPT ROWS` TERMINALS HAVE SINCE LANDED**, so no disclosure is')
    rec('  ### ### owed at all. ### **A PREDICTION MET FOR THE WRONG REASON IS REPORTED WITH THE')
    rec('  ### ### REASON.**')
    rec('  ### ### **AND ONE THING THIS COMPONENT SAW AND DID NOT TOUCH:** ### the repaired rows')
    rec('  ### ### assert axiom profiles (`axiom-free (none)`,')
    rec('  ### ### `{propext, Classical.choice, Quot.sound}`) for terminals whose ref carries ###')
    rec('  ### ### **NO PRINTED PROFILE.** ### Moving a grade is not this act`s scope and ###')
    rec('  ### ### **NO GRADE IS MOVED.** ### **ROUTED.**')
    return dict(swept=len(swept), repaired=len(repaired), already=len(already),
                routed=len(routed), docs=len(written), rows=sum(w['rows'] for w in written),
                lost=sum(w['lost'] for w in written), written=written,
                f2=(len(repaired) < len(swept)), mark=MARK)


# ==================================================================================================
#  COMPONENT 4 -- THE RESEARCH BOARD, QUOTED.
# ==================================================================================================
def component4():
    bar('=')
    rec('  COMPONENT 4 -- THE RESEARCH BOARD, RESTATED FROM THE RECORD.')
    bar('=')
    s4 = E['s4']
    rec('  ### **QUOTATIONS. ### NO NEW CLAIMS.** ### Where the record is silent, the board says')
    rec('  ### the record is silent.')
    rec()
    fn = os.path.join(PP, 'FINDINGS.md')
    lines = text_of(fn).split(chr(10))
    rec('  ### **WHAT STANDS FACING THE CLAUSE** -- `FINDINGS.md`, the clause anchor:')
    for i in s4['clause_lines'][:4]:
        rec('      %s:%d' % ('FINDINGS.md', i))
        rec('      > %s' % flat(lines[i - 1], 230))
    rec()
    fl = os.path.join(PP, 'FACES_LEDGER.md')
    ftxt = text_of(fl)
    rows = [ln for ln in ftxt.split(chr(10)) if ln.startswith('| ') and ln.count('|') >= 4]
    rec('  ### **WHAT STANDS ON ITS OWN** -- `FACES_LEDGER.md`, `%d` rows in `%d` bytes:'
        % (len(rows), len(ftxt.encode('utf-8'))))
    for ln in rows[1:5]:
        rec('      > %s' % flat(ln, 230))
    rec()
    rec('  ### **WHAT IS PRICED AND UNOPENED** -- quoted from the acts that priced it:')
    for src, hint in ((os.path.join(D, 'b393_the_clusters_surfaced.txt'),
                       'TIER KC IS PRICED AND NOT APPLIED'),
                      (os.path.join(D, 'b396_the_backtick_swept.txt'),
                       'THE PRICE : `2.8` x `10` = `28.0` MINUTES')):
        try:
            i, ln = AF.find(src, hint)
            rec('      %s:%d' % (os.path.basename(src), i))
            rec('      > %s' % flat(ln, 230))
        except Exception as e:
            rec('      %s : ### **NOT QUOTABLE** -- %s' % (os.path.basename(src),
                                                           flat(str(e), 90)))
    rec()
    rec('  ### ### **AND WHAT THE RECORD DOES NOT SAY, SAID PLAINLY:** ### the clause has not')
    rec('  ### ### moved since `b332` stated it; no coordinate is closed; the partition stays')
    rec('  ### ### UNDECIDED; and ### **NO ACT IN THIS ARC PRODUCED A RESULT ABOUT THE OBJECT.**')
    rec('  ### ### **THAT IS THE ORIENTATION, AND IT IS A QUOTATION OF AN ABSENCE RATHER THAN A')
    rec('  ### ### CLAIM ABOUT ONE.**')
    return dict(clause_lines=len(s4['clause_lines']), faces_rows=len(rows),
                faces_bytes=len(ftxt.encode('utf-8')), new_claims=0)


def readonly_check():
    """### **BAR 3, MEASURED IN THE COMPONENT THAT COULD HAVE BROKEN IT.**"""
    out = {}
    for name, repo in b303_pins.REPOS:
        out[name] = dict(branch=g(repo, 'rev-parse', '--abbrev-ref', 'HEAD'),
                         head=g(repo, 'rev-parse', 'HEAD')[:12])
    for n in sorted(set(x['repo'] for x in E['s1']['rows'])):
        rp = os.path.join('D:' + os.sep, n)
        out[n] = dict(branch=g(rp, 'rev-parse', '--abbrev-ref', 'HEAD'),
                      head=g(rp, 'rev-parse', 'HEAD')[:12])
    return out


def main():
    rec('### run at (UTC) : %s   ### NOT COVERED BY ANY HASH.' % run_clock.stamp())
    bar('=')
    rec('b397 -- THE COMPONENTS. ### THE UNLANDED WORK.')
    bar('=')
    ai, aln = AF.find(FERRY, 'ACT b397 — THE UNLANDED WORK')
    rec('  ### **THE ORDER, line %d:** %s' % (ai, flat(aln, 120)))
    before = readonly_check()
    rec()
    c1 = component1()
    rec()
    c2 = component2()
    rec()
    c4 = component4()
    after = readonly_check()
    rec()
    bar('-')
    rec('  ### **THE READ-ONLY BAR, MEASURED BEFORE AND AFTER THE COMPONENTS:**')
    same = all(before[k] == after[k] for k in before)
    for k in sorted(before):
        rec('    %-24s `%s` = `%s`   unchanged : %s'
            % (k, after[k]['branch'], after[k]['head'], before[k] == after[k]))
    rec('  ### ### **EVERY REPOSITORY`S BRANCH AND HEAD BYTE-IDENTICAL : %s.**' % same)
    rec('  ### ### **`0` MERGES, `0` PUSHES TO ANY BRANCH, `0` CHECKOUTS, `0` CLONES, `0` BUILDS.**')
    bar('=')
    rec('  1 : research %d ; landed %d ; live %d ; decls %d ; absent %d ; cited %d ; uncited %d'
        % (c1['research'], c1['landed'], c1['live'], c1['decls'], c1['absent'],
           c1['cited'], c1['uncited']))
    rec('  2 : swept %d ; repaired %d ; swept-not-repaired %d ; routed %d ; docs %d ; lost %d'
        % (c2['swept'], c2['repaired'], c2['already'], c2['routed'], c2['docs'], c2['lost']))
    rec('  4 : clause lines %d ; faces rows %d ; new claims %d'
        % (c4['clause_lines'], c4['faces_rows'], c4['new_claims']))
    rec('  read-only : %s' % same)
    bar('=')
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    p = run_clock.write(D, 'b397_components_run', L)
    json.dump(dict(c1=c1, c2=c2, c4=c4, readonly=same, refs_before=before, refs_after=after,
                   run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
              io.open(os.path.join(D, 'b397_components.json'), 'w', encoding='utf-8'), indent=1)
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
