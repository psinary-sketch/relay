# -*- coding: utf-8 -*-
"""b472_components.py -- COMPONENTS 0, 1 AND 2. ### Run after the seal (sha256 `5bd69717c130a358...`,
### locked 2026-09-22T17:25:15Z). ### **THE BUILD LOG IS NOT OPENED.** ### Every cell is read by the
### survey's own readers, imported from b472_extract.py; every sentence is built from the three cells and
### the shape clause under the face's reading (4); every placement cites its bank's line under reading (7).
"""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b472_extract as X  # noqa: E402  ### the readers are IMPORTED, not copied

D = os.path.join(ROOT, 'data')
PP = X.PP
NL = chr(10)
L = []
SITES = X.SITES

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def rec(s=''):
    L.append(s)
    print(s)


S = json.loads(io.open(os.path.join(D, 'b472_survey.json'), encoding='utf-8').read())
ST = json.loads(io.open(os.path.join(D, 'b472_run_state.json'), encoding='utf-8').read())

# ### ### **THE SIX SENTENCES.** ### Each is built from: the INDEX and its heading (b467, OPEN_TRAILS.md
# ### :7558-7563 and :7569), the KIND cell, the WITNESS cell (quoted fragments marked by '...'), and the
# ### shape clause (FACES_LEDGER.md:31). A class or support appears only where a cell states it.
SENT = {
    'i': ("At site (i) -- index: the class, a condition on the test function -- a proof would have to supply, "
          "in place of a family indexed by the class, one statement uniform in the class that owns the "
          "quantifiers which 'run over the class and, through the explicit formula, over the zeros' ('a `∀` "
          "with no `∃` inside it'); over what class and at what support is UNSTATED IN THE CELLS, and the "
          "witness is UNSTATED: the cell says the witness form 'does not transpose here at all', and this "
          "sentence does not fill it."),
    'ii': ("At site (ii) -- index: the height, the instrument's truncation -- a proof would have to supply one "
           "statement uniform in the height, 'ONE argument serving every height', in place of 'a method that "
           "produces zeros one at a time'; the class and the support are UNSTATED IN THE CELLS, and the witness "
           "is NONE KNOWN."),
    'iii': ("At site (iii) -- index: the width, a condition on the test function -- a proof would have to "
            "supply one statement uniform in the width, 'ONE `g` serving every width', over the class the cell "
            "quotes, 'g in Cc^infty(R) with support in [-A/2, A/2] such that f = g * g^*', at every support "
            "[-A/2, A/2] -- 'h1, one g works at every A; h2, the f it builds is not the degenerate one'; the "
            "witness is NONE KNOWN: 'No such g is named.'"),
    'iv': ("At site (iv) -- index: the width, a condition on the test function -- a proof would have to supply "
           "'one statement uniform in `a`', a uniform bound in place of the 'TEN VALUES indexed by the width'; "
           "the class, and the support beyond 'the width', are UNSTATED IN THE CELLS, and the witness is "
           "UNSTATED: 'a uniform bound is not an object in the family's parameter space'."),
    'v': ("At site (v) -- index: the representation, a datum of the representation -- a proof would have to "
          "supply 'ONE CONSTANT SERVING EVERY REPRESENTATION', the implied constant brought out of the inner "
          "existential of a '`∀∃ ⟹ ∃∀`', at KIND (b), which the cell transcribes from the "
          "entry; the class of representations and the support are UNSTATED IN THE CELLS, and the witness is "
          "NONE KNOWN: 'Theorem 5.1's absolute constant is a witness for the ARCHIMEDEAN side and not for this "
          "one'."),
    'vi': ("At site (vi) -- index: the modulus, a datum of the representation -- a proof would have to supply "
           "one statement across every finite modulus, from `h1` 'consistent at every finite modulus' to `h2` "
           "'(positive global density)'; the class and the support are UNSTATED IN THE CELLS, and the witness "
           "is NONE KNOWN: 'It names no object satisfying them'."),
}

# ### ### **COMPONENT 2's PLACEMENTS, UNDER READING (7).** ### Every cell cites its bank's lines; the
# ### level is read against the sentence above. `NOT PLACED` where the bank neither reads the site nor is
# ### named by the site's entry.
AF = {
    'i': ('NOT AT ALL', 'b468r_components.txt:85-87', '"NONE" -- "no statement uniform in the test function"'),
    'ii': ('IN PART', 'b468r_components.txt:88-91',
           '"UNIFORM IN T -- DOES NOT FIRE": uniform in the height from "T >= T0(eps)" on, and "a PROPORTION (2/3 '
           'of zeros), not a statement about each zero"; (R76) at OPEN_TRAILS.md:7634: the truncation is the '
           'corpus`s and no source fires it'),
    'iii': ('NOT AT ALL', 'b468r_components.txt:92-93', '"NONE" -- "no statement uniform in the test function`s support at fixed width"'),
    'iv': ('NOT AT ALL', 'b468r_components.txt:94-95', '"NONE" -- "the same index, the same absence"'),
    'v': ('NOT AT ALL', 'b468r_components.txt:96-99',
          '"K1 CLASS BOUNDARY" (the failure-kind key, OPEN_TRAILS.md:6439) -- "the second object is outside the '
          'class"; and per representation, "T0 is chosen after chi" (:101-103); (R78) at OPEN_TRAILS.md:7791: '
          'this boundary is structural and is not counted as an obstruction instance'),
    'vi': ('NOT AT ALL', 'b468r_components.txt:100-103',
           '"K1 CLASS BOUNDARY, AND PER-MODULUS" -- "it holds at every modulus and not uniformly across moduli", '
           'which is the family the site holds, not the statement across'),
}
ZT = {
    'iv': ('IN PART', 'b470_components.txt:70-72, :109, :117-118',
           'uniform in the width: EF_lit is stated for every k with ContDiff R 2 k and HasCompactSupport k '
           '(:109), and "the corpus`s w meets EF_lit`s hypotheses" (:70-72); but an IDENTITY carrying the full '
           'zero multiset, of which "THE IDENTITY b321 COMPUTES IS AN INSTANCE" (:118) -- not a uniform bound '
           'on the prime constituent'),
}


def main():
    rec('=' * 104)
    rec('COMPONENT 0 -- THE RUN`S STATE, NOT ITS LOG.')
    rec('=' * 104)
    rec('    pid              : %d' % ST['pid'])
    rec('    ### ### **STATE  : %s**   (read %s, process table: %s)' % (ST['state'], ST['read_utc'], ST['tasklist_row']))
    rec('    ### ### **LOG BYTES : %d**   (file-system size; last write %s)' % (ST['log_bytes'], ST['log_last_write_utc']))
    rec('    launched         : %s' % ST['launched_utc'])
    if ST['state'] == 'EXITED':
        rec('    ### ### **ELAPSED : %d s, launch to the log`s last write** (%d min %d s)'
            % (ST['elapsed_to_last_write_s'], ST['elapsed_to_last_write_s'] // 60, ST['elapsed_to_last_write_s'] % 60))
    rec('    lean / lake processes alive : %d / %d' % (ST['lean_processes'], ST['lake_processes']))
    rec('    how              : %s ; clock: %s' % (ST['how'], ST['clock']))
    rec('    ### ### **THE LOG STAYS UNREAD UNTIL THE ACT THAT READS IT.** ### The reader is the seat`s scratchpad')
    rec('    ### script b472_state.py; its whole text is quoted below so the reading can be checked.')
    try:
        src = io.open(os.path.join(os.environ.get('B472_SCRATCH', ''), 'b472_state.py'), encoding='utf-8').read()
    except Exception:
        src = ''
    for ln in src.split(NL):
        rec('      | %s' % ln)

    rec('')
    rec('=' * 104)
    rec('COMPONENT 1 -- THE SIX STATEMENTS.')
    rec('=' * 104)
    row = X.lines(os.path.join(PP, 'FACES_LEDGER.md'))[30]
    ents = X.entries(row)
    fd = X.lines(os.path.join(PP, 'FINDINGS.md'))
    e0 = S['e0']
    order = S['order']
    # ### the E0 mapping, recomputed from the live files with the survey's own functions, and its controls
    def mapping(text):
        t = X.norm(text)
        res = []
        for k in sorted(e0):
            n, run = X.lcs(t, X.norm(e0[k]['name'] + ' ' + e0[k]['kinds'] + ' ' + e0[k]['grades']))
            res.append((n, k, run))
        return sorted(res, reverse=True)
    pos = mapping(e0['K4']['name'] + ' ' + e0['K4']['kinds'])
    neg = mapping(X.read(os.path.join(D, 'b472_refusal.txt')))
    pos_ok = pos[0][1] == 'K4' and pos[0][0] >= 6
    neg_ok = neg[0][0] < 6
    rec('  THE MAPPING`S CONTROLS : positive (K4`s own text) -> %s at %d words : %s ; negative (the refusal record)'
        ' -> longest %d words : %s' % (pos[0][1], pos[0][0], 'PASS' if pos_ok else 'FAIL', neg[0][0],
                                       'PASS' if neg_ok else 'FAIL'))
    table = []
    for s in SITES:
        c = X.cell_reader(row, s)
        ix = S['index'][s]
        m = mapping(ents[s]['text'] + ' ' + c['cell'])
        rows = [k for n, k, run in m if n >= 6]
        rec('')
        rec('  ### (%s) %s' % (s, ents[s]['title']))
        rec('    INDEX   : %s -- %s   (OPEN_TRAILS.md:%d ; heading :7569)' % (ix['index'], S['heading'][s], ix['line']))
        rec('    KIND    : %s   (FACES_LEDGER.md:31, cell at char %d)' % (c['kind'], c['at']))
        rec('    WITNESS : %s' % c['witness'])
        rec('    cell    : %s' % c['cell'])
        rec('    ### ### **SENTENCE (%s):** %s' % (s, SENT[s]))
        if s == 'v':
            rec('    beside it, (R78) at OPEN_TRAILS.md:7791 : the class boundary such theorems show at site (v) "is')
            rec('      structural and is not counted as an obstruction instance".')
        if rows:
            best = []
            for k in rows:
                g = [x.strip() for x in e0[k]['grades'].split('|')]
                grades = [x.strip() for x in (g[0] + ';' + g[1] + ';' + g[2]).split(';') if x.strip() and x.strip() != '—']
                names = [x.split(' (')[0] for x in grades]
                top = max(order.index(n) for n in names if n in order)
                hard = [x for x in grades if x.split(' (')[0] == order[top]]
                best.append((k, hard, g[3] if len(g) > 3 else ''))
                rec('    ### ### **E0 (E0 key) : %s %s -- FINDINGS.md:%d (kinds), :%d (grades)**'
                    % (k, e0[k]['name'], e0[k]['kline'], e0[k]['gline']))
                rec('      the shared run : "%s" (%d words)' % ([r for n, kk, r in m if kk == k][0], [n for n, kk, r in m if kk == k][0]))
                rec('      the hardest grade, ties together : %s' % ' ; '.join(hard))
                rec('      the owners` own words : %s' % (g[3] if len(g) > 3 else ''))
                rec('      the kinds row : %s' % e0[k]['kinds'].strip())
            table.append(dict(site=s, title=ents[s]['title'], index=ix['index'], heading=S['heading'][s],
                              kind=c['kind'], witness=c['witness'], sentence=SENT[s],
                              e0=[dict(k=k, name=e0[k]['name'], grades=h, words=w) for k, h, w in best]))
        else:
            rec('    ### ### **E0 : NO E0 ROW** -- longest shared run %d words (%s)' % (m[0][0], m[0][1]))
            table.append(dict(site=s, title=ents[s]['title'], index=ix['index'], heading=S['heading'][s],
                              kind=c['kind'], witness=c['witness'], sentence=SENT[s], e0=[]))
    with_row = [t['site'] for t in table if t['e0']]
    rec('')
    rec('  ### ### **SITES WITH AN E0 ROW : %d (%s) ; NO E0 ROW : %d.**' % (len(with_row), ', '.join(with_row),
                                                                       6 - len(with_row)))

    rec('')
    rec('=' * 104)
    rec('COMPONENT 2 -- THE TWO EXTERNAL RESULTS IN THE SAME TABLE. ### NO NEW VERDICT.')
    rec('=' * 104)
    rec('  ### TWO NUMBERINGS SHARE THE LETTER K: E0`s constituents (FINDINGS.md:3045) and the failure-kind key')
    rec('  ### (OPEN_TRAILS.md:6439). b468r`s "K1 CLASS BOUNDARY" is the failure-kind key`s K1.')
    place = dict(af={}, zeta23={})
    rec('')
    rec('  the Alpoge-Furman theorem (arXiv 2608.13637v2), b468r`s read (b):')
    for s in SITES:
        lv, at, why = AF[s]
        v = S['af'][s]['verdict']
        rec('    (%-3s) ### **%-10s** %s -- bank verdict "%s" ; %s' % (s, lv, at, v, why))
        place['af'][s] = dict(level=lv, at=at, bank_verdict=v, why=why)
    rec('')
    rec('  zeta23`s EF_lit_zetaZeroConfig, b470`s bank (verdict at b470_components.txt:%d: %s):'
        % (S['z']['verdict_line'], S['z']['verdict'].replace('### ', '').strip()))
    for s in SITES:
        if s in ZT:
            lv, at, why = ZT[s]
            rec('    (%-3s) ### **%-10s** %s -- %s' % (s, lv, at, why))
            rec('          placed by reading (7)(b): site (iv)`s own entry names b321 (%s)' % S['iv_names_b321'])
            place['zeta23'][s] = dict(level=lv, at=at, why=why)
        else:
            rec('    (%-3s) ### **NOT PLACED** -- b470`s components bank reads no site of row U1 (%d lines name one), and'
                % (s, S['b470_site_lines']))
            rec('          site (%s)`s entry names no act whose object b470`s verdict is about' % s)
            place['zeta23'][s] = dict(level='NOT PLACED', at='b470_components.txt (0 lines naming a site)', why='')
    cnt = {}
    for r in ('af', 'zeta23'):
        cnt[r] = {lv: sum(1 for s in SITES if place[r][s]['level'] == lv)
                  for lv in ('IN WHOLE', 'IN PART', 'NOT AT ALL', 'NOT PLACED')}
        rec('  ### ### **%s : IN WHOLE %d ; IN PART %d ; NOT AT ALL %d ; NOT PLACED %d.**'
            % ('ALPOGE-FURMAN' if r == 'af' else 'zeta23 EF_lit_zetaZeroConfig', cnt[r]['IN WHOLE'], cnt[r]['IN PART'],
               cnt[r]['NOT AT ALL'], cnt[r]['NOT PLACED']))
    rec('  ### **ROUTED, NOT PLACED:** no bank reads EF_lit against site (i), whose cell names quantifiers "over the')
    rec('  ### class and, through the explicit formula, over the zeros". Whether it bears there is for an act that')
    rec('  ### reads it; this act gives no verdict.')
    rec('  ### ### **NO BRIDGE IS TYPED FROM EITHER RESULT TO ANY SITE, OR BETWEEN SITES. ROW U1 IS NOT WRITTEN.**')

    out = dict(state=ST, table=table, placements=place, counts=cnt, with_e0_row=with_row,
               controls=dict(pos=[pos[0][1], pos[0][0]], neg=neg[0][0], pos_ok=pos_ok, neg_ok=neg_ok))
    io.open(os.path.join(D, 'b472_components.txt'), 'w', encoding='utf-8', newline=NL).write(NL.join(L) + NL)
    io.open(os.path.join(D, 'b472_table.json'), 'w', encoding='utf-8', newline=NL).write(
        json.dumps(out, indent=1, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
