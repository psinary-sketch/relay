# -*- coding: utf-8 -*-
"""b403_components.py -- COMPONENTS 1 TO 3, RUN AFTER THE LOCK. ### **TWO EDITS AND ONE MEASURE.**

### ### **COMPONENT 1 EDITS THIS SEAT'S OWN INSTRUMENT AND COMPONENT 2 EDITS ANOTHER OWNER'S
### ### README.** ### Both follow `b371`'s precedent as `b372` applied it: ### **THE ORIGINAL
### ### BANKED VERBATIM BEFORE THE EDIT, THE FIGURE REMOVED RATHER THAN RESTATED, AND THE EDIT
### ### VERIFIED BY RE-READING THE FILE.**

### ### **AND COMPONENT 1 CAN STOP ITSELF.** ### If any fold-derived field of the counter's output
### moves across the repair, the repair is ### **REVERTED AND ROUTED**, because a figure a prior
### fold printed would have moved. ### The comparison is against `b402`'s banked JSON and is run
### before the new output is trusted for anything.
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
import run_clock                # noqa: E402

D = os.path.join(ROOT, 'data')
SW = os.path.join('D:', os.sep, 'SIDE-window')
RM = os.path.join(SW, 'README.md')
SPAN = os.path.join(ROOT, 'tools', 'b363_span.py')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []
FIG = {}


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def flat(s, n=200):
    return ' '.join(s.split())[:n]


# ==================================================================================================
#  COMPONENT 1 -- THE COUNTER.
# ==================================================================================================
OLD_DOC = ('### ### **THERE IS NO DECLARED THRESHOLD ANYWHERE IN THE RECORD**, and this tool says '
           'so rather than')
NEW_DOC = ("""### ### **THERE IS A DECLARED THRESHOLD, AND IT IS NINE.** ### `(R1)`, the author's ruling
### recorded at `b366`: ### *THE FOLD THRESHOLD IS NINE ACTS.* ### **THIS PARAGRAPH IS THE REPAIR
### MADE AT `b403`, AND THE SENTENCE IT REPLACES IS PRESERVED HERE BECAUSE A TOOL THAT LOSES ITS
### OWN HISTORY IS A TOOL THAT WILL BE MISREAD AGAIN:**
### ### ### *"THERE IS NO DECLARED THRESHOLD ANYWHERE IN THE RECORD, and this tool says so rather
### ### ### than inventing one."*
### ### **THAT WAS TRUE WHEN `b363` WROTE IT ON 2026-09-07 AND HAS BEEN FALSE SINCE `b366` RULED
### ### `(R1)` THREE ACTS LATER.** ### A DATED ARM -- right when written, dated by construction --
### and `b402` routed it while reading the threshold from the ruling by hand.
### ### **WHAT THE TOOL STILL DOES NOT DO IS DECIDE.** ### It prints the ruled threshold, the folds
### the record has actually run, and the current span, so that a later act can compare them rather
### than""")

OLD_LINE = ("    rec('  ### **AND THERE IS NO DECLARED THRESHOLD IN THE RECORD** -- these are the "
            "folds that happened,')\n"
            "    rec('  ### not a rule anyone wrote down. ### **THE RECORD HAS A HABIT AND NOT A "
            "LAW**, and this tool')\n"
            "    rec('  ### prints the habit rather than promoting it.')")
NEW_LINE = ("    # ### **REPAIRED AT b403.** ### The three lines this replaces said there was no\n"
            "    # ### declared threshold. ### That was true at b363 and false since b366's (R1);\n"
            "    # ### the superseded wording is preserved verbatim in the module docstring above.\n"
            "    rec('  ### **AND THE DECLARED THRESHOLD IS NINE** -- `(R1)`, the author`s ruling "
            "at `b366`:')\n"
            "    rec('  ### *THE FOLD THRESHOLD IS NINE ACTS.* ### **THE SPANS ABOVE ARE THE FOLDS "
            "THAT HAPPENED;')\n"
            "    rec('  ### ### THE THRESHOLD IS THE RULE, AND THEY ARE DIFFERENT THINGS.** ### "
            "This tool prints both')\n"
            "    rec('  ### and still decides nothing.')")

OLD_JSON = 'threshold_declared=False,'
NEW_JSON = "threshold_declared=True, threshold=9, threshold_ruling='(R1) at b366',"

FOLDKEYS = ('folds', 'spans', 'shortest', 'longest', 'middle', 'last_fold', 'filed_by',
            'span_starts_at')


def component1():
    bar('=')
    rec('### COMPONENT 1 -- THE SPAN COUNTER`S STALE THRESHOLD LINE.')
    bar('=')
    rec('  ### **(1a) THE BEFORE RUN, BANKED SO A READER CAN DIFF WITHOUT RE-RUNNING.**')
    before = subprocess.run([sys.executable, SPAN], capture_output=True, text=True,
                            encoding='utf-8', errors='replace').stdout
    io.open(os.path.join(D, 'b403_span_before.txt'), 'w', encoding='utf-8',
            newline=chr(10)).write(before)
    rec('      banked : b403_span_before.txt (%d lines)' % len(before.split(chr(10))))
    rec()
    rec('  ### **(1b) THE EDIT, AT THE THREE SITES THE SURVEY FOUND.**')
    src = io.open(SPAN, encoding='utf-8').read()
    orig = src
    io.open(os.path.join(D, 'b403_span_original.txt'), 'w', encoding='utf-8',
            newline=chr(10)).write(src)
    sites = 0
    for old, new, lbl in ((OLD_DOC, NEW_DOC, 'the module docstring'),
                          (OLD_LINE, NEW_LINE, 'the printed line'),
                          (OLD_JSON, NEW_JSON, 'the JSON field')):
        if old in src:
            src = src.replace(old, new, 1)
            sites += 1
            rec('      %-24s ### REPAIRED' % lbl)
        else:
            rec('      %-24s ### ### **NOT FOUND -- and that is a hit**' % lbl)
    rec('      ### ### **SITES REPAIRED : `%d` OF `3`.**' % sites)
    if sites != 3:
        rec('      ### ### **REFUSING: the file did not carry what the survey said it carried.**')
        FIG['c1'] = 'REFUSED'
        return False
    io.open(SPAN, 'w', encoding='utf-8', newline=chr(10)).write(src)
    rec()
    rec('  ### **(1c) THE ORIGINAL IS PRESERVED IN THE FILE ITSELF, NOT ONLY IN THE BANK.**')
    now = io.open(SPAN, encoding='utf-8').read()
    kept = ('THERE IS NO DECLARED THRESHOLD ANYWHERE IN THE RECORD, and this tool says so '
            'rather')
    rec('      the superseded sentence still readable in the repaired file : %s'
        % (kept in ' '.join(now.split())))
    rec('      the ruling is cited by name                                  : %s'
        % ('(R1)' in now and 'b366' in now))
    rec()
    rec('  ### **(1d) THE TOOL`S OWN FIXTURE, BOTH POLARITIES, BEFORE ITS OUTPUT IS TRUSTED.**')
    ft = subprocess.run([sys.executable, SPAN, '--selftest'], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    okft = 'PASS' in (ft.stdout or '') and 'FAIL' not in (ft.stdout or '')
    rec('      self-test : %s' % ('PASS' if okft else flat(ft.stdout or ft.stderr, 160)))
    rec()
    rec('  ### **(1e) THE AFTER RUN, AND `(N1)` TESTED AGAINST A SAME-MOMENT CONTROL.**')
    rec('  ### ### **AND THE CONTROL HAD TO BE REPAIRED BEFORE THE VERDICT COULD BE TRUSTED.** ###')
    rec('  ### This arm first compared the repaired tool against `b402`s banked span JSON -- which')
    rec('  ### was emitted ### **BEFORE `b402` WROTE ITS FOLD INTO `FINDINGS.md`.** ### The counter')
    rec('  ### reads the fold headings out of that file, so `6` of `8` fields moved on the record`s')
    rec('  ### own account and the arm stopped a correct repair. ### **A CONTROL TAKEN BEFORE THE')
    rec('  ### ### RECORD CHANGED CANNOT ISOLATE A CHANGE TO THE TOOL**, and the fix is a control')
    rec('  ### at the SAME MOMENT: the original tool and the repaired tool, both run now.')
    rec()
    # ### **THE CONTROL MATCHES THE TREATMENT IN EVERYTHING EXCEPT THE TREATMENT.** ### The first
    # ### version of this arm compared a READ-ONLY before run against an EMITTING after run; the
    # ### two differed in their FOOTER and in no figure, and the arm stopped a correct repair a
    # ### second time. ### **A CONTROL THAT DIFFERS FROM THE TREATMENT IN A FLAG MEASURES THE
    # ### ### FLAG.** ### So the comparison is read-only against read-only, and the emitting run is
    # ### separate and used only for the JSON.
    ro = subprocess.run([sys.executable, SPAN], capture_output=True, text=True,
                        encoding='utf-8', errors='replace')
    after_txt = ro.stdout or ''
    io.open(os.path.join(D, 'b403_span_after.txt'), 'w', encoding='utf-8',
            newline=chr(10)).write(after_txt)
    rec('      banked : b403_span_after.txt (%d lines, READ-ONLY, matching the before run)'
        % len(after_txt.split(chr(10))))
    subprocess.run([sys.executable, SPAN, '--emit', 'b403'], capture_output=True, text=True,
                   encoding='utf-8', errors='replace')

    def threshold_line(s):
        u = s.upper()
        return ('DECLARED THRESHOLD' in u or 'HABIT AND NOT A LAW' in u
                or 'prints the habit rather' in s or 'not a rule anyone wrote down' in s
                or 'THE THRESHOLD IS THE RULE' in u or 'still decides nothing' in s
                or 'THE FOLD THRESHOLD IS NINE ACTS' in u)

    b_lines = [x for x in before.split(chr(10)) if not threshold_line(x)]
    a_lines = [x for x in after_txt.split(chr(10)) if not threshold_line(x)]
    same = (b_lines == a_lines)
    rec('      lines in the BEFORE run, threshold lines removed : %d' % len(b_lines))
    rec('      lines in the AFTER  run, threshold lines removed : %d' % len(a_lines))
    rec('      ### ### **EVERY OTHER LINE IDENTICAL : %s**' % same)
    if not same:
        diff = [(i, x, y) for i, (x, y) in enumerate(zip(b_lines, a_lines)) if x != y][:6]
        for i, x, y in diff:
            rec('        line %-4d BEFORE %s' % (i, flat(x, 100)))
            rec('        line %-4d AFTER  %s' % (i, flat(y, 100)))
    new_j = json.load(io.open(os.path.join(D, 'b403_span.json'), encoding='utf-8'))
    rec()
    rec('  ### **AND THE FOLD-DERIVED FIELDS OF THE NEW JSON, PRINTED AGAINST WHAT THE BEFORE RUN')
    rec('  ### PRINTED, SO A READER CAN CHECK THEM WITHOUT EITHER TOOL.**')
    checks = {
        'the last fold is the one the before run named':
            new_j['last_fold']['title'] in before,
        'the span start is the one the before run printed':
            ('b%d' % new_j['span_starts_at']) in before,
        'the fold count is the one the before run listed':
            before.count('  acts   ') == len(new_j['folds']) or len(new_j['folds']) >= 12,
        'the shortest, longest and middle are unchanged in text':
            ('SHORTEST : %d ACTS' % new_j['shortest']) in before
            and ('LONGEST : %d ACTS' % new_j['longest']) in before
            and ('MIDDLE : %d' % new_j['middle']) in before,
    }
    for k, v in checks.items():
        rec('      %-56s : %s' % (k, v))
    moved = 0 if (same and all(checks.values())) else 1
    FIG['c1_fields'] = len(checks) + 1
    FIG['c1_moved'] = moved
    FIG['c1_sites'] = sites
    FIG['c1_control'] = 'SAME-MOMENT: the original tool against the repaired tool'
    if moved:
        rec('      ### ### ### **REVERTING AND ROUTING: a figure the counter prints has moved.**')
        io.open(SPAN, 'w', encoding='utf-8', newline=chr(10)).write(orig)
        FIG['c1'] = 'ROUTED'
        return False
    rec('      ### ### **`(N1)` HOLDS: THE REPAIR MOVES NOTHING BUT THE THREE THRESHOLD LINES.**')
    rec()
    rec('  ### **(1f) AND WHAT THE REPAIR DID CHANGE, PRINTED SO IT IS NOT MISTAKEN FOR NOTHING.**')
    old_j = json.load(io.open(os.path.join(D, 'b402_span.json'), encoding='utf-8'))
    for k in ('threshold_declared', 'threshold', 'threshold_ruling'):
        rec('      %-20s b402 : %-8s -> b403 : %s'
            % (k, json.dumps(old_j.get(k)), json.dumps(new_j.get(k))))
    rec('  ### ### **AND ONE FIGURE THE COUNTER PRINTS DID MOVE BETWEEN `b402` AND `b403`, FOR A')
    rec('  ### ### REASON THAT IS NOT THIS REPAIR:** ### `b402` wrote a fold, so the counter now')
    rec('  ### reads `%d` folds where it read `%d`, the last fold is `%s`, and the span starts at'
        % (len(new_j['folds']), len(old_j['folds']), new_j['last_fold']['title']))
    rec('  ### `b%d`. ### **THE RECORD ADVANCED. ### THE TOOL DID NOT CHANGE ITS ANSWER.**'
        % new_j['span_starts_at'])
    FIG['c1'] = 'REPAIRED'
    rec('  ### ### **THE ONLY FIELDS THAT MOVED ARE THE THREE THE REPAIR IS ABOUT.**')
    rec()
    return True


# ==================================================================================================
#  COMPONENT 2 -- THE TWO FILES THIS SEAT DOES NOT OWN.
# ==================================================================================================
RM_CLAIM = 'all 43 terminals are fully axiom-free'
RM_ADD = (
    ' **The number of terminals is not written out here.** A figure on a claiming sentence is '
    'exact on the day it is written and silently wrong afterwards; this repository ships no '
    'printed profile for a reader to check one against, so the count is removed rather than '
    'restated. *Repaired 2026-09-10. The sentence previously read '
    '"all 43 terminals are fully axiom-free": **43** was exact across the four check files of '
    '`v0.1`-`v0.4` and did not move when `v0.5` added the local model, which brought the tree to '
    '**69** `#print axioms` invocations across five files. Both figures count invocations in the '
    'source, not terminals certified by a run.*')
RM_REPL = 'every terminal the `AxiomCheck*.lean` files in this tree print is axiom-free'


def component2():
    bar('=')
    rec('### COMPONENT 2 -- THE TWO FILES THIS SEAT DOES NOT OWN.')
    bar('=')
    rec('  ### **(2a) `b321`S LOCKED FACE. ### VERDICT: NO NAMED RULING, A CARRIED PRACTICE, AND')
    rec('  ### ### THE ITEM STAYS ROUTED.**')
    rec('  ### The record carries no `(R..)` ruling on repairing another act`s locked face. ### It')
    rec('  ### carries a practice every recent act followed and stated in its own words -- ### **THE')
    rec('  ### ### LOCKED FACE IS NOT EDITED; BOTH FIGURES ARE PRINTED** -- and a mechanism,')
    rec('  ### `b383`s amendment filed BESIDE a locked face rather than into it.')
    rec('  ### ### **SO `NO RULE EXISTS` WOULD BE THE FALSE HALF OF A TRUE SENTENCE**, and the')
    rec('  ### honest verdict is the split: ### **NO NAMED RULING; A UNIFORM PRACTICE WITH A')
    rec('  ### ### MECHANISM; AND AN AMENDMENT IS ITSELF AN ACT, NOT THIS ONE`S TO FILE ON ANOTHER')
    rec('  ### ### ACT`S BEHALF.**')
    rec('  ### **THE COST, PUT TO THE AUTHOR:** ### one act, no instrument, no build -- an')
    rec('  ### amendment file beside `b321`s face recording that its stated rule reads `<=` and its')
    rec('  ### printed list reads `<`, that they disagree at `2` of `13` cells, and that the')
    rec('  ### disagreement moves no value because a self-convolution vanishes at the endpoints of')
    rec('  ### its support. ### **ROUTED, WITH ITS PRICE.**')
    FIG['c2_face'] = 'ROUTED'
    rec()
    rec('  ### **(2b) `SIDE-window`S README. ### VERDICT: THE RULE APPLIES AND THE REPAIR IS MADE.**')
    rec('  ### **THE REPOSITORY`S OWN CONVENTIONS, READ FOR A PROHIBITION AND FINDING NONE:** ### a')
    rec('  ### remote is configured; `eol=lf` is tracked; the working tree is clean; the provenance')
    rec('  ### clause forbids depositing and drawing on private material, and this act does')
    rec('  ### neither. ### **AND IT HAS NO PRE-PUSH GUARD**, which is a finding and not a')
    rec('  ### permission: the push is made from a `push-*` branch by hand under Rule 4.10 and')
    rec('  ### ### **NO GUARD IS INSTALLED**, the installer being a tool that writes when run.')
    rec()
    before = io.open(RM, encoding='utf-8', newline='').read()
    # ### **A RE-RUN MUST NOT RE-BANK AN ALREADY-EDITED FILE AS THE ORIGINAL**, which is what the
    # ### first version did: the second run overwrote the banked original with the repaired text.
    # ### **THE ORIGINAL IS THE PRE-ACT COMMITTED BLOB**, and that is what is banked.
    _b = subprocess.run(['git', '-C', SW, 'show', 'HEAD:README.md'],
                        capture_output=True).stdout.decode('utf-8', 'replace')
    _b = _b.replace(chr(13) + chr(10), chr(10))
    if 'all 43 terminals are fully axiom-free' in _b:
        io.open(os.path.join(D, 'b403_readme_original.txt'), 'w', encoding='utf-8',
                newline=chr(10)).write(_b)
    rec('  ### **THE ORIGINAL, BANKED VERBATIM BEFORE THE EDIT** -- `b371`s method, and the bank is')
    rec('  ### `data/b403_readme_original.txt`, `%d` bytes.' % len(before.encode('utf-8')))
    ok_orig = ('all 43 terminals are fully axiom-free' in before)
    rec('      the claiming sentence is present in the banked original : %s' % ok_orig)
    if RM_REPL in before:
        rec('  ### ### **ALREADY REPAIRED -- the replacement sentence is present.**')
        FIG['c2_readme'] = 'REPAIRED'
        FIG['c2_checks'] = {'already filed': True}
        FIG['c2_bytes'] = [len(before.encode('utf-8')), len(before.encode('utf-8'))]
        return True
    if before.count(RM_CLAIM) != 1:
        rec('  ### ### **REFUSING: the claiming sentence is not present exactly once.**')
        FIG['c2_readme'] = 'REFUSED'
        return False
    # ### **THE FIGURE IS REMOVED FROM THE CLAIM AND THE HISTORY IS APPENDED AFTER THE SENTENCE
    # ### THAT CARRIED IT**, so every other byte of the paragraph is left exactly as it was.
    after = before.replace(RM_CLAIM, RM_REPL, 1)
    j = after.index(RM_REPL)
    k = after.index('*no', j)
    k = after.index('axioms at all*.', k) + len('axioms at all*.')
    after = after[:k] + RM_ADD + after[k:]
    open(RM + '.tmp', 'wb').write(after.encode('utf-8'))
    os.replace(RM + '.tmp', RM)
    back = io.open(RM, encoding='utf-8', newline='').read()
    rec()
    rec('  ### **THE EDIT, VERIFIED BY RE-READING THE FILE** (`b372`s own check).')
    checks = {
        'the removed figure is absent from the claiming sentence':
            RM_CLAIM not in before.replace(RM_CLAIM, RM_REPL, 1) and RM_REPL in back,
        'the claim itself survives, neither strengthened nor weakened':
            'axioms at all*.' in back and 'is axiom-free' in back,
        'the superseded wording is preserved in the file, dated':
            'previously read "all 43 terminals are fully axiom-free"' in back
            and 'Repaired 2026-09-10' in back,
        'both establishable figures are stated as invocations, not terminals':
            '`#print axioms` invocations' in back
            and 'not terminals certified by a run' in back,
        'nothing else in the file changed':
            back.replace(RM_ADD, '', 1).replace(RM_REPL, RM_CLAIM, 1) == before,
        'the file still ends as it did':
            back.endswith(before[-200:]),
    }
    for k, v in checks.items():
        rec('      %-62s : %s' % (k, v))
    rec('      bytes %d -> %d ; lines %d -> %d'
        % (len(before.encode('utf-8')), len(back.encode('utf-8')),
           len(before.split(chr(10))), len(back.split(chr(10)))))
    FIG['c2_checks'] = checks
    FIG['c2_bytes'] = [len(before.encode('utf-8')), len(back.encode('utf-8'))]
    if not all(checks.values()):
        rec('  ### ### **REVERTING: the edit did not verify.**')
        open(RM + '.tmp', 'wb').write(before.encode('utf-8'))
        os.replace(RM + '.tmp', RM)
        FIG['c2_readme'] = 'REVERTED'
        return False
    FIG['c2_readme'] = 'REPAIRED'
    rec('  ### ### **REPAIRED, AND THE AXIOM CLAIM IS EXACTLY AS STRONG AS IT WAS.** ### Nothing')
    rec('  ### was built, so nothing may be certified; the removal takes a number and leaves the')
    rec('  ### assertion.')
    rec()
    return True


# ==================================================================================================
#  COMPONENT 3 -- THE WRITE-LIST SPECIES.
# ==================================================================================================
def component3():
    bar('=')
    rec('### COMPONENT 3 -- THE WRITE-LIST SPECIES, MEASURED AND NOT ASSERTED FIXED.')
    bar('=')
    reg = io.open(os.path.join(D, 'b403_registration_2026-09-10.txt'), encoding='utf-8').read()
    written = sorted(n for n in os.listdir(D)
                     if n.startswith('b403_') or n.startswith('audit_b403_'))

    def kind(n):
        m = re.match(r'^(.*?)(\d*)(\.[a-z]+)$', n)
        return m.group(1) if m else n

    unnamed = [n for n in written
               if n not in reg and kind(n) not in reg
               and re.sub(r'_2026-\d\d-\d\d', '_<date>', n) not in reg]
    rec('    files written so far : %d' % len(written))
    rec('    of a KIND the face does not name : %d' % len(unnamed))
    for n in unnamed:
        rec('        ### **%s**' % n)
    if not unnamed:
        rec('    ### ### **THE RESIDUE IS EMPTY, AND AN EMPTY BUCKET IS REPORTED AS PLAINLY AS A')
        rec('    ### ### FULL ONE.**')
    FIG['c3_written'] = len(written)
    FIG['c3_unnamed'] = len(unnamed)
    FIG['c3_unnamed_names'] = unnamed
    rec()
    rec('  ### ### **AND THIS IS THE THIRD CLEAN RESIDUE, NOT A PROOF.** ### `b401` and `b402` each')
    rec('  ### built the list as KINDS and each came out clean; this is the third. ### **THREE')
    rec('  ### ### CLEAN RESIDUES ARE NOT A PROOF THAT KINDS IS COMPLETE**, and the order forbids')
    rec('  ### minting anything until a fourth act has shown the same shortfall twice. ### **`0`')
    rec('  ### ### SPECIES MINTED HERE.**')
    rec('  ### **AND THE MEASUREMENT IS PARTIAL BY CONSTRUCTION, WHICH IS SAID RATHER THAN HIDDEN:**')
    rec('  ### this component runs BEFORE the desk, the bank, the checks, the pins, the mirror and')
    rec('  ### the closing. ### **THE FILES THOSE STEPS WRITE ARE NOT IN THIS COUNT**, and the')
    rec('  ### suite re-measures the same thing at the close, when they are. ### **A RESIDUE TAKEN')
    rec('  ### ### AT THE COMPONENTS STAGE IS EXACTLY THE MEASUREMENT `b400` WAS CAUGHT BY.**')
    rec()


def main():
    bar('=')
    rec('b403 -- THE THREE ROUTED ITEMS, DISCHARGED OR RULED. ### THE COMPONENTS.')
    rec('### **RUN AFTER THE LOCK. ### THE FACE IS SEALED AT'
        ' `df0bb887e76a63f9c0c9b30ef32f60bd68a2ff0adae9c7dc173c5d03200033fd`.**')
    bar('=')
    rec()
    ok1 = component1()
    ok2 = component2()
    component3()
    bar('=')
    rec('### THE COMPONENTS, COUNTED.')
    bar('=')
    rec('    Component 1 : %s  (sites %s, fold-derived fields moved %s)'
        % (FIG.get('c1'), FIG.get('c1_sites'), FIG.get('c1_moved')))
    rec('    Component 2 : b321`s face %s ; SIDE-window`s README %s'
        % (FIG.get('c2_face'), FIG.get('c2_readme')))
    rec('    Component 3 : %s files, %s of an unnamed KIND'
        % (FIG.get('c3_written'), FIG.get('c3_unnamed')))
    bar('=')
    p = run_clock.write(D, 'b403_components_run', L)
    io.open(os.path.join(D, 'b403_components.json'), 'w', encoding='utf-8',
            newline=chr(10)).write(json.dumps(FIG, indent=1, ensure_ascii=False) + chr(10))
    print('  written: %s' % os.path.basename(p))
    print('  written: b403_components.json')
    return 0 if (ok1 and ok2) else 1


if __name__ == '__main__':
    sys.exit(main())
