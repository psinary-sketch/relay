# -*- coding: utf-8 -*-
"""b378_terminals.py -- ADDITION ONE (EVERY REF) AND ADDITION TWO (THE TWO CONVENTIONS).

### ### **ADDITION ONE -- EVERY REF, NOT `main`.** ### `b377` searched one ref per kernel and reported
### `37` identifiers unresolved. ### **THAT FIGURE IS AN UPPER BOUND TAKEN AT ONE REF.** ### This file
### re-runs the search across ### **EVERY BRANCH AND EVERY TAG** ### of every kernel on disk, with the
### refs ### **ENUMERATED LIVE FROM EACH REPOSITORY AND PRINTED** -- never typed, never assumed.
### ### **AND WHERE A DOCUMENT NAMES A HELD BRANCH IN ITS OWN TEXT, THAT BRANCH IS SEARCHED BY NAME
### ### AND THE DOCUMENT'S OWN SENTENCE IS QUOTED.**

### ### **ADDITION TWO -- THE TWO CONVENTIONS.** ### The corpus writes terminal names ### **BARE** ### in
### its older documents and ### **DOTTED** ### in its newer ones. ### The matcher accepts both, carries
### fixtures in both polarities, and carries a ### **DISCRIMINATION ARM** ### proving it still refuses a
### name absent under either -- because ### **A MATCHER THAT ACCEPTS EVERYTHING IS NOT A MATCHER**, and
### widening one that was too narrow is exactly the moment to prove it did not become too wide.
### ### **BOTH DIALECTS ARE CORRECT IN THEIR OWN TERMS AND NO DOCUMENT IS REWRITTEN.**

### ### **THE SEARCH IS MADE AFFORDABLE WITHOUT BEING MADE NARROWER:** ### refs pointing at the same
### commit are searched ### **ONCE** ### and reported for every ref that shares it, and all the names
### are looked for in ### **ONE PASS PER TREE** ### rather than one pass per name. ### **DEDUPLICATION
### ### BY COMMIT IS NOT A SAMPLE. ### THE SAME TREE CANNOT GIVE TWO ANSWERS.**
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
DRIVE = 'D:' + os.sep

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# =====================================================================================================
# ### **THE MATCHER, ACCEPTING BOTH CONVENTIONS.**
# ### A Lean declaration site writes the LAST segment: `theorem foo` inside `namespace Bar`. ### So a
# ### DOTTED citation `Bar.foo` and a BARE citation `foo` look for the SAME declaration line, and the
# ### dotted one additionally requires the namespace to be confirmed in the same file.
# ### ### **THAT IS THE WHOLE WIDENING, AND IT IS ONE LINE OF ASYMMETRY, NOT A LOOSENING.**
# =====================================================================================================
KEYWORD = r'(?:theorem|lemma|def|abbrev|instance|structure|inductive|axiom)'
LEAD = (r'^[ \t]*(?:@\[[^\]]*\][ \t]*)?'
        r'(?:private[ \t]+|protected[ \t]+|noncomputable[ \t]+|partial[ \t]+|unsafe[ \t]+)*')

# ### **`git grep -E` IS POSIX ERE AND REJECTS `(?:...)` OUTRIGHT.** ### The first run of this file
# ### handed it a Python pattern; every invocation died with `Invalid preceding regular expression`,
# ### the caller read a non-zero exit as ### **NO MATCHES**, and the sweep reported `0 FOUND ON ANY
# ### REF` ### across 270 refs. ### **A SEARCH THAT CANNOT RUN LOOKS EXACTLY LIKE A SEARCH THAT FOUND
# ### ### NOTHING**, and only a contradiction with `b377`'s own record exposed it.
# ### ### **SO THE PATTERN HANDED TO `git` IS POSIX, AND A FATAL EXIT IS AN ERROR AND NOT AN ANSWER.**
KEYWORD_POSIX = r'(theorem|lemma|def|abbrev|instance|structure|inductive|axiom)'
LEAD_POSIX = (r'^[ \t]*(@\[[^]]*\][ \t]*)?'
              r'(private[ \t]+|protected[ \t]+|noncomputable[ \t]+|partial[ \t]+|unsafe[ \t]+)*')


def decl_re(last):
    """### **THE DECLARATION PATTERN FOR ONE NAME'S LAST SEGMENT.**"""
    return re.compile(LEAD + KEYWORD + r'[ \t]+' + re.escape(last) + r'\b', re.M)


def split(name):
    """### `(namespace_or_None, last_segment)` ### -- the only place the two dialects differ."""
    return (name.rsplit('.', 1)[0], name.rsplit('.', 1)[1]) if '.' in name else (None, name)


def declares(text, name, path=''):
    """### **DOES THIS FILE DECLARE THIS NAME, UNDER EITHER CONVENTION?**

    ### ### **BARE:** ### a declaration of the name.
    ### ### **DOTTED:** ### a declaration of the last segment ### **AND** ### the namespace confirmed,
    ### either by an `open`/`namespace` line in the same file or by the file's own path.
    """
    ns, last = split(name)
    if not decl_re(last).search(text):
        return False
    if ns is None:
        return True
    if re.search(r'^[ \t]*namespace[ \t]+' + re.escape(ns) + r'\b', text, re.M):
        return True
    if re.search(r'^[ \t]*namespace[ \t]+' + re.escape(ns.split('.')[0]) + r'\b', text, re.M):
        return True
    return ns.replace('.', '/') in path.replace('\\', '/') or ns in path.replace('/', '.')


# ---- ADDITION TWO'S FIXTURES, INCLUDING THE DISCRIMINATION ARM -------------------------------------
FIX_FILE = ('namespace SIDELvConservation' + chr(10)
            + 'theorem residue_irreducible : True := trivial' + chr(10)
            + 'lemma edge_drift_nonneg : True := trivial' + chr(10)
            + 'end SIDELvConservation' + chr(10))


def fixtures(verbose=True):
    """### **BOTH POLARITIES ON BOTH DIALECTS, PLUS THE ARM THAT PROVES IT STILL SAYS NO.**"""
    P = 'SIDELvConservation/Residue.lean'
    cases = [
        ('BARE, present            -- accepts', declares(FIX_FILE, 'residue_irreducible', P), True),
        ('DOTTED, present          -- accepts',
         declares(FIX_FILE, 'SIDELvConservation.residue_irreducible', P), True),
        ('BARE, absent             -- ### REFUSES',
         declares(FIX_FILE, 'no_such_terminal_here', P), False),
        ('DOTTED, absent           -- ### REFUSES',
         declares(FIX_FILE, 'SIDELvConservation.no_such_terminal_here', P), False),
        ('### **DOTTED, right name WRONG namespace -- REFUSES**',
         declares(FIX_FILE, 'SomeOtherSpace.residue_irreducible', 'Other/Thing.lean'), False),
        ('a mention that is not a declaration -- ### REFUSES',
         declares('-- we discuss residue_irreducible in prose' + chr(10), 'residue_irreducible', P),
         False),
        ('a prefix of a real name  -- ### REFUSES',
         declares(FIX_FILE, 'residue_irr', P), False),
    ]
    ok = all(got is want for _l, got, want in cases)
    if verbose:
        for lbl, got, want in cases:
            print('      %-56s got %-5s want %-5s  %s'
                  % (lbl, got, want, 'ok' if got is want else '### MISMATCH ###'))
    return ok, [dict(case=l, got=bool(g), want=w) for l, g, w in cases]


# =====================================================================================================
LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace')


def kernels():
    out = []
    for n in sorted(os.listdir(DRIVE)):
        p = os.path.join(DRIVE, n)
        if n.startswith('SIDE-') and os.path.isdir(os.path.join(p, '.git')):
            out.append((n, p))
    return out


def refs_of(repo):
    """### **ENUMERATED LIVE. ### NEVER TYPED.** ### Returns `{sha: [refnames]}` and the raw list."""
    r = git(repo, 'for-each-ref', '--format=%(objectname) %(refname)')
    by_sha, names = {}, []
    for ln in r.stdout.split(chr(10)):
        ln = ln.strip()
        if not ln or ' ' not in ln:
            continue
        sha, name = ln.split(' ', 1)
        if name.endswith('/HEAD'):
            continue
        by_sha.setdefault(sha, []).append(name)
        names.append(name)
    return by_sha, names


def main():
    R = json.load(io.open(os.path.join(D, 'b378_reads.json'), encoding='utf-8'))
    UN = R['unresolved']
    NAMES = [u['name'] for u in UN]
    LASTS = sorted(set(split(n)[1] for n in NAMES))

    rec('=' * 100)
    rec('b378 -- ADDITION ONE AND ADDITION TWO. ### **EVERY REF, AND BOTH CONVENTIONS.**')
    rec('=' * 100)
    rec('')
    rec('-' * 100)
    rec('  ### ADDITION TWO (a) -- THE MATCHER, FIXTURED BEFORE IT IS USED.')
    rec('-' * 100)
    ok, fx = fixtures(False)
    for c in fx:
        rec('      %-56s got %-5s want %-5s  %s'
            % (c['case'], c['got'], c['want'], 'ok' if c['got'] is c['want'] else '### MISMATCH'))
    rec('    ### ### **FIXTURE VERDICT : %s**'
        % ('BOTH DIALECTS ACCEPTED, AND IT STILL REFUSES' if ok else '### FAILED'))
    rec('    ### **THE DISCRIMINATION ARM IS THE LAST THREE CASES.** ### A matcher that accepts')
    rec('    ### everything is not a matcher; widening one that was too narrow is exactly the moment')
    rec('    ### to prove it did not become too wide.')
    if not ok:
        run_clock.write(D, 'b378_terminals_notes', LINES)
        return 2

    # ------------------------------------------------------------------ THE REFS, ENUMERATED LIVE
    rec('')
    rec('-' * 100)
    rec('  ### ADDITION ONE (a) -- THE REFS, ENUMERATED LIVE FROM EACH REPOSITORY.')
    rec('-' * 100)
    KS = kernels()
    refmap, total_refs, total_trees = {}, 0, 0
    for kn, kp in KS:
        by_sha, names = refs_of(kp)
        refmap[kn] = dict(path=kp, by_sha=by_sha, refs=names)
        total_refs += len(names)
        total_trees += len(by_sha)
    rec('    kernels on disk : %d' % len(KS))
    rec('    ### **REFS ENUMERATED : %d ### / ### DISTINCT COMMITS BEHIND THEM : %d**'
        % (total_refs, total_trees))
    rec('    ### ### **`b377` SEARCHED %d REFS -- ONE PER KERNEL. ### THIS ACT SEARCHES %d.**'
        % (len(KS), total_refs))
    rec('    ### refs pointing at the same commit are searched ONCE and reported for every ref that')
    rec('    ### shares it. ### **DEDUPLICATION BY COMMIT IS NOT A SAMPLE.**')
    rec('')
    for kn, _kp in KS:
        nm = refmap[kn]['refs']
        if len(nm) > 2:
            rec('      %-34s %2d refs / %2d commits  %s'
                % (kn, len(nm), len(refmap[kn]['by_sha']),
                   ', '.join(x.replace('refs/heads/', '').replace('refs/tags/', 'tag:')
                             for x in nm if not x.startswith('refs/remotes/'))[:60]))

    # ------------------------------------------------------------------------ THE SEARCH, ONE PASS
    rec('')
    rec('-' * 100)
    rec('  ### ADDITION ONE (b) -- THE SEARCH, ACROSS EVERY REF.')
    rec('-' * 100)
    alt = '|'.join(re.escape(x) for x in LASTS)
    pat = LEAD + KEYWORD + r'[ \t]+(' + alt + r')\b'
    # ### **THE PATTERN HANDED TO `git grep` IS POSIX**, per the note above.
    gpat = LEAD_POSIX + KEYWORD_POSIX + r'[ \t]+(' + alt + r')\b'
    found, gerrors = {}, []
    for kn, _kp in KS:
        kp = refmap[kn]['path']
        for sha, names in refmap[kn]['by_sha'].items():
            r = git(kp, 'grep', '-n', '-E', gpat, sha)
            # ### `git grep` EXITS 1 FOR "no matches" AND >1 FOR "I could not search".
            # ### ### **CONFLATING THOSE IS HOW A BROKEN SWEEP REPORTS A CLEAN ONE.**
            if r.returncode > 1:
                gerrors.append(dict(kernel=kn, sha=sha[:12], code=r.returncode,
                                    err=(r.stderr or '').strip()[:160]))
                continue
            if r.returncode != 0 or not r.stdout.strip():
                continue
            for ln in r.stdout.split(chr(10)):
                if not ln.strip() or ':' not in ln:
                    continue
                parts = ln.split(':', 3)
                if len(parts) < 4:
                    continue
                path, code = parts[1], parts[3]
                body = None
                for nm in NAMES:
                    ns, last = split(nm)
                    if not decl_re(last).search(code):
                        continue
                    if ns is not None:
                        if body is None:
                            body = git(kp, 'show', sha + ':' + path).stdout
                        if not declares(body, nm, path):
                            continue
                    found.setdefault(nm, []).append(
                        dict(kernel=kn, sha=sha[:12], refs=names, path=path,
                             line=int(parts[2]), code=code.strip()[:120]))
    rec('    identifiers carried forward : %d' % len(NAMES))
    rec('    ### **IDENTIFIERS FOUND ON SOME REF : %d**' % len(found))
    rec('    ### ### **SEARCHES THAT COULD NOT RUN : %d** %s'
        % (len(gerrors), (gerrors[0]['err'][:80] if gerrors else '')))
    rec('')
    rec('    ### **THE POSITIVE CONTROL. ### A SEARCH THAT CANNOT RUN LOOKS EXACTLY LIKE A SEARCH')
    rec('    ### ### THAT FOUND NOTHING**, and the first run of this file reported `0` across 270')
    rec('    ### refs because `git grep` was rejecting a Python-only pattern and the caller read the')
    rec('    ### fatal exit as an answer. ### **SO THE SWEEP NOW PROVES ITSELF CAPABLE BEFORE IT')
    rec('    ### ### REPORTS AN ABSENCE.**')
    CTRL = 'residue_irreducible'
    ctrl_hits = []
    for _kn, _kpx in KS:
        _kp = refmap[_kn]['path']
        for _sha, _names in refmap[_kn]['by_sha'].items():
            _r = git(_kp, 'grep', '-l', '-E',
                     LEAD_POSIX + KEYWORD_POSIX + r'[ \t]+' + CTRL + r'\b', _sha)
            if _r.returncode == 0 and _r.stdout.strip():
                ctrl_hits.append(dict(kernel=_kn, refs=_names, sha=_sha[:12]))
    ctrl_nonmain = [h for h in ctrl_hits if not any(x.endswith('/main') for x in h['refs'])]
    rec('    ### control name : `%s`' % CTRL)
    rec('    ### ### **FOUND ON %d COMMIT(S), OF WHICH %d ARE NOT `main` : %s**'
        % (len(ctrl_hits), len(ctrl_nonmain),
           'CONTROL HELD' if (ctrl_hits and ctrl_nonmain) else '### CONTROL FAILED ###'))
    for h in ctrl_nonmain[:3]:
        rec('    ###   %s @ %s' % (h['kernel'], ', '.join(
            x.replace('refs/heads/', '') for x in h['refs'])[:70]))
    ctrl_ok = bool(ctrl_hits and ctrl_nonmain and not gerrors)
    if not ctrl_ok:
        rec('    ### ### ### **REFUSING TO REPORT AN ABSENCE FROM A SEARCH THAT HAS NOT PROVED IT CAN')
        rec('    ### ### ### FIND A PRESENCE.**')
        run_clock.write(D, 'b378_terminals_notes', LINES)
        return 2

    # --------------------------------------------------------------------------------- MATHLIB
    rec('')
    rec('-' * 100)
    rec('  ### ADDITION ONE (c) -- AND `Mathlib`, WHICH IS ALSO ON THIS DISK.')
    rec('-' * 100)
    ml = None
    for kn, kp in KS:
        cand = os.path.join(kp, '.lake', 'packages', 'mathlib')
        if os.path.isdir(cand):
            ml = cand
            break
    mfound = {}
    if ml:
        rec('    mathlib package read at : %s' % os.path.relpath(ml, DRIVE))
        big = re.compile(pat, re.M)
        nfiles = 0
        for dp, dn, fn in os.walk(os.path.join(ml, 'Mathlib')):
            for f in fn:
                if not f.endswith('.lean'):
                    continue
                nfiles += 1
                fp = os.path.join(dp, f)
                try:
                    txt = io.open(fp, encoding='utf-8', errors='replace').read()
                except OSError:
                    continue
                if not big.search(txt):
                    continue
                for nm in NAMES:
                    if nm in mfound:
                        continue
                    if declares(txt, nm, os.path.relpath(fp, ml)):
                        mfound[nm] = os.path.relpath(fp, ml).replace(os.sep, '/')
        rec('    mathlib `.lean` files read : %d' % nfiles)
        rec('    ### **IDENTIFIERS DECLARED IN `Mathlib` : %d**' % len(mfound))
    else:
        rec('    ### **NO `Mathlib` PACKAGE FOUND ON DISK** -- the mathlib category cannot be')
        rec('    ### distinguished and every such name stays NOT-FOUND, which OVERSTATES the defect.')

    # ------------------------------------------------------------- NAMES THAT ARE CORPUS DOCUMENTS
    docnames = set()
    for dp, dn, fn in os.walk(PP):
        if '.git' in dp:
            continue
        for f in fn:
            if f.endswith('.md'):
                docnames.add(f[:-3])

    # --------------------------------------------------------------------------- THE HELD BRANCH
    rec('')
    rec('-' * 100)
    rec('  ### ADDITION ONE (d) -- THE HELD BRANCH THE DOCUMENT NAMES IN ITS OWN TEXT.')
    rec('-' * 100)
    RES = os.path.join(PP, 'phase1.5', 'proofs', 'THE_RESIDUE_OF_RH.md')
    hn, hline = AF.find(RES, 'The seven branch artifacts and the edge lemma, at their pins with '
                             '`#print axioms` profiles,')
    rec('    ### **THE DOCUMENT`S OWN SENTENCE**, `THE_RESIDUE_OF_RH.md` line %d:' % hn)
    for seg in re.findall(r'.{1,92}(?:\s|$)', hline.strip()):
        if seg.strip():
            rec('      | %s' % seg.rstrip())
    HELD = 'word-pairing-interface'
    heldk = 'SIDE-lv-conservation'
    heldrefs = [x for x in refmap.get(heldk, {}).get('refs', []) if HELD in x]
    rec('    ### the branch it names : `%s` in `%s`' % (HELD, heldk))
    rec('    ### refs matching that name, enumerated live : %s' % (heldrefs or 'NONE'))
    held_hits = {}
    for nm, hits in found.items():
        for h in hits:
            if h['kernel'] == heldk and any(HELD in x for x in h['refs']):
                held_hits.setdefault(nm, h)
    rec('    ### **IDENTIFIERS FOUND ON THAT HELD BRANCH : %d**' % len(held_hits))

    # ------------------------------------------------------------------- THE CLASSIFICATION, ONE EACH
    rec('')
    rec('-' * 100)
    rec('  ### ADDITION ONE (e) -- THE CORRECTED CLASSIFICATION. ### **EXACTLY ONE PER IDENTIFIER.**')
    rec('-' * 100)
    rows, tally = [], {}
    for u in UN:
        nm = u['name']
        hits = found.get(nm, [])
        onmain = [h for h in hits if any(x.endswith('/main') for x in h['refs'])]
        offmain = [h for h in hits if not any(x.endswith('/main') for x in h['refs'])]
        kset = sorted(set(h['kernel'] for h in hits))
        if hits and len(kset) > 1:
            # ### **`b377`'S OWN RULE, CARRIED:** ### a name declared in more than one kernel is not a
            # ### terminal a document can cite, and reading `hits[0]` would hide that.
            cls = '### **FOUND-BUT-IN MORE THAN ONE KERNEL**'
            where = 'declared in %d kernels : %s' % (len(kset), ', '.join(kset))
        elif hits:
            cls = ('FOUND-AT-main' if onmain else '### **FOUND-ON-A-NON-main-REF**')
            h = (onmain or offmain)[0]
            where = '%s @ %s (%s)' % (h['kernel'], h['refs'][0].replace('refs/heads/', ''), h['path'])
        elif nm in mfound:
            cls = 'A-Mathlib-NAME'
            where = 'Mathlib/%s' % mfound[nm]
        elif nm in docnames or nm.replace('_', '') in {d.replace('_', '') for d in docnames}:
            cls = 'NAMES-A-CORPUS-DOCUMENT'
            where = 'a `.md` in PLACE-papers, not a terminal'
        else:
            cls = 'NOT-FOUND-ON-ANY-REF-SEARCHED'
            where = 'none of %d refs across %d kernels, nor Mathlib' % (total_refs, len(KS))
        tally[cls] = tally.get(cls, 0) + 1
        rows.append(dict(name=nm, doc=u['doc'], prior_kind=u['kind'], classification=cls,
                         where=where, hits=len(hits), kernels=kset, n_kernels=len(kset),
                         refs_found_on=sorted(set(r for h in hits for r in h['refs'])),
                         on_main=len(onmain), off_main=len(offmain)))
    rec('    %-46s %-32s %s' % ('identifier', 'classification', 'where'))
    rec('    %s' % ('-' * 94))
    for r in rows:
        rec('    %-46s %-32s %s' % (r['name'][:46], r['classification'][:32], r['where'][:40]))
    rec('')
    rec('    ### ### **THE TALLY : %s**' % tally)
    still = tally.get('NOT-FOUND-ON-ANY-REF-SEARCHED', 0)
    rec('    ### ### ### **`b377` REPORTED `%d` UNRESOLVED AT ONE REF. ### THAT WAS AN UPPER BOUND'
        % len(UN))
    rec('    ### ### ### TAKEN AT ONE REF, AND IT IS SAID HERE IN THOSE WORDS.**')
    rec('    ### ### **THE CORRECTED COUNT OF IDENTIFIERS NO SEARCHED REF DECLARES : %d.**' % still)

    # ---------------------------------------------------- ADDITION TWO: THE CONVENTION SWEEP
    rec('')
    rec('-' * 100)
    rec('  ### ADDITION TWO (b) -- WHICH CONVENTION EACH CITING DOCUMENT USES.')
    rec('-' * 100)
    BR = json.load(io.open(os.path.join(D, 'b377_branch.json'), encoding='utf-8'))
    conv = []
    for r in BR['six']:
        bare = [c for c in r['candidates'] if '.' not in c]
        dotted = [c for c in r['candidates'] if '.' in c]
        which = ('BARE ONLY' if bare and not dotted else
                 'DOTTED ONLY' if dotted and not bare else
                 'BOTH' if bare and dotted else 'NEITHER -- it names none')
        conv.append(dict(file=r['file'], bare=len(bare), dotted=len(dotted), convention=which))
        rec('    %-34s bare %-3d dotted %-3d  ### **%s**'
            % (os.path.basename(r['file'])[:34][:-3], len(bare), len(dotted), which))
    rec('')
    rec('    ### ### **BOTH DIALECTS ARE CORRECT IN THEIR OWN TERMS AND NO DOCUMENT IS REWRITTEN BY')
    rec('    ### ### THIS ACT.** ### An older document naming `residue_irreducible` is not wrong; it')
    rec('    ### ### is writing the convention its era wrote.')
    rec('')
    rec('    ### **WHAT THE EARLIER PREDICATE`S NARROWNESS COST, STATED AND NOT ESTIMATED:**')
    rec('    ### `b376`s axis-B predicate required a ### **DOTTED** ### terminal, inside a row also')
    rec('    ### carrying kernel, pin and grade. ### A table in the BARE dialect could not satisfy it')
    rec('    ### however complete it was.')
    rec('    ### ### **THE COST IS NOT HYPOTHETICAL: ### IT SELECTED THE SIX.** ### `b377` inherited')
    rec('    ### that verdict as its whole population, and then found that several of the six already')
    rec('    ### carried a correspondence table -- which is the same defect surfacing twice.')
    rec('    ### **WHERE ELSE IN THE RECORD IT MAY HAVE COST THE SAME, NAMED AND NOT SWEPT:**')
    rec('    ###   ### **`b376`S WHOLE AXIS-B COLUMN** -- `303` documents scored `B-` on that')
    rec('    ###     predicate, and any of them writing the BARE dialect is scored as an absence.')
    rec('    ###     ### **THAT COLUMN IS NOT RE-MEASURED HERE AND IS NAMED AS SUSPECT.**')
    rec('    ###   ### **`b376`S `A+B+` QUADRANT AND EVERY COUNT DERIVED FROM IT**, including the')
    rec('    ###     certification/rubric overlap `b376` printed BY DOCUMENT.')
    rec('    ###   ### **AND `b375`S EXISTING-CENSUS COMPARISON**, which used a heading test rather')
    rec('    ###     than a terminal test and is therefore ### **NOT** ### affected by this defect --')
    rec('    ###     said so that the suspicion is bounded rather than free-floating.')
    rec('=' * 100)

    p = run_clock.write(D, 'b378_terminals_notes', LINES)
    io.open(os.path.join(D, 'b378_terminals.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(fixtures_ok=ok, fixtures=fx, control_ok=ctrl_ok,
                        control_name=CTRL, control_hits=len(ctrl_hits),
                        control_non_main=len(ctrl_nonmain), grep_errors=gerrors,
                        kernels=len(KS), refs=total_refs,
                        commits=total_trees, prior_refs_searched=len(KS),
                        carried=len(UN), rows=rows, tally=tally,
                        still_not_found=still, mathlib=mfound, mathlib_root=(ml or None),
                        held_branch=dict(name=HELD, kernel=heldk, refs=heldrefs,
                                         line=hn, sentence=hline.strip(),
                                         identifiers_found=sorted(held_hits)),
                        conventions=conv,
                        found={k: dict(hits=len(v),
                                       kernels=sorted(set(h['kernel'] for h in v)),
                                       refs=sorted(set(r for h in v for r in h['refs'])),
                                       sample=v[:3])
                               for k, v in found.items()},
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
