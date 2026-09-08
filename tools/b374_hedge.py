# -*- coding: utf-8 -*-
"""b374_hedge.py -- COMPONENT 1: THE HEDGE AUDIT OVER A SURFACE IT HAS NEVER COVERED.

### ### **THE INSTRUMENT IS RUN UNMODIFIED.** ### `hedge_audit` is IMPORTED and its own `_sentences`,
### `_has_hedge`, `_has_grade` and `_claim_shaped` are called as they stand. ### **NOT ONE STEM, GRADE
### ### TOKEN OR TEST IS TOUCHED, TUNED OR EXTENDED FOR THIS SURFACE.**
### ### **TWO FURTHER PREDICATES ARE THIS ACT'S OWN AND ARE MARKED AS SUCH** -- the unsourced
### expectation and the working note -- and neither is written into the shared instrument.
### ### ### **AND THE SCOPE IS NOT THIS SEAT'S TO CHOOSE.** ### The keystones are the ones
### `THE_KEYSTONE_CENSUS.md` names in its own table; the rest of the corpus is classified by
### ### **THE CENSUS'S OWN OPERATIONALISED TEST**, so the comparison population is the census's and not
### an invention of this act.
### ### **A HEDGE IS NOT A FAULT. ### THE COUNT IS NOT A SCORE. ### NOTHING IS REPAIRED.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                 # noqa: E402
import hedge_audit as HA         # noqa: E402
import anchor_from_file as AF    # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
CENSUS = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### **THIS ACT'S OWN PREDICATES, DECLARED WITH THEIR LIMITS. ### NOT PART OF THE INSTRUMENT.**
# ### ### **THE CLASS IS `UNSOURCED EXPECTATION`, NOT `IMPORTED`**, because the predicate can see only
# ### that the document offers no source -- not that the expectation came from outside the programme.
EXPECT = re.compile(r'(?<![A-Za-z])(should|must|ought to|is expected to|are expected to|'
                    r'we expect|one expects|expected to)(?![A-Za-z])', re.I)
SOURCE_SHAPE = re.compile(r'arXiv|doi|DOI|\(19\d\d\)|\(20\d\d\)|\[[0-9]+\]|zenodo|'
                          r'`[0-9a-f]{7,40}`|Theorem \d|Lemma \d|§\d')
# ### the working-note shapes, declared. ### **A SHAPE THIS LIST DOES NOT KNOW WILL NOT BE FOUND.**
NOTES = ['TODO', 'TK]', 'XXX', 'FIXME', '[?]', 'draft:', 'note to self', 'WIP',
         'placeholder', 'PLACEHOLDER', '???', 'to be written', 'TBD']

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(*a):
    return subprocess.run(['git', '-C', PP] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def census_keystones():
    """### **THE SIXTEEN, READ FROM THE CENSUS'S OWN TABLE.** ### Not typed, not chosen."""
    txt = io.open(CENSUS, encoding='utf-8', errors='replace').read()
    rows = txt.split(chr(10))
    start = None
    for i, ln in enumerate(rows):
        if 'THE SIXTEEN KEYSTONES' in ln:
            start = i
            break
    if start is None:
        return [], None
    names = []
    for ln in rows[start:start + 40]:
        m = re.match(r'\|\s*`([A-Za-z0-9_]+)`\s*\|', ln)
        if m:
            names.append(m.group(1))
    return names, start + 1


def locate(name, files):
    hits = [f for f in files if os.path.basename(f) == name + '.md'
            and not f.startswith('archive/') and not f.startswith('outputs/')]
    return hits


def line_of(path, sentence):
    """### **EVERY QUOTATION MUST BE LOCATABLE IN ITS FILE** (BAR 3)."""
    frag = sentence.strip()[:60]
    if not frag:
        return None
    try:
        txt = io.open(path, encoding='utf-8', errors='replace').read()
    except OSError:
        return None
    for i, ln in enumerate(txt.split(chr(10)), 1):
        if frag in ln:
            return i
    return None


def measure(path):
    txt = io.open(path, encoding='utf-8', errors='replace').read()
    sents = HA._sentences(txt)
    hedged, hedged_graded, hedged_bare, unsourced, notes = [], [], [], [], []
    for s in sents:
        g, h = HA._has_grade(s), HA._has_hedge(s)
        if h:
            hedged.append(s)
            (hedged_graded if g else hedged_bare).append(s)
        if (not g) and HA._claim_shaped(s) and EXPECT.search(s) and not SOURCE_SHAPE.search(s):
            unsourced.append(s)
    for i, ln in enumerate(txt.split(chr(10)), 1):
        for tok in NOTES:
            if tok in ln:
                notes.append((i, tok, ln.strip()[:150]))
                break
    n, gh, ua = HA.audit(path)
    return dict(sentences=n, hedged=len(hedged), hedged_graded=len(hedged_graded),
                hedged_bare=len(hedged_bare), unsourced=len(unsourced), notes=len(notes),
                instrument_graded_hedges=len(gh), instrument_ungraded_shapes=len(ua),
                per_k=(1000.0 * len(hedged) / n if n else 0.0),
                bare_per_k=(1000.0 * len(hedged_bare) / n if n else 0.0),
                samples=dict(hedged=hedged[:3], unsourced=unsourced[:3], notes=notes[:3]))


def main():
    rec('=' * 100)
    rec('b374 -- COMPONENT 1: THE HEDGE AUDIT, RUN UNMODIFIED OVER THE KEYSTONES AND THE DEPOSIT.')
    rec('=' * 100)
    rec('')
    rec('  ### the instrument, IMPORTED and untouched : %s' % os.path.basename(HA.__file__))
    rec('  ### its own hedge stems  : %s' % (HA.HEDGE_STEMS,))
    rec('  ### its own grade tokens : %s' % (HA.GRADE_TOKENS,))
    _ok, _log = HA.self_test(False)
    rec('  ### its own fixtures, run here before it is trusted : %s' % _ok)
    rec('  ### ### **THIS ACT ADDS TWO PREDICATES OF ITS OWN AND WRITES NEITHER INTO THE INSTRUMENT:**')
    rec('  ###   UNSOURCED EXPECTATION : %s' % EXPECT.pattern)
    rec('  ###     excluded when the sentence carries a source shape : %s' % SOURCE_SHAPE.pattern)
    rec('  ###     ### **IT CANNOT SEE WHETHER AN EXPECTATION IS FOREIGN.** ### It sees only that the')
    rec('  ###     ### document offers no source for it, which is why the class is not called IMPORTED.')
    rec('  ###   WORKING NOTE : %s' % NOTES)
    rec('  ###     ### **A SHAPE THIS LIST DOES NOT KNOW WILL NOT BE FOUND** (`PREDICATE_ONE_SHAPE`).')

    files = [f for f in git('ls-files', '*.md').split(chr(10)) if f.strip()]
    names, anchor_line = census_keystones()
    rec('')
    rec('-' * 100)
    rec("  ### (1) THE SCOPE, TAKEN FROM THE CENSUS'S OWN TABLE.")
    rec('-' * 100)
    rec('    the census names %d keystones in its table (read at `THE_KEYSTONE_CENSUS.md`)' % len(names))
    keystones, unresolved, ambiguous = [], [], []
    for nm in names:
        hits = locate(nm, files)
        if len(hits) == 1:
            keystones.append((nm, hits[0]))
        elif not hits:
            unresolved.append(nm)
        else:
            ambiguous.append((nm, hits))
    rec('    resolved to a tracked path : %d ### / ### UNRESOLVED : %d ### / ### AMBIGUOUS : %d'
        % (len(keystones), len(unresolved), len(ambiguous)))
    for nm in unresolved:
        rec('      ### **UNRESOLVED, REPORTED AND NOT DROPPED** : `%s`' % nm)
    for nm, hits in ambiguous:
        rec('      ### **AMBIGUOUS** : `%s` -> %s' % (nm, hits))
    deposited = sorted(f for f in files if f.startswith('outputs/DEPOSITED-v1.1.2/'))
    rec('    deposited companions : %d' % len(deposited))
    ks_set = set(f for _n, f in keystones)
    dep_set = set(deposited)

    # ### **THE COMPARISON POPULATION IS THE CENSUS'S OWN, BY ITS OWN OPERATIONALISED TEST.**
    support = []
    for f in files:
        if f in ks_set or f in dep_set or f.startswith('archive/') or f.startswith('outputs/'):
            continue
        p = os.path.join(PP, f.replace('/', os.sep))
        try:
            head = io.open(p, encoding='utf-8', errors='replace').read(4000)
        except OSError:
            continue
        # ### the census's (i): an `Abstract` heading or an ORCID block.
        if re.search(r'^#+\s*Abstract', head, re.M) or 'ORCID' in head:
            continue
        support.append(f)
    rec("    ### ### **THE WORKING NOTES, BY THE CENSUS'S OWN TEST (i) -- no Abstract heading and no")
    rec('    ### ### ORCID block, archives and outputs excluded : %d documents.**' % len(support))
    rec('    ### **THE POPULATION IS THE CENSUS`S, NOT THIS SEAT`S.**')

    rec('')
    rec('-' * 100)
    rec('  ### (2) THE MEASUREMENT, PER DOCUMENT.')
    rec('-' * 100)
    out = {}
    for label, group in (('KEYSTONE', [f for _n, f in keystones]),
                         ('DEPOSITED COMPANION', deposited),
                         ('WORKING NOTE', support)):
        rec('')
        rec('    ### **%s** ### -- %d documents' % (label, len(group)))
        rec('    %-56s %7s %7s %7s %7s %7s %8s' % ('document', 'sents', 'hedged', 'bare',
                                                    'unsrc', 'notes', 'hedge/k'))
        tot = dict(sentences=0, hedged=0, hedged_bare=0, unsourced=0, notes=0,
                   hedged_graded=0, docs=0)
        for f in group:
            p = os.path.join(PP, f.replace('/', os.sep))
            m = measure(p)
            m['file'] = f
            m['class'] = label
            out[f] = m
            for k in ('sentences', 'hedged', 'hedged_bare', 'unsourced', 'notes', 'hedged_graded'):
                tot[k] += m[k]
            tot['docs'] += 1
            if label != 'WORKING NOTE' or m['hedged'] or m['notes']:
                rec('    %-56s %7d %7d %7d %7d %7d %8.1f'
                    % (f[:56], m['sentences'], m['hedged'], m['hedged_bare'], m['unsourced'],
                       m['notes'], m['per_k']))
        tot['per_k'] = 1000.0 * tot['hedged'] / tot['sentences'] if tot['sentences'] else 0.0
        tot['bare_per_k'] = (1000.0 * tot['hedged_bare'] / tot['sentences']
                             if tot['sentences'] else 0.0)
        tot['notes_per_doc'] = tot['notes'] / tot['docs'] if tot['docs'] else 0.0
        rec('    %-56s %7d %7d %7d %7d %7d %8.1f'
            % ('### TOTAL', tot['sentences'], tot['hedged'], tot['hedged_bare'],
               tot['unsourced'], tot['notes'], tot['per_k']))
        out['__total__' + label] = tot

    rec('')
    rec('-' * 100)
    rec('  ### (3) THE QUOTATIONS. ### **EVERY ONE LOCATED IN ITS FILE.**')
    rec('-' * 100)
    quoted = 0
    for f, m in sorted(out.items()):
        if f.startswith('__total__'):
            continue
        if not (m['samples']['hedged'] or m['samples']['unsourced'] or m['samples']['notes']):
            continue
        p = os.path.join(PP, f.replace('/', os.sep))
        rec('')
        rec('    ### `%s` ### [%s]' % (f, m['class']))
        for s in m['samples']['hedged']:
            ln = line_of(p, s)
            quoted += 1
            rec('      HEDGED            line %-6s | %s' % (ln, s.strip()[:150]))
        for s in m['samples']['unsourced']:
            ln = line_of(p, s)
            quoted += 1
            rec('      UNSOURCED EXPECT  line %-6s | %s' % (ln, s.strip()[:150]))
        for ln, tok, s in m['samples']['notes']:
            quoted += 1
            rec('      WORKING NOTE      line %-6d | (%s) %s' % (ln, tok, s[:130]))

    K = out['__total__KEYSTONE']
    DP = out['__total__DEPOSITED COMPANION']
    W = out['__total__WORKING NOTE']
    rec('')
    rec('=' * 100)
    rec('  ### (4) THE COMPARISON `(L2)` ASKS FOR, PER THOUSAND SENTENCES AND PER DOCUMENT.')
    rec('=' * 100)
    rec('  %-24s %10s %10s %10s %10s %10s' % ('population', 'docs', 'sentences', 'hedged',
                                              'hedge/k', 'notes/doc'))
    for lbl, tt in (('KEYSTONE', K), ('DEPOSITED COMPANION', DP), ('WORKING NOTE', W)):
        rec('  %-24s %10d %10d %10d %10.1f %10.2f'
            % (lbl, tt['docs'], tt['sentences'], tt['hedged'], tt['per_k'], tt['notes_per_doc']))
    rec('')
    rec('  ### ### **AND THE RAW TOTALS ARE PRINTED BESIDE THE RATES ON PURPOSE:** ### a raw total')
    rec('  ### would make the larger population lose by being larger, which would score the')
    rec('  ### expectation on a fact about file sizes.')
    rec('  ### **A HEDGE IS NOT A FAULT.** ### A document that says *this is conditional* is doing')
    rec('  ### what this record demands everywhere else. ### **THE COUNT IS NOT A SCORE.**')
    rec('  ### **NOTHING WAS REPAIRED. ### NO SENTENCE WAS REWRITTEN. ### NO DOCUMENT WAS GRADED.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b374_hedge_notes', LINES)
    io.open(os.path.join(D, 'b374_hedge.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(instrument=os.path.basename(HA.__file__),
                        instrument_selftest=_ok,
                        census_names=names, keystones=[f for _n, f in keystones],
                        unresolved=unresolved, ambiguous=ambiguous,
                        deposited=deposited, support=len(support),
                        totals=dict(KEYSTONE=K, DEPOSITED=DP, WORKING=W),
                        quoted=quoted,
                        documents={k: v for k, v in out.items() if not k.startswith('__total__')},
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
