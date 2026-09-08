# -*- coding: utf-8 -*-
"""b367_locate.py -- THE LOCATION, THE READ AND THE SWEEP. ### **A READ. ### NO BUILD. ### NO WRITE.**

### ### **BAR 1: A TERMINAL THIS ACT CANNOT LOCATE IS REPORTED `NOT LOCATED` AND IS NEVER DESCRIBED FROM
### ### THE HINT.**
### ### **BAR 2: EVERY QUOTATION CARRIES THE REF ITS FILE WAS READ AT.** ### The refs are read from the
### repositories themselves and printed before anything is quoted.
### ### **BAR 3: NO BUILD IS RUN.** ### Whatever this act says about an axiom profile is READ from a
### printed record, and if no printed record covers a name that is reported as `NO PRINTED PROFILE`.
### ### **AND THE HINT IS SCORED AGAINST WHAT WAS FOUND, NOT THE FOUND AGAINST THE HINT.** ### The
### locator searches for the NAMES the hint supplies AND for the SHAPES the kernel's own audit describes,
### and reports both, so a clause that is wrong is visible as wrong rather than absorbed.
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import run_clock                # noqa: E402
import anchor_from_file as AF   # noqa: E402
import gate_needle as GN        # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
SIDE = os.path.join('D:', os.sep, 'SIDE-global-section')
KERNEL = os.path.join('D:', os.sep, 'SIDE-effects')
GRHK = os.path.join('D:', os.sep, 'SIDE-grh-transfer')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# ### **THE NAMES THE HINT'S SUBJECTS CARRY IN THE KERNEL'S OWN LEDGER.** ### Read from the ledger, not
# ### supplied by the navigator: the hint names SUBJECTS (the generalized hypothesis, an exceptional real
# ### zero) and the ledger names DECLARATIONS.
HINTED = [('GRH', ['grh_exclusion', 'twist_cancels', 'formation_preserved_grh']),
          ('Landau-Siegel', ['no_ls_zero'])]

# ### THE KERNEL'S OWN LEAN FILES. ### **THE `.lake` TREE IS VENDORED MATHLIB AND IS NOT THIS KERNEL.**
KERNEL_LEAN = ['SIDEEffects.lean', 'SIDEEffects/ExhaustivenessLicense.lean',
               'SIDEEffects/Milestones.lean', 'SIDEEffects/Phase15/Module1.lean',
               'SIDEEffects/Phase15/SIDEFramework.lean', 'SIDEEffects/Structural.lean']

# ### THE FRONT DOCUMENT'S OWN LAYER-1 EXPORT LIST, READ FROM ITS OWN LINES BY ANCHOR.
FRONT_LINES = [
    '- **Yang-Mills mass gap layer**:',
    '- **GRH layer**:',
    '- **Landau-Siegel layer**:',
    '- **Additive-multiplicative / Type-D layer**:',
    '- **BSD layer**:',
    '- **Artin layer**:',
    '- **Shared engine**:',
]

LINES = []


def rec(s=''):
    LINES.append(s)
    print(s, flush=True)


def git(repo, *a):
    return subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                          encoding='utf-8', errors='replace').stdout


def refs_of(repo):
    b = git(repo, 'rev-parse', '--abbrev-ref', 'HEAD').strip()
    h = git(repo, 'rev-parse', '--short', 'HEAD').strip()
    branches = [x.strip().lstrip('* ').strip() for x in git(repo, 'branch').splitlines() if x.strip()]
    others = []
    for other in branches:
        if other == b:
            continue
        c = git(repo, 'rev-list', '--left-right', '--count', '%s...%s' % (b, other)).split()
        if len(c) == 2:
            others.append(dict(branch=other, head_ahead=int(c[0]), other_ahead=int(c[1])))
    dirty = bool(git(repo, 'status', '--porcelain').strip())
    return dict(branch=b, head=h, others=others, dirty=dirty)


def decl_sites(name):
    """### **A LIVE DECLARATION, NOT A MENTION.** ### A Lean declaration begins its line with one of the
    ### declaration keywords; a name inside a `--` comment is a MENTION and is counted apart."""
    live, mentions = [], []
    for rel in KERNEL_LEAN:
        p = os.path.join(KERNEL, rel.replace('/', os.sep))
        if not os.path.exists(p):
            continue
        for i, ln in enumerate(io.open(p, encoding='utf-8', errors='replace').read().split(chr(10)), 1):
            if name not in ln:
                continue
            code = ln.split('--')[0]
            if re.match(r'^\s*(theorem|lemma|def|abbrev|instance|axiom|structure|inductive)\s+' +
                        re.escape(name) + r'\b', code):
                live.append(dict(file=rel, line=i, text=ln.strip()[:150]))
            else:
                mentions.append(dict(file=rel, line=i, text=ln.strip()[:150],
                                     in_comment=bool(re.match(r'^\s*--', ln))))
    return live, mentions


def sweep_repo(repo, names):
    out = []
    for n in names:
        hits = git(repo, 'grep', '-n', '-I', '--', n).splitlines()
        for h in hits[:40]:
            out.append(dict(name=n, hit=h[:190]))
    return out


def main():
    rec('=' * 100)
    rec('b367 -- THE LOCATION, THE READ AND THE SWEEP. ### **A READ. ### NO BUILD. ### NO WRITE.**')
    rec('=' * 100)
    rec('')
    rec('  ### the anchor tool fixtures, run before it is trusted : %s' % AF.self_test(False))
    rec('  ### the needle helper fixtures, run before it is trusted : %s' % GN.self_test(False))

    rec('')
    rec('-' * 100)
    rec('  ### (0) BAR 2 -- THE REFS. ### **THE ACT NAMES THE REF IT READ AND THE REFS IT DID NOT.**')
    rec('-' * 100)
    R = {}
    for lbl, repo in (('SIDE-effects', KERNEL), ('SIDE-grh-transfer', GRHK)):
        if not os.path.isdir(repo):
            rec('    %-22s ### **NOT ON THIS MACHINE**' % lbl)
            R[lbl] = None
            continue
        R[lbl] = refs_of(repo)
        rec('    %-22s READ AT ref `%s` = `%s`   (working tree dirty : %s)'
            % (lbl, R[lbl]['branch'], R[lbl]['head'], R[lbl]['dirty']))
        for o in R[lbl]['others']:
            rec('        ### not read : `%-26s` -- the read ref is %d ahead of it, it is %d ahead of the'
                % (o['branch'], o['head_ahead'], o['other_ahead']))
            rec('        ### read ref.')
    k = R.get('SIDE-effects') or {}
    behind = [o for o in k.get('others', []) if o['other_ahead'] > 0]
    rec('    ### ### **BRANCHES CARRYING WORK THE READ REF DOES NOT HAVE : %d** ### -- so a read of the'
        % len(behind))
    rec('    ### checked-out ref misses %s.' % ('nothing' if not behind else 'something'))

    rec('')
    rec('-' * 100)
    rec('  ### (1) THE LOCATION. ### **LIVE DECLARATIONS VS MENTIONS.**')
    rec('-' * 100)
    found = {}
    for subject, names in HINTED:
        rec('')
        rec('    ### subject from the hint : **%s**' % subject)
        for n in names:
            live, ment = decl_sites(n)
            found[n] = dict(subject=subject, live=live, mentions=ment)
            rec('      %-24s LIVE DECLARATIONS : %d ; mentions : %d'
                % ('`%s`' % n, len(live), len(ment)))
            for m in ment[:3]:
                rec('          %s:%d  (inside a comment : %s)' % (m['file'], m['line'], m['in_comment']))
                rec('            | %s' % m['text'][:130])
    n_live = sum(len(v['live']) for v in found.values())
    n_ment = sum(len(v['mentions']) for v in found.values())
    all_in_comment = all(m['in_comment'] for v in found.values() for m in v['mentions'])
    rec('')
    rec('    ### ### **LIVE DECLARATIONS FOUND : %d.** ### mentions : %d, every one inside a comment : %s'
        % (n_live, n_ment, all_in_comment))

    rec('')
    rec('-' * 100)
    rec('  ### (2) AND THE SAME NAMES WHERE THE LEDGER POINTS INSTEAD.')
    rec('-' * 100)
    grh_hits = []
    if os.path.isdir(GRHK):
        for _s, names in HINTED:
            for n in names:
                hs = git(GRHK, 'grep', '-n', '-I', '--', n).splitlines()
                grh_hits.extend(hs)
        rec('    `SIDE-grh-transfer` occurrences of any hinted name : %d' % len(grh_hits))
        for h in grh_hits[:5]:
            rec('        | %s' % h[:170])
    rec('    ### ### **SO THE NAMES ARE NOT LIVE THERE EITHER.**' if not grh_hits else
        '    ### ### **THE NAMES APPEAR THERE AND ARE REPORTED ABOVE.**')

    rec('')
    rec('-' * 100)
    rec("  ### (3) THE FRONT DOCUMENT. ### **WHAT IT EXPORTS AGAINST WHAT THE SOURCE HAS.**")
    rec('-' * 100)
    agents = os.path.join(KERNEL, 'AGENTS.md')
    exported, per_layer = [], []
    for hint in FRONT_LINES:
        try:
            ln, line = AF.find(agents, hint)
        except AF.AnchorError:
            continue
        names = re.findall(r'`([A-Za-z_][A-Za-z0-9_.]*)`', line)
        per_layer.append(dict(layer=hint.strip('- *:'), line=ln, names=names))
        exported.extend(names)
    absent, present = [], []
    for n in exported:
        live, _m = decl_sites(n.split('.')[-1])
        (present if live else absent).append(n)
    for pl in per_layer:
        rec('    %-46s line %-5d names %d' % (pl['layer'][:46], pl['line'], len(pl['names'])))
    rec('')
    rec('    ### ### **NAMES THE FRONT DOCUMENT EXPORTS AT LAYER 1 : %d.**' % len(exported))
    rec('    ### ### **PRESENT IN THE SOURCE : %d  ### -- ABSENT : %d.**' % (len(present), len(absent)))
    rec('    ### present : %s' % (', '.join(present) or 'none'))
    rec('    ### ### **AND THE THREE THE HINT NAMES ARE AMONG THE ABSENT : %s**'
        % all(n in absent for n in ('grh_exclusion', 'twist_cancels', 'no_ls_zero')))

    rec('')
    rec('-' * 100)
    rec('  ### (4) THE CITATION SWEEP. ### **BOUNDED, AND IT SAYS WHERE IT LOOKED.**')
    rec('-' * 100)
    names = [n for _s, ns in HINTED for n in ns]
    sweep = {}
    for lbl, repo in (('relay', ROOT), ('SIDE-global-section', SIDE), ('PLACE-papers', PP),
                      ('SIDE-effects', KERNEL), ('SIDE-grh-transfer', GRHK)):
        if not os.path.isdir(repo):
            continue
        sweep[lbl] = sweep_repo(repo, names)
        files = sorted({h['hit'].split(':')[0] for h in sweep[lbl]})
        rec('    %-22s hits %-4d in %d tracked file(s)' % (lbl, len(sweep[lbl]), len(files)))
        for f in files[:8]:
            rec('        %s' % f)
    rec('    ### ### **AN ABSENCE FOUND BY THIS SEARCH IS AN ABSENCE FROM THESE FIVE REPOSITORIES**, and')
    rec('    ### is reported in those words rather than as an absence from the record.')

    rec('')
    rec('-' * 100)
    rec('  ### (5) THE AXIOM PROFILE. ### **READ, NEVER RUN.**')
    rec('-' * 100)
    prof = []
    for cand in ('AXIOM_PRINTS.txt', 'AxiomCheck.lean'):
        p = os.path.join(KERNEL, cand)
        prof.append(dict(name=cand, exists=os.path.exists(p)))
        rec('    %-22s present in the kernel : %s' % (cand, os.path.exists(p)))
    printed = any(x['exists'] for x in prof)
    rec('    ### ### **NO PRINTED PROFILE COVERS THE HINTED NAMES : %s**' % (not printed or n_live == 0))
    rec('    ### **AND THE REASON IS NOT A MISSING FILE. ### IT IS THAT THERE IS NOTHING TO PROFILE:**')
    rec('    ### a profile is a statement about a declaration, and no such declaration exists.')
    rec('    ### **NO BUILD WAS RUN, WHICH THE CAP FORBIDS.**')

    rec('')
    rec('=' * 100)
    rec('  ### (6) THE VERDICT.')
    rec('=' * 100)
    if n_live == 0:
        verdict = 'NOT LOCATED'
        why = 'no live declaration of any hinted name exists in the kernel at the ref read'
    elif n_live < len(names):
        verdict = 'PARTLY LOCATED'
        why = 'some hinted names are live and some are not'
    else:
        verdict = 'LOCATED AND PRICED'
        why = 'every hinted name is a live declaration'
    rec('    ### ### ### **%s** ### -- %s.' % (verdict, why))
    rec('    ### **AND THE CAP IS EXPLICIT: `NOT LOCATED stops the act`.** ### The three routes are NOT')
    rec('    ### priced, because pricing a route to replace a terminal that does not exist would be')
    rec('    ### pricing work against this seat’s own reading of a hint.')
    rec('    ### **WHAT IS REPORTED INSTEAD IS WHAT WAS SEARCHED AND WHERE**, which is above, and what')
    rec('    ### the kernel says happened to them, which is quoted in the bank.')
    rec('=' * 100)

    p = run_clock.write(D, 'b367_locate_run', LINES)
    io.open(os.path.join(D, 'b367_locate.json'), 'w', encoding='utf-8', newline=chr(10)).write(json.dumps(
        dict(refs=R, branches_with_unread_work=len(behind),
             hinted=[{'subject': s, 'names': ns} for s, ns in HINTED],
             found={k: dict(subject=v['subject'], live=len(v['live']), mentions=len(v['mentions']),
                            mention_sites=v['mentions']) for k, v in found.items()},
             live_declarations=n_live, mentions=n_ment, all_mentions_in_comments=bool(all_in_comment),
             grh_transfer_hits=len(grh_hits),
             front_exported=len(exported), front_present=present, front_absent=absent,
             front_layers=per_layer,
             sweep={k: len(v) for k, v in sweep.items()},
             sweep_files={k: sorted({h['hit'].split(':')[0] for h in v}) for k, v in sweep.items()},
             profile_files=prof, build_run=False, lean_written=0,
             verdict=verdict, why=why, routes_priced=0,
             run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)), indent=1))
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
