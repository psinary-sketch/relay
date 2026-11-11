"""b753 -- the waiver's bank, composed from the results of the inventory's scripts (tools/b753_waiver_inv0.py to _inv9.py), which ran
before their commit, in the session's scratch directory, on 2026-11-11 from 18:33Z to 18:58Z. This composer runs none of them: it reads
the result files they left (argv 1, their directory) and prints counts, bank lines, the ledgers' line numbers, shares, origin paths and
classes. It prints no word of any row.

  python -X utf8 -u tools/b753_waiver.py <directory of the result files>
"""
import io, os, sys, pickle, hashlib, collections, time

REL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(REL, 'data', 'b753_waiver.txt')

COUNTS = """## THE COUNT TABLE, as printed to the author on 2026-11-11 before the waiver (the first inventory, scripts inv0 to inv5)
  rows citing a line of a PLACE-papers ledger and carrying 24 or more consecutive characters of it, a row the same path held at origin set apart:
    bank                                   rows   earliest commit past origin
    data/b753_citation_check.txt             31   9fc39fef
    data/b753_citation_check.json            18   9fc39fef
    data/b753_put_1.json                      1   9fc39fef
    data/b753_stepzero.txt                   11   9fc39fef
    data/b753_carry_acts.txt                  6   9fc39fef
    tools/acts/b753.py                        7   9fc39fef
    data/b753_ferry.txt                       5   9fc39fef
    data/b753_author_words_preseal.txt        1   46123070
    data/b753_branch_map.txt                  1   c275582f
    tools/b753_branch_map.py                  1   c275582f
    THE ROWS OUTSIDE THE ANCHORS BANK: 82
    data/b753_head_read.txt                   3   8db618bf   (:64, :65, :66; the description also the one text row of data/b753_head_read.json)
    data/b753_anchors.txt                   268   2544839e   (of its 414 lines: 152 sentence or tag rows, 76 slug rows, 13 later lines,
                                                              16 ceiling phrases, 2 lines of the layer's rule, 9 further lines)
  named beside the table: the needles of tools/acts/b753.py :861 and of tools/b753_anchors.py; the slugs in data/b753_defects.txt row (c')
    and in the subject of commit 2544839e; two rows of data/b753_rowgen_stepzero.txt (:15, :19).
  the looser pass (seven consecutive words shared with a private repository's tracked text): every source was PLACE-papers; 555 rows stood
    already at their own path at origin; 608 rows share their words with origin's tree; 199 were left for reading (86 and 113).
  the earliest commit past origin holding such words: 9fc39fef, the third of 32.
  of the other seven private repositories the banks carry names, sizes, dates and hashes."""

def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()[:16]

def main(sp):
    R = pickle.load(open(os.path.join(sp, 'inv6_753.pkl'), 'rb'))
    rf, hit = None, collections.defaultdict(dict)
    for k in range(3):
        a, h = pickle.load(open(os.path.join(sp, 'inv8_753_%d.pkl' % k), 'rb'))
        rf = a
        for i, d in h.items():
            for f, v in d.items():
                hit[i].setdefault(f, v)
    for i, r in enumerate(R):
        r['figs'], r['fhit'] = rf[i], hit.get(i, {})

    def wv(r):
        if not r['nsh']:
            return 'SHORT'
        if r['bestcov'] >= 0.9:
            return 'SAME'
        if r['cov'] >= 0.9:
            return 'SAME*'
        if r['cov'] >= 0.5:
            return 'MOST'
        return 'PART' if r['cov'] > 0 else 'ABSENT'

    def fv(r):
        return 'no figure' if not r['figs'] else '%d of %d' % (len(r['fhit']), len(r['figs']))

    def loc(r):
        return '%s:%d' % r['best'] if r['best'] else '-'

    def floc(r):
        ks = sorted(r['fhit'], key=lambda f: (f[0] != 'X', -len(f)))
        return '%s:%d' % r['fhit'][ks[0]] if ks else '-'

    def cls(r):
        w = wv(r)
        if w in ('SAME', 'SAME*'):
            return 'A'
        if r['figs'] and len(r['fhit']) == len(r['figs']):
            return 'B'
        if r['fhit']:
            return 'C'
        if r['figs']:
            return 'D'
        return 'E'

    L = []
    w = L.append
    w('b753 -- THE WAIVER`S BANK: THE INVENTORY`S COUNT TABLE AND ITS PER-ROW COLUMN, NO WORD OF ANY ROW (the author`s eighth word (1), 2026-11-11)')
    w('')
    w('### The author`s waiver (relay data/b753_author_words_preseal.txt, the eighth word; data/b753_events.txt) reaches PLACE-papers and no other')
    w('### private repository. This bank carries what the inventory counted: bank lines, the ledgers` line numbers, shares, origin paths and classes.')
    w('### THE SCRIPTS RAN BEFORE THEIR COMMIT: tools/b753_waiver_inv0.py to _inv9.py are byte copies of the scripts as they stood in the session`s')
    w('### scratch directory when they ran (2026-11-11, 18:33Z to 18:58Z); they name that directory`s files and are not re-run here. This bank is')
    w('### composed from their result files by tools/b753_waiver.py, at %s. The figure arm ran twice: its first matcher (inv6) missed' % time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()))
    w('### the formula of FINDINGS :825 on the control, was widened (inv8) and run again over the same tree; the words arm ran once (inv6).')
    w('')
    w('## THE SCRIPTS AND THEIR RESULT FILES (sha256, opening sixteen)')
    for i in range(10):
        p = os.path.join(REL, 'tools', 'b753_waiver_inv%d.py' % i)
        q = os.path.join(sp, 'inv%d_753.py' % i)
        w('  tools/b753_waiver_inv%d.py  %s  equal to the scratch script: %s' % (i, sha(p), open(p, 'rb').read() == open(q, 'rb').read()))
    for n in ('inv1_753.pkl', 'inv2_753.pkl', 'inv6_753.pkl', 'inv8_753_0.pkl', 'inv8_753_1.pkl', 'inv8_753_2.pkl'):
        w('  result file %s  %s  (in the scratch directory, not committed)' % (n, sha(os.path.join(sp, n))))
    w('')
    w(COUNTS)
    w('')
    w('## THE COLUMN: HOW IT WAS READ')
    w('  one pass over every blob of origin/main`s tree (0e855242): 37,429 blobs, 575,572,841 bytes; 35,998 text blobs read, 47 binary set apart.')
    w('  WORDS: the share of a row`s five-word runs found in that tree. SAME: one origin line holds nine tenths or more of them; SAME*: nine tenths')
    w('    over several lines; MOST: half or more; PART: fewer; ABSENT: no run found; SHORT: under three words, not tested. The path is the origin line')
    w('    holding the most runs.')
    w('  FIGURES: decimals, fractions, percentages and formula runs, compared after emphasis marks are removed; bare integers not compared. The')
    w('    extractor sometimes takes a neighbouring word into a formula, so "k of n" can understate; a bare number`s hit can be chance.')
    w('  CLASS: A the words stand ; B every figure stands, the words differ ; C some figures stand ; D a figure, not one found ; E no figure, the')
    w('    words not SAME. A hit says the words are in the pushed tree; it does not say who wrote them first.')
    w('  THE CONTROL, the navigator`s two anchors: FINDINGS :821 SAME at data/b428_extract.txt:266, figures 2 of 2 ; FINDINGS :825 PART, the')
    w('    formula`s right side at data/b148_figure_values_dossier.md:113, 1 of 2 (its left side as the anchor words it not found).')
    w('')
    by = collections.OrderedDict()
    for r in R:
        if r['bank'] == 'anchors' and r['anchor'] and r['kind'] == 'sentence/tag':
            by.setdefault(r['anchor'], []).append(r)
    w('## THE ANCHORS BANK, BY ANCHOR (data/b753_anchors.txt): the sentence row and the tag row')
    w('  bank line | FINDINGS line | words, share | origin line | figures | a figure at | class || tag row: bank line, words, share')
    c = collections.Counter()
    for a, rs in by.items():
        s = rs[0]
        c[cls(s)] += 1
        t = rs[1] if len(rs) > 1 else None
        w('  :%d | %s | %s %d%% | %s | %s | %s | %s || %s' % (s['n'], s['src'].replace('FINDINGS ', ''), wv(s), round(100 * (s['cov'] or 0)), loc(s), fv(s), floc(s), cls(s),
                                                        (':%d %s %d%%' % (t['n'], wv(t), round(100 * (t['cov'] or 0)))) if t else '-'))
    w('  ANCHORS %d ; BY CLASS OF THE SENTENCE ROW: %s' % (len(by), ' ; '.join('%s %d' % kv for kv in sorted(c.items()))))
    ct = collections.Counter(wv(rs[1]) for rs in by.values() if len(rs) > 1)
    w('  TAG ROWS %d: %s' % (sum(ct.values()), ' ; '.join('%s %d' % kv for kv in sorted(ct.items()))))
    cs = collections.Counter(wv(r) for r in R if r['kind'] == 'slug')
    w('  SLUG ROWS %d (the slug`s words as a run): %s' % (sum(cs.values()), ' ; '.join('%s %d' % kv for kv in sorted(cs.items()))))
    w('')
    w('## THE ANCHORS BANK, ITS OTHER QUOTING LINES')
    w('  bank line | kind | source | words, share | origin line | figures | a figure at')
    n_other = 0
    for r in R:
        if r['bank'] == 'anchors' and r['kind'] in ('later line', 'layer rule', 'ceiling phrase', 'other'):
            n_other += 1
            w('  :%d | %s | %s | %s %d%% | %s | %s | %s' % (r['n'], r['kind'], r['src'], wv(r), round(100 * (r['cov'] or 0)), loc(r), fv(r), floc(r)))
    na = sum(1 for r in R if r['bank'] == 'anchors')
    w('  THE COLUMN`S ROWS OF THIS BANK: %d (sentence or tag %d, slug %d, other lines %d); the count table`s 268 took 9 further lines where this' % (na, sum(len(v) for v in by.values()), sum(cs.values()), n_other))
    w('  parse takes 6 (a line counted there for a quoted run of twelve characters, here for a phrase of the rule, a control or the list).')
    w('')
    w('## THE ROWS OUTSIDE THE ANCHORS BANK')
    w('  bank : line | source | words, share | origin line | figures | a figure at')
    co = collections.Counter()
    for r in R:
        if r['bank'] != 'anchors':
            co[wv(r) if r['bank'] != 'head_read' else 'head read'] += 1
            w('  %s :%d | %s | %s %d%% | %s | %s | %s' % (r['bank'], r['n'], r['src'], wv(r), round(100 * (r['cov'] or 0)), loc(r), fv(r), floc(r)))
    w('  ROWS %d: %s' % (sum(co.values()), ' ; '.join('%s %d' % kv for kv in sorted(co.items()))))
    w('')
    w('### ### **THE WAIVER`S BANK: ANCHORS %d (A %d, B %d, C %d, D %d, E %d) ; ROWS OUTSIDE THE ANCHORS BANK %d AND THE HEAD READ`S 3 ; NO WORD OF ANY ROW PRINTED.**' % (
        len(by), c['A'], c['B'], c['C'], c['D'], c['E'], sum(co.values()) - co['head read']))
    text = '\n'.join(L) + '\n'
    tmp = OUT + '.tmp'
    with io.open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        f.write(text)
    os.replace(tmp, OUT)
    print('written', OUT, len(L), 'lines')
    print(L[-1])

if __name__ == '__main__':
    main(sys.argv[1])
