"""b714 -- THE COMPONENTS BANK'S STAND-IN, step [18] of the close (standing clauses v5 row (79)). UNSEALED; written after the seal on the
author's word at step [18] (relay data/b714_events.txt (7)).

The sealed route (tools/b714_record.py components, :2630-:2656) is b713's composer carried unrewritten and raised on worklist key C1_PP_FACES
(data/b714_events.txt (5)). This tool writes data/b714_components.txt alone, in the shape of b713's bank (relay 2f76d11c,
data/b713_components.txt): a head line, then one line per COMPONENT 0 to 6, the pilot on its own line beside Component 4. Every figure is read:
  - each component's commits from data/b714_steps.json by step row (its phase), and its banks from the files those commits carry (git show);
  - each N and S reading from the scores bank as written once (data/b714_scores.json), placed on the line of the first component whose banks
    its own reading names, the rest on Component 6's;
  - Component 6's entry and trail lines and the root from data/b714_findings.json, data/b714_trail.json and data/b714_act_root.json.
Before it writes, the membrane's reading for the bank under b714's own exclusion pattern is printed; where the membrane refuses, nothing is
written. After it writes, the bank's sha256 and this tool's are printed.
usage: python -X utf8 tools/b714_components_standin.py [dry]
"""
import hashlib
import json
import os
import re
import subprocess
import sys

T = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(T)
D = os.path.join(ROOT, 'data')
sys.path.insert(0, T)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
import b714_worklist as K          # noqa: E402

ACT = 'b714'
NL = '\n'
BANK = os.path.join(D, '%s_components.txt' % ACT)
# ### the components by the step bank's phases (tools/b714_record.py PRE_SEAL_PHASES and POST_SEAL_PHASES); the pilot on its own line
COMPONENTS = (('COMPONENT 0', ('step zero',)), ('COMPONENT 1', ('component 1',)), ('COMPONENT 2', ('component 2',)),
              ('COMPONENT 3', ('component 3',)), ('COMPONENT 4', ('component 4',)), ('THE PILOT', ('pilot',)),
              ('COMPONENT 5', ('component 5', 'gate', 'seal')), ('COMPONENT 6', ('pre-root', 'root')))
REPO = dict(relay=ROOT, pp=K.PP)
SCORE_KEYS = ('N1', 'N2', 'N3', 'N4', 'N5', 'S1', 'S2', 'S3')


def jl(name):
    p = os.path.join(D, name)
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest() if os.path.exists(p) else None


def files_of(repo, commit):
    """the files a commit changes against its first parent (a merge's own files: `git show` prints none for a merge)."""
    r = subprocess.run(['git', '-C', REPO[repo], 'diff', '--name-only', commit + '^1', commit], capture_output=True)
    return [x for x in r.stdout.decode('utf-8', 'replace').replace('\r', '').split(NL) if x.strip()]


def banks_of(repo, commit):
    """the banks a commit carries: relay's data/ files less the step bank itself; PLACE-papers' files by name."""
    fs = files_of(repo, commit)
    if repo == 'relay':
        return [f for f in fs if f.startswith('data/') and f != 'data/%s_steps.json' % ACT]
    return ['PLACE-papers ' + f for f in fs]


def lines():
    rows = jl('%s_steps.json' % ACT).get('rows') or []
    sc = jl('%s_scores.json' % ACT)
    fj, tj, rj = jl('%s_findings.json' % ACT), jl('%s_trail.json' % ACT), jl('%s_act_root.json' % ACT)
    comp = []
    for name, phases in COMPONENTS:
        cs = [(i + 1, r) for i, r in enumerate(rows) if r.get('phase') in phases]
        banks = []
        for _n, r in cs:
            for b in banks_of(r['repo'], r['commit']):
                if b not in banks:
                    banks.append(b)
        comp.append((name, phases, cs, banks))
    placed = {}
    for k in SCORE_KEYS:
        v = sc.get(k) or ['NOT IN THE SCORES BANK', '']
        named = set('data/' + m for m in re.findall(r'data/(b714_[\w.-]+)', str(v[1])))
        at = next((name for name, _p, _c, banks in comp if named & set(banks)), 'COMPONENT 6')
        placed.setdefault(at, []).append('%s %s' % (k, v[0]))
    out = []
    for name, phases, cs, banks in comp:
        commits = ' ; '.join('step row %d %s %s (%s)' % (n, r['repo'], r['commit'][:8], r['phase']) for n, r in cs) or 'NO STEP ROW'
        extra = ''
        if name == 'COMPONENT 6':
            extra = ' ; FINDINGS :%s ; the root %s ; OPEN_TRAILS :%s ; the mirror after the root' % (
                fj.get('entry_line'), (rj.get('root') or '### NOT COMPUTED')[:16], tj.get('line'))
        out.append('### %s : %s ; the banks they carry (%d): %s%s ; %s' % (
            name, commits, len(banks), ', '.join(banks) or 'NONE', extra, ' ; '.join(placed.get(name, [])) or 'no score reading names these banks'))
    head = ('%s -- THE COMPONENTS, BANKED UNDER (R324). Written by a stand-in tool (tools/b714_components_standin.py, unsealed) because the sealed '
            'route (tools/b714_record.py :2630-:2656) is b713`s composer carried unrewritten, and raised on worklist key C1_PP_FACES, which b714`s '
            'worklist does not carry (relay data/b714_events.txt (5), the author`s word at step [18] (7)).' % ACT)
    return [head, ''] + out, placed


def membrane():
    import act_membrane as MEM
    import b714_record as REC
    ex = REC.R.ROOT_EXCLUDE
    base = os.path.basename(BANK)
    print('### THE MEMBRANE`S READING for data/%s under b714`s own exclusion pattern (tools/b714_record.py R.ROOT_EXCLUDE):' % base)
    print('###   the pattern %s' % (ex.pattern if ex is not None else 'NONE'))
    print('###   the bank matched by the pattern (no root item): %s' % bool(ex is not None and ex.match(base)))
    print('###   the act`s root appended: %s' % (MEM.appended(ACT)[:28] or 'NO'))
    print('###   a bank the root names: %s' % MEM.named(base, ex))
    r = MEM.refuses(ACT, base, ex)
    print('###   the membrane: %s' % (r or 'PASSES -- the write may proceed'))
    return r, MEM, ex


def main():
    L, placed = lines()
    dry = 'dry' in sys.argv[1:]
    r, MEM, ex = membrane()
    if dry:
        print(NL.join(L))
        print('### DRY: nothing written')
        return 0
    if r:
        print('### ### **THE MEMBRANE REFUSES -- NOTHING WRITTEN.**')
        return 4
    if os.path.exists(BANK):
        print('### data/%s EXISTS -- NOTHING WRITTEN TWICE' % os.path.basename(BANK))
        return 3
    MEM.guard_path(ACT, BANK, ex)
    with open(BANK + '.tmp', 'wb') as fh:
        fh.write((NL.join(L) + NL).encode('utf-8'))
    os.replace(BANK + '.tmp', BANK)
    print(NL.join(L))
    print('### written: data/%s ; sha256 %s' % (os.path.basename(BANK), sha(BANK)))
    print('### the tool: tools/%s ; sha256 %s' % (os.path.basename(__file__), sha(os.path.abspath(__file__))))
    return 0


if __name__ == '__main__':
    sys.exit(main())
