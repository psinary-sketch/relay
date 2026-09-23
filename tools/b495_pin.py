# -*- coding: utf-8 -*-
"""b495_pin.py -- COMPONENT 1. ### **THE PIN, DECIDED BY A COMPARISON AND NOT BY A PREFERENCE.**

### `EF_lit`'s statement is extracted at tag `v1.0` (`3635e748`) and at `fbdc36b` FROM THE CORPUS'S
### OWN CLONE, each with its sha256. ### **BYTE-IDENTICAL -> PIN `v1.0`; ELSE PIN `fbdc36b`.**
### ### **THE REASON PRINTED IS THE COMPARISON ITSELF**, not a sentence about it.
"""
import hashlib
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
CLONE = os.path.join(D, 'anthropic-zeta23', 'formal-math')
MODULE = 'Zeta23/ExplicitFormula.lean'
# ### ### **THE PATH IS NOT THE SAME AT BOTH REVISIONS, AND A PATH MISS IS NOT A FINDING.**
# ### The first run of this component reported the statement ### **NOT FOUND** at `v1.0` and so
# ### scored the two revisions as differing -- which would have chosen `fbdc36b` for a reason that
# ### is not the order's. ### The cause is a LAYOUT MOVE: at `v1.0` the tree is rooted at
# ### `Zeta23/`, and by `fbdc36b` the `zeta23-palomar-layout` merge has moved it under `zeta23/`.
# ### ### **THE MODULE IS THEREFORE RESOLVED AT EACH REVISION BY LOOKING IT UP IN THAT
# ### ### REVISION'S OWN TREE**, and the path actually used is printed beside each reading.
PREFIXES = ('', 'zeta23/')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def resolve_path(rev):
    """### ### **THE MODULE'S PATH IN THIS REVISION'S OWN TREE.** ### Returns `(path, listed)`:
    ### `listed` is every candidate the tree carries, so a miss prints what WAS there."""
    names = subprocess.run(['git', '-C', CLONE, 'ls-tree', '-r', '--name-only', rev],
                           capture_output=True, text=True, encoding='utf-8',
                           errors='replace').stdout.split(NL)
    cands = [n.strip() for n in names if n.strip().endswith('/' + MODULE) or n.strip() == MODULE]
    for pre in PREFIXES:
        if pre + MODULE in cands:
            return pre + MODULE, cands
    return (cands[0] if cands else None), cands


def show(rev, path):
    """### The file's bytes at a revision. ### **BYTES, NOT TEXT** -- a decode would hide a
    ### difference that is exactly what this component exists to find."""
    r = subprocess.run(['git', '-C', CLONE, 'show', '%s:%s' % (rev, path)],
                       capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout.replace(b'\r\n', b'\n')


def statement(blob):
    """### ### **THE DECLARATION, FROM `def EF_lit` TO THE FIRST BLANK LINE AFTER ITS BODY.**
    ### The extractor is printed with its result so a reader can see WHAT was compared."""
    if blob is None:
        return None
    text = blob.decode('utf-8', 'replace')
    m = re.search(r'^def EF_lit\b', text, re.M)
    if not m:
        return None
    rest = text[m.start():]
    # ### the declaration ends at the first line that starts a NEW top-level declaration or at a
    # ### blank line followed by a non-indented line -- whichever comes first.
    lines = rest.split(NL)
    out = [lines[0]]
    for ln in lines[1:]:
        if ln.strip() == '':
            break
        out.append(ln)
    return NL.join(out).encode('utf-8')


def sha(b):
    return hashlib.sha256(b).hexdigest() if b is not None else None


def main():
    rec('=' * 104)
    rec('b495 COMPONENT 1 -- THE PIN. ### **DECIDED BY THE COMPARISON, NOT BY A PREFERENCE.**')
    rec('=' * 104)
    rec('  clone   : %s' % os.path.relpath(CLONE, ROOT).replace(os.sep, '/'))
    rec('  module  : %s' % MODULE)
    rec('  ### the clone is READ and NEVER written, and NEVER committed -- (R58).')
    rec('')

    revs = [('v1.0', 'v1.0'), ('fbdc36b', 'fbdc36b')]
    # ### **THE TAG IS RESOLVED, NOT ASSUMED.** ### The order names `v1.0` = `3635e748`; if the tag
    # ### in this clone resolves elsewhere the act must say so rather than carry the order's figure.
    resolved = {}
    for name, rev in revs:
        resolved[name] = subprocess.run(['git', '-C', CLONE, 'rev-parse', rev + '^{commit}'],
                                        capture_output=True, text=True).stdout.strip()
    rec('  ### THE REVISIONS, RESOLVED IN THIS CLONE:')
    for name, _ in revs:
        rec('    %-10s -> %s' % (name, resolved[name] or '### UNRESOLVED'))
    order_says = '3635e748'
    agrees = resolved['v1.0'].startswith(order_says)
    rec('    ### the order names `v1.0` = `%s` ; this clone resolves it to `%s` -- ### **%s**'
        % (order_says, resolved['v1.0'][:8], 'AGREE' if agrees else '### DISAGREE'))
    rec('')

    blobs, stmts, shas, fshas, paths = {}, {}, {}, {}, {}
    for name, _ in revs:
        paths[name], cands = resolve_path(resolved[name])
        blobs[name] = show(resolved[name], paths[name]) if paths[name] else None
        stmts[name] = statement(blobs[name])
        shas[name] = sha(stmts[name])
        fshas[name] = sha(blobs[name])

    rec('  ### THE MODULE`S PATH, RESOLVED IN EACH REVISION`S OWN TREE:')
    for name, _ in revs:
        rec('    %-10s -> %s' % (name, paths[name] or '### NOT IN THE TREE'))
    if paths['v1.0'] != paths['fbdc36b']:
        rec('    ### ### **THE PATHS DIFFER**, and that is a LAYOUT MOVE, not a statement change.')
        rec('    ### The `zeta23-palomar-layout` merge moved the tree under `zeta23/`. ### A reader')
        rec('    ### comparing the two by a single hard-coded path gets ### **NOT FOUND** at `v1.0`')
        rec('    ### and would pin `fbdc36b` for a reason the order never gave.')
    rec('')
    rec('  ### THE STATEMENT AT EACH REVISION, PRINTED WHOLE.')
    rec('  ' + '-' * 100)
    for name, _ in revs:
        rec('  --- `%s` (%s) at `%s` ---' % (name, (resolved[name] or '?')[:12],
                                             paths[name] or '### NOT IN THE TREE'))
        if stmts[name] is None:
            rec('      ### **NOT FOUND AT THIS REVISION.**')
            continue
        for ln in stmts[name].decode('utf-8').split(NL):
            rec('      %s' % ln)
        rec('      sha256 of the STATEMENT : %s' % shas[name])
        rec('      sha256 of the WHOLE FILE: %s' % fshas[name])
        rec('')

    same_stmt = (stmts['v1.0'] is not None and stmts['v1.0'] == stmts['fbdc36b'])
    same_file = (blobs['v1.0'] is not None and blobs['v1.0'] == blobs['fbdc36b'])
    pin = 'v1.0' if same_stmt else 'fbdc36b'
    rec('  ### THE COMPARISON, WHICH IS THE REASON.')
    rec('  ' + '-' * 100)
    rec('    statement bytes identical : ### **%s**  (%s vs %s)'
        % (same_stmt, (shas['v1.0'] or '?')[:16], (shas['fbdc36b'] or '?')[:16]))
    rec('    whole-file bytes identical: %s  (%s vs %s)'
        % (same_file, (fshas['v1.0'] or '?')[:16], (fshas['fbdc36b'] or '?')[:16]))
    rec('    ### ### **THE FILE IS NOT THE STATEMENT.** ### The order`s test is on the STATEMENT,')
    rec('    ### and both readings are printed so that a difference elsewhere in the module is')
    rec('    ### visible rather than swallowed by the rule that does not ask about it.')
    rec('')
    rec('  ### ### **PIN CHOSEN : `%s` = `%s`.**' % (pin, resolved[pin]))
    rec('  ### ### **THE REASON IS THE LINE ABOVE**: the statement is %sbyte-identical at the two'
        % ('' if same_stmt else 'NOT '))
    rec('  ### revisions, and the order`s rule reads ### *"byte-identical -> pin v1.0; else pin')
    rec('  ### fbdc36b"*. ### No preference entered.')
    rec('=' * 104)

    io.open(os.path.join(D, 'b495_pin.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(resolved=resolved, order_says=order_says, tag_agrees=agrees,
                   paths=paths, statement_sha=shas, file_sha=fshas, same_statement=same_stmt,
                   same_file=same_file, pin=pin, pin_sha=resolved[pin], module=MODULE),
              io.open(os.path.join(D, 'b495_pin.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: b495_pin.txt, b495_pin.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
