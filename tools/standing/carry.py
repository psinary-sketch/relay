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
### carry.py ruled <act> <prev> <ferry bank>
###   v1.27.0, (R357)(3)(viii): every carried figure and section printed beside the ruling; R1-R3 refused (exit 13), before the citation check
"""
import difflib
import io
import os
import re
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


# ### v1.13.0, (R343)(2)(vii): a kept branch is a name the act does not move: b730 (m), b731 (b), b732 (c), each the shift of zq-b730 by one act. push-bNNN alone is the act's and shifts
KEPT_BRANCH = re.compile(r'(?<![\w-])(?:zq|detect|keiper|c2|rebuild|port|scratch|pin|recut|challenge|corrigendum)-b[0-9]{3}(?![0-9])')


def substitute(text, subs):
    """the pairs applied in order, every kept branch's name held out of them."""
    held = []

    def hold(m):
        held.append(m.group(0))
        return '\0%d\0' % (len(held) - 1)
    out = KEPT_BRANCH.sub(hold, text)
    for a, b in subs:
        out = out.replace(a, b)
    return re.sub('\0([0-9]+)\0', lambda m: held[int(m.group(1))], out)


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


# ================================================================================ v1.27.0, (R357)(3)(viii): THE CARRY BESIDE THE RULING
# ### b746 defects (d) and (o): the carried worklist held b745's figures (PRE_PP at 5937961, b745's start) and checks sections 25-26 kept
# ### b745's six-dispatch form (a dispatch row, a read by run id) where (R356) ordered none. Here every carried figure and section is printed
# ### beside the ruling, and two kinds are REFUSED before the citation check:
# ###   R1 a worklist figure carried unchanged that names the previous act's own start (its PRE_PP or PRE_RELAY), the ruling not naming it
# ###   R2 a section carried unchanged (equal to the previous act's after the substitution) that reads a figure the ruling sets (RULED) whose
# ###      value moved between the two worklists, or that R3 refused: the section's form was written for the previous ruling's figure
# ###   R3 a ruled figure carried unchanged and non-empty with an element the ruling does not name
RULED = ('MAX_DISPATCHES', 'EF_RUNS')
HEXV = re.compile(r'\b(?=[0-9a-f]*[a-f])[0-9a-f]{7,40}\b')
KNAME = re.compile(r'\b(?:K|WL)\.([A-Z_][A-Z0-9_]*)\b')


def literals(text):
    """{name: value} for every top-level assignment of a literal in a worklist's text (ast; a non-literal skipped)."""
    import ast
    out = {}
    for node in ast.parse(text).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            try:
                out[node.targets[0].id] = ast.literal_eval(node.value)
            except (ValueError, SyntaxError, TypeError):
                pass
    return out


def _empty(v):
    return v is None or v == 0 or v == '' or (isinstance(v, (tuple, list, dict, set)) and not v)


def ruled(act_text, prev_text, wl_text, prev_wl_text, ruling_text, subs):
    """pure: (lines, refused) -- every carried figure and section printed beside the ruling; R1 and R2 refused."""
    import actmodule as AM
    W, P = literals(wl_text), literals(prev_wl_text)
    starts = [str(P.get(k) or '')[:7] for k in ('PRE_PP', 'PRE_RELAY') if P.get(k)]
    rl = ruling_text.replace('\r', '').split(NL)

    def named(tok):
        return next((i for i, l in enumerate(rl, 1) if tok in l), None)
    L, refused = ['## THE CARRIED FIGURES (worklist constants equal to the previous act`s after the substitution, non-empty), each beside the ruling'], []
    for k in sorted(set(W) & set(P)):
        v, pv = W[k], P[k]
        if _empty(v) or repr(v) != substitute(repr(pv), subs):
            continue
        hx = HEXV.findall(repr(v))
        at = [named(h[:7]) for h in hx]
        bad = [h for h in hx if h[:7] in starts and not named(h[:7])]
        L.append('  %-28s %-60s %s%s' % (k, repr(v)[:60], ('hex %s ; ' % ', '.join('%s %s' % (h[:8], (':%d' % a) if a else 'NOT NAMED') for h, a in zip(hx, at))) if hx else '',
                                         '### REFUSED (R1): names the previous act`s start %s' % ', '.join(bad) if bad else 'carried'))
        if bad:
            refused.append(('R1', k, 'the previous act`s start %s carried as this act`s figure, the ruling not naming it' % ', '.join(bad)))
    # ### R3: a ruled figure carried unchanged and non-empty, an element the ruling does not name: the previous ruling's figure as this act's
    for k in RULED:
        if k in W and k in P and not _empty(W[k]) and repr(W[k]) == repr(P[k]):
            el = list(W[k]) if isinstance(W[k], (tuple, list)) else [W[k]]
            un = [x for x in el if not named(str(x))]
            L.append('  %-28s %-60s %s' % (k, repr(W[k])[:60], ('### REFUSED (R3): a ruled figure carried unchanged, not named in the ruling: %s' % ', '.join(map(str, un))) if un else 'named in the ruling'))
            if un:
                refused.append(('R3', k, 'the previous act`s ruled figure carried unchanged, %d element(s) the ruling does not name' % len(un)))
    moved = [k for k in RULED if k in W and k in P and repr(W[k]) != repr(P[k])] + [r[1] for r in refused if r[0] == 'R3']
    L += ['', '## THE CARRIED SECTIONS (equal to the previous act`s after the substitution); the ruled figures %s, moved: %s' % (
        ', '.join('%s %r -> %r' % (k, P.get(k), W.get(k)) for k in RULED), ', '.join(moved) or 'NONE')]
    pb = dict((key, prev_text[s:e]) for key, s, e in AM.blocks(prev_text))
    n = 0
    for key, s, e in AM.blocks(act_text):
        if key not in pb or act_text[s:e] != substitute(pb[key], subs):
            continue
        n += 1
        reads = sorted(set(KNAME.findall(act_text[s:e])) & set(moved))
        if reads:
            L.append('  %s ### REFUSED (R2): carried unchanged, reads %s, a ruled figure that moved' % (' '.join(map(str, key)), ', '.join(reads)))
            refused.append(('R2', ' '.join(map(str, key)), 'carried unchanged and reads %s, moved %s' % (
                ', '.join(reads), '; '.join('%r -> %r' % (P[r], W[r]) for r in reads))))
    L.append('  carried sections %d ; refused %d' % (n, sum(1 for r in refused if r[0] == 'R2')))
    L += ['', '### ### **THE CARRY BESIDE THE RULING: REFUSED %d (R1 %d, R2 %d, R3 %d)%s.**' % (
        len(refused), sum(1 for r in refused if r[0] == 'R1'), sum(1 for r in refused if r[0] == 'R2'), sum(1 for r in refused if r[0] == 'R3'),
        ' -- ' + '; '.join('%s %s' % r[:2] for r in refused) if refused else ' ; NONE REFUSED')]
    return L, refused


def main(argv):
    if argv[:1] == ['check'] and len(argv) == 3:
        return check(argv[1], argv[2])
    if argv[:1] == ['ruled'] and len(argv) == 4:
        # ### carry.py ruled <act> <prev> <ferry bank>: the act's module and worklist beside the previous act's, at the working tree
        a, p, fb = argv[1], argv[2], argv[3]
        texts = [rd(_path(x)) for x in ('tools/acts/%s.py' % a, 'tools/acts/%s.py' % p, 'tools/%s_worklist.py' % a, 'tools/%s_worklist.py' % p, fb)]
        for x, t in zip(('tools/acts/%s.py' % a, 'tools/acts/%s.py' % p, 'tools/%s_worklist.py' % a, 'tools/%s_worklist.py' % p, fb), texts):
            if not t:
                sys.exit('### REFUSED: %s resolves to no file' % x)
        pn, an = int(p[1:]), int(a[1:])
        subs = (('b%d' % pn, 'b%d' % an), ('b%d' % (pn - 1), 'b%d' % (an - 1)))
        L, refused = ruled(texts[0], texts[1], texts[2], texts[3], texts[4], subs)
        print(NL.join(L))
        return 13 if refused else 0
    if len(argv) < 5 or '--subs' not in argv:
        sys.exit(__doc__)
    i = argv.index('--subs')
    subs = tuple(tuple(x.split(':', 1)) for x in argv[i + 1].split(','))
    carry(argv[0], argv[1], argv[2], subs, '--shifted' in argv, '--again' in argv)
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
