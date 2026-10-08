# -*- coding: utf-8 -*-
"""test_premise_status.py -- tools/premise_status.py's five-status rule (b640, (R250)(3) as the author answered before b640's seal), one
planted head per outcome, the order between outcomes, and the domain-variable reader on planted binders. ### Writes nothing."""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import premise_status as PS  # noqa: E402

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

CASES = [
    ('a planted Mathlib predicate on a quantified variable in every row reads DOMAIN',
     dict(upstream=True, domain_vars=[['p'], ['p']], consumed=[], inline=[], standalone=[], cited=False), 'DOMAIN'),
    ('a planted structure built inline in a proof reads DISCHARGED',
     dict(upstream=False, domain_vars=[[]], consumed=[], inline=[{'file': 'X.lean', 'line': 1}], standalone=[], cited=False), 'DISCHARGED'),
    ('a planted head whose standalone construction a proof consumes reads DISCHARGED',
     dict(upstream=False, domain_vars=[[]], consumed=[{'name': 'h_holds'}], inline=[], standalone=[{'name': 'h_holds'}], cited=False), 'DISCHARGED'),
    ('a planted premise cited T1-lit in every field reads CITED',
     dict(upstream=False, domain_vars=[[]], consumed=[], inline=[], standalone=[], cited=True), 'CITED'),
    ('a planted head with a standalone construction nothing consumes reads WITNESSED',
     dict(upstream=False, domain_vars=[['c']], consumed=[], inline=[], standalone=[{'name': 'w'}], cited=False), 'WITNESSED'),
    ('a planted premise constructed in salt checks alone reads OPEN',
     dict(upstream=False, domain_vars=[[]], consumed=[], inline=[], standalone=[], cited=False), 'OPEN'),
    ('a kernel predicate on a quantified variable is not DOMAIN (the answer: Mathlib`s alone)',
     dict(upstream=False, domain_vars=[['x']], consumed=[], inline=[], standalone=[], cited=False), 'OPEN'),
    ('a Mathlib predicate with one row on a fixed object is not DOMAIN',
     dict(upstream=True, domain_vars=[['p'], []], consumed=[], inline=[{'file': 'Y.lean', 'line': 2}], standalone=[], cited=False), 'DISCHARGED'),
]


def main():
    ok = 0
    n = 0
    for i, (label, f, want) in enumerate(CASES, 1):
        got = PS.classify5(f)[0]
        n += 1
        ok += got == want
        print('  (%d) %-90s wanted %s ; got %s ; %s' % (i, label, want, got, 'PASS' if got == want else 'FAIL'))
    binders = [{'name': 'p'}, {'name': 'hp'}]
    for k, (ty, want) in enumerate(((['p.Prime'], ['p']), (['Nat.Prime p'], ['p']), (['Nat.Prime 3'], []))):
        n += 1
        got = PS.domain_vars('Prime', '', [{'type': ty[0]}], binders)
        ok += got == want
        print('  (%d) %-90s wanted %s ; got %s ; %s' % (len(CASES) + k + 1, 'the domain reader on %r' % ty[0], want, got, 'PASS' if got == want else 'FAIL'))
    print('### ### **%d of %d cases as wanted -- %s**' % (ok, n, 'PASS' if ok == n else 'FAIL'))
    return 0 if ok == n else 1


if __name__ == '__main__':
    sys.exit(main())
