# -*- coding: utf-8 -*-
"""b373_status.py -- COMPONENT 2: THE STATUS COLUMN. ### **LISTED AND ROUTED; NO GRADE MOVED.**

### ### **THE ORDER'S REASON IS ADOPTED:** ### a row asserting a GRADE against a declaration this
### record has classified retired or absent is ### **A CLAIM ABOUT WHAT IS VERIFIED, NOT A STALE
### ### NUMBER.** ### A stale count misstates a quantity; a grade against an absent declaration asserts
### that something was checked that is not there to check.
### ### **THE CLASSIFIED SET IS THE RECORD'S OWN AND IS NOT RE-DERIVED HERE** -- `b369`'s absent list
### and `b372`'s per-declaration verdicts. ### **NO KERNEL IS OPENED.**
### ### ### **AND ONE DISTINCTION IS DRAWN BEFORE THE SWEEP, BECAUSE IT DECIDES ROWS:** ### a row that
### ### **STATES ITS OWN RETIREMENT** and grades the retirement is not the defect; a row that grades the
### DECLARATION as present-and-weak is. ### Treating them alike would report a corrected row as a
### defective one.
### ### **NO GRADE IS MOVED BY THIS SEAT.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### **THE GRADE VOCABULARY, DECLARED BEFORE THE SWEEP SO IT CAN BE DISAGREED WITH.**
# ### ### **AND ITS FAILURE MODE WITH IT (`PREDICATE_ONE_SHAPE`):** ### a row stating its grade in a
# ### shape this list does not know will not be found, so the shapes matched are printed and
# ### ### **NO COMPLETENESS IS CLAIMED.**
GRADES = ['✓F', '✓C', '✓', '⊘', 'SHELL', 'DERIVES', 'INTERFACES',
          'ENCODES-CONCLUSION', 'TAUTOLOGY', 'DEFINED-ONLY', 'PROVED', 'VERIFIED']

# ### the words by which a row states its OWN retirement. ### A row carrying one of these is
# ### reporting the withdrawal, not asserting the declaration is there.
SELF_RETIRED = ['RETIRED', 'WITHDRAWN', 'withdrawn', 'not present on any live branch',
                'retired', 'Retired', 'W-2 WITHDRAWAL', 'no longer', 'Placeholder']

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(*a):
    return subprocess.run(['git', '-C', PP] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def main():
    rec('=' * 100)
    rec('b373 -- COMPONENT 2: THE STATUS COLUMN. ### **LISTED AND ROUTED; NO GRADE MOVED.**')
    rec('=' * 100)
    rec('')
    # ---- the classified set, from the record's own banks -------------------------------------------
    rep = json.load(io.open(os.path.join(D, 'b369_repair.json'), encoding='utf-8'))
    bat = json.load(io.open(os.path.join(D, 'b372_batch.json'), encoding='utf-8'))
    absent369 = list(rep['absent'])
    from372 = {}
    for r in bat['rows']:
        for v in r['verdicts']:
            if v['verdict'] in ('RETIRED', 'ABSENT'):
                from372[v['terminal'].split('.')[-1]] = v['verdict']
    names = {}
    for n in absent369:
        names[n] = 'b369 (confirmed after b367 and b368): ABSENT at the kernel'
    for n, v in from372.items():
        names[n] = (names.get(n, '') + ' ; ' if n in names else '') + ('b372: %s' % v)
    rec('-' * 100)
    rec("  ### (1) THE CLASSIFIED SET. ### **THE RECORD'S OWN, NOT RE-DERIVED HERE.**")
    rec('-' * 100)
    rec('    from `b369` (the kernel at `%s`) : %d names classified ABSENT'
        % (rep['head'][:12], len(absent369)))
    rec('    from `b372` (the twelve flagged rows)   : %d names classified RETIRED or ABSENT'
        % len(from372))
    rec('    ### ### **THE UNION : %d DISTINCT DECLARATIONS.**' % len(names))
    rec('    %s' % sorted(names))
    rec('    ### **NO KERNEL IS OPENED TO RE-CLASSIFY ANY OF THEM.**')

    # ---- the sweep ---------------------------------------------------------------------------------
    files = [f for f in git('ls-files', '*.md').split(chr(10)) if f.strip()]
    rec('')
    rec('-' * 100)
    rec('  ### (2) THE SWEEP. ### **%d TRACKED MARKDOWN FILES.**' % len(files))
    rec('-' * 100)
    rec('    the grade vocabulary, declared : %s' % GRADES)
    rec('    ### ### **A ROW STATING ITS GRADE IN A SHAPE THIS LIST DOES NOT KNOW WILL NOT BE FOUND.**')
    rec('    ### ### **NO COMPLETENESS IS CLAIMED.**')
    # ### the rows b372 opened, and the declarations it found ALIVE in them.
    LIVE = {}
    for r in bat['rows']:
        alive = [v['terminal'] for v in r['verdicts'] if v['verdict'] == 'PRESENT']
        if alive:
            LIVE[(r['file'], r['line'])] = alive
    hits, scanned = [], 0
    word = {n: re.compile(r'(?<![A-Za-z0-9_])%s(?![A-Za-z0-9_])' % re.escape(n)) for n in names}
    for rel in files:
        p = os.path.join(PP, rel.replace('/', os.sep))
        try:
            txt = io.open(p, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        for i, ln in enumerate(txt.split(chr(10)), 1):
            if not ln.strip().startswith('|'):
                continue
            scanned += 1
            named = [n for n in names if word[n].search(ln)]
            if not named:
                continue
            grades = [g for g in GRADES if g in ln]
            if not grades:
                continue
            self_ret = [w for w in SELF_RETIRED if w in ln]
            # ### ### **AND A ROW THAT NAMES A CLASSIFIED DECLARATION MAY BE GRADING A LIVE ONE.**
            # ### `VERIFICATION_LOOM.md:540` carries the retired concept label `side_exclusion` in its
            # ### first cell and grades `techne_kernel.SIDE_exclusion`, which `b372` found ### **PRESENT
            # ### ### IN A DIFFERENT KERNEL.** ### Counting it as the defect would report a CORRECT row
            # ### as a defective one -- the same mistake, one step further out, as counting a row that
            # ### states its own retirement.
            live = LIVE.get((rel, i), [])
            hits.append(dict(file=rel, line=i, declarations=sorted(named), grades=grades,
                             states_own_retirement=bool(self_ret),
                             retirement_words=self_ret[:3],
                             grades_a_live_declaration=live,
                             classified={n: names[n] for n in sorted(named)},
                             text=ln.strip()))
    rec('    table rows scanned : %d' % scanned)
    rec('    ### ### **ROWS NAMING A CLASSIFIED DECLARATION AND CARRYING A GRADE : %d**' % len(hits))

    defect = [h for h in hits
              if not h['states_own_retirement'] and not h['grades_a_live_declaration']]
    corrected = [h for h in hits if h['states_own_retirement']]
    live_graded = [h for h in hits
                   if h['grades_a_live_declaration'] and not h['states_own_retirement']]
    rec('    ### ### **OF THOSE, STATING THEIR OWN RETIREMENT : %d ### -- NOT THE DEFECT**'
        % len(corrected))
    rec('    ### ### **AND GRADING A DECLARATION `b372` FOUND ALIVE : %d ### -- ALSO NOT THE DEFECT**'
        % len(live_graded))
    rec('    ### ### **AND ASSERTING THE GRADE WITHOUT EITHER : %d ### -- THE DEFECT**' % len(defect))

    rec('')
    rec('-' * 100)
    rec('  ### (3) THE DEFECTIVE ROWS, EACH WITH THE DOCUMENT THAT CARRIES IT.')
    rec('-' * 100)
    bycar = {}
    for h in defect:
        bycar.setdefault(h['file'], []).append(h)
    for rel in sorted(bycar):
        rec('')
        rec('    ### **CARRIER : `%s`** ### -- %d row(s)' % (rel, len(bycar[rel])))
        for h in bycar[rel]:
            rec('      line %-6d grade(s) %-28s declaration(s) %s'
                % (h['line'], ','.join(h['grades']), ', '.join('`%s`' % x
                                                               for x in h['declarations'])))
            rec('        | %s' % h['text'][:200])
            for n in h['declarations']:
                rec('        ### ### **`%s` : %s**' % (n, names[n]))

    rec('')
    rec('-' * 100)
    rec('  ### (4) THE ROWS THAT STATE THEIR OWN RETIREMENT. ### **REPORTED SO THEY ARE NOT MISTAKEN')
    rec('  ### ### FOR THE DEFECT.**')
    rec('-' * 100)
    for h in corrected:
        rec('      %-56s line %-6d %s' % (h['file'][:56], h['line'],
                                          ', '.join('`%s`' % x for x in h['declarations'])))
        rec('        the words by which it says so : %s' % h['retirement_words'])

    # ---- the consequence, routed -------------------------------------------------------------------
    rec('')
    rec('  ### **AND THE ROWS THAT NAME A CLASSIFIED DECLARATION BUT GRADE A LIVE ONE.**')
    rec('  ### ### **THESE ARE NOT THE DEFECT EITHER, AND SAYING SO IS THE POINT:** ### a row whose')
    rec('  ### first cell carries a retired concept LABEL while its terminal cell names a declaration')
    rec('  ### `b372` found alive is ### **A CORRECT ROW**, and counting it would be the same mistake as')
    rec('  ### counting a row that states its own retirement -- one step further out.')
    for h in live_graded:
        rec('      %-56s line %-6d names %s' % (h['file'][:56], h['line'],
                                                ', '.join('`%s`' % x for x in h['declarations'])))
        rec('        ### ### **BUT `b372` FOUND ALIVE IN THAT ROW : %s**'
            % ', '.join('`%s`' % x for x in h['grades_a_live_declaration']))
    rec('')
    rec('=' * 100)
    rec('  ### (5) THE CONSEQUENCE, ROUTED AND NOT ACTED ON.')
    rec('=' * 100)
    rec('  ### ### **%d ROWS IN %d DOCUMENTS ASSERT A GRADE AGAINST A DECLARATION THIS RECORD HAS'
        % (len(defect), len(bycar)))
    rec('  ### ### CLASSIFIED RETIRED OR ABSENT.**')
    rec('  ### ### **THAT IS NOT A STALE NUMBER. ### IT SAYS A THING WAS VERIFIED THAT IS NOT THERE TO')
    rec('  ### ### VERIFY**, and a reader traversing the row has no way to see the difference.')
    rec('  ### **AND NO GRADE IS MOVED BY THIS SEAT.** ### A grade is a judgement about verified')
    rec('  ### content; ### **A SEAT THAT REGRADES IS A SEAT THAT DECIDED WHAT WAS VERIFIED.** ### The')
    rec('  ### list is the product and the decision is the author`s.')
    rec('  ### ### **AND WHAT THE AUTHOR IS BEING ASKED IS NARROW:** ### for each row, whether the grade')
    rec('  ### should be struck, re-stated as a retirement the way `VERIFICATION_LOOM.md` already does')
    rec('  ### for one pair, or left with a pin that dates it. ### **THREE CHOICES, NOT AN OPEN')
    rec('  ### ### QUESTION**, and this act names them without choosing.')
    rec('=' * 100)
    p = run_clock.write(D, 'b373_status_notes', LINES)
    io.open(os.path.join(D, 'b373_status.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(classified=len(names), classified_names=sorted(names),
                        from_b369=len(absent369), from_b372=len(from372),
                        files=len(files), rows_scanned=scanned,
                        hits=len(hits), defect=len(defect), corrected=len(corrected),
                        live_graded=len(live_graded),
                        carriers=sorted(bycar), grades=GRADES,
                        detail=hits, grades_moved=0,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
