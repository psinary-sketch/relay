# -*- coding: utf-8 -*-
"""b468r_extract.py -- THE SURVEY FOR b468's SECOND RUN, WITH THE (R75) ARTEFACTS ON DISK.

### ### **b468 CLOSED ONCE AT ROW 316, STOPPED AT ITS GATE, WITH ITS FACE LOCKED.** ### This run takes
### the record's `r` suffix (b443r's precedent) so nothing of the first run is overwritten.
### ### **EVERY FACT THE FACE WILL STAND ON IS BANKED HERE, BEFORE THE SEAL**: the five hashes, the
### clone's HEAD, both papers' theorem texts and whether they agree, the support and window, the
### trusted statement files' declarations, and what the untrusted library says about its own inputs.
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
A = os.path.join(D, 'anthropic-zeta23')
TX = os.path.join(D, 'b468r_text')
FM = os.path.join(A, 'formal-math')
Z = os.path.join(FM, 'zeta23')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
LV = os.path.join('D:', os.sep, 'SIDE-lv-conservation')
NL = chr(10)
L, MISSES = [], []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p, enc='utf-8'):
    try:
        return io.open(p, encoding=enc, errors='replace').read().replace(chr(13), '')
    except Exception:
        return ''


def lines(p):
    return read(p).split(NL)


def find(p, needle, label, show=170):
    for i, l in enumerate(lines(p)):
        if needle in l:
            rec('    %-40s %s:%d' % (label, os.path.basename(p), i + 1))
            rec('      %s' % re.sub(r'\s+', ' ', l.strip())[:show])
            return i + 1
    MISSES.append((os.path.basename(p), label))
    rec('    %-40s ### MISS -- %r' % (label, needle))
    return None


def span(p, lo, hi):
    return re.sub(r'\s+', ' ', ' '.join(lines(p)[lo - 1:hi])).strip()


def main():
    rec('=' * 104)
    rec('b468r -- THE SURVEY. ### **THE (R75) ARTEFACTS ARE ON DISK; EVERYTHING IS VERIFIED BEFORE THE SEAL.**')
    rec('=' * 104)

    # ---------------------------------------------------------------- (P1) hashes
    rec('')
    rec('(P1) THE FIVE PDFs AGAINST SHA256SUMS.txt.')
    rec('-' * 104)
    raw = open(os.path.join(A, 'SHA256SUMS.txt'), 'rb').read()
    enc = 'utf-16' if raw[:2] in (b'\xff\xfe', b'\xfe\xff') else 'utf-8-sig'
    rec('    SHA256SUMS.txt encoding : %s ### a PowerShell write -- decoded as what it is' % enc)
    rows = [l.split() for l in raw.decode(enc).splitlines() if l.strip()]
    hashes = []
    for r in rows:
        name = r[0]
        if len(r) < 2:
            rec('    %-34s ### BLANK ROW -- IGNORED, AS ORDERED' % name)
            continue
        got = hashlib.sha256(open(os.path.join(A, name), 'rb').read()).hexdigest()
        ok = got == r[1].lower()
        rec('    %-34s %s %s' % (name, got, 'MATCH' if ok else '### MISMATCH -- ABSENT'))
        hashes.append(dict(name=name, sha256=got, match=ok))
    pdfs = [h for h in hashes if h['name'].endswith('.pdf')]
    rec('  ### ### **PDFs : %d ; MATCHING : %d.**' % (len(pdfs), sum(h['match'] for h in pdfs)))
    head_txt = open(os.path.join(A, 'formal-math.HEAD.txt'), 'rb').read().decode(enc).strip()
    head = subprocess.run(['git', '-C', FM, 'rev-parse', 'HEAD'], capture_output=True,
                          text=True).stdout.strip()
    dirty = subprocess.run(['git', '-C', FM, 'status', '--porcelain'], capture_output=True,
                           text=True).stdout.strip()
    rec('    formal-math.HEAD.txt : %s' % head_txt)
    rec('    the clone`s own HEAD : %s   ### **%s**' % (head, 'AGREE' if head == head_txt else 'DISAGREE'))
    rec('    the clone`s working tree clean : %s' % (dirty == ''))

    # ---------------------------------------------------------------- (P2) the theorems
    rec('')
    rec('(P2) THE MAIN THEOREM IN BOTH PAPERS, AND WHETHER THEY AGREE.')
    rec('-' * 104)
    CP = os.path.join(TX, 'claude_paper_2026-08-11.txt')
    AF = os.path.join(TX, 'alpoge_furman_2608.13637.txt')

    def theorem_block(p):
        ls = lines(p)
        a = next(i for i, l in enumerate(ls) if l.strip().startswith('Theorem A.'))
        b = next(i for i, l in enumerate(ls) if 'Date:' in l and i > a)
        c = next(i for i, l in enumerate(ls) if l.strip().startswith('Theorem B.'))
        return a + 1, span(p, a + 1, b), c + 1, span(p, c + 1, c + 2)

    ca, cA, cb, cB = theorem_block(CP)
    aa, aA, ab, aB = theorem_block(AF)
    norm = lambda s: re.sub(r'[^A-Za-z0-9]+', '', s)
    first_form = norm(cA) == norm(aA)
    # ### ### **THE FIRST FORM SAID `DISAGREE` AND IT WAS THE SPAN THAT WAS WRONG, NOT THE THEOREM.**
    # ### It cut Theorem A at the first `Date:` footnote -- and in the arXiv PDF that footnote falls
    # ### BEFORE the `c_MT` definition, which spills onto page 2, while in the Claude paper it falls
    # ### after. ### The same theorem, a different page break. ### **FORM 2 compares the theorem
    # ### proper -- from `Theorem A.` to the sentence ending `respectively` -- and compares the
    # ### `c_MT` definition as its own item wherever each PDF put it.** ### Both yields printed.
    def proper(p):
        ls = lines(p)
        a = next(i for i, l in enumerate(ls) if l.strip().startswith('Theorem A.'))
        b = next(i for i, l in enumerate(ls) if 'respectively' in l and i > a)
        d = next(i for i, l in enumerate(ls) if 'among' in l and 'windows' in l and i > a)
        # ### ### **FORM 3 FOR THE c_MT LINE.** ### The text layer broke the displayed formula across
        # ### lines DIFFERENTLY in the two PDFs -- numerators on one line, denominators on the next --
        # ### so no line-level comparison can decide it. ### The comparison is the MULTISET of
        # ### alphanumeric tokens over the formula's three-line window, which is invariant under how
        # ### the extraction happened to break it and changes if any symbol differs.
        win = span(p, d, d + 2)
        return norm(span(p, a + 1, b + 1)), sorted(re.findall(r'[A-Za-z0-9]+', win.replace('-', '')))
    (cP, cD), (aP, aD) = proper(CP), proper(AF)
    agreeA = (cP == aP) and (cD == aD)
    agreeB = norm(cB) == norm(aB)
    rec('    ### FORM 1 (cut at the first `Date:` footnote) -- Theorem A agrees : %s' % first_form)
    rec('    ### FORM 2 (the theorem proper + the c_MT definition, each located) : %s / %s'
        % (cP == aP, cD == aD))
    rec('    Claude paper, Theorem A at :%d ; Theorem B at :%d' % (ca, cb))
    rec('    2608.13637v2, Theorem A at :%d ; Theorem B at :%d' % (aa, ab))
    rec('    ### ### **THEOREM A AGREES, CHARACTER FOR CHARACTER ON ALPHANUMERICS : %s**' % agreeA)
    rec('    ### ### **THEOREM B AGREES, CHARACTER FOR CHARACTER ON ALPHANUMERICS : %s**' % agreeB)
    rec('    ### the comparison strips the extraction`s spacing and glyph damage and nothing else.')
    rec('    Theorem A (Claude paper, as extracted) :')
    rec('      %s' % cA[:400])
    rec('    Theorem B : %s' % cB[:200])
    find(AF, 'arXiv:2608.13637v2', 'the arXiv version on disk')
    find(AF, 'discovered and written by Claude', 'the arXiv authorship line')
    find(CP, 'We prove unconditionally that at least two thirds', 'the Claude abstract, unconditional')
    find(CP, 'counted with multiplicity, are simple and lie on the critical line', 'what it counts')
    find(CP, 'constants  3  ,  6  ,  0.6725  are  those', 'where 2/3, 5/6, 0.6725 come from')
    find(CP, '(1.2)], and Montgomery', 'the constants: continued')
    find(CP, 'this is optimal [CCLM17', 'the window constant is optimal')
    find(CP, 'The analytic inputs are those of Aryan', 'the cited analytic inputs')
    find(CP, 'The arithmetic inputs are Weil', 'the arithmetic inputs')
    find(CP, 'No mollifier, zero-density estimate', 'what is not used')

    # ---------------------------------------------------------------- (P3) support, window
    rec('')
    rec('(P3) THE SUPPORT CONDITION AND THE WINDOW.')
    rec('-' * 104)
    find(CP, 'Fix  an   even  window', 'the window class')
    find(CP, '(2.6)', 'the two windows, (2.6)')
    find(CP, 'supp          =    [-  L  ,  L  ]', 'the test function`s support')
    find(CP, 'supp(  )  [-L, L] = [- log X, log X]', 'the support against X')
    find(CP, 'With L := l = log(T /2) and', 'L = log(T/2pi): SUPPORT GROWS WITH T')
    find(CP, 'information beyond Fourier support 1', 'bandwidth one, in the paper`s words')
    find(CP, 'insensitive to o(N ) off-line zeros and hold for Davenport', 'the inputs and Epstein')
    rec('    ### ### **THE SUPPORT IS NOT FIXED: L = log(T/2pi), SO THE TEST FAMILY`S SUPPORT GROWS WITH')
    rec('    ### T.** ### In Montgomery`s normalisation that is Fourier support [-1, 1] -- `bandwidth one`.')

    # ---------------------------------------------------------------- (P4) ceiling, residue
    rec('')
    rec('(P4) THE PAPER`S CEILING SENTENCE, AND THE CORPUS`S RESIDUE SENTENCE.')
    rec('-' * 104)
    find(CP, 'The    bandwidth-one          ceiling.', 'the paper`s ceiling sentence, 7.2')
    find(os.path.join(PP, 'FINDINGS.md'), 'the residue at its most compressed (the chiasmus)',
         'the residue`s index line, live')
    find(os.path.join(PP, 'archive', '2026-08-24-ledger-split',
                      'FINDINGS-archive-1-entries-through-2026-08-20c.md'),
         '**The chiasmus', 'the residue sentence, its body')

    # ---------------------------------------------------------------- (P5) the Lean
    rec('')
    rec('(P5) THE LEAN, READ NOT TRUSTED.')
    rec('-' * 104)
    rec('    toolchain   : %s' % read(os.path.join(Z, 'lean-toolchain')).strip())
    m = json.loads(read(os.path.join(Z, 'lake-manifest.json')))
    ml = [p for p in m['packages'] if p['name'] == 'mathlib'][0]['rev']
    rec('    mathlib pin : %s   ### lakefile.toml and lake-manifest.json agree : %s'
        % (ml, ml in read(os.path.join(Z, 'lakefile.toml'))))
    tc = os.path.expanduser('~/.elan/toolchains')
    have = sorted(os.listdir(tc)) if os.path.isdir(tc) else []
    rec('    installed toolchains : %s' % have)
    rec('    ### ### **v4.33.0-rc2 INSTALLED : %s**' % any('v4.33.0-rc2' in h for h in have))

    TRUSTED = ['Challenge.lean', os.path.join('Challenge', 'XiPrime.lean')]
    decls = []
    for f in TRUSTED:
        src = lines(os.path.join(Z, f))
        for i, l in enumerate(src):
            mm = re.match(r'^(theorem|axiom)\s+(\S+)', l)
            if mm:
                j, body = i, []
                while j < len(src):
                    body.append(src[j])
                    if src[j].strip() == 'sorry' or ':= by' in src[j] and 'sorry' in src[j + 1] if j + 1 < len(src) else False:
                        pass
                    if src[j].strip() == 'sorry':
                        break
                    j += 1
                hyps = re.findall(r'\((h\w*)\s*:\s*([^)]*)\)', ' '.join(body))
                decls.append(dict(file=f, line=i + 1, kind=mm.group(1), name=mm.group(2),
                                  statement=NL.join(body), hypotheses=hyps,
                                  sorry=any(b.strip() == 'sorry' for b in body)))
    rec('    trusted-file declarations carrying sorry or axiom : %d' % len(decls))
    for d_ in decls:
        rec('      %-26s :%-4d %-7s %-54s hyps %s'
            % (d_['file'], d_['line'], d_['kind'], d_['name'][:54],
               [h for h, _ in d_['hypotheses']] or '-'))
    axd = [d_ for d_ in decls if d_['kind'] == 'axiom']
    rec('    ### ### **AXIOM DECLARATIONS IN THE TRUSTED FILES : %d.**' % len(axd))
    anyh = sorted(set(h for d_ in decls for h, _ in d_['hypotheses']))
    rec('    ### ### **HYPOTHESES CARRIED BY ANY TRUSTED STATEMENT : %s**' % (anyh or 'NONE'))
    find(os.path.join(Z, 'Challenge.lean'), "The `sorry`s below are deliberate",
         'what the file says of its sorrys')

    rec('')
    rec('  ### THE UNTRUSTED LIBRARY, ON ITS OWN INPUTS -- READ, AND LABELLED A CLAIM UNTIL RUN.')
    find(os.path.join(Z, 'Zeta23', 'Hypotheses.lean'), 'hypotheses are fields of the Prop-valued',
         'the hypothesis boundary')
    find(os.path.join(Z, 'Zeta23', 'Hypotheses.lean'), 'structure PaperInputs', 'PaperInputs')
    find(os.path.join(Z, 'Zeta23', 'Final.lean'), 'theorem paperInputs_zeta', 'PaperInputs DISCHARGED for zeta')
    find(os.path.join(Z, 'Zeta23', 'Final.lean'), 'theorem zetaEF', 'the explicit formula, proved')
    find(os.path.join(Z, 'Zeta23', 'Final.lean'), 'no hypotheses at all', 'the library`s own words')
    # ### ### **THE FIRST SCAN SHELLED OUT TO `grep` AND RETURNED 0 WHERE THE SESSION`S OWN SHELL
    # ### HAD FOUND 2.** ### A Windows process launch does not get the same `grep` the interactive
    # ### shell does, so the count depended on which binary answered. ### Done in Python instead.
    # ### ### **AND THE SECOND SCAN OVER-COUNTED:** `Hypotheses.lean:15` is a line of PROSE in a comment
    # ### that happens to begin with the word `axiom`. ### A regex over raw lines cannot tell a
    # ### declaration from a sentence. ### Form 3 strips Lean comments -- nested `/- ... -/` blocks
    # ### and `--` line comments -- before matching, and every raw hit is still printed with its reason.
    def strip_lean(txt):
        out, i, depth, n = [], 0, 0, len(txt)
        while i < n:
            if txt.startswith('/-', i):
                depth += 1
                i += 2
                continue
            if depth and txt.startswith('-/', i):
                depth -= 1
                i += 2
                continue
            if not depth and txt.startswith('--', i):
                j = txt.find(NL, i)
                i = n if j < 0 else j
                continue
            out.append(txt[i] if not depth or txt[i] == NL else ' ')
            i += 1
        return ''.join(out)
    ax_decl = []
    for dp, dns, fns in os.walk(Z):
        if '.git' in dp or '.lake' in dp:
            continue
        for fn in fns:
            if fn.endswith('.lean'):
                pth = os.path.join(dp, fn)
                for i, l in enumerate(strip_lean(read(pth)).split(NL)):
                    if re.match(r'^\s*(private\s+|protected\s+)?axiom\s', l):
                        ax_decl.append('%s:%d' % (os.path.relpath(pth, Z), i + 1))
    ax_all = []
    for dp, dns, fns in os.walk(Z):
        if '.git' in dp or '.lake' in dp:
            continue
        for fn in fns:
            if fn.endswith('.lean'):
                pth = os.path.join(dp, fn)
                for i, l in enumerate(lines(pth)):
                    if re.match(r'^\s*axiom\s', l):
                        ax_all.append('%s:%d:%s' % (os.path.relpath(pth, Z), i + 1, l.strip()))
    rec('    raw lines beginning with `axiom`, comments NOT stripped : %d' % len(ax_all))
    for a in ax_all:
        why = ('a line of PROSE inside the file`s header comment' if 'Hypotheses' in a
               else 'inside a `/-- ... -/` docstring EXAMPLE of the vendored tactic')
        rec('      %-70s ### %s' % (a[:70], why))
    rec('    ### ### **AXIOM DECLARATIONS, COMMENTS STRIPPED : %d** %s' % (len(ax_decl), ax_decl or ''))

    rec('')
    rec('  ### AUDIT.md, READ AS A CLAIM, AND COMPARED WITH THE TREE IT SITS IN.')
    aud = read(os.path.join(Z, 'AUDIT.md'))
    tree = read(os.path.join(Z, 'Challenge.lean')) + read(os.path.join(Z, 'Solution.lean'))
    named = sorted(set(re.findall(r"^'(\w+)' depends on axioms", aud, re.M)))
    absent = [n for n in named if n not in tree]
    rec('    statements AUDIT.md prints an axiom line for : %d' % len(named))
    rec('    ### ### **OF THOSE, NOT PRESENT IN THIS TREE`S Challenge.lean OR Solution.lean : %d**'
        % len(absent))
    for n in absent[:12]:
        rec('      %s' % n)
    rec('    AUDIT names `Challenge/Multiplicity.lean` : %s ; that file exists here : %s'
        % ('Challenge/Multiplicity.lean' in aud, os.path.exists(os.path.join(Z, 'Challenge', 'Multiplicity.lean'))))
    rec('    ### ### **SO AUDIT.md`S `RECORDED RESULTS AT THIS COMMIT` DESCRIBE A STATEMENT SET THAT IS NOT')
    rec('    ### THIS ONE.** ### It is not evidence about these statements, and is not used as such.')

    rec('')
    rec('  ### THE COMPARISON`S TWO SIDES.')
    pat = re.compile(r'li coefficient|keiper|bombieri.lagarias|blTerm|liCoeff', re.I)
    lih = []
    for dp, dns, fns in os.walk(os.path.join(Z, 'Zeta23')):
        for fn in fns:
            if fn.endswith('.lean'):
                pth = os.path.join(dp, fn)
                lih += ['%s:%d' % (fn, i + 1) for i, l in enumerate(lines(pth)) if pat.search(l)]
    li = NL.join(lih)
    rec('    Li-shaped declarations or prose in the 316 library files : %d' % (len(li.split(NL)) if li else 0))
    find(os.path.join(Z, 'Zeta23', 'Hypotheses.lean'), 'tsupport f ⊆ Icc (-(L / 2)) (L / 2)',
         'the EF`s own support hypothesis')
    lvs = subprocess.run(['git', '-C', LV, 'show', 'v0.10.0:SIDELvConservation/PartialPositivity.lean'],
                         capture_output=True, text=True, encoding='utf-8').stdout
    conj = [l for l in lvs.split(NL) if 'lam n = (∑ z ∈ low, blTerm z n) + tail n' in l]
    rec('    the deposit`s pending conjunct at lv v0.10.0 : %s' % (conj[0].strip() if conj else '### MISS'))
    if not conj:
        MISSES.append(('PartialPositivity.lean', 'second conjunct'))

    rec('')
    rec('=' * 104)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 104)
    io.open(os.path.join(D, 'b468r_extract.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(hashes=hashes, head=head, head_txt=head_txt, clean=dirty == '',
                   thmA_agree=agreeA, thmB_agree=agreeB, thmA_text=cA, thmB_text=cB,
                   mathlib=ml, toolchain_installed=any('v4.33.0-rc2' in h for h in have),
                   trusted=decls, trusted_axioms=len(axd), trusted_hyps=anyh,
                   audit_absent=absent, audit_named=len(named), literal_axioms=ax_all,
                   axiom_declarations=ax_decl,
                   li_hits=(len(li.split(NL)) if li else 0),
                   lv_conjunct=(conj[0].strip() if conj else None), misses=MISSES),
              io.open(os.path.join(D, 'b468r_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
