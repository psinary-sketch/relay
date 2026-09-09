# -*- coding: utf-8 -*-
"""b381_exemplars.py -- COMPONENT 1. ### **THE OLD CONTROL'S WEAKNESS, THEN THE REBUILD.**

### ### **THE TWO FACTS ARE ONE FINDING.** ### `b380`'s threshold was `2` and every synthesis
### declarer's reach cleared it, so ### **NO VALUE OF THE THRESHOLD WOULD HAVE FAILED THEM**; and both
### gathering declarers disagreed, so ### **THE ONLY SIDE THAT COULD HAVE INFORMED THE PREDICATE WAS
### ### THE SIDE IT GOT WRONG.** ### A control that cannot fail on one side and cannot inform on the
### other is not two defects. ### **IT IS ONE.**

### ### **THE REBUILD IS LEXICAL AND POSITIONAL AND NOTHING IS CURATED.** ### Every match is taken,
### every match is quoted with its file and its line, and ### **NO EXEMPLAR IS ADDED, DROPPED OR RANKED
### ### BY THIS SEAT'S JUDGEMENT OF WHAT A DOCUMENT IS.**

### ### ### **THE LEXICON IS COMMITTED HERE, BEFORE THE COUNTS EXIST.** ### The order names three
### verbs -- `record, collect, or certify`. ### Taken alone they are the order's own words and nothing
### else; taken with the gathering family they are what the phrase MEANS. ### **THE WIDE FAMILY IS THE
### ### EXEMPLAR SET AND THE ORDER'S THREE VERBS ARE REPORTED BESIDE IT**, so a reader sees exactly
### what each yields and neither is chosen after the fact.

### ### **AND THE DENIAL READING IS RUN TOO.** ### The locked face took `heads that say they record,
### collect, or certify` as naming a PURPOSE; the other reading is `heads that say they certify
### NOTHING`. ### **BOTH YIELDS ARE PRINTED** ### so the declared reading is inspectable rather than
### asserted.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock              # noqa: E402
import role_structure as RS   # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
HEAD_LINES = 40   # ### the locked face's figure, and it is the face's and not this tool's

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ---- THE LEXICON, FIXED BEFORE ANY COUNT -----------------------------------------------------------
ORDER_VERBS = r'(record|records|recorded|recording|collect|collects|collected|collecting|' \
              r'certify|certifies|certified|certifying)'
WIDE_VERBS = r'(record|records|recorded|recording|collect|collects|collected|collecting|' \
             r'certify|certifies|certified|certifying|log|logs|logged|gather|gathers|gathered|' \
             r'list|lists|listed|index|indexes|indexed|catalogue|catalogues|catalogued|' \
             r'inventory|inventories|register|registers|registered|track|tracks|tracked)'
# ### **THE DOCUMENT MUST NAME ITSELF.** ### A sentence about what somebody else records is not a
# ### statement of this document's purpose.
# ### ### **`it ` WAS IN THIS PATTERN ON THE FIRST RUN AND IT IS A DEFECT, NOT A CHOICE.** ### The
# ### locked face says the matcher looks for a sentence in which ### **THE DOCUMENT NAMES ITSELF**,
# ### and a bare pronoun names nothing. ### **THE REPAIR IS TO THE MATCHER'S FIDELITY TO THE FACE AND
# ### ### NOT TO THE RESULT**, and the defective yield is printed beside the repaired one so the
# ### correction is inspectable rather than silent.
SELF = r'(this\s+(file|document|note|page|ledger|log|record|list|index|register|table|census|' \
       r'roster|map|appendix|annex)|these\s+(entries|rows|notes))'
SELF_LOOSE = r'(this\s+(file|document|note|page|ledger|log|record|list|index|register|table|' \
             r'census|roster|map|appendix|annex)|it\s+|these\s+(entries|rows|notes))'
# ### ### **AND A CLASS DECLARATION IS NOT A PURPOSE STATEMENT.** ### The order says the exemplars
# ### come from the record's own purpose statements ### **RATHER THAN FROM CLASS DECLARATIONS**, so a
# ### line that IS a class declaration is excluded by the order's own words and not by preference.
CLASS_LINE = re.compile(r'DOCUMENT CLASS|STANDING TAXONOMY|\bTIER [KCNE]\b|author-ruled 2026-07-28',
                        re.I)
# ### **OR THE CORPUS'S OWN HEAD CONVENTION** -- a bare noun phrase naming the artifact kind.
# ### ### **AND THE NOUN PHRASE MUST BE DESCRIBING THE ARTIFACT, NOT MERELY OPENING A SENTENCE.**
# ### The first version fired on `THE CENSUS WARNED THE BIBLIOGRAPHY WOULD BE OVERSTATED` -- a
# ### sentence ABOUT a census, in the middle of prose. ### The locked face asks for a ### **PURPOSE
# ### ### STATEMENT**, and a purpose statement says what the thing is FOR: the noun is followed by
# ### `of`, `to`, `for`, a dash or a colon. ### **THE THIRD YIELD IS PRINTED BESIDE THE OTHER TWO.**
NOUN_KIND = (r'(record|log|ledger|register|index|catalogue|inventory|list|collection|census|'
             r'roster|table)')
NOUN_OPENER = re.compile(r'^\s*(?:[*#>\-\s]|\*\*)*(?:A|An|The)\s+(?:running\s+)?' + NOUN_KIND
                         + r'\s*(?:of|to|for|:|—|--)\b|'
                         r'^\s*(?:[*#>\-\s]|\*\*)*(?:A|An|The)\s+(?:running\s+)?' + NOUN_KIND
                         + r'\s*[—-]', re.I)
NOUN_OPENER_LOOSE = re.compile(r'^\s*(?:[*#>\-\s]|\*\*)*(?:A|An|The)\s+'
                               r'(running\s+)?' + NOUN_KIND + r'\b', re.I)
DENIAL = re.compile(r'\b(certif\w+|claim\w+|assert\w+|prove\w+|argu\w+)\s+nothing\b|'
                    r'\bnothing\s+is\s+(certified|claimed|asserted|proved|argued)\b', re.I)


def sentence_hit(line, verbs, self_pat=None, noun_pat=None, allow_class=False):
    """### **A HIT IS A SELF-REFERENCE AND A GATHERING VERB IN ONE LINE, OR THE NOUN OPENER.**
    ### **AND A CLASS DECLARATION IS NEVER A HIT**, because the order excludes it by name."""
    if CLASS_LINE.search(line) and not allow_class:
        return None
    low = line.lower()
    if (noun_pat or NOUN_OPENER).match(line):
        return 'noun-opener'
    if re.search(self_pat or SELF, low) and re.search(r'\b' + verbs + r'\b', low):
        return 'self-reference and a gathering verb'
    return None


def heads(root):
    """Every corpus document and its first `HEAD_LINES` lines, 1-indexed."""
    for dp, _dn, fn in os.walk(root):
        if '.git' in dp:
            continue
        for f in sorted(fn):
            if not f.endswith('.md'):
                continue
            rel = os.path.relpath(os.path.join(dp, f), root).replace(os.sep, '/')
            try:
                txt = io.open(os.path.join(dp, f), encoding='utf-8', errors='replace').read()
            except OSError:
                continue
            yield rel, txt, txt.split(chr(10))[:HEAD_LINES]


LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def main():
    rec('=' * 100)
    rec('b381 -- COMPONENT 1. ### THE OLD CONTROL`S WEAKNESS, AND THE REBUILT EXEMPLAR SET.')
    rec('=' * 100)

    # ---------------------------------------------------------------- THE POSITIVE CONTROL, FIRST
    rec('')
    rec('-' * 100)
    rec('  ### THE POSITIVE CONTROL, PRINTED BEFORE ANY COUNT.')
    rec('-' * 100)
    rec('  ### ### **A SCAN THAT CANNOT FIRE LOOKS EXACTLY LIKE A CORPUS THAT SAYS NOTHING**, so the')
    rec('  ### matcher is made to fire on a known presence before any absence is reported.')
    PROBES = [('a self-reference and a gathering verb', 'This file records every act in one line.'),
              ('the corpus`s own noun opener', 'A running log of the seam closes.'),
              ('the denial reading', 'It certifies nothing and proves nothing.')]
    ctrl = []
    for lbl, probe in PROBES:
        w = sentence_hit(probe, WIDE_VERBS)
        o = sentence_hit(probe, ORDER_VERBS)
        dn = bool(DENIAL.search(probe))
        ctrl.append(dict(case=lbl, wide=bool(w), order=bool(o), denial=dn))
        rec('    %-42s wide %-5s order %-5s denial %s' % (lbl, bool(w), bool(o), dn))
    NEG = 'A proof that the residue is irreducible, relating two kernels.'
    neg_ok = not sentence_hit(NEG, WIDE_VERBS) and not DENIAL.search(NEG)
    rec('    %-42s ### **AND IT REFUSES A DOCUMENT THAT ARGUES : %s**'
        % ('the negative polarity', neg_ok))
    controls_ok = all(c['wide'] for c in ctrl[:2]) and ctrl[2]['denial'] and neg_ok
    rec('  ### ### **CONTROLS HELD : %s** -- an absence may now be reported.' % controls_ok)

    # ------------------------------------------------------------ THE OLD CONTROL'S WEAKNESS
    E80 = json.load(io.open(os.path.join(D, 'b380_reads.json'), encoding='utf-8'))
    RS80 = json.load(io.open(os.path.join(D, 'b380_rescore.json'), encoding='utf-8'))
    rows80 = {r['file']: r for r in RS80['rows']}
    syn80, gat80 = E80['declare_synthesis'], E80['declare_gathering']
    THR80 = 2   # ### b380's declared threshold, from its own locked face
    rec('')
    rec('-' * 100)
    rec('  ### THE OLD CONTROL`S WEAKNESS -- ### **ONE FINDING, NOT TWO.**')
    rec('-' * 100)
    reaches = [rows80[f]['evidence']['reach'] for f in syn80]
    lo = min(reaches)
    rec('  ### `b380`s threshold : ### **%d**' % THR80)
    rec('  ### the synthesis declarers` reaches : %s' % ', '.join(str(x) for x in sorted(reaches)))
    rec('  ### ### **THE LOWEST OF THEM IS `%d`, AND THE THRESHOLD WAS `%d`.**' % (lo, THR80))
    cannot_fail = lo >= THR80
    rec('  ### ### **SO NO VALUE OF THE THRESHOLD AT OR BELOW `%d` WOULD HAVE FAILED ANY OF THEM : %s**'
        % (lo, cannot_fail))
    rec('  ### and on the other side:')
    for f in gat80:
        r = rows80[f]
        rec('      %-62s declared %s   b380 scored %s   reach %d'
            % (f, r['statement_a'], r['structural_a'], r['evidence']['reach']))
    disagreed = sum(1 for f in gat80 if rows80[f]['statement_a'] != rows80[f]['structural_a'])
    rec('  ### ### **BOTH GATHERING DECLARERS DISAGREED : %d OF %d.**' % (disagreed, len(gat80)))
    rec('  ### ### ### **THE ONE FINDING:** ### the side that could not fail carried `%d` documents'
        % len(syn80))
    rec('  ### ### ### and the side that could inform carried `%d` -- ### **AND THE PREDICATE GOT'
        % len(gat80))
    rec('  ### ### ### THAT SIDE WRONG.** ### A control that cannot fail on one side and cannot')
    rec('  ### ### ### inform on the other is ### **ONE DEFECT WITH TWO FACES.**')

    # ---------------------------------------------------------------------- THE REBUILD
    rec('')
    rec('-' * 100)
    rec('  ### THE REBUILD, FROM THE RECORD`S OWN PURPOSE STATEMENTS.')
    rec('-' * 100)
    rec('  ### head window : first %d lines ### / ### lexicon : the order`s three verbs, and the wide'
        % HEAD_LINES)
    rec('  ### gathering family reported beside them. ### **THE WIDE FAMILY IS THE EXEMPLAR SET.**')
    wide, order_only, denial, loose, loose2 = [], [], [], [], []
    scanned = 0
    for rel, _txt, head in heads(PP):
        scanned += 1
        for k, ln in enumerate(head, 1):
            if not ln.strip():
                continue
            hw = sentence_hit(ln, WIDE_VERBS)
            if hw:
                wide.append(dict(file=rel, line=k, text=ln.rstrip(), why=hw))
                if sentence_hit(ln, ORDER_VERBS):
                    order_only.append(dict(file=rel, line=k, text=ln.rstrip()))
                break
        # ### **THE TWO EARLIER MATCHERS, RUN BESIDE THE THIRD AND COUNTED.** ### The lineage is
        # ### printed because ### **A MATCHER REPAIRED AFTER ITS OUTPUT WAS SEEN IS A MATCHER WHOSE
        # ### ### LINEAGE A READER IS OWED.**
        for k, ln in enumerate(head, 1):
            if ln.strip() and sentence_hit(ln, WIDE_VERBS, SELF_LOOSE, NOUN_OPENER_LOOSE, True):
                loose.append(rel)
                break
        for k, ln in enumerate(head, 1):
            if ln.strip() and sentence_hit(ln, WIDE_VERBS, SELF, NOUN_OPENER_LOOSE):
                loose2.append(rel)
                break
        for k, ln in enumerate(head, 1):
            if DENIAL.search(ln):
                denial.append(dict(file=rel, line=k, text=ln.rstrip()))
                break
    rec('  documents scanned : %d' % scanned)
    rec('  ### ### ### **THE MATCHER LINEAGE, PRINTED BECAUSE TWO VERSIONS WERE REPAIRED AFTER')
    rec('  ### ### ### THEIR OUTPUT WAS SEEN.** ### Each repair traces to words written BEFORE the')
    rec('  ### run -- the face`s `the document names ITSELF` and the order`s `rather than from class')
    rec('  ### declarations` -- but ### **A READER IS OWED THE LINEAGE AND NOT ONLY THE LAST ONE.**')
    rec('    v1  `it ` as a self-reference, class lines allowed, any noun opener : ### **%d**'
        % len(loose))
    rec('    v2  self-reference tightened, class lines excluded                  : ### **%d**'
        % len(loose2))
    rec('    v3  noun opener must DESCRIBE the artifact (`of`/`to`/`for`/dash)   : ### **%d**'
        % len(wide))
    rec('  ### ### **AND `v1` MATCHED `%d` OF `%d` HEADS**, which is not a corpus that gathers -- it'
        % (len(loose), scanned))
    rec('  ### is a pronoun matching prose. ### **THE REPAIRS ARE TO FIDELITY, NOT TO THE RESULT.**')
    rec('  ### ### **HEADS STATING ONE IN THE ORDER`S THREE VERBS      : %d**' % len(order_only))
    rec('  ### ### **HEADS TAKING THE DENIAL READING (`certify nothing`) : %d**' % len(denial))
    rec('  ### ### ### **THE DENIAL READING WOULD HAVE YIELDED `%d` EXEMPLARS**, which is why the'
        % len(denial))
    rec('  ### locked face took the purpose reading -- ### **AND THE FIGURE IS PRINTED RATHER THAN')
    rec('  ### ### THE CHOICE ASSERTED.**')

    # ------------------------------------------------------------------ THE CONFLICTS
    conflicts = [w for w in wide if w['file'] in syn80]
    gathering = [w for w in wide if w['file'] not in syn80]
    rec('')
    rec('  ### ### **CONFLICTS -- A HEAD THAT GATHERS AND A CLASS LINE THAT DECLARES SYNTHESIS.**')
    rec('  ### Reported and ### **NOT RESOLVED**; excluded from BOTH exemplar sets, because an')
    rec('  ### exemplar that argues with itself cannot be a ground truth for anything.')
    if conflicts:
        for c in conflicts:
            rec('      %-62s line %-4d' % (c['file'], c['line']))
            rec('        | %s' % c['text'].strip()[:150])
    else:
        rec('      ### none.')
    syn_set = [f for f in syn80 if f not in set(c['file'] for c in conflicts)]

    rec('')
    rec('  ### ### **THE GATHERING EXEMPLARS, EACH QUOTED AT ITS OWN LINE : %d**' % len(gathering))
    for g in gathering:
        rec('      %-62s line %-4d  (%s)' % (g['file'], g['line'], g['why']))
        rec('        | %s' % g['text'].strip()[:150])

    # ------------------------------------------------------------------ THE QUOTES RE-READ
    bad = []
    for g in gathering:
        src = os.path.join(PP, g['file'].replace('/', os.sep))
        try:
            ls = io.open(src, encoding='utf-8', errors='replace').read().split(chr(10))
        except OSError:
            bad.append((g['file'], 'unreadable'))
            continue
        if g['line'] - 1 >= len(ls) or ls[g['line'] - 1].rstrip() != g['text']:
            bad.append((g['file'], g['line']))
    rec('')
    rec('  ### ### **EVERY QUOTE RE-READS OUT OF ITS OWN SOURCE AT ITS OWN LINE : %s** %s'
        % (not bad, bad[:3] or ''))

    # ------------------------------------------------------------------ THE BALANCE
    FLOOR = 5   # ### the locked face's figure
    rec('')
    rec('-' * 100)
    rec('  ### THE BALANCE.')
    rec('-' * 100)
    rec('  ### ### **SYNTHESIS EXEMPLARS : %d** ### (b380`s, carried unchanged, less conflicts)'
        % len(syn_set))
    rec('  ### ### **GATHERING EXEMPLARS : %d** ### (b380`s %d, plus %d found by purpose statement)'
        % (len(gathering) + len(gat80), len(gat80), len(gathering)))
    gather_set = sorted(set(gat80) | set(g['file'] for g in gathering))
    powered = len(gather_set) >= FLOOR
    rec('  ### the floor declared on the locked face : ### **%d**' % FLOOR)
    rec('  ### ### ### **THE SET %s** -- gathering side `%d` against a floor of `%d`.'
        % ('CAN FAIL IN BOTH DIRECTIONS' if powered else 'IS UNDERPOWERED', len(gather_set), FLOOR))
    if not powered:
        rec('  ### ### **AND THE ACT DOES NOT STOP.** ### Component 3 runs anyway and its separation')
        rec('  ### result is reported as ### **NOT DECISIVE**, because an underpowered result')
        rec('  ### reported as underpowered is worth more than no result.')

    rec('')
    rec('=' * 100)
    rec('  ### exemplars added, dropped or ranked by judgement : ### **0**')
    rec('  ### ### **EVERY MATCH WAS TAKEN. ### THE SET WAS FOUND AND NOT CHOSEN.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b381_exemplars_notes', LINES)
    out = dict(scanned=scanned, head_lines=HEAD_LINES, floor=FLOOR, powered=powered,
               controls_ok=controls_ok, controls=ctrl, negative_refused=neg_ok,
               b380_threshold=THR80, b380_synthesis_reaches=sorted(reaches),
               b380_lowest_synthesis_reach=lo, control_cannot_fail=cannot_fail,
               b380_gatherers_disagreeing=disagreed,
               wide_hits=len(wide), order_hits=len(order_only), denial_hits=len(denial),
               loose_hits=len(loose), loose2_hits=len(loose2),
               denial_yield=[x['file'] for x in denial],
               conflicts=conflicts, gathering_found=gathering,
               synthesis_set=syn_set, gathering_set=gather_set,
               quotes_reread=(not bad), quote_failures=bad,
               judgement_selections=0,
               run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p))
    io.open(os.path.join(D, 'b381_exemplars.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(out, indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0 if (controls_ok and not bad) else 1


if __name__ == '__main__':
    sys.exit(main())
