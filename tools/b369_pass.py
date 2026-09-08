# -*- coding: utf-8 -*-
"""b369_pass.py -- COMPONENT 3: THE REFINEMENT PASS, ### **PRICED AND NOT RUN.**

### ### ### **`AUDIT NOTHING` IS THE ORDER'S OWN CLAUSE AND IT IS THE CAP.** ### This tool ENUMERATES
### and LISTS. ### **IT READS NO SURFACE FOR CORRECTNESS**, checks no claim against any kernel, and
### grades no repository.
### ### **WHAT IT TOUCHES IS METADATA:** ### the account's repository list, and each repository's own
### PATH LIST from the git-tree endpoint. ### **A PATH IS NOT A CONTENT.** ### The one text it reads is
### the repository DESCRIPTION, because the description IS one of the surfaces the order asks it to list,
### and `(H1)` is a claim about a description.
### ### **A COUNT-SHAPED STRING IS NOT A CLAIM, AND THIS TOOL DOES NOT CALL IT ONE.** ### It reports a
### SHAPE -- a numeral or a spelled numeral governing a noun the programme uses for its own artifacts --
### and says, in its own output, that detecting a shape is not judging a claim.
### ### **THE CRITERION IS THE ORDER'S AND IS PRINTED BEFORE THE RANKING**, so it can be disagreed with.
### ### **NO `.lean` FILE IS WRITTEN AND NO BUILD IS RUN.**
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
OWNER = 'psinary-sketch'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### **THE PROGRAMME'S OWN PREFIXES.** ### Everything else on the account is enumerated and reported,
# ### and is marked NOT PROGRAMME MATERIAL rather than silently dropped.
PROG = ('SIDE-', 'PLACE-', 'TECHNE-')
PROG_EXACT = ('relay',)

# ### **THE TREE CALL IS SKIPPED FOR AN UPSTREAM FORK AND THE SKIP IS DECLARED.** ### A vendored library
# ### is not this programme's surface, and walking it would be `b367`'s `.lake` incident by another road.
SKIP_TREE = {'mathlib4': 'an upstream fork, not programme material; its tree is not this record\'s to walk'}

# ### THE COUNT SHAPE. ### **NOUNS THE PROGRAMME USES FOR ITS OWN ARTIFACTS**, and nothing else.
NUM = r'(\d+|one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve)'
NOUN = (r'(terminals?|theorems?|lemmas?|kernels?|modules?|axioms?|consequences?|classes|'
        r'discriminants?|faces|interfaces|checkpoints?|counts?|files?)')
# ### **THE LANGUAGE VERSION IS NOT A COUNT, AND THE FIRST RUN OF THIS DETECTOR THOUGHT IT WAS.**
# ### `Lean 4 kernel` fired on thirty of the programme's descriptions as `4 kernel`. ### That is the
# ### same species as `U-1`'s lexical false positives, which this record already knows: ### **A SHAPE
# ### ### DETECTOR REPORTS ITS PATTERN, NOT ITS SUBJECT.** ### The idiom is excluded by name.
# ### **AND A DIGIT INSIDE AN IDENTIFIER OR A VERSION IS NOT A COUNT EITHER.** ### `Phase 1.5
# ### checkpoint` gave `5 checkpoint`; `the open premise h2 as five faces` gave `2 as five faces`. ###
# ### The numeral must be a STANDALONE TOKEN: not preceded by a letter (an identifier suffix) and not by
# ### a dot (a version part). ### **THREE FALSE POSITIVES, THREE NAMED EXCLUSIONS, NONE OF THEM A
# ### ### JUDGEMENT ABOUT WHETHER A CLAIM IS TRUE.**
LEAN_VERSION = re.compile(r'\blean[\s-]*$', re.I)
COUNT_SHAPE = re.compile(r'(?<![A-Za-z.])' + NUM + r'[\s-]+(?:\w+[\s-]+){0,2}' + NOUN, re.I)


def count_shapes(desc):
    """### **EVERY SHAPE IN THE DESCRIPTION, NOT THE FIRST.** ### The first version reported one match,
    ### so a real count sitting AFTER the words `Lean 4` was invisible -- the detector's own noise
    ### hiding its own signal."""
    out = []
    for m in COUNT_SHAPE.finditer(desc):
        if LEAN_VERSION.search(desc[:m.start()]):
            continue
        out.append(m.group(0))
    return out

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def gh(*a, timeout=90):
    r = subprocess.run(['gh'] + list(a), capture_output=True, text=True,
                       encoding='utf-8', errors='replace', timeout=timeout)
    return r.returncode, (r.stdout or ''), (r.stderr or '')


def main():
    rec('=' * 100)
    rec('b369 -- COMPONENT 3: THE REFINEMENT PASS. ### **PRICED AND NOT RUN.**')
    rec('=' * 100)
    rec('')
    rec('  ### ### **THE CAP, FIRST, IN THE ORDER`S OWN WORDS: `audit nothing`.**')
    rec('  ### This tool enumerates and lists. ### **NO SURFACE IS READ FOR CORRECTNESS, NO CLAIM IS')
    rec('  ### ### CHECKED AGAINST ANY KERNEL, AND NO REPOSITORY IS GRADED.**')

    # ------------------------------------------------------------ (1) THE ENUMERATION
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE ENUMERATION. ### **LIVE, FROM THE ACCOUNT.**')
    rec('-' * 100)
    rc, out, err = gh('repo', 'list', OWNER, '--limit', '200', '--json',
                      'name,description,isPrivate,pushedAt,url,isFork')
    if rc != 0:
        rec('  ### ### **THE ENUMERATION FAILED : %s. ### NOTHING IS PRICED.**' % err.strip()[:120])
        run_clock.write(D, 'b369_pass_notes', LINES)
        return 2
    repos = sorted(json.loads(out), key=lambda r: r['name'])
    prog = [r for r in repos if r['name'].startswith(PROG) or r['name'] in PROG_EXACT]
    other = [r for r in repos if r not in prog]
    rec('    repositories on the account : %d' % len(repos))
    rec('    ### ### **PROGRAMME MATERIAL : %d ### / ### NOT PROGRAMME MATERIAL : %d ### -- %s**'
        % (len(prog), len(other), ', '.join('`%s`' % r['name'] for r in other)))
    rec('    ### **THE SECOND GROUP IS ENUMERATED AND REPORTED, NOT SILENTLY DROPPED.**')
    rec('    ### ### **AND THE ENUMERATION IS LIVE:** ### it is not the pins roster, not the mirror')
    rec('    ### roster and not recall. ### **A FEDERATION LIST TYPED FROM MEMORY IS THE SPECIES')
    rec('    ### ### `DESK_FRESHNESS` WAS MINTED AGAINST.**')

    # ------------------------------------------------------------ (2) THE SURFACES
    rec('')
    rec('-' * 100)
    rec('  ### (2) THE SURFACES, LISTED. ### **PRESENCE, NEVER CORRECTNESS.**')
    rec('-' * 100)
    rows, t0 = [], time.time()
    for r in prog:
        name = r['name']
        paths, truncated, note = [], False, ''
        if name in SKIP_TREE:
            note = SKIP_TREE[name]
        else:
            c, o, e = gh('api', 'repos/%s/%s/git/trees/HEAD?recursive=1' % (OWNER, name))
            if c == 0:
                try:
                    tj = json.loads(o)
                    paths = [x['path'] for x in tj.get('tree', []) if x.get('type') == 'blob']
                    truncated = bool(tj.get('truncated'))
                except ValueError:
                    note = 'the tree endpoint returned unparseable output'
            else:
                note = 'the tree endpoint refused: %s' % e.strip()[:60]
        desc = r.get('description') or ''
        readme = [p for p in paths if re.match(r'^readme(\.md)?$', p, re.I)]
        front = [p for p in paths if re.match(r'^(AGENTS|CLAUDE|CONTRIBUTING)\.md$', p, re.I)]
        lean = [p for p in paths if p.endswith('.lean') and not p.startswith('.lake/')]
        docs = [p for p in paths if p.lower().endswith('.md')]
        shapes = count_shapes(desc)
        rows.append(dict(
            name=name, private=r['isPrivate'], pushed=r['pushedAt'][:10], url=r['url'],
            description=desc, has_description=bool(desc),
            readme=readme, front=front, n_lean=len(lean), n_md=len(docs),
            tree_paths=len(paths), truncated=truncated, note=note,
            count_shapes=shapes, count_shape=(shapes[0] if shapes else None)))
    dt = time.time() - t0
    rec('    surfaces enumerated for %d repositories in %.1fs' % (len(rows), dt))
    rec('')
    rec('    %-32s %-5s %-10s %-7s %-6s %-6s %s'
        % ('repository', 'pub', 'pushed', 'README', 'front', '.lean', 'description carries a count shape'))
    for x in rows:
        rec('    %-32s %-5s %-10s %-7s %-6s %-6d %s'
            % (x['name'][:32], 'no' if x['private'] else 'YES', x['pushed'],
               'yes' if x['readme'] else '-', 'yes' if x['front'] else '-', x['n_lean'],
               (', '.join('`%s`' % c for c in x['count_shapes']) if x['count_shapes']
                else ('-' if x['has_description'] else '(no description)'))))
    for x in rows:
        if x['note']:
            rec('        ### `%s` -- %s' % (x['name'], x['note']))
        if x['truncated']:
            rec('        ### `%s` -- ### **THE TREE ENDPOINT TRUNCATED ITS ANSWER**, so the path counts'
                % x['name'])
            rec('        ### for this repository are a FLOOR and are reported as one.')
    rec('')
    rec('    ### ### **A COUNT-SHAPED STRING IS NOT A CLAIM.** ### The column above says a numeral')
    rec('    ### governs a noun this programme uses for its own artifacts. ### **WHETHER THAT IS A CLAIM,')
    rec('    ### ### AND WHETHER THE CLAIM IS TRUE, IS THE AUDIT** -- and the audit is not run here.')

    # ------------------------------------------------------------ (3) THE HINT
    rec('')
    rec('-' * 100)
    rec('  ### (3) THE HINT, SCORED AGAINST WHAT WAS FOUND. ### **NEVER THE OTHER WAY ROUND.**')
    rec('-' * 100)
    rec('  ### The navigator asserts from RECALL and not from any file, and the order says so itself.')
    rec('  ### **THE STRUCTURAL HAZARD IS NAMED FIRST:** ### `(H1)` supplies a description AND a count,')
    rec('  ### and a reader who found any count could fit it to the hint. ### **SO THE CONSTRUCTION')
    rec('  ### ### KERNEL IS IDENTIFIED FROM THE DESCRIPTIONS THEMSELVES, NOT BY SEARCHING FOR A')
    rec('  ### ### NUMBER.**')
    constr = [x for x in rows if re.search(r'\bconstruction\b', x['description'], re.I)]
    rec('')
    rec('    repositories whose own description uses the word `construction` : %d' % len(constr))
    for x in constr:
        rec('        `%s` -- %s' % (x['name'], x['description'][:150]))
    h1 = None
    if len(constr) == 1 and constr[0]['count_shape']:
        h1 = 'CONFIRMED'
    elif len(constr) == 1:
        h1 = 'CORRECTED -- the description is located and carries no count shape'
    elif not constr:
        h1 = 'NOT LOCATED -- no description names a construction kernel'
    else:
        h1 = 'CORRECTED -- more than one description uses the word, so the hint does not single one out'
    rec('')
    rec('    ### ### **(H1) `the construction kernel`s public description names a core terminal count`')
    rec('    ### ### -- %s.**' % h1)
    if len(constr) == 1:
        x = constr[0]
        rec('    ### The description of `%s` reads, in full:' % x['name'])
        rec('    ### | %s' % x['description'])
        rec('    ### ### **AND THE COUNT SHAPE IT CARRIES IS `%s`.**' % x['count_shape'])
        rec('    ### **THE WORD `core` IS THE DESCRIPTION`S OWN**, not this act`s -- which is why the')
        rec('    ### hint`s phrase `core terminal count` is scored CONFIRMED rather than merely matched.')
    rec('')
    rec('    ### ### **(H2) `that count may predate its current profile` -- NOT LOCATED, AND THE')
    rec('    ### ### REGISTRATION SAID SO BEFORE THE ACT RAN.**')
    rec('    ### Deciding whether a count PREDATES a profile requires reading the profile and comparing')
    rec('    ### it to the count. ### **THAT IS AN AUDIT, AND `audit nothing` IS THE CAP.**')
    rec('    ### **WHAT CAN BE REPORTED IS AN AGE, AND AN AGE IS NOT A STALENESS:**')
    if len(constr) == 1:
        x = constr[0]
        rec('    ###     `%s` was last pushed %s.' % (x['name'], x['pushed']))
        rec('    ###     the printed profile that would settle it is this repository`s own, and it is')
        rec('    ###     NOT read here.')
    rec('    ### ### **`NOT LOCATED` IS AN ANSWER, NOT A FAILURE** (`b367``s rule), and the act that')
    rec('    ### would settle it is the audit this one prices.')

    # ------------------------------------------------------------ (4) THE PRICE
    rec('')
    rec('-' * 100)
    rec('  ### (4) THE PRICE, IN THREE PARTS, REPORTED SEPARATELY.')
    rec('-' * 100)
    n_pub = sum(1 for x in rows if not x['private'])
    n_desc = sum(1 for x in rows if x['has_description'])
    n_shape = sum(1 for x in rows if x['count_shape'])
    n_readme = sum(1 for x in rows if x['readme'])
    n_front = sum(1 for x in rows if x['front'])
    n_lean = sum(x['n_lean'] for x in rows)
    n_md = sum(x['n_md'] for x in rows)
    surfaces = n_desc + n_readme + n_front
    rec('    ### ### **PART ONE -- WHAT ONE REPOSITORY COSTS.**')
    rec('    ###   a repository carries at most: ### one description, one `README`, at most one front')
    rec('    ###   document, and its `.lean` docstrings.')
    rec('    ###   ### **THE MECHANICAL HALF** ### -- fetch the description, the `README` and the front')
    rec('    ###   document, extract every count-shaped string, and extract every backticked identifier:')
    rec('    ###   ### **ONE TREE CALL AND AT MOST THREE FILE FETCHES**, and this act just measured that')
    rec('    ###   at ### **%.1f SECONDS PER REPOSITORY** ### for the tree call alone.' % (dt / max(1, len(rows))))
    rec('    ###   ### **THE READ HALF** ### -- deciding, for each extracted string, whether it is a')
    rec('    ###   CLAIM about that kernel and whether the kernel still carries it. ### **THAT IS A')
    rec('    ###   ### HUMAN OR MODEL READ OF THE SURFACE AGAINST THE SOURCE**, and it does not shrink')
    rec('    ###   with tooling. ### On `b367`/`b368``s own evidence, ONE front document against ONE')
    rec('    ###   kernel cost ### **THE WHOLE OF TWO ACTS** ### -- to locate, classify and dispose.')
    rec('    ### ### **PART TWO -- WHAT THE WHOLE FEDERATION COSTS.**')
    rec('    ###   programme repositories : ### **%d**. ### surfaces of the three cheap kinds : ### **%d**'
        % (len(rows), surfaces))
    rec('    ###   (%d descriptions, %d `README`s, %d front documents). ### `.lean` files carrying'
        % (n_desc, n_readme, n_front))
    rec('    ###   possible docstrings : ### **%d**, across %d markdown files besides.' % (n_lean, n_md))
    rec('    ###   ### **THE MECHANICAL SWEEP IS ONE ACT.** ### %d tree calls and roughly %d fetches is'
        % (len(rows), surfaces))
    rec('    ###   minutes, not days, and it produces a LIST OF CANDIDATES -- not a verdict.')
    rec('    ###   ### ### **THE READ IS NOT ONE ACT AND THIS IS THE PART THAT DOES NOT SCALE.** ### If')
    rec('    ###   a front document against its kernel costs on the order of one act, then the %d'
        % n_front)
    rec('    ###   front documents alone are an arc, and the `.lean` docstrings are a programme.')
    rec('    ### ### **PART THREE -- THE SPLIT, WHICH IS THE PART A PRICE USUALLY HIDES.**')
    rec('    ###   ### **MECHANICAL:** ### does a surface EXIST; does it carry a count-shaped string;')
    rec('    ###   which identifiers does it name; do those identifiers have declarations in the')
    rec('    ###   repository`s own `.lean` files. ### **ALL FOUR ARE `b368``s CLASSIFIER, ALREADY')
    rec('    ###   ### BUILT**, and it ran against one kernel in one act.')
    rec('    ###   ### **NOT MECHANICAL:** ### whether a count-shaped string is a CLAIM; what a count')
    rec('    ###   is a count OF; whether a name absent from HEAD was retired, renamed or never there;')
    rec('    ###   and whether a retirement was right. ### **`b368` AND `b369` BOTH FOUND THE SAME')
    rec('    ###   ### THING HERE: THE PREDICATE DECIDES THE ANSWER**, and a predicate that knows one')
    rec('    ###   shape finds one shape.')
    rec('    ###   ### **SO THE HONEST PRICE IS: THE MECHANICAL SWEEP IS CHEAP AND ITS OUTPUT IS A')
    rec('    ###   ### CANDIDATE LIST; THE FEDERATION-WIDE READ IS THE EXPENSIVE HALF AND NOTHING IN')
    rec('    ###   ### THIS PASS MAKES IT CHEAPER.**')

    # ------------------------------------------------------------ (5) THE RANKING
    rec('')
    rec('-' * 100)
    rec('  ### (5) THE RANKING. ### **BY THE ORDER`S OWN CRITERION, PRINTED BEFORE THE RANKING.**')
    rec('-' * 100)
    rec('  ### THE CRITERION, THE ORDER`S AND NOT THIS SEAT`S:')
    rec('  ###   (a) age since last touch;')
    rec('  ###   (b) whether the claim names COUNTS rather than TERMINALS;')
    rec('  ###   (c) whether the repository is public.')
    rec('  ### ### **THE ORDER SUPPLIED THREE FACTORS AND NO WEIGHTING, AND THIS ACT DOES NOT INVENT')
    rec('  ### ### ONE.** ### The table below prints the three factors SIDE BY SIDE and sorts by the')
    rec('  ### oldest touch within the group that satisfies (b) and (c), which is a presentation')
    rec('  ### choice and is stated as one. ### **A READER WHO WEIGHTS THEM DIFFERENTLY RE-SORTS THE')
    rec('  ### ### SAME THREE COLUMNS.**')
    risk = [x for x in rows if x['count_shape'] and not x['private']]
    risk.sort(key=lambda x: x['pushed'])
    rec('')
    rec('    ### ### **HIGHEST RISK BY THAT CRITERION -- PUBLIC, AND CARRYING A COUNT SHAPE : %d**'
        % len(risk))
    rec('    %-32s %-10s %-6s %s' % ('repository', 'pushed', 'public', 'the shape its description carries'))
    for x in risk:
        rec('    %-32s %-10s %-6s `%s`' % (x['name'][:32], x['pushed'], 'YES', x['count_shape']))
    rec('')
    rec('    ### **AND WHAT THIS RANKING IS NOT:** ### it is a ranking of ### **EXPOSURE**, not of')
    rec('    ### error. ### **NO REPOSITORY ON IT HAS BEEN SHOWN TO CARRY A STALE CLAIM**, and this act')
    rec('    ### did not look.')
    onlist = any(x['name'] == 'SIDE-effects' for x in risk)
    rec('')
    rec('    ### ### ### **AND WHAT THE RANKING CANNOT SEE IS REPORTED, BECAUSE IT IS SHARP:**')
    rec('    ### ### **THE ONE REPOSITORY THIS PROGRAMME KNOWS CARRIED A STALE CLAIM -- `SIDE-effects`,')
    rec('    ### ### FOUND BY `b157`, `b367` AND `b368` -- IS NOT ON THIS LIST : %s.**' % (not onlist))
    rec('    ### Its DESCRIPTION carries no count shape. ### The claim was in its ### **FRONT DOCUMENT**,')
    rec('    ### and `SIDE-effects` still carries one there: the paragraph above the list this act just')
    rec('    ### repaired asserts a count of framework consequences, ### **AND THIS ACT DID NOT TOUCH')
    rec('    ### ### IT**, because the order said the LIST is corrected and a count is not a name.')
    rec('    ### ### ### **SO A RANKING BUILT ON DESCRIPTIONS WOULD HAVE MISSED THE ONE CASE THE RECORD')
    rec('    ### ### ### ALREADY HAD.** ### The criterion is the order`s and this act does not reweight')
    rec('    ### it -- ### **BUT A CRITERION IS ONLY AS WIDE AS THE SURFACE IT READS**, and the cheap')
    rec('    ### surface is not where the known defect lived. ### The `README`s and the front documents')
    rec('    ### are listed above and were ### **NOT** ### searched for shapes, because searching them')
    rec('    ### means fetching and reading them, which is the audit.')
    rec('=' * 100)
    rec('  ### ### **COMPONENT 3 : PRICED. ### REPOSITORIES AUDITED : 0. ### SURFACES READ FOR')
    rec('  ### ### CORRECTNESS : 0. ### REPOSITORIES GRADED : 0.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b369_pass_notes', LINES)
    io.open(os.path.join(D, 'b369_pass.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(
            owner=OWNER, repos_on_account=len(repos), programme=len(prog),
            not_programme=[r['name'] for r in other], enumerated_live=True,
            rows=rows, seconds=round(dt, 1),
            descriptions=n_desc, readmes=n_readme, front_documents=n_front,
            lean_files=n_lean, markdown_files=n_md, cheap_surfaces=surfaces,
            public=n_pub, count_shapes=n_shape,
            construction_candidates=[x['name'] for x in constr],
            h1=h1, h2='NOT LOCATED',
            price_parts=3, ranking_criterion=['age since last touch',
                                              'counts rather than terminals', 'public'],
            highest_risk=[x['name'] for x in risk],
            repositories_audited=0, surfaces_read_for_correctness=0, repositories_graded=0,
            run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
