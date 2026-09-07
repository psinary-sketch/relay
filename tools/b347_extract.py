# -*- coding: utf-8 -*-
"""b347_extract.py -- THE EXTRACT STEP FOR THE THREE REPAIRS AND THE TWO RULES. ### **EVERY READ, TO DISK.**

### ### **WHAT THIS ACT IS READING FOR.** ### The two incidents the bar-floor rule is minted from, each at its own
### bank: b345's fixture, whose threshold sat below the floor of the routine it tested, and b346's uncertainty arm,
### whose second estimator was algebraically its first. ### b322's resolving-power rule, of which the new rule is the
### fixture-layer case, quoted from the act that sealed it. ### b344's seal-clock repair, which is the SHAPE the run
### file's clock repair follows, and its own honest limit. ### b345's `(E4)`, which is why a run file needs a clock at
### all. ### The satisfiability audit's own statement of its reach, which this act prices rather than closes. ### The
### flattener as it stands in every act that copied it, so the repair's reach is measured and not asserted. ### The
### standing-clauses file's own rule about what may be added to it, because the act-number clause is the author's and
### not a measured one. ### The two-routes module's existing text, so the third clause is APPENDED and nothing is
### edited. ### And the order's own sentences. ### b283's law: every quotation at its emitting file and its line.
"""
import io
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = r'D:\MY-DOwnloads\PLACE-papers'
TC = r'D:\MY-DOwnloads\TECHNE-Core'
MOD = os.path.join(TC, 'modules', '2026-09')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

NOTES = os.path.join(D, 'b347_extract_notes.txt')


def d(n):
    return os.path.join(D, n)


def t(n):
    return os.path.join(ROOT, 'tools', n)


ORDER = d('b347_order_2026-09-06.txt')

WANTED = [
    # ### ---- INCIDENT ONE: a bar finer than its object's floor (b345)
    ('b345 -- the fixture is a defective bar', d('b345_the_li_control_rerun.txt'),
     '### ### **THE TWO CANNOT BOTH HOLD, AND RUNNING THE FIXTURE IS WHAT SHOWED IT.**'),
    ('### it separates nothing at its own threshold', d('b345_the_li_control_rerun.txt'),
     '### **AT `1e-25` THE FIXTURE REJECTS THE CORRECT COPY AS WELL'),
    ('### the defective half is the recurrence threshold', d('b345_the_li_control_rerun.txt'),
     '### **THE DEFECTIVE HALF IS THE'),
    ('### a measurement is not a met bar', d('b345_the_li_control_rerun.txt'),
     '### instead is a measurement -- agreement to `4.394e-18` -- and ### **A MEASUREMENT IS NOT A MET BAR.**'),
    ("### (E4), why a run file needs a clock", d('b345_the_li_control_rerun.txt'),
     '### ### RUNNING ITS OWN SUITE TWICE.**'),
    ('### the seal is dated and the component is not', d('b345_the_li_control_rerun.txt'),
     '### own clock -- this act\'s registration is the first that does, at `2026-09-06T22:37:06Z` -- but ### **NO RUN FILE'),
    # ### ---- INCIDENT TWO: a bar whose two arms are algebraically one arm (b346)
    ('b346 -- (E1), the sealed uncertainty arm that did no work', d('b346_the_exponent_by_rate.txt'),
     '### ### **(E1) ONE OF THE SEALED UNCERTAINTY ARMS DID NO WORK, AND THE SEALED PAIRING IS DEFECTIVE.**'),
    ('### a two-point drift-zero is the local slope', d('b346_the_exponent_by_rate.txt'),
     '### ### SLOPE OF THOSE SAME TWO POINTS.**'),
    ('### the direction of the risk', d('b346_the_exponent_by_rate.txt'),
     '### ### **THE DIRECTION OF THE RISK, NAMED:**'),
    ('### a bar whose two arms are the same arm', d('b346_the_exponent_by_rate.txt'),
     '### ### THAT ORDER: A BAR WHOSE TWO ARMS ARE THE SAME ARM.**'),
    ('### (E2), the shared engine', d('b346_the_exponent_by_rate.txt'),
     '### ### **(E2) THE TWO EVALUATORS SHARE AN ENGINE, AND IT IS NAMED RATHER THAN CLAIMED ABSENT.**'),
    # ### ---- THE RULE THE NEW ONE IS A CASE OF
    ('b322 -- under-resolved is the weaker of the two', d('b322_components_run.txt'),
     '  ### ### ### **THE ACT TAKES THE WEAKER OF THE TWO: ### UNDER-RESOLVED.** ###'),
    ('### and it carries its price', d('b322_the_membership.txt'),
     '### ### ### **(5) SO THE VERDICT IS `UNDER-RESOLVED`, AND IT CARRIES ITS PRICE.**'),
    ('the resolving-power module, which this rule extends downward', os.path.join(MOD, 'RESOLVING_POWER.md'),
     '# The resolving-power rule'),
    # ### ---- THE SHAPE THE CLOCK REPAIR FOLLOWS, AND ITS HONEST LIMIT
    ("b344 -- the seal's own clock, by the order's words", t('reg_seal.py'),
     "CLOCK = '### sealed at (UTC) : '"),
    ('### the clock is outside the hash, said where the line is written', t('reg_seal.py'),
     '# ### `cmd_verify` are untouched; they cover the bytes ABOVE the block, so every seal written before this line existed'),
    ('### it recovers nothing sealed before it', t('reg_seal.py'),
     '# ### the seal was written by a tool that meant to record it. ### **IT RECOVERS NOTHING SEALED BEFORE IT, b342\'s OWN'),
    ('b344 -- the census before and after, none rewritten', t('b344_seal_clock.py'),
     '###   `--before`   every sealed file in `data/` verified and its verdict recorded, before the edit.'),
    # ### ---- THE AUDIT WHOSE REACH THIS ACT PRICES RATHER THAN CLOSES
    ("the satisfiability audit's own statement of its reach", d('audit_b346_reg_satisfiable.txt'),
     '  ### REACH: it compares the pairs it is GIVEN. ### A ceiling whose demand the act'),
    ('### it narrows the class; it does not close it', d('audit_b346_reg_satisfiable.txt'),
     '  ### **IT NARROWS THE CLASS; IT DOES NOT CLOSE IT.**'),
    ("b345 -- the audit could not catch a numerical inconsistency", d('b345_the_li_control_rerun.txt'),
     '### ### **THE SATISFIABILITY AUDIT DID NOT AND COULD NOT CATCH IT:**'),
    # ### ---- THE FLATTENER, AS IT STANDS IN EVERY COPY
    ('the flattener as b344 wrote it', t('b344_checks.py'),
     "    return re.sub(r'\\s+', ' ', re.sub(r'(?m)^###\\s*', ' ', s.replace('\\u2019', \"'\"))).strip()"),
    ('### as b345 copied it', t('b345_checks.py'),
     "    return re.sub(r'\\s+', ' ', re.sub(r'(?m)^###\\s*', ' ', s.replace('\\u2019', \"'\"))).strip()"),
    ('### and as b346 repaired it locally', t('b346_checks.py'),
     "    return re.sub(r'\\s+', ' ', re.sub(r'(?m)^(?:###\\s*)+', ' ', s.replace('\\u2019', \"'\"))).strip()"),
    ('b346 -- the closing record naming the defect', d('b346_checks_after.txt'),
     '  G-ROUTES (route B calls no function of route A; both evaluators unedited; the shared engine NAMED; the collapsed arm DECLARED):'),
    # ### ---- THE STANDING-CLAUSES FILE'S OWN RULE ABOUT WHAT MAY BE ADDED
    ('FERRY_STANDING -- the version and the citation form', t('FERRY_STANDING.md'),
     'VERSION: 1'),
    ('### the rule, and that the seat adds none by hand', t('FERRY_STANDING.md'),
     'RULE: a clause is STANDING when a majority of the range carries it (8 or more of 15); a clause below that is listed as FREQUENT, NOT STANDING; the seat adds none by hand'),
    ('### this file binds nothing by itself', t('FERRY_STANDING.md'),
     'THIS FILE BINDS NOTHING BY ITSELF: a ferry that restates a clause is not in conflict with it'),
    ('### its generator', t('b335_standing.py'), 'VERSION = 1'),
    ('the collision that the act-number clause answers', d('b344_ruling_2026-09-06.txt'),
     'behaviour and is banked as such. Add to FERRY_STANDING v2, when'),
    # ### ---- THE MODULE THAT GAINS A CLAUSE, AND THE SHAPE A MODULE TAKES
    ('the two-routes module -- what it refuses', os.path.join(MOD, 'TWO_ROUTES.md'),
     '## WHAT IT REFUSES'),
    ('### two quadratures over one integrand', os.path.join(MOD, 'TWO_ROUTES.md'),
     '- Two quadratures over one integrand as corroboration:'),
    ('### a module confers no grade', os.path.join(MOD, 'TWO_ROUTES.md'),
     'a module states the grade its owning act carries and confers none'),
    ('the defective-bars module, which the new rule sits beside', os.path.join(MOD, 'SEALED_BARS_FOUND_DEFECTIVE.md'),
     '# '),
    # ### ---- THE ORDER
    ('the order -- the rule over both species', ORDER,
     '(1) The bar-floor rule is stated over BOTH species and the'),
    ('### the gate mechanization, both arms', ORDER,
     'numerical threshold carries its object\'s floor or the word'),
    ('### the two-routes third clause', ORDER,
     '(2) The two-routes module gains the third clause by appended'),
    ('### the flattener repair and its reach', ORDER,
     '(3) The flattener defect is repaired in the gate utility once,'),
    ('### and the fold is next', ORDER,
     'After b347, the board returns to mathematics and the next act'),
]


def main():
    lines = []

    def rec(x=''):
        lines.append(x)

    rec('=' * 100)
    rec('b347_extract.py -- THE THREE REPAIRS AND THE TWO RULES. ### EVERY QUOTATION AT ITS EMITTING FILE, WITH ITS LINE.')
    rec('=' * 100)
    missing, paths_missing = 0, 0
    for lbl, path, frag in WANTED:
        rec('### ==== %s' % lbl)
        if not os.path.exists(path):
            paths_missing += 1
            rec('###      %s | ### **FILE NOT PRESENT**' % path)
            continue
        body = io.open(path, encoding='utf-8', errors='replace').read().splitlines()
        hits = [(i + 1, ln) for i, ln in enumerate(body) if frag in ln]
        short = path.replace(PP, '<papers>').replace(TC, '<techne>').replace(ROOT, '<relay>').replace(chr(92), '/')
        rec('###      %s | fragment %r | %d hit(s)' % (short, frag, len(hits)))
        if not hits:
            missing += 1
            rec('###      ### **NOT FOUND**')
            continue
        for n, ln in hits[:2]:
            rec('    | line %-5d %s' % (n, ln.strip()[:520]))
        rec('')
    rec('  ### ### **PATHS MISSING : %d ; QUOTATIONS NOT FOUND : %d**' % (paths_missing, missing))
    rec('=' * 100)
    io.open(NOTES, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(lines) + chr(10))
    print(chr(10).join(lines[-3:]))
    return 0 if not (missing or paths_missing) else 5


if __name__ == '__main__':
    sys.exit(main())
