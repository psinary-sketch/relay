# -*- coding: utf-8 -*-
"""lore_fixtures.py -- FIXTURES FOR THE MECHANIZABLE HARNESS-LORE RULES (built b266).

### WHY THIS EXISTS. `HARNESS_LORE.md` carries twenty-one rules and its own standing caution:
### ### **"Lore is not a guard."** ### b257: *"A rule in a module is not a mechanism."*
### ### **SO THE RULES THAT ### CAN ### BE MECHANIZED ARE MECHANIZED HERE, IN BOTH POLARITIES,
### ### AND THE ONES THAT CANNOT ARE NAMED AS JUDGEMENT RULES RATHER THAN QUIETLY LISTED BESIDE
### ### THEM AS THOUGH THEY WERE THE SAME KIND OF THING.**

### EACH FIXTURE HAS TWO LEGS AND BOTH MUST HOLD:
###   ### **POSITIVE** -- the law's own violation is DETECTED. ### A detector that never fires is
###     not a detector.
###   ### **NEGATIVE** -- a compliant case is NOT flagged. ### A detector that always fires is not
###     a detector either, and it is the failure mode that looks like rigour.
"""

# ### THE LIMIT, STATED IN THE HEADER BECAUSE A FIXTURE SUITE'S REACH WILL OTHERWISE BE ASSUMED.
# ### ### **THESE FIXTURES TEST THE ### SHAPE ### OF EACH LAW ON CONSTRUCTED DATA. ### THEY DO
# ### ### NOT TEST THAT A FUTURE ACT WILL APPLY THE LAW.** ### Rules 12, 14, 15, 16, 17, 19 are
# ### judgement rules: they govern what an act CHOOSES to do, and no fixture reaches a choice.
# ### **FILED AS LORE WITH THEIR INCIDENTS, NOT AS MECHANISMS.**
import sys


def leg(name, positive, negative):
    ok = bool(positive) and bool(negative)
    print('  %-46s pos:%-5s neg:%-5s %s'
          % (name, 'FIRES' if positive else 'MISS', 'quiet' if negative else 'FALSE-POS',
             'PASS' if ok else '### FAIL ###'))
    return ok


def main():
    print('=' * 96)
    print('HARNESS-LORE FIXTURES (lore_fixtures.py, b266) -- BOTH POLARITIES, RUN NOT CLAIMED')
    print('=' * 96)
    ok = True

    # ---------------------------------------------------------------- rule 11
    # ### A falsifier's verdict is bounded by its instrument's resolution.
    # ### The mechanism: a mode is RESOLVED only if its eigenvalue is stable under NQ -> 2NQ.
    def resolved(lam_nq, lam_2nq, bar=1e-6):
        return [i for i, (a, b) in enumerate(zip(lam_nq, lam_2nq))
                if abs(a - b) / max(abs(a), 1e-300) <= bar]

    # ### POSITIVE: b264's real shape -- the last two modes drift and MUST be excluded.
    lam1 = [1.0, 1e-3, 1e-6, 2.18e-8, 1.81e-8]
    lam2 = [1.0, 1e-3, 1e-6, 2.12e-8, 1.93e-8]
    pos11 = (resolved(lam1, lam2) == [0, 1, 2])
    # ### NEGATIVE: a genuinely resolved spectrum must NOT be truncated.
    neg11 = (resolved([1.0, 1e-3, 1e-6], [1.0, 1e-3, 1e-6]) == [0, 1, 2])
    ok &= leg('11 resolution bounds the falsifier', pos11, neg11)

    # ---------------------------------------------------------------- rule 13
    # ### Registrations are satisfiability-checked before sealing.
    def satisfiable(cap, demand):
        return demand <= cap

    # ### POSITIVE: b264's actual clause (I) -- 256 MB cap against the 204800 MB implied.
    pos13 = (satisfiable(256, 204800) is False)
    # ### NEGATIVE: b265's actual clause -- 512 MB cap against Q.layer(5600)'s 250.88 MB.
    neg13 = (satisfiable(512, 250.88) is True)
    ok &= leg('13 satisfiability before the seal', pos13, neg13)

    # ---------------------------------------------------------------- rule 18
    # ### Convergence needs INTERLEAVED axes; replicates sharing an error source certify nothing.
    def converged(outer_pair, inner_pair, bar=1e-8):
        """### BOTH axes, as b264's D2 correction requires."""
        def rel(p):
            a, b = p
            return abs(a - b) / max(abs(b), 1e-300)
        return rel(outer_pair) <= bar and rel(inner_pair) <= bar

    # ### POSITIVE: b264's real false pass -- the outer legs agree to 1e-12 while the inner
    # ### axis is off by 7.6. ### **A SINGLE-AXIS TEST WOULD HAVE CERTIFIED THIS.**
    pos18 = (converged((1.0, 1.0 + 1e-12), (1.0, 8.6)) is False)
    # ### NEGATIVE: a genuinely converged cell must pass both.
    neg18 = (converged((1.0, 1.0 + 1e-12), (1.0, 1.0 + 1e-12)) is True)
    ok &= leg('18 interleaved axes, not replicates', pos18, neg18)

    # ### AND THE SHARPER HALF OF 18, WHICH b265 FOUND ONE LEVEL DOWN:
    # ### a bar below the round-off floor of its own comparison measures noise, never the effect.
    def bar_is_readable(bar, value, roundoff_abs):
        return bar > roundoff_abs / max(abs(value), 1e-300)

    # ### POSITIVE: b265's real numbers -- a 1e-8 bar on A_0 ~ 5.6e-07 with 2.5e-14 round-off
    # ### gives a relative floor of ~4.4e-08. ### **THE BAR SAT BELOW ITS OWN FLOOR.**
    pos18b = (bar_is_readable(1e-8, 5.6e-7, 2.5e-14) is False)
    neg18b = (bar_is_readable(1e-6, 5.6e-7, 2.5e-14) is True)
    ok &= leg('18b a bar below its own round-off floor', pos18b, neg18b)

    # ---------------------------------------------------------------- rule 20
    # ### Exposure is graded by CALL PATH before it is measured.
    def exposed(body, symbol='Q.layer'):
        return symbol in body

    pos20 = (exposed('x = Q.layer(EPS_NQ)\n    return an(u)') is True)
    neg20 = (exposed('total = 0.0\n    for p in primes:\n        total += corr(k)') is False)
    ok &= leg('20 exposure by call path', pos20, neg20)

    # ### AND THE BUG THIS RULE'S OWN MECHANIZATION SHIPPED WITH (b265 D1, rule 5's family):
    # ### a body extractor must FIND the next definition, never be told its name.
    def body_of(src, fn):
        i = src.index('def %s' % fn)
        j = src.find(chr(10) + 'def ', i + 1)
        return src[i:j] if j > 0 else src[i:]

    src = ('def staircase(p, a):\n    return 1\n'
           'def left_side(a):\n    return 2\n'
           'def per_mode_eps_grids(rr):\n    x = Q.layer(EPS_NQ)\n')
    # ### POSITIVE: the correct extractor does NOT leak the later function's call into left_side.
    pos20b = (exposed(body_of(src, 'left_side')) is False)
    # ### NEGATIVE: it still finds the call where the call actually is.
    neg20b = (exposed(body_of(src, 'per_mode_eps_grids')) is True)
    ok &= leg('20b body extraction finds its successor', pos20b, neg20b)

    # ---------------------------------------------------------------- rule 21
    # ### A check's scope is stated as precisely as its finding.
    def scope_of(path, created_by_this_act, added_lines, total_lines):
        """### A file the act APPENDED to is scoped to its ADDED lines, not its whole text."""
        return total_lines if created_by_this_act else added_lines

    # ### POSITIVE: b265's real slip -- ERRATA.md scoped as created would sweep 232 lines
    # ### when the act wrote 30.
    pos21 = (scope_of('ERRATA.md', True, 30, 232) != scope_of('ERRATA.md', False, 30, 232))
    # ### NEGATIVE: a genuinely created file IS its whole text.
    neg21 = (scope_of('b266_run.txt', True, 90, 90) == 90)
    ok &= leg('21 created-vs-appended scope', pos21, neg21)

    print('')
    print('  ### **MECHANIZED: rules 11, 13, 18 (two legs), 20 (two legs), 21 -- SEVEN FIXTURES,')
    print('  ### EACH IN BOTH POLARITIES, EACH BUILT FROM ITS INCIDENT\'S OWN NUMBERS.**')
    print('  ### **JUDGEMENT RULES, NOT MECHANIZED AND SAID SO: 12, 14, 15, 16, 17, 19.**')
    print('  ###   They govern what an act CHOOSES to do -- to price a refusal, to distrust a')
    print('  ###   pre-authorized headline, to read before counting. ### **NO FIXTURE REACHES A')
    print('  ###   CHOICE, AND FILING THEM AS MECHANISMS WOULD BE THE SAME INTENTION WEARING A')
    print('  ###   TOOL\'S CLOTHES.**')
    print('')
    print('  VERDICT : ### **%s**' % ('ALL FIXTURES PASS IN BOTH POLARITIES'
                                      if ok else 'A FIXTURE FAILED'))
    print('  ### **AND THE STANDING CAUTION IS NOT RETIRED BY THIS FILE: LORE IS NOT A GUARD.**')
    print('  ### These fixtures test the SHAPE of each law on constructed data. ### They do not')
    print('  ### test that a future act will apply it.')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
