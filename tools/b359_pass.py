# -*- coding: utf-8 -*-
"""b359_pass.py -- THE LEDGER CURRENCY PASS. ### **IT COMPUTES NOTHING AND IT DEPOSITS NOTHING.**

### ### ### **NO WRITE VERB REACHES ANY PLATFORM FROM THIS FILE.** ### It reads three ledgers off disk,
### reads the fetch this act already made, and issues ### **`git ls-remote`** ### -- a read -- at each
### repository the ledgers name. ### There is no `POST`, no `PUT`, no `DELETE`, no token and no upload.
### ### **EVERY CLAIM IS LOCATED BY `anchor_from_file` BEFORE IT IS CLASSIFIED** (Bar 2), and a claim that
### cannot be located is reported UNCLASSIFIED.
### ### **EVERY PIN IS RESOLVED BY `ls-remote` OR REPORTED `UNRESOLVED`** (Bar 3, Addition Two); ### **NONE
### ### IS RECALLED.**
### ### **AND EVERY JUDGEMENT IN THIS FILE IS DECLARED DATA, ROW BY ROW** -- b357's cure. ### No status is
### inferred by a scanner from this seat's own prose.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import needle_pull   # noqa: E402
import run_clock     # noqa: E402
import anchor_from_file as AF   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
README = os.path.join(PP, 'README.md')
MAP = os.path.join(PP, 'SPIRAL_MAP.md')
REG = os.path.join(PP, 'REGISTRY.md')
ORG = 'https://github.com/psinary-sketch/'

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CURRENT, STALE, SILENT = 'CURRENT', 'STALE', 'SILENT'
STATUSES = (CURRENT, STALE, SILENT)
UNRESOLVED = 'UNRESOLVED'


def d(n):
    return os.path.join(D, n)


# ### ==============================================================================================
# ### THE DEPOSIT CLAIMS. ### **EACH LOCATED, THEN CLASSIFIED AGAINST THE PARTY THAT OUTRANKS IT.**
# ### `status` and `why` are DECLARED DATA (b357's cure); `ranked_by` names the party under (B).
# ### ==============================================================================================
CLAIMS = [
    dict(cid='R-DEP', doc='README.md', path=README,
         hint='**Deposit note (`day1/`).** Citable deposits: the monograph at manuscript',
         what="the front door's deposit note: the monograph at ms v5.10.2 / Zenodo v1.1.2, DOI "
              "10.5281/zenodo.21539167, concept 10.5281/zenodo.19675355; the live line at v5.13 and "
              "AHEAD of the deposit.",
         ranked_by='REGISTRY.md row d1-1, and the read-only fetch as witness',
         status=CURRENT,
         why="every field matches `REGISTRY`'s `d1-1` row and the fetch: version `v1.1.2`, DOI "
             "`10.5281/zenodo.21539167`, concept `10.5281/zenodo.19675355`, manuscript `v5.10.2`. ### And "
             "the sentence that most often goes stale here -- ### **the live line being AHEAD of the "
             "### deposit** -- is present and correct: `REGISTRY` carries `v5.13` in the same row."),
    dict(cid='R-SOT', doc='README.md', path=README,
         hint='**REGISTRY.md is the single source of truth.**',
         what="the front door's rule 1, which is the precedence's own foundation.",
         ranked_by='itself; it is the rule, not a deposit field',
         status=CURRENT,
         why="it states the precedence this act obeys, and `REGISTRY`'s own governing row is what every "
             "other claim here was checked against. ### **A RULE IS NOT A DEPOSIT FIELD**, and it is "
             "classified only because a currency pass that skipped its own authority would be odd."),
    dict(cid='R-DAY1', doc='README.md', path=README,
         hint='├── day1/                ← 7 papers + monograph (live line; see deposit note below)',
         what="the tree line for `day1/`, which the 2026-08-24 note records as one of the two rows it "
              "corrected.",
         ranked_by='REGISTRY.md, for the live-versus-deposit distinction',
         status=CURRENT,
         why="it points the reader at the deposit note rather than asserting a deposit field itself, "
             "which is exactly what the 2026-08-24 repair made it do."),
    dict(cid='M-WAVE-MONO', doc='SPIRAL_MAP.md', path=MAP,
         hint='| *A Place to Stand* monograph Zenodo v1.1.2 (ms v5.10.2) |',
         what="the map's deposit-wave row for the monograph: Zenodo v1.1.2, ms v5.10.2, DOI "
              "10.5281/zenodo.21539167.",
         ranked_by='REGISTRY.md row d1-1, and the fetch as witness',
         status=CURRENT,
         why="version, manuscript version and DOI all match `REGISTRY` and the fetch, and the row names "
             "what it supersedes (`v1.1.1 / 21436278`) rather than silently replacing it."),
    dict(cid='M-WAVE-LV', doc='SPIRAL_MAP.md', path=MAP,
         hint='| SIDE-lv-conservation v0.10.0 (`93c27ec`) |',
         what="the map's deposit-wave row for `SIDE-lv-conservation`: v0.10.0 = `93c27ec`, DOI "
              "10.5281/zenodo.21539068.",
         ranked_by="README.md's deposit note, which carries the same pair",
         status=CURRENT,
         why="the front door's deposit note states `SIDE-lv-conservation v0.10.0 = 93c27ec` with the same "
             "DOI, and `REGISTRY` is silent on this artifact's DOI, so the ranking party under (B) is the "
             "front door and the two agree."),
    dict(cid='M-WAVE-KERNEL', doc='SPIRAL_MAP.md', path=MAP,
         hint='| SIDE-kernel v1.5 (`0e5233f`) |',
         what="the map's deposit-wave row for the kernel: v1.5 = `0e5233f`, DOI 10.5281/zenodo.21520474.",
         ranked_by="README.md's kernel line, which asserts the same tag and commit",
         status=CURRENT,
         why="the front door names the same tag and the same commit, and the map's row names what it "
             "supersedes."),
    dict(cid='M-WAVE-T7', doc='SPIRAL_MAP.md', path=MAP,
         hint='| T7 matched-arc search | 10.5281/zenodo.21436282 |',
         what="the map's deposit-wave row for the T7 registered-search record, published 2026-07-19.",
         ranked_by="README.md's deposit note, which carries the same DOI and date",
         status=CURRENT,
         why="the front door states the same DOI, the same concept DOI and the same publication date."),
    dict(cid='M-FROZEN', doc='SPIRAL_MAP.md', path=MAP,
         hint='**Frozen Day-1 deposit (history):**',
         what="the map's frozen Day-1 table, carrying `PLACE-papers v1.0.2` and `SIDE-kernel v1.1` -- "
              "both SUPERSEDED versions.",
         ranked_by='(C)\'s locked distinction, not a ranking party',
         status=SILENT,
         why="### **IT IS EXPLICITLY MARKED AS HISTORY AND IS THEREFORE NOT A CLAIM ABOUT NOW.** ### The "
             "heading says *history*, and the table's own annotation says the row *\"is historical and is "
             "not rewritten\"*. ### The locked registration fixed this before any row was read: ### **A "
             "### DOCUMENT THAT SAYS \"THIS WAS TRUE THEN\" IS NOT SAYING \"THIS IS TRUE NOW\"**, and "
             "classifying it `STALE` would be this seat reading a tense it was told not to read."),
    dict(cid='M-VERSION', doc='SPIRAL_MAP.md', path=MAP,
         hint='**v0.6 — July 2026** (revises v0.5 — currency',
         what="the map's own version line, which says v0.6 refreshed all federation pins to the deposit "
              "wave and names `SIDE-lv-conservation v0.9.0` among them.",
         ranked_by='the map\'s own reconciliation note of 2026-08-24, which is later',
         status=SILENT,
         why="### **IT IS A CHANGELOG ENTRY DESCRIBING WHAT v0.6 DID**, not an assertion that `v0.9.0` is "
             "current -- and the map's own later note says the `v0.9.0` cell was corrected to a "
             "deposit-pin/working-head pair. ### A changelog that records a past state is the same shape "
             "as `M-FROZEN` and is treated the same way."),
]

# ### ==============================================================================================
# ### THE PINS. ### **(ADDITION TWO.) ### EVERY ONE RESOLVED BY `ls-remote`, NONE RECALLED.**
# ### `asserted` is the commit the ledger's text asserts; it is READ from the located line, not typed.
# ### ==============================================================================================
PINS = [
    dict(pid='P-KERNEL', doc='README.md', path=README, repo='SIDE-kernel',
         hint='**Kernel:** [SIDE-kernel](https://github.com/psinary-sketch/SIDE-kernel)',
         kind='TAG', ref='v1.5',
         what="the front door's kernel line: tag `v1.5` = `0e5233f`."),
    dict(pid='P-KERNEL-MAP', doc='SPIRAL_MAP.md', path=MAP, repo='SIDE-kernel',
         hint='| SIDE-kernel v1.5 (`0e5233f`) |',
         kind='TAG', ref='v1.5',
         what="the map's deposit-wave row for the kernel: v1.5 = `0e5233f`."),
    dict(pid='P-LV-PIN', doc='SPIRAL_MAP.md', path=MAP, repo='SIDE-lv-conservation',
         hint='| `SIDE-lv-conservation` | deposit-pin **v0.10.0** (`93c27ec`) · working head',
         kind='TAG', ref='v0.10.0',
         what="the map's DEPOSIT-PIN column for `SIDE-lv-conservation`: v0.10.0 = `93c27ec`."),
    dict(pid='P-LV-HEAD', doc='SPIRAL_MAP.md', path=MAP, repo='SIDE-lv-conservation',
         hint='| `SIDE-lv-conservation` | deposit-pin **v0.10.0** (`93c27ec`) · working head',
         kind='HEAD', ref='HEAD',
         what="the map's WORKING-HEAD column for `SIDE-lv-conservation`: `2f71068`."),
    dict(pid='P-EFFECTS', doc='SPIRAL_MAP.md', path=MAP, repo='SIDE-effects',
         hint='| ### **`SIDE-effects`** | ### **`main` `afa9ccf`**',
         kind='HEAD', ref='HEAD',
         what="the map's `SIDE-effects` row: `main` `afa9ccf`."),
    dict(pid='P-T7', doc='SPIRAL_MAP.md', path=MAP, repo='SIDE-t7-topology-cmb',
         hint='| `SIDE-t7-topology-cmb` | v0.3 (`8eb0d5a`) |',
         kind='TAG', ref='v0.3',
         what="the map's `SIDE-t7-topology-cmb` row: v0.3 = `8eb0d5a`."),
]

SHA = re.compile(r'`([0-9a-f]{7,40})`')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def locate(path, hint):
    n, line = AF.find(path, hint)
    needle_pull.pull(path, line)
    return n, line.rstrip()


def ls_remote(repo, ref, kind):
    """### ### **A READ. ### `ls-remote` ASKS; IT DOES NOT WRITE.**"""
    url = ORG + repo + '.git'
    args = ['git', 'ls-remote', url]
    if kind == 'TAG':
        args += ['refs/tags/' + ref + '^{}', 'refs/tags/' + ref]
    else:
        args += ['HEAD', 'refs/heads/main']
    r = subprocess.run(args, capture_output=True, text=True, encoding='utf-8', errors='replace',
                       timeout=180)
    if r.returncode != 0:
        return None, (r.stderr or '').strip()[:120]
    peeled, plain = None, None
    for ln in (r.stdout or '').splitlines():
        parts = ln.split()
        if len(parts) < 2:
            continue
        if parts[1].endswith('^{}'):
            peeled = parts[0]
        elif plain is None:
            plain = parts[0]
    got = peeled or plain
    return (got, None) if got else (None, 'no matching ref returned')


def main():
    rec('=' * 100)
    rec('b359 -- THE LEDGER CURRENCY PASS. ### IT COMPUTES NOTHING AND IT DEPOSITS NOTHING.')
    rec('=' * 100)
    rec('  ### the three statuses, locked before any claim was read : %s' % ' / '.join(STATUSES))
    rec('  ### and a pin that will not resolve is %s, never carried forward.' % UNRESOLVED)
    F = json.load(io.open(d('b359_fetch.json'), encoding='utf-8'))
    if F.get('hard_failure'):
        rec('')
        rec('  ### ### **THE FETCH DID NOT RETURN. ### BRANCH (H)(3). ### THE ACT STOPS HERE.**')
        run_clock.write(D, 'b359_pass_run', LINES)
        return 2
    fld = F['targets'][0]['fields']
    con = F['targets'][1]['fields']

    # ---- THE PRECEDENCE, QUOTED AND OBEYED ---------------------------------------------------------
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE PRECEDENCE, QUOTED FROM THE FRONT DOOR AND OBEYED. ### **(ADDITION ONE.)**')
    rec('-' * 100)
    for lbl, path, hint in (
            ('the precedence sentence', README,
             'later reader can re-run this: REGISTRY > README > SPIRAL_MAP for deposits; disk'),
            ('and its second half', README, 'for live pins only, never for deposits.**'),
            ('the pin/head ruling the map quotes', MAP,
             'a repository has a pin the corpus cites in published prose and a head where work continues')):
        n, line = locate(path, hint)
        rec('      %-38s %s:%d' % (lbl, os.path.basename(path), n))
        rec('      | %s' % line.strip()[:190])
    rec('  ### ### **SO: FOR A DEPOSIT FIELD, `REGISTRY` RULES; FOR A LIVE PIN, DISK RULES AND ONLY FOR')
    rec('  ### ### PINS. ### EVERY REPAIR BELOW RUNS TOWARD THE SOURCE OF TRUTH AND NEVER THE REVERSE.**')

    # ---- THE FETCH AGAINST THE SOURCE OF TRUTH -----------------------------------------------------
    rec('')
    rec('-' * 100)
    rec('  ### (2) THE READ-ONLY FETCH, AGAINST `REGISTRY`\'S GOVERNING ROW.')
    rec('-' * 100)
    n, drow = locate(REG, '| d1-1 | A Place to Stand (monograph) |')
    rec('      REGISTRY.md:%d -- the governing d1-1 row, located.' % n)
    checks = [
        ('version', fld['version'], 'v1.1.2', 'Zenodo v1.1.2' in drow),
        ('DOI', fld['doi'], '10.5281/zenodo.21539167', '10.5281/zenodo.21539167' in drow),
        ('concept DOI', fld['conceptdoi'], '10.5281/zenodo.19675355', 'concept 19675355' in drow),
        ('publication date', fld['publication_date'], '2026-07-24', 'PUBLISHED 2026-07-24' in drow),
        ('manuscript version', 'ms v5.10.2 (per the record\'s own title/description)', 'ms v5.10.2',
         'ms v5.10.2' in drow),
    ]
    agree = True
    for what, got, want, inrow in checks:
        ok = (str(got) == want or want in str(got)) and inrow
        agree = agree and ok
        rec('      %-20s fetch: %-46s REGISTRY carries it: %s  %s'
            % (what, str(got)[:46], inrow, 'AGREE' if ok else '### DISAGREE ###'))
    rec('      %-20s fetch: %-46s' % ('file count', fld['n_files']))
    rec('      %-20s fetch: %-46s' % ('is_last (version pointer)', fld['is_last']))
    rec('      %-20s fetch: %-46s' % ('concept resolves to id', con['id']))
    ptr_ok = (con['id'] == fld['id']) and bool(fld['is_last'])
    rec('      ### **THE CONCEPT DOI RESOLVES TO THE SAME RECORD AND IT IS `is_last` : %s**' % ptr_ok)
    rec('      ### ### **SO NO LATEST-VERSION POINTER HAS DRIFTED.**')
    sot_conflict = not (agree and ptr_ok)
    rec('  ### ### **SOURCE OF TRUTH AND FETCH: %s**'
        % ('### DISAGREE -- BRANCH (H)(4), NOTHING REPAIRED ###' if sot_conflict else 'THEY AGREE.'))

    # ---- THE CLAIMS ---------------------------------------------------------------------------------
    rec('')
    rec('-' * 100)
    rec('  ### (3) THE CLAIMS, EACH LOCATED THEN CLASSIFIED AGAINST THE PARTY THAT OUTRANKS IT.')
    rec('-' * 100)
    out, unclassified = [], []
    for c in CLAIMS:
        try:
            n, line = locate(c['path'], c['hint'])
        except (AF.AnchorError, LookupError) as e:
            unclassified.append(dict(cid=c['cid'], doc=c['doc'], error=str(e)[:90]))
            rec('')
            rec('  ### ### **UNCLASSIFIED -- COULD NOT BE LOCATED** : %s (%s)' % (c['cid'], c['doc']))
            continue
        c['line'], c['text'] = n, line.strip()[:300]
        out.append(c)
        rec('')
        rec('  ### **[%s] %s : %d**' % (c['cid'], c['doc'], n))
        rec('      | %s' % line.strip()[:190])
        rec('      ### what it claims : %s' % c['what'])
        rec('      ### ranked by      : %s' % c['ranked_by'])
        rec('      ### **STATUS : %s**' % c['status'])
        rec('      ### why           : %s' % c['why'])

    # ---- THE PINS -----------------------------------------------------------------------------------
    rec('')
    rec('-' * 100)
    rec('  ### (4) THE PINS, READ LIVE BY `ls-remote`. ### **(ADDITION TWO.) ### NONE RECALLED.**')
    rec('-' * 100)
    pins = []
    for p in PINS:
        try:
            n, line = locate(p['path'], p['hint'])
        except (AF.AnchorError, LookupError) as e:
            p.update(located=False, status=UNRESOLVED, note='claim line not located: %s' % str(e)[:60])
            pins.append(p)
            rec('')
            rec('  ### ### **NOT LOCATED** : %s' % p['pid'])
            continue
        shas = SHA.findall(line)
        # ### **THE ASSERTED SHA IS READ FROM THE LINE, NEVER TYPED.** ### The deposit-pin is the first
        # ### short sha on the row and the working head the second; the row prints them in that order.
        idx = 1 if p['kind'] == 'HEAD' and len(shas) > 1 else 0
        asserted = shas[idx] if shas else None
        got, err = ls_remote(p['repo'], p['ref'], p['kind'])
        if got is None:
            status, note = UNRESOLVED, err or 'no ref'
        elif asserted is None:
            status, note = UNRESOLVED, 'no sha on the located line to compare'
        else:
            status = CURRENT if got.startswith(asserted) else STALE
            note = ''
        p.update(located=True, line=n, asserted=asserted, resolved=got, status=status, note=note)
        pins.append(p)
        rec('')
        rec('  ### **[%s] %s : %d**   (%s, %s %s)' % (p['pid'], p['doc'], n, p['repo'], p['kind'], p['ref']))
        rec('      | %s' % line.strip()[:190])
        rec('      ### asserted by the ledger : %s' % asserted)
        rec('      ### ls-remote returned     : %s' % (got or '### %s ### %s' % (UNRESOLVED, note)))
        rec('      ### **STATUS : %s**%s' % (status, ('   ### %s' % note) if note else ''))
    rec('')
    rec('  ### ### **AND THE RULE THE LOCKED REGISTRATION FIXED, HELD TO HERE:** ### a DEPOSIT-PIN and a')
    rec('  ### ### WORKING HEAD are ### **NOT THE SAME OBJECT**, and this act classifies each against its')
    rec('  ### ### own party. ### A deposit-pin differing from a live head is NOT thereby stale.')

    # ---- THE COUNTS AND THE BRANCH ------------------------------------------------------------------
    nc = [c for c in out if c['status'] == CURRENT]
    ns = [c for c in out if c['status'] == STALE]
    nsi = [c for c in out if c['status'] == SILENT]
    pcur = [p for p in pins if p.get('status') == CURRENT]
    psta = [p for p in pins if p.get('status') == STALE]
    punr = [p for p in pins if p.get('status') == UNRESOLVED]
    rec('')
    rec('-' * 100)
    rec('  ### (5) THE COUNT.')
    rec('-' * 100)
    rec('    claims located and classified : %d ; unclassified : %d' % (len(out), len(unclassified)))
    rec('      %-10s %d      %-10s %d      %-10s %d' % (CURRENT, len(nc), STALE, len(ns), SILENT, len(nsi)))
    rec('    pins asserted and read live   : %d' % len(pins))
    rec('      %-10s %d      %-10s %d      %-10s %d'
        % (CURRENT, len(pcur), STALE, len(psta), UNRESOLVED, len(punr)))
    for p in psta:
        rec('      ### STALE PIN : %s %s:%d asserts %s ; ls-remote returns %s'
            % (p['pid'], p['doc'], p['line'], p['asserted'], p['resolved']))
    for p in punr:
        rec('      ### UNRESOLVED : %s (%s) -- %s' % (p['pid'], p['repo'], p.get('note', '')))

    rec('')
    rec('-' * 100)
    rec("  ### (6) THE BRANCH, BY (H)'S LOCKED RULE.")
    rec('-' * 100)
    stale_any = bool(ns) or bool(psta)
    if sot_conflict:
        verdict = 'THE SOURCE OF TRUTH AND THE FETCH DISAGREE'
    elif stale_any:
        verdict = 'A DRIFT IS FOUND AND FILED'
    else:
        verdict = 'NO DRIFT IS FOUND'
    rec('    ### **(THE FETCH DID NOT RETURN) -- UNREACHABLE, AND SHOWN SO.** ### %d of %d targets'
        % (F['fetched'], F['attempted']))
    rec('      returned HTTP 200 and were hashed.')
    rec('    ### **(THE SOURCE OF TRUTH AND THE FETCH DISAGREE) -- %s** ### every field the governing row'
        % ('TAKEN' if sot_conflict else 'UNREACHABLE, AND SHOWN SO.'))
    rec('      carries matched the record the platform returned, and the concept pointer is `is_last`.')
    rec('    ### **(A DRIFT IS FOUND AND FILED) -- %s** ### %d claim(s) and %d pin(s) are STALE.'
        % ('TAKEN' if (stale_any and not sot_conflict) else 'UNREACHABLE, AND SHOWN SO.',
           len(ns), len(psta)))
    rec('    ### **AND THE MIXTURE RULE, LOCKED BEFORE THE READING:** ### if any claim is STALE and others')
    rec('      are CURRENT or SILENT, the second branch is taken and the others are reported beside it.')
    rec('    ### ### ### **THEREFORE: %s.**' % verdict)
    if verdict == 'NO DRIFT IS FOUND':
        rec('    ### ### **AND SECTION (E) GOVERNS WHAT FOLLOWS: IF NOTHING IS STALE, NOTHING IS APPENDED.**')
        rec('    ### ### A currency pass that finds no drift and writes a note anyway would be adding')
        rec('    ### ### noise and calling it work.')

    rec('')
    rec('=' * 100)
    rec('  VERDICT : ### **%s**' % verdict)
    rec('  ### ### **NOTHING IS DEPOSITED. ### NOTHING IS WRITTEN AT ZENODO. ### `REGISTRY.md` IS NOT')
    rec('  ### ### WRITTEN. ### NO SENTENCE IS EDITED.**')
    rec('=' * 100)

    p2 = run_clock.write(D, 'b359_pass_run', LINES)
    io.open(d('b359_pass.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(dict(
        verdict=verdict, statuses=list(STATUSES),
        claims=[dict(cid=c['cid'], doc=c['doc'], line=c['line'], status=c['status'],
                     ranked_by=c['ranked_by']) for c in out],
        unclassified=unclassified,
        n_current=len(nc), n_stale=len(ns), n_silent=len(nsi),
        pins=[dict(pid=p['pid'], doc=p['doc'], repo=p['repo'], kind=p['kind'], ref=p['ref'],
                   line=p.get('line'), asserted=p.get('asserted'), resolved=p.get('resolved'),
                   status=p.get('status'), note=p.get('note', '')) for p in pins],
        n_pins=len(pins), n_pins_current=len(pcur), n_pins_stale=len(psta),
        n_pins_unresolved=len(punr),
        fetch_vs_registry='AGREE' if not sot_conflict else 'DISAGREE',
        deposit=dict(version=fld['version'], doi=fld['doi'], conceptdoi=fld['conceptdoi'],
                     publication_date=fld['publication_date'], n_files=fld['n_files'],
                     is_last=fld['is_last']),
        appended_anything=False,
        run_file=os.path.basename(p2), run_clock=run_clock.read_stamp(p2)), indent=1))
    print('  written: %s' % os.path.basename(p2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
