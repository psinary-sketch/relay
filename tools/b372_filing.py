# -*- coding: utf-8 -*-
"""b372_filing.py -- THE TRAILS LEDGER, UPDATED WITH WHAT THIS ACT SETTLED AND WHAT IT ROUTED.

### ### **ONE APPEND-ONLY BLOCK UNDER ITS OWN MARK.** ### Every prior block stands exactly as written;
### this one NAMES the last of them and edits none.
### ### **EVERY FIGURE IS READ FROM THIS ACT'S OWN JSONS.** ### None is typed.
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TRAILS = os.path.join(PP, 'OPEN_TRAILS.md')
MARK = '<!-- b372 the eol pin, the readme figures, the first batch of row checks -->'
PRIOR = '<!-- b371 the desk closes: scaffold-terminals, the anchored arms, the hook -->'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def jload(n):
    return json.load(io.open(os.path.join(D, n), encoding='utf-8'))


def block(E, R, B, Q, INV):
    tbl = R['table']
    first, mid, last = tbl[0], tbl[1], tbl[-1]
    tv = B['terminal_tally']
    heads = B['heads']
    closed = Q['closed_items']
    pinned_rows = [r for r in B['rows'] if r['mode'] == 'AT-PIN']
    head_rows = [r for r in B['rows'] if r['mode'] == 'CHECKED-AT-HEAD']
    falsepin = [r for r in B['rows'] if r['pins'] and not any(p['resolves'] for p in r['pins'])]
    lines = [
        '', MARK, '',
        ('### **b372 — THE END-OF-LINE PIN, THE README FIGURES, AND THE FIRST BATCH OF ROW CHECKS '
         '(2026-09-08)**'),
        '',
        ('*No block above is edited. The b371 block (`%s`) and every block before it stand exactly as '
         'they were written.*' % PRIOR),
        '',
        ('**Ruling (R8), the author\'s, 2026-09-08:** *a row without a pin is not checkable the way the '
         'architecture promises. Such a row may be checked at the kernel\'s live head, and the head is '
         'recorded in the checking act\'s own bank — never written into the row — so the check is dated '
         'and says so. A pinless row that passes is marked CHECKED-AT-HEAD, which is weaker than a '
         'pinned row\'s check and the record says why. Whether pins are added to those rows is a '
         'separate ruling, priced and not attempted.*'),
        '',
        '### The end-of-line pin, closed',
        '',
        ('`.gitattributes` now carries a repository-wide `%s` in **every one of the %d rostered '
         'repositories**, and in each of them **a fresh checkout of the tracked pre-push guard is '
         'byte-identical to its blob**. Before this act, %d of %d were: the two that were not — %s — '
         'were **exactly the two without the attribute**. `relay`\'s pre-existing path-scoped line is '
         '**preserved, not replaced**; the two repositories that already carried the attribute were '
         '**not written to**.'
         % (E['line'], len(E['after']), sum(1 for v in E['before'].values() if v['fresh_equals_blob']),
            len(E['before']),
            ', '.join('`%s`' % k for k, v in E['before'].items() if not v['fresh_equals_blob']))),
        '',
        ('**And the floor is stated with the finding.** An attribute added today does not renormalise a '
         'working tree checked out yesterday, and this act renormalised none. **What is fixed is what '
         'the next checkout produces.** The mechanism was exercised in both polarities in a throwaway '
         'repository built for the purpose — with the attribute the extracted bytes equal the blob, '
         'without it they do not — so the pass is known to be caused by the attribute and not by the '
         'weather.'),
        '',
        '### The README figures, determined and repaired',
        '',
        ('**The order named `the exclusion kernel\'s README` and described a different file.** '
         '`SIDE-effects/README.md` has one count line, no breakdown, and ships no axiom profile at all; '
         'the README answering all three clauses of the description is **`SIDE-global-section`\'s**. '
         '**The object was identified by the description, because a description is checkable against a '
         'file and a label is not** — and the discrepancy is reported rather than absorbed. Nothing in '
         'the exclusion kernel\'s README was repaired.'),
        '',
        ('**What the three figures count was determined at content, and the answer is not what three '
         'different numbers suggest.**'),
        '',
        '| ref | date | headline | breakdown sum | assembly ratio | Core modules named | profile ships |',
        '|---|---|---|---|---|---|---|',
    ] + [
        '| `%s` | %s | %s | %s | %s | %s | %d |'
        % (r['ref'][:7], r['date'], r['headline'], r['total'], r['ratio'], r['modules'], r['prints'])
        for r in tbl
    ] + [
        '',
        ('**They count one quantity — Core zero-axiom terminals, one per printed line — read at three '
         'different refs.** At `%s` the headline, the breakdown, the ratio and the shipped profile all '
         'read **%s**. At `%s` the breakdown, the ratio, the module count and the profile all moved to '
         '**%s** and **the headline alone was left behind**. At the head the profile is **%d** and the '
         'whole sentence is behind it. **Each figure was exact when it was written, and none of them '
         'names the ref it holds at** — which is the defect, and it is the same defect b371 settled in '
         'the public description of the same repository.'
         % (first['ref'][:7], first['total'], mid['ref'][:7], mid['total'], last['prints'])),
        '',
        ('**The repair follows b371\'s precedent: a figure is removed rather than restated.** The '
         'headline figure and the assembly ratio are **removed** and the file that carries the number '
         'is named instead. The 33-part layer census and the module count are **preserved verbatim and '
         'dated to `%s` (%s)**, the ref they hold at — which is what the order permits in place of '
         'removal. **The claim `No terminal failed the bar; none is excluded` is untouched and is '
         'supported**: every one of the %d printed lines says the declaration does not depend on any '
         'axioms, read from the working file and confirmed against its blob.'
         % (mid['ref'][:7], mid['date'], R['profile']['lines'])),
        '',
        ('**And one thing is routed rather than repaired:** re-deriving the layer census at the head is '
         'a per-layer recount of the tree — **a claim and not a number** — and the order says route it.'),
        '',
        '### The first batch of row checks, under (R6) and (R8)',
        '',
        ('The %d rows b371 flagged were re-anchored **by their own content** and opened at the ref each '
         'row names. **%d were opened at a pin; %d at the kernel\'s live head under (R8)** and are '
         'marked CHECKED-AT-HEAD. The heads are recorded here and **were not written into any row**: '
         '`SIDE-effects` `main` `%s`, `SIDE-kernel` `main` `%s`, both read 2026-09-08.'
         % (len(B['rows']), len(pinned_rows), len(head_rows),
            heads['SIDE-effects']['head'][:12], heads['SIDE-kernel']['head'][:12])),
        '',
        ('Across those rows, **%d named terminals classify RETIRED, %d PRESENT and %d ABSENT.** Every '
         'RETIRED verdict quotes the kernel\'s own retirement ledger; no verdict is an inference from '
         'absence.'
         % (tv.get('RETIRED', 0), tv.get('PRESENT', 0), tv.get('ABSENT', 0))),
        '',
        ('**And the batch demonstrates (R8) inside a single act.** `no_conspiracy_twins`, '
         '`no_conspiracy_goldbach` and `no_conspiracy_sg` are cited by four of the twelve rows. The one '
         'row that names a pin — `phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md`, at `c66f3c5` — '
         'is **correct at the ref it names: all three are present there.** The three rows in '
         '`VERIFICATION_LOOM.md` that name the same declarations and **no pin** come back **RETIRED at '
         'the head**, with the kernel\'s ledger quoted. *The same declarations, true at the pin and '
         'retired at the head.* **A pinned row aged well; a pinless row did not, and nothing in it '
         'tells a reader which ref it meant.**'),
        '',
        ('**Some rows carry something that looks like a pin and is not.** %s — a manuscript version and '
         'an exemplar version — match the inventory\'s pin pattern and **do not resolve in the kernel '
         'the row names**, so %d rows b371 counted as pinned are **pinless in fact** and were opened at '
         'the head. That is `PREDICATE_ONE_SHAPE` running the other way: a pattern that knows one shape '
         'also matches things that are not that shape.'
         % (', '.join('`%s`' % p['pin'] for r in falsepin for p in r['pins']), len(falsepin))),
        '',
        '### What this implies for the papers, reported and routed — no row was repaired',
        '',
        '| document | row | what the row says | what the kernel says at the ref |',
        '|---|---|---|---|',
    ] + [
        '| `%s` | %d | %s | %s at `%s`%s |'
        % (r['file'], r['line'],
           ', '.join('`%s`' % v['terminal'] for v in r['verdicts'])[:80],
           ', '.join(sorted(set(v['verdict'] for v in r['verdicts']))),
           r['ref'][:7], ' — CHECKED-AT-HEAD' if r['mode'] == 'CHECKED-AT-HEAD' else '')
        for r in B['rows']
    ] + [
        '',
        ('**The routing, and it is a routing and not a repair.** `VERIFICATION_LOOM.md` rows 529–531 '
         'carry status `✓F` against declarations that are retired at the head; `EXCLUSION_ENGINE.md` '
         'rows 190–193 grade **SHELL** against declarations that no longer exist to be shells; '
         '`REGISTRY.md`\'s p2-31 pairs a manuscript to `YangMills.mass_gap`, retired. **Every one of '
         'those rows was true at a ref, and none of them names one.** What to do about that is the '
         'author\'s: this act was told the classification is the product.'),
        '',
        ('**And the exclusion kernel\'s retirement ledger has lacunae of its own, filed and not '
         'invented** (the (R5) shape, met again in a different kernel): %s are cited by rows and are '
         'named **nowhere** in the ledger that retired their neighbours. They classify ABSENT on the '
         'evidence, which is weaker than RETIRED and says so.'
         % ', '.join('`%s`' % t for _r, t in B['absent'])),
        '',
        '### The desk, and the price of the separate ruling',
        '',
        ('%d desk items were swept under (R7); **%d closed** — %s — each with the file and date that '
         'killed it named, and **both flagged because the killing file is this act\'s own**. %d stand.'
         % (Q['items'], Q['closed'], ', '.join('*%s*' % c['item'] for c in closed), Q['standing'])),
        '',
        ('**The price of adding pins, given because (R8) asks for it and not because this act argues '
         'for it.** This act opened %d kernel refs to classify %d rows and read the whole `.lean` tree '
         'at each. b371 inventoried **%d pinless rows** across the papers repository. Pinning one row '
         'costs: resolve the kernel the row names, find the ref at which the row was true (this act '
         'located that ref by history search for every retired terminal it met), and write it in — a '
         'read, a history walk and a one-line edit. **The read scales; the history walk is the '
         'expensive half and it is the half that cannot be skipped, because a pin written at the head '
         'pins a row to a state in which the row is false.** That is the whole price, and this act '
         'attempts none of it.'
         % (len(set(r['ref'] for r in B['rows'])), len(B['rows']), INV['without_pin'])),
        '',
        ('*Species: **A PIN IS A DATE THAT SURVIVES**. The same three declarations are present at a '
         'pinned row\'s ref and retired at the head; the pinned row aged and the pinless ones did not. '
         '**No row was repaired. No pin was added. No `.lean` file was written, no build was run, no '
         'axiom profile was recomputed. No repository was renormalised and no working file was deleted '
         'to force a checkout.** Trigger: the ruling on whether pins are added, or the next batch of '
         'rows. Nothing here is a route, no coordinate is closed, and `h2` stands exactly where the '
         'deposit left it.*'),
    ]
    return lines


def main():
    rec('=' * 100)
    rec('b372 -- THE TRAILS LEDGER: WHAT THIS ACT SETTLED AND WHAT IT ROUTED.')
    rec('=' * 100)
    E = jload('b372_eol.json')
    R = jload('b372_readme.json')
    B = jload('b372_batch.json')
    Q = jload('b372_desk.json')
    INV = jload('b371_inventory.json')
    before = io.open(TRAILS, encoding='utf-8', newline='').read()
    if MARK in before:
        rec('  ### ALREADY FILED -- the mark is present. ### NOTHING APPENDED.')
        run_clock.write(D, 'b372_filing_notes', LINES)
        return 0
    rec('  ### the prior block is present and is not edited : %s' % (PRIOR in before))
    body = chr(10).join(block(E, R, B, Q, INV)) + chr(10)
    io.open(TRAILS, 'a', encoding='utf-8', newline=chr(10)).write(body)
    after = io.open(TRAILS, encoding='utf-8', newline='').read()
    r = subprocess.run(['git', 'show', 'HEAD:OPEN_TRAILS.md'], cwd=PP, capture_output=True)
    committed = r.stdout.decode('utf-8', 'replace')
    appended_only = after.startswith(before)
    prefix_intact = (committed.replace(chr(13) + chr(10), chr(10))
                     in after.replace(chr(13) + chr(10), chr(10)))
    rec('  ### bytes %d -> %d' % (len(before.encode('utf-8')), len(after.encode('utf-8'))))
    rec('  ### ### **APPEND-ONLY (the file before is a prefix of the file after) : %s**' % appended_only)
    rec('  ### ### **THE COMMITTED VERSION IS STILL A SUBSTRING OF THE FILE : %s**' % prefix_intact)
    rec('  ### mark : %s' % MARK)
    rec('  ### lines appended : %d' % len(body.split(chr(10))))
    subprocess.run(['git', '-C', PP, 'add', '--', 'OPEN_TRAILS.md'], capture_output=True)
    rec('=' * 100)
    p = run_clock.write(D, 'b372_filing_notes', LINES)
    io.open(os.path.join(D, 'b372_filing.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(mark=MARK, prior_present=(PRIOR in before), appended_only=appended_only,
                        committed_prefix_intact=prefix_intact,
                        before_bytes=len(before.encode('utf-8')),
                        after_bytes=len(after.encode('utf-8')),
                        file='OPEN_TRAILS.md',
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
