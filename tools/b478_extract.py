# -*- coding: utf-8 -*-
"""b478_extract.py -- THE SURVEY, AND THE COUNTED REHEARSAL UNDER (R70).

### ### **THE CELL RULE, FIXED HERE BEFORE ANY CELL IS READ:**
###   `SAME OBJECT` -- the site's INDEX is the constituent's own VARIABLE, by the two entries' own text.
###   `TOUCHES`     -- the site's statement, if supplied, would constrain that constituent's grade,
###                    the two entries naming the same object.
###   `APART`       -- neither.
### ### **EVERY NON-`APART` CELL CARRIES DECIDING WORDS FROM BOTH SIDES, AND THIS TOOL VERIFIES EACH
### QUOTATION VERBATIM IN ITS OWN SOURCE** -- the site's in `FACES_LEDGER.md:31`, the constituent's in
### the `E0` rows at `FINDINGS.md:3045` and `:3060`. ### A quotation that is not found is a MISS.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
NL = chr(10)
L, MISSES = [], []
SITES = ('i', 'ii', 'iii', 'iv', 'v', 'vi')
KS = ('K1', 'K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8')

# ### THE CELLS. ### Only the non-APART ones are listed; every other pair is APART by the rule above.
# ### Each carries (verdict, the site's own words, the constituent's own words).
CELLS = {
    ('i', 'K8'): ('SAME OBJECT',
                  'are UNOWNED, and they are the clause',
                  'over the class (infinite) and, through the explicit formula, over the zeros'),
    ('i', 'K1'): ('TOUCHES',
                  'over the class, infinite',
                  'a local proposition per seed (lawful or not)'),
    ('i', 'K2'): ('TOUCHES',
                  'they are the clause',
                  'for every `g` with the vanishing conditions'),
    ('ii', 'K8'): ('SAME OBJECT',
                   'one convergent series did what sixty boxes of argument principle could not do for the height',
                   'through the explicit formula, over the zeros'),
    ('ii', 'K2'): ('TOUCHES',
                   'BOUNDED BY A MEASUREMENT and not by an argument',
                   'for a lawful `f` the pole term vanishes'),
    ('iii', 'K1'): ('TOUCHES',
                    'AN EXHAUSTION AT EVERY WIDTH IS NOT AN EXHAUSTION ACROSS WIDTHS',
                    'a local proposition per seed (lawful or not)'),
    ('iii', 'K2'): ('TOUCHES',
                    'the criterion quantifies over the union of all supports',
                    'for every `g` with the vanishing conditions'),
    ('iii', 'K8'): ('TOUCHES',
                    'Boas-Kac exhausts the admissible class AT a support',
                    'over the class (infinite)'),
    ('iv', 'K4'): ('TOUCHES',
                   'against an archimedean quantity',
                   'prime side IS the source’s finite-places sum'),
    ('iv', 'K5'): ('TOUCHES',
                   'against an archimedean quantity',
                   'the sign certified at every frame, the size at none'),
    ('iv', 'K2'): ('TOUCHES',
                   'one statement uniform in `a`',
                   'the corpus’s convention `places = PR - A`'),
    ('iv', 'K8'): ('TOUCHES',
                   'indexed by the width `a`',
                   'over the class (infinite)'),
}

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


def read(p):
    try:
        return io.open(p, encoding='utf-8', errors='replace').read()
    except Exception:
        return ''


def norm(s):
    s = s.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    s = s.replace('—', '--').replace('–', '-').replace('–', '-')
    s = s.replace('→', '->')
    return re.sub(r'\s+', ' ', s).strip().upper()


def main():
    rec('=' * 104)
    rec('b478 -- THE SURVEY. ### THE CELL RULE IS FIXED IN THIS FILE`S OWN HEAD, BEFORE ANY CELL.')
    rec('=' * 104)

    # ### the two sources, each read at its own address
    row = read(os.path.join(PP, 'FACES_LEDGER.md')).split(NL)[30]
    fd = read(os.path.join(PP, 'FINDINGS.md')).split(NL)
    if not row.startswith('| U1 |'):
        MISSES.append(('FACES_LEDGER.md', 'row U1 at :31'))
    e0 = {}
    for n in list(range(3045, 3055)) + list(range(3059, 3070)):
        m = re.match(r'\| \*\*(K\d)\*\* ([^|]+)\|(.*)$', fd[n])
        if m:
            k = m.group(1)
            e0.setdefault(k, dict(name=m.group(2).strip(), text='', lines=[]))
            e0[k]['text'] += ' ' + fd[n]
            e0[k]['lines'].append(n + 1)
    rec('')
    rec('(P1) THE TWO SOURCES, AT THEIR ADDRESSES.')
    rec('-' * 104)
    rec('    row U1        : FACES_LEDGER.md:31, %d characters' % len(row))
    rec('    the E0 rows   : FINDINGS.md:3045-3054 (kinds) and :3060-3069 (grades) -- %d constituents'
        % len(e0))
    for k in KS:
        rec('      %s %-52s lines %s' % (k, e0[k]['name'][:52], e0[k]['lines']))
    if sorted(e0) != sorted(KS):
        MISSES.append(('FINDINGS.md', 'E0 rows %d of 8' % len(e0)))

    rec('')
    rec('(P2) THE REHEARSAL UNDER (R70): THE ONE PAIR b472 FOUND, (i) AGAINST K8.')
    rec('-' * 104)
    v, sq, kq = CELLS[('i', 'K8')]
    site_ok = norm(sq) in norm(row)
    k_ok = norm(kq) in norm(e0['K8']['text'])
    rec('    the cell returned          : ### **%s**' % v)
    rec('    the site`s own words       : "%s"  -- found in row U1 : %s' % (sq, site_ok))
    rec('    the constituent`s own words: "%s"  -- found in K8 : %s' % (kq, k_ok))
    rec('    b472`s independent finding : the only site of six whose text shares a six-word run with an')
    rec('      E0 row, and the row was K8 -- reached by a different test (a word-aligned run), so the')
    rec('      two agree without either being the other`s evidence.')
    if not (site_ok and k_ok and v == 'SAME OBJECT'):
        MISSES.append(('rehearsal', '(i) x K8'))

    rec('')
    rec('(P3) EVERY DECLARED CELL, WITH BOTH QUOTATIONS VERIFIED IN ITS OWN SOURCE.')
    rec('-' * 104)
    table = {}
    for s in SITES:
        for k in KS:
            if (s, k) in CELLS:
                v, sq, kq = CELLS[(s, k)]
                a = norm(sq) in norm(row)
                b = norm(kq) in norm(e0[k]['text'])
                if not a:
                    MISSES.append(('%s x %s' % (s, k), 'site words not in row U1: %s' % sq[:50]))
                if not b:
                    MISSES.append(('%s x %s' % (s, k), 'constituent words not in %s: %s' % (k, kq[:50])))
                table[(s, k)] = dict(verdict=v, site_words=sq, k_words=kq, site_found=a, k_found=b)
                rec('    (%-3s) x %-3s %-12s site %s ; constituent %s' % (s, k, v, a, b))
            else:
                table[(s, k)] = dict(verdict='APART', site_words='', k_words='', site_found=None, k_found=None)
    same = [(s, k) for (s, k), c in table.items() if c['verdict'] == 'SAME OBJECT']
    touch = [(s, k) for (s, k), c in table.items() if c['verdict'] == 'TOUCHES']
    rec('  ### ### **SAME OBJECT %d ; TOUCHES %d ; APART %d ; CELLS %d.**'
        % (len(same), len(touch), 48 - len(same) - len(touch), len(table)))

    rec('')
    rec('(P4) THE TWO REVERSE READS.')
    rec('-' * 104)
    ktouched = sorted({k for (s, k), c in table.items() if c['verdict'] != 'APART'},
                      key=lambda x: KS.index(x))
    kuntouched = [k for k in KS if k not in ktouched]
    stouched = sorted({s for (s, k), c in table.items() if c['verdict'] != 'APART'},
                      key=lambda x: SITES.index(x))
    suntouched = [s for s in SITES if s not in stouched]
    rec('    constituents touched by at least one site : %s' % ', '.join(ktouched))
    rec('    ### ### **CONSTITUENTS NO SITE TOUCHES : %s**' % ', '.join(kuntouched))
    rec('    sites touching at least one constituent : %s' % ', '.join(stouched))
    rec('    ### ### **SITES NO CONSTITUENT TOUCHES : %s**' % ', '.join(suntouched))

    rec('')
    rec('=' * 104)
    rec('  ### MISSES : %d %s' % (len(MISSES), MISSES or ''))
    rec('=' * 104)
    io.open(os.path.join(D, 'b478_extract.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    json.dump(dict(cells={'%s|%s' % k: v for k, v in table.items()},
                   same_object=['%s|%s' % p for p in same], touches=['%s|%s' % p for p in touch],
                   k_touched=ktouched, k_untouched=kuntouched,
                   s_touched=stouched, s_untouched=suntouched,
                   e0_names={k: e0[k]['name'] for k in KS}, misses=MISSES),
              io.open(os.path.join(D, 'b478_survey.json'), 'w', encoding='utf-8', newline=NL),
              indent=1, ensure_ascii=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
