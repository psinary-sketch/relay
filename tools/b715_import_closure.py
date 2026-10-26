# -*- coding: utf-8 -*-
"""b715_import_closure.py -- THE STANDING TOOLSET'S SIZE, MEASURED (the author's word (1)(d), relay data/b715_author_words_preseal.txt): the
transitive set of tools/*.py modules b714's fourteen close tools import, each with its line count and its act-literal count (the pattern
\\bb\\d{3}\\b over the whole source, comments and docstrings counted), banked as data/b715_import_closure.txt. The scratchpad probe of
data/b715_records.txt (4) carried into relay's tools/ beside the toolset, its walk and its counts unchanged, run once more here; its foot is
read against the record's figures (197 modules, 166 act-named, 31 shared, 134978 lines, 12883 literals) and printed EQUAL or DIFFERS.
Written whole by the Write tool at b715. Route: `bank` (the one write, through the membrane) or `dry` (prints, writes nothing).
"""
import os
import re
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
sys.path.insert(0, T)
NL = chr(10)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

SEEDS = ['b714_worklist', 'b714_record', 'b714_checks', 'b714_closing', 'b714_citation', 'b714_tests', 'b714_standing',
         'b714_corrigendum', 'b714_regspec', 'b714_reg_gate', 'b714_report', 'b714_hook', 'b714_repairs', 'b714_carry']
IMP = re.compile(r'^\s*(?:import|from)\s+([A-Za-z_][A-Za-z0-9_]*)', re.M)
LIT = re.compile(r'\bb\d{3}\b')
RECORD = dict(modules=197, act=166, shared=31, lines=134978, literals=12883)   # ### data/b715_records.txt (4), the scratchpad run


def src(m):
    p = os.path.join(T, m + '.py')
    return open(p, encoding='utf-8', errors='replace').read() if os.path.isfile(p) else None


def walk():
    seen, todo = {}, list(SEEDS)
    while todo:
        m = todo.pop()
        if m in seen:
            continue
        s = src(m)
        if s is None:
            continue
        seen[m] = s
        for n in IMP.findall(s):
            if n not in seen and os.path.isfile(os.path.join(T, n + '.py')):
                todo.append(n)
    return seen


def lines():
    seen = walk()
    act = sorted(m for m in seen if re.match(r'^b\d{3}_', m))
    shared = sorted(m for m in seen if not re.match(r'^b\d{3}_', m))
    got = dict(modules=len(seen), act=len(act), shared=len(shared), lines=sum(seen[m].count('\n') for m in seen),
               literals=sum(len(LIT.findall(seen[m])) for m in seen))
    L = ['b715 -- THE STANDING TOOLSET`S SIZE: THE MODULES b714`S CLOSE IMPORTS, TRANSITIVELY, WITH LINES AND ACT LITERALS (%s)' %
         time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### rows are modules of relay tools/, act-named first then shared, each: the module | lines (newlines counted) | act literals (the',
         '### pattern \\bb\\d{3}\\b over the whole source). The walk from b714`s fourteen tools: %s.' % ' '.join(SEEDS),
         '### Written by tools/b715_import_closure.py (the author`s word (1)(d)); the scratchpad probe`s walk and counts unchanged.', '']
    L += ['  %-34s | lines %6d | act literals %5d' % (m, seen[m].count('\n'), len(LIT.findall(seen[m]))) for m in act + shared]
    eq = ['%s %s %s' % (k, got[k], 'EQUAL' if got[k] == RECORD[k] else 'DIFFERS (the record %s)' % RECORD[k]) for k in RECORD]
    L += ['', '### against data/b715_records.txt (4), the scratchpad run: ' + ' ; '.join(eq),
          '', '### ### **MODULES %d (ACT-NAMED %d, SHARED %d) ; LINES %d ; ACT LITERALS %d ; AGAINST THE RECORD %s.**' % (
              got['modules'], got['act'], got['shared'], got['lines'], got['literals'],
              'EQUAL' if all(got[k] == RECORD[k] for k in RECORD) else 'DIFFERS')]
    return L


def main(route):
    L = lines()
    if route == 'bank':
        import act_membrane as MEM
        import b715_record as REC
        p = os.path.join(D, 'b715_import_closure.txt')
        MEM.guard_path('b715', p, REC.R.ROOT_EXCLUDE)
        with open(p + '.tmp', 'wb') as fh:
            fh.write((NL.join(L) + NL).encode('utf-8'))
        os.replace(p + '.tmp', p)
    print(NL.join(L[-3:]))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'dry')
