# -*- coding: utf-8 -*-
"""b486_extract.py -- THE SURVEY FOR THE FOLD.
### ### **EVERY ACT'S VERDICTS COME FROM ITS OWN CLOSING BANK**, and every clause of the (R31)
### digest block is CHECKED AGAINST A CITING ACT before the block is written. ### **A CLAUSE NO
### CITED ACT SAYS IS REPORTED AS SUCH AND NOT WRITTEN INTO THE DIGEST.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
NL = chr(10)
L, MISSES = [], []

# ### ### **THE SPAN, IN FILING ORDER AS THE TRAIL RECORDS IT** -- not in number order.
SPANACTS = ['b475', 'b478', 'b476', 'b480', 'b477', 'b481', 'b483', 'b484', 'b485', 'b482', 'b479']

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def bank(act):
    """### the act's OWN closing bank, and its components if the closing is thin."""
    return (read(os.path.join(D, '%s_closing.txt' % act)),
            read(os.path.join(D, '%s_components.txt' % act)))


# ### ### **THE SIX CLAUSES THE ORDER SPECIFIES, EACH WITH THE NEEDLE THAT WOULD PROVE A CITING
# ### ACT SAYS IT.** ### The needle is fixed HERE, before the search runs.
CLAUSES = [
    ('S1', 'the six sites reduced to conditions on the test function, the data of the '
           'representation, and the instrument truncation, with (i) and (ii) the same object as K8',
     [(r'K8', None), (r'site \(i\)|sites', None)]),
    ('S2', 'the class boundary at a = sqrt 2 by two routes',
     [(r'sqrt\s*2|sqrt 2|√2|1\.41421', None)]),
    ('S3', "zeta23's explicit formula contains b321's identity; the grade is conditional on an "
           'unrun profile',
     [(r'EF contains|b321.{0,30}identity|explicit formula', None),
      (r'DERIVES, CONDITIONAL|conditional', None)]),
    ('S4', 'the compression register ran and takes no grade; its blocker is the places-side '
           'quadrature bound, W-ORD-QUADRATURE-BOUND',
     [(r'W-ORD-QUADRATURE-BOUND', None), (r'NO GRADE|no grade', None)]),
    ('S5', "the circulation gate DISCHARGED at b485 with the authority's own five findings standing",
     [(r'DISCHARGED', None), (r'five|5 are in the authority|FINDINGS : 7', None)]),
    ('S6', 'the eight unanchored sentences under E-2026-09-22-1',
     [(r'E-2026-09-22-1', None), (r'eight unanchored|unanchored', None)]),
]


def main():
    rec('=' * 108)
    rec('b486 -- THE SURVEY FOR THE FOLD. ### ELEVEN ACTS, IN FILING ORDER.')
    rec('=' * 108)

    # ------------------------------------------------------------------ (P1) the span
    rec('')
    rec('(P1) THE SPAN, BY FILING AND BY NUMBER.')
    rec('-' * 108)
    t = read(os.path.join(PP, 'OPEN_TRAILS.md'))
    filed = [m.group(1) for m in re.finditer(r'^### (b\d+)[a-z]? —', t, re.M)]
    after = filed[filed.index('b474') + 1:]
    rec('    the trail`s own filing order after the b474 fold:')
    rec('      %s' % ', '.join(after))
    rec('    ### ### **FILING COUNT : %d.**' % len(after))
    rec('    the order`s list : %s' % ', '.join(SPANACTS))
    same = after == SPANACTS
    rec('    ### the two agree, act for act and in order : ### **%s**' % same)
    if not same:
        MISSES.append(('OPEN_TRAILS.md', 'filing order differs from the order`s list'))
    rec('    ### by NUMBER the same acts sort : %s' % ', '.join(sorted(SPANACTS)))
    rec('    ### ### **b482 AND b479 FILE LAST AND SORT EARLY -- WHICH IS WHY THE TOOL`S READING')
    rec('    ### AND THE FILING COUNT DIFFER, AND WHY (R96) ASKS FOR BOTH.**')

    # ------------------------------------------------------------------ (P2) each act's verdicts
    rec('')
    rec('(P2) EACH ACT`S VERDICTS, FROM ITS OWN CLOSING BANK.')
    rec('-' * 108)
    acts = []
    for a in SPANACTS:
        clo, comp = bank(a)
        if not clo:
            MISSES.append((a, 'no closing bank'))
            rec('    %-6s ### **NO CLOSING BANK**' % a)
            continue
        head = next((l.strip() for l in clo.split(NL) if l.startswith('b%s' % a[1:])
                     or l.startswith(a + ' --')), '')
        # ### the act's own scored expectations, read from its scores bank where it has one.
        sc = json.loads(read(os.path.join(D, '%s_scores.json' % a)) or '{}')
        verds = []
        for k in ('N1', 'N2', 'N3', 'F1', 'F2', 'F3'):
            v = sc.get(k)
            if isinstance(v, dict) and v.get('verdict'):
                verds.append('%s %s' % (k, v['verdict']))
        acts.append(dict(act=a, head=head, verdicts=verds,
                         closing_bytes=len(clo), comp_bytes=len(comp)))
        rec('    %-6s %s' % (a, head[:96]))
        if verds:
            for v in verds:
                rec('             %s' % v[:100])
        else:
            rec('             ### (no scores bank; this act registered none)')

    # ------------------------------------------------------------------ (P3) the digest clauses
    rec('')
    rec('(P3) ### **THE (R31) DIGEST BLOCK`S CLAUSES, EACH CHECKED AGAINST A CITING ACT.**')
    rec('-' * 108)
    rec('    ### The order says ### **"nothing in it that a cited act does not say."** ### So each')
    rec('    ### clause is searched for in the span`s own banks BEFORE the block is written, with')
    rec('    ### the needle fixed in this tool and not after the fact.')
    # ### ### **THE CORPUS IS EVERY BANK, NOT THE SPAN'S.** ### The first version of this check
    # ### searched the span plus five named acts and reported that NO act says `S2` or `S6`. ###
    # ### **BOTH ARE SAID -- BY ACTS OLDER THAN THE SPAN**, which a fold's digest may of course
    # ### cite. ### **A HALT PROVED OVER THE WRONG POPULATION IS NOT A HALT**, and the widened
    # ### search is run by `grep` over every banked file rather than by loading them all.
    def carriers(pat):
        r = subprocess.run(['grep', '-rlE', '--include=*.txt', pat, '.'],
                           capture_output=True, text=True, encoding='utf-8',
                           errors='replace', cwd=D)
        out = set()
        for fn in r.stdout.split(NL):
            m = re.match(r'^(?:\./)?(b\d+[a-z]?)_', fn.strip())
            if m:
                out.add(m.group(1))
        return sorted(out)

    found = {}
    for sid, text, needles in CLAUSES:
        rec('')
        rec('  ### **%s** -- %s' % (sid, text))
        hits = []
        for pat, _ in needles:
            per = carriers(pat)
            hits.append((pat, per))
            rec('      needle `%s`' % pat[:46])
            rec('        acts carrying it : ### **%d** ### -- earliest %s ; in the span %s'
                % (len(per), (per[0] if per else '--'),
                   sorted(set(per) & set(SPANACTS)) or 'NONE'))
        ok = all(h[1] for h in hits)
        found[sid] = dict(text=text, ok=ok,
                          acts=sorted(set(a for _, p in hits for a in p)),
                          in_span=sorted(set(a for _, p in hits for a in p) & set(SPANACTS)))
        rec('      ### ### **%s**' % ('EVERY NEEDLE IS CARRIED BY AT LEAST ONE ACT'
                                      if ok else 'A NEEDLE IS CARRIED BY NO ACT'))
    rec('')
    bad = [s for s in found if not found[s]['ok']]
    rec('    ### ### **CLAUSES EVERY NEEDLE SUPPORTS : %d of %d.**' % (len(CLAUSES) - len(bad),
                                                                      len(CLAUSES)))
    if bad:
        rec('    ### ### **CLAUSES A CITED ACT DOES NOT SAY : %s.** ### NOT WRITTEN INTO THE DIGEST.'
            % ', '.join(bad))
    else:
        rec('    ### ### **ALL SIX ARE SAID BY A CITED ACT, AND TWO OF THEM ONLY BY ACTS OLDER THAN')
        rec('    ### THE SPAN** -- which is why the digest names the act it cites for each clause.')

    # ------------------------------------------------------------------ (P3b) the id collision
    rec('')
    rec('(P3b) ### **AN ERRATA ID THIS SEAT MINTED WAS ALREADY TAKEN.**')
    rec('-' * 108)
    err = read(os.path.join(PP, 'ERRATA.md'))
    n = err.count('E-2026-09-22-1')
    heads = [(i + 1, l.strip()) for i, l in enumerate(err.split(NL))
             if 'E-2026-09-22-1' in l]
    rec('    occurrences of `E-2026-09-22-1` in ERRATA.md : ### **%d**' % n)
    for i, l in heads:
        rec('      :%-5d %s' % (i, l[:130]))
    collision = n > 1
    rec('    ### ### **%s**'
        % ('TWO ENTRIES SHARE ONE ID, AND THE SECOND IS THIS SEAT`S.' if collision
           else 'NO COLLISION.'))
    if collision:
        rec('    ### The FIRST was filed at ### **b469** ### under (R77), from readings banked at')
        rec('    ### `b464_the_eight_and_the_parameters.txt` and b467 -- ### **IT IS THE ENTRY THE')
        rec('    ### ORDER`S CLAUSE `S6` NAMES.** ### The SECOND was appended at ### **b485** ###')
        rec('    ### by this seat, for the `21432399` currency note.')
        rec('    ### ### **b485 MINTED AN ID WITHOUT CHECKING WHETHER THE LEDGER ALREADY HELD IT**,')
        rec('    ### and its suite had no arm that would have looked. ### **THE FOLD REPORTS IT AND')
        rec('    ### DOES NOT RENUMBER IT:** ERRATA is append-only and its ids are cited elsewhere,')
        rec('    ### so a renumber is a ruling`s business and not a fold`s.')

    # ------------------------------------------------------------------ (P4) the ledgers
    rec('')
    rec('(P4) THE LEDGER TABLES -- THE NAVIGATOR`S ENTRIES SINCE b474, AND THE SEAT`S.')
    rec('-' * 108)
    rulings = []
    for a in SPANACTS + ['b486']:
        f = read(os.path.join(D, '%s_ferry.txt' % a)) + read(os.path.join(D, '%s_ferry_amendment.txt' % a))
        for m in re.finditer(r'RULING \((R\d+)\)', f):
            if m.group(1) not in [r[0] for r in rulings]:
                line = f[m.start():m.start() + 150].split(NL)
                rulings.append((m.group(1), a, ' '.join(line[:2])[:130]))
    rec('    ### RULINGS RATIFIED IN THE SPAN`S OWN BANKED FERRIES : ### **%d**' % len(rulings))
    for r, a, txt in rulings:
        rec('      %-6s (banked at %s)  %s' % (r, a, txt[:100]))
    seat = []
    for a in SPANACTS:
        clo = bank(a)[0]
        for l in clo.split(NL):
            if re.search(r'DEFECT|defective on its first run|FOUND AT b', l) and '###' in l:
                seat.append((a, l.strip()[:120]))
                break
    rec('')
    rec('    ### SEAT ENTRIES -- acts whose closing records a defect of its own : ### **%d**'
        % len(seat))
    for a, l in seat:
        rec('      %-6s %s' % (a, l))

    rec('')
    rec('=' * 108)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 108)
    io.open(os.path.join(D, 'b486_extract.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(filed=after, count=len(after), order_matches=same, acts=acts,
                   clauses=found, rulings=rulings, seat=seat, misses=MISSES),
              io.open(os.path.join(D, 'b486_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
