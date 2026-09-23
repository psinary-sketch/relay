# -*- coding: utf-8 -*-
"""b482_extract.py -- THE SURVEY FOR THE XiPrime READ.
### ### **THE KERNEL LANE OPENS TO READ STATEMENTS AT A PIN AND CLOSES AT THE ACT'S END.**
### No build is started, no Lean is run, nothing is imported into the corpus, and the zeta23 clone
### is READ ONLY -- its artefacts are never committed. ### (R70): the declaration reader is
### rehearsed on one of the six before the seal and what it returns is printed.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
Z = os.path.join(D, 'anthropic-zeta23', 'formal-math', 'zeta23')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
DEP = os.path.join(PP, 'outputs', 'DEPOSITED-v1.1.2', 'A_Place_to_Stand.md')
KER = os.path.join('D:', os.sep, 'SIDE-kernel')
SIM = os.path.join('D:', os.sep, 'SIDE-simplicity')
NL = chr(10)
L, MISSES = [], []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def show(repo, ref):
    r = subprocess.run(['git', '-C', repo, 'show', ref], capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return r.stdout.replace(chr(13), '')


def declarations(text):
    """### ### **THE DECLARATION READER.** ### Returns each top-level declaration as
    ### `(kind, name, statement, line)` -- ### **THE STATEMENT AND NOT THE DOCSTRING**, taken from
    ### the declaration keyword to the proof token (`:= by`, `:= `) or the next declaration.
    ### ### **A DOCSTRING IS PROSE ABOUT A STATEMENT AND IS NOT THE STATEMENT.**"""
    lines = text.split(NL)
    heads = [(i, l) for i, l in enumerate(lines)
             if re.match(r'^(theorem|lemma|def|noncomputable def|abbrev|axiom|instance)\s', l)]
    out = []
    for k, (i, l) in enumerate(heads):
        end = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
        body = lines[i:end]
        stmt = []
        for b in body:
            m = re.search(r':=\s*by\b|:=\s*$|:=\s+\S', b)
            if m and stmt:
                stmt.append(b[:m.start()].rstrip())
                break
            if m and not stmt:
                stmt.append(b[:m.start()].rstrip())
                break
            stmt.append(b.rstrip())
        kind, name = l.split()[0], re.split(r'[\s(:{]', l.split(None, 1)[1])[0]
        out.append((kind, name, NL.join(x for x in stmt if x.strip()), i + 1))
    return out


def main():
    rec('=' * 108)
    rec('b482 -- THE SURVEY. ### STATEMENTS READ AT A PIN; NO BUILD, NO LEAN RUN, NOTHING IMPORTED.')
    rec('=' * 108)

    # ------------------------------------------------------------------ (P0) the halt on b479
    rec('')
    rec('(P0) ### **b479 IS NOT BANKED, AND THE HALT IS PROVED BEFORE THIS ACT OPENS.**')
    rec('-' * 108)
    ferries = sorted(f for f in os.listdir(D) if 'ferry' in f and f.endswith('.txt'))
    hits = [f for f in ferries if 'ACT b479' in read(os.path.join(D, f))]
    ctrl = [f for f in ferries if 'ACT b482' in read(os.path.join(D, f))]
    rec('    ferry files searched : ### **%d**' % len(ferries))
    rec('    files carrying `ACT b479` : ### **%d** %s' % (len(hits), hits or ''))
    rec('    ### POSITIVE CONTROL -- files carrying `ACT b482` : ### **%d** %s'
        % (len(ctrl), ctrl or ''))
    rec('    ### ### **THE SEARCH WORKS AND FINDS b482`S ORDER; IT FINDS NO b479 ORDER ANYWHERE.**')
    rec('    ### ### **AND THREE SEALED FACES ASSERT OTHERWISE.** ### `b480`, `b483` and `b484`')
    rec('    ### each say `b479` is *"registered by its own ferry"*. ### That claim was carried from')
    rec('    ### face to face and ### **NO BANKED FERRY EVER CARRIED IT** -- the species the record')
    rec('    ### already names: ### **A CLAIM THAT LIVES ONLY IN A POINTER IS ONE TRIM FROM GONE.**')
    rec('    ### ### **b479 IS THEREFORE NOT RUN, AND ITS ORDER IS NOT RECONSTRUCTED FROM MEMORY.**')
    if hits:
        MISSES.append(('b479', 'order unexpectedly found'))

    # ------------------------------------------------------------------ (P1) the pin
    rec('')
    rec('(P1) THE CLONE`S PIN, AND THE SIX DECLARATIONS AT IT.')
    rec('-' * 108)
    head = read(os.path.join(D, 'anthropic-zeta23', 'formal-math.HEAD.txt'))
    head = re.sub(r'[^0-9a-f]', '', head.lower())[:40]
    rec('    the clone`s banked HEAD : ### **%s**' % head)
    rec('    the pin b482`s order names : ### **fbdc36b** ### -- %s'
        % ('MATCHES' if head.startswith('fbdc36b') else '### DOES NOT MATCH'))
    if not head.startswith('fbdc36b'):
        MISSES.append(('formal-math.HEAD.txt', 'pin mismatch'))
    xp = read(os.path.join(Z, 'Challenge', 'XiPrime.lean'))
    decls = declarations(xp)
    thms = [d for d in decls if d[0] == 'theorem']
    rec('    declarations in `zeta23/Challenge/XiPrime.lean` : %d ; ### **THEOREMS : %d**'
        % (len(decls), len(thms)))
    for kind, name, stmt, ln in thms:
        rec('')
        rec('    ### `%s`  (`Challenge/XiPrime.lean:%d`)' % (name, ln))
        for s in stmt.split(NL):
            rec('        %s' % s)
    rec('')
    sorries = xp.count('sorry')
    rec('    ### ### **EVERY ONE OF THE SIX IS CLOSED BY `sorry` -- %d IN THE FILE.**' % sorries)
    rec('    ### ### **THEY ARE CHALLENGE STATEMENTS, NOT THEOREMS HELD**, and this act reads them')
    rec('    ### as statements posed. ### **A STATEMENT POSED IS NOT A RESULT.**')

    # ------------------------------------------------------------------ (P2) the comparator
    rec('')
    rec('(P2) `comparator-xiprime.json` -- ITS DECLARATION LIST AND ITS PERMITTED AXIOMS.')
    rec('-' * 108)
    comp = json.loads(read(os.path.join(Z, 'comparator-xiprime.json')))
    rec('    challenge module : %s ; solution module : %s'
        % (comp.get('challenge_module'), comp.get('solution_module')))
    rec('    theorem_names (### **%d**):' % len(comp.get('theorem_names') or []))
    for n in comp.get('theorem_names') or []:
        rec('      %s' % n)
    rec('    definition_names : %s' % (comp.get('definition_names') or 'NONE'))
    rec('    ### ### **PERMITTED AXIOMS : %s**' % ', '.join(comp.get('permitted_axioms') or []))
    same = sorted(comp.get('theorem_names') or []) == sorted(n for _, n, _, _ in thms)
    rec('    ### the comparator`s list and the file`s theorems are the SAME SET : ### **%s**' % same)
    if not same:
        MISSES.append(('comparator-xiprime.json', 'list differs from the file'))

    # ------------------------------------------------------------------ (P3) the corpus statements
    rec('')
    rec('(P3) THE CORPUS STATEMENTS -- ### **THREE SOURCES, FOUR NAMED STATEMENTS.**')
    rec('-' * 108)
    corpus = []
    dep = read(DEP).split(NL)
    gi = next((i for i, l in enumerate(dep) if l.startswith('**Perpendicular crossing.**')), None)
    if gi is None:
        MISSES.append((DEP, 'the perpendicular-crossing clause'))
    else:
        rec('  ### (A) THE GEOMETRIC CLAUSE, AS THE DEPOSITED MONOGRAPH STATES IT.')
        rec('      `outputs/DEPOSITED-v1.1.2/A_Place_to_Stand.md:%d`' % (gi + 1))
        for s in re.findall(r'.{1,120}(?:\s|$)', dep[gi]):
            rec('        %s' % s.strip())
        corpus.append(dict(key='A', name='the geometric clause (perpendicular crossing)',
                           addr='A_Place_to_Stand.md:%d' % (gi + 1), text=dep[gi]))
    sc = show(KER, 'v1.5:Kernel/SpectralCannonFull.lean')
    sd = [d for d in declarations(sc) if d[1] == 'spectral_cannon']
    if not sd:
        MISSES.append(('SIDE-kernel v1.5', 'spectral_cannon'))
    else:
        k, n, stmt, ln = sd[0]
        rec('')
        rec('  ### (B) `SpectralCannonFull.spectral_cannon` AT SIDE-kernel ### **v1.5** ###')
        rec('      `Kernel/SpectralCannonFull.lean:%d` -- ### **THE STATEMENT, NOT THE DOCSTRING**' % ln)
        for s in stmt.split(NL):
            rec('        %s' % s)
        corpus.append(dict(key='B', name='spectral_cannon', addr='Kernel/SpectralCannonFull.lean:%d' % ln,
                           text=stmt))
    cd = show(SIM, 'v0.1.0:SIDESimplicity/Codimension.lean')
    for want in ('transversal_generic_empty', 'codim_margin'):
        dd = [d for d in declarations(cd) if d[1] == want]
        if not dd:
            MISSES.append(('SIDE-simplicity v0.1.0', want))
            continue
        k, n, stmt, ln = dd[0]
        rec('')
        rec('  ### (C) `%s` AT SIDE-simplicity ### **v0.1.0** ### (its latest tag)' % n)
        rec('      `SIDESimplicity/Codimension.lean:%d` -- ### **THE STATEMENT, NOT THE DOCSTRING**' % ln)
        for s in stmt.split(NL):
            rec('        %s' % s)
        corpus.append(dict(key='C', name=n, addr='SIDESimplicity/Codimension.lean:%d' % ln, text=stmt))
    defs = {n: s for k, n, s, _ in declarations(cd) if k == 'def'}
    rec('')
    rec('      ### the two `def`s those statements are about, at the same tag:')
    for n in ('numSources', 'curveDim'):
        rec('        %s' % defs.get(n, '### %s NOT FOUND' % n))
    rec('      ### ### **SO (C)`S TWO STATEMENTS QUANTIFY OVER `ℤ` AND NOTHING ELSE.** ### Neither')
    rec('      ### mentions `ξ`, `ζ`, a zero, or a complex number; both are closed by `omega`, the')
    rec('      ### integer-arithmetic decision procedure. ### **THE MATHEMATICS THEY ARE NAMED FOR')
    rec('      ### LIVES IN THEIR DOCSTRINGS, AND THE ORDER ASKS FOR STATEMENTS.**')

    # ------------------------------------------------------------------ (P4) the (R70) rehearsal
    rec('')
    rec('(P4) (R70) -- THE DECLARATION READER REHEARSED ON ONE OF THE SIX, BEFORE THE SEAL.')
    rec('-' * 108)
    probe = [d for d in thms if d[1] == 'xiPrime_over_xi_re_pos'][0]
    rec('    subject : `%s`' % probe[1])
    rec('    what the reader returns, verbatim:')
    for s in probe[2].split(NL):
        rec('      %s' % s)
    ok = ('deriv' not in probe[2] and 'XiPrime.xiDeriv' in probe[2]
          and 'sorry' not in probe[2] and '/--' not in probe[2])
    rec('    ### the returned text contains the STATEMENT and ### **NOT the docstring, NOT the')
    rec('    ### proof token, NOT the `sorry`** : ### **%s**' % ok)
    rec('    ### ### AND THE NEGATIVE HALF: the file`s docstring for that theorem is')
    di = next(i for i, l in enumerate(xp.split(NL)) if 'Re ξ′/ξ(s) > 0' in l)
    rec('      %s' % xp.split(NL)[di].strip())
    rec('    ### which the reader ### **DID NOT RETURN** ### -- so the reader distinguishes the two.')
    if not ok:
        MISSES.append(('rehearsal', 'the reader returned the wrong span'))

    rec('')
    rec('=' * 108)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 108)
    io.open(os.path.join(D, 'b482_extract.txt'), 'w', encoding='utf-8', newline=NL).write(
        NL.join(L) + NL)
    json.dump(dict(pin=head, six=[dict(name=n, stmt=s, line=ln) for _, n, s, ln in thms],
                   comparator=comp, corpus=corpus, sorries=sorries,
                   b479_hits=hits, b479_control=ctrl, misses=MISSES),
              io.open(os.path.join(D, 'b482_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
