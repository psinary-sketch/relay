# -*- coding: utf-8 -*-
"""b385_extract.py -- EXTRACT-TO-DISK, AND THE TARGETED SEARCH FOR THE RESERVOIR RULE.

### ### **`b383` SEARCHED FOR THE NAVIGATOR'S NAME FOR THE RULE AND NOT FOR THE RULE.** ### Its
### probes were `reservoir`, `reviewer pool`, `reviewer budget` -- and the standing rule uses none of
### those words. ### **THE TARGETED SEARCH HERE USES THE RULE'S OWN VOCABULARY**, which the order
### supplied: `mirror-refresh`, `MANIFEST`, `recall`, `session protocol`.
### ### **THE POSITIVE CONTROL FIRES ON A KNOWN RULE FIRST**, and every term is printed.
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


FERRY = d('b385_ferry_2026-09-09.txt')
REG = os.path.join(PP, 'REGISTRY.md')
TAX = os.path.join(PP, 'phase1.5', 'method', 'THE_DOCUMENT_CLASS_TAXONOMY.md')
GUARD = os.path.join(ROOT, '.githooks', 'pre-push')
B378 = d('b378_the_refs_widened.txt')
B383 = d('b383_the_standard_read.txt')
AMEND = d('b383_amendment_2026-09-09.txt')

READS = [
    # ---- THE ORDER ---------------------------------------------------------------------------------
    ('the order -- the act', 'ORDER', FERRY,
     'ACT b385 - THE SIX ON THE TRAILS, THE RULE FOUND OR ABSENT, AND'),
    ('the order -- component 1, the clusters on the trails ledger', 'ORDER', FERRY,
     'COMPONENT 1 - THE NOT-YET-SYNTHESIZED CLUSTERS, entered on the'),
    ('the order -- component 1, a cluster needing a synthesis belongs on the to-do system',
     'ORDER', FERRY,
     "trails ledger through its writer, per the author's ruling that"),
    ('the order -- component 1, one entry per cluster and what it carries', 'ORDER', FERRY,
     'per cluster: the cluster as the registry names it, where its'),
    ('the order -- component 1, the many-to-many rule beside each entry', 'ORDER', FERRY,
     'it - several keystones, one, or none yet; not owed, not'),
    ('the order -- component 1, nothing is opened', 'ORDER', FERRY,
     'a plurality as an anomaly. Nothing is opened; these are trail'),
    ('the order -- component 2, the reservoir rule found or absent', 'ORDER', FERRY,
     'COMPONENT 2 - THE RESERVOIR RULE, FOUND OR ABSENT: the'),
    ('the order -- component 2, the navigator`s paraphrase', 'ORDER', FERRY,
     'navigator quoted to the author a standing rule that a session'),
    ('the order -- component 2, the manifest is the authority over recall', 'ORDER', FERRY,
     "export, and that the export's manifest is the reviewer's"),
    ('the order -- component 2, search targeted rather than general', 'ORDER', FERRY,
     'again, targeted rather than general: the registry\'s session-'),
    ('the order -- component 2, the LOCATED verdict scores the paraphrase clause by clause',
     'ORDER', FERRY,
     'rule first. Verdicts: (LOCATED - quoted whole with its'),
    ('the order -- component 2, the NOT LOCATED verdict', 'ORDER', FERRY,
     'any over-statement named) / (NOT LOCATED -'),
    ('the order -- component 3, the three that wait on nothing', 'ORDER', FERRY,
     'COMPONENT 3 - THE THREE THAT WAIT ON NOTHING, as the draft'),
    ('the order -- component 3, by digest and content match, never by filename', 'ORDER', FERRY,
     'whose canonical copies are unconfirmed, confirmed by digest and'),
    ('the order -- component 3, the faces ledger and the roster`s own rules', 'ORDER', FERRY,
     'roster, added if the roster\'s own rules permit an addition or'),
    ('the order -- component 3, each done or routed, none partly', 'ORDER', FERRY,
     'routed if they do not. Each done or routed, none partly.'),
    ('the order -- component 4, the citation question routed not answered', 'ORDER', FERRY,
     'COMPONENT 4 - THE CITATION QUESTION, ROUTED AND NOT ANSWERED:'),
    ('the order -- component 4, state the question in the standard`s own words', 'ORDER', FERRY,
     'ruling one tier and reading the parts apart. State the question'),
    ('the order -- component 4, the failure the tiers exist to prevent, quoted beside',
     'ORDER', FERRY,
     'failure the tiers exist to prevent quoted beside them. Recommend'),
    ('the order -- (F1), the rule is located and the paraphrase over-stated', 'ORDER', FERRY,
     'expectations: (F1) the reservoir rule is LOCATED in a'),
    ('the order -- (F2), all three complete without a ruling', 'ORDER', FERRY,
     "over-stated its scope; (F2) all three of Component 3's items"),

    # ---- THE RULE, LOCATED -------------------------------------------------------------------------
    ('the rule -- the section heading, a session protocol and a standing rule', 'RULE', REG,
     '## SESSION PROTOCOL — reviewer mirror-refresh (standing rule, 2026-07-29)'),
    ('the rule -- clause one, any session reasoning about paper CONTENT', 'RULE', REG,
     '**Any session in which the chat reviewer reasons about paper *content* begins with a fresh '
     'mirror-refresh export.**'),
    ('the rule -- the procedure, and the MANIFEST`s two columns as the authority', 'RULE', REG,
     '- **Procedure.** Create `D:\\MY-DOwnloads\\mirror-refresh-<today>\\` fresh'),
    ('the rule -- why it is a hard rule: two recorded errors', 'RULE', REG,
     '- **Why this is a hard rule, not a nicety.** Stale mirror content has already produced two '
     'recorded errors'),
    ('the rule -- the currency check, the MANIFEST wins', 'RULE', REG,
     '- **Currency check.** If a reviewer\'s claim disagrees with the current MANIFEST'),

    # ---- THE STANDARD, FOR COMPONENT 4 -------------------------------------------------------------
    ('the standard -- TIER K may be cited as certification', 'STANDARD', TAX,
     '**Tier K — Keystone-certified.** A document whose load-bearing claims are backed by a '
     '**machine-checked kernel terminal at a pin**'),
    ('the standard -- TIER C is never cited as certification', 'STANDARD', TAX,
     '**Tier C — Cluster-synthesis.** A document that **organizes** certified results into a '
     'cross-system picture'),
    ('the standard -- the failure the tiers exist to prevent', 'STANDARD', TAX,
     'The formation-universality over-claim (June 2026) happened because a **Tier-C synthesis '
     'panel**'),
    ('the standard -- the two failures it makes structurally impossible', 'STANDARD', TAX,
     '*Standing standard, 2026-07-28 (Tier E added 2026-08-08, author-ruled).'),
    ('the standard -- CATALOGOS, read the panels as C and the terminals as K', 'STANDARD', TAX,
     '- **CATALOGOS** — a Tier-C synthesis that *contains* Tier-K terminal citations'),
    ('the standard -- UNIVERSALITY, mostly K with the C-scope note', 'STANDARD', TAX,
     '- **UNIVERSALITY.md** — its ζ_K count-7 claim is K-grade'),
    ('the standard -- THE_SUBSTRATE, Tier K containing a Related Work section', 'STANDARD', TAX,
     '- **THE_SUBSTRATE** — **Tier K** (its Correspondence table is pinned terminals)'),
    ('the standard -- Tier E relaxes the audience, never the certificate', 'STANDARD', TAX,
     '**Tier E — Filing-facing.** A document written for counsel or a patent examiner'),

    # ---- THE GUARD -------------------------------------------------------------------------------
    ('the guard -- its own install line, which the record no longer uses', 'GUARD', GUARD,
     '# Tracked copy: tools/git-hooks/pre-push. Install: cp tools/git-hooks/pre-push '
     '.git/hooks/pre-push'),

    # ---- b378 ON THE ARCHIVE ------------------------------------------------------------------------
    ('b378 -- confirmed by digest and title line, never by filename', 'PRIOR', B378,
     '### ### **CONFIRMED BY A VERIFIED DIGEST AND BY A TITLE LINE. ### NEVER BY FILENAME** -- the'),
    ('b378 -- the 86 it made no claim about', 'PRIOR', B378,
     '### `archive/` on the canonical drive and the mirror carries `6` of them; the other `86` '
     'were'),
    ('b378 -- nothing was removed and the removal is the author`s', 'PRIOR', B378,
     '### ### ### **NOTHING WAS REMOVED, MOVED OR RENAMED. ### THE REMOVAL IS THE AUTHOR`S AND '
     'DEPENDS'),

    # ---- b383, AND THE AMENDMENT --------------------------------------------------------------------
    ('b383 -- a seat cannot restate a rule it cannot read', 'PRIOR', B383,
     '### ### **A SEAT CANNOT RESTATE A RULE IT CANNOT READ**, and a seat that supplies the'),
    ('b383 -- the conjunction is excluded, not merely unnamed', 'PRIOR', B383,
     '### ### **WRONG IN ONE PARTICULAR, AND IT MATTERS: THE CONJUNCTION IS NOT MERELY'),
    ('the amendment -- several keystones, one, or none yet', 'AMEND', AMEND,
     "cluster's synthesis rather than sitting isolated. A cluster may"),
    ('the amendment -- NOT-YET-SYNTHESIZED, not owed and not deficient', 'AMEND', AMEND,
     'than superseding it. A cluster with no keystone is NOT-YET-'),
    ('the amendment -- the rule is stated beside every count', 'AMEND', AMEND,
     'reporting cluster-to-keystone counts states this rule beside'),
    ('the amendment -- it is a laboratory', 'AMEND', AMEND,
     "The author's reason, banked verbatim: it is a laboratory -"),
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
    rec('b385_extract.py -- EXTRACT-TO-DISK, AND THE TARGETED SEARCH.')
    rec('=' * 100)
    rec('')
    rec('-' * 100)
    rec('  ### THE REFS.')
    rec('-' * 100)
    refs = {}
    for name, repo in b303_pins.REPOS:
        br = git(repo, 'rev-parse', '--abbrev-ref', 'HEAD')
        hd = git(repo, 'rev-parse', 'HEAD')[:12]
        refs[name] = dict(branch=br, head=hd, dirty=bool(git(repo, 'status', '--porcelain')))
        rec('    %-22s ref `%s` = `%s`   ### tree dirty : %s'
            % (name, br, hd, refs[name]['dirty']))

    # ------------------------------------------------- THE TARGETED SEARCH, PRINTED BEFORE THE READS
    rec('')
    rec('-' * 100)
    rec('  ### COMPONENT 2 -- THE TARGETED SEARCH FOR THE RULE.')
    rec('-' * 100)
    rec('  ### ### **`b383` SEARCHED FOR THE NAVIGATOR`S NAME FOR THE RULE AND NOT FOR THE RULE.**')
    rec('  ### Its probes were `reservoir`, `reviewer pool`, `reviewer budget` -- and ### **THE')
    rec('  ### ### STANDING RULE USES NONE OF THOSE WORDS.** ### This search uses the rule`s own')
    rec('  ### vocabulary, which the order supplied.')

    WRITES = {'OPEN_TRAILS.md', 'CORRESPONDENCE.md', 'banked_index.py', 'FINDINGS.md'}
    ROOTS = [PP, os.path.join(ROOT, 'tools'), os.path.join(TC, 'modules')]

    def sweep(pattern):
        hits = []
        for root in ROOTS:
            for dp, _dn, fn in os.walk(root):
                if '.git' in dp or '.lake' in dp:
                    continue
                for f in fn:
                    if not f.endswith(('.md', '.txt', '.py')) or 'b385' in f or f in WRITES:
                        continue
                    p = os.path.join(dp, f)
                    try:
                        txt = io.open(p, encoding='utf-8', errors='replace').read()
                    except OSError:
                        continue
                    for i, ln in enumerate(txt.split(chr(10)), 1):
                        if pattern.lower() in ln.lower():
                            hits.append((os.path.relpath(p, root).replace(os.sep, '/'), i,
                                         ln.strip()[:120]))
                            break
        return hits

    ctrl = sweep('internal-until-fruit')
    rec('    ### **POSITIVE CONTROL** `internal-until-fruit` (a known rule) : ### **%d FILE(S)**'
        % len(ctrl))
    for h in ctrl[:2]:
        rec('        %s line %d' % (h[0], h[1]))
    TERMS = ['SESSION PROTOCOL', 'mirror-refresh', 'reviewer set', 'not from recall',
             "reviewer's authority", 'Currency check', 'reservoir']
    probes, found_at = {}, []
    for term in TERMS:
        hits = sweep(term)
        probes[term] = [(h[0], h[1]) for h in hits]
        rec('    %-22s : ### **%d file(s)**' % (term, len(hits)))
        for h in hits[:2]:
            rec('        %s line %-5d | %s' % (h[0], h[1], h[2]))
        if term in ('SESSION PROTOCOL', "reviewer's authority", 'not from recall'):
            found_at += [(h[0], h[1]) for h in hits]
    located = any(h[0] == 'REGISTRY.md' for h in found_at)
    rec('  ### ### ### **VERDICT : %s.**' % ('LOCATED' if located else 'NOT LOCATED'))
    if located:
        rec('  ### ### **IT IS IN `REGISTRY.md`, UNDER `## SESSION PROTOCOL — reviewer')
        rec('  ### ### mirror-refresh (standing rule, 2026-07-29)`** -- exactly where the order said')
        rec('  ### to look. ### **`b383`S ABSENCE CLAIM IS REFUTED BY THIS ACT**, and the reason is')
        rec('  ### that it searched for a NAME the record does not use.')

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
            out.append(dict(label=lbl, tag=tag, file=os.path.basename(path), path=path,
                            line=None, text=None, error=str(e)[:200]))
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
    rec('  ### ### **BY TAG : %s**' % bytag)
    rec('  ### **NO DOCUMENT WAS EDITED BY THIS TOOL.**')
    rec('=' * 100)
    pth = run_clock.write(D, 'b385_extract_notes', LINES)
    io.open(d('b385_reads.json'), 'w', encoding='utf-8', newline=chr(10)).write(
        json.dumps(dict(reads=len(READS), without_anchor=noanchor, anchors_differing=differing,
                        by_tag=bytag, refs=refs, control_hits=len(ctrl),
                        probes={k: len(v) for k, v in probes.items()},
                        probe_hits=probes, rule_located=located, built=out,
                        run_file=os.path.basename(pth),
                        run_clock=run_clock.read_stamp(pth)), indent=1))
    print('  written: %s' % os.path.basename(pth))
    return 0 if noanchor == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
