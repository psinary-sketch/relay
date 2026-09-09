# -*- coding: utf-8 -*-
"""b392_components.py -- (R19) AND (R20) WRITTEN, AND THE DEPOSIT CENSUS.

### ### **BOTH AMENDMENTS ARE ADDITIVE AND EVERY PRIOR LINE IS PRESERVED BYTE-FOR-BYTE**, measured
### against the pre-act blob and never within the run.
### ### **THE CENSUS IS TAKEN FROM THE CORPUS'S OWN RECORD.** ### The platform answered nothing on
### six routes at `b389` and ### **IS NOT ASKED AGAIN**; every figure here is the corpus's claim
### about itself and is labelled so.
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
TAX = os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
REGISTRY = os.path.join(PP, 'REGISTRY.md')
README = os.path.join(PP, 'README.md')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
OUT = os.path.join(D, 'b392_components.txt')
R19_MARK = '<!-- b392 (R19) THE FINISHED KEYSTONE AS A NAMED CLASS, 2026-09-09 -->'
R20_MARK = '<!-- b392 (R20) THE DEPOSIT RULE, 2026-09-09 -->'
R20_PTR = '<!-- b392 (R20) POINTER, 2026-09-09 -->'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []


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


def append_block(rel, mark, block):
    """### **APPEND, THEN PROVE THE PRIOR TEXT SURVIVED AGAINST THE PRE-ACT BLOB.**"""
    full = os.path.join(PP, rel.replace('/', os.sep))
    pre = blob(rel)
    cur = io.open(full, encoding='utf-8', newline='').read()
    if mark in cur:
        rec('      ### ALREADY FILED -- the mark is present. ### NOTHING APPENDED.')
    else:
        io.open(full, 'a', encoding='utf-8', newline=chr(10)).write(
            chr(10).join(block) + chr(10))
    after = io.open(full, encoding='utf-8', newline='').read().replace(chr(13) + chr(10), chr(10))
    pl, al = pre.split(chr(10)), after.split(chr(10))
    prefix = after.startswith(pre.rstrip(chr(10)))
    survived = sum(1 for k, x in enumerate(pl) if k < len(al) and al[k] == x)
    a, d = numstat(rel)
    rec('      prior lines %d, all present and byte-identical : %s ; appended below everything : %s'
        % (len(pl), survived == len(pl), prefix))
    rec('      ### **DIFF AGAINST THE PRE-ACT BLOB : `+%d` / `-%d`. ### DELETIONS MUST BE `0`.**'
        % (a, d))
    subprocess.run(['git', '-C', PP, 'add', '--', rel], capture_output=True)
    return dict(rel=rel, prior=len(pl), survived=survived, prefix=prefix, added=a, deleted=d,
                ok=(survived == len(pl) and prefix and d == 0))


# ==================================================================================================
#  COMPONENT 1 -- (R19).
# ==================================================================================================
def component1():
    bar('=')
    rec('  ### COMPONENT 1 -- `(R19)`: THE FINISHED KEYSTONE IS A NAMED CLASS.')
    bar('=')
    # ### **THE ANCHORS ARE READ FROM THE PRE-ACT BLOB, NOT THE LIVE FILE.** ### This act's own
    # ### block QUOTES the sentence it anchors on, so on a re-run the live file carries it twice
    # ### and the anchor refuses as AMBIGUOUS. ### **A SWEEP EXCLUDES EVERYTHING ITS OWN ACT
    # ### ### WRITES** (`b368`) -- and so must an anchor.
    def infile(text, hint, label):
        hits = [(i, ln) for i, ln in enumerate(text.split(chr(10)), 1) if hint in ln]
        if len(hits) != 1:
            raise SystemExit('### %s: %d matches in the pre-act blob' % (label, len(hits)))
        return hits[0]
    pretax = blob('phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md')
    premap = blob('SPIRAL_MAP.md')
    ti, tln = infile(pretax, '**Tier C — Cluster-synthesis.**', 'tier C')
    ri, rln = infile(pretax, 'The formation-universality over-claim (June 2026) happened because a',
                     'the June 2026 failure')
    mi, mln = infile(premap, "b186's SYNTHESIS/NOTES/LEDGER SCHEME IS RETIRED", 'the retirement')
    rec('  ### **THE TWO THINGS THE GUARD MUST CARRY, READ AT THEIR OWN LINES BEFORE IT IS'
        ' WRITTEN:**')
    rec('  ###   `THE_DOCUMENT_CLASS_TAXONOMY.md` line %d -- the failure the tiers prevent:' % ri)
    rec('      > %s' % flat(rln, 330))
    rec('  ###   `SPIRAL_MAP.md` line %d -- the scheme retired for spanning them:' % mi)
    rec('      > %s' % flat(mln, 330))
    rec('  ###   `THE_DOCUMENT_CLASS_TAXONOMY.md` line %d -- Tier C`s citation rule, the one the'
        % ti)
    rec('  ###   new class must not loosen:')
    rec('      > %s' % flat(tln[tln.find('*Citation rule:*'):] if '*Citation rule:*' in tln
                            else tln, 220))
    rec()
    block = [
        '', R19_MARK, '',
        ('## The fifth class — RULING `(R19)`, the author’s, 2026-09-09 '
         '*(added; nothing above this line is edited)*'),
        '',
        ('**Tier KC — the finished keystone.** A document that **synthesizes a subject cluster** '
         '*and* **carries the verification apparatus**. It is a conjunction of what Tier K and '
         'Tier C each do alone, and it is named because the corpus writes such documents and had '
         'no word for them.'),
        '',
        ('*Obligation.* **Every load-bearing claim is stated clearly in the body** and **carried '
         'by a row in a correspondence table placed after the front matter, where a reader meets '
         'it** — not appended where only a returning reader will find it. **Each row names what '
         'backs it in the front door’s own vocabulary** — `kernel-verified`, `theorem-supported`, '
         '`argument-supported`, `computationally-verified`, `synthesis-suggested`, '
         '`milestone-open`, `statement-grade` — and **a claim whose backing is not '
         'machine-checked says so in the row**. Plus **glossary, bibliography, and other tables '
         'as the document needs them**: the furniture is part of the class, because a finished '
         'keystone is a document a stranger can use.'),
        '',
        ('*Citation rule, written so a reader who has never seen this taxonomy can obey it:* '
         '**A SYSTEMATIC SYNTHESIS WITH A VERIFICATION CONCORDANCE — CITE THE SYNTHESIS FOR '
         'ORIENTATION, CITE EACH CONCORDANCE ROW AT ITS STATED GRADE.**'),
        '',
        ('> ### **THE GUARD, WRITTEN INTO THE CLASS AND NOT BESIDE IT: THIS CLASS CONFERS NO '
         'CITATION LICENSE THE TWO TIERS DO NOT ALREADY CONFER.** *It names a **conjunction** and '
         'a **furniture obligation**. Nothing in it permits a synthesis conclusion to be cited as '
         'certification. A row at `kernel-verified` is cited as Tier K allows; a synthesis '
         'relationship is cited as Tier C allows — **for orientation, never as certification of '
         'the relationships it draws**. The conjunction adds a table and a discipline; it adds no '
         'warrant.*'),
        '',
        ('> **AND THE GUARD IS THERE BECAUSE THE CORPUS HAS BEEN HURT TWICE BY EXACTLY THIS '
         'SHAPE.** *First, the failure these tiers were built to prevent, in this document’s own '
         'rationale:* “**The formation-universality over-claim (June 2026) happened because a '
         'Tier-C synthesis panel … was read and cited as a Tier-K certification. The tuple was a '
         'synthesis *coordinate*; it was cited as a *proven invariant*.**” *Second, the scheme '
         'retired in August for spanning the tiers, recorded in `SPIRAL_MAP.md`’s head:* “**b186’s '
         'SYNTHESIS/NOTES/LEDGER SCHEME IS RETIRED, 2026-08-26 (b190).** *Reason: … its '
         '“SYNTHESIS” class spanned Tier K and Tier C at once —* **collapsing the very '
         'distinction the standing taxonomy exists to enforce.**”'),
        '',
        ('> ### **SO THE DIFFERENCE BETWEEN `Tier KC` AND THE RETIRED SCHEME IS THE WHOLE POINT '
         'OF THE CLASS.** *The retired scheme spanned the tiers by **dissolving** them — one '
         'class where two rules had been. `Tier KC` spans them by **carrying both rules at once**: '
         'the body’s synthesis is cited as Tier C is cited, and each concordance row is cited as '
         'Tier K is cited, at the grade the row states. **A class that collapses the distinction '
         'is retired; a class that keeps both sides of it is a class.**'),
        '',
        ('**No document is reclassified into `Tier KC` by this ruling, and no candidate is named '
         'here.** Placement is a separate act and a separate decision.'),
        '',
    ]
    r = append_block('phase1.5/method/THE_DOCUMENT_CLASS_TAXONOMY.md', R19_MARK, block)
    now = io.open(TAX, encoding='utf-8', errors='replace').read()
    guard = 'CONFERS NO CITATION LICENSE THE TWO TIERS DO NOT ALREADY CONFER' in now
    q1 = 'formation-universality over-claim (June 2026)' in now
    q2 = 'SYNTHESIS/NOTES/LEDGER SCHEME IS RETIRED' in now
    cite = ('A SYSTEMATIC SYNTHESIS WITH A VERIFICATION CONCORDANCE' in now)
    noplace = 'No document is reclassified into `Tier KC` by this ruling' in now
    rec()
    rec('  ### ### **THE GUARD IS IN THE CLASS`S OWN TEXT : %s**' % guard)
    rec('  ### ### **THE JUNE 2026 OVER-CLAIM QUOTED : %s ; THE AUGUST 2026 RETIREMENT QUOTED : %s**'
        % (q1, q2))
    rec('  ### ### **THE CITATION RULE IS WRITTEN FOR A STRANGER : %s**' % cite)
    rec('  ### ### **NO DOCUMENT RECLASSIFIED, AND THE CLASS SAYS SO : %s**' % noplace)
    rec('  ### ### ### **AND THE CLASS STATES WHAT SEPARATES IT FROM THE RETIRED SCHEME:** ### the')
    rec('  ### ### ### retired one ### **DISSOLVED** ### the tiers; this one ### **CARRIES BOTH')
    rec('  ### ### ### RULES AT ONCE.** ### **A CLASS THAT COLLAPSES THE DISTINCTION IS RETIRED; A')
    rec('  ### ### ### CLASS THAT KEEPS BOTH SIDES OF IT IS A CLASS.**')
    return dict(file=r, guard=guard, quoted_failure=q1, quoted_retirement=q2,
                citation_rule=cite, no_placement=noplace,
                ok=(r['ok'] and guard and q1 and q2 and cite and noplace))


# ==================================================================================================
#  COMPONENT 2 -- (R20) AND THE DEPOSIT CENSUS.
# ==================================================================================================
DOI = re.compile(r'10\.5281/zenodo\.(\d+)')
ELIDED = re.compile(r'[…\.]{1,3}(\d{8})')
HIST = re.compile(r'(?i)(supersede|superseded|prior|lineage|historical|affected deposits|'
                  r'errat|withdraw|replaced|former|→)')
SKIP = ('.git', 'archive', 'outputs')


def corpus_files():
    for dp, dn, fn in os.walk(PP):
        rel = os.path.relpath(dp, PP).replace(os.sep, '/')
        if rel.split('/')[0] in SKIP:
            continue
        for f in sorted(fn):
            if f.endswith('.md'):
                yield (rel + '/' + f if rel != '.' else f), os.path.join(dp, f)


def component2():
    bar('=')
    rec('  ### COMPONENT 2 -- `(R20)`: THE DEPOSIT RULE, WITH ITS CURRENCY OBLIGATION.')
    bar('=')
    ni, nln = AF.find(README, '**Deposit note (`day1/`).** Citable deposits:')
    rec('  ### **THE DEPOSIT NOTE, READ AT ITS OWN LINE** -- `README.md` line %d:' % ni)
    rec('      > %s' % flat(nln, 430))
    listed = set(DOI.findall(nln))
    rec('  ### ### **DOIs IT NAMES : `%d`** ### -- three citable records with their concepts.'
        % len(listed))
    rec()
    block = [
        '', R20_MARK, '',
        ('## THE DEPOSIT RULE — RULING `(R20)`, the author’s, 2026-09-09 '
         '*(added; no row, lineage or deposit figure above this line is edited)*'),
        '',
        '**WHAT DEPOSITS, AND WHY.** Three limbs, and nothing else deposits by default:',
        '',
        ('1. **A manuscript wave deposits with its companion papers.** The wave is the unit; a '
         'paper does not go alone and does not stay behind.'),
        ('2. **A kernel deposits when a published claim cites its terminals.** The trigger is the '
         'citation, not the tag: a kernel nobody has cited in a published claim has nothing to '
         'be citable *for*.'),
        ('3. **A pre-registered search deposits because its registration committed to publishing '
         'every outcome.** The commitment is made before the result is known, so a null outcome '
         'deposits exactly as a positive one does.'),
        '',
        ('> ### **THE CURRENCY OBLIGATION.** *Every deposited record **either** sits at a version '
         'a citable claim uses, **or** carries a note saying it is historical. There is no third '
         'state. A record that is neither current nor marked is a record a reader can cite '
         'without knowing it has been superseded — which is the failure the deposit line exists '
         'to prevent.*'),
        '',
        ('**WHERE THIS RULE LIVES.** Here, in `REGISTRY.md`, because the registry is the corpus’s '
         'source of truth for deposits — the `d1-1` row, the per-kernel lineages and the Day-1 '
         'deposit history are all here. `README.md`’s deposit note **points at this rule** and '
         'does not restate it: **the source of truth first, the front door pointing at it.**'),
        '',
        ('*Recorded with its reason, as the corpus’s rules are: this rule is **descriptive before '
         'it is prescriptive**. The three limbs are what the corpus already did — the monograph '
         'went as a wave, `SIDE-lv-conservation` went because published claims cite its '
         'terminals, and the T7 matched-arc search went because its registration committed it. '
         'Writing it down changes no past deposit; it makes the next one checkable.*'),
        '',
    ]
    r1 = append_block('REGISTRY.md', R20_MARK, block)
    ptr = [
        '', R20_PTR, '',
        ('**The deposit rule is `REGISTRY.md` → “THE DEPOSIT RULE — RULING `(R20)`”.** *What '
         'deposits, and the currency obligation every deposited record carries, are stated there '
         'and are not restated here: the registry is the source of truth for deposits and this '
         'note points at it.*'),
        '',
    ]
    r2 = append_block('README.md', R20_PTR, ptr)
    rec()
    bar()
    rec('  ### ### **THE CENSUS, FROM THE CORPUS`S OWN RECORD AND NOT FROM THE PLATFORM.**')
    bar()
    rec('  ### **THE PLATFORM ANSWERED NOTHING ON SIX ROUTES AT `b389` AND IS NOT ASKED AGAIN BY')
    rec('  ### ### THIS ACT.** ### **EVERY FIGURE BELOW IS THE CORPUS`S OWN CLAIM ABOUT ITSELF**,')
    rec('  ### and is labelled so rather than presented as a verified state.')
    rec()
    ctx, elided = {}, {}
    for pth, full in corpus_files():
        for i, ln in enumerate(io.open(full, encoding='utf-8', errors='replace').read()
                               .split(chr(10)), 1):
            for m in DOI.finditer(ln):
                ctx.setdefault(m.group(1), []).append((pth, i, ln))
            for m in ELIDED.finditer(ln):
                if 'zenodo' in ln.lower() or 'DOI' in ln or 'concept' in ln.lower():
                    elided.setdefault(m.group(1), []).append((pth, i, ln))
    # ### **A DOI IS NOT A RECORD, AND A COUNT THAT CONFLATES THEM DESCRIBES NEITHER.** ### The
    # ### deposit note names `6` DOIs -- THREE VERSION RECORDS AND THEIR THREE CONCEPT DOIs -- and
    # ### a first form of this component reported that as `6` citable records.
    rec('  ### ### **DOIs THE CORPUS NAMES : `%d`.**' % len(ctx))
    rec('  ### ### **THE DEPOSIT NOTE NAMES `%d` OF THEM: ### **`3` VERSION RECORDS AND THEIR `3`'
        % len(listed))
    rec('  ### ### CONCEPT DOIs.** ### **A DOI IS NOT A RECORD**, and a count that conflates them')
    rec('  ### ### describes neither.')
    rec('  ### ### **UNLISTED DOIs : `%d`.**' % (len(ctx) - len(listed)))
    rec()
    rec('  ### **THE THREE CITABLE RECORDS AGAINST THE THREE LIMBS, ONE FOR ONE:**')
    rec('  ###   limb 1, a manuscript wave      -> the monograph, Zenodo `v1.1.2` `21539167`')
    rec('  ###   limb 2, a kernel a claim cites -> `SIDE-lv-conservation v0.10.0` `21539068`')
    rec('  ###   limb 3, a pre-registered search-> the T7 matched-arc record `21436282`')
    rec('  ### ### ### **THE RULE THE AUTHOR RATIFIED DESCRIBES WHAT THE CORPUS ALREADY DID.** ###')
    rec('  ### ### ### **IT IS DISCOVERED, NOT IMPOSED**, which is the strongest form a written')
    rec('  ### ### ### rule can take.')
    rec()
    rec('  ### **EVERY UNLISTED RECORD, WITH THE LIMB IT SATISFIES OR FAILS:**')
    fails, passes = [], []
    for d in sorted(ctx, key=lambda x: int(x)):
        if d in listed:
            continue
        marked = [c for c in ctx[d] if HIST.search(c[2])]
        el = elided.get(d, [])
        el_marked = [c for c in el if HIST.search(c[2])]
        if marked or el_marked:
            verdict = 'PASSES LIMB (b)'
            passes.append(d)
        else:
            verdict = '### **FAILS BOTH LIMBS**'
            fails.append(d)
        rec('    %-10s occurrences %-3d  historical-marked %-3d  elided-marked %-2d  %s'
            % (d, len(ctx[d]), len(marked), len(el_marked), verdict))
        if el_marked and not marked:
            rec('        ### ### **CLEARED ONLY BY AN ELIDED DOI, WHICH A FULL-DOI MATCHER CANNOT')
            rec('        ### ### SEE:** ### `%s` line %d' % (el_marked[0][0], el_marked[0][1]))
            rec('        > %s' % flat(el_marked[0][2], 200))
            rec('        ### **A PREDICATE THAT KNOWS ONE SHAPE FINDS ONE SHAPE.** ### Without')
            rec('        ### this read the record would have been convicted of a defect the')
            rec('        ### registry had already cleared.')
        if verdict.endswith('LIMBS**'):
            c = ctx[d][0]
            rec('        the only place it is named : `%s` line %d' % (c[0], c[1]))
            rec('        > %s' % flat(c[2], 200))
            rec('        ### **NEITHER AT A VERSION A CITABLE CLAIM USES, NOR CARRYING A NOTE')
            rec('        ### ### SAYING IT IS HISTORICAL.**')
    rec()
    rec('  ### ### ### **RECORDS FAILING BOTH LIMBS : `%d`.**' % len(fails))
    rec('  ### ### **RECORDS PASSING LIMB (b) : `%d`.**' % len(passes))
    rec('  ### ### **`(L2)` EXPECTED AT LEAST THREE. ### THE COUNT IS `%d`.**' % len(fails))
    if len(fails) < 3:
        rec('  ### ### ### **`(L2)` IS REFUTED, AND THE ACT SAYS SO.** ### **AN EXPECTATION IS NOT')
        rec('  ### ### ### A TARGET**, and a third failure was not manufactured to meet one.')
    else:
        rec('  ### ### ### **`(L2)` IS MET.**')
    rec()
    rec('  ### ### **AND ONE THING THE SURVEY THOUGHT IT HAD, WHICH THIS COMPONENT`S OWN')
    rec('  ### ### INSTRUMENT CANNOT ESTABLISH.**')
    kernel = []
    for d in ctx:
        for c in ctx[d]:
            k = c[2].find('10.5281/zenodo.' + d)
            if k > 0 and 'SIDE-kernel' in c[2][max(0, k - 90):k]:
                kernel.append(d)
                break
    kernel_listed = [d for d in kernel if d in listed]
    rec('  ### The pre-lock survey read `SIDE-kernel` as a deposit line satisfying limb (b)')
    rec('  ### everywhere and limb (a) nowhere -- ### **A DEPOSIT LINE WITH NO CURRENT RECORD.**')
    rec('  ### **THE TEST FOR IT IS PROXIMITY: A DOI COUNTS AS A KERNEL RECORD IF `SIDE-kernel`')
    rec('  ### ### SITS WITHIN NINETY CHARACTERS BEFORE IT.** ### That test returns `%d` DOIs:'
        % len(kernel))
    rec('  ###   %s' % sorted(kernel))
    rec('  ### ### **AND IT IS WRONG.** ### `19675355` is the MONOGRAPH`s concept DOI and')
    rec('  ### `21436280` is `SIDE-lv-conservation v0.8.0`; both sit on lines that mention')
    rec('  ### `SIDE-kernel` for a different reason. ### **PROXIMITY IS NOT ATTACHMENT.**')
    rec('  ### ### ### **THE FINDING IS WITHDRAWN AS NOT ESTABLISHED BY THIS ACT`S INSTRUMENT,')
    rec('  ### ### ### AND THE QUESTION IS ROUTED.**')
    rec('  ### **THIS COMPONENT HAS ALREADY TIGHTENED THIS TEST TWICE.** ### A third tightening,')
    rec('  ### made after seeing that the second still disagreed with the conclusion it was')
    rec("  ### supposed to support, would be ### **TUNING FOR A RESULT** ### (`b380`s forbidden")
    rec('  ### direction) -- so the component stops and reports that it cannot tell.')
    rec('  ### ### **WHAT REMAINS TRUE AND CHECKABLE:** ### the deposit note`s three citable')
    rec('  ### records are the monograph, `SIDE-lv-conservation` and the T7 search, and ###')
    rec('  ### **`SIDE-kernel` IS NOT AMONG THEM** -- read directly off the note`s own line, not')
    rec('  ### by proximity. ### **WHETHER THAT IS A DEFECT UNDER LIMB (a) DEPENDS ON WHETHER A')
    rec('  ### ### PUBLISHED CLAIM CITES ITS TERMINALS, WHICH THIS ACT DID NOT MEASURE.**')
    rec('  ### ### ### **ROUTED TO THE AUTHOR AS A QUESTION, NOT FILED AS A FINDING.**')
    rec()
    rec('  ### ### **THE REMEDIATION, PRICED AND ROUTED.**')
    rec('  ###   `%d` records need a historical note or a citable listing : ### **CORPUS WORK,'
        % len(fails))
    rec('  ###   ### ONE LINE EACH IN `REGISTRY.md` OR THE DEPOSIT NOTE.**')
    rec('  ###   `1` deposit line needs a current citable record named : ### **CORPUS WORK IF A')
    rec('  ###   ### DEPOSITED VERSION ALREADY QUALIFIES; PLATFORM WORK IF IT DOES NOT** -- and')
    rec('  ###   ### **THIS ACT CANNOT TELL WHICH FROM HERE**, because the platform half cannot be')
    rec('  ###   ### seen from the corpus.')
    rec('  ### ### **THE PLATFORM IS NOT WRITTEN TO. ### NOTHING DEPOSITS. ### THE REMEDIATION IS')
    rec('  ### ### THE AUTHOR`S.**')
    return dict(registry=r1, readme=r2, known=len(ctx), listed=len(listed),
                unlisted=len(ctx) - len(listed), fails=len(fails), passes=len(passes),
                failing=fails, kernel_probe=len(kernel), kernel_established=False,
                l2=(len(fails) >= 3), ok=(r1['ok'] and r2['ok']))


def main():
    rec('### run at (UTC) : %s   ### NOT COVERED BY ANY HASH.' % run_clock.stamp())
    bar('=')
    rec('b392 -- THE TWO RULINGS WRITTEN.')
    bar('=')
    c1 = component1()
    rec()
    c2 = component2()
    rec()
    bar('=')
    rec('  1 : (R19) written ; guard %s ; both failures quoted %s ; no placement %s ; +%d/-%d'
        % (c1['guard'], c1['quoted_failure'] and c1['quoted_retirement'], c1['no_placement'],
           c1['file']['added'], c1['file']['deleted']))
    rec('  2 : (R20) written ; known %d ; listed %d ; unlisted %d ; failing both limbs %d ; '
        '(L2) %s' % (c2['known'], c2['listed'], c2['unlisted'], c2['fails'], c2['l2']))
    rec('  ### **NOTHING DEPOSITS. ### THE PLATFORM WAS NOT CALLED. ### NO PRIOR LINE WAS EDITED.**')
    bar('=')
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    p = run_clock.write(D, 'b392_components_run', L)
    json.dump(dict(c1=c1, c2=c2, run_file=os.path.basename(p),
                   run_clock=run_clock.read_stamp(p)),
              io.open(os.path.join(D, 'b392_components.json'), 'w', encoding='utf-8'), indent=1)
    print('  written: %s' % os.path.basename(OUT))
    return 0 if (c1['ok'] and c2['ok']) else 1


if __name__ == '__main__':
    sys.exit(main())
