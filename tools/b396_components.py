# -*- coding: utf-8 -*-
"""b396_components.py -- THE LIST, THE SIX RE-RUNS, THE PRICE, AND THE ANCHOR MODE PROVED.

### ### **THE WIDENING FOR EVERY RE-RUN IS WRITTEN INTO THIS FILE BEFORE IT IS RUN**, one per
### figure, so that ### **A RE-RUN CANNOT BE TUNED TO ITS RESULT** (`b380`'s forbidden direction).
###
### ### **AND A CONFIRMATION IS THE WEAKER RESULT.** ### It proves the figure is not an artefact
### of THE SHAPE THAT WAS WIDENED. ### **A NARROWNESS THIS SWEEP IS DEAF TO WOULD SURVIVE EVERY
### ### CONFIRMATION IN THIS ACT**, and the five deafnesses are restated with the verdicts.
"""
import ast
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
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
FERRY = os.path.join(D, 'b396_ferry_2026-09-10.txt')
OUT = os.path.join(D, 'b396_components.txt')
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core', 'modules', '2026-09')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []
E = json.load(io.open(os.path.join(D, 'b396_reads.json'), encoding='utf-8'))


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def flat(s, n=200):
    return ' '.join(s.split())[:n]


def text_of(p):
    return io.open(p, encoding='utf-8', errors='replace').read()


# ==================================================================================================
#  COMPONENT 1 -- THE LIST.
# ==================================================================================================
def component1():
    bar('=')
    rec('  COMPONENT 1 -- THE SWEEP. ### **THE PRODUCT IS A LIST OF FINDINGS AT RISK.**')
    bar('=')
    s1, s0 = E['s1'], E['s0']
    rec('  ### **THE FUNNEL, EVERY STAGE PRINTED:**')
    rec('  ###   `tools/b*.py` parsed                          ### **`%d`** (unparseable `%d`)'
        % (s1['parsed'], len(s1['broke'])))
    rec('  ###   carrying a backtick ANYWHERE (a raw `grep`)   ### **`%d`** of `%d`'
        % (s0['raw_backtick'], s0['tools']))
    rec('  ###   carrying at least one NARROW TEST             ### **`%d`**' % s1['narrow'])
    rec('  ###   ### **CARRYING AT LEAST ONE AT-RISK FIGURE**  ### **`%d`**' % s1['atrisk_files'])
    rec('  ###   ### **AT-RISK FIGURES**                       ### **`%d`**' % s1['figures'])
    rec('  ### ### **`%d` OF `%d` IS WHY A RAW `grep` IS NOT THE INSTRUMENT.** ### Almost every'
        % (s0['raw_backtick'], s0['tools']))
    rec('  ### ### one of those backticks is PROSE. ### **A BACKTICK IN A SENTENCE IS NOT A')
    rec('  ### ### BACKTICK IN A MATCHER.**')
    rec()
    rec('  ### **THE THREE FILTERS TRIED AND DISCARDED BEFORE THE LOCK, WITH THEIR YIELDS:**')
    rec('  ###   (i)   `the module prints an absence somewhere`     kept ### **`374` of `407`**')
    rec('  ###   (ii)  `the act`s name appears in a ledger`         kept ### **`350` of `380`**')
    rec('  ###   (iii) `the instrument reads corpus text`           kept ### **`79` of `82`**')
    rec('  ### ### **A FILTER THAT KEEPS NINE TENTHS OF ITS INPUT IS NOT A FILTER**, and a')
    rec('  ### ### tightening made in silence is one nobody can audit (`b381`).')
    rec('  ### ### **(iii) IS A TRUE DISTINCTION THIS TOOL CANNOT DRAW:** ### a narrow matcher')
    rec('  ### ### against text the act WROTE fails its own gate loudly; one against the CORPUS')
    rec('  ### ### shrinks a finding in silence. ### **THAT IS WHERE THE RISK LIVES AND THE ACT')
    rec('  ### ### CANNOT SEPARATE IT** -- filed as a limit, not applied as a filter.')
    rec('  ### ### ### **AND THREE VACUOUS FILTERS IN ONE ACT IS THE RESULT:** ### the shape is')
    rec('  ### ### ### **PERVASIVE**, so ### *how many findings rest on a backtick* ### **HAS NO')
    rec('  ### ### ### ANSWER AT INSTRUMENT GRANULARITY.** ### It has one at FIGURE granularity,')
    rec('  ### ### ### and this is it.')
    rec()
    rec('  ### **THE AT-RISK FIGURES, BY ACT. ### EACH NAMES ITS INSTRUMENT, ITS LINE, THE NAME')
    rec('  ### THE YIELD IS BOUND TO, AND THE REPORT THAT MAKES IT NEGATIVE.**')
    byact = {}
    for r in s1['rows']:
        byact.setdefault(r['act'], []).append(r)
    for a in sorted(byact):
        rec()
        rec('    ### **%s** -- `%d` at-risk figure(s)' % (a, len(byact[a])))
        for r in byact[a]:
            rec('      %s:%d  [%s]' % (r['file'], r['report_line'], ','.join(r['why'])))
            rec('        matcher : %s' % r['literal'])
            rec('        bound to: `%s`   in `%s`' % (r['name'], r['func']))
            rec('        reports : %s' % r['report'])
    rec()
    rec('  ### ### **AND NARROW IS NOT A DEFECT.** ### `%d` instruments carry a narrow test with'
        % (s1['narrow'] - s1['atrisk_files']))
    rec('  ### ### no negative finding standing on it, and ### **THEY ARE NOT COUNTED AS AT')
    rec('  ### ### RISK.**')
    return dict(parsed=s1['parsed'], narrow=s1['narrow'], files=s1['atrisk_files'],
                figures=s1['figures'], acts=len(byact), discards=3,
                not_at_risk=s1['narrow'] - s1['atrisk_files'])


# ==================================================================================================
#  COMPONENT 2 -- THE SIX RE-RUNS. ### **EVERY WIDENING IS WRITTEN HERE BEFORE IT RUNS.**
# ==================================================================================================
CORR = os.path.join(SIDE, 'CORRESPONDENCE.md')
INDEX = os.path.join(T, 'banked_index.py')

# ### ==================================================================================================
# ### ### **THE FIGURE IS THE UNIT, NOT THE MATCH COUNT.** ### An earlier form of this component
# ### compared how many times each literal matched and called two of the six MOVED. ### Both were
# ### artefacts of the harness: ### **IT READ THE WRONG INPUT** ### -- the act's `data/` records
# ### instead of the text the matcher actually read -- and ### **IT COMPARED COUNTS WHERE THE
# ### ### FIGURE IS A BOOLEAN.** ### `b318` asks *does the registration say so*; `b323` asks *does
# ### the query return NO KEY*. ### A literal matching once or three times leaves both answers
# ### `True`, and ### **A FIGURE THAT DOES NOT MOVE HAS NOT MOVED, WHATEVER THE COUNT DID.**
# ###
# ### ### **SO EACH RE-RUN DECLARES ITS KIND** -- `COUNT` or `PRESENCE` -- ### **AND THE VERDICT IS
# ### ### READ OFF THE FIGURE.** ### Where the count moves and the figure does not, that is reported
# ### as ### **NARROWNESS WITHOUT CONSEQUENCE**, which is a real observation and not a moved figure.
# ###
# ### ### **AND WHERE THE INSTRUMENT ALREADY CARRIES A SECOND FORM, THE RE-RUN USES BOTH** -- `b318`
# ### matches an uppercase form OR a lowercase one, and testing only the first would convict an arm
# ### that was already widened by the hand that wrote it.
# ### ==================================================================================================

# (act, instrument, figure, kind, input, NARROW forms, WIDE form, the widening said)
RERUNS = [
    ('b307', 'b307_correspondence.py', 'correspondence rows the row-parser can see', 'COUNT',
     ('file', CORR), [r'^\| (\d+) \|'], r'^\s*\|\s*(\d+)\s*\|',
     'allow leading whitespace and any spacing around the pipes -- a row indented or padded '
     'differently is still a row'),
    ('b318', 'b318_checks.py', 'the registration says W_infinity is not computed', 'PRESENCE',
     ('file', os.path.join(D, 'b318_registration_2026-09-04.txt')),
     ['W_infinity` IS NOT COMPUTED', 'W_infinity` is not computed'],
     r'(?is)w[_ ]?infinity.{0,4}\s+is\s+not(?:\s|#)+computed',
     'drop the backtick, allow an underscore or a space in the name, ignore case, and ### **LET '
     'THE PHRASE CROSS A LINE BREAK AND ITS MARKERS** -- the face states this fact more than '
     'once and at least one statement wraps'),
    ('b323', 'b323_checks.py', 'an index query for a phrase nobody keyed returns NO KEY',
     'PRESENCE', ('query', 'a phrase no act has ever keyed b396'),
     ['### NO KEY'], r'(?i)\bno\s+key\b',
     'drop the marker prefix and ignore case -- a NO KEY reported without `###` is still a NO KEY'),
    ('b326', 'b326_checks.py', 'the correspondence row numbered 164', 'COUNT',
     ('file', CORR), [r'\| 164 \|'], r'^\s*\|\s*164\s*\|',
     'allow any spacing around the row number and anchor it to the line start, so a 164 '
     'appearing mid-row is not counted'),
    ('b332', 'b332_correspondence.py', 'correspondence rows the row-parser can see', 'COUNT',
     ('file', CORR), [r'^\| (\d+) \|'], r'^\s*\|\s*(\d+)\s*\|',
     'the same widening as b307, on the same ledger, by the same literal'),
    ('b392', 'b392_checks.py', 'the deposit rule heading stands in the registry', 'PRESENCE',
     ('file', os.path.join(PP, 'REGISTRY.md')),
     ['THE DEPOSIT RULE \u2014 RULING `(R20)`'],
     r'(?i)the\s+deposit\s+rule\s*[\u2014\u2013-]+\s*ruling\s*.?\(?R20\)?',
     'drop the backticks, accept any dash, allow flexible spacing and ignore case'),
]
CHEAPEST = ['b307', 'b318', 'b323']
EXPOSED = ['b392', 'b326', 'b332']


def _is_regex(s):
    return s.startswith('^') or '\\' in s or '(?i' in s


def _count(pattern, text):
    if _is_regex(pattern):
        return len(re.findall(pattern, text, re.M))
    return text.count(pattern)


def _input_text(kind_src):
    how, what = kind_src
    if how == 'file':
        return text_of(what), os.path.basename(what)
    # ### **THE LIVE INPUT, REPRODUCED**: the matcher read a subprocess's stdout, so the re-run
    # ### runs that subprocess. ### **READING THE ACT'S RECORDS INSTEAD WOULD BE THE WRONG INPUT.**
    r = subprocess.run([sys.executable, INDEX, '--query', what], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return (r.stdout or ''), 'banked_index.py --query (live stdout)'


def component2():
    bar('=')
    rec('  COMPONENT 2 -- SIX RE-RUNS. ### **BOTH YIELDS FOR EACH, AND THE WIDENING STATED**')
    bar('=')
    rec('  ### **THE ORDER GAVE TWO CRITERIA AND THEY PICK DIFFERENT SETS:**')
    rec('  ###   the CHEAPEST three     : ### **%s**' % ', '.join('`%s`' % x for x in CHEAPEST))
    rec('  ###   the MOST EXPOSED three : ### **%s**' % ', '.join('`%s`' % x for x in EXPOSED))
    shared = set(CHEAPEST) & set(EXPOSED)
    rec('  ### ### **THEY SHARE `%d` MEMBERS. ### THE SETS ARE DISJOINT.**' % len(shared))
    rec('  ### **WHICH SET WAS RUN, AND WHY:** ### ### **BOTH. ### ALL SIX.** ### The order says to')
    rec('  ### run the draft`s three and to say so if the sets differ; the navigator says he would')
    rec('  ### rather know the exposed ones are wrong than that the cheap ones are right. ### Every')
    rec('  ### one of the six is a local read, so ### **RUNNING BOTH SETS COSTS LESS THAN THE')
    rec('  ### ### PARAGRAPH THAT WOULD JUSTIFY CHOOSING BETWEEN THEM.** ### A choice not worth')
    rec('  ### making is not made.')
    rec()
    rec('  ### ### **THE UNIT IS THE FIGURE AND NOT THE MATCH COUNT.** ### An earlier form of this')
    rec('  ### ### component compared counts and called two of the six MOVED. ### **BOTH WERE')
    rec('  ### ### ARTEFACTS OF THE HARNESS:** ### it read the act`s `data/` records instead of the')
    rec('  ### ### text the matcher actually read, and it compared counts where the figure is a')
    rec('  ### ### BOOLEAN. ### **A FIGURE THAT DOES NOT MOVE HAS NOT MOVED, WHATEVER THE COUNT')
    rec('  ### ### DID** -- so each re-run declares `COUNT` or `PRESENCE` and the verdict is read')
    rec('  ### ### off the figure.')
    rec('  ### ### **AND EVERY WIDENING IS WRITTEN IN THE TOOL BEFORE IT RUNS**, so ### **A RE-RUN')
    rec('  ### ### CANNOT BE TUNED TO ITS RESULT** (`b380`).')
    out = []
    for act, inst, what, kind, src, narrows, wide, said in RERUNS:
        body, inname = _input_text(src)
        n_hits = sum(_count(x, body) for x in narrows)
        w_hits = _count(wide, body)
        if kind == 'COUNT':
            n_fig, w_fig = n_hits, w_hits
            same = (n_fig == w_fig)
        else:
            n_fig, w_fig = (n_hits > 0), (w_hits > 0)
            same = (n_fig == w_fig)
        if not same:
            verdict = 'MOVED'
            note = ('the figure itself differs under the widened predicate : `%s` -> `%s`'
                    % (n_fig, w_fig))
        else:
            verdict = 'CONFIRMED'
            note = ('the figure is unchanged under the widened predicate, so it is not an '
                    'artefact of THIS shape')
        consequence = (n_hits != w_hits and same)
        rec()
        rec('  ' + '-' * 96)
        rec('    ### **%s** -- `%s`   [%s]   figure kind: **%s**'
            % (act, inst, 'CHEAPEST' if act in CHEAPEST else 'MOST EXPOSED', kind))
        rec('    the figure      : %s' % what)
        rec('    the input       : `%s`  ### **THE TEXT THE MATCHER ACTUALLY READ**' % inname)
        for x in narrows:
            rec('    the NARROW form : %s' % x)
        rec('    the WIDE form   : %s' % wide)
        rec('    ### **THE WIDENING, STATED:** ### %s' % said)
        rec('    matches         : narrow `%d`   wide `%d`' % (n_hits, w_hits))
        rec('    ### **THE FIGURE : narrow `%s` ### wide `%s` ### --> %s**'
            % (n_fig, w_fig, verdict))
        rec('    %s' % note)
        if consequence:
            rec('    ### ### **NARROWNESS WITHOUT CONSEQUENCE:** ### the widened form matches `%d`'
                % w_hits)
            rec('    ### ### where the narrow one matches `%d`, and the figure is the same either'
                % n_hits)
            rec('    ### ### way. ### **THE INSTRUMENT IS NARROW AND THE FINDING IS NOT AT RISK'
                )
            rec('    ### ### FROM IT** -- which is a real observation and not a moved figure.')
        out.append(dict(act=act, inst=inst, what=what, kind=kind, input=inname,
                        narrow=narrows, wide=wide, said=said,
                        narrow_hits=n_hits, wide_hits=w_hits,
                        narrow_figure=n_fig, wide_figure=w_fig, verdict=verdict,
                        narrowness_without_consequence=consequence,
                        set=('CHEAPEST' if act in CHEAPEST else 'MOST EXPOSED')))
    rec()
    rec('  ' + '-' * 96)
    vs = {}
    for o in out:
        vs[o['verdict']] = vs.get(o['verdict'], 0) + 1
    nwc = [o for o in out if o['narrowness_without_consequence']]
    moved = [o for o in out if o['verdict'] == 'MOVED']
    rec('  ### ### **THE SIX VERDICTS : %s**' % vs)
    rec('  ### ### **FIGURES MOVED BY A WIDENED PREDICATE : `%d`.**' % len(moved))
    for o in moved:
        rec('  ###   `%s` %s : `%s` -> `%s`' % (o['act'], o['what'], o['narrow_figure'],
                                                o['wide_figure']))
    rec('  ### ### **NARROW WITHOUT CONSEQUENCE : `%d`** ### -- the count moved, the figure did not:'
        % len(nwc))
    for o in nwc:
        rec('  ###   `%s` : narrow `%d` matches, wide `%d`, figure `%s` both ways'
            % (o['act'], o['narrow_hits'], o['wide_hits'], o['narrow_figure']))
    rec()
    rec('  ### ### **`(L2)` ASKED WHETHER AT LEAST ONE RE-RUN MOVES A BANKED FIGURE.** ### On these')
    rec('  ### ### six the answer is ### **%s**, and this seat registered `(E2)` before the lock:'
        % ('MET' if moved else 'REFUTED'))
    rec('  ### ### ### **THE RE-RUNS WILL MOSTLY CONFIRM, AND CONFIRMING IS THE WEAKER RESULT.**')
    rec('  ### ### A refuted `(L2)` is a real answer and not a disappointment -- ### **THE ARC`S')
    rec('  ### ### ONE KNOWN MOVE WAS FOUND BY READING A DOCUMENT, NOT BY WIDENING A REGEX.**')
    rec()
    rec('  ### ### **AND A CONFIRMATION IS THE WEAKER RESULT.** ### It proves a figure is not an')
    rec('  ### ### artefact of ### **THE SHAPE THAT WAS WIDENED**, and nothing more. ### These five')
    rec('  ### ### deafnesses stand behind every `CONFIRMED` above:')
    rec('  ###     -- a narrowness assembled from a VARIABLE at run time')
    rec('  ###     -- a narrowness living in the DATA an instrument reads')
    rec('  ###     -- a matcher passed in from ANOTHER module')
    rec('  ###     -- a shape restriction with no string and no case method')
    rec('  ###     -- ### **WHETHER A NARROW MATCHER IS WRONG** -- the shape is measured, never')
    rec('  ###        the verdict')
    rec('  ### ### **`(L3)` IS ALREADY MET, AND BY `b395` RATHER THAN BY THIS ACT:** ### `b394`')
    rec('  ### ### reported ### *no kernel repository it names is on the drive* ### for `8`')
    rec('  ### ### keystones and the drive holds one for every one of them. ### **THAT IS A FINDING')
    rec('  ### ### THIS ARC REPORTED AS AN ABSENCE THAT DID NOT SURVIVE A WIDENED PREDICATE**, and')
    rec('  ### ### this act names it rather than re-discovering it.')
    return dict(runs=len(out), verdicts=vs, moved=len(moved), rows=out,
                cheapest=CHEAPEST, exposed=EXPOSED, shared=len(shared),
                nwc=len(nwc), l2=(len(moved) > 0), l3_by_b395=True)


# ==================================================================================================
#  COMPONENT 3 -- THE WORK NOW AVAILABLE, PRICED AND NOT DONE.
# ==================================================================================================
def component3():
    bar('=')
    rec('  COMPONENT 3 -- THE TEN NOW REACHABLE. ### **PRICED. ### NOT READ.**')
    bar('=')
    s5 = E['s5']
    per = float(s5['per_keystone'])
    ten = s5['readable']
    total = round(per * ten, 1)
    rec('  ### **THE RATE, READ FROM THE ACT THAT MEASURED IT** -- `b394`\'s own component JSON:')
    rec('  ###   `%s` minutes for three keystones, ### **`%s` PER KEYSTONE**' % (s5['minutes'],
                                                                                per))
    rec('  ###   against `b390`\'s `%s` for one, read one at a time' % s5['b390'])
    rec('  ### **THE POPULATION, READ FROM `b395`:** ### **`%d` READABLE WITHOUT A CLONE.**' % ten)
    rec()
    rec('  ### ### **THE PRICE : `%s` x `%d` = ### **`%s` MINUTES.**' % (per, ten, total))
    rec('  ### **WHAT IT BUYS:** ### `%d` of the census\'s `%s` are reconciled today; reading the'
        % (s5['reconciled'], s5['of']))
    rec('  ### ten would take that to ### **`%d` OF `%s`**, leaving ### **`%d`** ### -- `ENUMERA`,'
        % (s5['reconciled'] + ten, s5['of'], s5['of'] - s5['reconciled'] - ten))
    rec('  ### which names no terminal and needs an author rather than a reader.')
    rec()
    rec('  ### ### **THE FIGURE IS A FLOOR BECAUSE ITS INPUT IS A FLOOR.** ### `b394` declared')
    rec('  ### ### both of its figures floors, read at the component while the act continued, and')
    rec('  ### ### ### **A PRICE BUILT ON A FLOOR IS A FLOOR.** ### This act does not promote it')
    rec('  ### ### into an estimate.')
    rec('  ### ### **AND THE SAMPLE THE RATE CAME FROM IS NAMED AGAIN:** ### `b394` read ###')
    rec('  ### ### *the reachable ones*, ### the population most likely to be in good order, so')
    rec('  ### ### ### **A RATE TAKEN FROM THE EASY END PRICES THE HARD END TOO CHEAPLY.**')
    rec('  ### ### **THE TEN ARE NOT READ BY THIS ACT.** ### They are priced, and the item stays')
    rec('  ### ### on the desk as ### **AVAILABLE AND NOT DONE.**')
    return dict(per_keystone=per, ten=ten, minutes=total, reconciled=s5['reconciled'],
                of=s5['of'], after=s5['reconciled'] + ten,
                remaining=s5['of'] - s5['reconciled'] - ten)


# ==================================================================================================
#  ADDITION THREE -- THE ANCHOR MODE, PROVED; AND THE MODULE.
# ==================================================================================================
MODULE = 'EDITING_ANCHOR_EXCLUDES_PRESERVED.md'


def addition3():
    bar('=')
    rec('  ADDITION THREE -- THE PRESERVATION HAZARD, FILED AND MECHANIZED IN PART.')
    bar('=')
    s4 = E['s4']
    rec('  ### **THE INCIDENT:** ### `b395`\'s needle for the live cluster row matched `b388`\'s')
    rec('  ### preserved quotation of the superseded table and ### **RESOLVED TO IT SILENTLY**,')
    rec('  ### having met it first. ### **AN ACT EDITING BY THAT ANCHOR WOULD HAVE EDITED A')
    rec('  ### ### QUOTATION THE CORPUS PRESERVED SO THAT IT WOULD NOT CHANGE.**')
    rec()
    rec('  ### **THE RULE, FILED:** ### an anchor used to EDIT ### **EXCLUDES PRESERVED BLOCKS BY')
    rec('  ### ### CONSTRUCTION**, and an anchor resolving inside one is ### **REFUSED RATHER')
    rec('  ### ### THAN DISAMBIGUATED** -- because a caller told `AMBIGUOUS` picks one, and')
    rec('  ### picking is how the quotation gets edited.')
    rec()
    rec('  ### **IS IT MECHANIZABLE? ### THE SURVEY SAYS YES, IN PART:** ### the paper tree')
    rec('  ### carries ### **`%d`** ### contiguous blockquoted blocks across ### **`%d`**'
        % (s4['blocks'], s4['files']))
    rec('  ### documents, `%d` lines of `%d`, plus `%d` explicit preservation banners.'
        % (s4['lines'], s4['total'], s4['banners']))
    rec('  ### ### **A `>`-PREFIXED LINE IS A STRUCTURAL FACT A TOOL READS WITHOUT JUDGEMENT.**')
    rec()
    # ### THE MECHANIZED HALF, PROVED BY THE OWNER INSTRUMENT'S OWN FIXTURES.
    r = subprocess.run([sys.executable, os.path.join(T, 'anchor_from_file.py'), '--self-test'],
                       capture_output=True, text=True, encoding='utf-8', errors='replace')
    lines = [x for x in (r.stdout or '').split(chr(10)) if 'PASS' in x or 'FAIL' in x]
    rec('  ### **THE MECHANIZED HALF, IN `tools/anchor_from_file.py`:** ### an ### **OPT-IN,')
    rec('  ### ### DEFAULT-OFF** ### `editing=True` that excludes blockquoted lines and refuses an')
    rec('  ### anchor resolving only inside one.')
    rec('  ### **ITS OWN FIXTURES, RUN:** ### exit `%d`, `%d` arms, `%d` failing'
        % (r.returncode, len(lines), sum(1 for x in lines if 'FAIL' in x)))
    for x in lines:
        rec('      %s' % flat(x, 108))
    # ### **NO CALLER MOVED.**
    callers, moved = [], []
    for f in sorted(os.listdir(T)):
        if not f.endswith('.py') or f == 'anchor_from_file.py':
            continue
        src = text_of(os.path.join(T, f))
        if 'anchor_from_file' not in src and 'AF.find' not in src:
            continue
        callers.append(f)
        if re.search(r'\.find\([^)]*editing\s*=', src) or re.search(r'anchor\([^)]*editing', src):
            moved.append(f)
    rec()
    rec('  ### ### **CALLERS OF THE ANCHOR TOOL : `%d`. ### CALLERS PASSING `editing` : `%d`.**'
        % (len(callers), len(moved)))
    rec('  ### ### **EVERY EXISTING CALLER`S BEHAVIOUR IS UNCHANGED**, because the parameter')
    rec('  ### ### defaults to `False` and no caller sets it. ### **AN OWNER INSTRUMENT WAS')
    rec('  ### ### WIDENED WITHOUT MOVING ONE READER.**')
    rec('  ### **AND THE DEFAULT IS OFF ON PURPOSE:** ### an anchor used to QUOTE a preserved')
    rec('  ### block is CORRECT -- that is how an act cites what an earlier act preserved. ###')
    rec('  ### **THE HAZARD IS EDITING BY AN ANCHOR, NOT READING BY ONE.**')
    rec()
    rec('  ### **THE JUDGEMENT HALF, LISTED APART AND NOT CLAIMED AS MECHANIZED:** ### whether a')
    rec('  ### passage with no `>` is preserved. ### `>` is ### **SUFFICIENT AND NOT NECESSARY**,')
    rec('  ### so the arm is ### **A FLOOR ON THE HAZARD AND NOT A GUARD AGAINST IT** -- which is')
    rec('  ### this act`s own subject turned on its own remedy, and the act says so rather than')
    rec('  ### letting the mechanized half stand for the whole rule.')
    # ### THE MODULE.
    before = sorted(x for x in os.listdir(TC) if x.endswith('.md'))
    body = MODULE_TEXT % (s4['blocks'], s4['files'], s4['banners'])
    p = os.path.join(TC, MODULE)
    io.open(p, 'w', encoding='utf-8', newline=chr(10)).write(body)
    after = sorted(x for x in os.listdir(TC) if x.endswith('.md'))
    rec()
    rec('  ### **THE MODULE:** ### `%s`' % MODULE)
    rec('  ###   `TECHNE-Core/modules/2026-09/` : `%d` -> `%d` ; `%d` bytes'
        % (len(before), len(after), len(body.encode('utf-8'))))
    rec('  ### ### **LOCAL ONLY, UNTRACKED AND NOT PUSHED** -- `TECHNE-Core` is private until the')
    rec('  ### ### provisionals, and that is a state and not an omission.')
    halves = ('Mechanizable:' in body and 'Not mechanizable:' in body)
    rec('  ### ### **THE MODULE STATES ITS TWO HALVES APART : %s.**' % halves)
    return dict(blocks=s4['blocks'], files=s4['files'], banners=s4['banners'],
                fixture_rc=r.returncode, arms=len(lines),
                failing=sum(1 for x in lines if 'FAIL' in x),
                callers=len(callers), moved=len(moved),
                modules_before=len(before), modules_after=len(after),
                module=MODULE, halves=halves, bytes=len(body.encode('utf-8')))


MODULE_TEXT = '''# EDITING_ANCHOR_EXCLUDES_PRESERVED.md — an anchor that edits must not resolve into a quotation

**Minted b396 (2026-09-10), from b395's near miss.**
**Status: RULE with a MECHANIZED half and a JUDGEMENT half. The halves are listed apart.**

## The rule

**An anchor used to EDIT excludes preserved blocks by construction, and an anchor that resolves
inside one is REFUSED rather than disambiguated.**

Refusing is the whole point. A caller told `AMBIGUOUS` picks one of the matches, and **picking is
how the quotation gets edited.**

## The incident

b395 executed a re-anchoring in `SPIRAL_MAP.md`. The cluster table's `Simplicity / RH cascade` row
appears **twice**: once live, and once inside b388's preserved quotation of the superseded table,
whose row opens on the same cells. b395's first needle —

    | **Simplicity / RH cascade**

— matched the **quotation**, at line 258, and **resolved to it silently**, having met it first. The
act caught it only because it printed the resolved line number beside the live one it expected.

**An act editing by that anchor would have edited a quotation the corpus preserved precisely so that
it would not change.** That is falsification, not repair, and (R4) exists to forbid it: *preserve by
quotation, repair by edit.*

## Why this is not the ordinary ambiguity

`anchor_from_file` already refuses a hint matching two lines. That guard did not fire here in the
dangerous direction: had the live row's opening cells differed slightly from the quotation's — a
version bumped, a word added — the needle would have matched **only the quotation**, resolved
cleanly, and reported success. **A one-match resolution into a preserved block is the failure that
looks like a pass.**

## The mechanized half

**Mechanizable:** whether a line is blockquoted. A `>`-prefixed line is a structural fact a tool
reads without judgement, and the paper tree carries **%d contiguous blockquoted blocks across %d
documents**, plus **%d explicit preservation banners**.

`tools/anchor_from_file.py` gains `find(path, hint, editing=True)`: it drops blockquoted matches, and
if **every** match was blockquoted it raises rather than returning one.

**It is opt-in and the default is unchanged.** An anchor used to QUOTE a preserved block is correct —
that is how an act cites what an earlier act preserved — and every existing caller reads rather than
edits. **The hazard is editing by an anchor, not reading by one.** Turning the exclusion on by
default would break correct readers to guard against a mistake they are not making.

## The judgement half — and it is not the mechanized one

**Not mechanizable:** whether a passage carrying no `>` is preserved. A banner, an HTML comment, an
appended annotation or a bare convention names the rest, and no tool decides which. **`>` is
sufficient and not necessary**, so `editing=True` is **a floor on the hazard and not a guard against
it.**

This limit is the same species the act that minted this rule was measuring: **a predicate that knows
one shape finds one shape.** The remedy inherits the disease, and saying so is the only honest way to
ship it.

## What follows

- **Pass `editing=True` from any instrument that will WRITE at the line it resolves.** Reading
  callers leave it alone.
- **When a table is refreshed and its prior form preserved above it, expect the needle to meet the
  quotation first.** Anchor on the live row's own bytes, not on its opening cells.
- **A resolution that succeeds is not a resolution that is right.** Print the line number you
  resolved beside the one you expected, which is the only reason b395 caught this at all.
- See [[predicate-one-shape]] and [[repairing-a-report-erases-it]]: all three are about instruments
  that cannot tell a record of a thing from the thing.

## The scope of this module

It states a rule, names one incident, and ships one opt-in guard. **It does not claim any act in the
record has edited a preserved block** — b395's was a near miss, caught before any write — and it
prices no audit of past edits.
'''


def main():
    rec('### run at (UTC) : %s   ### NOT COVERED BY ANY HASH.' % run_clock.stamp())
    bar('=')
    rec('b396 -- THE COMPONENTS. ### HOW MANY FINDINGS REST ON A BACKTICK.')
    bar('=')
    ai, aln = AF.find(FERRY, 'ACT b396 — HOW MANY FINDINGS REST ON A BACKTICK. The')
    rec('  ### **THE ORDER, line %d:** %s' % (ai, flat(aln, 120)))
    rec()
    c1 = component1()
    rec()
    c2 = component2()
    rec()
    c3 = component3()
    rec()
    a3 = addition3()
    rec()
    bar('=')
    rec('  1 : parsed %d ; narrow %d ; at-risk instruments %d ; FIGURES %d ; acts %d ; discards %d'
        % (c1['parsed'], c1['narrow'], c1['files'], c1['figures'], c1['acts'], c1['discards']))
    rec('  2 : runs %d ; verdicts %s ; moved %d ; sets share %d ; (L2) %s'
        % (c2['runs'], c2['verdicts'], c2['moved'], c2['shared'], c2['l2']))
    rec('  3 : %s x %d = %s min ; %d of %d -> %d of %d ; remaining %d'
        % (c3['per_keystone'], c3['ten'], c3['minutes'], c3['reconciled'], c3['of'],
           c3['after'], c3['of'], c3['remaining']))
    rec('  A3: blocks %d ; fixtures rc %d (%d arms, %d failing) ; callers %d moved %d ; modules %d->%d'
        % (a3['blocks'], a3['fixture_rc'], a3['arms'], a3['failing'], a3['callers'],
           a3['moved'], a3['modules_before'], a3['modules_after']))
    bar('=')
    io.open(OUT, 'w', encoding='utf-8', newline=chr(10)).write(chr(10).join(L) + chr(10))
    p = run_clock.write(D, 'b396_components_run', L)
    json.dump(dict(c1=c1, c2=c2, c3=c3, a3=a3,
                   run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
              io.open(os.path.join(D, 'b396_components.json'), 'w', encoding='utf-8'), indent=1)
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
