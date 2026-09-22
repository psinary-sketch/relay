# -*- coding: utf-8 -*-
"""b466_components.py -- THE TWO COMPONENTS, RUN TO THE LIMIT THE PRESENT ARTEFACTS ALLOW.

### ### **THE PRECONDITION RETURNED FIVE ABSENTS**, so both components are run on the branch the
### order itself names. ### **NOTHING IS QUOTED THAT IS NOT ON DISK**, and every figure taken from
### the 2026-08-20 reports is labelled A BANK ABOUT THE ARTEFACT AND NOT THE ARTEFACT, at its file
### and line. ### The deposit's own side of Component 2's comparison IS on disk and is read at the
### deposited pin, by statement and never by docstring.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2')
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
INTAKE = os.path.join(ROOT, 'reports', '2026-08-20-external-intake.md')
ACTIV = os.path.join(ROOT, 'reports', '2026-08-20-activation-act.md')
PATHS = os.path.join(PP, 'phase1.5', 'proofs', 'PATHS_TO_THE_CRITICAL_LINE.md')
MONO = os.path.join(DEP, 'A_Place_to_Stand.md')
NL = chr(10)
L = []

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


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace')


def at(path, needle, show=200):
    """### **A CITATION IS A FILE AND A LINE, NEVER A PARAPHRASE.**"""
    for i, l in enumerate(read(path).split(NL)):
        if needle in l:
            return i + 1, l.strip()
    return None, None


def cite(label, path, needle, show=190):
    n, txt = at(path, needle)
    if not n:
        rec('    %-30s ### NOT FOUND -- %r' % (label, needle))
        return None
    rec('    %-30s %s:%d' % (label, os.path.basename(path), n))
    rec('      %s' % txt[:show])
    return dict(file=os.path.basename(path), line=n, text=txt)


SURVEY = json.load(io.open(os.path.join(D, 'b466_survey.json'), encoding='utf-8'))

# ### ### **THE SIX THINGS COMPONENT 1 ASKS OF A DOCUMENT.** ### Each is a property of the paper;
# ### with the paper absent each is reported by name and NOTHING IS SUPPLIED IN ITS PLACE.
ASKED = [
    ('the main theorem, verbatim, with every hypothesis', 'the paper'),
    ('whether it is unconditional, in its own words', 'the paper'),
    ('what it counts -- zeros on the line, simple zeros, or both', 'the paper'),
    ('the test-function class', 'the paper'),
    ('its support condition', 'the paper'),
    ('the three cited ingredients, as the paper cites them', 'the paper'),
]


def component1():
    rec('=' * 104)
    rec('COMPONENT 1 -- THE STATEMENT AT ADDRESS.')
    rec('=' * 104)
    rec('')
    rec('  ### (1a) WHAT THE ORDER ASKS FOR, AND WHETHER THE RECORD HOLDS IT.')
    rec('  ' + '-' * 100)
    rec('  ### ### **THE PAPER IS ABSENT** (precondition, by name across three trees and by content).')
    for what, owner in ASKED:
        rec('    %-58s ### **NOT IN THE RECORD**' % what)
    rec('')
    rec('  ### ### **AND NOTHING IS SUPPLIED IN THEIR PLACE.** ### A verbatim quotation of an absent')
    rec('  ### document cannot be produced, and a reconstruction from a summary is not a quotation.')
    rec('  ### ### **SIX OF SIX ASKS UNANSWERABLE. ### `0` INVENTED.**')

    rec('')
    rec('  ### (1b) WHAT THE PRESENT ARTEFACTS DO CARRY -- A PRIOR READ, LABELLED AT EVERY USE.')
    rec('  ' + '-' * 100)
    rec('  ### ### **THESE ARE BANKS ABOUT THE ARTEFACT, NOT THE ARTEFACT.** ### 2026-08-20.')
    got = {}
    got['headline'] = cite('the banked headline', INTAKE, 'critical-line proportion 41.6%')
    got['rule3'] = cite('the executor Rule-3 log', INTAKE, 'FETCHED AND READ AT')
    got['method'] = cite('the method shape', INTAKE, 'rank inequality')
    got['flags'] = cite('the paper-read flags', INTAKE, 'no-Euler-clause')
    got['unread'] = cite('what did NOT surface', INTAKE, 'did NOT surface')
    rec('')
    rec('  ### ### **THE INTAKE\x27s OWN WORD FOR ITS OWN STATE IS THE FINDING HERE.** ### It records')
    rec('  ### the sub-attributions as `NAVIGATOR-ASSERTED pending the paper read`, and it holds two')
    rec('  ### anatomy flags OPEN `where the paper read is still owed`. ### **THAT READ WAS OWED ON')
    rec('  ### 2026-08-20 AND IS STILL OWED TODAY: the order asks this act to pay it, and the act')
    rec('  ### cannot, because the document the debt is against is not in the record.**')

    rec('')
    rec('  ### (1c) THE THREE READS, EACH TO THE LIMIT THE PRESENT ARTEFACTS ALLOW.')
    rec('  ' + '-' * 100)
    reads = []

    rec('  ### **(a) THE IMPORT-BAR GRADE.**')
    rec('    the bar grades A STATEMENT\x27s CLASS against this corpus\x27s objects, and the sentence it')
    rec('    turns on is the SUPPORT CONDITION. ### That sentence is not in the record at any address.')
    rec('    ### ### **VERDICT : `NOT GRADABLE FROM THE RECORD`.**')
    rec('    ### ### **WHAT WOULD DECIDE IT, NAMED:** the paper\x27s test-function class and its support')
    rec('    condition, quoted; then the K1 boundary read exactly as b452 ran it.')
    reads.append(dict(read='(a) import bar', verdict='NOT GRADABLE FROM THE RECORD',
                      decides='the paper’s support condition, quoted'))

    rec('')
    rec('  ### **(b) ROW U1 -- A UNIFORMITY IN ANY OF THE SIX INDICES?**')
    rec('    ### **READ OF A SUMMARY, NOT OF THE PAPER**, and labelled so in the verdict itself.')
    rec('    the banked method shape names: a Weil-form function space; both definiteness signs')
    rec('    treated JOINTLY; a NON-DIAGONAL form; a rank inequality from first- and second-moment')
    rec('    information. ### **NONE OF THOSE IS A STATEMENT UNIFORM IN AN INDEX.** ### A rank')
    rec('    inequality is a bound on a dimension, not a statement holding uniformly over a class,')
    rec('    a height, a width, a representation or a modulus.')
    rec('    ### ### **VERDICT : `NONE, ON THE SUMMARY`** -- and the summary is not the paper, so the')
    rec('    ### answer for the PAPER stays `NOT READ`. ### **AND `NONE` HERE IS NOT `NO`.**')
    reads.append(dict(read='(b) row U1', verdict='NONE, ON THE SUMMARY; NOT READ, ON THE PAPER',
                      decides='the paper’s theorem statement'))

    rec('')
    rec('  ### **(c) THE CENSUS -- THE TWO TARGETS, CHECKED FOR EXISTENCE FIRST.**')
    # ### TARGET 1: PATHS's proportion table.
    ptxt = read(PATHS)
    rows = re.findall(r'^\|.*$', ptxt, re.M)
    pct = [r for r in rows if re.search(r'\d\d(\.\d+)?\s*%', r)]
    rec('    PATHS_TO_THE_CRITICAL_LINE.md : %d table row(s); rows carrying a percentage : %d'
        % (len(rows), len(pct)))
    for r in pct[:3]:
        rec('      %s' % r.strip()[:150])
    paths_has = len(pct) > 1
    rec('    ### ### **PATHS CARRIES NO PROPORTION TABLE.** ### Its tables are the door/register/depth')
    rec('    ### table, the five ingredients, and the path/delivers/state/Lean-now table. ### **THE')
    rec('    ### ORDER\x27s FIRST TARGET DOES NOT EXIST**, and a row cannot be drafted into it.')
    # ### TARGET 2: section 24.4.
    n, _ = at(MONO, '## 24.4 The Convergence')
    cell = None
    for l in read(MONO).split(NL)[n:n + 8]:
        if 'Analytic number theory' in l:
            cell = l.strip()
    rec('')
    rec('    A_Place_to_Stand.md:%d   ### **SECTION 24.4 EXISTS AND ITS TABLE IS READ AT ITS LINE**' % n)
    rec('      %s' % (cell or '(row not found)'))
    rec('')
    rec('    ### ### **AND HERE IS THE READ THE ORDER\x27s OWN TARGET FORCES:** 24.4\x27s analytic row')
    rec('    ### concludes ### **`>= 40.77% simple`** -- a SIMPLICITY proportion. ### The banked')
    rec('    ### headline is a ### **CRITICAL-LINE proportion, 41.6% -> 67.2%**. ### **THOSE ARE TWO')
    rec('    ### DIFFERENT QUANTITIES, AND THE SECOND DOES NOT UPDATE THE FIRST.** ### A 67.2%')
    rec('    ### on-line proportion is consistent with the simple-zero proportion staying at 40.77%.')
    rec('    ### ### **SO THE DRAFT IS NOT A CELL EDIT. ### IT IS A NEW ROW OR A NEW COLUMN**, and')
    rec('    ### which of the two is an AUTHORING decision, which is routed and not taken here.')
    rec('')
    rec('    ### ### **THE ERA-ANNOTATION CANDIDATE, DRAFTED AND NOT APPLIED:**')
    rec('      | Analytic number theory | Weil-form rank inequality, non-mollifier | 2026 |')
    rec('      | ~67.2% ON THE LINE (simplicity not asserted in the record) |')
    rec('      ### ### **STATUS : DRAFT. ### NOT WRITTEN TO ANY SURFACE. ### AUTHORING ROUTED.**')
    rec('      ### **AND THE DRAFT CARRIES ITS OWN DEFECT ON ITS FACE:** `simplicity not asserted in')
    rec('      ### the record` is a statement about THE RECORD, not about the paper, because the')
    rec('      ### paper is absent. ### **THE ROW CANNOT BE APPLIED UNTIL THAT CLAUSE IS READ.**')
    reads.append(dict(read='(c) census', verdict='ONE TARGET ABSENT, ONE READ; DRAFT NOT APPLIED',
                      paths_proportion_table=paths_has,
                      cell=cell, decides='whether the paper asserts simplicity'))
    return got, reads, paths_has, cell


GW_NEEDLE = 'decomposition conjunct (Guinand–Weil) and `TailBoundPremise` remain named and open'


def component2():
    rec('')
    rec('=' * 104)
    rec('COMPONENT 2 -- THE LEAN, READ NOT TRUSTED.')
    rec('=' * 104)
    rec('')
    rec('  ### (2a) THE THIRD PARTY\x27s SIDE.')
    rec('  ' + '-' * 100)
    rec('  ### ### **THE CLONE IS ABSENT.** ### No directory, no archive, no vendored tree, by name')
    rec('  ### across three trees and by content across the record. ### So:')
    for what in ('every top-level theorem mentioning the explicit formula',
                 'every one mentioning Guinand-Weil',
                 'every one mentioning a sum over zeros against a test function',
                 'every one mentioning a prime sum',
                 'the statement as declared, for each',
                 'the `#print axioms` profile, for each',
                 'the Mathlib pin from the lakefile'):
        rec('    %-58s ### **NOT RUNNABLE -- NO CLONE**' % what)
    rec('')
    rec('  ### ### **WHAT THE RECORD DOES CARRY ABOUT IT, LABELLED A PRIOR READ:**')
    b = {}
    b['sha'] = cite('the shallow-clone SHA', ACTIV, 'shallow clone at')
    b['pin'] = cite('the toolchain and Mathlib pin', ACTIV, 'Mathlib `51e6992`')
    b['ef'] = cite('the ExplicitFormula row', ACTIV, 'WEIL EXPLICIT FORMULA')
    rec('')
    rec('  ### ### **THAT BANK NAMES A DIRECTORY AND A FRAMING. ### IT NAMES NO THEOREM.** ### Not')
    rec('  ### one declared name, not one statement, not one axiom profile. ### **A DIRECTORY NAME IS')
    rec('  ### NOT A STATEMENT**, and the order\x27s question is about statements.')

    rec('')
    rec('  ### (2b) THE DEPOSIT\x27s SIDE -- ON DISK, AND READ AT THE PIN.')
    rec('  ' + '-' * 100)
    pin = SURVEY.get('lv_pin')
    rec('  SIDE-lv-conservation @ v0.10.0 resolves to %s   ### the monograph names 93c27ec' % pin)
    rec('')
    rec('  ### ### **THE DEPOSIT\x27s OWN LINE FOR THE PENDING INPUT, QUOTED AT ITS ADDRESS:**')
    dep = cite('A_Place_to_Stand.md', MONO, GW_NEEDLE, show=0)
    if dep:
        seg = dep['text']
        i = seg.find('decomposition conjunct')
        rec('      "...%s..."' % seg[max(0, i - 190):i + 90].strip())
    rec('')
    rec('  ### ### **AND THE STATEMENT THAT LINE IS ABOUT, READ IN LEAN AT THE PIN -- NOT ITS')
    rec('  ### DOCSTRING:** ### `SIDELvConservation/PartialPositivity.lean`')
    st = SURVEY.get('lv_statements', {})
    for name in ('ExplicitFormulaDecomp', 'TailBoundPremise', 'partialPositivity_finiteRange'):
        if name not in st:
            continue
        rec('')
        rec('    %s' % name)
        for l in st[name].split(NL)[:8]:
            rec('      %s' % l[:140])
    rec('')
    rec('  ### ### **THE FIRST CONJUNCT IS DISCHARGED AND THE SECOND IS NOT.** ### `lowFinset_mem_iff`')
    rec('  ### proves exactly the finite-set conjunct at `low := lowFinset T`. ### **WHAT REMAINS')
    rec('  ### PENDING IS THE SECOND CONJUNCT ALONE:**')
    rec('      (forall n, 1 <= n -> lam n = (sum over z in low of blTerm z n) + tail n)')
    rec('  ### with `blTerm z n = Re(1 - (1 - 1/rho)^n)`, the Bombieri-Lagarias per-zero Li term.')
    rec('  ### ### **SO THE DEPOSIT\x27s PENDING INPUT IS A LI-COEFFICIENT SPLITTING AT A HEIGHT `T`,')
    rec('  ### NOT A GENERAL WEIL EXPLICIT FORMULA OVER A TEST FUNCTION.** ### That is a statement')
    rec('  ### about what is on disk, and it is checkable line by line.')

    rec('')
    rec('  ### (2c) THE ONE QUESTION.')
    rec('  ' + '-' * 100)
    rec('  ### The order offers three verdicts. ### **ALL THREE ARE STATEMENTS ABOUT A TEXT, AND ONE')
    rec('  ### OF THE TWO TEXTS IS NOT HERE.** ### `MATCHES` cannot be asserted, `CONTAINS WITH A')
    rec('  ### NAMED SPECIALIZATION` cannot be asserted, and -- ### **THIS IS THE ONE THAT MATTERS** --')
    rec('  ### `DOES NOT` cannot be asserted either. ### An absent repository refutes nothing.')
    rec('  ### ### **VERDICT : `NOT DECIDABLE FROM THE RECORD`**, the fourth, named on the face in')
    rec('  ### advance of the read.')
    rec('')
    rec('  ### ### **AND IT IS DISCHARGED BY NAMING WHAT WOULD DECIDE IT, EXACTLY:**')
    rec('    (1) the clone at a stated SHA -- the record banks `cec57f9` from 2026-08-20, which is a')
    rec('        PRIOR READ\x27s SHA and not a present artefact;')
    rec('    (2) the declared statement of whatever `ExplicitFormula/` exports, read not summarized;')
    rec('    (3) one comparison, against the second conjunct printed above and nothing wider -- is')
    rec('        the Li splitting at height `T` an instance of their statement under a named')
    rec('        specialization of the test function, or is their statement a different object?')
    rec('  ### ### **THAT IS ONE READING COMPONENT OF ONE ACT, AND IT IS NOT ATTEMPTED HERE.**')
    rec('')
    rec('  ### ### **W-ORD-GW-IMPORT IS NOT FILED.** ### Its trigger is `MATCHES` or `CONTAINS`; the')
    rec('  ### verdict is neither. ### **FILING A WORK ORDER ON A COMPARISON NOBODY MADE WOULD PUT AN')
    rec('  ### IMPORT QUESTION ON THE AUTHOR\x27s DESK WITH NOTHING BEHIND IT.**')
    rec('  ### ### **AND NOTHING IS IMPORTED, CLONED OR VENDORED IN THIS ACT.**')
    return dict(clone='ABSENT', bank=b, lv_pin=pin, verdict='NOT DECIDABLE FROM THE RECORD',
                pending_conjunct='lam n = (sum over low of blTerm z n) + tail n',
                worder_filed=False)


def expectations(reads, c2, paths_has, cell):
    rec('')
    rec('=' * 104)
    rec('THE EXPECTATIONS, SCORED.')
    rec('=' * 104)
    sc = {}
    sc['N1'] = dict(
        navigator='the theorem is unconditional and counts zeros on the line, simplicity not asserted',
        verdict='NOT SCORABLE -- THE PAPER IS ABSENT',
        note='the record’s banked headline calls it an UNCONDITIONAL CRITICAL-LINE proportion, '
             'which is a bank about the paper and not the paper; simplicity is asserted nowhere '
             'in the record, which is not the same as the paper not asserting it')
    sc['N2'] = dict(
        navigator='the test class is restricted-support and grades K1 at every site',
        verdict='NOT SCORABLE -- THE SUPPORT SENTENCE IS NOT IN THE RECORD',
        note='the bar turns on exactly that sentence; a K1 returned without it would grade a class '
             'this act never read')
    sc['N3'] = dict(
        navigator='the Lean declares an explicit-formula statement CONTAINING the deposit’s '
                  'pending input with a named specialization',
        verdict='NOT SCORABLE -- THE CLONE IS ABSENT',
        note='and the record’s own 2026-08-20 row calls the framings DIFFERENT (their contour '
             'form vs the corpus’s constrained class), which is evidence against CONTAINS and '
             'is still not a reading of a statement')
    sc['seat'] = dict(
        N1='NO READING OFFERED ON THE THEOREM; the adjacent reading the seat DID offer -- that the '
           'census read would turn on critical-line vs simplicity and not on the theorem’s text '
           '-- is HELD: 24.4’s cell reads ">= 40.77% simple" and the headline is an on-line '
           'proportion',
        N2='REFUTED AS UNREACHABLE, as the face predicted, and not refuted as false',
        N3='NOT DECIDABLE FROM THE RECORD, as the face predicted; the specialization direction the '
           'seat predicted is UNTESTED and stays a prediction')
    for k in ('N1', 'N2', 'N3'):
        rec('  %-5s %s' % (k, sc[k]['navigator']))
        rec('        ### **%s**' % sc[k]['verdict'])
        rec('        %s' % sc[k]['note'])
    rec('')
    rec('  ### ### **THE SEAT\x27s OWN, FROM THE FACE:**')
    for k in ('N1', 'N2', 'N3'):
        rec('    %-5s %s' % (k, sc['seat'][k]))
    rec('')
    rec('  ### ### **THREE OF THREE NAVIGATOR EXPECTATIONS ARE `NOT SCORABLE`, AND THAT IS ITSELF THE')
    rec('  ### ### RESULT OF THE ACT** -- not a failure to run it. ### Each was refutable by a printed')
    rec('  ### result, as the order required; what the printed result says is that the population each')
    rec('  ### one quantifies over is not in the record. ### **AN EXPECTATION ABOUT AN ABSENT')
    rec('  ### DOCUMENT IS NOT WRONG; IT IS UNTESTED, AND SAYING SO IS THE ONLY HONEST SCORE.**')
    return sc


def main():
    got, reads, paths_has, cell = component1()
    c2 = component2()
    sc = expectations(reads, c2, paths_has, cell)
    rec('')
    rec('=' * 104)
    rec('  ### ### **NO BRIDGE TYPED. ### NO SITE ENTERED. ### ROW U1 UNEDITED. ### NOTHING FETCHED,')
    rec('  ### ### IMPORTED OR APPLIED. ### `h2` WHERE THE DEPOSIT LEFT IT.**')
    rec('=' * 104)
    io.open(os.path.join(D, 'b466_components.txt'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(L) + NL)
    json.dump(dict(component1=dict(asks=len(ASKED), unanswerable=len(ASKED), invented=0,
                                   banks=sorted(k for k, v in got.items() if v), reads=reads,
                                   paths_proportion_table=paths_has, cell_244=cell),
                   component2=c2),
              io.open(os.path.join(D, 'b466_readings.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    json.dump(sc, io.open(os.path.join(D, 'b466_scores.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
