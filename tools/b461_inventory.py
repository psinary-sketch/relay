# -*- coding: utf-8 -*-
"""b461_inventory.py -- COMPONENT 1: THE INVENTORY OF b460's SIXTY-FOUR ARMS.

### ### **EVERY RULE APPLIED HERE IS ON THE LOCKED FACE** -- the enumeration rule, the `what it
### reads` rule decided by identifiers, the two control columns, and the three status values.
### ### **NOTHING IS RETIRED HERE.** ### The inventory classifies; Component 2 disposes.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
SUITE = os.path.join(T, 'b460_checks.py')
FACE460 = os.path.join(D, 'b460_registration_2026-09-21.txt')
NL = chr(10)
L = []

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    return io.open(p, encoding='utf-8-sig', errors='replace').read().replace(chr(13), '')


def predicates(src):
    """### **EXTRACT EACH `arm(...)` CALL'S PREDICATE BY BRACKET MATCHING**, not by a line regex:
    ### the calls span lines and a line regex would truncate half of them."""
    out = {}
    for m in re.finditer(r"arm\(\s*('([GF]-[A-Z0-9-]+)'|'G-%s-SCORED' % n)\s*,", src):
        i, depth = m.end(), 0
        start = i
        while i < len(src):
            c = src[i]
            if c in '([{':
                depth += 1
            elif c in ')]}':
                if depth == 0:
                    break
                depth -= 1
            elif c == ',' and depth == 0:
                break
            i += 1
        name = m.group(2) or 'LOOP-N-SCORED'
        out[name] = ' '.join(src[start:i].split())
    return out


# ### **THE REAL POSITIVE CONTROLS THE RECORD ITSELF SUPPLIES.** ### Each names an incident, an act
# ### and what the arm did on it. ### **NOTHING HERE IS SYNTHETIC AND NOTHING IS INVENTED.**
REAL = {
    'G-WRITELIST-KINDS': ('b458: the arm read only HEAD, so when the closing commit landed the six '
                          'breaching names fell out of scope and it turned FAIL to PASS with no file '
                          'removed. ### That HEAD-only state is an input it must fail on.'),
    'G-CORPUS-SCOPE': ('b458: read the working tree, which is empty after the commit, so it failed '
                       'post-push on a repository that was exactly as it should be.'),
    'G-ARMS-DECLARED-EQ-RUN': ('b458: compared the declared set against a run list that was still being '
                               'appended to, so it could only ever fail.'),
    'G-CARRIED-TOOLS-REPOINTED': ('b458: spelled the prior act`s artefact names in its own body and then '
                                  'scanned itself, finding all seven -- b403`s G-FERRYWORDS species.'),
    'G-LOCKGATE-EIGHT': ('b460: its first form read `VERDICT :` as a substring, which also matches '
                         '`FIXTURE VERDICT :` -- an A2 violation committed by the suite itself.'),
    'G-C1-EDGE-TWO-ROUTES': ('b460: its first form searched the extract for `pp = [2]`, which the extract '
                             'never writes; the needle was the face`s wording, not the bank`s.'),
    'G-LOCKGATE-NOT-REDIRECTED': ('b458: its label said `not redirected` and its test said `one notes file`, '
                                  'so four honest gate runs failed it -- the WRONG_ARM species.'),
}


def classify(expr):
    """### **BY THE IDENTIFIERS IN THE PREDICATE AND NOTHING ELSE**, as the face fixes."""
    r = []
    if re.search(r'\bline_with\(', expr):
        r.append('a banked verdict LINE')
    if re.search(r'\bface\b', expr):
        r.append('THE ACT`S OWN FACE, its wording')
    if re.search(r"\.json'|\bctl\b|\btec\b|\breh\b|\bscores\b|\bcells_all\b", expr):
        r.append('a measurement this act banked')
    if re.search(r'\bgits?\(', expr):
        r.append('repository state')
    if re.search(r'os\.path\.exists|os\.listdir', expr):
        r.append('a file`s presence')
    if re.search(r'\bread\(', expr) and not r:
        r.append('a banked file`s whole text')
    if expr.strip() == 'True':
        r = ['NOTHING -- a constant']
    return r or ['a banked file`s whole text']


def main():
    src, face = read(SUITE), read(FACE460)
    dec = sorted(set(re.findall(r'\b[GF]-[A-Z0-9-]+', face)) - {'G-NO'})
    preds = predicates(src)
    loop = preds.get('LOOP-N-SCORED', "'\"%s\"' % n in scores")
    for n in ('N1', 'N2', 'N3'):
        preds.setdefault('G-%s-SCORED' % n, loop)

    rec('=' * 110)
    rec('### COMPONENT 1 -- THE INVENTORY OF b460`S SIXTY-FOUR ARMS.')
    rec('=' * 110)
    rec('  ### THE ENUMERATION RULE, AS THE FACE FIXED IT : the arms the b460 FACE declares -- what RUNS,')
    rec('  ### not what is spelled. ### declared %d ; matched to a predicate %d ; UNMATCHED %d'
        % (len(dec), sum(1 for a in dec if a in preds), sum(1 for a in dec if a not in preds)))
    unmatched = [a for a in dec if a not in preds]
    for a in unmatched:
        rec('      ### UNMATCHED : %s   ### carried with NO DISPOSITION.' % a)
    rec('')

    rows = []
    for a in dec:
        e = preds.get(a, '')
        reads = classify(e)
        const = (e.strip() == 'True')
        real = REAL.get(a)
        # ### STATUS, BY THE FACE'S THREE VALUES.
        if const:
            pos_status, neg_status = 'CANNOT BE STATED', 'CANNOT BE STATED'
        elif real:
            pos_status, neg_status = 'ONE-LINE ADDITION (a REAL input exists)', 'ONE-LINE ADDITION'
        else:
            pos_status, neg_status = 'ONE-LINE ADDITION (synthetic only)', 'ONE-LINE ADDITION'
        pos = (real if real else
               ('CANNOT BE STATED -- the predicate is the constant `True`' if const else
                'SYNTHETIC: the same source with the string, line or field the predicate tests removed'))
        neg = ('CANNOT BE STATED -- a constant passes on every input, so no input distinguishes it'
               if const else 'the real source this act banked, unmutated')
        rows.append(dict(name=a, reads=reads, expr=e[:160], const=const,
                         positive=pos, negative=neg, pos_status=pos_status, neg_status=neg_status,
                         real=bool(real), exercised_today=False))

    rec('  %-38s %-34s %-16s %s' % ('arm', 'what it reads', 'positive control', 'exercised today'))
    rec('  ' + '-' * 106)
    for r in rows:
        rec('  %-38s %-34s %-16s %s'
            % (r['name'], '; '.join(r['reads'])[:34],
               'REAL' if r['real'] else ('NONE' if r['const'] else 'synthetic'),
               'NO'))
    rec('')
    n_real = sum(1 for r in rows if r['real'])
    n_const = sum(1 for r in rows if r['const'])
    n_synth = len(rows) - n_real - n_const
    n_both_today = sum(1 for r in rows if r['exercised_today'])
    rec('  ### ### **THE COUNTS, PRINTED WHETHER OR NOT THEY HELP AN EXPECTATION.**')
    rec('      arms enumerated                                        : %d' % len(rows))
    rec('      with a REAL positive control (drawn from the record)   : %d' % n_real)
    rec('      with only a SYNTHETIC positive control                 : %d' % n_synth)
    rec('      with NO positive control statable at all               : %d' % n_const)
    rec('      ### ### **ARMS CARRYING BOTH CONTROLS EXERCISED TODAY   : %d.**' % n_both_today)
    rec('      ### **AND THAT LAST FIGURE IS THE INVENTORY`S POINT:** `b460_checks.py` runs no arm against')
    rec('      ### any control. ### Every predicate is evaluated once, on the live act, and nothing ever')
    rec('      ### checks that it COULD have said otherwise.')
    rec('')
    rec('  ### THE READS, TALLIED:')
    tal = {}
    for r in rows:
        for k in r['reads']:
            tal[k] = tal.get(k, 0) + 1
    for k in sorted(tal, key=lambda x: -tal[x]):
        rec('      %-42s %d' % (k, tal[k]))
    face_only = [r['name'] for r in rows if r['reads'] == ['THE ACT`S OWN FACE, its wording']]
    rec('      ### ### **ARMS WHOSE ONLY SOURCE IS THE ACT`S OWN FACE : %d.**' % len(face_only))
    rec('      ### An arm of this class can be given a synthetic control -- delete the sentence -- but what')
    rec('      ### it then tests is ### **THAT THE FACE SAYS A THING, NOT THAT THE ACT DID IT.**')
    for a in face_only:
        rec('          %s' % a)
    rec('=' * 110)
    io.open(os.path.join(D, 'b461_inventory.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(rows=rows, declared=len(dec), unmatched=unmatched, n_real=n_real,
                   n_synth=n_synth, n_const=n_const, both_today=n_both_today,
                   face_only=face_only, tally=tal),
              io.open(os.path.join(D, 'b461_inventory.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return rows


if __name__ == '__main__':
    main()
    print('  written: b461_inventory.txt and b461_inventory.json')
