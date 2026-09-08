# -*- coding: utf-8 -*-
"""b374_funceq.py -- COMPONENT 4: THE FUNCTIONAL EQUATION AT THE LEVEL OF THE FAMILY. ### A FILING.

### ### **BOTH HALVES ARE QUOTED FROM THE ACTS THAT STATED THEM, AND NOTHING IS CLAIMED BEYOND WHAT
### ### THOSE ACTS STATE.** ### The quotations are PULLED by anchor from the banked files, never typed.
### ### ### **AND THE ACT THAT DERIVED THE REFLECTION ALSO STATES HOW FAR IT DOES NOT GO.** ### That
### sentence is pulled and placed ### **IN THE FILING ITSELF, NOT IN A FOOTNOTE**, because a filing
### that carries the result and drops the limit is `b367`'s species: a summary that keeps claiming what
### its source dropped.
### ### **A CONSTRUCTION AND A REFLECTION ARE NOT ONE STATEMENT BECAUSE THEY CAN BE WRITTEN IN ONE
### ### SENTENCE.** ### The filing joins nothing the acts did not join.
### ### **NO NEW MATHEMATICS. ### NO GRADE CONFERRED, RAISED OR MOVED. ### NO BAR SET.**
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                 # noqa: E402
import anchor_from_file as AF    # noqa: E402
import needle_pull               # noqa: E402

D = os.path.join(ROOT, 'data')
B291 = os.path.join(D, 'b291_the_involution.txt')
B293 = os.path.join(D, 'b293_family_run.txt')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### (label, file, hint, what it is in the filing)
PULLS = [
    ('the reflection, derived', B291,
     'THEREFORE `F_eR : S(lambda, mu) -> S(mu, lambda)`', 'HALF ONE'),
    ('the grade it carries, naming its own import', B291,
     'GRADE: ### DERIVES-on-IMPORT ### -- the import being CC', 'THE GRADE'),
    ('the self-dual member', B291,
     "THE CORPUS'S ARCHIMEDEAN MEMBER IS SELF-DUAL.", 'HALF TWO'),
    ('the diagonal, met at most once', B291,
     'EACH DILATION ORBIT MEETS THE DIAGONAL AT MOST ONCE.', 'THE DIAGONAL'),
    ('how far the act does NOT go', B291,
     'AND NONE OF THIS IS EXTENDED TO THE FINITE PLACES.', 'THE LIMIT'),
    ('the finite family, a different act', B293,
     'b293 -- THE FINITE TWO-RADIUS FAMILY.', 'THE OTHER ACT'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def main():
    rec('=' * 100)
    rec('b374 -- COMPONENT 4: THE FUNCTIONAL EQUATION AT THE LEVEL OF THE FAMILY. ### **A FILING.**')
    rec('=' * 100)
    rec('')
    rec('  ### ### **A FILING IS A PLACE IN THE RECORD, NOT A RESULT.** ### Nothing below is derived')
    rec('  ### here, nothing is graded here, and nothing is joined that the acts did not join.')
    rec('')
    rec('-' * 100)
    rec('  ### (1) THE QUOTATIONS, PULLED BY ANCHOR AND NEVER TYPED.')
    rec('-' * 100)
    pulled, bad = [], 0
    for label, path, hint, role in PULLS:
        try:
            n, line = AF.find(path, hint)
            needle_pull.pull(path, line)
        except Exception as e:
            bad += 1
            rec('  ### ### **NOT PULLED** : %s -- %s' % (label, str(e)[:120]))
            continue
        pulled.append(dict(label=label, role=role, file=os.path.basename(path), line=n,
                           text=line.rstrip()))
        rec('')
        rec('  [%-14s] %s' % (role, label))
        rec('      `%s`:%d' % (os.path.basename(path), n))
        rec('      | %s' % line.rstrip()[:210])
    rec('')
    rec('  ### quotations pulled : %d of %d   ### NOT PULLED : %d' % (len(pulled), len(PULLS), bad))
    if bad:
        rec('  ### ### **A FILING MISSING A HALF IS NOT A FILING.**')
        run_clock.write(D, 'b374_funceq_notes', LINES)
        return 1

    by = {x['role']: x for x in pulled}
    rec('')
    rec('-' * 100)
    rec('  ### (2) THE FILING.')
    rec('-' * 100)
    rec('')
    rec('  ### ### ### **THE FUNCTIONAL EQUATION, READ AT THE LEVEL OF THE FAMILY.**')
    rec('')
    rec('  ### **HALF ONE -- THE REFLECTION.** ### `b291` derived it and stated it as:')
    rec('      | %s' % by['HALF ONE']['text'].strip()[:200])
    rec('  ### The transform carries a member of the two-parameter family to the member with its two')
    rec('  ### parameters exchanged. ### **THAT IS A REFLECTION ACROSS THE DIAGONAL OF THE FAMILY**, and')
    rec('  ### `b291` says so in the same section:')
    rec('      | %s' % by['THE DIAGONAL']['text'].strip()[:200])
    rec('')
    rec('  ### **AND THE GRADE IS THE ACT`S OWN AND NAMES ITS OWN IMPORT:**')
    rec('      | %s' % by['THE GRADE']['text'].strip()[:200])
    rec('  ### ### **THIS FILING DOES NOT RAISE IT, LOWER IT, OR RESTATE IT WITHOUT THE IMPORT.**')
    rec('')
    rec('  ### **HALF TWO -- THE SELF-DUAL POINT.** ### `b291`, immediately after the reflection:')
    rec('      | %s' % by['HALF TWO']['text'].strip()[:200])
    rec('  ### The corpus`s object sits at the point the reflection fixes. ### **THAT IS WHAT `SELF-DUAL')
    rec('  ### ### POINT OF THAT REFLECTION` MEANS HERE, AND IT MEANS NOTHING MORE.**')
    rec('')
    rec('  ### ### ### **AND THE LIMIT, IN THE SAME ACT`S OWN WORDS, IN THE FILING AND NOT IN A')
    rec('  ### ### ### FOOTNOTE:**')
    rec('      | %s' % by['THE LIMIT']['text'].strip()[:200])
    rec('  ### ### **SO THE READING IS ARCHIMEDEAN AND THE ACT SAID SO WHEN IT MADE IT.**')
    rec('')
    rec('  ### **AND THE FINITE TWO-RADIUS FAMILY IS A DIFFERENT ACT AND IS NAMED AS ONE:**')
    rec('      | %s' % by['THE OTHER ACT']['text'].strip()[:200])
    rec('  ### ### **A CONSTRUCTION AND A REFLECTION ARE NOT ONE STATEMENT BECAUSE THEY CAN BE WRITTEN')
    rec('  ### ### IN ONE SENTENCE.** ### `b293` built a finite family; `b291` reflected an archimedean')
    rec('  ### one and recorded that it did not extend the reflection. ### **THIS FILING JOINS NOTHING')
    rec('  ### ### THEY DID NOT JOIN**, and a reader who wants them joined is reading a question, not a')
    rec('  ### result.')
    rec('')
    rec('  ### **WHAT THIS FILING IS FOR:** ### the record now has ### **ONE PLACE** ### where the two')
    rec('  ### halves sit together with the grade and the limit attached, so a later act asking *is')
    rec('  ### there a functional equation at the level of the family* is handed the answer the acts')
    rec('  ### actually gave -- ### **AND THE SHAPE OF WHAT THEY DID NOT GIVE.**')
    rec('')
    rec('=' * 100)
    rec('  ### **NO NEW MATHEMATICS. ### NO GRADE CONFERRED, RAISED OR MOVED. ### NO BAR SET.**')
    rec('  ### **NOTHING IS CLAIMED BEYOND WHAT THE TWO ACTS STATE.**')
    rec('=' * 100)
    p = run_clock.write(D, 'b374_funceq_notes', LINES)
    io.open(os.path.join(D, 'b374_funceq.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(pulled=len(pulled), not_pulled=bad, quotations=pulled,
                        halves=2, limit_in_filing=True, joined_beyond_acts=0,
                        grades_conferred=0, bars_set=0, new_mathematics=0,
                        run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
                   indent=1, ensure_ascii=False))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
