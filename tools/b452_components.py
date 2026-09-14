# -*- coding: utf-8 -*-
"""b452_components.py -- THE CLASS BOUNDARY READ BY ITS SIDE, AND THE SIX SITES READ BY THEIR GENERATOR. ### **AFTER THE LOCK.**

### Usage: `dump` -- every failure's class text at its failing step, its quotations, its site's object, and the R1/R2 word hits;
###        `report` -- the face's test applied, with the hand read below, into data/b452_components.txt, b452_sides.json, b452_sites.json.
### ### No re-expression is performed, no candidate re-attempted, no site proposed.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
OUT = os.path.join(D, 'b452_components.txt')
SIDESJ = os.path.join(D, 'b452_sides.json')
SITESJ = os.path.join(D, 'b452_sites.json')
DUMP = os.path.join(D, 'b452_dump.json')
NL = chr(10)
SITES = [('i', 'b424_candidates.json'), ('ii', 'b427_candidates.json'), ('iii', 'b428_candidates.json'),
         ('iv', 'b436_candidates.json'), ('v', 'b442_site_v.json'), ('vi', 'b443r_site_vi.json')]
R1_WORDS = re.compile(r'(?i)\bnetwork|representation matrix|\bprobe|\bactivation')
R2_WORDS = re.compile(r'(?i)\bsupport|\bwindow|\bwidth|prime[s]? (?:enter|involved)|no prime|rational primes are not')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(p):
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13) + chr(10), NL)


def dump_json(p, o):
    io.open(p + '.tmp', 'w', encoding='utf-8').write(json.dumps(o, indent=1, ensure_ascii=False))
    os.replace(p + '.tmp', p)


def site_objects():
    out = {}
    for l in read(os.path.join(D, 'b443r_u1_draft.md')).split(NL):
        m = re.match(r'^\| \*\*\((i|ii|iii|iv|v|vi)\)\*\* ([^|]+)\| ([^|]+)\| ([^|]+)\|', l)
        if m:
            out[m.group(1)] = dict(site=m.group(2).strip(), holds=m.group(3).strip(), missing=m.group(4).strip())
    return out


def failures():
    objs = site_objects()
    rows = []
    for s, p in SITES:
        for c in json.load(io.open(os.path.join(D, p), encoding='utf-8'))['candidates']:
            if 'steps' in c:
                k = (c.get('first') or 1) - 1
                why = c['steps'][k]['why'] if c['steps'] else ''
                qs = [q.get('text', '') for q in c.get('quotes', []) if q.get('step') == k + 1]
            elif 'why' in c:
                why = c.get('why', '')
                qs = [q.get('text', '') if isinstance(q, dict) else str(q) for q in c.get('quotes', [])]
            else:
                why = c.get('verdict', '')
                qs = []
            label = c['kind']
            body = re.sub(r'^\s*' + re.escape(label) + r'\s*(--)?\s*', '', why or '').strip()
            text = ' '.join([body] + qs)
            rows.append(dict(site=s, id=c['id'], name=c['name'], kind=label, class_text=body, quotes=qs,
                             object=objs.get(s, {}), r1=sorted(set(m.group(0).lower() for m in R1_WORDS.finditer(text + ' ' + json.dumps(objs.get(s, {}))))),
                             r2=sorted(set(m.group(0).lower() for m in R2_WORDS.finditer(text)))))
    return rows


def dump():
    rows = failures()
    dump_json(DUMP, rows)
    for r in rows:
        print('(%s) %-4s %-26s R1%s R2%s | %s' % (r['site'], r['id'], r['kind'][:26], r['r1'] or '', r['r2'] or '', r['name'][:70]))
        print('       CLASS: %s' % r['class_text'][:300])
        for q in r['quotes'][:2]:
            print('       QUOTE: %s' % ' '.join(q.split())[:300])
    print('failures %d ; K1 %d' % (len(rows), sum(1 for r in rows if r['kind'] == 'CLASS BOUNDARY')))
    return 0


# ------------------------------------------------------------------------------------------------ THE HAND READ OF THE WORD TEST'S HITS
R2_CLAUSE_WINDOW = ('the largest prime-free window is `(1/2, 2)`, and the largest one-prime window is `(1/3, 3)` '
                    '(day1/Exhaustive_Enumeration.md:171)')
R2_CLAUSE_WIDTH = ('support truncation controls width exactly as `2 log a` (OPEN_TRAILS-archive-2-historical-landings-and-programs.md:8431): '
                   'one support fixes one width')
R2_CLAUSE_DISTINCT = ('index truncation does not localise support ... `DISTINCT` between the two kinds '
                      '(OPEN_TRAILS-archive-2-historical-landings-and-programs.md:8431)')
# (site, id) -> (applies, verdict, clause or missing, why)
HAND = {
    ('i', 'C1'): (True, 'SOURCE-SIDE', R2_CLAUSE_WINDOW, 'the class is the prime-free support; the site`s object quantifies over the whole class, which "CARRIES NONE" of that hypothesis, so its supports reach past the window'),
    ('i', 'C5'): (True, 'SOURCE-SIDE', R2_CLAUSE_WINDOW, 'the same prime-free support class; the same object'),
    ('i', 'C2'): (True, 'SOURCE-SIDE', R2_CLAUSE_WIDTH, 'the class is one support with a^2 >= 2; the object ranges over every support, and one support is one width'),
    ('i', 'C3'): (True, 'SOURCE-SIDE', R2_CLAUSE_WIDTH, 'the class is one width at a time; the object is the union over widths'),
    ('iii', 'C3'): (True, 'SOURCE-SIDE', R2_CLAUSE_WIDTH, 'Boas-Kac exhausts AT a width; the object is one g serving every width'),
    ('iii', 'C5'): (True, 'SOURCE-SIDE', R2_CLAUSE_WINDOW, 'the prime-free support class; the object serves every width'),
    ('iii', 'C6'): (True, 'SOURCE-SIDE', R2_CLAUSE_WINDOW, 'the prime-free support at one width; the object serves every width'),
    ('iii', 'C7'): (True, 'SOURCE-SIDE', R2_CLAUSE_WINDOW, '"small enough intervals" is a window condition; the object serves every width, beyond any prime-free window'),
    ('iii', 'C12'): (True, 'SOURCE-SIDE', R2_CLAUSE_DISTINCT, 'the class is indexed by n, which the bank says "is not a support width"; R2 holds index and support DISTINCT'),
    ('ii', 'B8'): (True, 'UNDECIDED', 'the support of the test function the height site`s object is evaluated with', 'the class is the prime-free support; the bank says the condition is "on the test function and not on the height" and does not state that function`s support'),
    ('ii', 'B9'): (True, 'UNDECIDED', 'the support of the test function the height site`s object is evaluated with', 'the same class as B8 and the same silence on the object`s support'),
    ('iii', 'C17'): (False, None, None, '"width" occurs only in "not a statement across widths"; the class is a seven-cell decided list, not a support window -- R2 does not apply'),
    ('iii', 'C18'): (False, None, None, '"support widths" occurs only in "not over support widths"; the class is bases and levels -- R2 does not apply'),
    ('iii', 'C20'): (False, None, None, '"supports" occurs only in "not supports"; the class is dilations in L2 -- R2 does not apply'),
    ('i', 'C8'): (False, None, None, '"window" is "AVAILABLE at the window"; the class is a page of an artefact -- R2 does not apply'),
    ('ii', 'B7'): (False, None, None, 'the same Proposition C.1 page -- R2 does not apply'),
    ('iii', 'C8'): (False, None, None, 'the same Proposition C.1 page -- R2 does not apply'),
    ('iii', 'C1'): (False, None, None, 'support and width name the evaluator`s reach, not a class the source ranges over -- R2 does not apply'),
    ('iii', 'C10'): (False, None, None, 'the evaluator`s measured reach, not a class -- R2 does not apply'),
    ('iii', 'C2'): (False, None, None, 'an absence: "NOT LOCATED in the pinned source" -- no class to apply R2 to'),
    ('iii', 'C4'): (False, None, None, 'an absence: "NOT LOCATED in the pinned source" -- no class to apply R2 to'),
}
THIN = re.compile(r'^\s*(FAILED AT A QUOTED STEP)?\s*$')


def decide(r):
    key = (r['site'], r['id'])
    if THIN.match(r['class_text'] or '') and not r['quotes']:
        return dict(verdict='UNDECIDED', clause=None, missing='the class the source ranges over (the bank records only "%s")' % (r['class_text'] or 'nothing'),
                    applies=None, why='the bank carries no class text beyond its verdict')
    if r['r1']:
        return dict(verdict='UNREAD', clause=None, missing='R1 hit not hand-read', applies='R1', why='')
    if key in HAND:
        ap, v, cl, why = HAND[key]
        if ap:
            if v == 'UNDECIDED':
                return dict(verdict=v, clause=None, missing=cl, applies='R2', why=why)
            return dict(verdict=v, clause=cl, missing=None, applies='R2', why=why)
        if r['r2']:
            return dict(verdict='SOURCE-SIDE', clause='%s -- with no held re-expression having this class or this object in its domain' % r['class_text'][:220],
                        missing=None, applies='none (R2 word hit hand-read as a mention)', why=why)
    if r['r2']:
        return dict(verdict='UNREAD', clause=None, missing='R2 hit not hand-read', applies='R2?', why='')
    return dict(verdict='SOURCE-SIDE', clause='%s -- with no held re-expression having this class or this object in its domain' % r['class_text'][:220],
                missing=None, applies='none', why='no R1 or R2 word in the class text or the site`s object')


def report():
    L = []

    def rec(s=''):
        L.append(s)
        print(s)

    rows = failures()
    for r in rows:
        r.update(decide(r))
    k1 = [r for r in rows if r['kind'] == 'CLASS BOUNDARY']
    non = [r for r in rows if r['kind'] != 'CLASS BOUNDARY']
    rec('=' * 110)
    rec('b452 -- THE CLASS BOUNDARY READ BY ITS SIDE, AND THE SIX SITES READ BY THEIR GENERATOR. ### AFTER THE LOCK.')
    rec('=' * 110)
    rec('')
    rec('  ### ### **COMPONENT 1 -- WHICH SIDE THE BOUNDARY IS ON, PER CANDIDATE.**')
    rec('    R1 (REPARAMETERIZATION_BARRIERS_v0_1.md:94-101): GL(n)/O(n) reparameterizations of a network`s representations -- domain: a network`s representations.')
    rec('    R2 (Exhaustive_Enumeration.md:171; archived OPEN_TRAILS:8431): support as width 2 log a; prime-free window (1/2, 2); index DISTINCT from support.')
    rec('    word test yield over all 82 failures: R1 %d ; R2 %d (K1 %d, non-K1 %d) ; every R2 hit hand-read below.'
        % (sum(1 for r in rows if r['r1']), sum(1 for r in rows if r['r2']), sum(1 for r in k1 if r['r2']), sum(1 for r in non if r['r2'])))
    rec('')
    for s, _p in SITES:
        rec('    ### SITE (%s) -- the object: %s' % (s, (next((r['object'].get('missing', '') for r in rows if r['site'] == s), ''))[:130]))
        for r in [x for x in k1 if x['site'] == s]:
            rec('      %-4s %-12s %s' % (r['id'], r['verdict'], r['name'][:80]))
            rec('           class, as the bank quotes it : %s' % (r['class_text'] or '(none)')[:200])
            if r['quotes']:
                rec('           quotation at the step        : %s' % ' '.join(r['quotes'][0].split())[:200])
            if r['verdict'] == 'SOURCE-SIDE':
                rec('           deciding clause              : %s' % r['clause'][:220])
            elif r['verdict'] == 'UNDECIDED':
                rec('           missing                      : %s' % r['missing'][:200])
            if r.get('why'):
                rec('           hand read                    : %s' % r['why'][:200])
    parts = dict((v, [r for r in k1 if r['verdict'] == v]) for v in ('OBJECT-SIDE', 'SOURCE-SIDE', 'UNDECIDED', 'UNREAD'))
    rec('')
    rec('    THE PARTITION OF THE %d K1 CANDIDATES:' % len(k1))
    rec('      %-6s %-12s %-12s %-10s %s' % ('site', 'OBJECT-SIDE', 'SOURCE-SIDE', 'UNDECIDED', 'K1'))
    for s, _p in SITES:
        rec('      (%-4s %-12d %-12d %-10d %d' % (s + ')', sum(1 for r in parts['OBJECT-SIDE'] if r['site'] == s), sum(1 for r in parts['SOURCE-SIDE'] if r['site'] == s),
                                               sum(1 for r in parts['UNDECIDED'] if r['site'] == s), sum(1 for r in k1 if r['site'] == s)))
    rec('      %-6s %-12d %-12d %-10d %d' % ('total', len(parts['OBJECT-SIDE']), len(parts['SOURCE-SIDE']), len(parts['UNDECIDED']), len(k1)))
    rec('  ### ### **OBJECT-SIDE %d ; SOURCE-SIDE %d ; UNDECIDED %d ; UNREAD %d ; SUM %d OF 47.**'
        % (len(parts['OBJECT-SIDE']), len(parts['SOURCE-SIDE']), len(parts['UNDECIDED']), len(parts['UNREAD']), sum(len(v) for v in parts.values())))
    rec('    SOURCE-SIDE by what decided it: R2 applied %d ; no held re-expression in the class`s or object`s domain %d'
        % (sum(1 for r in parts['SOURCE-SIDE'] if r['applies'] == 'R2'), sum(1 for r in parts['SOURCE-SIDE'] if r['applies'] != 'R2')))
    rec('')
    rec('    THE POSITIVE CONTROL -- the same test over the %d non-K1 failures:' % len(non))
    for r in [x for x in non if x['r2'] or x['r1']]:
        rec('      (%s) %-4s %-26s %s -- %s' % (r['site'], r['id'], r['kind'][:26], r['verdict'], (r.get('why') or '')[:120]))
    ctrl = [r for r in non if r['verdict'] == 'OBJECT-SIDE']
    rec('  ### ### **THE CONTROL IS %s** -- %d non-K1 failures OBJECT-SIDE by the same test.%s'
        % ('FIRED' if ctrl else 'ABSENT', len(ctrl), '' if ctrl else ' ### ABSENT IS NOT PASSED: the test has not been shown able to say OBJECT-SIDE.'))
    rec('    ### NO RE-EXPRESSION WAS PERFORMED; THE ACT READ WHETHER ONE IS HELD.')
    dump_json(SIDESJ, dict(rows=rows, partition=dict((v, [(r['site'], r['id']) for r in parts[v]]) for v in parts),
                           counts=dict((v, len(parts[v])) for v in parts), control=len(ctrl), control_state=('FIRED' if ctrl else 'ABSENT'),
                           r1_yield=sum(1 for r in rows if r['r1']), r2_yield=sum(1 for r in rows if r['r2'])))

    # ---------------------------------------------------------------------------------------- COMPONENT 2
    rec('')
    rec('  ### ### **COMPONENT 2 -- THE SIX SITES, BY WHAT NAMED THEM.**')
    acts = [('(i)-(iii)', 'b355', 'b355_sortie_closing.txt', '### The shape common to three places where the record needs a statement UNIFORM in an index and holds'),
            ('(iv)', 'b401', 'b401_the_absent_element_searched.txt', '**SCOPE: THE ABSENT ELEMENT SEARCHED, AND THE FOURTH SITE ENTERED.**'),
            ('(v)-(vi)', 'b404', 'b404_the_fifth_and_sixth_sites.txt', "**SCOPE: THE FIFTH SITE ENTERED, THE SIXTH ENTERED, AND THE ROW'S LAW STRAINED.**")]
    RULEW = re.compile(r'(?i)generated by|\bevery (?:site|place|instance|index)\b|the range\b|exhaust')
    site_rows = []
    for sites, act, f, needle in acts:
        ls = read(os.path.join(D, f)).split(NL)
        i = next((n for n, l in enumerate(ls, 1) if needle in l), None)
        hits = [(n, l.strip()) for n, l in enumerate(ls, 1) if RULEW.search(l) and ('U1' in l or 'site' in l.lower() or 'instance' in l.lower())]
        rec('    %-9s named by %s at %s:%s' % (sites, act, f, i))
        rec('              | %s' % (' '.join(ls[i - 1].split())[:200] if i else '### NOT LOCATED'))
        rec('              rule-word hits beside a site or instance: %d' % len(hits))
        for n, l in hits[:4]:
            rec('                %s:%d | %s' % (f, n, l[:170]))
            if act == 'b404' and 'crt_exhaustiveness' in l:
                rec('                HAND READ: the word matched is `crt_exhaustiveness`, a kernel theorem named in Addition Two -- a mention, not a rule naming sites')
        site_rows.append(dict(sites=sites, act=act, address='%s:%s' % (f, i), rule_hits=[(n, l[:200]) for n, l in hits]))
    fl = read(os.path.join(PP, 'FACES_LEDGER.md')).split(NL)
    law_i = next((n for n, l in enumerate(fl, 1) if l.startswith('| U1 |')), None)
    law = re.search(r'### \*\*THE SHAPE, NAMED AND NOT PROVED: ([^*]+)\*\*', fl[law_i - 1]) if law_i else None
    rec('    the row`s own criterion, FACES_LEDGER.md:%s : "THE SHAPE, NAMED AND NOT PROVED: %s"' % (law_i, law.group(1).strip() if law else '### NOT LOCATED'))
    rec('    ### THAT IS A MEMBERSHIP TEST -- it says what makes a place a site -- AND NOT A GENERATOR: it prints no finite range.')
    closed = False
    rec('  ### ### **VERDICT : %s.** Each site was entered by an act that found it: three at b355, the fourth at b401, the fifth and sixth at b404.' % ('A CLOSED ENUMERATION' if closed else 'A LIST, ASSEMBLED SITE BY SITE'))
    need = ('a generator with a finite range printed on its face -- for instance the explicit formula`s channels or the pentagon`s registers, if the author rules one '
            'of them the index set -- and, for every member of that range, either the site it yields or a statement that the uniformity obstruction does not arise there')
    rec('    WHAT THE RECORD WOULD NEED TO CLOSE IT : %s.' % need)
    rec('    ### NO SEVENTH SITE IS PROPOSED; THE RANGES NAMED ABOVE ARE THE ORDER`S EXAMPLES, NOT A CHOICE.')
    dump_json(SITESJ, dict(acts=site_rows, law_line=law_i, law=(law.group(1).strip() if law else None), verdict=('CLOSED' if closed else 'LIST'), need=need))

    # ---------------------------------------------------------------------------------------- EXPECTATIONS
    rec('')
    rec('  ### ### **THE EXPECTATIONS.**')
    n1 = 'HELD' if parts['OBJECT-SIDE'] else 'REFUTED'
    n2 = 'HELD' if not closed else 'REFUTED'
    rec('    (N1) OBJECT-SIDE is not empty                                ### %s -- OBJECT-SIDE %d; the control %s' % (n1, len(parts['OBJECT-SIDE']), 'FIRED' if ctrl else 'ABSENT'))
    rec('    (N2) the six sites are a LIST and not a closed enumeration   ### %s' % n2)
    rec('    ### the seat`s own from the face: (N1) REFUTED -- %s; (N2) HELD -- %s.' % ('HELD' if n1 == 'REFUTED' else 'REFUTED', 'HELD' if n2 == 'HELD' else 'REFUTED'))
    rec('    ### beside (N1), not a verdict: with the control ABSENT the test has shown it can say SOURCE-SIDE and UNDECIDED and has not shown')
    rec('    ### it can say OBJECT-SIDE, so an empty OBJECT-SIDE here is a result of this test over these two sources and no wider.')
    rec('')
    rec('    ### NO RE-EXPRESSION PERFORMED. ### NO SITE PROPOSED. ### NO GRADE MOVED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO. ### THE FOUR LISTS ARE OPEN.')
    rec('=' * 110)
    S = json.load(io.open(SIDESJ, encoding='utf-8'))
    S['expect'] = dict(n1=n1, n2=n2)
    dump_json(SIDESJ, S)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'dump'
    sys.exit(dict(dump=dump, report=report)[mode]())
