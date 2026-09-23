# -*- coding: utf-8 -*-
"""b495_create.py -- COMPONENT 2. ### **THE REPOSITORY, CREATED BY VENDORING.**

### ### **EVERY BODY IS A BYTE-IDENTICAL COPY AT THE PIN**, and the proof of that is not a claim
### but a pair of digests per module: ### **THE SOURCE FILE'S sha256 AT THE PIN, AND THE COPIED
### BODY'S sha256 TAKEN BEFORE ANY HEADER IS PREPENDED.** ### They must agree at all fifty-seven.
### ### **NO FILE IS EDITED BEYOND ITS PREPENDED ATTRIBUTION HEADER.**
"""
import hashlib
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
CLONE = os.path.join(D, 'anthropic-zeta23', 'formal-math')
TARGET = os.path.join('D:', os.sep, 'SIDE-explicit-formula')
SEED = 'Zeta23.WeilEF.Main'
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def git_clone(*a):
    return subprocess.run(['git', '-C', CLONE] + list(a), capture_output=True,
                          text=True, encoding='utf-8', errors='replace').stdout


def blob(pin, path):
    """### ### **BYTES AT THE PIN, NEWLINE-NORMALISED ONCE AND ONLY ONCE.**
    ### `git show` hands back the blob as stored; the normalisation is applied to BOTH the hashed
    ### source and the written body, so the two digests compare like with like. ### b372's `eol=lf`
    ### and b435's autocrlf lesson are why this is done here and not left to the filesystem."""
    r = subprocess.run(['git', '-C', CLONE, 'show', '%s:%s' % (pin, path)], capture_output=True)
    return None if r.returncode != 0 else r.stdout.replace(b'\r\n', b'\n')


def modpath(m):
    return '/'.join(m.split('.')) + '.lean'


def closure(pin, seed, names):
    """### ### **THE LOCAL IMPORT CLOSURE, COMPUTED -- NOT RECALLED FROM THE FACE.**
    ### An `import` line is recognised ANYWHERE in the file: the first parse of this closure broke
    ### because it stopped at the licence header's first non-import line and returned ONE module."""
    seen, ext, stack = set(), set(), [seed]
    while stack:
        m = stack.pop()
        if m in seen or m in ext:
            continue
        p = modpath(m)
        if p not in names:
            ext.add(m)
            continue
        seen.add(m)
        b = blob(pin, p)
        for ln in b.decode('utf-8', 'replace').split(NL):
            if ln.strip().startswith('import '):
                stack.append(ln.strip().split()[1])
    return sorted(seen), sorted(ext)


HDR_ZETA23 = """/-
VENDORED INTO SIDE-explicit-formula -- NOT WRITTEN HERE.

Source     : anthropics/formal-math, the `zeta23` formalization
Source path: %s
Pin        : %s = %s
Copied     : byte-identical; sha256 of the body below = %s
Licence    : Apache License 2.0 -- see LICENSE and NOTICE, carried whole from the source.

SPIRAL_MAP section 7 rule 7 (composites vendor with attribution) is satisfied by this header.
SPIRAL_MAP section 7 rule 9 (vanilla Lean 4 syntax discipline) is WAIVED for this namespace:
a vendored file is not edited, and the waiver is recorded in SPIRAL_MAP beside rule 9 with
act b495 as its reason.

NOTHING BELOW THIS BLOCK IS THIS PROGRAMME'S WORK, AND NOTHING BELOW IT HAS BEEN ALTERED.
-/
"""

HDR_PNT = """/-
SECOND ATTRIBUTION -- THIS FILE DERIVES FROM PrimeNumberTheoremAnd.

zeta23's own NOTICE names the files under `Zeta23/FromPNTPlus/` as derived from
PrimeNumberTheoremAnd (https://github.com/AlexKontorovich/PrimeNumberTheoremAnd),
Copyright the PrimeNumberTheoremAnd contributors, Apache License 2.0; and states that some
of those in turn derive from mathlib (https://github.com/leanprover-community/mathlib4),
Copyright the mathlib contributors, Apache License 2.0, with their original headers preserved.

THAT CHAIN IS NOT RESTATED HERE AND IS NOT SUMMARISED: the file's own upstream notice,
immediately below, is the record, and it is carried unaltered.
-/
"""

README = """# SIDE-explicit-formula

**A VENDORED KERNEL. NOTHING IN THIS REPOSITORY IS THIS PROGRAMME'S MATHEMATICS.**

Every `.lean` body here is a byte-identical copy of a file in `anthropics/formal-math`
(the `zeta23` formalization) at the pin recorded below. Each carries a prepended
attribution header and nothing else was changed.

| | |
|:--|:--|
| source | `anthropics/formal-math`, the `zeta23` formalization |
| pin | `%(pin)s` = `%(pin_sha)s` |
| modules vendored | %(n)d -- the local import closure of `%(seed)s` |
| of those, derived from PrimeNumberTheoremAnd | %(npnt)d, under `Zeta23/FromPNTPlus/` |
| toolchain | `%(toolchain)s` -- as zeta23 pins it |
| mathlib | `%(mathlib)s` -- as zeta23 pins it |
| licence | Apache 2.0; `LICENSE` and `NOTICE` carried whole from the source |

**WHY THE PIN IS `v1.0`.** `EF_lit`'s statement was read at tag `v1.0` and at `fbdc36b` and
the two are byte-identical (sha256 `%(stmt_sha)s`), so the order's rule
selects the tag. The comparison is banked at `relay/data/b495_pin.txt`.

**WHAT IS NOT CLAIMED.** This repository has **no profile**. Nothing here has been built or
`#print axioms`'d by this programme at the time of its creation, and **no document of the
corpus cites any terminal in it** until a profile is banked. A vendored copy is not a result,
a push is not a verification, and a launched build is not a built build.

**TOOLCHAIN DIVERGENCE IS EXPECTED.** SPIRAL_MAP section 7 rule 4 pins the federation to one
toolchain "unless stated otherwise"; this kernel states otherwise, and pins what its source
pins, because a vendored body must compile against the library its author compiled it against.
"""


def main():
    pinj = json.loads(io.open(os.path.join(D, 'b495_pin.json'), encoding='utf-8').read())
    pin, pin_sha = pinj['pin'], pinj['pin_sha']

    rec('=' * 104)
    rec('b495 COMPONENT 2 -- THE REPOSITORY. ### **CREATED BY VENDORING, NOT BY WRITING.**')
    rec('=' * 104)
    rec('  target : %s' % TARGET)
    rec('  source : the corpus`s own clone, at the pin component 1 CHOSE -- `%s` = `%s`'
        % (pin, pin_sha[:12]))
    rec('  ### ### **THE PIN IS READ FROM COMPONENT 1`S BANK, NOT RETYPED.**')
    rec('')

    names = set(x.strip() for x in
                git_clone('ls-tree', '-r', '--name-only', pin_sha).split(NL) if x.strip())
    mods, ext = closure(pin_sha, SEED, names)
    pnt = [m for m in mods if m.startswith('Zeta23.FromPNTPlus')]
    rec('  ### THE CLOSURE, COMPUTED AT THE PIN.')
    rec('    seed                     : `%s`' % SEED)
    rec('    local modules in closure : ### **%d**' % len(mods))
    rec('    external import roots    : %d  (not vendored; fetched by `lake` from their own pins)'
        % len(ext))
    rec('    of the closure, under `Zeta23/FromPNTPlus/` : ### **%d**' % len(pnt))
    rec('    ### ### **THE TEN ARE NOT CHOSEN BY THIS ACT.** ### zeta23`s own `NOTICE` says')
    rec('    ### *"The derived files are the ones under Zeta23/FromPNTPlus/"*, and this is that set')
    rec('    ### intersected with the closure. ### The predicate is the source`s, not the seat`s.')
    rec('')

    if os.path.isdir(TARGET):
        rec('  ### ### **THE TARGET ALREADY EXISTS. ### REFUSING TO WRITE INTO IT.**')
        rec('  ### A create that overwrites is not a create, and this act has no ruling to replace')
        rec('  ### an existing repository. ### %s' % TARGET)
        return 2

    # ---------------------------------------------------------------- the copy
    rows, mismatches = [], []
    os.makedirs(TARGET)
    for m in mods:
        src = modpath(m)
        body = blob(pin_sha, src)
        src_sha = sha(body)
        dst = os.path.join(TARGET, *m.split('.')) + '.lean'
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        # ### ### **THE BODY IS WRITTEN FIRST AND HASHED FROM DISK BEFORE ANY HEADER EXISTS.**
        # ### Hashing the in-memory bytes would prove only that the variable was not reassigned.
        with open(dst, 'wb') as fh:
            fh.write(body)
        with open(dst, 'rb') as fh:
            copied_sha = sha(fh.read())
        agree = (copied_sha == src_sha)
        if not agree:
            mismatches.append(m)
        rows.append(dict(module=m, src=src, src_sha=src_sha, body_sha=copied_sha,
                         agree=agree, pnt=(m in pnt)))

    rec('  ### THE BODY DIGESTS -- SOURCE AT THE PIN vs COPY ON DISK, BEFORE ANY HEADER.')
    rec('    modules copied            : %d' % len(rows))
    rec('    ### ### **DIGESTS AGREEING   : %d OF %d**' % (len(rows) - len(mismatches), len(rows)))
    rec('    ### DIGESTS DISAGREEING     : %d %s' % (len(mismatches), mismatches or ''))
    if mismatches:
        rec('    ### ### **HALT. ### A BODY THAT DIFFERS FROM ITS SOURCE IS NOT A VENDORED BODY.**')
        return 2
    rec('')

    # ---------------------------------------------------------------- the headers
    for r in rows:
        dst = os.path.join(TARGET, *r['module'].split('.')) + '.lean'
        with open(dst, 'rb') as fh:
            body = fh.read()
        head = (HDR_ZETA23 % (r['src'], pin, pin_sha, r['body_sha'])).encode('utf-8')
        if r['pnt']:
            head += HDR_PNT.encode('utf-8')
        with open(dst, 'wb') as fh:
            fh.write(head + body)
        # ### ### **AND THE BODY IS RE-HASHED AFTER THE PREPEND**, from the tail of the file, so
        # ### the claim "nothing but a header was added" is CHECKED and not merely intended.
        with open(dst, 'rb') as fh:
            after = fh.read()
        r['header_bytes'] = len(head)
        r['body_intact'] = (after[len(head):] == body) and after.startswith(head)
        r['second_header'] = bool(r['pnt'])

    broken = [r['module'] for r in rows if not r['body_intact']]
    rec('  ### THE HEADERS.')
    rec('    rule 7 header (zeta23 at the pin) on : ### **%d of %d**'
        % (sum(1 for r in rows if r['header_bytes']), len(rows)))
    rec('    second header (PrimeNumberTheoremAnd) on : ### **%d**'
        % sum(1 for r in rows if r['second_header']))
    rec('    ### ### **BODIES STILL INTACT AFTER THE PREPEND : %d of %d** %s'
        % (len(rows) - len(broken), len(rows), broken or ''))
    if broken:
        return 2
    rec('')

    # ---------------------------------------------------------------- licence and pins
    carried = {}
    for name in ('LICENSE', 'NOTICE'):
        b = blob(pin_sha, name)
        with open(os.path.join(TARGET, name), 'wb') as fh:
            fh.write(b)
        with open(os.path.join(TARGET, name), 'rb') as fh:
            got = sha(fh.read())
        carried[name] = dict(src_sha=sha(b), dst_sha=got, agree=(sha(b) == got), bytes=len(b))
    rec('  ### `LICENSE` AND `NOTICE`, CARRIED WHOLE -- Apache 2.0 section 4.')
    for name, c in carried.items():
        rec('    %-8s %d bytes ; source %s ; copy %s ; ### **%s**'
            % (name, c['bytes'], c['src_sha'][:16], c['dst_sha'][:16],
               'IDENTICAL' if c['agree'] else '### DIFFER'))
    rec('')

    toolchain = blob(pin_sha, 'lean-toolchain').decode('utf-8').strip()
    manifest = json.loads(blob(pin_sha, 'lake-manifest.json').decode('utf-8'))
    mathlib = next((p.get('rev', '') for p in manifest['packages'] if p['name'] == 'mathlib'), '')
    with open(os.path.join(TARGET, 'lean-toolchain'), 'wb') as fh:
        fh.write(blob(pin_sha, 'lean-toolchain'))
    with open(os.path.join(TARGET, 'lake-manifest.json'), 'wb') as fh:
        fh.write(blob(pin_sha, 'lake-manifest.json'))
    rec('  ### THE PINS, TAKEN FROM THE SOURCE AND NOT TYPED.')
    rec('    lean-toolchain : `%s`' % toolchain)
    rec('    mathlib        : `%s`' % mathlib[:12])
    rec('    ### rule 4`s expected per-kernel divergence; the README states it otherwise.')
    rec('')

    # ### ### **RULE 8: `@[default_target]` + `globs := #[.submodules ...]`, OR A SILENT 0-JOB BUILD.**
    lakefile = ('name = "SIDEExplicitFormula"' + NL
                + 'defaultTargets = ["SIDEExplicitFormula"]' + NL + NL
                + '[[require]]' + NL + 'name = "mathlib"' + NL
                + 'scope = "leanprover-community"' + NL
                + 'rev = "%s"' % mathlib + NL + NL
                + '[[lean_lib]]' + NL + 'name = "SIDEExplicitFormula"' + NL
                + 'globs = ["Zeta23.+"]' + NL)
    io.open(os.path.join(TARGET, 'lakefile.toml'), 'w', encoding='utf-8',
            newline=NL).write(lakefile)
    io.open(os.path.join(TARGET, 'SIDEExplicitFormula.lean'), 'w', encoding='utf-8',
            newline=NL).write('import %s' % SEED + NL)
    io.open(os.path.join(TARGET, 'README.md'), 'w', encoding='utf-8', newline=NL).write(
        README % dict(pin=pin, pin_sha=pin_sha, n=len(mods), seed=SEED, npnt=len(pnt),
                      toolchain=toolchain, mathlib=mathlib[:12],
                      stmt_sha=pinj['statement_sha'][pin]))
    io.open(os.path.join(TARGET, '.gitattributes'), 'w', encoding='utf-8',
            newline=NL).write('* text eol=lf' + NL)
    io.open(os.path.join(TARGET, '.gitignore'), 'w', encoding='utf-8',
            newline=NL).write('.lake/' + NL)
    rec('  ### THE KERNEL`S OWN FILES (the only files here this act WROTE rather than copied):')
    rec('    `lakefile.toml` -- rule 8`s `defaultTargets` + `globs`, without which `lake` reports')
    rec('      a CLEAN build having compiled NOTHING.')
    rec('    `SIDEExplicitFormula.lean` -- the library root, one `import %s`.' % SEED)
    rec('    `README.md` -- what is vendored, from where, at what pin, and ### **WHAT IS NOT')
    rec('      CLAIMED.** ### `.gitattributes` (`eol=lf`, b372) and `.gitignore` (`.lake/`).')
    rec('  ### ### **NO `.lean` BODY WAS WRITTEN BY THIS ACT.**')
    rec('=' * 104)

    io.open(os.path.join(D, 'b495_create.txt'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(L) + NL)
    json.dump(dict(pin=pin, pin_sha=pin_sha, target=TARGET, seed=SEED,
                   modules=len(rows), agreeing=len(rows) - len(mismatches),
                   mismatches=mismatches, pnt=[r['module'] for r in rows if r['pnt']],
                   carried=carried, toolchain=toolchain, mathlib=mathlib,
                   external_roots=len(ext), rows=rows),
              io.open(os.path.join(D, 'b495_create.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: b495_create.txt, b495_create.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
