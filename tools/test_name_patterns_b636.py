# -*- coding: utf-8 -*-
"""test_name_patterns_b636.py -- THE TEST OF tools/terminal_table.py's b636 EDIT, under (R246)(2)(ii): the generator's two name patterns
(NAME_RE, PRINT_SRC) read Lean identifiers as Lean does -- Unicode letters, subscripts, primes, the ₀ and ζ of the names that failed.

### The thirteen names of relay data/b635_phantom_names.json, read at SIDE-explicit-formula v0.25 (8c51431) by git; nothing is written.
###   (1) each of the thirteen `#print axioms` lines, read from its AxiomCheck file at the pin by its banked line, gives its full name
###       to PRINT_SRC (the twelve truncations their full form, LSeries_eq_mul_integral itself);
###   (2) the control: the ASCII PRINT_SRC of relay be879893 (the pattern before this edit) gives the twelve truncated heads, as b635 found;
###   (3) NAME_RE reads each of the thirteen full names whole from a backticked span on a ledger-shaped line;
###   (4) the control: the ASCII NAME_RE of be879893 reads none of the twelve full forms;
###   (5) the generator's own print reader (prints_at) at the pin carries all thirteen full names and none of the twelve heads;
###   (6) Lean's identifier characters: ζ and Greek letters, ₀ ₁ ᵢ subscripts, primes, ! and ?, ℝ and 𝔼 read inside a name;
###   (7) Lean's exclusions: λ, Π and Σ end a name (keywords in Lean), as do a space, `+` and `(`; a span holding them is no name.
### Usage: python tools/test_name_patterns_b636.py
"""
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import terminal_table as TT   # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
NL = chr(10)
KER, PIN = 'D:/SIDE-explicit-formula', '8c51431ada7798c65fa26b07ef99a447d7c15735'
# ### the two patterns as committed at relay be879893 (tools/terminal_table.py :52-:53), before this edit -- the controls
OLD_NAME = re.compile(r'`([A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*)`')
OLD_PRINT = re.compile(r'^[ \t]*#print[ \t]+axioms[ \t]+([A-Za-z_][A-Za-z0-9_.\u2019\']*)', re.M)


def blob(path):
    r = subprocess.run(['git', '-C', KER, 'show', '%s:%s' % (PIN, path)], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if r.returncode == 0 else None


def main():
    j = json.load(open(os.path.join(ROOT, 'data', 'b635_phantom_names.json'), encoding='utf-8'))
    names = [(x['name'], x.get('full') or x['name'], x['source']) for x in j['names']]
    trunc = [(h, f) for h, f, _ in names if f != h]
    res = []

    def want(label, cond):
        res.append(bool(cond))
        print('  %-110s %s' % (label, 'PASS' if cond else '### FAIL'))

    got_new, got_old = [], []
    for head, full, src in names:
        f, ln = src.split(' :')
        line = (blob(f) or '').split(NL)[int(ln) - 1]
        m, mo = TT.PRINT_SRC.search(line), OLD_PRINT.search(line)
        got_new.append((full, m.group(1) if m else None))
        got_old.append((head, mo.group(1) if mo else None))
    bad = [x for x in got_new if x[0] != x[1]]
    want('(1) the thirteen print lines read whole by PRINT_SRC: %d of %d %s' % (len(names) - len(bad), len(names), bad or ''), len(names) == 13 and not bad)
    old_ok = [x for x in got_old if x[0] == x[1]]
    want('(2) control, the ASCII PRINT_SRC: %d of 13 give the banked head (the twelve cut, LSeries whole)' % len(old_ok), len(old_ok) == 13)
    nr = [(full, [m.group(1) for m in TT.NAME_RE.finditer('| `%s` | DERIVES |' % full)]) for _h, full, _s in names]
    want('(3) NAME_RE reads the thirteen full names whole: %d of 13' % sum(1 for f, g in nr if g == [f]), all(g == [f] for f, g in nr))
    no = [f for _h, f in trunc if OLD_NAME.findall('`%s`' % f)]
    want('(4) control, the ASCII NAME_RE: reads %d of the twelve full forms' % len(no), len(trunc) == 12 and not no)
    _files, src, _out = TT.prints_at(KER, PIN)
    fulls, heads = [f for _h, f, _s in names], [h for h, _f in trunc]
    want('(5) prints_at at the pin: %d of 13 full names present, %d of 12 heads present' % (sum(f in src for f in fulls), sum(h in src for h in heads)),
         all(f in src for f in fulls) and not any(h in src for h in heads))
    ok6 = ['zeta_ζ_bound', 'Λ_Ω.αβ', 'x₀', 'L₁_nonneg', 'aᵢ', "f''", 'mem_iff!', 'isOk?', 'Gammaℝ_one', 'exp_𝔼']
    g6 = [(s, TT.NAME_RE.findall('`%s`' % s)) for s in ok6]
    want('(6) Lean identifier characters read: %s' % [s for s, g in g6 if g == [s]], all(g == [s] for s, g in g6))
    bad7 = ['fooλ', 'Πx', 'aΣb', 'a b', 'a+b', 'f(x)']
    g7 = [(s, TT.NAME_RE.findall('`%s`' % s)) for s in bad7]
    want('(7) Lean exclusions end a name, the span no name: %s' % [s for s, g in g7 if g], not any(g for _s, g in g7))
    n = sum(res)
    print('### ### **%d of %d cases as wanted -- %s**' % (n, len(res), 'PASS' if n == len(res) else 'FAIL'))
    return 0 if n == len(res) else 1


if __name__ == '__main__':
    sys.exit(main())
