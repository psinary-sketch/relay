# -*- coding: utf-8 -*-
"""b347_repairs.py -- THE COMPONENTS, IN THE ORDER THE SEALED REGISTRATION PUTS THEM.

###   (C) the run file's own clock      -- the utility's fixtures, and a census of what carries no clock.
###   (D) the audit's numerical limit   -- named in the audit's own output, and PRICED as a count.
###   (E) the flattener                 -- the utility's fixtures, and the REACH measured statically.
###   (F) the bar-floor rule            -- the gate's fixtures, the census over the record, this act's own file.
###   (G) the two-routes third clause and the standing clauses' v2 -- both written, both read back.
### ### **NOTHING HERE MEASURES AN OBJECT. ### THIS ACT MEASURES INSTRUMENTS.**
### ### Its own run file is written through `run_clock`, so it is the first run file in the corpus to carry the
### instant it was written -- which is the point of (C) and is stated rather than left to be noticed.
"""
import ast
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                  # noqa: E402
import gate_text                  # noqa: E402
import registration_gate as RG    # noqa: E402

D = os.path.join(ROOT, 'data')
TC = r'D:\MY-DOwnloads\TECHNE-Core'
MOD = os.path.join(TC, 'modules', '2026-09')
IDXM = os.path.join(TC, 'modules', 'INDEX.md')
REG = os.path.join(D, 'b347_registration_2026-09-06.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


# ### ==============================================================================================
# ### (C) THE RUN FILE'S OWN CLOCK.
# ### ==============================================================================================
def component_C():
    rec('')
    rec('=' * 100)
    rec("  (C) THE RUN FILE'S OWN CLOCK.")
    rec('=' * 100)
    rec('  THE FIXTURES, BOTH POLARITIES:')
    ok = run_clock.self_test(verbose=False)
    for line in _capture(run_clock.self_test):
        rec(line)
    runs = sorted(n for n in os.listdir(D) if n.endswith('.txt') and ('_run' in n or n.endswith('_run.txt')))
    with_clock = [n for n in runs if run_clock.read_stamp(os.path.join(D, n))]
    rec('')
    rec('  THE CENSUS OF WHAT CARRIES A CLOCK, over every run file in data/:')
    rec('    run files in the record : %d ; carrying a clock : %d ; carrying none : %d'
        % (len(runs), len(with_clock), len(runs) - len(with_clock)))
    rec('    carrying one : %s' % (with_clock if with_clock else 'none yet -- this act writes the first'))
    rec('    ### ### **THE REPAIR IS NOT RETROACTIVE AND THE CENSUS IS HOW THAT IS SAID IN NUMBERS.** ### Every')
    rec('    ### run file written before this tool carries no clock and cannot be given one; b345\'s `(E4)` stays')
    rec('    ### exactly as b345 declared it.')
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return dict(ok=bool(ok), runs=len(runs), with_clock=len(with_clock), named=with_clock)


def _capture(fn):
    import io as _io
    import contextlib
    buf = _io.StringIO()
    with contextlib.redirect_stdout(buf):
        fn(verbose=True)
    return [l for l in buf.getvalue().split(chr(10)) if l.strip()]


# ### ==============================================================================================
# ### (D) THE SATISFIABILITY AUDIT'S NUMERICAL LIMIT: NAMED, AND PRICED AS A COUNT.
# ### ==============================================================================================
def component_D():
    rec('')
    rec('=' * 100)
    rec("  (D) THE SATISFIABILITY AUDIT'S NUMERICAL LIMIT -- NAMED IN ITS OWN OUTPUT, AND PRICED.")
    rec('=' * 100)
    src = io.open(os.path.join(ROOT, 'tools', 'reg_satisfiable.py'), encoding='utf-8').read()
    named = 'A NUMERICAL ONE' in src and "bar-floor arms (b347)" in src
    rec('  the limit named in the audit\'s own printed output : %s' % named)
    # ### re-measure the audit on one registration, to show its existing verdicts are unchanged
    spec = os.path.join(D, 'b346_satisfiable.json')
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'reg_satisfiable.py'), spec],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    unchanged = 'JOINTLY SATISFIABLE' in (r.stdout or '')
    rec("  b346's spec re-audited after the edit and its verdict unchanged : %s" % unchanged)
    # ### THE PRICE, AS A COUNT READ FROM THE RECORD AND NOT AS A PLAN.
    regs = sorted(n for n in os.listdir(D) if re.match(r'^b\d+_registration_', n))
    carry, pairable, hand = [], [], []
    for n in regs:
        txt = io.open(os.path.join(D, n), encoding='utf-8', errors='replace').read()
        f, a, nth, nma = RG.bar_floor_check(txt)
        if nth:
            carry.append(n)
            (pairable if not f else hand).append(n)
    rec('')
    rec('  THE PRICE, AS A COUNT READ FROM THE RECORD. ### **A PRICE IS NOT A PREDICTION AND THIS IS NOT A PLAN.**')
    rec('    registrations in the record                                  : %d' % len(regs))
    rec('    carrying at least one numerical threshold                    : %d' % len(carry))
    rec('    whose thresholds already sit beside a floor or an UNPRICED    : %d' % len(pairable))
    rec('    that would need a hand reading to pair a threshold to a floor : %d' % len(hand))
    rec('    ### ### **THAT LAST NUMBER IS THE PRICE OF CLOSING THE LIMIT AT THE TEXTUAL LAYER.** ### The')
    rec('    ### NUMERICAL layer -- a checker that knows what floor a routine actually has -- is not priced here')
    rec('    ### and is not built. ### **THE LIMIT IS NAMED AND PRICED. ### IT IS NOT CLOSED.**')
    ok = named and unchanged
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return dict(ok=bool(ok), named=bool(named), verdict_unchanged=bool(unchanged),
                registrations=len(regs), carry=len(carry), pairable=len(pairable), hand=len(hand),
                hand_named=hand)


# ### ==============================================================================================
# ### (E) THE FLATTENER: ONE UTILITY, AND THE REACH MEASURED.
# ### ==============================================================================================
def _bf_phrases(path):
    """### STATICALLY: every string literal this checks file compares against its FLATTENED bank.
    ### ### **READ FROM THE SYNTAX TREE, NOT FROM A GREP, so a phrase inside a comment is not counted.**"""
    try:
        tree = ast.parse(io.open(path, encoding='utf-8').read())
    except (OSError, SyntaxError):
        return []
    out = []
    for n in ast.walk(tree):
        if not (isinstance(n, ast.Compare) and len(n.ops) == 1 and isinstance(n.ops[0], ast.In)):
            continue
        L, R = n.left, n.comparators[0]
        if not (isinstance(L, ast.Constant) and isinstance(L.value, str)):
            continue
        case = None
        # ### `phrase in bf`
        if isinstance(R, ast.Name) and R.id == 'bf':
            case = ''
        # ### `phrase in bf.lower()` / `.upper()` -- the arm b344 actually wrote, which a narrower
        # ### extractor misses. ### The case fold is applied to the phrase too, or the comparison is not
        # ### the one the act made.
        elif (isinstance(R, ast.Call) and isinstance(R.func, ast.Attribute)
              and isinstance(R.func.value, ast.Name) and R.func.value.id == 'bf'
              and R.func.attr in ('lower', 'upper')):
            case = R.func.attr
        # ### `phrase in flat(...)`
        elif isinstance(R, ast.Call) and isinstance(R.func, ast.Name) and R.func.id == 'flat':
            case = ''
        if case is None:
            continue
        out.append((L.value, case))
    return out


def component_E():
    rec('')
    rec('=' * 100)
    rec('  (E) THE FLATTENER -- ONE UTILITY, AND ITS REACH MEASURED.')
    rec('=' * 100)
    rec('  THE FIXTURES, BOTH POLARITIES:')
    ok = gate_text.self_test(verbose=False)
    for line in _capture(gate_text.self_test):
        rec(line)
    rec('')
    rec('  THE REACH, MEASURED STATICALLY FROM EACH ACT\'S OWN CHECKS FILE AGAINST ITS OWN BANK:')
    acts = [('b342', 'b342_checks.py', 'b342_the_two_rules_as_modules.txt'),
            ('b343', 'b343_checks.py', 'b343_the_maps_next_reach.txt'),
            ('b344', 'b344_checks.py', 'b344_the_floor_priced.txt'),
            ('b345', 'b345_checks.py', 'b345_the_li_control_rerun.txt'),
            ('b346', 'b346_checks.py', 'b346_the_exponent_by_rate.txt')]
    weakened, rows = [], []
    for act, tool, bank in acts:
        tp, bp = os.path.join(ROOT, 'tools', tool), os.path.join(D, bank)
        if not (os.path.exists(tp) and os.path.exists(bp)):
            rec('    %-6s ### one of its files is not present -- skipped' % act)
            continue
        txt = io.open(bp, encoding='utf-8', errors='replace').read()
        new, old = gate_text.flat(txt), gate_text.flat_b344(txt)
        def hit(phrase, case, hay):
            h = hay.lower() if case == 'lower' else (hay.upper() if case == 'upper' else hay)
            return phrase in h
        ph = _bf_phrases(tp)
        w = [p for p, c in ph if hit(p, c, new) and not hit(p, c, old)]
        both = [p for p, c in ph if hit(p, c, new) and hit(p, c, old)]
        neither = [p for p, c in ph if not hit(p, c, new)]
        rows.append(dict(act=act, phrases=len(ph), weakened=len(w), both=len(both), neither=len(neither), which=w))
        rec('    %-6s phrases compared against the flattened bank : %-3d ; found under BOTH : %-3d ; found ONLY under the repair : %-3d ; found under NEITHER : %d'
            % (act, len(ph), len(both), len(w), len(neither)))
        for p in w:
            rec('        ### WEAKENED BY THE DEFECT : %r' % p[:96])
            weakened.append((act, p))
    rec('')
    rec('    ### ### **ARMS THE DEFECT SILENTLY WEAKENED : %d**' % len(weakened))
    rec("    ### **AND THE MEASUREMENT'S OWN LIMIT, SO THE COUNT IS NOT READ FOR MORE THAN IT IS:** the extractor")
    rec('    ### reads the syntax tree for phrases compared against the flattened bank by name (`bf`, `bf.lower()`,')
    rec('    ### `bf.upper()`, `flat(...)`). ### **AN ARM THAT FLATTENS INTO A VARIABLE UNDER ANOTHER NAME, OR THAT')
    rec('    ### COMPARES A COMPUTED STRING RATHER THAN A LITERAL, IS INVISIBLE TO IT.** ### The count is a lower')
    rec('    ### bound on the reach and is reported as one.')
    rec('    ### **AND `found under NEITHER` IS NOT A DEFECT COUNT.** ### The extractor is STATIC and cannot see')
    rec('    ### which branch of a conditional arm ran. ### b343\'s two are one phrase, taken twice from the two')
    rec('    ### halves of a single `if/else` whose OTHER half is the one that matched; its arm passed on that')
    rec('    ### half. ### **A PHRASE IN AN UNTAKEN BRANCH IS NOT AN UNMATCHED ARM, AND NOTHING IS RE-VERDICTED')
    rec('    ### ON THIS COUNT.**')
    rec('    ### ### **AND WHAT FOLLOWS FROM THAT IS NOTHING AUTOMATIC.** ### An arm whose phrase failed to match')
    rec('    ### made its gate FAIL, not pass: ### **THE DEFECT\'S DIRECTION IS TOWARD FALSE ALARM, NOT TOWARD')
    rec('    ### FALSE CLEARANCE.** ### That is why it survived two acts -- a failing arm gets rewritten, and a')
    rec('    ### rewritten arm looks like a passing one. ### **NO PAST ACT IS RE-VERDICTED AND NO PAST COPY OF THE')
    rec('    ### FLATTENER IS EDITED: THE RECORD DOES NOT SILENTLY OVERWRITE ITSELF.**')
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return dict(ok=bool(ok), rows=rows, weakened=[list(x) for x in weakened])


# ### ==============================================================================================
# ### (F) THE BAR-FLOOR RULE: THE GATE'S FIXTURES, THE CENSUS, AND THIS ACT'S OWN REGISTRATION.
# ### ==============================================================================================
def component_F():
    rec('')
    rec('=' * 100)
    rec('  (F) THE BAR-FLOOR RULE -- THE GATE ARMS, THEIR FIXTURES, AND THE CENSUS OVER THE RECORD.')
    rec('=' * 100)
    rec('  THE FIXTURES, BOTH POLARITIES OF EACH ARM, ON SYNTHETIC TEXT DRAWN FROM NO BANK:')
    ok = RG.bar_floor_self_test(verbose=False)
    for line in _capture(RG.bar_floor_self_test):
        rec(line)
    rec('')
    rec('  THE INDEX-QUERY ARM, UNTOUCHED, STILL FIRING ON ITS OWN CASE:')
    import tempfile
    d2 = tempfile.mkdtemp(prefix='b347_gate_')
    p2 = os.path.join(d2, 'r.txt')
    io.open(p2, 'w', encoding='utf-8', newline=chr(10)).write('### THE ROUTE IS MARKED OPEN and nothing is queried.' + chr(10))
    rc2, _l = RG.check(p2)
    p3 = os.path.join(d2, 'q.txt')
    io.open(p3, 'w', encoding='utf-8', newline=chr(10)).write('### THE ROUTE IS MARKED OPEN ; the index was queried: NO KEY.' + chr(10))
    rc3, _l = RG.check(p3)
    idx_ok = (rc2 == 1 and rc3 == 0)
    rec('    a mark with no query -> HARD FAILURE (%d) ; a mark with a recorded query -> PASS (%d) : %s' % (rc2, rc3, idx_ok))
    rec('')
    rec('  THE CENSUS OVER EVERY REGISTRATION IN THE RECORD. ### **NO PAST REGISTRATION IS RE-VERDICTED.**')
    regs = sorted(n for n in os.listdir(D) if re.match(r'^b\d+_registration_', n))
    fires, clean, rows = [], [], []
    for n in regs:
        txt = io.open(os.path.join(D, n), encoding='utf-8', errors='replace').read()
        f, a, nth, nma = RG.bar_floor_check(txt)
        rows.append(dict(name=n, floor_misses=len(f), arm_misses=len(a), thresholds=nth, multiarm=nma))
        (fires if (f or a) else clean).append(n)
    rec('    registrations gated : %d ; would FIRE on at least one arm : %d ; CLEAR : %d'
        % (len(regs), len(fires), len(clean)))
    rec('    ### **THE ROWS THAT WOULD FIRE ARE LISTED; THE ONES THAT WOULD NOT ARE COUNTED AND NOT LISTED.** ### Most')
    rec('    ### of the record carries no numerical threshold at all, and a quiet row is quiet because there was')
    rec('    ### nothing for the arm to look at, not because the arm looked and approved.')
    rec('    %-46s %-12s %-12s %-12s %s' % ('registration', 'thresholds', 'floor miss', 'multi-arm', 'arm miss'))
    for r in rows:
        if not (r['floor_misses'] or r['arm_misses']):
            continue
        rec('    %-46s %-12d %-12d %-12d %d' % (r['name'][:46], r['thresholds'], r['floor_misses'], r['multiarm'], r['arm_misses']))
    quiet_no_threshold = sum(1 for r in rows if not r['thresholds'] and not r['multiarm'])
    rec('    ### of the %d that would not fire, %d carry NEITHER a threshold NOR a multi-arm passage for the arms to see'
        % (len(clean), quiet_no_threshold))
    rec('    ### ### **A REGISTRATION THAT WOULD FIRE IS NAMED AND LEFT EXACTLY AS IT IS.** ### The arms bind')
    rec('    ### registrations written AFTER them. ### Nothing above is edited and nothing is re-verdicted.')
    rec('')
    rec("  AND THIS ACT'S OWN REGISTRATION, GATED, ITS VERDICT REPORTED WHATEVER IT IS:")
    own = io.open(REG, encoding='utf-8', errors='replace').read()
    f, a, nth, nma = RG.bar_floor_check(own)
    rec('    thresholds %d ; floor misses %d ; multi-arm passages %d ; arm misses %d' % (nth, len(f), nma, len(a)))
    for ln, s in (f + a)[:10]:
        rec('        line %-5d %s' % (ln, s))
    rec('    ### ### **THIS ACT DOES NOT EXEMPT ITSELF, AND ITS OWN FILE IS SEALED, SO WHAT THE ARMS FIND HERE IS')
    rec('    ### ### CARRIED AND NOT FIXED.**')
    rec('  ### %s' % ('PASS' if (ok and idx_ok) else '### FAIL ###'))
    return dict(ok=bool(ok and idx_ok), fixtures=bool(ok), index_arm=bool(idx_ok),
                registrations=len(regs), would_fire=len(fires), clear=len(clean), fires=fires, rows=rows,
                own=dict(thresholds=nth, floor_misses=len(f), multiarm=nma, arm_misses=len(a),
                         lines=[[x, y] for x, y in (f + a)]))


# ### ==============================================================================================
# ### (G) THE TWO MODULES AND THE STANDING CLAUSES' SECOND VERSION.
# ### ==============================================================================================
BAR_FLOOR = '''# The bar-floor rule

*TECHNE module draft · extracted 2026-09-06 (research seat, b347) · **PRIVATE, TECHNE-Core, local-only**. Owning-act citations are to the `relay` record. **Grade-honest: a module states the grade its owning act carries and confers none.** Nothing deposits.*

---

## WHAT IT DOES

A numerical bar is stated **with the floor of the object it tests**. A bar below that floor is
**uninformative rather than strict**: it rejects a correct implementation exactly as it rejects a
broken one, so it separates nothing. And a bar with several arms is stated **with what makes the
arms independent**; arms that are algebraically one arm are one arm, and an arm that cannot vary
cannot contribute.

This is the resolving-power rule (b322) **one level down**. b322 asks whether two candidates sit
closer together than the instrument's own distance from the answer. This asks the same question of
a **bar** and its **object**: a threshold finer than what the object can reach is a threshold the
object can never satisfy, and a second arm that is the first arm is not a second measurement.

## WHEN IT APPLIES

Before a bar is sealed. The floor is a property of the routine, not of the run, so it can be
computed or bounded **before any value exists** — which is exactly when a registration is written.

## WHAT IT REFUSES

- A tolerance stated without the floor of the routine it is applied to.
- A multi-arm uncertainty whose arms are not shown to differ on an input the act actually ran.
- Reporting two arms as *agreeing* when one of them could not have disagreed.
- Repairing either defect after the fact by editing the sealed text. **A sealed bar found defective
  by running it is measured and tabled, never edited** — the companion module says the rest.

## THE TWO INCIDENTS THIS RULE IS MINTED FROM

**b345 — a bar finer than its object's floor.** The registration fixed a hand-rolled digamma at an
upward recurrence to `|w| >= 20` with the Stirling asymptotic through `B_10`, **and in the same
paragraph** required it to agree with a library implementation to `1e-25`. The first term that
truncation drops leaves the routine a floor near `4.4e-18`, and the measured miss tracked that
dropped term at every one of the six sealed points. **At `1e-25` the fixture rejected the correct
copy as well as the broken one, so at its own threshold it separated nothing.** Tabled, not
repaired. (relay `data/b345_the_li_control_rerun.txt`, section (4).)

**b346 — a bar whose two arms are algebraically one arm.** The registration defined an uncertainty
as the largest of three arms: the spread of a local slope over the top pair of a window, the drift
of a second estimator as the window's bottom was raised, and the difference between the two
estimators. But the second estimator was defined as the exponent annihilating a **two-point** drift
— and **a `q` that annihilates a two-point drift is algebraically the local slope of those same two
points**. So the second estimator collapsed onto the first: the third arm sat at machine level and
the second was **structurally zero**, since raising a window's bottom cannot move a top-pair
estimator. Tabled, not repaired, with the direction of the risk named — a structurally zero arm
cannot inflate an uncertainty, so it can only leave it understated — and the understatement bounded
by a labelled diagnostic. (relay `data/b346_the_exponent_by_rate.txt`, section (6) `(E1)`.)

## THE MECHANIZATION, AND WHAT IT IS WORTH

`relay/tools/registration_gate.py` gained two arms at b347. A paragraph stating a numerical
threshold must carry, in that same paragraph, either the floor of the object it tests or the token
`UNPRICED`; a paragraph declaring a bar with several arms must carry either what makes the arms
independent or the token `SINGLE-ARM`. Both arms have fixtures in both polarities.

**And the gate matches text.** It cannot tell a floor from the words of one, and a registration
that writes `UNPRICED` beside every bar passes and has priced nothing. **It raises the cost of an
unpriced bar from zero to a deliberate word** — which is the same reach `reg_seal.py` claims for
its own hash, and no more.

## PROVENANCE

- **Acts:** b345 (2026-09-06), the first incident, tabled on its own sealed face; b346 (2026-09-06),
  the second, likewise; b347 (2026-09-06), which minted the rule over both species and mechanized
  it. **The author ruled the rule and both additions; the seat wrote them.**
- **Ancestor:** b322's resolving-power rule (`RESOLVING_POWER.md`), of which this is the
  fixture-layer case; and `SEALED_BARS_FOUND_DEFECTIVE.md`, which says what to do once a defective
  bar has been found.
- **Grade:** b345 and b346 each carry their own act's grade and this module confers none. **The rule
  is a method, not a result.**
'''

TWO_ROUTES_BLOCK = '''
<!-- b347 -->

## THIRD CLAUSE — added 2026-09-06 (b347), by the author's order

*The text above is not edited. This block adds a clause; it withdraws none.*

**Two estimators are shown to differ on an input the act actually ran, or they are one estimator
wearing two names.** Sharing no code is necessary and is not sufficient: two routines written
separately can still compute the same expression, and one that is algebraically the other agrees
with it perfectly and certifies nothing.

**And a shared engine is named, with what it therefore does not certify.** Two routes that call the
same quadrature, the same eigensolver, or the same node counts share an error source; naming it is
not a defect, but claiming disjointness over it is.

**The incident.** b346 sealed a second estimator as the exponent annihilating the drift of
`rho^q eps` *across the top of the converged window* — two points. A `q` that annihilates a
two-point drift **is** the local slope of those two points, so the second estimator collapsed onto
the first: their difference sat at machine level and the uncertainty arm keyed to the window's
bottom was structurally zero. The act tabled it rather than repairing it, and said so rather than
reporting the two routes as agreeing. In the same act both evaluators took the prolate layer and
the node counts from the owner's files — declared deliberately by b313's copy-maker, because the
exponent reaches neither — and b346 named that shared engine and stated that independence of the
prolate solver is not certified. (relay `data/b346_the_exponent_by_rate.txt`, sections (6) `(E1)`
and `(E2)`.)

*Grade unchanged; this clause confers none. See `BAR_FLOOR_RULE.md` for the bar-side statement of
the same defect.*
'''


def component_G():
    rec('')
    rec('=' * 100)
    rec("  (G) THE TWO MODULES AND THE STANDING CLAUSES' SECOND VERSION.")
    rec('=' * 100)
    wrote = []
    # ### the new module
    p = os.path.join(MOD, 'BAR_FLOOR_RULE.md')
    if os.path.exists(p):
        rec('  BAR_FLOOR_RULE.md : ALREADY PRESENT -- not rewritten')
    else:
        io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(BAR_FLOOR)
        wrote.append('BAR_FLOOR_RULE.md')
        rec('  BAR_FLOOR_RULE.md : WRITTEN, %d lines' % len(BAR_FLOOR.splitlines()))
    shape = all(h in BAR_FLOOR for h in ('## WHAT IT DOES', '## WHEN IT APPLIES', '## WHAT IT REFUSES', '## PROVENANCE'))
    grade = 'confers none' in BAR_FLOOR
    rec('    the September shape (does / applies / refuses / provenance) : %s ; and it confers no grade : %s' % (shape, grade))
    # ### the appended block, nothing edited
    tr = os.path.join(MOD, 'TWO_ROUTES.md')
    before = io.open(tr, encoding='utf-8').read()
    if '<!-- b347 -->' in before:
        rec('  TWO_ROUTES.md     : the b347 mark is already present -- REFUSED, nothing written')
        appended = True
    else:
        io.open(tr, 'w', encoding='utf-8', newline=chr(10)).write(before.rstrip(chr(10)) + chr(10) + TWO_ROUTES_BLOCK)
        wrote.append('TWO_ROUTES.md')
        appended = True
    after = io.open(tr, encoding='utf-8').read()
    prefix = after.startswith(before.rstrip(chr(10)))
    rec('    TWO_ROUTES.md is a TRUE PREFIX of what it was, so nothing above the block is edited : %s' % prefix)
    rec('    the clause in the order\'s words : %s' % ('one estimator\nwearing two names' in TWO_ROUTES_BLOCK))
    # ### the standing clauses
    fs = io.open(os.path.join(ROOT, 'tools', 'FERRY_STANDING.md'), encoding='utf-8').read()
    v = re.search(r'^VERSION: (\d+)$', fs, re.M)
    v2 = v and v.group(1) == '2'
    authored = '## AUTHOR-RULED CLAUSES (NOT MEASURED)' in fs and '**A1**' in fs
    notmeasured = 'NOT MEASURED; carried by no count' in fs
    nottaught = 'THE SCAN HAS NOT BEEN TAUGHT THIS CLAUSE' in fs
    scan_src = io.open(os.path.join(ROOT, 'tools', 'ferry_scan.py'), encoding='utf-8').read()
    scan_untaught = 'act number' not in scan_src.lower()
    ck = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'b335_standing.py'), '--check'],
                        capture_output=True, text=True, encoding='utf-8', errors='replace')
    counts_ok = 'counts disagreeing with the file 0' in (ck.stdout or '')
    rec('')
    rec('  FERRY_STANDING : VERSION 2 : %s ; the author-ruled section present : %s' % (bool(v2), authored))
    rec('    the clause marked NOT MEASURED : %s ; the file says the scan was not taught it : %s' % (notmeasured, nottaught))
    rec('    and the scan really was NOT taught it (its source carries no act-number rule) : %s' % scan_untaught)
    rec('    every measured count RE-MEASURED LIVE and none disagreeing : %s' % counts_ok)
    ok = shape and grade and prefix and bool(v2) and authored and notmeasured and nottaught and scan_untaught and counts_ok
    rec('  ### TECHNE files written this run : %d (CAP 2)' % len(wrote))
    rec('  ### %s' % ('PASS' if ok else '### FAIL ###'))
    return dict(ok=bool(ok), wrote=wrote, prefix=bool(prefix), version2=bool(v2), authored=bool(authored),
                scan_untaught=bool(scan_untaught), counts_ok=bool(counts_ok))


def main():
    rec('=' * 100)
    rec('b347 -- THE THREE REPAIRS AND THE TWO RULES. ### THE COMPONENTS, IN THE SEALED ORDER.')
    rec('=' * 100)
    C = component_C()
    Dd = component_D()
    E = component_E()
    F = component_F()
    G = component_G()
    fails = [k for k, v in (('C', C), ('D', Dd), ('E', E), ('F', F), ('G', G)) if not v['ok']]
    rec('')
    rec('=' * 100)
    rec('  ### NOTHING HERE MEASURED AN OBJECT ; NO FRAME BUILT ; NO BAR MOVED ; NO ACT RE-VERDICTED.')
    rec('  ### COMPONENTS FAILING : %d %s' % (len(fails), fails if fails else ''))
    rec('=' * 100)
    p = run_clock.write(D, 'b347_repairs_run', LINES)
    io.open(os.path.join(D, 'b347_repairs.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(C=C, D=Dd, E=E, F=F, G=G, fails=fails, run_file=os.path.basename(p),
             run_clock=run_clock.read_stamp(p)), indent=1))
    print('  ### run file : %s ; its clock : %s' % (os.path.basename(p), run_clock.read_stamp(p)))
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
