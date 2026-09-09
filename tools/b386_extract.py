# -*- coding: utf-8 -*-
"""b386_extract.py -- EXTRACT-TO-DISK, THE GUARD TOPOLOGY SURVEYED, AND THE ATTESTATION EXPERIMENT.

### ### **THE SURVEY RUNS BEFORE THE LOCK BECAUSE THE FACE MUST BE WRITTEN FROM MEASURED FACTS.**
### `b385`'s face permitted ONE comment line in ONE file and could not finish the repair, because
### its executor believed there was one guard. ### **THERE ARE THREE COPIES IN `relay` AND TWO IN
### ### EVERY OTHER ROSTERED REPOSITORY**, and a face written before counting them would fail the
### same way. ### So this tool counts every copy, digests each against every tracked blob of either
### guard path, and prints which blob each copy is recoverable from -- ### **BEFORE ANYTHING IS
### ### DELETED, WHICH IS THE ORDER `b385` GOT WRONG.**
###
### ### **AND THE ATTESTATION EXPERIMENT IS AN EXPERIMENT, NOT A CLAIM.** ### Component 4(i) asks
### whether the search lesson is mechanizable. ### The lesson itself -- *use the rule's own words,
### not the name a reader gave it* -- ### **CANNOT BE CHECKED BEFORE THE RULE IS FOUND**, since its
### own words are what you are looking for. ### What CAN be checked is weaker and mechanical:
### ### **IS EACH TERM OF THE QUERY ATTESTED ANYWHERE IN THE CORPUS AT ALL?** ### A term that
### occurs nowhere cannot find anything, and an absence built out of such terms is uninformative.
### ### **THIS TOOL RUNS THAT CHECK ON BOTH INCIDENTS' ACTUAL TERM LISTS AND PRINTS BOTH SCORES**,
### so the question is settled by a result rather than by an opinion.
###
### ### **THE SWEEP EXCLUDES EVERYTHING THIS ACT WRITES** (`b368`, widened `b383`), and the
### attestation sweep is run TWICE -- once over the corpus as it stands, and once with the records
### of `b383`-`b386` excluded, because ### **THOSE RECORDS NOW CONTAIN THE VERY TERMS BEING
### ### TESTED** ### and a contaminated count would flatter the check.
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
import b303_pins                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


FERRY = d('b386_ferry_2026-09-09.txt')
CLOSING385 = d('b385_closing.txt')
BANK385 = d('b385_the_six_on_the_trails.txt')
HOOKS385 = d('b385_hooks.txt')
REGISTRY = os.path.join(PP, 'REGISTRY.md')
GUARD = os.path.join(ROOT, '.githooks', 'pre-push')
SRC = os.path.join(ROOT, 'tools', 'git-hooks', 'pre-push')
HOOKTOOL = os.path.join(ROOT, 'tools', 'b304_hooks.py')
B383RUN = d(json.load(io.open(d('b383_components.json'), encoding='utf-8'))['run_file'])
B385RUN = d(json.load(io.open(d('b385_components.json'), encoding='utf-8'))['run_file'])

READS = [
    # ---- THE ORDER --------------------------------------------------------------------------------
    ('the order -- the act', 'ORDER', FERRY,
     'ACT b386 — THE GUARD MADE SINGLE-SOURCED. Number not claimed by'),
    ('the order -- the face is not widened mid-act', 'ORDER', FERRY,
     "gate; the face is not widened mid-act for any reason — b385's"),
    ('the ruling (R15) -- one guard, one source', 'RULING', FERRY,
     'strikeable: ONE GUARD, ONE SOURCE. A guard has exactly one'),
    ('the ruling (R15) -- the installer reads from that source', 'RULING', FERRY,
     'tracked source of truth in each repository, and whatever'),
    ('the ruling (R15) -- the three disposals of a second copy', 'RULING', FERRY,
     'or made a pointer to the source, or the repository is'),
    ('the ruling (R15) -- whichever the repository`s mechanics allow', 'RULING', FERRY,
     'reconfigured so the source is what runs — whichever the'),
    ('the ruling (R15) -- a topology defect, not a repair job', 'RULING', FERRY,
     'of one guard is not a repair job; it is a topology defect, and'),
    ('the order -- component 1, the three options quoted first', 'ORDER', FERRY,
     "COMPONENT 1 — THE THREE OPTIONS, QUOTED FIRST: reproduce b385's"),
    ('the order -- component 1, halt if none implements it', 'ORDER', FERRY,
     'that one. If none implements it, HALT and report — the author'),
    ('the order -- component 2, the face written wide enough to finish', 'ORDER', FERRY,
     'COMPONENT 2 — THE REPAIR ITSELF, with the face written wide'),
    ('the order -- component 2, the installer shown reading from the source', 'ORDER', FERRY,
     'single tracked source carrying the repaired line; the installer'),
    ('the order -- component 2, the disposal chosen and why', 'ORDER', FERRY,
     'disposed of per (R15) with which disposal was chosen and why;'),
    ('the order -- component 2, the gate cleared by the repair not the arm', 'ORDER', FERRY,
     'repository afterward, with the failing gate cleared by the'),
    ('the order -- component 3, the installer`s second defect', 'ORDER', FERRY,
     "COMPONENT 3 — THE INSTALLER'S SECOND DEFECT: the same tool"),
    ('the order -- component 3, repair the tool or route it with the price', 'ORDER', FERRY,
     'recoverable from any tracked blob, and repair the tool so it'),
    ('the order -- component 4(i), the search lesson', 'ORDER', FERRY,
     'COMPONENT 4 — TWO FILINGS: (i) the search lesson, minted — a'),
    ('the order -- component 4(i), the rule`s own words not the reader`s name', 'ORDER', FERRY,
     "search for a rule uses the rule's own words, not the name a"),
    ('the order -- component 4(i), mechanized or filed as judgement', 'ORDER', FERRY,
     'mechanized if a query-construction check is mechanizable, else'),
    ('the order -- component 4(ii), the paraphrase corrected on the record', 'ORDER', FERRY,
     "(ii) the navigator's paraphrase of the reviewer rule corrected"),
    ('the order -- the closing, the guard item closed only if the exercise passes',
     'ORDER', FERRY,
     "item closed only if Component 2's exercise passes and left open"),
    ('the order -- (F1), deletion of the untracked-path copy', 'ORDER', FERRY,
     '(R15) is deletion of the untracked-path copy with the installer'),
    ('the order -- (F2), the backup recoverable from a tracked blob', 'ORDER', FERRY,
     "repointed; (F2) the destroyed backup's content is recoverable"),

    # ---- b385`S THREE OPTIONS, WHERE THEY ACTUALLY ARE ---------------------------------------------
    ('b385 option (a) -- repair the source, leaving both files', 'OPTION', CLOSING385,
     '###   ### **(a) REPAIR THE SOURCE** ### so the two agree, leaving both files.'),
    ('b385 option (b) -- retire the source and repoint the installer', 'OPTION', CLOSING385,
     '###   ### **(b) RETIRE THE SOURCE** ### and repoint `b304_hooks.py`s `SOURCE` at'),
    ('b385 option (b) -- one source of truth, the tool installs what runs', 'OPTION', CLOSING385,
     '###     the tool installs the file the repositories actually run.'),
    ('b385 option (c) -- neither, the comment allowed to drift', 'OPTION', CLOSING385,
     '###   ### **(c) NEITHER**, and record that the guard`s comment is allowed to drift because'),
    ('b385 -- the face must name the file it may write', 'OPTION', CLOSING385,
     '### ### **WHICHEVER IS CHOSEN, THE FACE MUST NAME THE FILE IT MAY WRITE**, because this '
     'act`s did'),

    # ---- b385`S OWN ACCOUNT OF THE DEFECT ----------------------------------------------------------
    ('b385 -- two tracked guard files', 'PRIOR', CLOSING385,
     '### There are ### **TWO TRACKED GUARD FILES** ### in `relay` -- `.githooks/pre-push`, '
     'which the'),
    ('b385 -- the closure withdrawn', 'PRIOR', CLOSING385,
     '### ### **COMPONENT 3(a), THE GUARD`S STALE INSTALL LINE, IS NOT CLOSED.** ### The desk '
     'filed it'),
    ('b385 -- the backup overwritten and then removed', 'PRIOR', CLOSING385,
     '### ### **ONE SIDE EFFECT, NAMED RATHER THAN SWALLOWED:** ### `b304_hooks.py` overwrote '
     'the'),
    ('b385 -- a file moved is not a file replaced', 'PRIOR', CLOSING385,
     '### ### ### **THE SPECIES: `A FILE MOVED IS NOT A FILE REPLACED`.** ### `b371` moved the '
     'guard'),
    ('b385 bank -- the guard repaired under (R4)', 'PRIOR', BANK385,
     '### ### **(a) THE GUARD`S STALE INSTALL LINE -- `DONE`.** ### The tracked guard'),
    ('b385 hooks record -- relay replaced', 'PRIOR', HOOKS385,
     '  relay                  REPLACED (previous kept as .b304-backup)'),
    ('b385 hooks record -- the relay exercise skipped', 'PRIOR', HOOKS385,
     '  relay                  ### **SKIPPED -- working tree carries 1 uncommitted path(s).'),

    # ---- THE GUARD FILES AND THE INSTALLER ---------------------------------------------------------
    ('the installed guard -- its repaired install line', 'GUARD', GUARD,
     '# Tracked at .githooks/pre-push (moved there b371, 2026-09-08). Install: git config '
     'core.hooksPath .githooks'),
    ('the second tracked copy -- its stale install line', 'GUARD', SRC,
     '# Tracked copy: tools/git-hooks/pre-push. Install: cp tools/git-hooks/pre-push '
     '.git/hooks/pre-push'),
    ('the installer -- the SOURCE it reads from', 'GUARD', HOOKTOOL,
     "SOURCE = os.path.join(ROOT, 'tools', 'git-hooks', 'pre-push')"),
    ('the installer -- the backup it writes without checking', 'GUARD', HOOKTOOL,
     "        shutil.copy2(dest, dest + '.b304-backup')"),
    ('the installer -- the destination it installs into', 'GUARD', HOOKTOOL,
     "    dest = os.path.join(repo_path, HOOKS_DIR, 'pre-push')"),

    # ---- THE RULE, FOR COMPONENT 4(ii) -------------------------------------------------------------
    ('the rule -- its standing-rule heading', 'RULE', REGISTRY,
     '## SESSION PROTOCOL — reviewer mirror-refresh (standing rule, 2026-07-29)'),
    ('the rule -- the currency check, the authority clause', 'RULE', REGISTRY,
     "- **Currency check.** If a reviewer's claim disagrees with the current MANIFEST"),
    ('the rule -- the procedure and the manifest columns', 'RULE', REGISTRY,
     '- **Procedure.** Create `D:'),

    # ---- THE TWO SEARCHES, FOR COMPONENT 4(i) ------------------------------------------------------
    ('b383`s search -- the reservoir probe', 'SEARCH', B383RUN,
     '###   probe `reservoir             ` : ### **'),
    ('b383`s search -- the reviewer pool probe', 'SEARCH', B383RUN,
     '###   probe `reviewer pool         ` : ### **'),
    ('b383`s search -- the reviewer budget probe', 'SEARCH', B383RUN,
     '###   probe `reviewer budget       ` : ### **'),
    ('b385`s search -- the three terms that found it', 'SEARCH', B385RUN,
     '### ### ### **THE THREE TERMS THAT FOUND IT WERE `SESSION PROTOCOL`, `reviewer`s'),
    ('b385`s search -- all three from the rule`s own vocabulary', 'SEARCH', B385RUN,
     '### ### ### VOCABULARY, WHICH THE ORDER SUPPLIED.**'),
]

# ### ### **THE TWO INCIDENTS' ACTUAL TERM LISTS**, taken from the acts' own tools and not retyped
# ### from memory: `b383_extract.py` line 289 and `b385_extract.py`'s `TERMS`.
B383_TERMS = ['reservoir', 'reviewer pool', 'reviewer budget', 'reviewers are finite',
              'held in reserve', 'one reviewer']
B385_TERMS = ['SESSION PROTOCOL', 'mirror-refresh', 'reviewer set', 'not from recall',
              "reviewer's authority", 'Currency check', 'reservoir']

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.strip()


def lf(b):
    return b.replace(b'\r\n', b'\n')


def sha(b):
    import hashlib
    return hashlib.sha256(b).hexdigest()


def main():
    rec('=' * 100)
    rec('b386_extract.py -- EXTRACT-TO-DISK, THE GUARD TOPOLOGY, AND THE ATTESTATION EXPERIMENT.')
    rec('=' * 100)
    rec('')
    rec('-' * 100)
    rec('  ### THE REFS.')
    rec('-' * 100)
    refs = {}
    for name, repo in b303_pins.REPOS:
        br = git(repo, 'rev-parse', '--abbrev-ref', 'HEAD')
        hd = git(repo, 'rev-parse', 'HEAD')[:12]
        refs[name] = dict(branch=br, head=hd, dirty=bool(git(repo, 'status', '--porcelain')))
        rec('    %-22s ref `%s` = `%s`   ### tree dirty : %s'
            % (name, br, hd, refs[name]['dirty']))

    # --------------------------------------------------------------- THE GUARD TOPOLOGY, SURVEYED
    rec('')
    rec('-' * 100)
    rec('  ### THE GUARD TOPOLOGY. ### **EVERY COPY, IN EVERY ROSTERED REPOSITORY, BEFORE')
    rec('  ### ANYTHING IS TOUCHED.**')
    rec('-' * 100)
    # ### **EVERY TRACKED BLOB OF EITHER GUARD PATH, ACROSS ALL HISTORY** -- the recoverability
    # ### set. ### A copy that matches none of these is a copy that CANNOT be restored if deleted,
    # ### and that is the fact `b385` needed and did not have.
    blobs = {}
    for path in ('.githooks/pre-push', 'tools/git-hooks/pre-push'):
        for c in git(ROOT, 'log', '--format=%H', '--all', '--', path).split(chr(10)):
            if not c.strip():
                continue
            r = subprocess.run(['git', '-C', ROOT, 'show', '%s:%s' % (c.strip(), path)],
                               capture_output=True)
            if r.returncode == 0:
                blobs['%s:%s' % (c.strip()[:7], path)] = lf(r.stdout)
    rec('  ### tracked blobs of either guard path, across all history : ### **%d**' % len(blobs))
    for k, v in sorted(blobs.items()):
        rec('      %-40s %5d bytes (LF)   sha %s' % (k, len(v), sha(v)[:16]))

    rec('')
    rec('  %-22s %-26s %7s %-18s %-8s %s'
        % ('repo', 'path', 'bytes', 'sha (LF-normalised)', 'tracked', 'recoverable from'))
    copies = []
    for name, repo in b303_pins.REPOS:
        tracked = set(git(repo, 'ls-files').split(chr(10)))
        for rel in ('.githooks/pre-push', 'tools/git-hooks/pre-push',
                    '.git/hooks/pre-push'):
            p = os.path.join(repo, rel.replace('/', os.sep))
            if not os.path.exists(p):
                continue
            raw = io.open(p, 'rb').read()
            n = lf(raw)
            match = sorted(k for k, v in blobs.items() if v == n)
            istr = rel in tracked
            copies.append(dict(repo=name, path=rel, bytes=len(raw), sha=sha(n),
                               tracked=istr, recoverable_from=match))
            rec('  %-22s %-26s %7d %-18s %-8s %s'
                % (name, rel, len(raw), sha(n)[:16], istr, ', '.join(match) or '### NONE'))
    hooks_paths = {name: git(repo, 'config', 'core.hooksPath') for name, repo in b303_pins.REPOS}
    rec('')
    rec('  ### **`core.hooksPath` IN EVERY ROSTERED REPOSITORY** -- which decides WHICH copy runs:')
    for k, v in hooks_paths.items():
        rec('      %-22s core.hooksPath = `%s`' % (k, v or '### UNSET'))
    tracked_copies = [c for c in copies if c['tracked']]
    untracked_copies = [c for c in copies if not c['tracked']]
    unrecoverable = [c for c in copies if not c['recoverable_from']]
    rec('')
    rec('  ### ### **COPIES ON DISK : %d. ### TRACKED : %d. ### UNTRACKED : %d.**'
        % (len(copies), len(tracked_copies), len(untracked_copies)))
    rec('  ### ### **COPIES RECOVERABLE FROM NO TRACKED BLOB : %d.**' % len(unrecoverable))
    for c in unrecoverable:
        rec('      ### ### **%s / %s** -- deleting this would destroy content' % (c['repo'],
                                                                                 c['path']))
    byrepo = {}
    for c in tracked_copies:
        byrepo.setdefault(c['repo'], []).append(c['path'])
    rec('  ### ### **TRACKED COPIES PER REPOSITORY** ### -- `(R15)` allows exactly one:')
    for k, v in byrepo.items():
        rec('      %-22s %d  %s%s' % (k, len(v), v, '   ### ### **TWO. THE DEFECT.**'
                                      if len(v) > 1 else ''))
    diverged = len(set(c['sha'] for c in copies)) > 1
    rec('  ### ### **DISTINCT CONTENTS ACROSS ALL COPIES : %d** ### -- so the copies %s'
        % (len(set(c['sha'] for c in copies)),
           'DIVERGE' if diverged else 'agree'))

    # ------------------------------------------------------- THE ATTESTATION EXPERIMENT, 4(i)
    rec('')
    rec('-' * 100)
    rec('  ### COMPONENT 4(i) -- IS THE SEARCH LESSON MECHANIZABLE?')
    rec('-' * 100)
    rec('  ### ### **THE LESSON ITSELF IS NOT CHECKABLE BEFORE THE SEARCH**: it says use the')
    rec('  ### rule`s own words, and ### **THE RULE`S OWN WORDS ARE WHAT YOU ARE LOOKING FOR.**')
    rec('  ### ### **THE WEAKER CHECK IS MECHANICAL:** ### is each term of the query ### **ATTESTED')
    rec('  ### ### ANYWHERE IN THE CORPUS AT ALL?** ### A term that occurs nowhere cannot find')
    rec('  ### anything, and an absence assembled from such terms is uninformative.')
    ROOTS = [PP, os.path.join(ROOT, 'tools'), os.path.join(TC, 'modules')]
    WRITES = {'OPEN_TRAILS.md', 'CORRESPONDENCE.md', 'banked_index.py', 'FINDINGS.md'}
    LATER = ('b383', 'b384', 'b385', 'b386')

    def sweep(pattern, exclude_acts):
        hits = []
        for root in ROOTS:
            for dp, _dn, fn in os.walk(root):
                if '.git' in dp or '.lake' in dp:
                    continue
                for f in fn:
                    if not f.endswith(('.md', '.txt', '.py')) or f in WRITES:
                        continue
                    if 'b386' in f:
                        continue
                    if exclude_acts and any(a in f for a in LATER):
                        continue
                    p = os.path.join(dp, f)
                    try:
                        txt = io.open(p, encoding='utf-8', errors='replace').read()
                    except OSError:
                        continue
                    for i, ln in enumerate(txt.split(chr(10)), 1):
                        if pattern.lower() in ln.lower():
                            hits.append((os.path.relpath(p, root).replace(os.sep, '/'), i))
                            break
        return hits

    # ### **THE POSITIVE CONTROL FIRST**, on both sweeps, because an attestation count of zero
    # ### everywhere would otherwise be indistinguishable from a dead sweep (`b378`).
    att = {}
    for lbl, exc in (('the corpus as it stands', False),
                     ('with the b383-b386 records excluded', True)):
        ctrl = sweep('internal-until-fruit', exc)
        rec('')
        rec('  ### **SWEEP: %s.** ### POSITIVE CONTROL `internal-until-fruit` : ### **%d FILE(S)**'
            % (lbl, len(ctrl)))
        for tag, terms in (('b383', B383_TERMS), ('b385', B385_TERMS)):
            counts = {}
            for term in terms:
                counts[term] = len(sweep(term, exc))
            live = sum(1 for v in counts.values() if v)
            att[(tag, exc)] = dict(counts=counts, attested=live, total=len(terms),
                                   control=len(ctrl))
            rec('    ### **`%s`S QUERY -- %d TERMS, %d ATTESTED, %d UNATTESTED:**'
                % (tag, len(terms), live, len(terms) - live))
            for k, v in counts.items():
                rec('        %-24s : %3d file(s)%s'
                    % ('`%s`' % k, v, '   ### ### **UNATTESTED**' if not v else ''))
    rec('')
    rec('  ### ### ### **THE CHECK SEPARATES THE TWO INCIDENTS, AND THE SCORE IS PRINTED RATHER')
    rec('  ### ### ### THAN ASSERTED.**')
    for exc in (False, True):
        rec('      %-36s b383 %d/%d attested   b385 %d/%d attested'
            % ('the corpus as it stands' if not exc else 'b383-b386 records excluded',
               att[('b383', exc)]['attested'], att[('b383', exc)]['total'],
               att[('b385', exc)]['attested'], att[('b385', exc)]['total']))

    rec('')
    rec('-' * 100)
    rec('  ### THE READS. ### **HINT TYPED -> ANCHOR READ FROM THE FILE -> NEEDLE PULLED.**')
    rec('-' * 100)
    out, noanchor, differing, bytag = [], 0, 0, {}
    for lbl, tag, path, hint in READS:
        rec('')
        rec('  [%-8s] %s' % (tag, lbl))
        try:
            n, line = AF.find(path, hint)
        except Exception as e:
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
        rec('      | %s' % line.strip()[:220])
        out.append(dict(label=lbl, tag=tag, file=os.path.basename(path), path=path,
                        line=n, text=line.rstrip(chr(10))))
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), noanchor))
    rec('  ### ### **BY TAG : %s**' % bytag)
    rec('  ### **NO DOCUMENT WAS EDITED BY THIS TOOL. ### NO COPY WAS DELETED BY IT EITHER.**')
    rec('=' * 100)
    pth = run_clock.write(D, 'b386_extract_notes', LINES)
    io.open(d('b386_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(
            reads=len(READS), without_anchor=noanchor, anchors_differing=differing,
            by_tag=bytag, refs=refs, built=out,
            copies=copies, blobs={k: len(v) for k, v in blobs.items()},
            hooks_paths=hooks_paths,
            copies_total=len(copies), copies_tracked=len(tracked_copies),
            copies_untracked=len(untracked_copies), copies_unrecoverable=len(unrecoverable),
            tracked_per_repo={k: v for k, v in byrepo.items()}, diverged=diverged,
            attestation={'%s|%s' % (t, e): v for (t, e), v in att.items()},
            b383_terms=B383_TERMS, b385_terms=B385_TERMS,
            run_file=os.path.basename(pth),
            run_clock=run_clock.read_stamp(pth)), indent=1))
    print('  written: %s' % os.path.basename(pth))
    return 0 if noanchor == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
