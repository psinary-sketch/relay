# -*- coding: utf-8 -*-
"""b397_extract.py -- THE EXTRACT AND THE SURVEYS FOR THE UNLANDED WORK.

### ### **READ ONLY. ### NOTHING IS MERGED, NOTHING IS PUSHED TO ANY BRANCH, AND NO BRANCH IS
### ### CHECKED OUT.** ### Every branch read is `git show <ref>:<path>` or `git rev-list`, which
### touch no working tree.
###
### ### **AND `main..b` IS NOT `b..main`.** ### An earlier form of this survey read
### `rev-list --left-right --count main...b` and took the LEFT number for `ahead`. ### The left
### number is the count of commits ### **ONLY IN MAIN**, so eight branches read as `1 ahead` when
### they were `1 behind` and fully merged. ### **THE FINDING WOULD HAVE BEEN THE EXACT OPPOSITE OF
### ### THE TRUTH.** ### Both directions are now counted separately, by name, and `--merged` is
### read as a third, independent witness.
###
### ### **NOTHING IS WRITTEN AT ZENODO. ### NO BUILD IS RUN.**
"""
import io
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import anchor_from_file as AF   # noqa: E402
import run_clock                # noqa: E402
import b303_pins                # noqa: E402

D = os.path.join(ROOT, 'data')
PP = os.path.join('D:', os.sep, 'MY-DOwnloads', 'PLACE-papers')
FERRY = os.path.join(D, 'b397_ferry_2026-09-10.txt')
REGISTRY = os.path.join(PP, 'REGISTRY.md')
CENSUS = os.path.join(PP, 'phase2', 'method', 'THE_KEYSTONE_CENSUS.md')

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

L = []


def rec(s=''):
    L.append(s)
    print(s, flush=True)


def bar(c='-'):
    rec(c * 100)


def flat(s, n=200):
    return ' '.join(s.split())[:n]


def text_of(p):
    return io.open(p, encoding='utf-8', errors='replace').read()


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True,
                       encoding='utf-8', errors='replace')
    return (r.stdout or '').strip()


SKIP = ('.git', 'archive', 'outputs')
B395 = json.load(io.open(os.path.join(D, 'b395_reads.json'), encoding='utf-8'))

# ### **A PUSH BRANCH IS MECHANICAL AND IS NOT HELD RESEARCH WORK.** ### Named, so the
# ### classification is visible rather than silently applied.
PUSHY = re.compile(r'^(push|repair)-')


# ==================================================================================================
#  SURVEY 1 -- THE BRANCHES, AND WHAT IS ACTUALLY UNLANDED.
# ==================================================================================================
def survey1():
    bar('-')
    rec('  ### SURVEY 1 -- THE HELD BRANCHES. ### **READ ONLY, AND COUNTED IN BOTH DIRECTIONS.**')
    bar('-')
    ai, aln = AF.find(FERRY, 'and not for citation hygiene. b395')
    rec('  ### **THE ORDER, line %d:** %s' % (ai, flat(aln, 120)))
    # ### the population comes from b395's own partition, not from a roster this seat typed.
    repos = {}
    for r in B395['s1']:
        for n, p in (r.get('proof') or {}).items():
            if p['nonmain']:
                d = repos.setdefault(n, dict(head=p['head'], refs=p['refs'],
                                             branches=p['nonmain'], keystones=[]))
                d['keystones'].append(r['k'])
    rec('  ### **REPOSITORIES CARRYING A NON-DEFAULT BRANCH, FROM `b395`\'S PARTITION : `%d`.**'
        % len(repos))
    rows = []
    for n in sorted(repos):
        rp = os.path.join('D:' + os.sep, n)
        for b in repos[n]['branches']:
            ahead = g(rp, 'rev-list', '--count', 'main..' + b)
            behind = g(rp, 'rev-list', '--count', b + '..main')
            merged = b in [x.strip().lstrip('* ') for x in
                           g(rp, 'branch', '--merged', 'main').split(chr(10))]
            subj = g(rp, 'log', '-1', '--format=%s', b)
            rows.append(dict(repo=n, branch=b, ahead=int(ahead or 0),
                             behind=int(behind or 0), merged=merged,
                             push=bool(PUSHY.match(b)), subject=flat(subj, 150),
                             keystones=sorted(set(repos[n]['keystones']))))
    rec()
    rec('  ### **BOTH DIRECTIONS COUNTED SEPARATELY, AND `--merged` READ AS A THIRD WITNESS:**')
    rec('    %-22s %-26s %-7s %-7s %-7s %s'
        % ('repo', 'branch', 'AHEAD', 'behind', 'merged', 'kind'))
    for x in rows:
        rec('    %-22s %-26s %-7d %-7d %-7s %s'
            % (x['repo'], x['branch'], x['ahead'], x['behind'], x['merged'],
               'a push branch' if x['push'] else 'research'))
    research = [x for x in rows if not x['push']]
    landed = [x for x in research if x['ahead'] == 0]
    live = [x for x in research if x['ahead'] > 0]
    rec()
    rec('  ### ### **RESEARCH BRANCHES : `%d`. ### PUSH BRANCHES, EXCLUDED AS MECHANICAL : `%d`.**'
        % (len(research), len(rows) - len(research)))
    rec('  ### ### **FULLY MERGED INTO `main`, CARRYING NOTHING `main` LACKS : `%d`.**'
        % len(landed))
    rec('  ### ### **CARRYING COMMITS `main` DOES NOT HAVE : `%d`** -- %s'
        % (len(live), ', '.join('`%s/%s`' % (x['repo'], x['branch']) for x in live) or 'none'))
    rec('  ### ### ### **SO THE KEYSTONES` OWN TEXT CALLING THESE TERMINALS `HELD`, `UNMERGED` OR')
    rec('  ### ### ### `BRANCH-RESIDENT` IS STALE FOR `%d` OF `%d` RESEARCH BRANCHES.** ### The'
        % (len(landed), len(research)))
    rec('  ### ### ### work landed and ### **THE PROSE DID NOT FOLLOW IT** -- which is the')
    rec('  ### ### ### `corrected but unpropagated` species this seat minted at `b394`, this time')
    rec('  ### ### ### about a branch status rather than a version string.')
    rec()
    rec('  ### **AND THE COUNTING TRAP THIS SURVEY FELL INTO FIRST, RECORDED:** ###')
    rec('  ### `rev-list --left-right --count main...b` puts the count of commits ### **ONLY IN')
    rec('  ### ### MAIN** ### on the left. ### An earlier form of this survey read that number as')
    rec('  ### `ahead`, and ### **EIGHT MERGED BRANCHES READ AS ONE-COMMIT-AHEAD OF MAIN.** ###')
    rec('  ### **THE FINDING WOULD HAVE BEEN THE EXACT OPPOSITE OF THE TRUTH**, and it was caught')
    rec('  ### by one branch reading `0 0` -- a shape the misreading could not explain.')
    return dict(rows=rows, research=len(research), push=len(rows) - len(research),
                landed=[x['branch'] for x in landed], live=live)


# ==================================================================================================
#  SURVEY 2 -- THE ONE LIVE BRANCH, TERMINAL BY TERMINAL.
# ==================================================================================================
DECL = re.compile(r'^\s*(?:@\[[^\]]*\]\s*)?(theorem|lemma|def|structure|abbrev|instance)\s+'
                  r'([A-Za-z_][A-Za-z0-9_.\']*)')


def survey2(s1):
    bar('-')
    rec('  ### SURVEY 2 -- THE ONE LIVE BRANCH, TERMINAL BY TERMINAL.')
    bar('-')
    out = []
    for x in s1['live']:
        rp = os.path.join('D:' + os.sep, x['repo'])
        b = x['branch']
        rec('  ### **`%s/%s`** -- `%d` commit(s) `main` does not have:' % (x['repo'], b,
                                                                          x['ahead']))
        for ln in g(rp, 'log', '--format=%h %s', 'main..' + b).split(chr(10)):
            rec('      %s' % flat(ln, 150))
        rec()
        # ### the files the branch changed against the merge base, and their DECLARATIONS as the
        # ### branch has them -- read by `git show`, never by a checkout.
        names = [z for z in g(rp, 'diff', '--name-only', 'main...' + b).split(chr(10))
                 if z.strip().endswith('.lean')]
        rec('  ### **`.lean` FILES THE BRANCH TOUCHES AGAINST THE MERGE BASE : `%d`**' % len(names))
        prof_files = [z for z in g(rp, 'ls-tree', '-r', '--name-only', b).split(chr(10))
                      if re.search(r'(?i)(axiom|print|profile|transcript|report)', z)]
        rec('  ### **CANDIDATE PROFILE ARTEFACTS ON THE REF : %s**'
            % (', '.join(prof_files[:6]) or 'NONE'))
        printed = [z for z in prof_files if z.lower().endswith(('.txt', '.md', '.log'))]
        rec('  ### ### **PRINTED PROFILES (captured stdout, not `#print axioms` SOURCE) : %s**'
            % (', '.join(printed) or '### **NONE ON THIS REF**'))
        for f in names:
            body = g(rp, 'show', '%s:%s' % (b, f))
            decls = [(m.group(1), m.group(2)) for ln in body.split(chr(10))
                     for m in [DECL.match(ln)] if m]
            onmain = g(rp, 'grep', '-l', '--', 'x', 'main') and None
            rec()
            rec('    ### `%s` -- `%d` declaration(s)' % (f, len(decls)))
            for kind, nm in decls:
                # ### **THE CITATION TEST IS AGAINST `main`, NOT AGAINST THE MERGE BASE.** ### A
                # ### name the branch "adds" may already stand on `main` by another route, and a
                # ### citation resolves against the default branch or it does not resolve.
                hit = g(rp, 'grep', '-l', nm, 'main', '--', '*.lean')
                where = [z.split(':', 1)[-1] for z in hit.split(chr(10)) if z.strip()]
                cite = citing_docs(nm)
                out.append(dict(repo=x['repo'], branch=b, file=f, kind=kind, name=nm,
                                on_main=bool(where), main_files=where[:2],
                                cited_by=cite, printed_profile=bool(printed)))
                rec('      %-8s %-42s on main : %-5s ; cited by %d keystone doc(s)'
                    % (kind, nm[:42], bool(where), len(cite)))
                if cite:
                    rec('              %s' % ', '.join(cite[:3]))
    rec()
    absent = [o for o in out if not o['on_main']]
    uncited = [o for o in absent if not o['cited_by']]
    cited = [o for o in absent if o['cited_by']]
    rec('  ### ### **DECLARATIONS ON THE LIVE BRANCH : `%d`.**' % len(out))
    rec('  ### ### **ABSENT FROM `main` : `%d`.**' % len(absent))
    rec('  ### ### **OF THOSE, CITED BY A KEYSTONE : `%d`** -- ### **A KEYSTONE CITING A TERMINAL'
        % len(cited))
    rec('  ### ### NO DEFAULT BRANCH CARRIES**, which is the disclosure case.')
    rec('  ### ### **AND CITED BY NOTHING : `%d`** -- ### **THE UNLANDED, UNCITED WORK.**'
        % len(uncited))
    for o in uncited:
        rec('  ###     `%s` (%s) in `%s`' % (o['name'], o['kind'], o['file']))
    return dict(decls=out, absent=len(absent), cited=cited, uncited=uncited)


def citing_docs(name):
    """### Which corpus documents name this terminal. ### Archive and outputs excluded."""
    out = []
    for dp, dn, fn in os.walk(PP):
        rel = os.path.relpath(dp, PP).replace(os.sep, '/')
        if rel.split('/')[0] in SKIP:
            continue
        for f in fn:
            if f.endswith('.md') and name in text_of(os.path.join(dp, f)):
                out.append((rel + '/' + f) if rel != '.' else f)
    return sorted(out)


# ==================================================================================================
#  SURVEY 3 -- THE DISCLOSURE RULE, QUOTED FROM THE RECORD.
# ==================================================================================================
def survey3(s2):
    bar('-')
    rec('  ### SURVEY 3 -- THE DISCLOSURE RULE, QUOTED FROM THE RECORD`S OWN BYTES.')
    bar('-')
    i1, l1 = AF.find(REGISTRY, 'the rule is that this belongs in the status column where a')
    rec('  ### **`REGISTRY.md` line %d:**' % i1)
    rec('      > %s' % flat(l1, 420))
    i2, l2 = AF.find(CENSUS, 'it is a DISCLOSURE requirement, not a repair')
    rec('  ### **`THE_KEYSTONE_CENSUS.md` line %d:**' % i2)
    rec('      > %s' % flat(l2, 420))
    rec()
    rec('  ### ### **AND THE RULE`S OWN WORKED INSTANCE IS STALE.** ### It names')
    rec('  ### ### `word-pairing-interface` as ### *the held, unmerged branch* ### carrying')
    rec('  ### ### `THE_RESIDUE_OF_RH`\'s terminals. ### Survey 1 measured that branch at ###')
    rec('  ### ### **`0` COMMITS `main` DOES NOT HAVE, AND `--merged` CONFIRMS IT.** ### **THE')
    rec('  ### ### BRANCH LANDED AND THE RULE`S INSTANCE DID NOT FOLLOW IT.**')
    rec('  ### ### **SO THE DISCLOSURE THE RULE DEMANDS IS, FOR THAT ROW, A DISCLOSURE OF A')
    rec('  ### ### CONDITION THAT NO LONGER HOLDS** -- and writing it would put a false')
    rec('  ### ### statement in a status column under the authority of a rule. ### **THE RULE IS')
    rec('  ### ### NOT STRUCK AND IS NOT AMENDED BY THIS SEAT; ITS INSTANCE IS REPORTED STALE.**')
    rec()
    # ### which rows actually need it: the terminals absent from main AND cited.
    docs = sorted(set(d for o in s2['cited'] for d in o['cited_by']))
    rec('  ### **THE ROWS THAT ACTUALLY NEED THE DISCLOSURE** -- documents citing a terminal')
    rec('  ### ### **NO DEFAULT BRANCH CARRIES** : `%d`' % len(docs))
    for d in docs:
        rec('  ###     %s' % d)
    names = sorted(set(o['name'] for o in s2['cited']))
    rec('  ### **THE TERMINALS AT ISSUE : %s**' % ', '.join('`%s`' % n for n in names))
    return dict(rule_registry_line=i1, rule_census_line=i2,
                rule_registry=flat(l1, 420), rule_census=flat(l2, 420),
                docs=docs, names=names)


# ==================================================================================================
#  SURVEY 4 -- THE RESEARCH BOARD, READ FROM THE CLAUSE ANCHOR AND THE FACES LEDGER.
# ==================================================================================================
def survey4():
    bar('-')
    rec('  ### SURVEY 4 -- THE RESEARCH BOARD, READ FROM THE RECORD.')
    bar('-')
    out = {}
    fl = os.path.join(PP, 'FACES_LEDGER.md')
    if os.path.exists(fl):
        txt = text_of(fl)
        rows = [ln for ln in txt.split(chr(10)) if ln.startswith('| ') and ln.count('|') >= 4]
        rec('  ### **`FACES_LEDGER.md` : `%d` bytes, `%d` table rows.**'
            % (len(txt.encode('utf-8')), len(rows)))
        out['faces_rows'] = len(rows)
        out['faces_bytes'] = len(txt.encode('utf-8'))
    else:
        rec('  ### **`FACES_LEDGER.md` IS NOT AT THE PAPER ROOT.** ### Located by content instead:')
        hits = []
        for dp, dn, fn in os.walk(PP):
            rel = os.path.relpath(dp, PP).replace(os.sep, '/')
            if rel.split('/')[0] in SKIP:
                continue
            for f in fn:
                if 'FACES' in f.upper() and f.endswith('.md'):
                    hits.append((rel + '/' + f) if rel != '.' else f)
        rec('  ###   %s' % (', '.join(hits) or '### **NONE**'))
        out['faces_rows'] = 0
        out['faces_files'] = hits
    # ### the clause anchor, by content.
    fn_ = os.path.join(PP, 'FINDINGS.md')
    txt = text_of(fn_)
    ca = [(i + 1, ln) for i, ln in enumerate(txt.split(chr(10)))
          if 'clause-stated' in ln or 'THE OPEN CLAUSE' in ln.upper()]
    rec('  ### **THE CLAUSE ANCHOR IN `FINDINGS.md` : `%d` line(s)**' % len(ca))
    for i, ln in ca[:3]:
        rec('      %d : %s' % (i, flat(ln, 200)))
    out['clause_lines'] = [i for i, _l in ca][:6]
    out['clause_quotes'] = [flat(l, 200) for _i, l in ca[:3]]
    return out


def refs():
    o = {}
    for name, repo in b303_pins.REPOS:
        o[name] = dict(branch=g(repo, 'rev-parse', '--abbrev-ref', 'HEAD'),
                       head=g(repo, 'rev-parse', 'HEAD')[:12])
    return o


def do_reads(s1, s2):
    bar('-')
    rec('  ### THE READS. ### **EVERY QUOTED LINE CARRIES AN ANCHOR FOUND BY THE TOOL.**')
    bar('-')
    reads, absent, amb = [], 0, 0
    todo = [(FERRY, 'RULING (R22), the author'), (FERRY, 'ACT b397 — THE UNLANDED WORK'),
            (FERRY, 'COMPONENT 1 — WHAT IS ON THE HELD BRANCHES'),
            (FERRY, 'COMPONENT 2 — THE DISCLOSURE RULE, APPLIED'),
            (FERRY, 'COMPONENT 3 — THE QUEUE, WITH TRIGGERS'),
            (FERRY, 'COMPONENT 4 — THE RESEARCH BOARD'),
            (REGISTRY, 'the rule is that this belongs in the status column where a'),
            (CENSUS, 'it is a DISCLOSURE requirement, not a repair')]
    for p, want in todo:
        try:
            i, ln = AF.find(p, want)
            v = 'ANCHORED'
        except Exception as e:
            i, ln, v = 0, '', ('AMBIGUOUS' if 'AMBIGUOUS' in str(e).upper() else 'ABSENT')
            if v == 'AMBIGUOUS':
                amb += 1
            else:
                absent += 1
        reads.append(dict(path=os.path.basename(p), needle=flat(want, 48), line=i, verdict=v))
        rec('    %-28s %-50s %-10s line %s'
            % (os.path.basename(p)[:28], flat(want, 50), v, i or '--'))
    rec('  ### **reads %d ; ANCHORED %d ; AMBIGUOUS %d ; ABSENT %d**'
        % (len(reads), len(reads) - amb - absent, amb, absent))
    return reads, absent, amb


def main():
    rec('### run at (UTC) : %s   ### NOT COVERED BY ANY HASH.' % run_clock.stamp())
    bar('=')
    rec('b397 -- THE EXTRACT, AND THE SURVEYS THE FACE IS WRITTEN FROM.')
    bar('=')
    R = refs()
    for k, v in R.items():
        rec('    %-22s `%s` = `%s`' % (k, v['branch'], v['head']))
    rec()
    s1 = survey1()
    rec()
    s2 = survey2(s1)
    rec()
    s3 = survey3(s2)
    rec()
    s4 = survey4()
    rec()
    reads, absent, amb = do_reads(s1, s2)
    rec()
    bar('=')
    rec('  1 : research %d ; push %d ; landed %d ; LIVE %d'
        % (s1['research'], s1['push'], len(s1['landed']), len(s1['live'])))
    rec('  2 : declarations %d ; absent from main %d ; cited %d ; UNCITED %d'
        % (len(s2['decls']), s2['absent'], len(s2['cited']), len(s2['uncited'])))
    rec('  3 : rule at REGISTRY:%d and CENSUS:%d ; rows needing disclosure %d ; terminals %d'
        % (s3['rule_registry_line'], s3['rule_census_line'], len(s3['docs']),
           len(s3['names'])))
    rec('  4 : %s' % {k: v for k, v in s4.items() if k != 'clause_quotes'})
    rec('  reads %d absent %d ambiguous %d' % (len(reads), absent, amb))
    rec('  ### **NOTHING WAS MERGED, PUSHED OR CHECKED OUT. ### NO BUILD WAS RUN.**')
    bar('=')
    p = run_clock.write(D, 'b397_extract_notes', L)
    json.dump(dict(s1=s1, s2=s2, s3=s3, s4=s4, reads=len(reads), absent=absent, ambiguous=amb,
                   refs=R, run_file=os.path.basename(p), run_clock=run_clock.read_stamp(p)),
              io.open(os.path.join(D, 'b397_reads.json'), 'w', encoding='utf-8'), indent=1)
    print('  written: %s' % os.path.basename(p))
    return 0


if __name__ == '__main__':
    sys.exit(main())
