# -*- coding: utf-8 -*-
"""b673_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b673's step zero; the ferry banked after
it; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT NAVIGATOR ANSWER before the seat acts on it. Carried from
tools/b672_citation.py by the Write tool: the helpers unchanged (both apostrophes, SESSIONS_AFTER, the after-root redirect of (R282)(2)
row 1: once data/act_roots.txt carries b673's root, an answer's print goes to data/b673_defects.txt and to no root-named bank); the
constants and the rows b673's.

### Before the ferry is banked, every path, line, bank, branch, tag, declaration and named rule the ruling (R283) and the ferry cite is
### checked for existence at HEAD and the misses printed; a miss is raised to the author before the component that cites it runs, not
### repaired silently; the print is banked as data/b673_citation_check.txt and read by the suite. A declaration the ruling orders written is
### printed TO BE WRITTEN, not a cite.
### The ruling and ferry are read from the session transcript (the user line carrying 'RULING (R283) BEGIN'), never from a scratch copy.
### Routes: `python tools/b673_citation.py check` -> data/b673_citation_check.txt (.json);
###         `python tools/b673_citation.py ferry`  -> data/b673_ferry.txt and data/b673_ferry_scan.txt (ferry_scan.py's output, captured);
###         `python tools/b673_citation.py answer <needle>` -> the latest session answer carrying <needle>, its cites checked, the print APPENDED
###         to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b673; this tool writes only the banks named above.
"""
import gzip
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
KE = 'D:/SIDE-explicit-formula'
BR = 'chi-li-b669'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/b895aca8-50cf-4976-9217-c566f780a886.jsonl'
SESSIONS_AFTER = ()
ANCHOR, TAIL = 'RULING (R283) BEGIN', 'FERRY END (part 1 of 1)'
REPOS = (ROOT, PP, KE)
MIRROR = 'D:/MY-DOwnloads/mirror-refresh-2026-10-16-b672.zip'
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


def _user_texts(results=True):
    """the session's user texts; with results, the results of the seat's own prompts alone (b670 defect (e))."""
    ask = set()
    for raw in (r for s in (SESSION,) + SESSIONS_AFTER for r in io.open(s, encoding='utf-8', errors='replace')):
        try:
            o = json.loads(raw)
        except ValueError:
            continue
        if o.get('isCompactSummary'):
            continue
        cs = (o.get('message') or {}).get('content')
        for c in (cs if isinstance(cs, list) else []):
            if isinstance(c, dict) and c.get('type') == 'tool_use' and c.get('name') == 'AskUserQuestion':
                ask.add(c.get('id'))
        if o.get('type') == 'user':
            for t in ([cs] if isinstance(cs, str) else [c.get('text', '') for c in (cs or []) if isinstance(c, dict) and c.get('type') == 'text']):
                yield t
            for c in (cs if isinstance(cs, list) else []) if results else []:
                if isinstance(c, dict) and c.get('type') == 'tool_result' and c.get('tool_use_id') in ask:
                    t = c.get('content')
                    yield ''.join(x.get('text', '') for x in t) if isinstance(t, list) else (t or '')


def ferry_text():
    """the ruling and the ferry as pasted: the last user line of the session carrying the anchor, from the anchor to the ferry's end."""
    best = None
    for t in _user_texts(results=False):
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


def grep_lines(path, pat, flags=0):
    t = rd(path) or ''
    return [(i, l.strip()) for i, l in enumerate(t.split(NL), 1) if re.search(pat, l, flags)]


def kshow(path):
    rc, o = g(KE, 'show', '%s:%s' % (BR, path))
    return o if rc == 0 else None


def kline(path, n):
    t = kshow(path)
    ls = t.split(NL) if t is not None else []
    return ls[n - 1] if 0 < n <= len(ls) else ''


def kgrep(pat):
    """the declaration's file and line on the branch, git grep bounded to *.lean (the house rule for a kernel search)."""
    rc, o = g(KE, 'grep', '-n', '-E', pat, BR, '--', '*.lean')
    hits = [l[len(BR) + 1:] for l in o.split(NL) if l.strip() and 'AxiomCheck' not in l]
    return hits


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
    # ### the ferry's read-first list
    for f in ('data/b672_closing.txt', 'data/b672_defects.txt', 'data/b669_chi_li_plan.txt', 'data/b669_chi_li_landing.txt',
              'data/b572_lemmas.txt', 'data/b572_crit_probe.lean.txt', 'data/b672_closing_push_out.txt', 'data/b671_narrow_plan.txt',
              'tools/act_root.py', 'tools/push_gated.sh', 'tools/ferry_scan.py'):
        add('ferry read-first; ruling', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-6')
    nz = 'data/b671_epstein_zeros_narrowed.json'
    add('ferry read-first; ruling (4)', nz, os.path.exists(p(*nz.split('/'))),
        'ABSENT at the working tree: b671 committed %s.gz (its .json is gzipped under its own name, data/b671_large_banks.txt); read through '
        'gzip -- RAISED' % nz if not os.path.exists(p(*nz.split('/'))) else 'exists', '0, 2')
    # ### (R283)(1): b672 at its weight
    cl = rd(p('data', 'b672_closing.txt')) or ''
    head = cl.split(NL)[0]
    add('ruling (1)', 'relay db2b75f4 (the closing), the record push read by hand as 92e07d46, PLACE-papers 8b85716',
        commit_in(ROOT, 'db2b75f4') and commit_in(ROOT, '92e07d46') and commit_in(PP, '8b85716')
        and g(ROOT, 'merge-base', '--is-ancestor', '92e07d46', 'db2b75f4')[0] == 0, 'git cat-file; merge-base; the closing`s head "%s"' % head[:110], '1')
    ar = act_root_line('b672')
    n_items = len([i for i in (json.loads(rd(p('data', 'b672_act_root.json')) or '{}').get('items') or []) if i.startswith('data/')])
    add('ruling (1)', 'root 41f49fc1... over 43 banks', ar and ar[0][1].startswith('41f49fc1') and n_items == 43,
        'data/act_roots.txt b672 %s ; data/b672_act_root.json`s data items %d' % (ar[0][1][:16] if ar else None, n_items), '1')
    dj = json.loads(rd(p('data', 'b672_correspondence_diff.json')) or '{}')
    c = dj.get('counts') or {}
    for k, v in (('CELLS CHANGED', 189), ('ABSENT', 7), ('NOT PRINTED', 48), ('NO PRINT BANK', 12), ('HELD: DEPOSIT PIN', 11), ('MULTI', 5)):
        add('ruling (1)', '%s %d' % (k, v), c.get(k) == v, 'data/b672_correspondence_diff.json counts %s = %s' % (k, c.get(k)), '1')
    add('ruling (1)', '14 files, 13 roster files and EXHAUSTIVENESS`s identical partner', len(dj.get('files') or []) == 14
        and any(x.get('written') and 'EXHAUSTIVENESS' in x.get('doc', '') for x in dj.get('pairs') or []),
        'files %d ; the pair written: %s' % (len(dj.get('files') or []), [x['doc'] for x in dj.get('pairs') or [] if x.get('written')]), '1')
    add('ruling (1)', 'eight grade tokens moved downward', len(dj.get('grade_down') or []) == 8, 'grade_down %d' % len(dj.get('grade_down') or []), '1')
    for pat, what in ((r'ROWS WITH A COMMIT 114 \(b670: 100\) ; AT THE TAG 52 \(b670: 3\) ; BEHIND 54 \(b670: 90\)', 'reading (ii) 54 behind against 90'),
                      (r'H1 HELD ; H2 HELD AT THE GENERATOR’S CLAIM; REFUTED BY b670’S METHOD ; H3 HELD ; H4 NOT HELD ; H5 HELD', 'H1-H5 as the ruling reads them'),
                      (r'LIVE PASSING : 87\. ### LIVE FAILING : 1 \[.G-READFIRST-CITED.\]', 'suite 87 of 88 with G-READFIRST-CITED'),
                      (r'AGREE 9 of 9', 'the sealed tools 9 of 9'), (r'Act root: b672 41f49fc1', 'the mirror`s root line')):
        h = grep_lines(p('data', 'b672_closing.txt'), pat)
        add('ruling (1)', what, h, 'data/b672_closing.txt :%s' % (h[0][0] if h else None), '1')
    at = rd(p('data', 'b672_correspondence_after.txt')) or ''
    add('ruling (1)', '0 at the leading clause; b670`s count 100 read as 110', 'AT THE LEADING CLAUSE (THE GENERATOR`S CLAIM) 0' in at
        and 'ROWS WITH A COMMIT 110 = b670`S 100' in at, 'data/b672_correspondence_after.txt', '1')
    dl = rd(p('data', 'b672_defects.txt')) or ''
    # ### defect (a): the first run read the owner after "THE " alone; (e) is b670's, "(e) b670'S:", and went unread
    letters = re.findall(r"^    \(([a-h])\) (?:THE )?([\w']+?)(?:'S)?:? ", dl, re.M)
    letters = [(x, ("NAVIGATOR'S" if o == 'NAVIGATOR' else o)) for x, o in letters]
    add('ruling (1)', 'eight defects (a)-(h), (c) and (g) the navigator`s', [x[0] for x in letters] == list('abcdefgh')
        and [x[0] for x in letters if x[1] == "NAVIGATOR'S"] == ['c', 'g'], 'data/b672_defects.txt: the navigator`s %s' % [x[0] for x in letters if x[1] == "NAVIGATOR'S"], '1')
    add('ruling (1)', 'the record push`s read-back read by hand as 92e07d46 (defect (h))', '(h) THE HOST' in dl and '92e07d463207c46aa54f30b1155c6f1afcfcdf79' in dl,
        'data/b672_defects.txt (h)', '1')
    add('ruling (1)', 'the mirror mirror-refresh-2026-10-16-b672.zip CLEAN with the root line', os.path.exists(MIRROR)
        and 'CLEAN ON ALL THREE CLAUSES' in (rd(p('data', 'b672_mirror_verify.txt')) or ''), MIRROR, '1')
    v113 = rd(os.path.join(PP, 'phase1.5', 'simplicity', 'SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md')) or ''
    add('ruling (1)', 'the b651 line on SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md', 'b651\'S LINE, CARRIED TO THE COPY OF RECORD' in v113, 'the v1.1.3 copy', '1')
    for n, needle in ((8791, '## The Correspondence generator'),):
        l = line(FIND, n) or ''
        add('ruling (1)', 'FINDINGS :%d' % n, needle in l, l[:90], '1')
    for n, needle in ((14436, 'THREE RULES'), (14438, 'THE LEDGER SPLIT'), (14440, 'THE KERNELS WITH NO RELAY PRINT BANK'),
                      (14442, '`W-ORD-TABLE-SHAPE`'), (14444, '`W-ORD-GRADE-MOVED`'), (14446, '`W-ORD-PRINT-TARGETS`'),
                      (14448, '`W-ORD-ABSENT-DECLARATIONS`'), (14450, '`W-ORD-ONE-COPY`'), (14454, '### b672'), (14334, 'W-ORD-LI-CONVERSE-NATIVE')):
        l = line(OT, n) or ''
        add('ruling (1), (6); ferry', 'OPEN_TRAILS :%d' % n, needle in l, l[:110], '1-6')
    l52 = line(OT, 14452) or ''
    add('ruling (1)', 'W-ORD-PROSE-PINS "entered at OPEN_TRAILS :14440-:14450" with the four orders', False,
        'the order stands at :14452 (%s), past the range the ruling names; :14440 is the no-print-bank list, :14450 W-ORD-ONE-COPY -- RAISED' % l52[:50], '1')
    # ### (R283)(2)-(3): the object on the branch
    add('ruling (2)', '%s at b804bf2' % BR, g(KE, 'rev-parse', '--short=7', BR)[1].strip() == 'b804bf2', 'git rev-parse', '0-3')
    lc = 'SIDEExplicitFormula/Schema/LiConverseCfg.lean'
    for n, needle, what in ((129, 'sorry', 'V4 at :129 (the sorry of powerSum_re_le_neg_infinitely, :125)'),
                            (139, 'sorry', 'V5 at :139 (the sorry of remainder_le, :135)'),
                            (145, 'theorem li_nonneg_cfg_imp_online', 'S5 at :145'), (159, 'theorem li_nonneg_chi_imp_grh_chi', 'S6 at :159')):
        add('ruling (2)', what, needle in kline(lc, n), '%s :%d "%s"' % (lc, n, kline(lc, n).strip()[:60]), '2-3')
    lj = rd(p('data', 'b669_chi_li_landing.txt')) or ''
    for nm in ('exists_dominant_point', 'dominant_finite', 'norm_geom_sum_le', 'norm_sum_powerSum_le'):
        add('ruling (2)', '%s DERIVES on the branch (V2, V3, V4`s two geometric-sum steps)' % nm,
            re.search(r'Schema\.%s\s+DERIVES' % nm, lj), 'data/b669_chi_li_landing.txt', '2')
    v4doc = kline(lc, 121)
    add('ruling (3)', 'V4 as the branch states it: the NEGATIVE sign alone, c = Σ m_i² / (8 Σ m_i) (the ruling states both signs, c = Σ m_k² / (4 Σ m_k))',
        '8 Σ m_i' in v4doc or '8 * ∑' in kline(lc, 128), '%s :121, :127-:128 -- the plan prints the sign S5 consumes (Component 2)' % lc, '2')
    for pat, what in (('^def pairTerm', 'pairTerm'), ('^def liTerm', 'liTerm'), ('^def liCoeffCfg', 'liCoeffCfg'),
                      ('^def HCount', 'HCount (RestBound.lean)'), ('^def HStrip', 'HStrip (RestBound.lean)'),
                      ('count : ∃ A₀', 'Config.lean`s count field (HCount as dominant_summable consumes it)'),
                      ('^structure ZeroConfig', 'ZeroConfig'), ('^theorem rh_equiv_mathlib', 'rh_equiv_mathlib'),
                      ('^theorem positivity_implies_RH', 'the vendored positivity_implies_RH'), ('zetaZeroConfig', 'zetaZeroConfig'),
                      ('^theorem chiZeroConfig_local_count|theorem chiZeroConfig_local_count', 'chiZeroConfig_local_count'),
                      ('^theorem grh_chi_imp_li_nonneg_chi', 'the forward half at χ (S7`s other direction)'),
                      ('^theorem li_nonneg_iff_rh', 'the vendored-route equivalence li_nonneg_iff_rh'), ('Summable', 'LiWeil`s summability lemmas')):
        h = kgrep(pat)
        if 'Summable' in pat:
            h = [x for x in h if x.startswith('SIDEExplicitFormula/LiWeil.lean')]
        add('ruling (3), (5); ferry', what, h, (h[0][:110] if h else 'NOT FOUND on %s' % BR), '2-3')
    add('ferry read-first', 'PageConverses.lean', kshow('SIDEExplicitFormula/PageConverses.lean') is not None, 'SIDEExplicitFormula/PageConverses.lean', '2')
    add('ferry read-first', 'Config.lean`s HStrip', 'HStrip' in (kshow('SIDEExplicitFormula/Schema/Config.lean') or ''),
        'HStrip in Config.lean: %s -- defined at RestBound.lean :40; the ferry`s "Config.lean`s HCount and HStrip" read as RestBound.lean`s, '
        'Config.lean carrying the count field -- RAISED' % ('HStrip' in (kshow('SIDEExplicitFormula/Schema/Config.lean') or '')), '2')
    rc, man = g(KE, 'show', '%s:lake-manifest.json' % BR)
    add('ruling (3)', 'Mathlib at de5ce8a9', 'de5ce8a9a66a4aa68a9bdbb35b63a06d34d9ca11' in man, 'lake-manifest.json at %s' % BR, '2-3')
    add('ruling (5)', 'print_targets.txt on the branch', kshow('print_targets.txt') is not None, 'print_targets.txt at %s' % BR, '3')
    for nm in ('li_nonneg_chi_iff_grh_chi', 'li_nonneg_imp_rh_native'):
        add('ruling (5)', '%s -- TO BE WRITTEN, not a cite' % nm, not kgrep(r'theorem %s\b' % nm), 'absent on %s, as the ruling orders it written' % BR, '3')
    rc, tg = g(KE, 'tag', '--list', 'v0.32')
    add('ruling (5)', 'tag v0.32 -- TO BE MADE, not a cite', tg.strip() == '', 'absent locally', '4')
    pl = grep_lines(p('data', 'b669_chi_li_plan.txt'), r'W-ORD-LI-CONVERSE-NATIVE, its trigger "S5 DERIVES"')
    add('ruling (6)', 'W-ORD-LI-CONVERSE-NATIVE (named in b669`s plan, its trigger "S5 DERIVES")', pl,
        'data/b669_chi_li_plan.txt :%s ; OPEN_TRAILS :14334 names it; no entry of its own on OPEN_TRAILS' % (pl[0][0] if pl else None), '4')
    add('ruling (6)', 'the ceiling sentence ((R183)(3)) at README :125 and REGISTRY :960', '`(R183)`(3)' in (line(os.path.join(PP, 'README.md'), 125) or '')
        and '`(R183)`(3)' in (line(os.path.join(PP, 'REGISTRY.md'), 960) or ''), 'README.md :125 ; REGISTRY.md :960', '4')
    fp = os.path.join(PP, 'THE_CLAUSE_AND_ITS_COMPILED_FACES.md')
    add('ruling (6)', '"the faces page`s line on unequal converses"', False,
        'no file carries the name; read as THE_CLAUSE_AND_ITS_COMPILED_FACES.md (the ζ page; its PageConverses lines :137-:138), present %s; the '
        'line is drafted, written to no keystone -- RAISED' % os.path.exists(fp), '4')
    # ### (R283)(4): the control's input
    try:
        nj = json.loads(gzip.decompress(open(p('data', 'b671_epstein_zeros_narrowed.json.gz'), 'rb').read()).decode('utf-8'))
        rows_ = nj.get('rows') or []
    except Exception:
        rows_ = []
    off = [r for r in rows_ if r.get('kind') == 'OFF']
    add('ruling (4)', 'b671`s narrowed balls: the off-line points with multiplicity (count) one', off and all(r.get('count') == 1 for r in off),
        'data/b671_epstein_zeros_narrowed.json.gz: rows %d, OFF %d' % (len(rows_), len(off)), '2')
    # ### (R283)(9)
    for k in ('SIDE-window', 'SIDE-trivium'):
        add('ruling (9)', k, os.path.isdir('D:/' + k), 'D:/%s' % k, '6')
    # ### step zero's branches
    for repo, nm, b in ((ROOT, 'relay', 'push-b672'), (ROOT, 'relay', 'push-b672-root'), (ROOT, 'relay', 'push-b672-closing'),
                        (PP, 'PLACE-papers', 'push-b672'), (PP, 'PLACE-papers', 'push-b672-root'), (KE, 'SIDE-explicit-formula', BR)):
        add('ferry Component 0', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    for rule, cl_, comp in (('R278', (4,), '0-6'), ('R251', (3,), '6'), ('R254', (2,), '0-6'), ('R279', (4,), '3')):
        ok, how = rule_clause(rule, cl_)
        add('ruling; ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ruling (8)', 'the draft at v5, held', '23228113' in (rd(p('tools', 'b672_worklist.py')) or ''), 'tools/b672_worklist.py DRAFT', '6')
    return R


def _write(L, R, miss):
    for name, data in (('b673_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b673_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b673 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662), RUN BEFORE THE FERRY IS BANKED (%s)' % time.strftime(
        '%Y-%m-%dT%H:%M:%SZ', time.gmtime()), '',
         '### the source: the ruling and the ferry as pasted, read from the session transcript (%d characters, %r to %r); every cite checked at '
         'HEAD; rows are cites: where | what | OK or MISS | how | the component that cites it.' % (len(text), ANCHOR, TAIL), '']
    for where, what, ok, how, comp in R:
        L.append('  %-4s | %s | %s | %s | Component %s' % ('OK' if ok else 'MISS', where, what, how, comp))
    L += ['', '### THE MISSES, EACH RAISED TO THE AUTHOR BEFORE THE COMPONENT THAT CITES IT RUNS (none repaired silently):']
    L += ['  %s -- %s (Component %s)' % (what, how, comp) for _w, what, ok, how, comp in miss] or ['  NONE']
    L += ['', '### ### **CITES CHECKED %d ; OK %d ; MISSES %d.**' % (len(R), len(R) - len(miss), len(miss))]
    _write(L, R, miss)
    print(NL.join(L[-(len(miss) + 4):]))


def ferry(*a):
    text = ferry_text()
    q = os.path.join(D, 'b673_ferry.txt')
    open(q + '.tmp', 'wb').write((text + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b673_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b673_ferry.txt %d characters ; ferry_scan exit %d' % (len(text), r.returncode))


def after_root():
    """(R282)(2) row 1: the exclusion list read before the write -- True once data/act_roots.txt carries b673's root."""
    return bool(act_root_line('b673'))


def answer(needle, *a):
    """(R278)(4): the latest session text carrying `needle` (a navigator answer or note) -- its relay paths, ledger lines and commits checked
    at HEAD, the print appended to the citation bank, or after the root to the defects bank, with the answer named."""
    best = None
    for t in _user_texts():
        u = t.replace('’', "'")
        if needle in t and ("NAVIGATOR'S ANSWER" in u or "NAVIGATOR'S NOTE" in u or "AUTHOR'S" in u):
            best = t
    if best is None:
        sys.exit('### NO ANSWER CARRYING %r IN THE SESSION -- NOTHING WRITTEN' % needle)
    rows_ = []
    for pth in sorted(set(re.findall(r'\b((?:data|tools)/[\w./-]+\.[a-z]{2,4})\b', best))):
        ex = os.path.exists(os.path.join(ROOT, *pth.split('/')))
        if not ex and re.match(r'^(data|tools)/b673_', pth):
            rows_.append(('path, this act`s bank or tool the answer orders written -- TO BE WRITTEN, not a cite', pth, True))
        elif not ex and 'bNNN' in pth:
            rows_.append(('path, a placeholder of a form for later acts -- not a cite', pth, True))
        else:
            rows_.append(('path', pth, ex))
    for m in re.finditer(r'\b(FINDINGS|OPEN_TRAILS)\b((?:[^:\n]{0,20}:\d{3,5})+(?:(?:,|;| and|,? or)\s*:\d{3,5})*)', best):
        for n in sorted(set(re.findall(r':(\d{3,5})', m.group(2)))):
            rows_.append(('line', '%s :%s' % (m.group(1), n), line(os.path.join(PP, m.group(1) + '.md'), int(n)) is not None))
    for h in sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', best))):
        if re.search(r'[a-f]', h) and re.search(r'\d', h):
            rows_.append(('commit', h, any(commit_in(r_, h) for r_ in REPOS)))
    miss = [r for r in rows_ if not r[2]]
    q = os.path.join(D, 'b673_defects.txt' if after_root() else 'b673_citation_check.txt')
    old = (rd(q) or '').rstrip(NL)
    L = ['', '### (R278)(4) THE MID-ACT CHECK (%s): the navigator`s answer carrying %r, %d characters; its cites checked at HEAD before the seat '
         'acts on it%s:' % (time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), needle, len(best),
                            ' (after the root: printed to the defects bank, (R282)(2) row 1)' if after_root() else '')]
    L += ['  %-4s | %s | %s' % ('OK' if ok else 'MISS', k, w) for k, w, ok in rows_] or ['  (no path, ledger line or commit named)']
    L += ['### ### **ANSWER CITES CHECKED %d ; OK %d ; MISSES %d%s.**%s' % (len(rows_), len(rows_) - len(miss), len(miss),
                                                                         (' -- RAISED: ' + ', '.join(w for _k, w, _o in miss)) if miss else '',
                                                                         ' -- VACUOUS: no cite to check.' if not rows_ else '')]
    open(q + '.tmp', 'wb').write((old + NL + NL.join(L) + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    print(NL.join(L))


if __name__ == '__main__':
    fn = {'check': check, 'ferry': ferry, 'answer': answer}.get(sys.argv[1] if len(sys.argv) > 1 else '')
    if fn is None:
        print('usage: b673_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
