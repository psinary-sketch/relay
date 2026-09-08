# -*- coding: utf-8 -*-
"""b363_census.py -- THE CENSUS, THE CLASSIFICATION, AND THE CONTROL.

### ### **NO SCANNER INFERS A JUDGEMENT FROM PROSE HERE** -- `b357`'s incident, and the right cure here for
### the same reason it was there: ### **THE SUBJECT OF THIS ACT IS A CHECK THAT COULD CONFIRM RATHER THAN
### ### TEST.** ### So the classification is ### **DECLARED DATA**, stated arm by arm by this seat, with the
### anchor it rests on located and printed beside it.
### ### **WHAT THE TOOL DOES DECIDE:** ### the arithmetic. ### It sums the banks' own headline figures, sums
### the enumerated arms, compares the two, and compares both against the draft's figure -- ### **AND IT
### ### REFUSES TO EMIT IF THE ENUMERATION AND THE HEADLINES DISAGREE**, because a census whose parts do not
### add to its own total is not a census.
### ### **AND THE CONTROL:** ### the banked suites are ### **NOT EDITED.** ### Each is COPIED into `tools/`
### under a declaring name so its own path arithmetic still works, run, compared against the verdict its own
### act banked, and ### **THE COPY IS DELETED IN A `finally`.** ### The copies are not tools this act ships.
"""
import io
import json
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock               # noqa: E402
import anchor_from_file as AF  # noqa: E402
import gate_needle as GN       # noqa: E402  ### THE HELPER THIS ACT BUILDS, EXERCISED HERE

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


B360, B361, B362 = d('b360_the_fold.txt'), d('b361_the_held_item.txt'), d('b362_the_approximation_register.txt')
DRAFT = d('b362_closing.txt')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


# ### (act, bank, the headline hint, the figure the headline declares, spelled as the bank spells it)
HEADLINES = [
    ('b360', B360, '(E7) FOUR ARMS OF THIS ACT', 4, 'FOUR'),
    ('b361', B361, '(E4) TWO ARMS OF THIS ACT', 2, 'TWO'),
    ('b362', B362, '(E5) FIVE ARMS OF THIS ACT', 5, 'FIVE'),
]

# ### THE POPULATION, ARM BY ARM. ### (id, act, bank, the anchor hint, what the arm was, the class, the
# ### reason). ### **THE CLASS IS THIS SEAT'S JUDGEMENT AND IS DECLARED, NOT INFERRED.**
R = 'RETIRED BY THE HELPER'
N = 'NOT RETIRED'
ARMS = [
    ('A1', 'b360', B360,
     'RATHER THAN SOFTENED.** ### One self-needle was typed with a marker prefix the bank does not carry',
     'a self-needle typed with a marker prefix the bank does not carry on that line', R,
     'the needle was TYPED. ### Built from the file it would have been the file’s own line, markers and '
     'all.'),
    ('A2', 'b360', B360,
     "RETIRE IT** -- and was re-typed against the file. ### One arm looked for the deposit",
     "a plain substring searched against markup carrying emphasis inside the phrase", R,
     'a PRESENTATION mismatch. ### The helper discards emphasis on both sides, so the arm would have been '
     'quiet on the same text.'),
    ('A3', 'b360', B360, 'FIRST VERSION DEMANDED A COMPONENT ORDER THIS ACT NEVER PROMISED',
     'G-ORDER demanded an ordering between two components that the registration never fixed', N,
     '### **A WRONG ARM.** ### Its predicate tested the seat’s habits and not the ritual its label '
     'named. ### **NO NEEDLE TOOL REACHES THIS**, and a needle built from a file is still a needle for the '
     'wrong question.'),
    ('A4', 'b360', B360,
     'component order as measured rather than demanding one. ### And ### **`G-ROSTER`',
     "G-ROSTER searched the raw bank for a sentence the bank wraps through", R,
     'a PRESENTATION mismatch, of the wrapping kind. ### The helper compares with markers and line breaks '
     'discarded on both sides.'),
    ('A5', 'b361', B361, 'FILE.** ### `G-SCOPE`',
     'G-SCOPE typed a noun the reading does not use', R,
     'the needle was TYPED, and typed with a different word for the same thing. ### Built from the file it '
     'would have carried the file’s noun.'),
    ('A6', 'b361', B361, "and `G-NUMBERS` asked for the correspondence row",
     'G-NUMBERS asked the bank for a row number the bank had not printed', N,
     '### **A MISSING SENTENCE, AND THE ARM WAS RIGHT.** ### The bank genuinely did not carry the number; '
     'the cure was the bank printing what it owed. ### **A HELPER THAT MADE THIS ARM QUIET WOULD BE A '
     'DEFECT AND NOT A CURE.**'),
    ('A7', 'b362', B362,
     'CORRECTED TO THE FILE RATHER THAN SOFTENED.** ### Two were inherited needles still carrying the',
     'an inherited needle carrying the previous leg’s wording', R,
     'the needle was TYPED, and inherited. ### **THE HELPER RAISES ON A HINT THAT MATCHES NOTHING IN ITS '
     'OWN FILE**, so the silence becomes a refusal.'),
    ('A8', 'b362', B362,
     'CORRECTED TO THE FILE RATHER THAN SOFTENED.** ### Two were inherited needles still carrying the',
     'a second inherited needle, same shape', R,
     'the same, and it shares its bank line with A7 -- ### **THE BANK DESCRIBES TWO ARMS IN ONE SENTENCE**, '
     'which is why the census counts arms and not lines.'),
    ('A9', 'b362', B362, "previous leg",
     'an arm asked the bank for a row number the bank had not printed', N,
     '### **A MISSING SENTENCE, AND THE ARM WAS RIGHT** -- the same shape as A6, in a second act.'),
    ('A10', 'b362', B362,
     'THE WRONG ARM ENTIRELY** -- a true-prefix test on a ledger whose new row is SPLICED INTO THE',
     'a true-prefix test on a ledger whose new row is spliced into the table', N,
     '### **A WRONG ARM**, and the bank says so in those words. ### The predicate tested append-onlyness '
     'where the correct write is an insertion. ### **NO NEEDLE TOOL REACHES THIS.**'),
    ('A11', 'b362', B362, "THE NEEDLE-WRAPPING SPECIES, TWICE OVER**: the deposit",
     'a phrase printed across two INDENTED lines, where the shared flattener strips markers only at the '
     'start of a line', R,
     'a PRESENTATION mismatch. ### **AND IT IS THE ARM THAT SET THIS HELPER’S NORMALISATION**: '
     '`gate_text.flat` could not reach it, so `gate_needle.norm` strips marker runs WHEREVER THEY OCCUR.'),
]

SUITES = [('b355', 0), ('b356', 0), ('b357', 0), ('b360', 0), ('b361', 0), ('b362', 0)]
BANKED = {'b355': 'b355_checks_run.txt', 'b356': 'b356_checks_run.txt', 'b357': 'b357_checks_postpush.txt',
          'b360': 'b360_checks_postpush.txt', 'b361': 'b361_checks_postpush.txt',
          'b362': 'b362_checks_postpush.txt'}


def banked_verdict(act):
    p = d(BANKED[act])
    if not os.path.exists(p):
        return None
    m = re.findall(r'GATES FAILING : (\d+)', io.open(p, encoding='utf-8', errors='replace').read())
    return int(m[-1]) if m else None


def run_copy(act):
    """### COPY THE SUITE INTO `tools/` SO ITS OWN PATH ARITHMETIC STILL WORKS, RUN IT, DELETE THE COPY.
    ### ### **THE BANKED SUITE IS NEVER OPENED FOR WRITING.**"""
    src = os.path.join(T, '%s_checks.py' % act)
    dst = os.path.join(T, 'b363_copy_%s_checks.py' % act)
    if not os.path.exists(src):
        return None, 'NO SUITE AT %s' % os.path.basename(src), None
    shutil.copy2(src, dst)
    try:
        r = subprocess.run([sys.executable, dst], capture_output=True, text=True,
                           encoding='utf-8', errors='replace', timeout=900)
        out = (r.stdout or '') + (r.stderr or '')
        m = re.findall(r'GATES FAILING : (\d+)', out)
        return (int(m[-1]) if m else None), out, r.returncode
    finally:
        if os.path.exists(dst):
            os.remove(dst)


def needles_of(act):
    """### THE (path, anchor) PAIRS A SUITE DECLARES, READ BY IMPORTING THE COPY. ### **NOTHING IS
    ### EDITED**; the module is read for its own lists."""
    src = os.path.join(T, '%s_checks.py' % act)
    dst = os.path.join(T, 'b363_copy_%s_checks.py' % act)
    shutil.copy2(src, dst)
    try:
        import importlib
        name = 'b363_copy_%s_checks' % act
        if name in sys.modules:
            del sys.modules[name]
        mod = importlib.import_module(name)
        out, found = [], []
        # ### **THE NAMES ARE READ FROM THE MODULE, NOT ASSUMED.** ### The first version of this
        # ### exercise looked for two names and reported `0 declared` for three suites that use a
        # ### third -- ### **AN ABSENCE THAT WAS NOT THERE, PRODUCED BY A NAME TYPED RATHER THAN
        # ### READ**, which is this act's own subject turned on this act's own tool.
        for attr in sorted(a for a in dir(mod)
                           if a.isupper() and ('NEEDLE' in a or 'HINT' in a)):
            v = getattr(mod, attr, None)
            if not isinstance(v, (list, tuple)) or not v:
                continue
            # ### **THE SHAPE IS READ TOO, NOT ASSUMED.** ### b355/b356/b357 declare PAIRS
            # ### `(label, hint)` against the module's own `BANK`; b360/b361/b362 declare TRIPLES
            # ### `(label, path, hint)`. ### The first version of this exercise required a triple and
            # ### reported `BUILT 0` for the three older suites -- ### **THE SAME SPECIES A SECOND
            # ### TIME, ONE LAYER DOWN.**
            bank = getattr(mod, 'BANK', None)
            shape = 'triple' if all(len(i) >= 3 for i in v) else 'pair'
            note = ''
            n0 = len(out)
            for item in v:
                if not isinstance(item, (list, tuple)):
                    continue
                if len(item) >= 3:
                    out.append((attr, item[0], item[1], item[2]))
                elif len(item) == 2 and bank:
                    out.append((attr, item[0], bank, item[1]))
                elif len(item) == 2:
                    note = ',NO BANK ATTR'
            found.append('%s(%d,%s%s->%d)' % (attr, len(v), shape, note, len(out) - n0))
        return out, None, found
    except Exception as e:
        return [], '%s: %s' % (type(e).__name__, str(e)[:110]), []
    finally:
        if os.path.exists(dst):
            os.remove(dst)


def main():
    rec('=' * 100)
    rec('b363 -- THE CENSUS, THE CLASSIFICATION, AND THE CONTROL.')
    rec('=' * 100)

    rec('')
    rec("  ### THE HELPER'S OWN FIXTURES, RUN HERE BEFORE IT IS TRUSTED (both polarities):")
    fx = GN.self_test(True)
    rec('  ### gate_needle fixtures : %s' % fx)
    if not fx:
        rec('  ### REFUSING TO CENSUS WITH A HELPER THAT FAILS ITS OWN FIXTURES.')
        run_clock.write(D, 'b363_census_run', LINES)
        return 2

    # ================================================================================================
    rec('')
    rec('-' * 100)
    rec("  ### (1) THE POPULATION, FROM THE BANKS' OWN HEADLINE FIGURES.")
    rec('-' * 100)
    total_head, bad = 0, 0
    for act, bank, hint, fig, spelled in HEADLINES:
        try:
            n, line = AF.find(bank, hint)
            ok = spelled in line
            rec('    %-5s %-34s line %-5d declares %-5s (%d) : %s'
                % (act, os.path.basename(bank), n, spelled, fig, ok))
            rec('        | %s' % line.strip()[:150])
            if not ok:
                bad += 1
            total_head += fig
        except AF.AnchorError as e:
            bad += 1
            rec('    %-5s ### ### **NOT LOCATED** : %s' % (act, str(e).split(chr(10))[0][:110]))
    rec('')
    rec('    ### ### **THE BANKS DECLARE, IN SUM : %d ARMS.**' % total_head)

    # ================================================================================================
    rec('')
    rec('-' * 100)
    rec('  ### (2) THE ENUMERATION, ARM BY ARM, EACH LOCATED AT ITS OWN BANK.')
    rec('-' * 100)
    located, unlocated = [], []
    for aid, act, bank, hint, what, cls, why in ARMS:
        try:
            n, line = AF.find(bank, hint)
            located.append((aid, act, n, cls))
            rec('')
            rec('    %-4s %-5s %s : line %d' % (aid, act, os.path.basename(bank), n))
            rec('         what it was : %s' % what)
            rec('         %-22s %s' % (cls, why))
        except AF.AnchorError as e:
            unlocated.append(aid)
            rec('    %-4s ### ### **NOT LOCATED** : %s' % (aid, str(e).split(chr(10))[0][:110]))
    rec('')
    rec('    ### arms enumerated : %d   ### NOT LOCATED : %d' % (len(located), len(unlocated)))

    # ================================================================================================
    rec('')
    rec('-' * 100)
    rec('  ### (3) THE ARITHMETIC, AND THE REFUSAL IF IT DOES NOT ADD.')
    rec('-' * 100)
    n_enum = len(located)
    agree = (n_enum == total_head) and not unlocated and not bad
    rec('    the banks\' headline figures sum to : %d' % total_head)
    rec('    the arms enumerated one by one     : %d' % n_enum)
    rec('    ### ### **THEY AGREE : %s**' % agree)
    if not agree:
        rec('    ### ### **REFUSING TO EMIT A CENSUS WHOSE PARTS DO NOT ADD TO ITS OWN TOTAL.**')
        run_clock.write(D, 'b363_census_run', LINES)
        return 1
    n_ret = sum(1 for _a, _b, _n, c in located if c == R)
    n_not = n_enum - n_ret
    rec('')
    rec('    ### ### **RETIRED BY THE HELPER : %d ### / ### NOT RETIRED : %d ### OF %d.**'
        % (n_ret, n_not, n_enum))
    wrongarms = [a for a, _b, _c, _d2 in [(x[0], x[1], x[2], x[3]) for x in located]
                 if a in ('A3', 'A10')]
    missing = [a for a, _b, _c, _d2 in [(x[0], x[1], x[2], x[3]) for x in located]
               if a in ('A6', 'A9')]
    rec('    ### of the NOT RETIRED: ### **%d ARE WRONG ARMS (%s)** and ### **%d ARE MISSING SENTENCES '
        '(%s)**' % (len(wrongarms), ', '.join(wrongarms), len(missing), ', '.join(missing)))

    # ================================================================================================
    rec('')
    rec('-' * 100)
    rec("  ### (4) THE DRAFT, SCORED AGAINST THE COUNT.")
    rec('-' * 100)
    for lbl, hint in (("the draft's population figure", 'NINE ARMS THAT FIRED ON THEIR OWN ACTS'),
                      ("the draft's retirement estimate",
                       'census of thirteen incidents should convert to a cure covering nine or ten')):
        n, line = AF.find(DRAFT, hint)
        rec('    %s -- b362_closing.txt : line %d' % (lbl, n))
        rec('        | %s' % line.strip()[:170])
    rec('')
    rec('    ### ### ### **THE DRAFT IS REFUTED, AND REFUTED IN ITS INPUT AS WELL AS ITS OUTPUT.**')
    rec('    ### The draft summed its own two legs at NINE and added b360\'s FOUR to reach THIRTEEN. ###')
    rec('    ### **THE BANKS DECLARE %d: FOUR, TWO AND FIVE.** ### The draft\'s nine was arithmetic over its'
        % total_head)
    rec('    ### own banks and it was wrong -- ### **WHICH IS WHY THE ADDITION ASKED FOR A COUNT AND NOT A')
    rec('    ### CONFIRMATION.**')
    rec('    ### **AND THE RETIREMENT ESTIMATE IS REFUTED TOO: NINE OR TEN CLAIMED, %d COUNTED.**' % n_ret)

    # ================================================================================================
    rec('')
    rec('-' * 100)
    rec('  ### (5) THE CONTROL. ### **THE BANKED SUITES ARE COPIED, RUN AND THE COPIES DELETED.**')
    rec('-' * 100)
    control = []
    for act, _z in SUITES:
        want = banked_verdict(act)
        got, out, rc = run_copy(act)
        same = (want is not None and got is not None and want == got)
        control.append(dict(act=act, banked=want, copy=got, reproduced=bool(same), rc=rc))
        rec('    %-5s banked GATES FAILING %-5s ; the copy reports %-5s ; ### REPRODUCED : %s'
            % (act, want, got, same))
        if not same:
            rec('        ### ### **DOES NOT REPRODUCE. ### REPORTED, NOT ADJUSTED.**')
            if isinstance(out, str):
                for ln in [x for x in out.split(chr(10)) if 'GATES FAILING' in x or '### FAIL' in x][:6]:
                    rec('        | %s' % ln.strip()[:150])
    nrep = sum(1 for c in control if c['reproduced'])
    rec('')
    rec('    ### ### **COPIES REPRODUCING THEIR OWN ACT\'S VERDICT : %d of %d.**' % (nrep, len(control)))
    rec('    ### **A COPY THAT DOES NOT REPRODUCE IS A MEASUREMENT OF A SUITE READING A MOVED REPOSITORY,')
    rec('    ### AND NOT A FAILURE OF THE HELPER**, which no copy uses. ### Each is named above with the')
    rec('    ### arms it reports.')

    # ================================================================================================
    rec('')
    rec('-' * 100)
    rec("  ### (6) THE HELPER, EXERCISED OVER EVERY NEEDLE THOSE SUITES DECLARE.")
    rec('-' * 100)
    ex = []
    for act, _z in SUITES:
        pairs, err, found = needles_of(act)
        if err:
            rec('    %-5s ### ### **NOT READ : %s**' % (act, err))
            ex.append(dict(act=act, read=False, error=err))
            continue
        built = refused = 0
        misses = []
        for attr, lbl, path, anchor in pairs:
            try:
                GN.build(path, anchor)
                built += 1
            except GN.NeedleError as e:
                refused += 1
                misses.append((attr, lbl, str(e)[:90]))
        rec('    %-5s declares %-26s ### %-4d needles ### BUILT %-4d ### REFUSED %d'
            % (act, ', '.join(found) or 'NO NEEDLE LIST FOUND', len(pairs), built, refused))
        for attr, lbl, why in misses[:6]:
            rec('        ### REFUSED  %-14s %-46s %s' % (attr, lbl[:46], why))
        ex.append(dict(act=act, read=True, lists=found, declared=len(pairs), built=built,
                       refused=refused, misses=[list(m) for m in misses]))
    tot_d = sum(e.get('declared', 0) for e in ex)
    tot_b = sum(e.get('built', 0) for e in ex)
    tot_r = sum(e.get('refused', 0) for e in ex)
    rec('')
    rec('    ### ### **OVER THE SUITES READ: %d NEEDLES DECLARED, %d BUILT, %d REFUSED.**' % (tot_d, tot_b, tot_r))
    rec('    ### **AND WHAT A REFUSAL MEANS HERE IS NOT WHAT IT MEANS IN A LIVE SUITE:** ### these anchors')
    rec('    ### were verified by their own acts against files that have since moved. ### **A REFUSAL IS A')
    rec('    ### MEASUREMENT OF DRIFT IN THE RECORD, NOT A DEFECT IN THE ARM THAT PASSED.**')
    rec('    ### **THIS IS A MEASUREMENT OF THE RECORD\'S OWN SUITES AND NOT A GRADE ON THEM, AND NO SUITE')
    rec('    ### WAS EDITED BY IT.**')

    rec('')
    rec('=' * 100)
    rec('  ### ### **VERDICT: BUILT AND FOUND NARROWER THAN ITS RULE.** ### The helper exists, its fixtures')
    rec('  ### hold in both polarities including an arm that should fire and still does, and the census puts')
    rec('  ### its reach at ### **%d OF %d** ### -- below the draft\'s claim, and below it for two distinct'
        % (n_ret, n_enum))
    rec('  ### reasons the draft named only one of.')
    rec('=' * 100)
    p = run_clock.write(D, 'b363_census_run', LINES)
    io.open(d('b363_census.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(headline_sum=total_head, enumerated=n_enum, agree=bool(agree), retired=n_ret,
             not_retired=n_not, wrong_arms=wrongarms, missing_sentences=missing,
             draft_population=9 + 4, draft_retirement='nine or ten',
             arms=[dict(id=a[0], act=a[1], anchor_line=[x[2] for x in located if x[0] == a[0]][0],
                        classification=a[5], what=a[4], why=a[6]) for a in ARMS],
             control=control, copies_reproducing=nrep, copies=len(control),
             needles_declared=tot_d, needles_built=tot_b, needles_refused=tot_r, exercise=ex,
             verdict='BUILT AND FOUND NARROWER THAN ITS RULE',
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
