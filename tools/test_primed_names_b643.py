# -*- coding: utf-8 -*-
"""test_primed_names_b643.py -- (R253)(3)(b): THE TEXTUAL READER LEXES A PRIMED IDENTIFIER AS LEAN DOES.

### tools/terminal_table.py resolves a row's statement through b378_terminals.decl_re (imported, not copied), which ended a name with
### `\\b`: after a final `'` no word boundary falls before a space, so dedekind_rhs', TrivialSummandPremise' and
### trivialSummandPremise'_witness' were never found (relay data/b642_table.txt), and `\\b` after an unprimed name falls before a `'`, so
### dedekind_rhs could resolve to dedekind_rhs'. The planted lines test both directions; the live arm resolves the three rows at
### SIDE-explicit-formula main through terminal_table.statement.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b378_terminals as B  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

EF = 'D:/SIDE-explicit-formula'
PRIMED = ("SIDEExplicitFormula.Schema.Dedekind.dedekind_rhs'", "SIDEExplicitFormula.Schema.Dedekind.TrivialSummandPremise'",
          "SIDEExplicitFormula.SaltCheckNonvacuity.trivialSummandPremise'_witness'")


def m(last, line):
    return B.decl_re(last).search(line) is not None


def live():
    import terminal_table as TT
    return all(TT.statement(EF, 'main', n) is not None for n in PRIMED)


CASES = [
    ("dedekind_rhs' found at `theorem dedekind_rhs' (q : ℕ)`", lambda: m("dedekind_rhs'", "theorem dedekind_rhs' (q : ℕ) [NeZero q]")),
    ("TrivialSummandPremise' found at `def TrivialSummandPremise' (k : ℝ → ℂ)`",
     lambda: m("TrivialSummandPremise'", "def TrivialSummandPremise' (k : ℝ → ℂ) : Prop :=")),
    ("trivialSummandPremise'_witness' found at its theorem line, the name ending in a prime before a colon",
     lambda: m("trivialSummandPremise'_witness'", "theorem trivialSummandPremise'_witness' : Schema.Dedekind.TrivialSummandPremise' (fun _ => 1) :=")),
    ("the unprimed dedekind_rhs found at its own line", lambda: m("dedekind_rhs", "theorem dedekind_rhs (hT : TrivialSummandPremise) (hE : EulerFactorPremise q) (k : ℝ → ℂ) :")),
    ("CONTROL: the unprimed dedekind_rhs NOT found at dedekind_rhs'`s line", lambda: not m("dedekind_rhs", "theorem dedekind_rhs' (q : ℕ) [NeZero q]")),
    ("CONTROL: foo NOT found at a subscripted foo₁", lambda: not m("foo", "theorem foo₁ : True := trivial")),
    ("CONTROL: foo NOT found at foo_bar", lambda: not m("foo", "theorem foo_bar : True := trivial")),
    ("the three primed rows resolve at SIDE-explicit-formula main through terminal_table.statement", live),
]


def main():
    ok = 0
    for i, (name, f) in enumerate(CASES, 1):
        try:
            r = bool(f())
        except Exception as e:
            r = False
            name += ' (raised %s)' % type(e).__name__
        ok += r
        print('  (%d) %-110s %s' % (i, name, 'PASS' if r else '### FAIL'))
    print('### ### **%d of %d cases as wanted -- %s**' % (ok, len(CASES), 'PASS' if ok == len(CASES) else 'FAIL'))
    return 0 if ok == len(CASES) else 1


if __name__ == '__main__':
    sys.exit(main())
