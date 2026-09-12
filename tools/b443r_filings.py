# -*- coding: utf-8 -*-
"""b443r_filings.py -- SITE (vi)'S EXHAUSTED LIST, ONE BLOCK THROUGH THE WRITER'S `append_block`.
### ### Every first-failing quotation verified by the writer's `verify_quotes` first; a miss and nothing is filed.
### ### The U1 draft and the routed (v) block are NOT appended -- they live in `data/b443r_u1_draft.md`."""
import io
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import b327_faces_row as W  # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
RUN = os.path.join(D, 'b443r_filings_run.txt')
NL = chr(10)
SRC = {'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md': os.path.join(PP, 'phase2', 'method', 'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md'),
       'b431_components.txt': os.path.join(D, 'b431_components.txt'),
       'FACES_LEDGER.md': os.path.join(PP, 'FACES_LEDGER.md'),
       'b358_source_lagarias0404394.txt': os.path.join(D, 'b358_source_lagarias0404394.txt'),
       'b328_source_text.txt': os.path.join(D, 'b328_source_text.txt')}
WHERE = {'ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md': 'PLACE-papers `phase2/method/ADDITIVE_MULTIPLICATIVE_CONSPIRACY.md`',
         'FACES_LEDGER.md': 'PLACE-papers `FACES_LEDGER.md`'}

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s)


def esc(s):
    return s.replace('|', chr(92) + '|')


def main():
    sv = json.load(io.open(os.path.join(D, 'b443r_site_vi.json'), encoding='utf-8'))
    q = [(SRC[fn], ndl, False) for r in sv['candidates'] for fn, ndl in r['quotes'][:1]]
    miss = W.verify_quotes(q)
    rec('  block site (vi) : quotations %d, misses %d %s' % (len(q), len(miss), miss or ''))
    if miss or any(r['kind'] == 'HELD' for r in sv['candidates']):
        rec('  block site (vi) : NOT FILED')
        io.open(RUN, 'w', encoding='utf-8', newline=NL).write(NL.join(LINES) + NL)
        return 1
    kinds = {}
    for r in sv['candidates']:
        kinds[r['kind']] = kinds.get(r['kind'], 0) + 1
    labels = dict(b424='(i)', b427='(ii)', b428='(iii)', b436='(iv)', b442='(v)', b443='(vi)')
    percb = '; '.join('%s %d of %d' % (labels[a], t.get('CLASS BOUNDARY', 0), sum(t.values()))
                      for a, t in sv['tallies'].items())
    body = ['<!-- b443 update: site (vi) -->', '',
            '## UPDATE — filed 2026-09-12 (b443): row U1, entry (vi) — the witness column’s exhausted list, and the arc’s last site',
            '',
            '*Rows above are never rewritten; an update names the row it bears on. Written through the writer’s `append_block`. Row U1’s line, entry (vi)’s `KIND: NOT EMPTY` and `WITNESS: NONE KNOWN`, and the freeze at six (b409) stand as they read; no seventh site is entered.*',
            '',
            '| candidate | first failing step | the quoted step, and the reason |', '|:--|:--|:--|']
    for r in sv['candidates']:
        fn, ndl = r['quotes'][0]
        where = WHERE.get(fn, 'relay `data/%s`' % fn)
        body.append('| **%s** %s | %s — %s | *"%s"* (%s); %s |'
                    % (r['id'], esc(r['name']), r['step'], r['kind'], esc(ndl), where, esc(r['why'])))
    body += ['',
             '*%d candidates, read at their sources and attempted by b424’s three steps. **No witness held.** First failing steps: %s. The site’s own cell was quoted first and stands. The keystone’s line 231, which credits a 1919 sieve result with lower bounds for twin primes, is filed in relay as a sentence owing a source read — no verified source holds a sieve text — and the keystone is not edited.*'
             % (len(sv['candidates']), '; '.join('%s %d' % kv for kv in sorted(kinds.items(), key=lambda x: (-x[1], x[0])))),
             '',
             '*__The arc, at its sixth and last site, counted from banked JSON.__ %d candidates across six sites; no witness held at any. The union of failure kinds was %d after five sites and is %d after six — **the sixth site added no new way to fail.** The class boundary is the largest kind (%d of %d) but not the majority at every site: %s. Row U1’s restatement in the conspiracy keystone’s residue form is drafted and routed (relay `data/b443r_u1_draft.md`) and not applied. No grade is conferred, no bridge typed, nothing claimed about `h2`. **W-ORD-WITNESS-ENUMERATION is checkpointed after (vi).** Filed by b443 (relay `data/b443r_site_vi.json`).*'
             % (sv['total'], sv['union5'], sv['union6'], sv['aggregate'].get('CLASS BOUNDARY', 0), sv['total'], percb)]
    st, msg = W.append_block('<!-- b443 update: site (vi) -->', body)
    rec('  block site (vi) append_block : %s -- %s' % (st, msg))
    io.open(RUN, 'w', encoding='utf-8', newline=NL).write(NL.join(LINES) + NL)
    return 0


if __name__ == '__main__':
    sys.exit(main())
