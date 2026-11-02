# -*- coding: utf-8 -*-
"""b736_e0landing.py -- (R346)(3)(ii), THE GRADER'S PRIVATE LEXICON: tools/b703's and tools/b735_ef.py's E0_EXTENSION landed in the shared tools/e0_rule.py, the three forms its control, the ζ and Dirichlet instances re-graded
unchanged. Each row graded through the rule at relay d4e0ea02 (b735's closing, the extension not in it) and through the rule at this tree. Controls before figures. Writes data/b736_e0_landing.txt.

  python -X utf8 -u tools/b736_e0landing.py [--bank]
"""
import importlib.util
import io
import os
import subprocess
import sys
import tempfile
import time

T = os.path.dirname(os.path.abspath(__file__))
RELAY = os.path.dirname(T)
EF, TIP, BASE = 'D:/SIDE-explicit-formula', 'b25fd82c', 'd4e0ea02'
EZ, MAIN = 'SIDEExplicitFormula/Schema/EpsteinZQ.lean', 'SIDEExplicitFormula/Schema/ZQ/EF/Main.lean'
LANDED = ((EZ, 'zq_count'), (EZ, 'zq_explicit_formula'), (EZ, 'zq_li_nonneg_imp_online'))
FORMS = ((MAIN, 'zq_count_instance'), (MAIN, 'zq_explicit_formula_instance'), (MAIN, 'zq_li_nonneg_imp_online_instance'))
OTHERS = (('Zeta23/WeilEF/Main.lean', 'EF_lit_zeta'), ('Zeta23/WeilEF/Main.lean', 'EF_lit_zetaZeroConfig'), ('SIDEExplicitFormula/Chi/Main.lean', 'EF_lit_chi_holds'),
          ('SIDEExplicitFormula/Chi/ZeroSummability.lean', 'EF_zero_sum_summable_chi'), ('SIDEExplicitFormula/Chi/LocalCount.lean', 'LFunction_zeros_finite_of_isCompact'))
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def show(rel):
    return subprocess.run(['git', '-C', EF, 'show', '%s:%s' % (TIP, rel)], capture_output=True, text=True, encoding='utf-8').stdout


def sig(src, name):
    L = src.split('\n')
    i = next(k for k, l in enumerate(L) if l.startswith('theorem %s ' % name))
    j = next(k for k in range(i, len(L)) if ':=' in L[k])
    return ' '.join('\n'.join(L[i:j + 1]).split('theorem %s' % name, 1)[1].split(':=', 1)[0].split())


def load(path, name):
    s = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(s)
    sys.modules[name] = m
    s.loader.exec_module(m)
    return m


def grade(E, head):
    try:
        g = E.grade(' ' + head + ' ', 'theorem')
        return g[0], g[1]
    except Exception as e:  # noqa: BLE001
        return 'RAISED', '%s: %s' % (type(e).__name__, str(e)[:90])


def main(argv):
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, 'e0_old.py')
        with open(p, 'wb') as f:
            f.write(subprocess.run(['git', '-C', RELAY, 'show', '%s:tools/e0_rule.py' % BASE], capture_output=True).stdout)
        old = load(p, 'e0_old')
        new = load(os.path.join(T, 'e0_rule.py'), 'e0_new')
        added = sorted(set(new.LEXICON) - set(old.LEXICON))
        moved = sorted(k for k in old.LEXICON if new.LEXICON.get(k) != old.LEXICON[k])
        L = ['b736 -- (R346)(3)(ii): THE E0 EXTENSION LANDED IN THE SHARED RULE (%s)' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
             '### through the rule at relay %s and at this tree; the statements read at SIDE-explicit-formula %s, the header to its `:=`.' % (BASE, TIP), '', '## THE CONTROLS, BEFORE ANY FIGURE']
        ok = True

        def ctl(what, c):
            nonlocal ok
            ok = ok and c
            L.append('  %-74s %s' % (what, 'AS WANTED' if c else 'NOT AS WANTED'))
        ctl('the rule`s own self_test at this tree, both polarities', new.self_test() is True)
        ctl('the entries added are the three and no other: %s' % added, added == ['WideConfig', 'ZQPremises', 'ZQZeros'])
        ctl('no entry of the rule moved: %s' % (moved or 'none'), not moved)
        ctl('MET unchanged', tuple(new.MET) == tuple(old.MET))
        L += ['', '## THE ROWS (the declaration | the rule at %s | the rule at this tree)' % BASE]
        srcs = {}
        for label, rows, want in (('THE THREE PREMISE-FREE FORMS, THE CONTROL', FORMS, 'equal'), ('THE ζ AND DIRICHLET INSTANCES', OTHERS, 'equal'), ('THE LANDED LINES', LANDED, 'read')):
            L.append('  ' + label)
            for rel, n in rows:
                h = sig(srcs.setdefault(rel, show(rel)), n)
                a, b = grade(old, h), grade(new, h)
                L.append('    %-38s %-12s %-12s %s' % (n, a[0], b[0], b[1][:90]))
                if want == 'equal':
                    ctl('%s unchanged' % n, a == b)
                else:
                    ctl('%s raised before and reads INTERFACES on h' % n, a[0] == 'RAISED' and b[0] == 'INTERFACES')
        L += ['', '### THE THREE FORMS READ DERIVES UNDER THE RULE AS IT STOOD: THE GRADE AT b735 DID NOT REST ON THE EXTENSION; THE LANDED LINES DID, THE RULE AS IT STOOD RAISING ON WideConfig.', '',
              '### ### **THE EXTENSION LANDED: %d ENTRIES ; %s.**' % (len(added), 'CONTROLS ALL AS WANTED' if ok else 'CONTROLS NOT ALL AS WANTED')]
    print('\n'.join(L))
    if '--bank' in argv:
        with io.open(os.path.join(RELAY, 'data', 'b736_e0_landing.txt'), 'w', encoding='utf-8', newline='\n') as f:
            f.write('\n'.join(L) + '\n')
        print('written data/b736_e0_landing.txt')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
