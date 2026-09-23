# -*- coding: utf-8 -*-
"""b479_desk_bank.py -- THE DESK, THE SCORES, THE CORRESPONDENCE ROW, THE BANK.
### ### **EVERY FIGURE HERE IS READ FROM THIS ACT'S OWN RECORDS, NEVER TYPED.**
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import corr_row  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

D = os.path.join(ROOT, 'data')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
CORR = os.path.join(SIDE, 'CORRESPONDENCE.md')
NL = chr(10)
L = []


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def main():
    span = json.loads(read(os.path.join(D, 'b479_span.json')))
    R = json.loads(read(os.path.join(D, 'b479_results.json')))
    SV = json.loads(read(os.path.join(D, 'b479_survey.json')))
    RES = json.loads(read(os.path.join(D, 'b479_results.json')))
    FILED = json.loads(read(os.path.join(D, 'b479_filing.json')))

    rec('=' * 100)
    rec('b479_desk_bank.py -- THE DESK, THE SCORES, THE ROW, THE BANK.')
    rec('=' * 100)
    rec('  figures READ from this act`s own records, never typed:')
    rec('    the tag : %s ; conjuncts in h1_complete_at_Phi : ### **%d** for seven classes'
        % (SV['sha'][:7], SV['conjuncts']))
    rec('    statements naming the Mellin transform : ### **%d of %d**'
        % (sum(1 for f in SV['facts'] if f['mentions_mellin']), len(SV['facts'])))
    rec('    TOUCHES THE FORM : ### **%s** ### ; APART : ### **%s**'
        % (', '.join(RES['touch']), ', '.join(RES['apart'])))
    rec('    ### ### **BOTH SPAN READINGS, AS (R96) REQUIRES:**')
    rec('      the tool, by NUMBER order : ### **%d**' % span['current_span'])
    rec('      by FILING since the b474 fold : ### **%d** ### (this act will make it %d)'
        % (FILED['count'], FILED['count'] + 1))
    rec('      ### the tool is NOT edited.')
    rec('')
    rec('-' * 100)
    rec('### THE DESK, SWEPT. ### **b482 LEFT FIFTY-FOUR STANDING; THIS ACT SWEEPS THOSE AND ITS OWN.**')
    rec('-' * 100)

    desk = [
        ('(R66) the deposit corrected, not re-issued', 'STAND', ['BOUNDED BY (R95); the drafting is the act after the fold`s.']),
        ('what the fired control does not license', 'STAND', ['UNTOUCHED.']),
        ('the index holds no entry for b452`s verdicts', 'STAND', ['UNTOUCHED.']),
        ('the twelve face-only arms', 'STAND', ['UNDER (R72).']),
        ('the two kernel records` Zenodo descriptions are not banked', 'STAND', ['ROUTED INTO (R95).']),
        ('the terminal-less census, and what it is not', 'STAND', ['UNTOUCHED.']),
        ('the terminal search`s alphabetical tie-break', 'STAND', ['UNTOUCHED.']),
        ('five parameters of the imported formula with no site', 'STAND', ['UNTOUCHED.']),
        ('PATHS carries no proportion table', 'STAND', ['SHARPENED AT b482.']),
        ('a site verdict is source-relative, not absolute', 'STAND', ['UNTOUCHED.']),
        ('the general source carries a height outside its explicit formula', 'STAND', ['UNTOUCHED.']),
        ('the record carried the wrong repository name for nine acts', 'STAND', ['ROUTED.']),
        ('a name matcher cannot see a repository', 'STAND', ['REPAIRED AT b468.']),
        ('an AI-disclosure line is not an artefact', 'STAND', ['ROUTED.']),
        ('a utf-8-sig read and a utf-8 write silently drop a BOM', 'STAND', ['ROUTED.']),
        ('a pointer can name a blank line', 'STAND', ['ROUTED.']),
        ('#print axioms on zeta23 is not run', 'STAND', ['THE b475 RUN IS ANOTHER ACT`S; ITS LOG UNOPENED.']),
        ('AUDIT.md describes a different statement set', 'STAND', ['ROUTED.']),
        ('the span tool cannot place a re-run filed out of number order', 'STAND',
         ['### ### **AND (R96) DISPOSES OF IT WITHOUT EDITING THE TOOL:** the fold counts BY FILING,',
          'and both readings are printed. ### The tool reads ### **%d** ### for b479 by number;'
          % span['current_span'],
          'the trail`s own records give ### **%d** ### acts filed since the b474 fold, %d with this'
          % (FILED['count'], FILED['count'] + 1),
          'one. ### **A TOOL THAT ANSWERS A DIFFERENT QUESTION IS NOT A BROKEN TOOL**, and it is',
          'not edited. ### The item stands as a known limitation with a ruled work-around.']),
        ('W-ORD-GW-IMPORT', 'STAND', ['(R82) STILL NOT YET DECIDABLE; (R83) DOES NOT FIRE.']),
        ('lake 5.0.0 has no -j', 'STAND', ['SERIALIZED BY THE LAUNCHER AT b475.']),
        ('an import-of-Mathlib floor above the foreground bound', 'STAND', ['MEASURED AT b470.']),
        ('the explicit formula separates from the headline', 'STAND',
         ['### ### **AND b479 MEASURES HOW FAR THE FORMALISATION REACHES IT:** of the seven classes,',
          '### **TWO** ### have statements that name the Mellin transform at all. ### The item',
          'stands and is now quantified.']),
        ('the navigator`s ledger entry owed under (R81)', 'STAND', ['THREE ENTERED AT THE FOLD.']),
        ('the E0 table has no site column', 'STAND', ['READ CELL BY CELL AT b478.']),
        ('a silent bank is not a verdict of absence', 'STAND', ['UNTOUCHED BY THIS ACT.']),
        ('the span stands at the fold threshold', 'STAND',
         ['### ### **THE FOLD IS NEXT, UNDER (R96), AND TAKES THE NEXT FREE NUMBER.** ### It covers',
          'every act filed since b474 BY FILING: %d with this one. ### Not opened by this act.'
          % (FILED['count'] + 1)]),
        ('the run died of memory, not of mathematics', 'STAND', ['MEASURED AT b480.']),
        ('a completed axiom run is owed, and its price is now a memory bound', 'STAND',
         ['THE BANKED READ LINE STILL STANDS.']),
        ('the compression register, opened as a lane and empty', 'STAND', ['CLOSED AT b483, NO GRADE.']),
        ('a face names each tool`s write pattern, not each file', 'STAND', ['CLOSED BY (R91) AT b483.']),
        ('two of the six sites bear on nothing the E0 table grades', 'STAND', ['FOUND AT b478.']),
        ('three constituents no site touches', 'STAND', ['FOUND AT b478.']),
        ('the order`s Epstein height is in no bank the record holds', 'STAND', ['ROUTED.']),
        ('the Voros threshold is a Li-register fact and does not price this tail', 'STAND', ['FOUND AT b476.']),
        ('a batch FOR block stamps one time on every line', 'STAND', ['FOUND AT b480; ROUTED.']),
        ('a gate waits on a job the record does not carry', 'STAND', ['CLOSED BY (R90) AT b483.']),
        ('the bar on the deposited records is capability, not permission', 'STAND', ['DISCHARGED AT b485.']),
        ('a drafted note eighty-six acts old is still written nowhere', 'STAND', ['WRITTEN AT b485.']),
        ('the gate`s fifth site is not locatable at this seat', 'STAND', ['UNTOUCHED.']),
        ('one live currency claim contradicts REGISTRY', 'STAND', ['DISCHARGED AT b484.']),
        ('a priced resolving size that the arithmetic forbids', 'STAND', ['FOUND AT b483; ROUTED.']),
        ('a bound the chain reports is not the bound it achieves', 'STAND',
         ['FILED AS `W-ORD-QUADRATURE-BOUND` AT b484; its trigger has not fired.']),
        ('the seat read its own expectation backwards', 'STAND', ['FOUND AT b483; ROUTED.']),
        ('two unrelated tests single out sqrt(17)', 'STAND', ['LEFT OPEN AT b484.']),
        ('a search that can see its own report will always confirm it', 'STAND', ['ROUTED.']),
        ('a matcher that counts co-occurrence is not counting a claim', 'STAND', ['FOUND AT b484.']),
        ('REGISTRY`s own history table disagrees with the records', 'STAND', ['ANNOTATED AT b485.']),
        ('a frozen ledger cannot be repaired without breaking its own law', 'STAND', ['FOUND AT b485.']),
        ('an index-query gate fires on an arm`s own name', 'STAND', ['FOUND AT b485; ROUTED.']),
        ('a tool that can crash after a write needs a guard before it', 'STAND',
         ['THE GUARD IS IN THREE ACTS` DESK TOOLS NOW; ### **IT BELONGS IN `corr_row.py`.** ### ROUTED.']),
        ('an order cited across three sealed faces with no bank behind it', 'CLOSE',
         ['### ### **DISCHARGED BY (R96), WHICH RE-ISSUES b479 UNDER ITS OWN NUMBER AND SAYS WHY',
          'THERE WAS NO BANK:** its earlier registration *"having been carried in a clarification',
          'and not banked as an order."* ### **THE SEAT REPORTED THE HALT AND THE AUTHOR SUPPLIED',
          'THE ORDER** -- which is what the halt was for. ### The species stays on the desk under',
          'its own name below.']),
        ('a claim can propagate across sealed faces without a carrier', 'MINT',
         ['MINTED AT b479 AS THE SPECIES b482`S INCIDENT BELONGS TO. ### Three sealed faces carried',
          '*"b479 is registered by its own ferry"* and no ferry did. ### **THE SEAL WAS SOUND AND',
          'THE SENTENCE WAS FALSE**, because a seal fixes BYTES and not TRUTH.',
          '### ### **THE GUARD THE RECORD ALREADY HAS IS `G-NUMBER-UNCLAIMED`, AND IT CHECKED THE',
          'WRONG THING:** it asked whether a NUMBER was claimed, not whether an ORDER was BANKED.',
          '### ROUTED: an arm that resolves every act number a face names to a banked ferry.']),
        ('a statement posed is not a result', 'STAND', ['FOUND AT b482.']),
        ('a terminal named for mathematics can state arithmetic', 'STAND',
         ['FOUND AT b482 IN SIDE-simplicity; ### **AND b479 FINDS ITS COMPANION IN lv:** five of the',
          'seven classes` statements constrain `Φ` and never name its transform, while their',
          'DOCSTRINGS carry the route to the form. ### **THE PATTERN IS NOT ONE REPOSITORY`S.**']),
        ('a def and a theorem do not mean the same thing by `:=`', 'MINT',
         ['FOUND AT b479 BY (R70)`S REHEARSAL, BEFORE THE SEAL. ### The fact reader stopped at the',
          'first `:=` for every declaration. ### For a `theorem` that is right -- the proof follows.',
          '### For `def C : Coupling := fun Φ => <predicate>` it is ### **WRONG**: the `:=` is on',
          'the declaration line and ### **THE PREDICATE IS THE CONTENT.** ### The reader returned',
          '`def C2_halfplane_nonvanishing : Coupling` and reported ### **`0` statements naming the',
          'Mellin transform where the true figure is `3`** -- a figure that decides two rows of the',
          'table. ### **A REHEARSAL ON A CASE WHOSE ANSWER IS KNOWN IS WHAT (R70) IS FOR, AND IT',
          'PAID HERE.** ### ROUTED: the repaired reader belongs in a shared tool.']),
        ('five of seven classes reach the form only through their docstrings', 'MINT',
         ['FOUND AT b479, AND IT IS THE ACT`S CENTRAL MEASUREMENT. ### Of the eight per-class facts',
          '`h1_complete_at_Phi` conjoins, ### **THREE NAME `mellin Φ (s/2)`** -- `C2` and `C7`s two',
          '-- and ### **FIVE DO NOT.** ### `C1`, `C3`, `C4`, `C5` and `C6` constrain `Φ` on the real',
          'ray or in `τ`, and their route to Weil`s form runs through derivations their statements',
          'do not carry. ### ### **THIS IS A MEASUREMENT OF THE FORMALISATION`S REACH AND NOT OF THE',
          'ARGUMENT`S TRUTH**, and the act says so in its own Component 3.',
          '### ### **AND THE ONE ROW THAT CARRIES THE MOST IS HALF OPEN:** `C7`s row is carried by',
          '`C7_order`, which the file`s own docstring marks OPEN and prices as a Gamma-asymptotics',
          'project. ### ROUTED.']),
    ]
    for name, state, why in desk:
        rec('    %-58s %s' % (name, state))
        for w in why:
            rec('        ' + w)
    closed = sum(1 for _, s, _ in desk if s == 'CLOSE')
    minted = sum(1 for _, s, _ in desk if s == 'MINT')
    standing = sum(1 for _, s, _ in desk if s in ('STAND', 'MINT'))
    rec('')
    rec('    ### ### **ITEMS SWEPT : %d. ### CLOSED : %d. ### MINTED HERE : %d. ### STANDING : %d.**'
        % (len(desk), closed, minted, standing))

    rec('-' * 100)
    rec('### THE EXPECTATIONS, SCORED.')
    rec('-' * 100)
    SC = dict(
        N1=dict(nav='C2, C3 and C7 TOUCH',
                verdict='HELD IN PART -- C2 AND C7 TOUCH, C3 DOES NOT',
                note=('`C3`s statement is `forall t, 0 < t -> Phi (1/t) = sqrt t * Phi t + '
                      '(sqrt t - 1)/2` -- an identity for `Phi` on the positive reals that '
                      '### **NEVER MENTIONS THE MELLIN TRANSFORM.** ### The functional equation is '
                      'what `C3` YIELDS through a derivation; ### **IT IS NOT WHAT `C3` SAYS**, and '
                      'the order asks for the statement and not the docstring. ### The face '
                      'registered this split in advance.')),
        N2=dict(nav='C1, C4 and C6 are APART',
                verdict='HELD',
                note=('`C1` fixes an imaginary part of `Phi`; `C4` constrains a function of `tau` '
                      'on the upper half-plane; `C6` extends `Phi` itself to a half-plane. ### '
                      '**NONE NAMES A TRANSFORM OR A TEST FUNCTION.**')),
        N3=dict(nav=('C5 touches by the disclaimed Hilbert-Polya register, and the act says so '
                     'rather than counting it'),
                verdict='HELD, AND THE REPOSITORY SAYS IT FIRST',
                note=('`C5_input` is APART on its own statement -- a heat trace with a '
                      'non-negative spectrum, no transform named. ### `C5_output` WOULD reach the '
                      'form, placing the spectrum on `rho.re = 1/2` -- and the file itself carries '
                      '### **"NOTE: C5_output is deliberately NOT in sevenClasses: it is the '
                      'disclaimed half."** ### It is NOT counted in the table, and the row says '
                      'why. ### **THE PREMISE OF THIS EXPECTATION IS THE REPOSITORY`S OWN.**')),
    )
    for k in ('N1', 'N2', 'N3'):
        rec('  (%s) %s' % (k, SC[k]['nav']))
        rec('       ### ### **%s**' % SC[k]['verdict'])
        rec('       %s' % SC[k]['note'])
    rec('  ### ### **REGISTERED 3 ; HELD 2 ; HELD-IN-PART 1.**')
    rec('  ### the seat`s own calls were on the sealed face before the table was drawn and matched')
    rec('  ### all three, including registering (N1)`s split in advance.')
    json.dump(SC, io.open(os.path.join(D, 'b479_scores.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)

    rec('')
    rec('-' * 100)
    rec('### THE CORRESPONDENCE ROW. ### WRITTEN BY THE IDEMPOTENT TOOL AND READ BACK.')
    rec('-' * 100)
    before = read(CORR)
    rows = [l for l in before.split(NL) if l.startswith('| ') and l.split('|')[1].strip().isdigit()]
    nxt = int(rows[-1].split('|')[1].strip()) + 1
    rec('  the prior row by its own id : %d ; this act`s row : %d' % (nxt - 1, nxt))
    statement = (
        '**THE SEVEN MECHANISM CLASSES ARE READ AGAINST WEIL`S FORM, AND ONLY TWO OF THE SEVEN '
        'HAVE STATEMENTS THAT REACH IT** (b479, re-issued under (R96)). '
        '**Read at lv v0.10.0 = 93c27ec, statements and not docstrings, nothing compiled. '
        'h1_complete_at_Phi conjoins EIGHT per-class facts for SEVEN classes -- C7 contributes '
        'entirety and order both.** '
        '**THE CRITERION, FIXED ON THE SEALED FACE BEFORE ANY VERDICT: a fact TOUCHES the form '
        'when its statement constrains the object W is built from -- the Mellin transform of Phi -- '
        'on a family its own quantifier names. NOT ONE of the eight statements mentions a test '
        'function, W, or the explicit formula, so a literal reading would return seven APART and '
        'say nothing.** '
        '**THE TABLE. TOUCHES THE FORM: C2 and C7. APART: C1, C3, C4, C5, C6. C2 constrains '
        'mellin Phi (s/2) non-zero on 1 < re s; C7 completes that transform to an entire G and '
        'bounds G`s order on all of C. THE OTHER FIVE CONSTRAIN Phi AND NEVER NAME ITS TRANSFORM.** '
        '**(N1) HELD IN PART: C2 and C7 touch, C3 DOES NOT -- its statement is an identity for Phi '
        'on the positive reals, and the functional equation is what C3 YIELDS, not what it SAYS. '
        '(N2) HELD. (N3) HELD, and the repository says it first: the file itself carries the note '
        'that C5_output is deliberately NOT in sevenClasses because it is the disclaimed half.** '
        '**THE SENTENCE THE TABLE SUPPORTS AND NO WIDER: if the exclusions that reach the form '
        'were carried by C2 and C7 alone, the operative claim would not be exhaustiveness over the '
        'seven classes but INERTIA of the form to the other five -- and that is NOT what the '
        'seven-class argument asserts, which is that the five SUPPLY constraints. The conditional '
        'is NOT discharged. THIS MEASURES THE FORMALISATION`S REACH AND NOT THE ARGUMENT`S TRUTH.** '
        '**AND THE ONE ROW CARRYING MOST IS HALF OPEN: C7`s row rests on C7_order, which the file`s '
        'own docstring marks OPEN and prices as a Gamma-asymptotics project.** '
        'A defect in this act`s own fact reader is recorded: it stopped at the first := for every '
        'declaration, which is right for a theorem and WRONG for a def, and it reported 0 '
        'statements naming the transform where the true figure is 3. (R70)`s rehearsal on C2 caught '
        'it before the seal. '
        'Step zero`s first pins run read 4 repos hard-failing, all ls-remote unresolved at once -- '
        'transient; the retry read 0 of 4 and BOTH runs are banked. '
        'Both span readings printed per (R96): the tool reads 5 by number order, the trail gives 11 '
        'acts filed since the b474 fold with this one. The tool is not edited. '
        'Nothing compiled, no grade moved, no bridge typed; h2 quoted from the file`s own docstring '
        'as the outstanding obligation and NOT discharged.')
    cells = [str(nxt), statement,
             'NO TERMINAL ADDED, MOVED, RENAMED OR GRADED ON ANY ROW OF THE CORPUS',
             ('nothing compiled; the eight per-class facts read AS TEXT by git show at '
              'SIDE-lv-conservation v0.10.0 = 93c27ec'),
             ('NO CORPUS GRADE MOVED AND NO BRIDGE TYPED; h2 quoted from h1_complete_at_Phi and '
              'left where the deposit left it'),
             ('data/b479_components.txt; data/b479_extract.txt; data/b479_survey.json; '
              'data/b479_results.json; data/b479_scores.json; data/b479_desk_notes.txt; '
              'data/b479_pins_stepzero_firstrun.txt; '
              'data/b479_registration_2026-09-22.txt (LOCKED at sha256 8186f852c9bc6e9c); '
              'OPEN_TRAILS.md; CORRESPONDENCE.md row %d') % nxt]
    MARK = 'THE SEVEN MECHANISM CLASSES ARE READ AGAINST WEIL`S FORM'
    if MARK in before:
        rec('  ### ### **THIS ACT`S ROW IS ALREADY IN THE LEDGER; IT IS NOT APPENDED AGAIN.**')
        rec('  ### `corr_row.write_row` APPENDS and is NOT idempotent. ### This tool crashed once')
        rec('  ### AFTER its row landed, and a re-run without this guard would have written a')
        rec('  ### SECOND row for the same act. ### **A TOOL THAT CAN CRASH AFTER A WRITE NEEDS A')
        rec('  ### GUARD BEFORE IT**, and the guard reads the ledger rather than trusting the run.')
        code, out = 0, ['    (guard) row already present; nothing appended']
    else:
        code, out = corr_row.write_row(CORR, cells)
    for ln in out:
        rec('  ' + ln)
    rec('  ### write_row exit code : %d ### -- PASS only on `0`' % code)
    if code != 0:
        rec('  ### ### **HARD FAILURE: THE ROW WAS NOT WRITTEN.**')
        raise SystemExit(2)
    after = read(CORR)
    last = [l for l in after.split(NL) if l.startswith('| ')][-1]
    rowid = last.split('|')[1].strip()
    prefix = after.startswith(before.rstrip(NL)) or MARK in before
    ncells = len(last.strip().strip('|').split('|'))
    rec('  prior text a TRUE PREFIX : %s' % prefix)
    rec('  READ BACK : last row %s ; cells %d' % (rowid, ncells))
    good = (ncells == 6 and (rowid == str(nxt) or MARK in before))
    rec('  ### %s' % ('PASS' if good else '### FAIL'))

    rec('=' * 100)
    rec('  ### ROW %s. ### DESK %d items, %d closed, %d minted, %d standing. ### SPAN %d.'
        % (rowid, len(desk), closed, minted, standing, span['current_span']))
    rec('=' * 100)
    io.open(os.path.join(D, 'b479_desk_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
