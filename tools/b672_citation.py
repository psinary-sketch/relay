# -*- coding: utf-8 -*-
"""b672_citation.py -- THE CITATION CHECK AS A GATE STEP (standing from b662, OPEN_TRAILS :14136), b672's step zero; the ferry banked after
it; and, from (R278)(4) (OPEN_TRAILS :14292), THE CHECK ON EACH MID-ACT NAVIGATOR ANSWER before the seat acts on it. Carried from
tools/b671_citation.py by the Write tool: the helpers unchanged (b671's repaired readers: both apostrophes, SESSIONS_AFTER), the constants
and the rows b672's; and, under (R282)(2) row 1, the answer route reads the root's exclusion list before it writes: once the act root is
appended to data/act_roots.txt for b672, its print goes to the defects bank (data/b672_defects.txt, which the root excludes) and to no
root-named bank.

### Before the ferry is banked, every path, line, bank, branch, tag, tool and named rule the ruling (R282) and the ferry cite is checked for
### existence at HEAD and the misses printed; a miss is raised to the author before the component that cites it runs, not repaired silently;
### the print is banked as data/b672_citation_check.txt and read by the suite.
### The ruling and ferry are read from the session transcript (the user line carrying 'RULING (R282) BEGIN'), never from a scratch copy.
### Routes: `python tools/b672_citation.py check` -> data/b672_citation_check.txt (.json);
###         `python tools/b672_citation.py ferry`  -> data/b672_ferry.txt and data/b672_ferry_scan.txt (ferry_scan.py's output, captured);
###         `python tools/b672_citation.py answer <needle>` -> the latest session answer carrying <needle>, its cites checked, the print APPENDED
###         to the citation bank before the root and to the defects bank after it.
### Written by the Write tool at b672; this tool writes only the banks named above.
"""
import io
import json
import os
import re
import subprocess
import sys
import time
import zipfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D, T = os.path.join(ROOT, 'data'), os.path.join(ROOT, 'tools')
NL = chr(10)
PP = 'D:/MY-DOwnloads/PLACE-papers'
KE = 'D:/SIDE-explicit-formula'
SESSION = 'C:/Users/echo chamber/.claude/projects/D--/b895aca8-50cf-4976-9217-c566f780a886.jsonl'
# ### the act's continuation sessions (tools/b672_worklist.py SESSIONS_AFTER), read after the first, so "the latest" stays the latest
SESSIONS_AFTER = ()
ANCHOR, TAIL = 'RULING (R282) BEGIN', 'FERRY END (part 1 of 1)'
REPOS = (ROOT, PP, KE)
MIRROR = 'D:/MY-DOwnloads/mirror-refresh-2026-10-14-b670.zip'    # ### the last mirror export (b670's); b671 made none
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


def one_copy_pairs():
    """OPEN_TRAILS :14386 item (b): (unversioned path, [versioned basenames]) as b671 entered them."""
    t = line(os.path.join(PP, 'OPEN_TRAILS.md'), 14386) or ''
    b = t[t.find('(b)'):t.find('**`W-ORD-ONE-COPY`**')]
    return [(m.group(1), [x.strip() for x in m.group(2).split(',')]) for m in re.finditer(r'([\w./-]+\.md) \(([^)]+)\)', b)]


def rows():
    """(where, what, ok, how, component)."""
    R = []
    add = lambda where, what, ok, how, comp: R.append((where, what, bool(ok), how, comp))   # noqa: E731
    p = lambda *a: os.path.join(ROOT, *a)   # noqa: E731
    FIND, OT = os.path.join(PP, 'FINDINGS.md'), os.path.join(PP, 'OPEN_TRAILS.md')
    for f in ('data/b671_closing.txt', 'data/b671_defects.txt', 'data/b586_corroboration.txt', 'data/b670_correspondence.txt',
              'data/b670_correspondence.json', 'data/b670_state.txt', 'data/b671_closing_push_out.txt', 'data/b671_reap_reading.txt',
              'data/b670_methods.txt', 'data/b670_rules.txt', 'tools/b670_record.py', 'tools/mirror_roster.json', 'tools/terminal_table.py',
              'tools/e0_rule.py', 'tools/ferry_scan.py', 'tools/act_root.py', 'tools/push_gated.sh'):
        add('ferry read-first; ruling', f, os.path.exists(p(*f.split('/'))), 'exists at the working tree', '0-5')
    cl = rd(p('data', 'b671_closing.txt')) or ''
    head = cl.split(NL)[0]
    # ### (R282)(1): b671 at its weight
    add('ruling (1)', 'relay 64158393 (the closing) after 4e3a46d6 (the record), PLACE-papers d6d2d4b', commit_in(ROOT, '64158393')
        and commit_in(ROOT, '4e3a46d6') and commit_in(PP, 'd6d2d4b') and g(ROOT, 'merge-base', '--is-ancestor', '4e3a46d6', '64158393')[0] == 0,
        'git cat-file; merge-base --is-ancestor; the closing`s head "%s"' % head[:110], '1')
    ar = act_root_line('b671')
    n_items = len([i for i in (json.loads(rd(p('data', 'b671_act_root.json')) or '{}').get('items') or []) if i.startswith('data/')])
    add('ruling (1)', 'root 9e045502... over 60 banks', ar and ar[0][1].startswith('9e045502') and n_items == 60,
        'data/act_roots.txt b671 %s ; data/b671_act_root.json`s data items %d' % (ar[0][1][:16] if ar else None, n_items), '1')
    for pat, what in ((r'POINTS 163 ; ON NARROWED 146 OF 146.*OFF NARROWED 17 OF 17 ; UNRESOLVED 0 ; HALF-WIDTH 1e-24', '163 points, 146 on, 17 off, none unresolved, 10^-24'),
                      (r'hQtie 18 of 41', 'hQtie 18 of 41'), (r'H1 HELD ; H2 HELD ; H3 REFUTED ; H4 HELD', 'H3 REFUTED, H1 H2 H4 HELD'),
                      (r'INSTRUMENT 23, OBJECT 0', 'every failed control INSTRUMENT, none OBJECT'),
                      (r'run 2 RUN 2 : DONE ; HOST LOW 1522 MB', 'run 2`s host low 1,522 MB'),
                      (r'LIVE PASSING : 85\. ### LIVE FAILING : 1 \[.G-ACTROOT-LAST.\]', 'suite 85 of 86 pre-push, G-ACTROOT-LAST'),
                      (r'LIVE PASSING : 84\. ### LIVE FAILING : 2', 'suite 84 of 86 post-push'),
                      (r'run again alone .* LIVE PASSING 85', 'the post-push rerun 85 of 86'),
                      (r'b671 closed: .*suite 84 of 86', 'the closing`s head line carrying the run`s figure (84 of 86)'),
                      (r'AGREE 9 of 9', 'the sealed tools 9 of 9'), (r'18 defects', 'eighteen defects')):
        h = grep_lines(p('data', 'b671_closing.txt'), pat)
        add('ruling (1)', what, h, 'data/b671_closing.txt :%s' % (h[0][0] if h else None), '1')
    rr = grep_lines(p('data', 'b671_reap_reading.txt'), r'free 2016 ; the hold 2560')
    add('ruling (1)', 'the second breach, 2,016 MB free against 2,560', rr, 'data/b671_reap_reading.txt :%s' % (rr[0][0] if rr else None), '1')
    dl = rd(p('data', 'b671_defects.txt')) or ''
    letters = re.findall(r"^    \(([a-r])\) THE ([\w']+)", dl, re.M)
    add('ruling (1)', 'eighteen defects (a)-(r), the navigator`s by letter', len(letters) == 18 and [x[0] for x in letters] == list('abcdefghijklmnopqr'),
        'data/b671_defects.txt: the navigator`s %s' % ', '.join('(%s)' % x[0] for x in letters if x[1] == "NAVIGATOR'S"), '1')
    mt = grep_lines(p('data', 'b670_methods.txt'), r'AT b671: METHODS 12 ; READY 11')
    add('ruling (1)', 'the methods table at 11 READY of 12', mt, 'data/b670_methods.txt :%s' % (mt[0][0] if mt else None), '1')
    for n, needle in ((8761, '## Q0’s 163 points narrowed'),):
        l = line(FIND, n) or ''
        add('ruling (1)', 'FINDINGS :%d' % n, needle in l, l[:90], '1')
    for n, needle in ((14396, 'beneath `W-ORD-EPSTEIN-BALL-WIDTH`'), (14398, '### `W-ORD-MAP-ANGLE-FORM`'), (14406, 'THE KERNEL ITEM RE-DATED'),
                      (14384, 'THE SEQUENCE LINE'), (14412, '### b671'), (14386, '`W-ORD-ONE-COPY`'), (14264, 'W-ORD-EPSTEIN-BALL-WIDTH')):
        l = line(OT, n) or ''
        add('ruling (1), (5); ferry', 'OPEN_TRAILS :%d' % n, needle in l, l[:110], '1-5')
    l96 = line(OT, 14396) or ''
    add('ruling (1)', 'the two width figures beneath W-ORD-EPSTEIN-BALL-WIDTH (about 10^-31; 1.5·10^-40)', '10⁻³¹' in l96 and '1.5·10⁻⁴⁰' in l96, 'OPEN_TRAILS :14396', '1')
    l04 = (line(OT, 14404) or '')
    add('ruling (1)', 'W-ORD-MAP-ANGLE-FORM`s trigger "before the next narrowing act"', 'before the next narrowing act' in l04, 'OPEN_TRAILS :14404: %s' % l04[:60], '1')
    add('ruling (1)', 'the Bessel bar 2^-200', '2⁻²⁰⁰' in (line(OT, 14408) or ''), 'OPEN_TRAILS :14408', '1')
    add('ruling (1), (9)', 'chi-li-b669 at b804bf2', g(KE, 'rev-parse', '--short=7', 'chi-li-b669')[1].strip() == 'b804bf2', 'git rev-parse chi-li-b669', '0, 9')
    # ### (R282)(2): the rules
    rl = grep_lines(p('data', 'b671_defects.txt'), r'exclusion list before it writes')
    add('ruling (2) row 1', 'b671`s defect (r) rules line, verbatim, beneath (r)', rl, 'data/b671_defects.txt :%s' % ', :'.join(str(x[0]) for x in rl), '0')
    # ### (R282)(3): the object
    rb = rd(p('data', 'b586_corroboration.txt')) or ''
    docs = re.findall(r'^\| (\S+) \| (\S+\.md) \| (PRESENT|a table of another name|ABSENT)', rb, re.M)
    tab = [d for d in docs if d[2] != 'ABSENT']
    add('ruling (3)', 'the 19 tables of data/b586_corroboration.txt', len(tab) == 19, 'rows %d, with a table %d' % (len(docs), len(tab)), '2')
    ed = grep_lines(os.path.join(PP, 'phase2', 'method', 'E_DIFFICULTY_THEOREM_v1_0_4.md'), r'^### Correspondence')
    add('ruling (3)', 'E_DIFFICULTY_THEOREM`s table', ed, 'phase2/method/E_DIFFICULTY_THEOREM_v1_0_4.md :%s (b586 read v1.0.3 ABSENT; b589 wrote the table in v1.0.4)' % (
        ed[0][0] if ed else None), '2')
    ci = grep_lines(p('data', 'b670_correspondence.txt'), r'TABLES 19 ; RE-FOUND AT HEAD 19 ; ROWS WITH A COMMIT 100 ; AT THE TAG 3 ; BEHIND 90')
    add('ruling (3), (6) H1-H2', '100 rows with a commit, 90 behind, 3 at the tag (b670 reading (ii))', ci, 'data/b670_correspondence.txt :%s' % (ci[0][0] if ci else None), '2-3')
    st = rd(p('data', 'b670_state.txt')) or ''
    add('ruling (6) H5', 'b670`s state line for (ii)', '(ii)  90 rows to zero' in st, 'data/b670_state.txt', '3')
    rl5 = rd(p('data', 'b670_rules.txt')) or ''
    add('ruling (3); b670 rules row 5', 'the roster reader withholds TECHNE_TOOLKIT text', 'ROW 5 --' in rl5 and 'TECHNE_TOOLKIT' in rl5, 'data/b670_rules.txt ROW 5', '2-3')
    # ### the kernels named by b670's reading, with a relay print bank or none
    rj = json.loads(rd(p('data', 'b670_correspondence.json')) or '{}')
    # ### defect (a): the first run read a `kernels` key the json does not carry; its kernels are the keys of `tags`
    kn = sorted((rj.get('tags') or {}).keys()) if isinstance(rj.get('tags'), dict) else []
    add('ruling (4)', 'the kernels b670`s reading names (its json`s tags)', kn, ', '.join(kn) or 'NO tags KEY', '2')
    # ### (R282)(5): the one copy of record
    pairs = one_copy_pairs()
    miss = []
    for base, vs in pairs:
        if not os.path.exists(os.path.join(PP, *base.split('/'))):
            miss.append(base)
        for v in vs:
            if not os.path.exists(os.path.join(PP, os.path.dirname(base), v)):
                miss.append(v)
    add('ruling (5)', 'b671`s census item (b): the unversioned and versioned pairs, 25 by name', len(pairs) == 25 and not miss,
        'OPEN_TRAILS :14386 pairs %d ; files absent at the working tree %s' % (len(pairs), miss or 'NONE'), '2-3')
    sm = grep_lines(os.path.join(PP, 'phase1.5', 'simplicity', 'SIMPLICITY_OF_RIEMANN_ZEROS.md'), r'\(R261\)`\(3\)\(d\)')
    sv = grep_lines(os.path.join(PP, 'phase1.5', 'simplicity', 'SIMPLICITY_OF_RIEMANN_ZEROS_v1_1_3.md'), r'\(R261\)`\(3\)\(d\)')
    add('ruling (5)', 'SIMPLICITY_OF_RIEMANN_ZEROS.md`s b651 ceiling line, absent from v1_1_3', sm and not sv,
        'the base copy :%s ; the versioned copy none' % (sm[0][0] if sm else None), '3')
    add('ruling (5)', 'PLACE-papers/archive/superseded/ (to be made by the moves)', os.path.isdir(os.path.join(PP, 'archive')),
        'archive/ exists; archive/superseded/ %s -- TO BE MADE, not a cite' % ('EXISTS' if os.path.isdir(os.path.join(PP, 'archive', 'superseded')) else 'absent'), '3')
    try:
        man = zipfile.ZipFile(MIRROR).read('MANIFEST.md').decode('utf-8-sig')
    except Exception:
        man = ''
    add('ferry read-first', 'the mirror`s MANIFEST.md', man, '%s MANIFEST.md %d characters' % (MIRROR, len(man)), '2')
    # ### (R282)(7): the ledger split form
    add('ruling (7)', 'the 2026-08-24 ledger split (archive-1, archive-2)', os.path.isdir(os.path.join(PP, 'archive', '2026-08-24-ledger-split')),
        'PLACE-papers archive/2026-08-24-ledger-split: %s' % ', '.join(sorted(os.listdir(os.path.join(PP, 'archive', '2026-08-24-ledger-split')))
                                                                    if os.path.isdir(os.path.join(PP, 'archive', '2026-08-24-ledger-split')) else ''), '1')
    ot_b = os.path.getsize(OT)
    add('ruling (7)', 'OPEN_TRAILS at about 2 MB', 1.8e6 < ot_b < 2.2e6, 'OPEN_TRAILS.md %d bytes' % ot_b, '1')
    # ### (R282)(10)
    for k in ('SIDE-window', 'SIDE-trivium'):
        add('ruling (10)', k, os.path.isdir('D:/' + k), 'D:/%s' % k, '5')
    # ### branches for step zero
    for repo, nm, b in ((ROOT, 'relay', 'push-b671'), (ROOT, 'relay', 'push-b671-root'), (ROOT, 'relay', 'push-b671-closing'),
                        (PP, 'PLACE-papers', 'push-b671'), (PP, 'PLACE-papers', 'push-b671-root'), (KE, 'SIDE-explicit-formula', 'chi-li-b669')):
        add('ferry Component 0', '%s %s' % (nm, b), branch_listed(repo, b), 'git branch --list', '0')
    for rule, cl_, comp in (('R278', (4,), '0-5'), ('R251', (3,), '5'), ('R254', (2,), '0-5')):
        ok, how = rule_clause(rule, cl_)
        add('ruling; ferry', '(%s)(%s)' % (rule, ', '.join(str(c) for c in cl_)), ok, how, comp)
    add('ruling (9)', 'the draft at v5, held', '23228113' in cl and 'v5' in cl, 'data/b671_closing.txt (N5)', '5')
    return R


def _write(L, R, miss):
    for name, data in (('b672_citation_check.txt', (NL.join(L) + NL).encode('utf-8')),
                       ('b672_citation_check.json', (json.dumps(dict(at=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=R,
                                                                       misses=[r[1] for r in miss]), indent=1, ensure_ascii=False) + NL).encode('utf-8'))):
        q = os.path.join(D, name)
        open(q + '.tmp', 'wb').write(data)
        os.replace(q + '.tmp', q)


def check(*a):
    text = ferry_text()
    R = rows()
    miss = [r for r in R if not r[2]]
    L = ['b672 -- THE CITATION CHECK, A GATE STEP AT STEP ZERO (standing from b662), RUN BEFORE THE FERRY IS BANKED (%s)' % time.strftime(
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
    q = os.path.join(D, 'b672_ferry.txt')
    open(q + '.tmp', 'wb').write((text + NL).encode('utf-8'))
    os.replace(q + '.tmp', q)
    r = subprocess.run([sys.executable, '-X', 'utf8', os.path.join(T, 'ferry_scan.py'), q], capture_output=True, cwd=ROOT)
    s = os.path.join(D, 'b672_ferry_scan.txt')
    open(s + '.tmp', 'wb').write((r.stdout + r.stderr).replace(b'\r\n', b'\n'))
    os.replace(s + '.tmp', s)
    print('  b672_ferry.txt %d characters ; ferry_scan exit %d' % (len(text), r.returncode))


def after_root():
    """(R282)(2) row 1: the exclusion list read before the write -- True once data/act_roots.txt carries b672's root."""
    return bool(act_root_line('b672'))


def answer(needle, *a):
    """(R278)(4): the latest session text carrying `needle` (a navigator answer or note) -- its relay paths, ledger lines and commits checked
    at HEAD, the print appended to the citation bank, or after the root to the defects bank, with the answer named."""
    best = None
    for t in _user_texts():
        u = t.replace('’', "'")     # ### b671 defect (g): an answer pasted with the curly apostrophe read as the straight
        if needle in t and ("NAVIGATOR'S ANSWER" in u or "NAVIGATOR'S NOTE" in u or "AUTHOR'S" in u):
            best = t
    if best is None:
        sys.exit('### NO ANSWER CARRYING %r IN THE SESSION -- NOTHING WRITTEN' % needle)
    rows_ = []
    for pth in sorted(set(re.findall(r'\b((?:data|tools)/[\w./-]+\.[a-z]{2,4})\b', best))):
        ex = os.path.exists(os.path.join(ROOT, *pth.split('/')))
        if not ex and re.match(r'^(data|tools)/(b672_|correspondence_gen|test_correspondence_gen)', pth):
            rows_.append(('path, this act`s bank or tool the answer orders written -- TO BE WRITTEN, not a cite', pth, True))
        else:
            rows_.append(('path', pth, ex))
    for m in re.finditer(r'\b(FINDINGS|OPEN_TRAILS)\b((?:[^:\n]{0,20}:\d{3,5})+(?:(?:,|;| and|,? or)\s*:\d{3,5})*)', best):
        for n in sorted(set(re.findall(r':(\d{3,5})', m.group(2)))):
            rows_.append(('line', '%s :%s' % (m.group(1), n), line(os.path.join(PP, m.group(1) + '.md'), int(n)) is not None))
    for h in sorted(set(re.findall(r'\b([0-9a-f]{7,12})\b', best))):
        if re.search(r'[a-f]', h) and re.search(r'\d', h):
            rows_.append(('commit', h, any(commit_in(r_, h) for r_ in REPOS)))
    miss = [r for r in rows_ if not r[2]]
    q = os.path.join(D, 'b672_defects.txt' if after_root() else 'b672_citation_check.txt')
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
        print('usage: b672_citation.py check | ferry | answer <needle>')
        sys.exit(2)
    fn(*sys.argv[2:])
