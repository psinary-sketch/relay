# -*- coding: utf-8 -*-
"""b398_extract.py -- THE EXTRACT AND THE SURVEYS FOR THE LI-WEIL BRIDGE.

### ### **NO NEW COMPUTATION. ### NO INSTRUMENT RUN. ### NO KERNEL BUILT.** ### The order's own
### condition: the question is whether what the record already holds assembles, and ### **AN ACT
### ### THAT COMPUTES SOMETHING NEW HAS CHANGED THE QUESTION.** ### Every figure here is READ from
### the file that emitted it, at its own line, by the anchor tool.
###
### ### **AND THE TWO MARGINS ARE UNFOLDED TO THEIR BASE OBJECTS BEFORE EITHER IS DESCRIBED IN THE
### ### OTHER'S LANGUAGE** -- the order's first instruction, and the reason the place-sets can be
### stated before any comparison is attempted.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import run_clock                # noqa: E402
import b303_pins                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FERRY = os.path.join(D, 'b398_ferry_2026-09-10.txt')
FACES = os.path.join(PP, 'FACES_LEDGER.md')
BALPOS = os.path.join(PP, 'phase1.5', 'spectral', 'BALANCE_AND_POSITIVITY.md')
FINDINGS = os.path.join(PP, 'FINDINGS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def flat(s, n=240):
    return ' '.join(s.split())[:n]


def text_of(p):
    return io.open(p, encoding='utf-8', errors='replace').read()


READS = []


def q(path, hint, label, n=300):
    """### **EVERY QUOTATION IS PULLED BY THE ANCHOR TOOL FROM THE FILE THAT EMITTED IT.**"""
    try:
        i, ln = AF.find(path, hint)
        v = 'ANCHORED'
    except Exception as e:
        i, ln, v = 0, '', ('AMBIGUOUS' if 'AMBIGUOUS' in str(e).upper() else 'ABSENT')
    READS.append(dict(path=os.path.basename(path), label=label, line=i, verdict=v,
                      text=flat(ln, 600)))
    rec('    %s  ### `%s:%s`' % (label, os.path.basename(path), i or '--'))
    if v == 'ANCHORED':
        rec('      > %s' % flat(ln, n))
    else:
        rec('      ### **%s** -- the hint matched %s' % (v, 'many lines' if v == 'AMBIGUOUS'
                                                         else 'nothing'))
    return i, ln


# ==================================================================================================
#  SURVEY 1 -- THE TWO MARGINS, UNFOLDED SIDE BY SIDE.
# ==================================================================================================
def survey1():
    bar('-')
    rec('  ### SURVEY 1 -- THE TWO MARGINS, EACH TO ITS BASE OBJECTS.')
    bar('-')
    rec('  ### ### **THE PLACE-SETS FIRST, BEFORE ANY COMPARISON** -- the order`s own instruction.')
    rec()
    rec('  ### **(A) THE SONIN OBJECT`S PLACE-SET.**')
    q(os.path.join(D, 'b197_values_and_c0.txt'),
      'for every finite S containing',
      '### **THE THEOREM THE RECORD READ, AND THE WITHDRAWAL IT FORCED**', 460)
    q(os.path.join(D, 'b197_values_and_c0.txt'),
      'the summand shape "Tr_infinity + SUM_p Tr_p" is WITHDRAWN',
      '### **THE WITHDRAWN SHAPE, NAMED**', 380)
    rec('  ### ### **SO THE SONIN OBJECT IS ARCHIMEDEAN-ONLY, AND NOT BY OMISSION:** ### the')
    rec('  ### ### semilocal Sonin space is ### **ONE ARCHIMEDEAN COPY**, and ### **FINITE PLACES')
    rec('  ### ### CONTRIBUTE NO INDEPENDENT SONIN DIRECTIONS** -- read-refuted by Theorem 2 of')
    rec('  ### ### `2310.18423`, and the shape `Tr_infinity + SUM_p Tr_p` is ### **WITHDRAWN.**')
    rec('  ### ### ### **PLACE-SET OF THE SONIN MARGIN : `{infinity}`.**')
    rec()
    rec('  ### **(B) THE LI OBJECT`S PLACE-SET.**')
    q(FACES, 'in which S∞(n) and Sf(n) correspond to the contributions of the archimedean place',
      '### **THE SOURCE`S OWN DECOMPOSITION**', 420)
    rec('  ### ### ### **PLACE-SET OF THE LI MARGIN : `{infinity} UNION {all finite places}`,')
    rec('  ### ### ### PLUS A POLE TERM AT `s = 0` THAT IS NOT A PLACE AT ALL.**')
    rec()
    rec('  ### ### ### **(F1) IS MET AT THE FIRST THING PRINTED: THE PLACE-SETS DIFFER.**')
    rec()
    bar('-')
    rec('  ### THE SONIN MARGIN, CONSTITUENT BY CONSTITUENT.')
    bar('-')
    q(FACES, 'F2 -- the Sonin margin: W_∞(f) − Tr(θ(g) S θ(g)*) on f = g conv g^#',
      '(1) THE MARGIN, THE TEST CLASS AND THE SUPPORT CONDITION', 340)
    q(os.path.join(D, 'b333_derive_run.txt'),
      '(151) -> (152)-(153): W_inf = -W_R',
      '(2) THE ARCHIMEDEAN DISTRIBUTION AND ITS IDENTIFICATION', 300)
    q(os.path.join(D, 'b327_bridge_run.txt'),
      'the archimedean distribution 2 Re(Gamma_R', '(3) THE KERNEL BOTH CHANNELS EVALUATE', 340)
    q(os.path.join(D, 'b324_the_keystones_reread.txt'),
      'into a ZERO channel and an archimedean channel, against',
      '(4) THE DECOMPOSITION, AND THE OPERATOR', 300)
    q(os.path.join(D, 'b324_the_keystones_reread.txt'),
      'none, against `S` the orthogonal projection', '(5) THE OPERATOR, NAMED', 300)
    rec()
    bar('-')
    rec('  ### THE LI MARGIN, CONSTITUENT BY CONSTITUENT.')
    bar('-')
    q(FACES, 'F3 -- the Li margin: M(n) := λ_Z(n) + λ_A(n) = λ_n',
      '(1) THE MARGIN AND ITS TWO CHANNELS', 300)
    q(FACES, "own words: *\"f_A(s) = log s",
      '(2) THE SPLIT, IN THE KEYSTONE`S OWN WORDS', 340)
    q(FACES, 'The special test functions Gn(s)',
      '(3) THE FAMILY AND ITS WEIL NORM', 300)
    q(FACES, 'gives λ_A(n) = S∞(n) + 1 for every n ≥ 1',
      '(4) THE POLE CONSTANT, DERIVED AT b327 UNDER A SEALED BAR', 380)
    q(os.path.join(D, 'b327_bridge_run.txt'), 'whose second term is the finite places, lambda_Z',
      '(5) ### **THE PRIME SUMMAND, BANKED**', 420)
    rec()
    rec('  ### ### **AND THE PROGRAMME`S OWN CAUTION ABOUT ITS SPLIT, QUOTED:**')
    q(FACES, "The programme's split is not S_∞/S_NA over places",
      '(6) THE SPLIT IS NOT A PLACE-SPLIT', 240)
    return dict(reads=len(READS))


# ==================================================================================================
#  SURVEY 2 -- THE READING'S TWO HALVES, EACH TESTED AGAINST THE RECORD.
# ==================================================================================================
def survey2():
    bar('-')
    rec('  ### SURVEY 2 -- THE NAVIGATOR`S READING, IN TWO HALVES, EACH TESTED.')
    bar('-')
    rec('  ### ### **AND THE FIRST FORM OF THIS SURVEY GOT IT BACKWARDS.** ### It read `b197`\'s')
    rec('  ### ### withdrawal of the shape `Tr_infinity + SUM_p Tr_p` as covering the premise and')
    rec('  ### ### called the reading refuted. ### **`b197` ITSELF FORBIDS THAT READING**, in a')
    rec('  ### ### sentence written to stop exactly this:')
    q(os.path.join(D, 'b197_values_and_c0.txt'),
      'THAT WITHDRAWAL IS ABOUT THE **SONIN** TRACE SUMMAND',
      '### **THE WARNING THIS SEAT WALKED INTO**', 420)
    q(os.path.join(D, 'b197_values_and_c0.txt'),
      "E's SHAPE, AND IS RECORDED HERE SO THAT NOBODY LATER READS IT AS IF IT DID",
      '### **AND WHY IT WAS WRITTEN DOWN**', 300)
    rec('  ### ### **THE WITHDRAWAL COVERS A SONIN-TRACE DECOMPOSITION OVER PLACES. ### IT DOES')
    rec('  ### ### NOT COVER THE FINITE SIDE ROUTED THROUGH THE QUOTIENT CHANNEL**, which is what')
    rec('  ### ### the reading describes and what the clause statement banks.')
    rec()
    rec('  ### **HALF ONE, ASSERTED:** ### *at a finite place the source`s construction on the')
    rec('  ### object returns the test function at the identity times the constrained dimension,')
    rec('  ### carrying no logarithm and no sampling at prime powers.*')
    rec('  ### ### **TESTED : BANKED, AND AT KERNEL TERMINALS.**')
    q(FINDINGS, 'The places sum, unfolded as the arc realized it',
      '### **THE CLAUSE STATEMENT`S OWN WORDS**', 460)
    q(FINDINGS, '| **K3** the finite places’ contribution | KERNEL TERMINALS:',
      '### **K3, UNFOLDED TO ITS OWNER**', 520)
    rec('  ### ### **`B329.*` (24, ZERO-AXIOM) AND `B310.*` CARRY IT, AND THE DECOMPOSITION AND')
    rec('  ### ### SCALING PARTS ARE GENERAL.** ### The reading`s first half is not a conjecture')
    rec('  ### ### about the record; ### **IT IS A QUOTATION OF IT.**')
    rec()
    rec('  ### **HALF TWO, ASSERTED:** ### *the corpus`s prime summand IS the source`s local Weil')
    rec('  ### term factor for factor.*')
    rec('  ### ### **TESTED : BANKED, VERBATIM, WITH ONE STATED EXCEPTION.**')
    q(FINDINGS, '| **K4** the prime sum | a derivation on content:',
      '### **K4, UNFOLDED TO ITS OWNER**', 520)
    rec('  ### ### **`the corpus`s prime side IS the source`s finite-places sum, factor for')
    rec('  ### ### factor`** -- and ### **`DIFFERENT ONLY IN THE CUTOFF WINDOW (b306)`**, which')
    rec('  ### ### the act carries rather than drops.')
    rec('  ### ### **AND THE SECOND, INDEPENDENT DESCRIPTION THE RECORD ALSO HOLDS:**')
    q(os.path.join(D, 'b327_bridge_run.txt'), 'whose second term is the finite places, lambda_Z',
      '### `lambda_Z(n) = -S_f(n)`, derived at `b327`', 420)
    rec('  ### ### **SO BOTH HALVES OF THE READING ARE BANKED.** ### The seat`s first reading was')
    rec('  ### ### wrong and is corrected here, before the lock, with the file that caught it')
    rec('  ### ### quoted above.')
    rec()
    rec('  ### **WHAT THE READING THEN NEEDS, AND WHAT THE RECORD DOES NOT HOLD.**')
    rec('  ### The conclusion is that the Sonin margin read place-wise, plus the finite')
    rec('  ### dimensional terms, IS the Weil functional. ### Unfolded:')
    rec('  ###   the Sonin margin is  ### **`W_inf(f) - Tr(theta(g) S theta(g)*)`**')
    rec('  ###   the Weil functional is ### **`W_inf(f) + SUM_p W_p(f)`**')
    rec('  ### ### **THE TWO AGREE IF AND ONLY IF `-Tr(theta(g) S theta(g)*) = SUM_p W_p(f)`.**')
    rec('  ### ### **AND THAT IDENTIFICATION IS EXACTLY WHAT THE LEDGER TYPES AS OWED.**')
    q(FACES, 'the margins differ at their second term (a compressed square against the finite',
      '### **THE LEDGER`S OWN TYPING OF WHAT IS MISSING**', 420)
    rec('  ### ### **THE FINITE-PLACE TERMS ARE BANKED (K3) AND THE COMPRESSED SQUARE IS BANKED')
    rec('  ### ### (b320, b321, and the source`s Theorem 4.7). ### WHAT IS NOT BANKED IS THAT')
    rec('  ### ### THEY ARE THE SAME OBJECT.** ### `b324`, constituent (4), on the square:')
    q(os.path.join(D, 'b324_the_keystones_reread.txt'), 'The square is not a zero channel',
      '### **AND THE SQUARE IS NOT A ZERO CHANNEL**', 300)
    rec()
    rec('  ### **AND A SECOND OBSTRUCTION, INDEPENDENT OF THE FIRST, WHICH THE READING`S LAST')
    rec('  ### CLAUSE RUNS INTO:** ### the reading ends ### *which is what the Li margin evaluates')
    rec('  ### on its own family.*')
    q(os.path.join(D, 'b327_bridge_run.txt'), 'is a rational function whose inverse Mellin',
      '### **THE FAMILY OBSTRUCTION**', 460)
    rec('  ### ### **THE SONIN MARGIN IS NOT DEFINED ON THE LI FAMILY.** ### So even with the')
    rec('  ### ### identification, the two sides would be ### **ONE FUNCTIONAL EVALUATED ON TWO')
    rec('  ### ### DISJOINT FAMILIES** -- which is what `b327` already banked, and which is a')
    rec('  ### ### decomposition of neither into the other:')
    q(os.path.join(D, 'b327_bridge_run.txt'),
      'ONE DISTRIBUTION ON TWO FAMILIES, NOT ONE FUNCTIONAL', '### b327`s verdict', 300)
    rec()
    rec('  ### ### ### **THE VERDICT : UNDECIDABLE FROM THE RECORD.** ### Both premises are')
    rec('  ### ### ### banked; the conclusion needs one statement the record does not hold; and')
    rec('  ### ### ### the ledger already types that statement as owed. ### **THE READING IS')
    rec('  ### ### ### NEITHER ADOPTED NOR REFUTED -- IT IS SHOWN TO REST ON THE OWED BRIDGE')
    rec('  ### ### ### ITSELF**, which is why no amount of re-reading closes it.')
    rec('  ### ### **THE EXACT MISSING STATEMENT, TYPED:**')
    rec('  ###   ### **(M)** ### for every `g` in the source`s class, `-Tr(theta(g) S theta(g)*) =')
    rec('  ###   SUM_p W_p(g conv g-bar^#)` in the source`s normalization.')
    rec('  ###   ### **TYPE : A RESULT.** ### Not a read: no file states it. ### Not a ruling: it')
    rec('  ###   is a mathematical identity, not an author`s choice. ### Not a construction: both')
    rec('  ###   sides already exist in the record. ### **IT IS A DERIVATION ON CONTENT, AND IT IS')
    rec('  ###   ### THE OWED BRIDGE`S FIRST HALF.**')
    rec('  ### ### **AND `(F2)` IS MET: UNDECIDABLE, NOT ASSEMBLES.** ### But the order`s reason')
    rec('  ### ### is ### **NOT** ### the one the measurement found: the order expected a')
    rec('  ### ### normalization never fixed across the two families, and the missing statement is')
    rec('  ### ### an ### **IDENTIFICATION OF TWO SECOND TERMS AT ONE PLACE-SET**, prior to any')
    rec('  ### ### question about families. ### **A PREDICTION MET FOR A DIFFERENT REASON IS')
    rec('  ### ### REPORTED WITH THE REASON.**')
    return dict(verdict='UNDECIDABLE FROM THE RECORD', half_one='BANKED', half_two='BANKED',
                missing='(M) -Tr(theta(g) S theta(g)*) = SUM_p W_p(g conv g-bar^#)',
                missing_type='RESULT', f2='MET, for a different reason',
                self_correction=True, reads=len(READS))


# ==================================================================================================
#  SURVEY 3 -- THE LEDGER'S OWED ROW, AND THE TRIGGER COLUMN.
# ==================================================================================================
def survey3():
    bar('-')
    rec('  ### SURVEY 3 -- THE OWED ROW, AND THE TRIGGER COLUMN `(R23)` SWEEPS.')
    bar('-')
    q(FACES, 'THE LIVE ROW L1 READS IT: the archimedean distribution is one on both families',
      '### **THE OWED ROW, AS THE LEDGER ALREADY TYPES IT**', 420)
    rec()
    # ### **THE TRIGGER SWEEP, BOUNDED BY THE TABLE THAT HAS A TRIGGER COLUMN.**
    # ### An earlier form of this survey looked for `| none |` anywhere and returned `51` rows --
    # ### and a sweep that keeps fifty-one is not a sweep. ### **THE FACES LEDGER HAS NO TRIGGER
    # ### ### COLUMN AT ALL** (its pair table is `pair | kind | relation`, and its `NONE` means
    # ### *the record states no relation*), so the order's `none` lives in `OPEN_TRAILS.md`'s
    # ### WORK-ORDER TABLE, whose header names `trigger` as its last column. ### **THAT TABLE IS
    # ### ### THE POPULATION, AND IT IS FOUND BY ITS OWN HEADER AND NOT BY A LINE NUMBER.**
    TR = os.path.join(PP, 'OPEN_TRAILS.md')
    lines = text_of(TR).split(chr(10))
    hdr = [i for i, ln in enumerate(lines, 1)
           if ln.startswith('| | trail | species | what is owed') and 'trigger' in ln]
    rec('  ### **THE WORK-ORDER TABLE, FOUND BY ITS OWN HEADER : line(s) %s.**' % hdr)
    hits = []
    for h in hdr:
        for i in range(h + 2, min(h + 40, len(lines) + 1)):
            ln = lines[i - 1]
            if not ln.startswith('|'):
                break
            cells = [c.strip() for c in ln.strip().strip('|').split('|')]
            wid = next((c for c in cells if 'W-ORD-' in c), '')
            trig = cells[-1] if cells else ''
            rec('      line %d  %-34s trigger : `%s`' % (i, wid[:34], trig))
            if trig.lower().strip('`. ') == 'none':
                hits.append((os.path.basename(TR), i, wid.strip('`'), flat(ln, 200)))
    rec('  ### ### **ROWS WHOSE TRIGGER READS `none` : `%d`.**' % len(hits))
    for _f, i, w, _l in hits:
        rec('  ###     line %-6d %s' % (i, w))
    rec('  ### ### **AND `(R23)` NAMES THE FIRST ONE`S NEW TRIGGER ITSELF:** ### *THE AUTHOR`S')
    rec('  ### ### WORD*, and this paste is that word. ### The other two must each be given a')
    rec('  ### ### firable trigger or be marked ### **SHELVED WITH THE REASON.**')
    return dict(none_rows=len(hits), header=hdr,
                rows=[(i, w) for _f, i, w, _l in hits])


# ==================================================================================================
#  SURVEY 4 -- THE CLAUSE ANCHOR, FOR COMPONENT 4.
# ==================================================================================================
def survey4():
    bar('-')
    rec('  ### SURVEY 4 -- THE CLAUSE ANCHOR.')
    bar('-')
    lines = text_of(FINDINGS).split(chr(10))
    ca = [(i + 1, ln) for i, ln in enumerate(lines)
          if 'clause-stated' in ln or 'THE OPEN CLAUSE' in ln.upper()]
    rec('  ### **THE CLAUSE ANCHOR IN `FINDINGS.md` : `%d` line(s).**' % len(ca))
    for i, ln in ca[:4]:
        rec('      FINDINGS.md:%d' % i)
        rec('      > %s' % flat(ln, 300))
    return dict(clause_lines=[i for i, _l in ca][:8])


def refs():
    o = {}
    for name, repo in b303_pins.REPOS:
        r1 = subprocess.run(['git', '-C', repo, 'rev-parse', '--abbrev-ref', 'HEAD'],
                            capture_output=True, text=True, encoding='utf-8', errors='replace')
        r2 = subprocess.run(['git', '-C', repo, 'rev-parse', 'HEAD'], capture_output=True,
                            text=True, encoding='utf-8', errors='replace')
        o[name] = dict(branch=(r1.stdout or '').strip(), head=(r2.stdout or '').strip()[:12])
    return o


def main():
    rec('### run at (UTC) : %s   ### NOT COVERED BY ANY HASH.' % run_clock.stamp())
    bar('=')
    rec('b398 -- THE EXTRACT, AND THE SURVEYS THE FACE IS WRITTEN FROM.')
    bar('=')
    R = refs()
    for k, v in R.items():
        rec('    %-22s `%s` = `%s`' % (k, v['branch'], v['head']))
    rec()
    q(FERRY, 'ACT b398 — THE LI–WEIL BRIDGE', '### THE ORDER', 200)
    q(FERRY, 'RULING (R23), the author', '### THE RULING', 200)
    rec()
    s1 = survey1()
    rec()
    s2 = survey2()
    rec()
    s3 = survey3()
    rec()
    s4 = survey4()
    rec()
    bar('=')
    anch = sum(1 for r in READS if r['verdict'] == 'ANCHORED')
    amb = sum(1 for r in READS if r['verdict'] == 'AMBIGUOUS')
    abs_ = sum(1 for r in READS if r['verdict'] == 'ABSENT')
    rec('  reads %d ; ANCHORED %d ; AMBIGUOUS %d ; ABSENT %d' % (len(READS), anch, amb, abs_))
    rec('  3 : trigger-none rows %d' % s3['none_rows'])
    rec('  4 : clause lines %s' % s4['clause_lines'][:4])
    rec('  ### **NO COMPUTATION WAS RUN. ### NO INSTRUMENT WAS RUN. ### NO KERNEL WAS BUILT.**')
    bar('=')
    p = run_clock.write(D, 'b398_extract_notes', L)
    json.dump(dict(reads=READS, anchored=anch, ambiguous=amb, absent=abs_,
                   s3=s3, s4=s4, refs=R,
                   run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
              io.open(os.path.join(D, 'b398_reads.json'), 'w', encoding='utf-8'), indent=1)
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
