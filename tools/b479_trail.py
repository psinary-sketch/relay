# -*- coding: utf-8 -*-
"""b479_trail.py -- THE TRAIL RECORD, APPENDED. ### **APPEND-ONLY, BOM PRESERVED, PREFIX PROVED.**"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OT = os.path.join(PP, 'OPEN_TRAILS.md')
NL = chr(10)

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

R = json.load(io.open(os.path.join(D, 'b479_results.json'), encoding='utf-8'))
SPAN = json.load(io.open(os.path.join(D, 'b479_span.json'), encoding='utf-8'))

ENTRY = """
### b479 — the seven classes against the form, a read — filed 2026-09-22

**Of the seven mechanism classes, only two have statements that reach Weil's form.** *Re-issued under `(R96)`, after `b482` proved no banked ferry ever carried this act's order.*

#### What was read, and how

`SIDE-lv-conservation` at **`v0.10.0` = `93c27ec`**, by `git show`, **as text — nothing compiled**. `h1_complete_at_Phi` conjoins **eight** per-class facts for **seven** classes: `C7` contributes both `C7_entirety` and `C7_order`.

**The criterion, fixed on the sealed face before any verdict.** The order asks whether each fact *constrains Weil's form `W` on some family of test functions*, read from the **statement and not the docstring**. **Not one of the eight statements mentions a test function, `W`, or the explicit formula** — all eight are predicates on `Φ`. A literal reading would return seven `APART` and say nothing. So:

> **A fact touches the form when its statement constrains the object `W` is built from — the Mellin transform of `Φ` — on a family its own quantifier names.**

**Statements naming `mellin Φ (s/2)`: 3 of 8.**

#### The table

| | class | verdict |
|:--|:--|:--|
| **C1** | Schwarz reflection / realness | **APART** |
| **C2** | Euler / multiplicative | **TOUCHES THE FORM** |
| **C3** | functional equation / theta | **APART** |
| **C4** | modular / PSL₂(ℤ) | **APART** |
| **C5** | spectral | **APART** |
| **C6** | Cauchy–Riemann / analyticity | **APART** |
| **C7** | Hadamard | **TOUCHES THE FORM** |

**C2's constraining clause:** `∀ s : ℂ, 1 < s.re → mellin Φ (s / 2) ≠ 0` — the transform itself, constrained on a half-plane the statement's own quantifier names.

**C7's:** `G s = mellin Φ (s/2) + 1/s + 1/(1-s)` on `1 < s.re`, **with** `‖G s‖ ≤ C · exp (A · ‖s‖ · log (‖s‖+2))` on all of `ℂ`. The row is carried by **`C7_order`** — entirety alone does not give the bound, as the file's own docstring says.

**And the five that are apart, in their own words:** `C1` fixes an imaginary part of `Φ`; `C3` is an identity for `Φ` on the positive reals; `C4` constrains a function of `τ` on the upper half-plane; `C5_input` is a heat trace with a non-negative spectrum; `C6` extends `Φ` itself. **None names a transform.**

#### The sentence the table supports, and no wider

**Two of the seven — `C2` and `C7`.** The other five constrain `Φ` and not its transform, and their route to the form runs through derivations their statements do not carry. **That is a statement about what they say. It is not a claim that they are irrelevant to the form.**

**And one of the two is half open.** `C7`'s row rests on `C7_order`, which the file's own docstring marks **OPEN** — *"a Γ-asymptotics project, not a corollary of what exists."*

> *IF the exclusions that reach Weil's form were carried by `C2` and `C7` alone, then exhaustiveness over the seven classes would not be the operative claim: the operative claim would be that the form is **inert** to the other five — that `C1`, `C3`, `C4`, `C5` and `C6` leave `W` unmoved on every family of test functions. **And that inertia is not what the seven-class argument asserts**: it asserts that the five **supply** constraints, not that they leave the form free.*

**The conditional is not discharged.** The stem `inerti` is at no address in `FINDINGS.md` or `REGISTRY.md`, so the sentence uses the vocabulary the order names without claiming the record holds it. **This measures the formalisation's reach, not the argument's truth**, and this act makes no claim about the latter.

**And `h2` is quoted and not discharged** — `h1_complete_at_Phi`'s own docstring: *"`h2` (nonvanishing of the Mellin transform at the operative point) remains the outstanding obligation."*

#### The expectations

| | verdict |
|:--|:--|
| **(N1)** C2, C3 and C7 touch | **HELD IN PART** — C2 and C7 do; **C3 does not** |
| **(N2)** C1, C4 and C6 are apart | **HELD** |
| **(N3)** C5 touches only by the disclaimed register | **HELD — and the repository says it first**: *"NOTE: `C5_output` is deliberately NOT in `sevenClasses`: it is the disclaimed half."* |

#### Two things this act found in its own instruments

**A `def` and a `theorem` do not mean the same thing by `:=`.** The fact reader stopped at the first `:=` for both. For a theorem that is right — the proof follows. For `def C : Coupling := fun Φ => <predicate>` it is **wrong**: the `:=` is on the declaration line and **the predicate is the content**. The reader returned `def C2_halfplane_nonvanishing : Coupling` and reported **0** statements naming the transform where the true figure is **3** — a figure that decides two rows. **`(R70)`'s rehearsal on `C2` caught it before the seal**, which is exactly what a rehearsal on a known case is for.

**And step zero failed once.** The first pins run read `REPOS HARD-FAILING : 4` — all four `ls-remote` calls unresolved *at once*, which is the shape of a network blip, not four repository faults. A direct call immediately after returned the correct SHA. The retry reads **0 of 4, all `0/0`**, and **both runs are banked** — a gate that fired is evidence even when it fired on the weather.

#### What this act does not do

**Nothing is compiled and no kernel is built.** No grade moves, no bridge is typed, `C5_output` is not counted, row U1 is unedited, the four lists stay OPEN, no claim about RH in either direction.

**Both span readings, per `(R96)`:** the tool reads **{span}** by number order; the trail's own records give **{filed}** acts filed since the `b474` fold, **{filedplus}** with this one. **The tool is not edited.** The fold follows under `(R96)` and is not opened here.
"""

import json as _j
FILED = _j.load(io.open(os.path.join(D,'b479_filing.json'),encoding='utf-8'))
ENTRY = ENTRY.replace('{span}', str(SPAN['current_span'])).replace('{filed}', str(FILED['count'])).replace('{filedplus}', str(FILED['count']+1))


def main():
    before = io.open(OT, 'rb').read()
    tail = before.decode('utf-8-sig', 'replace')[-2:]
    sep = '' if tail.endswith(NL + NL) else (NL if tail.endswith(NL) else NL + NL)
    add = (sep + ENTRY.strip(NL) + NL).encode('utf-8')
    io.open(OT, 'ab').write(add)
    after = io.open(OT, 'rb').read()

    print('=' * 96)
    print('b479_trail.py -- THE TRAIL RECORD, APPENDED.')
    print('=' * 96)
    print('  bytes before        : %d' % len(before))
    print('  bytes appended      : %d' % len(add))
    print('  bytes after         : %d' % len(after))
    print('  BOM still present   : %s' % after.startswith(b'\xef\xbb\xbf'))
    print('  PRIOR BYTES A TRUE PREFIX : %s' % after.startswith(before))
    print('  arithmetic closes   : %s' % (len(after) == len(before) + len(add)))
    txt = after.decode('utf-8-sig', 'replace').replace(chr(13), '')
    heads = [l for l in txt.split(NL) if l.startswith('### b479 ')]
    print('  b479 headings in the file : %d ### -- PASS only on 1' % len(heads))
    ok = (after.startswith(before) and after.startswith(b'\xef\xbb\xbf')
          and len(after) == len(before) + len(add) and len(heads) == 1)
    print('  ### %s' % ('PASS' if ok else '### FAIL'))
    print('=' * 96)
    io.open(os.path.join(D, 'b479_trail_notes.txt'), 'w', encoding='utf-8', newline=NL).write(
        'before %d appended %d after %d prefix %s bom %s headings %d verdict %s%s'
        % (len(before), len(add), len(after), after.startswith(before),
           after.startswith(b'\xef\xbb\xbf'), len(heads), 'PASS' if ok else 'FAIL', NL))
    return 0 if ok else 2


if __name__ == '__main__':
    sys.exit(main())
