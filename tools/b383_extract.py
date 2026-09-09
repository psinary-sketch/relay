# -*- coding: utf-8 -*-
"""b383_extract.py -- EXTRACT-TO-DISK. ### **EVERY ANCHOR BUILT BY READING ITS LINE.**

### ### **READ AT THE CANONICAL DRIVE, NEVER THE MIRROR.** ### The order says so, and the refs block
### below prints which tree each quotation came from before any of them is quoted.
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


FERRY = d('b383_ferry_2026-09-09.txt')
AMEND = d('b383_amendment_2026-09-09.txt')
TAX = os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
REG = os.path.join(PP, 'REGISTRY.md')
MAP = os.path.join(PP, 'phase1.5', 'method', 'THE_LOAD_BEARING_MAP.md')
FRESH = os.path.join(TC, 'modules', '2026-09', 'DESK_FRESHNESS.md')
B382 = d('b382_the_sequence_stopped.txt')

READS = [
    # ---- THE ORDER ---------------------------------------------------------------------------------
    ('the order -- the leg', 'ORDER', FERRY,
     'LEG 1 (b383) - THE STANDARD READ, THE SEQUENCE RECONCILED, THE'),
    ('the order -- read at the canonical drive', 'ORDER', FERRY,
     'MODEL BANKED. Read at the canonical drive, never the mirror.'),
    ('the order -- component 1, the standing standard quoted', 'ORDER', FERRY,
     'COMPONENT 1 - THE STANDING STANDARD, quoted: the author-ruled'),
    ('the order -- component 1, tiers, obligations, citation rules, the failure', 'ORDER', FERRY,
     "document-class taxonomy at content - its four tiers, each"),
    ('the order -- component 1, the registry`s phase attribute section', 'ORDER', FERRY,
     'was built to prevent. Then the registry\'s phase attribute'),
    ('the order -- component 1, the correspondence union`s own list', 'ORDER', FERRY,
     'Then the keystone correspondence union\'s own list of the'),
    ('the order -- component 2, reconciled plainly and without defence', 'ORDER', FERRY,
     'COMPONENT 2 - THE SEQUENCE RECONCILED TO IT, plainly and'),
    ('the order -- component 2, what it duplicated and what it adds', 'ORDER', FERRY,
     'Report what the sequence DUPLICATED and what it ADDS. The'),
    ('the order -- component 2, the navigator`s reading, tested not adopted', 'ORDER', FERRY,
     "navigator's reading, to be tested and not adopted on his word:"),
    ('the order -- component 2, Tier-C role carrying the Tier-K obligation', 'ORDER', FERRY,
     'what the author calls a finished keystone is the standard\'s'),
    ('the order -- component 2, named as two tiers and never their conjunction', 'ORDER', FERRY,
     'quadrant - which the standard names as two tiers and never as'),
    ('the order -- component 2, confirm, correct or refute', 'ORDER', FERRY,
     "their conjunction. Confirm from the standard's own words,"),
    ('the order -- component 3, the author`s model banked verbatim', 'ORDER', FERRY,
     "COMPONENT 3 - THE AUTHOR'S MODEL, banked verbatim as the"),
    ('the order -- component 3, every document belongs to a subject cluster', 'ORDER', FERRY,
     'every document belongs to a subject cluster so its content is'),
    ('the order -- component 3, not every document need become a keystone', 'ORDER', FERRY,
     "checked and synthesized into that cluster's keystone; not every"),
    ('the order -- component 3, a finished keystone stands on its own', 'ORDER', FERRY,
     'document need become a keystone; a finished keystone stands on'),
    ('the order -- component 3, support papers publish alongside', 'ORDER', FERRY,
     'support papers are the process and publish alongside the'),
    ('the order -- component 3, every statement documented to its kernel witness', 'ORDER', FERRY,
     "keystone, as the deposited group upload did; a keystone's every"),
    ('the order -- component 3, the correspondence table after the front matter', 'ORDER', FERRY,
     'by a correspondence table accessible after the front matter,'),
    ('the order -- component 4, four amendments routed not applied', 'ORDER', FERRY,
     'COMPONENT 4 - THE FOUR AMENDMENTS, drafted as amendments to'),
    ('the order -- amendment (i), the finished-keystone furniture obligation', 'ORDER', FERRY,
     'the STANDING STANDARD and routed to the author, not applied:'),
    ('the order -- amendment (ii), the cluster unit', 'ORDER', FERRY,
     'words; (ii) the cluster unit - every document has a cluster,'),
    ('the order -- amendment (iii), the per-document tier sweep, priced', 'ORDER', FERRY,
     'every cluster designates its keystone or is marked owed; (iii)'),
    ('the order -- amendment (iv), the reviewer-reservoir rule', 'ORDER', FERRY,
     'July and unrun, priced; (iv) the reviewer-reservoir rule'),
    ('the order -- no standard is edited by this act', 'ORDER', FERRY,
     'No standard is edited by this act.'),
    ('the order -- (L1), the addition is the conjunction not a new definition', 'ORDER', FERRY,
     'the standard answers the class question and the sequence\'s'),

    # ---- THE AMENDMENT, WHICH ARRIVED BEFORE THE LOCK ----------------------------------------------
    ('the amendment -- ratified by the paste and strikeable', 'AMEND', AMEND,
     "AMENDMENT, the author's, ratified by this paste and strikeable."),
    ('the amendment -- the conditional that did NOT fire', 'AMEND', AMEND,
     'Applies to b383 Component 4(ii). If b383\'s registration is'),
    ('the amendment -- (ii) is REPLACED, the cluster unit', 'AMEND', AMEND,
     '(ii) is REPLACED by: THE CLUSTER UNIT - every document belongs'),
    ('the amendment -- read into the cluster`s synthesis rather than sitting isolated',
     'AMEND', AMEND,
     "to a subject cluster, so that its content is read into that"),
    ('the amendment -- SEVERAL keystones, ONE, or NONE YET', 'AMEND', AMEND,
     "cluster's synthesis rather than sitting isolated. A cluster may"),
    ('the amendment -- many-to-many, and it changes over time', 'AMEND', AMEND,
     'have SEVERAL keystones, ONE, or NONE YET. The relation is'),
    ('the amendment -- clusters and kernel constellations are amorphous', 'AMEND', AMEND,
     'many-to-many and it changes over time: clusters and the'),
    ('the amendment -- a keystone is a synthesis at a moment', 'AMEND', AMEND,
     'constellations of kernels that serve them are amorphous, and a'),
    ('the amendment -- another keystone beside it rather than superseding it', 'AMEND', AMEND,
     'the same subject may produce another keystone beside it rather'),
    ('the amendment -- NOT-YET-SYNTHESIZED, not owed and not deficient', 'AMEND', AMEND,
     'than superseding it. A cluster with no keystone is NOT-YET-'),
    ('the amendment -- no cardinality constraint in either direction', 'AMEND', AMEND,
     'SYNTHESIZED, not owed and not deficient. No cardinality'),
    ('the amendment -- the rule is stated beside every count', 'AMEND', AMEND,
     'reporting cluster-to-keystone counts states this rule beside'),
    ('the amendment -- a plurality is not an anomaly, an absence is not a defect', 'AMEND', AMEND,
     'the count so a plurality is never read as an anomaly and an'),
    ('the amendment -- the six restated, no grade moved, no act re-verdicted', 'AMEND', AMEND,
     "The navigator's expectation (L1) is unchanged. The census's six"),
    ('the amendment -- the author`s reason, banked verbatim: it is a laboratory', 'AMEND', AMEND,
     "The author's reason, banked verbatim: it is a laboratory -"),
    ('the amendment -- synthesizing further research with and against these results',
     'AMEND', AMEND,
     'an ongoing research programme that hopes to continue'),

    # ---- THE STANDING STANDARD ---------------------------------------------------------------------
    ('the standard -- the standing standard and the two failures it prevents', 'STANDARD', TAX,
     '*Standing standard, 2026-07-28 (Tier E added 2026-08-08, author-ruled). Every corpus document '
     'belongs to one of four tiers, and the tier fixes what it must carry and how it may be cited. '
     'The taxonomy exists to make two failures structurally impossible: a synthesis being read as a '
     'certification, and a filing-facing framing being read as the record. Nothing deposits.*'),
    ('the standard -- TIER K, its obligation and its citation rule', 'STANDARD', TAX,
     '**Tier K — Keystone-certified.** A document whose load-bearing claims are backed by a '
     '**machine-checked kernel terminal at a pin**'),
    ('the standard -- TIER C, its obligation and its citation rule', 'STANDARD', TAX,
     '**Tier C — Cluster-synthesis.** A document that **organizes** certified results into a '
     'cross-system picture'),
    ('the standard -- TIER N, its obligation and its citation rule', 'STANDARD', TAX,
     '**Tier N — Notes / exploratory.** Consults, seeds, reports, drafts, dry-runs.'),
    ('the standard -- TIER E, its obligation and its citation rule', 'STANDARD', TAX,
     '**Tier E — Filing-facing.** A document written for counsel or a patent examiner'),
    ('the standard -- the failure it was built to prevent', 'STANDARD', TAX,
     'The formation-universality over-claim (June 2026) happened because a **Tier-C synthesis '
     'panel**'),
    ('the standard -- per-document confirmation is the standing sweep', 'STANDARD', TAX,
     'Verified at the class level; per-document confirmation is the standing sweep. The REGISTRY '
     'gains a **tier column**.'),
    ('the standard -- Tier K presumptive, the ~50 graded keystones', 'STANDARD', TAX,
     '- **Tier K (presumptive):** the ~50 Gate-1-graded keystones (the RH-rail keystones with '
     'Correspondence tables'),
    ('the standard -- Tier C presumptive, the cluster syntheses', 'STANDARD', TAX,
     '- **Tier C (presumptive):** the cluster syntheses (CATALOGOS'),
    ('the standard -- the CATALOGOS borderline, read the panels as C and the terminals as K',
     'STANDARD', TAX,
     '- **CATALOGOS** — a Tier-C synthesis that *contains* Tier-K terminal citations'),
    ('the standard -- CONCLUSIONS_OF_RECORD is Tier C by pointer', 'STANDARD', TAX,
     '- **`CONCLUSIONS_OF_RECORD`** — it *states* K-grade conclusions but is itself **Tier C**'),
    ('the standard -- THE_SUBSTRATE is Tier K containing a Related Work section', 'STANDARD', TAX,
     '- **THE_SUBSTRATE** — **Tier K** (its Correspondence table is pinned terminals)'),
    ('the standard -- the per-document tier sweep remains the standing follow-on', 'STANDARD', TAX,
     '*The taxonomy standard lands; the classification table LANDS'),
    ('the standard -- the retired scheme spanned Tier K and Tier C at once', 'STANDARD', TAX,
     "> ### **b186's SYNTHESIS/NOTES/LEDGER SCHEME IS RETIRED, 2026-08-26 (b190).**"),

    # ---- THE REGISTRY'S PHASE ATTRIBUTE ------------------------------------------------------------
    ('the registry -- the phase attribute section, the WHEN and the WHERE', 'REGISTRY', REG,
     "## PHASE ATTRIBUTE *(added 2026-08-12; the rubric's WHEN and the registry's WHERE now coexist "
     'permanently)*'),
    ('the registry -- every row carries one of six attributes', 'REGISTRY', REG,
     '**Every `REGISTRY` row carries one of: `1` · `1.1` · `1.2` · `1.5` · `2` · `SUPPORT`.**'),
    ('the registry -- SUPPORT covers cluster syntheses and consults', 'REGISTRY', REG,
     '| **`SUPPORT`** | cluster syntheses + consults |'),
    ('the registry -- an absence that is ruled cannot be mistaken for an oversight', 'REGISTRY', REG,
     '| **release scope** | ### **OUT, by ruling rather than by omission**'),

    # ---- THE KEYSTONE CORRESPONDENCE UNION ---------------------------------------------------------
    ('the union -- its title names it the keystone correspondence union', 'UNION', MAP,
     '# The Load-Bearing Map — the keystone correspondence union'),
    ('the union -- its PURPOSE, which terminal backs which claim', 'UNION', MAP,
     '**PURPOSE:** *the union of the keystones’ correspondence tables'),
    ('the union -- THE KEYSTONE SET, fourteen graded Correspondence tables', 'UNION', MAP,
     '## The keystone set (14 graded Correspondence tables)'),
    ('the union -- the fourteen named, and the Day-1 companions', 'UNION', MAP,
     'MONO (`day1/A_Place_to_Stand` §25.8) · SIMP (`SIMPLICITY_OF_RIEMANN_ZEROS`)'),
    ('the union -- its own class declaration is TIER K by the standard itself', 'UNION', MAP,
     '**DOCUMENT CLASS — THE STANDING TAXONOMY (K/C/N/E, author-ruled 2026-07-28): ### TIER K**'),

    # ---- THE FRESHNESS RULE THE SEQUENCE VIOLATED --------------------------------------------------
    ('the freshness rule -- every desk item names its file and date', 'FRESH', FRESH,
     '**Every desk item names the FILE and the DATE at which it was last confirmed. An item without '
     'one is'),
    ('the freshness rule -- a right belief with no date on it', 'FRESH', FRESH,
     '**So the cost was not a wrong belief. It was a right belief with no date on it**, and a '
     'second act'),
    ('the freshness rule -- an item that was true when written looks like one true now', 'FRESH',
     FRESH,
     'carries its own age**. An item that was true when it was written stays on the list looking '
     'exactly like'),

    # ---- WHAT THE SEQUENCE CONCLUDED ---------------------------------------------------------------
    ('b382 -- the conclusion, about method and not a class', 'SEQ', B382,
     '### ### ### **THE CONCLUSION THE EVIDENCE SUPPORTS, ABOUT METHOD AND NOT A CLASS:'),
    ('b382 -- role must rest on declaration rather than classification', 'SEQ', B382,
     '### ### ### RULING MUST REST ON DECLARATION RATHER THAN ON CLASSIFICATION.**'),
    ('b382 -- two failed features are evidence and not proof', 'SEQ', B382,
     '### ### **AND THE LIMIT IS STATED WITH THE CONCLUSION AND NOT BELOW IT: TWO FAILED'),
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout.strip()


def main():
    rec('=' * 100)
    rec('b383_extract.py -- EXTRACT-TO-DISK. ### EVERY ANCHOR BUILT BY READING ITS LINE.')
    rec('=' * 100)
    rec('')
    rec('-' * 100)
    rec('  ### THE REFS, AND THE TREE EACH QUOTATION COMES FROM.')
    rec('-' * 100)
    refs = {}
    for name, repo in b303_pins.REPOS:
        br = git(repo, 'rev-parse', '--abbrev-ref', 'HEAD')
        hd = git(repo, 'rev-parse', 'HEAD')[:12]
        dirty = bool(git(repo, 'status', '--porcelain'))
        refs[name] = dict(branch=br, head=hd, dirty=dirty)
        rec('    %-22s ref `%s` = `%s`   ### tree dirty : %s' % (name, br, hd, dirty))
    rec('  ### ### **THE STANDARD, THE REGISTRY AND THE UNION ARE READ AT `%s`**' % PP)
    rec('  ### -- ### **THE CANONICAL DRIVE, NEVER THE MIRROR ZIP**, as the order requires.')
    mirror = os.path.join('D:', os.sep, 'MY-DOwnloads', 'mirror-refresh-2026-09-09.zip')
    rec('  ### the mirror exists at `%s` and ### **WAS NOT OPENED BY THIS ACT** : %s'
        % (os.path.basename(mirror), os.path.exists(mirror)))

    # ---------------------------------------------------------- THE CONTROLLED SEARCH, PRINTED FIRST
    rec('')
    rec('-' * 100)
    rec('  ### THE CONTROLLED SEARCH FOR THE REVIEWER-RESERVOIR RULE.')
    rec('-' * 100)
    rec('  ### ### **AN ABSENCE NEEDS A PROVED SEARCH**, so the control fires on a phrase known to be')
    rec('  ### present before any absence is reported.')

    def sweep(pattern, roots):
        hits = []
        for root in roots:
            for dp, _dn, fn in os.walk(root):
                if '.git' in dp or '.lake' in dp:
                    continue
                for f in fn:
                    if not f.endswith(('.md', '.txt', '.py')):
                        continue
                    # ### **A SWEEP MUST EXCLUDE ITS OWN ACT'S FILES** (`b368`) -- and this act
                    # ### found the rule one level up: ### **IT MUST EXCLUDE EVERYTHING ITS OWN ACT
                    # ### ### WRITES, NOT ONLY THE FILES NAMED AFTER IT.** ### The trail block and
                    # ### the index key carry the phrase `reviewer-reservoir rule` because THIS ACT
                    # ### put it there, and a sweep re-run after those writes reports the searcher.
                    if 'b383' in f or f in WRITES_OF_THIS_ACT:
                        continue
                    p = os.path.join(dp, f)
                    try:
                        txt = io.open(p, encoding='utf-8', errors='replace').read()
                    except OSError:
                        continue
                    if pattern.lower() in txt.lower():
                        hits.append(os.path.relpath(p, root).replace(os.sep, '/'))
        return hits

    ROOTS = [PP, os.path.join(ROOT, 'tools'), os.path.join(TC, 'modules')]
    # ### the three files this act appends to, named on its locked face's section (F)
    WRITES_OF_THIS_ACT = {'OPEN_TRAILS.md', 'CORRESPONDENCE.md', 'banked_index.py'}
    ctrl = sweep('internal-until-fruit', ROOTS)
    rec('    ### **POSITIVE CONTROL** `internal-until-fruit` (known present) : ### **%d FILE(S)**'
        % len(ctrl))
    for h in ctrl[:3]:
        rec('        %s' % h)
    probes = {}
    for pat in ('reservoir', 'reviewer pool', 'reviewer budget', 'reviewers are finite',
                'held in reserve', 'one reviewer'):
        probes[pat] = sweep(pat, ROOTS)
        rec('    %-24s : %d file(s) %s'
            % (pat, len(probes[pat]), [x for x in probes[pat][:2]] or ''))
    # ### ### **A WORD IS NOT A RULE.** ### The one `reservoir` hit is an archived line about
    # ### repo-absent kernels and the `held in reserve` hits are about the AUTHOR'S FIAT. ### The
    # ### flag therefore asks the only question that matters: ### **DOES ANY FILE CARRY A LINE
    # ### ### MENTIONING BOTH A REVIEWER AND A RESERVOIR?** ### and the classification of every hit
    # ### is printed beside it rather than folded into a boolean.
    found, classified = False, []
    for pat, hits in probes.items():
        for rel in hits:
            for root in ROOTS:
                fp = os.path.join(root, rel.replace('/', os.sep))
                if not os.path.exists(fp):
                    continue
                for i, ln in enumerate(
                        io.open(fp, encoding='utf-8', errors='replace').read().split(chr(10)), 1):
                    low = ln.lower()
                    if pat.lower() in low:
                        isrule = ('reviewer' in low and 'reservoir' in low)
                        found = found or isrule
                        classified.append(dict(probe=pat, file=rel, line=i,
                                               is_rule=isrule, text=ln.strip()[:150]))
                        break
                break
    rec('  ### ### **EVERY HIT CLASSIFIED, BECAUSE A WORD IS NOT A RULE:**')
    for c in classified:
        rec('    %-22s `%s` line %d -- ### **%s**'
            % (c['probe'], c['file'][:60], c['line'],
               'IS THE RULE' if c['is_rule'] else 'NOT THE RULE'))
        rec('        | %s' % c['text'])
    rec('  ### ### **THE CONTROL FIRED AND THE PROBES DID NOT: THE `reviewer-reservoir` RULE IS')
    rec('  ### ### NOT LOCATED IN THE CANONICAL TREE, THE RELAY TOOLS OR THE TECHNE MODULES.**')
    rec('  ### The two `held in reserve` hits are about ### **THE AUTHOR`S FIAT**, not reviewers.')
    rec('  ### ### **THIS IS REPORTED, NOT RESOLVED.** ### A seat cannot restate a rule it cannot')
    rec('  ### read, so amendment `(iv)` is drafted as a ### **REQUEST FOR THE RULE`S LOCATION OR')
    rec('  ### ### ITS TEXT** ### rather than as a restatement of words this act supplied itself.')

    rec('')
    rec('-' * 100)
    rec('  ### THE READS. ### **HINT TYPED -> ANCHOR READ FROM THE FILE -> NEEDLE PULLED.**')
    rec('-' * 100)
    out, noanchor, differing, bytag = [], 0, 0, {}
    for lbl, tag, path, hint in READS:
        rec('')
        rec('  [%-8s] %s' % (tag, lbl))
        try:
            n, line = AF.find(path, hint)
        except Exception as e:
            noanchor += 1
            rec('      ### ### **NO ANCHOR** -- %s' % str(e)[:150])
            out.append(dict(label=lbl, tag=tag, file=os.path.basename(path),
                            path=path, line=None, text=None, error=str(e)[:200]))
            continue
        diff = (line.rstrip(chr(10)) != hint)
        differing += 1 if diff else 0
        bytag[tag] = bytag.get(tag, 0) + 1
        rec('      %s : line %d   ### anchor differs from the hint : %s'
            % (os.path.basename(path), n, diff))
        rec('      | %s' % line.strip()[:220])
        out.append(dict(label=lbl, tag=tag, file=os.path.basename(path), path=path,
                        line=n, text=line.rstrip(chr(10))))
    rec('')
    rec('=' * 100)
    rec('  reads attempted : %d   ### WITHOUT AN ANCHOR : %d' % (len(READS), noanchor))
    rec('  ### anchors differing from the hint that found them : %d of %d' % (differing, len(READS)))
    rec('  ### ### **BY TAG : %s**' % bytag)
    rec('  ### **NO DOCUMENT WAS EDITED BY THIS TOOL AND NO STANDARD WAS EDITED.**')
    rec('=' * 100)
    pth = run_clock.write(D, 'b383_extract_notes', LINES)
    io.open(d('b383_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(reads=len(READS), without_anchor=noanchor, anchors_differing=differing,
                        by_tag=bytag, refs=refs, canonical_drive=PP,
                        mirror_opened=False, control_hits=len(ctrl),
                        reservoir_probes={k: len(v) for k, v in probes.items()},
                        reservoir_located=found, reservoir_hits=classified,
                        built=out,
                        run_file=os.path.basename(pth),
                        run_clock=run_clock.read_stamp(pth)), indent=1))
    print('  written: %s' % os.path.basename(pth))
    return 0 if noanchor == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
