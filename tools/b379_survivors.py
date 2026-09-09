# -*- coding: utf-8 -*-
"""b379_survivors.py -- THE DRAFT'S COMPONENT 2 AND ADDITION TWO APPLIED.

### `b378` cut `37` unresolved identifiers to `14` that survive: not `Mathlib`, not corpus documents,
### and declared by no ref of any kernel on this disk. ### The draft asked for one step further:
### ### **RENAMED, PROSE THAT WAS NEVER A TERMINAL, A KERNEL NOT ON THIS DISK, OR NEVER COMPILED** --
### read from ### **THE SENTENCE THAT NAMES EACH**, not from the name alone.

### ### **AND `row_categories` IS APPLIED TO THE WHOLE `37`**, so the categories `b378` discovered by
### hand are now assigned by a fixtured module. ### **A CATEGORY REPORTED AS AN ABSENCE IS A FALSE
### ### DEFECT**, and the module exists so a later checker stops making them.

### ### **THE SEARCH EVIDENCE IS `b378`'S, RE-READ FROM ITS BANK AND NOT RE-RUN.** ### `b378`'s sweep
### carried a positive control and reported `0` failed searches; ### **RE-RUNNING IT WOULD COST TWENTY
### ### MINUTES AND CHANGE NO ANSWER**, and the bank records which refs were searched. ### The one
### thing re-read live is the sentence, because that is what this component is about.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import row_categories as RC   # noqa: E402
import run_clock              # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### **THE FOUR REMAINING EXPLANATIONS THE DRAFT NAMED, AND HOW EACH IS EVIDENCED.**
# ### ### **EACH IS DECIDED FROM THE SENTENCE, AND WHERE THE SENTENCE DOES NOT DECIDE IT THE ANSWER
# ### ### IS `UNDECIDED-BY-ITS-SENTENCE`** -- which is a reading of the document, not a verdict on it.
PROSE_SHAPE = re.compile(r'\b(let|write|denote|set|define|with|where|for|put)\b[^`]{0,40}$', re.I)
MATH_CONTEXT = re.compile(r'\$|\\\(|\\\[|[=<>≤≥∈∑∫]|\bthe (quantity|value|number|constant|grid|'
                          r'residual|array|column|field|term)\b', re.I)
KERNEL_NAMED = re.compile(r'`(SIDE-[A-Za-z0-9-]+)`')
COMPILE_WORDS = re.compile(r'\b(compiled|compiles|verified|machine-checked|`#print axioms`)\b', re.I)
RENAME_WORDS = re.compile(r'\b(renamed|formerly|was called|superseded|retired)\b', re.I)

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def naming_sentence(rel, name):
    """### **THE FIRST LINE OF THE DOCUMENT THAT NAMES THIS IDENTIFIER, WITH ITS LINE NUMBER.**"""
    p = os.path.join(PP, rel.replace('/', os.sep))
    try:
        lines = io.open(p, encoding='utf-8', errors='replace').read().split(chr(10))
    except OSError:
        return None, None
    tick = '`' + name + '`'
    for i, ln in enumerate(lines, 1):
        if tick in ln:
            return i, ln.strip()
    return None, None


def explain(name, sent):
    """### **ONE STEP FURTHER, READ FROM THE SENTENCE.** ### Returns `(explanation, why)`."""
    if not sent:
        return 'NOT-NAMED-IN-THE-DOCUMENT-AT-THIS-HEAD', ('the identifier is not on the page now; '
                                                          'the document moved since b377 read it')
    if RENAME_WORDS.search(sent):
        return 'THE-DOCUMENT-ITSELF-SAYS-IT-MOVED', 'the sentence carries a rename or retirement word'
    kn = KERNEL_NAMED.findall(sent)
    if kn:
        return 'A-KERNEL-IS-NAMED-BESIDE-IT', ('the sentence names %s, so the claim is that a kernel '
                                               'carries it' % ', '.join('`%s`' % k for k in kn))
    if COMPILE_WORDS.search(sent):
        return 'THE-SENTENCE-CLAIMS-IT-IS-COMPILED', ('the sentence uses a compilation word beside a '
                                                      'name no ref declares')
    if MATH_CONTEXT.search(sent) or PROSE_SHAPE.search(sent.split('`' + name + '`')[0][-60:]):
        return 'PROSE-THAT-WAS-NEVER-A-TERMINAL', ('the sentence uses it as a quantity or a symbol, '
                                                   'not as a citation')
    return 'UNDECIDED-BY-ITS-SENTENCE', 'the sentence does not decide which explanation applies'


def main():
    TM = json.load(io.open(os.path.join(D, 'b378_terminals.json'), encoding='utf-8'))
    DOCS = RC.corpus_document_basenames(PP)

    rec('=' * 100)
    rec('b379 -- THE SURVIVORS, ONE STEP FURTHER. ### **AND THE ROW CATEGORIES, APPLIED.**')
    rec('=' * 100)
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE CATEGORY MODULE, FIXTURED BEFORE IT IS USED.')
    rec('-' * 100)
    ok, cases = RC.self_test(False)
    for c in cases:
        rec('      %-58s got %-24s want %-24s %s'
            % (c['case'][:58], c['got'][:24], c['want'][:24],
               'ok' if c['got'] == c['want'] else '### MISMATCH'))
    rec('    ### ### **FIXTURE VERDICT : %s**'
        % ('EVERY CATEGORY RECOGNISED, AND EVERY ONE REFUSED WHERE IT DOES NOT APPLY' if ok
           else '### FAILED'))
    rec('    ### **THE FRONT DOOR`S OWN WORDS, CARRIED AND NOT REPLACED** (`%s`):' % RC.FRONT_DOOR)
    rec('    ###   | %s' % RC.FRONT_DOOR_QUOTE)
    rec('    ### categories : %d, of which ADDED AT b379 : %d -- %s'
        % (len(RC.CATEGORIES), len(RC.ADDED_AT_B379), ', '.join(RC.ADDED_AT_B379)))
    rec('    ### ### **THE MODULE RETURNS A CATEGORY AND NEVER A VERDICT.** ### Naming a row a library')
    rec('    ### lemma says where the terminal lives; ### **IT DOES NOT SAY THE ROW IS RIGHT.**')
    if not ok:
        run_clock.write(D, 'b379_survivors_notes', LINES)
        return 2

    # -------------------------------------------------- THE CATEGORIES OVER THE WHOLE 37
    rec('')
    rec('-' * 100)
    rec('  ### (2) THE CATEGORIES, ASSIGNED BY THE MODULE OVER ALL %d CARRIED IDENTIFIERS.'
        % TM['carried'])
    rec('-' * 100)
    found = TM['found']
    ml = TM['mathlib']
    assigned, tally = [], {}
    for r in TM['rows']:
        nm = r['name']
        hits, refs = [], r.get('refs_found_on') or []
        f = found.get(nm)
        if f:
            for h in f.get('sample', []):
                hits.append(dict(path=h.get('path'), refs=h.get('refs')))
        if nm in ml:
            hits.append(dict(path='.lake/packages/mathlib/' + ml[nm], refs=['refs/heads/master']))
        line, sent = naming_sentence(r['doc'], nm)
        cat, why = RC.categorise(nm, hits, refs, sent or '', DOCS)
        tally[cat] = tally.get(cat, 0) + 1
        assigned.append(dict(name=nm, doc=r['doc'], b378_class=r['classification'],
                             category=cat, why=why, line=line, sentence=(sent or '')[:240]))
    rec('    %-46s %-28s %s' % ('identifier', 'category', 'why'))
    rec('    %s' % ('-' * 94))
    for a in assigned:
        rec('    %-46s %-28s %s' % (a['name'][:46], a['category'], a['why'][:32]))
    rec('')
    rec('    ### ### **THE TALLY : %s**' % tally)
    notloc = [a for a in assigned if a['category'] == 'NOT_LOCATED']
    rec('    ### ### **AND ONLY %d OF %d ARE `NOT_LOCATED` -- THE ONE CATEGORY THAT ASSERTS AN'
        % (len(notloc), len(assigned)))
    rec('    ### ### ABSENCE.** ### A checker with these categories reports %d defects where the old'
        % len(notloc))
    rec('    ### ### one reported %d.' % len(assigned))

    # ------------------------------------------------------ THE SURVIVORS, ONE STEP FURTHER
    rec('')
    rec('-' * 100)
    rec('  ### (3) THE SURVIVORS, ONE STEP FURTHER, FROM THE SENTENCE THAT NAMES EACH.')
    rec('-' * 100)
    rec('    ### **WHAT `b378` LEFT:** ### %d identifiers that no ref of any kernel declares and that'
        % TM['still_not_found'])
    rec('    ### `Mathlib` does not carry either.')
    rec('')
    survivors = []
    for a in assigned:
        if a['category'] != 'NOT_LOCATED':
            continue
        expl, why = explain(a['name'], a['sentence'])
        survivors.append(dict(a, explanation=expl, explanation_why=why))
        rec('    ### `%s` ### -- `%s` line %s'
            % (a['name'], os.path.basename(a['doc'])[:-3], a['line']))
        rec('        the sentence that names it : %s' % (a['sentence'] or 'NOT ON THE PAGE')[:132])
        rec('        ### ### **%s** ### -- %s' % (expl, why))
    etally = {}
    for sv in survivors:
        etally[sv['explanation']] = etally.get(sv['explanation'], 0) + 1
    rec('')
    rec('    ### ### **THE EXPLANATIONS : %s**' % etally)
    rec('    ### ### ### **NOT ONE DOCUMENT WAS REPAIRED AND NOT ONE NAME WAS INVENTED.** ### The')
    rec('    ### ### ### outcome is a classification, which is what the draft asked for.')
    rec('    ### **AND WHERE THE SENTENCE DOES NOT DECIDE, THE ANSWER IS `UNDECIDED-BY-ITS-SENTENCE`**')
    rec('    ### rather than a guess. ### **A READING OF A DOCUMENT IS NOT A VERDICT ON IT.**')
    rec('=' * 100)

    p = run_clock.write(D, 'b379_survivors_notes', LINES)
    io.open(os.path.join(D, 'b379_survivors.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(fixtures_ok=ok, fixtures=cases, front_door=RC.FRONT_DOOR,
                        front_door_quote=RC.FRONT_DOOR_QUOTE,
                        categories=list(RC.CATEGORIES), added_at_b379=list(RC.ADDED_AT_B379),
                        assigned=assigned, tally=tally, not_located=len(notloc),
                        survivors=survivors, explanations=etally,
                        documents_repaired=0, names_invented=0,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
