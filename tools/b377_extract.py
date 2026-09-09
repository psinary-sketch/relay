# -*- coding: utf-8 -*-
"""b377_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE.**

### ### **NO LINE NUMBER IN THIS FILE IS TYPED.** ### Each read names a file and a HINT; the anchor
### tool locates the hint in the file and returns the line it actually found. ### **A HINT THAT MATCHES
### ### NOTHING, OR MATCHES TWICE, IS REFUSED** -- and the refusal is the tool working.
### ### **THE ORDER, ITS AMENDMENT, THE AUTHOR'S ROLE CLAUSE, THE TAXONOMY'S OBLIGATION, `b376`'S FIVE
### ### OPTIONS AND ALL EIGHT DOCUMENTS ARE PULLED VERBATIM BEFORE ANY PREDICATE IS WRITTEN.**
"""
import io
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import run_clock                # noqa: E402
import b303_pins                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
TC = os.path.join('D:', os.sep, 'MY-DOwnloads', 'TECHNE-Core')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def d(n):
    return os.path.join(D, n)


def p(*a):
    return os.path.join(PP, *a)


FERRY = d('b377_ferry_2026-09-08.txt')
B376BANK = d('b376_the_two_axis_read.txt')
B375BANK = d('b375_the_keystone_and_cluster_census.txt')
TAX = p('phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
CENSUS = p('phase2', 'method', 'THE_KEYSTONE_CENSUS.md')
PRED = os.path.join(TC, 'modules', '2026-09', 'PREDICATE_ONE_SHAPE.md')

# ### **THE SIX AND THE TWO, NAMED FROM `b376`'S BANKED JSON AND NEVER TYPED AS A LIST HERE.**
_AX = json.load(io.open(d('b376_axes.json'), encoding='utf-8'))
_P375 = json.load(io.open(d('b375_population.json'), encoding='utf-8'))
_SC = {x['file']: x for x in _AX['scored']}
CERT = _P375['tests']['taxonomy_tier_k']
SIX = [f for f in CERT if _SC[f]['axis_b'] == 'B-']
TWO = [f for f in CERT if _SC[f]['axis_b'] == 'B?']

DECL_HINT = ('**DOCUMENT CLASS — THE STANDING TAXONOMY (K/C/N/E, author-ruled 2026-07-28): '
             '### TIER K**')

READS = [
    # ---- THE ORDER ---------------------------------------------------------------------------------
    ('the order -- the act', 'ORDER', FERRY,
     'ACT b377 - THE UNBLOCKED OBLIGATION, AND THE RULING\'S EVIDENCE'),
    ('the order -- the scope', 'ORDER', FERRY,
     'repair-or-route under an obligation the taxonomy already'),
    ('the order -- nothing ruled, nothing moved', 'ORDER', FERRY,
     'class ruled, NO document reclassified, NO declaration moved,'),
    ('the order -- component 1, the role clause first half', 'ORDER', FERRY,
     'evidence and not as a ruling: "Keystones are for clarifying'),
    ('the order -- component 1, the role clause second half', 'ORDER', FERRY,
     'vision in explanatory clarity just because we have been'),
    ('the order -- component 1, the role axis not the apparatus axis', 'ORDER', FERRY,
     'they speak to the role'),
    ('the order -- component 2, the five options quoted whole', 'ORDER', FERRY,
     "COMPONENT 2 - THE FIVE OPTIONS, QUOTED WHOLE: b376's Component"),
    ('the order -- component 3, the six documents', 'ORDER', FERRY,
     'COMPONENT 3 - THE SIX DOCUMENTS, which do not wait on the'),
    ('the order -- component 3, the branch fixed here', 'ORDER', FERRY,
     'decide by a branch fixed here: if the'),
    ('the order -- component 3, route and repair nothing', 'ORDER', FERRY,
     'cannot be located, ROUTE it with'),
    ('the order -- component 3, a document says what it says', 'ORDER', FERRY,
     'No declaration is'),
    ('the order -- component 4, the census drift filed', 'ORDER', FERRY,
     "COMPONENT 4 - TWO FILINGS: (i) the prior census document's own"),
    ('the order -- component 4, the six clusters as a work-order', 'ORDER', FERRY,
     'six clusters with registry rows and no keystone, restated'),
    ('the order -- component 4, priced and NOT opened', 'ORDER', FERRY,
     'Filed as a work-order, priced if the record'),
    ("the order -- the navigator's expectations", 'ORDER', FERRY,
     'expectations: (F1) most of the six can be met by appending from'),
    # ---- THE AMENDMENT -----------------------------------------------------------------------------
    ('the amendment -- (A1) not determinable is not absent', 'AMEND', FERRY,
     'and LEFT - not determinable is not absent, and neither is'),
    ('the amendment -- (A1) state what would decide it', 'AMEND', FERRY,
     'for each what the read could not decide and what would decide'),
    ('the amendment -- (A2) the findings layer alone', 'AMEND', FERRY,
     'on a keystone and is not in it was taken against the findings'),
    ('the amendment -- (A2) the wider question', 'AMEND', FERRY,
     "is wider - what bears on a keystone's subject anywhere"),
    ('the amendment -- (A2) a FLOOR, not re-measured here', 'AMEND', FERRY,
     'banked figure as a FLOOR against the wider question, name the'),
    # ---- THE TAXONOMY'S OWN OBLIGATION -------------------------------------------------------------
    ("the taxonomy -- Tier K and what it obliges", 'TAX', TAX,
     '**Tier K — Keystone-certified.** A document whose load-bearing claims are backed'),
    ('the taxonomy -- Tier C, which certifies nothing', 'TAX', TAX,
     '**Tier C — Cluster-synthesis.** A document that **organizes** certified results'),
    ('the taxonomy -- the presumptive Tier K roster', 'TAX', TAX,
     '- **Tier K (presumptive):** the ~50 Gate-1-graded keystones'),
    # ---- b376's FIVE OPTIONS -----------------------------------------------------------------------
    ('b376 -- component 6 opens', 'OPTIONS', B376BANK,
     '### COMPONENT 6 -- WHAT THIS READ CANNOT DECIDE.'),
    ('b376 -- option 1, axis B alone', 'OPTIONS', B376BANK,
     '### **OPTION 1 -- ONE CLASS, RULED ON AXIS B ALONE.**'),
    ('b376 -- option 2, axis A alone', 'OPTIONS', B376BANK,
     '### **OPTION 2 -- ONE CLASS, RULED ON AXIS A ALONE.**'),
    ('b376 -- option 3, both conjoined', 'OPTIONS', B376BANK,
     '### **OPTION 3 -- ONE CLASS, RULED ON BOTH AXES CONJOINED**'),
    ('b376 -- option 4, two marks rather than one class', 'OPTIONS', B376BANK,
     '### **OPTION 4 -- TWO MARKS RATHER THAN ONE CLASS**'),
    ('b376 -- option 5, retire the word', 'OPTIONS', B376BANK,
     '### **OPTION 5 -- RULE NOTHING AND RETIRE THE WORD.**'),
    ('b376 -- none is recommended', 'OPTIONS', B376BANK,
     'NONE IS RECOMMENDED, NONE IS RANKED, AND NO ORDERING BELOW IS AN ORDERING OF'),
    # ---- THE CENSUS DRIFT --------------------------------------------------------------------------
    ('the census -- the STATED definition, three clauses', 'CENSUS', CENSUS,
     '| ### **KEYSTONE** | (i) states results for external readers'),
    ('the census -- the OPERATIONALISED line', 'CENSUS', CENSUS,
     '**OPERATIONALISED:** (i) = an `Abstract` heading or an ORCID block'),
    ('the census -- the detector returned 20', 'CENSUS', CENSUS,
     '> **The detector returned 20 for KEYSTONE.'),
    # ---- b375's TWO CARRIED FINDINGS ---------------------------------------------------------------
    ('b375 -- the clusters with no keystone', 'B375', B375BANK,
     'A CLUSTER WITH NO KEYSTONE IS A FINDING AND IS REPORTED AS ONE'),
    ('b375 -- column (d), by anchor and never summarized', 'B375', B375BANK,
     'NEVER SUMMARIZED** -- the order`s own words.'),
    # ---- THE LORE ----------------------------------------------------------------------------------
    ('the lore -- a predicate that knows one shape', 'LORE', PRED,
     '**A predicate written against the shape you have seen will report exactly that shape and '
     'will report'),
]

# ### **AND ONE READ PER DOCUMENT, ANCHORED ON ITS OWN DECLARATION** -- the line that put it in the
# ### certification-test set in the first place. ### **THE DOCUMENT IS QUOTED SAYING WHAT IT IS.**
for _f in SIX:
    READS.append(('the six -- %s declares its tier' % os.path.basename(_f)[:-3], 'SIX',
                  p(*_f.split('/')), DECL_HINT))
for _f in TWO:
    READS.append(('the two -- %s declares its tier' % os.path.basename(_f)[:-3], 'TWO',
                  p(*_f.split('/')), DECL_HINT))

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.strip()


def main():
    rec('=' * 100)
    rec('b377 -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    ok = AF.self_test() if hasattr(AF, 'self_test') else True
    rec('  ### anchor_from_file fixtures : %s' % ok)
    rec('')
    rec('-' * 100)
    rec('  ### THE REFS, PRINTED BEFORE ANY QUOTATION.')
    rec('-' * 100)
    refs = {}
    for name, repo in b303_pins.REPOS:
        br = git(repo, 'rev-parse', '--abbrev-ref', 'HEAD')
        hd = git(repo, 'rev-parse', 'HEAD')[:12]
        dirty = bool(git(repo, 'status', '--porcelain'))
        refs[name] = dict(branch=br, head=hd, dirty=dirty)
        rec('    %-22s ref `%s` = `%s`   ### tree dirty : %s' % (name, br, hd, dirty))
    rec('')
    rec('-' * 100)
    rec('  ### THE READS. ### **HINT TYPED -> ANCHOR READ FROM THE FILE -> NEEDLE PULLED.**')
    rec('-' * 100)
    out, noanchor, differing, bytag = [], 0, 0, {}
    for lbl, tag, path, hint in READS:
        rec('')
        rec('  [%-7s] %s' % (tag, lbl))
        try:
            n, line = AF.find(path, hint)
        except Exception as e:
            noanchor += 1
            rec('      ### ### **NO ANCHOR** -- %s' % str(e)[:150])
            out.append(dict(label=lbl, tag=tag, file=os.path.basename(path), line=None,
                            text=None, error=str(e)[:200]))
            continue
        diff = (line.rstrip(chr(10)) != hint)
        differing += 1 if diff else 0
        bytag[tag] = bytag.get(tag, 0) + 1
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.basename(path), n, diff))
        rec('      | %s' % line.strip()[:200])
        out.append(dict(label=lbl, tag=tag, file=os.path.basename(path),
                        rel=os.path.relpath(path, PP).replace(os.sep, '/')
                        if path.startswith(PP) else os.path.basename(path),
                        line=n, text=line.rstrip(chr(10))))
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), noanchor))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (differing, len(READS)))
    rec('  ### ### **BY TAG : %s**' % bytag)
    rec('  ### ### **THE SIX AND THE TWO ARE NAMED FROM `b376`S BANKED JSON, NOT TYPED HERE:**')
    rec('  ###   the six (declare TIER K, score `B-`) : %d' % len(SIX))
    rec('  ###   the two (declare TIER K, score `B?`) : %d' % len(TWO))
    rec('  ### **NO DOCUMENT WAS EDITED BY THIS TOOL AND NO DECLARATION WAS MOVED.**')
    rec('=' * 100)
    pth = run_clock.write(D, 'b377_extract_notes', LINES)
    io.open(d('b377_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(reads=len(READS), without_anchor=noanchor,
                        anchors_differing=differing, by_tag=bytag, refs=refs,
                        six=SIX, two=TWO, built=out,
                        run_file=os.path.basename(pth),
                        run_clock=run_clock.read_stamp(pth)), indent=1))
    print('  written: %s' % os.path.basename(pth))
    return 0 if noanchor == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
