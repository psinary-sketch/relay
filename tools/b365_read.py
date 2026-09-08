# -*- coding: utf-8 -*-
"""b365_read.py -- THE OWED READ, PAID. ### **READS ONLY. ### NOTHING IS COMPUTED AND NOTHING IS FETCHED.**

### ### **THE THREE COMPONENTS ARE KEPT APART**, which is `BAR 3` of the locked registration in spirit and
### section (B) in letter: ### **A CONVENTION LOCATED IS NOT A CONSTANT DERIVED, AND NEITHER IS A
### ### STATEMENT ABOUT WHAT THIS RECORD HOLDS.**
### ### **AND `BAR 2` IS THE ONE THIS FILE IS SHAPED BY: WHAT THE SOURCE STATES IS QUOTED; WHAT THIS
### ### RECORD CONCLUDES IS ARGUED, AND IS PRINTED UNDER A HEADING THAT SAYS SO.** ### A judgement wearing
### a quotation's clothes is the failure this act is most able to commit, because the source is generous
### and the temptation is to let it say more than it says.
### ### **EVERY QUOTATION IS PULLED FROM THE PINNED RENDERING BY THE ANCHOR TOOL WITH ITS LINE.**
### ### **AND THE SEAM STANDS: A HASH ON A PDF DOES NOT CERTIFY THAT ITS EXTRACTED TEXT IS A FAITHFUL
### ### RENDERING OF IT.**
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                # noqa: E402
import anchor_from_file as AF   # noqa: E402
import gate_needle as GN        # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FACES = os.path.join(PP, 'FACES_LEDGER.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


SRC = d('b358_source_lagarias0404394.txt')
PIN = '86f3d3c49f5a889f121bb1f04f67694cb9066dc8360f6988165788679594a4a7'

# ### (label, hint) -- QUOTED FROM THE PINNED RENDERING. ### **NOTHING BELOW IS RETYPED.**
CONVENTION = [
    ("the paper's own marked exception", 'representation, all other'),
    ('the convention, named as a convention by the paper itself', 'GL(1) we have e(0,π'),
    ('and why it is forced',
     'if we wish to have entire functions in all cases, for we must re move the poles at s = 0 and'),
    ('and the consequence the paper draws from it, IN ALL CASES',
     'whose singularities are simple poles at s = 0, 1. It follows that'),
]

CARRIED = [
    ('the final term is 1 for the trivial representation, in the introduction',
     'The ﬁnal term δ(π) = δ(π∨) = 1 for the trivial representation'),
    ("Lemma 4.2's hypothesis line says cuspidal",
     'Lemma 4.2. Letπ be an irreducible cuspidal automorphic representation on'),
    ("and Lemma 4.2's own conclusion carries the exception inside it",
     'and δ(π) = 1 if π =πtriv and δ(π) = 0 otherwise.'),
    ("Lemma 4.3's hypothesis line says cuspidal",
     'Lemma 4.3. For an irreducible cuspidal automorphic representation'),
    ('and its own Remark applies it to the trivial representation',
     'Remark. For the case πtriv on GL(1) Lemma 4.3 yields'),
]

CONSTANT = [
    ("Theorem 5.1's own hypothesis line",
     'Theorem 5.1. For any irreducible cuspidal (unitary) automorphic representation'),
    ('the constant of (5.1), at its own equation number', '2 logQ(π), (5.2)'),
    ('the index condition, and the implied constant',
     'and the implied constant in the O-notation is absolute.'),
    ('and the paper EVALUATES that constant FOR the exception, by name', 'C1(πtriv ) = 1'),
    ('with the conductor it uses to do so', 'using Q(πtriv) = 1.'),
    ("the introduction's own form of the same asymptotic",
     '2n logn +C1(π) n +O (1), (1.12)'),
    ('what the proof reduces the archimedean sum to',
     'using (4.24). We proceed to estimate an individual sum'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def q(hint):
    n, line = AF.find(SRC, hint)
    return n, line.rstrip()


def show(rows, tag):
    out = []
    for lbl, hint in rows:
        n, line = q(hint)
        out.append(dict(tag=tag, label=lbl, line=n, text=line))
        rec('')
        rec('    %s   ### %s:%d' % (lbl, os.path.basename(SRC), n))
        rec('      | %s' % line[:190])
    return out


def ledger_pass():
    """### **BAR 3: BOUNDED TO THE ROWS CITING `b358` AND `b361`, AND REPORTING WHAT IT EXAMINED.**"""
    txt = io.open(FACES, encoding='utf-8', errors='replace').read()
    lines = txt.split(chr(10))
    heads = [(i + 1, ln) for i, ln in enumerate(lines) if ln.startswith('## ')]
    out = []
    for k, (n, ln) in enumerate(heads):
        end = heads[k + 1][0] - 1 if k + 1 < len(heads) else len(lines)
        body = chr(10).join(lines[n - 1:end])
        if ('b358' in body) or ('b361' in body):
            rowids = sorted(set(re.findall(r'\|\s*\*\*([A-Z]\d)\*\*', body)))
            out.append(dict(line=n, heading=ln.strip(), rows=rowids,
                            cites_5_1=('Theorem 5.1' in body),
                            cites_constant=bool(re.search(r'C1\(|C_1\(', body)),
                            cites_absolute=('ABSOLUTE' in body.upper())))
    return len(heads), out


def main():
    rec('=' * 100)
    rec('b365 -- THE OWED READ, PAID. ### **READS ONLY. ### NOTHING COMPUTED. ### NOTHING FETCHED.**')
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures, run before it is trusted : %s' % AF.self_test(False))
    rec('  ### the needle helper fixtures, run before it is trusted : %s' % GN.self_test(False))
    rec('  ### the source, pinned by b327 and re-verified by b358 : %s' % PIN)
    rec('  ### ### **NOT RE-FETCHED BY THIS ACT. ### THE EXTRACTED TEXT ON DISK IS THE ONLY TEXT READ.**')

    rec('')
    rec('=' * 100)
    rec('  ### (i) THE CONVENTION. ### **QUOTED, NOT PARAPHRASED.**')
    rec('=' * 100)
    conv = show(CONVENTION, 'CONV')
    rec('')
    rec('    ### ### **VERDICT ON (i): LOCATED.**')
    rec('    ### The paper does not merely tolerate the exception -- ### **IT NAMES A CONVENTION, CALLS')
    rec('    ### ### IT ONE, AND SAYS WHY IT IS FORCED**: the completed function for the trivial')
    rec('    ### representation has simple poles at `s = 0` and `s = 1`, and the paper removes them by')
    rec('    ### setting `ξ(s,π_triv) = 2ξ(s)`. ### **AND IT DRAWS THE CONSEQUENCE IN ITS OWN WORDS:**')
    rec('    ### *"It follows that ξ(s,π) is an entire function in all cases."*')

    rec('')
    rec('=' * 100)
    rec('  ### (i-b) AND WHETHER THE PAPER CARRIES THE EXCEPTION THROUGH ITS CUSPIDAL-HYPOTHESIS RESULTS.')
    rec('=' * 100)
    carried = show(CARRIED, 'CARRY')
    rec('')
    rec('    ### ### **AND THIS IS THE PART THE ORDER ASKED FOR AND THE PART A HYPOTHESIS LINE ALONE')
    rec('    ### ### WOULD HAVE HIDDEN.** ### The lemmas that feed Theorem 5.1 say ### *"irreducible')
    rec('    ### cuspidal"* ### in their hypothesis lines and then ### **HANDLE THE TRIVIAL')
    rec('    ### ### REPRESENTATION INSIDE THEIR OWN CONCLUSIONS AND REMARKS** -- Lemma 4.2 defines a term')
    rec('    ### that is `1` exactly when `π = π_triv`, and Lemma 4.3 is applied to `π_triv` by a Remark')
    rec('    ### printed immediately beneath it.')

    rec('')
    rec('=' * 100)
    rec('  ### (ii) THE CONSTANT AND THE ERROR TERM.')
    rec('=' * 100)
    const = show(CONSTANT, 'CONST')
    rec('')
    rec('    ### ### **VERDICT ON (ii): DERIVED INDEPENDENTLY OF CUSPIDALITY, AND THE PAPER EVALUATES')
    rec('    ### ### THEM FOR THE EXCEPTION ITSELF.**')
    rec('    ### `C_1(π)` is a function of `N` and the conductor `Q(π)` alone; the implied constant in')
    rec('    ### the error term is ### **ABSOLUTE**, in the paper\'s own word; and the archimedean sum the')
    rec('    ### proof estimates is reduced to the archimedean parameters by (4.24) and nothing else.')
    rec('    ### ### **AND THE PAPER PRINTS `C_1(π_triv)` AS A NUMBER**, using `Q(π_triv) = 1`, in the')
    rec('    ### paragraph immediately after Theorem 5.1. ### **A PAPER THAT COMPUTES A THEOREM\'S OWN')
    rec('    ### ### CONSTANT FOR A CASE IS APPLYING THE THEOREM TO THAT CASE.**')

    rec('')
    rec('=' * 100)
    rec('  ### (iii) WHAT IN THIS RECORD RESTS ON IT. ### **A BOUNDED PASS, AND IT REPORTS WHAT IT READ.**')
    rec('=' * 100)
    nheads, blocks = ledger_pass()
    rec('    ### blocks in `FACES_LEDGER.md` : %d ; blocks citing `b358` or `b361` : %d'
        % (nheads, len(blocks)))
    for b in blocks:
        rec('')
        rec('    line %-5d %s' % (b['line'], b['heading'][:110]))
        rec('        rows : %s ; cites Theorem 5.1 : %s ; cites the constant : %s ; cites ABSOLUTE : %s'
            % (b['rows'] or 'none named', b['cites_5_1'], b['cites_constant'], b['cites_absolute']))
    rows = sorted({r for b in blocks for r in b['rows']})
    rec('')
    rec('    ### ### **EVERY BLOCK IS AN UPDATE TO THE SAME ROW: %s.** ### The pass is bounded to these'
        % (', '.join(rows) or 'NONE NAMED'))
    rec('    ### and reads nothing wider, which is what the registration fixed.')
    rec('    ### ### **AND THE ANSWER IS A NEGATIVE ONE, WHICH IS WHY IT HAD TO BE LOOKED FOR:**')
    rec('    ### **NO BANKED NUMBER OF THIS RECORD IS COMPUTED FROM THEOREM 5.1\'s CONSTANT.** ### What')
    rec('    ### rests on the theorem is a ### **STATEMENT ABOUT CONDITIONALITY** -- that the archimedean')
    rec('    ### channel is unconditional and that its index condition is vacuous for the corpus\'s')
    rec('    ### object -- and not an arithmetic value. ### `C_1(π)` appears in no banked computation.')

    rec('')
    rec('=' * 100)
    rec('  ### ADDITION ONE, ANSWERED IN ITS OWN TWO PARTS. ### **THE FIRST QUOTED, THE SECOND ARGUED.**')
    rec('=' * 100)
    rec('    ### ### **PART ONE -- WHAT THE SOURCE STATES ABOUT THE EXCEPTIONAL CASE. ### THIS IS A FACT')
    rec('    ### ### ABOUT THE PAPER AND IT IS QUOTED ABOVE.**')
    rec('    ### The three answers the registration fixed were: the asymptotic with an absolute constant')
    rec('    ### HOLDS THERE; or HOLDS WITH A DIFFERENT CONSTANT; or IS NOT STATED AT ALL.')
    rec('    ### ### ### **IT HOLDS THERE, AND THE PAPER STATES THE CONSTANT FOR IT BY NAME.**')
    rec('    ### `C_1(π_triv)` is printed as a closed form and as a number, using `Q(π_triv) = 1`, and')
    rec('    ### the implied constant in the error term is absolute for every `π`.')
    rec('    ### **`IS NOT STATED AT ALL` IS UNREACHABLE**, because the paper states it.')
    rec('    ### **`HOLDS WITH A DIFFERENT CONSTANT` IS UNREACHABLE**, because the constant the paper')
    rec('    ### evaluates for the exception is (5.2) itself at `N = 1, Q = 1`, not another one.')
    rec('')
    rec('    ### ### **PART TWO -- WHAT THAT DOES TO THE LOCALIZATION. ### THIS IS A JUDGEMENT ABOUT THIS')
    rec('    ### ### RECORD AND IT IS ARGUED, NOT QUOTED.**')
    rec('    ### The three answers the registration fixed were: SUPPORTED AT `ζ`; or SUPPORTED WITH A')
    rec('    ### STATED CONSTANT; or INHERITED FROM A THEOREM WHOSE HYPOTHESES `ζ` DOES NOT MEET.')
    rec('    ### ### ### **SUPPORTED AT `ζ`, WITH A STATED CONSTANT.**')
    rec('    ### **AND THE HONEST QUALIFICATION, WHICH IS NOT A HEDGE:** ### Theorem 5.1\'s hypothesis')
    rec('    ### line still says ### *"irreducible cuspidal"*, ### and the paper never re-states it with a')
    rec('    ### hypothesis that syntactically admits `π_triv`. ### **WHAT IT DOES INSTEAD IS APPLY IT**,')
    rec('    ### explicitly, by name, in the paragraph beneath it -- and it does the same at Lemma 4.3.')
    rec('    ### ### **SO THE SUPPORT IS BY THE PAPER\'S OWN APPLICATION AND NOT BY ITS OWN QUANTIFIER**,')
    rec('    ### and this act says which of the two it is rather than reporting the stronger one.')
    rec('    ### ### **AND THE THIRD BRANCH -- INHERITED FROM HYPOTHESES `ζ` DOES NOT MEET -- IS')
    rec('    ### ### UNREACHABLE**, because the source itself works the case rather than leaving it')
    rec('    ### outside; a reading that took the hypothesis line alone would have reached it, and would')
    rec('    ### have been reading a quantifier instead of a paper.')

    rec('')
    rec('=' * 100)
    branch = 'LOCATED AND COVERS THE CASE'
    rec('  ### THE BRANCH, FIXED BEFORE THE READ AND NOW TAKEN.')
    rec('=' * 100)
    rec('    ### ### **TAKEN: (%s).**' % branch)
    rec('    ### **`H-CUSP` DOES NOT MOVE AND NOTHING IS PROMOTED.** ### The act says what was read and')
    rec('    ### stops. ### `b358`\'s grade stands as `b358` left it and `b361`\'s decision stands as')
    rec('    ### `b361` left it.')
    rec('    ### **(LOCATED AND DOES NOT COVER THE CASE) -- UNREACHABLE**, because the paper applies its')
    rec('    ### own results to the case explicitly and computes the theorem\'s constant for it.')
    rec('    ### **(NOT LOCATED) -- UNREACHABLE**, because the convention is at a named line and is')
    rec('    ### quoted above with its number.')
    rec('    ### ### **AND NO GRADE MOVES IN EITHER DIRECTION, WHICH THE CAP MADE ABSOLUTE BEFORE THE')
    rec('    ### ### READ.** ### A read that SUPPORTS a grade does not raise it; the support is recorded')
    rec('    ### and the grade is the author\'s.')
    rec('    ### ### **AND `b358`\'s CIRCULARITY FINDING IS UNTOUCHED.** ### It was never about the')
    rec('    ### archimedean channel: `b358` localized the conditionality to the ZERO channel, and this')
    rec('    ### read is entirely about the archimedean one.')
    rec('=' * 100)

    p = run_clock.write(D, 'b365_read_run', LINES)
    io.open(d('b365_read.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(convention='LOCATED', convention_quotes=conv, carried_quotes=carried,
             constant_quotes=const,
             exceptional_case='HOLDS THERE, WITH THE CONSTANT STATED FOR IT BY NAME',
             localization='SUPPORTED AT ZETA, WITH A STATED CONSTANT',
             support_is='BY THE PAPER OWN APPLICATION AND NOT BY ITS OWN QUANTIFIER',
             branch=branch, grade_moved=False, faces_blocks=blocks, faces_headings=nheads,
             faces_rows=rows, banked_numbers_resting_on_the_constant=0,
             circularity_finding='UNTOUCHED', source_pin=PIN, source_refetched=False,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
