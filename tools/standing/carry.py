# -*- coding: utf-8 -*-
"""tools/standing/carry.py -- THE CARRY BY DIFF as a standing route (v1.4.0, (R334)(2)(ix)): a tool or sections file carried from the
previous act by the act names' substitution alone, its diff banked, and THE SUBSTITUTION REFUSED WHERE IT SHIFTS A NAME PAST WHAT EXISTS --
a module or tool the carried text names that tools/ lacks, where the source line named one that exists (b721 (p), b723 (d), b724 (d):
tools/b724_address_scan.py's `import b723_llm_line`, carried from b722_llm_line, which no act wrote). The refusal is before the write.

### carry.py <src_rel> <dst_rel> <name> --subs a:b,c:d,... [--shifted] [--again]
###   the pairs applied in the order given (descending, so each name shifts once); the diff banked in data/<act>_carry_<name>.txt, <act> the
###   destination's act (the second name of the first pair); `--shifted` writes a refused carry, the shifted names printed in its bank
### carry.py check <src_rel> <dst_rel>
###   a print only: the shifted names between two files already written; exit 1 where there are any
"""
import difflib
import io
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
ROOT = os.path.dirname(T)
D = os.path.join(ROOT, 'data')
NL = chr(10)
if T not in sys.path:
    sys.path.insert(0, T)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import standing.repeat as RP  # noqa: E402


def rd(p):
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else ''


def substitute(text, subs):
    out = text
    for a, b in subs:
        out = out.replace(a, b)
    return out


def udiff(old, new, a_name, b_name):
    sm = difflib.SequenceMatcher(None, old, new, autojunk=False)
    L = ['--- ' + a_name, '+++ ' + b_name]
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == 'equal':
            continue
        L.append('@@ -%d,%d +%d,%d @@' % (i1 + 1, i2 - i1, j1 + 1, j2 - j1))
        L += ['-' + l for l in old[i1:i2]] + ['+' + l for l in new[j1:j2]]
    return L


def _path(rel):
    return rel if os.path.isabs(rel) else os.path.join(ROOT, *rel.split('/'))


def carry(src_rel, dst_rel, name, subs, shifted_ok=False, again=False):
    old = rd(_path(src_rel))
    if not old:
        sys.exit('### %s IS NOT THERE -- NOTHING CARRIED' % src_rel)
    dst = _path(dst_rel)
    if os.path.exists(dst) and not again:
        sys.exit('### %s EXISTS -- NOTHING WRITTEN (give --again to rewrite the carried form)' % dst_rel)
    new = substitute(old, subs)
    shifted = RP.shifted_missing(old, new, T)
    if shifted and not shifted_ok:
        sys.exit(NL.join(['### THE SUBSTITUTION SHIFTS %d NAME(S) PAST WHAT EXISTS -- NOTHING WRITTEN ((R334)(2)(ix)):' % len(shifted)]
                         + ['  :%d %s (tools/%s.py absent; the source line named a module that exists)' % (i, n, n) for i, n in shifted]
                         + ['### repair the carried form by hand after `--shifted`, or carry the name unshifted']))
    act = subs[0][1]
    ol, nl_ = old.split(NL), new.split(NL)
    diff = udiff(ol, nl_, src_rel, dst_rel)
    changed = sum(1 for l in diff if l.startswith('+') and not l.startswith('+++'))
    L = ['%s -- THE CARRY BY DIFF (tools/standing/carry.py): %s -> %s (%s)' % (act, src_rel, dst_rel, time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())), '',
         '### the substitution alone (%s); %d lines, %d changed' % (', '.join('%s -> %s' % s for s in subs), len(nl_), changed),
         '### SHIFTED PAST WHAT EXISTS: %s' % ('; '.join(':%d %s' % s for s in shifted) if shifted else 'NONE'), '',
         '### THE DIFF OF THE SUBSTITUTION, FROM autojunk=False OPCODES:'] + ['  ' + l for l in diff]
    L += ['', '### ### **CARRIED %s ; LINES %d ; CHANGED %d ; SHIFTED %d%s**' % (dst_rel, len(nl_), changed, len(shifted),
                                                                          ' (WRITTEN BY --shifted)' if shifted else '')]
    p = os.path.join(D, '%s_carry_%s.txt' % (act, name))
    import act_membrane as MEM
    MEM.guard_path(act, p, None)
    for path, body in ((dst, new), (p, NL.join(L) + NL)):
        with open(path + '.tmp', 'wb') as fh:
            fh.write(body.encode('utf-8'))
        os.replace(path + '.tmp', path)
    print(NL.join(L[:4] + L[-1:]))


def check(src_rel, dst_rel):
    shifted = RP.shifted_missing(rd(_path(src_rel)), rd(_path(dst_rel)), T)
    for s in shifted:
        print('  :%d %s' % s)
    print('### SHIFTED PAST WHAT EXISTS: %d' % len(shifted))
    return 1 if shifted else 0


def main(argv):
    if argv[:1] == ['check'] and len(argv) == 3:
        return check(argv[1], argv[2])
    if len(argv) < 5 or '--subs' not in argv:
        sys.exit(__doc__)
    i = argv.index('--subs')
    subs = tuple(tuple(x.split(':', 1)) for x in argv[i + 1].split(','))
    carry(argv[0], argv[1], argv[2], subs, '--shifted' in argv, '--again' in argv)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
