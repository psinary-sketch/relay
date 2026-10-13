# -*- coding: utf-8 -*-
"""b666_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b666's step zero; and the ferry banked
after it. Carried from tools/b665_citation.py: the helpers unchanged, the constants and the rows b666's.

### Before the ferry is banked, every path, line, bank, branch, tag, tool and named rule the ruling (R276) and the ferry cite is checked for
### existence at HEAD and the misses printed; a miss is raised to the author before the component that cites it runs, not repaired silently;
### the print is banked as data/b666_citation_check.txt and read by the suite.
### The ruling and ferry are read from the session transcript (the user line carrying 'RULING (R276) BEGIN'), never from a scratch copy.
### Each cite is a row: (where it is cited, what is cited, the check, the component that cites it). Figures the ruling states about prior
### banks are checked against those banks as well.
### Routes: `python tools/b666_citation.py check` -> data/b666_citation_check.txt (.json);
###         `python tools/b666_citation.py ferry`  -> data/b666_ferry.txt and data/b666_ferry_scan.txt (ferry_scan.py's output, captured).
### Written by the Write tool at b666; this tool writes only the four banks named above.
"""
import io
import json
import os
import re
import subprocess
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
EF = 'D:/SIDE-explicit-formula'
KD = 'D:/SIDE-cosmo'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/96a5c4ea-0b59-4b9b-bbd4-bf76d508ffdf.jsonl'
ANCHOR, TAIL = 'RULING (R276) BEGIN', 'FERRY END (part 1 of 1)'
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')


def g(repo, *a):
    r = subprocess.run(['git', '-C', repo] + list(a), capture_output=True, text=True, encoding='utf-8', errors='replace')
    return r.returncode, r.stdout.replace(chr(13), '')


def rd(p):
    return io.open(p, encoding='utf-8', errors='replace').read().replace(chr(13), '') if os.path.exists(p) else None


def line(p, n):
    t = rd(p)
    ls = t.split(NL) if t is not None else []
    return ls[n - 1] if 0 < n <= len(ls) else None


def ferry_text():
    """the ruling and the ferry as pasted: the last user line of the session carrying the anchor, from the anchor to the ferry's end."""
    best = None
    for raw in io.open(SESSION, encoding='utf-8', errors='replace'):
        if ANCHOR not in raw:
            continue
        try:
            o = json.loads(raw)
        except ValueError:
            continue
        if o.get('type') != 'user' or o.get('isCompactSummary'):
            continue
        cs = (o.get('message') or {}).get('content')
        texts = [cs] if isinstance(cs, str) else [c.get('text', '') for c in (cs or []) if isinstance(c, dict) and c.get('type') == 'text']
        for t in texts:
            i, j = t.find(ANCHOR), t.find(TAIL)
            if i >= 0 and j > i:
                best = t[i:j + len(TAIL)].replace(chr(13), '')
    if best is None:
        sys.exit('### THE RULING IS NOT A USER LINE OF THIS SESSION -- NOTHING WRITTEN')
    return best


def commit_in(repo, sha):
    rc, _o = g(repo, 'cat-file', '-e', sha + '^{commit}')
    return rc == 0


def branch_listed(repo, b):
    rc, o = g(repo, 'branch', '--list', b)
    return bool(o.strip())


def rule_clause(rule, clauses):
    """a named rule's clauses in the ferry bank that carries its ruling."""
    for f in sorted(os.listdir(D)):
        if f.endswith('_ferry.txt'):
            t = rd(os.path.join(D, f))
            if t and ('RULING (%s) BEGIN' % rule) in t:
                body = t[t.index('RULING (%s) BEGIN' % rule):]
                return all(('(%d)' % c) in body for c in clauses), 'data/%s' % f
    return False, 'no ferry bank carries RULING (%s)' % rule


def act_root_line(act):
    t = rd(os.path.join(D, 'act_roots.txt')) or ''
    ls = [l.split() for l in t.split(NL) if l.strip()]
    return [l for l in ls if l[0] == act]


def jload(name):
    try:
        return json.load(io.open(os.path.join(D, name), encoding='utf-8'))
    except Exception:
        return {}


def grep_line(path, pat):
    t = rd(path) or ''
    for i, l in enumerate(t.split(NL), 1):
        if re.search(pat, l):
            return i, l.strip()
    return None, None


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    # ### the banks the read-first names
    for f in ('data/b665_closing.txt', 'data/b665_defects.txt', 'data/b647_table_kernels.txt', 'data/b647_table_SIDE-cosmo.txt',
              'data/b649_axiom_claim_rows.txt', 'data/b657_sentence_grades.txt', 'data/b665_closing_push_out.txt'):
        add('ferry read-first', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-3')
    dft = rd(p('data', 'b665_defects.txt')) or ''
    letters = re.findall(r"^    \(([a-z])\) THE ([\w']+)", dft, re.M)
    add('ruling (1)', '"five defects, all the seat`s"', len(letters) == 5 and all(w == "SEAT'S" for _l, w in letters),
        'data/b665_defects.txt rows: %s' % ', '.join('(%s) %s' % x for x in letters), '1')
    # ### b665 at its weight
    cl = rd(p('data', 'b665_closing.txt')) or ''
    add('ruling (1)', 'relay 0ff929e0, PLACE-papers a708de2', commit_in(ROOT, '0ff929e0') and commit_in(PP, 'a708de2') and 'PLACE-papers a708de2' in cl,
        'git cat-file; the closing`s head prints "%s"' % cl.split(NL)[0][:90], '1')
    add('ruling (1)', 'SIDE-explicit-formula 02bc85d, tag v0.30', g(EF, 'rev-parse', '--short=7', 'v0.30^{commit}')[1].strip() == '02bc85d', 'v0.30 peeled', '1')
    for n, needle in ((8589, 'b664 AT ITS WEIGHT'), (8591, 'The Keiper finite-n equality')):
        l = line(os.path.join(PP, 'FINDINGS.md'), n) or ''
        add('ruling (1)', 'FINDINGS :%d' % n, needle in l, l[:90], '1')
    for n, needle in ((14216, 'W-ORD-FT-FIRST-ORDER DISCHARGED'), (14218, '### b665')):
        l = line(os.path.join(PP, 'OPEN_TRAILS.md'), n) or ''
        add('ruling (1)', 'OPEN_TRAILS :%d' % n, needle in l, l[:90], '1')
    rl = act_root_line('b665')
    add('ruling (1)', 'root cf08faff...', rl and rl[0][1].startswith('cf08faff'), 'data/act_roots.txt b665 line', '1')
    ck = rd(p('data', 'b665_checks_postpush.txt')) or ''
    add('ruling (1)', 'suite 79 of 80, the SIDE-cosmo row alone declared', 'LIVE PASSING : 79' in ck and "LIVE FAILING : 1 ['G-AXIOM-CLAIM']" in ck,
        'data/b665_checks_postpush.txt', '1')
    ctl = rd(p('data', 'b665_keiper_control.txt')) or ''
    add('ruling (1)', 'H3 at 12 of 12, two planted wrong bindings refused', 'KEIPER AGREES AT 12 OF 12' in ctl and 'IT HAS.' in ctl,
        'data/b665_keiper_control.txt', '1')
    add('ruling (1)', 'K4 (GammaRZetaValues) open since b641, listed', 'K4, GammaRZetaValues' in cl, 'data/b665_closing.txt CARRIED FORWARD (b)', '1')
    face = rd(p('data', 'b665_registration_2026-10-13.txt')) or ''
    add('ruling (1)', 'the five declared readings, as the face states them', all(('(%s)' % r) in face for r in ('i', 'ii', 'iii', 'iv', 'v')),
        'data/b665_registration_2026-10-13.txt section (A): readings (i)-(viii) on the face; the ruling`s five are (i) the two dispatches, (ii) the '
        'rounding margin, (iii) the uncompiled η-form, (iv) the unreached Stieltjes clause, (v) the shared-additive bank', '1')
    # ### the kernel at the tie
    kt = rd(p('data', 'b647_table_kernels.txt')) or ''
    rows_ = re.findall(r'^  (SIDE-\S+)\s+(\w+) \|\s+\d+ \|\s+\d+ \|\s+\d+ \|\s+(\d+) \|', kt, re.M)
    done = ('SIDE-kernel', 'SIDE-global-section', 'SIDE-lv-conservation', 'SIDE-structural-error-correction', 'SIDE-carrier-spec', 'SIDE-effects')
    rest = sorted(((int(n), k) for k, _rev, n in rows_ if k not in done), reverse=True)
    top = [k for n, k in rest if rest and n == rest[0][0]]
    add('ruling (2)', 'two kernels at 6 OVERREACHES, SIDE-grh-transfer and SIDE-cosmo', rest and rest[0][0] == 6 and sorted(top) == ['SIDE-cosmo', 'SIDE-grh-transfer'],
        'data/b647_table_kernels.txt :%s (SIDE-cosmo), :%s (SIDE-grh-transfer); after the six cut, the top count %s held by %s; next %s' % (
            grep_line(p('data', 'b647_table_kernels.txt'), r'^  SIDE-cosmo ')[0], grep_line(p('data', 'b647_table_kernels.txt'), r'^  SIDE-grh-transfer ')[0],
            rest[0][0] if rest else '?', top, [(k, n) for n, k in rest[len(top):len(top) + 3]]), '2')
    f665 = rd(p('data', 'b665_registration_2026-10-13.txt')) or ''
    add('ruling (2)', 'the kernel carrying a declared suite failure', 'SIDE-cosmo SIDECosmo/SteaneExemplar.lean:6 (knill_laflamme_t1)' in f665,
        'b665`s face declares G-AXIOM-CLAIM on SIDE-cosmo SteaneExemplar.lean:6; SIDE-grh-transfer carries none', '2')
    al, alt = grep_line(os.path.join(PP, 'OPEN_TRAILS.md'), r'THE ALTERNATION OF RESEARCH AND RE-CUT ACTS')
    add('ruling (2)', 'the alternation on OPEN_TRAILS', al, 'OPEN_TRAILS :%s (b654, (R264)(2))' % al, '1')
    k47 = rd(p('data', 'b647_table_SIDE-cosmo.txt')) or ''
    ids = sorted(set(re.findall(r'^  (SIDE-cosmo@c5cba30:\S+) \| OVERREACHES', k47, re.M)))
    nb = len(ids)
    add('ferry read-first', 'SIDE-cosmo`s b647 bank (rows are blocks)', nb == 6,
        'data/b647_table_SIDE-cosmo.txt: %d distinct OVERREACHES blocks read at c5cba30 (each listed in the non-matches section and again in the '
        'full table): %s' % (nb, ', '.join(i.split(':', 1)[1] for i in ids)), '2')
    ax = rd(p('data', 'b649_axiom_claim_rows.txt')) or ''
    n9, l9 = grep_line(p('data', 'b649_axiom_claim_rows.txt'), r'source\s+: SIDE-cosmo/SIDECosmo/SteaneExemplar.lean:6')
    add('ruling (2)', 'the axiom-claim bank`s SteaneExemplar :6 row', n9 and 'ROW 1' in ax, 'data/b649_axiom_claim_rows.txt :%s (ROW 1, OVERREACHES, its licensed '
        'cell at :%s)' % (n9, grep_line(p('data', 'b649_axiom_claim_rows.txt'), r'licensed : knill_laflamme_t1')[0]), '2')
    rc, km = g(KD, 'rev-parse', '--short=7', 'main')
    add('ferry read-first; ruling (2)', 'the change banks for SIDE-cosmo since b647, if any', km.strip() == 'c5cba30',
        'main %s = b647`s read c5cba30: no change since, no change bank owed ((R267)(3) as written)' % km.strip(), '2')
    tc = line(os.path.join(KD, 'lean-toolchain'), 1) or ''
    add('ferry read-first', 'the kernel`s lean-toolchain and lakefile by line', tc and os.path.exists(os.path.join(KD, 'lakefile.toml')),
        'lean-toolchain :1 %s ; lakefile.toml :4 %s ; the mathlib rev :%s' % (tc.strip(), (line(os.path.join(KD, 'lakefile.toml'), 4) or '').strip(),
                                                                        grep_line(os.path.join(KD, 'lakefile.toml'), r'^rev = ')[0]), '3')
    add('ruling (2)', 'the workflow on its main where absent', not os.path.exists(os.path.join(KD, '.github', 'workflows', 'build-module.yml')),
        'build-module.yml absent at main (lean_action_ci.yml, create-release.yml, update.yml there; push-triggered)', '3')
    rc, tg = g(KD, 'tag', '--list')
    add('ruling (2)', 'the tag at the next patch step in its series', 'v0.3' in tg.split() and 'v0.3.1' not in tg.split(),
        'tags: %s ; v0.3 at %s ; main past it' % (' '.join(tg.split()), g(KD, 'rev-parse', '--short=7', 'v0.3^{commit}')[1].strip()), '3')
    for f in ('data/b657_sentence_grades.txt',):
        add('ferry read-first', '%s as the form' % f, os.path.exists(p(*f.split('/'))), 'exists', '2')
    # ### branches for step zero
    for repo, nm, b in ((ROOT, 'relay', 'push-b665'), (ROOT, 'relay', 'push-b665-root'), (ROOT, 'relay', 'push-b665-closing'),
                        (PP, 'PLACE-papers', 'push-b665'), (PP, 'PLACE-papers', 'push-b665-root'),
                        (EF, 'SIDE-explicit-formula', 'push-b665-merge'), (EF, 'SIDE-explicit-formula', 'keiper-b665')):
        add('ferry Component 0', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    # ### rules and tools
    for rule, cl_, comp in (('R265', (2, 3, 4), '2-3'), ('R267', (3,), '2'), ('R263', (4,), '3'), ('R251', (3,), '5'), ('R254', (2,), '0-5')):
        ok, how = rule_clause(rule, cl_)
        add('ruling (2); ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ruling (3)', 'the mirror export in the b655 form', all(os.path.exists(p('tools', f)) for f in ('mirror_build.ps1', 'mirror_verify.py')),
        'tools/mirror_build.ps1, tools/mirror_verify.py', '5')
    add('ruling (5)', 'b667 W-ORD-EPSTEIN-CERTIFY', 'W-ORD-EPSTEIN-CERTIFY' in (line(os.path.join(PP, 'OPEN_TRAILS.md'), 14158) or ''), 'OPEN_TRAILS :14158', '5')
    for f in ('tools/push_gated.sh', 'tools/act_root.py', 'tools/additive_shared.py', 'tools/ferry_scan.py', 'tools/licensed_table.py', 'tools/axiom_claim.py'):
        add('ferry', f, os.path.exists(p(*f.split('/'))), 'exists', '0-5')
    return R


def check(*a):
    text = ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b666 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662), RUN BEFORE THE FERRY IS BANKED (%s)' % time.strftime(
        '%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the source: the ruling and the ferry as pasted, read from the session transcript (%d characters, %r to %r); every cite checked at '
         'HEAD; rows are cites: where | what | OK or MISS | how | the component that cites it.' % (len(text), ANCHOR, TAIL), '']
    for where, what, ok, how, comp in R:
        L.append('  %-4s | %s | %s | %s | Component %s' % ('OK' if ok else 'MISS', where, what, how, comp))
    L += ['', '### THE MISSES, EACH RAISED TO THE AUTHOR BEFORE THE COMPONENT THAT CITES IT RUNS (none repaired silently):']
    L += ['  %s -- %s (Component %s)' % (what, how, comp) for _w, what, ok, how, comp in miss] or ['  NONE']
    L += ['', '### ### **CITES CHECKED %d ; OK %d ; MISSES %d.**' % (len(R), len(R) - len(miss), len(miss))]
    for name, data in (('b666_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b666_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)
    print(NL.join(L[-(len(miss) + 4):]))


def ferry(*a):
    text = ferry_text()
    q = os.path.join(D, 'b666_ferry.txt')
    open(q + '.tmp', 'wb').write((text + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    r = subprocess.run([sys.executable, os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b666_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b666_ferry.txt %d characters ; ferry_scan exit %d' % (len(text), r.returncode))


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b666_citation.py check | ferry')
        sys.exit(2)
    fn(*sys.argv[2:])
