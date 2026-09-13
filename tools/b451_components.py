# -*- coding: utf-8 -*-
"""b451_components.py -- THE RECONCILIATION'S REMAINDER NAMED, AND THE ROUTED ITEMS GROUPED. ### **AFTER THE LOCK.**

### Usage: `lore` -- the filing's one line appended to TECHNE PREDICATE_ONE_SHAPE.md (prior bytes proved a prefix);
###        `report` -- Components 1 and 2 into data/b451_components.txt, data/b451_remainder.json, data/b451_kinds.json.
### ### No keystone is opened. No matcher is edited. Every count is read off a bank.
"""
import io
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TE = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')
LORE = os.path.join(TE, 'modules', '2026-09', 'PREDICATE_ONE_SHAPE.md')
OUT = os.path.join(D, 'b451_components.txt')
REMJ = os.path.join(D, 'b451_remainder.json')
KINDJ = os.path.join(D, 'b451_kinds.json')
LORERUN = os.path.join(D, 'b451_lore_append_run.txt')
NL = chr(10)
LINE = ('- **Incidents after the mint (b451):** b390’s version matcher, which required the version to follow the name with only '
        'backticks or spaces between (b391 re-measured `28` across `11` as `32` across `13`, relay `data/b391_components.txt`); '
        'b394’s repository matcher, which knew only a backticked lowercase name and banked a ceiling of eleven unreachable keystones '
        'that b395 answered (`data/b395_the_ceiling_answered.txt`); and b450’s two — the table-header test that required a first '
        'header cell of exactly `claim` and counted `0` rows under `5` tables headed `Claim (as stated here)`, and the file-name '
        'citation matcher that found `0` citations where a title-name shape found `8` (`data/b450_components.txt`). '
        'Work-order `W-ORD-MATCHER-SHAPE` is filed with b451’s trail record.')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def read(p):
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13) + chr(10), NL)


def dump(p, o):
    io.open(p + '.tmp', 'w', encoding='utf-8').write(json.dumps(o, indent=1, ensure_ascii=False))
    os.replace(p + '.tmp', p)


def line_of(path, needle):
    for i, l in enumerate(read(path).split(NL), 1):
        if needle in l:
            return i, l
    return None, ''


def lore():
    before = open(LORE, 'rb').read()
    out = []
    if 'Incidents after the mint (b451)' in before.decode('utf-8'):
        out.append('the b451 line is already present; nothing appended')
    else:
        nl = b'\r\n' if b'\r\n' in before else b'\n'
        new = before.rstrip(b'\r\n') + nl + nl + LINE.encode('utf-8') + nl
        open(LORE + '.tmp', 'wb').write(new)
        os.replace(LORE + '.tmp', LORE)
        after = open(LORE, 'rb').read()
        added = [x for x in after[len(before.rstrip(b'\r\n')):].split(b'\n') if x.strip()]
        out.append('PREDICATE_ONE_SHAPE.md : PRIOR BYTES A TRUE PREFIX : %s' % ('YES' if after.startswith(before.rstrip(b'\r\n')) else 'NO'))
        out.append('non-empty lines added : %d' % len(added))
    io.open(LORERUN, 'w', encoding='utf-8', newline=NL).write(NL.join(out) + NL)
    print(NL.join(out))
    return 0


def report():
    L = []

    def rec(s=''):
        L.append(s)
        print(s)

    rec('=' * 110)
    rec('b451 -- THE RECONCILIATION`S REMAINDER NAMED, AND THE ROUTED ITEMS GROUPED BY THE RULING EACH NEEDS. ### AFTER THE LOCK.')
    rec('=' * 110)

    # ---------------------------------------------------------------------------------------- COMPONENT 1
    rec('')
    rec('  ### ### **COMPONENT 1 -- THE REMAINDER, FROM THE BANKS.**')
    cen = read(os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')).split(NL)
    population = [re.match(r'\|\s*`([A-Za-z_0-9]+)`', cen[i - 1]).group(1) for i in range(73, 89) if re.match(r'\|\s*`([A-Za-z_0-9]+)`', cen[i - 1])]
    b390_path = os.path.join(D, 'b390_the_proofreading_pass.txt')
    b390_line, b390_txt = line_of(b390_path, '### ### **AND EVERY PIN `ADDITIVE_MULTIPLICATIVE_CONSPIRACY` CITES RESOLVES')
    b390 = [k for k in population if ('`%s`' % k) in b390_txt]
    b394_line, b394_txt = line_of(os.path.join(D, 'b394_the_reconciliation_batched.txt'), '### ### **THE THREE : ')
    b394 = [k for k in re.findall(r'`([A-Z_0-9]+)`', b394_txt)]
    b450_line, b450_txt = line_of(os.path.join(D, 'b450_the_eligible_set_and_the_batch.txt'), '**Eligible (11), in census order:**')
    b450 = re.findall(r'`([A-Za-z_0-9]+)`', b450_txt.split('.')[0] if False else b450_txt.split(' are marked ')[0])
    b450 = [k for k in b450 if k in population]
    b450 = list(dict.fromkeys(b450))[:11] if len(b450) >= 11 else b450
    sets = [('b390', b390, 'b390_the_proofreading_pass.txt:%s' % b390_line), ('b394', b394, 'b394_the_reconciliation_batched.txt:%s' % b394_line),
            ('b450', b450, 'b450_the_eligible_set_and_the_batch.txt:%s' % b450_line)]
    union, overlaps = [], []
    for act, s, addr in sets:
        for k in s:
            if k in union:
                overlaps.append((k, act))
            else:
                union.append(k)
    remainder = [k for k in population if k not in union]
    strays = [k for k in union if k not in population]
    rec('    the population, THE_KEYSTONE_CENSUS.md:73-88 : %d' % len(population))
    for act, s, addr in sets:
        rec('    %-5s reconciled %2d  at %-46s %s' % (act, len(s), addr, ', '.join(s)))
    rec('    ### THE ARITHMETIC : %d + %d + %d = %d ; overlaps %d %s ; union %d ; outside the population %d ; population %d - union %d = %d'
        % (len(b390), len(b394), len(b450), len(b390) + len(b394) + len(b450), len(overlaps), overlaps or '', len(union), len(strays),
           len(population), len(union), len(remainder)))
    need = []
    if remainder:
        rec('  ### ### **THE ARITHMETIC DOES NOT CLOSE. THE REMAINDER : %d -- %s.**' % (len(remainder), ', '.join(remainder)))
        for k in remainder:
            if k == 'ENUMERA':
                n1, t1 = line_of(os.path.join(D, 'b395_the_ceiling_answered.txt'), '`ENUMERA` names no terminal for any route to reach. ### **WHAT IT NEEDS')
                n2, t2 = line_of(os.path.join(D, 'b395_the_ceiling_answered.txt'), 'IS AN AUTHOR NAMING ITS TERMINAL.**')
                n3, t3 = line_of(os.path.join(D, 'b395_components.txt'), 'so there is nothing to settle and no clone would help')
                rec('    %s -- WHAT IT NEEDS, IN b395`S BANK:' % k)
                rec('      b395_the_ceiling_answered.txt:%s-%s | %s %s' % (n1, n2, t1.strip()[-70:], t2.strip()))
                rec('      b395_components.txt:%s | %s' % (n3, t3.strip()[:160]))
                rec('    ### NEITHER A CLONE NOR A BRANCH-READING RULING: the record says an author naming its terminal. ### ROUTED.')
                need.append(dict(k=k, need='an author naming its terminal', clone=False, branch_ruling=False,
                                 quotes=['b395_the_ceiling_answered.txt:%s-%s' % (n1, n2), 'b395_components.txt:%s' % n3]))
            else:
                rec('    %s -- ### NO NEED LOCATED IN b395`S BANK; ROUTED.' % k)
                need.append(dict(k=k, need=None))
    else:
        rec('  ### ### **THE ARITHMETIC CLOSES. NOTHING REMAINS.** The roster: %s' % ', '.join(population))
    rec('    the roster, for checking : %s' % ', '.join('%s%s' % (k, '' if k in union else ' [UNRECONCILED]') for k in population))
    dump(REMJ, dict(population=population, sets=[dict(act=a, members=s, address=addr) for a, s, addr in sets], union=union,
                    overlaps=overlaps, strays=strays, remainder=remainder, need=need))

    # ---------------------------------------------------------------------------------------- COMPONENT 2
    rec('')
    rec('  ### ### **COMPONENT 2 -- THE TWENTY-NINE, GROUPED BY THE RULING EACH NEEDS.**')
    B = json.load(io.open(os.path.join(D, 'b450_batch.json'), encoding='utf-8'))
    items = B['verdict']['routed_items']
    comp = read(os.path.join(D, 'b450_components.txt')).split(NL)
    head = next(i for i, l in enumerate(comp, 1) if 'THE REPAIRS ROUTED, COUNTED APART : 29' in l)
    rows = []
    for n, (k, what, why) in enumerate(items):
        addr = 'b450_components.txt:%d' % (head + 1 + n)
        clause = why.split(';')[0].strip()
        rest = ';'.join(why.split(';')[1:]).strip()
        if re.search(r'\bis authoring\b', clause):
            kind = 'AUTHORING'
        elif 'registry row' in clause and re.search(r"the author`s|the author's", clause):
            kind = 'REGISTRY ROW'
        elif clause:
            kind = clause.upper()
        else:
            kind = 'THE ITEM DOES NOT SAY'
        form = ('a correspondence table' if 'table' in clause else 'absent material' if 'absent material' in clause
                else 'prose' if 'prose' in clause else 'a registry row' if 'registry row' in clause else '')
        pre = ''
        if re.search(r'not located', rest):
            pre = 'the finding`s form is not located in FINDINGS.md or OPEN_TRAILS.md'
        elif re.search(r'not reproduced|never carried', rest):
            pre = 'the census`s era finding is not reproduced: the keystone never carried the pin'
        rows.append(dict(n=n + 1, keystone=k, what=what, clause=clause, kind=kind, form=form, precondition=pre, address=addr))
    kinds = {}
    for r in rows:
        kinds.setdefault(r['kind'], []).append(r)
    kinds.setdefault('THE ITEM DOES NOT SAY', [])
    UNBLOCK = {
        'AUTHORING': 'the author`s word to write into a keystone: add the era findings it does not carry, rewrite the lines that still call landed branches held, and write the missing correspondence tables -- each keystone edit then becomes a repair an act can make',
        'REGISTRY ROW': 'the author`s recording under (R17): the registry row for INDEX_ARITY_AT_THE_CRITICAL_LINE brought to its head, and rows entered for EXHAUSTIVENESS_LICENSE and THE_RESIDUE_OF_RH',
        'THE ITEM DOES NOT SAY': 'nothing -- no item left its ruling unnamed',
    }
    rec('    items read from b450_batch.json`s routed_items : %d ; addresses b450_components.txt:%d-%d' % (len(rows), head + 1, head + len(rows)))
    rec('')
    rec('    %-22s %-5s %s' % ('KIND', 'COUNT', 'ITEMS (keystone -- what -- form -- address)'))
    for kind in sorted(kinds, key=lambda x: (x == 'THE ITEM DOES NOT SAY', -len(kinds[x]))):
        rs = kinds[kind]
        rec('    %-22s %-5d' % (kind, len(rs)))
        for r in rs:
            rec('        %-34s %-62s %-22s %s%s' % (r['keystone'][:34], r['what'][:62], r['form'], r['address'],
                                                  ('  ### PRECONDITION NAMED: ' + r['precondition']) if r['precondition'] else ''))
        rec('        WHAT A RULING WOULD UNBLOCK : %s' % UNBLOCK.get(kind, '(a kind produced by the items; its line is its clause: %s)' % kind))
    by_form = {}
    for r in kinds.get('AUTHORING', []):
        by_form[r['form']] = by_form.get(r['form'], 0) + 1
    rec('')
    rec('    within AUTHORING, by the form its clause names (not kinds) : %s' % by_form)
    rec('    items naming a precondition beside their ruling : %d %s' % (sum(1 for r in rows if r['precondition']), [(r['keystone'], r['what'][:40]) for r in rows if r['precondition']]))
    real_kinds = [k for k in kinds if kinds[k]]
    rec('  ### ### **KINDS WITH MEMBERS : %d ; THE ITEM DOES NOT SAY : %d ; THE COUNTS SUM TO %d OF %d.**'
        % (len(real_kinds), len(kinds['THE ITEM DOES NOT SAY']), sum(len(v) for v in kinds.values()), len(rows)))
    rec('    ### NO RULING IS PROPOSED. ### NO ITEM IS ANSWERED. ### EACH UNBLOCK LINE DESCRIBES WHAT WAITS.')
    largest = max(real_kinds, key=lambda x: len(kinds[x]))
    dump(KINDJ, dict(items=rows, kinds=dict((k, [r['n'] for r in v]) for k, v in kinds.items()), counts=dict((k, len(v)) for k, v in kinds.items()),
                     real_kinds=real_kinds, largest=largest, by_form=by_form, unblock=UNBLOCK))

    # ---------------------------------------------------------------------------------------- FILING
    rec('')
    rec('  ### ### **THE FILING.**')
    lr = read(LORERUN) if os.path.exists(LORERUN) else ''
    rec('    PREDICATE_ONE_SHAPE.md : the b451 line present %d ; %s' % (read(LORE).count('Incidents after the mint (b451)'),
                                                                     'PRIOR BYTES A TRUE PREFIX : YES' if 'TRUE PREFIX : YES' in lr else '### PREFIX NOT PROVED'))
    rec('    W-ORD-MATCHER-SHAPE : filed with the trail record; trigger: the next act that matches a table header, a document name or a')
    rec('    version by pattern. ### NO MATCHER IS EDITED.')

    # ---------------------------------------------------------------------------------------- EXPECTATIONS
    rec('')
    rec('  ### ### **THE EXPECTATIONS.**')
    n1i = 'HELD' if len(remainder) == 1 else 'REFUTED'
    n1ii = 'REFUTED AS WORDED' if (remainder == ['ENUMERA'] and need and need[0].get('clone') is False) else ('HELD' if remainder else 'REFUTED')
    n2a = 'HELD' if len(real_kinds) < 10 else 'REFUTED'
    n2b = 'HELD' if (largest == 'AUTHORING' and all(len(kinds[k]) < len(kinds['AUTHORING']) for k in real_kinds if k != 'AUTHORING')) else 'REFUTED'
    rec('    (N1)(i)  the remainder is exactly one keystone                      ### %s -- %d: %s' % (n1i, len(remainder), remainder))
    rec('    (N1)(ii) it is the one b395 left unreadable without a clone         ### %s -- it is b395`s unreadable one, and b395 says no clone would help' % n1ii)
    rec('    (N2)(a)  fewer than ten kinds                                       ### %s -- %d with members' % (n2a, len(real_kinds)))
    rec('    (N2)(b)  authoring is the largest kind                              ### %s -- %s' % (n2b, dict((k, len(kinds[k])) for k in kinds)))
    seat = dict(n1i='HELD', n1ii='REFUTED AS WORDED', n2a='HELD', n2b='HELD')
    got = dict(n1i=n1i, n1ii=n1ii, n2a=n2a, n2b=n2b)
    rec('    ### the seat`s own from the face, declared as seen: %s' % '; '.join('%s %s -- %s' % (k, seat[k], 'HELD' if seat[k] == got[k] else 'REFUTED') for k in seat))
    rec('')
    rec('    ### NO KEYSTONE OPENED OR EDITED. ### NO MATCHER EDITED. ### NO GRADE MOVED. ### NO CLAIM ABOUT RH, h2 OR ANY ZERO. ### THE FOUR LISTS ARE OPEN.')
    rec('=' * 110)
    K = json.load(io.open(KINDJ, encoding='utf-8'))
    K['expect'] = got
    K['seat'] = seat
    dump(KINDJ, K)
    io.open(OUT, 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    return 0


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'report'
    sys.exit(dict(lore=lore, report=report)[mode]())
