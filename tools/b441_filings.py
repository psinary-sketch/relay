# -*- coding: utf-8 -*-
"""b441_filings.py -- THE FILINGS. ### **GENERATED FROM THIS ACT'S RECORDS, NEVER TYPED FROM A RUN.**

### ### (1) `FACES_LEDGER.md` -- ONE UPDATE BLOCK through the writer's `append_block`, naming row `S1`,
### constituent `K5`: the identification in two halves at their own grades, and the pole's double role.
### ### **EVERY QUOTATION IS PASSED TO THE WRITER'S `verify_quotes` FIRST; ANY MISS AND NOTHING IS
### APPENDED** (face, section (S)).
### ### (2) `TECHNE-Core/modules/2026-09/AXIOM_PROFILE_IS_PARTLY_FORM.md` -- written and committed
### LOCALLY. ### **NO PUSH.**
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b327_faces_row as W  # noqa: E402

D = os.path.join(ROOT, 'data')
T = os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TECHNE = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
MOD_REL = 'modules/2026-09/AXIOM_PROFILE_IS_PARTLY_FORM.md'
MARK = '<!-- b441 update -->'
RUN = os.path.join(D, 'b441_filings_run.txt')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def git(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True)
    return r.returncode, (r.stdout or b'').decode('utf-8', 'replace') + (r.stderr or b'').decode(
        'utf-8', 'replace')


def main():
    rec('=' * 100)
    rec('b441_filings.py -- THE LEDGER BLOCK THROUGH THE WRITER; THE TECHNE MODULE, LOCAL.')
    rec('=' * 100)
    routes = json.load(io.open(os.path.join(D, 'b441_routes.json'), encoding='utf-8'))
    price = json.load(io.open(os.path.join(D, 'b441_price.json'), encoding='utf-8'))
    if not (routes.get('tol1_met') and routes.get('tol2_met')):
        rec('  ### A TOLERANCE WAS NOT MET -- the counting half is ONE ROUTE and this tool refuses to file')
        rec('  ### it as two. ### NOTHING WRITTEN.')
        io.open(RUN, 'w', encoding='utf-8', newline=NL).write(NL.join(LINES) + NL)
        return 1
    r1000 = [r for r in routes['rows'] if r['T'] == 1000][0]

    CC = os.path.join(D, 'b328_source_text.txt')
    B440 = os.path.join(D, 'b440_components.txt')
    B441 = os.path.join(D, 'b441_components.txt')
    quotes = [
        (CC, 'It is the derivative of 2', False),
        (os.path.join(PP, 'SPIRAL_MAP.md'), 'its `W` is a prime-power COUNTING FUNCTION', False),
        (B440, 'THE LAWFULNESS CONDITION `h-hat(i/2) = 0`', False),
        (B440, 'THE `1` IS THE POLE OF ZETA AT `s = 1`', False),
        (B440, 'IT IS EXACTLY `(1 + 1/c) / 2`', False),
        (B441, 'TOLERANCE 1 : MET. ### TOLERANCE 2 : MET.', False),
        (os.path.join(T, 'b317_smear.py'), 'test function is the single condition', False),
    ]
    miss = W.verify_quotes(quotes)
    rec('  quotations passed to the writer`s verify_quotes : %d ; misses : %d %s'
        % (len(quotes), len(miss), miss or ''))
    if miss:
        rec('  ### **NOT FILED** -- section (S). ### NOTHING APPENDED.')
        io.open(RUN, 'w', encoding='utf-8', newline=NL).write(NL.join(LINES) + NL)
        return 1

    body = [
        MARK, '',
        '## UPDATE — filed 2026-09-12 (b441): row S1, constituent K5 only — the archimedean channel identified as the smooth zero-ordinate density',
        '',
        '*Rows above are never rewritten; an update names the row and the constituent it bears on. Written through the writer’s `append_block`, every quotation verified first by the writer’s `verify_quotes`. No row is written, no cell of the register, and the freeze at six stands.*',
        '',
        '| the half | what it says | its grade, and where it comes from |',
        '|:--|:--|:--|',
        '| **the kernel half** | the channel’s kernel is twice the derivative of the Riemann–Siegel angular function, so the integrated channel `INT_0^T h+/(2 pi)` equals `theta(T)/pi` | **CARRIED, NOT NEW** — the verified source’s own words, *"It is the derivative of 2 θpτq, where θ is the Riemann-Siegel angular function"* (CC (153)–(154), relay `data/b328_source_text.txt`), quoted by b333’s survey and under K5’s existing DERIVES-ON-IMPORTS; checked numerically at b441 by two routes sharing no code, agreeing within `1e-12` at six heights |',
        '| **the counting half** | the Riemann–von Mangoldt main term minus `theta(T)/pi` is `1 - 1/(48 pi T) + O(T^-3)`; **the `1` is the pole of zeta at `s = 1`** | **MEASURED, not a theorem of this record** — route A `mpmath.quad` over `digamma`, route B `loggamma` with no quadrature; the deficit times `48 pi T` reads `%s` at `T = 1000`, within the stated `1e-6`, against a floor set by the `O(T^-3)` term; absent from PLACE-papers prose, relay’s banks, and both verified sources before b441 |' % r1000['scaled'][:12],
        '| **the pole’s double role** | the aim’s second moment condition is the lawfulness condition, which is the requirement that the test function not register the pole; that pole is the constant separating the integrated channel from the counting formula; and the same condition is what breaks the seed family’s self-similarity, by exactly `(1 + 1/c)/2` | **a juxtaposition of three graded lines, no mechanism claimed** — READ (the instrument’s eq. (54)); MEASURED (the counting half above); MEASURED at b439 with the factor derived at b440 and checked to nine figures |',
        '',
        '*What the identification does not do, stated so it is not over-read: it changes neither of site (ii)’s failing steps. `B3` stands at S2 — the identified channel contains no zero’s real part and is density-register by construction. `B5` stands at S3 — the uniform counting statements the verified sources give (Lagarias Theorem 2.1(4) and its unit-interval consequence) are counts, and a count uniform in the height places no zero. Of the five statements priced, %s: exact at every height, %s; uniform only in the O-sense for large height, %s; and for %s the source states no domain in the quoted text.*' % (len(price['candidates']), ', '.join(price['exact']) or 'none', ', '.join(c['id'] for c in price['candidates'] if 'O-SENSE' in c['uniformity']) or 'none', ', '.join(c['id'] for c in price['candidates'] if 'NOT STATED' in c['uniformity']) or 'none'),
        '',
        '*And `SPIRAL_MAP.md:114`, which b440’s prose called a denial, is left unedited: it disclaims any relation between `SIDE-window`’s prime-power counting function and `W_2`/`W_∞` — a true statement about a name collision — and says nothing about zero-ordinates. The word *denial* was this seat’s, in b440’s components and closing; the navigator’s premise repeated it. No grade is conferred by a seat, no bridge is typed between sites, and nothing is claimed about `h2`. Filed by b441 (relay `data/b441_the_identification_filed.txt`).*',
    ]
    status, msg = W.append_block(MARK, body)
    rec('  FACES_LEDGER.md append_block : %s -- %s' % (status, msg))

    # ---------------------------------------------------------------- the TECHNE module
    mod = os.path.join(TECHNE, MOD_REL.replace('/', os.sep))
    text = MODULE
    if os.path.exists(mod):
        rec('  TECHNE module : ALREADY PRESENT, not rewritten')
    else:
        io.open(mod, 'w', encoding='utf-8', newline=NL).write(text)
        rc, out = git(TECHNE, 'add', MOD_REL)
        rc2, out2 = git(TECHNE, 'commit', '-q', '-m',
                        'AXIOM_PROFILE_IS_PARTLY_FORM.md -- an axiom profile is partly a property of '
                        'how a statement is written (b440, b441). LOCAL, NOT PUSHED.')
        rc3, head = git(TECHNE, 'log', '-1', '--format=%h %s')
        rc4, ahead = git(TECHNE, 'rev-list', '--count', 'origin/main..HEAD')
        rec('  TECHNE module written : %s ; add rc %d ; commit rc %d ; HEAD %s ; ahead of origin/main %s'
            % (MOD_REL, rc, rc2, head.strip()[:60], ahead.strip()))
    rec('  ### **NO PUSH OF TECHNE-Core.**')
    rec('=' * 100)
    io.open(RUN, 'w', encoding='utf-8', newline=NL).write(NL.join(LINES) + NL)
    return 0 if status == 'WRITTEN' or status == 'DUPLICATE' else 1


MODULE = """# AN AXIOM PROFILE IS PARTLY A PROPERTY OF HOW A STATEMENT IS WRITTEN

*Minted at b441, from b440's probes. Local; not pushed.*

## The species

A theorem's axiom profile is read as evidence about **what** it proves: a statement that depends on no
axioms is taken to be constructively clean, one that depends on `propext` and `Quot.sound` is taken
to lean on extensionality and quotients. **That reading is partly wrong.** The same content, written
in two forms, can carry two different profiles -- because the profile records the *lemmas the
elaborator chose to reach the statement as written*, and different phrasings route through
different library lemmas.

## The incident

**b440, two probes of one fact, in a vanilla Lean 4 kernel with no Mathlib and no Batteries.** The
fact: a natural number `n` is not among the prime powers strictly below `n`.

| the statement as written | `#print axioms` |
|---|---|
| `16 ∉ primePowersLT 16` | `[propext, Quot.sound]` |
| `(primePowersLT 16).elem 16 = false` | no axioms at all |
| `primePowersLT 16 = [2, 3, 4, 5, 7, 8, 9, 11, 13]` | no axioms at all |

Both were closed by `decide`. The propositional membership form routes through library lemmas about
`List.Mem`, and those carry the two axioms; the decidable-equality form closes by reduction alone.
A positive control -- `(primePowersLT 17).elem 16 = true`, also axiom-free -- showed the equational
arm can answer both ways.

## Where it stands beside the grades

The record grades a cited terminal by reading its **statement** against a **named claim** --
`DERIVES`, `INTERFACES`, `ENCODES-CONCLUSION / SHELL`, and, since b433, `NOT THE CLAIM` (so the
grades now number four, not three) -- and records its axiom profile **separately**, at fixed
shorthands, never rounded up. The grades already say that a profile says nothing about whether a
statement matches its claim. **This species says a second thing the grades do not: a profile does
not even belong to the content alone.** It belongs to the content *as phrased*.

## What it implies for reading a profile as evidence

1. **A profile certifies the terminal, not the fact.** "The fact is axiom-free" is not established by
   one phrasing's profile; "this terminal is axiom-free" is.
2. **A dirtier profile is not evidence of a stronger dependence.** `[propext, Quot.sound]` on one form
   and none on another means the fact never needed them. Before reading a profile as a finding about
   the mathematics, try the equational or `Bool` phrasing and print both.
3. **A cleaner profile is not evidence of a weaker claim.** The two forms above state the same thing.
4. **A repository's standard is met by its statements, not its facts.** A kernel that promises "no
   axioms at all" must phrase every terminal in a form that meets it, and a natural propositional
   phrasing can silently fail the standard it was written to meet.
5. **So a profile is read like any other output: as a property of the object printed, never extended
   to a neighbouring object it resembles.**

## Provenance

relay `data/b440_components.txt` (the probe output, quoted there including its failure text);
relay `data/b440_kernel_attempt.json` (the profiles, parsed from the output); `PLACE-papers/README.md`
(the grades and the axiom shorthands). The general observation that library lemmas carry `propext`
while equation lemmas are clean was first banked at b418.
"""


if __name__ == '__main__':
    sys.exit(main())
