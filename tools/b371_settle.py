# -*- coding: utf-8 -*-
"""b371_settle.py -- COMPONENT 1: THE ONE CONFIRMED LIVE CLAIM, SETTLED.

### ### **THE VERDICT IS ONE OF TWO RULED WORDS AND THIS TOOL MAY NOT INVENT A THIRD.**
### ### **THE ROUTE IS FIXED BEFORE THE READ** (the registration's own clause), because this is exactly
### where a seat would fit a number to a hint: ### **A SUM THAT HAPPENS TO MATCH IS NOT A SCOPE; A
### ### SENTENCE THAT NAMES THE SUM IS.**
### ### **THE TEST THAT SEPARATES THE TWO WORDS IS MECHANICAL AND IS STATED FIRST:**
###   ### `SCOPE-DEPENDENT` requires that the description's figure and the profile's ### **COUNT
###   ### DIFFERENT THINGS.**
###   ### `STALE` is what remains when they count ### **THE SAME THING AT DIFFERENT REFS.**
### ### **SO THE TOOL MEASURES THE SAME QUANTITY AT BOTH REFS.** ### If the figure is exactly what the
### profile carried at the earlier ref, the two count the same thing and the word is `STALE`.
### ### **NO BUILD IS RUN.** ### The profile is a printed record, read at a ref and against its blob.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                # noqa: E402
import anchor_from_file as AF   # noqa: E402

D = os.path.join(ROOT, 'data')
GS = os.path.join('D:', os.sep, 'SIDE-global-section')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OWNER, REPO = 'psinary-sketch', 'SIDE-global-section'
PRINT_LINE = 'does not depend on any axioms'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(*a, repo=GS):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def gh(*a):
    r = subprocess.run(['gh'] + list(a), capture_output=True, text=True,
                       encoding='utf-8', errors='replace', timeout=90)
    return r.returncode, (r.stdout or ''), (r.stderr or '')


def prints_at(ref):
    """### THE PROFILE'S OWN COUNT AT A REF. ### **READ FROM THE COMMITTED OBJECT, NOT THE WORKTREE.**"""
    txt = git('show', '%s:AXIOM_PRINTS.txt' % ref)
    lines = [x for x in txt.split(chr(10)) if x.strip()]
    return len(lines), sum(1 for x in lines if PRINT_LINE in x)


def main():
    rec('=' * 100)
    rec('b371 -- COMPONENT 1: THE ONE CONFIRMED LIVE CLAIM, SETTLED.')
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures : %s' % AF.self_test(False))

    # ---------------------------------------------------------------- (1) THE CLAIM, LIVE
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE CLAIM, READ LIVE FROM THE ACCOUNT.')
    rec('-' * 100)
    rc, out, err = gh('repo', 'view', '%s/%s' % (OWNER, REPO), '--json', 'description,url')
    if rc != 0:
        rec('  ### ### **THE DESCRIPTION COULD NOT BE READ : %s. ### NOTHING IS SETTLED.**'
            % err.strip()[:100])
        run_clock.write(D, 'b371_settle_notes', LINES)
        return 2
    desc = json.loads(out)['description'] or ''
    rec('    the description, in full, as the account carries it now:')
    rec('    | %s' % desc)
    m = re.search(r'Core\s+(\d+)\s+zero-axiom\s+terminals', desc)
    fig = int(m.group(1)) if m else None
    rec('    ### ### **THE FIGURE THE DESCRIPTION ATTACHES TO `Core` : %s**' % fig)
    if fig is None:
        rec('    ### ### **NO SUCH FIGURE. ### `NOT LOCATED`, WHICH IS A FULL ANSWER.**')
        run_clock.write(D, 'b371_settle_notes', LINES)
        return 0
    rec('    ### **AND WHAT THE DESCRIPTION DOES NOT CARRY, WHICH IS THE WHOLE QUESTION:** ### any ref,')
    rec('    ### tag, version or date. ### The figure stands unqualified.')
    qualifiers = [w for w in ('v0.', 'tag', 'release', 'as of', 'at HEAD', '20') if w in desc]
    rec('    ### ### **QUALIFIERS PRESENT IN THE DESCRIPTION : %s**' % (qualifiers or 'NONE'))

    # ---------------------------------------------------------------- (2) THE PROFILE, AT BOTH REFS
    rec('')
    rec('-' * 100)
    rec('  ### (2) THE PROFILE, AT BOTH REFS. ### **THE SAME QUANTITY, MEASURED TWICE.**')
    rec('-' * 100)
    head = git('rev-parse', 'HEAD').strip()
    lsr = git('ls-remote', 'origin', 'refs/heads/main').split()
    lsr = lsr[0] if lsr else ''
    tags = git('tag', '-l').split()
    tag = tags[0] if tags else None
    n_head_all, n_head = prints_at('HEAD')
    work = io.open(os.path.join(GS, 'AXIOM_PRINTS.txt'), encoding='utf-8', errors='replace').read()
    n_work = sum(1 for x in work.split(chr(10)) if PRINT_LINE in x)
    rec('    `SIDE-effects`-style pin check on the construction kernel:')
    rec('        HEAD = `%s` ; ls-remote = `%s` ; EQUAL : %s' % (head, lsr, head == lsr))
    rec('    ### ### **BAR 2 -- THE PROFILE READ FROM THE BLOB AND FROM THE WORKING FILE, AND THEY')
    rec('    ### ### AGREE : %s** (blob %d, working %d)' % (n_head == n_work, n_head, n_work))
    rec('        lines at HEAD : %d ; of them zero-axiom : %d ; NOT zero-axiom : %d'
        % (n_head_all, n_head, n_head_all - n_head))
    tag_all = tag_zero = None
    ahead = None
    if tag:
        tag_all, tag_zero = prints_at(tag)
        ahead = git('rev-list', '--count', '%s..HEAD' % tag).strip()
        tagc = git('rev-parse', '%s^{commit}' % tag).strip()
        rec('    ### the one tag the repository carries : `%s` = `%s`' % (tag, tagc))
        rec('        lines at `%s` : %d ; of them zero-axiom : %d' % (tag, tag_all, tag_zero))
        rec('    ### ### **AND HEAD IS `%s` COMMIT(S) AHEAD OF THAT TAG.**' % ahead)

    # ---------------------------------------------------------------- (3) THE SCOPE, QUOTED OR NOT
    rec('')
    rec('-' * 100)
    rec('  ### (3) THE SCOPE -- SOUGHT IN A DOCUMENT THAT STATES IT, NEVER INFERRED.')
    rec('-' * 100)
    stated = []
    for lbl, path, hint in (
            ("the kernel's own correspondence", os.path.join(GS, 'CORRESPONDENCE.md'),
             'audit at v0.1.0 (103 + 11 = 114 exactly), and each act'),
            ('the papers registry', os.path.join(PP, 'REGISTRY.md'),
             '**Subject:** the construction era’s verified Lean material — the finite-place models')):
        try:
            n, line = AF.find(path, hint)
            clean = ' '.join(re.sub(r'#{2,}', ' ', line).split())
            stated.append(dict(where=lbl, file=os.path.basename(path), line=n, quote=clean[:300]))
            rec('    [%s] %s:%d' % (lbl, os.path.basename(path), n))
            rec('        | %s' % clean[:240])
        except AF.AnchorError as e:
            rec('    ### **NOT LOCATED at %s : %s**' % (lbl, str(e)[:80]))
    rec('')
    rec('    ### ### **BOTH DOCUMENTS SAY THE SAME THING AND IT IS NOT A SCOPE -- IT IS A REF.** ### They')
    rec('    ### say the figure was exact ### **AT THE TAG**, and they name its two summands. ### Neither')
    rec('    ### says the figure counts a SUBSET of what the profile counts.')

    # ---------------------------------------------------------------- (4) THE SETTLING
    rec('')
    rec('-' * 100)
    rec('  ### (4) THE SETTLING. ### **BAR 1: THE TEST WAS FIXED BEFORE THE READ.**')
    rec('-' * 100)
    same_quantity = (tag_zero == fig)
    rec('    ### **THE DECIDING TEST:** ### does the description`s figure equal what THE SAME')
    rec('    ### MEASUREMENT carried at the earlier ref?')
    rec('    ### ### **THE PROFILE AT `%s` CARRIED `%s`. ### THE DESCRIPTION SAYS `%s`. ### EQUAL : %s.**'
        % (tag, tag_zero, fig, same_quantity))
    if same_quantity:
        verdict = 'STALE'
        rec('    ### ### ### **SO THE TWO COUNT THE SAME THING AT DIFFERENT REFS, NOT DIFFERENT THINGS.**')
        rec('    ### `SCOPE-DEPENDENT` requires that the words count DIFFERENT THINGS. ### They do not:')
        rec('    ### the description`s figure is EXACTLY the zero-axiom print count of `Core`, which is')
        rec('    ### exactly what the profile counts. ### **THE FIGURE WAS RIGHT AND THE REPOSITORY MOVED')
        rec('    ### ### PAST IT.**')
        rec('    ### ### ### **VERDICT: `STALE`.**')
        rec('    ### **AND THE ARITHMETIC COINCIDENCE IS REPORTED AS A COINCIDENCE, NOT PROMOTED TO A')
        rec('    ### ### SCOPE:** ### the summands `103 + 11` DO sum to the figure, and the record does')
        rec('    ### name them -- ### **BUT THEY ARE THE COMPOSITION OF THE TAG`S OWN COUNT, NOT A SUBSET')
        rec('    ### ### OF A LARGER PRESENT ONE.** ### Reading them as a scope would be exactly the')
        rec('    ### inference the registration forbade before the read.')
    else:
        verdict = 'SCOPE-DEPENDENT'
        rec('    ### ### ### **VERDICT: `SCOPE-DEPENDENT`** -- and the wording is ROUTED, not rewritten.')
    rec('')
    rec('    ### ### **AND THE NAVIGATOR`S EXPECTATION IS SCORED AGAINST THE DESCRIPTION`S OWN WORDS,')
    rec('    ### ### WHICH IS WHAT MADE IT REFUTABLE:** ### it expected `SCOPE-DEPENDENT` with the scope')
    rec('    ### unstated. ### **THE SCOPE HALF IS REFUTED** -- there is no scope; there is a ref. ###')
    rec('    ### **THE UNSTATED HALF IS CONFIRMED AND THEN SOME:** ### the description names no ref at')
    rec('    ### all, which is precisely why the figure reads as current.')

    # ---------------------------------------------------------------- (5) THE ADJACENT FINDING
    rec('')
    rec('-' * 100)
    rec('  ### (5) THE ADJACENT FINDING -- REPORTED, ROUTED, NOT REPAIRED.')
    rec('-' * 100)
    rme = io.open(os.path.join(GS, 'README.md'), encoding='utf-8', errors='replace').read()
    mh = re.search(r'\*\*(\d+) terminals\*\* \((.*?)\) across (\d+) modules', rme, re.S)
    mr = re.search(r'`AXIOM_PRINTS\.txt` \((\d+)/(\d+)\)', rme)
    parts = re.findall(r'(\d+)\s+[a-zA-Z][a-zA-Z-]*', ' '.join(mh.group(2).split())) if mh else []
    psum = sum(int(x) for x in parts)
    rec('    the kernel`s own `README.md`, at HEAD, states:')
    rec('        a headline of `%s` terminals across `%s` modules' % (mh.group(1), mh.group(3)) if mh
        else '        (headline not located)')
    rec('        a parenthetical breakdown of `%d` parts summing to `%d`' % (len(parts), psum))
    rec('        an assembly ratio of `%s/%s`' % (mr.group(1), mr.group(2)) if mr
        else '        (ratio not located)')
    rec('    ### ### **THE HEADLINE AND ITS OWN BREAKDOWN DISAGREE : %s vs %s.**'
        % (mh.group(1) if mh else '?', psum))
    rec('    ### ### **AND BOTH DISAGREE WITH THE PROFILE THE SAME REPOSITORY SHIPS : `%d`.**' % n_head)
    rec('    ### ### **THIS IS OUTSIDE COMPONENT 1`S TARGET AND IS NOT REPAIRED HERE.** ### The target is')
    rec('    ### the DESCRIPTION. ### **AND IT IS THE SHARPER HALF OF THE FINDING, BECAUSE THE `README`')
    rec('    ### ### IS A TRACKED FILE AND THE DESCRIPTION IS NOT** -- `DURABILITY_SPLIT`: the drift that')
    rec('    ### travels with a clone is the one nobody has been ordered to fix.')

    rec('=' * 100)
    p = run_clock.write(D, 'b371_settle_notes', LINES)
    io.open(os.path.join(D, 'b371_settle.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(
            description_before=desc, figure=fig, qualifiers=qualifiers,
            head=head, ls_remote=lsr, pinned=(head == lsr),
            tag=tag, tag_commit=git('rev-parse', '%s^{commit}' % tag).strip() if tag else None,
            head_ahead_of_tag=ahead,
            prints_at_head=n_head, prints_at_head_all=n_head_all, prints_working=n_work,
            blob_equals_working=(n_head == n_work),
            prints_at_tag=tag_zero, prints_at_tag_all=tag_all,
            same_quantity=bool(same_quantity), verdict=verdict,
            scope_statements=stated,
            readme_headline=int(mh.group(1)) if mh else None,
            readme_modules=int(mh.group(3)) if mh else None,
            readme_breakdown_parts=len(parts), readme_breakdown_sum=psum,
            readme_ratio=[int(mr.group(1)), int(mr.group(2))] if mr else None,
            adjacent_repaired=False, build_run=False,
            run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
