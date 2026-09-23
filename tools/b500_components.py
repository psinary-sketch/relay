# -*- coding: utf-8 -*-
"""b500_components.py -- COMPONENTS 1 AND 2. ### **THE LOG READ WHOLE, AND THE THREE PROFILES.**

### ### **THE ORDER HAS A STOP IN IT.** ### Component 2: if the three profiles are not all the
### standard three, this act ### **PRINTS WHICH AND STOPS BEFORE COMPONENT 3.** ### This tool
### implements that stop and refuses to run Component 3 past it.
"""
import hashlib
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
LOG = os.path.join(D, 'b498_ef_build.log')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


# ### ### **THE STANDARD THREE, AS THE CORPUS DEFINES IT** (VERIFICATION_LOOM L138, `std3`).
# ### Matched on the WHOLE axiom string as the order requires -- a PREFIX match would read
# ### `[propext, Classical.choice, Quot.sound, sorryAx]` as the standard three.
STD3 = ('propext', 'Classical.choice', 'Quot.sound')
NAMES = ('EF_lit_zetaZeroConfig', 'EF_lit', 'EF_lit_zeta')

MARK = re.compile(r'^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3})\s{2}(.*)$')
ENDLINE = re.compile(r'END (.+?)\*\* : EXIT (-?\d+)')
# ### `lake` prints a built module as `✓ [k/n] Built Some.Module` or `Building Some.Module`
BUILT = re.compile(r'(?:Built|Building|Replayed)\s+([A-Za-z_][A-Za-z0-9_.]*)')
FAILED = re.compile(r'(?:\berror:|✖).{0,200}')
DURATION = re.compile(r'\((\d+(?:\.\d+)?)s\)')
AXIOM = re.compile(r"^(?:\d{4}-\d{2}-\d{2}T[0-9:.]+\s+)?'([A-Za-z_][A-Za-z0-9_.]*)'\s+"
                   r"(does not depend on any axioms|depends on axioms: \[([^\]]*)\])", re.M)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    with open(LOG, 'rb') as fh:
        raw = fh.read()
    text = raw.decode('utf-8', 'replace').replace(chr(13), '')
    lines = text.split(NL)

    rec('=' * 104)
    rec('b500 COMPONENTS 1 AND 2 -- ### **THE LOG READ WHOLE, AND THE THREE PROFILES.**')
    rec('=' * 104)
    rec('')
    rec('### COMPONENT 1 -- THE LOG.')
    rec('-' * 104)
    rec('    file   : `relay/data/b498_ef_build.log`')
    rec('    bytes  : ### **%d** ; lines : ### **%d**' % (len(raw), len([x for x in lines if x])))
    rec('    sha256 : %s' % sha(raw))
    rec('    ### ### **COMMITTED UNCHANGED** by this act; b498 declined because its process owned it.')
    rec('')

    marks = [(m.group(1), m.group(2)) for m in
             (MARK.match(x) for x in lines) if m]
    instants = sorted(set(t for t, _ in marks))
    rec('    marks (stamped lines)        : ### **%d**' % len(marks))
    rec('    ### ### **DISTINCT INSTANTS   : %d**' % len(instants))
    rec('    first mark : %s' % (instants[0] if instants else '### NONE'))
    rec('    last mark  : %s' % (instants[-1] if instants else '### NONE'))
    if instants:
        import datetime
        def p(t):
            return datetime.datetime.strptime(t, '%Y-%m-%dT%H:%M:%S.%f')
        wall = (p(instants[-1]) - p(instants[0])).total_seconds()
    else:
        wall = 0.0
    rec('    ### ### **WALL TIME FROM THE LOG`S OWN OUTER MARKS : %.1f s** (%.1f min)'
        % (wall, wall / 60.0))
    durs = [float(x) for x in DURATION.findall(text)]
    rec('    `lake`s summed reported durations : ### **%.1f s** across %d reported spans'
        % (sum(durs), len(durs)))
    rec('    ### the two numbers measure different things; `lake` builds in parallel, so the sum may exceed the wall.')
    rec('')

    ends = [(m.group(1), int(m.group(2))) for m in
            (ENDLINE.search(x) for x in lines) if m]
    nonzero = [e for e in ends if e[1] != 0]
    rec('    `END` / `EXIT` lines : ### **%d**' % len(ends))
    for what, code in ends:
        hexs = ('0x%08X' % (code & 0xFFFFFFFF))
        rec('      %-36s EXIT ### **%d** (%s)%s'
            % (what.replace('**', '').strip(), code, hexs,
               '  ### ### **STATUS_CONTROL_C_EXIT**' if hexs == '0xC000013A' else ''))
    rec('    ### ### **NON-ZERO EXITS : %d**' % len(nonzero))
    rec('')

    built = sorted(set(BUILT.findall(text)))
    built_lines = sorted(set(re.findall(r'\bBuilt\s+([A-Za-z_][A-Za-z0-9_.]*)', text)))
    replayed = sorted(set(re.findall(r'\bReplayed\s+([A-Za-z_][A-Za-z0-9_.]*)', text)))
    b_mathlib = [m for m in built_lines if m.startswith('Mathlib')]
    b_zeta = [m for m in built_lines if m.startswith('Zeta23')]
    b_other = [m for m in built_lines if not m.startswith(('Mathlib', 'Zeta23'))]
    rec('    ### ### **`Built` LINES (COMPILED) : %d** -- Zeta23.* %d ; Mathlib.* %d ; other %d %s'
        % (len(built_lines), len(b_zeta), len(b_mathlib), len(b_other), b_other))
    rec('    `Replayed` lines (NOT compiled) : %d' % len(replayed))
    rec('    modules built (by `lake`s own Built/Building/Replayed lines) : ### **%d** %s'
        % (len(built), built[:6] if built else ''))
    fails = [x for x in lines if FAILED.search(x) and 'BEGIN' not in x and 'END ' not in x]
    # ### ### **THE FIRST RUN MATCHED THE WORD `failed` INSIDE AN `info:` MESSAGE** -- `ring`'s
    # ### "Try this: ring_nf" advice. ### Those lines are printed apart and are NOT failures.
    advice = [x for x in lines if 'failed' in x.lower() and not FAILED.search(x)]
    rec('    lines carrying the word `failed` that are NOT errors (advice text) : %d' % len(advice))
    rec('    ### ### **MODULES THAT FAILED, BY NAME : %s**'
        % ('NONE' if not fails else '%d LINE(S) MATCH A FAILURE SHAPE' % len(fails)))
    for f in fails[:8]:
        rec('      %s' % f[:110])
    rec('')

    rec('### COMPONENT 2 -- THE THREE PROFILES.')
    rec('-' * 104)
    found = {m.group(1): (m.group(2), m.group(3)) for m in AXIOM.finditer(text)}
    rec('    `#print axioms` OUTPUT LINES ANYWHERE IN THE LOG : ### **%d**' % len(found))
    verdicts = {}
    for n in NAMES:
        hit = next((k for k in found if k == n or k.endswith('.' + n)), None)
        if hit is None:
            verdicts[n] = ('ABSENT', None)
            rec('    `%-24s` -> ### **ABSENT**' % n)
            continue
        kind, axs = found[hit]
        if kind == 'does not depend on any axioms':
            verdicts[n] = ('OTHER', 'axiom-free')
            rec('    `%-24s` -> ### **OTHER** : *"does not depend on any axioms"*' % n)
            continue
        got = tuple(a.strip() for a in (axs or '').split(','))
        if got == STD3:
            verdicts[n] = ('STANDARD THREE', axs)
            rec('    `%-24s` -> ### **STANDARD THREE** : `[%s]`' % (n, axs))
        else:
            verdicts[n] = ('OTHER', axs)
            rec('    `%-24s` -> ### **OTHER** : `[%s]`' % (n, axs))
    rec('    ### the match is on the ### **WHOLE AXIOM STRING**, as the order requires. ### A')
    rec('    ### PREFIX match would read `[propext, Classical.choice, Quot.sound, sorryAx]` as the')
    rec('    ### standard three, which is the one reading that must never be possible here.')
    rec('')

    allstd = all(v[0] == 'STANDARD THREE' for v in verdicts.values())
    anyother = any(v[0] == 'OTHER' for v in verdicts.values())
    r82 = 'HOLDS' if allstd else ('VOID' if anyother else 'VOID FOR WANT OF A RUN')
    rec('    ### ### **ALL THREE THE STANDARD THREE : %s**' % allstd)
    rec('    ### ### **(R82), BY ITS OWN WORDS : %s**' % r82)
    if not allstd:
        which = [n for n in NAMES if verdicts[n][0] != 'STANDARD THREE']
        rec('    ### ### **NOT ALL THREE. ### WHICH : %s -- ALL %s.**'
            % (which, verdicts[which[0]][0]))
        rec('    ### ### **(R82) IS NOT CLAIMED BY THIS ACT.** ### It holds only if all three read')
        rec('    ### the standard three, and they do not. ### **NOR IS (R82) REFUTED** -- a profile')
        rec('    ### that was never printed is not a profile that came out wrong, and')
        rec('    ### ### **ABSENT IS NOT OTHER.**')
        rec('')
        rec('    ### ### **### STOP. ### COMPONENT 3 IS NOT RUN. ###**')
        rec('    ### The order: *"otherwise print which and STOP before Component 3."* ### The')
        rec('    ### REGISTRY row keeps `PENDING`, no name is written beside it, the terminal table')
        rec('    ### is NOT regenerated for a profile move, and ### **NO ROW CITES THE KERNEL.**')
        rec('    ### ### **A STOP OBEYED IS A RESULT.** ### Running Component 3 anyway would have')
        rec('    ### written three profiles into REGISTRY that no run produced.')
    rec('=' * 104)

    io.open(os.path.join(D, 'b500_components.txt'), 'w', encoding='utf-8',
            newline=NL).write(NL.join(L) + NL)
    json.dump(dict(bytes=len(raw), sha256=sha(raw), lines=len([x for x in lines if x]),
                   marks=len(marks), distinct_instants=len(instants),
                   first=instants[0] if instants else None,
                   last=instants[-1] if instants else None,
                   wall_seconds=wall, lake_summed=sum(durs), lake_spans=len(durs),
                   ends=[dict(what=w.replace('**', '').strip(), exit=c) for w, c in ends],
                   nonzero_exits=len(nonzero), modules_built=built,
                   failure_lines=len(fails),
                   profiles={n: dict(verdict=v[0], axioms=v[1]) for n, v in verdicts.items()},
                   all_standard_three=allstd, component3_run=allstd, r82=r82,
                   built_lines=built_lines, built_zeta=len(b_zeta), built_mathlib=len(b_mathlib),
                   built_other=b_other, replayed=len(replayed)),
              io.open(os.path.join(D, 'b500_results.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    print('  written: b500_components.txt, b500_results.json')
    return 0


if __name__ == '__main__':
    sys.exit(main())
